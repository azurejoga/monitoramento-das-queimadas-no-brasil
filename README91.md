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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bcc2e166-e2df-3a56-b64e-ece98d10f3ca | -2.86085 | -53.96029 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7605789f-8094-354e-84ba-618340cf9028 | -2.84085 | -52.5407 | 2024-11-28 05:18:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1435819-7580-34e4-bc74-fe31c2b50322 | -3.31125 | -50.03043 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 431dc752-3dda-348d-9819-0f1f34c9eb1e | -3.51919 | -50.21864 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebf334e6-d208-3385-8356-7e8bcdae874a | -2.57412 | -53.97641 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0fc2deeb-f840-3b6f-bacc-0a8d55892cf3 | -2.60723 | -53.96666 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 61aa8167-5809-3ea3-8634-d1b4ecb3e259 | -6.47255 | -54.91291 | 2024-11-28 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e12bec6-4dc8-3cf3-ad6b-896f3e7f6869 | -3.24262 | -50.14462 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1ac31f7-f13c-3c7a-be9e-f1576acdb396 | -3.2397 | -51.55113 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f6f6fbda-8611-3e5e-b52a-67c77c6b228c | -2.61881 | -51.80771 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff7a7add-e849-3fdb-83a0-b9a10f16bc89 | -2.83708 | -54.1142 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| c669a390-1dc7-3e25-a252-42e0f1365967 | -2.8033 | -54.02575 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e771511-a7f8-3cc6-8455-69b098136f1e | -3.5107 | -50.31001 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f00f50d2-a98d-3875-8453-3d4fa67d530c | -3.25061 | -50.62471 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d706b87f-b35f-33ff-a9e9-1ba2e04d6870 | -2.69589 | -51.98194 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 150478ca-ca83-35ed-a9d8-4d356f383257 | -3.46702 | -50.53434 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 681d67f9-4ceb-3ed3-8d3d-c5ecafc9d3af | -4.2263 | -50.88746 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fab34143-155f-3e1d-9079-3b581fbb830b | -3.30561 | -50.27632 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0faf5fd9-a9fc-384d-9a43-accd2ed07fb8 | -3.00874 | -53.21619 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3dbc9104-196c-3e02-9626-2925844a49a5 | -3.63855 | -54.44622 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01d4b927-fe0d-3a7a-955b-b22f245705e7 | -3.30711 | -54.17579 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7c56348-242a-3d83-a3e7-cecc8fb18584 | -2.20388 | -54.52571 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72a2b5fe-81e0-35bb-95b8-32b35f318212 | -2.23228 | -53.68583 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a272342-ce56-3b14-8d7f-edfc8186fc62 | -2.80134 | -54.06476 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ff66f12c-84f9-3d69-9ba0-217fa306e974 | -3.21251 | -53.8429 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd6dd756-9a0c-3459-9b02-5d9e1954d6f8 | -3.10784 | -53.10674 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ba48c1e-6b7e-33d3-a0e0-b662c19bdb37 | -3.51616 | -50.30784 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8791412f-11b6-3e6e-adda-372eb2c5ddf9 | -3.09322 | -54.13011 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 487780cc-84a6-397f-abd0-a01428309ee6 | -2.73778 | -54.10592 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d75f78e0-5908-37c0-ab92-bb5d5699daa4 | -2.9545 | -51.28689 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b74e6fea-44b9-3a97-86b8-ec3e805a2def | -2.99093 | -53.36386 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f4d96f8-5592-3996-a7c4-48afd6c59633 | -2.98415 | -53.89064 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8223cd2d-79ba-34e9-80f3-cdaf70520119 | -3.27151 | -51.26515 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2941395-c18a-3a39-9043-64360d947f1c | -3.23802 | -54.22747 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9112c711-4feb-3dca-9fcf-904302fca8d4 | -1.81617 | -55.62911 | 2024-11-28 05:18:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0049f1e-8a9f-3d0e-aa79-b1240c6fb5b6 | -3.26603 | -50.43814 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a4640e6-2f54-3574-bfd3-7cdbf311360a | -3.51512 | -51.6553 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3940620a-1c70-30ef-bb90-509be440d239 | -4.48333 | -48.11418 | 2024-11-28 05:18:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f2f5da5-7f1b-30fc-a5d1-abd9f0d2adf5 | -3.24297 | -51.55988 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a8388bf8-96e8-3eff-ba15-7d54fc841820 | -2.17366 | -52.13451 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3c1008c4-5a78-39ee-b698-9c074807ef7b | -3.08155 | -54.56596 | 2024-11-28 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85260a6f-6652-34f0-bc1b-b42a43720f27 | -4.17171 | -48.62536 | 2024-11-28 05:18:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 93b39c2d-0d2a-3d5b-a222-ece1680c6873 | -2.73294 | -48.89768 | 2024-11-28 05:18:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8682d0f6-9bed-35de-b3da-eed8a53dac18 | -3.12071 | -53.10506 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95d69e8f-fde6-3ec0-9502-6ac6da50aba4 | -4.06599 | -54.38546 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53e5cc99-e8e6-3c6f-bd0e-4fa5411f176b | -2.31262 | -51.95567 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5abd35e3-134f-30c3-8241-54a23030e0af | -3.49915 | -53.80464 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| a4869e15-ff23-343b-8d06-ca0b88fdb168 | -3.9658 | -48.08039 | 2024-11-28 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a1fbae55-c859-33bd-9e1a-1511c9a6c780 | -2.80627 | -51.58899 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9a899b88-f42a-3048-b902-c5568e312304 | -2.1879 | -52.12815 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce73dda2-2973-3519-8c3b-e1f538105b46 | -3.69672 | -51.37186 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36d1596f-16a1-3fc5-b90e-26e105022908 | -3.23323 | -50.31558 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 451afabc-7ada-3b49-adb4-940969c46236 | -2.96465 | -53.88751 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02e1863f-f007-3c34-a20d-0828a51e1f5c | -3.72337 | -50.1879 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c92f95d-4055-3bf0-a2e3-c8a89fdc50bd | -3.57038 | -52.27829 | 2024-11-28 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16aec30b-257d-3c16-8302-f2086681a54b | -3.06059 | -53.28683 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5d35999-654a-3e2e-b280-fc71e56d5d98 | -4.11594 | -48.48494 | 2024-11-28 05:18:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a44e1a8-b562-3dd8-839d-8a414f603678 | -1.5897 | -52.271 | 2024-11-28 05:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 2af4c6b8-52a9-3073-b3ff-6660ecd6320d | -5.9975 | -45.3607 | 2024-11-28 05:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 6ae8f27a-2aeb-34d3-9056-2f244c125672 | -3.3852 | -45.8465 | 2024-11-28 05:20:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 4543cca3-68f0-352b-9933-2f7e627fbb8d | -6.1735 | -42.6221 | 2024-11-28 05:20:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| ae7591b9-ca9a-30c0-923c-7c466b108657 | -5.979 | -45.3395 | 2024-11-28 05:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| d8917a22-667c-370e-9a7b-8fc9f08e19fb | -5.9788 | -45.3621 | 2024-11-28 05:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 05888e82-71f3-3eb5-b4aa-85109fcfb7f0 | -3.3853 | -45.8241 | 2024-11-28 05:20:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 56.7 |
| eed4a1a0-c789-3ca4-84cb-f75e1d0d035a | -3.3837 | -50.1125 | 2024-11-28 05:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 4e87f327-e8bf-3f81-bbe0-61c19fb70f68 | -9.77778 | -64.77842 | 2024-11-28 05:20:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c112ded9-2a4c-3237-aca6-2e30606610d0 | -11.85794 | -63.35524 | 2024-11-28 05:20:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 02fb5c4d-f6e9-36f8-86d5-8aca89c823e2 | -12.2596 | -60.72029 | 2024-11-28 05:20:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8ea554d-3d54-369d-acaa-5998a549e95b | -13.4211 | -60.22453 | 2024-11-28 05:20:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 613e68ac-43c2-3fd4-95a2-8618b904605f | -9.61228 | -64.68729 | 2024-11-28 05:20:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1de98e62-b52c-32c7-9bc6-1ed79353e8e2 | -9.51767 | -64.46208 | 2024-11-28 05:20:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c842f259-69cc-35e1-8c0f-732cbfb8f6fb | -9.77471 | -64.77267 | 2024-11-28 05:20:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a06ffd7-588c-39fc-adcc-8bfb5033f6ea | -10.46656 | -49.64941 | 2024-11-28 05:20:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6251103e-b4f6-3dc7-b343-d70be586606d | -12.11674 | -63.80044 | 2024-11-28 05:20:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d417cc2a-9095-375d-9a6a-04a42ccd226e | -9.07814 | -49.58004 | 2024-11-28 05:20:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 596a950f-b694-3684-b009-aa9791e7c8d9 | -11.91605 | -63.67694 | 2024-11-28 05:20:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab5a00fc-527f-3c1f-a919-bd5e9aa77925 | -9.07866 | -49.57606 | 2024-11-28 05:20:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 616b3d8e-f682-3945-bb33-b8a9e06dd721 | -12.05133 | -63.85229 | 2024-11-28 05:20:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 773c9c8f-0d6d-302c-a6b6-48d69d9f2949 | -12.65032 | -61.92097 | 2024-11-28 05:20:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80714509-913a-3048-9971-fdfe7afdd587 | -12.58948 | -62.00832 | 2024-11-28 05:20:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e44ec37-411e-39cb-9d73-e7a8f6749165 | -13.41497 | -60.19808 | 2024-11-28 05:20:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1dd0f11-ef13-34f0-8967-2bf6c65143a5 | -12.58612 | -62.00776 | 2024-11-28 05:20:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bd6a284f-06f8-309c-88ed-264aeba572cf | -11.90884 | -63.67569 | 2024-11-28 05:20:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37433f00-645d-3a03-861f-88fba9c01927 | -11.90749 | -63.67604 | 2024-11-28 05:20:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86600826-94de-3edd-b25a-08ea13608140 | -13.69027 | -59.84246 | 2024-11-28 05:20:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 175525a8-a5a1-3ae9-b96e-2cce9695cac9 | -11.91245 | -63.67631 | 2024-11-28 05:20:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf6513a1-5466-3670-8201-b49cd2076a6c | -11.83871 | -62.67659 | 2024-11-28 05:20:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bd22112-bf16-3d3c-954f-4434857887c8 | -13.59127 | -59.77917 | 2024-11-28 05:20:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46516ca8-9824-3df3-9def-c698defa033b | -20.13161 | -53.32435 | 2024-11-28 05:22:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bcd7961-01f8-34a1-83ec-1dc98af60e47 | -20.90645 | -55.32593 | 2024-11-28 05:22:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b464231-b0d5-3fa8-95fc-df95293dfd76 | -22.11819 | -49.60722 | 2024-11-28 05:22:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 7faa39f6-90b5-3822-b02d-6852a959bb24 | -16.46412 | -55.08202 | 2024-11-28 05:22:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 84cecdc5-eae1-363a-9d52-bc88ee254e58 | -19.71807 | -53.63177 | 2024-11-28 05:22:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 7b7e4a23-10ec-379e-a49e-e4ec34bfa256 | -19.55921 | -56.70946 | 2024-11-28 05:22:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d9ed1774-9eb2-3316-9d33-05727185aa8e | -17.6009 | -53.74743 | 2024-11-28 05:22:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe15bdb3-1775-367e-a650-6c9c54d98f05 | -17.64496 | -57.58244 | 2024-11-28 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 418063b9-73bf-3e6f-9928-73938a1f8e83 | -16.44019 | -55.96518 | 2024-11-28 05:22:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9cf7ce67-7fe7-300d-bccf-5ce720e2c540 | -20.33034 | -48.82262 | 2024-11-28 05:22:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0127a76e-b37c-3d82-bb22-050f3586e76b | -16.07817 | -60.10105 | 2024-11-28 05:22:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ceb1faa-451f-3049-8b59-4438b0ae260d | -18.77411 | -55.84267 | 2024-11-28 05:22:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |


[Clique aqui para ver as próximas entradas](README92.md)
