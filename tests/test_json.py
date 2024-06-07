import json

# Ouvrir le fichier JSON
file_path = 'data/pubmed.json'
with open(file_path, 'r') as f:
    try:
        data = json.load(f)
        print("JSON chargé avec succès!")
        print(data)
    except json.JSONDecodeError as e:
        print(f"Erreur lors du chargement du JSON: {e}")
    
print(data)

