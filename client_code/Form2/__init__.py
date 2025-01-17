from ._anvil_designer import Form2Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form3')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1')

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form3')

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form4')

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form5')

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form6')
