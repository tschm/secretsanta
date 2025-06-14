# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo==0.13.15",
# ]
# ///
"""
Secret Santa App - A simple application to create Secret Santa pairings.

This Marimo app allows users to input two groups of names, processes them,
shuffles them, and displays the shuffled results. It can be used to organize
co"""

import marimo

__generated_with = "0.13.15"
app = marimo.App()

with app.setup:
    from random import shuffle as random_shuffle

    import marimo as mo


@app.function
def process_names(names_str: str) -> list[str]:
    """Process a comma-separated string of names into a list.

    Args:
        names_str (str): Comma-separated string of names

    Returns:
        list: List of stripped names with empty entries removed
    """
    return [name.strip() for name in names_str.split(",") if name.strip()]


@app.function
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


@app.cell
def _():
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
def __input_names_a():
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
    names_a = mo.ui.text(placeholder="A,B,C...")
    names_b = mo.ui.text(placeholder="A,B,C...")

    # Create text input fields with labels
    mo.md(
        f"""
        Enter a comma-separated list of names for the 1st group: {names_a}

        Enter a comma-separated list of names for the 2nd group: {names_b}
        """
    )
    return names_a, names_b


@app.cell
def _(names_a, names_b, process_names, shuffle_names):
    """
    Process input names, shuffle them, and display the results.

    This cell takes the input from the text fields, processes the comma-separated
    strings into lists, shuffles each list randomly, and displays the shuffled
    results. These shuffled lists can be used for Secret Santa pairings where
    each person from group 1 gives a gift to the corresponding person in group 2.

    Args:
        mo: The Marimo module for UI rendering
        names_a: UI component containing names for the first group
        names_b: UI component containing names for the second group
        process_names: Function to convert comma-separated strings to lists
        shuffle_names: Function to randomly shuffle lists
    """
    # Process the input strings into lists of names
    aa = process_names(names_a.value)
    bb = process_names(names_b.value)

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


if __name__ == "__main__":
    app.run()
