import os

FILE_NAME = "contacts2.txt"

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    file = open("contacts2.txt", "a")
    file.write(f"{name},{phone},{email}\n")

add_contact()