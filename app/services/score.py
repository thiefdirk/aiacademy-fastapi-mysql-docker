from app.models.score import Score

class ScoreService(object):
    def __init__(self) -> None:
        pass
    

    def score(self, name, kor, eng, math):
        self.korean = kor
        self.english = eng
        self.math = math
        self.name = name
        
        score = Score(self.korean, self.english, self.math)
        print(f'{self.name}의 점수: {score.scoring()}')