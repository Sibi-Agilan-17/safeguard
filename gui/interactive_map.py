from tkintermapview import TkinterMapView
import ttkbootstrap as ttk

class InteractiveMapPage:
    """
    Displays an interactive map for locating nearby facilities and shows emergency contact information.
    """
    def __init__(self, parent, on_back_callback):
        self.parent = parent
        self.on_back_callback = on_back_callback
        self._setup_ui()

    def _setup_ui(self):
        """
        Sets up the interactive map UI.
        """
        # Map View
        self.map_view = TkinterMapView(self.parent, width=375, height=500, corner_radius=0)
        self.map_view.pack(pady=10)
        self.map_view.set_position(13.0827, 80.2707)  # Default: Chennai, India
        self.map_view.set_zoom(10)

        # Emergency Contact
        self.emergency_contact_label = ttk.Label(self.parent, text="Emergency Contact: 112", font=("Arial", 12, "bold"), bootstyle="danger")
        self.emergency_contact_label.pack(pady=10)

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
        self.map_view.destroy()
        self.emergency_contact_label.destroy()
        self.back_button.destroy()