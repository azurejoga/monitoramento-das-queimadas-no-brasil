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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80debb15-be2d-329e-ba74-f88d85d47529 | -5.12842 | -55.97186 | 2025-11-15 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7aa5b251-08d1-3f15-b4f7-9291443b3426 | -2.95594 | -48.58993 | 2025-11-15 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 498c1c1f-0a3b-3c4a-9236-b1361a2f07d5 | -3.99046 | -48.00052 | 2025-11-15 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99249d38-0d77-34b1-a782-7c0e0fb863fa | -4.17705 | -50.42665 | 2025-11-15 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ad62d1a-b28a-3b15-a756-e9a0f521bdec | -4.76068 | -50.683 | 2025-11-15 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4877f470-f433-3809-bc8a-88e0f3c72613 | -4.40151 | -50.43338 | 2025-11-15 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4062070a-b131-3d39-85db-8e7dd127230e | -3.21254 | -50.19133 | 2025-11-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c1d110d9-de14-3c3a-b0c5-593d8809626d | -4.73268 | -47.1623 | 2025-11-15 05:16:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 2b7fa5a7-b07e-39b2-af61-01e7bd386c67 | -3.45923 | -50.11641 | 2025-11-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0c3e7218-18fb-3628-8671-3a44dfa86b83 | -7.52463 | -47.19352 | 2025-11-15 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5d42b9c-c480-3765-b1a0-6127e8123c5a | -7.71334 | -49.38423 | 2025-11-15 05:16:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d0ed922-1560-313a-a8b7-6b2aba5bae43 | -6.03277 | -52.42076 | 2025-11-15 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adbe1984-5e26-3ea5-84f8-9915d2e42f35 | -3.59651 | -54.67847 | 2025-11-15 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adbb0511-4268-303f-b0d9-31f0a4943319 | -7.7073 | -49.38714 | 2025-11-15 05:16:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7484eed-dbd8-3e08-8d5e-7a9595b94057 | -3.85895 | -49.12374 | 2025-11-15 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21435820-b536-3d78-a2df-f437250dc535 | -2.79233 | -52.97361 | 2025-11-15 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c300a23-ce78-31e9-a008-2be243033221 | -3.15098 | -45.39065 | 2025-11-15 05:16:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 14a0aa5c-0932-3468-a6f6-f8b4143f2641 | -4.72657 | -47.1611 | 2025-11-15 05:16:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1d9c0829-89be-3aaf-95bc-1eda94369618 | -8.32579 | -45.40967 | 2025-11-15 05:16:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 19737047-3481-35ea-9c77-44497a52c276 | -3.5325 | -50.87851 | 2025-11-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e2fa80d-4513-34ab-a858-122a5e3ffcc9 | -3.57573 | -49.54404 | 2025-11-15 05:16:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7f7d45b-e473-3ecd-aa1e-efa1ceff9342 | -4.72723 | -47.15647 | 2025-11-15 05:16:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 898bcab8-8ab9-3a1a-bbde-83865a8acbe5 | -4.41678 | -50.82743 | 2025-11-15 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b382a986-e330-339f-8e90-a8b3fbf08772 | -6.16209 | -48.049 | 2025-11-15 05:16:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d593fc5e-ba42-32a9-9cad-fe0744fa002e | -3.08324 | -52.92256 | 2025-11-15 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b03361d-9094-3124-8961-379093ad5986 | -5.57383 | -47.09927 | 2025-11-15 05:16:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7df1ebba-db6e-3f74-8e67-3a44af7e6e39 | -7.53031 | -47.19954 | 2025-11-15 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 919b79dc-9b26-3150-94f4-cffdb90a679b | -9.13019 | -47.11925 | 2025-11-15 05:16:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f9ea800-5484-3aa2-a91a-51247245b9cc | -7.53212 | -47.20252 | 2025-11-15 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8e5ecff4-8846-3734-8f8e-2a987ce362ea | -5.12491 | -55.97132 | 2025-11-15 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3effbaa1-ae71-312e-9cb6-cf7129a460e0 | -3.73475 | -52.43564 | 2025-11-15 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 803951f3-5672-3457-a758-c84cb73cde7f | -8.63083 | -54.9417 | 2025-11-15 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fabbb20-bf2c-3b84-a220-34ddbf8322fa | -3.16839 | -45.2211 | 2025-11-15 05:16:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e112795d-ab81-3996-9a44-5f9117ab1826 | -4.10783 | -50.06281 | 2025-11-15 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8881635a-4d69-3c93-ad73-13f3e4cc66aa | -6.16272 | -48.04446 | 2025-11-15 05:16:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5510b471-7ff3-34ba-bf49-f8e1b776cc7b | -3.86251 | -49.12359 | 2025-11-15 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59d2f8b4-48c5-33bd-8591-0acafd2d9d48 | -1.70476 | -54.21645 | 2025-11-15 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98bb23d7-e564-3763-83e3-8812ce56a7de | -4.35395 | -46.48933 | 2025-11-15 05:16:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 74bc96a0-4334-38ac-b4f0-bd5a9049e125 | -3.70041 | -51.62582 | 2025-11-15 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cde699f3-8c2d-3286-a6c0-99aef44f020e | -3.41546 | -49.9949 | 2025-11-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c47423fa-9d14-3d52-bfb7-412441bcdb88 | -3.69413 | -54.62494 | 2025-11-15 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fffd28a0-af02-3933-a029-aefd8d582b92 | -8.74677 | -48.31518 | 2025-11-15 05:16:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 721b4e8e-0a3f-325f-a98a-03fb6d539ed1 | -10.1062 | -47.51847 | 2025-11-15 05:16:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8153192b-2fb5-3f66-940b-14dae03bc9b3 | -3.38417 | -50.16748 | 2025-11-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 314bd7eb-0306-39f7-9ca9-4ed94b876faf | -3.30188 | -50.10912 | 2025-11-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| edbcf6d3-6683-3e62-a1f7-c3b8317e33d5 | -2.68784 | -49.8575 | 2025-11-15 05:16:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1025081c-0c46-3aad-a82c-62a5a975b32f | -3.6736 | -52.14769 | 2025-11-15 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79a1608f-f666-3251-99e3-2a372f8fcc9e | -2.29838 | -55.74862 | 2025-11-15 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e16754ab-0318-3476-8511-9c785d4d0ab7 | -3.86224 | -49.13818 | 2025-11-15 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4288bdc-70af-3d37-b396-fae4eb3bb6b5 | -9.10152 | -47.78235 | 2025-11-15 05:16:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a6f9def-03f6-39dc-91e8-c451dacb0906 | -2.7974 | -52.96742 | 2025-11-15 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d72f5b4-66dc-3ecb-9a6f-1539d412af78 | -3.1486 | -45.38534 | 2025-11-15 05:16:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| daf4c65b-ca69-3c58-a329-b9b1083249e8 | -2.85819 | -53.00873 | 2025-11-15 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59e80afc-5a15-355e-a802-2477f4927ba7 | -3.39047 | -51.51429 | 2025-11-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e54d1ce9-19d7-3bcc-9291-344eb795f52f | -2.88347 | -51.43155 | 2025-11-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0929d53b-e4da-3f40-95ce-7cea1cf65702 | -2.80142 | -52.96809 | 2025-11-15 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a701a2d0-27fd-37bd-a473-54ccb0c64c39 | -6.16063 | -48.04314 | 2025-11-15 05:16:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0b956b30-4c66-32d0-84ab-54bbc5570c56 | -3.6045 | -54.67535 | 2025-11-15 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7bdd85ef-f861-3793-9236-f9b17198f87e | -1.71347 | -54.38018 | 2025-11-15 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| edcd5429-5f2e-3dc5-a64a-62be0c0f8b41 | -3.26277 | -50.09115 | 2025-11-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e33fe365-d479-32a8-8a1c-2f6f40cdeec3 | -6.15411 | -48.04675 | 2025-11-15 05:16:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e0c8691e-7b5b-3a79-8312-ff122447f0fe | -3.22363 | -45.4821 | 2025-11-15 05:16:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cfe73102-261a-3494-8cde-8e1b235d0e61 | -4.35601 | -46.49129 | 2025-11-15 05:16:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ad1d08d1-9e56-3d5f-a90f-064d6ee7ea74 | -3.86106 | -49.13383 | 2025-11-15 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 832b0236-2091-3234-8832-2b2a85f88c68 | -2.86861 | -51.47037 | 2025-11-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd77010b-39da-33b0-8ded-19a70a7b9729 | -3.73547 | -49.04733 | 2025-11-15 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ed23aba-a006-3d1e-b654-ea9712f782a2 | -3.75562 | -50.43016 | 2025-11-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e463a2c5-1a64-3300-9260-9f1275b0c182 | -3.52594 | -56.31699 | 2025-11-15 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60f40b7c-f76f-31b6-851f-0c60bc7d2dd0 | -4.17787 | -50.42107 | 2025-11-15 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe3fd5b6-8828-3c7d-81bf-30e92edd99f9 | -3.52877 | -56.32124 | 2025-11-15 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d8205f1-24b3-30c7-869b-a240f8153499 | -3.28237 | -51.545 | 2025-11-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f7449010-63e9-3a25-a233-f5b167c4f2de | -1.83721 | -53.80215 | 2025-11-15 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d32b6de7-b991-3306-995f-d8fd17b07d8b | -6.15681 | -48.04355 | 2025-11-15 05:16:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 070315f0-7178-3e1c-83f3-800395d4093c | -3.38596 | -50.1679 | 2025-11-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f97bc1c0-a672-3f73-bfcf-59349c5fb3ef | -2.68121 | -49.86468 | 2025-11-15 05:16:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6750f7e6-0072-34db-a7ab-88795a843c92 | -6.16869 | -48.04498 | 2025-11-15 05:16:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e28e3782-bcb6-3182-b089-f853d54a7d32 | -3.37941 | -50.13214 | 2025-11-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 560f0692-a250-32ea-b46a-5c252c527ba6 | -3.45839 | -50.12208 | 2025-11-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a7f2e00c-0ed9-3f7b-91e8-28b74e2d4e80 | -9.82671 | -49.7729 | 2025-11-15 05:16:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dd378e56-4dca-3b19-a68c-61663694e60e | -7.52395 | -47.19865 | 2025-11-15 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35987026-45ed-31ec-921d-ed4d82be0b27 | -3.15301 | -50.27005 | 2025-11-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6040f68f-d4b3-3b08-abbf-a5caf310402e | -6.15617 | -48.04807 | 2025-11-15 05:16:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| dcfb22e7-dcf5-30f7-8d66-c3275a488ece | -4.35823 | -50.79167 | 2025-11-15 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 825d96b4-9473-3342-a228-5843898b43da | -4.00886 | -48.80777 | 2025-11-15 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be8ec8e0-db9a-365e-a61b-a38d4b775c5c | -7.5264 | -47.19643 | 2025-11-15 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d30ee6e0-c54e-3910-864f-5e72951921b3 | -2.69326 | -49.85538 | 2025-11-15 05:16:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfad309b-29d8-3db7-b24c-4ad998b937f5 | -3.17389 | -45.21702 | 2025-11-15 05:16:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 689a1741-d727-35c9-848b-4014527f82f0 | -2.79636 | -52.97428 | 2025-11-15 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d71b4dc-9df6-3584-b6a7-1bed9a265e8b | -4.11327 | -50.06075 | 2025-11-15 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92129c50-cc6b-3dcf-8d66-3ad99d02dea7 | -3.42148 | -51.507 | 2025-11-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e822cbfd-f8b6-3d55-b606-2f005b1e1378 | -4.01433 | -48.80859 | 2025-11-15 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79a715fe-10e4-39ac-b5fb-85c5fff15602 | -8.32664 | -45.40303 | 2025-11-15 05:16:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 064dd11e-260c-3d5a-a585-7b2866618320 | -5.58579 | -47.1049 | 2025-11-15 05:16:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9bae976a-2ee3-3c8d-abe5-aac6d91dabef | -2.01716 | -53.00115 | 2025-11-15 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da8a8fd4-f25f-3850-8b81-d1f8608a05e9 | -6.16804 | -48.04965 | 2025-11-15 05:16:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bc9b86c6-9029-3d1d-b33d-8f01ec6f07d4 | -4.27047 | -46.84417 | 2025-11-15 05:16:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee93a28b-d76f-31c2-a0e5-a5279bc6c13f | -2.9515 | -45.15912 | 2025-11-15 05:16:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 9e27f3db-9ca2-3902-b706-f26755b009f8 | -4.10825 | -50.05991 | 2025-11-15 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d77ee69f-a3ea-3862-93ea-807f9ae99ca7 | -4.72508 | -48.56364 | 2025-11-15 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a09d8a39-32b0-3046-950c-f689256a6e0a | -2.30323 | -53.52151 | 2025-11-15 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README52.md)
