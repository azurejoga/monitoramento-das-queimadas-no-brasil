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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2f1b382-bd7d-3225-aa28-fa09549e66c1 | -3.249 | -50.31125 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| ca12f1e5-74cc-3446-a117-76436c4debee | -3.20361 | -50.61727 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 4dce3d91-2a70-336c-946d-1c674a98ee97 | -2.42329 | -53.65902 | 2024-11-10 06:12:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3c144f54-4195-3bce-b946-e93019928e6a | -2.09323 | -48.79638 | 2024-11-10 06:12:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 92a075e2-1550-3ce4-a173-41473d6479da | -3.10525 | -49.40634 | 2024-11-10 06:12:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| eea4d1fb-7218-3056-ad5c-f3d975524bab | -1.16762 | -52.08933 | 2024-11-10 06:12:00 | AQUA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 5f3830db-7eda-3bb2-807f-22c906f0aa28 | -3.24921 | -50.30399 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 5cd6b204-1466-3672-b453-86321b0adc0b | -2.67402 | -51.81912 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b960e110-b018-397c-9016-b0e2d4537d67 | -1.5433 | -52.20375 | 2024-11-10 06:12:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 2aa76f5b-e635-36e9-bbfc-d74c0e13829e | -2.09637 | -48.82634 | 2024-11-10 06:12:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 295e8f2b-7e91-324a-b1ff-7ac41f8eca8e | -1.67152 | -52.04396 | 2024-11-10 06:12:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 1b5efebd-d6c2-35a1-827c-3fb91bfd2001 | -1.48135 | -54.30103 | 2024-11-10 06:12:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 10241edf-58f0-347e-8888-99b4c0a2e287 | -3.20572 | -50.62472 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 2b1c8f52-2bb4-333d-b89c-7fff9735ccab | 2.85294 | -60.07551 | 2024-11-10 06:12:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 12fbfb28-4eaa-3fc7-a5ec-c90f76848b1d | -3.22366 | -50.27299 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 183.1 |
| 7d5339fb-45f9-318b-b3ac-7954042554f0 | -3.2198 | -50.30002 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 34041964-cf5f-39c6-9ae3-8b420149d3aa | -3.12813 | -50.42248 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 18b9eab8-a804-3ee8-b98f-de54f2aec45b | -3.22326 | -50.28016 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 124.7 |
| a06a5f3c-08ed-350a-8d5c-ea2e5c3e2543 | -3.14269 | -50.42432 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 423ffac9-ed34-3f5e-baad-3e83b99ee075 | -2.93167 | -51.47567 | 2024-11-10 06:12:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| e3a700c0-1e2b-30f8-8b22-b50b7f747391 | -3.1245 | -50.44895 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 478a0734-e045-333d-b3bd-159dcc581009 | -2.76186 | -49.33862 | 2024-11-10 06:12:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 2da9a3fc-70d5-36ad-8b6b-a917c58bfb4c | -3.2345 | -50.30204 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 164.9 |
| 71597467-2dcd-31e4-b6cc-cbd6b5399928 | -2.94597 | -52.57401 | 2024-11-10 06:12:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 0f213064-3f92-3bbf-bd17-c89b01d34600 | -3.23429 | -50.30923 | 2024-11-10 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 67ecc0c4-474e-367c-a2c8-8f3efe369da1 | -1.27807 | -53.7173 | 2024-11-10 06:12:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 08faab94-ca73-3ba8-b920-610826f11d39 | -1.34105 | -54.63071 | 2024-11-10 06:12:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 5a3afbad-117e-391d-a28a-efc6724d5d82 | -1.52158 | -55.00227 | 2024-11-10 06:12:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1f4f2c30-bdb1-3e09-a86b-dc4ac579dcfd | -2.91837 | -51.47375 | 2024-11-10 06:12:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| b68bc5ad-b78f-395d-9d08-181875f83fdb | -5.05448 | -49.99992 | 2024-11-10 06:14:00 | AQUA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 6975a26b-5df5-3606-83f9-39cb34722ada | -3.35659 | -53.41078 | 2024-11-10 06:14:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 4a9d28e4-b0aa-361b-91fd-2b789510837e | -3.00992 | -53.24993 | 2024-11-10 06:14:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 763e6fbd-5cf5-349a-b8e2-679d9966603d | -3.4345 | -50.28657 | 2024-11-10 06:14:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| f69c37a4-ac4a-3b8f-ba9f-96c638013705 | -3.35886 | -53.39545 | 2024-11-10 06:14:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 9a2e1b70-c041-3185-9682-6eaf539186e9 | -3.94308 | -48.13615 | 2024-11-10 06:14:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| ad1dfcee-76c5-364c-b40b-eb1c827f1ea5 | -3.0931 | -53.31524 | 2024-11-10 06:14:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 96136562-d3f2-37f5-8597-ade42ef6ff56 | -3.69863 | -54.61203 | 2024-11-10 06:14:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fc37e7c3-c161-37c9-906d-5aab21459abf | -3.09508 | -53.31004 | 2024-11-10 06:14:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 0b1fcc96-590c-36cb-873b-fbca32ff1882 | -3.23117 | -53.06701 | 2024-11-10 06:14:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 47146096-bf68-39fe-b5fa-886a125420ee | -4.10174 | -51.06284 | 2024-11-10 06:14:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| eb3c1b7f-b9bd-30b9-be78-50d9db1d4b7c | -3.01118 | -53.25903 | 2024-11-10 06:14:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 5b25e254-2a7d-372f-a809-474c53f622f8 | -3.22168 | -53.04929 | 2024-11-10 06:14:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 64ce6b8b-e1e0-3fdf-a53b-9bbc6e495e8f | -3.22719 | -53.04312 | 2024-11-10 06:14:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 76a22bfb-f546-3f55-b394-9379a89d3b13 | -3.96041 | -48.14636 | 2024-11-10 06:14:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 59966219-2976-3beb-8ab0-67f4bbbde6ed | -3.01921 | -53.2673 | 2024-11-10 06:14:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 80fe8ec1-b807-3173-a6fd-c2f70268be45 | -4.10745 | -49.11044 | 2024-11-10 06:14:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| b4fcc0e1-cb79-352b-a207-2ff1e287b5bd | -3.00772 | -53.26556 | 2024-11-10 06:14:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 8efddd7f-c246-3b5f-946d-de07ecead747 | -3.35581 | -53.40205 | 2024-11-10 06:14:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 5f279ded-39be-3899-aa76-d920d7127122 | -3.07848 | -57.50201 | 2024-11-10 06:14:00 | AQUA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0e4e9c0a-0a14-3c2e-9e9a-4a1242aee468 | -3.23346 | -53.05076 | 2024-11-10 06:14:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 369f9d67-4976-3600-8605-5d60cd6485e8 | -4.28106 | -50.66204 | 2024-11-10 06:14:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 1756a54b-1575-378e-8d6c-d9ef91a4c392 | -4.10439 | -48.95968 | 2024-11-10 06:14:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| f82b2dca-2dfc-3049-ab67-5d89a8e4da59 | -3.28729 | -53.25431 | 2024-11-10 06:14:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 4b8011a3-c7a6-3b3b-86d9-6a72527b1414 | -3.22478 | -53.05937 | 2024-11-10 06:14:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| e86c6e2b-3a13-3d05-9ef8-ff30dcb3b7dc | -3.86972 | -51.97028 | 2024-11-10 06:14:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 80ffda03-2ba7-369e-94e4-bfe1e48f6bb2 | -3.26777 | -53.70244 | 2024-11-10 06:14:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 3d125b5d-1d0b-33e0-87bf-dad729c64217 | -3.10459 | -53.31681 | 2024-11-10 06:14:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9ffd017f-6bbb-3831-8ca0-613f3b47dd7d | -2.84906 | -53.97597 | 2024-11-10 06:14:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| bceb0e19-29ae-3d8b-b64a-b2d84e56ebbf | -3.43396 | -50.29364 | 2024-11-10 06:14:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 872de9f1-2306-3fed-a6ff-9ce0aa4f70c9 | -3.28531 | -53.66016 | 2024-11-10 06:14:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 04b32770-cdfd-376c-a318-598c8cd74c26 | -3.25662 | -53.70087 | 2024-11-10 06:14:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 9512e6c3-3e89-33c2-8544-a81c23f0c7f2 | -3.50701 | -54.02905 | 2024-11-10 06:14:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3b881de5-270e-3bfa-a776-36164a3e9299 | -4.10151 | -49.10259 | 2024-11-10 06:14:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 9aa89f59-82ed-3041-a423-5504e0e0486e | -3.21941 | -53.06551 | 2024-11-10 06:14:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| be2246ba-0881-3e6b-9c3e-c346cd6f1e88 | -3.28679 | -53.24345 | 2024-11-10 06:14:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 213f0f23-740e-3c60-a102-092dcd5f4976 | -2.83822 | -53.97443 | 2024-11-10 06:14:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 098cdcc9-674a-3ddb-95c3-f88b3e6c697e | -3.50839 | -53.78526 | 2024-11-10 06:14:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 8e1e6b0e-ac57-3b61-9c02-a2910f373454 | -3.28455 | -53.25945 | 2024-11-10 06:14:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f50592b2-9dad-3b7e-baaf-87ddd5617360 | -3.94296 | -48.14357 | 2024-11-10 06:14:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 1268be1d-3b4e-344b-92a9-ac1edac78d59 | -3.90435 | -51.91322 | 2024-11-10 06:14:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| de192c9d-c20e-37b9-9f22-cf6b3c75ef13 | -3.28316 | -53.67492 | 2024-11-10 06:14:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 5e05ed57-4fdf-3876-a049-7be14e0c22a5 | -2.44958 | -57.94405 | 2024-11-10 06:14:00 | AQUA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 37933be2-5b24-3a92-8616-5f937dec4ba7 | -17.61979 | -57.51475 | 2024-11-10 06:16:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| 5690f854-f7b1-3c44-b79e-ae90fe7d0df3 | -17.28899 | -57.48504 | 2024-11-10 06:16:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.2 |
| 0173f72b-3be7-35df-8235-b0441a07b473 | -17.60928 | -57.51332 | 2024-11-10 06:16:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 247.8 |
| 4bc31ec4-a808-3c27-870b-be6c5840299e | -17.29554 | -57.47937 | 2024-11-10 06:16:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.6 |
| 94203965-d802-30cb-9378-8b7a1f972b0b | -17.28726 | -57.49817 | 2024-11-10 06:16:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 31.4 |
| 64fe7c52-823a-3d62-9f6e-1eb475af9d91 | -17.61809 | -57.52798 | 2024-11-10 06:16:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.5 |
| fe6b127b-23bf-3ed9-8cbf-42b71d35e32c | -17.61098 | -57.50005 | 2024-11-10 06:16:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.2 |
| ea83c61b-5772-3e40-8061-ee2050a5a415 | -17.59876 | -57.51189 | 2024-11-10 06:16:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 37.6 |
| 42522fb7-3a1f-32fa-92fd-0c3b0b14e9c2 | -17.24706 | -57.47933 | 2024-11-10 06:16:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 9d7d4032-5552-36f2-bd43-84b8938bb62d | -17.62859 | -57.52942 | 2024-11-10 06:16:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 7eda2a9b-ae1c-3b5f-bf95-a20b892a725b | -12.42043 | -64.13681 | 2024-11-10 06:16:00 | AQUA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 0c855eda-147b-383f-aa6e-453246d033e6 | -17.63202 | -57.50292 | 2024-11-10 06:16:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| ab2a94b3-123b-3b1d-b43f-132c06e16a24 | -17.62321 | -57.48819 | 2024-11-10 06:16:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 56014257-0c41-35f7-8965-fda1aae1a704 | -17.60589 | -57.53977 | 2024-11-10 06:16:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 8c49ba0e-3058-3a20-b904-e28f172b5277 | -17.6215 | -57.50149 | 2024-11-10 06:16:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.6 |
| 3695d6bc-c8aa-3da8-8033-0a850eda6c55 | -17.29773 | -57.49959 | 2024-11-10 06:16:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 4d555285-3409-3fe3-983c-4e4bdd1cbc5f | -17.24537 | -57.49245 | 2024-11-10 06:16:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.2 |
| 9e244822-5c4b-35e8-a73a-d8c4c086c867 | -17.6303 | -57.51618 | 2024-11-10 06:16:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.4 |
| 1f841a3d-c43b-3178-ad97-cc786054a40e | -17.29389 | -57.49253 | 2024-11-10 06:16:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.3 |
| fff37295-d66a-38da-9b58-d27b9ab95430 | -12.42245 | -64.12433 | 2024-11-10 06:16:00 | AQUA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 30.8 |
| a5ee9225-ca46-3082-b9cb-522fbe4a7ad7 | -17.29947 | -57.48647 | 2024-11-10 06:16:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.8 |
| b221001e-5cac-3b02-a565-de8d13b9aa47 | -17.59708 | -57.52512 | 2024-11-10 06:16:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.7 |
| d77f0914-bc0d-35c9-b4b6-4dda410a5d46 | -3.2536 | -50.3059 | 2024-11-10 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 704949ea-a39e-332c-a828-4eb7520e7b1b | -2.0953 | -48.8338 | 2024-11-10 06:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| f9ea7bc7-b6d8-3d8e-9f39-60408e963136 | -3.1422 | -50.4562 | 2024-11-10 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 88f6bc77-c147-31ec-883d-c6a7930f77f8 | -3.1239 | -50.4358 | 2024-11-10 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 237dd464-14ca-3597-bb07-f6f83967fb42 | -2.9494 | -52.7748 | 2024-11-10 06:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 472fcc2d-745e-381d-a151-78283b860d20 | -2.931 | -52.7753 | 2024-11-10 06:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |


[Clique aqui para ver as próximas entradas](README123.md)
