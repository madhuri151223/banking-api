from app import transfer_money

def test_successful_transfer():
    assert transfer_money(1000, 300) == 700

def test_insufficient_balance():
    try:
        transfer_money(500, 700)
        assert False
    except ValueError as error:
        assert str(error) == "Insufficient balance"

def test_invalid_transfer():
    try:
        transfer_money(1000, -100)
        assert False
    except ValueError as error:
        assert str(error) == "Transfer amount must be positive"
