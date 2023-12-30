
from sklearn.datasets import load_iris
from sklearn.datasets import load_wine

from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

X, y = load_wine(return_X_y=True)

W,x=load_diabetes(return_X_y=True)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=0,shuffle=False)
print("Training Data:",X_train.shape)
print(X_test.shape)
from sklearn import svm
#A_train,A_test,c_train,c_test=train_test_split(A,c,test_size=0.4,random_state=0,shuffle=False)
#print("Training Data:",X_train.shape)
#print(X_test.shape)
W_train,W_test, x_train , x_test=train_test_split(W,x,test_size=0.4,random_state=0,shuffle=False)
print("Training Data:",X_train.shape)
print(X_test.shape)


clf = svm.SVC()
dt=tree.DecisionTreeClassifier() #dt initialize
rf=RandomForestClassifier()   #rf initialize
lr=LogisticRegression()     #lr initialize
nb=GaussianNB()

clf.fit(X_train,y_train)   #training
dt.fit(X_train,y_train)
rf.fit(X_train,y_train)
lr.fit(X_train,y_train)
nb.fit(X_train,y_train)

acc=clf.score(X_test,y_test)   #testing on dataset
acc_dt=dt.score(X_test,y_test)
acc_rf=rf.score(X_test,y_test)
acc_lr=lr.score(X_test,y_test)
acc_nb=nb.score(X_test,y_test)

acc_tr=clf.score(X_train,y_train)    #training accuracy
print("***********")
print("****** testing accuracy*******")
print(acc)
print(acc_dt)
print(round(acc_rf,2)*100)
print(round(acc_lr,2)*100)
print(round(acc_nb,2)*100)

print("*********")
print("**** trainig accuracy*****")
print(round(acc_tr,2)*100)



svm_cv=cross_val_score(clf,X,y,cv=7)
dt_cv=cross_val_score(dt,X,y,cv=7)
print(svm_cv)
print(svm_cv.mean())
print(svm_cv.std())















#koi se  b 3 dataset lene hee iris k ilawa (60,40),(70,30),(80,20)
# cross validation (3,4),(5,4),(7,4)
# mean + std




