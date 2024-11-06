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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26871ded-6f2e-3920-9066-3596dc140910 | -6.1229 | -43.9578 | 2024-11-06 02:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| d0171d7b-1227-3bda-82eb-99081d88a64a | -1.2922 | -54.5585 | 2024-11-06 02:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 0db2eb72-2b1e-3fe4-b381-4305975a4c58 | -3.0207 | -53.443 | 2024-11-06 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| ccbf3cc4-d039-36cb-a6fe-2ba7bb255a0f | -2.6764 | -51.8189 | 2024-11-06 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| d4d383fb-1c9b-382d-bb65-472dea5d1bcd | -2.8607 | -51.7937 | 2024-11-06 02:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 53b32006-6c35-3cbf-8fcb-0109da5ab549 | -3.0607 | -52.5066 | 2024-11-06 02:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 6c2331a3-19bd-36dd-a89d-72c5471c39cf | -2.8506 | -49.4744 | 2024-11-06 02:20:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 0254be45-09f5-3643-a9a0-b39661aee330 | -6.4906 | -44.6862 | 2024-11-06 02:20:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| eeb56e8b-523a-3555-9f6b-c4cee3455e91 | -2.8065 | -51.4855 | 2024-11-06 02:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| f7c6f8d8-4b90-3ac4-bfe7-0ade294ba446 | 3.6184 | -51.3162 | 2024-11-06 02:20:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 113.8 |
| ce77b591-487c-31ab-ab03-bd08e1072834 | -6.1039 | -43.9824 | 2024-11-06 02:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 1f445885-c6ae-31dd-9996-d4fcfdb4b6fa | -6.5014 | -47.4813 | 2024-11-06 02:20:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 246.5 |
| 12705ebc-8447-3952-a0fe-22f1667fdcf9 | -3.3285 | -50.0723 | 2024-11-06 02:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| e5921fcd-4f32-38ba-84d1-27ca491e3895 | -2.9186 | -51.047 | 2024-11-06 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| a703d509-209f-3eab-a89d-918a0b4dc36c | -6.1041 | -43.9593 | 2024-11-06 02:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 91876016-1f3d-322d-9e06-c4dccbe732a7 | -6.1226 | -43.9809 | 2024-11-06 02:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 34faa9a2-d171-3953-8483-c205a0340abd | -3.0207 | -53.4227 | 2024-11-06 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 877b25d7-101b-3c81-a24e-4c50d488a74d | -3.1433 | -50.2044 | 2024-11-06 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 952acf6d-4819-34ee-9f39-4380b9a042d0 | -3.0213 | -53.2607 | 2024-11-06 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 14bb7d25-33b6-35b2-a431-dd6d0cc8a65a | -6.4827 | -47.4827 | 2024-11-06 02:20:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 140.5 |
| ed662cda-30bd-39b0-b79d-5c5b8f494ace | -3.0396 | -53.2805 | 2024-11-06 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| fd63a40c-3d4b-33b0-b10e-45b0ff2c6e2c | -3.1802 | -50.2032 | 2024-11-06 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 5f525b46-c39e-3eb6-98b8-3089a87fc19c | -3.2163 | -50.391 | 2024-11-06 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| f350a15d-9ebb-32f8-9367-4da02b9a830c | -4.1246 | -43.5833 | 2024-11-06 02:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 435e551a-9985-3282-a043-47f86f868d30 | -3.1618 | -50.1828 | 2024-11-06 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 135101cd-15df-3a7b-870c-fd0585049959 | 3.6183 | -51.3369 | 2024-11-06 02:20:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 54.4 |
| f26a68ae-6c4f-3799-8e67-c35ef7a479f8 | -3.967 | -48.15 | 2024-11-06 02:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| a85708df-d193-31d8-a06e-4b15c010eab9 | -2.706 | -54.1556 | 2024-11-06 02:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 490556f3-c93a-3513-aea6-f2dcb1f4c6ce | -6.4825 | -47.5046 | 2024-11-06 02:20:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 3b0f8b35-56a0-3c17-bdfc-cfb499a63c6d | -2.1746 | -53.7036 | 2024-11-06 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| f30a3513-931f-34fc-9a79-97f1515bd43a | -2.6764 | -51.8395 | 2024-11-06 02:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 26c9d4b3-583d-36c0-a2a6-002e3676116a | -4.1432 | -43.5822 | 2024-11-06 02:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 435089e7-5b47-396c-986d-11fee3d9f981 | -3.0397 | -53.2603 | 2024-11-06 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 5747ad0b-6943-36fe-86ee-6db9266957ff | -3.2348 | -50.3904 | 2024-11-06 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| f3a2a8b9-ccfa-36ab-83fa-947e5b23cbb7 | -6.5012 | -47.5033 | 2024-11-06 02:20:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 147caf26-2139-309e-8a10-f55a4045b56d | -3.1617 | -50.2038 | 2024-11-06 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 96eafa40-1b86-3aa8-840b-e9c3c8f4f89b | -3.1393 | -51.2069 | 2024-11-06 02:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 6e74edc3-5abb-3eb0-a37a-61b4820b1c8d | -2.8423 | -51.7942 | 2024-11-06 02:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 4ab88682-a847-3588-9cf3-75b7a3b4a796 | -6.5094 | -44.6847 | 2024-11-06 02:20:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 2ae974eb-b2f3-314a-98f5-81c5b5150394 | -2.1947 | -46.5517 | 2024-11-06 02:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 05a53c06-a996-3406-a2fa-092bed14cc89 | -2.8608 | -51.7731 | 2024-11-06 02:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 162.5 |
| 6e9e5ac3-76e4-347c-a858-e6c1036bf632 | -2.9371 | -51.0465 | 2024-11-06 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 08d20cc6-cce0-39fe-a5a9-39ce45420f96 | 3.6 | -51.3168 | 2024-11-06 02:20:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 39e80747-25cd-3ff3-a1e7-ba0430398a46 | -3.2164 | -50.3701 | 2024-11-06 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| eff832ad-863d-3bee-919c-acfaf993cb97 | -3.0023 | -53.4232 | 2024-11-06 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 83abbf6b-a718-3403-b74e-dc6de3e74e05 | -6.1414 | -43.9794 | 2024-11-06 02:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 67246136-603f-3e00-adf1-6a361b450bc8 | -3.2163 | -50.391 | 2024-11-06 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 6b175557-7b9c-3b49-9a7c-d73ec7933f0a | -6.4825 | -47.5046 | 2024-11-06 02:30:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 765bbf2d-a628-3681-a911-5e12dad42b52 | -2.7427 | -54.1548 | 2024-11-06 02:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 1920ed4f-2713-3fa7-88a5-284cd0e3d8e7 | -3.0207 | -53.443 | 2024-11-06 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| bcd59ba6-bfbb-3c91-b010-9f3ebd7aa71d | -6.1039 | -43.9824 | 2024-11-06 02:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| eb699452-5608-322a-924a-90d839aee657 | -3.2415 | -53.3967 | 2024-11-06 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 5e7b3b4f-107b-3ce1-b610-4dc910ae25e0 | -3.967 | -48.15 | 2024-11-06 02:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 23396eed-4090-369e-b641-0f9325a3ff36 | -2.706 | -54.1556 | 2024-11-06 02:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 7c7481d4-1eba-3b4b-bbd7-5d082005a057 | -3.0607 | -52.5066 | 2024-11-06 02:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 211e8f68-40d3-399e-973a-eb10bd9ebba7 | -6.1416 | -43.9563 | 2024-11-06 02:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 0610ba0c-ecab-351f-9463-679c44e1bf4d | -3.0213 | -53.2607 | 2024-11-06 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| d8c47c69-9a03-3b08-97e9-d7186e2a18c7 | 3.6 | -51.3168 | 2024-11-06 02:30:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 07ad3288-beb0-3280-98c0-bb4c72b570f7 | 3.6184 | -51.3162 | 2024-11-06 02:30:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 16a158c1-2b48-3f04-be4b-eef20186ab22 | -6.5094 | -44.6847 | 2024-11-06 02:30:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 3c92017f-eb39-353e-865b-90927cb40a46 | -3.0794 | -47.7727 | 2024-11-06 02:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 3cd24e48-6996-3d8c-9b90-be61d848387c | -3.0397 | -53.2603 | 2024-11-06 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| d84c5129-aac1-3a3b-86df-bd75160fca4e | -2.7243 | -54.1552 | 2024-11-06 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 59154d95-ee29-3430-a12e-99e2baf9cd96 | -2.9554 | -51.0668 | 2024-11-06 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 24e5303d-3384-3842-b1a5-b8cfe4c411e0 | -2.8424 | -51.7529 | 2024-11-06 02:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| d66b0f00-8cf8-374c-a009-2080a35b9449 | -2.7244 | -54.1351 | 2024-11-06 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 2595388f-cfcc-3c33-98a4-caa43d86abb7 | -3.0396 | -53.2805 | 2024-11-06 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| b6b9f3fa-ac87-376e-99cc-c69fb20dd8a5 | -2.6764 | -51.8395 | 2024-11-06 02:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 0c126c82-54aa-3e46-8f0b-4c456a5701d3 | -3.1433 | -50.2044 | 2024-11-06 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 9bc2da3b-b32d-3e7f-8a99-b6f4148b330e | -3.1213 | -51.1036 | 2024-11-06 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| d6b15354-2879-367d-8b2a-bd9060d95c60 | -2.8065 | -51.4855 | 2024-11-06 02:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| c6428834-5046-3787-8d06-fdae5c55b736 | -2.9555 | -51.046 | 2024-11-06 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| f14c989f-6ca1-3b77-b50e-29b83448c0a7 | -3.1616 | -50.2248 | 2024-11-06 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 3b4f0f8d-53e9-36c6-9786-89b24728dfd8 | -2.8607 | -51.7937 | 2024-11-06 02:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| cf571d42-04e4-3600-80fb-ecde198daaa7 | -3.1802 | -50.2032 | 2024-11-06 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 1948168c-e7fd-30fa-bce1-d263f348b529 | -6.5014 | -47.4813 | 2024-11-06 02:30:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 238.5 |
| a1398272-89cc-3a93-875d-9b684f955a43 | -2.8506 | -49.4744 | 2024-11-06 02:30:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 1114ae60-bc65-33e4-b4eb-64d694ef05e5 | -3.2349 | -50.3695 | 2024-11-06 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| a55c5040-2e73-33d4-890e-527f31a4206a | -3.0023 | -53.4434 | 2024-11-06 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 10859776-f475-32f5-950e-6328f9e75015 | -6.1226 | -43.9809 | 2024-11-06 02:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 7f0e8af5-b201-3e73-abbb-366bf8370a2b | -3.3285 | -50.0723 | 2024-11-06 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| e6483153-b56f-34c1-be66-409a82d47bd4 | -2.9185 | -51.0678 | 2024-11-06 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 5374c592-ce9a-3a6f-91fb-1b69b973b1de | -4.1246 | -43.5833 | 2024-11-06 02:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 0755d3de-1cd3-3f81-abd4-a6acbe0aaef2 | -4.1432 | -43.5822 | 2024-11-06 02:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 8eaeb44d-b35d-392b-8c8b-27d4b67eee66 | -3.2164 | -50.3701 | 2024-11-06 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 7c5130b7-e938-3674-adff-f3a4817f2801 | -4.5614 | -48.0141 | 2024-11-06 02:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 2efc18df-aa44-32e5-85d5-f475f06d3a60 | -6.1229 | -43.9578 | 2024-11-06 02:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| fb5f7e54-63fe-38e7-85ac-c49b03153811 | -6.4906 | -44.6862 | 2024-11-06 02:30:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 60f0ae94-c5b9-35dd-9161-e6d8dfba0bc6 | -6.4827 | -47.4827 | 2024-11-06 02:30:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 153.6 |
| c958d720-0b67-3889-a27f-53df12fe279c | -2.8608 | -51.7731 | 2024-11-06 02:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 148.0 |
| a9addd51-7729-3d59-a9d0-4ae9b3fe7ddf | -6.1041 | -43.9593 | 2024-11-06 02:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 362979cd-dee5-328d-8b69-e1ee6c04a3bb | -2.937 | -51.0673 | 2024-11-06 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 3cbe3b0d-1020-3065-b8f3-4cd3b8354aeb | -2.6764 | -51.8189 | 2024-11-06 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| ef4c25dc-29fa-3bb9-88fb-dd2bbc169aea | -3.0207 | -53.4227 | 2024-11-06 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 7eeac42b-0663-3d65-ac0a-3ebf2c450125 | -2.8064 | -51.5061 | 2024-11-06 02:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| f10d1799-b167-37d4-a35d-9551a93624cc | -3.2348 | -50.3904 | 2024-11-06 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| cc75e6ce-c865-38f1-a653-396ee300567a | -2.8423 | -51.7942 | 2024-11-06 02:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| d1399554-54fe-342f-a782-07227b650e80 | -3.1617 | -50.2038 | 2024-11-06 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 3e0ff474-d2c1-320f-8126-4e7963271407 | -3.0212 | -53.281 | 2024-11-06 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 8ab97baa-4aef-3347-8b03-813c767a84dc | -6.5012 | -47.5033 | 2024-11-06 02:30:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 178.7 |


[Clique aqui para ver as próximas entradas](README19.md)
