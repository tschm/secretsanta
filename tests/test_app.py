from random import seed

from pysanta import process_names, shuffle_names


def test_process_names_normal():
    """Test processing names with normal input."""
    names_str = "Alice, Bob, Charlie, David"
    expected = ["Alice", "Bob", "Charlie", "David"]
    assert process_names(names_str) == expected


def test_process_names_with_empty():
    """Test processing names with empty entries."""
    names_str = "Alice, , Bob, , Charlie"
    expected = ["Alice", "Bob", "Charlie"]
    assert process_names(names_str) == expected


def test_process_names_with_whitespace():
    """Test processing names with extra whitespace."""
    names_str = "  Alice  ,  Bob  , Charlie "
    expected = ["Alice", "Bob", "Charlie"]
    assert process_names(names_str) == expected


def test_process_names_empty_string():
    """Test processing an empty string."""
    names_str = ""
    expected = []
    assert process_names(names_str) == expected


def test_shuffle_names():
    """Test that shuffling names returns a list with the same elements."""
    # Set a fixed seed for reproducibility
    seed(42)
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    shuffled = shuffle_names(names)

    # Check that the shuffled list contains the same elements
    assert sorted(shuffled) == sorted(names)

    # Check that the order is different (this could theoretically fail,
    # but it's extremely unlikely with 5 elements)
    assert shuffled != names


def test_shuffle_names_empty_list():
    """Test shuffling an empty list."""
    names = []
    shuffled = shuffle_names(names)
    assert shuffled == []


def test_shuffle_names_single_element():
    """Test shuffling a list with a single element."""
    names = ["Alice"]
    shuffled = shuffle_names(names)
    assert shuffled == names
