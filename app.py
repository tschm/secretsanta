import marimo

__generated_with = "0.9.31"
app = marimo.App()


@app.cell
def __(mo):
    """Display the Secret Santa application title.

    Args:
        mo: The marimo module instance for rendering markdown.

    Returns:
        None
    """
    mo.md(r"""# Secret Santa""")
    return


@app.cell
def __input_names_a(mo):
    """Create input fields for entering names for two groups.

    This function creates two text input fields for users to enter comma-separated
    lists of names for two different groups, and displays them with appropriate labels.

    Args:
        mo: The marimo module instance for UI components and rendering.

    Returns:
        tuple: A tuple containing two text input UI elements (names_A, names_B).
    """
    names_A = mo.ui.text(placeholder="A,B,C...")
    names_B = mo.ui.text(placeholder="A,B,C...")

    # Create shuffle button with conditional enabling
    mo.md(
        f"""
        Enter a comma-separated list of names for the 1st group: {names_A}

        Enter a comma-separated list of names for the 2nd group: {names_B}
        """
    )
    return names_A, names_B


@app.cell
def __(mo, names_A, names_B):
    """Shuffle the names from both groups and display the results.

    This function takes the comma-separated names from both input fields,
    converts them to lists, shuffles each list separately, and displays
    the shuffled results.

    Args:
        mo: The marimo module instance for rendering markdown.
        names_A: The UI text input element containing names for the first group.
        names_B: The UI text input element containing names for the second group.

    Returns:
        None
    """
    from random import shuffle

    aa = list([name.strip() for name in names_A.value.split(",") if name.strip()])
    bb = list([name.strip() for name in names_B.value.split(",") if name.strip()])

    shuffle(aa)
    shuffle(bb)

    mo.md(
        f"""
        Shuffled 1st group: {aa}

        Shuffled 2nd group: {bb}
        """
    )


@app.cell
def __():
    """Import and initialize the marimo module.

    This function imports the marimo module and returns it for use in other cells.
    It serves as the initialization cell for the application.

    Returns:
        tuple: A tuple containing the marimo module instance.
    """
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
