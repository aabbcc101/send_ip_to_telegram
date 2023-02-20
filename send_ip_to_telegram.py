# U can check and get your new dynamic ip this way after rebooting your router 
# It can be useful when you don't possess a static one

import requests
import time

def send_telegram(text: str):
    token = "5751913776:YOUR_TOKEN_MUST_BE_HERE"
    url = "https://api.telegram.org/bot"
    
    # who gets the channel id
    #https://api.telegram.org/bot5751913776:YOUR_TOKEN_MUST_BE_HERE/getUpdates
    channel_id = "-1001numbers7202"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })

    if r.status_code != 200:
        raise Exception("post_text error")


def sheduler_ip(last_ip):
    url_ip =  "https://ifconfig.co/ip"
    url_country =  "https://ifconfig.co/country"
    
    try:
        request_ip = requests.get(url_ip)
        if request_ip.status_code != 200:
            return last_ip
        new_ip_text = request_ip.text 
        
        request_country  = requests.get(url_country)
        
        if request_country.status_code != 200:
            return last_ip
        
        if new_ip_text != last_ip:
            send_telegram("The new ip has been gotten. CITADELDEVELOP is " + new_ip_text + " The country is " + request_country.text)
            return new_ip_text
        else:              
            return last_ip
               
        
    except Exception as e:  # This is the correct syntax
        return last_ip
                
if __name__ == '__main__':
    ip = '0.0.0.0'
    while 1:
        ip = sheduler_ip(ip)
        time.sleep(300) #5



