from iebank_api.models import Account
import pytest

def test_create_account():
    """
    GIVEN an Account model
    WHEN a new Account is created
    THEN check the fields are defined correctly
    """
    account = Account('John Doe', '€', 'Finland')  # Add 'country'
    assert account.name == 'John Doe'
    assert account.currency == '€'
    assert account.account_number is not None
    assert account.balance == 0.0
    assert account.status == 'Active'
    assert account.country == 'Finland'

def test_default_status():
    """
    GIVEN an Account model
    WHEN a new Account is created
    THEN check the status is defaulted to 'Active'
    """
    account = Account('Jane Doe', '€', 'Germany')
    assert account.status == 'Active'