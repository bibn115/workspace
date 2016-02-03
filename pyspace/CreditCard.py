#!/usr/bin/python3


class CreditCard:
    """Consumer credit card class"""

    def __init__(self,customer,bank,acnt,limit):
        """Create a new credit card instance

        The initial balance should be set to zero
        Variables:
        - customer: the name of the customer.
        - bank    : the name of the bank.
        - acnt    : the account identifier.
        - limit   : credit limit(measured in dollars)
        """
        self._customer = customer
        self._bank     = bank
        self._acnt     = acnt
        self._limit    = limit
        self._balance  = 0

    def get_customer(self):
        """return the name of the customer"""
        return self._customer

    def get_bank(self):
        """return the name of the bank"""
        return self._bank

    def get_account(self):
        """return the account number"""
        return self._acnt

    def get_limit(self):
        """return the credit card limit"""
        return self._limit

    def get_balance(self):
        """return the balance available in the account"""
        return self._balance

    def charge(self,price):
        """Assuming that sufficient credit available
        charge the price to the customer credit"""
        if price+self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self,payment):
        """Process customer payment and deduce from the balance"""
        self._balance -= payment



