import json
import os

def transform_geojson(input_file, output_file):
    try:
        # Verifica se o arquivo de entrada existe
        if not os.path.exists(input_file):
            print(f"Arquivo de entrada {input_file} não encontrado.")
            return
        
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
        
        print(f"Transformação concluída com sucesso! Arquivo salvo em {output_file}")
    
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON. Verifique se o arquivo está no formato GeoJSON válido.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Define os arquivos de entrada e saída com caminhos completos
input_file = r'//10.100.56.41/c$/PRJ/ESTAGIARIOS/Bianca/leaflet/ladario/layersLadario/input.geojson'
output_file = r'//10.100.56.41/c$/PRJ/ESTAGIARIOS/Bianca/leaflet/ladario/layersLadario/output.geojson'

# Executa a transformação
transform_geojson(input_file, output_file)
