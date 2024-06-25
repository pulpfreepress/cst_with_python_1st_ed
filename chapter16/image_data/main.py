"""Demonstrate reading binary image data."""

import os




def main():

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


	# Tag Constants
	make_key = '010f'
	model_key = '0110'
	orientation_key = '0112'
	x_resolution_key = '011a'
	y_resolution_key = '011b'
	resolution_unit_key = '0128'
	software_key = '0131'
	datetime_key = '0132'
	artist_key = '013b'
	ycbcrpositioning_key = '0213'
	copyright_key = '8298'
	exif_offset_key = '8769'
	gps_info_key = '8825'

	tags = {}
	tags[make_key] = 'Make'
	tags[model_key] = 'Model'
	tags[orientation_key] = 'Orientation'
	tags[x_resolution_key] = 'X-Resolution'
	tags[y_resolution_key] = 'Y-Resolution'
	tags[resolution_unit_key] = 'Resolution Unit'
	tags[software_key] = 'Software'
	tags[datetime_key] = 'DateTime'
	tags[artist_key] = 'Artist'
	tags[ycbcrpositioning_key] = 'YCbCrPositioning'
	tags[copyright_key] = 'Copyright'
	tags[exif_offset_key] = 'EXIF Offset'
	tags[gps_info_key] = 'GPS Info'



	orientation = {}
	orientation[1] = 'Horizontal (Normal)'
	orientation[2] = 'Horizontal Mirrored'
	orientation[3] = 'Rotated 180 Degrees'
	orientation[4] = 'Vertical Mirrored'
	orientation[5] = 'Horizontal Mirrored then Rotated 190 Degrees CCW'
	orientation[6] = 'Rotated 90 Degrees CW'
	orientation[7] = 'Horizontal Mirrored then Rotated 90 Degrees CW'
	orientation[8] = 'Rotated 90 Degrees CCW'


	resolution_unit = {}
	resolution_unit[1] = 'Not Absolute'
	resolution_unit[2] = 'Pixels/Inch'
	resolution_unit[3] = 'Pixels/Centimeter'

	# JPEG Constants
	jpeg_soi = b'\xFF\xD8'
	processing_software_tag = 11
	image_width_tag = 256
	image_length_tag = 257
	

	try:
		working_dir = os.getcwd()
		image_dir = 'images'
		image_dir_path = os.path.join(working_dir, image_dir)

		if not os.path.exists(image_dir_path):
			os.makedirs(image_dir_path)


		#filename = input('Enter Image Filename: ')
		filename = input('Image Filename: ')

		with open(os.path.join(image_dir_path, filename), 'rb') as f:
			content = f.read()
			f.seek(0)
			print(f'Frist 24 bytes: {f.read(48)}')
			f.seek(0)
			exif_section_offset = content.index(bytes.fromhex('FFFe'))
			f.seek(exif_section_offset)
			print(f'EXIF Section Offset: {exif_section_offset} Read 2 : {f.read(2)}')
			f.seek(exif_section_offset + 2)
			print(f'Offset: {exif_section_offset + 2} Read 4 : {f.read(4)}')
			f.seek(exif_section_offset + 6)
			print(f'Offset: {exif_section_offset + 6} Read 4 : {f.read(4)}')
			f.seek(exif_section_offset + 8)
			print(f'First Endian \'I\' Offset: {exif_section_offset + 8} Read 2 : {f.read(2)}')

			first_endian_byte_offset = exif_section_offset + 8
			f.seek(first_endian_byte_offset + 8)
			exif_entries = int(swap_bytes(f.read(2)))
			print(f'Exif Entries: {exif_entries}')
			# Read Tags

			

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
				
				if data_length == 1:
					match tag_hex:
						case '0112':
							print(f'Data: {orientation[data_or_offset]}')
						case '0128':
							print(f'Data: {resolution_unit[data_or_offset]}')
						case _: continue

				f.seek(last_position)
						
				
					
				
	except (OSError, Exception) as e:
		print(f'Problem reading image file: {e}')


def swap_bytes(b:bytes)-> bytes:
	return b[1] + b[0]


if __name__ == '__main__':
	main()
