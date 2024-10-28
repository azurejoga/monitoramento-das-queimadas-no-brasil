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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30d44a17-9b95-3286-b33e-b2f1260aa325 | -3.10398 | -51.32379 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 29b2592d-41ae-3909-ba52-a5c81a726ee0 | -3.1002 | -51.25796 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f313640f-e63c-33b3-9c02-cb7347749cdb | -3.09961 | -51.26171 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ecb88d8f-5221-33e7-bec6-378c21c01939 | -3.09879 | -51.33446 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a44d91e0-643c-39a8-a67b-8701b4ae08fe | -3.09536 | -51.33393 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72a4978d-e487-344b-ac4e-d90776e16bad | -3.08333 | -51.1392 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 256ad0d6-69ec-39d1-837a-3297c802027a | -3.08281 | -51.11971 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eaa0376f-cf00-3c5d-aba5-ce6f70a32f0d | -3.08275 | -51.14298 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f95ea2a-f4c7-314f-a53c-4ffdcf95e235 | -3.08222 | -51.1235 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c72329c8-f746-3d6f-a7d6-ad218df2504f | -3.08163 | -51.1273 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f399856-7cf0-3993-9644-92d3cc1f8def | -3.08105 | -51.13108 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 329631fa-4bd0-318e-9310-ecc6ae60ba71 | -3.07988 | -51.13865 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 608908c9-b7bf-3585-b16a-9b458e39b77a | -3.07935 | -51.11916 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| edd342a0-8f6f-3103-a035-9b8f045eddbd | -3.07929 | -51.14244 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7169b1da-fb9c-3c5a-8720-e679583707dd | -3.07876 | -51.12296 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f7a2dca-a74a-3075-8cf9-988a41b1aaad | -3.07873 | -51.35042 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3572b06-a6f7-3ea4-a4bd-d0f068f98286 | -3.07838 | -51.26229 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 836ea11a-900e-3c48-8313-8ac90049e568 | -3.07818 | -51.12675 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76feb342-1b84-3c78-b923-d0f732b579b3 | -3.07779 | -51.26606 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e046e895-f1fa-3c02-9221-9a2cf3e9466d | -3.07611 | -51.25422 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbd15a88-fc18-3e1b-b51f-85917d9101b7 | -3.03344 | -51.46132 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 255b7b9d-5a4b-34a0-8c54-eb00be0e0ac1 | -3.03286 | -51.46504 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3186a324-ffdd-334b-bd62-cf89914e6ff4 | -3.02439 | -51.38402 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eefde86b-0947-3f9b-8d8c-ab54813567e6 | -3.02381 | -51.38773 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 160e8d2b-070f-3a50-b841-54cba8553474 | -3.02096 | -51.38348 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7550c071-3408-378c-8d1b-1a52ec815100 | -2.97769 | -51.04976 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21bcce33-90c7-3fe1-afd5-0ef1c1992af3 | -2.9771 | -51.05357 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e31c8d17-d48e-3325-80f0-0ad070b3e7bb | -2.95639 | -51.00336 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d72cd23b-cc7e-3cea-93ed-e9ed0a5aac03 | -4.53109 | -50.98658 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9955c61b-09a3-35b9-a8e4-399f2454be46 | -4.52756 | -50.98602 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5722c791-86a1-323d-bb6f-d3eab784fdf8 | -4.47634 | -50.99031 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 209a1de5-2f52-3c0f-ad05-ea649911e631 | -4.47574 | -50.99428 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 84bbf519-2b70-3788-aefe-d6b52c5f464d | -4.47281 | -50.98976 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| beb23602-8862-3c3a-8d2f-f08cf67028fe | -4.47221 | -50.99373 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fca6bba-ad27-3ed0-a47e-956c71f05816 | -4.47161 | -50.9977 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1375dd9-ec4c-3854-acd6-69cf53f77f1d | -3.77209 | -51.94422 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97351089-5038-39b3-92a5-81981114a8ee | -3.77153 | -51.94783 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49efeb1d-c9e9-335a-bae0-f68c94112b88 | -3.76871 | -51.94369 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16f51a4b-22df-3e9e-aecb-f33dd8c20fc7 | -3.76815 | -51.94731 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2c62d63-52db-3514-b641-562dabff34a8 | -3.76758 | -51.95092 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48315638-6787-3cae-98d0-06e55e58fa17 | -3.76619 | -51.39601 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25b7f3dc-a117-320a-9f04-bb242b38a879 | -3.76561 | -51.39984 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76adba36-8669-3144-81e1-ebf283b8c41c | -3.76534 | -51.06367 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f0cb2fe-8aaf-3719-ba31-26c0a542e3c1 | -3.76474 | -51.06752 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8ad4891-677f-31da-b0e8-6475757fc7fd | -3.76184 | -51.06316 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c489bc5-30d7-3d1e-bb78-d9c93b905a93 | -3.76126 | -51.06696 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f342eac3-8ea5-3ae9-bcac-7637a7bc39d5 | -3.74732 | -51.81395 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef2034cc-6ddd-3d74-b1c6-2570ea50f88d | -3.69534 | -51.83572 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 785f4a93-d9ac-3ba8-bce2-b0a8a7afd8ad | -3.69478 | -51.83936 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff6c9677-001a-3883-9551-89fe8e91e0ea | -3.69139 | -51.83884 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe8fb605-319e-3143-94f5-f50578ffd5ff | -3.68971 | -51.84979 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22b1ab09-ee20-3810-aab7-bc022de25398 | -3.68915 | -51.85345 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e4bf950-af47-3070-a10a-ae30c76fa4c6 | -3.68841 | -51.55993 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1f2dfa2e-6aca-320e-9303-f4f66adc76ed | -3.68499 | -51.55939 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 88ea44ff-e8ab-3a84-aa49-1a6e044e276c | -3.68441 | -51.56312 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 276359f7-b986-3178-b7ce-8dbb4c7bbe68 | -3.68157 | -51.55885 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 416fcc12-e758-3058-8eba-88eb52b68a6f | -3.681 | -51.56258 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 24e3def3-1dc4-3977-9557-d20b2dcad474 | -3.67815 | -51.55832 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| cca953d4-3cb4-301b-bfea-365c3c6d0ae1 | -3.67758 | -51.56204 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c0884908-b406-36af-9940-ab87510de491 | -3.62397 | -51.5462 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b07b29ae-51a1-3ff6-b4f7-a6e5b144f6b1 | -3.62211 | -51.46671 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46af22c8-dd05-3fad-b21d-c7d5e49dfcf6 | -4.17745 | -51.23502 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58ae6023-eb1c-359d-bba9-7488381e11b8 | -4.13769 | -51.09824 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69a87073-42c4-3920-8fc5-be27b1297600 | -3.86832 | -50.8909 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bafdd121-c26d-314a-8d29-b71a41acea7e | -3.86479 | -50.89038 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c7edb8c6-4564-3bf1-8930-b21336c7fdc5 | -3.86419 | -50.89434 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 95f4bcb9-5a1b-3aa6-ac46-758fcbace5ee | -3.85822 | -51.07368 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7f76db97-4cca-3fc1-b34b-f23e7c6a3ea1 | -3.85763 | -51.07751 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e17645b-2421-3e9f-9bba-5ca86b183d8b | -3.80677 | -50.95833 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba96b2b4-e277-3464-8c35-158859ef7494 | -3.80616 | -50.96227 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0cf1c22-df3f-349d-a8e7-7e929881cdf2 | -3.80266 | -50.96169 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a8989f6-ace4-36d1-ba72-339f2ae216fe | -3.80204 | -50.96566 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b57ad1e-2146-3581-b0e1-b79dfbb5d46f | -3.80142 | -50.96963 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c8a4b4b-ee21-3e9c-a3c2-5756bca87909 | -3.79916 | -50.96113 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9eaefeed-5c8c-3b67-b413-385252fe06ed | -3.79854 | -50.96508 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cf47d2c-fd83-395b-a922-9ee6e7a1bc46 | -3.79792 | -50.96904 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eaa58bb5-72bf-387c-8da1-5110e67e3c33 | -3.96152 | -52.20506 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c946cf9-527b-3012-8b75-1b1ddbbf2614 | -3.96096 | -52.20866 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e066efb-6f31-36ad-8518-f1346bc57064 | -3.9598 | -52.19382 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0cda564-7d71-3bb9-89da-7336c3fba880 | -3.95816 | -52.20452 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6595aba9-c6bd-38d0-93ea-641a9d830349 | -3.9576 | -52.20813 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb22a464-c417-35ed-8198-6dd14432ea5d | -3.95644 | -52.19333 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ceac3b98-1b30-30d2-8736-459a49a1f7a9 | -3.92797 | -52.11881 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d5430b13-2888-3da2-ad97-b128929a80ca | -3.92741 | -52.12241 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31258f58-766c-3e80-8a90-952798654124 | -3.92685 | -52.12599 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fe945d4-eeaa-38c9-8fff-65c9ccc6ce6f | -3.92404 | -52.12188 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa118399-5a9d-3a8b-b291-7a81dca10dc6 | -3.92348 | -52.12547 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8ca1354-bbb1-3fd9-b9fa-2f7a7709323b | -3.8961 | -52.19092 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ddea549-f495-3d12-9b02-94b21e56a90e | -3.89555 | -52.19447 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 66c2c766-413f-321e-8e92-98f3cab0703c | -3.88878 | -52.17154 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccf8f03d-46ba-3e82-b6f1-777638867d2b | -3.88823 | -52.17508 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abb274a8-91ef-3079-8eed-48705d737e9a | -3.8859 | -52.12335 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a500714-2962-3296-9efd-3f4200494f1e | -3.86294 | -52.13818 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32cd05b1-e522-31de-b333-49a2caf94c04 | -3.85999 | -51.69924 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dd92d1dd-2b08-3c28-9ccf-b4f8687de834 | -3.85942 | -51.70293 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cfb5ea93-b951-36b5-9916-f058e205e24e | -3.85939 | -51.8157 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78e3bc8a-c020-34e2-acf7-6dec6bc0b234 | -3.85885 | -51.70663 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff490667-5a4e-3b2e-9346-5b3676289ada | -3.85882 | -51.81936 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1787e15e-4123-3f54-921b-d906ae50de13 | -3.85715 | -51.69503 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d7508e2-4c86-3ac0-aca6-8ca968f558c0 | -3.85658 | -51.69873 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README62.md)
