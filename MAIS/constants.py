import pathlib

# resources paths
UI = pathlib.Path(__file__).parent/"ui/mais.ui"
PLACEHOLDER_IMAGE = pathlib.Path(__file__).parent/"assets/images/placeholder.png"

# style sheets
VISIBLE_INDICATOR = "font-size: 12px; color: rgba(255, 0, 0, 255)"
INVISIBLE_INDICATOR = "font-size: 12px; color: rgba(255, 0, 0, 0)"
GRAYED = "color: rgb(119, 118, 123);"
BLACKED = "color: rgb(0, 0, 0);"

# tasks indexes
ALIGN = 0
COMPRESS = 1
STACK = 2  

# compress indexes
JPEG = 0
PNG = 1
GIF = 2

# stack indexes
MEDIAN = 0

# cached
CACHED_DIR = pathlib.Path(__file__).parent/"cached"
JPEG_CACHED_DIR = CACHED_DIR/"jpeg"
TIFF_CACHED_DIR = CACHED_DIR/"tiff"