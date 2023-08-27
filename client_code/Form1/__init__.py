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
    self.curr_file = None
    self.curr_ra_step = 1
    self.curr_gi_step = 1
    self.query_ra_steps = None
    self.data = {}
    
    # Any code you write here will run before the form opens.
    self.author_page1.visible = False
    self.author_page2.visible = False
    self.author_page3.visible = False
    self.author_page4.visible = True

    # Building the Data
    self.curr_file = app_tables.files.get(ID="f50ec0b7-f960-400d-91f0-c42a6d44e3d0")
    
    self.query_ra_steps = app_tables.ra_steps.search(file = self.curr_file)
    ra_step_id = [s.get_id() for s in self.query_ra_steps]

    # building the dictionary
    count = 0
    
    for s in ra_step_id:
      count = count+1
      gi_steps = app_tables.gi_steps.search(
        ra_step = app_tables.ra_steps.get_by_id(s)
      )
      gi_ids = [r.get_id() for r in gi_steps]
      self.data[count] = gi_ids
      
    
    alert(self.data)
    
              
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

    # Create the dictionary
    test_dict = {1 : ['0001', '0002']} # step : [gi steps]
    
    

  def btn_next_question_click(self, **event_args):
    """This method is called when the button is clicked"""

    ra = self.curr_ra_step
    gi = self.curr_gi_step
    data = {1 : 2, 2 : 3} 
    iterate = self.itr(data)
    
    if iterate == False:
      question = app_tables.question.get(
      gi_step = app_tables.gi_steps.get_by_id(499134,763054673)
    )
    else:
      pass


    