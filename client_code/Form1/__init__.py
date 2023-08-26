from ._anvil_designer import Form1Template
from anvil import *
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
    self.author_page1.visible = True
    self.author_page2.visible = False
    self.author_page3.visible = False
    self.author_page4.visible = False
    
    

    query_ra_step = app_tables.ra_steps.search()
    gi_steps = {}
  
    for s in query_ra_step:
      temp = s.get_id()
      alert()app_tables.gi_steps.get_by_id(s.get_id())

  def btn_outline_click(self, **event_args):
    """This method is called when the button is clicked"""

    self.author_page1.visible = False
    self.author_page2.visible = True

    global query_ra_step
    query_ra_step = app_tables.ra_steps.search()
    self.rpanel_ra_step.items = query_ra_step
    self.rpanel_ra_step2.items = query_ra_step

  def btn_gi_click(self, **event_args):
    """This method is called when the button is clicked"""

    self.author_page2.visible = False
    self.author_page3.visible = True

  def btn_question_click(self, **event_args):
    """This method is called when the button is clicked"""

    self.author_page3.visible = False
    self.author_page4.visible = True

    self.item = app_tables.question.get()
    



    
    
    


    
    





    
    
    
    


    

