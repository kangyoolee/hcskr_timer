import time
import asyncio
import hcskr
import json
import os

with open('/Users/kangyoolee/OneDrive/코딩/hcskr_timer/config.json',encoding='UTF-8') as f:
    config = json.load(f)

async def check():
    await hcskr.asyncSelfCheck(config['name'],config['birth'],config['area'],config['schoolname'],config['schoolclass'],config['password'])

def command_check(option):
    if option == 'time' or option == 't':
        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)
        print(result)
    elif option == 'status' or option == 's':
        print(
f'''이름 : {config['name']}
생년월일 : {config['birth']}
지역 : {config['area']}
학교이름 : {config['schoolname']}
학교구분 : {config['schoolclass']}
비밀번호 : {config['password']}
알람시간 : {config['time']}''')
    elif option == 'stop':
        print('프로그램을 종료하시겠습니까? ( Y / n )')
        a = str(input())
        if a == 'Y' or a == 'y' or a == 'yes':
            print('프로그램을 종료하겠습니다.')
            exit()
        else:
            print('Abort.')
    else:
        print('존재하지 않는 명령어 입니다.')

print(f'''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Made by Kangyoo Lee ( https://github.com/kang309 )
이 프로그램은 hcskr 자가진단 라이브러리를 이용해 만들었습니다. ( https://github.com/331leo/hcskr_python )
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''+
f'''
이름 : {config['name']}
생년월일 : {config['birth']}
지역 : {config['area']}
학교이름 : {config['schoolname']}
학교구분 : {config['schoolclass']}
비밀번호 : {config['password']}
알람시간 : {config['time']}
다음 내용으로 프로그램을 실행하시겠습니까? ( Y / n )''',end = ' ')

answer = input()
if answer == 'Y' or answer == 'y' or answer == 'yes':
    print(
'''
프로그램을 실행하겠습니다!
''')
    
    print(
'''~~~~~~~~~~~< 사용법 >~~~~~~~~~~~
time 또는 t 입력 -> 현재시간 출력
status 또는 s 입력 -> 설정내용 출력
stop 입력 -> 프로그램 종료
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
    while True:

        while True:

            localtime = time.localtime()
            result = time.strftime("%I:%M:%S %p", localtime)

            if result == config['time']:
                asyncio.get_event_loop().run_until_complete(check())
                print('자가진단 완료. ( 현재 시각 : {0} )'.format(result))
                break;
            
            print('>>>',end=' ')
            option = str(input())
            command_check(option)

else:
    print('Abort.')


