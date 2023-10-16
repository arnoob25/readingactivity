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

    # preventing unusual horizontal scrolling on mobile
    is_mobile = anvil.js.call_js(
      '''
        function() {
          return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
        }
      '''
    )

    self.inquiry10.visible = True
    
    if is_mobile:
      self.col_spacing = 'none'
    

  def btn_student_next_question_click(self, **event_args):
    if self.inquiry10.visible is True:
      self.inquiry10.visible = False
      self.inquiry21.visible = True
      pass
    elif self.inquiry21.visible is True:
      self.title.scroll_into_view()
      self.inquiry21.visible = False
      self.inquiry22.visible = True
      pass
    elif self.inquiry22.visible is True:
      self.inquiry22.visible = False
      self.inquiry31.visible = True
      pass
