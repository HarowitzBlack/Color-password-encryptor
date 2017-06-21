import random

def gen_rgb():
  rgb_list = []
  for x in range(0,255):
    rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    if rgb not in rgb_list:
      rgb_list.append(rgb)
  return rgb_list


hex_list = []
def rgb2hex(rgb):
  hex = "#{:02x}{:02x}{:02x}".format(rgb[0],rgb[1],rgb[2])
  return hex

# generates rgb values
color_list = gen_rgb()
for rgbx in range(len(color_list)):
  hex_cols = rgb2hex(color_list[rgbx])
  hex_list.append(hex_cols)

print(hex_list)
