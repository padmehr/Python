# -*- coding: utf-8 -*-

"""This module provides a model to manage the medicine table."""

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QMessageBox
import threading
import time




class RemindersModel:
    def __init__(self):
        self.model = self._createModel()

    @staticmethod
    def _createModel():
        """Create and set up the model."""
        tableModel = QSqlTableModel()
        tableModel.setTable("reminder")
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = ("ID", "Name", "Notify per x seconds")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel

    def reminder(self, seconds, name):
        print(f"{name} thread is started")
        print(f"I will alert you in {seconds} seconds")
        time.sleep(10)
        #self.showMessageBox(name)
        print(f"{name} medicine is Due")
        
    def threadStarter(self):
        thread = []
        row = self.model.rowCount()
        for index in range(row):
            seconds = self.model.record(index).value('notify')
            name = self.model.record(index).value('name')
            th = threading.Thread(target=self.reminder, args=[seconds, name])
            thread.append(th)
            th.start()
            
    def showMessageBox(self, name):
        QMessageBox.about(self, "Reminder", f"{name} is Due")
        

    def addReminder(self, data):
        """Add a reminder to the database."""
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column_index, field in enumerate(data):
            self.model.setData(self.model.index(rows, column_index + 1), field)
        self.model.submitAll()
        self.model.select()
        

    def deleteReminder(self, row):
        """Remove a reminder from the database."""
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()

    def clearReminders(self):
        """Remove all reminders in the database."""
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
