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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21d8e745-8708-32e4-b9ec-1205f3cf58a7 | -3.45071 | -50.3754 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9c971f9f-2b8e-3598-ac96-4d167f808629 | -3.32758 | -49.62987 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d90216a-222d-3003-b0a9-329d9a3e90f0 | -4.39897 | -50.5008 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01f0f50e-4f6f-358b-9d87-14d2281ed91b | -2.2946 | -48.55263 | 2024-11-06 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bd5e65d7-9644-367b-b714-d8eae5da0acb | -1.48874 | -60.37654 | 2024-11-06 04:36:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6becce50-b1fa-377f-81c3-b71985dbc7c6 | -2.84467 | -51.77277 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| bdab2f38-5a10-3c02-b0d4-987e1f5b6a0b | -3.33489 | -50.08177 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d84cb8c-e683-3c5c-a532-0be663af62db | 1.35681 | -50.86972 | 2024-11-06 04:36:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 000d68b5-ddb4-3c5c-91a0-99206c33072c | -1.35678 | -51.94853 | 2024-11-06 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11ed15e9-05cc-3538-a0b6-33ba31a8a50c | -2.9259 | -51.05222 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 49e1ac3e-338e-307a-b1d4-29d5098ebfaa | -5.4795 | -44.8569 | 2024-11-06 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0160ff4-1cb0-3b10-b288-6b34bc38d631 | -2.82908 | -52.90136 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| fb84bbb6-5007-395b-ae20-c4093716828c | -3.48731 | -50.38488 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 55f44c6b-cd75-3c4f-bf48-f1c40f62ab26 | -2.45013 | -48.94602 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f30ec8d-0724-39f4-85c2-5641846d339c | -3.10713 | -50.28806 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3fc7dd2-3c9f-32c4-a243-a7b36398f6fb | -2.79373 | -48.57452 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4856a3bf-6c20-3320-93db-5749ddd7207f | -2.82373 | -52.9102 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| daf62a48-258c-3deb-907c-cbb2ab79fca8 | -3.24877 | -53.36326 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b929b943-cd60-3d05-922f-5052e6c2cbfc | -0.40224 | -52.00293 | 2024-11-06 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9e28e60-0e77-3edd-a118-73c2b8bef5a4 | -3.75497 | -51.78097 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1176ebac-beb0-312b-afad-15010b82614d | -2.70379 | -48.65192 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd320915-2b98-379c-9495-f0a0a63bfe1d | -4.69319 | -45.64518 | 2024-11-06 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05e98f57-c7ca-34d5-b209-d87ccc6cb06b | -3.96465 | -48.14996 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af1fad81-debc-3f22-860d-1867c3215836 | -2.8979 | -48.62568 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 108c4538-fcc0-37fc-9976-a86126951471 | -3.03903 | -53.2696 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac3e1640-a7d3-3c3b-a28d-4f61a2071a8c | -2.88171 | -51.30798 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6f1bcee-8d54-3a1a-ae64-2b33897326f5 | -3.08554 | -54.50459 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b57ff2c8-66bb-31ff-969c-04ff2ec5d998 | -3.22824 | -54.86338 | 2024-11-06 04:36:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56414c60-49b9-3d2c-b8d4-79ce81239395 | -2.41001 | -48.8763 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bd6cc38-a547-39a1-86d0-3ef58955d7f6 | -0.24523 | -48.59707 | 2024-11-06 04:36:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57a55d98-1e62-3102-8071-56856b68696b | -4.03751 | -48.29247 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76928918-00bd-31c3-b827-d9a8bc7ad246 | -4.77191 | -48.68029 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 243f893d-cce1-3500-9b5f-9d896276b56e | -2.89545 | -44.80709 | 2024-11-06 04:36:00 | NOAA-20 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 475e1d66-7eef-3483-b0cf-097e4656b79a | -2.71863 | -54.15058 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| c77ddfa2-caf2-3de2-9882-abab3578604c | -2.67482 | -51.83198 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ea274dcc-0774-31a8-8316-a39f9edfa0de | -3.06579 | -47.77108 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2c06a81b-15ce-322b-8ed4-d4e09760f839 | -2.52899 | -48.20559 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b8eccd94-8140-3d23-bcc1-117887ff845d | -2.82985 | -48.67135 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ccb4f9e9-eb0e-3eb5-965d-0d1e53300752 | -3.6567 | -50.25237 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 222dff03-6cd4-3f21-9c1e-317a3de04f88 | -4.06624 | -45.95032 | 2024-11-06 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 656f8276-6a94-3cc6-8fdd-83529e0fa9de | -3.098 | -54.29185 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10e0f3a9-330c-3b64-a766-d999475dbc22 | -2.42027 | -46.688 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f52c1932-4fa1-3c08-9b6a-a0951bfd324e | -2.91609 | -51.04674 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 54d06788-28d3-31c1-9fbc-103e77dbd2b7 | -3.24159 | -50.01976 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f766ac74-26d8-3491-9596-befa219579f5 | -2.84518 | -49.86368 | 2024-11-06 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02b0f908-39a8-3da8-96e7-9f898980939d | -1.37634 | -51.41924 | 2024-11-06 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d2bc4f2-9ab4-3a55-9557-da5ad46dd82e | -3.66017 | -52.34378 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb748f13-a8e5-36b3-b05f-ed76fa35e48a | -5.55309 | -43.70722 | 2024-11-06 04:36:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ff9acdf8-2b3b-3c84-8998-8197b015e569 | -3.9555 | -48.36122 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bce83097-1555-3abe-88dc-821c48605524 | 0.45748 | -50.27649 | 2024-11-06 04:36:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95ba65c2-e6d3-3fe5-8bd7-723e19ad979c | -3.22823 | -50.38504 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 5c69ba56-21b7-3073-89ea-4179738e6499 | -2.15535 | -53.66561 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa3ce230-0669-3dc2-8ff5-622598460500 | -4.24675 | -48.04016 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83bd76c6-c962-38c2-a351-1354a5d17c0a | -2.93407 | -51.04568 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e85bac12-6539-363e-b1f6-12aa6f0d947a | -3.65649 | -52.34321 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd40cdde-f719-38ba-8d62-d29b72043b40 | -2.42227 | -53.66403 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60c0eb4c-5599-3324-b0a3-d3453bceda09 | -2.99959 | -54.09517 | 2024-11-06 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b08f334e-18ea-38a0-b824-f21816cccc4a | -4.70826 | -45.8167 | 2024-11-06 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 140da56e-bc8e-3141-ac23-9dc00ce0c95d | -3.77461 | -51.29517 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09491138-3510-33bd-97e1-2b0d8452bae2 | -5.55365 | -43.70338 | 2024-11-06 04:36:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fafbde70-54a6-3f4b-b71f-864d5fe40a1f | -2.62358 | -51.72734 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45dd9a51-c4aa-3f8a-ab1e-40009e765692 | -4.37189 | -47.23326 | 2024-11-06 04:36:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f77edcf7-5d48-3dba-b8d8-5bcc1e19be4b | -2.74966 | -48.72581 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8ce3fda5-382d-3c08-b4d1-0405bb3ee358 | -2.88531 | -53.97474 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 588278a3-bd79-31eb-a959-b9ddae6c6861 | -2.74079 | -54.11921 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bab7542d-39b1-32b0-86bc-f3ba3d91f6ad | -2.90754 | -49.51408 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30ef549a-e1c5-313b-be4e-d2a900876066 | -2.63332 | -48.58112 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34d219d2-e89f-3318-acdc-78bd79d5404a | -3.96634 | -48.16088 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3c4d48db-357b-3d06-af36-099f09ab486a | -5.54947 | -43.70279 | 2024-11-06 04:36:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 256d50ef-1e5e-3354-a1ad-9887ac3c9df0 | -2.98894 | -49.51612 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4762e950-d414-3e54-bd4c-f267f39af86a | -2.77586 | -54.73541 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a98e3459-1fca-3372-9abb-af208b11fa2b | -4.68995 | -46.38796 | 2024-11-06 04:36:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ef45c85d-5139-3bdf-8ff8-2b284a91b5c1 | -2.64719 | -49.11837 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0efe7a3-d8b1-3f1c-91b4-5c4c28845ab7 | -3.86094 | -46.61983 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b74cb46e-dca4-3533-87f6-c7aaa2301b0c | -2.83958 | -51.34575 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fdd8f60-e7f4-370f-ab69-e8d45f0e3c58 | -3.64245 | -50.1774 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d79b500c-0684-3cb1-9e9e-7eacea39c1a9 | -2.16324 | -50.51056 | 2024-11-06 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc58ff64-1391-3d83-b827-fe33eee1922e | -1.76785 | -51.29673 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2697681b-6cbc-3bf0-8e63-01fb73baa4b9 | -4.91 | -48.55656 | 2024-11-06 04:36:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98ce20e1-56fb-3750-91d9-e9d9280a573e | -2.83265 | -48.34844 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b467d3dd-5c41-3f65-a2c5-8cd07a937141 | -3.1151 | -54.24719 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f897eba0-9b34-3477-912d-9135ecebafd3 | -2.36059 | -46.80268 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59c71cf5-83a2-3b1f-b93d-fab3f2c89cf7 | -2.65307 | -48.56308 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f59baae0-7d08-3d63-9a31-00e0d4c7000e | -2.72766 | -51.70874 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55578e1c-00e2-3872-ba5f-963211832c4b | -4.24119 | -48.03211 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea2b3fb5-c836-3a89-8c3d-52efce0d29f4 | -3.1235 | -51.10925 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c22409db-100f-3040-bd3c-ef7241d56846 | -4.20998 | -53.55857 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 26e0351d-9401-3244-bc1a-1ce645c63223 | -2.49039 | -49.18537 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 899f9085-3771-3d51-9825-1133c8df4820 | -3.54071 | -47.38892 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| bfce15eb-640a-3e1d-b143-e1c012c52698 | -2.39147 | -49.14514 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9621185b-bd6e-3506-a72d-a6a10b1cf7a5 | -3.1026 | -50.29473 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 826357b2-3a05-3a4d-b13d-8e64d8506718 | -2.50233 | -49.10942 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62c93471-d6a8-32ea-8e8e-bb60de94b530 | -1.76518 | -51.22237 | 2024-11-06 04:36:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cccec28f-814b-318b-84d6-49faf5f15154 | -3.09195 | -49.40055 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57b46047-eaaa-31d1-93c7-79cd73cbb7b7 | -2.34468 | -48.94714 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3599aaa0-a9da-37c5-8990-4d42292b70fa | -3.0265 | -48.11006 | 2024-11-06 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3313f711-0a6a-3ca7-9291-6dc38a90e2b7 | -4.0298 | -48.29836 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 390877ec-dad0-35d4-9b48-d0249185a766 | -3.96579 | -48.16435 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| edad9974-872e-31c0-9120-ae7353c29ac5 | -2.96405 | -48.72395 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| deddc7f7-3358-3b92-a11d-db71b3f69a56 | -2.6072 | -54.5469 | 2024-11-06 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README42.md)
