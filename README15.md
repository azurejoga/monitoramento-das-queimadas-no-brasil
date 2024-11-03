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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24395622-aac9-3a97-815e-2288099f93c5 | -2.71395 | -49.30394 | 2024-11-03 01:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 15822989-bba4-3a57-b99e-54298abf6b8b | -2.70968 | -49.33294 | 2024-11-03 01:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 150.8 |
| 8f093019-9e2d-3f69-8269-1d72d649fd0f | -2.65137 | -48.58696 | 2024-11-03 01:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 36fd55fe-c9b8-32c4-83ae-ef56cd194331 | -2.64912 | -48.59231 | 2024-11-03 01:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 02eafdd1-1e6c-3378-8c3c-e1d4b6593514 | -2.64523 | -48.54766 | 2024-11-03 01:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 52d8ad18-f5ac-3ab9-a5a1-5df7c0ec3f53 | -2.64325 | -48.55304 | 2024-11-03 01:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 3a75deb2-1ba8-3179-a833-d33c07f033ff | -2.6342 | -48.58967 | 2024-11-03 01:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| bd98c913-3ae5-3a65-af9f-a7b58f712108 | -2.63196 | -48.59502 | 2024-11-03 01:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| d13560b1-1b01-3fd2-8964-2a115f4ac87e | -2.59395 | -53.37705 | 2024-11-03 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| ce3abfb5-0389-3376-8c0e-528dec55be4e | -2.58454 | -53.39505 | 2024-11-03 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 700f01b7-fa6e-3093-907f-6e2dfb34a738 | -2.58215 | -53.37876 | 2024-11-03 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 16853a41-dc29-37c3-aa6a-8b89945f4a0a | -2.57275 | -53.3967 | 2024-11-03 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 2e283fd2-4eb8-3bcf-b855-20fb823e5394 | -2.57034 | -53.38037 | 2024-11-03 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 25906a60-45a1-38af-8bfb-33a7cf52adbd | -2.56382 | -53.38784 | 2024-11-03 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| afa3f13b-ed78-3970-a530-7d85307c365d | -2.54505 | -49.22836 | 2024-11-03 01:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| c9e8d22b-3aff-365a-96ee-8db7d868e084 | -2.51797 | -54.12028 | 2024-11-03 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 907abd98-ab41-3c05-9be9-762af5af68cd | -2.28591 | -48.83057 | 2024-11-03 01:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| c594a818-4010-3dc2-b6f7-ed4921a3ee3d | -2.28013 | -48.7922 | 2024-11-03 01:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 4aebd32f-7a1f-3c3d-9cee-eecba9a4f0c4 | -2.27731 | -48.79952 | 2024-11-03 01:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 322eff71-84ea-3885-be8e-afedea1c7b9f | -2.17853 | -53.68138 | 2024-11-03 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 34bf48fe-40cf-3cd8-879e-c539dbe3d866 | -2.1692 | -53.69858 | 2024-11-03 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 583b61f5-33c7-3dd2-9984-3f551162b5eb | -2.16692 | -53.68295 | 2024-11-03 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| e40f31bd-1bfc-35eb-957b-f4be4e538acb | -2.04899 | -56.36172 | 2024-11-03 01:34:00 | TERRA_M-M | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 411d0e22-e868-3fe2-ba6d-710ac3b2536f | -2.04032 | -56.0653 | 2024-11-03 01:34:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 7583b0ad-eada-3372-89c7-43e1eb82b3f7 | -1.91214 | -54.6409 | 2024-11-03 01:34:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| cb7ce81c-2031-3844-98db-122b28050e44 | -1.90622 | -54.64975 | 2024-11-03 01:34:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e2afd8f0-3839-31b5-a011-137f2a2b7cc3 | -1.87662 | -54.70073 | 2024-11-03 01:34:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9d585973-5cf2-36d9-8271-2ff8f7393079 | -1.87472 | -54.68738 | 2024-11-03 01:34:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 386f0902-f63e-33fa-a330-79111fa8fafa | -1.86397 | -54.68895 | 2024-11-03 01:34:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 75a63c1a-e77d-30a8-bf50-1d13e7f62000 | -1.81706 | -55.2813 | 2024-11-03 01:34:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6eb6612b-604e-3e2b-b37c-a799165666a8 | -1.75486 | -55.1389 | 2024-11-03 01:34:00 | TERRA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f09955f3-d551-3046-aae2-0dc8d6c78cb2 | -1.71145 | -55.77028 | 2024-11-03 01:34:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| e55206e5-bd4e-317d-b1e0-9d40640f7843 | -1.57927 | -52.17495 | 2024-11-03 01:34:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 70a2e5fd-809b-3581-8ab9-106b0c35efa6 | -1.57615 | -52.15367 | 2024-11-03 01:34:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 3e891d0b-8ec9-3917-b4ff-b4509fb76a79 | -1.56648 | -54.21611 | 2024-11-03 01:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| a05294f4-718f-349f-82ce-d228bf85571a | -1.56492 | -54.20818 | 2024-11-03 01:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| fd7530a8-f90c-3fe0-ba49-01cd90ead4d3 | -1.56433 | -54.20153 | 2024-11-03 01:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 12dd099b-b5b6-313b-a2c0-35ad0e48fc3b | -1.52832 | -55.41553 | 2024-11-03 01:34:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1e8436b4-7921-3ddb-b66b-100f9f37ba35 | -1.52705 | -52.00618 | 2024-11-03 01:34:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 8ed6bf92-1438-3044-9b8d-9dd6d8f2531e | -1.52109 | -52.12369 | 2024-11-03 01:34:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| b49c48f5-8d34-3bec-b6ef-89e0e5dc4d98 | -1.46949 | -55.50314 | 2024-11-03 01:34:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| d7c7b929-c96b-30d3-a797-ea1b9cf8e3b6 | -1.45841 | -55.78987 | 2024-11-03 01:34:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 89512779-dec5-3d61-9cac-5b90e532ec90 | -1.36536 | -53.60842 | 2024-11-03 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ac9e454c-bfe4-3a99-959f-9f8e5d3666b2 | -1.3615 | -55.46391 | 2024-11-03 01:34:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cb379018-e42d-3e36-9f71-c9e05367a1b2 | -1.33446 | -54.61164 | 2024-11-03 01:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 159c6949-5e98-37a7-a8fb-8ec8dd73fbd7 | -1.32744 | -54.64081 | 2024-11-03 01:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| be0f061c-ddb6-306c-9ee4-337946fa5d20 | -1.28146 | -53.40397 | 2024-11-03 01:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 81d26d65-4d10-303b-aa55-fab4bc57865b | -1.2791 | -53.38692 | 2024-11-03 01:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 6e852440-b0d6-33af-9e00-fd12a8946f61 | -1.27674 | -53.36993 | 2024-11-03 01:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 2bc39e9c-c3f4-353b-b233-869dcd1094f9 | -1.27668 | -53.41563 | 2024-11-03 01:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 645c19f2-ebf6-3de6-9d55-fb67707767d7 | -1.27418 | -53.39863 | 2024-11-03 01:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 144.4 |
| 9ff4750a-7c4b-3f08-bf45-a7e2658f0dc3 | -1.27181 | -53.42292 | 2024-11-03 01:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 74a5ed12-b8f1-39db-a0e9-8e565dfb74ca | -1.27169 | -53.38162 | 2024-11-03 01:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 564d4406-5ea5-37c7-b61c-5d76b53bfed2 | -1.26943 | -53.40588 | 2024-11-03 01:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 9b4ed8cf-75a5-3d7d-8276-d73806bd2e6a | -1.26704 | -53.38873 | 2024-11-03 01:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| e3de53ba-1d53-3df9-94cf-bf7eed29cf07 | -1.26463 | -53.37146 | 2024-11-03 01:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 0af07df7-3606-31e1-9d98-6b1e7d4e4ce7 | -1.26334 | -55.71267 | 2024-11-03 01:34:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| f6a98326-3567-380e-bb6a-5110ae93976b | -1.26217 | -53.40058 | 2024-11-03 01:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 69b4b786-83bc-319e-8ecf-38fd78ed31be | -1.2617 | -55.70111 | 2024-11-03 01:34:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 60c4cef2-7338-3047-b929-c0b4e051f879 | -1.26006 | -55.6896 | 2024-11-03 01:34:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| be71ffc0-be4e-3315-964e-372e0844841d | -1.21851 | -55.8309 | 2024-11-03 01:34:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b25ef7d4-905b-3d5c-94a3-6ab3d33b3147 | -1.20469 | -54.01897 | 2024-11-03 01:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| b2fd0780-726e-3ca6-b6ae-d16dffed9b55 | -1.20161 | -53.66322 | 2024-11-03 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| f92862cc-fdd4-3c15-825f-23e736acbd29 | -1.2007 | -53.90931 | 2024-11-03 01:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 3131c65b-7275-37b3-8214-238a81ae97d1 | -1.19919 | -53.64596 | 2024-11-03 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 334f0c67-8553-3e8c-93d8-989a07c1391e | -1.15838 | -54.09418 | 2024-11-03 01:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d6306cc9-c753-3ef0-a9ea-1d8d5207b91f | -1.15622 | -54.07884 | 2024-11-03 01:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 25447443-f209-30a4-8ecf-a3d9180900ac | -1.09585 | -53.65086 | 2024-11-03 01:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 84b1e99d-b46a-369e-8533-644e7ef1faf3 | -1.08407 | -53.65292 | 2024-11-03 01:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 7219f1ad-d5ba-37f4-8f34-8f97c79e2eb2 | -0.67959 | -51.69814 | 2024-11-03 01:34:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 79b4cb06-eb57-3e44-9ec6-85d8b2578816 | -1.2572 | -53.3938 | 2024-11-03 01:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 32008a1b-0ae4-3b38-9a14-516d8c3fdb06 | -1.2755 | -53.4138 | 2024-11-03 01:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| d7619fb1-f79d-305c-aae7-f70fcb969641 | -1.2755 | -53.3936 | 2024-11-03 01:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 675985f1-0ccf-32ff-a31e-2c04edf3e0ad | -1.2756 | -53.3734 | 2024-11-03 01:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| b8a45ad1-01b8-30c9-a735-02ffca9a628e | -2.1746 | -53.6834 | 2024-11-03 01:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 409fe10f-41ad-3604-a363-82c6ca5f7ada | -2.2802 | -48.8082 | 2024-11-03 01:35:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| bf223de7-5d9f-3dc9-994b-72fdd0644d72 | -2.2986 | -48.8078 | 2024-11-03 01:35:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 05179f9b-6c8c-37d5-8175-174ef23cc98d | -2.6507 | -48.5629 | 2024-11-03 01:35:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| a46bd076-43fc-3670-8a71-8f935efe1eff | -2.5796 | -53.3927 | 2024-11-03 01:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 0cba0b85-be8a-39b3-8e61-ad7e088fdf75 | -2.5797 | -53.3724 | 2024-11-03 01:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 74c800b0-969a-38b3-9768-38cad556fb3e | -2.6321 | -48.5849 | 2024-11-03 01:35:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| d161a607-fb63-3704-b9e1-554d7b59d984 | -2.7033 | -49.33 | 2024-11-03 01:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| e8c79f26-3c05-3ffb-97cb-a17c6e8cddf9 | -2.7218 | -49.3295 | 2024-11-03 01:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| a0302a00-f5f4-3045-bc2b-e80908ff5de4 | -2.6322 | -48.5634 | 2024-11-03 01:35:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| dc3a3483-7f10-367a-9275-0dffbdc5cc7a | -2.6506 | -48.5844 | 2024-11-03 01:35:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| b5bc4eb5-5c87-341b-926b-531468227dae | -2.7419 | -54.4353 | 2024-11-03 01:35:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 145.0 |
| aedabb44-b4fd-34d6-821e-659a8c7c7fed | -2.7419 | -54.4153 | 2024-11-03 01:35:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 2014d1f1-a8a9-3e4a-972b-e517166d5532 | -2.7602 | -54.4349 | 2024-11-03 01:35:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 208.1 |
| 5ad9782d-bdc3-33a9-8c26-5f5bd7cc0d95 | -2.7603 | -54.4149 | 2024-11-03 01:35:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 195.0 |
| 63233ac9-110e-34fb-8d34-432bee49d037 | -3.0397 | -53.2603 | 2024-11-03 01:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| fdc1263a-a748-3afd-b685-497912db245e | -3.055 | -54.1474 | 2024-11-03 01:35:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| f06d0ef0-06e8-3554-ba1d-a9b19402562c | -3.0734 | -54.167 | 2024-11-03 01:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 855c587c-2634-3843-ba92-47b4c4ae026f | -3.0734 | -54.147 | 2024-11-03 01:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 148.2 |
| 71d06918-ce4e-31e4-a64d-b0fd7fd561b6 | -3.0918 | -54.1465 | 2024-11-03 01:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| cbaec97a-6426-3a1c-b403-8dd36f22867f | -3.1059 | -50.3105 | 2024-11-03 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 9f35a64c-f378-3121-a5dc-da1409adf9b3 | -3.106 | -50.2896 | 2024-11-03 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 233.7 |
| 391fb425-d559-3f23-a827-cdf309be2e92 | -3.1061 | -50.2686 | 2024-11-03 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 6f2b5473-bde2-3afb-8a22-2752cb65ffe3 | -3.1245 | -50.289 | 2024-11-03 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 654c3e24-cb2c-35b6-81f4-3c826418f35d | -3.2415 | -53.3967 | 2024-11-03 01:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 0fe5d956-f7b5-367e-bd87-2754c662e17a | -3.3276 | -50.2825 | 2024-11-03 01:35:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |


[Clique aqui para ver as próximas entradas](README16.md)
