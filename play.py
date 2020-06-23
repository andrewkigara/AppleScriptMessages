import os
import privInfo


faucet_lyrics = open('faucet.txt', 'r')
x = faucet_lyrics.readlines()
for line in x:
	lines = line.split()
	for word in lines:
		os.system('osascript send.scpt {} "{}"'.format(privInfo.wyatt, word))
		#print("124, ", word)









# def get_lines(file_path):
# 	with open(file_path, 'r') as f:
# 		text = f.readlines()

# 	return text

# def get_words(file_path):
# 	with open(file_path, 'r') as f:
# 		text = f.readlines()
# 		for x in text:
# 			words = text.rsplit('\n')
# 	return words

# def send_message(phone_number, message):
# 	os.system('osascript send.scpt {} "{}"'.format(phone_number, message))

# if __name__ == "__main__":
# 	text = get_lines('faucet.txt')
# 	print(text)
# 	# for line in text:
# 	# 	send_message(config.FRIEND2, line)