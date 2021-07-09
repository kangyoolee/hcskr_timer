import time

while True:
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)

    if result == '12:09:00 AM':
        print('완성!')
        break;