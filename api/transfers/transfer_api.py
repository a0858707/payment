from main import app
from .transfer_models import P2PDent

# 3anpoc Ha nepeBon AeHer MeXAy kapTaMu
@app.post('/api/transfer-money')
async def money_transfer(transfer_data: P2PDent):
    result = transfer_data
    print(result)
    return {'status': 1, "message": result}

#Функция получения последних транзакций пользователя
@app.get ('/api/monitoring')
async def user_payments(user_id: int, card_id =0):
    pass