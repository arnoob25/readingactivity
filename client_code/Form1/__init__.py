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

    # Declate instance variables
    self.curr_ra_step = 1
    self.curr_gi_step = 1
    
    # Any code you write here will run before the form opens.
    self.author_page1.visible = False
    self.author_page2.visible = False
    self.author_page3.visible = False
    self.author_page4.visible = True


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

  def itr(self, dic):
      end = False

      if self.curr_gi_step+1 <= dic[self.curr_ra_step]:
        self.curr_gi_step = self.curr_gi_step + 1
      elif self.curr_ra_step+1 in dic:
        self.curr_ra_step = self.curr_ra_step + 1
        self.curr_gi_step = 1
      else: 
        end = True

      return end

  def btn_gen_outline_click(self, **event_args):
    """This method is called when the button is clicked"""

    self.author_page1.visible = False
    self.author_page2.visible = True

    

    self.rpanel_ra_step.items = query_ra_step
    self.rpanel_ra_step2.items = query_ra_step

  def btn_gen_gi_click(self, **event_args):
    """This method is called when the button is clicked"""

    self.author_page2.visible = False
    self.author_page3.visible = True

  def btn_gen_question_click(self, **event_args):
    """This method is called when the button is clicked"""

    self.author_page3.visible = False
    self.author_page4.visible = True

    # Creating the dictionary
    test_dict = {1 : ['one', 'two']} # step : [gi steps]
    
    # Functionality for getting question data

    question = app_tables.question.get(
      gi_step = app_tables.gi_steps.get_by_id(curr_gi)
    )

  def btn_next_question_click(self, **event_args):
    """This method is called when the button is clicked"""

    ra = self.curr_ra_step
    gi = self.curr_gi_step
    data = {1 : 2, 2 : 3} 
    iterate = self.itr(data)
    
    if iterate == False:
      alert(f"Current step: {ra}, Current gi: {gi}")
    else:
      pass


    