### DATA Engineering Pipeline

Projet d'implémentation d'une data pipline traitant des données CSV et JSON.
L'objectif est de générer un fichier JSON contenant un graphe de liaison entre différents médicaments et leurs mentions dans des publications scientifiques et des essais cliniques.

## Installation
1. cloner le dépot:
    ```sh
    git clone 
    cd PYTHON_TEST_DE V2.0
    ```
2. Créer un environnement virtuel pour installer les bons packages :
    ```sh
    python -m venv MonEnv
    Sur Windows: MonEnv\Scripts\activate
    ```
3. Installez les dépendances :
    ```sh
    pip install -r requirements.txt
    ```

## Strucuture du Projet

PYTHON_TEST_DE V2.0/
|
|-- data/ # toutes les données
| |-- drugs.csv
| |-- pubmed.csv
| |-- pubmed.json
| |-- clinical_trials.csv
|
|--output/ # espace de sortie du main.py
| |-- result.json
|
|-- src/ # programmes de traitement
| |-- dataCleaner.py
| |-- dataLoader.py
| |-- dataToJson.py
| |-- queries.py 
|
|-- test/
| |-- # programmes brouillons de test pour créer tout le reste
|
|-- main.py # lanceur de la pipeline
|-- README.md
|-- requirements.txt
|-- SQL DE.txt


## Auteur
Luis Alexandre Alba sanchez, étudiant M1 Bio-iformatique EFREI Paris, Villejuif
LinkedIn: linkedin.com/in/luis-alexandre-albasanchez
