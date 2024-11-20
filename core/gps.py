import random
import geocoder


class GPSTracker:
    """
    Handles GPS tracking functionality.
    """

    def __init__(self):
        self.g = geocoder.ip('me')
        self.last_coordinates = None

    def get_coordinates(self):
        """
        Fetches the current GPS coordinates using geopy.
        :return: Tuple of (latitude, longitude)
        """
        try:
            location = self.g.latlng

            if location:
                self.last_coordinates = location
                return location
        except Exception as e:
            print(f"Error fetching location: {e}")

    def save_coordinates(self, coordinates):
        """
        Saves the given coordinates to a file.
        :param coordinates: Tuple of (latitude, longitude)
        """
        with open("assets/data/coordinates.txt", "w") as f:
            f.write(f"{coordinates[0]},{coordinates[1]}")
