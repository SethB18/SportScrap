from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from DrissionPage import ChromiumPage
app = Flask(__name__)
import re

@app.route('/')
def home():
    url = 'https://www.magu114.com/tvlist.php'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    games = soup.find_all(class_='sports_game_list')
    lists = soup.find_all(class_='swiper-slide')
    sport_list = []

    for img in lists:
        photo = img.find('img')  # Find the first <img> tag within img element
        
        if photo is not None:
            # Get the 'src' attribute if the <img> tag was found
            image = photo.get('src')
            if image:  # Ensure 'src' exists
                print(image+"\n")
                if(image=="/data/file/17103943732728309426_uiEDCzxO5f0cb2794545d3381fb34225cbfc8f16beaa5bc9.png"):
                    icon = "soccer-ball.png"
                elif(image=="/data/file/17103943872728309427_zoeABk30d6cfd38ba9f0ec85da002c4b42a89185a7b92163.png"):
                    icon ="baseball.png"
                elif(image=="/data/file/17103943962728309426_btSv7qWPe9622b069a20cfdb892ee3b9cb9d10b161abaff7.png"):
                    icon ="basketball.png"
                elif(image=="/data/file/17103944042728309427_mYjQdfRw7b8487cad46b2258c4c91de89328b37341224bbc.png"):
                    icon ="volleyball.png"
                elif(image=="/data/file/17103944122728309426_FwQ2l9en56c8c298e8be8d5ba10af010197e6680579927f2.png"):
                    icon ="game.png"
                elif(image=="/data/file/17103944192728309426_fi0LDsUN45648e781f58fab40b0bb621e5fd972fbc09b6f6.png"):
                    icon ="ice.png"
                elif(image=="/data/file/17103944272728309427_xBIwc5lM1297969ee0e5e0922ada2c552b3ed5a8262691dc.png"):
                    icon ="league-of-legends-icon.png"
                elif(image=="/data/file/17103944372728309427_AqWDwi6Vbf9bb221bccd7393639bf112e229a4bfe7878dec.png"):
                    icon ="champion.png"
                elif(image=="/data/file/17106534252890389102_vGpJW4qNb6461f95a17a22c42a27c9e8da1856178205c1ec.png"):
                    icon ="punch.png"
                elif(image=="/data/file/17110861342890390332_YGEjl8is29e95cf6f0d50919f57a17f9b84b77327a7f0377.png"):
                    icon ="rugby-ball.png"
                else:
                    icon = "balls-sports.png"
                sport_list.append(icon)  # Add the image URL to the list
            else:
                print("No 'src' attribute found for this <img> tag")
        else:
            print("No <img> tag found within this element")

    print(sport_list)

    # print(sport_list)
    matchGame = []
    # for tt in textLeft:
    #     para = tt.get_text()
    #     teamLeft.append(para)
    # for tt in textRight:
    #     para = tt.get_text()
    #     teamRight.append(para)
    for game in games:
        teamL = game.find(class_='sglb_sports_team left').get_text()
        teamR = game.find(class_='sglb_sports_team right').get_text()
        league = game.find(class_='sglt_league').get_text()
        date = game.find(class_='sglt_date').get_text()
        gameId = game.find(class_='sports_game_list_bottom').get('onclick')
        if gameId:  # Ensure 'onclick' is not None or empty
            match = re.search(r"TVViewer\('(\d+)'", gameId)
            if match:  # Check if regex found a match
                subGameId = match.group(1)
            else:
                subGameId = 'Not Live yet'
        else:
            subGameId = 'Not GameId'
        gameObject = {
            'teamLeft':teamL,
            'teamRight':teamR,
            'league' : league,
            'date' : date,
            'watch' : subGameId
        }
        matchGame.append(gameObject)

    return render_template('index.html', allGames = matchGame, sports=sport_list)

if __name__ == '__main__':
    app.run(debug=True)
