import tkinter as tk
from tkinter import ttk
from core.gps import GPSTracker


class GPSTrackerPage:
    """
    Displays the user's GPS location and allows exporting coordinates.
    """
    def __init__(self, parent):
        self.parent = parent
        self.gps_tracker = GPSTracker()
        self._setup_ui()

    def _setup_ui(self):
        """
        Sets up the UI for the GPS tracker.
        """
        # Coordinates Display
        coords_frame = ttk.Frame(self.parent)
        coords_frame.pack(pady=20)

        self.coords_label = ttk.Label(coords_frame, text="Coordinates: N/A", font=("Arial", 14))
        self.coords_label.pack(pady=10)

        # Fetch Location Button
        fetch_button = ttk.Button(self.parent, text="Get Location", command=self.fetch_location)
        fetch_button.pack(pady=10)

        # Export Button
        export_button = ttk.Button(self.parent, text="Export Location", command=self.export_location)
        export_button.pack(pady=10)

    def fetch_location(self):
        """
        Fetches the current GPS location and updates the label.
        """
        coordinates = self.gps_tracker.get_coordinates()
        if coordinates:
            lat, lon = coordinates
            self.coords_label.config(text=f"Coordinates: {lat}, {lon}")
        else:
            self.coords_label.config(text="Coordinates: Unable to fetch location")

    def export_location(self):
        """
        Exports the current GPS location to a local file.
        """
        coordinates = self.gps_tracker.get_coordinates()

        if coordinates:
            self.gps_tracker.save_coordinates(coordinates)
            tk.messagebox.showinfo("Success", "Location exported successfully.")
        else:
            tk.messagebox.showerror("Error", "Unable to fetch location.")
