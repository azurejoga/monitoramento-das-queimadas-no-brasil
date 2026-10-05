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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09ba9e01-8bc9-3db9-b8c3-7cfe77b6d1ff | -2.81159 | -54.12733 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28005d91-aea7-3c34-a4e3-710380bbecfc | -3.47366 | -50.10189 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da516f42-7d68-3363-80d3-b9c62f520595 | -5.84451 | -53.82327 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dd326fe-0490-3292-851e-15e915c88c83 | -4.11235 | -49.07382 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5cfb51d7-6d8c-356a-9251-c4460315a9d2 | -4.11531 | -49.07854 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bf03e1a-f5b0-3e4e-bc3f-8b04fbea640d | -3.2727 | -50.40319 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 04555a9b-d298-3ad7-a349-3f3d6669f4f5 | -3.11753 | -53.74976 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 61888c05-dfd5-34d1-b7d0-9c765a222521 | -1.7629 | -55.03374 | 2026-10-05 04:57:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5178e1a-118e-39b9-a293-4d3975515153 | -3.12896 | -53.72171 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a960bed-6d4f-3e3d-809f-b327c3b49b1e | -2.9174 | -54.12401 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 14fc53d3-50fa-32b3-b1e4-7e451bbc6f86 | -3.27504 | -53.81938 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c711d54b-81c5-3540-a21e-6fedd18cd9b2 | -3.01899 | -54.18971 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38f3a728-ac35-38ea-afa4-46bc39dee49c | -2.80772 | -54.10743 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd79b768-34a8-3bb0-92d0-20e5bcfd5215 | -4.11301 | -49.06964 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3ce1bba7-967b-3214-898d-a2b3fb78eded | -6.17705 | -52.75871 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c20dc48-6400-3b62-86a8-a2156c142626 | -3.84696 | -50.31385 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d2413313-3eb2-3560-99ac-7e58c3c9dc51 | -3.0064 | -53.87519 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8a9b3f2c-348e-3755-b82a-a4d0549b9679 | -3.15865 | -50.43753 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0166f8ec-fa05-3c17-b68d-f9d6a584bbdb | -2.94628 | -54.18658 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a82bbfa-0e55-3322-8219-18f2e0f082c7 | -3.80444 | -55.65875 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d503869a-e6de-37ea-9424-3d8edde55993 | -3.61438 | -50.97705 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f858c3cb-ff18-3e6d-886e-ea67aae11471 | -8.66421 | -54.56874 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8892f465-2860-35ed-b8f7-8b59d42432e6 | -4.30607 | -50.78734 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 867bbafe-0834-3f22-9ef5-fb4e1058e5ea | -6.08277 | -53.47915 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c086cdf-4fde-34d0-ac88-d70c9c33619d | -3.11579 | -53.76069 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 71249666-aba8-3881-8441-d3c37b69bbc8 | -3.51272 | -54.61043 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12aef2f2-82a5-311a-8027-beb49fc0472e | -4.06114 | -54.31614 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 21408842-0b09-3e16-88d6-744679d2e5bd | -3.84412 | -50.30956 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7356a4a2-c09d-3af5-9094-e73fb87941e3 | -2.9698 | -54.10544 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a08dcd04-e5b4-3052-811d-fed972688b92 | -6.1675 | -55.3791 | 2026-10-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80b5486f-e2ad-32dd-91d5-417123f44db0 | -2.90748 | -54.14172 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d1dfefb-e39d-3c59-90a4-2392435c0fec | -3.04748 | -54.23294 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63fae0df-8436-342d-b603-6f4303f0cfe4 | -3.04523 | -54.22483 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7ac122af-f693-3896-8804-30a2a56ac541 | -2.8134 | -54.11604 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a779567c-0753-3a23-9184-e453b10561ea | -3.70274 | -50.65424 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 053eb4d2-f5a9-33b6-8ad5-39bbe15b945b | -2.9484 | -54.12899 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0ee81ba-9f18-3a33-a130-cf8edd417590 | -5.6159 | -57.23081 | 2026-10-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aeab76e6-c679-3d7e-a7a9-825e75f7f755 | -2.987 | -54.10817 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95c8447c-cea4-358b-bae9-c7581d58a9e8 | -3.12316 | -53.75813 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 4ccbbeee-6803-3527-9ec8-36407a666fc5 | -3.04134 | -54.20488 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25e60794-b4d4-3a76-b3d7-6c5bf15bb971 | -2.97159 | -54.09419 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 309e6c33-e93a-3d99-b5e5-ea44d37a313b | -2.7911 | -54.10095 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80bab810-f136-38e8-aa35-cbd176ed1d3a | -6.05561 | -53.47843 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b062bb6b-8e8d-33ec-9c44-28f79b41c93f | -3.1216 | -53.72427 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff6ff04a-94f8-38ff-a83a-6c030336e12a | -2.92713 | -54.12943 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2db11c39-a1b7-3d1a-9535-298c6e85f092 | -3.08468 | -54.17701 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| c0f71e6c-91fc-396b-b5c1-8f5503db2868 | -3.57176 | -54.65088 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33014927-ce9b-3509-9dc6-9653462de960 | -2.81582 | -54.10101 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aff251fd-4400-3e89-a94d-77bb36932cd5 | -4.07856 | -48.95675 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b63094c-d585-305a-a55d-e8e09b61be6b | -3.11713 | -53.70865 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a35dc439-1c2a-3817-9742-d5a2200e30bb | -6.9123 | -43.67092 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9e79b8a7-81cc-337c-ac8c-5fb5c6b51d5d | -5.98981 | -53.63638 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 52ef6bfd-9217-3f79-852f-835047221b51 | -3.84754 | -50.31012 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b826518-f8d7-395e-86c6-9de5f752c280 | -3.50511 | -54.61317 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8698c22f-1841-3f7b-a6fa-07ab45ffe58b | -6.62896 | -52.99348 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 13f569c9-2de5-3449-9117-8f429ecc57c2 | -2.99759 | -57.78899 | 2026-10-05 04:57:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b9ef583-b883-3e7a-a95b-46b2838f9c18 | -1.60415 | -55.41221 | 2026-10-05 04:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| adad4a21-e683-3704-b8b4-8f1650994ecd | -2.89552 | -54.12824 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46045ef1-e633-30e9-b13a-0f749daac1b9 | -2.81443 | -54.13165 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 129c5628-f64a-3766-b021-5889f12000b3 | -3.13517 | -53.72643 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 8dc99732-37fd-3d6c-ba69-2019063085b7 | -7.42772 | -63.5633 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5562737a-d9e5-358e-b2cd-7bcb335c3188 | -3.11878 | -53.72009 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ef98130-2720-3c9f-8684-36edc34a4367 | -3.90369 | -49.71032 | 2026-10-05 04:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cb741be1-8070-3740-b5fc-86d6a4db871e | -8.53065 | -54.59503 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eade556a-6f62-3880-a765-60bd0dc037c7 | -8.23003 | -47.86327 | 2026-10-05 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 375c8402-0086-35de-8129-e6b3deb8e4a6 | -3.10851 | -53.74086 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6c5843f-5cc8-3eca-b318-616f781e52fc | -2.99351 | -54.75283 | 2026-10-05 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cafbb830-4129-3f4c-817a-10d3dae5163b | -3.22461 | -54.30709 | 2026-10-05 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55de5e57-976a-3926-9a82-3cbbf91c9904 | -1.47294 | -54.77948 | 2026-10-05 04:57:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 294234eb-1120-36ad-a425-5dddc9d33d8f | -3.11704 | -53.73101 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9142cfe8-394d-3e24-8451-5f7418ae3ef7 | -8.53019 | -54.57652 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a60b714-9f45-355e-8ed4-162e81358636 | -3.19185 | -54.09798 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bfc2c226-ac0b-35f9-88c3-9a5d204949be | -3.12954 | -53.71807 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| a642f876-52ba-3e2c-939c-a69190138b90 | -2.96516 | -54.11243 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7559ac53-64e8-3181-9d5a-4774852616e6 | -3.11637 | -53.75705 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2dd04c20-4409-33ee-ad8a-bf05257c3566 | -6.64729 | -55.32567 | 2026-10-05 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e653169-7e69-36dc-b63f-f10d82240837 | -3.10511 | -53.74032 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 153692c5-9a7b-3cfd-aa0f-7d3df7d6e9f8 | -9.23523 | -46.68359 | 2026-10-05 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f63dcc58-e479-3894-a7d8-31fe7803383f | -8.67495 | -54.54474 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a61c9025-d909-3c70-9243-4f081e0a6654 | -7.22708 | -55.19169 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70331484-a464-3541-9c67-39a57aa14eb8 | -3.01147 | -53.8873 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ec86913-0c53-39ee-af5f-a4fa6a6212e5 | -2.85417 | -51.57955 | 2026-10-05 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 904352ee-1bf8-3883-9304-17002e76cf91 | -4.46794 | -54.97571 | 2026-10-05 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c87ba9e-60a6-3068-8568-f0fd734bf193 | -2.48651 | -56.09029 | 2026-10-05 04:57:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6174b0e6-6037-3e8b-8a9d-273d6f7e0c04 | -3.71699 | -59.68908 | 2026-10-05 04:57:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af7be5f5-cee2-3b45-9ba2-b42ef0c2892d | -2.81117 | -54.10798 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a73e973-d20a-3145-a989-e1733a282f2b | -8.67207 | -54.56267 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8442fcb6-36e1-3035-ac4d-3da2fc3bb643 | -3.51908 | -54.61544 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0184e7c6-a904-3a5b-8e02-6b48b17737d1 | -4.1244 | -53.81079 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 967c154c-b53b-38d5-8da5-32a360bba960 | -3.92219 | -49.71228 | 2026-10-05 04:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e974d6dd-6f16-39a3-a2c9-a71046f48397 | -2.81806 | -54.10907 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56c279a6-4a10-3d0a-8fc9-98f0063928b4 | -7.45163 | -63.56358 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d78573d-44de-39a6-9529-e9aac10b16c8 | -6.87818 | -43.67995 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c67b35d9-8538-35cc-8cb5-4324aa34127e | -2.95289 | -54.14514 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| cd9bd142-7ca5-3ef4-872b-4d3e493b4644 | -3.11132 | -53.74504 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90d69aca-5177-3916-aaeb-efb216b87f53 | -5.99658 | -53.52964 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc7d3ccf-443f-3f95-817e-f0d63551fbc6 | -2.84802 | -51.29483 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 343a0984-97a0-31a6-9a06-b6984422a4bb | -2.91009 | -54.10363 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2f3450a-0ded-3896-b67b-62a9bd0e7724 | -2.85598 | -53.91652 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2c8e2a2-1c41-32c4-8576-feb0106e04a1 | -3.21578 | -48.97188 | 2026-10-05 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README32.md)
