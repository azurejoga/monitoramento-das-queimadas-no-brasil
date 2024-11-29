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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c6c4b3d-1eb9-341f-9672-b735d2db3df4 | -3.12239 | -53.26194 | 2024-11-29 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c4589bcf-f3b2-30e8-a1e8-ad42eaeb6175 | -3.0407 | -50.97799 | 2024-11-29 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 899d69e9-b474-3338-b516-648ae23953c4 | -2.57844 | -49.995 | 2024-11-29 05:44:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 907967b3-03ee-3bd8-a7f3-b16341350b0d | -3.26905 | -49.89277 | 2024-11-29 05:44:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| b95e3568-21ac-31ae-a582-46f51e635ded | -2.96117 | -53.72012 | 2024-11-29 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 45f3b9b5-1321-303d-a61b-720b40f35310 | -3.05622 | -54.04425 | 2024-11-29 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 64c9eeff-9254-3898-a753-8bb5e09d5a4d | -3.38854 | -54.28328 | 2024-11-29 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b8a00293-bc9f-3cfd-b463-c1d0969c388c | -2.72097 | -48.66609 | 2024-11-29 05:44:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c255cc10-e366-3ee5-a853-0ad95c0989b2 | -2.96338 | -53.71363 | 2024-11-29 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 03f99046-dcc6-314e-b57f-c64e5b93da32 | -3.30493 | -50.74939 | 2024-11-29 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| db4aef30-483f-3faa-8d1c-1fa90b7c23a1 | -4.47083 | -44.56074 | 2024-11-29 05:44:00 | AQUA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 33c608c8-1a49-30b2-9e13-887818449dc8 | -2.97676 | -53.28945 | 2024-11-29 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 183.5 |
| 845227bd-9d78-35e4-b4bb-c7b254056093 | -3.95984 | -48.09091 | 2024-11-29 05:44:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 83aed25b-e595-3db6-b599-128d91859fd5 | -3.67921 | -54.44314 | 2024-11-29 05:44:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e366313d-6302-3c6a-a16b-92263f2a5259 | -3.57135 | -53.02293 | 2024-11-29 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cc666e73-2038-3153-a15d-24fa29a053bb | -4.11162 | -50.97681 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c776321c-4705-3bf1-8bf4-dbab5f531191 | -2.26306 | -53.46073 | 2024-11-29 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 111b5682-f1d4-3c27-a5bb-b9905df16523 | -2.70178 | -51.9971 | 2024-11-29 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9473a1cf-2f82-3e19-9b4c-406e625ba6ab | -3.27037 | -49.88391 | 2024-11-29 05:44:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d5317718-59ab-397f-8eb3-e7ba168ee2a6 | -0.26676 | -51.62552 | 2024-11-29 05:44:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e9f60f33-842d-38a9-923f-93c003bc44fa | -2.25334 | -53.75223 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 686d96b5-fbd0-3427-a990-1ed2d8ffa1de | -1.9392 | -52.96242 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad44afc5-461c-327b-987f-7860678794f3 | -1.24354 | -53.35745 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf8a3f62-6251-3ba9-aded-d7229fc5efba | -0.26565 | -51.63256 | 2024-11-29 05:44:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a855418-7f7e-3172-b540-004ec8d3df79 | -1.06899 | -53.63597 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 696f0870-db62-382b-b158-72264fb18c0d | 1.28056 | -55.91826 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75e7ecbb-c0b8-3c00-ac99-6207a7d7b4ce | 1.22391 | -55.94083 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7fd30abb-6004-3230-bf39-0e379c7bd18c | -2.58317 | -54.24768 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d69376dc-08c8-39e6-8d55-9a4ef6947391 | -1.21367 | -53.55497 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 863a5fc8-cc73-31f7-a54f-7c329ccf7626 | -1.20232 | -53.71653 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 955d438a-275b-312c-9906-792180431369 | 1.22022 | -55.95177 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7dc16157-e9cb-3d58-beb0-ec1f3827e068 | -1.68602 | -52.43581 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5621aa5f-6517-30d3-8965-85f7c99f62f1 | -1.60608 | -55.43087 | 2024-11-29 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88586f7b-9593-3ff0-8829-57e347cc041f | -1.24391 | -53.36181 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a3fdd1f-e857-381e-b3dc-bf51da132eea | -1.10137 | -54.12818 | 2024-11-29 05:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 711f4055-858b-30e8-b5c4-a3e35ee7b35e | -1.4328 | -55.24333 | 2024-11-29 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5369e3fb-2a3f-3d9d-85a7-c5b913ae39af | -1.62532 | -52.37124 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60c7e747-8af9-322c-a9bf-dc967c01b5d7 | -1.68693 | -52.43419 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2dc9eb9e-7d1e-3f8c-97c0-8c94b82e8794 | -1.47646 | -52.6568 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbf94123-769f-3b77-b6d1-f8dda628311f | -1.94598 | -52.96333 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69e0a67c-c26b-354b-9ad7-6238575ba3e7 | -1.58928 | -52.27755 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 872f8705-3158-33d8-a04d-b959eebaae8c | -1.30352 | -55.74565 | 2024-11-29 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b064de4-08ea-375b-ae13-ab6e36c8cc3a | -1.58059 | -53.84424 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 585b32a0-45a6-31b6-b77a-9a1d8c670231 | -1.56294 | -55.78901 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8a82602-2212-3890-ab50-f84fd0422512 | -1.72084 | -52.48782 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d437f303-24e5-3220-b1c8-d4dbef6855f9 | 1.20501 | -55.99228 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 59f40bcf-2d49-3c95-a475-e1bfcff83727 | -1.60312 | -52.2936 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5c218cb0-ce1f-3720-ad5b-79a040217db1 | -1.69895 | -52.44448 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 64efdbee-cf5e-330f-b98d-c82c5d9cba96 | -1.89212 | -54.54252 | 2024-11-29 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32a22aed-c188-30f6-abd5-1d05496a6e48 | -1.27093 | -52.20192 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 573717e0-22cc-32f1-9a8f-c8931f0305c3 | -1.21535 | -53.7596 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1b7122b7-4371-3d97-b4e2-686e8ac23001 | -1.43216 | -55.24749 | 2024-11-29 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f735d9be-a1ce-3fd8-84af-856696010428 | -1.58167 | -53.84864 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| ab3e00f2-11ed-30d3-acef-a609edcdb5ee | -1.89137 | -54.54737 | 2024-11-29 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ceb51c34-2419-3f88-b224-a293cbad0bdb | -1.49497 | -52.44316 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d83b7adf-3270-39e5-ab2e-71a4bdddd86c | -1.60095 | -55.42579 | 2024-11-29 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ce6c24f-c647-3b0d-917d-da4afccc8340 | -1.92141 | -52.88474 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51d8fabb-b79e-37c1-849c-93cc8ce94822 | -0.56521 | -51.70007 | 2024-11-29 05:44:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8102db7c-3656-3204-98d7-eea5a05fb8fd | 1.20865 | -55.98119 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89ccdbc4-d19e-3101-b256-fc8560fb3989 | -1.09743 | -54.12528 | 2024-11-29 05:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6dfcd029-5dca-3bda-b053-2ab23f288c31 | -1.08029 | -53.63825 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b6d9dec-c21b-3144-902c-f400dfc18359 | 1.21488 | -55.95259 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5a2b0ab9-2e81-3d61-980e-e30413aa6ef2 | -1.52569 | -55.37441 | 2024-11-29 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d3cf933-19ab-34fd-9e3f-1245e20c815c | -1.56238 | -55.79266 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63e993b6-0f21-3f4b-bba6-d06d1c9827c6 | -1.58697 | -53.84525 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 42cb127b-a446-31e5-977c-5235bc084367 | -1.30056 | -55.74402 | 2024-11-29 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d6493e38-4c7c-3c68-ad71-a31ca0fc5664 | 1.23405 | -55.93585 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ac134b6-94ff-34a0-9946-526135e1cad4 | -1.71282 | -52.77158 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b3627088-c1a1-3b3d-91ff-8678274e1030 | 1.21202 | -55.95747 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9aa240d2-353a-35ff-9f6f-b99f707936c3 | -1.62387 | -53.87176 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03705efb-dd4b-3560-84ef-12e4fb73fe43 | -0.14196 | -60.86699 | 2024-11-29 05:44:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02665c99-be8b-3344-b89d-c067bd58107a | -1.26392 | -52.20085 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5730803e-4b7a-3b9b-9065-971ce7109a5a | 1.21064 | -55.96014 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b99bbb95-31a1-3d32-b46f-daaf906056fa | -1.25748 | -54.54557 | 2024-11-29 05:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfc37613-c962-38c6-b4fd-9e71787e2933 | -1.25178 | -54.54687 | 2024-11-29 05:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9911e30-0a19-3ddd-a026-4b3fff2a710e | -1.59118 | -52.27818 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 03a2084e-b4f2-3190-9f06-c27cbfe451d5 | -1.30621 | -55.74476 | 2024-11-29 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4374b86e-09c6-327b-830b-575715e71f68 | -1.92285 | -52.88528 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 747ef6ec-6042-3835-b87d-6864b191f2c0 | -1.29997 | -55.74777 | 2024-11-29 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 37c97232-af85-342f-bebb-64b3b0cc1674 | -1.66338 | -53.78442 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbf8dec3-270a-3742-94cc-a80864e6fae0 | 1.28698 | -55.92419 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09635c4b-c532-31c5-b801-a2d52f2aff3a | 1.21967 | -55.94839 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9ed97c7a-91f7-36b1-8938-f209241d7317 | -1.89148 | -54.54467 | 2024-11-29 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 65826ef0-b3f0-3932-b3f5-4e1e8842260c | -1.29788 | -55.74483 | 2024-11-29 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35333fcc-5d94-38a6-be15-d60b15720e3e | 4.39819 | -60.74498 | 2024-11-29 05:44:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ee59244-5058-39a5-afdd-80eb2820845c | -1.53024 | -52.67146 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e633a588-0973-3007-a579-2f4ca7665e69 | -1.42128 | -55.27951 | 2024-11-29 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| edb6aa05-44d7-3965-9646-69e92499609a | 1.20809 | -55.97781 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a9ec785-9107-3e67-97be-9a3833432fd8 | -1.69797 | -52.451 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ac1c36ec-9c62-3379-bc76-ec6eeda3d5b1 | -1.21936 | -53.55865 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 83d2ad19-480e-368a-9a83-4163e2a61153 | -1.3591 | -54.6562 | 2024-11-29 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e075c86c-0963-3360-8d56-a215ba7bac72 | -1.16221 | -53.58591 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e4db716a-944d-34b1-9b10-379d6c588c94 | -1.29845 | -55.74107 | 2024-11-29 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5fc778e7-51bd-3b9a-b904-520ed0e3e2a9 | -1.20041 | -53.71921 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aaa2ee21-350b-38b5-ada1-3df0372ad1c9 | -1.22019 | -53.55342 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f15b2547-75eb-3043-8716-eafab648ae3b | -1.06755 | -53.63568 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c1cbe320-7c44-3d6a-bad8-1d6974cf3c31 | -1.91464 | -52.88361 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92a55168-61bf-32eb-9b87-1c9c34835c05 | -1.71251 | -52.49776 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5bd26c05-b35e-3817-8b63-6ab25f563ac1 | -1.53089 | -52.6717 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e8255fe5-358e-3c4d-ab4c-00f850e326d6 | 0.59812 | -60.46701 | 2024-11-29 05:44:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README104.md)
