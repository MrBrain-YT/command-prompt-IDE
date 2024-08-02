import threading
import os

from __key_listener import Listener
from __terminal_viewer import viewer
from __closer import closer

os.environ["text"] = ""
os.environ["cursor_pos"] = "0"
os.environ["cursor_line"] = "0"

list = Listener()
listenerThread = threading.Thread(target=list.init_keys)
viewer = threading.Thread(target=viewer)

listenerThread.start()
viewer.start()

listenerThread.join()
viewer.join()