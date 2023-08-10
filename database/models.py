from database import Base
from sqlalchemy import Column, String, BigInteger, DateTime, Float
from sqlalchemy.orm import relationship

#User table
class User(Base):
    __tablename__ = "users"
    id = Column(BigInteger, autoincrement=True,primary_key = True)
    profile_photo=Column(String)
    name= Column(String, nullable=False)
    surname= Column(String, nullable=False)
    phone_number=Column(BigInteger, nullable=False)
    emaile= Column(String, nullable=False)
    city= Column(String)
    reg_date= Column(DateTime)
    password= Column(String, nullable=False)
#card table
class Card(Base):
    __tablename__ = 'cards'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('user.id'), nullable=True)
    card_number= Column(BigInteger, nullable=False, unique=True)
    exp_date= Column (Integer, nullable=False)
    card_balance= Column(Float, default=15000)
    card_name= Column(String, default='My card')
    reg_date= Column(DateTime)
    user_fk= relationship(User, lazy="subquerry")
# payments table
class Transactions(Base):
    __tablename__ = "user_transactions"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    card_from = Column(BigInteger, ForeignKey('cards.card_number'))
    amount= Column(Float)
    card_to = Column(BigInteger, Foreignkey('cards.card_number'))
    transfer_time = Column(DateTime)
    card_from_fk = relationship(Card, lazy="subquery")
    card_to_fk = relationship(Card, lazy="subquery")
#payment category table

class PayCategory(Base):
    __tablename__ = 'pay_categories'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    category_name=Column(String, nullable=False)
    reg_date=Column(DateTime)