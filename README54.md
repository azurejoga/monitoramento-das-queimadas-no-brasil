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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6b2b8f4-fe88-3733-89c9-a70ecbb1657b | -1.81339 | -52.1674 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8ea32544-5111-3993-8b36-4d1bc3f478ed | -1.45386 | -54.51112 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09ed67c5-8e06-3034-abfe-84392bc5e353 | -2.775 | -54.04322 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ceaaac14-ca0f-30f3-b1ea-c9cb6ebd4e6a | -1.46272 | -51.12028 | 2024-11-23 05:10:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16211f6c-ce72-32f2-b710-96778409e705 | -0.21853 | -51.19016 | 2024-11-23 05:10:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82878db6-ad13-3e52-a803-5e5a80592a0e | -1.18106 | -51.96116 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 63f55d62-1b5c-336e-bc71-9355d20b89aa | -1.65663 | -53.7764 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d2d4991-4361-3622-8480-482e19218d2f | -1.62421 | -53.32143 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e352ff7f-c9bd-328e-91ab-20a760ccf820 | -1.21896 | -51.95372 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dbc2780e-9c6d-3ab3-b4bc-9fc06952c5df | -1.28054 | -54.54216 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d13d3e86-b591-3061-9339-948ee483892d | -1.65247 | -53.77982 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bce5c492-9856-3c6d-9849-8043e5fc0e04 | -1.62406 | -53.31454 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4d2ee8d-04f5-31f2-9008-66f39d5ef47d | -1.43363 | -53.38883 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55495541-db4f-36ac-945c-bb5ce0856a54 | -1.39276 | -55.19793 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aedc6435-adef-3521-b9a5-c271bb42f6a5 | -2.704 | -46.26122 | 2024-11-23 05:10:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df769495-b613-35c1-968f-37025ee99999 | -2.94141 | -48.01543 | 2024-11-23 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 374b246b-6d81-3448-b3d5-7652dbbac1b3 | -1.27109 | -52.98315 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d40f6059-68d2-3547-b11b-1a8bf86e4359 | -2.57553 | -51.88245 | 2024-11-23 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d407403-c230-3819-a9cb-ab6b51fe50a3 | -0.04434 | -51.26046 | 2024-11-23 05:10:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e409e740-1dc7-3504-ab2a-6f70263aabfd | -1.61422 | -55.72058 | 2024-11-23 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b8b2a4c-20a6-363d-b9fb-17a8ef91bd37 | -1.50078 | -51.97791 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ef04fea-c1f3-345d-aa31-ec9bb6664fc9 | -2.01049 | -48.10047 | 2024-11-23 05:10:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a815452-79db-3313-a168-0f5f1942bd42 | -1.22663 | -51.79794 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 17bd44d5-1fca-3381-b7ea-db00428c169f | -0.57028 | -51.72868 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e8402a8-7b90-3db4-a48b-e0e3f49d9da3 | -2.39682 | -48.99995 | 2024-11-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 73791540-856e-366e-a736-b19c410806fb | -2.76903 | -54.05856 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8feee48f-85e9-333f-b119-88b9969a6728 | -1.61969 | -52.60577 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 93dc80a3-f94c-3794-8e84-887f594b017b | -2.13492 | -46.4032 | 2024-11-23 05:10:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e8ca87fa-2e2a-3f28-93df-f020a1a60560 | -2.76367 | -54.06991 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42ed0c67-3d36-3d75-b860-c8bac837a73f | -1.92939 | -52.08546 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b5f414d-b62f-3947-9739-63d1c63d5f61 | -1.98944 | -53.13404 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71d9b6f7-65bc-3936-a79c-607a8da7b57e | -2.599 | -54.05778 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f312eddf-8d45-3fbf-ad51-05fea618b282 | -1.62277 | -52.58097 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 56219fed-681c-35fb-88f0-20736488e1f4 | -1.20042 | -51.97088 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5136dbe8-2254-31dc-950f-d7094778b230 | -1.1949 | -51.77089 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c33a333a-d515-3e94-9026-8cc963f8ef2c | -2.08802 | -46.28395 | 2024-11-23 05:10:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07f29c8e-43e0-3ab1-9176-b071dff4cc35 | -2.44806 | -49.08015 | 2024-11-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 85409e2a-9410-3ba6-90e3-b7e8821f1c2d | -1.60554 | -52.26408 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bce211aa-f137-3202-80bc-899a5bc173f4 | -2.01697 | -51.17516 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb09d55b-3d6b-3b66-89ec-e5bb62aedecf | -0.2174 | -51.19045 | 2024-11-23 05:10:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45fde98d-cdf2-3fc8-bb2f-51e283ea7485 | -1.60147 | -52.2391 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f894bd0-feee-3aba-acff-a42d248dd0ef | -1.57642 | -54.31083 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03ae4cd1-0630-301b-a6c3-b7b67ba6cee4 | -1.22407 | -51.73935 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6b171b4a-d12c-319c-b888-2bd12991c762 | -1.60864 | -52.59742 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8b4f6781-79ce-3f13-97dc-7827e54401a3 | -2.15726 | -50.45995 | 2024-11-23 05:10:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 774e057a-0831-3c6a-afa1-7922acf63659 | 0.59648 | -60.46703 | 2024-11-23 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 4b2bd9e4-7ab3-303a-8ddb-e85afb28184d | -1.20588 | -51.74842 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f149086b-874b-320a-bb3e-11fe8917b858 | -2.76577 | -48.60549 | 2024-11-23 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf3338aa-4d9c-3393-ad4a-951d242a01a4 | 1.3298 | -60.71538 | 2024-11-23 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd5c793e-1d3d-382f-a1aa-e780d5f93f24 | -1.7247 | -52.7305 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| af357cd3-b771-303f-8f4f-61d5522dc14a | -2.13004 | -46.40571 | 2024-11-23 05:10:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2007eb02-2a82-396a-884c-7e224f1cefa5 | -2.62196 | -54.04923 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c09b8142-9381-346c-9134-30a441adb400 | -0.93297 | -53.20823 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57db47fb-1623-3a40-ad72-9380dc1b6055 | -1.94881 | -49.52586 | 2024-11-23 05:10:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 680bb24d-5c9e-3481-8bcf-97673e07dc6c | -2.1635 | -54.45935 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c0ae9e45-aa4f-36d6-837b-5b0064ded0d9 | -1.14422 | -51.68034 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f36d6b38-241e-39f0-9122-a690f9fd82ad | -1.43489 | -53.38061 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da2d3a42-74eb-3353-a965-dc137240d8cd | -1.24465 | -51.78534 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f85fe17a-9dae-3490-a628-910ce87620c6 | -2.23809 | -53.61924 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99d223cc-121e-316c-b8f2-da7b95657706 | -1.63062 | -52.68619 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38732301-d652-3de7-9f5a-baaf3fac47a1 | -2.58279 | -54.04371 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09c97fb0-98a6-3b5e-916e-f77216fc9fac | -1.7781 | -53.62572 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fb21f1bf-f493-3682-942f-5ed197b55168 | -2.69753 | -46.26445 | 2024-11-23 05:10:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b82620f-645e-3b9b-b5c5-322837c37236 | -1.78753 | -53.63545 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b3ab2a91-d092-3bb0-8d63-4d5ada2ec078 | -1.26031 | -51.76206 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| df792dd9-a033-3417-8ef5-2689ebe58935 | -2.70209 | -46.27377 | 2024-11-23 05:10:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb1014b2-4668-3c4f-9943-35ff6417f485 | -2.70621 | -51.9942 | 2024-11-23 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a628ab37-642d-3ac4-8155-eb8c8e33f7b6 | -2.55629 | -54.05169 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| df6a530a-a9a9-3351-a66a-b84803d434d4 | -1.11785 | -53.39469 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 86b2fc0a-ac0c-3785-8216-0c06b7389a91 | -1.38996 | -55.19387 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04cf2937-81bc-36af-8ada-43a1c7cbf0ab | -1.62833 | -53.31092 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4c7dd5a-3d91-3878-aab5-00cca5329324 | -1.42029 | -52.817 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b49b3e2-1004-3052-9aac-f6a4fdc8d2ab | -0.76434 | -51.74781 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e5adfdf-b51a-3a82-8989-29960ea3c952 | -0.04708 | -50.81741 | 2024-11-23 05:10:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a2b1861-9737-3ea9-bf73-dcffaa241351 | -1.84942 | -53.7015 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b4e2082d-b5d4-3b82-95c6-1409f13ac70a | -0.9907 | -51.76584 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5cd3e7ea-068b-3b8c-b480-570da0e8f160 | -0.36599 | -51.56765 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 220359c5-d299-3e50-88d5-e387e21e7ce4 | 1.36913 | -55.93912 | 2024-11-23 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9d66aa9-289e-370b-977a-baee52eba687 | -2.71991 | -54.14388 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2db3254-640f-3f99-ad76-3e3bb676889e | -1.12375 | -53.40395 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 08fd63e9-cb89-3024-a374-1300c2d21b96 | -2.78848 | -51.41035 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5b7271d-2dfb-360c-96e9-47167b8a07e1 | -1.78627 | -53.64352 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 68309bfa-1183-3560-baf6-30d4c208eaa0 | -1.25751 | -53.36021 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb916291-1b2b-30df-b33e-285d47e73b3b | -0.93604 | -47.55534 | 2024-11-23 05:10:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13d3c909-4704-3f07-88e0-01cf06e382d9 | -2.4611 | -53.70188 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3dc36cd8-78bb-3a4e-b0f3-0c2846370c3f | -1.45442 | -54.50747 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69246a85-70fc-37ea-b54e-e91677a3c0db | -1.05053 | -51.74185 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 745075d5-85fc-39b3-8390-8145610ec476 | -2.43424 | -49.37339 | 2024-11-23 05:10:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76c4f643-bf24-32a7-bdb4-6de2c808e05b | -1.11364 | -53.39824 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| cfcfe311-b3e4-33f4-ab8b-d26a0e8cdbff | -1.77769 | -53.6049 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ae3aa8b2-47e1-31d5-981d-b7f00ffe5aaa | -2.49963 | -49.00132 | 2024-11-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8dcb0c4b-04fa-3493-92f7-69e7af3b2f43 | -2.5996 | -54.05385 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3395b639-ba88-3c96-9981-9961daf2f08b | -2.37094 | -50.39008 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 828dcfe5-6b40-3bd9-934c-ac417698ef84 | -1.21922 | -51.7402 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c5fbb4ef-b9d6-3c33-b47b-7b98435a156a | -1.656 | -53.78038 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ade79651-7d0b-3a2c-b529-44facccfbb56 | -1.85004 | -53.69748 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 25d5e4a6-1c39-3ebd-b67c-b178a1171fce | -2.74267 | -47.54104 | 2024-11-23 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e1b2cc1-50fb-3d14-b0d1-2ec1deb65677 | -1.89631 | -53.32608 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 300f479c-54db-3ca2-ac2e-f7a05f5827b4 | -2.70638 | -46.28022 | 2024-11-23 05:10:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 05e26519-bb07-3282-a166-5a2941f02d42 | -1.61453 | -52.58436 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README55.md)
