'''My Calculator Test'''
# import order, place standard imports before third-party imports
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide

@pytest.fixture
def setup_calculations():
    """Clear history and add sample calculations for tests."""
    Calculations.clear_history()  # Ensure a clean state before each test
    # Adding sample calculations to the history for tests
    Calculations.add_calculation(Calculation.create(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation.create(Decimal('20'), Decimal('3'), subtract))
    Calculations.add_calculation(Calculation(Decimal('3'), Decimal('2'), multiply))
    Calculations.add_calculation(Calculation(Decimal('6'), Decimal('3'), divide))

def test_add_calculation(setup_calculations: None): # pylint: disable=redefined-outer-name
    """Test adding a calculation."""
    calc = Calculation.create(Decimal('2'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, "Failed to add the calculation to the history"

def test_get_history(setup_calculations: None): # pylint: disable=redefined-outer-name
    """Test retrieving calculation history."""
    history = Calculations.get_history()
    assert len(history) == 4, "History does not contain the expected number of calculations"

def test_clear_history(setup_calculations: None): # pylint: disable=redefined-outer-name
    """Test clearing the calculation history."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History was not cleared"

def test_get_latest(setup_calculations: None): # pylint: disable=redefined-outer-name
    """Test getting the latest calculation."""
    latest = Calculations.get_latest()
    assert latest.a == Decimal('6') and latest.b == Decimal('3'), "Did not get the correct latest calculation"

def test_find_by_operation(setup_calculations: None): # pylint: disable=redefined-outer-name
    """Test finding calculations by operation type."""
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) == 1, "Did not find the correct number of calculations with add operation"
    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(subtract_operations) == 1, "Did not find the correct number of calculations with subtract operation"

def test_get_latest_with_empty_history():
    """Test getting the latest calculation when history is empty."""
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Expected None for latest calculation with empty history"
