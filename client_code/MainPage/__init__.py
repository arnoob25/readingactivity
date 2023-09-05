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
    self.curr_ra_step = 0
    self.curr_gi_step = 0
    self.query_ra_steps = None
    self.data = {} # Task: might not need it
    self.question = None

    # temp data storage
    self.lo = ""
    self.milestones = []
    self.gi_steps = {} # Task: might not need it
    self.inquiries = [
    [
        {
            "question": "Can you tell me what are the four valves in the heart and their locations?",
            "context": "An interactive simulation would be an effective tool to aid the student in achieving the goal of this question. The simulation could show a cross-section of the heart with the four valves and their locations. The student could interact with the simulation by clicking on each valve to see how it opens and closes, coordinating with the contraction and relaxation of the heart. The simulation could also show what happens when a valve does not function properly, such as blood flowing in the wrong direction or not flowing at all.",
            "prompt": "1:1 What do you observe when you click on each valve in the simulation? Can you describe what happens when a valve does not function properly?",
            "options": [
                {"title": "Blood flows in the wrong direction"},
                {"title": "Blood does not flow at all"},
                {"title": "Blood flow is not affected"},
                {"title": "The heart stops beating"},
            ],
        },
        {
            "question": "Can you explain how these valves regulate blood flow through the heart?",
            "context": "An interactive simulation would be an effective tool to aid the student in achieving the goal of this question. The simulation could show a cross-section of the heart with the four valves and their locations. The student could interact with the simulation by clicking on each valve to see how it opens and closes, coordinating with the contraction and relaxation of the heart. The simulation could also show what happens when a valve does not function properly, such as blood flowing in the wrong direction or not flowing at all.",
            "prompt": "1:2 What do you observe when you click on each valve in the simulation? Can you describe what happens when a valve does not function properly?",
            "options": [
                {"title": "Blood flows in the wrong direction"},
                {"title": "Blood does not flow at all"},
                {"title": "Blood flow is not affected"},
                {"title": "The heart stops beating"},
            ],
        },
        {
            "question": "Can you describe how the opening and closing of these valves are coordinated with the contraction and relaxation of the heart?",
            "context": "An interactive simulation would be an effective tool to aid the student in achieving the goal of this question. The simulation could show a cross-section of the heart with the four valves and their locations. The student could interact with the simulation by clicking on each valve to see how it opens and closes, coordinating with the contraction and relaxation of the heart. The simulation could also show what happens when a valve does not function properly, such as blood flowing in the wrong direction or not flowing at all.",
            "prompt": "1:3 What do you observe when you click on each valve in the simulation? Can you describe what happens when a valve does not function properly?",
            "options": [
                {"title": "Blood flows in the wrong direction"},
                {"title": "Blood does not flow at all"},
                {"title": "Blood flow is not affected"},
                {"title": "The heart stops beating"},
            ],
        },
        {
            "question": "Can you explain how this coordination ensures that blood flows in only one direction through the heart?",
            "context": "An interactive simulation would be an effective tool to aid the student in achieving the goal of this question. The simulation could show a cross-section of the heart with the four valves and their locations. The student could interact with the simulation by clicking on each valve to see how it opens and closes, coordinating with the contraction and relaxation of the heart. The simulation could also show what happens when a valve does not function properly, such as blood flowing in the wrong direction or not flowing at all.",
            "prompt": "1:4 What do you observe when you click on each valve in the simulation? Can you describe what happens when a valve does not function properly?",
            "options": [
                {"title": "Blood flows in the wrong direction"},
                {"title": "Blood does not flow at all"},
                {"title": "Blood flow is not affected"},
                {"title": "The heart stops beating"},
            ],
        },
    ],
    [
        {
            "question": "Can you tell me what are the four valves in the heart and their locations?",
            "context": "An interactive simulation would be an effective tool to aid the student in achieving the goal of this question. The simulation could show a cross-section of the heart with the four valves and their locations. The student could interact with the simulation by clicking on each valve to see how it opens and closes, coordinating with the contraction and relaxation of the heart. The simulation could also show what happens when a valve does not function properly, such as blood flowing in the wrong direction or not flowing at all.",
            "prompt": "2:1 What do you observe when you click on each valve in the simulation? Can you describe what happens when a valve does not function properly?",
            "options": [
                {"title": "Blood flows in the wrong direction"},
                {"title": "Blood does not flow at all"},
                {"title": "Blood flow is not affected"},
                {"title": "The heart stops beating"},
            ],
        },
        {
            "question": "Can you explain how these valves regulate blood flow through the heart?",
            "context": "An interactive simulation would be an effective tool to aid the student in achieving the goal of this question. The simulation could show a cross-section of the heart with the four valves and their locations. The student could interact with the simulation by clicking on each valve to see how it opens and closes, coordinating with the contraction and relaxation of the heart. The simulation could also show what happens when a valve does not function properly, such as blood flowing in the wrong direction or not flowing at all.",
            "prompt": "2:2 What do you observe when you click on each valve in the simulation? Can you describe what happens when a valve does not function properly?",
            "options": [
                {"title": "Blood flows in the wrong direction"},
                {"title": "Blood does not flow at all"},
                {"title": "Blood flow is not affected"},
                {"title": "The heart stops beating"},
            ],
        },
        {
            "question": "Can you describe how the opening and closing of these valves are coordinated with the contraction and relaxation of the heart?",
            "context": "An interactive simulation would be an effective tool to aid the student in achieving the goal of this question. The simulation could show a cross-section of the heart with the four valves and their locations. The student could interact with the simulation by clicking on each valve to see how it opens and closes, coordinating with the contraction and relaxation of the heart. The simulation could also show what happens when a valve does not function properly, such as blood flowing in the wrong direction or not flowing at all.",
            "prompt": "2:3 What do you observe when you click on each valve in the simulation? Can you describe what happens when a valve does not function properly?",
            "options": [
                {"title": "Blood flows in the wrong direction"},
                {"title": "Blood does not flow at all"},
                {"title": "Blood flow is not affected"},
                {"title": "The heart stops beating"},
            ],
        },
        {
            "question": "Can you explain how this coordination ensures that blood flows in only one direction through the heart?",
            "context": "An interactive simulation would be an effective tool to aid the student in achieving the goal of this question. The simulation could show a cross-section of the heart with the four valves and their locations. The student could interact with the simulation by clicking on each valve to see how it opens and closes, coordinating with the contraction and relaxation of the heart. The simulation could also show what happens when a valve does not function properly, such as blood flowing in the wrong direction or not flowing at all.",
            "prompt": "2:4 What do you observe when you click on each valve in the simulation? Can you describe what happens when a valve does not function properly?",
            "options": [
                {"title": "Blood flows in the wrong direction"},
                {"title": "Blood does not flow at all"},
                {"title": "Blood flow is not affected"},
                {"title": "The heart stops beating"},
            ],
        },
    ],
]
    
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
    self.curr_ra_step = 0
    self.curr_gi_step = 0
    self.query_ra_steps = None
    self.data = {}
    self.question = None
    
    self.title.text = "Author a Reading Activity"
    self.author_page1.visible = True
    self.author_page2.visible = False
    self.author_page3.visible = False
    self.author_page4.visible = False
    self.author_page5.visible = False
           
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

    self.title.text = f"Step 1 question: 1 of {len(self.inquiries[0])}"
    self.title.scroll_into_view()
    self.author_page3.visible = False
    self.author_page4.visible = True
    
    # ------ making inference ------

    '''for s in self.milestones:
      temp_q_list = []
      for q in s['gi_steps']:
        gi_step = q
        objective = s['objective']
        
        context, prompt, options, assessment = server.call('inquiry', objective, gi_step)

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
      self.inquiries.append(temp_q_list)'''
        
    # ------ displaying the data ------

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
      self.title.text = self.curr_file['title']
      
  def btn_go_home_click(self, **event_args):
    """This method is called when the button is clicked"""

    # ------ save data in the DB ------

    # ra_step
    for s in self.milestones:
      app_tables.ra_steps.add_row(
        title-ra_step=
      )
    
    # Task: Have to save the self.milestones data into the DB
    # Task: have to save the self.gi_steps data into the DB
    # Task: map gi_steps (DB row) to corresponding ra_steps in the ra_step table
    
    self.title.scroll_into_view()
    self.reset()
    pass