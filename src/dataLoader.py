import pandas as pd
import json

def load_data():
    """
    Parameters:
    None

    Returns:
    drugs_df (pandas.DataFrame) : la liste des drugs à chercher.
    clinical_trials_df (pandas.DataFrame) : la liste des clinical trials à trascrire dans un json sous certaines conditions.
    pubmed_df (pandas.DataFrame) : la liste des pubmed à trascrire dans un json sous certaines conditions.
    """
    # enregistremnt en dataframe des csv
    df_drugs = pd.read_csv('data/drugs.csv')
    df_clinical_trials = pd.read_csv('data/clinical_trials.csv')
    df_pubmed_csv = pd.read_csv('data/pubmed.csv')

    # enregistremnt en dataframe du json
    with open('data/pubmed.json', 'r') as f:
        df_json_pubmed = pd.DataFrame(json.load(f))

    # fusion des dataframes pubmed
    df_pumeds = pd.concat([df_pubmed_csv, df_json_pubmed], ignore_index=True)

    return df_drugs, df_clinical_trials, df_pumeds