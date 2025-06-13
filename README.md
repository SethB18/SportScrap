# 🕸️ Web Scraper Flask App

A simple web scraping tool built using Python and BeautifulSoup, wrapped in a Flask web interface. Users can enter a URL, trigger the scraper, and see the results on the page.

--Note : The Target Domain Usaully Chnage thier domain this might cause the iframe and display the whole not just video

you can update this ---> spider.py right click the domain and change to thier current domain URl also change on app.js 


---

## 📦 Features

- Web-based interface using Flask
- Scrapes data with BeautifulSoup
- Output displayed in the browser
- Easy to set up and run locally

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/SethB18/SportScrap.git
cd SportScrap
-----Guid to Run Project

------- for clear project venv you need to rm venv and required it again by 

rm -rf venv
python3 -m venv venv
source venv/bin/activate

-------------For dependencies
pip show flask 
----------if it dont exist yet you can install by 
pip install flask 
pip install request flask beautifulsoup4
pip install drissionpage

export FLASK_APP=spider.py   # on Linux/macOS
set FLASK_APP=spider.py      # on Windows

flask run
