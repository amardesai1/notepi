from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
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

f = open("output.txt", "r")
lastnote = f.read()

if lastnote!=output:
    f = open("output.txt", "w")
    f.write(output)                                                                                                                                                                                                    f.close()                                                                                                                                                                                                      
    inky_display = InkyPHAT("red")
    inky_display.set_border(inky_display.WHITE)

    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)

    from font_fredoka_one import FredokaOne
    font = ImageFont.truetype(FredokaOne, 22)

    message = output
    length = len(message)
    lines = length//17
    lastline = length%17

    if length < 18:
        w, h = font.getsize(message)
        x = (inky_display.WIDTH / 2) - (w / 2)
        y = (inky_display.HEIGHT / 2) - (h / 2)

        draw.text((x, y), message, inky_display.RED, font)

    else:
        if lastline!=0:
            lines+=1

        w, h = font.getsize("01234567890123456")
        height = 20*(lines//2)
        x = (inky_display.WIDTH / 2) - (w / 2)
        y = (inky_display.HEIGHT / 2) - (h / 2)-height
        start = 0
        end = 17-length
        for i in range(lines):
            msgslice = message[start:end]
            draw.text((x, y), msgslice, inky_display.RED, font)
            start+=17
            end+=17
            y+=20
            if end>0:
                draw.text((x, y), message[start:], inky_display.RED, font)
                break

    inky_display.set_image(img)
    inky_display.show()