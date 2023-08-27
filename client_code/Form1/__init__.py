from ._anvil_designer import Form1Template
from anvil import *
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
    self.curr_gi_step = 3
    self.query_ra_steps = None
    self.data = {}
    
    # Any code you write here will run before the form opens.
    self.author_page1.visible = True
    self.author_page2.visible = False
    self.author_page3.visible = False
    self.author_page4.visible = False
    self.author_page5.visible = False

    # review
    self.curr_file = app_tables.files.get(ID="f50ec0b7-f960-400d-91f0-c42a6d44e3d0")

  def reset(self):
    self.curr_file = None
    self.curr_ra_step = 1
    self.curr_gi_step = 1
    self.query_ra_steps = None
    self.data = {}
    
    self.author_page1.visible = True
    self.author_page2.visible = False
    self.author_page3.visible = False
    self.author_page4.visible = False
    self.author_page5.visible = False
           
  def itr(self, dic):
      end = False

      if self.curr_gi_step+1 <= len(dic[self.curr_ra_step]):
        self.curr_gi_step = self.curr_gi_step + 1
      elif self.curr_ra_step+1 in dic:
        self.curr_ra_step = self.curr_ra_step + 1
        self.curr_gi_step = 1
      else: 
        end = True
        self.btn_next_question.text = "Proceed"

      return end

  def btn_gen_outline_click(self, **event_args):
    """This method is called when the button is clicked"""

    self.title.text = "Steps of the Rading Activity:"
    self.author_page1.visible = False
    self.author_page2.visible = True

    self.query_ra_steps = app_tables.ra_steps.search(file = self.curr_file)
    
    self.rpanel_ra_step.items = self.query_ra_steps
    self.rpanel_ra_step2.items = self.query_ra_steps

  def btn_gen_gi_click(self, **event_args):
    """This method is called when the button is clicked"""

    self.title.text = "Steps with Guided Inquiries:"
    self.author_page2.visible = False
    self.author_page3.visible = True

  def btn_gen_question_click(self, **event_args):
    """This method is called when the button is clicked"""

    self.title.text = "Step 30 (question 1/3):"
    self.author_page3.visible = False
    self.author_page4.visible = True

    # Building the Data
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

    # Testing the question fetching [Remove it afterwards]
    curr_gi = app_tables.gi_steps.get(
      ra_step = app_tables.ra_steps.get(
        file = self.curr_file,
        serial = self.curr_ra_step 
      ),
      serial = self.curr_gi_step
    )
    curr_gi_step_id = curr_gi.get_id()
    
    question = app_tables.question.get(
      gi_step= app_tables.gi_steps.get_by_id(curr_gi_step_id)
    )

    # displaying data
    self.rtext_context.content = question['context']
    self.rtext_prompt.content = question['prompt']
    self.rpanel_options.items = question['options']
    
  def btn_next_question_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.author_page5.visible = True
    
    iterate = self.itr(self.data)
    curr_gi = app_tables.gi_steps.get(
      ra_step = app_tables.ra_steps.get(
        file = self.curr_file,
        serial = self.curr_ra_step 
      ),
      serial = self.curr_gi_step
    ) # have to get the current gi_step (this is a query)
    curr_gi_step_id = curr_gi.get_id()
    
    
    if iterate == False:
      question = app_tables.question.get(
      gi_step = app_tables.gi_steps.get_by_id(curr_gi_step_id)
      )
    else:
      self.btn_next_question.text = "Proceed"
      self.author_page4.visible = False
      self.author_page5.visible = True
      self.title.text = self.curr_file['title']

  def btn_go_home_click(self, **event_args):
    """This method is called when the button is clicked"""

    self.reset()
    pass


