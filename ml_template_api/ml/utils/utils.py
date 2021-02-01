import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from matplotlib import pyplot
from stop_words import get_stop_words
import joblib
from datetime import date
import sys

from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from stop_words import get_stop_words

class DataHandler:
    
    """
        R?cup?ration des data depuis le GCS Bucket
    """

    def __init__(self):
        self.df_vaccin = None 
        
    def get_data(self):
        """
            R?cup?ration du 
        """
        self.df_vaccin= pd.read_csv("utils/vaccination_tweets.csv",sep=",",index_col=0)
        print("data charg?s")
    
    def clean_text(self):
        self.df['text'] = df['text'].apply(lambda tweet: re.sub('[^A-Za-z]+', ' ', tweet.lower()))

    def get_process_data(self):
        """
            Lancement des diff?rente m?thode get_data()+goup_data()
        """
        self.get_data()
        self.clean_text()
        print('Data processed')
        return self.get_data()
		
class FeatureRecipe:
    
    def __init__(self, data: pd.DataFrame()):
        self.df_data = data
        self.cate = []
        self.floa = []
        self.intt = []
        self.drop = []
        

    def separate_variable_types(self) -> None:
        """ TODO : Diviser les types de variables dans un tableau """
        #variables = self.df_data.dtypes
        #var_tab = Arrays('int64',['125946'])
        #print(var_tab[int64])
        
        """correction"""
        print("separating columns")
        for col in self.df_data.columns:
            if self.df_data[col].dtypes == int:
                self.intt.append(self.df_data[col])
            elif self.df_data[col].dtypes == float:
                self.floa.append(self.df_data[col])
            else:
                self.cate.append(self.df_data[col])
        print ("dataset column size : {} \nnumber of discreet values : {} \nnumber of continuous values : {} \nnumber of others : {} \ntaille total : {}".format(len(self.df_data.columns),len(self.intt),len(self.floa),len(self.cate),len(self.intt)+len(self.floa)+len(self.cate) ))
    
    
    def drop_uselessf(self):
        """ TODO : Supprimer les colonnes inutiles du dataset """
        colonnes_drop=['user_created',
                       'user_followers',
                       'user_friends',
                       'user_favourites',
                      ]
        self.df_data.drop(columns=colonnes_drop)
        print('colonnes supprimer')
    
    def drop_duplicate(self):
        """ TODO : Supprimer les lignes dupliqu?es du dataset """
        print('duplicate')
        a=0
        for i in self.df_data:
            a+=1
            b=0
            for j in self.df_data:
                b +=1
                if a != b and self.df_data[i].equals(self.df_data[j]) == True:
                    self.df_data.drop(columns=j)
                    print('{} supprim?e'.format(j))
    
    def Verif_data(self):
        print('verif date')
        """ V?rif des data sup?rieur a 3%"""
        for colonne in  self.df_data:
            nbNaN =  self.df_data[colonne].isna().sum()
            if (nbNaN /  self.df_data.shape[0]) * 100 > 3:
                del  self.df_data[colonne]
                print('{} supprim?e'.format(colonne))
        


    def prepare_data(self):
        self.separate_variable_types()
        self.drop_uselessf()
        self.drop_duplicate()
        self.Verif_data()
        return self.df_data
	
class FeatureExtractor:
    """
    Feature Extractor class
    """
    def __init__(self, data: pd.DataFrame, flist: list = None):
        """
            Input : pandas.DataFrame, feature list to drop
            Output : X_train, X_test, y_train, y_test according to sklearn.model_selection.train_test_split

        """
        self.df_data = data
        self.X = self.df_data['text']
        self.y = self.df_data['retweets']
        self.clf = None
        
    def make_pipeline(self):
        self.clf = make_pipeline(
                            TfidfVectorizer(stop_words=get_stop_words('en')),
                            OneVsRestClassifier(SVC(kernel='linear', probability=True))
                            )
        
        self.clf = self.clf.fit(X=self.X, y=self.y)
        
        return self.clf
		
class ModelBuild: 
    def __init__(self, model_path, save, n_estimators):
        """
        constructeur 
        """
        self.model_filename = model_path
        self.saveModel = save
        self.date = date.today().isoformat()
        self.n_estimators=n_estimators
    
    def train(self,clf,X,Y):
        clf.fit(X, Y)

    def predict_test(self,clf,text):
        #test 
        clf.predict_proba([text])[0]

    def print_accuracy(self,clf,X,Y):
        """
            affichage de la precision des predictions
        """
        accuracy=clf.score(X,Y)
        print('precision : {}'.format(accuracy))
    
    def FeatureImportance(self,X,Y,clf):
        """
            attribut un score aux valeurs utilis? pour la prediction bas? 
            sur leurs utilit?
        """
        clf.fit(X,Y)
        importance =  clf.coef_()
        for i,v in enumerate(importance):
            print('Feature: %0d, Score: %.5f' % (i,v))
        pyplot.bar([x for x in range(len(importance))], importance)
        pyplot.show()
        
    def save_model(self,clf):
        #save weights 
        model_filename = "model.joblib.z"
        joblib.dump((clf), model_filename)
        
    def calculData(self,clf,X,Y,text):
        self.train(clf,X,Y)
        self.predict_test(clf,text)
        self.print_accuracy(clf,X,Y)
        #self.FeatureImportance(X,Y,clf)
        self.save_model(clf)