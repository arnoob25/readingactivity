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
    anvil.server.call(
      "outline", 
      self.textbox_ilo.text,
      self.textbox_title.text
    )

    query_ra_step = app_tables.ra_steps.search()
    self.rpanel_ra_step.items = query_ra_step
    self.rpanel_ra_step2 = query_ra_step

  def button_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    query_gi_steps = app_tables.gi_steps.search()
    self.rpanel_gi_steps.items = query_gi_steps
    pass

    
    

    

