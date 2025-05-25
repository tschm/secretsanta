import marimo
from typing import Tuple, Any
from pysanta import process_names, shuffle_names

__generated_with = "0.9.31"
app = marimo.App()


@app.cell
def __(mo: Any) -> None:
    mo.md(r"""# Secret Santa""")
    return


@app.cell
def __input_names_a(mo: Any) -> Tuple[Any, Any]:
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
def __(mo: Any, names_A: Any, names_B: Any) -> None:
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


@app.cell
def __() -> Tuple[Any]:
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
