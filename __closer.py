import os

def closer() -> bool:
	if os.environ.get("exit") != "true":
		return False
	else:
		return True