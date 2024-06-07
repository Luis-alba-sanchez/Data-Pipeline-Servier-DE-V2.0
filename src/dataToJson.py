import re

def find_mentions(title, drugs_df):
    """
    Parameters:
    title (str) : Le titre à relire.
    drugs_df (pandas.DataFrame) : la liste des drugs à chercher.

    Returns:
    list(str) : La liste des drugs présentent dans le titre.
    """
    mentions = []
    for _, row in drugs_df.iterrows():
        if re.search(r'\b' + re.escape(row['drug']) + r'\b', title, re.IGNORECASE):
            mentions.append(row['drug'])
    return mentions

def transform_data(drugs_df, clinical_trials_df, pubmed_df):
    """
    Parameters:
    drugs_df (pandas.DataFrame) : la liste des drugs à chercher.
    clinical_trials_df (pandas.DataFrame) : la liste des clinical trials à trascrire dans un json sous certaines conditions.
    pubmed_df (pandas.DataFrame) : la liste des pubmed à trascrire dans un json sous certaines conditions.

    Returns:
    json : graphe  de  liaison  entre  les différents médicaments et leurs mentions respectives.
    """
    mentions = []

    for _, row in clinical_trials_df.iterrows():
        drugs = find_mentions(row['scientific_title'], drugs_df)
        for drug in drugs:
            mentions.append({
                'drug': drug,
                'source': 'clinical_trials',
                'title': row['scientific_title'],
                'date': row['date'],
                'journal': row['journal']
            })

    for _, row in pubmed_df.iterrows():
        drugs = find_mentions(row['title'], drugs_df)
        for drug in drugs:
            mentions.append({
                'drug': drug,
                'source': 'pubmed',
                'title': row['title'],
                'date': row['date'],
                'journal': row['journal']
            })
    
    return mentions
