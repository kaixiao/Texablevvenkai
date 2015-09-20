# this code is boilerplate that doesn't work
# copied from SO

import png, array

point = (2, 10) # coordinates of pixel to be painted red

reader = png.Reader(filename='data/averaging_transform.png')
w, h, pixels, metadata = reader.read_flat()
# pixel_byte_width = 4 if metadata['alpha'] else 3
# pixel_position = point[0] + point[1] * w
# new_pixel_value = (255, 0, 0, 0) if metadata['alpha'] else (255, 0, 0)
# pixels[
#   pixel_position * pixel_byte_width :
#   (pixel_position + 1) * pixel_byte_width] = array.array('B', new_pixel_value)

im = []
for pixel in pixels:
	im.append(pixel)
im = [im[i*w:(i+1)*w-1] for i in range(h)]
# print h, len(im)

# output = open('image-with-red-dot.png', 'wb')
# writer = png.Writer(w, h, **metadata)
# writer.write_array(output, pixels)
# output.close()