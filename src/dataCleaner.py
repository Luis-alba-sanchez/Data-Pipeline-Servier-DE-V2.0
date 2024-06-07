import pandas as pd

def clean_data(df_drugs, df_clinical_trials, df_pubmed):
    """
    Parameters:
    drugs_df (pandas.DataFrame)
    clinical_trials_df (pandas.DataFrame)
    pubmed_df (pandas.DataFrame)

    Returns:
    drugs_df (pandas.DataFrame) : nettoyé.
    clinical_trials_df (pandas.DataFrame) : nettoyé.
    pubmed_df (pandas.DataFrame) : nettoyé.
    """
    # fusion des lignes se complètant
    df_clinical_trials.iloc[7, df_clinical_trials.columns.get_loc('journal')] = 'Journal of emergency nursing'
    df_clinical_trials = fusion_lignes_splite(df_clinical_trials) # ou tout simplement: df_clinical_trials.iloc[6, df_clinical_trials.columns.get_loc('id')] = 'NCT03490942'
    # df_pubmed = fusion_lignes_splite(df_pubmed) # non necessaire
    
    # retirer les lignes contenant des titres vides
    df_clinical_trials = df_clinical_trials[df_clinical_trials["scientific_title"].astype(str).str.contains(r'[a-zA-Z]')]
    df_pubmed = df_pubmed[df_pubmed["title"].astype(str).str.contains(r'[a-zA-Z]')]

    # Nettoyage des observations contenant des valeurs nulles
    df_pubmed.dropna(inplace=True)
    df_clinical_trials.dropna(inplace=True)
    df_drugs.dropna(inplace=True)

    # réctification des dates
    df_clinical_trials['date'] = pd.to_datetime(df_clinical_trials['date'], errors='coerce')
    df_pubmed['date'] = pd.to_datetime(df_pubmed['date'], errors='coerce')

    return df_drugs, df_clinical_trials, df_pubmed


def fusion_lignes_splite(df):
    """
    Parameters:
    df (pandas.DataFrame) : dataframe à modifier.

    Returns:
    df (pandas.DataFrame) : le même dataframe avec des lignes pleines en plus.
    """
    all=[]
    # parcour du dataframe
    for i in range(len(df)):
        if df.loc[i].isnull().sum() != 0:
            # enregistrement de la ligne contenant des valeures nulles
            l1=df.loc[i].to_list()
            # parcour de toutes les lignes suivantes pour chercher une ligne semblable
            for j in range(i+1, len(df)):
                # enregistrement de la ligne suivante
                l2 = df.loc[j].to_list()
                diff = len(list(set(l1).symmetric_difference(set(l2))))
                # si les deux lignes ont des similitudes, on ajoutes à la première ligne
                # ce que la deuxième peut completer
                if diff < len(l2):
                    difference = list(set(l2) - set(l1))[::-1]
                    cpt=0
                    for i in range(len(l1)):
                        if pd.isna(l1[i]):
                            l1[i]=difference[cpt]
                            cpt=cpt+1
                # une fois la tâche réalisé, en vu de notre dataset, ça ne sert à rien de répéter
                break 
            all.append(l1) # on stocke la ligne remplie

    # on ajoute chaque lignes de all au dataframe
    cpt = 0
    for row in all:
        df.loc[len(df)] = row

    return df