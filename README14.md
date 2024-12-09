# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 922e3863-15f2-3204-8294-472250bfcc95 | -17.4 | -44.93 | 2024-12-09 11:00:00 | MSG-03 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8b75a780-2b59-3594-8b21-7e951a45f342 | -15.73 | -45.95 | 2024-12-09 11:00:00 | MSG-03 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 319f111b-49c2-3851-bab7-4879a444b68d | -6.9828 | -34.9165 | 2024-12-09 11:20:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 135.8 |
| 2cb48d4a-1d4c-3177-90a1-7b4711891ddc | -6.9825 | -34.9441 | 2024-12-09 11:20:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 101.8 |
| 7658f0de-c32d-3da6-b923-a880942cab4c | -8.85762 | -35.57455 | 2024-12-09 11:42:00 | TERRA_M-M | CAMPESTRE | ALAGOAS | Brasil | 2701357 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| e489e720-dbcf-3dcb-90a1-d0b94def5b37 | -6.98431 | -34.92076 | 2024-12-09 11:42:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 23.2 |
| 36a24c50-cf26-3983-a387-1451d6fabbf8 | -4.76031 | -40.49865 | 2024-12-09 11:42:00 | TERRA_M-M | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 45.9 |
| 52160dff-da48-33c3-a0c1-7408c80fd7b3 | -10.56825 | -36.71631 | 2024-12-09 11:42:00 | TERRA_M-M | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 298237fd-860d-3e78-be93-360763ef871b | -7.27308 | -35.9394 | 2024-12-09 11:42:00 | TERRA_M-M | CAMPINA GRANDE | PARAÍBA | Brasil | 2504009 | 25 | 33 | nan | nan | nan | Caatinga | 18.3 |
| dc03360e-70a9-3e72-82ae-5d568c2d9762 | -4.7574 | -40.50544 | 2024-12-09 11:42:00 | TERRA_M-M | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 42.2 |
| a12cf4fd-7d24-3a2d-9078-90485c4e7073 | -6.98278 | -34.93109 | 2024-12-09 11:42:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 37.2 |
| b27c9cd5-a31f-38b4-86b1-035217d2072c | -6.6225 | -35.09569 | 2024-12-09 11:42:00 | TERRA_M-M | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| e0ba873f-0687-3395-ae26-b72b5cba7377 | -6.98123 | -34.94157 | 2024-12-09 11:42:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 27.5 |
| f4b6a208-108d-3b95-ba04-ac1a92a9a67b | -7.06824 | -39.04843 | 2024-12-09 11:42:00 | TERRA_M-M | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 47.5 |
| 812216d2-57a6-3572-a3bb-75c92abf7f5c | -6.62402 | -38.78355 | 2024-12-09 11:42:00 | TERRA_M-M | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 23.4 |
| bedb7566-af33-3078-86e2-775a8958ac8b | -17.41514 | -44.89495 | 2024-12-09 11:44:00 | TERRA_M-M | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 0b0efebb-2dbc-3e01-a9e4-a946a2fd94be | -7.5953 | -46.6205 | 2024-12-09 13:00:00 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 132.5 |
| da208938-e9fc-370a-9a10-9665055934fe | 1.803 | -55.9997 | 2024-12-09 13:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 79b286d8-d2ee-3f35-95f9-5899d7cd0018 | 1.803 | -55.9997 | 2024-12-09 13:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 43b38e65-3541-3201-aa06-42c7aa37730f | -1.6589 | -45.921 | 2024-12-09 13:50:00 | GOES-16 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 4e53cc86-8b20-3ce4-8a70-9b024c3a9618 | -7.0625 | -39.044 | 2024-12-09 14:00:00 | GOES-16 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 92.6 |
| 4b11fe81-4cc4-36ed-b437-f27dfd1842f6 | -12.6532 | -43.8312 | 2024-12-09 14:00:00 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 321d138d-2e82-3715-8bbb-a40c31e5a4d6 | -7.7913 | -37.1241 | 2024-12-09 14:10:00 | GOES-16 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 103.4 |
| 3f738624-3f44-3f30-beca-af42f354e819 | -1.4549 | -45.9248 | 2024-12-09 14:10:00 | GOES-16 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 159.1 |


