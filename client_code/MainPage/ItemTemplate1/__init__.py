from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def btn_instruction_click(self, **event_args):
    """This method is called when the button is clicked"""

    if self.instruction.visible == False:
      self.instruction.visible = True
      self.btn_instruction.icon = "fa:angle-up"
    else:
      self.instruction.visible = False
      self.btn_instruction.icon = "fa:angle-down"





