import socket
import tkinter as tk
from datetime import datetime
from time import sleep
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

now = datetime.now()

# driver = webdriver.Chrome(executable_path="/home/aydinnyunus/Downloads/Birthday-master/chromedriver")

#Keep the current chrome session
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=./User_Data')

master = tk.Tk()
master.title("Whatsapp Bot")
width = 500
height = 700
canvas1 = tk.Canvas(master, width=width, height=height, relief='raised', bg='white')
canvas1.pack()
# load the .gif image file
# canvas1.create_line(15, 25, 200, 25)
canvas1.create_line(width / 2, 0, width / 2, height, dash=(4, 2))
canvas1.create_line(800, height / 2, 0, height / 2, dash=(4, 2))

cx = canvas1.canvasx(width / 2)
cy = canvas1.canvasy(height / 2)
cid = canvas1.find_closest(cx, cy)[0]
canvas1.itemconfigure(cid, fill="blue")

# canvas1.create_line(55, 85, 155, 85, 105, 180, 55, 85)
# canvas1.create_text(400, 10, fill="black", font="Times 20 italic bold",
#                  text="Whatsapp Bot")
gif1 = tk.PhotoImage(file='images/GZd3Pv.png')
# gif2 = tk.PhotoImage(file='images/9022c3da331305796ded3dda4c619df0.png')

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
#canvas1.create_image(400, 350, image=gif2)

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas1.create_image(width / 2, height / 2, image=gif1)


# label1 = tk.Label(master, text='Whatsapp Bot')
# label1.config(font=('helvetica', 14))
# canvas1.create_window(200, 25, window=label1)
def blueSelection(event=None):
    l1 = tk.Label(master,
                  text="Enter the Message ", bg="blue")
    l2 = tk.Label(master,
                  text="How many message do you want to send ?", bg="blue")
    l3 = tk.Label(master,
                  text="Enter the Phone Number ", bg="blue")

    canvas1.create_window(100, 250, window=l1)
    canvas1.create_window(150, 290, window=l2)
    canvas1.create_window(100, 330, window=l3)

    e1 = tk.Entry(master)

    e2 = tk.Entry(master)

    e3 = tk.Entry(master)

    canvas1.create_window(400, 250, window=e1)
    canvas1.create_window(400, 290, window=e2)
    canvas1.create_window(400, 330, window=e3)

    def Driver():
        message_text = e1.get()  # message you want to send
        no_of_message = e2.get()
        if type(no_of_message) == int:
            print("The number is integer" + str(no_of_message))
        else:
            try:
                no_of_message = int(no_of_message)
            except:
                m1 = tk.Label(master,
                              text="ERROR : Please enter digits for No of Messages.", fg="red", bg="black")

                canvas1.create_window(250, 170, window=m1)
                m1.after(5000, m1.destroy)

        if len(message_text) == 0 or len(str(no_of_message)) == 0:
            m1 = tk.Label(master,
                          text="ERROR : Please fill the blanks.", fg="red", bg="black")

            canvas1.create_window(250, 140, window=m1)
            m1.after(5000, m1.destroy)

        phone_number = int(e3.get())

        if len(str(phone_number)) != 12:
            m1 = tk.Label(master,
                          text="ERROR : Please enter 12 digits for Phone Number.", fg="red", bg="black")

            canvas1.create_window(250, 200, window=m1)
            m1.after(5000, m1.destroy)
        else:
            phone_number = [phone_number]
            driver = webdriver.Chrome(executable_path="/home/aydinnyunus/Downloads/Birthday-master/chromedriver", options=options)
            driver.get("http://web.whatsapp.com")
            sleep(15)  # wait time to scan the code in second

            def element_presence(driver, by, xpath, time):
                element_present = EC.presence_of_element_located((By.XPATH, xpath))
                WebDriverWait(driver, time).until(element_present)

            def is_connected():
                try:
                    # connect to the host -- tells us if the host is actually
                    # reachable
                    socket.create_connection(("www.google.com", 80))
                    return True
                except:
                    is_connected()

            def send_whatsapp_msg(driver, phone_no, text, no):
                sleep(5)
                driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))

                try:
                    sleep(7)
                    element_presence(driver, By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]', 30)
                    txt_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                    for x in range(no):
                        txt_box.send_keys(text)
                        txt_box.send_keys("\n")

                except Exception as e:
                    print("Invalid Phone Number:" + str(phone_no))

            for mobile_no in phone_number:
                try:
                    sleep(5)
                    send_whatsapp_msg(driver, mobile_no, message_text, no_of_message)

                except Exception as e:
                    sleep(10)
                    is_connected()

    c1 = tk.Button(text='Send', command=Driver, bg='blue', fg='white',
                   font=('helvetica', 9, 'bold'))
    canvas1.create_window(250, 380, window=c1)


