import os
import time
import inspect
import importlib

import keyboard

import keymap
from __closer import closer

class Listener(object):
	"""Key listener methods"""
	def __init__(self) -> None:
		# import files from plugin directory
		for plaginPath in [file.replace(".py", "") for file in os.listdir("./plagins/") if ".py" in file]:
			module = importlib.import_module("plagins." + plaginPath)
			functions = [{"name":name, "obj":obj} for name, obj in inspect.getmembers(module, inspect.isfunction)]
			for function in functions:
				self.last_plugin = function.get("obj")
				exec("self." + function.get("name") + "= self.last_plugin")

	def init_keys(self) -> None:
		# Init keymap
		for keyInfo in keymap.special.keys():
			keyboard.add_hotkey(keyInfo, eval("self." + keymap.special.get(keyInfo)))

		# main key listener cycle
		while True:
			key = keyboard.read_key()
			if key not in keymap.special.keys() and len(key) == 1:
				# use add_char from default_keys.py from plagins
				self.add_char(key)
				# time for repair write double key in 1 click
				time.sleep(0.14)

			if closer():
				break