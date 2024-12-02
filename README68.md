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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f1e491a-fe99-39eb-869c-cf7a56569657 | -1.01086 | -51.73109 | 2024-12-02 04:48:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 021ec9fe-acb8-3e50-93b0-eff07791239a | -4.19137 | -50.6852 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2702f384-d153-3974-b476-a417f0ffddf9 | -3.12057 | -53.98766 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97be1a6f-83db-3155-9d65-eb91ed2f2ccc | -2.93276 | -54.3261 | 2024-12-02 04:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 801e4c82-328f-3633-8411-2003c30f3d02 | -2.59483 | -53.96589 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3db40fc-046e-3762-b9ed-d5b94c61ef53 | -4.36664 | -50.73413 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2bfa6ed-5ba8-3b8e-acc5-f93cbed69814 | -1.10787 | -53.59243 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52f5c0c7-76ab-3ac1-8790-360b814f5e1f | -3.25844 | -53.86996 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b5fe031-14d7-385c-ac13-57ba2daea598 | -4.03288 | -51.02686 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cb41793-f26f-314e-b6c1-d8b8053c63f4 | -1.53531 | -51.20457 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dabb8836-5bac-3935-a5ef-66ce68c89bb0 | -1.61854 | -53.88912 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c63f8832-f8f9-367f-a83c-541c58cfb5cb | -4.27682 | -50.70219 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a200f8b-c0a7-3e48-893a-24e0ae256697 | -2.76805 | -48.56966 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 458ede45-1fd0-3503-b022-d33301b984f5 | -2.04688 | -51.19324 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78f73148-2298-3c40-a7a4-8bfcc186473a | -1.57234 | -55.3351 | 2024-12-02 04:48:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e68a316d-00d0-35c4-b964-1ec9dc054ee6 | -2.60103 | -54.22755 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 588cdfce-b630-3b85-b188-14c20e4fc890 | -3.70763 | -52.18987 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99ff7419-28ca-335c-b94e-64b72ccdb50c | -2.66592 | -46.09706 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c804d55-8e96-3d0f-859e-2aeea8dc8ae0 | -1.63035 | -53.85958 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0b51867-6969-3a28-91d9-9452bb2d43d4 | -2.56233 | -53.39631 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b1847d5-17dd-32fc-9860-59f9e9e260f3 | -2.44704 | -49.30923 | 2024-12-02 04:48:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27e0ba87-b997-3989-a945-8a020584b18d | -3.09273 | -51.26133 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80d860de-e904-377b-9c8b-b44a722638f0 | -3.26245 | -53.64632 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0e282bd-c06b-384e-b23f-45955b476b15 | -0.13461 | -51.492 | 2024-12-02 04:48:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a851d393-0164-3ff5-a816-0718d02d0840 | -2.44105 | -53.63056 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b5742ba5-6c81-3ee5-9394-50e9dea880dd | -3.62371 | -51.53498 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5a8b375-6c55-3b92-8a73-cb13d08af850 | -1.51751 | -51.14552 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd8bbff4-284c-356b-b6b0-af8c9e4426e4 | -2.86561 | -54.02297 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49abaeb4-64e5-3b74-97fd-927b9bad91c0 | -3.08966 | -53.71864 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd458a22-ce23-3a80-82d1-0bac0fef7e56 | -5.58593 | -45.14608 | 2024-12-02 04:48:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 9d984617-cda2-3902-867e-aec5337f1a4e | -1.44018 | -53.39762 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7c35eee-acb2-3640-bd54-f63a5c65b989 | -1.99298 | -46.45895 | 2024-12-02 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0391afa9-fee6-31df-9780-334ac3d7250a | 1.12984 | -55.98951 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 701ff84a-4173-33d8-a0a5-7b9351b1f020 | -3.26621 | -51.10741 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f43734dc-f1ff-31b7-a610-06ba0b75560e | -1.43743 | -55.22963 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e66e3557-4f46-3640-a596-5ec6e02afda6 | -2.56343 | -54.34735 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 89af9081-3f55-303c-863a-81b6e4aceb82 | -3.2543 | -50.57826 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 59d05a48-a9d8-368d-bbaf-592de83e7dcb | -1.58979 | -51.24862 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f615ee9-02d0-3801-a809-bba7809a373c | -3.10401 | -49.45718 | 2024-12-02 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb708537-c923-370e-ac70-c0c852134dbc | -2.82786 | -54.09192 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88ff72d6-2b8f-3541-8c92-338294dfdf8a | -3.81675 | -52.08043 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3a961f7-b181-36d5-91d6-081824d3af52 | -3.02382 | -54.02385 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2da41b69-e953-3fdf-b1f7-fb7697efc3db | -2.11539 | -50.34147 | 2024-12-02 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9ce84b5-f846-3ed1-b863-68b660f99bda | -4.33726 | -50.40195 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4004e2fe-db34-3838-957e-986679159909 | -1.36326 | -53.64339 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8f0bc8cc-6895-3db9-a821-deeb45d34353 | -3.53803 | -51.49687 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 822340e5-6335-3e87-80b6-ac44b20e1dc8 | -1.2677 | -51.634 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dedf268-e5a1-3903-86a0-6cb2e10f8519 | -1.28266 | -51.668 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94b31cdb-94db-3f22-a25f-b96eb9c82860 | -3.12488 | -51.12103 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fbfc991-8346-3f05-95e2-37a8dd463dc4 | -3.13946 | -48.53699 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87a8ece4-9044-3714-89cd-8d29e772945f | -3.33863 | -50.24676 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e288029c-1b98-3ece-b519-cd32e7df4778 | -3.46322 | -53.88273 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da8e74db-2240-3b70-8896-7605d81ed031 | -3.32761 | -50.02183 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5c4ac8f-28aa-3a06-bd86-98fea1036027 | -3.25104 | -53.65206 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d9edbd9-b8c0-3c8d-b213-a8eb39eff4a5 | -3.05545 | -48.5285 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05b4a0c1-fe94-306b-a9c4-d95780792e5c | -3.36186 | -51.12613 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6a0bc7c-47b3-3d5c-b1e6-50f169c57c38 | -1.31849 | -51.67709 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed7fdfba-ab85-3f17-ada4-5e36deab8c75 | -1.31903 | -51.67365 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f5f89ea-6824-351a-9374-b1d08846ea3b | -1.6943 | -52.43832 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a34a5d1-9896-3ecc-8bc7-e45eaf2b69c9 | -4.5569 | -45.71979 | 2024-12-02 04:48:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7073ef96-1f68-32e1-9fcd-c8479b45d815 | -1.56858 | -55.3345 | 2024-12-02 04:48:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8689d4d-39a4-316e-9f89-4d739f517431 | -2.37453 | -53.8279 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c007f0c7-f7c6-3d85-87d9-7c1d643d0c46 | -3.19333 | -46.58341 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 001adad2-00a2-3e4e-8052-b2d6c1b85cf5 | -2.53621 | -53.97643 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1b03bc0b-37f7-30f1-9bcf-ea3122c1e3a4 | -1.37489 | -52.39611 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e09d1ae4-d266-3853-80e0-13dc42b52835 | -3.30747 | -46.40477 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd5ce3e9-b699-394f-ae0d-6196bbe7f88a | -0.63821 | -53.44092 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3d06c9e-664f-3f85-802a-37d5910b2e6c | -3.65413 | -50.22399 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2ff55fa-6342-3c3f-8b81-f023e229a2ca | -3.66881 | -50.19633 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ce0c56ca-3013-34df-a5a3-4d0e269bb948 | -3.02547 | -54.03583 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b79bf704-2f7e-364b-98b7-dfffb4b732ff | -3.79578 | -49.94091 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fbafca6-bfee-3baf-835b-f0fb03b57c90 | -2.45251 | -53.62477 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cfab5fdd-9c37-3fcc-93ff-260931fa83c0 | -3.30372 | -51.10644 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 052320c3-7bd6-32f8-b126-7a2d88fcc154 | -1.08189 | -53.22496 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14f62b7a-8f4e-3bd3-89e5-1ab6b95a1faa | -2.27451 | -53.77394 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d8735a38-8b1b-3bec-bfd4-d1e8aab6894f | -1.3218 | -51.6776 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1627ef9-7bfc-3738-b194-e64e3528babd | -1.68228 | -53.94597 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1d67442-05bc-3ae2-abb9-48e2fcdeceff | -2.98339 | -51.45929 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 514ad57c-f438-3ecd-a14c-40fc867191ac | -3.12881 | -45.98352 | 2024-12-02 04:48:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b0c0148-0eb8-3817-8f3f-53b00aaf7752 | -4.55708 | -45.72106 | 2024-12-02 04:48:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f163eb41-40c7-3fac-9761-47f886607d66 | -4.18409 | -53.84927 | 2024-12-02 04:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e2e4afd-e7d8-381f-bb4e-aeeb53146a98 | -3.6919 | -47.11873 | 2024-12-02 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a5900940-fa2e-3b23-a13f-be1bb4f234e8 | -3.39167 | -53.26887 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d99333d4-8e22-33d3-980f-46999e798176 | -3.43805 | -49.73837 | 2024-12-02 04:48:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd377f08-b4da-3af2-8d60-9110f966e71d | -1.26787 | -55.7074 | 2024-12-02 04:48:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f81db09-7804-3704-ad59-d4a1b04077fa | -4.06796 | -51.06041 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 87ab03c2-e2f9-3d2f-a002-5c5d212145af | -3.02156 | -54.0157 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4848720a-02c4-3cdd-bdee-f0a8c8ecfc8a | -2.52781 | -54.00657 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b0570d1a-d0db-3825-9634-6c8f7593a413 | -3.29644 | -53.67444 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42c237a8-e85d-3f7c-af2e-7f04475ae03b | -3.40697 | -50.00734 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce211494-b59d-3153-97a4-27f58b6aaaba | -3.78936 | -52.4044 | 2024-12-02 04:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 954d004b-972a-3030-9b98-de06d8de3232 | -2.59235 | -45.65044 | 2024-12-02 04:48:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 049de06c-62f3-378b-8c48-188475b72b07 | -3.33414 | -53.37052 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb250c2b-47ea-368c-98ab-cbe74984ff2d | -4.08638 | -46.13882 | 2024-12-02 04:48:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eca927a2-bb06-3135-ae5b-eb9b4e28046f | -2.44671 | -48.44782 | 2024-12-02 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe399211-3e7a-35a9-883b-022280161fb0 | -2.79332 | -54.12988 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4cbc6e99-6467-3787-b326-9113049bf91c | -2.38797 | -54.35825 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41c99a6e-96f1-3510-a3fd-9f49dc991eae | -1.17311 | -53.42507 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13a1d317-3182-3b57-b3db-f35940a69ecc | -2.72463 | -45.07519 | 2024-12-02 04:48:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35dc3d94-b35e-38b9-b9b6-ce731f444759 | -1.45467 | -53.5956 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README69.md)
