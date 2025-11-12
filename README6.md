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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a970c8c-7078-3aa6-bbd1-66c1a37334cd | -4.9643 | -43.7182 | 2025-11-12 03:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| f19058ae-f401-313c-9679-8b90ea2e9f3f | -4.1161 | -48.0136 | 2025-11-12 03:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 5e35883b-238c-3eed-b5af-5d2fa59f589f | -4.116 | -48.0352 | 2025-11-12 03:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 88c535d2-ac0b-3d85-a5c8-488b9d4772c1 | -4.9641 | -43.7413 | 2025-11-12 03:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 1d91218e-82d2-366d-ba54-8f141ae4b476 | -4.9456 | -43.7194 | 2025-11-12 03:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 2aea1b3d-c05d-32ce-bcf4-f704f62b4e99 | -4.1161 | -48.0136 | 2025-11-12 03:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 5b1e1027-2008-3d8d-b010-ebe29b3dc6db | -4.0976 | -48.0144 | 2025-11-12 03:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 3448fd7c-1699-3825-9d60-61cecba50a36 | -4.0977 | -47.9927 | 2025-11-12 03:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 3a3347eb-0fc6-37a0-a60c-247ee185668e | -10.5076 | -44.944 | 2025-11-12 03:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| b6836da5-397c-3825-85e6-102163863fe4 | -4.9454 | -43.7425 | 2025-11-12 03:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 1b92605e-e6c3-3f9f-a84a-3360f6d72592 | -4.1161 | -48.0136 | 2025-11-12 03:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 7e9ded47-9b7a-3335-8e11-d3546e629ceb | -4.9456 | -43.7194 | 2025-11-12 03:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| a87f1558-1379-35cc-87ab-ac0bdfb65f49 | -4.9643 | -43.7182 | 2025-11-12 03:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 19f73455-676b-3417-946f-d1dca075d0a4 | -4.9641 | -43.7413 | 2025-11-12 03:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 5117d368-50ef-341e-876a-5c083ca56219 | -4.0974 | -48.0361 | 2025-11-12 03:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 607d02bc-1cd3-31bf-9c2c-5f5517ef81fd | -4.0976 | -48.0144 | 2025-11-12 03:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 120.1 |
| b9e5f876-3cfe-3989-a1ee-52903df828f2 | -4.9643 | -43.7182 | 2025-11-12 03:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 4f68fd15-f89d-3309-ba5f-79b9c325754a | -4.9456 | -43.7194 | 2025-11-12 03:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 0af241eb-1f3a-33ae-82cb-0bc14e596fa0 | -4.0974 | -48.0361 | 2025-11-12 03:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 236eba1b-c816-3add-9d2a-a6e486808a78 | -4.1161 | -48.0136 | 2025-11-12 03:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 45edf211-6787-36b3-9537-90f996028b13 | -4.0976 | -48.0144 | 2025-11-12 03:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 6d3b4008-4b01-3a70-83d8-f50c645ce4ec | -3.26025 | -41.40614 | 2025-11-12 03:40:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9bbbeff0-35a7-3dba-8154-7ba8bb362c34 | -3.12622 | -45.25082 | 2025-11-12 03:40:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5abbc20b-ac67-31c0-a7d4-e5c855b23ccb | -3.59693 | -43.42686 | 2025-11-12 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f46a785-d13a-3a0a-b67f-51d50941a760 | -3.25936 | -44.67305 | 2025-11-12 03:40:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3e422100-3efe-36ed-9680-4193d7e04747 | -3.44989 | -39.36311 | 2025-11-12 03:40:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| fe782b35-c660-3c46-931b-a2017055561b | -2.94959 | -45.55383 | 2025-11-12 03:40:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0e8ea7bf-117d-30e1-802e-9e55578b7378 | -3.97104 | -40.96339 | 2025-11-12 03:40:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9ac8014d-23d8-337a-b46f-e8e23be5a0b7 | -3.25964 | -41.40887 | 2025-11-12 03:40:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e7fbaee9-b7a4-34c9-930a-351de5ad7616 | -3.35437 | -42.15792 | 2025-11-12 03:40:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 1c3ffc3b-ee8d-344b-985a-2589e1714b59 | -3.25854 | -44.67023 | 2025-11-12 03:40:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51966dda-b89a-35d6-8730-f18c8596d23b | -3.26503 | -41.40488 | 2025-11-12 03:40:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6f47aa18-a370-3058-8310-d57090190037 | -3.86787 | -40.98898 | 2025-11-12 03:40:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 17c579ae-c01a-3245-8aca-da27e3f7281d | -2.94349 | -45.55285 | 2025-11-12 03:40:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9091c15b-ef0f-3c19-b1b5-7de4cd0ae812 | -3.35483 | -42.1612 | 2025-11-12 03:40:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 62a4c3de-6731-371f-8a2d-9fdcd9b012c7 | -4.33614 | -38.36594 | 2025-11-12 03:40:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 29ed5832-a099-32e7-835d-43749fe30a8d | -3.05304 | -40.81152 | 2025-11-12 03:40:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| abea5e24-c3e2-3b9b-a4fe-4957629b3cbf | -3.13217 | -45.25187 | 2025-11-12 03:40:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28615fc7-6c34-37d3-b0ef-53f25bb2dcce | -2.94881 | -45.55845 | 2025-11-12 03:40:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7dd331f4-5121-3952-8027-b14d7a16cc29 | -3.25868 | -44.67701 | 2025-11-12 03:40:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 51085056-afbd-3ed1-b82c-94c5fd528a73 | -3.26484 | -41.40686 | 2025-11-12 03:40:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 61e36d37-8a70-34de-a028-d6fe4c834c91 | -3.26423 | -41.4096 | 2025-11-12 03:40:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d53ed7ba-33e9-3427-9e61-d72ab1fc59b0 | -3.34914 | -42.16569 | 2025-11-12 03:40:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 13147e5a-24be-3c55-a864-6dd3f83b6573 | -3.79244 | -40.56581 | 2025-11-12 03:40:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a78142d3-e53b-3147-ad79-61f13b3ae47b | -3.05232 | -40.81585 | 2025-11-12 03:40:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a9f9304b-497a-3c1c-8dcd-4cfa33860072 | -3.86761 | -40.98698 | 2025-11-12 03:40:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| af00908c-20bc-39fd-b49c-570ddb1d7371 | -3.43046 | -42.46538 | 2025-11-12 03:40:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5d61dac1-2456-35c8-8a2a-3960f343dbd2 | -3.35 | -42.16039 | 2025-11-12 03:40:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6f0f1564-a7fc-3bb7-9f31-9d866c03b96e | -3.25723 | -44.67818 | 2025-11-12 03:40:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3ca5d388-3b5b-3ffb-9eee-7547653a8849 | -3.45044 | -39.35967 | 2025-11-12 03:40:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ea154e28-dab1-3855-85e4-aa09df3a645f | -3.25789 | -44.67421 | 2025-11-12 03:40:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3a5c4a01-3631-3ca0-863d-544d92145f62 | -3.59638 | -43.43007 | 2025-11-12 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ed3d202-3fb1-3e9d-9b0c-54f9b7f138cf | -3.35347 | -42.16322 | 2025-11-12 03:40:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 184c086b-474b-3852-9316-d083c30e7d8e | -3.00465 | -45.15422 | 2025-11-12 03:40:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2d7154fd-468b-3d35-bb39-667fd76bc9fb | -3.26296 | -44.67918 | 2025-11-12 03:40:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 111222fc-8bf6-30cc-989e-04a55352c2cf | -4.7576 | -42.66967 | 2025-11-12 03:42:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 413a7996-8c55-389b-b560-dabe41177261 | -7.29693 | -45.07332 | 2025-11-12 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7f90b0b-fe80-39f7-83fe-0e7befbf2087 | -4.93775 | -44.2962 | 2025-11-12 03:42:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5548f197-17f3-3bc4-b0e9-f42da2909926 | -7.13207 | -41.86853 | 2025-11-12 03:42:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a9651bb1-fee0-33a3-91b0-40ab4ed47c9e | -3.96272 | -43.77761 | 2025-11-12 03:42:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c4c38c5-1b7c-3eb9-a529-437c332dbdd1 | -4.94881 | -43.74853 | 2025-11-12 03:42:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e1a599e-682e-3637-acf4-db00b307c5ff | -7.24956 | -41.63207 | 2025-11-12 03:42:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e3348a93-40e3-3be2-b73b-70a308657bb5 | -7.09356 | -40.45032 | 2025-11-12 03:42:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 78b89c1d-eb62-36c9-9ef1-27d3292d819a | -6.51933 | -35.21161 | 2025-11-12 03:42:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 42.8 |
| b2ba5d4b-abe7-3c84-9b52-ec71243dc5aa | -8.92535 | -35.40185 | 2025-11-12 03:42:00 | NOAA-20 | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f70e3f17-a124-31e4-a6c1-cd4a1a5518c9 | -3.71512 | -45.83034 | 2025-11-12 03:42:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cac8b1e4-0c81-3da5-9c39-a220d3573105 | -5.49196 | -39.17045 | 2025-11-12 03:42:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a6f2f1f7-2b07-3081-b6e3-6a04652c49c7 | -3.70902 | -45.82919 | 2025-11-12 03:42:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15658983-4f67-3d5b-adc5-9a67fe32c21f | -10.42115 | -36.85327 | 2025-11-12 03:42:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a419dfac-0916-3f0b-9617-1ab78456b74e | -6.43934 | -43.48899 | 2025-11-12 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc6269fb-81f7-342c-940f-c70633116738 | -6.61101 | -42.07406 | 2025-11-12 03:42:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4a6a43a6-05c8-3670-bc66-37e0a7acb923 | -6.54436 | -43.04187 | 2025-11-12 03:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1cd1b7db-0b47-3024-9cc6-392eb0e9dd0a | -7.13687 | -41.25743 | 2025-11-12 03:42:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8fedcf8d-1d50-310b-a3cd-900166e92926 | -8.31292 | -43.64224 | 2025-11-12 03:42:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6d01798f-88cd-3386-a69a-de09c4a69cb8 | -3.70981 | -45.82446 | 2025-11-12 03:42:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34652083-6020-3f7e-94e9-6dd969ba2ebb | -8.00494 | -43.35268 | 2025-11-12 03:42:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 227f4aed-ffeb-3f13-855c-a3cc05d7ce91 | -4.29687 | -40.05344 | 2025-11-12 03:42:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d620512c-2211-3aa8-8121-dc65e426f6f0 | -4.93421 | -44.29285 | 2025-11-12 03:42:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b90603b2-3313-3baf-813d-db2fafc67ec4 | -4.91233 | -44.32154 | 2025-11-12 03:42:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bad944cb-eebb-3243-8034-1bf7079d83c9 | -5.49118 | -39.17514 | 2025-11-12 03:42:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 55c781ac-38f1-3b04-9453-f4425b15421d | -6.67996 | -35.07809 | 2025-11-12 03:42:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2572f1f9-6df7-3a7a-8473-9604bf8514cd | -6.99293 | -42.78699 | 2025-11-12 03:42:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4cbe8b63-8b8d-3b9c-b8ec-b7f1f4319aed | -3.70942 | -45.82631 | 2025-11-12 03:42:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9b5303ee-c924-3d47-9734-1d5cba0653c1 | -7.28004 | -41.58545 | 2025-11-12 03:42:00 | NOAA-20 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 1686dcbc-20e4-3d71-bc1e-1f892d0f28c2 | -10.25722 | -36.68904 | 2025-11-12 03:42:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 43b929d5-b359-3520-964d-5f63e69d7e24 | -7.60009 | -38.84953 | 2025-11-12 03:42:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 27426c7d-1fd9-3f87-a755-e216c44fbafc | -5.64809 | -45.99293 | 2025-11-12 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a84ff6c3-b48f-3c9f-8117-13a0a308fbee | -7.28076 | -41.58126 | 2025-11-12 03:42:00 | NOAA-20 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 0823ef4a-67d1-3e67-a842-7c737d474196 | -6.51218 | -35.21402 | 2025-11-12 03:42:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6745e933-4f9f-3def-8d34-76a3591d4699 | -6.47648 | -43.53852 | 2025-11-12 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32dfba58-b14f-3af0-ba37-14674bb22eb8 | -8.34912 | -40.97636 | 2025-11-12 03:42:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ce6cdccc-2b76-303f-ad56-48e4c78c259a | -10.2611 | -36.68607 | 2025-11-12 03:42:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2c6de0df-e1d0-39cd-a9d3-f0c83857565d | -4.77762 | -46.4513 | 2025-11-12 03:42:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6229d6f-033f-364a-b7c6-43e806fd1c8e | -5.30925 | -40.85115 | 2025-11-12 03:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 517be2a1-e206-33b0-842d-93b2d9018c25 | -4.14528 | -47.66068 | 2025-11-12 03:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 296e2abe-3e5e-34ff-b751-2e98b0240c0e | -5.33017 | -35.55416 | 2025-11-12 03:42:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1d43d94e-d14d-3088-8bac-3190ffc5f610 | -6.61154 | -42.07588 | 2025-11-12 03:42:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5f5b5528-b544-31c8-8c97-33672dcb3880 | -7.59935 | -38.85394 | 2025-11-12 03:42:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dc2bcf35-35ee-31b0-9996-72e963451f59 | -4.31264 | -43.05524 | 2025-11-12 03:42:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ca63034-d73d-3f31-8617-c19ae48b6a5c | -6.41005 | -42.28753 | 2025-11-12 03:42:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |


[Clique aqui para ver as próximas entradas](README7.md)
