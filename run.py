import os
import time
import random



while True:
    input1 = input("\n1. Whatstapp Web\n2. Whatstapp android\n\n\n=> ")
    if input1 == '1':
        provider = input("\nCth: \nTelkomsel 13\nIndosat 57\nTri 96\n\n => ")
        a = int(input("\Banyaknya ? => "))
        os.system('clear')
        for i in range(a):
            data1 = random.randint(1234,5678)
            data2 = random.randint(2345,6789)
            x = "https://web.whatsapp.com/send/?phone=628{}{}{}&text&type=phone_number&app_absent=0".format(provider,data1,data2)
            print(x)
            time.sleep(0.5)
        exit()
    elif input1 == '2':
        provider1 = input("\nCth: \nTelkomsel 13\nIndosat 57\nTri 96\n\n => ")
        b = int(input("\Banyaknya ? => "))
        os.system('clear')
        for i in range(b):
            data3 = random.randint(1234,5678)
            data4 = random.randint(2345,6789)
            y = "wa.me/628{}{}{}".format(provider1,data3,data4)
            print(y)
            time.sleep(0.5)
        exit()
    else:
        exit()




