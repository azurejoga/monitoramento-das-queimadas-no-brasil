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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c221c6a5-969e-323e-a177-56ad10e75db2 | -2.96313 | -51.27515 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e91de5a-3b00-376a-b1af-f47ae1c984c4 | -3.41379 | -50.30309 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f854ebb-1bdf-3f03-aa4a-b133a09f1f6c | -2.16039 | -50.5063 | 2024-11-06 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5de023dd-b990-3aa6-bbce-7c834cf3c0d5 | -3.66292 | -50.23503 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cce768c7-d5f7-319c-a7ac-ee3f062501a3 | -3.15281 | -51.14945 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4bf527c5-b06a-31ba-a79c-6ad5351f7123 | -4.28494 | -48.64263 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e248fd5-dda5-333c-bb22-ccc9fccfde62 | -3.71629 | -49.42786 | 2024-11-06 04:36:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 19f06eb6-b884-3f0b-8aca-4bf4827c6794 | -3.00877 | -53.23243 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fabdf4cb-cf31-329a-b15a-b3287206f5b5 | -3.71279 | -53.75338 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e41178e1-4755-32a7-8990-1c453d0114af | -2.85186 | -51.77392 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| c3d1c9fd-fa89-3fce-b12f-d4e04a867416 | -2.82544 | -49.77719 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 72485f74-71e8-325f-87bd-109df8d125d1 | -3.0267 | -53.27076 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 1a494ca0-881c-3090-a609-c50d0ead7400 | -2.34848 | -48.92305 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cf37eca-74ef-37c0-b397-d908475c40b7 | -1.52589 | -52.22669 | 2024-11-06 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7333e60f-dacc-3b4f-8ec6-135886266fb0 | -3.12698 | -51.10981 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3b7a980c-75f9-3239-94e1-40ec490f9b3b | -2.05577 | -53.40751 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df72d383-381e-3d86-abcb-5c8df7f3a6a3 | -2.82297 | -52.93932 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4a513da0-a3eb-38d1-918f-e83c5db802f1 | -2.42338 | -49.867 | 2024-11-06 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a27fb79-04be-3d6e-bfc8-68d3ad4c5378 | -3.23822 | -53.40271 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 708cebad-70a6-3557-910a-c2d77516108e | -3.63517 | -52.33542 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0cee7ab9-17aa-3cc6-a82a-8db1564f0097 | -3.24551 | -50.01674 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4703a145-4eba-34bb-8478-f770e340ab36 | -2.3725 | -46.74833 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fe8f6d8-2bd6-31ec-bacd-10155bb7aee6 | -2.82145 | -52.9488 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| d9b272f4-e1f9-378f-a859-a49c38fe6a0f | -4.17225 | -45.62995 | 2024-11-06 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48fef69b-5892-398b-87d0-5328a28780f9 | -3.16326 | -50.59564 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37b7a9d0-6973-325c-815f-f6c8f69e339c | -3.10589 | -51.13018 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6aa91da5-3d36-38c6-88ca-6747ca953402 | -3.02072 | -50.45398 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1bcfb06-6221-34f5-8165-8b9750c5d2bc | -2.91261 | -51.04619 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 087897a9-a4e8-305c-9462-90c4652184a6 | -2.90319 | -51.46985 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 423fcc6f-18cd-35f0-ba85-9022a38bd31c | -3.17067 | -49.54844 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22cddeb9-394c-3724-a524-d31dce6900ce | -1.28769 | -54.56958 | 2024-11-06 04:36:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 500b0755-e95b-3051-a4df-44d6ddffa0ee | -3.10202 | -50.29835 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3978e73a-3514-3ef6-beb4-45b4658f55f4 | -2.58946 | -46.18665 | 2024-11-06 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b67fbd01-67f5-3e5c-8ae5-78692acdc7a6 | -4.10548 | -48.50837 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e55a72e-0f2e-3632-8303-e06ef8c469ba | -3.01563 | -53.43555 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| c5e28bf8-6bf3-38e3-9e45-5392f944d205 | -3.05931 | -52.50158 | 2024-11-06 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b4f1387e-d0b3-3c83-8381-ccdf6098e031 | -3.02982 | -48.11057 | 2024-11-06 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77168700-3d8a-3e4f-8cab-cb1daa16ca81 | -2.38922 | -50.3228 | 2024-11-06 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c6d69bb-4f2f-3770-81dd-50e198aa4445 | -2.92651 | -51.0484 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c412db2d-0a62-3fe9-8f63-1c66d3c61923 | -2.66653 | -48.64951 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc5409cf-68db-3177-af7f-4eb95a1a7402 | -2.9386 | -51.0621 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 95c7da82-412a-3ef8-acf2-7394c4e9f878 | -2.91893 | -49.11826 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33494fb9-2ef2-3edd-963d-045a74495063 | -2.51861 | -49.13712 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 41449293-11f3-3254-b96a-9a4514f04072 | -3.29429 | -51.04519 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2370ebb4-2d7b-300e-bf5f-9da822f221e6 | -2.90525 | -49.39978 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b8ea1f4-b1ee-3708-93e7-3fe385a0c664 | -2.61424 | -49.1981 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d91264ed-3f2e-37cc-8f36-c847c8db64eb | -3.24215 | -53.40662 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6cfa5574-3f9e-3587-ae3c-ef84a8981983 | -0.13851 | -51.38958 | 2024-11-06 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4d5a324-075c-3f4e-a3d7-1e93e1aa982f | -3.23196 | -53.39457 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb403db9-ec8e-3bfb-830b-1df7615d75c3 | -3.10104 | -50.26122 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24873c42-b2fb-350c-ac38-aca5dbcf1583 | -3.10598 | -50.29526 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f755efe-b579-3839-904b-7e9e0cca4351 | -3.52311 | -51.66734 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3acb9a39-0402-3250-b557-eabbafd1617a | -2.81678 | -48.55701 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8aa84f7d-476a-3b73-9d63-0d1918d83183 | -2.86852 | -51.39096 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b526ddb-0250-3b93-8486-530f90d6e8fc | -3.03402 | -54.21126 | 2024-11-06 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3259e35-051e-3f33-8b53-2643e1d40c73 | -2.2705 | -49.20085 | 2024-11-06 04:36:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3a4a5ba-6580-3de4-a57a-34efea66a299 | -3.68828 | -51.36486 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5eb1aa21-4b68-3a01-9d3a-ee8da9c6bac4 | -3.52988 | -50.3432 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 629e094a-dbce-33c4-9ea2-9eae2058d01a | -3.2955 | -51.04571 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 478857ab-90ec-30a6-aaf9-9379e99a4a8a | -2.74636 | -48.7253 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f344fcbc-49a8-3fd3-b1b2-efb664f0151d | -3.03818 | -54.21193 | 2024-11-06 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1623e372-c198-3590-a7a2-48514c17fd73 | -2.39953 | -47.8179 | 2024-11-06 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59a9a156-7d7d-3ed9-a448-cf1aa5ca81f6 | -4.44237 | -50.97554 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a745e6ef-f05e-3c1a-88e9-26230866dfd6 | -3.83357 | -46.49841 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a209443-ce38-33a0-9e55-6b1db408e5ac | -4.77468 | -48.68425 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b1ac07bf-914d-3e05-a9ce-59a04afdc6c3 | -2.61096 | -51.30308 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3bb7a821-14d6-3e8d-ac36-75c70d30c46d | -2.92243 | -51.05167 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3a0d5b15-901b-39c0-b219-96ab4e237a2c | -3.17972 | -50.602 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d9ca5969-d22e-325d-9588-8dae5026c830 | -3.98021 | -48.15923 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10037030-06d6-3079-9066-78fff000d319 | -4.05729 | -48.25295 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b29b9ba-2ae2-3213-9e96-a7d6294b4b34 | -3.58349 | -50.267 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f00fbfb-46c2-3304-90ae-f28a77147239 | -4.3453 | -48.62773 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5c1a0df-991d-3c38-991c-5bd7dc26226e | -2.912 | -51.05002 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 206fe9b7-b65f-3820-a5df-7fad9a035dcd | -3.20268 | -53.22705 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 1ef89d83-20e1-34fd-ae7a-ecf08fc3e71e | -4.07056 | -53.94373 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 4036ed6a-e7ec-31b9-91b9-020b4fc72edf | -3.50978 | -46.109 | 2024-11-06 04:36:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94266909-3093-348f-992d-ed84f48ce536 | -3.20348 | -53.22208 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 50f9d3ec-1221-3b3d-8385-61e11bbd7f57 | -3.52478 | -50.35348 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5cd3f72-1193-3805-ab0d-1d85c0e50184 | -2.88469 | -48.62363 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbaa0f44-9e70-324d-8c96-b48ceee1820b | -2.40512 | -50.31033 | 2024-11-06 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1f8f2d6-db58-3f23-9639-fed13b19e748 | -4.13704 | -43.58419 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 3a42aab1-44e5-3076-9522-2c02150a0ed5 | -3.03217 | -53.26154 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f97a65b8-4292-3b6b-a396-fdb91914613f | -3.65845 | -51.9344 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed137aa7-588d-31df-a66b-de434947cb15 | -5.08361 | -47.79261 | 2024-11-06 04:36:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 634b32a0-f10f-3da9-857b-e66957c885c3 | -2.969 | -53.86858 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f1ec5b59-c32d-3fab-a1d5-e8ab72daba48 | -3.19878 | -53.22646 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8cf94bee-8e2d-3ff0-9b85-2aa96befd6f4 | -2.93354 | -52.53866 | 2024-11-06 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 64c0d36a-2e69-3188-8b95-2b262a30135a | -3.55764 | -47.3798 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53e74883-0eeb-3950-b53d-753da18c5a54 | -3.09659 | -50.24576 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b7c57adb-9357-340c-96cb-9e5ce04b1370 | -4.1931 | -51.02036 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4eb461e5-38bb-3ca5-a5c4-f9ae3a8e4ecb | -4.68525 | -46.3952 | 2024-11-06 04:36:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e387f717-775c-3b22-af2e-570643cce2d8 | -6.3244 | -39.51653 | 2024-11-06 04:36:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aea6d4c8-7c38-3ae8-8fbf-9201bf439be8 | -5.0685 | -44.22814 | 2024-11-06 04:36:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fa5fb9b-56b5-38ed-9413-b4ea35020897 | -3.5242 | -50.35709 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d81effdd-f326-3fcd-a641-6b2386933c42 | -5.37095 | -46.42788 | 2024-11-06 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c41d02e1-7117-3901-a432-c7febcd99120 | -2.95659 | -51.06102 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f355ee79-12ce-3613-9d9e-a6442506d65c | -3.87127 | -52.38212 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35460a70-d9d9-339a-90b5-47501d7103e6 | -2.34512 | -48.9014 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20a78a16-8386-3136-8681-e5bfd2f49f19 | -3.96688 | -48.15742 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d3d8dcf9-d374-3b94-a59a-3bfb3bb6cd16 | -3.15518 | -50.20347 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |


[Clique aqui para ver as próximas entradas](README44.md)
