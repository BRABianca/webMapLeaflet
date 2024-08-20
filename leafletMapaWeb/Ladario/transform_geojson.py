import json

def transform_geojson(input_file, output_file):
    # Lê o arquivo GeoJSON
    with open(input_file, 'r') as infile:
        data = json.load(infile)
    
    # Inicializa a lista de features transformadas
    transformed_features = []
    
    # Itera sobre as features e transforma
    for feature in data['features']:
        transformed_feature = {
            "type": "Feature",
            "properties": feature['properties'],
            "geometry": feature['geometry']
        }
        transformed_features.append(transformed_feature)
    
    # Cria a nova estrutura de GeoJSON
    transformed_data = {
        "type": "FeatureCollection",
        "features": transformed_features
    }
    
    # Salva a nova estrutura em um arquivo
    with open(output_file, 'w') as outfile:
        json.dump(transformed_data, outfile, indent=4)

# Define os arquivos de entrada e saída com caminhos completos
input_file = r'//10.100.56.41/c$/PRJ/ESTAGIARIOS/Bianca/leaflet/ladario/layersLadario/input.geojson'
output_file = r'//10.100.56.41/c$/PRJ/ESTAGIARIOS/Bianca/leaflet/ladario/layersLadario/output.geojson'

# Executa a transformação
transform_geojson(input_file, output_file)
