import json
from src.dataLoader import load_data
from src.dataCleaner import clean_data
from src.dataToJson import transform_data
from src.queries import journal_with_most_mentions, find_related_drugs

def run_pipeline():
    
    drugs_df, clinical_trials_df, pubmed_df = load_data() # Chargement des données
    drugs_df, clinical_trials_df, pubmed_df = clean_data(drugs_df, clinical_trials_df, pubmed_df) # nettoyage des données
    mentions = transform_data(drugs_df, clinical_trials_df, pubmed_df) # recherche des mentions des drugs

    output_path = 'output/result.json'
    with open(output_path, 'w') as f:
        json.dump(mentions, f, default=str)

    # Extraire le nom du journal qui mentionne le plus de médicaments différents
    print("Journal avec le plus de mensions:", journal_with_most_mentions(mentions))

    # Trouver l'ensemble des médicaments mentionnés par les mêmes journaux que 'ATROPINE'
    print("Drugs liés à l'ATROPINE:", find_related_drugs('ATROPINE', mentions))

if __name__ == "__main__":
    run_pipeline()
