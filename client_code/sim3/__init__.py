from ._anvil_designer import sim3Template
from anvil import *
import anvil.server
import random

class sim3(sim3Template):
    def __init__(self, **properties):
        self.init_components(**properties)

        # Initialize your 'b' elements
        self.bs = [{'color': color, 'x': 0, 'y': i*100+50} for i, color in enumerate(['red', 'blue', 'green', 'yellow'])]

        # Initialize your 'd' elements
        self.ds = [Label(text=f"Mass: {random.uniform(15, 75):.2f}\nForce: {random.uniform(50, 350):.2f}") for _ in range(4)]

        # Add 'd' elements to a FlowPanel for layout
        self.canvas_1.add_component(*self.ds)

        # Add onclick events to your buttons
        self.button_e.set_event_handler('click', self.on_button_e_click)
        self.button_f.set_event_handler('click', self.on_button_f_click)

    def on_button_e_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.button_e.enabled = False
        self.animate()

    def animate(self):
        finished = False
        for b, d in zip(self.bs, self.ds):
            mass = float(d.text.split(": ")[1].split("\n")[0])
            force = float(d.text.split(": ")[2])
            acceleration = force / mass
            b['x'] += acceleration
            if b['x'] >= self.canvas_1.get_width() - 50:
                finished = True
                b['x'] = self.canvas_1.get_width() - 50
                self.button_f.enabled = True
            else:
                # Redraw the rectangle at the new position
                self.canvas_1.draw_rect(x=b['x'], y=b['y'], width=50, height=50, fill=b['color'])
        if not finished:
            call_in_background(self.animate)

    def on_button_f_click(self, **event_args):
        """This method is called when the button is clicked"""
        for b in self.bs:
            b['x'] = 0
            # Redraw the rectangle at the new position
            self.canvas_1.draw_rect(x=b['x'], y=b['y'], width=50, height=50, fill=b['color'])
        self.button_e.enabled = True
