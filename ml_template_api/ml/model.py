from utils import utils

data = utils.DataHandler()
data.get_process_data()
feature = utils.FeatureRecipe(data.df_vaccin)
feature.prepare_data()
train = utils.FeatureExtractor(feature.df_data)
clf = train.make_pipeline()
modelbuild = utils.ModelBuild("",True,50)
modelbuild.calculData(train.clf,train.X,train.y,"Covid")
