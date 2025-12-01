#!/usr/bin/env python3
"""
rat_grid.py

A simple Python application that simulates a remote-controlled "rat" on a 20x20 grid.
Features:
 - Tkinter GUI visualization
 - Keyboard control (arrow keys, WASD)
 - TCP text command server (port 9999 by default) for remote control
 - A* pathfinding for GOTO x y
 - Obstacles, battery, status display

Run:
    python rat_grid.py

Remote usage example (from another terminal on same machine):
    $ nc localhost 9999
    GOTO 5 10
    STATUS

Author: ChatGPT (example educational code)
"""

import threading
import socket
import queue
import tkinter as tk
from tkinter import messagebox
import time
import random
import heapq

# Configuration
GRID_SIZE = 20
CELL_PIXEL = 30
WINDOW_PADDING = 10
CANVAS_SIZE = GRID_SIZE * CELL_PIXEL
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 9999
TICK_INTERVAL_MS = 150  # movement tick when following path
OBSTACLE_DENSITY = 0.12  # fraction of cells initially obstacles

# Utility: A* pathfinding
def astar(start, goal, blocked, grid_size):
    """Return path as list of (x,y) from start (exclusive) to goal (inclusive).
    Uses Manhattan distance heuristic on 4-neighbor grid. Returns [] if no path.
    """
    sx, sy = start
    gx, gy = goal
    if start == goal:
        return []

    def neighbors(node):
        x, y = node
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x+dx, y+dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size and (nx,ny) not in blocked:
                yield (nx, ny)

    def heuristic(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    open_heap = []
    heapq.heappush(open_heap, (heuristic(start, goal), 0, start))
    came_from = {}
    gscore = {start: 0}
    closed = set()

    while open_heap:
        _, cost, current = heapq.heappop(open_heap)
        if current == goal:
            # reconstruct path
            path = []
            while current != start:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        if current in closed:
            continue
        closed.add(current)
        for n in neighbors(current):
            tentative = gscore[current] + 1
            if tentative < gscore.get(n, 10**9):
                came_from[n] = current
                gscore[n] = tentative
                heapq.heappush(open_heap, (tentative + heuristic(n, goal), tentative, n))
    return []

# Thread-safe command queue for the GUI to consume
cmd_queue = queue.Queue()

class RatControllerApp:
    def __init__(self, root):
        self.root = root
        root.title("Remote-controlled Rat — 20x20 Grid")
        self.grid_size = GRID_SIZE
        self.cell_px = CELL_PIXEL
        self.canvas = tk.Canvas(root, width=CANVAS_SIZE + 2*WINDOW_PADDING,
                                height=CANVAS_SIZE + 120, bg="white")
        self.canvas.pack()
        self.info_text = tk.StringVar()
        self.info_label = tk.Label(root, textvariable=self.info_text, font=("Courier", 11))
        self.info_label.pack(pady=4)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=4)
        tk.Button(btn_frame, text="Reset", command=self.reset).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_frame, text="Toggle Obstacles", command=self.toggle_obstacles).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_frame, text="Randomize Obstacles", command=self.randomize_obstacles).pack(side=tk.LEFT, padx=4)

        # state
        self.obstacles_enabled = True
        self.obstacles = set()
        self.rat_pos = (0, 0)  # (x, y)
        self.battery = 100
        self.path = []  # list of positions to follow
        self.moving = False
        self.lock = threading.Lock()

        self._draw_grid()
        self._draw_rat()
        self.randomize_obstacles()

        # Keybindings
        root.bind("<Up>", lambda e: self.move_command("UP"))
        root.bind("<Down>", lambda e: self.move_command("DOWN"))
        root.bind("<Left>", lambda e: self.move_command("LEFT"))
        root.bind("<Right>", lambda e: self.move_command("RIGHT"))
        root.bind("w", lambda e: self.move_command("UP"))
        root.bind("s", lambda e: self.move_command("DOWN"))
        root.bind("a", lambda e: self.move_command("LEFT"))
        root.bind("d", lambda e: self.move_command("RIGHT"))

        # periodic tick for processing queue and path movement
        self.root.after(100, self._tick)

    def _draw_grid(self):
        self.canvas.delete("grid")
        for i in range(self.grid_size + 1):
            x = WINDOW_PADDING + i * self.cell_px
            self.canvas.create_line(x, WINDOW_PADDING, x, WINDOW_PADDING + self.grid_size*self.cell_px, tag="grid")
            y = WINDOW_PADDING + i * self.cell_px
            self.canvas.create_line(WINDOW_PADDING, y, WINDOW_PADDING + self.grid_size*self.cell_px, y, tag="grid")
        # labels
        self.canvas.delete("labels")
        for i in range(self.grid_size):
            cx = WINDOW_PADDING + i*self.cell_px + self.cell_px/2
            self.canvas.create_text(cx, WINDOW_PADDING + self.grid_size*self.cell_px + 10, text=str(i), anchor="n", tag="labels", font=("Arial",7))
            cy = WINDOW_PADDING + i*self.cell_px + self.cell_px/2
            self.canvas.create_text(WINDOW_PADDING - 10, cy, text=str(i), anchor="e", tag="labels", font=("Arial",7))

    def _draw_rat(self):
        # remove previous rat
        self.canvas.delete("rat")
        x, y = self.rat_pos
        left = WINDOW_PADDING + x*self.cell_px + 4
        top = WINDOW_PADDING + y*self.cell_px + 4
        right = left + self.cell_px - 8
        bottom = top + self.cell_px - 8
        # simple oval representing the rat
        self.canvas.create_oval(left, top, right, bottom, fill="gray20", tag="rat")
        # eye
        ex = left + (right-left)*0.7
        ey = top + (bottom-top)*0.3
        self.canvas.create_oval(ex-2, ey-2, ex+2, ey+2, fill="white", tag="rat")

    def _draw_obstacles(self):
        self.canvas.delete("obstacle")
        for (ox, oy) in self.obstacles:
            left = WINDOW_PADDING + ox*self.cell_px + 2
            top = WINDOW_PADDING + oy*self.cell_px + 2
            right = left + self.cell_px - 4
            bottom = top + self.cell_px - 4
            self.canvas.create_rectangle(left, top, right, bottom, fill="sienna", tag="obstacle")

    def update_info(self):
        obs_count = len(self.obstacles) if self.obstacles_enabled else 0
        info = f"Pos: {self.rat_pos}    Battery: {self.battery}%    Obstacles: {obs_count}    Path: {len(self.path)}"
        self.info_text.set(info)

    def reset(self):
        with self.lock:
            self.rat_pos = (0, 0)
            self.battery = 100
            self.path = []
            self.moving = False
            self.randomize_obstacles()
        self._draw_rat()
        self.update_info()

    def toggle_obstacles(self):
        with self.lock:
            self.obstacles_enabled = not self.obstacles_enabled
            if not self.obstacles_enabled:
                self.obstacles.clear()
        self._draw_obstacles()
        self.update_info()

    def randomize_obstacles(self):
        with self.lock:
            self.obstacles.clear()
            if not self.obstacles_enabled:
                return
            total = self.grid_size*self.grid_size
            n = int(total * OBSTACLE_DENSITY)
            # avoid rat start
            choices = [(x, y) for x in range(self.grid_size) for y in range(self.grid_size) if (x,y) != self.rat_pos]
            self.obstacles = set(random.sample(choices, min(n, len(choices))))
        self._draw_obstacles()
        self.update_info()

    def move_command(self, cmd):
        """Move one step via local keyboard or network command."""
        with self.lock:
            dx, dy = 0, 0
            cmd = cmd.strip().upper()
            if cmd in ("UP","W"):
                dy = -1
            elif cmd in ("DOWN","S"):
                dy = 1
            elif cmd in ("LEFT","A"):
                dx = -1
            elif cmd in ("RIGHT","D"):
                dx = 1
            else:
                return
            new = (self.rat_pos[0] + dx, self.rat_pos[1] + dy)
            # boundaries
            if not (0 <= new[0] < self.grid_size and 0 <= new[1] < self.grid_size):
                # collision with wall - beep or flash
                self._flash_cell(self.rat_pos)
                return
            if self.obstacles_enabled and new in self.obstacles:
                # collision with obstacle
                self._flash_cell(new)
                return
            # apply move
            self.rat_pos = new
            self.battery = max(0, self.battery - 1)
            # if keyboard move, stop any current path
            self.path = []
            self.moving = False
        self._draw_rat()
        self.update_info()

    def _flash_cell(self, cell):
        # visual feedback for collision
        x, y = cell
        left = WINDOW_PADDING + x*self.cell_px + 2
        top = WINDOW_PADDING + y*self.cell_px + 2
        right = left + self.cell_px - 4
        bottom = top + self.cell_px - 4
        rect = self.canvas.create_rectangle(left, top, right, bottom, fill="red", tag="flash")
        self.root.after(150, lambda: self.canvas.delete(rect))

    def goto(self, target):
        """Calculate path to target and start following it."""
        tx, ty = target
        if not (0 <= tx < self.grid_size and 0 <= ty < self.grid_size):
            return False
        with self.lock:
            blocked = set(self.obstacles) if self.obstacles_enabled else set()
            if (tx,ty) in blocked:
                return False
            path = astar(self.rat_pos, (tx,ty), blocked, self.grid_size)
            if not path and (tx,ty) != self.rat_pos:
                return False
            self.path = path
            self.moving = True
        return True

    def stop(self):
        with self.lock:
            self.path = []
            self.moving = False
        self.update_info()

    def _tick(self):
        # process commands from queue (from network server)
        try:
            while True:
                cmd = cmd_queue.get_nowait()
                self._handle_remote_cmd(cmd)
        except queue.Empty:
            pass

        # follow path if moving
        with self.lock:
            if self.moving and self.path:
                next_pos = self.path.pop(0)
                # double-check obstacle didn't appear
                if self.obstacles_enabled and next_pos in self.obstacles:
                    self.moving = False
                    self.path = []
                else:
                    self.rat_pos = next_pos
                    self.battery = max(0, self.battery - 1)
                    if not self.path:
                        self.moving = False
        self._draw_rat()
        self._draw_obstacles()
        self.update_info()
        self.root.after(TICK_INTERVAL_MS, self._tick)

    def _handle_remote_cmd(self, cmd):
        # cmd is already upper-cased in server, may include args
        parts = cmd.strip().split()
        if not parts:
            return
        p0 = parts[0]
        if p0 in ("UP","DOWN","LEFT","RIGHT","W","A","S","D"):
            self.move_command(p0)
        elif p0 == "GOTO" and len(parts) >= 3:
            try:
                x = int(parts[1]); y = int(parts[2])
                ok = self.goto((x,y))
                # remote server sends response; we don't handle that here (server will respond)
            except ValueError:
                pass
        elif p0 == "STOP":
            self.stop()
        elif p0 == "RESET":
            self.reset()
        elif p0 == "OBSTACLES" and len(parts) >= 2:
            val = parts[1]
            if val == "ON":
                self.obstacles_enabled = True
                self.randomize_obstacles()
            elif val == "OFF":
                self.obstacles_enabled = False
                self.obstacles.clear()
        elif p0 == "BATTERY" and len(parts) >= 2:
            try:
                b = int(parts[1]); self.battery = max(0, min(100, b))
            except ValueError:
                pass
        elif p0 == "RANDOMIZE":
            self.randomize_obstacles()
        # any other commands ignored here; server can respond

