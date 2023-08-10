# RepeBon aeHer
def money_transfer_db(card_from, card_to, amount, transaction_date):
db = next(get_db())
card_from_db = db.query(Card).filter_by(card_number=card_from).first()
card_to_db = db.query(Card).filter_by(card_numher=card_to).first()
# llposepka ecTb nW aTW kapTbl
if card_from_db and card_to_db:
H nposeoka AOCTaTOYHO nw AeHer
if card_from_db.card_balance >= amount:
    card_to_db.card_balance += amount
    new_transaction = Transaction(card_from=card_from,
                                  card
    to = card_to
    amount = amount,
    transfer
    _time = transaction_date)
    i
    transfer_service.py
    db.add(new_transaction)
    db.commit()
    return True
    return 'HeAocTaTO4HO cpeACTB'
    return 'Oun6ka B AaHHbIX"