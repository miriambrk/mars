# mars
Mission to Mars application
Files:
1) mission_to_mars.ipynb - original Jupyter notebook with the scraping of various Mars websites
2) scrape.py - Python file with the scraping code
3) template/index.html - the HTML file for the website
4) static/css/style2.css - the CSS file for the format
5) Procfile - for Heroku
6) requirements.txt


This is set up to use a mLab mongodb and run in Heroku as http://mars-mission.herokuapp.com/. Unfortunately, I don't know how 
to get it to find chromedriver. I finally included chromedriver in my repo, but that didn't help either. I have tried with and without
special Heroku Buildpacks for chromedriver and Chrome. 

