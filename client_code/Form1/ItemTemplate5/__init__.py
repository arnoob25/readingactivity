from ._anvil_designer import ItemTemplate5Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ItemTemplate5(ItemTemplate5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    # After the author runs "generate questions"
    query_options = app_tables.options.search()
    self.rpanel_options.items = query_options