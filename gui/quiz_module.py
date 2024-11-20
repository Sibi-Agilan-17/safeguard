import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import json
from random import shuffle

class QuizModule:
    """
    A quiz to test knowledge about disaster preparedness.
    """
    def __init__(self, parent, on_back_callback):
        self.parent = parent
        self.on_back_callback = on_back_callback
        self.questions = self.load_questions()
        shuffle(self.questions)
        self.current_index = 0
        self.score = 0
        self._setup_ui()

    def load_questions(self):
        """
        Loads quiz questions from a JSON file.
        """
        try:
            with open(r"C:\Users\sibia\PycharmProjects\codessey\assets\data\quiz_questions.json", "r") as file:
                return json.load(file)["questions"]
        except FileNotFoundError:
            return [{"question": "Error loading questions.", "options": ["Retry"], "answer": 0}]

    def _setup_ui(self):
        """
        Sets up the quiz UI.
        """
        # Title
        self.title_label = ttk.Label(self.parent, text="Disaster Preparedness Quiz", font=("Arial", 16, "bold"), bootstyle="inverse-primary")
        self.title_label.pack(pady=10)

        # Question Display
        self.question_label = ttk.Label(self.parent, text="", font=("Arial", 12), wraplength=350, anchor=CENTER)
        self.question_label.pack(pady=20)

        # Options
        self.option_buttons = []
        for i in range(4):
            button = ttk.Button(self.parent, text="", bootstyle="outline-primary", command=lambda i=i: self.check_answer(i))
            button.pack(fill=X, padx=20, pady=5)
            self.option_buttons.append(button)

        # Navigation
        self.back_button = ttk.Button(self.parent, text="Back", bootstyle="outline-secondary", command=self.on_back)
        self.back_button.pack(pady=10)

        self.load_next_question()

    def load_next_question(self):
        """
        Loads the next question or displays the score.
        """
        if self.current_index < len(self.questions):
            question = self.questions[self.current_index]
            self.question_label.config(text=question["question"])
            for i, option in enumerate(question["options"]):
                self.option_buttons[i].config(text=option, bootstyle="outline-primary")
        else:
            self.display_score()

    def check_answer(self, selected_index):
        """
        Checks the user's answer and updates the score.
        """
        correct_index = self.questions[self.current_index]["answer"]
        if selected_index == correct_index:
            self.option_buttons[selected_index].config(bootstyle="success")
            self.score += 1
        else:
            self.option_buttons[selected_index].config(bootstyle="danger")
            self.option_buttons[correct_index].config(bootstyle="success")

        self.parent.after(1000, self.load_next_question)
        self.current_index += 1

    def display_score(self):
        """
        Displays the user's score.
        """
        self.question_label.config(text=f"Your Score: {self.score}/{len(self.questions)}")
        for button in self.option_buttons:
            button.pack_forget()

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
        self.title_label.destroy()
        self.question_label.destroy()
        for button in self.option_buttons:
            button.destroy()
        self.back_button.destroy()