import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import KFold,cross_val_score,GridSearchCV,StratifiedKFold, RandomizedSearchCV
from sklearn.experimental import enable_halving_search_cv
from sklearn.model_selection import HalvingGridSearchCV, HalvingRandomSearchCV
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import accuracy_score, r2_score
from sklearn.model_selection import train_test_split
from sklearn.experimental import enable_iterative_imputer # 이터러블 입력시 사용하는 모듈 추가
from sklearn.impute import SimpleImputer, KNNImputer, IterativeImputer 
from sklearn.ensemble import RandomForestClassifier ,RandomForestRegressor
from xgboost import XGBRegressor # xgboost 사용
from sklearn.svm import LinearSVC, SVC
from sklearn.pipeline import make_pipeline, Pipeline # pipeline을 사용하기 위한 함수
from app.utils.context import Context

class DDarung:
    
    context = Context()
    
    def __init__(self) -> None:
        self.train_set = None
        self.test_set = None
        self.model = None
        self.x_train = None
        self.x_test = None
        self.y_train = None
        self.y_test = None  
    
    # def hook(self, path, train, test):
    #     self.from_csv(path, train, test)
    #     self.missing_value_process()
    #     self.preprocess()
    #     self.learning()
    #     self.test()
    
    def from_csv(self, path, fname):
        this = self.context
        this.path = path
        this.fname = fname
        return pd.read_csv(this.path+this.fname)
        
        # train_set = pd.read_csv(path + train, # + 명령어는 문자를 앞문자와 더해줌
        #                         index_col=0) # index_col=n n번째 컬럼을 인덱스로 인식

        # test_set = pd.read_csv(path + test, # 예측에서 쓸거임                
        #                     index_col=0)
        # return train_set, test_set
    
    def missing_value_process(self, this):
        train_set = this.train
        test_set = this.test
        imputer1 = KNNImputer(missing_values=np.nan, n_neighbors=3) # n_neighbors default값은 3
        imputer2 = KNNImputer(missing_values=np.nan, n_neighbors=3) # n_neighbors default값은 3
        imputer1.fit(train_set) # 데이터프레임에 적용하기 위해 fit()함수 사용
        imputer2.fit(test_set) # 데이터프레임에 적용하기 위해 fit()함수 사용
        train_set_imputer = imputer1.transform(train_set) # transform()함수를 사용하여 데이터프레임을 적용하기 위해 transform()함수 사용
        test_set_imputer = imputer2.transform(test_set) # transform()함수를 사용하여 데이터프레임을 적용하기 위해 transform()함수 사용
        train_set = pd.DataFrame(train_set_imputer, columns=train_set.columns) # 데이터프레임을 데이터프레임으로 변환하기 위해 DataFrame()함수 사용
        test_set = pd.DataFrame(test_set_imputer, columns=test_set.columns) # 데이터프레임을 데이터프레임으로 변환하기 위해 DataFrame()함수 사용
        this.train = train_set
        this.test = test_set
        return this
    
    def learning(self, this):     
        train_set = this.train
        x = train_set.drop(['count'], axis=1)  # drop 데이터에서 ''사이 값 빼기
        y = train_set['count'] 
        x_train, x_test, y_train, y_test = train_test_split(x,y,
                                                    train_size=0.75,
                                                    random_state=31
                                                    )
        parameters_rfr = [{'RFR__bootstrap': [True], 'RFR__max_depth': [5, 10, None], 'RFR__max_features': ['auto', 'log2'], 'RFR__n_estimators': [5, 6, 7, 8, 9, 10, 11, 12, 13, 15]}]
        kfold = KFold(n_splits=5,shuffle=True,random_state=100)
        pipe = Pipeline([('minmax', MinMaxScaler()), ('RFR', RandomForestRegressor())], verbose=1)
        model = GridSearchCV(pipe, parameters_rfr,verbose=1,cv=kfold,
                     refit=True,n_jobs=-1,)
        model.fit(x_train,y_train)
        print(x_train)
        print(y_train)
        this.model = model
        this.x_test = x_test
        this.y_test = y_test
        return this
    
    def test(self, this):
        test_set = this.test
        model = this.model
        x_test = this.x_test
        y_test = this.y_test
        print(x_test)
        print(y_test)
        result = model.score(x_test, y_test)
        y_predict = model.predict(test_set)
        print('model.score : ', result) # model.score :  1.0
        print("최적의 파라미터 :",model.best_params_)
        return y_predict
    

        