def orangeSelection(event=None):
    with open('birthdays.json') as json_file:
        data = json.load(json_file)
    l1 = tk.Label(master,
                  text="Enter the Message ", bg="orange")
    l2 = tk.Label(master,
                  text="Enter the Birth Month", bg="orange")
    l3 = tk.Label(master, text="Enter the Birth Day (2 Digits) ", bg="orange")
    l4 = tk.Label(master,
                  text="Enter the Phone Number ", bg="orange")

    canvas1.create_window(100, 250, window=l1)
    canvas1.create_window(100, 290, window=l2)
    canvas1.create_window(100, 330, window=l3)
    canvas1.create_window(100, 370, window=l4)

    h1 = tk.Entry(master)
    h2 = tk.Entry(master)
    h3 = tk.Entry(master)
    h4 = tk.Entry(master)

    canvas1.create_window(400, 250, window=h1)
    canvas1.create_window(400, 290, window=h2)
    canvas1.create_window(400, 330, window=h3)
    canvas1.create_window(400, 370, window=h4)

    def Driver():

        for p in data:
            if int(p['birth_month']) == now.strftime("%m") and int(p['birth_day']) == now.strftime("%d"):
                driver = webdriver.Chrome(executable_path="/home/aydinnyunus/Downloads/Birthday-master/chromedriver", options=options)
                driver.get("http://web.whatsapp.com")
                sleep(15)  # wait time to scan the code in second

        def element_presence(driver, by, xpath, time):
            element_present = EC.presence_of_element_located((By.XPATH, xpath))
            WebDriverWait(driver, time).until(element_present)

        def is_connected():
            try:
                # connect to the host -- tells us if the host is actually
                # reachable
                socket.create_connection(("www.google.com", 80))
                return True
            except:
                is_connected()

        def send_whatsapp_msg(driver, phone_no):
            sleep(5)
            driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))

            try:
                sleep(7)
                element_presence(driver, By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]', 30)
                txt_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                for m in data:
                    txt_box.send_keys(m['message_text'])
                    txt_box.send_keys("\n")


            except Exception as e:
                print("Invalid Phone Number:" + str(phone_no))

        for mobile_no in data:
            try:
                print(mobile_no['birth_month'])
                driver = webdriver.Chrome(executable_path="/home/aydinnyunus/Downloads/Birthday-master/chromedriver", options=options)
                if mobile_no['birth_month'] == now.strftime("%m") and mobile_no['birth_day'] == now.strftime("%d"):
                    mobile_no = mobile_no['no']
                    print(mobile_no)
                sleep(5)
                send_whatsapp_msg(driver, mobile_no)

            except Exception as e:
                sleep(10)
                is_connected()

    def Add():
        import json
        data = {}
        data1 = []

        message_text = h1.get()  # message you want to send
        birth_month = h2.get()
        birth_day = h3.get()

        if len(message_text) == 0 or len(birth_day) == 0 or len(birth_month) == 0:
            m1 = tk.Label(master,
                          text="ERROR : Please fill the blanks.", fg="red", bg="black")

            canvas1.create_window(250, 140, window=m1)
            m1.after(5000, m1.destroy)

        if int(birth_month) > 12 or int(birth_month) <= 0:
            m1 = tk.Label(master,
                          text="ERROR : Please enter in interval 1-12", fg="red", bg="black")

            canvas1.create_window(250, 230, window=m1)
            m1.after(5000, m1.destroy)

        if int(birth_day) > 30 or int(birth_day) <= 0:
            if len(birth_day) != 2:
                m1 = tk.Label(master,
                              text="ERROR : Please enter 2 Digits", fg="red", bg="black")

                canvas1.create_window(250, 80, window=m1)
                m1.after(5000, m1.destroy)
            m1 = tk.Label(master,
                          text="ERROR : Please enter in interval 1-30", fg="red", bg="black")

            canvas1.create_window(250, 110, window=m1)
            m1.after(5000, m1.destroy)

        if type(birth_month) == int and type(birth_day) == int:
            print("The number is integer" + str(birth_day))
        else:
            try:
                birth_day = int(birth_day)
            except:
                m1 = tk.Label(master,
                              text="ERROR : Please enter digits for Birth Date.", fg="red", bg="black")

                canvas1.create_window(250, 170, window=m1)
                m1.after(5000, m1.destroy)

        phone_number = h4.get()

        try:
            phone_number = int(phone_number)
        except:
            m1 = tk.Label(master,
                          text="ERROR : Please enter 12 digits for Phone Number.", fg="red", bg="black")

            canvas1.create_window(250, 200, window=m1)
            m1.after(5000, m1.destroy)
        with open('birthdays.json') as json_file:
            data = json.load(json_file)

            temp = data['people']

            # python object to be appended
            phone_number = str(phone_number)
            birth_day = str(birth_day)
            y = {
                'no': phone_number + '\n',
                'birth_month': birth_month + '\n',
                'birth_day': birth_day + '\n',
                'message_text': message_text + '\n'
            }

            # appending data to emp_details
            temp.append(y)

        with open("birthdays.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    c1 = tk.Button(text='Send', command=Driver, bg='orange', fg='white',
                   font=('helvetica', 9, 'bold'))
    canvas1.create_window(300, 420, window=c1)

    c4 = tk.Button(text='Add', command=Add, bg='orange', fg='white',
                   font=('helvetica', 9, 'bold'))

    canvas1.create_window(200, 420, window=c4)


