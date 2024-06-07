### DATA Engineering Pipeline

Projet d'implémentation d'une data pipline traitant des données CSV et JSON.<br>
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

PYTHON_TEST_DE V2.0/<br>
|<br>
|-- data/ # toutes les données<br>
| |-- drugs.csv<br>
| |-- pubmed.csv<br>
| |-- pubmed.json<br>
| |-- clinical_trials.csv<br>
|<br>
|--output/ # espace de sortie du main.py<br>
| |-- result.json<br>
|<br>
|-- src/ # programmes de traitement<br>
| |-- dataCleaner.py<br>
| |-- dataLoader.py<br>
| |-- dataToJson.py<br>
| |-- queries.py <br>
|<br>
|-- test/<br>
| |-- # programmes brouillons de test pour créer tout le reste<br>
|<br>
|-- main.py # lanceur de la pipeline<br>
|-- README.md<br>
|-- requirements.txt<br>
|-- SQL DE.txt<br>


## Auteur
Luis Alexandre Alba sanchez, étudiant M1 Bio-iformatique EFREI Paris, Villejuif<br>
LinkedIn: linkedin.com/in/luis-alexandre-albasanchez
