
import requests
import json
import PIL
from PIL import Image,ImageFont,ImageDraw
from datetime import date


api_key = "5bbaea6400e80974fde1868716909b04"
#lat = "48.208176"
#lon = "16.373819"
us_list=["New York","Chicago","San fransisco"]
#india_list=["Surat","Mumbai","Delhi"]
canada_list=["Squamish","Ottawa","Edmonton"]
uk_list=["London","Manchester","Liverpool"]
country_list=[us_list, uk_list, canada_list]
position=[460,660,960]


for country in country_list:
    image=Image.open("post1.png")
    draw= ImageDraw.Draw(image)

#------For heading----------
    font = ImageFont.truetype('open-sans/OpenSans-Bold.ttf',size=50)
#font=ImageFont.load_default()
    content= "Today's Weather"
    color='rgb(0,0,0)'
    (x,y)=(50,100)
    draw.text((x,y), content, color, font=font)


#------For date and time------
    font = ImageFont.truetype('open-sans/OpenSans-Italic.ttf',size=30)
#font=ImageFont.load_default()
    today=date.today()
    content=date.today().strftime("%A - %B %d, %Y")
    color='rgb(0,0,0)'
    (x,y)=(50,175)
    draw.text((x,y), content, color, font=font)

index=0
for city in country:
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=5bbaea6400e80974fde1868716909b04&units=metric".format(
        city)

    response = requests.get(url)
    data = json.loads(response.text)
    #print(data)

    font = ImageFont.truetype('open-sans/OpenSans-Italic.ttf', size=40)
    color = 'rgb(0,0,0)'
    (x, y) = (70,position[index])
    draw.text((x, y), city, color, font=font)

    font = ImageFont.truetype('open-sans/OpenSans-Regular.ttf', size=60)
    content=str(data['main']['temp'])+ "\u00b0C"
    color = 'rgb(0,0,0)'
    (x, y) = (755, position[index])
    draw.text((x, y), content, color, font=font)

    index +=1

#image.show()
image.save(str(date.today())+country[0]+".png")