def redSelection(event=None):
    phone_number_list = []
    l1 = tk.Label(master,
                  text="Enter the Message ", bg="red")
    l3 = tk.Label(master,
                  text="Enter the Phone Number ", bg="red")

    canvas1.create_window(100, 250, window=l1)
    canvas1.create_window(100, 330, window=l3)

    e1 = tk.Entry(master)

    e3 = tk.Entry(master)

    canvas1.create_window(400, 250, window=e1)
    canvas1.create_window(400, 330, window=e3)

    def Driver():
        message_text = e1.get()  # message you want to send
        if len(message_text) == 0:
            m1 = tk.Label(master,
                          text="ERROR : Please fill the blanks.", fg="red", bg="black")

            canvas1.create_window(250, 140, window=m1)
            m1.after(5000, m1.destroy)
        else:
            driver = webdriver.Chrome(executable_path="/home/aydinnyunus/Downloads/Birthday-master/chromedriver", options=options)
            driver.get("http://web.whatsapp.com")
            sleep(15)  # wait time to scan the code in second

            def element_presence(driver, by, xpath, time):
                element_present = EC.presence_of_element_located((By.XPATH, xpath))
                WebDriverWait(driver, time).until(element_present)

            def is_connected():
                try:
                    # connect to the host -- tells us if the host is actually
                    # reachable
                    socket.create_connection(("www.google.com", 80))
                    return True
                except:
                    is_connected()

            def send_whatsapp_msg(driver, phone_no, text):
                sleep(5)
                driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))

                try:
                    sleep(7)
                    element_presence(driver, By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]', 30)
                    txt_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                    txt_box.send_keys(text)
                    txt_box.send_keys("\n")

                except Exception as e:
                    print("Invalid Phone Number:" + str(phone_no))

            for mobile_no in phone_number_list:
                try:
                    sleep(5)
                    send_whatsapp_msg(driver, mobile_no, message_text)

                except Exception as e:
                    sleep(10)
                    is_connected()

    def Add():
        phone_number = e3.get()
        try:
            phone_number = int(phone_number)
        except:
            m1 = tk.Label(master,
                          text="ERROR : Please enter 12 digits for Phone Number.", fg="red", bg="black")

            canvas1.create_window(250, 200, window=m1)
            m1.after(5000, m1.destroy)
        phone_number_list.insert(0, phone_number)
        print(phone_number_list)

    c1 = tk.Button(text='Send', command=Driver, bg='red', fg='white',
                   font=('helvetica', 9, 'bold'))
    canvas1.create_window(300, 370, window=c1)

    c4 = tk.Button(text='Add', command=Add, bg='red', fg='white',
                   font=('helvetica', 9, 'bold'))

    canvas1.create_window(200, 370, window=c4)


