import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation


def main():
    #df[nombreColumna][NúmeroFila] da el valor
    #print(df['Desc_curso'][0])
    print('Elige una opción:')
    print('1.Árbol de decisión 2.Bayes 3. Ver primeros datos')
    op=input()
    op=int(op)
    #Carga el archivo excel a un DataFrame
    #uevo Comentario
    print('Leyendo excel...')
    df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
    if op==1:
        obtenerArbolDec(df)
    if op==2:
        obtenerBayes(df)
    if op==3:
        verPrimerosDatos(df)    

def verPrimerosDatos(dataSet):
    print(dataSet.head())        

def obtenerArbolDec(dataSet):
    print('Elaborando árbol de decisión...')
    #Paso 1. Obtener variables dependientes e independientes (X:Independiente, Y:Dependiente)
    #En Python, como nomenclatura, "Feature columns"="Independent (X)", "Target Columns"="Dependent(Y)"
    print('Establenciendo variables independientes (X) y dependientes (Y)...')
    col_indep = ['Desc_curso', 'Facultad']
    X = dataSet[col_indep] 
    col_dep = ['NOTA_CURSO<12_(groups)']
    Y = dataSet[col_dep]
    #Paso 2: Dividir el dataset original en training set y test set
    print('Obteniendo set de Entrenamiento y pruebas...')
    #Para este ejemplo el los tamaños son: 30% test, 70% training
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1)
    print('Iniciando Proceso de árbol de decisión...')
    #Paso 4: Iniciallizar árbol de deicisón
    clf = DecisionTreeClassifier()
    print('Entrenando modelo...')
    #Paso 5: Entrenar modelo
    clf = clf.fit(X_train,Y_train)
    #Predicción para el dataset test
    y_pred = clf.predict(X_test)
    # Midiendo exactitud del modelo
    # Comentario
    print("Exactitud:",metrics.accuracy_score(Y_test, y_pred))
    print('-----Fin arbol de decisión------')

def obtenerBayes(dataSet):
    print('Elaborando proceso de Bayes...')
    print('-----Fin proceso de Bayes------')    
    
    



if __name__=='__main__':
    main()

