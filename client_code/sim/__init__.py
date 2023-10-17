from ._anvil_designer import simTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.js.window as window

class sim(simTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.car.x = 0

  
  def simulate_click(self, **event_args):
    """This method is called when the button is clicked"""
    window.jQuery(self.car).animate({'left': '100%'}, 5000) 

