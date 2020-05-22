blockchain = []



def add_list():

   blockchain.append(3.2)

   print(blockchain)



add_list()

add_list()

add_list()


element1 = input("Give the first element of the blockchain ")

blockchain = [element1]

def add_list():

   blockchain.append([blockchain[-1], 3.2])

   print(blockchain)



add_list()

add_list()

add_list()
# the above is some BS, and I need to learn why my code dont work as intended

blockchain = []
def get_last_value():
    """extracting the last element of the blockchain list"""
    return(blockchain[-1])

def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])

def get_transaction_value():
    user_value = float(input('Enter your transaction amount'))
    return user_value

def get_user_choice():
    user_input = input("Please give your choice here:")
    return user_input

def print_block():
    for block in blockchain:
        print("Here is your block")
        print(block)

def verify_chain():
    index = 0
    valid = True
    for block in blockchain:
        if index == 0:
            index += 1
            continue
        elif block[0] == blockchain[index -1]:
            valid = True
        else:
            valid = False
            break
        index += 1
    return valid

tx_amount = get_transaction_value()
add_value(tx_amount)

while True:
    print("Choose an option")
    print('Choose 1 for adding a new transaction')
    print('Choose 2 for printing the blockchain')
    print('Choose 3 if you want to manipulate the data')
    print('Choose anything else if you want to quit')

    user_choice = get_user_choice()

    if user_choice == "1":
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_value())

    elif user_choice == "2":
        print_block()

    elif user_choice == "3":
        if len(blockchain) >= 1:
            blockchain[0] = 2

    else:
        break

    if not verify_chain():
        print('Blockchain manipulated')
        break
