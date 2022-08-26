class Score(object):
    def __init__(self, kor, eng, math):
        self.korean = kor
        self.english = eng
        self.math = math
    
    def scoring(self):
        score_mean = (self.korean + self.english + self.math)/3
        if score_mean >= 95:
            return 'A+'
        elif score_mean >= 90:
            return 'A'
        elif score_mean >= 85:
            return 'B+'
        elif score_mean >= 80:
            return 'B'
        elif score_mean >= 75:
            return 'C+'
        elif score_mean >= 70:
            return 'C'
        elif score_mean >= 65:
            return 'D+'
        elif score_mean >= 60:
            return 'D'
        else:
            return 'F'