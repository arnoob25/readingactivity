from ._anvil_designer import ItemTemplate2Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ItemTemplate2(ItemTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def btn_gi_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    if self.cpanel_2.visible:
      self.cpanel_2.visible = False
      self.btn_gi.icon = "fa:angle-down"
    else:
      self.cpanel_2.visible = True
      self.btn_gi.icon = "fa:angle-up"
