from time import sleep
import json 
import requests
from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QApplication, QDialog, QLineEdit, QTableView, QHeaderView, QGraphicsView, QGraphicsScene
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QPainter, QColor, QFont
from PyQt6.QtCore import QTimer
import sys 
from PyQt6 import uic
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import datetime

# --------------------------------------------------------------------------------------------------------- 
# These are the stylesheets to create the matrix like style of the app

styleSheet1 = """
            QDialog {
                background-color: #0d0d0d; /* Dark background for the dialog */
                color: #00FF41; /* Green text color */
                font-size: 24px; /* General font size */
            }

            QLabel {
                color: #00FF41; /* Green text for labels */
                font-weight: bold; /* Bold font for emphasis */
                font-size: 24px; /* Set font size for labels */
            }

            QLineEdit {
                background-color: #1e1e1e; /* Dark background for input fields */
                color: #00FF41; /* Green text color */
                border: 2px solid #00FF41; /* Green border */
                padding: 5px; /* Padding for input fields */
                font-size: 24px; /* Font size for input fields */
            }

            QLineEdit:focus {
                border: 2px solid #00FF41; /* Green border when focused */
                background-color: #0a0a0a; /* Slightly darker background when focused */
            }

            QPushButton {
                background-color: #1e1e1e; /* Dark button background */
                color: #00FF41; /* Green text color */
                border: 2px solid #00FF41; /* Green border for buttons */
                padding: 10px; /* Padding for buttons */
                border-radius: 5px; /* Rounded corners */
                font-size: 24px; /* Font size for buttons */
            }

            QPushButton:hover {
                background-color: #00FF41; /* Green background on hover */
                color: #1e1e1e; /* Dark text color on hover */
            }

            QPushButton:pressed {
                background-color: #0a0a0a; /* Darker background when pressed */
            }
        """


styleSheet2 = """
            QDialog {
                background-color: #0d0d0d; /* Dark background for the dialog */
                color: #00FF41; /* Green text color */
                font-size: 24px; /* General font size */
            }

            QLabel {
                color: #00FF41; /* Green text for labels */
                font-weight: bold; /* Bold font for emphasis */
                font-size: 24px; /* Set font size for labels */
            }

            QPushButton {
                background-color: #1e1e1e; /* Dark button background */
                color: #00FF41; /* Green text color */
                border: 2px solid #00FF41; /* Green border for buttons */
                padding: 10px; /* Padding for buttons */
                border-radius: 5px; /* Rounded corners */
                font-size: 24px; /* Font size for buttons */
            }

            QPushButton:hover {
                background-color: #00FF41; /* Green background on hover */
                color: #1e1e1e; /* Dark text color on hover */
            }

            QPushButton:pressed {
                background-color: #0a0a0a; /* Darker background when pressed */
            }

            QLineEdit {
                background-color: #1e1e1e; /* Dark background for input fields */
                color: #00FF41; /* Green text color */
                border: 2px solid #00FF41; /* Green border */
                padding: 5px; /* Padding for input fields */
                font-size: 24px; /* Font size for input fields */
            }

            QLineEdit:focus {
                border: 2px solid #00FF41; /* Green border when focused */
                background-color: #0a0a0a; /* Slightly darker background when focused */
            }
        """


