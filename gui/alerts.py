import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import json

class AlertsPage:
    """
    Displays disaster alerts based on location.
    """
    def __init__(self, parent, on_back_callback):
        self.parent = parent
        self.on_back_callback = on_back_callback
        self.alerts = self.load_alerts()
        self._setup_ui()

    def load_alerts(self):
        """
        Loads disaster alerts from a JSON file.
        """
        try:
            with open("assets/data/disaster_alerts.json", "r") as file:
                return json.load(file)["alerts"]
        except FileNotFoundError:
            return ["No alerts available."]

    def _setup_ui(self):
        """
        Sets up the alerts UI.
        """
        # Title
        self.title_label = ttk.Label(self.parent, text="Disaster Alerts", font=("Arial", 16, "bold"), bootstyle="inverse-danger")
        self.title_label.pack(pady=10)

        # Alert List
        self.alert_labels = []
        for alert in self.alerts:
            alert_label = ttk.Label(self.parent, text=alert, wraplength=350, bootstyle="danger")
            alert_label.pack(fill=X, pady=5)
            self.alert_labels.append(alert_label)

        # Navigation
        self.back_button = ttk.Button(self.parent, text="Back", bootstyle="outline-secondary", command=self.on_back)
        self.back_button.pack(pady=10)

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
        for label in self.alert_labels:
            label.destroy()
        self.back_button.destroy()