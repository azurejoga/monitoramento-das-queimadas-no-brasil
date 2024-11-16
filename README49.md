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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8a37eb0-8450-32f5-8c03-830e70593111 | -3.58124 | -50.53516 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 978647a0-5ed9-32ce-9715-267cc2adf008 | -4.0757 | -49.13733 | 2024-11-16 04:50:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7deb443e-da0f-310b-a8fc-df8297abb2d3 | -7.07394 | -49.29505 | 2024-11-16 04:50:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf51551d-3662-3120-86d9-f52a4a5d8501 | -5.12172 | -45.16022 | 2024-11-16 04:50:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f4ac536-880c-309f-9d2b-f75b25a03d9e | -3.68911 | -50.1094 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d6af3e6-c6a0-3bc7-b643-e73cf967aabb | -5.74757 | -49.45982 | 2024-11-16 04:50:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 3a7c02c4-9cae-3992-9f34-b1e514b5fda6 | -3.57839 | -50.50906 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4fad946b-9d5f-318f-8fed-806a103c7694 | -4.70163 | -50.35914 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6be3ba9e-2dfc-35fe-8154-49c7f380317e | -4.37599 | -50.71497 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4207f403-ecd1-3a7d-804b-1f9c402a804d | -10.83594 | -44.45944 | 2024-11-16 04:50:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71ce0e1a-9bfc-3054-aaf4-ef4edc05c4c5 | -5.23868 | -44.91732 | 2024-11-16 04:50:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 82a7392d-adba-3061-adda-8ed6ea469eb5 | -3.76373 | -52.14901 | 2024-11-16 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c9e7fa45-46c7-3c82-92d2-dae3647a5beb | -5.11907 | -45.15709 | 2024-11-16 04:50:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d5e88fd-f840-3556-a3b0-11f7bd49803f | -4.56038 | -48.01035 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5676536-61e1-3191-8d56-cb769ea6bd1b | -4.22883 | -50.67377 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c09cf558-88be-3b70-b7e7-51688f2cea4a | -3.79826 | -52.10159 | 2024-11-16 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8bd236a4-49fd-3014-996a-09362f2bbf70 | -4.29996 | -50.14712 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b41f16c9-8da4-3f39-8f85-f176b4eb128b | -7.40054 | -40.3973 | 2024-11-16 04:50:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 69ffe1d1-5657-3c2e-817f-64527b7a5666 | -4.90375 | -44.03062 | 2024-11-16 04:50:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3fba000-91a5-34e5-98d6-a83639f719ca | -3.68854 | -50.11309 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 139b388a-befe-3f15-95e4-6826973f064a | -4.10337 | -46.88852 | 2024-11-16 04:50:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78a3c23c-e825-3c2a-ad72-30c8079b601d | -4.36018 | -45.86618 | 2024-11-16 04:50:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e12e275-a6f6-3d2d-8ef4-38ada767df88 | -4.90839 | -44.03397 | 2024-11-16 04:50:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba290a52-8933-3b1a-b56d-3e90574556b2 | -3.71629 | -51.84587 | 2024-11-16 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 729b7723-00e8-36d8-a18a-139b314580e5 | -4.37279 | -45.6307 | 2024-11-16 04:50:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd9b27c6-935c-3f50-b92c-6a1e302103b3 | -5.15558 | -44.09308 | 2024-11-16 04:50:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 09e29891-d7fa-3013-a7d7-8a770af99926 | -4.26917 | -48.54309 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 808bd69f-a2d4-351b-be84-9fe00bf9a887 | -4.25057 | -45.90356 | 2024-11-16 04:50:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebf8fda9-a3d2-3d33-903a-7a9da683fbd0 | -5.00422 | -44.31988 | 2024-11-16 04:50:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd381fb3-bf0f-3cbf-8d4b-c36e6c320a38 | -3.56807 | -50.25619 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cabbf98-8f89-31c3-bfc8-6e3bc22fac11 | -4.35889 | -45.87145 | 2024-11-16 04:50:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c91454da-86a5-30a3-b2b0-78772847f6c0 | -4.55967 | -48.01502 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 480a9de1-204e-3c13-98f0-444b2c8deedf | -4.90652 | -43.23215 | 2024-11-16 04:50:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cfb3336b-6e00-34a4-b448-e10eda2320eb | -3.81053 | -51.78667 | 2024-11-16 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 206118f2-82ac-3865-bc4b-a79c94b777ab | -3.55195 | -51.46426 | 2024-11-16 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ea6a274-11b2-3c10-bc30-15a0f4d4c788 | -4.30016 | -48.06609 | 2024-11-16 04:50:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 18bf98c9-e4f7-32be-811a-6aef2cc73917 | -3.99173 | -48.41999 | 2024-11-16 04:50:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5191bc4-25b5-393f-bcf2-bc82b70c278e | -5.00341 | -44.32536 | 2024-11-16 04:50:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5abb419c-461c-33a1-91d4-5a1705e509d2 | -4.10469 | -46.87739 | 2024-11-16 04:50:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3f756bc-dc3c-3081-ab16-17996e7f448b | -5.15564 | -44.08974 | 2024-11-16 04:50:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7fabfe95-153b-3cb0-86b4-f9c8f6a2b06f | -7.40025 | -40.38658 | 2024-11-16 04:50:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5a6e18ec-851a-355f-8067-dc734ef1c734 | -4.12691 | -50.42997 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bba657b1-9f3e-36be-834a-579447ef7fcb | -3.57898 | -50.52752 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 969373a0-b7bb-38aa-80de-9836499c0e75 | -3.6062 | -52.22295 | 2024-11-16 04:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c9a6485-a7db-3a5f-8991-a707e9ef8c52 | -4.13612 | -48.23014 | 2024-11-16 04:50:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02e55500-c85f-3128-8f17-e09874df95ce | -4.26547 | -48.54255 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9aca2475-c01b-3996-87ba-8f8afca2bdd5 | -3.98049 | -49.9471 | 2024-11-16 04:50:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e36d8793-af18-380f-96e3-e1ee0ab211d9 | -7.07089 | -46.75698 | 2024-11-16 04:50:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f9c3977-2619-376f-b395-2036c93d3526 | -5.15601 | -44.09018 | 2024-11-16 04:50:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 11a5793b-d2bf-3558-848b-d73d03e7da70 | -4.72596 | -48.11566 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a7fcb25-ee63-3474-8662-afd0775c9238 | -4.35892 | -45.87489 | 2024-11-16 04:50:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4cfec36-ffcd-3cd1-be8a-31c7f60e269d | -4.02714 | -49.19193 | 2024-11-16 04:50:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af1fe312-4963-3204-aba3-6264dee33cbf | -6.29954 | -39.48527 | 2024-11-16 04:50:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 11b04b5a-dfcc-38f6-b4d7-6b77fc627074 | -3.92773 | -52.25199 | 2024-11-16 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 14c03b44-4b96-3d8a-b152-852f71ea2b26 | -5.91117 | -46.22819 | 2024-11-16 04:50:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc0158bb-4291-3498-833f-287570488526 | -3.37167 | -52.71746 | 2024-11-16 04:50:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3e46f7c1-ba3a-30f2-a705-1e279b438c40 | -4.69822 | -50.35862 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fb5cca9-fc05-3342-932f-a4bc1d7b5ede | -4.27926 | -48.20383 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f52911f-babe-3fa8-a50a-0630249796d7 | -3.71299 | -51.84535 | 2024-11-16 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3b92a23-79bd-3941-8c50-8fcc388982c9 | -4.35955 | -45.86715 | 2024-11-16 04:50:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 820effd1-80ee-3a2e-a201-16f8842a9f10 | -7.43734 | -46.93678 | 2024-11-16 04:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 960ba616-aebf-38a5-95ab-a14a0a16718d | -3.24495 | -53.51841 | 2024-11-16 04:50:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9f8aa3da-d73c-3ad1-96af-b4e6cc58939d | -3.91222 | -49.04378 | 2024-11-16 04:50:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4cd30594-011a-36c9-9050-248d1b8740ba | -3.8563 | -51.81845 | 2024-11-16 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f656122d-7931-3ce8-bb42-63bf4a75889d | -3.50534 | -51.02293 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c67fe752-bb09-3d3e-823e-6c9dc4583b9a | -4.99929 | -44.31914 | 2024-11-16 04:50:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 460dc9c6-e627-3935-8924-198ac6a5ebaa | -3.58235 | -50.52803 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 53ef9f60-7dd1-3c0e-b3a1-fe3c27903081 | -4.90294 | -44.03621 | 2024-11-16 04:50:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dcf300b8-d9bd-3e1f-a7db-2f98b6b77bf5 | -3.60896 | -52.22691 | 2024-11-16 04:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c51066c-1494-334b-ab13-73e9f93557b8 | -7.39952 | -40.3923 | 2024-11-16 04:50:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5ab32daa-ccc2-3b1c-a49f-aa165a15bc3f | -5.71845 | -44.81075 | 2024-11-16 04:50:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c558b4b3-26ce-31f7-ad5c-36f609014e28 | -3.58461 | -50.53568 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a6908b2-1b9f-3b3b-8793-8ed0ed1ca27a | -3.57328 | -52.21389 | 2024-11-16 04:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b69e35c6-2f08-315f-be14-36e04e72e5d1 | -3.53581 | -51.58888 | 2024-11-16 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd69f649-f1a0-3ee1-bd1c-dcf2505bef0a | -4.90605 | -43.23544 | 2024-11-16 04:50:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6de069e-eb60-3a59-8359-7c853e97952a | -3.56469 | -50.23331 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c030fdfb-e8e1-3727-be51-80843c45ba9d | -7.39977 | -40.40298 | 2024-11-16 04:50:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 6.2 |
| bae1db3c-482a-33ce-bd67-63932a9a6a57 | -4.21146 | -50.69688 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c630efd5-5a6e-3330-a8e6-0b44b9075637 | -4.37346 | -45.62626 | 2024-11-16 04:50:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5546238d-2b37-3ea6-ace8-e5b3aa84ea3f | -3.24834 | -53.51895 | 2024-11-16 04:50:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4c8adfba-e09c-386f-a8cd-699a7bc1e195 | -4.27105 | -48.20726 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50425689-853b-3fa3-b72e-d0a91a5de836 | -4.53739 | -43.56131 | 2024-11-16 04:50:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e85062de-841d-3be4-ae96-b476d978e52c | -6.24515 | -47.27308 | 2024-11-16 04:50:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75aec93c-9318-3896-8277-c762bcc26b54 | -4.29637 | -48.06552 | 2024-11-16 04:50:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 728ace7b-02dd-34fc-953f-e6ad103f2b2e | -4.90922 | -44.02831 | 2024-11-16 04:50:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45abcde0-d9b7-3521-a914-8776d6a76ab6 | -4.37331 | -48.57034 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8f05fd6-9ca7-373f-a553-0126bded57f0 | -3.25477 | -53.67632 | 2024-11-16 04:50:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a85868ec-54db-3de4-a941-3ed6575ef649 | -3.56864 | -50.25255 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2bd0ecf-1989-33e9-887e-b880b6297ddc | -4.2322 | -50.67428 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4483dfd9-5207-3e83-a018-55fa4f245b88 | -4.22058 | -47.21388 | 2024-11-16 04:50:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c83b0d8-c1d8-38a8-ac94-ad153890738c | -4.37525 | -48.07982 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c289cf49-4596-3e12-ac3e-69bd131925ad | -10.66568 | -44.49949 | 2024-11-16 04:50:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d0b0a9e-1219-3f11-8766-37aa4cb2e6ae | -4.30324 | -48.07138 | 2024-11-16 04:50:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40128de7-fbd4-3529-890d-6a63108f487a | -4.22828 | -50.67736 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edb9f114-7396-3ad6-a91a-2ea6512347a9 | -3.51533 | -49.94306 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c6b1a2d3-7051-3e20-b1db-540922d53d10 | -4.28609 | -48.2095 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7d40846e-e228-3d36-bb45-6757d1797f45 | -7.39805 | -40.4037 | 2024-11-16 04:50:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| aee30e10-9a69-34e3-a54a-ddb77638a32f | -10.66514 | -44.49614 | 2024-11-16 04:50:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2b83c9c3-5580-39d8-a027-9ebc4526b638 | -6.02613 | -48.02885 | 2024-11-16 04:50:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b09b9bfd-6563-3961-baeb-56ad0b31950a | -4.8173 | -42.91681 | 2024-11-16 04:50:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README50.md)
