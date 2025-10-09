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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2bfd63ed-8966-3308-81bd-c2d792c0bc88 | -16.37776 | -46.39119 | 2025-10-09 04:21:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3de9a9bb-2d11-30d8-bd4a-1fb360c46660 | -15.29329 | -47.32016 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40d6e417-263c-39d3-9ad6-e44641924425 | -15.49795 | -46.86901 | 2025-10-09 04:21:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8b21814-22fd-3275-824c-4ec392ae63f1 | -17.33967 | -45.09232 | 2025-10-09 04:21:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a22f8585-5e20-38c1-af46-57ac092818f3 | -17.37857 | -46.65728 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5cddb88-9ddf-3957-aafc-1a7c3f9cba02 | -14.52778 | -48.70692 | 2025-10-09 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56593554-1088-3522-95a7-c362ac9dda30 | -17.39047 | -46.88436 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fbd909bf-ac84-3ede-a9e4-7c7f02393cb5 | -14.84995 | -48.43894 | 2025-10-09 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 16fa67a7-a5a6-35f7-af7d-d2647f20549e | -17.53273 | -46.7566 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 31acbac4-c900-3251-90a5-2b7544e7a1af | -18.04013 | -44.9869 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30e9be0d-8b51-30c3-b265-c680a9c33be8 | -18.41191 | -45.23947 | 2025-10-09 04:21:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3acf8e90-8500-3f94-87eb-2a218f2a6d45 | -17.38704 | -45.05619 | 2025-10-09 04:21:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b0813a3-10c0-3011-b1fb-3fdabfd7fe00 | -17.97458 | -57.50758 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1023a2c0-cdbd-3684-8e9b-e0d0c6fd8e0e | -18.04162 | -44.70494 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbca804e-857e-3607-8e52-ec018cd2d7d3 | -17.63239 | -47.20308 | 2025-10-09 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4bb9350-ce94-3674-8255-615ace098ce2 | -17.95078 | -45.00154 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 521e02d4-e154-35f7-b6f8-4b115047cba1 | -15.47113 | -47.96773 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 44f2ef1f-e2e6-3436-9218-468d49070792 | -14.9343 | -46.78222 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5067e29b-92e2-3d49-b3e1-03a552975eb6 | -14.93317 | -46.78933 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a6c72521-4770-3cfd-be31-445e3531e2ce | -18.01996 | -57.56618 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 458ea000-0b0b-3cc2-b642-6cae6d323e68 | -17.91826 | -57.50515 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| b800d82f-4bcc-3628-853a-066e57a87f21 | -17.27061 | -46.91293 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6fdd85fd-0d18-3598-bce0-0a1f5568c708 | -16.37625 | -46.38078 | 2025-10-09 04:21:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6e07cb3-042f-3580-a750-6530f9e2529a | -16.70389 | -47.59324 | 2025-10-09 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7dbced46-c82c-3b8f-9bff-af0fa159bc98 | -15.47413 | -47.94928 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3f83e27f-733b-352b-800a-5ce113c85b0e | -21.60098 | -47.37402 | 2025-10-09 04:21:00 | NOAA-20 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94faa209-fe18-3d3e-87d9-bb9e8bc401ce | -15.2274 | -46.36732 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4acba8bb-d2ea-35e0-93d3-22d36d87a4ee | -17.97925 | -57.51274 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| f680fe78-c9e2-3c3e-9edd-c068d1ff0e32 | -15.99584 | -59.55193 | 2025-10-09 04:21:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60de56d4-a51d-3e74-853a-35b610b9fa76 | -17.91763 | -57.50815 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| fa4ee9c3-b374-36f9-9ddb-e70f975beb8d | -16.0842 | -45.78736 | 2025-10-09 04:21:00 | NOAA-20 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50373b54-0906-307e-b9f4-75d82080dc7e | -15.36255 | -44.16062 | 2025-10-09 04:21:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0abddc63-990c-3688-b639-85af4ff0c4c6 | -15.78487 | -46.2537 | 2025-10-09 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24026a98-a7c2-344f-aa5a-bcedf67c33f9 | -17.84598 | -57.65415 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1108ef29-b363-3aaf-898b-aadfc11411e7 | -14.52844 | -48.703 | 2025-10-09 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f784436-d407-35b5-adee-55ee14a8f109 | -18.77903 | -44.61536 | 2025-10-09 04:21:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| dddf7c94-a69b-36dc-9d98-ddb9f284705a | -17.37801 | -46.6609 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a21c6a41-2ea3-335b-b60c-2373bd904997 | -17.2012 | -47.649 | 2025-10-09 04:21:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a34fb9a-30c4-3aec-8a2b-ace520e76072 | -17.93867 | -57.54008 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f151d5cd-9cd8-3c3a-8c9d-3718068393a2 | -18.41879 | -45.24055 | 2025-10-09 04:21:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 52b186b8-0fe9-3715-b16a-26c1d49420a1 | -17.62851 | -47.20612 | 2025-10-09 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e223a9ad-2ca8-3ac9-9b84-abbeaff87750 | -16.62454 | -46.76761 | 2025-10-09 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2417b43e-c9ae-3224-beb5-9d9254b1fa66 | -17.3899 | -46.88796 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53cd2d61-3403-350b-bc2b-bcededf0d239 | -17.58157 | -46.06633 | 2025-10-09 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fff051ff-daf5-3eed-9de5-95d6f5edebe5 | -15.47339 | -47.96384 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21e596d6-6b0f-3234-ba44-564082bbbd31 | -16.07857 | -47.08413 | 2025-10-09 04:21:00 | NOAA-20 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87457f44-094b-38d3-a058-eb96bbe661f7 | -17.91348 | -57.50042 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.8 |
| 46f165fa-ac6e-31b0-9458-1b66614255a5 | -15.99806 | -59.5423 | 2025-10-09 04:21:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3e0bc8e-8498-3f96-ba29-53fb2e62a607 | -18.78562 | -47.0155 | 2025-10-09 04:21:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a0a05d9-72ea-3c8e-8b22-95dc15cf76d5 | -15.08054 | -46.60927 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 019476d3-7f77-3fd0-8375-e333a7b7ec90 | -18.07397 | -44.47561 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68d80ea8-3cfa-3e70-9dd7-fa048ccf7770 | -17.89462 | -57.66256 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 353b4c64-ee1f-34bd-bf48-3f63ebc3373f | -15.8145 | -43.78152 | 2025-10-09 04:21:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6b6826de-f04d-39fd-a81f-2387da62a76d | -18.39284 | -46.87865 | 2025-10-09 04:21:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f3535e06-a066-33ad-97f2-b48e724b3b17 | -18.05048 | -44.96436 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ed7f9301-41cd-3fb3-b546-a31a4ada41c4 | -15.52399 | -41.85677 | 2025-10-09 04:21:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3c6c8ccc-58ad-3c90-9fd4-5fb0109bcad1 | -18.41592 | -45.23609 | 2025-10-09 04:21:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 51ca83b1-3d1b-351a-8b14-d8ccaef77b4f | -16.60435 | -58.16256 | 2025-10-09 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 625a0017-d097-3821-a6a8-110d8a5a66b9 | -17.39103 | -46.88076 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d97784dc-6fa9-3765-a6cc-b775cee748e4 | -15.39212 | -48.04899 | 2025-10-09 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 466356ce-46ae-3d53-b230-d5ce64ce894b | -18.41535 | -45.24001 | 2025-10-09 04:21:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 84e8b77f-2280-32cc-b848-299b3451f7d5 | -17.89377 | -57.6665 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2f6dea81-a73a-3b56-aa68-ff3db38c1a6b | -15.31697 | -43.85439 | 2025-10-09 04:21:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7f8dc2fd-47a8-3968-93b9-8fedcffb35e7 | -16.42617 | -47.81792 | 2025-10-09 04:21:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec069a40-1a2e-3e8e-93df-8563752251d8 | -17.2172 | -47.65554 | 2025-10-09 04:21:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fdad8c45-c72e-3703-8bcc-a7587a16396a | -17.23904 | -46.94081 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff951520-de34-328d-a824-f6dbf4b837ce | -18.40332 | -45.25024 | 2025-10-09 04:21:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33454944-e50c-3279-bd20-5025c3fc612a | -17.6082 | -47.1841 | 2025-10-09 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da592827-79c8-3bd4-b13b-f206388a6277 | -15.22903 | -46.37856 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70dc8ab7-6c38-355b-b777-1d060c83c3fa | -16.27642 | -47.14289 | 2025-10-09 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82a19f00-a927-3d3d-84e9-923c27e02ff9 | -15.15518 | -49.56671 | 2025-10-09 04:21:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 245ba39b-c47b-3c7f-8755-2c7b0d0db80a | -15.47017 | -47.9524 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b295273a-a5f2-3081-8a0c-77703cc7a080 | -18.05279 | -44.94852 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 89e540bf-3fe7-3a9c-9aab-c15f8f39ab76 | -16.69886 | -45.0056 | 2025-10-09 04:21:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c3d7e06-2cd0-3d66-9180-6993c30f1572 | -18.06169 | -57.55416 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8fd9a9c2-a8ca-39e6-b379-71d92f9bb206 | -17.98075 | -44.96592 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 98623980-ec08-3367-b7b1-e97a2b536202 | -15.29728 | -46.18126 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e99be5b-5a93-3717-844d-868f21113316 | -15.48802 | -46.86736 | 2025-10-09 04:21:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8a107d8-10be-3825-aebb-f4c5d3f45782 | -15.49414 | -47.9637 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f267be72-f7ec-33ec-afb5-379e02c244cb | -17.81542 | -57.66034 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e713c78c-0092-3426-94a0-8c80b6d3d779 | -18.41648 | -45.2322 | 2025-10-09 04:21:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 64fb5150-2ad1-33bc-89f0-d9909ba84dfc | -16.74624 | -43.97255 | 2025-10-09 04:21:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6e1bb82e-afb8-3511-bd0e-3c4521160037 | -17.95251 | -44.98976 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 416b663e-0859-31dd-b09c-99ec3ebd968e | -16.28879 | -45.24543 | 2025-10-09 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5a7f6f9-590a-352b-9c35-ab7c131a1879 | -15.38109 | -47.30139 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ed91251-7f71-3e2d-a0d9-b80614aa6419 | -17.89124 | -44.26342 | 2025-10-09 04:21:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2be8fe03-8e83-3745-9442-ef7f40f4beb1 | -18.08871 | -44.44862 | 2025-10-09 04:21:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd2c5eeb-3b6d-3c8e-9c33-488b7e640683 | -16.08031 | -45.79045 | 2025-10-09 04:21:00 | NOAA-20 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81ebbb4c-9e2c-30bd-8799-aeec0a8b5322 | -17.53329 | -46.75299 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2ebb17e7-98eb-3830-834a-322fed7ede3c | -17.3717 | -46.89687 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 444839d2-8786-3713-815b-7d0f593f9e58 | -15.39151 | -48.0527 | 2025-10-09 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9e1b1549-34cb-3415-8055-9e0d19e94f7c | -20.71209 | -49.38033 | 2025-10-09 04:21:00 | NOAA-20 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd6339b1-c276-38d0-875c-3f8c3aab32f9 | -18.29627 | -45.43252 | 2025-10-09 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c244b2f3-fa2e-3220-9427-44bf63d61726 | -16.37513 | -46.38797 | 2025-10-09 04:21:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1757830e-a0ae-395c-958c-387e9eb51efc | -17.35649 | -46.64615 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04386c86-c548-385a-8dbb-28a612f03070 | -17.88819 | -57.66529 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6ab4bf1d-0cd8-3f7b-bc71-6e8175fc580d | -18.54169 | -45.0657 | 2025-10-09 04:21:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5628055e-75e0-39fc-ba21-a7f3783c2d9d | -16.62067 | -46.77064 | 2025-10-09 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b086e01-ad63-33e6-960e-583c566798fb | -14.92655 | -46.78825 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d96e944a-8d21-3406-9870-0aea9fd6a257 | -19.3374 | -43.90281 | 2025-10-09 04:21:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README48.md)
