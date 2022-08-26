from app.models.grade import Grade

class GradeService(object):
    def __init__(self) -> None: # arguements는 모델에서 사용할 수 있는 변수들을 모아놓은 곳입니다, hyperparameters는 모델을 학습시키는데 사용되는 변수들을 모아놓은 곳입니다.
        self.credit = 0

    def set_score(self,name, korean, english, math):
        grade = Grade(name, korean, english, math)
        grade.set_avg()
        avg = grade.get_avg()
        if avg >= 90:
            self.credit = 'A'
        elif avg >= 80:
            self.credit = 'B'
        elif avg >= 70:
            self.credit = 'C'
        elif avg >= 60:
            self.credit = 'D'
        else:
            self.credit = 'F'
        
    def get_grade(self, name, korean, english, math):
        self.set_score(name, korean, english, math)
        return self.credit
