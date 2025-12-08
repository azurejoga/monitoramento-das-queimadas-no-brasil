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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 424575dd-d0d2-3f66-bf7e-b3dfa6bbd30a | -0.31416 | -51.70372 | 2025-12-08 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dab272dd-3ee9-378c-8679-5727322da3e1 | -2.2574 | -46.11621 | 2025-12-08 05:14:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00c0f0b8-4493-385b-9108-891e95c1ca8a | -3.39666 | -44.16425 | 2025-12-08 05:14:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c972f0f-9fce-381a-aad8-b3410be8e7e0 | -1.364 | -47.69872 | 2025-12-08 05:14:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42e5bfff-a475-3eb2-a865-a0ba3a817c12 | -2.50651 | -51.79943 | 2025-12-08 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| af71d8c6-a68c-3f02-8040-2f67b2e39508 | -4.50457 | -55.80568 | 2025-12-08 05:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1afa07b-6cbd-3644-a2da-2f6c37adb163 | -2.25156 | -46.11531 | 2025-12-08 05:14:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2f4abc0-f4c3-3168-b4c1-ef1f321dd3bf | -0.80763 | -51.94815 | 2025-12-08 05:14:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ad6a7ea6-1c0c-35a2-b125-ffdaccdf7a7b | -0.13284 | -51.74183 | 2025-12-08 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c9f0fb1-89e6-3c84-8124-eeea321a02c9 | -0.37908 | -51.96166 | 2025-12-08 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a796cc3-168a-35a5-989f-85f6b584fd9f | -1.36266 | -47.69845 | 2025-12-08 05:14:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfcba86b-31bb-353c-9b03-4e670d3db370 | -2.63762 | -46.96331 | 2025-12-08 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aec44bdf-56de-3ef3-b1a6-8640b2ab8681 | -0.31162 | -51.7004 | 2025-12-08 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2843f9b-e6eb-3570-9817-4255688d498e | -0.30019 | -51.69166 | 2025-12-08 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8b40d61-16a4-3859-9798-a19c1a4d867c | -0.31028 | -51.70311 | 2025-12-08 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 986fd2ea-3a25-3856-96b2-07b4504a27cf | -3.66277 | -47.16584 | 2025-12-08 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07708b45-5803-3ea5-b3bd-17ee104c73bd | -3.65721 | -47.165 | 2025-12-08 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a31b2107-37c9-381d-950e-0f3b06dc3b90 | -4.50121 | -55.80516 | 2025-12-08 05:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5598ff14-ebe7-3158-9c50-261902297487 | -4.11186 | -50.44183 | 2025-12-08 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b2a1980-8617-3251-85af-e8f2780874b8 | -4.11251 | -50.43748 | 2025-12-08 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc49b50f-843a-3a49-8e51-5f3fd67e7591 | -3.54516 | -54.72769 | 2025-12-08 05:14:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5864393d-84c7-3a38-a55b-cc5ab95baa63 | -1.68019 | -45.86825 | 2025-12-08 05:14:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5ed1b55-caa7-3279-b023-414d1934836b | -2.25176 | -46.11771 | 2025-12-08 05:14:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6858e12-cb60-34e8-b3d1-cccb40229ea3 | -2.25678 | -46.12035 | 2025-12-08 05:14:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3519583c-86e6-3031-81f0-3f98c791f0cb | -0.99916 | -52.31736 | 2025-12-08 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46b04249-29e3-3f13-a25e-918ab045849d | -0.98288 | -52.97594 | 2025-12-08 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27bf97de-cbd9-3ab7-a9b2-0247d94b0ba4 | -2.63817 | -46.95974 | 2025-12-08 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 02d18469-30de-3c81-b164-823c8934e66d | -0.80839 | -51.94337 | 2025-12-08 05:14:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fb39874a-4569-3dd2-b122-276551486633 | -0.30407 | -51.69225 | 2025-12-08 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 14d6229d-3816-346b-82ba-6d581c3286af | 0.47975 | -54.07922 | 2025-12-08 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1984740b-63ef-3176-8a58-0f4fbae49e9e | -2.64261 | -46.96778 | 2025-12-08 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c2dafc81-f62c-3498-8d98-0ca5a9173923 | -1.68083 | -45.864 | 2025-12-08 05:14:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36bf67b2-c8fe-34ff-902d-fbe38cfb150e | -2.25241 | -46.11354 | 2025-12-08 05:14:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a46327d-8505-3e18-b31c-cca4f916813f | -0.80936 | -51.94536 | 2025-12-08 05:14:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d6c3bfbc-f83f-34ab-8f8d-f9b1f6352267 | -0.38362 | -51.9576 | 2025-12-08 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 336065ef-5bc7-347b-9187-eaf8dd62c420 | -0.3829 | -51.96227 | 2025-12-08 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3857d9d3-c2e7-3b93-9623-20acd52516e7 | -0.31106 | -51.69829 | 2025-12-08 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ceeed18-9c78-3069-8ab8-546ef8d44954 | -2.63708 | -46.96683 | 2025-12-08 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d7b7304-7e1b-3a59-a958-af24b08194e7 | -3.38996 | -44.16329 | 2025-12-08 05:14:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6287dcba-11d1-36e0-aef4-054a0dd94f7e | -9.44425 | -59.20698 | 2025-12-08 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 218c971f-8e42-31f6-a3e9-16daa62a196e | -0.38183 | -51.96441 | 2025-12-08 05:33:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01d1210c-71c3-387d-bf13-4bad5a369bd2 | 3.67683 | -51.38608 | 2025-12-08 05:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 190716e2-75b8-3cab-aab6-93f85878ba50 | 3.41999 | -51.25159 | 2025-12-08 05:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7c364785-c530-35f2-94da-89f934a11473 | -0.29928 | -51.69404 | 2025-12-08 05:33:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cd24fc5-eb88-3f33-80d9-ede59042fe77 | 3.29763 | -60.83459 | 2025-12-08 05:33:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0370fc3b-5611-3036-8f71-c0ab4526df2c | 3.67474 | -51.38637 | 2025-12-08 05:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b46164d-0d5f-3c63-956c-d0375e385fec | 4.31953 | -60.07676 | 2025-12-08 05:33:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbcf7e3d-18ea-30f9-9735-54f1858d0c92 | 3.39759 | -51.25957 | 2025-12-08 05:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 446d4e99-2b7a-31cd-ade7-6f8b3aefb978 | 3.3004 | -60.83059 | 2025-12-08 05:33:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6331f021-7807-3283-be93-fa715de8ed4b | 3.39828 | -51.26362 | 2025-12-08 05:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d9e682fb-e388-36fa-89a5-b75021b0842a | 3.415 | -51.25281 | 2025-12-08 05:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 29b43733-a880-367b-9eb7-202474d3d35e | 3.30482 | -60.83703 | 2025-12-08 05:33:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 776ef0e6-66b3-3ca1-af00-e1bb2c8dc2d4 | 4.34983 | -60.22448 | 2025-12-08 05:33:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ebc8d3f-2b99-30d4-a56d-f8a9c6134e69 | 3.42066 | -51.25565 | 2025-12-08 05:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8c27d02-a12a-3061-819e-12cea2e5b47b | -2.07983 | -56.59291 | 2025-12-08 05:33:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6082e59b-37ab-3549-be4d-aee8d9b91582 | 3.40845 | -51.25356 | 2025-12-08 05:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d43544b8-e58f-3d0b-a394-f48a57feac67 | -2.50559 | -51.8058 | 2025-12-08 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7055daf-9d7e-3ed1-a90e-3ecdd5b47b66 | 3.42147 | -51.25589 | 2025-12-08 05:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e3f4ad6-e446-3427-aca9-77759f05ee4b | 3.40268 | -51.25454 | 2025-12-08 05:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| acbb6f5c-11e4-3c60-82ac-f3c262c94903 | -0.30523 | -51.69495 | 2025-12-08 05:33:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 640a6cab-801f-3f2f-8e07-3ff0caed876f | 3.66971 | -51.39134 | 2025-12-08 05:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f908d46-690b-35f4-927d-5b75ecda35d2 | 3.42643 | -51.25468 | 2025-12-08 05:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee5ce262-920c-3784-b062-1971f3ca9eaf | 3.67182 | -51.39103 | 2025-12-08 05:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a056483-21d1-3c80-8dcf-b626c3671f1a | 3.41422 | -51.25257 | 2025-12-08 05:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 06614d20-1c95-3cbd-b47a-7bda5a6db5b5 | -0.38248 | -51.9603 | 2025-12-08 05:33:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4034919-4306-33af-b780-aca576dd2f1c | -2.08036 | -56.59134 | 2025-12-08 05:33:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d070ef67-b23d-303c-8a25-c6c3a770d7d3 | -2.50628 | -51.80117 | 2025-12-08 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0de60e0f-63a4-3d3a-9d37-48bb2fafea91 | 3.30095 | -60.83407 | 2025-12-08 05:33:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5949c65-4539-3a64-9b55-fda94e37d651 | 3.40913 | -51.25761 | 2025-12-08 05:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fb074cb7-1037-33bf-8103-2c3788a9459b | 4.26465 | -59.88345 | 2025-12-08 05:33:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a847460-768f-3ffb-8aa4-3ab4d944941d | 3.40336 | -51.25859 | 2025-12-08 05:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a3ce0432-3704-3c99-87fa-8ea93a4a1b38 | 3.42077 | -51.25184 | 2025-12-08 05:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bee0bcbd-df26-32af-834a-1ea377eac995 | 3.40923 | -51.25378 | 2025-12-08 05:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2393de0c-c85d-3d2b-b5a3-822953daa1dd | 3.67541 | -51.3904 | 2025-12-08 05:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f8f73234-2e87-3be3-afd7-4e02ad1c6aa0 | 3.29984 | -60.82712 | 2025-12-08 05:33:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4b05635c-7435-3c1b-92a8-7f01ba8ff46a | 3.39738 | -51.24837 | 2025-12-08 06:16:00 | AQUA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 20.4 |
| bdc0ec61-0798-312e-866b-502c67e47953 | 3.40728 | -51.24694 | 2025-12-08 06:16:00 | AQUA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 22.6 |
| d6a103de-b9b9-3d95-956a-6475b7af588f | 3.39902 | -51.25969 | 2025-12-08 06:16:00 | AQUA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 286dd7bd-b926-38b6-85b0-c73bc76bb291 | 3.40892 | -51.25826 | 2025-12-08 06:16:00 | AQUA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8447ac41-0df0-3fad-8b10-da034b5b4fef | 3.39614 | -51.25422 | 2025-12-08 06:16:00 | AQUA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 1aa905f2-b74c-3b6e-8eed-2bf1cd46bd60 | -4.14503 | -42.42245 | 2025-12-08 06:18:00 | AQUA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 22.4 |
| 4e90ed7e-7e7b-3b4c-bf58-4573327294d0 | -3.73138 | -45.64907 | 2025-12-08 06:18:00 | AQUA_M-M | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b92640fd-51e7-36cb-9b71-e01167f5ea3a | -2.63764 | -46.9705 | 2025-12-08 06:18:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bee49f18-c4b1-3da3-9dae-1b685bc78fac | -3.09449 | -45.25565 | 2025-12-08 06:18:00 | AQUA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 63b76f79-f5ec-3b33-8645-fad862971f8c | -3.4103 | -44.10211 | 2025-12-08 06:18:00 | AQUA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 409708a7-d9e4-3de6-b7d4-ab54e79a5303 | -2.63914 | -46.96035 | 2025-12-08 06:18:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 4798e7ce-79e6-33c0-b6d1-2f991fe21732 | -3.32807 | -42.83685 | 2025-12-08 12:14:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| aa16591d-077c-3f1d-aaa1-65025be3b125 | -4.31888 | -43.81853 | 2025-12-08 12:14:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| ff4ebe86-1dd1-311b-8f0c-9d72900be669 | -1.41776 | -47.38811 | 2025-12-08 12:14:00 | TERRA_M-T | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| bffe230f-9156-342e-98c4-ced54775cb7f | -2.91156 | -42.28085 | 2025-12-08 12:14:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 06a6ba11-a240-3395-baaa-ea9b413871c0 | -1.89313 | -46.45858 | 2025-12-08 12:14:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c0866011-ffb5-3ebc-a078-fcaa3e5997a2 | -2.90339 | -42.08313 | 2025-12-08 12:14:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 9ddfafd4-9d06-3a83-921b-47681a93f49f | -1.68102 | -45.87095 | 2025-12-08 12:14:00 | TERRA_M-T | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b1475c9f-fca5-3046-b327-8790aab1d366 | -4.38247 | -43.35461 | 2025-12-08 12:14:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 03e57df6-038b-341e-92f3-680f631b2645 | -1.43606 | -45.90865 | 2025-12-08 12:14:00 | TERRA_M-T | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 14b20949-7aab-3c8a-ae6c-039af0f7dd53 | -2.70842 | -45.2556 | 2025-12-08 12:14:00 | TERRA_M-T | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 846f54ed-5a11-3643-ac75-c4dd0d84bb96 | -2.19328 | -45.38749 | 2025-12-08 12:14:00 | TERRA_M-T | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 699b5c20-b5d7-3439-8328-c8deaaeb701d | -4.47801 | -42.9893 | 2025-12-08 12:14:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 834b837e-8fc9-357d-90c7-fbf6031a908c | -4.47934 | -42.98087 | 2025-12-08 12:14:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 4df1146d-4317-3997-a7ba-ea710a565cb7 | -1.73906 | -45.65878 | 2025-12-08 12:14:00 | TERRA_M-T | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README6.md)
