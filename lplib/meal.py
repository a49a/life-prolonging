from datetime import datetime


class Meal:

    def __init__(self, meal_time):
        self.now = datetime.now()
        self.meal_time = meal_time

    def is_time(self):
        for x in self.meal_time:
            if self.now.hour < x['start']:
                s = "现在还不是饭时，快吃" + x['zh'] + "了"
                return s
            if self.has_meal(x['start'], x['end']):
                s = "现在是吃" + x['zh'] + "的时候"
                return s
        return "别吃夜宵！实在忍不住吃点水果喝个牛奶"

    def has_meal(self, start, end):
        if (self.now.hour >= start) and (self.now.hour < end):
            return True
        return False






