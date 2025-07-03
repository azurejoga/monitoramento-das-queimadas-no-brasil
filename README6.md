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
| 39dfb154-3563-395a-8c8e-7455b0793648 | -14.6291 | -53.8809 | 2025-07-03 02:50:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 78613b1d-d8dd-306e-9bac-e946ce3591ac | -7.2219 | -43.0682 | 2025-07-03 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 125.6 |
| f340e33f-25ad-3823-b7c4-00301256de26 | -6.2945 | -43.6659 | 2025-07-03 02:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| a888300c-0656-3710-bad6-0cdea65c4a5b | -7.2222 | -43.0447 | 2025-07-03 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| 18dfeb30-557e-37f5-86d9-1df7fbf3533c | -6.9416 | -42.8834 | 2025-07-03 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 200.4 |
| 1c4fb9e7-24c8-30a5-a6f4-b492bd8d5634 | -6.9602 | -42.9052 | 2025-07-03 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.3 |
| e12d7392-787d-3676-b9d5-a36fbc86a060 | -7.2408 | -43.0664 | 2025-07-03 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 1491c0c3-63c0-32a5-8094-eebf1121ee98 | -17.76043 | -39.66002 | 2025-07-03 02:56:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7d16c9ef-4a1f-38b9-9b2d-008a4137d02b | -17.75344 | -39.65813 | 2025-07-03 02:56:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 60af1bf7-8565-35f6-a67c-077d06c1edcb | -6.9602 | -42.9052 | 2025-07-03 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 114.0 |
| 4ec19f2b-a151-3b21-8c4d-f130207709e6 | -7.2222 | -43.0447 | 2025-07-03 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.1 |
| 00a36d16-e1f0-3e92-9293-fa9f20d56107 | -14.6291 | -53.8809 | 2025-07-03 03:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| f647a8a7-0c9a-3b64-8394-fdc4dc673a9c | -6.9605 | -42.8816 | 2025-07-03 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 389.3 |
| b381963b-1b67-3a0b-89c1-ff857a4a9d2e | -6.1792 | -48.0494 | 2025-07-03 03:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 23b44891-a157-36b4-9b96-5b7726859843 | -6.9607 | -42.858 | 2025-07-03 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.6 |
| 5c1e9bea-be80-37b2-b2e3-b60d6a96dde4 | -7.2219 | -43.0682 | 2025-07-03 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 126.9 |
| 13e05fb6-32b4-3b1a-829a-2c478c6bedd3 | -18.22 | -51.3446 | 2025-07-03 03:00:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 690b4f57-15dd-308a-84f0-abca912dce1d | -6.9416 | -42.8834 | 2025-07-03 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 146.0 |
| 9d03e16c-898e-3262-80a9-64b0686413f6 | -6.9793 | -42.8798 | 2025-07-03 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.0 |
| 38e6bad0-d13f-35ab-82ca-3492fd14669a | -7.2408 | -43.0664 | 2025-07-03 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 4e0bf7a5-fec0-310b-a0aa-adb3b15d889e | -7.2408 | -43.0664 | 2025-07-03 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.8 |
| 0173a191-ea11-3960-9639-e5627a49aadf | -6.9793 | -42.8798 | 2025-07-03 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.8 |
| 4975a2f2-f5bf-3a3d-b7ef-7cf3ef85af55 | -6.9602 | -42.9052 | 2025-07-03 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.3 |
| ef85c743-76b3-34cc-8885-fd4e52f1fb6d | -14.6291 | -53.8809 | 2025-07-03 03:10:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| bbbf28f5-1d87-350d-ab82-4fcc78fb681e | -7.2222 | -43.0447 | 2025-07-03 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| f832806b-9064-3e2e-9183-4d955887a975 | -6.1792 | -48.0494 | 2025-07-03 03:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 336dca77-1e09-38f5-9320-3abc5ad625db | -18.2 | -51.3481 | 2025-07-03 03:10:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 213acf46-1200-3d7c-9050-26fd4022bf02 | -6.9416 | -42.8834 | 2025-07-03 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 202.6 |
| 8945d48a-10ff-3508-b8f4-2cb20e2f3840 | -18.22 | -51.3446 | 2025-07-03 03:10:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 5a156367-fa3a-36c0-91bc-3a246544b03c | -6.9605 | -42.8816 | 2025-07-03 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 364.2 |
| 6f71591d-13ef-3828-a10e-30264f80df81 | -7.2219 | -43.0682 | 2025-07-03 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 122.8 |
| 34365ecf-a8ad-3972-b367-6acb8c2a8dcf | -6.94866 | -42.8872 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| 5dee28a6-6834-3a62-bac6-4849e87fb520 | -6.95183 | -42.88823 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 49.2 |
| 5e3b66dc-f8bf-3fb8-86fd-e3f00b0fb965 | -6.94601 | -42.88026 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 36.2 |
| a7ef2cd3-7aa4-39fd-9852-b552edee87e7 | -6.95438 | -42.89546 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 8f947e3a-5581-3337-a8bf-85a86abe6841 | -7.22198 | -43.07098 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 9d8dd4d0-ae21-3a74-98ed-b18485980d29 | -6.95132 | -42.8736 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| b0aec294-0da8-3072-834d-022f34c95717 | -6.96276 | -42.89005 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 33.6 |
| 35ff8f68-9f9b-35da-a31f-ea43af3f14fb | -7.22333 | -43.06391 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 39d29c81-78db-3ada-b4e3-42472a939393 | -7.23359 | -43.0675 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 9c25cc03-ac49-3c73-a7e2-3a0afd22146e | -6.18017 | -42.61379 | 2025-07-03 03:15:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 25eb40e5-966f-3d5e-9dbd-14265c8ad7a7 | -7.95122 | -37.18269 | 2025-07-03 03:15:00 | NOAA-20 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fbc622f2-17d0-3a83-bd62-e41640c445a2 | -7.23045 | -43.0652 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 31a43d98-3bab-36f8-aca6-be0f9c8b6f53 | -6.19486 | -42.65318 | 2025-07-03 03:15:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b32e62ff-082c-3543-af1a-d016c695f325 | -6.94999 | -42.88039 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| 4fd1fff6-98c5-3f6e-90c3-18322300b8ce | -7.19388 | -43.10212 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 7b5d7be6-3471-3471-888f-6e1207194792 | -7.2322 | -43.07456 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| b7ce43d7-3c69-3ea1-8920-e669e697d890 | -6.96718 | -42.88444 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 35.0 |
| f4b1d548-2f40-346f-bd4a-5373f768a043 | -7.21755 | -43.05563 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 656eb2f5-3bc8-3779-bf52-d7b457b8d4b0 | -10.69499 | -37.05057 | 2025-07-03 03:15:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 323101c5-ad33-3a50-8a75-d566c1339e48 | -6.96589 | -42.89131 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 30.3 |
| 7d64d5aa-96e2-33fc-86a0-b8b2fec1d154 | -7.22912 | -43.07222 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 796278a5-1929-39da-9e02-3b11112317db | -6.9641 | -42.88317 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 33.6 |
| de8b841b-8a91-3c42-b630-fb02eacfaf22 | -6.95049 | -42.8953 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 49.2 |
| 2329bb5c-bc95-362b-94e8-2419f8d6c124 | -6.37888 | -39.25534 | 2025-07-03 03:15:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cdee727e-dad0-3b04-84da-3f11fc8a6ad6 | -6.37963 | -39.25119 | 2025-07-03 03:15:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 54620c64-a9b3-35d3-986d-576acbc21377 | -6.95756 | -42.89668 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 30.3 |
| 43268ede-2418-33ed-8bc5-cda47406a5b8 | -6.96145 | -42.876 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 35.0 |
| 67241d3d-8840-3383-9c83-2f76b00b05f3 | -6.19331 | -42.64452 | 2025-07-03 03:15:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 439a646d-9979-30c3-919c-3838f6982e63 | -6.95574 | -42.88846 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| 1c6d50ee-3c79-31b4-99f9-b9376415027b | -7.22465 | -43.057 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 25.0 |
| a7ce2b3a-5a6a-3634-a573-b7e09ad49694 | -7.20376 | -43.0891 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 365802ab-76f4-3354-8f17-d4c2a6685c58 | -7.95609 | -37.18352 | 2025-07-03 03:15:00 | NOAA-20 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 17cfbcda-9a27-3bf0-8ea5-e0341d66a3a7 | -6.19619 | -42.64585 | 2025-07-03 03:15:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 6f096305-4ebc-3f02-bccd-517c471c49da | -6.9544 | -42.87457 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 36.2 |
| 5ee6857a-b9ef-389c-accd-fbec0eb3de02 | -6.94729 | -42.89421 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 61d13638-abb0-3c4c-8520-ea2d8df0a2bc | -3.2471 | -40.08236 | 2025-07-03 03:15:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 98981fe0-ddca-3918-ada3-27e2c5008b60 | -6.95707 | -42.88164 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| 6377323c-9325-398f-9021-8405e7f23991 | -6.95886 | -42.88974 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 30.3 |
| a77b8115-8a3e-3e1a-a647-e7dd107d9fec | -7.2162 | -43.06267 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 6dc1564b-9033-3ec5-ab4a-62e1b81bf4f2 | -7.4762 | -34.84367 | 2025-07-03 03:15:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 292b7e2a-96d9-385c-9c22-4b801e985859 | -6.94472 | -42.88707 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 49.2 |
| d0e43426-ea27-30a6-84f8-0b058153a6e6 | -6.17744 | -42.61274 | 2025-07-03 03:15:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 99144039-53f1-327b-a8d0-62744b66733a | -6.95312 | -42.88137 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 36.2 |
| 87629a42-6826-30f0-8d96-09f468eb5085 | -6.95839 | -42.87488 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 381e02c6-dc6a-3a81-bab5-b20fa6f3bb06 | -7.19525 | -43.09496 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| ae74a3d1-be54-321c-95d5-d494917ecfb5 | -6.96016 | -42.88283 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 35.0 |
| fbb10d26-79f5-3a10-bd43-88ee17a57969 | -6.96543 | -42.87632 | 2025-07-03 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 0d9eaef0-57b0-3f64-ad55-26e39203fb4b | -6.19195 | -42.65173 | 2025-07-03 03:15:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a4922161-b099-3319-97f0-878a17314ef0 | -11.14211 | -43.32488 | 2025-07-03 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 645e4819-8f1b-315d-beb6-fcb1738f9231 | -11.83747 | -43.80163 | 2025-07-03 03:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39d7dd3d-6569-3c30-aeae-b78057f9a5bc | -11.83806 | -43.79992 | 2025-07-03 03:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c77a61d2-2450-35d2-9d50-d4f003435791 | -11.14197 | -43.33175 | 2025-07-03 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 01b34da7-139d-37a4-8bd7-510d5282a684 | -11.84493 | -43.80138 | 2025-07-03 03:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6fffd59-e8c9-3f87-9a89-6fd309a4b231 | -11.84435 | -43.80307 | 2025-07-03 03:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f0d1f49-21df-35a1-8ef1-03c2ea988d36 | -11.14329 | -43.32548 | 2025-07-03 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 56b2094c-e79a-309f-abbd-c212e92d94fa | -11.14083 | -43.33117 | 2025-07-03 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| d40cef5b-7578-3e50-ae4c-c79ace3f2bf2 | -19.74416 | -42.00297 | 2025-07-03 03:19:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6e1b506b-461a-3b2b-9f03-b7166b02852d | -18.90168 | -39.90583 | 2025-07-03 03:19:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d5eef59e-9f6f-33fc-b2c4-446ed400211e | -18.90644 | -39.90693 | 2025-07-03 03:19:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 31f1139d-0309-38b8-9369-1f455582667c | -17.6623 | -42.26638 | 2025-07-03 03:19:00 | NOAA-20 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6bf1c55d-306e-3ffb-8454-c140d2b0bfa4 | -17.75678 | -39.66099 | 2025-07-03 03:19:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e262b5cf-f9ee-3d90-abe6-50f95be9d988 | -17.75835 | -39.66004 | 2025-07-03 03:19:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4c38a066-d196-390a-bfd3-f25f1d005bc4 | -17.66338 | -42.26918 | 2025-07-03 03:19:00 | NOAA-20 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9b1bec37-3e37-3867-818b-bb3c2c7313c0 | -18.90125 | -39.91076 | 2025-07-03 03:19:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b11c12d9-1340-3f20-ad3e-7faeb91163a8 | -17.75356 | -39.65895 | 2025-07-03 03:19:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8ec23e3f-6976-3bdc-a090-90b7f07b9e42 | -17.66149 | -42.27019 | 2025-07-03 03:19:00 | NOAA-20 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8c7c690a-9bc9-3e07-9fda-7acaf7449570 | -18.90235 | -39.90522 | 2025-07-03 03:19:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| eb77603a-b723-361a-af27-83e5e0b880d1 | -19.74343 | -42.00635 | 2025-07-03 03:19:00 | NOAA-20 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 265394a7-04b4-36a5-83f8-5cb63eef4c57 | -7.2219 | -43.0682 | 2025-07-03 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 114.0 |


[Clique aqui para ver as próximas entradas](README7.md)
