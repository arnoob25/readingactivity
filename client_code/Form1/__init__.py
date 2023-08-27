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

    # After steps are generated
    global query_ra_step
    query_ra_step = app_tables.ra_steps.search()
    l_ra_step = [s.get_id() for s in query_ra_step]

    # After GIs are generated
    global l_gi_step
    l_gi_step = {}
    step_count = 0
    
    for i in l_ra_step:
      step_count = 0
      query_gi_step = app_tables.gi_steps.search(
        ra_step = app_tables.ra_steps.get_by_id(i)
      )
      temp_list = [gi for gi in query_gi_step]

      l_gi_step[f"Step {step_count}"] = temp_list
    alert(l_ra_step)
    alert(l_gi_step)
    

  def btn_outline_click(self, **event_args):
    """This method is called when the button is clicked"""

    self.author_page1.visible = False
    self.author_page2.visible = True

    

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


    # Test the iteration
    test_dict = {'step 1' : ['gi1','gi2','gi3','gi4'], 'step 2' : ['gi1','gi2','gi3']}
    for i in test_dict:
      for i in test_dict[i]:
        global curr_gi

    
    # Functionality for getting question data

    question = app_tables.question.get(
      gi_step = app_tables.gi_steps.get_by_id(curr_gi)
    )

    
        


  def btn_next_question_click(self, **event_args):
    """This method is called when the button is clicked"""

    
    pass


    