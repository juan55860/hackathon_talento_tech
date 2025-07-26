import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def linear_regression(df, x_column, y_column):
    """
    Realiza una regresión lineal con un DataFrame.
    df: DataFrame con los datos
    x_column: nombre de la columna independiente
    y_column: nombre de la columna dependiente
    """
    X = df[[x_column]]  # variable independiente
    y = df[y_column]    # variable dependiente

    # Crear y entrenar el modelo
    modelo = LinearRegression()
    modelo.fit(X, y)

    # Ver resultados del modelo
    print(f"Pendiente (a): {modelo.coef_[0]:.4f}")
    print(f"Intersección (b): {modelo.intercept_:.4f}")

    # Visualización
    plt.scatter(X, y, color='blue', label='Datos reales')
    plt.plot(X, modelo.predict(X), color='red', label='Línea de regresión')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f"Regresión lineal: {y_column} vs {x_column}")
    plt.legend()
    plt.show()

    return modelo