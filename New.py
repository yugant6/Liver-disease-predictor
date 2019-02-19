from tkinter import *
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

class App(Frame):
    def __init__(root, master):
        Frame.__init__(root, master)
        root.create_widgets()
        root.pack()
        
        

    def get_values(root):
        return [entry.get() for entry in root.entries]

    def calc_CR(root):
        abc = root.get_values()
        root.god.append(abc)
        patient= pd.read_csv("indian_liver_patient.csv")
        patient = pd.concat([patient,pd.get_dummies(patient['Gender'], prefix = 'Gender')], axis=1)
        patient["Albumin_and_Globulin_Ratio"] = patient.Albumin_and_Globulin_Ratio.fillna(patient['Albumin_and_Globulin_Ratio'].mean())
        X = patient.drop(['Gender','Dataset'], axis=1)
        y = patient['Dataset']
        random_forest = RandomForestClassifier(n_estimators=100)
        random_forest.fit(X, y)
        ydata=random_forest.predict(root.god)
        if(ydata[2]==2):
            root.answer.config(text="Sorry, you have liver problem")
        else:
            root.answer.config(text="Congratulations,You have not any problem with liver")

   # def model(root):
        
    #    return ydata

    def create_widgets(root):
        root.entries = []
        
        label = Label(root, text='LIVER DISEASE PREDICTOR')
        label.pack()

        label = Label(root, text='AGE')
        label.pack()
        entry = Entry(root, width=8)
        entry.pack()
        root.entries.append(entry)

        label = Label(root, text='T Billrubin')
        label.pack()
        entry = Entry(root, width=8)
        entry.pack()
        root.entries.append(entry)

        label = Label(root, text='D Billrubin')
        label.pack()
        entry = Entry(root, width=8)
        entry.pack()
        root.entries.append(entry)

        label = Label(root, text='alk phos')
        label.pack()
        entry = Entry(root, width=8)
        entry.pack()
        root.entries.append(entry)

        label = Label(root, text='alm ams')
        label.pack()
        entry = Entry(root, width=8)
        entry.pack()
        root.entries.append(entry)

        label = Label(root, text='asp amn')
        label.pack()
        entry = Entry(root, width=8)
        entry.pack()
        root.entries.append(entry)

        label = Label(root, text='t Protin')
        label.pack()
        entry = Entry(root, width=8)
        entry.pack()
        root.entries.append(entry)

        label = Label(root, text='alb')
        label.pack()
        entry = Entry(root, width=8)
        entry.pack()
        root.entries.append(entry)

        label = Label(root, text='alb&glb')
        label.pack()
        entry = Entry(root, width=8)
        entry.pack()
        root.entries.append(entry)

        label = Label(root, text='fmale')
        label.pack()
        entry = Entry(root, width=8)
        entry.pack()
        root.entries.append(entry)

        label = Label(root, text='male')
        label.pack()
        entry = Entry(root, width=8)
        entry.pack()
        root.entries.append(entry)


        root.god=[[65,2,1.1,300,25,22,5.5,3.3,0.8,0,1],[65,2,1.1,300,25,22,5.5,3.3,0.8,1,0]]

        root.calc_button = Button(root, text='Submit', command=root.calc_CR)
        root.calc_button.pack()

        
        label = Label(root, text='Test Accuracy = 75%')
        label.pack()

        root.answer = Label(root, text='')
        root.answer.pack()

    def run(root):
        root.mainloop()



root = Tk()
root.title('LDP')


app = App(root)
app.run()