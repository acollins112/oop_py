import pytest
from oop_loan_pmt import Loan

@pytest.fixture
def sample_loan():
    return Loan(100000, 30, 0.06)

def test_calculate_discount_factor(sample_loan):
    sample_loan.calculateDiscountFactor()
    discount_factor = sample_loan.getDiscountFactor()
    print(f"Testing discount factor calculation: {discount_factor}")
    assert discount_factor == pytest.approx(166.7916, abs=1e-4)

def test_calculate_loan_payment(sample_loan):
    sample_loan.calculateLoanPmt()
    loan_payment = sample_loan.getLoanPmt()
    print(f"Testing loan payment calculation: {loan_payment}")
    assert loan_payment == pytest.approx(599.55, abs=1e-2)

def test_full_loan_payment_calculation(sample_loan):
    sample_loan.calculateLoanPmt()
    discount_factor = sample_loan.getDiscountFactor()
    loan_payment = sample_loan.getLoanPmt()
    print(f"Testing full loan payment calculation:")
    print(f"Discount factor: {discount_factor}, Loan payment: {loan_payment}")
    assert discount_factor == pytest.approx(166.7916, abs=1e-4)
    assert loan_payment == pytest.approx(599.55, abs=1e-2)
