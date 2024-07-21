from ._anvil_designer import Form1Template
from anvil import *
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form2')

    anvil.users.login_with_form()
    anvil.server.call('print_my_permissions')

  
    
