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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7246d567-1029-323e-8c5f-f52bfe46abbb | -3.64899 | -41.53418 | 2024-11-26 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 143b33c7-4c2c-3176-9987-1ca3bb347799 | -2.56798 | -46.4237 | 2024-11-26 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 531f9599-7912-3a78-877d-ebd7ef6a560b | -3.44583 | -50.27146 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48b4401a-ea4c-3362-a544-113d5c1bbfe6 | -2.93377 | -48.8255 | 2024-11-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c3658040-cd0e-3ac5-97c9-c2aadc65b130 | -3.9549 | -48.0629 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d36c876-0693-3615-aca8-010690d4e228 | -3.96904 | -48.05344 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1c4deeac-9776-3579-97da-0ad55ba9af4e | -3.97718 | -48.05493 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fd370bd3-8960-3e8f-88ea-39b79a8635ee | -3.97542 | -48.06573 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 8464ca70-ede7-384a-8435-d5aa60cedff8 | -4.77652 | -47.84063 | 2024-11-26 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4c510fb7-4e07-3259-9ced-513b4ebaa0ec | -4.53517 | -43.29019 | 2024-11-26 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 08261b62-e347-3ed8-85b2-2d8ccf50a775 | -3.83865 | -41.55987 | 2024-11-26 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0d96d53a-f017-3580-8b3b-f17340aed61e | -4.50691 | -45.20288 | 2024-11-26 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9d1efaa3-e7bb-3252-b75b-51be68454a9e | -2.69483 | -46.87292 | 2024-11-26 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70e79781-0868-350b-8a2e-e158bf016a84 | -3.91197 | -42.42326 | 2024-11-26 04:14:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b403d468-91d8-3c10-b653-bc2617b6318b | -3.95251 | -48.07742 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6b6217a-3e59-397e-9e05-c61800f12144 | -3.34229 | -50.50928 | 2024-11-26 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1145b4ee-6142-3dd9-a7a8-86d662ccfa97 | -2.46064 | -46.55919 | 2024-11-26 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a893591d-ce40-306e-ad57-5e3e6fc36f69 | -3.39923 | -50.02084 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fff1c321-4c73-3617-80f3-fe0c2d8c72da | 0.94874 | -50.7369 | 2024-11-26 04:14:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bf81fcb-3bc9-3831-9bd3-e83bdee406d5 | -1.8695 | -44.76683 | 2024-11-26 04:14:00 | NOAA-21 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3fca1b32-8ceb-3304-b426-c20ab5094273 | -3.91358 | -42.41292 | 2024-11-26 04:14:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 068f05fc-51e8-3e49-b749-c2ac74e97ad3 | -2.7914 | -48.56551 | 2024-11-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40b20e96-9140-33e6-b370-8da42bb2c431 | -3.44616 | -50.2696 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72ea75c3-962a-34d3-b291-1b0bb9097806 | -1.63619 | -53.30005 | 2024-11-26 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 76d558e6-414e-3db1-b83f-ef9967423895 | -3.98887 | -48.32348 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11090d71-ca4f-313e-ad23-37af547653d3 | -3.07223 | -49.20203 | 2024-11-26 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 767f5bb3-210f-3c58-b5ef-cb89f889cc92 | -2.71467 | -46.26032 | 2024-11-26 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ce5efb5-2446-3680-841e-0062458bf152 | -4.32295 | -47.5379 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 06b03810-a0b6-3d61-9bba-f24483e72dec | -2.09423 | -46.54856 | 2024-11-26 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8dcdfa0c-ae55-3eed-9494-68348f08d624 | -3.96543 | -48.07547 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9cdcfa33-4893-3d93-9aad-012bc6789a77 | -3.96662 | -48.06819 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 692d3652-91f0-387f-914b-6b23a6b0ff68 | -3.46247 | -50.83677 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 26733a3e-2ae0-3d33-9017-f4b66fc86f4e | -3.96955 | -48.07599 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2fed686b-3849-301c-9be9-a6e1abde5300 | -3.45519 | -50.00425 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07885cbd-8acd-3ebe-9881-41c2fb0a4f89 | -3.45991 | -50.00496 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e690ce45-011b-390a-b53b-80b2e2ffe9b9 | -3.27642 | -48.75259 | 2024-11-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0d2db43-3c4b-3e2e-bd04-baa630f2d3bf | -3.24363 | -45.67862 | 2024-11-26 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72fcfa98-a1a6-328b-96cc-b6930cb26360 | -3.50957 | -50.30283 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a8ffad0-204f-393b-9b50-703d6518ea1b | -4.95357 | -38.53151 | 2024-11-26 04:14:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 050a9609-552d-3c4b-8a80-e57229702b20 | -3.96948 | -48.1022 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e837393-c0ec-3d94-bdf2-3870e7c808fd | -3.94783 | -48.08033 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02913636-df13-3962-9521-7fca034041fb | -3.17677 | -48.43896 | 2024-11-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| dd346998-301f-3dc8-88ba-0da86de9a96b | -3.96596 | -48.09796 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c1dde6a-81c2-3884-95af-fee00a1e1c45 | -0.24411 | -48.58076 | 2024-11-26 04:14:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f7af9f9-17b1-312e-a6b0-094fffc2bbdb | -3.95776 | -48.09668 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 46d69fb7-77a2-3206-909d-dc6d00698a9a | -3.91528 | -42.42376 | 2024-11-26 04:14:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 9ce7dec1-ce44-3e80-ae87-7c49dee207e1 | -3.96304 | -48.0901 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 335c9e6a-7cc4-3184-acb0-f12eb88a7ae0 | -3.3861 | -50.0932 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c098b37a-2e0a-3e0f-97c7-aef1d65aae52 | -2.00476 | -48.73683 | 2024-11-26 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a52c213d-6f2e-3be8-86b1-6931acef6f27 | -1.4465 | -47.11876 | 2024-11-26 04:14:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0962bc2-ab43-3cd0-9e05-6d762a6f9059 | -3.45746 | -50.83609 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a579ec91-92d4-333e-9b90-49cfd13fc8d0 | -5.94965 | -39.66502 | 2024-11-26 04:14:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 4491438c-3143-3d5a-8ba6-20fb0124429c | -3.83407 | -46.56107 | 2024-11-26 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 763e6a4c-9f5c-38d4-80e2-312af1da8d06 | -3.98241 | -48.07436 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26fad762-069b-3566-9c0e-6dd695bc5d4b | -3.97477 | -48.0955 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 577ee8f7-e25f-37b4-8d0c-a6e2074d95d2 | -1.19285 | -51.77258 | 2024-11-26 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eae2ea5e-da4a-3615-b0e9-4db60772eecc | -4.35657 | -43.32182 | 2024-11-26 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e5e2885-9123-38e4-82aa-735937025e7c | -3.06143 | -53.28211 | 2024-11-26 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3b7f97d4-d4c6-376e-896f-cbe798d5437b | -3.96494 | -48.05284 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7136229-df6c-30e2-a46d-169f67d71454 | -3.38733 | -50.0918 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb6066a6-4116-3c48-842f-541a80fcc28f | -3.4685 | -50.2538 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d7725b9-2cab-39a4-a2c2-ebe888b0a5ec | -3.98821 | -48.06448 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11df98d4-ca91-3961-8443-5caa43bc7047 | -3.9531 | -48.07382 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb925d18-ab43-39ec-9d61-0b580bcba03b | -3.94842 | -48.07676 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c3df69e-1858-3bd9-bfa8-ce8cf95b1da0 | -3.95141 | -48.05856 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 673600b4-b44d-362a-b8f4-eab45d90279c | -3.18038 | -48.4436 | 2024-11-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 2b548ba8-c703-3b8b-877e-6a829c74495c | -3.94724 | -48.08391 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29a05b66-b981-3992-9fd7-3a7d5fd61d48 | -2.60377 | -46.81168 | 2024-11-26 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36c080be-2b25-3891-94c3-68ee24ab63ec | -4.80812 | -43.30853 | 2024-11-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dad1dc3e-9dd2-372e-8bf3-dd64e08abefe | -3.38851 | -44.17764 | 2024-11-26 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 50971dd8-27ab-362e-8c8e-99f7363d11b2 | -2.5316 | -45.59969 | 2024-11-26 04:14:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92e18a2c-eb7a-3280-837a-b482891e089a | -3.96364 | -48.08645 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9d1c2d37-7e53-347d-a6fa-97fa71428e68 | -2.93675 | -48.7784 | 2024-11-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ed7babf-29a9-3289-a613-66ee945480ca | -3.11459 | -45.08138 | 2024-11-26 04:14:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0b99859-0dde-3402-a84c-77de77540a83 | -0.88458 | -51.71951 | 2024-11-26 04:14:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50d4a6d9-6e15-3d50-b0ba-dfdceeeb7e95 | -5.85455 | -39.42199 | 2024-11-26 04:14:00 | NOAA-21 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6eabd4a2-45bc-3246-9017-f9a0792d3298 | -3.9712 | -46.72714 | 2024-11-26 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 545e649b-51e2-368e-a322-f83a59ec96f1 | -4.54401 | -43.29863 | 2024-11-26 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 912fd988-b1ba-32fe-a0fe-ce80be53046b | -3.32391 | -50.05692 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 74b0170c-96e6-3c48-abe2-b4954a9d0834 | -5.12104 | -38.08183 | 2024-11-26 04:14:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f9c810ff-cb80-36bc-973f-64de6f247426 | -3.42781 | -49.99449 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2b6aebba-41cd-3105-ba6a-105b93b11679 | -3.96602 | -48.07187 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 0e358427-6404-3f71-b102-909892e52104 | -1.56232 | -45.68322 | 2024-11-26 04:14:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae12f990-9472-3f59-927d-9fd1e13b86c3 | -3.39303 | -44.17097 | 2024-11-26 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f4c3744e-f217-3011-8af8-60c66aef1485 | -2.88916 | -48.74068 | 2024-11-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1284eb30-d403-358b-9797-7b4c2651f99f | -4.31354 | -47.52114 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3e2912b0-242a-326e-8386-475942c1a97f | -1.56665 | -45.6795 | 2024-11-26 04:14:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0baa80de-cbad-3477-b297-641c204789c8 | -3.96715 | -48.09067 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4b40f5fc-cfd9-3b1e-b0ef-b738102fd61b | -3.98183 | -48.07795 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26d4af9a-2615-3d9f-90c7-83f3cd085d7b | -6.06355 | -39.18508 | 2024-11-26 04:14:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 13c0632a-635f-3d0f-84c1-12f9677e5bb5 | -4.80758 | -43.31198 | 2024-11-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2635507a-78f6-32e5-b949-13b5e10518c5 | -2.32814 | -46.12497 | 2024-11-26 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e533c29c-6b56-3641-944f-e969262bfb51 | -4.54233 | -43.28776 | 2024-11-26 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac76662e-a5a0-33f0-840d-1778d8877f1b | -3.98764 | -48.06804 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc5281f5-95af-3ca6-b9f4-9c019314308d | -2.57743 | -45.47229 | 2024-11-26 04:14:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bea5ca28-5ea3-3b42-9c62-3944c8403afc | -4.54071 | -43.29811 | 2024-11-26 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ce7043f-9462-3f11-86b8-97132535a29f | -2.54676 | -46.40751 | 2024-11-26 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f9f78bb-d3e8-3f60-8e1a-5d17039149c3 | -1.82878 | -45.58322 | 2024-11-26 04:14:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42a1f465-f1c8-3c24-9ca2-d406c1154bcd | 2.16865 | -50.69944 | 2024-11-26 04:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3bbbd21-b79b-3efc-8380-bc19e5714a68 | -2.60763 | -46.81224 | 2024-11-26 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README14.md)
