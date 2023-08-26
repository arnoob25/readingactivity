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
    data = [] # data on empty page

    # After the author clicks "generate outline"
    query_ra_step = app_tables.ra_steps.search()
    self.rpanel_ra_step.items = query_ra_step
    self.rpanel_ra_step2.items = query_ra_step

    # After the author clicks "generate question"
    self.rpanel_questions.items = app_tables.question.search()



    
    
    
    


    

