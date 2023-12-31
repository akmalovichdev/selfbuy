from app.settings import db

def start(message):
    text = '''
Привет!

Через этого бота можно оставить заявку на выкуп или раздачу товара. Объявление будет опубликовано в канале для выкупов и раздач. 

Сейчас тебе надо будет ответить на сколько простых вопросов
'''
    return text

def questions(message, type):
    if type == 'productLink':
        text = 'Ссылка на товар, который необходимо выкупить.'
    elif type == 'purchaseCount':
        text = 'Сколько выкупов необходимо (если нужно выкупать 7 дней подряд, то пишите суммарно за неделю)?'
    elif type == 'purchasePurpose':
        text = 'Для какой цели выкупы (отзывы, продвижение, свой вариант)?'
    elif type == 'isProductRetrievalPlanned':
        text = 'Планируете забирать товар? Организация и оплата обратной логистики полностью лежит на Вас.'
    elif type == 'cityForPurchase':
        text = 'В какой город нужно выкупать? Укажите (Москва), несколько (Москва, СПБ, Краснодар) или "В любой"'
    elif type == 'purchaseAlgorithm':
        text = "Опишите алгоритм для выкупа (например: Зайти в мобильную версию, ввести ключ 'Платье черное с открытой спиной', поставить фильтр по цене в диапазоне до 2000 рублей, указать объем скидки 47%. Мой товар будет на 5 позиции.)"
    elif type == 'isBuyerRetrievalNeeded':
        text = 'Нужно ли покупателю забирать товар? (Нужно, заберу сам)'
    elif type == 'isReviewNeeded':
        text = 'Нужно ли писать отзыв? (да/да, с фото/не нужно)'
    elif type == 'isRulesAgreed':
        text = '''
Спасибо, Вы ответили на все вопросы. После модерации объявление будет опубликовано в канале. Вам останется только написать всем, кто откликнется. 

В следующем сообщении подтвердите, что ознакомились с правилами и сообщение отправится на модерацию.
'''
    elif type == 'privacy':
        text = '''
Вся ответственность за перевод средств покупателю и организацию процесса возврата товара лежит на мне. Организаторы канала не проверяли пользователей и не несут отвественности за вашу коммуникацию.
'''
    elif type == 'success':
        text = 'Все готово после модерации ваш товар будет опубликован в канале!'
    return text

def distribution(message, type):
    if type == 'productLink':
        text = 'Ссылка на товар, который будете раздавать'
    elif type == 'cashback':
        text = 'Кэшбэк за товар (варианты ответа: 100%, 50%, либо свой вариант в ответном сообщении)'
    elif type == 'algoritm':
        text = 'Опишите алгоритм для заказа товара'
    elif type == 'cashbackDay':
        text = ' Через сколько дней переведете кэшбэк (варианты ответа: сразу, 7 дней, 14 дней, 21 день)'
    elif type == 'isRulesAgreed':
        text = '''
Спасибо, Вы ответили на все вопросы. После модерации объявление будет опубликовано в канале. Вам останется только написать всем, кто откликнется. 

В следующем сообщении подтвердите, что ознакомились с правилами и сообщение отправится на модерацию.
'''
    elif type == 'privacy':
        text = '''
Обратите внимание, что Вы выбрали опцию "Раздача". Это означает, что покупатель оставляет товар себе, при этом вы должны перевести кэшбэк покупателю в течение оговоренного срока. 

Вся ответственность за перевод средств покупателю лежит на мне. Организаторы канала не проверяли пользователей и не несут отвественности за вашу коммуникацию.
'''
    elif type == 'success':
        text = 'Все готово после модерации ваш товар будет опубликован в канале!'
    return text

def sendQuestions(call, data, type):
    if type == 'questions':

        text = f'''
Заявка на выкуп товара от <a href='tg://user?id={call.from_user.id}'>{call.from_user.full_name}</a>

1) Товар для выкупа: {data['productLink']}
2) Планируемое количество выкупов: {data['purchaseCount']}
3) Цель выкупов: {data['purchasePurpose']}
4) Планируете ли забирать товар у покупателя: {data['isProductRetrievalPlanned']}
5) Требуемые города для выкупов: {data['cityForPurchase']}
6) Алгоритм для выкупа товара: 
{data['purchaseAlgorithm']}
7) Нужно ли забрать товар с ПВЗ: {data['isBuyerRetrievalNeeded']}
8) Нужно ли писать отзыв? 
{data['isReviewNeeded']}

Ставьте + в комментариях, продавец свяжется с вами для организации выкупа.
'''
    elif type == 'distribution':
        text = f'''
Заявка на раздачу товара от <a href='tg://user?id={call.from_user.id}'>{call.from_user.full_name}</a>

1) Товар для раздачи: {data['productLink']}
2) Кэшбэк за товар: {data['cashback']}
3) Алгоритм заказа товара: {data['algoritm']}
4) Через сколько дней переведут кэшбэк: {data['cashbackDay']}

Ставьте + в комментариях, продавец свяжется с вами для организации выкупа.
'''
    return text


def publish(id, type):
    if type == 'questions':
        productLink = db.select('id', id, 'purchases', 'productLink')
        purchaseCount = db.select('id', id, 'purchases', 'purchaseCount')
        purchasePurpose = db.select('id', id, 'purchases', 'purchasePurpose')
        isProductRetrievalPlanned = db.select('id', id, 'purchases', 'isProductRetrievalPlanned')
        cityForPurchase = db.select('id', id, 'purchases', 'cityForPurchase')
        purchaseAlgorithm = db.select('id', id, 'purchases', 'purchaseAlgorithm')
        isBuyerRetrievalNeeded = db.select('id', id, 'purchases', 'isBuyerRetrievalNeeded')
        isReviewNeeded = db.select('id', id, 'purchases', 'isReviewNeeded')

        text = f'''
✅ Выкуп

1) Товар для выкупа: {productLink}
2) Планируемое количество выкупов: {purchaseCount}
3) Цель выкупов: {purchasePurpose}
4) Планируете ли забирать товар у покупателя: {isProductRetrievalPlanned}
5) Требуемые города для выкупов: {cityForPurchase}
6) Алгоритм для выкупа товара:
{purchaseAlgorithm}
7) Нужно ли забрать товар с ПВЗ: {isBuyerRetrievalNeeded}
8) Нужно ли писать отзыв? 
{isReviewNeeded}

Ставьте + в комментариях, продавец свяжется с вами для организации выкупа.
'''
    elif type == 'distribution':
        productLink = db.select('id', id, 'distribution', 'productLink')
        cashback = db.select('id', id, 'distribution', 'cashback')
        algoritm = db.select('id', id, 'distribution', 'algoritm')
        cashbackDay = db.select('id', id, 'cashbackDay', 'cashbackDay')

        text = f'''
🔥 Разадача

1) Товар для раздачи: {productLink}
2) Кэшбэк за товар: {cashback}
3) Алгоритм заказа товара: {algoritm}
4) Через сколько дней переведут кэшбэк: {cashbackDay}

Ставьте + в комментариях, продавец свяжется с вами для организации выкупа.
'''
        
    return text