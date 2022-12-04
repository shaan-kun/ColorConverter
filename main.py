def rgb_to_hex(red, green, blue):
    red = int(red)
    green = int(green)
    blue = int(blue)

    return red, green, blue


def rgb_to_cmyk(red, green, blue):
    red = red / 255
    green = green / 255
    blue = blue / 255

    black = 1 - max(red, green, blue)

    if black == 1:
        return 0, 0, 0, 1

    cyan = (1 - red - black) / (1 - black)
    magenta = (1 - green - black) / (1 - black)
    yellow = (1 - blue - black) / (1 - black)

    return cyan, magenta, yellow, black


def rgb_to_hsl(red, green, blue):
    red = red / 255
    green = green / 255
    blue = blue / 255

    color_max = max(red, green, blue)
    color_min = min(red, green, blue)
    delta = color_max - color_min

    if delta == 0:
        if color_max == 0:
            return 0, 0, 0
        else:
            return 0, 0, 1

    hue = 0
    if color_max == red:
        hue = 60 * ((green - blue) / delta % 6)
    elif color_max == green:
        hue = 60 * ((blue - red) / delta + 2)
    elif color_max == blue:
        hue = 60 * ((red - green) / delta + 4)

    lightness = (color_max + color_min) / 2
    saturation = 0 if delta == 0 else delta / (1 - abs(2 * lightness - 1))

    return hue, saturation, lightness


def rgb_to_hsv(red, green, blue):
    red = red / 255
    green = green / 255
    blue = blue / 255

    color_max = max(red, green, blue)
    color_min = min(red, green, blue)
    delta = color_max - color_min

    hue = 0
    if color_max == red:
        hue = 60 * ((green - blue) / delta % 6)
    elif color_max == green:
        hue = 60 * ((blue - red) / delta + 2)
    elif color_max == blue:
        hue = 60 * ((red - green) / delta + 4)

    saturation = 0 if color_max == 0 else delta / color_max
    value = color_max

    return hue, saturation, value


def hex_to_rgb(red, green, blue):
    red = int(red, 16)
    green = int(green, 16)
    blue = int(blue, 16)

    return red, green, blue


def cmyk_to_rgb(cyan, magenta, yellow, black):
    red = 255 * (1 - cyan) * (1 - black)
    green = 255 * (1 - magenta) * (1 - black)
    blue = 255 * (1 - yellow) * (1 - black)

    return red, green, blue


def hsl_to_rgb(hue, saturation, lightness):
    color = (1 - abs(2 * lightness - 1)) * saturation
    x = color * (1 - abs((hue / 60) % 2 - 1))
    m = lightness - color / 2

    red, green, blue = 0, 0, 0
    if 0 <= hue < 60:
        red, green, blue = color, x, 0
    elif 60 <= hue < 120:
        red, green, blue = x, color, 0
    elif 120 <= hue < 180:
        red, green, blue = 0, color, x
    elif 180 <= hue < 240:
        red, green, blue = 0, x, color
    elif 240 <= hue < 300:
        red, green, blue = x, 0, color
    elif 300 <= hue < 360:
        red, green, blue = color, 0, x

    red = (red + m) * 255
    green = (green + m) * 255
    blue = (blue + m) * 255

    return red, green, blue


def hsv_to_rgb(hue, saturation, value):
    color = value * saturation
    x = color * (1 - abs((hue / 60) % 2 - 1))
    m = value - color

    red, green, blue = 0, 0, 0
    if 0 <= hue < 60:
        red, green, blue = color, x, 0
    elif 60 <= hue < 120:
        red, green, blue = x, color, 0
    elif 120 <= hue < 180:
        red, green, blue = 0, color, x
    elif 180 <= hue < 240:
        red, green, blue = 0, x, color
    elif 240 <= hue < 300:
        red, green, blue = x, 0, color
    elif 300 <= hue < 360:
        red, green, blue = color, 0, x

    red = (red + m) * 255
    green = (green + m) * 255
    blue = (blue + m) * 255

    return red, green, blue
