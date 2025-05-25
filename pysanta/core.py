"""Core functionality for the Secret Santa application."""

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
