from database.models import User, Card
from database import get_db

# registar (tutor)


##1##
#функция проврки номера телефона и пароля
def check_number(phone, password):
    db = next(get_db())
phone = db.query().filter_by(id=).first()
## функция добавления карт (carddent)

#функция получения данных пользователя по user_id filter by
