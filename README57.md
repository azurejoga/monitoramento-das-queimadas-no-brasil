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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3205ba5-0fad-3a17-98be-aa6f6e09b87e | -2.17647 | -52.13534 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28d7ee14-5adc-3b31-af90-20d133ab98b8 | -1.5026 | -52.12075 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4817c178-b496-3361-9607-d2d717a1fb7c | -1.64059 | -52.69163 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4774851a-4c7f-3e67-95bb-e3c512100edd | -0.13199 | -51.69749 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20f77f5d-3e77-3eb3-8d1c-997761124e9f | -1.64768 | -52.66805 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2a5d779-c450-3ad4-99f2-97a8cf8ca354 | -2.10213 | -48.89344 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea98e4e4-0eb9-3b29-9e57-74705a6cd6a9 | -1.09531 | -47.50358 | 2024-11-21 04:53:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d253637f-5d50-3a0d-9297-2249f898a0af | -0.9082 | -52.57419 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa9597c0-7bb4-3db9-ac50-a779d610570a | -2.69179 | -46.25165 | 2024-11-21 04:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8851a7fe-653f-371c-988b-788b4fdda6cf | -2.37242 | -50.33306 | 2024-11-21 04:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d9acc9a-8ac6-300b-aa74-6300497d28f6 | -1.28043 | -54.55415 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d684797b-685e-32a7-a92d-c29050c1cccb | -2.1458 | -50.64822 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4b99edfd-891a-3c70-83c5-733d4fcfaf80 | -0.39816 | -51.53972 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d897d6b-753e-31f4-8a2b-567d35d848b5 | -1.77984 | -53.60064 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 60ef717c-dd18-3433-a9f4-2be5a9c355cf | -1.70714 | -52.72347 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fde54a7-3813-3c7d-ba88-1e658661d3c0 | -1.08031 | -53.18768 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6a217110-1f25-3873-991d-e738e54450b8 | -1.65381 | -52.69368 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13e398ac-275c-3d48-8315-b06175a9f08e | -2.83462 | -46.67931 | 2024-11-21 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b84ef60-b89b-3931-b2c8-1e97f5af96e8 | -2.22586 | -48.37932 | 2024-11-21 04:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc2f1d62-b93b-375a-a463-f1e7944c2327 | -1.46442 | -55.45206 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45a6ee43-2fad-35e1-9734-ea852b9b0b08 | -1.51002 | -52.22538 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2081c5b-71c1-351a-8a05-b0f21ad68bc0 | -0.77321 | -51.74572 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eff50456-d74e-3c4a-a9f7-e26f2de9e21c | -1.73022 | -52.70591 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 553badf1-f8f6-3024-8cbb-4b82dcb055d5 | -1.26797 | -51.62587 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e483e1d-1ed5-341d-b0b9-52e7d3bba15f | -1.61344 | -52.47551 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2fb0145c-f751-3406-94d1-a1cf78760c33 | -1.13238 | -54.2128 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3656a91c-dcea-36bc-a027-9129e6ec63e9 | -1.3479 | -55.44658 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d42e9d4e-ceba-37db-9dcf-29d80cc415e2 | -2.72419 | -48.73441 | 2024-11-21 04:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2aad53f-1775-36f0-82bf-e1866ba3cd71 | -1.41203 | -52.07095 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b3be1f5-e4b7-3ff3-9f8d-cb39e4acebb4 | -1.19766 | -51.76768 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e7c94ba-602c-3a99-80b1-fe1a84b569ff | -1.13418 | -53.66529 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7e9c0f7-e648-3f52-a94e-008986f50631 | -1.73119 | -53.02268 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| efe22860-fe2d-38ea-b4bd-9b2a55b336c3 | -2.14701 | -53.57663 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8962ee15-b1a9-3df0-a9ef-3a5c3c1b08d6 | -0.83101 | -52.87144 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe9f311a-ca46-34fc-acb5-6fea1b88bfa3 | -0.17252 | -51.63542 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0af9b6a7-789d-348d-a0a1-0056f9601334 | -2.62392 | -48.06693 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1fbb6104-3835-38f0-a6ac-f6fb0424047f | -1.47761 | -51.1384 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed253e89-7e3b-3f79-a2fd-cbb871673b6c | -1.98804 | -53.1405 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fefb934b-c633-3c68-a21c-da7fa83452f1 | -1.64058 | -55.68126 | 2024-11-21 04:53:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f762853-b78a-3cf2-9a20-f9bcb9e125a4 | -2.57366 | -49.19853 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a274322-dc60-3d6d-84a7-cdc617563add | -2.72472 | -48.73098 | 2024-11-21 04:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7717c126-9152-32c8-800e-fc04f322e274 | -1.18915 | -51.9753 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e08b7cf-5ea5-3495-b848-2b52bdbb906e | -1.33003 | -51.85674 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e55a07a-a694-31e3-9be3-a8a8c0327d7d | -2.28232 | -50.58446 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8d85f90-402a-3373-bb8c-c7931e2a9883 | -1.64544 | -46.96135 | 2024-11-21 04:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4961cd6f-50b9-35c9-ad59-edfed1f10146 | -2.15304 | -48.9207 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa5a324f-db54-3347-8207-c80e0915e941 | -1.19582 | -51.97633 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 750716f7-203a-3f06-9218-002b05ae0bf9 | -2.26221 | -48.4225 | 2024-11-21 04:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51b70f32-d91c-373d-87a4-a54a1cfb2f77 | -2.19822 | -50.68016 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f42718f-aab8-37fc-964c-6fb40f8c1f41 | -2.60834 | -49.25134 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7e7e862a-2ca8-327d-a3dd-5bfed7dad1a7 | -2.66696 | -46.23553 | 2024-11-21 04:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c0b4cca-aa29-36cd-b269-7a2e8dae7abf | -1.14907 | -51.94759 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0dc81e0-2efe-3152-b61f-d2f948d82f8a | -1.11836 | -53.39762 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9a1d7618-1dd3-396f-9322-3647dee35765 | -1.3661 | -51.38326 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0aa49d06-7df7-3e6b-a671-0aeb255fee96 | -2.27532 | -49.56 | 2024-11-21 04:53:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 021ad480-f1f4-346e-844d-004319299146 | -1.41508 | -52.22491 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f5a6c91-ace6-3b3c-88fa-e088f769a61b | -1.54454 | -54.29157 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42883411-079b-30e2-b3d1-2df69a432b13 | -1.60125 | -52.25054 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6c8e16e-92b3-379a-bef2-aae3b0cb57a9 | -1.23839 | -51.74862 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 488d092b-bfe9-386f-a97c-445e5c2bb271 | -2.65366 | -49.28379 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 424eee8a-790b-3298-b7e0-9059bc583fdd | -1.42356 | -51.62429 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dba75ab3-8c79-341c-87b3-c5827a0bfe04 | -1.34561 | -55.43836 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf484176-d169-3232-9772-09dadb6a3f1e | -1.53354 | -52.03238 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c58734a-924f-336d-9b70-224bb2155774 | -2.0921 | -53.34276 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7376163c-d346-3262-88cc-7de3618be1d7 | -1.12079 | -53.59953 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa42ee69-c77a-3f0d-afb9-6a53368af85b | -0.79933 | -51.23772 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c5ed60f-3e27-3495-9002-e42d7c22caf0 | -1.49941 | -52.18454 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74d9ccfd-1f4d-3506-8b28-057e4d0fdcb4 | -3.59012 | -43.63382 | 2024-11-21 04:53:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86b4f72d-8cbb-3ba3-8f8b-b17b4c49c340 | -1.33913 | -52.18824 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3577b20-fdfa-3adb-bed8-f404fd8cc8bb | -1.11091 | -52.34428 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a21b424-63ec-3496-9b25-4c5183c43e41 | -1.79571 | -54.03966 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 081ebaf8-ba18-3ff2-be86-24031181b811 | -1.61879 | -52.59301 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84fcdaa3-c2be-319f-9385-c7c19ded6464 | -2.15534 | -50.49286 | 2024-11-21 04:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a87bfd74-10af-39b2-9247-db7eea1bdb36 | -0.07126 | -51.50027 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe870dc4-2468-31de-bd8d-4e051be8d4e7 | -1.75602 | -52.67113 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 04da71ef-dc48-3f36-8b49-905485e6dcc7 | -2.19888 | -49.55029 | 2024-11-21 04:53:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 228ca955-b03e-3ba8-a3a7-f015f66641c1 | -0.29593 | -51.6069 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2b7df2b0-4c83-3223-bd5a-8bf34701c2be | -1.70882 | -50.20058 | 2024-11-21 04:53:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7bb74ea-4181-3b27-bd34-eab0932e304a | -0.66637 | -51.66757 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e643c610-5cfe-3e1c-b304-1c5470e9c4bd | -1.22783 | -51.79406 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a10d8c8-3184-3fb6-8561-677691177ab2 | -0.95449 | -51.71946 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2c44a6a-e81d-3475-b5d8-c35edc16061c | -2.1837 | -52.13286 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f4029c1-6726-3614-b1bc-64771ebe55ec | -1.51374 | -51.15521 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed7ba870-518a-379e-9219-03d8779c1639 | -1.61627 | -55.40453 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d308d00-7cdc-30be-8753-7bcb213e0fce | -2.65918 | -48.48388 | 2024-11-21 04:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dfde167f-2e17-3af7-a895-6bff754ce799 | -2.2073 | -50.76839 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e35f4d5a-bb35-3e46-b79d-21d8c5b7dd95 | -1.98527 | -53.13655 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54ccdfc3-800a-3f55-b337-d84002049df9 | -1.98858 | -53.13707 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d09e871-ab7d-3311-b694-434932002740 | -1.55322 | -53.44102 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68255133-9aae-38dc-a986-40b727a81fd3 | -1.499 | -51.99111 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d504d24-e83a-3570-86f0-316040e65864 | -1.73144 | -52.39488 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3da63837-479c-3557-b206-c64e30b6d997 | -1.60061 | -46.8708 | 2024-11-21 04:53:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 014455c7-f655-3a5d-b9fc-37276d102e27 | -0.88531 | -51.72324 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57ce3d84-b560-312d-b854-ecb380c108d4 | -1.10758 | -51.75774 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57fe4118-39dd-3acb-b3b1-d5bf0d5cc5c2 | -1.23504 | -51.7481 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 401faf81-1a6e-3d45-ac2e-4186a9b49e8f | -1.21883 | -51.74197 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 22d025af-752b-3c65-a3ff-5cd2d242ddb6 | -2.01837 | -51.17806 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 60644843-f0cd-3b0f-acba-87322f7fbfdc | -1.63505 | -52.68372 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48062538-2fe0-38d1-b2e0-0e9fc0d44fcd | -2.74184 | -47.53827 | 2024-11-21 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db43fbe4-7cca-3831-ac88-c1f34d726ee7 | -2.41817 | -48.9771 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README58.md)
