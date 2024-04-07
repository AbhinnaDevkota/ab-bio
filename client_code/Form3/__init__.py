from ._anvil_designer import Form3Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form2')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    blog = str(self.text_area_1)
    anvil.server.call('submit' , blog = blog)
    Notification('Well done now you are a blog writer.').show()
