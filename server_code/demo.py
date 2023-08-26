import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import uuid

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42

@anvil.server.callable
def outline(ilo, filename):
  u_id = str(uuid.uuid4())
  app_tables.ilo.add_row(title_ilo=ilo)
  list = []
  for i in app_tables.ilo.search(title_ilo = ilo):
    list.append(i) 
  app_tables.files.add_row(ilo = list, ID = u_id, filename = filename)