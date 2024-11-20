def apply_theme(widget):
    """
    Applies consistent styling to a widget.
    :param widget: A tkinter widget to style.
    """
    widget.configure(
        background="white",
        foreground="black",
        font=("Arial", 12)
    )
