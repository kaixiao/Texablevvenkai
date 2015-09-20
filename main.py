# this code is boilerplate that doesn't work
# copied from SO

import png, array

point = (2, 10) # coordinates of pixel to be painted red

reader = png.Reader(filename='img1.png')
w, h, pixels, metadata = reader.read_flat()
# pixel_byte_width = 4 if metadata['alpha'] else 3
# pixel_position = point[0] + point[1] * w
# new_pixel_value = (255, 0, 0, 0) if metadata['alpha'] else (255, 0, 0)
# pixels[
#   pixel_position * pixel_byte_width :
#   (pixel_position + 1) * pixel_byte_width] = array.array('B', new_pixel_value)

planes = metadata['planes']

pixel_list = []
for pixel in pixels:
	pixel_list.append(pixel)

im = []
idx = 0
for i in range(h):
	im.append([])
	for j in range(w):
		im[i].append([])
		for k in range(planes):
			im[i][j].append(pixel_list[idx])
			idx += 1

def color_to_bw(img):
	h = len(img)
	w = len(img[0])
	out = []
	for i in range(h):
		out.append([])
		for j in range(w):
			out[i].append((img[i][j][0] + img[i][j][1] + img[i][j][2]) / 3.0)
	return out

def binary_image(img):
	# takes a black and white image. 2d array. everything greater than 128 becomes 255, everything less is 0
	h = len(img)
	w = len(img[0])
	out = []
	for i in range(h):
		out.append([])
		for j in range(w):
			out[i].append(255*int(img[i][j] >= 128))
	return out

bw = color_to_bw(im)
bw = binary_image(bw)
print len(bw)
# print h, len(im)

# output = open('image-with-red-dot.png', 'wb')
# writer = png.Writer(w, h, **metadata)
# writer.write_array(output, pixels)
# output.close()

f = open('clipped.png', 'wb')      # binary mode is important
w = png.Writer(w, h, greyscale=True)
w.write(f, bw)
f.close()




def unroll2d(arr):
	out = []
	for a in arr:
		for x in a:
			out.append(x)
	return out