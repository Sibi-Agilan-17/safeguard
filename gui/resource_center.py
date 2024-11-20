import webbrowser
import json
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class ResourceCenterPage:
    """
    Displays resources for disaster preparedness.
    """
    def __init__(self, parent, on_back_callback):
        self.parent = parent
        self.on_back_callback = on_back_callback
        self.resources = self.load_resources()
        self._setup_ui()

    def load_resources(self):
        """
        Loads resources from a JSON file.
        """
        try:
            with open(r"C:\Users\sibia\PycharmProjects\codessey\assets\data\resource_links.json", 'r') as file:
                return json.load(file)['resources']
        except FileNotFoundError:
            return {'General': ['Error loading resources.']}

    def _setup_ui(self):
        """
        Sets up the resource center UI.
        """
        # Title
        self.title_label = ttk.Label(self.parent, text='Resource Center', font=('Arial', 16, 'bold'), bootstyle='inverse-info')
        self.title_label.pack(pady=10)

        # Resource Links
        self.resource_labels = []
        for category, links in self.resources.items():
            category_label = ttk.Label(self.parent, text=category, font=('Arial', 12, 'bold'))
            category_label.pack(anchor=W, padx=20, pady=5)
            self.resource_labels.append(category_label)
            for link in links:
                link_label = ttk.Label(self.parent, text=link, bootstyle='primary', cursor="hand2")
                link_label.pack(anchor=W, padx=40)
                link_label.bind("<Button-1>", lambda e, url=link: self.open_link(url))
                self.resource_labels.append(link_label)

        # Navigation
        self.back_button = ttk.Button(self.parent, text='Back', bootstyle='outline-secondary', command=self.on_back)
        self.back_button.pack(pady=10)

    def open_link(self, url):
        """
        Opens the given URL in the web browser.
        """
        webbrowser.open_new(url)

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
        for label in self.resource_labels:
            label.destroy()
        self.back_button.destroy()