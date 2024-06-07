from collections import Counter

def journal_with_most_mentions(data):
    journal_mentions = Counter(mention['journal'] for mention in data)
    return journal_mentions.most_common(1)[0][0]


def find_related_drugs(medication, data):
    related_drugs = set()
    for mention in data:
        if mention['source'] == 'pubmed' and mention['drug'] == medication:
            related_drugs.update(related_mention['drug'] for related_mention in data if related_mention['journal'] == mention['journal'] and related_mention['source'] == 'pubmed' and related_mention['drug'] != medication)
    return related_drugs