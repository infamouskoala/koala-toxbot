import requests

url = "https://discord.com/api/v9/reporting/message"
file = open("account.txt","r")
tokens = file.read().splitlines()
sagian_sucks_dick = []  # USS CAN SUCK MY DICK SAGIAN THE DICKRIDER NEVER GETS ANYTHING DONE HIMSELF

black = "\033[1;30m"
red = "\033[1;31m"    
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"    
purple = "\033[1;35m"    
cyan = "\033[1;36m"    
white = "\033[1;37m"   

print(f"""{blue} ____  __.           .__       ___________           
|    |/ _|_________  |  | _____\__    ___/______  ___
|      < /  _ \__  \ |  | \__  \ |    | /  _ \  \/  /
|    |  (  <_> ) __ \|  |__/ __ \|    |(  <_> >    < 
|____|__ \____(____  /____(____  /____| \____/__/\_ |
        \/         \/          \/                  \/{white}""")
channel = int(input("Channel ID: "))
msgid = int(input("Message ID: "))
guildid = int(input("Server ID: "))
reason = input("Reason: ")

# HEIL AOS, DEATH TO SAGIAN

for fagian in tokens:
    print(f"{yellow}[+ KOALA TOXXER +]{white}{fagian} is trying to report..")

    # headers
    sagian_gave_me_head = {
        "Authorization" : fagian
    }
    # payload
    sagian_never_paid_for_my_shit = {
        "channel_id": channel, 
        "message_id": msgid, 
        "guild_id": guildid, 
        "reason" : reason,
        "elements": {},
        "name":"message",
        "version":"1.0"
    }
    r = requests.post('https://discord.com/api/v9/report', headers=sagian_gave_me_head, json=sagian_never_paid_for_my_shit)
    if r.status_code == 200:
        print(f"{green}[+ KOALA TOXXER +]{white}{fagian} Reported the message!")
    else:
        print(f"{red}Something broke, status code: {r.status_code}{white}")

print(f"{cyan}[!]{white} Reported successfully.")
# FUCK SAGIAN, SAGIAN IS NOTHING BUT A DICKRIDER WHO RIDES FOR CLOUT.
# RODE ME, RODE 707, RODE NINOV AND NOW RIDING SYRA. HAVE SOME FUCKING SHAME U FUCKING FAGGOT