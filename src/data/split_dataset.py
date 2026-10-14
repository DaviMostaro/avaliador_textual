from sklearn.model_selection import train_test_split

def separar_arquivos(arquivos):
    classes = []

    for arquivo in arquivos:
        classes.append(arquivo["classe"])

    treino, temporario = train_test_split(
        arquivos,
        test_size = 0.30,
        random_state = 42,
        stratify = classes,
    )

    classes_temporarias = []

    for arquivo in temporario:
        classes_temporarias.append(arquivo["classe"])

    validacao, teste = train_test_split(
        temporario,
        test_size = 0.50,
        random_state = 42,
        stratify = classes_temporarias,
    )

    return treino, validacao, teste