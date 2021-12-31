import requests
import json

def get_serves(url, regions_mundi):
    r = requests.get(url)
    dict_regions = r.json() # regiões
 
    # A chave 'archive' contém uma lista de 'objetos' Json, onde cada objeto é representado por um dicionário?
    list_arq_regions = dict_regions['archive']

    # Quantidade total de servidores
    n_regions_total = len(list_arq_regions)

    # Lista que irá armazenar servidores utilizados pela mundiale que estão na lista de 'objetos'
    regions_mundi_check = []

    # Percorre a lista de 'objetos' Json
    for dict_region in list_arq_regions:
        for region_mundi in regions_mundi:
            # Verifica se o nome do 'objeto' corrente está na lista de servidores da Mundiale
            if region_mundi in dict_region['service_name']:
                regions_mundi_check.append(dict_region['service_name'])

    n_regions_mundiale = len(regions_mundi_check)
    n_regions_global = n_regions_total - n_regions_mundiale
    dict_final = {'global': n_regions_global,
                  'mundiale': n_regions_mundiale}

    # The process of encoding the JSON is usually called serialization
    # Quão importânte é essa conversão?
    return json.dumps(dict_final) 
    
if __name__ == '__main__':
    url = 'https://status.aws.amazon.com/data.json'
    regions_mundi = ['N. Virginia', 'Oregon', 'Sao Paulo']

    regions_filter = get_serves(url, regions_mundi)
    print(regions_filter)