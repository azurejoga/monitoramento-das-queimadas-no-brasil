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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 620ef4d8-d0c5-3deb-8728-ce2c232c741f | -0.39128 | -52.02694 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ae219a47-f693-3106-81ba-63ffb5419594 | 3.10519 | -60.60912 | 2026-10-05 04:55:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22b6a156-3f17-3469-bb47-a59ca9f2d2f0 | -1.08257 | -54.11007 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 082fc228-a174-3042-b931-294d323de15c | 1.802 | -55.55027 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6efb3da6-5dbd-3d33-af51-c763de719499 | -0.35112 | -50.36892 | 2026-10-05 04:55:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a7d5238-706e-3be1-a2f3-f83fda6c8054 | -1.10502 | -54.14959 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 81247fa9-47a9-3993-a9f6-52dd6e5cc7fa | -2.10006 | -48.23183 | 2026-10-05 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5833e1e9-c3ae-34ef-8f6b-a03a266a1600 | 1.85137 | -55.82288 | 2026-10-05 04:55:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 378d797d-b809-3c26-a421-6d139d8b19a8 | -1.10626 | -54.14175 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 864dfc47-5fc5-387f-acbb-75525e0d8a05 | -1.19074 | -53.38741 | 2026-10-05 04:55:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90022b66-d467-337d-838c-729a4ffd9c1d | 0.70086 | -51.4349 | 2026-10-05 04:55:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6ac83d7-7289-3896-8f2f-dcad934e2089 | 2.0822 | -50.88653 | 2026-10-05 04:55:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5e33a40-747c-3965-9ddb-ba15a069ce23 | -1.22497 | -54.12383 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eddeb871-cb0c-3a27-bc6c-d5f3902bca2b | 2.09461 | -50.72987 | 2026-10-05 04:55:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95fd0ce0-0610-397b-b388-2dbb853c6f3e | -1.19133 | -53.38374 | 2026-10-05 04:55:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a859d6d-a864-3713-80a2-26a6fb1e82c5 | -0.39405 | -52.03091 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 000c2897-498e-37c8-bb08-f3cb6fdc964d | -1.19607 | -54.21566 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e30b7d43-9bbb-3853-81ed-5412e3ce452a | -1.30991 | -54.22763 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f23015b8-58e8-3dea-812b-e258541c77d7 | -1.05752 | -53.5858 | 2026-10-05 04:55:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7076a392-dc1b-3858-8842-fe9f8c108c36 | 1.85537 | -55.82226 | 2026-10-05 04:55:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1a4e4fd9-d3a4-3618-8226-972c6a9c48dc | 3.10344 | -60.59768 | 2026-10-05 04:55:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df506f35-edc6-3ddf-aa82-9119ce305113 | -1.09656 | -54.11233 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3648cde6-bd31-3eeb-b980-238e8d231561 | -1.08318 | -54.10621 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d8c3dca-c98e-33e4-9d8a-6cf8e84f9eaa | 1.87879 | -55.76202 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2437f974-3ec4-3b77-9bd1-c4ba0f1357fc | -0.24073 | -48.49096 | 2026-10-05 04:55:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2964c14-0ed3-357d-be30-48f3bd06aa27 | 1.87295 | -55.777 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 595ff061-9f10-331a-b874-2a98b611e678 | 0.70032 | -51.43147 | 2026-10-05 04:55:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a305eefc-f5f0-3d91-b4e1-71564052af5d | 1.87268 | -55.80178 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e85b2a5-f163-3951-9669-61e20453c3d2 | -1.10151 | -54.14902 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ff301366-20e8-39e4-9b0a-c469fd5af2c7 | -1.86598 | -50.60799 | 2026-10-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1180f232-a2ad-3658-a30c-89fa74362281 | -0.39183 | -52.02349 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8658bcb8-b4b8-3d8d-84c0-1552924cc281 | 3.35705 | -51.34277 | 2026-10-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f3dfc9f-80a1-3209-90f5-37673d424610 | -1.17717 | -49.25948 | 2026-10-05 04:55:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 20839cf1-806e-3104-bc42-7a9253ade904 | 2.01335 | -50.92529 | 2026-10-05 04:55:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcb382c2-eb7a-300b-9fe8-c248ae02d0bd | -0.39073 | -52.03039 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fbd6291c-9354-34f7-823f-a509e751372e | -0.38188 | -52.04279 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| adae8c4b-b6b2-37db-93dc-a1fb0c1c2181 | -1.08956 | -54.11122 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 621c2475-d587-3a6d-a007-8588b92370e2 | 1.74933 | -55.62514 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f500ba4a-1851-3807-858f-4914e83a47cc | 1.73273 | -55.64836 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5de064c0-215e-3083-93fd-bf960ec05725 | -0.38683 | -52.03294 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 723d038f-e4b3-338c-8611-7879eb1b7232 | -1.14565 | -54.21561 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aeaf033f-7d78-3a88-b8e3-00b3a84242b3 | -0.39681 | -52.03489 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 91e1209e-0cd1-3f9d-b36e-5d5fae092e22 | -1.86654 | -50.60447 | 2026-10-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 63765808-074d-3109-94f2-c0a53f8c0355 | 1.8583 | -55.81469 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1bd8f6b3-f943-3ec1-8ccf-5b734038c928 | 1.80219 | -55.55339 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 209d5f82-0db0-31c0-8f7e-1f444e1da3b4 | 2.07998 | -50.89391 | 2026-10-05 04:55:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b29f9bd-1b3a-393b-aad3-5742a7a92705 | -0.40344 | -52.03593 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39782491-f380-370a-888b-fb86d68f88fe | 1.747 | -55.61012 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b077afc8-3dfc-327f-9982-d5a0da709715 | 1.72879 | -55.64898 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f54d53b0-d058-3792-b7f5-baccaa2f1438 | -1.05693 | -53.58949 | 2026-10-05 04:55:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f67c132-e243-3b13-9abd-d3dbfb83589e | 1.87534 | -55.76608 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26acb954-1bb5-368b-898d-9fa33be05675 | 3.10089 | -60.59797 | 2026-10-05 04:55:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48cf64d8-8a5f-3808-9b9e-dee70fba2b62 | 1.03747 | -50.02289 | 2026-10-05 04:55:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea9b1c62-d9dc-3050-ad20-839e433d8bfe | 1.75332 | -55.59892 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce5bfcd0-a318-35d7-aa19-3cdb6abc8921 | -1.33157 | -54.22717 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5c5b56f-63d9-3ad3-921d-60e4c637aaea | -0.39791 | -52.02798 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8638b3cf-fee1-3d30-a984-1840d15079a5 | 1.87215 | -55.79832 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7327a33-b588-3344-afb1-78bc3ffea621 | 1.60332 | -55.79144 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 375e6483-d48b-31df-bdf6-a3fbd31c1f9d | 1.72562 | -55.65469 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 950faaf7-0e52-386a-a7cf-113974cb5d79 | -0.37911 | -52.03881 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ac92f28-b78d-3972-89e6-d7881e162339 | 3.10256 | -60.60942 | 2026-10-05 04:55:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a911a86-441b-3bd1-8654-f37f9d45c1b2 | -1.19473 | -53.38425 | 2026-10-05 04:55:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| daedfee7-a8c6-3a4c-8bc2-aee45a99bdf9 | 1.86177 | -55.81059 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e4bad84-6c97-3b03-b5e7-30d6f89b5a2b | -0.39295 | -52.03782 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4452398f-2834-3f1a-a0d2-b9e27c597d62 | -0.37966 | -52.03535 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5243bf2-5261-3793-860b-453bc2b1a6c4 | 1.86896 | -55.77765 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f46e2b75-5b21-3921-8dff-636857857a52 | -0.38847 | -52.02258 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 964b8005-850c-33fe-b56a-e3b66ab94669 | 3.10945 | -60.56168 | 2026-10-05 04:55:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 460ca1b6-5938-3e81-8cc9-69992d915970 | -1.09594 | -54.11623 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c39e5eb1-737e-3779-9046-4715fed123fc | 1.82966 | -55.54903 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce787d38-2aea-3fe6-a884-19d314f7d0f8 | 1.83044 | -55.55406 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cdd2627-94b6-34a0-a149-6a2d207aef16 | 2.34659 | -50.75314 | 2026-10-05 04:55:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b7602bb-7679-3891-aca9-9c1a84ccc694 | 3.35428 | -51.34676 | 2026-10-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d525d847-02de-3424-9aa9-301a304b80a3 | -1.09883 | -54.12064 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70c2c72d-944e-3ef5-9910-49780a2c2697 | 2.01059 | -50.92923 | 2026-10-05 04:55:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67281501-acd2-39cd-b461-e4c8e4b1d479 | 1.72245 | -55.66039 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 774cca21-0b35-32dd-b8d5-0229ae76148a | 1.73512 | -55.63765 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd3d0642-4c02-340e-903e-60125f065b1a | 2.3565 | -50.75158 | 2026-10-05 04:55:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2e5c5e2-8b6a-3bcf-b538-5fce459958ac | -0.40122 | -52.0285 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4185a482-4b3b-35a1-93fb-9ebc2d60c913 | -1.10356 | -54.11343 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71b7ea7e-6010-3647-bd8b-b3252e7629d2 | 1.80611 | -55.55276 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0340fd6e-4ca4-3a46-a7cc-220723960ceb | -0.39571 | -52.04179 | 2026-10-05 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a248d033-a185-30aa-ae2f-83437b8d6884 | -1.12045 | -54.1201 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ab87e04-6fc1-3d76-a528-0100f5869d4d | 1.86124 | -55.80712 | 2026-10-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50620ab3-445f-35da-ade6-7ec98cd4be7c | -1.09306 | -54.11177 | 2026-10-05 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffe0ed10-7e62-3783-9752-058a88a16c21 | -5.84907 | -53.4739 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14c71c7b-de10-3805-84cb-805c41c5f126 | -2.97029 | -54.21383 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 864ea77b-4591-37aa-9706-76ab36414f29 | -2.81038 | -54.13487 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b7f2f98-31ce-3d45-bffd-65ce19596e26 | -3.91458 | -49.71509 | 2026-10-05 04:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 11a7d22d-e239-3756-b668-e0652a9c391f | -2.95977 | -54.14628 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| be3a60c0-1c00-3098-acfe-54eeb99d5279 | -3.06055 | -54.17317 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dac82568-9ad0-3f23-9de0-1aaef728e741 | -3.00883 | -57.74667 | 2026-10-05 04:57:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 121b0dc6-4b19-3615-97c4-6cba5aeb93cb | -4.30613 | -50.89788 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fbf4667-5802-30fe-9b51-2a66a0a4ae0f | -2.67532 | -49.02871 | 2026-10-05 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e449f21-bfac-3473-a6b0-beb7107a7471 | -1.47514 | -54.53293 | 2026-10-05 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b0722b5-385f-36a6-a1cf-1669e9fa2ae9 | -6.3291 | -55.32011 | 2026-10-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70bf616a-0c35-3e94-82d2-3bee508e1c94 | -2.78704 | -54.10416 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da1b2db4-59ca-359e-b61a-36e3f3ec9006 | -3.11084 | -53.7263 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab6c25ab-b1d0-3873-8271-f8f2604353a9 | -2.97443 | -54.09849 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3608be6c-409d-32a5-88da-8153c250332a | -3.12053 | -53.70919 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |


[Clique aqui para ver as próximas entradas](README31.md)
