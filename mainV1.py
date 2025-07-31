# Arthur van Poecke Submission(draft 1)

import os, time

aircraftlist = []
airportslist = []
UKcode = None
Intcode = None
distance1 = None
type1 = None
costperseat1 = None
range1 = None
capacity1 = None
minfirstclass1 = None
user_input31 = None
standardclass1 = None
pofs = None
poss = None
InternationalName = None
Mainwhileloop = True

def check(var):
    return bool(var)

def extractdata():
    fp = open(r'Flight Planner\aircraft.csv', 'r')
    fp1 = open(r'Flight Planner\airports.csv', 'r')
    for line in fp:
        line = line.strip('\n')
        aircraft = line.split(',')  
        aircraftlist.append(aircraft)
    for line in fp1:
        line = line.strip('\n')
        airports = line.split(',')
        airportslist.append(airports)
    fp.close()

def display_menu():
    os.system('cls')
    print('|----------------------------------------|')
    print('|Flight planning profitability calculator|')
    print('|----------------------------------------|')
    print('|Options                                 |')
    print('|-------                                 |')
    print('|1. Enter airport details                |')
    print('|2. Enter flight details                 |')
    print('|3. Enter Price Plan                     |')
    print('|4. Calculate Profit                     |')
    print('|5. Clear data                           |')
    print('|6. Quit                                 |')
    print('|----------------------------------------|')

def Option1():
    Whileloop = True
    global UKcode
    global Intcode
    global distance1
    global InternationalName
    while Whileloop:
        user_input = input('Enter UK airport code:').strip().lower() 
        if user_input not in ['lpl', 'boh']:
            print('User Input was not one of the eligible codes (LPL or BOH), please try again')
            display_menu()
            return
        UKcode = user_input
        print(f'UK Airport Code: {UKcode.upper()}')
        user_input1 = input('Enter overseas airport code: ').strip().upper()
        Intcode = user_input1
        match = None
        for row in airportslist:
            code = row[0].strip()
            if user_input1 == code:
                match = row
        if match:
            code = match[0]
            name = match[1]
            if user_input == 'lpl':
                distance = int(match[2])  
                distance1 = distance
            elif user_input == 'boh':
                distance = int(match[3])  
                distance1 = distance
            print(f"Airport\n-------\nCode: {code}\nName: {name}\nDistance to {user_input.upper()}: {distance}KM")
            InternationalName = name
            user_input79 = input('Have you selected the correct flight route?').lower().strip()
            if user_input79 == 'yes':
                Whileloop = False
                display_menu()
                return
            else:
                UKcode = None
                Intcode = None
                InternationalName = None
                distance1 = None
        else:
            print("No airport found.")
            display_menu()
            return

def Option2():
    Whileloop = True
    Whileloop1 = True
    global type1
    global costperseat1
    global capacity1
    global range1
    global minfirstclass1
    global user_input31
    global standardclass1
    while Whileloop:
        user_input2 = input('Enter the desired aircraft model:').lower()
        match1 = None
        for row in aircraftlist:
            aircraft_type = row[0]
            if user_input2 == aircraft_type:
                match1 = row 
        if match1: 
            aircraft_type = match1[0]
            costperseat = int(match1[1])       
            range = int(match1[2])             
            capacity = int(match1[3])          
            minfirstclass = int(match1[4])     
            if range > int(distance1):         
                print(f'Aircraft\n--------\nType: {aircraft_type}\nCost per seat per 100KM: {costperseat}\nRange: {range}KM\nCapacity if all seats standard class: {capacity}\nMinimum first class seats: {minfirstclass}')
            else:
                print(f'Aircraft range is too small for the selected trip. Please choose another aircraft.')
                display_menu()
                return
            type1 = aircraft_type
            costperseat1 = costperseat
            range1 = range
            capacity1 = capacity
            minfirstclass1 = minfirstclass
            user_input79 = input('Have you selected the correct aircraft type? ').lower().strip()
            if user_input79 == 'yes':
                Whileloop = False
            else:
                type1 = None
                costperseat1 = None
                capacity1 = None
                range1 = None
                minfirstclass1 = None
        else:
            print('Aircraft type not found')
            display_menu()
            return
    while Whileloop1:
        user_input3 = int(input('Enter the number of first class seats:'))
        halfcapacity = 1/2 * capacity1
        if user_input3 < minfirstclass1:
            print(f'Not enough first class seats. Minimum is {minfirstclass1}')
            display_menu()
            return
        elif user_input3 > halfcapacity:
            print(f'Too many first class seats, the maximum is {halfcapacity} ')
            display_menu()
            return
        standardclass29 = user_input3 * 2
        standardclass = capacity1 - standardclass29
        print(f'Number of First Class Seats: {user_input3}')
        print(f'Number of Standard Class Seats: {standardclass}')
        user_input31 = user_input3
        standardclass1 = standardclass
        user_input81 = input('Have you selected the correct numbers? ').strip().lower()
        if user_input81 == 'yes':
            Whileloop1 = False
            display_menu()
            return
        else:
            user_input31 = None
            standardclass1 = None

