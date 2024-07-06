"""JPEG and EXIF Tag and Marker definitions.

NOTE: This is not a complete list by any means. 
"""

import types


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