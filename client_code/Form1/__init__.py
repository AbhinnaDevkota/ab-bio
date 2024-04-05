from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    email = str(self.text_box_1)
    hobby = str(self.text_area_1)
    anvil.server.call('submit' , email = email, hobby = hobby)
    Notification("your response has been recorded").show()

  

  
    
