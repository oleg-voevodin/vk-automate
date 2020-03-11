from random import randint as rt
from pickle import dump, load
from datetime import datetime
from time import sleep as slp
from vk_api import VkApi
import os

def exiting():
    print('Saving configs..')
    with open('config', 'wb') as config_file:
        dump(datetimes, config_file)
    print('Good luck!'); exit()

datetimes = []

login = input('Enter a VK login: ')
password = input('Enter a VK password: ')

vk_session = VkApi(login, password, app_id='2685278')
vk_session.auth()
vk = vk_session.get_api()

if not os.path.exists('config') or os.path.getsize('config') <= 10:
    os.system('type nul>config')
    print('Now we need to configure something.')
    while True:
        temp = []
        temp.append(input('Enter a task name: '))
        temp.append(input('Enter a time (in format HH:MM:SS), when you need to send the message: '))
        temp.append(vk.utils.resolveScreenName(screen_name=input('Enter a link of person, who you need to receive the message: ').split('/')[-1])['object_id'])
        temp.append(input('Enter the message for him:'))
        datetimes.append(temp)
        choice = input('User added. Do you want to add another one? (yes/no): ')
        if choice.lower() in 'no': break
        
else:
    with open('config', 'rb') as config_file:
        datetimes = load(config_file)

try:
    while True:
        for task in datetimes:
            # task[0] - task name, task[1] - time of executing, task[2] - user_id, task[3] - message
            if task[1] == datetime.now().time().strftime('%H:%M:%S'):
                vk.messages.send(user_id=task[2], random_id=rt(0, 131767), message=task[3])
                slp(1.5)

except KeyboardInterrupt:
    exiting()i

            
            
