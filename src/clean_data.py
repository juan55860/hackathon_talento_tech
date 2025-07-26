from sklearn.preprocessing import MinMaxScaler

def normalize_data(df, columns):
    """
    Normaliza las columnas numéricas especificadas en el DataFrame usando MinMaxScaler.
    Devuelve un nuevo DataFrame con las columnas normalizadas.
    """
    scaler = MinMaxScaler()
    df_norm = df.copy()
    df_norm[columns] = scaler.fit_transform(df[columns])
    return df_norm
