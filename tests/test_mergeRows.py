import pandas as pd
df_clinical_trials = pd.read_csv('data/clinical_trials.csv')

all=[]
# parcour du dataframe
for i in range(len(df_clinical_trials)):
    if df_clinical_trials.loc[i].isnull().sum() != 0:
        # enregistrement de la ligne contenant des valeures nulles
        l1=df_clinical_trials.loc[i].to_list()
        # parcour de toutes les lignes suivantes pour chercher une ligne semblable
        for j in range(i+1, len(df_clinical_trials)):
            # enregistrement de la ligne suivante
            l2 = df_clinical_trials.loc[j].to_list()
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
    df_clinical_trials.loc[len(df_clinical_trials)] = row

print(df_clinical_trials)
    