styleSheet3 = """
            QDialog {
                background-color: #0d0d0d; /* Dark background for the dialog */
                color: #00FF41; /* Green text color */
                font-size: 24px; /* General font size */
            }

            QLabel {
                color: #00FF41; /* Green text for labels */
                font-weight: bold; /* Bold font for emphasis */
            }

            QLineEdit {
                background-color: #1e1e1e; /* Dark background for input fields */
                color: #00FF41; /* Green text color */
                border: 2px solid #00FF41; /* Green border */
                padding: 5px; /* Padding for input fields */
            }

            QLineEdit:focus {
                border: 2px solid #00FF41; /* Green border when focused */
                background-color: #0a0a0a; /* Slightly darker background when focused */
            }

            QPushButton {
                background-color: #1e1e1e; /* Dark button background */
                color: #00FF41; /* Green text color */
                border: 2px solid #00FF41; /* Green border for buttons */
                padding: 10px; /* Padding for buttons */
                border-radius: 5px; /* Rounded corners */
            }

            QPushButton:hover {
                background-color: #00FF41; /* Green background on hover */
                color: #1e1e1e; /* Dark text color on hover */
            }

            QPushButton:pressed {
                background-color: #0a0a0a; /* Darker background when pressed */
            }

            QTableView {
                background-color: #1e1e1e; /* Dark background for the table */
                color: #00FF41; /* Green text color for the table */
                border: none; /* Remove border */
            }

            QHeaderView {
                background-color: #1e1e1e; /* Dark background for headers */
                color: #00FF41; /* Green text for headers */
                border: none; /* Remove border from header */
            }

            QTableView::item {
                background-color: #1e1e1e; /* Dark background for table items */
                border: 1px solid #00FF41; /* Green border for table items */
            }

            QTableView::item:selected {
                background-color: #00FF41; /* Green background for selected items */
                color: #1e1e1e; /* Dark text color for selected items */
            }

            QTableView::item:hover {
                background-color: #00FF41; /* Highlight on hover */
                color: #1e1e1e; /* Dark text color on hover */
            }
        """
styleSheet4 = """
            QDialog {
                background-color: #0d0d0d; /* Dark background for the dialog */
                color: #00FF41; /* Green text color */
                font-size: 24px; /* General font size */
            }

            QLabel {
                color: #00FF41; /* Green text for labels */
                font-weight: bold; /* Bold font for emphasis */
            }

            QLineEdit {
                background-color: #1e1e1e; /* Dark background for input fields */
                color: #00FF41; /* Green text color */
                border: 2px solid #00FF41; /* Green border */
                padding: 5px; /* Padding for input fields */
            }

            QLineEdit:focus {
                border: 2px solid #00FF41; /* Green border when focused */
                background-color: #0a0a0a; /* Slightly darker background when focused */
            }

            QPushButton {
                background-color: #1e1e1e; /* Dark button background */
                color: #00FF41; /* Green text color */
                border: 2px solid #00FF41; /* Green border for buttons */
                padding: 10px; /* Padding for buttons */
                border-radius: 5px; /* Rounded corners */
            }

            QPushButton:hover {
                background-color: #00FF41; /* Green background on hover */
                color: #1e1e1e; /* Dark text color on hover */
            }

            QPushButton:pressed {
                background-color: #0a0a0a; /* Darker background when pressed */
            }

            QTableView {
                background-color: #1e1e1e; /* Dark background for the table */
                color: #00FF41; /* Green text color for the table */
                border: none; /* Remove border */
            }

            QHeaderView {
                background-color: #1e1e1e; /* Dark background for headers */
                color: #00FF41; /* Green text for headers */
                border: none; /* Remove border from header */
            }

            QTableView::item {
                background-color: #1e1e1e; /* Dark background for table items */
                border: 1px solid #00FF41; /* Green border for table items */
            }

            QTableView::item:selected {
                background-color: #00FF41; /* Green background for selected items */
                color: #1e1e1e; /* Dark text color for selected items */
            }

            QTableView::item:hover {
                background-color: #00FF41; /* Highlight on hover */
                color: #1e1e1e; /* Dark text color on hover */
            }
        """

# --------------------------------------------------------------------------------------------------------- 
# Defining some needed funcions 

def save_to_json(): # Function to save the users into a json file 
    with open("users.json", "w") as file:
        json.dump(users, file, indent=2)
    sleep(1)


def timer(self, button, base_text): # <- this function is for when someone click a button, for the button blink some message and after
    def change_text():              # 1.5 seconds, go back to the original text, for example, the button buy, when clicked will change 
        button.setText(base_text)   # the text to Success! and then go back to buy after 1.5 seconds
        self.timer.stop()

    self.timer = QTimer()
    self.timer.setInterval(1500)
    self.timer.timeout.connect(change_text)
    self.timer.start()

