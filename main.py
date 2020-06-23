# AppleScript
# Sends information from a separate file as iMessages
# ---------------------------------------------------
# send.scpt Handles the terminal output
# main.py Main python script
# file.txt The information being sent
# 
# --- They eed to be in the same directory ---
# 
# Created by Andrew Kigara on 6/22/20.
# Copyright © 2020 Andrew Kigara. All rights reserved.
#






import os
import privInfo
from time import sleep

def text_message(file_name, phone_number):
	send_objects = []
	f = open(file_name, 'r')
	lines = f.readlines()
	for line in lines:
		line.strip()
		send_objects.append(line)
	print(send_objects)

	send_message(send_objects, phone_number)


def send_message(messages, phone_number):
	for message in messages:
		print(message, end = "")
		#sleep(1)
		#os.system('osascript send.scpt {} {}'.format(phone_number, message))


# def send_message(phone_number, message):
# 	# 
# 	x = message.splitlines("\n")
# 	for word in x:
# 		print(word)
# 		os.system('osascript send.scpt {} {}'.format(phone_number, word))

if __name__ == "__main__":
	text_message('file.txt', privInfo.number_1)
	# send_message(privInfo.izzy_number, privInfo.izzy_message)

	# lyrics = get_lyrics('lyrics.txt')
	# for lyrss in lyrics:
	# 	send_message(privInfo.phil_number, lyrss)