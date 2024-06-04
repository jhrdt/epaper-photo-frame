import struct

# def as_shorts(i):
#     """Reads a integer as two 4bit shorts, represented as two ints."""
#     if isinstance(i, bytes):
#         i = ord(i)
#     four_bit_mask = 0b00001111
#     a = i & four_bit_mask  # leading 4 bits
#     b = i >> 4  # trailing 4 bits
#     return (b, a)

def as_int(tuple):
    return tuple[0]

def bmp_header(fh):
    type_ = fh.read(2).decode()
    size =  struct.unpack('I', fh.read(4))
    reserved_1 = struct.unpack('H', fh.read(2))
    reserved_2 = struct.unpack('H', fh.read(2))
    offset = struct.unpack('I', fh.read(4))
    result = {
        "type": type_,
        "size": size,
        "reserved_1": reserved_1,
        "reserved_2": reserved_2,
        "offset": as_int(offset)
    }
    fh.seek(0)
    return result

def bmp_dib_header(fh):
    fh.seek(14)
    dib_header_size = struct.unpack('I', fh.read(4))
    width = struct.unpack('I', fh.read(4))
    height = struct.unpack('I', fh.read(4))
    color_planes = struct.unpack('H', fh.read(2))
    bit_per_pixel = struct.unpack('H', fh.read(2))
    compression_method  = struct.unpack('I', fh.read(4))
    raw_img_size = struct.unpack('I', fh.read(4))
    horiziontal_resolution = struct.unpack('I', fh.read(4))
    vertical_resolution = struct.unpack('I', fh.read(4))
    number_of_colours = struct.unpack('I', fh.read(4))
    important_colours = struct.unpack('I', fh.read(4))
    result = {
        "dib_header_size" : dib_header_size,
        "width" : as_int(width),
        "height" : as_int(height),
        "color_planes" : color_planes,
        "bit_per_pixel" : as_int(bit_per_pixel),
        "compression_method" : compression_method,
        "raw_img_size" : raw_img_size,
        "horiziontal_resolution" : horiziontal_resolution,
        "vertical_resolution" : vertical_resolution,
        "number_of_colours" : as_int(number_of_colours),
        "important_colours" : important_colours,
    }
    fh.seek(0)
    return result


# def pixel_as_bytes(fh):
#     fh.seek(0)
#     header = bmp_header(fh)
#     dib_header = bmp_dib_header(fh)

#     offset = header["offset"]
#     fh.seek(offset)

#     width = dib_header["width"]
#     height = dib_header["height"]
#     assert width * height == 600 * 448, "Expected size 600x448"

#     bit_per_pixel = dib_header["bit_per_pixel"]
#     assert bit_per_pixel == 4, "Expected 4 bits per pixel"

#     num_of_colours = dib_header["number_of_colours"]
#     assert num_of_colours == 7, "Expected 7 colours"

#     bits_per_width = bit_per_pixel * width
#     bytes_per_width = int(bits_per_width / 8)

#     pixels = width * height
#     buf = [0x00] * pixels
#     for line_no in range(height):
#         row = height - (line_no + 1)
#         offset = row * width
#         for i in range(bytes_per_width):
#             single_byte = fh.read(1)  # two pixels for 1 byte
#             short1, short2 = as_shorts(single_byte)
#             buf[offset + (i * 2)] = short1
#             buf[offset + (i * 2) + 1] = short2
#     return bytes(buf)

def as_bytes(fh):
    fh.seek(0)
    header = bmp_header(fh)
    dib_header = bmp_dib_header(fh)

    offset = header["offset"]
    fh.seek(offset)

    width = dib_header["width"]
    height = dib_header["height"]

    bit_per_pixel = dib_header["bit_per_pixel"]
    bits_per_width = bit_per_pixel * width
    bytes_per_width = int(bits_per_width // 8)

    for i in range(height):
        row = height - (i + 1)
        pad = row * bytes_per_width
        fh.seek(offset + pad)
        for i in range(bytes_per_width):
            byte = fh.read(1)
            yield byte

# def as_ints(fh):
#     for b in as_bytes(fh):
#         short1, short2 = as_shorts(b)
#         yield short1
#         yield short2
