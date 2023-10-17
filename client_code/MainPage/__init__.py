import uuid
import anvil.js
import anvil.users
from anvil import *
import anvil.server as server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ._anvil_designer import MainPageTemplate


class MainPage(MainPageTemplate):
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    '''# Declare instance variables
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
    self.inquiries = []'''

    # preventing unusual horizontal scrolling on mobile
    is_mobile = anvil.js.call_js(
      '''
        function() {
          return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
        }
      '''
    )

    if is_mobile:
      self.col_spacing = 'none'
    
    '''# Any code you write here will run before the form opens.
    self.student_page1.visible = True
    self.student_page_end.visible = False

    # Testing the student end // Task: remove this
    self.curr_file = app_tables.files.get(
      id = 'demo'
    )
    
    self.inquiries = self.curr_file['inquiries']
    self.question = self.inquiries[0][0]
    #self.interactive_component.html = server.call('restore_html', self.question['code'])
    self.title.text = self.question['question'] # Task: restore actual code: f"Step {1} question: {1} of {len(self.inquiries[0])}"
    self.rtext_student_context.content = self.question['context']
    self.rtext_student_prompt.content = self.question['inquiry']
    self.rpanel_student_options.items = self.question['options']'''

  def btn_student_next_question_click(self, **event_args):
    if self.inquiry10.visible is True:
      self.title.scroll_into_view()
      self.inquiry10.visible = False
      self.inquiry21.visible = True
      pass
    elif self.inquiry21.visible is True:
      self.title.scroll_into_view()
      self.inquiry21.visible = False
      self.inquiry22.visible = True
      pass
    elif self.inquiry22.visible is True:
      self.title.scroll_into_view()
      self.inquiry22.visible = False
      self.inquiry31.visible = True
      pass
    elif self.inquiry31.visible is True:
      self.title.scroll_into_view()
      self.inquiry31.visible = False
      self.inquiry32.visible = True
      pass
    elif self.inquiry32.visible is True:
      self.title.scroll_into_view()
      self.inquiry32.visible = False
      self.inquiry40.visible = True
      pass
    elif self.inquiry40.visible is True:
      self.title.scroll_into_view()
      self.inquiry40.visible = False
      self.inquiry51.visible = True
      pass
    elif self.inquiry51.visible is True:
      self.title.scroll_into_view()
      self.inquiry51.visible = False
      self.inquiry52.visible = True
      pass
    elif self.inquiry52.visible is True:
      self.title.scroll_into_view()
      self.inquiry52.visible = False
      self.inquiry61.visible = True
      pass
    elif self.inquiry61.visible is True:
      self.title.scroll_into_view()
      self.inquiry61.visible = False
      self.inquiry62.visible = True
      pass

  def wrong(self, **event_args):
    """This method is called when this radio button is selected"""
    pass
    

  def right(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.rtext_student_prompt_copy_11.visible is True:
      self.rtext_student_prompt_copy_11.visible = False
    else:
      self.rtext_student_prompt_copy_11.visible = True
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.rtext_student_prompt_copy_10.visible is True:
      self.rtext_student_prompt_copy_10.visible = False
    else:
      self.rtext_student_prompt_copy_10.visible = True
    pass

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.rtext_student_prompt_copy_12.visible is True:
      self.rtext_student_prompt_copy_12.visible = False
    else:
      self.rtext_student_prompt_copy_12.visible = True
    pass

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.rtext_student_prompt_copy_13.visible is True:
      self.rtext_student_prompt_copy_13.visible = False
    else:
      self.rtext_student_prompt_copy_13.visible = True
    pass
    
  def button_5_click(self, **event_args):
    if self.rtext_student_prompt_copy_15.visible is True:
      self.rtext_student_prompt_copy_15.visible = False
    else:
      self.rtext_student_prompt_copy_15.visible = True
    pass
    
  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.rtext_student_prompt_copy_16.visible is True:
      self.rtext_student_prompt_copy_16.visible = False
    else:
      self.rtext_student_prompt_copy_16.visible = True
    pass

  def button_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_box_1.visible is True:
      self.text_box_1.visible = False
    else:
      self.text_box_1.visible = True
    pass

  def button_8_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_box_1_copy_2.visible is True:
      self.text_box_1_copy_2.visible = False
    else:
      self.text_box_1_copy_2.visible = True
    pass

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    self.condition_1 = self.text_box_1.text
    alert(self.condition_1)
    pass

  def text_box_1_copy_2_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    self.condition_2 = self.text_box_1_copy_2.text
    alert(self.condition_2)
    pass