# Simple TCP server to accept text commands and respond.
class CommandServer(threading.Thread):
    def __init__(self, host, port, app):
        super().__init__(daemon=True)
        self.host = host
        self.port = port
        self.app = app
        self.sock = None
        self.shutdown_flag = threading.Event()

    def run(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.sock.bind((self.host, self.port))
            self.sock.listen(5)
            print(f"[Server] Listening on {self.host}:{self.port} (text commands)")
        except Exception as e:
            print(f"[Server] Failed to start: {e}")
            return

        while not self.shutdown_flag.is_set():
            try:
                self.sock.settimeout(1.0)
                conn, addr = self.sock.accept()
            except socket.timeout:
                continue
            except Exception as e:
                print(f"[Server] Accept failed: {e}")
                continue

            print(f"[Server] Connection from {addr}")
            client = threading.Thread(target=self.handle_client, args=(conn, addr), daemon=True)
            client.start()

    def handle_client(self, conn, addr):
        conn.settimeout(1.0)
        try:
            conn.sendall(b"RAT SERVER READY\n")
            buf = b""
            while True:
                try:
                    data = conn.recv(1024)
                    if not data:
                        break
                    buf += data
                    while b"\n" in buf:
                        line, buf = buf.split(b"\n", 1)
                        line = line.decode("utf-8", errors="ignore").strip()
                        if not line:
                            continue
                        response = self.process_command(line)
                        if response is not None:
                            conn.sendall((response + "\n").encode("utf-8"))
                except socket.timeout:
                    # also check if server is shutting down
                    if self.shutdown_flag.is_set():
                        break
                    continue
        except Exception as e:
            print(f"[Server] Client handler error for {addr}: {e}")
        finally:
            try:
                conn.close()
            except:
                pass
            print(f"[Server] Connection closed {addr}")

    def process_command(self, raw_line):
        """Process a command and return a response string (or None)."""
        line = raw_line.strip()
        if not line:
            return None
        up = line.upper()
        # push command to GUI thread
        if up.startswith("GOTO "):
            parts = up.split()
            if len(parts) >= 3:
                try:
                    x = int(parts[1]); y = int(parts[2])
                    success = self.app.goto((x,y))
                    return "OK" if success else "FAIL"
                except ValueError:
                    return "ERROR invalid coords"
        elif up in ("UP","DOWN","LEFT","RIGHT","W","A","S","D"):
            cmd_queue.put(up)
            return "OK"
        elif up == "STOP":
            cmd_queue.put("STOP")
            return "OK"
        elif up == "RESET":
            cmd_queue.put("RESET")
            return "OK"
        elif up.startswith("OBSTACLES "):
            cmd_queue.put(up)
            return "OK"
        elif up.startswith("BATTERY "):
            cmd_queue.put(up)
            return "OK"
        elif up == "STATUS":
            with self.app.lock:
                return f"POS {self.app.rat_pos[0]} {self.app.rat_pos[1]} BATTERY {self.app.battery} OBS {len(self.app.obstacles)}"
        elif up == "RANDOMIZE":
            cmd_queue.put("RANDOMIZE")
            return "OK"
        elif up == "HELP":
            return "Commands: UP DOWN LEFT RIGHT GOTO x y STOP RESET STATUS OBSTACLES ON/OFF BATTERY n"
        else:
            return "ERROR unknown command"

    def stop(self):
        self.shutdown_flag.set()
        try:
            if self.sock:
                self.sock.close()
        except:
            pass

def main():
    root = tk.Tk()
    app = RatControllerApp(root)
    server = CommandServer(SERVER_HOST, SERVER_PORT, app)
    server.start()
    # on close, stop server
    def on_close():
        if messagebox.askokcancel("Quit", "Quit application?"):
            server.stop()
            root.destroy()
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()
    # ensure server stopped
    server.stop()

if __name__ == "__main__":
    main()
