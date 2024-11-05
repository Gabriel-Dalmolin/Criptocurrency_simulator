from time import sleep
import json 
import requests

def save_to_json(): # Function to save the users into a json file 
    with open("users.json", "w") as file:
        json.dump(users, file, indent=2)
    sleep(1)


ids = "bitcoin,ethereum,solana,cardano,tether,binancecoin,ripple,dogecoin,shiba-inu,polkadot,litecoin" # The coins ids 

def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ids,  
        "vs_currencies": "usd"       
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

prices = get_crypto_prices()
try:
    with open("users.json", "r") as file:
        users = json.load(file)
except:
    users = {}

cryptos_avaiable = [(name, prices[name]["usd"]) for name in prices]

user_logged = None
running = True
while running:
    if not user_logged:
        print("-"*150)
        print("What do you want to do?")
        print("1 - Log into your account")
        print("2 - Create an account")
        print("3 - Quit")
        print("-"*150)
        action = input().replace(" ", "")

        if action == "1":
            print("print your user and then your password separated by one comma")
            inp = input()
            try: user, password = inp.split(","); user = user.strip(); password = password.strip()
            except ValueError: print("You should input 2 values separated by a comma, your name, and then your password");sleep(1);continue

            if user in users and users[user]["password"] == password:
                print("You logged in")
                user_logged = user
                sleep(1)
            else:
                print("Username or password incorrect")
        elif action == "2":
            print("print your user and then your password separated by one comma")
            inp = input()
            try: user, password = inp.split(","); user = user.strip(); password = password.strip()
            except ValueError: print("You should input 2 values separated by a comma, your name, and then your password");sleep(1);continue

            if user not in users:
                users[user] = {"user": user, "password": password, "balance": 0, "cryptos": {}}
            else:
                print("Username alredy registered")
        elif action == "3":
            save_to_json()
            quit()
        else:
            print("\nError, action not identified")
            sleep(1)
    else: 
        print("-"*150)
        print("What do you want to do?")
        print("1 - Add balance")
        print("2 - Buy crypto")
        print("3 - Sell crypto")
        print("4 - See balance")
        print("5 - Leave account")
        print("6 - Quit")
        print("-"*150)
        action = input().replace(" ", "")

        if action == "1":
            print("\nHow much do you want to add?")
            money_added = float(input().strip())
            users[user_logged]["balance"] += money_added
            print(f"Money added, now you have {users[user_logged]['balance']} available")


        elif action == "2":
            print("\n" + "-"*150)
            for num, crypto in enumerate(cryptos_avaiable):
                name_crypto, crypto_price = crypto
                print(f"{num} - {name_crypto}: {crypto_price}")
            print("-"*150, "\n")
            print("Type the number of the crypto you want to buy and the amount separated by a comma or print quit to go back")
            inp = input().replace(" ","")
            if inp.lower() == "quit":
                continue
            
            try: coin_index, quantity = inp.split(","); coin_index, quantity = int(coin_index), float(quantity)
            except ValueError: print("Error, you should input 2 values, and them should only be numbers and one comma");sleep(1);continue
            if coin_index >= len(cryptos_avaiable):
                print("the coin that you selected doesn't exist")
                continue


            crypto_name, crypto_price = cryptos_avaiable[coin_index]
            total_cost = crypto_price * quantity

            if users[user_logged]["balance"] >= total_cost:
                users[user_logged]["balance"] -= total_cost
                if crypto_name in users[user_logged]["cryptos"]:
                    users[user_logged]["cryptos"][crypto_name] += quantity
                else:
                    users[user_logged]["cryptos"][crypto_name] = quantity
                print(f"You bought {quantity} {crypto_name}(s)")
            else:
                print("Insufficient balance")


        elif action == "3":
            print("\n" + "-"*150)
            crypto_list = list(users[user_logged]["cryptos"].items())
            for num, (name_crypto, quantity) in enumerate(crypto_list):
                print(f"{num} - {name_crypto}: {quantity}")
            print("-"*150, "\n")
            print("Type the number of the crypto you want to sell and the amount separated by a comma or print quit to go back")
            inp = input().replace(" ","")
            if inp.lower() == "quit":
                continue

            try: coin_index, quantity = inp.split(","); coin_index, quantity = int(coin_index), float(quantity)
            except ValueError: print("Error, you should input 2 values, and them should only be numbers and one comma");sleep(1);continue
            if coin_index >= len(users[user_logged]["cryptos"]):
                print("the coin that you selected doesn't exist")
                continue
            name_crypto, current_quantity = crypto_list[coin_index]


            if quantity <= current_quantity:
                users[user_logged]["cryptos"][name_crypto] -= quantity
                if users[user_logged]["cryptos"][name_crypto] == 0:
                    del users[user_logged]["cryptos"][name_crypto]
                
                cripto_price = 0
                for  crypto, price in cryptos_avaiable:
                    if crypto == name_crypto:
                        cripto_price = price
                total_price = cripto_price * quantity
                users[user_logged]["balance"] += total_price 
                print(f"You sold {quantity} {name_crypto}(s) for {total_price}")
            else:
                print("Insufficient quantity to sell")
        
        elif action == "4":
            print(("-"*50)+"\n"+"balance:",str(users[user_logged]["balance"])+"\n"+("-"*50))
            sleep(0.5)


        elif action == "5":
            print("Logging out")
            user_logged = None
            sleep(1)

        elif action == "6":
            print("\nGoodbye")
            sleep(1)
            save_to_json()
            quit()

        else:
            print("Error, action not identified")


