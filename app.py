"""
Secret Santa App - A simple application to create Secret Santa pairings.

This Marimo app allows users to input two groups of names, processes them,
shuffles them, and displays the shuffled results. It can be used to organize
co"""

import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell
def _():
    """
    Define utility functions for processing and shuffling names.

    This cell imports the random shuffle function and defines two helper functions:
    1. process_names: Converts a comma-separated string into a list of names
    2. shuffle_names: Randomly shuffles a list of names

    Returns:
        tuple: (process_names, shuffle_names) functions for use in other cells
    """
    from random import shuffle as random_shuffle

    def process_names(names_str: str) -> list[str]:
        """Process a comma-separated string of names into a list.

        Args:
            names_str (str): Comma-separated string of names

        Returns:
            list: List of stripped names with empty entries removed
        """
        return [name.strip() for name in names_str.split(",") if name.strip()]

    def shuffle_names(names_list: list[str]) -> list[str]:
        """Shuffle a list of names.

        Args:
            names_list (list): List of names to shuffle

        Returns:
            list: Shuffled list of names
        """
        # Create a copy to avoid modifying the original
        result = names_list.copy()
        random_shuffle(result)
        return result

    return process_names, shuffle_names


@app.cell
def _(mo):
    """
    Display the application title.

    This cell renders the main title of the Secret Santa application using Marimo's
    markdown functionality.

    Args:
        mo: The Marimo module for UI rendering
    """
    mo.md(r"""# Secret Santa""")
    return


@app.cell
def __input_names_a(mo):
    """
    Create input fields for two groups of names.

    This cell creates two text input fields where users can enter comma-separated
    lists of names for two different groups. These groups will be used for the
    Secret Santa pairing.

    Args:
        mo: The Marimo module for UI rendering

    Returns:
        tuple: (names_A, names_B) UI text input components containing the entered names
    """
    names_A = mo.ui.text(placeholder="A,B,C...")
    names_B = mo.ui.text(placeholder="A,B,C...")

    # Create text input fields with labels
    mo.md(
        f"""
        Enter a comma-separated list of names for the 1st group: {names_A}

        Enter a comma-separated list of names for the 2nd group: {names_B}
        """
    )
    return names_A, names_B


@app.cell
def _(mo, names_A, names_B, process_names, shuffle_names):
    """
    Process input names, shuffle them, and display the results.

    This cell takes the input from the text fields, processes the comma-separated
    strings into lists, shuffles each list randomly, and displays the shuffled
    results. These shuffled lists can be used for Secret Santa pairings where
    each person from group 1 gives a gift to the corresponding person in group 2.

    Args:
        mo: The Marimo module for UI rendering
        names_A: UI component containing names for the first group
        names_B: UI component containing names for the second group
        process_names: Function to convert comma-separated strings to lists
        shuffle_names: Function to randomly shuffle lists
    """
    # Process the input strings into lists of names
    aa = process_names(names_A.value)
    bb = process_names(names_B.value)

    # Shuffle both lists randomly
    aa = shuffle_names(aa)
    bb = shuffle_names(bb)

    # Display the shuffled results
    mo.md(
        f"""
        Shuffled 1st group: {aa}

        Shuffled 2nd group: {bb}
        """
    )
    return


@app.cell
def _():
    """
    Import the marimo module for UI functionality.

    This cell imports the marimo module and makes it available to other cells
    in the application. Marimo is used for creating interactive UI elements
    and displaying content.

    Returns:
        tuple: (mo,) The marimo module for use in other cells
    """
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
