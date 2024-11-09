import pytest
from customers_db import CustomersDB


def test_insert_customer():
    db = CustomersDB()
    db.connect()

    db.insert_customer("sam", "abc@gmail.com")
    customer = db.get_customer_by_name("sam")

    assert customer is not None
    assert customer['name'] == "sam"
    assert customer['email'] == "abc@gmail.com"

    db.clear_customers()
    db.close()

def test_get_all_customers():
    db = CustomersDB()
    db.connect()

    db.insert_customer("abc", "abc@gmail.com")
    db.insert_customer("efg", "efg@gmail.com")

    customers = db.get_all_customers()
    assert len(customers) == 2

    db.clear_customers()
    db.close()