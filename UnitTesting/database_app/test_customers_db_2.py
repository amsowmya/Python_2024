import pytest
from customers_db import CustomersDB


@pytest.fixture
def db():
    db_instance = CustomersDB()
    db_instance.connect()
    yield db_instance

    db_instance.clear_customers()
    db_instance.close()


def test_insert_customer(db):
    db.insert_customer("sam", "abc@gmail.com")
    customer = db.get_customer_by_name("sam")

    assert customer is not None
    assert customer['name'] == "sam"
    assert customer['email'] == "abc@gmail.com"

def test_get_all_customers(db):
    db.insert_customer("abc", "abc@gmail.com")
    db.insert_customer("efg", "efg@gmail.com")

    customers = db.get_all_customers()
    assert len(customers) == 2
