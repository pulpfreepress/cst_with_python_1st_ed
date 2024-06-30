"""Demonstrate reading binary image EXIF data."""

import os
import types

# JPEG Markers and Segments
jpeg_markers = types.SimpleNamespace()
jpeg_markers.SOI = b'\xff\xd8'
jpeg_markers.EOI = b'\xff\xd9'
jpeg_markers.APP1 = b'\xff\xe1'
jpeg_markers.COMMENT = b'\xff\xfe'

# Tag Codes -- String version of 2-byte hex values 
# Very small subset of EXIF tags
# Object properties can be used in match cases
tag_codes = types.SimpleNamespace()
tag_codes.make = '010f'
tag_codes.model = '0110'
tag_codes.orientation = '0112'
tag_codes.x_resolution = '011a'
tag_codes.y_resolution = '011b'
tag_codes.resolution_unit = '0128'
tag_codes.software = '0131'
tag_codes.datetime = '0132'
tag_codes.artist = '013b'
tag_codes.ycbcrpositioning = '0213'
tag_codes.copyright = '8298'
tag_codes.exif_offset = '8769'
tag_codes.gps_info = '8825'

# Tag Values
tags = {}
tags[tag_codes.make] = 'Make'
tags[tag_codes.model] = 'Model'
tags[tag_codes.orientation] = 'Orientation'
tags[tag_codes.x_resolution] = 'X-Resolution'
tags[tag_codes.y_resolution] = 'Y-Resolution'
tags[tag_codes.resolution_unit] = 'Resolution Unit'
tags[tag_codes.software] = 'Software'
tags[tag_codes.datetime] = 'DateTime'
tags[tag_codes.artist] = 'Artist'
tags[tag_codes.ycbcrpositioning] = 'YCbCrPositioning'
tags[tag_codes.copyright] = 'Copyright'
tags[tag_codes.exif_offset] = 'EXIF Offset'
tags[tag_codes.gps_info] = 'GPS Info'

# Tag Types
tag_types = {}
tag_types[1] = ('Unsigned Byte')
tag_types[2] = ('ASCII String')
tag_types[3] = ('Unsigned Short')
tag_types[4] = ('Unsigned Long')
tag_types[5] = ('Unsigned Rational')
tag_types[6] = ('Signed Byte')
tag_types[7] = ('Undefined')
tag_types[8] = ('Signed Short')
tag_types[9] = ('Signed Long')
tag_types[10] = ('Signed Rational')
tag_types[11] = ('Single')
tag_types[6] = ('Double')

# Orientation Values
orientation = {}
orientation[1] = 'Horizontal (Normal)'
orientation[2] = 'Horizontal Mirrored'
orientation[3] = 'Rotated 180 Degrees'
orientation[4] = 'Vertical Mirrored'
orientation[5] = 'Horizontal Mirrored then Rotated 190 Degrees CCW'
orientation[6] = 'Rotated 90 Degrees CW'
orientation[7] = 'Horizontal Mirrored then Rotated 90 Degrees CW'
orientation[8] = 'Rotated 90 Degrees CCW'

# Resolution Unit Values
resolution_unit = {}
resolution_unit[1] = 'Not Absolute'
resolution_unit[2] = 'Pixels/Inch'
resolution_unit[3] = 'Pixels/Centimeter'


def main():
	try:
		# Setup file paths
		working_dir = os.getcwd()
		image_dir = 'images'
		image_dir_path = os.path.join(working_dir, image_dir)

		# Create image director if it does not exist
		if not os.path.exists(image_dir_path):
			os.makedirs(image_dir_path)

		# Get JPEG image filename from user
		filename = input('JPEG Image Filename: ')

		# Open JPEG file in read binary mode
		with open(os.path.join(image_dir_path, filename), 'rb') as f:
			content = f.read()

			# Verify it's a JPEG file
			if is_jpeg_file(content[:2], content[-2:]):
				print(f'{filename} is a JPEG file. Extracting EXIF data...')
			else:
				print(f'{filename} is not a JPEG file. Exiting...')
				return
			
			app1_segment_offset = content.index(jpeg_markers.APP1)
			if app1_segment_offset != 0:
				print(f'App1 Segment offset: {app1_segment_offset}')

			comment_segment_offset = content.index(jpeg_markers.COMMENT)
			if comment_segment_offset != 0:
				print(f'Comment Segment offset: {comment_segment_offset}')


			f.seek(0)
			print(f'Frist 24 bytes: {f.read(48)}')
			f.seek(0)
			
			f.seek(comment_segment_offset)
			print(f'Comment Section Offset: {comment_segment_offset} Read 2 : {f.read(2)}')
			f.seek(comment_segment_offset + 2)
			print(f'Offset: {comment_segment_offset + 2} Read 4 : {f.read(4)}')
			f.seek(comment_segment_offset + 6)
			print(f'Offset: {comment_segment_offset + 6} Read 4 : {f.read(4)}')
			f.seek(comment_segment_offset + 8)
			print(f'First Endian \'I\' Offset: {comment_segment_offset + 8} Read 2 : {f.read(2)}')

			first_endian_byte_offset = comment_segment_offset + 8
			f.seek(first_endian_byte_offset + 8)
			exif_entries = int(swap_bytes(f.read(2)))
			print(f'Exif Entries: {exif_entries}')

			# Read Tags (Every 12 bytes)
			for i in range(exif_entries):
				print(f' {i} : {"*" * 20}')
				tag = bytearray(f.read(2))
				print(f'Raw bytes: {bytes(tag)}')
				tag_hex = f'{tag[1]:02x}{tag[0]:02x}'
				print(f'Tag Hex: {tag_hex}')
				print(f'Tag Name: {tags.get(tag_hex)}')
				tag_type = int(swap_bytes(f.read(2)))
				print(f'Tag Type: {tag_types[tag_type]}')
				data_length = int(swap_bytes(f.read(2)) + swap_bytes(f.read(2)))
				print(f'Data Length: {data_length}')
				data_or_offset = int(swap_bytes(f.read(2)) + swap_bytes(f.read(2)))
				print(f'Data/Offset: {data_or_offset}')
				last_position = f.tell()

				if data_length > 4:
					f.seek(first_endian_byte_offset + data_or_offset)
					print(f'Data: {f.read(data_length)}')
				elif data_length == 1:
					match tag_hex:
						case tag_codes.orientation:
							print(f'Data: {orientation[data_or_offset]}')
						case tag_codes.resolution_unit:
							print(f'Data: {resolution_unit[data_or_offset]}')
						case _: continue

				f.seek(last_position)
				
	except (OSError, Exception) as e:
		print(f'Problem reading image file: {e}')


def is_jpeg_file(first_two_file_bytes:bytes, last_two_file_bytes:bytes)->bool:
	if __debug__:
		print(f'{first_two_file_bytes} : {last_two_file_bytes}')
	return (first_two_file_bytes == jpeg_markers.SOI) and (last_two_file_bytes == jpeg_markers.EOI)

def swap_bytes(b:bytes)-> bytes:
	"""Swap little endian bytes."""
	return b[1] + b[0]




if __name__ == '__main__':
	main()
