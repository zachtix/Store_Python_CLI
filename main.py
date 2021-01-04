import sqlite3
import time
# Module
import manage_store
import cashier
# Module

n = 1

while n > 0:
    print('What do you want?')
    print('[1]Manage Store')
    print('[2]Cashier')
    print('[3]Exit')

    want = int(input())

    if want == 1:
        manage_store.menu()
    if want == 2:
        cashier.calculate()
    if want == 3:
        time.sleep(0.2)
        n = -1
        print('Exit Program')
        
