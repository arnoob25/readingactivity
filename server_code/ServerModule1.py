import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.server

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
#
@anvil.server.callable
def start_animation(form_id):
    form = anvil.server.get_session(form_id)
    
    while form.car.left < form.container.width - form.car.width - 2:
        form.speed -= form.brake_force / form.mass
        if form.speed < 0:
            form.speed = 0

        new_pos = form.car.left + form.speed
        if new_pos > max_pos:
            new_pos = max_pos

        form.car.left = new_pos

        if new_pos >= form.threshold.left:
            form.message.text = 'Failure'
            break
        elif speed == 0 and new_pos < threshold.left:
            form.message.text = 'Success'
            break

        time.sleep(0.01)  # Wait a bit before the next frame

    form.reset_button.enabled = True
