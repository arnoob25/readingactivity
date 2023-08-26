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
    self.author_page1.visible = False
    self.author_page2.visible = False
    self.author_page3.visible = False
    self.author_page4.visible = True
    ra = app_tables.ra_steps.get(serial = 3)
    gi = app_tables.gi_steps.get(
      q.
      ra_step_test = ra
    )
    self.rpanel_questions.items = app_tables.question.get(
      gi_step_test = gi
    )

  query_ra_step = []

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

    
    
    


    
    





    
    
    
    


    

