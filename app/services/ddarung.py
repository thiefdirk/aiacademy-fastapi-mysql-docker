from app.models.ddarung import DDarung
from app.utils.context import Context
import pandas as pd

class DDarungService:
    
    ddarung = DDarung()
    
    def preprocess(self, path, train, test) -> object:
        model = self.ddarung
        this = model.context
        this.train = model.from_csv(path, train)
        this.test = model.from_csv(path, test)
        this.id = this.test['id']
        this = model.missing_value_process(this)
        this = model.learning(this)
        this = model.test(this)
        return this
    
    def submit(self, path, train, test):
        this = self.preprocess(path, train, test)
        submit = pd.read_csv('./data/submission.csv')
        submit['count'] = this
        submit.to_csv(path + 'submission.csv', index = True)
        
        