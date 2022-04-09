import datetime as dt

class Calculator():
    def __init__(self, limit):
        self.limit=limit
        records=[]

    def add_record(self,record):
        self.records.append(record)
        
    def get_today_stats(self):
        today_stats=0
        for i in self.records:
            if i.date==dt.datetime.now().date():
                today_stats+=i.amount()
        return today_stats

    def get_week_stats(self):
        week_stats=0
        today=dt.datetime.now().date()
        week_ago=dt.timedelta(days=7)
        for i in self.records:
            if i.date>=today and i.date<=week_ago:
                week_stats+=i.amount
        return week_stats

class Record():
    def __init__(self, amount, comment, date=''):
        self.amount= amount
        self.comment= comment
        if self.date=='':
            date= dt.datetime().now().date()

class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        today_calories=self.get_today_stats()
        if today_calories<self.limit:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit-today_calories} кКал' 
        else:
            return 'Хватит есть!'

class CashCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self,currency):
        USD_RATE= 74.85
        EUR_RATE= 81.71
        RUB_RATE= 1
        currencies={
        'rub': (RUB_RATE, 'руб'),
        'usd': (USD_RATE, 'usd'),
        'eur': (EUR_RATE, 'eur')
        }
        today_cash=round(self.get_today_stats()/currencies[currency],2)
        if self.limit>today_cash:
            return f'На сегодня осталось {self.limit-today_cash} {currencies[currency][1]}'
        if self.limit<today_cash:
            return f'Денег нет, держись: твой долг - {today_cash-self.limit} {currencies[currency][1]}'
        else:
            return 'Денег нет, держись'
