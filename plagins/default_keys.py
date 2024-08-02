import os
import time

import keyboard

def add_char(char:str):
	os.environ["text"] = os.environ["text"][:int(os.environ["cursor_pos"])] + char + os.environ["text"][int(os.environ["cursor_pos"]):]
	os.environ["cursor_pos"] = str(int(os.environ["cursor_pos"]) + 1)

def space() -> None:
	add_char(" ")

def enter() -> None:
	add_char("\n")
	os.environ["cursor_line"] = str(int(os.environ["cursor_line"]) + 1)


def tab() -> None:
	add_char("\t")

def debug() -> None:
	os.environ["pause"] = "true"
	time.sleep(2)


def backspace() -> None:
	if int(os.environ["cursor_pos"]) > 0:
		if os.environ["text"][int(os.environ["cursor_pos"]) - 1] == "\n":
			os.environ["cursor_line"] = str(int(os.environ["cursor_line"]) - 1)

		os.environ["text"] = os.environ["text"][:int(os.environ["cursor_pos"]) - 1] +  os.environ["text"][int(os.environ["cursor_pos"]):]
		os.environ["cursor_pos"] = str(int(os.environ["cursor_pos"]) - 1)

def right() -> None:
	if int(os.environ["cursor_pos"]) < len(os.environ["text"]):
		if os.environ["text"][int(os.environ["cursor_pos"])] == "\n":
			# os.environ["pause"] = "true"
			# time.sleep(2)
			if int(os.environ["cursor_line"]) < len(os.environ["text"].split("\n")):
				os.environ["cursor_line"] = str(int(os.environ["cursor_line"]) + 1)
		os.environ["cursor_pos"] = str(int(os.environ["cursor_pos"]) + 1)


def left() -> None:
	if int(os.environ["cursor_pos"]) > 1:
		if os.environ["text"][int(os.environ["cursor_pos"]) - 1] == "\n":
			if int(os.environ["cursor_line"]) != 0:
				os.environ["cursor_line"] = str(int(os.environ["cursor_line"]) - 1)
		os.environ["cursor_pos"] = str(int(os.environ["cursor_pos"]) - 1)

def up() -> None:
	lines = os.environ["text"].split("\n")
	cursor_line = int(os.environ["cursor_line"])
	if cursor_line != 0:
		cursor_len_line_start = len(os.environ["text"][:int(os.environ["cursor_pos"])].split("\n")[-1])
		cursor_len_line_end = len(os.environ["text"][int(os.environ["cursor_pos"]):].split("\n")[0])
		# debug()
		next_len_line_end = len(os.environ["text"][int(os.environ["cursor_pos"]) - cursor_len_line_start:].split("\n")[0]) - cursor_len_line_start
		len_next_line = len(lines[cursor_line - 1])
		if cursor_len_line_start <= len_next_line:
			# debug()
			os.environ["cursor_pos"] = str(int(os.environ["cursor_pos"]) - (cursor_len_line_start + next_len_line_end) + 2)
		else:
			os.environ["cursor_pos"] = str(int(os.environ["cursor_pos"]) - (cursor_len_line_start + 1))
		os.environ["cursor_line"] = str(int(cursor_line) - 1)

def down() -> None:
	lines = os.environ["text"].split("\n")
	cursor_line = int(os.environ["cursor_line"])
	if cursor_line < len(lines) - 1:
		cursor_len_line_start = len(os.environ["text"][:int(os.environ["cursor_pos"])].split("\n")[-1])
		cursor_len_line_end = len(os.environ["text"][int(os.environ["cursor_pos"]):].split("\n")[0])
		len_next_line = len(lines[cursor_line + 1])
		if cursor_len_line_start <= len_next_line:
			os.environ["cursor_pos"] = str(int(os.environ["cursor_pos"]) + (cursor_len_line_start + cursor_len_line_end) + 1)
		else:
			os.environ["cursor_pos"] = str(int(os.environ["cursor_pos"]) + (len_next_line + cursor_len_line_end) + 1)

		os.environ["cursor_line"] = str(int(cursor_line) + 1)

def save() -> None:
	os.environ["pause"] = "true"
	# keyboard.press_and_release("backspace")
	# for i in range(len(os.environ["text"])):
	# 	keyboard.press_and_release("backspace")
	# 	time.sleep(0.1)

	file_name = input("Write path for save file and open mode:\n|-- file path -->")
	file_mode = input("|-- file mode -->")

	if len(file_name.split(".")) >= 2:
		if file_mode in ["w", "a"]:
			with open(file_name, file_mode) as file:
				file.write(os.environ["text"])
		else:
			print("File mode not avaiable")
	else:
		print("File name not avaiable")
	
	time.sleep(2)
	os.environ["pause"] = ""




def close_ide():
	os.environ["exit"] = "true"
