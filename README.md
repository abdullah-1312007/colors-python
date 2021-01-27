# ColorsPy

This is a simple python package that can be used for adding colors in PyGame or just to see the RGB values of almost any color.

Example Code:
- Basic use:
``` py
    from colorspy import *

    print(red)
    print(blue)
```

- For PyGame:
``` py
    import colorspy as colors
    import pygame

    pygame.init()

    win = pygame.display.set_mode((800, 600))
    run = True

    while run:
	"""
   	Rest of your code
	"""

    	win.fill(colors.red)

    	pygame.display.update
```

- Color Conversion:
``` py
    from colorspy import *

    converter = ColorConverter()

    """
    If you want any other color's HEX value, you could just pass a tuple of the RGB values.
    The hash variable is a boolean that tells that if you want a hash sign in the HEX value.
    """

    hex_red = converter.rgb2hex(red, hash=True) 

    """
    This will return the RGB value of blue.
    """

    rgb_blue = converter.hex2rgb("0000ff") 
```
- Color Picker
``` py
import colorspy as colors

my_color = colors.color_picker()

"""
This will return a list of the RGB value and the HEX value of the color you select. There is also a argument hex_value which is a boolean. You can use that to decide that whether you want the HEX value or not.
"""
```

v 0.1
- Added most basic colors.

v 0.2
- Added support for RGB to HEX and HEX to RGB color conversion.
- Added a few more colors.

v 0.2.1
- Fixed a minor bug

v 0.3
- Added a whole lot more colors.
- Added a color picker to choose colors easily.

v 0.4
- Fixed color values of some colors
