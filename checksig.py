#!/usr/bin/env python3

# Configuration:
APPNAME = "Clipboard Notifier"  # an arbitrary application name
TITLE = "Clipboard modified"    # the bold headline of each notification
ICON = "edit-paste"             # name of the icon to show
MAXLENGTH = 100                 # maximum message length

# Imports:
import gi
import signal
import notify2
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

# Set up signal handler for killing the script with Ctrl+C from terminal:
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Initialize the notifications library:
notify2.init(APPNAME)

# Callback function to handle clipboard modification events:
def callback(*args):
    # Get new clipboard content:
    text = clip.wait_for_text()
    # Truncate long content to avoid huge notification bubbles:
    body = text if len(text) < MAXLENGTH else text[:MAXLENGTH] + "..."
    # Create and show notification bubble:
    notify2.Notification(TITLE, body, ICON).show()

# Set up clipboard and register callback for change events
clip = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
clip.connect("owner-change", callback)

# Start Gtk main loop and wait for events:
Gtk.main()
