import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from safeguard.gui.quiz_module import QuizModule
from safeguard.gui.alerts import AlertsPage
from safeguard.gui.resource_center import ResourceCenterPage
from safeguard.gui.interactive_map import InteractiveMapPage
from safeguard.core.gps import GPSTracker
from safeguard.gui.disaster_slideshow import DisasterSlideshow


class AppWindow:
    """
    Main window for the emergency preparedness app.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("SafeGuard: Emergency Preparedness")
        self.root.geometry("375x667")  # Mobile-like screen dimensions
        self.root.resizable(False, False)

        # GPS Tracker
        self.gps_tracker = GPSTracker()

        # Emergency Contact
        self.emergency_number = self.get_emergency_number()

        # UI Setup
        self._setup_main_menu()

    def get_emergency_number(self):
        """
        Fetches the emergency number based on the user's current GPS location.
        :return: Emergency number for the detected location.
        """
        country_emergency_numbers = {
            "India": "112",
            "United States": "911",
            "United Kingdom": "999",
            "Australia": "000",
            "Canada": "911",
        }
        coordinates = self.gps_tracker.get_coordinates()
        if coordinates:
            country = self.gps_tracker.g.country
            return country_emergency_numbers.get(country, "112")  # Default to "112" if country not found
        else:
            return "112"  # Default to "112" if GPS fails

    def _setup_main_menu(self):
        """
        Sets up the main menu UI.
        """
        # Title
        ttk.Label(
            self.root,
            text="SafeGuard",
            font=("Arial", 20, "bold"),
            bootstyle="inverse-primary",
        ).pack(fill=X, pady=20)

        # Emergency Number
        ttk.Label(
            self.root,
            text=f"Emergency Number: {self.emergency_number}",
            font=("Arial", 12),
            bootstyle="inverse-danger",
        ).pack(pady=10)

        # Menu Buttons
        menu_frame = ttk.Frame(self.root, padding=20)
        menu_frame.pack(fill=BOTH, expand=True)

        ttk.Button(
            menu_frame,
            text="Disaster Slideshow",
            bootstyle="outline-primary",
            command=self.show_disaster_slideshow,
        ).pack(fill=X, pady=10)

        ttk.Button(
            menu_frame,
            text="Disaster Alerts",
            bootstyle="outline-warning",
            command=self.show_alerts,
        ).pack(fill=X, pady=10)

        ttk.Button(
            menu_frame,
            text="More",
            bootstyle="outline-info",
            command=self._setup_more_menu,
        ).pack(fill=X, pady=10)

        ttk.Button(
            menu_frame,
            text="Exit",
            bootstyle="danger",
            command=self.root.quit,
        ).pack(fill=X, pady=10)

    def _setup_more_menu(self):
        """
        Sets up the more menu UI.
        """
        self._clear_screen()

        # Title
        ttk.Label(
            self.root,
            text="More Options",
            font=("Arial", 20, "bold"),
            bootstyle="inverse-primary",
        ).pack(fill=X, pady=20)

        # Menu Buttons
        menu_frame = ttk.Frame(self.root, padding=20)
        menu_frame.pack(fill=BOTH, expand=True)

        ttk.Button(
            menu_frame,
            text="Resource Center",
            bootstyle="outline-info",
            command=self.show_resource_center,
        ).pack(fill=X, pady=10)

        ttk.Button(
            menu_frame,
            text="Disaster Quiz",
            bootstyle="outline-success",
            command=self.show_quiz,
        ).pack(fill=X, pady=10)

        ttk.Button(
            menu_frame,
            text="Interactive Map",
            bootstyle="outline-secondary",
            command=self.show_interactive_map,
        ).pack(fill=X, pady=10)

        ttk.Button(
            menu_frame,
            text="Back",
            bootstyle="outline-secondary",
            command=self._setup_main_menu,
        ).pack(fill=X, pady=10)

    def show_disaster_slideshow(self):
        """
        Displays the disaster slideshow.
        """
        self._clear_screen()
        DisasterSlideshow(self.root, self._setup_main_menu)
    def show_alerts(self):
        """
        Displays the disaster alerts page.
        """
        self._clear_screen()
        AlertsPage(self.root, self._setup_main_menu)

    def show_resource_center(self):
        """
        Displays the resource center page.
        """
        self._clear_screen()
        ResourceCenterPage(self.root, self._setup_main_menu)

    def show_quiz(self):
        """
        Displays the quiz module.
        """
        self._clear_screen()
        QuizModule(self.root, self._setup_main_menu)

    def show_interactive_map(self):
        """
        Displays the interactive map page.
        """
        self._clear_screen()
        InteractiveMapPage(self.root, self._setup_main_menu)

    def _clear_screen(self):
        """
        Clears all widgets from the screen.
        """
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = ttk.Window(themename="cosmo")  # Modern bootstrap theme
    app = AppWindow(root)
    root.mainloop()