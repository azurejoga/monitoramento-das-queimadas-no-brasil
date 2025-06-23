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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 293e1fec-5c40-34bc-a216-c52f9cbda840 | -8.07452 | -43.09581 | 2025-06-23 11:47:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.1 |
| 1356797a-b852-3b14-b32a-d94f30634db4 | -13.58517 | -41.81781 | 2025-06-23 11:49:00 | TERRA_M-M | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 6849544f-d208-3944-8f8f-b7c32dac1012 | -19.98646 | -47.16587 | 2025-06-23 11:49:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 2dd0690e-ade8-335b-bb3d-690219082abb | -16.46691 | -44.99059 | 2025-06-23 11:49:00 | TERRA_M-M | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 2cb3b9d1-f78b-324a-a528-3e3657a1ec0f | -14.88963 | -41.34151 | 2025-06-23 11:49:00 | TERRA_M-M | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| aad72f69-480e-33eb-b989-e9101e8a949e | -13.5754 | -41.81621 | 2025-06-23 11:49:00 | TERRA_M-M | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 0a0de798-959e-3add-9b84-3c14659b7aad | -11.81264 | -43.77908 | 2025-06-23 11:49:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 426f6b34-88fc-33e4-b23b-357c505accb5 | -21.27253 | -42.29296 | 2025-06-23 11:49:00 | TERRA_M-M | BARÃO DE MONTE ALTO | MINAS GERAIS | Brasil | 3105509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| d971949a-b8ca-394b-8c02-ed1f61e68e46 | -16.46623 | -45.01874 | 2025-06-23 11:49:00 | TERRA_M-M | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 6613d8df-026f-3602-8e9c-88ec4ab093e1 | -17.66801 | -46.83982 | 2025-06-23 11:49:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 83af1a9f-d385-398e-af9c-3625c833ec1e | -18.01662 | -45.99495 | 2025-06-23 11:49:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 70ed4d0e-d1d4-361f-8406-c3ed5d2d0b60 | -20.66391 | -43.4591 | 2025-06-23 11:49:00 | TERRA_M-M | CATAS ALTAS DA NORUEGA | MINAS GERAIS | Brasil | 3115409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 019c7186-2670-3af5-82a1-da2720c658a1 | -16.46394 | -45.00759 | 2025-06-23 11:49:00 | TERRA_M-M | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 81.9 |
| cb7e587d-e3c9-309e-b3d5-4707dea63b74 | -14.39108 | -46.13994 | 2025-06-23 11:49:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 22.3 |
| d911ad5f-9a69-3089-b65c-45debe33f3c7 | -19.12657 | -40.16674 | 2025-06-23 11:49:00 | TERRA_M-M | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 20311f3d-24c1-3cab-8004-b79b635c991c | -11.57506 | -44.65477 | 2025-06-23 11:49:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 222.5 |
| 798dfcff-2f6d-39bb-842b-f07af71001b1 | -20.05311 | -45.71148 | 2025-06-23 11:49:00 | TERRA_M-M | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 5a99c383-2f51-3bf2-bb8c-390d4aa7b7b7 | -19.05327 | -40.34878 | 2025-06-23 11:49:00 | TERRA_M-M | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| da6fd704-71ca-33d7-8af3-7d3cf6a63e74 | -14.89742 | -41.35322 | 2025-06-23 11:49:00 | TERRA_M-M | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 5afd31b2-fb41-3caf-8e42-0c921ae07500 | -14.88806 | -41.35167 | 2025-06-23 11:49:00 | TERRA_M-M | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 17.0 |
| d44eb311-dc67-3b07-930b-e2fbc436c989 | -20.05396 | -45.72192 | 2025-06-23 11:49:00 | TERRA_M-M | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ce30990f-961c-3c4d-800d-0ed9bf756fdb | -16.46909 | -45.00162 | 2025-06-23 11:49:00 | TERRA_M-M | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 5d76d941-e7ce-3c96-b804-fb94b19dd0f5 | -8.5909 | -51.5746 | 2025-06-23 11:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 155.3 |
| 8b9d3084-2571-362d-8bd3-241574eace7e | -8.0703 | -43.0981 | 2025-06-23 11:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 126.4 |
| b63f8ef3-6321-3e29-9f76-a314bcb57690 | -11.5812 | -44.6554 | 2025-06-23 11:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 1ea52cb5-fcb3-334d-8b7f-99435a329487 | -8.07 | -43.1216 | 2025-06-23 11:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 139.1 |
| 0d79a6c6-509c-3ff3-8935-7d752672a5aa | -16.2171 | -49.9705 | 2025-06-23 12:00:00 | GOES-19 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 862ecbda-ff25-364a-b9f0-f07fe4afb57e | -11.5812 | -44.6554 | 2025-06-23 12:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 174.1 |
| c319027f-0b1e-3008-8de3-07f4f5730d9a | -8.0703 | -43.0981 | 2025-06-23 12:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 172.2 |
| 0d246ccc-7510-33ae-8f51-b48c7774818e | -8.5909 | -51.5746 | 2025-06-23 12:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 167.5 |
| 528762dc-56ba-37e5-ae2d-dba709098062 | -16.4682 | -45.0031 | 2025-06-23 12:00:00 | GOES-19 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 97.2 |
| d1faf3eb-a3db-342c-97e6-064c699bba6e | -8.5907 | -51.5955 | 2025-06-23 12:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| ee28b548-fcf2-38f5-8459-4b87545a471e | -8.051 | -43.1237 | 2025-06-23 12:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 116.8 |
| e8c2a864-2bfa-38fc-866b-b25bef64e78c | -16.2171 | -49.9705 | 2025-06-23 12:10:00 | GOES-19 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 149b0376-b44c-3b47-8379-3b36c81efd26 | -8.0703 | -43.0981 | 2025-06-23 12:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 182.6 |
| c272f5f6-5439-3025-b519-2d8c200537dc | -8.5909 | -51.5746 | 2025-06-23 12:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 215.8 |
| 91e4cc6c-73ae-3915-98b9-56cf4bca140b | -8.5722 | -51.5761 | 2025-06-23 12:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 3a6daf46-547c-3a3f-aa7a-db7e945e5046 | -8.07 | -43.1216 | 2025-06-23 12:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 176.6 |
| 66599928-3907-3f8c-8fe9-3b9968ed4ae5 | -11.5812 | -44.6554 | 2025-06-23 12:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| e8212f49-203f-308e-b4e9-5be5e319cea5 | -8.0703 | -43.0981 | 2025-06-23 12:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 197.2 |
| d458cf56-f715-3ca4-b287-071d0d3079bc | -8.5907 | -51.5955 | 2025-06-23 12:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 7edc106f-651c-3549-8e59-947d338b0add | -8.07 | -43.1216 | 2025-06-23 12:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 229.5 |
| cd2872c1-7cb0-3226-aa17-a1279249631d | -8.051 | -43.1237 | 2025-06-23 12:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 149.3 |
| 2fb681be-4e16-3a4e-b1e9-cc29afb4880d | -8.5722 | -51.5761 | 2025-06-23 12:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 3b2ee635-3972-392b-9d05-40ac2fb7fda3 | -8.5909 | -51.5746 | 2025-06-23 12:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 189.9 |
| 987e8dee-575e-3095-a697-7ff9a8f6a8c0 | -11.5812 | -44.6554 | 2025-06-23 12:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| a0b76f1f-6e48-351b-a84c-b8f355950975 | -8.07 | -43.1216 | 2025-06-23 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 211.0 |
| 5b79a5e3-e75d-372b-82fc-3eb2a9ce20c6 | -8.5909 | -51.5746 | 2025-06-23 12:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 197.2 |
| d15ed72a-8bef-3e69-b8c4-7fe8941732e3 | -8.051 | -43.1237 | 2025-06-23 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 163.4 |
| 75c5cb68-c50d-3bc1-a68e-bfa726d372e9 | -11.5812 | -44.6554 | 2025-06-23 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 148.5 |
| e58ea775-4bf1-395d-ae28-1d96c6f3990d | -8.5907 | -51.5955 | 2025-06-23 12:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| e82ee4da-e601-39d1-a3de-ae1c1a9e7793 | -16.4682 | -45.0031 | 2025-06-23 12:30:00 | GOES-19 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 99.1 |
| df4d0318-3608-33ec-acb6-21310f25d5f7 | -8.0703 | -43.0981 | 2025-06-23 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 223.5 |
| cf3f176f-5ed8-34c3-8497-4782f8082f34 | -8.5722 | -51.5761 | 2025-06-23 12:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| cbf05b6b-bef2-3ed3-9ad0-b7b1a1181ee9 | -16.4682 | -45.0031 | 2025-06-23 12:40:00 | GOES-19 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 74e0d731-0804-3c18-a178-f316db2f7a99 | -8.5907 | -51.5955 | 2025-06-23 12:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 409d2357-f875-348f-ac3f-2c30e88f5dd9 | -8.5909 | -51.5746 | 2025-06-23 12:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 205.6 |
| 65d2b702-2f15-3f0c-8e04-60b523c93e10 | -11.5808 | -44.6786 | 2025-06-23 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| af2127ef-851a-3c14-bc88-4396c5f43511 | -7.3143 | -43.2235 | 2025-06-23 12:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 100.0 |
| e423fa38-84a2-35e9-a3d4-07efb4450405 | -8.0703 | -43.0981 | 2025-06-23 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 298.9 |
| 1aa0ff8b-a9b6-3fdb-8661-9a7f8b682557 | -8.07 | -43.1216 | 2025-06-23 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 261.6 |
| 2c7a310e-021c-3f77-956d-44eb8365f95d | -11.5812 | -44.6554 | 2025-06-23 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 178.4 |
| 02d2433c-14f7-35f8-bf18-78d21e966b95 | -7.2955 | -43.2253 | 2025-06-23 12:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 92.2 |
| 15e861b4-3e46-36e9-b30a-7fb0d366c0de | -8.051 | -43.1237 | 2025-06-23 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 121.9 |
| 6a3396d9-f463-35d9-9c16-b567797aa77a | -8.5907 | -51.5955 | 2025-06-23 12:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| be677054-43b5-36e0-ac40-95e9ff610e41 | -16.4682 | -45.0031 | 2025-06-23 12:50:00 | GOES-19 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 94.9 |
| c68d08fb-a666-3161-99a3-725311219793 | -11.5808 | -44.6786 | 2025-06-23 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 1d8395c7-cebc-3c35-a43f-6ab9bc6e044f | -11.5812 | -44.6554 | 2025-06-23 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 152.2 |
| a390c3c2-1587-3e62-8ec9-c09ac020dff8 | -8.051 | -43.1237 | 2025-06-23 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 200.7 |
| 0c80fe6e-b211-32be-b44f-170535cc005f | -8.07 | -43.1216 | 2025-06-23 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 386.3 |
| d3b85d45-6f07-396b-80ff-068fe9352443 | -16.2171 | -49.9705 | 2025-06-23 12:50:00 | GOES-19 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 53c9d3fe-5c84-38be-936b-6b9dc77ca3d7 | -7.3143 | -43.2235 | 2025-06-23 12:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 114.4 |
| ef4507a3-c914-3137-b582-8b8d72c91e71 | -8.0703 | -43.0981 | 2025-06-23 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 314.7 |
| 35521fdb-1597-385a-99fb-a18910ecfedb | -8.5909 | -51.5746 | 2025-06-23 12:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 196.1 |
| ebf5141a-6e38-34a2-9de6-634652b18b50 | -8.6097 | -51.5731 | 2025-06-23 13:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 5d35094f-22f3-3b21-ae75-aa79f9483727 | -8.0703 | -43.0981 | 2025-06-23 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 313.7 |
| 89e8495a-c53d-34da-a25e-c7617a0aa70f | -11.5812 | -44.6554 | 2025-06-23 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 8620867d-cf8d-3510-8ad3-e124fd2e8c95 | -8.07 | -43.1216 | 2025-06-23 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 288.7 |
| 7cad08a8-c883-3ef9-8a32-b4fed5ce5064 | -8.5909 | -51.5746 | 2025-06-23 13:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 361.6 |
| 2e6eb73c-e703-394f-adba-bea01c566b46 | -8.5911 | -51.5537 | 2025-06-23 13:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 3c632e82-35fb-3394-893b-b2840541ff98 | -8.051 | -43.1237 | 2025-06-23 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 197.3 |
| 5b842e7c-5d8b-3a08-92cd-1a5e5c53c62e | -8.5907 | -51.5955 | 2025-06-23 13:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 5acbd028-8d46-33fc-b1a4-b5a8cdf87095 | -11.5812 | -44.6554 | 2025-06-23 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| d9a34156-7d44-3f9c-9ca8-c4045229be28 | -8.07 | -43.1216 | 2025-06-23 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 279.8 |
| 34a7864a-f5e5-3984-b8f1-43fe6eb33426 | -8.051 | -43.1237 | 2025-06-23 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 164.6 |
| 3130f2aa-78cd-3b87-a6d2-5da427bf5ca2 | -8.5911 | -51.5537 | 2025-06-23 13:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 83448154-6300-3559-9c33-f6826dd7761d | -8.0703 | -43.0981 | 2025-06-23 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 310.5 |
| 9be881fd-4d8b-35e3-8da6-d7cc1f49e6bf | -8.5907 | -51.5955 | 2025-06-23 13:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| eb10fd1b-a372-3748-a876-4660a9719eb4 | -7.3143 | -43.2235 | 2025-06-23 13:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 137.1 |
| adb4787c-a11c-383d-a385-92f02d4dcc80 | -8.5909 | -51.5746 | 2025-06-23 13:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 365.6 |
| 74617bfd-5358-34a8-bb8b-3bc96a83920a | -11.2699 | -52.4814 | 2025-06-23 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 4641eef9-595d-3157-944f-e2d77ae86273 | -8.5907 | -51.5955 | 2025-06-23 13:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 1d2c2056-4580-3da2-8dbb-a377a7cee17d | -7.4758 | -45.5551 | 2025-06-23 13:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 78abbe5d-dd04-373f-83d3-835f09f933e7 | -11.2702 | -52.4605 | 2025-06-23 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| e551b1f8-4d65-31f1-b85d-f4b9e3497aee | -8.0703 | -43.0981 | 2025-06-23 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 259.0 |
| 25e43875-ddb5-3089-bc8a-7ba0cde3223b | -8.07 | -43.1216 | 2025-06-23 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 328.9 |
| 80f2f14a-7909-3c43-9210-14aa9123a33e | -11.5812 | -44.6554 | 2025-06-23 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 4b566785-3e76-36f1-8b29-908e3fcf05d4 | -7.457 | -45.5568 | 2025-06-23 13:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 6d02331d-eb08-39a7-8d0c-3816abf6c4d4 | -8.051 | -43.1237 | 2025-06-23 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 147.6 |
| 40fa0679-957b-381c-b103-3fa0cab00792 | -8.5909 | -51.5746 | 2025-06-23 13:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 230.8 |


[Clique aqui para ver as próximas entradas](README12.md)
