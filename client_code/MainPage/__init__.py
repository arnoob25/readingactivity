from ._anvil_designer import MainPageTemplate
from anvil import *
import anvil.server as server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import uuid
import anvil.js

class MainPage(MainPageTemplate):
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Declare instance variables
    self.curr_file = None
    self.curr_ra_step = 0
    self.curr_gi_step = 0
    self.query_ra_steps = None # Task: might not need it
    self.data = {} # Task: might not need it
    self.question = None # Task: might not need it

    # temp data storage
    self.lo = ""
    self.milestones = []
    self.gi_steps = {} # Task: might not need it
    self.inquiries = []

    # prevent horizontal scrolling on mobile
    is_mobile = anvil.js.call_js(
      '''
        function() {
          return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
        }
      '''
    )

    if is_mobile:
      self.col_spacing = 'none'
    
    
    # Any code you write here will run before the form opens.
    self.author_page1.visible = False
    self.author_page2.visible = False
    self.author_page3.visible = False
    self.author_page4.visible = False
    self.author_page5.visible = False
    self.student_page1.visible = True
    self.student_page2.visible = False

    '''# Testing the student end // Task: remove this
    self.curr_file = app_tables.files.get(
      id = '72274cd6-2491-bc38-aa02-4cc2e53a986d'
    )
    self.title.text = self.curr_file['title']
    self.inquiries = self.curr_file['inquiries']
    self.question = self.inquiries[0][0]
    self.rtext_student_context.content = self.question['context']
    self.rtext_student_prompt.content = self.question['prompt']
    self.rpanel_student_options.items = self.question['options']'''

  # ------ helper functions ------ 
  
  def reset(self):
    # Task: review if everything is being reset properly
    self.curr_file = None
    self.curr_ra_step = 0
    self.curr_gi_step = 0
    self.query_ra_steps = None
    self.data = {}
    self.question = None
    self.lo = ""
    self.milestones = []
    self.gi_steps = {} # Task: might not need it
    self.inquiries = []
    
    self.title.text = "Author a Reading Activity"
    self.author_page1.visible = True
    self.author_page2.visible = False
    self.author_page3.visible = False
    self.author_page4.visible = False
    self.author_page5.visible = False
    self.student_page1.visible = False
    self.student_page1.visible = False
           
  def itr(self):
      end = False
      if self.curr_gi_step+1 <= len(self.inquiries[self.curr_ra_step])-1:
        self.curr_gi_step = self.curr_gi_step + 1
        #alert(f"(Incr gi) ra: {self.curr_ra_step} of {len(self.inquiries)}, gi: {self.curr_gi_step} of {len(self.inquiries[self.curr_ra_step])}")
      elif self.curr_ra_step+1 <= len(self.inquiries)-1:
        self.curr_ra_step = self.curr_ra_step + 1
        self.curr_gi_step = 0
        #alert(f"(Incr ra) ra: {self.curr_ra_step}, gi: {self.curr_gi_step}")
      else:
        end = True

      return end
    
  def update_inquiry(self):

      # ------ making inference ------

      ra = self.curr_ra_step
      gi = self.curr_gi_step
      curr_inquiry = self.inquiries[ra][gi]
    
      step = self.milestones[ra]
      objective = step['objective']
      gi_step = step['gi_steps'][gi]['question']
      context, inquiry, options = server.call('inquiry', objective, gi_step)

      # ------ updating inference data into the inquiry - list ------

      dic = {'context': context, 'inquiry': inquiry, 'options': options}
      update_data = curr_inquiry
      update_data.update(dic)
    
      # ------ displaying the data ------

      self.title.text = f"Step {ra+1} question: {gi+1} of {len(self.inquiries[ra])}"
      self.question = curr_inquiry
      
      self.tarea_context.text = self.question['context']
      self.tarea_prompt.text = self.question['inquiry']
      self.rpanel_options.items = self.question['options']
  
  # ------ event listeners (author end) ------

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

    # ------ saving data in the DB ------

    try:
      query_ilo = app_tables.ilo.get(title_ilo = ilo)
    except:
      app_tables.ilo.add_row(title_ilo = ilo)
      
    self.id = str(uuid.uuid4())
    app_tables.files.add_row(
      title = filename,
      id = self.id,
      User = anvil.users.get_user(),
      ilo = app_tables.ilo.get(title_ilo = ilo),
    )

    self.curr_file = app_tables.files.get(
      id = self.id
    )

  def btn_gen_gi_click(self, **event_args):
    """This method is called when the button is clicked"""

    # ------ basic ui logic ------

    self.title.text = "Steps with Guided Inquiries:"
    self.title.scroll_into_view()
    self.author_page2.visible = False
    self.author_page3.visible = True

    # ------ making inference ------

    for s in self.milestones:
      serial = int(s['serial'])
      objective = s['objective']
      list_gi_steps = server.call('gi', serial, self.milestones, self.lo, objective)
      
      # adding the gi_steps list to the dictionary
      self.milestones[self.milestones.index(s)]['gi_steps'] = list_gi_steps

    # ------ saving data in the DB ------
    # saving the milestones to prevent data loss due to unexpected issues

    self.curr_file.update(
      milestones = self.milestones
    )

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
      temp_q_list = []
      for q in s['gi_steps']:
        
        # create the list of questions in the gi
        question = {
          'question': q['question']
        }

        temp_q_list.append(question)
      self.inquiries.append(temp_q_list)
        
    # ------ displaying the data ------

    self.update_inquiry()
    
  def btn_next_question_click(self, **event_args):
    """This method is called when the button is clicked"""

    iterate = self.itr() # updates curr_ra_step and curr_gi_step, and returns True when reached the end
    self.title.scroll_into_view()
  
    if iterate == False and self.question is not None: # didn't reach the end and the question was updated with a valid inquiry
      self.update_inquiry()
    else:
      self.author_page4.visible = False
      self.author_page5.visible = True
      self.title.text = self.curr_file['title']
      
  def btn_go_home_click(self, **event_args):
    """This method is called when the button is clicked"""

    # ------ save data in the DB ------

    self.curr_file.update(
      milestones = self.milestones,
      inquiries = self.inquiries
    )
    
    self.title.scroll_into_view()
    self.reset()
    pass

  # ------ event listeners (student end) ------

  def btn_student_next_question_click(self, **event_args):
    """This method is called when the button is clicked"""
    iterate = self.itr()
    self.title.scroll_into_view()
  
    if iterate == False and self.question is not None:
      self.update_inquiry()
    else:
      self.student_page1.visible = False
      self.student_page2.visible = True
      self.title.text = self.curr_file['title'] # Task: review it
    pass

  def btn_student_go_home_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.title.scroll_into_view()
    self.reset()
    self.author_page1.visible = False
    self.student_page1.visible = True
    pass
