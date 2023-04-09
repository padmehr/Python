# -*- coding: utf-8 -*-

"""This module provides RP reminder application."""

import sys

from PyQt5.QtWidgets import QApplication

from rpreminder.database import createConnection
from rpreminder.views import Window


def main():
    """RP reminder main function."""
    # Create the application
    app = QApplication(sys.argv)
    # Connect to the database before creating any window
    if not createConnection("reminder.sqlite"):
        sys.exit(1)
    # Create the main window if the connection succeeded
    win = Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec_())
