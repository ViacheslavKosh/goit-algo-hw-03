# Враховуючи завдання - чиста функция яка повертає різницю між датами як ціле число

from datetime import datetime

def get_days_from_today(date):
    
    try:
        # Повертаємо рядок дати як об'єкт datatime
        date_object = datetime.strptime(date, "%Y-%m-%d")
        
        # Отримуэмо поточну дату 
        date_today = datetime.today()
        
        # Використовуючи метод toordinal() отримуємо різницю в днях між датами як ціле число
        difference = date_today.toordinal() - date_object.toordinal()
        
        # Повертаємо отриману різницю
        return difference
    
    # Якщо дата введена в невірному форматі то отримаемо зауваження
    except ValueError:
        print(f"Incorrect date format {date}. Try again with format: 'YYYY-MM-DD'")

