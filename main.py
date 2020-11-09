import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
import utils as tool


def main():
    #df[nombreColumna][NúmeroFila] da el valor
    #print(df['Desc_curso'][0])
    print('Elige una opción:')
    print('1.Árbol de decisión 2.Bayes 3. Ver primeros datos')
    op=input()
    op=int(op)
    #Carga el archivo excel a un DataFrame
    #uevo Comentario
    tool.imprimirHora()
    tool.imprimirEstadistica()
    print('Leyendo excel...')
    df=tool.procesoEditarDataSet('data_v2.xlsx')
    if op==1:
        tool.obtenerArbolDec(df)
        tool.imprimirHora()
    if op==2:
        tool.obtenerBayes(df)
        tool.imprimirHora()
    if op==3:
        tool.verPrimerosDatos(df) 
        tool.imprimirHora()   

       
    
if __name__=='__main__':
    main()

