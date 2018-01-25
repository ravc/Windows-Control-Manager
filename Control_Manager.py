import pyowm
import subprocess
import time
import smtplib
import os
import getpass
import feedparser

def Weather(location):
    owm = pyowm.OWM('api key here')

    observation = owm.weather_at_place(location)
    w = observation.get_weather()
    #print(w)

    fc = owm.daily_forecast(location, limit=5)
    f = fc.get_forecast()

    wind = w.get_wind()
    humidity = w.get_humidity()
    temp = w.get_temperature('fahrenheit')
    clouds = w.get_clouds()
    rain = w.get_rain()
    snow = w.get_snow()
    stat = w.get_status()
    srise = w.get_sunrise_time()
    sset = w.get_sunset_time()

    print ('Sunrise at: ' + time.ctime(srise))
    print ('Sunset at: ' + time.ctime(sset))
    print (temp)
    print ('Humidity: ' + str(humidity) + '%')
    print ('Current Status: ' + stat)
    print ('Cloud coverage: ' + str(clouds) + '%')
    print ('wind: ' + str(wind))
    print ('Rain volume: ' + str(rain))
    print ('Snow volume: ' + str(snow))

    print('\n''Five day forecast')
    for weather in f:
        print(time.ctime(weather.get_reference_time()),weather.get_status())

    input('\n''Press any key to return')

def Battery():
    subprocess.call("powercfg -getactivescheme")
    print('\n')

    print('low, mid, or max''\n')

    p = input()
    if p == 'low':
        subprocess.call("powercfg -SETACTIVE SCHEME_MAX")
        print('Low power mode on')
    elif p == 'mid':
        subprocess.call("powercfg -SETACTIVE SCHEME_BALANCED")
        print('Balanced power mode on')
    elif p == 'max':
        subprocess.call("powercfg -SETACTIVE SCHEME_MIN")
        print('High power mode on')
    else:
        print('not a valid input')

    input('Press any key to return')

def Email(usr, pwd, to, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(usr, pwd)
        server.sendmail(usr, to, msg)
        server.close()
        print('sent')
    except:
        print('failed')
    input()

def Rss():
	rss2 = 'http://www.engadget.com/rss.xml'
	rss4 = 'http://www.theguardian.com/us/rss'
	rss5 = 'https://www.reddit.com/r/news/.rss'
	
	print('\n''Engadget''\n')
	f2 = feedparser.parse(rss2)
	print(f2['entries'][0]['title'])
	print(f2['entries'][1]['title'])
	print(f2['entries'][2]['title'])
	print(f2['entries'][3]['title'])
	print(f2['entries'][4]['title'])
	input('\n''Press any key to continue')
	os.system('cls')
	
	print('\n''The Guardian''\n')
	f4 = feedparser.parse(rss4)
	print(f4['entries'][0]['title'])
	print(f4['entries'][1]['title'])
	print(f4['entries'][2]['title'])
	print(f4['entries'][3]['title'])
	print(f4['entries'][4]['title'])
	input('\n''Press any key to continue')
	os.system('cls')
	
	print('\n''Reddit News''\n')
	f5 = feedparser.parse(rss5)
	print(f5['entries'][0]['title'])
	print(f5['entries'][1]['title'])
	print(f5['entries'][2]['title'])
	print(f5['entries'][3]['title'])
	print(f5['entries'][4]['title'])
	input('\n''Press any key to continue')
	os.system('cls')
	
while True:            
    print('\n''Control Manager 1.2')
    print('\n''Please select an option''\n')
    print('1: Weather')
    print('2: News')
    print('3: Send Email')
    print('4: Battery Mode''\n')

    c = input()
    os.system('cls')

    if c == '1':
        print('Please choose a location''\n')
        print('\n''1: College Station')
        print('2: Fort Worth')
        print('3: Dallas''\n')
        l = input()
        os.system('cls')
        if l == '1':
            print('\n''The weather in College Station is: ''\n')
            Weather('CollegeStation,us')
        elif l == '2':
            print('\n''The weather in Fort Worth is: ''\n')
            Weather('FortWorth,us')
        elif l == '3':
            print('\n''The weather in Dallas is: ''\n')
            Weather('Dallas,us')
        os.system('cls')
    elif c == '2':
        Rss()
        os.system('cls')
    elif c == '3':
        print('\n''Must use GMail account with SMTP enabled''\n')
        usr = input('Gmail email: ')
        os.sytem('cls')
        print('\n''Please input email password: ')
        pwd = getpass.getpass()
        os.sytem('cls')
        to = input('Send to: ')
        msg = input('Please input message: ')
        Email(usr, pwd, to, msg)
        os.system('cls')
    elif c == '4':
        Battery()
        os.system('cls')
