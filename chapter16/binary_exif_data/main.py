"""Demonstrate reading binary image EXIF data."""

import os
from constants import jpeg_markers
from constants import tag_codes
from constants import tag_types
from constants import tags
from constants import orientation
from constants import resolution_unit


def main():
	try:
		# Setup file paths
		working_dir = os.getcwd()
		image_dir = 'images'
		image_dir_path = os.path.join(working_dir, image_dir)

		# Create image directory if it does not exist
		if not os.path.exists(image_dir_path):
			os.makedirs(image_dir_path)

		# Get JPEG image filename from user
		filename = input('JPEG Image Filename: ')

		# Open JPEG file in read binary mode
		with open(os.path.join(image_dir_path, filename), 'rb') as f:
			
			# Read entire file
			content = f.read()

			# Print first 512 bytes and print hex
			for s in content[:512]:
				print(f'{s:02x} ', end='')
			print()

			# Read  forst 512 bytes and print chars
			for s in content[:512]:
				print(f'{chr(s)} ', end='')
			print()

			# Reset file pointer to beginning of file
			f.seek(0)

			# Verify it's a JPEG file
			print(f'Verifying JPEG File...')
			if is_jpeg_file(content[:2], content[-2:]):
				print(f'{filename} is a JPEG file. Extracting EXIF data...')
			else:
				print(f'{filename} is not a JPEG file. Exiting...')
				return
			

			# Find Segment Offsets
			print(f'{"-" * 10} Segment Offsets {"-" * 10}')
	
			app1_segment_offset = None
			try:
				app1_segment_offset = content.index(jpeg_markers.APP1)
				print(f'APP1 Segment offset: {app1_segment_offset}')
			except Exception:
				print(f'APP1 segment not found.')

			exif_segment_offset = None
			try:
				exif_segment_offset = content.index(jpeg_markers.EXIF)
				print(f'Exif Segment offset: {exif_segment_offset}')
			except Exception:
				print('Exif segment not found.')

			comment_segment_offset = None
			try:
				comment_segment_offset = content.index(jpeg_markers.COMMENT)
				print(f'Comment Segment offset: {comment_segment_offset}')
			except Exception:
				print('Comment segment not found.')

			# Exit if no EXIT segment
			if not exif_segment_offset:
				print(f'{filename} does not contain an EXIF segment. ')
				print('Exiting program.')
				return

			# Determine Endian
			endian_offset = None
			intel = False
			try:
				endian_offset = f.seek(exif_segment_offset + 6)
				endian_marker = f.read(4)
				if endian_marker == jpeg_markers.INTEL:
					intel = True
					print(f'Endian Marker: {endian_marker} : Endian is INTEL')
				else:
					print(f'Endian Marker: {endian_marker} : Endian is MOTOROLA')
			
			except Exception:
				print('Endian offset not found.')
				
			# Print the endian marker
			f.seek(endian_offset)
			print(f'Endian Offset: {endian_offset} Read 4 : {f.read(4)}')
			f.seek(endian_offset + 8)
			exif_entries_raw_bytes = bytearray(f.read(2))

			# How many EXIF records are there?
			print(f'Exif Entries Raw Bytes: {bytes(exif_entries_raw_bytes)}')
			f.seek(-2, 1)
			exif_entries = int(swap_bytes(f.read(2)))
			print(f'Exif Entries: {exif_entries}')

			print('*' * 130)
			# Print column headers
			print(f'{"No.":<8}{"Raw Bytes":<10}{"Tag Hex":<10}{"Tag Name":30} ' \
			f'{"Tag Type":<20} {"Length":<8}{"Data/Offset":<15}{"Data":<50}')
			print('-' * 130)

			# Read Tag Records
			# Every 12 bytes from just past exif_entries bytes.
			# 
			# ----Tag Record Layout----
			# Tag:         2 Bytes
			# Tag Type:    2 Bytes 
			# Data Length: 4 Bytes
			# Data/Offset: 4 Bytes
			###########################

			for i in range(exif_entries):
				# Read tag bytes
				tag = bytearray(f.read(2))

				# Convert to hex string
				tag_hex = 0
				if intel:
					tag_hex = f'{tag[1]:02x}{tag[0]:02x}'
					
				else:
					tag_hex = f'{tag[0]:02x}{tag[1]:02x}'

				# Read Tag Type
				tag_type = int(swap_bytes(f.read(2)))
				# Read Data Length
				data_length = \
					int(swap_bytes(f.read(2)) + swap_bytes(f.read(2)))
				# Read data or offset
				data_or_offset = \
					int(swap_bytes(f.read(2)) + swap_bytes(f.read(2)))
			
				data = 'None'
				if data_length > 4:
					last_position = f.tell()
					f.seek(endian_offset + data_or_offset)
					data = f.read(data_length)
					f.seek(last_position)
				elif data_length == 1:
					match tag_hex:
						case tag_codes.orientation:
							data = orientation[data_or_offset]
						case tag_codes.resolution_unit:
							data = resolution_unit[data_or_offset]
						case _: pass

				# Print EXIF data
				print(f'{i: <8d}{f"{tag[0]:02x}{tag[1]:02x}":10}{tag_hex: <10}' \
				f'{tags.get(tag_hex):30}{tag_types.get(tag_type):<20}' \
				f'{data_length:<8d}{data_or_offset:<15}{data}')
		
			

	except (OSError, Exception) as e:
		print(f'Problem reading image file: {e}')


# Utility Methods
def is_jpeg_file(first_two_file_bytes:bytes, 
				 last_two_file_bytes:bytes)->bool:
	"""Verify JPEG SOI and EOI."""
	if __debug__:
		print(f'SOI: {first_two_file_bytes} : \
		EOI: {last_two_file_bytes}')
	return (first_two_file_bytes == jpeg_markers.SOI) \
		and (last_two_file_bytes == jpeg_markers.EOI)


def swap_bytes(b:bytes)-> bytes:
	"""Swap little endian bytes."""
	return b[1] + b[0]
	

if __name__ == '__main__':
	main()
