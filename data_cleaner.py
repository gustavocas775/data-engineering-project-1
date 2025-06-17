# data_cleaner.py
import pandas as pd

def clean_data(filepath):
    df = pd.read_csv(filepath)
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    df = df.dropna()
    print("Datos limpios y listos.")
    return df

if __name__ == "__main__":
    # Crear un archivo de datos dummy para el ejemplo
    dummy_data = {
        'ID': [1, 2, 3, 4, 5, 6],
        'NUM': [1, 2, 3, 4, 5, 6],
        'Nombre Completo': ['Juan Perez', 'Maria Garcia', 'Carlos Lopez', 'Ana Martinez', 'Pedro Sanchez', 'Juan Lopez'],
        'Edad': [25, 30, None, 40, 35, 20],
        'Ciudad': ['Lima', 'Bogota', 'Quito', 'Lima', 'Santiago', 'Arequipa']
    }
    pd.DataFrame(dummy_data).to_csv('raw_data.csv', index=False)

    # Procesar los datos dummy
    print("Procesando raw_data.csv...")
    cleaned_df = clean_data('raw_data.csv')
    print(cleaned_df.head())
    cleaned_df.to_csv('cleaned_data.csv', index=False)
    print("Datos limpios guardados en cleaned_data.csv")