from ._anvil_designer import MainPageTemplate
from anvil import *
import anvil.server as server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import uuid

class MainPage(MainPageTemplate):
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Declare instance variables
    self.curr_file = None
    self.curr_ra_step = 0
    self.curr_gi_step = 0
    self.query_ra_steps = None
    self.data = {} # Task: might not need it
    self.question = None

    # temp data storage
    self.lo = ""
    self.milestones = []
    self.gi_steps = {} # Task: might not need it
    self.inquiries = []
    
    # Any code you write here will run before the form opens.
    self.author_page1.visible = False
    self.author_page2.visible = False
    self.author_page3.visible = False
    self.author_page4.visible = False
    self.author_page5.visible = False
    self.student_page1.visible = True
    self.student_page2.visible = False

    self.curr_file = app_tables.files.get(
      id = '72274cd6-2491-bc38-aa02-4cc2e53a986d'
    )

    # Testing the student end
    self.title.text = self.curr_file['title']
    self.inquiries = self.curr_file['inquiries']
    self.question = self.inquiries[0][0]
    self.rtext_student_context.content = self.question['context']
    self.rtext_student_prompt.content = self.question['prompt']
    self.rpanel_student_options.items = self.question['options']

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

  def get_gi_id(self):
    curr_gi = app_tables.gi_steps.get(
      ra_step = app_tables.ra_steps.get(
        file = self.curr_file,
        serial = self.curr_ra_step 
      ),
      serial = self.curr_gi_step
    )
    curr_gi_step_id = curr_gi.get_id()
    return curr_gi_step_id # Task: we don't need it (remove)

  def disp_question_data(self):
    self.tarea_context.text = self.question['context']
    self.tarea_prompt.text = self.question['prompt']
    self.rpanel_options.items = self.question['options']
    '''self.title.text = f"Step {self.curr_ra_step} (question {self.curr_gi_step}/{len(self.data[self.curr_ra_step])}):"
    # Task: Figure out how to handle the title'''
  
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

    # self.curr_file_id = self.curr_file.get_id() # Task: i don't need it (remove)

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
      serial = int(s['serial'])
      objective = s['objective']
      list_gi_steps = server.call('gi', serial, self.milestones, self.lo, objective) # Task: Add another parameter, the outline (list)
      
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
      temp_q_list = []
      for q in s['gi_steps']:
        gi_step = q
        objective = s['objective']
        
        context, prompt, options = server.call('inquiry', objective, gi_step)

        # convert list of strings into list of dicts to display the options
        choices = [] # list of options as dictionaries
        for i in options:
          d = {
            'title': i
          }
          choices.append(d)
 
        
        # create the list of questions in the gi
        question = {
          'question': gi_step['question'],
          'context': context,
          'prompt': prompt,
          'options': choices
        }
        temp_q_list.append(question)
      self.inquiries.append(temp_q_list)
        
    # ------ displaying the data ------

    self.title.text = f"Step 1 question: 1 of {len(self.inquiries[0])}"
    self.question = self.inquiries[0][0]
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

    iterate = self.itr()
    self.title.text = f"Step {self.curr_ra_step+1} question: {self.curr_gi_step+1} of {len(self.inquiries[self.curr_ra_step])}"
    self.title.scroll_into_view()
  
    if iterate == False and self.question != None:
      #id = self.get_gi_id() - to be used when querying from the DB
      '''self.question = app_tables.question.get(
        gi_step = app_tables.gi_steps.get_by_id(id)
      )'''
      self.question = self.inquiries[self.curr_ra_step][self.curr_gi_step]
      self.disp_question_data() # update ui content
    else:
      self.author_page4.visible = False
      self.author_page5.visible = True
      self.title.text = self.curr_file['title'] # Task: review it
      
  def btn_go_home_click(self, **event_args):
    """This method is called when the button is clicked"""

    # ------ save data in the DB ------

    self.curr_file.update(
      milestones = self.milestones,
      inquiries = self.inquiries
    )
    
    '''for s in self.milestones:
      # save data in the ra_steps - table
      app_tables.ra_steps.add_row(
        title = s['title'],
        serial = int(s['serial']),
        objective = s['objective'],
        instruction = s['instruction'],
        file = self.curr_file
        # Task: map the steps with the current file 
      )

      # querying data to refer to and update
      ra_step = app_tables.ra_steps.get(
          file = self.curr_file,
          serial = int(s['serial'])
        )
      
      # save data in the gi_steps - table 
      gis = s['gi_steps']
      for i in gis:
        app_tables.gi_steps.add_row(
          title = i['question'],
          serial = int(i['serial']),
          ra_step = ra_step,
          file = self.curr_file
          # Task: map the steps with the current file
        )
  
      # map gi_steps with ra_steps - table
      gi_steps = app_tables.gi_steps.search(
        ra_step = ra_step
      )
      ra_step.update(
        gi_steps = app_tables.gi_steps.search(
          ra_step = ra_step
        )
      )
      
      # save the inquiries in the question - table
      for q in self.inquiries[s]:
        for c in q['options']:
          app_tables.options.add_row(
            title = c['title'],
            question = q
          )
        options = app_tables.options.search()
        app_tables.question.add_row(
          prompt = q['prompt'],
          context = q['context'],
          options = app_tables.options.search(
            question = q
          )
        )'''
    
    self.title.scroll_into_view()
    self.reset()
    pass

  # ------ event listeners (student end) ------

  def btn_student_next_question_click(self, **event_args):
    """This method is called when the button is clicked"""
    iterate = self.itr()
    self.title.scroll_into_view()
  
    if iterate == False and self.question != None:
      #id = self.get_gi_id() - to be used when querying from the DB
      '''self.question = app_tables.question.get(
        gi_step = app_tables.gi_steps.get_by_id(id)
      )'''
      self.question = self.inquiries[self.curr_ra_step][self.curr_gi_step]
      self.disp_question_data() # update ui content
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