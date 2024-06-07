import pandas as pd
import json

def load_data(loc_drugs='data/drugs.csv', 
              loc_clinicalTrials='data/clinical_trials.csv', 
              loc_pubmedCSV='data/pubmed.csv',
              loc_pubmedJSON='data/pubmed.json'):

    df_drugs = pd.read_csv(loc_drugs)
    df_clinical_trials = pd.read_csv(loc_clinicalTrials)
    df_pubmed_csv = pd.read_csv(loc_pubmedCSV)

    with open(loc_pubmedJSON, 'r') as f:
        df_json_pubmed = pd.DataFrame(json.load(f))

    df_pumeds = pd.concat([df_pubmed_csv, df_json_pubmed], ignore_index=True)

    return df_drugs, df_clinical_trials, df_pumeds

df_drugs, df_clinical_trials, df_pubmeds = load_data()






def clean_data(df_drugs, df_clinical_trials, df_pubmed):
    # Nettoyage des données des essais cliniques
    df_clinical_trials.dropna(subset=['scientific_title', 'journal', 'date'], inplace=True)
    try:
        df_clinical_trials = df_clinical_trials[df_clinical_trials["scientific_title"].astype(str).str.contains(r'[a-zA-Z]')]
    except Exception as e:
        print(f"Erreur lors du filtrage des scientific_title: {e}")
    df_clinical_trials['date'] = pd.to_datetime(df_clinical_trials['date'], errors='coerce')
    
    # Nettoyage des données PubMed
    df_pubmed.dropna(subset=['title', 'journal', 'date'], inplace=True)
    try:
        df_pubmed['date'] = pd.to_datetime(df_pubmed['date'], errors='coerce')
    except Exception as e:
            print(f"Erreur lors de la transformation en datetime: {e}")
    
    # Nettoyage des données des médicaments
    df_drugs.dropna(inplace=True)
    
    return df_drugs, df_clinical_trials, df_pubmed

df_drugs, df_clinical_trials, df_pubmeds = clean_data(df_drugs, df_clinical_trials, df_pubmeds)
if not df_drugs.isnull().values.any():
    print('df_drugs ne contient pas de valuers nulles')
else:
    print('df_drugs contient des valuers nulles')

if not df_clinical_trials.isnull().values.any():
    print('df_clinical_trials ne contient pas de valuers nulles')
else:
    print('df_clinical_trials contient des valuers nulles')

if not df_pubmeds.isnull().values.any():
    print('df_pubmeds ne contient pas de valuers nulles')
else:
    print('df_pubmeds contient des valuers nulles')