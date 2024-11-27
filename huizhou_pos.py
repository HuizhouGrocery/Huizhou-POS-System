import tkinter as tk
import ttkbootstrap as ttk 
from tkinter import messagebox
from tkinter import PhotoImage

import win32api
import win32print
from glob import glob

import uuid 

import sqlite3

import datetime

currentDateTime = datetime.datetime.now()
uid = uuid.uuid1() 

products = {
    "01": {"name": "红豆", "price": 8.00},
    "02": {"name": "E1400蜂蜜", "price": 189.00},
    "03": {"name": "腊香肠", "price": 26.00},
    "04": {"name": "腊猪蹄", "price": 27.00},
    "05": {"name": "腊肉", "price": 25.00}
}


def writeTofile(str, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'w',encoding='UTF-8') as file:
        file.writelines(str)

def print_receipt(filename):
    
    # set the default printer
    printer_name = win32print.GetDefaultPrinter()
    print_defaults = {'DesiredAccess': win32print.PRINTER_ALL_ACCESS}

    printer_handle = win32print.OpenPrinter(printer_name,print_defaults)

    txt_dir = filename
    for f in glob(txt_dir, recursive=True):
        win32api.ShellExecute(0, "print", f, None,  ".",  0)

    win32print.ClosePrinter(printer_handle)


