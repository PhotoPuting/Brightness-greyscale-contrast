# Brightness-greyscale-contrast
 Python-Package for creating a nice looking contrast on your image (color + greyscale)

## Install:
``
python3 setup.py install --user
``

## Usage:
```python
from brightness_greyscale_contrast.process import BGC

if __name__ == "__main__":
    BGC("img5.jpg", True) 
```

## Reference:
<strong>`class BGC:`</strong> <br>
`img_url: string: name of your image (default=input.jpg)` <br>
`show_img_after: bool: show image after the process (default=False)`