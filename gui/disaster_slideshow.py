import json
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class DisasterSlideshow:
    """
    Displays disaster instructions as a visually enhanced slideshow.
    """
    def __init__(self, parent, on_back_callback):
        self.parent = parent
        self.on_back_callback = on_back_callback
        self.current_index = 0
        self.instructions = self.load_disaster_data()

        self._setup_ui()

    def load_disaster_data(self):
        """
        Loads disaster instructions from a JSON file.

        :return: List of instructions.
        """
        try:
            with open(r"C:\Users\sibia\PycharmProjects\codessey\assets\data\disaster_info.json", "r") as file:
                return json.load(file)["instructions"]
        except (FileNotFoundError, KeyError):
            return ["Error loading disaster data. Please check the file."]

    def _setup_ui(self):
        """
        Sets up the UI for the slideshow.
        """
        # Instruction Display
        self.text_area = ttk.Text(self.parent, wrap=WORD, height=15, width=70, font=("Arial", 12))
        self.text_area.pack(pady=20)
        self.text_area.insert(END, self.instructions[self.current_index])
        self.text_area.config(state=DISABLED)

        # Navigation Buttons
        button_frame = ttk.Frame(self.parent)
        button_frame.pack(pady=10)

        self.prev_button = ttk.Button(button_frame, text="Previous", bootstyle="danger", command=self.previous_slide)
        self.prev_button.pack(side=LEFT, padx=5)

        self.back_button = ttk.Button(button_frame, text="Back", bootstyle="outline-secondary", command=self.on_back)
        self.back_button.pack(side=LEFT, padx=5)

        self.next_button = ttk.Button(button_frame, text="Next", bootstyle="success", command=self.next_slide)
        self.next_button.pack(side=LEFT, padx=5)

        self.parent.bind("<Left>", lambda event: self.previous_slide())
        self.parent.bind("<Right>", lambda event: self.next_slide())
        self.parent.bind("<Return>", lambda event: self.next_slide())

    def update_text_area(self):
        """
        Updates the text area with the current instruction.
        """
        self.text_area.config(state=NORMAL)
        self.text_area.delete("1.0", END)
        self.text_area.insert(END, self.instructions[self.current_index])
        self.text_area.config(state=DISABLED)

    def previous_slide(self):
        """
        Navigates to the previous slide, looping to the end if at the beginning.
        """
        self.current_index = (self.current_index - 1) % len(self.instructions)
        self.update_text_area()

    def next_slide(self):
        """
        Navigates to the next slide, looping to the beginning if at the end.
        """
        self.current_index = (self.current_index + 1) % len(self.instructions)
        self.update_text_area()

    def on_back(self):
        """
        Handles the back button click event.
        """
        self._clear_screen()
        self.on_back_callback()

    def _clear_screen(self):
        """
        Clears all widgets from the screen.
        """

        for widget in self.parent.winfo_children():
            widget.destroy()
