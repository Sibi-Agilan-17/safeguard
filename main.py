from gui.app_window import MainWindow


def initialize_app():
    """
    Initializes and starts the SafeGuard app.
    """
    root = ttk.Window(themename="cosmo")  # Modern bootstrap theme
    AppWindow(root)
    root.mainloop()


if __name__ == "__main__":
    initialize_app()
