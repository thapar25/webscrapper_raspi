import requests
import smtplib
import time
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/Logitech-G102-Customizable-Lighting-Programmable/dp/B08LT9BMPP/ref=sr_1_3_mod_primary_lightning_deal?dchild=1&keywords=logitech+g102+lightsync+gaming+mouse&qid=1613138146&sbo=Tc8eqSFhUl4VwMzbE4fw%2Fw%3D%3D&smid=A14CZOWI0VEHLG&sr=8-3'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}

page=requests.get(URL,headers=headers)    
soup=BeautifulSoup(page.content,'html.parser')

def fetch_val():
    title=soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
   
    val=(price[2]+price[4:7])
    print (val)
    compare(val)
    

def compare(val):
    file1 = open('price.txt', 'r')
    prev_val=file1.read()

    #print (prev_val)
    
    
    prev_val.split()
    x=int(prev_val)
    y=int(val)
    if(y<x):
        print("changing value...")
        change(val)
        sendmail(val)
        

    file1.close()

def change(val):
     file1=open('price.txt', 'w+')
     new_val=val 
     file1.write(new_val)
     
     file1.close()

def sendmail(val):
    email = '#your_email'
    password = '#your_email_password'
    send_to_email ='#recipient_email'
    message = 'The value dropped to INR :\t' + val + '\n\n\n'+'[Sent from Rasberry Pi]'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    
    server.starttls()  
    server.login(email, password)  
    print('Sending email...')
    server.sendmail(email, send_to_email, message)
    server.quit()  
    print('Email Sent!')


while(1>0):
    fetch_val()

    time.sleep(86400)


