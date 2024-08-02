import os

from __closer import closer

def viewer():
	while True:
		if os.environ.get("pause") != "true":
			text = os.environ["text"]
			cursor = int(os.environ["cursor_pos"]) -1
			if text != "":
				if text[cursor] != " ":
					print(text[:cursor] + text[cursor].swapcase() + text[cursor + 1:])
				else:
					print(text[:cursor] + "_" + text[cursor + 1:])
			else:
				print(text)
			os.system('cls')

		if closer():
			break