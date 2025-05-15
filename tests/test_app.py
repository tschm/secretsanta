"""
Tests for the Secret Santa application.
"""
import pytest
from unittest.mock import MagicMock

# Import the app module
import app


def test_app_initialization():
    """Test that the app is initialized correctly."""
    assert app.app is not None


def test_title_display():
    """Test the title display function."""
    # Create a mock marimo module
    mock_mo = MagicMock()
    
    # Call the title display function
    app.__(mock_mo)
    
    # Verify that md was called with the correct title
    mock_mo.md.assert_called_once_with(r"""# Secret Santa""")


def test_input_names():
    """Test the input names function."""
    # Create a mock marimo module with ui components
    mock_mo = MagicMock()
    mock_mo.ui.text.return_value = "mock_text_input"
    
    # Call the input names function
    names_A, names_B = app.__input_names_a(mock_mo)
    
    # Verify that text inputs were created
    assert mock_mo.ui.text.call_count == 2
    assert names_A == "mock_text_input"
    assert names_B == "mock_text_input"
    
    # Verify that md was called to display the inputs
    mock_mo.md.assert_called_once()


def test_shuffle_names():
    """Test the shuffle names function."""
    # Create mock objects
    mock_mo = MagicMock()
    mock_names_A = MagicMock()
    mock_names_B = MagicMock()
    
    # Set up the mock values
    mock_names_A.value = "Alice, Bob, Charlie"
    mock_names_B.value = "David, Eve, Frank"
    
    # Call the shuffle function
    app.__(mock_mo, mock_names_A, mock_names_B)
    
    # Verify that md was called to display the results
    mock_mo.md.assert_called_once()
