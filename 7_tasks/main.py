from bs4 import BeautifulSoup
import webbrowser
import platform
import urllib.request, urllib.error, urllib.parse
import time


print('Menu list :\n1. Enter a line and each word of the line will be searched on google \n'
      '2. whatever you type, it will search every word\'s image on google\n'
      '3. print all urls on first page of google\n'
      '4. current time and date \n'
      '5. open default web browser -- Platform detected and then opening web browser\n'
      '6. All ip address on the network to be shown\n'
      '7. Enter URL and check owner and email id if available\n')

choice = int(input("Enter any number from 1 to 7 to perform specific task : "))

if choice == 1:
    line = input('Enter a line : ')
    line = line.strip()
    words = line.split()
    print(words)
    for each_word in words:
        webbrowser.open_new_tab("https://www.google.com/search?q="+each_word+"&oq="+each_word)

elif choice == 2:
    line = input('Enter a line : ')
    line = line.strip()
    words = line.split()
    print(words)
    for each_word in words:
        webbrowser.open_new_tab("https://www.google.com/search?q="+each_word+"&tbm=isch")

elif choice == 3:
    #line = input("Enter a line : ")
    #line = line.strip()
    url = "http://pagalworld.co"
#    #file = 'https://pagalworld.co/parmanu-2018-hindi-movie-mp3-songs/files.html'
    urll = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(urll, 'html.parser')
    tags = soup('a')
    for tag in tags:
        print(tag.get('href', None))

elif choice == 4:
    current_time = time.ctime()
    print(current_time)

elif choice == 5:
    os_name = platform.platform()
    print("Detected", os_name, "opening default browser")
    webbrowser.open("https://www.google.com")

elif choice == 6:
    exec(open('task6.py').read())

elif choice == 7:
    exec(open('task7.py').read())