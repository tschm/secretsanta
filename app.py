import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell
def _():
    from random import shuffle as random_shuffle
    from typing import List

    def process_names(names_str: str) -> List[str]:
        """Process a comma-separated string of names into a list.

        Args:
            names_str (str): Comma-separated string of names

        Returns:
            list: List of stripped names with empty entries removed
        """
        return [name.strip() for name in names_str.split(",") if name.strip()]

    def shuffle_names(names_list: List[str]) -> List[str]:
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
    mo.md(r"""# Secret Santa""")
    return


@app.cell
def __input_names_a(mo):
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
def _(mo, names_A, names_B, process_names, shuffle_names):
    aa = process_names(names_A.value)
    bb = process_names(names_B.value)

    aa = shuffle_names(aa)
    bb = shuffle_names(bb)

    mo.md(
        f"""
        Shuffled 1st group: {aa}

        Shuffled 2nd group: {bb}
        """
    )
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
