"""
Pytest configuration file for the Secret Santa application tests.
"""
import pytest
from unittest.mock import MagicMock


@pytest.fixture
def mock_marimo():
    """
    Fixture that provides a mock marimo module.
    
    Returns:
        MagicMock: A mock object that simulates the marimo module.
    """
    mock_mo = MagicMock()
    mock_mo.ui.text.return_value = MagicMock()
    return mock_mo


@pytest.fixture
def mock_names_input():
    """
    Fixture that provides mock name input objects.
    
    Returns:
        tuple: A tuple containing two mock objects for names_A and names_B.
    """
    mock_names_A = MagicMock()
    mock_names_A.value = "Alice, Bob, Charlie"
    
    mock_names_B = MagicMock()
    mock_names_B.value = "David, Eve, Frank"
    
    return mock_names_A, mock_names_B