from PIL import Image

image = Image.open("Images/senate.jpg")

## greys = [" ", ".", "-", "\"", "r", "/", ">", ")", "[", "I", "Y", "Z", "h", "#", "8", "@"][::-1]
greys = [" ", ".", "-", "\"", "r", "/", ">", ")", "[", "I", "Y", "Z", "h", "#", "8", "@"] # (Reversed)


imageList = []

for y in range(image.height):
    for x in range(image.width):
        try: imageList.append(str(int(round((image.load()[x, y][0] + image.load()[x, y][1] + image.load()[x, y][2])/(3*17)))))
        except:
            try: imageList.append(str(int(round((image.load()[x, y] + image.load()[x, y] + image.load()[x, y])/(3*17)))))
            except: pass
    imageList.append("\n")


for i in range(len(imageList)):
    if imageList[i] != "\n":
        imageList[i] = (greys[int(imageList[i])])*2

print("".join(imageList))