def greenSelection(event=None):
    l1 = tk.Label(master,
                  text="Enter the Message ", bg="green")
    l2 = tk.Label(master,
                  text="Enter the Hour", bg="green")
    l3 = tk.Label(master, text="Enter the Minutes ", bg="green")
    l4 = tk.Label(master,
                  text="Enter the Phone Number ", bg="green")

    canvas1.create_window(100, 250, window=l1)
    canvas1.create_window(100, 290, window=l2)
    canvas1.create_window(100, 330, window=l3)
    canvas1.create_window(100, 370, window=l4)

    g1 = tk.Entry(master)
    g2 = tk.Entry(master)
    g3 = tk.Entry(master)
    g4 = tk.Entry(master)

    canvas1.create_window(400, 250, window=g1)
    canvas1.create_window(400, 290, window=g2)
    canvas1.create_window(400, 330, window=g3)
    canvas1.create_window(400, 370, window=g4)

    def Driver():
        message_text = g1.get()  # message you want to send
        phone_number = int(g4.get())
        phone_number = [phone_number]
        hour = int(g2.get())
        minutes = int(g3.get())

        if len(message_text) == 0 or len(str(phone_number)) == 0 or len(str(hour)) == 0 or len(str(minutes)) == 0:
            m1 = tk.Label(master,
                          text="ERROR : Please fill the blanks.", fg="red", bg="black")

            canvas1.create_window(250, 140, window=m1)
            m1.after(5000, m1.destroy)
        if hour >= 24:
            m1 = tk.Label(master,
                          text="ERROR : Please use 'Celebrate Birthday' Option (Hour>=24).", fg="red", bg="black")

            canvas1.create_window(250, 110, window=m1)
            m1.after(10000, m1.destroy)

        else:
            resultHour = (hour - now.hour) * 3600
            resultMin = (minutes - now.minute) * 60
            result = resultHour + resultMin
            print(result)

            if hour == now.hour and minutes == now.minute:
                driver = webdriver.Chrome(executable_path="/home/aydinnyunus/Downloads/Birthday-master/chromedriver", options=options)
                driver.get("http://web.whatsapp.com")
                sleep(15)  # wait time to scan the code in second
            driver = webdriver.Chrome(executable_path="/home/aydinnyunus/Downloads/Birthday-master/chromedriver", options=options)
            driver.get("http://web.whatsapp.com")
            sleep(15)  # wait time to scan the code in second

            def element_presence(driver, by, xpath, time):
                element_present = EC.presence_of_element_located((By.XPATH, xpath))
                WebDriverWait(driver, time).until(element_present)

            def is_connected():
                try:
                    # connect to the host -- tells us if the host is actually
                    # reachable
                    socket.create_connection(("www.google.com", 80))
                    return True
                except:
                    is_connected()

            def send_whatsapp_msg(driver, phone_no, text):
                sleep(5)
                driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))

                try:
                    sleep(7)
                    element_presence(driver, By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]', 30)
                    txt_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

                    sleep(result)

                    txt_box.send_keys(text)
                    txt_box.send_keys("\n")

                except Exception as e:
                    print("Invalid Phone Number:" + str(phone_no))

            for mobile_no in phone_number:
                try:
                    sleep(5)
                    send_whatsapp_msg(driver, mobile_no, message_text)

                except Exception as e:
                    sleep(10)
                    is_connected()

    c1 = tk.Button(text='Send', command=Driver, bg='green', fg='white',
                   font=('helvetica', 9, 'bold'))
    canvas1.create_window(250, 400, window=c1)


