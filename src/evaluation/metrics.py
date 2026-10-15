from collections import Counter

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
)

CLASSES = [
    "Ensino Fundamental I",
    "Ensino Fundamental II",
    "Ensino Médio",
    "Ensino Superior",
]

def avaliar_modelo(modelo, exemplos):
    textos = []
    classes_reais = []

    for exemplo in exemplos:
        textos.append(exemplo["texto"])
        classes_reais.append(exemplo["classe"])

    classes_previstas = modelo.predict(textos)

    print("\nDistribuição das classes reais:")
    print(Counter(classes_reais))

    print("\nDistribuição das classes previstas:")
    print(Counter(classes_previstas))

    acuracia = accuracy_score(classes_reais, classes_previstas)
    macro_f1 = f1_score(
        classes_reais,
        classes_previstas,
        labels=CLASSES,
        average="macro",
        zero_division=0,
    )

    print("Acurácia:", round(acuracia, 4))
    print("Macro F1:", round(macro_f1, 4))

    print("\nRelatório por classe:")
    print(
        classification_report(
            classes_reais,
            classes_previstas,
            labels=CLASSES,
            zero_division=0
        )
    )

    print("Matriz de confusão:")
    print("Ordem das classes:", CLASSES)
    print(
        confusion_matrix(
            classes_reais,
            classes_previstas,
            labels=CLASSES,
        )
    )