class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SQLite Database Huizhou Grocery POS System")
        self.root.geometry("1100x800")

        # Create a database or connect to an existing one
        self.conn = sqlite3.connect(r"Your database working directory\\huizhou_order.db")
        self.cursor = self.conn.cursor()

        # # Create a table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS testv7_order (id INTEGER PRIMARY KEY, order_number TEXT, final_price TEXT, detail TEXT, time TEXT)''')
        self.conn.commit()

        # Put logo image into GUI

        self.image = PhotoImage(file=r"Your current working directory(pwd)\logo.png")
        self.image_label = ttk.Label(root, image=self.image)
        self.image_label.place(x=500, y=20, width=110, height=127)

        # Create a label for the product ID

        self.product_info_label = ttk.Label(root, text="红豆:\t 01\nE1400蜂蜜:\t02\n腊香肠:\t03\n腊猪蹄:\t04\n腊肉:\t05\n",font=("Times New Roman", 15))
        self.product_info_label.pack(pady=500)
        self.product_info_label.place(x=750, y=130,height=300)

        self.product_id_label = ttk.Label(root, text="Product ID:",font=("Arial", 10))
        self.product_id_label.pack(pady=10)
        self.product_id_label.place(x=150, y=220)
  
        # Create an entry box for the product ID
        self.product_id_entry = ttk.Entry(root, state="normal")
        self.product_id_entry.pack(pady=10)
        self.product_id_entry.place(x=260, y=215)

        # Create a label for the product name
        self.product_name_label = ttk.Label(root, text="Product Name:",font=("Arial", 10))
        self.product_name_label.pack()
        self.product_name_label.place(x=150, y=275)

        # Create an entry box for the product name
        self.product_name_entry = ttk.Entry(root, state="normal")
        self.product_name_entry.pack(pady=10)
        self.product_name_entry.place(x=260, y=270)

        # Create a label for the product price
        self.product_price_label = ttk.Label(root, text="Product Price:",font=("Arial", 10))
        self.product_price_label.pack()
        self.product_price_label.place(x=150, y=325)

        # Create an entry box for the product price
        self.product_price_entry = ttk.Entry(root, state="normal")
        self.product_price_entry.pack(pady=10)
        self.product_price_entry.place(x=260, y=320)

        # Create a label for the product quantity
        self.product_quantity_label = ttk.Label(root, text="Product Quantity:",font=("Arial", 10))
        self.product_quantity_label.pack()
        self.product_quantity_label.place(x=150, y=380)

        # Create an entry box for the product quantity
        self.product_quantity_entry = ttk.Entry(root, state="normal")
        self.product_quantity_entry.pack(pady=10)
        self.product_quantity_entry.place(x=260, y=375)

        # Create a label for the total price
        self.total_price_label = ttk.Label(root, text="Total Price:",font=("Arial", 10))
        self.total_price_label.pack()
        self.total_price_label.place(x=150, y=435)

        # Create an entry box for the total price
        self.total_price_entry = ttk.Entry(root, state="normal")
        self.total_price_entry.pack(pady=10)
        self.total_price_entry.place(x=260, y=430)

        # Create a label for the final price
        self.final_price_label = ttk.Label(root, text="Final Price: ",font=("Arial", 10))
        self.final_price_label.pack(pady=10)
        self.final_price_label.place(x=150, y=490)
  
        # Create an entry box for the final price
        self.final_price = ttk.Entry(root,state="normal")
        self.final_price.pack(pady=10)
        self.final_price.place(x=260, y=485)

        # Create a button to calculate the total price
        self.calculate_button = ttk.Button(root, text="Calculate Price",command=self.calculate_total) 
        self.calculate_button.pack(pady=10)
        self.calculate_button.place(x=200, y=620,width = 120,height=45)

        # Create a button to move to next item
        self.next_item = ttk.Button(root, text="Next Item",command=self.next_item)
        self.next_item.pack(pady=10)
        self.next_item.place(x=400, y=620,width = 120,height=45)

        # Create a button to check out
        self.checkout_button = ttk.Button(root, text="Check Out",command=self.check_out)
        self.checkout_button.pack(pady=10)
        self.checkout_button.place(x=600, y=620,width = 120,height=45)

        self.clearitem_button = ttk.Button(root, text="Clear Item",command=self.clear_item)
        self.clearitem_button.pack(pady=10)
        self.clearitem_button.place(x=800, y=620,width = 120,height=45)

        # Create some lists for products
        self.list_ofprice = []
        self.list_ofitem = []
        self.list_ofreceipt = []


    def calculate_total(self):
        # Get the product ID from the entry box
         product_id = self.product_id_entry.get().strip()

        # Retrieve the product details from the product database
         product = products.get(product_id)

        # If the product is found, calculate the total price
         if product:
        # Get the quantity from the entry box
          quantity = int(self.product_quantity_entry.get())

        # Calculate the total price
          total_price = product['price'] * quantity

        # Update the product name, price, quantity, and total price in the entry boxes
          self.product_name_entry.config(state="normal")
          self.product_name_entry.delete(0, tk.END)
          self.product_name_entry.insert(0, product['name'])
         
          self.product_price_entry.config(state="normal")
          self.product_price_entry.delete(0, tk.END)
          self.product_price_entry.insert(0, product['price'])
        

          self.product_quantity_entry.config(state="normal")
          self.product_quantity_entry.delete(0, tk.END)
          self.product_quantity_entry.insert(0, quantity)
       

          self.total_price_entry.config(state="normal")
          self.total_price_entry.delete(0, tk.END)
          self.total_price_entry.insert(0, total_price)
       
          # Sum up all items price 
          price = float(self.total_price_entry.get())
       
          self.list_ofprice.append(price)

          total = sum(self.list_ofprice)

          self.final_price.config(state="normal")
          self.final_price.delete(0, tk.END)
          self.final_price.insert(0, total)


          # put all values to one list
          self.list_ofitem.append("商品编号："+product_id+'\t')
          self.list_ofitem.append(product['name']+' \t  ')
          self.list_ofitem.append('单价：¥'+str(product['price'])+'\t')
          self.list_ofitem.append("数量： *"+str(quantity)+'\t')
          self.list_ofitem.append('总价：¥'+str(price)+'\n')
   
         else:
        # Display an error message if the product is not found
          messagebox.showerror("Error", "Product not found")

    def check_out(self):
          # check out order
          total = sum(self.list_ofprice)      
          final_price = total 

          order_number = str(uid.int)
       
          detail = ''.join(map(str, self.list_ofitem))
          time = f"{currentDateTime}"  # If we insert time format to the sqlite database directly, we may face errors or warnings. Just change it to string format.

          if final_price != 0:
            self.cursor.execute("INSERT INTO testv7_order (order_number, final_price,detail,time) VALUES (?,?,?,?)", (order_number,final_price,detail,time))
         
            self.conn.commit()
         
            messagebox.showinfo("showinfo", "You have inserted data") 

            res = messagebox.askquestion('Order_Details', 'Do you want to print this order')
            if   res == 'yes':
                    textPath = r"Your current working directory(pwd)\\"  + "receipt.txt"
             
                    self.list_ofreceipt.append('--------------------------\n')
                    self.list_ofreceipt.append('遵义汇舟食品零售有限公司\n')
                    self.list_ofreceipt.append('订单编号：'+ order_number+ '\n')
                    self.list_ofreceipt.append('订单总价：¥'+ str(final_price)+ '\n')
                    self.list_ofreceipt.append(detail+'\n')
                    self.list_ofreceipt.append('收据打印时间：'+str(time)+'\n')
                    self.list_ofreceipt.append('欢迎惠顾汇舟食品！\n')
                    self.list_ofreceipt.append('--------------------------\n')

                    writeTofile(self.list_ofreceipt, textPath)
                  
                    print_receipt(textPath)
                    
                    messagebox.showinfo('Response', "You have printed order")
                    
            elif res == 'no':
                    messagebox.showinfo('Response', 'You must be a cat fan.')
            else:
                    messagebox.showwarning('error', 'Something went wrong!')


            # Empty all lists
            self.list_ofprice = []
            self.list_ofitem = []
            self.list_ofreceipt = []
          
          else:
            messagebox.showwarning("Warning", "You do not have item")


          self.product_id_entry.delete(0, tk.END)
          self.product_name_entry.delete(0, tk.END)
          self.product_price_entry.delete(0, tk.END)
          self.product_quantity_entry.delete(0, tk.END)
          self.total_price_entry.delete(0, tk.END)
          self.final_price.delete(0, tk.END)


    def next_item(self):
          
          self.product_id_entry.delete(0, tk.END)
          self.product_name_entry.delete(0, tk.END)
          self.product_price_entry.delete(0, tk.END)
          self.product_quantity_entry.delete(0, tk.END)
          self.total_price_entry.delete(0, tk.END)

    def clear_item(self):     
          #clear all items and prices
          self.list_ofprice = []
          self.list_ofitem = []
          self.list_ofreceipt = []

          self.product_id_entry.delete(0, tk.END)
          self.product_name_entry.delete(0, tk.END)
          self.product_price_entry.delete(0, tk.END)
          self.product_quantity_entry.delete(0, tk.END)
          self.total_price_entry.delete(0, tk.END)
          self.final_price.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()
