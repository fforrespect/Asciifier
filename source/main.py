import sys
import AsciiArt

filepath = "../Images/"

AsciiArt.image_to_string(f"{filepath}{sys.argv[1]}", True)