ch = tk.Label(master, text="Send Message X Times", fg="white", bg="lightblue")
ch.bind("<Button-1>", blueSelection)
ch.config(font=('helvetica', 14))
canvas1.create_window(120, 270, window=ch)

ch2 = tk.Label(master, text="Celebrate Birthday", fg="white", bg="orange")
ch2.bind("<Button-1>", orangeSelection)
ch2.config(font=('helvetica', 14))
canvas1.create_window(380, 270, window=ch2)

ch3 = tk.Label(master, text="Send Message to X Person", fg="white", bg="red")
ch3.bind("<Button-1>", redSelection)
ch3.config(font=('helvetica', 14))
canvas1.create_window(120, 640, window=ch3)

ch4 = tk.Label(master, text="Send Message at Specific Time", fg="white", bg="lightgreen")
ch4.bind("<Button-1>", greenSelection)
ch4.config(font=('helvetica', 14))
canvas1.create_window(380, 640, window=ch4)

"""""""""

canvas1.create_text(400, 90, fill="black", font="Times 15 italic bold",
                    text="What do you want ?\n"
                         "1-Send Message X Times.\n"
                         "2-Send Message in specific time\n"
                         "3-Send Message to a lot of people\n")
label2 = tk.Label(master, text="What do you want ?\n"
                               "1-Send Message X Times.\n"
                               "2-Send Message in specific time\n"
                               "3-Send Message to a lot of people\n")
label2.config(font=('helvetica', 10))
canvas1.create_window(400, 100, window=label2)


entry1 = tk.Entry(master)
canvas1.create_window(400, 140, window=entry1)
"""""""""""

"""""""""""
def choose():
    selection = int(entry1.get())
    print("Welcome to Whatsapp Message Bot \n")


    elif selection == 2:



    elif selection == 3:

        count = int(input("How many person do you want to enter ?"))
        message_text = input("Enter the message :")  # message you want to send
        no_of_message = int(
            input("How many message do you want to send ? "))  # no. of time you want the message to be send
        liste = []
        for i in range(count):
            temp = input("Enter the phone number with country code (Example 90500000000) ")
            liste.append(temp)
            print(liste)
        phone_number = liste[0]
        print(phone_number)

        driver = webdriver.Chrome(executable_path="/home/aydinnyunus/Downloads/Birthday-master/chromedriver", options=options)
        driver.get("http://web.whatsapp.com")
        sleep(15)  # wait time to scan the code in second

    else:
        error = tk.Label(master, text='Please enter in interval (1-3)', fg="red")
        error.config(font=('helvetica', 14))
        canvas1.create_window(200, 250, window=error)


"""""""""
"""""""""
button1 = tk.Button(text='Select', command=choose, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(450, 180, window=button1)

button2 = tk.Button(text='Quit', command=master.quit, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))

canvas1.create_window(350, 180, window=button2)
"""""""""
"""""""""
# entry1 = tk.Entry(master)
# canvas1.create_window(200, 140, window=entry1)

# selection = entry1.get()


# choose = int(str(e4.get()))
"""""""""""

master.mainloop()
