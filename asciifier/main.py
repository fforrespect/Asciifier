import sys
import requests

import AsciiArt

IMAGE_STORE_FP = "../imageStore/image.jpg"

filepath = sys.argv[1]

if "https://" in filepath or "http://" in filepath:
    response = requests.get(filepath)
    with open(IMAGE_STORE_FP, "wb") as f:
        f.write(response.content)
    filepath = IMAGE_STORE_FP

AsciiArt.image_to_string(filepath, True)
