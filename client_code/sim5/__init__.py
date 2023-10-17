from ._anvil_designer import sim5Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users

class sim5(sim5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def simulate_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def simulate_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.car.left = 0
    self.speed = self.top_speed
    self.message.text = ''
    self.simulate_button.enabled = False
    self.reset_button.enabled = False

    # Start the animation
    anvil.server.call('start_animation', self.get_id())


