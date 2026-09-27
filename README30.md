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
| 3be56a4b-77f1-3c7c-890b-15bdf16df4a9 | -8.28051 | -45.41595 | 2026-09-27 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ab868221-6751-355b-be8c-398c69e9e512 | -4.84209 | -42.89016 | 2026-09-27 04:51:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 10b03d07-6a9d-3b7a-8f9e-bf91865f50be | -3.8757 | -52.28163 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cd71c68-2050-348b-9e89-aa21fc0ab3f0 | -4.25729 | -51.05083 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ab585752-c36e-3287-a57c-6b148dfaa146 | -1.93049 | -52.31735 | 2026-09-27 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab433db9-0181-3e5c-ab84-99d70a3bd892 | -8.36226 | -44.15404 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 434563a7-faf0-34e5-ab7e-605a56b98c4d | -8.35127 | -44.16209 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 101.2 |
| cd5250ef-1ff5-3b73-86b1-e20871666937 | -8.36843 | -44.14812 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4dea4c88-3e32-394f-a23f-a9615839431f | -3.19541 | -51.03559 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a0aa470f-f21c-36ea-8b26-45a35ad32395 | -7.68209 | -54.74647 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d80e41f-9c6b-32d5-b2ab-f8bb3ed6615e | -1.74378 | -55.24801 | 2026-09-27 04:51:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d7f7424-737a-3680-8d63-91c769629f8c | -7.47283 | -54.99683 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7843f18c-4b1b-328c-a8a0-ad386d6793d9 | -4.4623 | -55.03075 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d7b8ea4-c1dd-3210-9874-c7b8bb6a6856 | -4.36378 | -55.28598 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b218ce8-fae9-35cc-a511-1c702b028dec | -3.00249 | -50.47481 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2a2723f-502c-3133-b480-c5383c25c7bc | -2.9642 | -54.08477 | 2026-09-27 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6b00a65-aec1-3739-825e-06212488ef3c | -6.84749 | -43.50996 | 2026-09-27 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2378d927-2740-3b11-b1b9-7234b0742f71 | -8.35839 | -44.14949 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 475188ed-0070-39e4-9223-a55718e4d4be | -2.06514 | -56.87009 | 2026-09-27 04:51:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| edaec93d-7184-3cea-8ca8-ec0ce55a7aca | -3.22601 | -54.31726 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2d397b7c-b208-344e-98d1-a4b1f94af83e | -8.04074 | -54.89375 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f6de6c25-d37b-3661-8db5-924bbeb6886b | -4.5281 | -54.98373 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebda0ed6-59da-362b-ba2c-479761e2ac08 | -2.55347 | -57.41348 | 2026-09-27 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09c906d7-4eb8-39ea-a228-c9f9a716a5b9 | -3.76916 | -51.80721 | 2026-09-27 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32544494-6f49-3480-9b7d-b2cbc7cd34b8 | -6.15783 | -47.12758 | 2026-09-27 04:51:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fef24d95-0d5b-3b2b-8d63-fa3e01e2f6f9 | -8.34855 | -44.18193 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 21cde7bb-d667-39b8-9fbf-9251efa956d7 | -4.69711 | -55.94346 | 2026-09-27 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63ecdd0d-2de4-3a60-87d8-5f5b9497a465 | -6.05987 | -53.60765 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0a80bf04-210a-3bdf-8ff1-45e37298482c | -8.34915 | -44.138 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3d47a26-a267-34d2-95ce-19e26206db4b | -4.50631 | -54.94038 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f9869c1b-f251-3250-b656-a94ae2035007 | -3.27077 | -50.14174 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74cd9527-6b3a-38b7-8c16-3424ac876b1e | -2.90624 | -54.11786 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ca5f521-6035-3ea7-ab86-2df2633956cc | -2.63666 | -48.55751 | 2026-09-27 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3501ca38-6c6b-3a4c-bfce-507d0a949605 | -6.1306 | -53.04975 | 2026-09-27 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab3b04bc-9e04-333b-a769-c3b6cfc0b1c3 | -2.99911 | -50.47429 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 465798f0-886a-3840-9871-6cd6bfb5d844 | -5.99004 | -51.87672 | 2026-09-27 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 793d76db-4ea9-3442-b9a8-ddc929a9d91e | -8.09276 | -54.74125 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02d94a06-2ab0-3f28-b4df-7a55261cb6cc | -6.77622 | -48.66626 | 2026-09-27 04:51:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6accd99b-3e36-319e-bfb7-b5b5f8d8692a | -6.13337 | -53.05371 | 2026-09-27 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf38c5e7-513e-33bd-a7c2-a4d40bf24ffd | -3.19874 | -51.0361 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 862bdd30-23e9-36c6-a348-87792ca4e77e | -3.76862 | -51.81065 | 2026-09-27 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7538b58-0446-33d8-accc-ed92c16a533c | -6.07841 | -57.81131 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bead3427-ae5d-350f-ba7a-25dadc822265 | -3.8724 | -52.28112 | 2026-09-27 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66192855-4b8f-3dd1-8c81-cd32aed65623 | -4.56992 | -54.94638 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5e718f31-0f5a-3486-afcc-d49a73ebaaa1 | -4.46304 | -55.03012 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1acf6c1f-68b7-363e-9985-4309212d5441 | -3.41715 | -50.41914 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c239ea30-4769-3e5b-9706-bd9654f3d890 | -6.88277 | -55.55495 | 2026-09-27 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48a271d6-455a-3e7a-8ec5-104a4d584dd8 | -7.49664 | -46.60486 | 2026-09-27 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80773956-3fa3-34a4-9dff-264be45342e6 | -3.67403 | -50.84496 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09641d0f-5426-3176-b7e4-350c6b205b3d | -3.19929 | -51.0326 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| a5a3cad3-7693-3dd7-984d-f6ebd73b4321 | -4.27523 | -55.13609 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4de1e54-13e2-34b1-89d1-3f7c97aa64e9 | -8.62821 | -54.66791 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bdcb7e5-c03e-38d0-add0-e6305b212d52 | -3.71978 | -54.6582 | 2026-09-27 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 33da301b-6524-3e1c-b426-438e9665704b | -8.35207 | -44.1492 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6c42845b-c3bc-3240-9dca-29d569802c59 | -3.1982 | -51.0396 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3c56d9dc-1c0a-3d87-86c5-0528087a4968 | -3.07334 | -54.41432 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9e4340e-b973-3f40-9630-c0212aab4a06 | -5.16768 | -56.00365 | 2026-09-27 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 46320d59-aa03-3925-bc6f-10506f40ad57 | -8.35383 | -44.1828 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 56c8747c-4cd3-3d2b-80b3-4aaa5abb55f5 | -3.96778 | -59.34602 | 2026-09-27 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8472d0da-84bd-30ab-b5f5-301d086c7189 | -2.65627 | -56.54052 | 2026-09-27 04:51:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0dc645a5-9730-3b9b-9ae7-25e7aa81eafc | -6.87525 | -59.87708 | 2026-09-27 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f948fab-1698-3c71-bd03-422ec518efd2 | -4.49868 | -54.94317 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4ecd72c3-039f-3428-8d6d-ff3db72a661d | -3.22362 | -54.33237 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6b93f609-4f9c-3d35-9837-1396e13838ef | -2.78868 | -57.69692 | 2026-09-27 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 90c8e03a-4fd5-3c16-b9fe-62be58585a85 | -2.99966 | -50.47068 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e85c2b59-98a4-3bbb-a793-831c90d9af81 | -8.07695 | -54.75361 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd4b62b6-df95-39a4-8e1d-c24b66fe1095 | -6.09066 | -57.62719 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40ca8111-c7b0-319d-a834-4676d4634739 | -4.84708 | -42.89451 | 2026-09-27 04:51:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| bd30a708-977f-34af-b784-e0d89f1fb773 | -2.79662 | -57.67434 | 2026-09-27 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4bc1c424-032b-3c29-8dad-71c3a0440183 | -3.22707 | -54.33294 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dba2f307-3fc8-3396-a672-271d5388ed47 | -2.50832 | -56.22801 | 2026-09-27 04:51:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48437cd7-afbb-33c7-8856-af255d587950 | -4.56931 | -54.9502 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ca63d39b-0ff1-3da1-9497-923ae5cddc74 | -2.44549 | -50.25714 | 2026-09-27 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b6ab23e-40c6-3a74-81d3-8aecae77dee9 | -6.83527 | -43.51875 | 2026-09-27 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60596365-3cb2-35a1-8988-04fd734a3c79 | -8.35922 | -44.17744 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| b90c5780-d4bf-3bd9-bd70-88e46851c2b1 | -3.87186 | -52.28455 | 2026-09-27 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77e9e02c-cfd0-3a67-a4de-b681a5086fd5 | -8.15417 | -54.8223 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf72e473-ebb2-3313-bcfc-77c14085069f | -4.46415 | -55.42991 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b893319-54ac-337e-a45f-b1cfece356aa | -8.35307 | -44.18329 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| ba4fab4f-7ee0-3134-938c-f321232977cb | -5.82689 | -52.0302 | 2026-09-27 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 376be829-2dfc-3b88-b725-979d388546cf | -6.63652 | -59.94918 | 2026-09-27 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af7d09e8-facb-3001-9278-341c2d1ea5d1 | -3.86993 | -51.79451 | 2026-09-27 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 117e6428-5fa3-336c-8f76-848aa77db494 | -8.35293 | -44.18939 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 3699698c-2042-30f5-a2c2-42e47c74aebc | -4.34569 | -55.77274 | 2026-09-27 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e8cd6d1-7377-3967-a1bc-ba1f97fb699b | -3.69832 | -51.36767 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5133d6e9-4a39-308a-b4cb-78e4cc143819 | -7.69667 | -54.76375 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acbb8e30-d345-3387-b09d-5f40a133a829 | -6.05377 | -53.60312 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbc30687-0a12-3b9e-818a-02959bfcd82f | -5.17056 | -56.008 | 2026-09-27 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e43636b9-7c1d-3eb3-9286-9e32ebd3eae9 | -8.35965 | -44.17411 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 4c1fa36b-c6a5-3830-828b-9a63a97e9590 | -4.5856 | -54.92436 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d47935c-cd96-3830-9cb8-0e5d33bfe759 | -6.87831 | -55.55508 | 2026-09-27 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf3ea6e1-7a3c-3cd0-ab4d-995a822e5efd | -4.25449 | -51.04677 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50fd17f7-df87-3927-8059-44814e690c3f | -3.22767 | -54.32914 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a7eedc5-5b71-3e15-a115-2c631399ba0d | -7.47521 | -54.98201 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cdb7312a-18be-36f6-98b6-07266ba39e98 | -6.13282 | -53.05717 | 2026-09-27 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01bb9272-7603-3695-9021-465ddfe4ab3d | -3.23112 | -54.32967 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 222baff7-ad07-38ac-b44b-e3c9c736af41 | -4.28692 | -48.6116 | 2026-09-27 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2387de5-32b7-34b5-b4fe-5eeada4d33cd | -6.17517 | -44.59058 | 2026-09-27 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e147e169-fad9-3b12-926b-00233b0477f9 | -5.75893 | -45.29403 | 2026-09-27 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d7c26082-03aa-395e-bd38-a136342e869d | -5.7351 | -43.27684 | 2026-09-27 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README31.md)