def get_crypto_prices(coin_id=None, days="1"):
    """
    Fetches either current prices or historical prices from CoinGecko API.
    If `coin_id` is provided along with `days`, fetches historical data for that coin.
    """
    if coin_id is None:
        # Fetch current market data
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 100,
            "page": 1,
            "sparkline": "false"
        }
    else:
        # Fetch historical market data for a specific coin
        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
        params = {
            "vs_currency": "usd",
            "days": days  # e.g., '30' for last 30 days
        }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao obter dados da API:", response.status_code)
        return []


def my_quit(): # <- my custom quit function to save before quitting
    save_to_json()
    quit()



def login(user, password):
    user_logged = None
    if not user or not password:
        return None
    if user in users and users[user]["password"] == password:
        print(f"Welcome {user}")
        user_logged = user
        sleep(1)
    else:
        print("Username or password incorrect")
    return user_logged

def register(user, password):
    if user not in users:
        users[user] = {"user": user, "password": password, "balance": 0, "cryptos": {}}
    else:
        print("Username alredy registered")
    return True

# --------------------------------------------------------------------------------------------------------- 
# Defining some variables that i'm gonna use soon

user_logged = None

prices = get_crypto_prices()
try:
    with open("users.json", "r") as file:
        users = json.load(file)
except:
    users = {}

cryptos_avaiable = [(crypto["id"], crypto["name"], crypto["current_price"]) for crypto in prices]



# --------------------------------------------------------------------------------------------------------- 

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui", self) # <- loading UI from the file login.ui
        self.setWindowTitle("Login page")

        self.setStyleSheet(styleSheet1)





        #--------------------------------------------------------------------------------- finding the parts of the UI
        self.login_button = self.findChild(QPushButton, "login_button")
        self.login_button.clicked.connect(self.handle_login)

        self.register_button = self.findChild(QPushButton, "register_button")
        self.register_button.clicked.connect(self.handle_register)

        self.quit_button = self.findChild(QPushButton, "quit_button")
        self.quit_button.clicked.connect(my_quit)
        

        self.name_input = self.findChild(QLineEdit, "name_input")
        self.password_input = self.findChild(QLineEdit, "password_input")
        
        #---------------------------------------------------------------------------------

    def handle_login(self):
        user, password = self.name_input.text().strip(), self.password_input.text().strip()
        global user_logged
        user_logged = login(user, password)
        if user_logged:
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        else:
            self.login_button.setText("User/password incorrect")
            timer(self, self.login_button, "Buy")
            

    def handle_register(self):
        user, password = self.name_input.text().strip(), self.password_input.text().strip()
        if register(user, password):
            self.register_button.setText("Success!")
        timer(self, self.register_button, "Register")
        
class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("mainWindowui.ui", self)
        self.setWindowTitle("Crypto simulator")

        self.setStyleSheet(styleSheet2)


        self.balance_text = self.findChild(QLabel, "balance_text")
        self.balance_text.setText(f"Actually you have {users[user_logged]["balance"]} dollars")
    
        self.balance_input = self.findChild(QLineEdit, "balance_input")

        self.button_1_balance = self.findChild(QPushButton, "button_1")
        self.button_1_balance.clicked.connect(self.add_to_balance)


        self.button_2_buy = self.findChild(QPushButton, "button_2")
        self.button_2_buy.clicked.connect(self.open_buy_window)

        self.button_3_sell = self.findChild(QPushButton, "button_3")
        self.button_3_sell.clicked.connect(self.open_sell_window)

        self.button_4_plot = self.findChild(QPushButton, "button_4")
        self.button_4_plot.clicked.connect(self.open_viewer_window)

        self.button_5_logout = self.findChild(QPushButton, "button_5")
        self.button_5_logout.clicked.connect(self.logout)

        self.button_6_quit = self.findChild(QPushButton, "button_6")
        self.button_6_quit.clicked.connect(my_quit)

        self.button_7_delete_account = self.findChild(QPushButton, "button_7")
        self.button_7_delete_account.clicked.connect(self.delete_account)
        

    def open_buy_window(self):
        self.buy_window = BuyWindow()
        self.buy_window.show()
        self.close()

    def open_sell_window(self):
        self.sell_window = SellWindow()
        self.sell_window.show()
        self.close()
    
    def open_viewer_window(self):
        self.plot_window = PlotWindow()
        self.plot_window.show()
        self.close()

    def logout(self):
        global user_logged
        user_logged = None 
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()


    def add_to_balance(self):
        try:
            money_to_add = int(self.balance_input.text())
            users[user_logged]["balance"] += money_to_add
            self.balance_text.setText(f"Actually you have {users[user_logged]["balance"]} dollars")
            self.balance_input.setText(f"Added {money_to_add} dollars")
            timer(self, self.balance_input, "")
        except ValueError:
            self.balance_input.setText(f"Error, Value Error")
            timer(self, self.balance_input, "")
        
    def delete_account(self):
        del users[user_logged]
        self.logout()

class PlotWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("plot.ui", self)
        self.setWindowTitle("Crypto simulator")

        self.setStyleSheet(styleSheet4)

        self.back_button = self.findChild(QPushButton, "back_button")
        self.back_button.clicked.connect(self.go_back)

        self.id_input = self.findChild(QLineEdit, "id_input")

        self.graph = self.findChild(QGraphicsView, "graphic")

        self.table = self.findChild(QTableView, "table")
        self.model = QStandardItemModel(len(cryptos_avaiable), 3)
        self.model.setHorizontalHeaderLabels(["ID", "Crypto", "Price"])

        for row, items in enumerate(cryptos_avaiable):
            for column, item in enumerate(items):
                self.model.setItem(row, column, QStandardItem(str(item)))

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        self.table.setModel(self.model)

        self.plot_button = self.findChild(QPushButton, "plot_button")
        self.plot_button.clicked.connect(self.plot_crypto_price_history)

    def plot_crypto_price_history(self):
        try:
            crypto_id = int(self.id_input.text()) - 1
            coin_id, crypto_name, _ = cryptos_avaiable[crypto_id]

            data = get_crypto_prices(coin_id=coin_id, days="30")
            
            if isinstance(data, dict) and "prices" in data:
                prices = data["prices"]
                
                dates = [datetime.datetime.fromtimestamp(price[0] / 1000) for price in prices]
                values = [price[1] for price in prices]

                fig, ax = plt.subplots()
                ax.set_facecolor("#0d0d0d")
                fig.patch.set_facecolor("#0d0d0d")
                ax.plot(dates, values, color="#00FF41", label=crypto_name)
                ax.set_title(f"{crypto_name} Price History (30 Days)", color = "#00FF41")
                ax.set_xlabel("Date", color = "#00FF41")
                ax.set_ylabel("Price (USD)", color = "#00FF41")
                ax.legend(facecolor="#00FF41", edgecolor="#00FF41")
                fig.autofmt_xdate()


                ax.tick_params(axis='x', colors="#00FF41")  
                ax.tick_params(axis='y', colors="#00FF41") 

                canvas = FigureCanvas(fig)
                self.graph.setScene(QGraphicsScene())
                self.graph.scene().addWidget(canvas)
            else:
                print("Error: Data format is incorrect or historical data not available.")

        except (IndexError, ValueError) as e:
            print(str(e))
        except KeyError:
            print("Error: Historical data not available.")


    def go_back(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()


class BuyWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("buy_sell.ui", self)
        self.setWindowTitle("Crypto simulator")
        self.setStyleSheet(styleSheet3)

        self.buy_button = self.findChild(QPushButton, "buy_sell_button")
        self.buy_button.setText("Buy")
        self.buy_button.clicked.connect(self.buy)

        self.back_button = self.findChild(QPushButton, "back_button")
        self.back_button.clicked.connect(self.go_back)

        self.id_input = self.findChild(QLineEdit, "id_input")

        self.amount_input = self.findChild(QLineEdit, "amount_input")


        self.table = self.findChild(QTableView, "table")
        self.model = QStandardItemModel(len(cryptos_avaiable), 3)
        self.model.setHorizontalHeaderLabels(["ID", "Crypto", "Price"])

        
        for row, items in enumerate(cryptos_avaiable):
            for column, item in enumerate(items):
                self.model.setItem(row, column, QStandardItem(str(item)))

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        self.table.setModel(self.model)

    def go_back(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def buy(self):
        try:
            coin_index = int(self.id_input.text()) - 1
            quantity = float(self.amount_input.text())
            _, crypto_name, crypto_price = cryptos_avaiable[coin_index]
            total_cost = crypto_price * quantity
            if users[user_logged]["balance"] >= total_cost:
                users[user_logged]["balance"] -= total_cost
                if crypto_name in users[user_logged]["cryptos"]:
                    users[user_logged]["cryptos"][crypto_name] += quantity
                else:
                    users[user_logged]["cryptos"][crypto_name] = quantity
                print(f"You bought {quantity} {crypto_name}(s)")
                self.buy_button.setText(f"Bought {quantity} {crypto_name}(s) for {total_cost}")
                timer(self, self.buy_button, "Buy")
            else:
                print("Insufficient balance")
                self.buy_button.setText("Insufficient balance")
                timer(self, self.buy_button, "Buy")
        except (ValueError, IndexError) as e:
            print(f"Error: {str(e)}")
            self.buy_button.setText("Invalid input")
            timer(self, self.buy_button, "Buy")
            
            

        
class SellWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("buy_sell.ui", self)
        self.setWindowTitle("Crypto simulator")

        self.setStyleSheet(styleSheet4)

        self.sell_button = self.findChild(QPushButton, "buy_sell_button")
        self.sell_button.setText("Sell")
        self.sell_button.clicked.connect(self.sell)

        self.back_button = self.findChild(QPushButton, "back_button")
        self.back_button.clicked.connect(self.go_back)

        self.id_input = self.findChild(QLineEdit, "id_input")

        self.amount_input = self.findChild(QLineEdit, "amount_input")

        self.table = self.findChild(QTableView, "table")
        self.crypto_list = users[user_logged]["cryptos"]
        self.model = QStandardItemModel(len(self.crypto_list), 2)
        self.model.setHorizontalHeaderLabels(["Crypto", "Quantity"])
        for row, (crypto_name, crypto_quantity) in enumerate(self.crypto_list.items()):
            self.model.setItem(row, 0, QStandardItem(str(crypto_name))) 
            self.model.setItem(row, 1, QStandardItem(str(crypto_quantity))) 

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        self.table.setModel(self.model)

    def go_back(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def sell(self):
        try:
            coin_index = int(self.id_input.text().strip()) - 1
            quantity = float(self.amount_input.text().strip())
            name_crypto, current_quantity = list(self.crypto_list.items())[coin_index]
            cripto_price = next((price for id, crypto, price in cryptos_avaiable if crypto == name_crypto), None)
            
            if cripto_price is None:
                print("Error: Cryptocurrency price not found.")
                return
            total_price = cripto_price * quantity
            
            if quantity <= current_quantity:
                users[user_logged]["cryptos"][name_crypto] -= quantity
                if users[user_logged]["cryptos"][name_crypto] == 0:
                    del users[user_logged]["cryptos"][name_crypto]
                
                users[user_logged]["balance"] += total_price 
                print(f"You sold {quantity} {name_crypto}(s) for ${total_price:.2f}")
                self.sell_button.setText(f"Sold {quantity} {name_crypto}(s) for ${total_price:.2f}")
                timer(self, self.sell_button, "Sell")
            else:
                print("Insufficient quantity to sell")
                self.sell_button.setText("Insufficient cryptos")
                timer(self, self.sell_button, "Sell")
        except (ValueError, IndexError) as e:
            print(f"Error: {str(e)}")
            self.sell_button.setText("Invalid input")
            timer(self, self.sell_button, "Sell")
        

app = QApplication(sys.argv)
login_window = LoginWindow()
login_window.show()
app.exec()
