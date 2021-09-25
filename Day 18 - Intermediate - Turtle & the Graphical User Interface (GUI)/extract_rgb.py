import colorgram
# Extract RGB Values from Images

rgb_colors = []
colors = colorgram.extract("image.jpg", 38)
#print(colors)
for color in colors:
    #rgb_colors.append(color.rgb) 還需再整理
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)
