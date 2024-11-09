import pytest
from src.bank import BankAccount


def test_create_account():
    account = BankAccount("Mira Patel", 100)

    assert account.owner == 'Mira Patel'
    assert account.balance == 100

def test_deposit():
    account = BankAccount("Venkat")
    account.deposit(50)
    account.deposit(40)
    assert account.balance == 90

    with pytest.raises(ValueError):
        account.deposit(-10)

def test_withdraw():
    account = BankAccount("Veera")
    account.deposit(500)
    account.deposit(700)
    account.withdraw(200)
    assert account.balance == 1000

    with pytest.raises(ValueError):
        account.withdraw(1500)

@pytest.mark.skip(reason="Skipping this test due to some reason")
def test_get_balance():
    account = BankAccount("Irfan", 700)
    assert account.get_balance() == 700