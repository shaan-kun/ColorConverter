import sys


def rgb_to_hex(red, green, blue):
    return hex(red), hex(green), hex(blue)


def rgb_to_cmyk(red, green, blue):
    red = red / 255
    green = green / 255
    blue = blue / 255

    black = 1 - max(red, green, blue)

    if black == 1:
        return 0, 0, 0, 100

    cyan = (1 - red - black) / (1 - black)
    magenta = (1 - green - black) / (1 - black)
    yellow = (1 - blue - black) / (1 - black)

    return round(cyan * 100), round(magenta * 100), round(yellow * 100), round(black * 100)


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
            return 0, 0, 100

    hue = 0
    if color_max == red:
        hue = 60 * ((green - blue) / delta % 6)
    elif color_max == green:
        hue = 60 * ((blue - red) / delta + 2)
    elif color_max == blue:
        hue = 60 * ((red - green) / delta + 4)

    lightness = (color_max + color_min) / 2
    saturation = 0 if delta == 0 else delta / (1 - abs(2 * lightness - 1))

    return round(hue), round(saturation * 100), round(lightness * 100)


def rgb_to_hsv(red, green, blue):
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
            return 0, 0, 100

    hue = 0
    if color_max == red:
        hue = 60 * ((green - blue) / delta % 6)
    elif color_max == green:
        hue = 60 * ((blue - red) / delta + 2)
    elif color_max == blue:
        hue = 60 * ((red - green) / delta + 4)

    saturation = 0 if color_max == 0 else delta / color_max
    value = color_max

    return round(hue), round(saturation * 100), round(value * 100)


# def hex_to_rgb(red, green, blue):
#     red = int(red, 16)
#     green = int(green, 16)
#     blue = int(blue, 16)
#
#     return red, green, blue


def cmyk_to_rgb(cyan, magenta, yellow, black):
    cyan /= 100
    magenta /= 100
    yellow /= 100
    black /= 100

    red = 255 * (1 - cyan) * (1 - black)
    green = 255 * (1 - magenta) * (1 - black)
    blue = 255 * (1 - yellow) * (1 - black)

    return round(red), round(green), round(blue)


def hsl_to_rgb(hue, saturation, lightness):
    saturation /= 100
    lightness /= 100

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

    return round(red), round(green), round(blue)


def hsv_to_rgb(hue, saturation, value):
    saturation /= 100
    value /= 100

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

    return round(red), round(green), round(blue)


def rgb_to_color(color, values):
    return {
        'hex': rgb_to_hex,
        'cmyk': rgb_to_cmyk,
        'hsl': rgb_to_hsl,
        'hsv': rgb_to_hsv,
    }[color](*values)


def color_convert(func, values):
    values = func(*values)
    return rgb_to_color(color_2, values)


if __name__ == '__main__':
    color_1 = sys.argv[1]
    color_2 = sys.argv[-1]
    values = sys.argv[2:-1]

    result = None
    if color_1 == 'rgb':
        result = rgb_to_color(color_2, [int(num) for num in values])
    elif color_1 == 'hex':
        result = rgb_to_color(color_2, [int(num, 16) for num in values])
    elif color_1 == 'cmyk':
        result = color_convert(cmyk_to_rgb, [int(num) for num in values])
    elif color_1 == 'hsl':
        result = color_convert(hsl_to_rgb, [int(num) for num in values])
    elif color_1 == 'hsv':
        result = color_convert(hsv_to_rgb, [int(num) for num in values])

    print(*result)
