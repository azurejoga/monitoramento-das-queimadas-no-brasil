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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 157bb994-848e-320c-8117-e272491cb192 | -3.2463 | -53.64042 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 55b8e08a-956c-387d-a8fd-fe2acdb45e21 | -4.16858 | -46.81511 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e93b0512-bf9c-330f-839c-554bbb62a7b1 | -4.18551 | -50.67868 | 2024-11-28 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b627d2cd-10c2-30e6-917a-1dcc8ea8356a | -3.78784 | -46.68969 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76216c53-f055-3a08-ad74-129da4c51b86 | -3.53971 | -44.94384 | 2024-11-28 04:25:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4468df6a-ff36-3d07-9436-08285f60fb57 | -3.41526 | -53.88706 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28e09da2-3640-34cb-a624-665c210acaa1 | -3.26489 | -45.3738 | 2024-11-28 04:25:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d311efd4-51c6-3b55-af4f-2747f34b8ec6 | -3.07718 | -48.66729 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3920166f-4379-315e-b27b-feb7aa4b6671 | -2.81528 | -54.07851 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06be8ea6-7b98-3771-bdec-be89b7456601 | -4.80715 | -43.30176 | 2024-11-28 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f25f9863-c759-3cd3-a683-fe33d2164e1f | -16.83606 | -46.13153 | 2024-11-28 04:25:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7bcfebe-650f-359e-a3b1-7f55bf537861 | -3.34798 | -53.73973 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6573aa0-f04f-379b-a339-43f45279b4b0 | -3.61115 | -51.15722 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7c3b5bfe-1729-31b6-b0c6-484ea3cac5b8 | -3.77447 | -46.68763 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 996b749f-2cb0-30b0-b09a-87037fe7cff6 | -4.1446 | -48.23154 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91c0a933-bef5-3014-8928-c13e19249031 | -3.70827 | -47.12642 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac0647d3-9eb2-339c-88b1-9fd9c61b143c | -2.84133 | -46.84793 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b561876a-dfee-3e50-930d-4934d8bd014d | -3.60696 | -51.15656 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 03c3cb7a-d3aa-34a0-a93a-3cfa7859c601 | -2.24808 | -53.62501 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a05d3d12-434d-3e43-9a8c-c3273de52bf0 | -3.50145 | -50.49625 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b0ea42b-8a5f-3ebf-a19e-24fb6813c0e9 | -3.7234 | -49.96474 | 2024-11-28 04:25:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14d923ed-19f7-3489-bc7a-ddccd3d3d3d1 | -2.87389 | -46.8604 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f90cc4a-1c80-3e73-a99f-bbf617fc09e5 | -3.84333 | -46.53307 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57526ab1-aee5-34e2-9d59-dff62266e9af | -3.05541 | -51.05778 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de9ada1c-006c-34f4-a8d1-57cb3dc2a5a8 | -2.25853 | -53.7552 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04eaf7ed-a2e8-3a08-84bd-3549f87ae5bb | -2.94078 | -51.59375 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6ef1bba4-6355-3729-a26a-7a897cdcbfe5 | -2.79077 | -48.08883 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd6323ad-d040-387d-81aa-31f9fcc78bb4 | -3.28705 | -45.51463 | 2024-11-28 04:25:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c01602d9-4458-3c95-b144-f396e2ef9d9c | -3.35341 | -50.51098 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d11b13be-4582-35ca-a709-ef1031f787e8 | -2.31868 | -51.95889 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 503eefc0-9bae-3a0f-877a-74615c2a49e0 | -9.07815 | -49.58039 | 2024-11-28 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 285b456e-6b73-3c0b-9570-6c09628d1a75 | -4.67151 | -44.61317 | 2024-11-28 04:25:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| ecf3dbec-828c-36d0-b030-627f03421ecc | -4.03257 | -51.02338 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9a07ce9d-4f00-3e04-b9a7-d50242e9e127 | -3.78728 | -46.69322 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37c00722-5ceb-3417-add3-3e3378a925aa | -4.25621 | -48.0708 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d456261-2db0-393a-b63a-760790164e60 | -4.04211 | -48.2603 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57fc515d-403b-3a5c-9a46-7aaa5648ff5e | -3.00192 | -45.46961 | 2024-11-28 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 302c705d-5cbc-334d-814b-e1a0984af8f7 | -4.05158 | -46.69562 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa30ab85-7fd4-398d-82ae-52ee40f1e74f | -3.95417 | -49.92757 | 2024-11-28 04:25:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86a76272-40e3-3e32-beb8-9926741afac4 | -3.71108 | -47.13055 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29b0fa9d-2f06-37a2-8c53-381465917542 | -2.84126 | -46.87 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| e2869090-19fd-3941-9931-c33e5456239d | -4.99131 | -42.66954 | 2024-11-28 04:25:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bdc7d1f2-f421-3bc5-b1e9-21d41f68ce1a | -2.25751 | -53.47101 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d989fae-8cc0-30cc-a792-aaf8697c19e7 | -5.26415 | -44.77335 | 2024-11-28 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 16c883e8-737d-3918-afd7-7e99a5c4ecbe | -3.93843 | -46.89474 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 293ffe6d-a9ae-3bc9-8055-12780401cb33 | -3.50129 | -53.80661 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 912d4a75-193a-3600-8533-fd105f836388 | -4.6034 | -49.39296 | 2024-11-28 04:25:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7fb34e33-8d98-39a9-9721-9a3c76a704fb | -3.10032 | -53.25677 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ad23973-e311-3d1c-bcac-e4555a14419c | -3.97824 | -46.73065 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87c0d0d3-e76d-32af-bbf5-a6a9b21dc9bf | -3.94206 | -46.72137 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7f0d097-7640-3ed0-8df0-7b60984feb20 | -2.91077 | -54.18623 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afcf8808-1f57-3c50-b39c-d5f431a92174 | -3.69303 | -51.37278 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fe2f0e66-3e35-39be-aa0f-5b842c8115f5 | -3.34202 | -46.2872 | 2024-11-28 04:25:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 073f4ed8-07aa-3229-8b15-de80180fcdf8 | -3.77782 | -46.68813 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a15f7817-1846-3eb1-9ae5-7f69dc68de3d | -3.8154 | -47.46788 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a792b7f-919b-3cc1-9275-284eefe04eb5 | -3.04723 | -48.52309 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa23910e-da70-38c1-8dee-23bf48fa0188 | -2.84527 | -46.84486 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 46d0529a-ce38-37b9-8233-537d8427d201 | -3.65384 | -49.95345 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d5c28db-ec93-3feb-9956-200fe4d61cd7 | -2.84298 | -46.85923 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e12ce3ed-3603-3805-ae6f-b406fe27afdd | -3.80343 | -46.6777 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9d3d980-573b-366e-9659-de2bfcebc8d9 | -4.02824 | -46.54443 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ad78c5d-e459-3035-9f45-7c2bb5da8e52 | -4.66235 | -44.04137 | 2024-11-28 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91c1cf0c-942d-362a-85c0-0bb5ecc47e93 | -3.765 | -46.68261 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d51f8eda-c640-3e8f-93ee-b90343271f8d | -2.17324 | -52.13601 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fb5b4559-acd0-3aa3-88a9-d75ece6229a7 | -3.32939 | -45.50362 | 2024-11-28 04:25:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb9d0f2c-1dd5-3f4a-95dd-e117b754de4c | -5.58363 | -42.9297 | 2024-11-28 04:25:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 445821e2-ea06-3b3b-9c9f-753fcf40aeac | -9.15964 | -49.4819 | 2024-11-28 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 102d1018-50c7-30b4-a78a-c4cae2440668 | -3.98136 | -46.99289 | 2024-11-28 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e014bd1e-cc67-3f51-8d8c-34b72854dabb | -4.04632 | -46.85746 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e17a7a83-b5a1-32d2-9bc7-fc890679f80a | -3.41263 | -47.59603 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2a3bd24f-06ea-35bb-85c4-50c69580225b | -3.08968 | -51.03193 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6eb34cf9-436d-3cf5-8c2d-7e51a2ea31bc | -2.89163 | -51.72754 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f38f0c3f-4e6a-34fa-8eb8-5f2f8d981000 | -2.84864 | -46.84539 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41a296e1-061e-39e7-b9b9-f31a36c68946 | -3.40093 | -54.28383 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28ea51e3-708b-398e-8219-43901b10bca1 | -3.76667 | -46.67205 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2180849a-a8ef-3608-8f2b-985c46b5cea8 | -2.86493 | -46.85159 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 85c43811-5a58-39e3-af84-4eafbe79e98f | -3.71015 | -51.7968 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7e15d25-ac59-3eab-be9e-b487a92b7d53 | -3.34891 | -53.73423 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f8fc7c9b-5727-35c6-b22b-2ffe5030785f | -3.57031 | -52.28032 | 2024-11-28 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d88eb03-1f34-30fe-9469-7998a7d82003 | -4.11159 | -46.94413 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9e61487-6d2b-3861-b485-54773961d41d | -3.39056 | -54.28201 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 699b53e3-69ae-34d3-88c4-f765ed448d7d | -3.79894 | -46.59795 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83b1adfe-9ecf-3688-a10f-9d3fb149e62b | -15.09777 | -54.62435 | 2024-11-28 04:25:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 809117de-9bf1-3c2e-9304-e755bbdbb8f8 | -4.66009 | -44.03353 | 2024-11-28 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c258b84c-ed1a-30bf-af5a-1551391afeef | -1.64312 | -55.23238 | 2024-11-28 04:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29554cfd-00de-3c44-9550-f8ee96748090 | -2.6275 | -51.77121 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 693d89f4-1081-3361-9347-782d228baac1 | -4.50949 | -45.79794 | 2024-11-28 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3eb849e5-f68b-34c3-86f3-97f94d66ef64 | -2.83179 | -46.84277 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a5969e2-a9a6-3da9-b4e1-b3b537a46457 | -3.94902 | -46.91463 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7d6f9fb-901a-3f3a-afd0-22db39e7dd06 | -4.66084 | -46.92877 | 2024-11-28 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55a58070-c6e4-3eb2-849a-54ca3f48935b | -3.80674 | -46.61347 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fbbbee3-4a21-391b-8e73-88131c053ed1 | -2.25439 | -53.7483 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5fa2a8b-cb39-33d0-af3e-9a8531df4de1 | -3.37127 | -46.66087 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af2d9fd4-f40e-3b4b-abd0-6e0ab8745abd | -2.41496 | -53.82747 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a885adf-9aa2-341d-889a-a441c6991fe1 | -3.29311 | -45.51909 | 2024-11-28 04:25:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 8e574a68-c37f-3b61-9aee-caf5a4060d31 | -3.99916 | -47.91812 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 063dc8ef-1fad-325e-914e-934c2bd0b64e | -2.60771 | -51.94938 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 641bab91-f9ac-3904-8343-619a28bd4ea3 | -4.66714 | -46.28575 | 2024-11-28 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd60ad3d-1da8-3749-ab57-e0c60fa19cd7 | -2.82237 | -54.03519 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33972e7e-a043-381b-bfae-d63d80a92274 | -3.70547 | -47.12229 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README54.md)
