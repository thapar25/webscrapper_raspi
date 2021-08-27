# webscrapper for raspi

The following project was made to keep track of an item on www.amazon.in
The credit to the code goes to Dev Ed from Youtube.
I used his piece of code to deploy it 24*7 on my raspberry pi4 and i am working on it to improve item selection and deriving multiple item details.

To keep the program runnning all the time, I am using file storage system as the data items to store are singular in the first version.

For running the program at raspi bootup:

(Enter in terminal)
        
        sudo nano /etc/rc.local
        
(Scroll down, and just before the exit 0 line, enter the following code)

        python /home/pi/scrape.py &
        
#keywords
        #BeautifulSoup4  #SMTP  #RaspberryPi