def Option3():
    whileloop = True
    global pofs
    global poss
    while whileloop:
        user_input4 = float(input('Enter the price per first class seat:'))  
        user_input5 = float(input('Enter the price per standard class seat:'))  
        pofs = user_input4
        poss = user_input5
        print(f'Price per first class seat selected is £{pofs}')
        print(f'Price per standard class seat selected is £{poss}')
        user_input81 = input('Have you entered the correct numbers?').lower().strip()
        if user_input81 == 'yes':
            whileloop = False
            display_menu()
            return
        else:
            pofs = None
            poss = None

def Option4():
    WhileLoop = True
    required_data = {
        'UKcode': (UKcode, 'Option 1'),
        'Intcode': (Intcode, 'Option 1'),
        'distance1': (distance1, 'Option 1'),
        'type1': (type1, 'Option 2'),
        'costperseat1': (costperseat1, 'Option 2'),
        'range1': (range1, 'Option 2'),
        'capacity1': (capacity1, 'Option 2'),
        'minfirstclass1': (minfirstclass1, 'Option 2'),
        'user_input31': (user_input31, 'Option 2'),
        'standardclass1': (standardclass1, 'Option 2'),
        'pofs': (pofs, 'Option 3'),
        'poss': (poss, 'Option 3')
    }
    missing_options = {page for value, page in required_data.values() if not check(value)}
    if not missing_options:
        print('All Values have been inputted')
        os.system('cls')
    else:
        print('Some data values are missing.')
        for option in sorted(missing_options):
            print(f'Please go to {option} and answer the questions.')
        time.sleep(2)
        display_menu()
        return
    distance2 = distance1 / 100
    costperseattotal = costperseat1 * distance2
    numofseats = user_input31 + standardclass1
    flightcost = costperseattotal * numofseats
    standardclassincome = poss * standardclass1
    firstclassincome = pofs * user_input31
    flightincome = standardclassincome + firstclassincome
    flightprofit = flightincome - flightcost
    if UKcode == 'lpl':
        UKairportname = 'Liverpool John Lennon Airport'
    elif UKcode == 'boh':
        UKairportname = 'Bournemouth Airport'
    print(f'Flight Information')
    print(f'------------------')
    print(f'UK Airport: {UKcode.upper()}, {UKairportname}')
    print(f'International Airport: {Intcode}, {InternationalName} Airport')
    print(f'Distance: {distance1} Kilometres')
    print(f'Type of Aircraft: {type1}')
    print(f'Maximum flight range: {range1} Kilometres')
    print(f'Running cost per seat per 100Km: £{costperseat1}')
    print(f'Capacity if all seats are standard class: {capacity1}')
    print(f'Number of first-class seats: {user_input31}')
    print(f'Number of standard-class seats: {standardclass1}')
    print(f'Price of a standard-class seat: £{poss}')
    print(f'Price of a first-class seat: £{pofs}')
    print(f'Flight cost per seat: £{costperseattotal}')
    print(f'Flight cost: £{flightcost}')
    print(f'Flight income: £{flightincome}')
    print(f'Flight profit: £{flightprofit}')
    while WhileLoop:
        user_input5 = input('Would you like to return to the main menu').lower().strip()
        if user_input5 == 'yes':
            WhileLoop = False
            display_menu()
        elif user_input5 == 'no':
            print('Take all the time you need')
        else:
            print('please print yes or no')

def Option5():
    global UKcode
    global Intcode
    global distance1
    global type1
    global costperseat1
    global range1
    global capacity1
    global minfirstclass1
    global user_input31
    global standardclass1
    global pofs
    global poss
    UKcode = None
    Intcode = None
    distance1 = None
    type1 = None
    costperseat1 = None
    range1 = None
    capacity1 = None
    minfirstclass1 = None
    user_input31 = None
    standardclass1 = None
    pofs = None
    poss = None
    print('All data has now been cleared')
    time.sleep(1)
    os.system('cls')
    display_menu()

def Option6():
    global Mainwhileloop
    os.system('cls')
    user_input6 = input('Are you sure you would like to quit?').lower().strip()
    if user_input6 == 'yes':
        print('Quitting program now')
        time.sleep(1)
        os.system('cls')
        Mainwhileloop = False
    else: 
        os.system('cls')
        display_menu()

def Selection():
    while Mainwhileloop:
        selection = input('Select option:')
        if selection == '1':
            os.system('cls')
            Option1()
        elif selection == '2':
            os.system('cls')
            Option2()
        elif selection == '3':
            os.system('cls')
            Option3()
        elif selection == '4':
            os.system('cls')
            Option4()
        elif selection == '5':
            os.system('cls')
            Option5()
        elif selection == '6':
            os.system('cls')
            Option6()
        else:
            print('Invalid Option, please select again')

def run():
    extractdata()
    display_menu()
    Selection()

run()






