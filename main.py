import time
import asyncio
import hcskr
import json

with open('config.json',encoding='UTF-8') as f:
    config = json.load(f)

async def check():
    await hcskr.asyncSelfCheck(config['name'],config['birth'],config['area'],config['schoolname'],config['schoolclass'],config['password'])

def command_check(option):
    if option == 'time' or 't':
        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)
        print(result)
    
while True:

    while True:

        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)
        option = input()
        command_check(option)

        if result == '12:01:15 PM':
            asyncio.get_event_loop().run_until_complete(check())
            print('자가진단 완료. ( 현재 시각 : {0} )'.format(result))
            break;
