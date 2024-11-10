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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c30fe59-7a78-3252-a40b-d8336a6b0781 | -2.0954 | -48.8125 | 2024-11-10 13:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 5cdd0f2f-66c1-3777-871d-cfaf371c5dd1 | -23.9095 | -54.0606 | 2024-11-10 13:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 201.2 |
| 10255cf2-345f-3f11-8058-98c322128fb6 | -1.8017 | -48.0666 | 2024-11-10 13:10:00 | GOES-16 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| f84dc846-b58e-3d1f-9ac7-b6c16ad3112c | -4.0913 | -49.1323 | 2024-11-10 13:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 788f7d1c-9cda-367d-b990-a4781816ffe9 | -17.6073 | -57.5099 | 2024-11-10 13:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 356.5 |
| 5bb0d861-3f02-3f2f-96e3-9eb90da8e2ae | -8.6553 | -40.5231 | 2024-11-10 13:10:00 | GOES-16 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 126.9 |
| 567749a1-393a-351e-bb88-f085c93bab9f | -4.1246 | -43.5833 | 2024-11-10 13:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 728b64c9-7767-3c2b-a42d-7fab9946f04b | -1.5299 | -54.9941 | 2024-11-10 13:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 154.4 |
| 271eb0e7-db96-37a7-9319-440ed515b130 | -4.4349 | -44.6229 | 2024-11-10 13:20:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 6d386ea4-72ed-32a7-9ec5-0f881620c783 | -17.6069 | -57.5304 | 2024-11-10 13:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 302.2 |
| a5efdb7b-ef4d-36b9-bd76-788560d225dc | -3.9955 | -46.3981 | 2024-11-10 13:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 93.0 |
| e345bf03-e17a-333a-9091-d3fce1d03f57 | -3.4015 | -50.2801 | 2024-11-10 13:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 215.1 |
| 246fbfbb-3792-39ed-b4cc-936f5285e3d1 | -5.4548 | -43.2426 | 2024-11-10 13:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 63693789-6043-3484-9bc6-aa248cbbc8fa | -2.0477 | -46.1125 | 2024-11-10 13:20:00 | GOES-16 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 49486a7e-e712-30f0-a751-736d935f6b4b | -5.4546 | -43.2659 | 2024-11-10 13:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 8b26570a-635c-3491-a990-a05f0138fcd9 | -1.8017 | -48.0666 | 2024-11-10 13:20:00 | GOES-16 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 167.5 |
| 9b9e2d03-a1dd-3468-b181-79b123aba103 | -17.2933 | -57.4857 | 2024-11-10 13:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 149.0 |
| 70b066ae-081b-3489-ac5e-909d94086125 | -17.628 | -57.4458 | 2024-11-10 13:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.2 |
| 85245548-c69d-31ed-8296-946a72df6c16 | -2.0664 | -46.0899 | 2024-11-10 13:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 113.7 |
| f009f44c-a340-332d-b650-b76c5fdd730a | -2.0655 | -46.356 | 2024-11-10 13:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 90677fe5-626a-3929-9f6c-44d5a3442c5d | -1.5299 | -54.9941 | 2024-11-10 13:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| a56e749f-185d-3eed-a2d5-2abf69a07b97 | -5.9788 | -45.3621 | 2024-11-10 13:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 403e690c-b944-3763-b93c-d7fcbd9cc529 | -23.9089 | -54.083 | 2024-11-10 13:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 119.3 |
| cf1b8ec3-c2d0-3378-8bb5-f35d589f66b1 | -2.0954 | -48.8125 | 2024-11-10 13:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| c8375293-8e56-3b4e-aeec-31ebf26a8a0c | -4.1246 | -43.5833 | 2024-11-10 13:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| f23e37ab-33bd-3dea-9367-ffd0e33408e0 | -4.0913 | -49.1323 | 2024-11-10 13:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 74e8d10f-2fe2-3850-87f2-3049dca76dfd | -3.9953 | -46.4203 | 2024-11-10 13:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 154.7 |
| 7b9c6bd7-97a9-3dba-b650-515c11628e5b | -1.5116 | -54.9944 | 2024-11-10 13:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| a3891038-bf7b-3327-a5b8-f0318587b7db | -4.9108 | -45.8598 | 2024-11-10 13:20:00 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 4f7e91a4-2ed7-3c30-852c-eec270eb6cca | -4.1099 | -49.1315 | 2024-11-10 13:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| e2c0310e-e7e7-30fb-9616-bff4e4d1e37a | -17.6083 | -57.4482 | 2024-11-10 13:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 152.1 |
| f229c188-1511-3152-b365-dbc40abe98e6 | -17.6073 | -57.5099 | 2024-11-10 13:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 352.8 |
| 7f511655-7a47-318d-a604-e70f7fc4c15c | -2.0953 | -48.8338 | 2024-11-10 13:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| f88e2c1b-8874-3065-bcde-b8ab1291ff71 | -4.3978 | -41.9226 | 2024-11-10 13:20:00 | GOES-16 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 8662cbe2-d0f4-32ab-9b49-ad46c557c2a4 | -6.1366 | -42.5544 | 2024-11-10 13:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 100.4 |
| 5f2719a4-f314-35af-929d-80d0b66fb44d | -4.3979 | -41.8987 | 2024-11-10 13:20:00 | GOES-16 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 141.5 |
| 65095843-093a-329e-8f0a-f85deb21c5f3 | -17.5872 | -57.5328 | 2024-11-10 13:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.0 |
| a3798ee6-6618-3755-a134-c027731812cd | -5.455 | -43.2192 | 2024-11-10 13:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 91f33622-bae8-35f9-9062-0332b0d50798 | -2.0656 | -46.3339 | 2024-11-10 13:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 159eae66-692a-3507-be27-4538ba06aa17 | -2.6388 | -46.7597 | 2024-11-10 13:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| ba0eb181-b193-326d-a797-7d71db54295b | -2.2502 | -46.5723 | 2024-11-10 13:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 57018381-ec91-3938-a77a-53a8a1b6b158 | -6.2672 | -44.5442 | 2024-11-10 13:20:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 188fc50a-b39f-3300-9b03-5ba45dbbacbf | -5.66 | -43.344 | 2024-11-10 13:20:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 13728d49-6a84-3109-9477-cf47e83ff166 | -3.9485 | -48.1508 | 2024-11-10 13:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| c6928830-e74f-3b36-9806-6b86c91f72ff | -2.931 | -52.7753 | 2024-11-10 13:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 89194dcc-11fa-3578-a635-7e137cabcb08 | -2.0478 | -46.0903 | 2024-11-10 13:20:00 | GOES-16 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 8c3d8a94-2cf2-34ee-8c52-9deb819d5874 | -5.5608 | -43.9775 | 2024-11-10 13:20:00 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| cbd2e5fe-ba97-314e-a254-cec4e8f0bc1f | -3.8413 | -44.1283 | 2024-11-10 13:20:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 0129d844-5e78-33b9-85df-b2908a58781e | -2.8605 | -51.8349 | 2024-11-10 13:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 95c3f0db-3746-3034-82fd-233e2e40d9eb | -23.9095 | -54.0606 | 2024-11-10 13:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 144.1 |
| 05141bd5-4e6c-3136-82d5-00358c4f40c4 | -3.9669 | -48.1716 | 2024-11-10 13:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 511a5209-f2e9-31ee-a8de-41d9375c7c51 | -3.9483 | -48.1724 | 2024-11-10 13:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| bca62eaf-3427-3afb-ab5b-5396d3ea1834 | -2.455 | -46.3235 | 2024-11-10 13:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 58530a85-f1bc-33b0-9aec-aecfa4ea3d18 | -6.1363 | -42.578 | 2024-11-10 13:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 370.3 |
| c50e0038-5bd1-3c07-b8b6-795314ff6098 | -17.6073 | -57.5099 | 2024-11-10 13:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 342.7 |
| 3ac386b6-c832-34f3-9f9d-12196b6a0391 | -2.0664 | -46.0899 | 2024-11-10 13:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 138.3 |
| cd994cff-31ed-3340-922b-51ac4e2ea344 | -2.0953 | -48.8338 | 2024-11-10 13:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 168.5 |
| 5046deb5-4f8f-3b92-8931-70a8c77478aa | -5.5608 | -43.9775 | 2024-11-10 13:30:00 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 56c0ea2e-4d73-31c4-98bd-82bd35f321c4 | -3.9483 | -48.1724 | 2024-11-10 13:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 091ed64a-436b-339c-8f02-0ac99ad7e0cb | -2.1021 | -46.532 | 2024-11-10 13:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 6d801a55-4a7d-3c51-b1bb-3feab079562c | -2.0664 | -46.0676 | 2024-11-10 13:30:00 | GOES-16 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 3ceb47ef-f3fb-32e2-8d0a-16e50582a3ab | -2.0655 | -46.356 | 2024-11-10 13:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| f812b299-e00c-3346-9c29-726d2936dc3d | -6.1366 | -42.5544 | 2024-11-10 13:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 98.4 |
| 60a2674e-5dd2-310f-88d7-6799016ad080 | -1.5116 | -54.9944 | 2024-11-10 13:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| a68899ab-8130-3caa-b78b-0f59a4782e86 | -3.9486 | -48.1291 | 2024-11-10 13:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 01bccc2b-63c7-3bb4-9ac8-737e0f542271 | -3.8413 | -44.1283 | 2024-11-10 13:30:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 461bb20f-10e7-3c12-b337-d9d2d335f955 | -1.8017 | -48.0666 | 2024-11-10 13:30:00 | GOES-16 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 170.0 |
| 66b1cd50-c4e8-3d1e-aadb-db9bde3bbbfe | -6.2672 | -44.5442 | 2024-11-10 13:30:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| d9e53020-27f1-3621-9a78-e13be9750eeb | -8.3775 | -44.1617 | 2024-11-10 13:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 94c6b20b-56d4-3570-8b77-81cac1062092 | -6.1363 | -42.578 | 2024-11-10 13:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 261.9 |
| 89d46eb7-9c4b-3cb1-aea7-26e026aafe9b | -7.1144 | -47.8505 | 2024-11-10 13:30:00 | GOES-16 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| f5f2ee50-43b8-3a48-8ba1-53cbf4574f48 | -4.1244 | -43.6064 | 2024-11-10 13:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 948a97c4-1f31-3e2e-ad94-2b869c7418c7 | -5.66 | -43.344 | 2024-11-10 13:30:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 74d0ba1d-06bb-3c46-b64e-88d6b98baf51 | -4.1099 | -49.1315 | 2024-11-10 13:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 84d1bcac-3341-3219-a028-fa539a5654a9 | -2.931 | -52.7753 | 2024-11-10 13:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| fb4345d9-8471-3487-bbb7-d77b5f1bc755 | -3.9485 | -48.1508 | 2024-11-10 13:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 1094eba8-5108-3414-b7d2-d521c2111f66 | -2.8605 | -51.8349 | 2024-11-10 13:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 847217c4-e58b-3d38-8583-67862420f1ac | -17.6273 | -57.487 | 2024-11-10 13:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 134.8 |
| 0beab064-b7a3-3eed-bff9-3420b89ffec1 | -5.9788 | -45.3621 | 2024-11-10 13:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 4281689f-b18e-3fb8-bd81-f7c8e81d9364 | -5.455 | -43.2192 | 2024-11-10 13:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 9a5cad71-f09c-3529-9f9d-8ed633205a86 | -17.628 | -57.4458 | 2024-11-10 13:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.4 |
| 9a126723-ce65-3fab-8553-d0f21a00e3b2 | -4.3979 | -41.8987 | 2024-11-10 13:30:00 | GOES-16 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 7b5f908d-6ff2-3a0a-8e68-bfaac78eb1ac | -2.0478 | -46.0903 | 2024-11-10 13:30:00 | GOES-16 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| bfcdb335-15a7-3f1a-836f-d84697a54534 | -1.5299 | -54.9941 | 2024-11-10 13:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| e78fa9f8-10ea-34af-b162-3db8bc5e9173 | -23.9095 | -54.0606 | 2024-11-10 13:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 122.2 |
| 3969d282-4c9f-362a-929b-fe057b1d30a6 | -2.6387 | -46.7817 | 2024-11-10 13:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 15db9401-a08b-3b4d-abf5-41b83e10465f | -17.2933 | -57.4857 | 2024-11-10 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 175.4 |
| 689f3722-59e3-3bd8-916d-83e3190fed32 | -4.1246 | -43.5833 | 2024-11-10 13:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 5badde3a-3ec5-33d2-a5b1-9e3b4e50c6e3 | -17.6069 | -57.5304 | 2024-11-10 13:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 321.9 |
| aa888f05-a497-3637-a0c0-4d8706bf01df | -2.0954 | -48.8125 | 2024-11-10 13:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 153.3 |
| bc623361-4061-34cc-a5ea-8e36bbbe96fd | -3.9953 | -46.4203 | 2024-11-10 13:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 32d2d2f7-71b9-3279-8bb6-a659b79d296b | -6.9424 | -42.8126 | 2024-11-10 13:30:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 68.4 |
| 09c119cd-ca47-312d-b453-c0db37136c29 | -5.4546 | -43.2659 | 2024-11-10 13:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 950d5b05-596e-353c-97c9-790f2d2f5fc4 | -3.9669 | -48.1716 | 2024-11-10 13:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 86f7b416-a210-347e-8cdb-77e59743aee7 | -17.5872 | -57.5328 | 2024-11-10 13:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 143.3 |
| 86f9f413-fd54-3643-b485-1b488dd412ab | -23.9089 | -54.083 | 2024-11-10 13:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 84.8 |
| 2a74db02-62db-3a16-813e-7051ee130bac | -4.9108 | -45.8598 | 2024-11-10 13:30:00 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 2c15225e-4fb6-3594-8077-b8d2aaccd0b4 | -2.2095 | -47.733 | 2024-11-10 13:30:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 2a73e712-5072-3a80-9196-ff6dd5db4c58 | -4.4349 | -44.6229 | 2024-11-10 13:30:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 3f421bc8-d2d1-33bd-b05b-79319381d84c | -2.2502 | -46.5723 | 2024-11-10 13:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |


[Clique aqui para ver as próximas entradas](README129.md)
