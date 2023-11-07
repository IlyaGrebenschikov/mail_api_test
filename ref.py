import requests
import sys


user = input()

def get_domain():
    page = 1
    domain_url = requests.get(f'https://api.mail.gw/domains?page={page}').json()

    for status in domain_url['hydra:member']:
        while True:
            if status['isActive']:
                domain_log = status['domain'] 
                  
                return domain_log
            
            else:
                page += 1
                domain_url = requests.get(f'https://api.mail.gw/domains?page={page}').json()
                continue
            

domain = get_domain()
            
def create_account_logpass(login=str(input()), pass_1=str(input())) -> dict:
        log_pass = {
            'address': str(login) + '@' + str(domain),
            'password': str(pass_1),
        }
                
        return log_pass
    
        
log_pass = create_account_logpass()   
     
def create_account():
        accounts_url = 'https://api.mail.gw/accounts'
        resp_account = requests.post(accounts_url, json=log_pass)
            
        return resp_account
    

account = create_account()  

def get_token():
    token_url = 'https://api.mail.gw/token'
    resp_token = requests.post(token_url, json=log_pass)
        
    return resp_token


token = get_token()

def get_arr_messages():
    auth = {
        'Authorization': f'Bearer {token.json()["token"]}'
    }
    url = requests.get('https://api.mail.gw/messages?page=1', headers=auth)
    
    
    return url.json()

all_messages = get_arr_messages()


while True:
    if user == 'account':
        print(account, log_pass)
        user = input()
        continue
    
    if user == 'token':
        print(token)
        user = input()
        continue
    
    if user == 'messages':
        if get_arr_messages()['hydra:totalItems'] > 0:
            for k in get_arr_messages()['hydra:member']:
                print(k['intro'])
        else:
            print('try again')
            user = input()
            continue      
            
        print(get_arr_messages())
        user = input()
        continue
    
    if user == 'exit':
        sys.exit()
