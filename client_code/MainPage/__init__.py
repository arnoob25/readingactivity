from ._anvil_designer import MainPageTemplate
from anvil import *
import anvil.server as server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class MainPage(MainPageTemplate):
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Declate instance variables
    self.curr_file = None
    self.curr_ra_step = 1
    self.curr_gi_step = 1
    self.query_ra_steps = None
    self.data = {}
    self.question = None

    # temp data storage
    self.lo = ""
    self.milestones = []
    self.gi_steps = {} # might not need it
    self.inquiries = []
    
    # Any code you write here will run before the form opens.
    self.author_page1.visible = True
    self.author_page2.visible = False
    self.author_page3.visible = False
    self.author_page4.visible = False
    self.author_page5.visible = False

    # review
    self.curr_file = app_tables.files.get(title="Cardiac Cycle")
  
  # ------ helper functions ------ 
  
  def reset(self):
    self.curr_file = None
    self.curr_ra_step = 1
    self.curr_gi_step = 1
    self.query_ra_steps = None
    self.data = {}
    self.question = None
    
    self.title.text = "Author a Reading Activity"
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

      return end

  def get_gi_id(self):
    curr_gi = app_tables.gi_steps.get(
      ra_step = app_tables.ra_steps.get(
        file = self.curr_file,
        serial = self.curr_ra_step 
      ),
      serial = self.curr_gi_step
    )
    curr_gi_step_id = curr_gi.get_id()
    return curr_gi_step_id

  def disp_question_data(self):
    self.tarea_context.text = self.question['context']
    self.tarea_prompt.text = self.question['prompt']
    self.rpanel_options.items = self.question['options']
    '''self.title.text = f"Step {self.curr_ra_step} (question {self.curr_gi_step}/{len(self.data[self.curr_ra_step])}):"
    # Task: Figure out how to handle the title'''
  
  # ------ event listeners ------

  def btn_gen_outline_click(self, **event_args):
    """This method is called when the button is clicked"""

    # ------ basic ui logic ------
    
    self.title.text = "Steps of the Rading Activity:"
    self.title.scroll_into_view()
    self.author_page1.visible = False
    self.author_page2.visible = True
    self.author_page2.scroll_into_view(smooth = False)

    # ------ making inference ------
    
    ilo = self.tbox_ilo.text
    self.milestones, self.lo, filename = server.call('outline',ilo)

    # ------ displaying the data ------
    
    self.rpanel_ra_step.items = self.milestones

    # Task: have to crate new DB item with the filename

    """
    # ------ DB query ------

    # Task: I haven't yet saved the data into the DB, so the data must be loaded from the dictionary
    
    self.query_ra_steps = app_tables.ra_steps.search(file = self.curr_file)
    self.rpanel_ra_step.items = self.query_ra_steps
    self.rpanel_ra_step2.items = self.query_ra_steps
    """
   
  def btn_gen_gi_click(self, **event_args):
    """This method is called when the button is clicked"""

    # ------ basic ui logic ------

    self.title.text = "Steps with Guided Inquiries:"
    self.title.scroll_into_view()
    self.author_page2.visible = False
    self.author_page3.visible = True

    # ------ making inference ------

    for s in self.milestones:
      serial = s['serial']
      objective = s['objective']
      list_gi_steps = server.call('gi', serial, self.lo, objective)
      
      # adding the gi_steps list to the dictionary
      self.milestones[self.milestones.index(s)]['gi_steps'] = list_gi_steps

    # ------ displaying the data ------
    
    self.rpanel_ra_step2.items = self.milestones

  def btn_gen_question_click(self, **event_args):
    """This method is called when the button is clicked"""

    # ------ basic ui logic ------
    
    self.title.scroll_into_view()
    self.author_page3.visible = False
    self.author_page4.visible = True
    
    # ------ making inference ------

    for s in self.milestones:
      for q in s['gi_steps']:
        choices = []
        objective = s['objective']
        gi_step = q
        context, prompt, options, assessment = server.call('inquiry', objective, gi_step)

        # turning the items into dict allows us to display them in the ui
        for i in options:
          d = {
            'title': i
          }
          choices.append(d)
        
        # creating the list of inquiries
        dic = {
          'question': gi_step,
          'context': context,
          'prompt': prompt,
          'options': choices
        }
        self.inquiries.append(dic)
        
    # ------ displaying the data ------

    alert(self.inquiries)
    
    self.question = self.inquiries[0]
    self.disp_question_data()
    
    

    
    """
    # ------ DB query ------
  
    # Building the Data (Task: I might not need it)
    ra_step_id = [s.get_id() for s in self.query_ra_steps]
    count = 0
    for s in ra_step_id:
      count = count+1
      gi_steps = app_tables.gi_steps.search(
        ra_step = app_tables.ra_steps.get_by_id(s)
      )
      gi_ids = [r.get_id() for r in gi_steps]
      self.data[count] = gi_ids

    # Displaying the data
    id = self.get_gi_id()
    
    self.question = app_tables.question.get(
      gi_step= app_tables.gi_steps.get_by_id(id)
    )
    """
    
  def btn_next_question_click(self, **event_args):
    """This method is called when the button is clicked"""

    self.title.scroll_into_view()
    iterate = self.itr(self.data)
  
    if iterate == False and self.question != None:
      #id = self.get_gi_id() - to be used when querying from the DB
      '''self.question = app_tables.question.get(
        gi_step = app_tables.gi_steps.get_by_id(id)
      )'''
      self.question = self.inquiries[self.curr_ra_step, self.curr_gi_step]
      self.disp_question_data() # update ui content
      
    else:
      self.author_page4.visible = False
      self.author_page5.visible = True
      self.title.text = self.curr_file['title']
      
  def btn_go_home_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    # Task: Have to save the self.milestones data into the DB
    # Task: have to save the self.gi_steps data into the DB
    # Task: map gi_steps (DB row) to corresponding ra_steps in the ra_step table
    
    self.title.scroll_into_view()
    self.reset()
    pass