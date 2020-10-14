from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
import os
import requests
from bs4 import BeautifulSoup

url = 'https://pc.amardesai.org/noteform.php'

res = requests.get(url)

html_page = res.content

soup = BeautifulSoup(html_page, 'html.parser')

text = soup.find_all(text=True)

output = ''

blacklist = [

    '[document]',

    'noscript',

    'header',

    'html',

    'meta',

    'head',

    'input',

    'script',

    # there may be more elements you don't want, such as "style", etc.

]

for t in text:

    if t.parent.name not in blacklist:

        output += '{} '.format(t)

output = output.strip()

#print output;

f = open("output.txt", "r")
lastnote = f.read()
#print(lastnote)

if lastnote!=output:
    f = open("output.txt", "w")
    f.write(output)
    f.close()


    inky_display = InkyPHAT("red")
    inky_display.set_border(inky_display.WHITE)

    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)

    from font_fredoka_one import FredokaOne

    font = ImageFont.truetype(FredokaOne, 22)

    message = output
    #message = "test text"
    w, h = font.getsize(message)
    x = (inky_display.WIDTH / 2) - (w / 2)
    y = (inky_display.HEIGHT / 2) - (h / 2)

    draw.text((x, y), message, inky_display.RED, font)
    inky_display.set_image(img)
    inky_display.show()

