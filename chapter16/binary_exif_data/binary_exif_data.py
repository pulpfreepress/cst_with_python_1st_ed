"""Demonstrate reading binary image EXIF data."""

import os
import types
from io import BufferedRandom


# JPEG Markers and Segments
jpeg_markers = types.SimpleNamespace()
jpeg_markers.SOI = b'\xff\xd8'
jpeg_markers.EOI = b'\xff\xd9'
jpeg_markers.APP1 = b'\xff\xe1'
jpeg_markers.COMMENT = b'\xff\xfe'
jpeg_markers.EXIF = b'Exif'
jpeg_markers.INTEL = b'II*\x00'
jpeg_markers.MOTOROLA = b'MM\x00*'

# Tag Codes -- String version of 2-byte hex values 
# Very small subset of EXIF tags
# Object properties can be used in match cases
tag_codes = types.SimpleNamespace()
tag_codes.image_width = '0100'
tag_codes.image_length = '0101'
tag_codes.bits_per_sample = '0102'
tag_codes.photometric_interpretation = '0106'
tag_codes.make = '010f'
tag_codes.model = '0110'
tag_codes.orientation = '0112'
tag_codes.samples_per_pixel = '0115'
tag_codes.x_resolution = '011a'
tag_codes.y_resolution = '011b'
tag_codes.resolution_unit = '0128'
tag_codes.software = '0131'
tag_codes.datetime = '0132'
tag_codes.artist = '013b'
tag_codes.host_computer = '013c'
tag_codes.ycbcrpositioning = '0213'
tag_codes.copyright = '8298'
tag_codes.exif_offset = '8769'
tag_codes.gps_info = '8825'
tag_codes.unknown = '0000'

# Tag Values
tags = {}
tags[tag_codes.image_width] = 'Image Width'
tags[tag_codes.image_length] = 'Image Length'
tags[tag_codes.bits_per_sample] = 'Bits Per Sample'
tags[tag_codes.photometric_interpretation] = 'Photometric Interpretation'
tags[tag_codes.make] = 'Make'
tags[tag_codes.model] = 'Model'
tags[tag_codes.orientation] = 'Orientation'
tags[tag_codes.samples_per_pixel] = 'Samples Per Pixel'
tags[tag_codes.x_resolution] = 'X-Resolution'
tags[tag_codes.y_resolution] = 'Y-Resolution'
tags[tag_codes.resolution_unit] = 'Resolution Unit'
tags[tag_codes.software] = 'Software'
tags[tag_codes.datetime] = 'DateTime'
tags[tag_codes.artist] = 'Artist'
tags[tag_codes.host_computer] = 'Host Computer'
tags[tag_codes.ycbcrpositioning] = 'YCbCrPositioning'
tags[tag_codes.copyright] = 'Copyright'
tags[tag_codes.exif_offset] = 'EXIF Offset'
tags[tag_codes.gps_info] = 'GPS Info'
tags[tag_codes.unknown] = 'Unknown'

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
tag_types[12] = ('Double')
tag_types[129] = ('UTF-8')


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

		# Create image directory if it does not exist
		if not os.path.exists(image_dir_path):
			os.makedirs(image_dir_path)

		# Get JPEG image filename from user
		filename = input('JPEG Image Filename: ')

		# Open JPEG file in read binary mode
		with open(os.path.join(image_dir_path, filename), 'rb') as f:
			
			# Read entire file
			content = f.read()

			# Print first 512 bytes
			for s in content[:512]:
				print(f'{s:02x} ', end='')
			print()

			for s in content[:512]:
				print(f'{chr(s)} ', end='')
			print()

			f.seek(0)
			print(f'{f.read(512)}')
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

			# Determine Endian
			if exif_segment_offset:
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
				
				# Print each EXIF record
				print(f'{"-" * 10} Exif Entries: {exif_entries} {"-" * 10}')

				print(f'{"No.":<8}{"Raw Bytes":<10}{"Tag Hex":<10}{"Tag Name":30}{"Tag Type":<20}{"Length":<8}{"Data/Offset":<15}{"Data":<50}')

				# Read Tags (Every 12 bytes)
				# ----Tag Record Layout----
				# Tag:         2 Bytes
				# Tag Type:    2 Bytes 
				# Data Length: 4 Bytes
				# Data/Offset: Variable
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
					data_length = int(swap_bytes(f.read(2)) + swap_bytes(f.read(2)))
					# Read data or offset
					data_or_offset = int(swap_bytes(f.read(2)) + swap_bytes(f.read(2)))
				
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


					print(f'{i: <8d}{f'{tag[0]:02x}{tag[1]:02x}':10}{tag_hex:<10}{tags.get(tag_hex):30}{tag_types.get(tag_type):<20}{data_length:<8d}{data_or_offset:<15}{data}')
			else:
				print(f'{filename} does not contain an EXIF segment. ')


	except (OSError, Exception) as e:
		print(f'Problem reading image file: {e}')



# Utility Methods

def is_jpeg_file(first_two_file_bytes:bytes, last_two_file_bytes:bytes)->bool:
	"""Verify JPEG SOI and EOI."""
	if __debug__:
		print(f'SOI: {first_two_file_bytes} : EOI: {last_two_file_bytes}')
	return (first_two_file_bytes == jpeg_markers.SOI) and (last_two_file_bytes == jpeg_markers.EOI)


def swap_bytes(b:bytes)-> bytes:
	"""Swap little endian bytes."""
	return b[1] + b[0]




if __name__ == '__main__':
	main()
