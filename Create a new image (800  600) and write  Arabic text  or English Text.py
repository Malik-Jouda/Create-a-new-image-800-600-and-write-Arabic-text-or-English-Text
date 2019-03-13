#  Create a new image (800 * 600) and write  Arabic text or English Text
# install: pip install --upgrade arabic-reshaper
# install: pip install python-bidi
# install: pip install Pillow

# import arabic_reshaper
# import get_display
# import ImageFont
# import Image
# import ImageDraw
import arabic_reshaper
from bidi.algorithm import get_display
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


# use a font!
fontFile = "arial.ttf"

image = Image.new('RGB', (800, 600), color = 'green')

# load the font
font = ImageFont.truetype(fontFile, 40)

# text1 and text2 Possible to be Arabic or English
text1 = input("Enter The Text 1 in English : ")
text2 = input("Enter The Text 2 in English : ")
text3 = input("Enter The Text 3 in Arabic : ")
text4 = input("Enter The Text 4 in Arabic : ")

reshaped_text1 = arabic_reshaper.reshape(text1)    # correct its shape
reshaped_text2 = arabic_reshaper.reshape(text2)    # correct its shape
reshaped_text3 = arabic_reshaper.reshape(text3)    # correct its shape
reshaped_text4 = arabic_reshaper.reshape(text4)    # correct its shape

bidi_text1 = get_display(reshaped_text1)           # correct its direction
bidi_text2 = get_display(reshaped_text2)           # correct its direction
bidi_text3 = get_display(reshaped_text3)           # correct its direction
bidi_text4 = get_display(reshaped_text4)           # correct its direction

# start drawing on image
draw = ImageDraw.Draw(image)

#draw.text((Width , height), text , color , font)
draw.text((130, 70), bidi_text1, fill="blue", font=font)
draw.text((155, 130), bidi_text2, fill="blue", font=font)
draw.text((530, 230), bidi_text3, fill="blue", font=font)
draw.text((555, 300), bidi_text4, fill="blue", font=font)

draw = ImageDraw.Draw(image)

# Save Image
image.save("result.jpg")

# show The new Image
image.show()