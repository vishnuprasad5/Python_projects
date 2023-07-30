import mysql.connector
import random
import time


mydb = mysql.connector.connect(
       host= 'localhost',
       user ='root',
       password = 'root',
       port = 3306,
       database = 'bank')

mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM DATA_BASE')
data_base = mycursor.fetchall()

for i in data_base:
    print(i)

def main():
    print('\nAlready a user ? '
          '\n---------------'
          '\n1.  Yes'
          '\n2.  No ')
    op=int(input("""\nEnter option : """))
    if op == 2:
        sign_up()
    elif op == 1:
        login_func()
    else:
        print("Unsupported operation !! ")
        main()


def sign_up():
    print('\n <<<<< Sign Up >>>>> \n')
    global username
    username = input('Enter a Username: ')
    for u in data_base:
        if username == u[1]:
            print('\n Username already taken !! \n')
            sign_up()
    else:
        print(f'\n Username {username} available \n Generating PIN ......')
        time.sleep(2)
        global pin
        pin = random.randint(1000,9999)
        print(f'''\n\t\t Your PIN: {pin} \n        
Instructions
1. Keep your PIN confidential: Banks emphasize the importance of keeping your PIN confidential and not sharing it with anyone, including bank representatives, family members, or friends.
2. Memorize your PIN: Customers are advised to memorize their PIN and avoid writing it down or storing it in easily accessible places like wallets, phones, or diaries.
3. Change your PIN periodically: Banks may recommend customers to change their PIN periodically for added security. This practice helps guard against unauthorized access to the account.
4. Use secure ATMs and payment terminals: Customers are advised to use ATMs and payment terminals from reputable sources and to be cautious of skimming devices or suspicious activities that may compromise their PIN.
5. Cover the keypad when entering your PIN: To prevent shoulder surfing or hidden cameras from capturing your PIN, banks suggest covering the keypad with your hand or body while entering your PIN at ATMs or payment terminals.
6. Report any suspicious activity: If you suspect unauthorized access or suspicious activity related to your PIN or account, banks urge customers to report it immediately to their customer service or the bank's fraud hotline. 
                ''')
        details()


def details():
    f_name = input('First Name : ')
    l_name = input('Last Name : ')
    number = input('Phone Number : ')
    email = input('Email ID : ')
    balance = float(input('Deposit Amount : '))

    insert = f"""
                 INSERT INTO DATA_BASE (USERNAME , PIN, FIRST_NAME, LAST_NAME, PHONE_NO, EMAIL_ID, BALANCE) VALUES
                 ('{username.lower()}', {pin}, '{f_name}', '{l_name}', {number}, '{email}', {balance})
              """
    mycursor.execute(insert)
    print(f'\n SIGN UP Successful, Log in again !! \n')

    mydb.commit()
    mydb.close()
    exit()



def login_func():
    print('\n <<<<<<< Login >>>>>>>>> \n')
    global x
    x = input('Enter your username: ' )
    y = int(input('Enter your PIN: '))
    for u in data_base:
        if u[1] == x and u[2] != y or u[1] != x and y == u[2]:
            print('''
            Incorrect username or password !!
            ''')
            login_func()
        elif u[1] == x and u[2] == y:
            print(f''' \n\t\t <^> Hello {u[3]+" "+u[4]} <^> \n''')
            option_selector()


def option_selector():
    print('Select an option'
          '\n----------------'
          '\n1. Transactions'
          '\n2. Account Details'
          '\n3. Log out')
    os = int(input('Enter your option: '))
    if os == 1:
        transactions()
    elif os == 2:
        account_details()
    elif os == 3:
        log_out()
    else:
        print('Wrong command !!')
        option_selector()


def transactions():
    print('\nSelect your Transaction'
          '\n-----------------------'
          '\n1. Withdrawal'
          '\n2. Deposit '
          '\n3. Check Balance'
          '\n4. Back ')
    t = int(input('Enter your option : '))
    if t == 1:
        withdrawal()
    elif t == 2:
        deposit()
    elif t == 3:
        balance()
    elif t == 4:
        option_selector()


def withdrawal():
    withdraw = int(input('Enter your Amount: '))
    for u in data_base:
        if x == u[1] and withdraw > u[7]:
            print('insufficient amount !! ')
            withdrawal()
        if x == u[1] and withdraw < u[7]:
            print('\nProcessing...... \n')
            time.sleep(5)
            print(''' \n\t\t <^ Cash withdrawn successfully !! ^> \n''')
            withdrawal_balance = u[7] - withdraw

            update_wb = (f"""UPDATE DATA_BASE SET BALANCE = {withdrawal_balance} WHERE USERNAME='{x}' """)
            mycursor.execute(update_wb)

            mydb.commit()
            mydb.close()

            print('\n---- Would you like to see your balance ? ---- \n1. Yes \n2. No \n')
            b1 = int(input('Enter your option : '))
            if b1 == 1:
                print(f'Balance: ₹ {withdrawal_balance}')
                print('Thank you :)')
            if b1 == 2:
                print('Thank you :)')


def deposit():
    deposit = int(input('Enter your Amount: '))
    for u in data_base:
        if x == u[1] :
            print('\nCounting your cash..... \n')
            time.sleep(5)
            deposit_balance = u[7] + deposit

            update_db = (f""" UPDATE DATA_BASE SET BALANCE = {deposit_balance} WHERE USERNAME='{x}' """)
            mycursor.execute(update_db)

            mydb.commit()
            mydb.close()

            print('\n\t\t <^ Cash deposited successfully !! ^> \n ')
            print('\n---- Would you like to see your balance ? ---- \n1. Yes \n2. No \n')
            b1 = int(input('Enter your option : '))
            if b1 == 1:
                print(f'Balance: ₹ {deposit_balance}')
                print('\nThank you :)')
                if b1 == 2:
                    print('\nThank you :)')


def balance():
    for u in data_base:
        if x == u[1]:
            print('Balance : ₹', u[7])
            print('\nThank you :)')
    print('\nPress 1 for Back \n ')
    int(input('Enter option: '))
    transactions()


def account_details():
    for u in data_base:
        if x == u[1]:
            print(f'\nAccount details'
                  f'\n---------------'
                  f'\nA/C No   : {u[0]}'
                  f'\nUsername : {u[1]}'
                  f'\nName     : {u[3]+ " "  + u[4]}'
                  f'\nEmail Id : {u[6]}'
                  f'\nPhone No : {u[5]}'
                  f'\nBalance  : {u[7]}')

            print('\nPress 1 for Back')
            int(input('Enter option: '))
            option_selector()


def log_out():
    print('Logged out successfully !!')
    exit()

main()