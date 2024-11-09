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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 964a1611-0375-35ec-8364-5c7e9ee8db38 | -3.66443 | -50.26006 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8ab8af1-6238-32bf-bb82-2a0f2abee954 | -2.97797 | -50.2965 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1041d962-22a9-3b1a-a15d-c26fea098bc7 | -3.18421 | -51.12016 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc40ab56-4cfb-37fa-a423-bcbc23244f91 | -6.3132 | -42.75401 | 2024-11-09 04:33:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ee8f1831-3fd8-3392-8e84-ba89cda94e8d | -2.82399 | -49.43395 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9d6a34e-ebd0-3d8e-bdd1-fd63ebb5d1be | -4.19907 | -48.39815 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 588be839-e95c-3c4d-aed7-2e705def0084 | -4.267 | -46.91681 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 246f7458-88a6-3fb2-91cb-08bdea9ec1ad | -2.97195 | -51.4503 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1b310fd-2e09-3199-8575-cb6ed4515f55 | -5.65073 | -42.72818 | 2024-11-09 04:33:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 438dafe5-2c9e-352c-910e-7f9e9d44471e | -5.04017 | -45.87322 | 2024-11-09 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16087acc-3bec-30dd-a8c5-5a353044d251 | -4.83753 | -45.63914 | 2024-11-09 04:33:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| beba7f14-8cb4-35fb-8b7a-2c21869d8ac9 | -2.67059 | -50.95679 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f06ebebc-ba16-3475-8b91-7310cd136cc7 | -4.11551 | -46.88634 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64a053fd-28a6-3f8e-ace2-d7cde5220f2e | -3.97194 | -48.17672 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 40044af5-c22e-3049-9156-45e879d5d1c7 | -3.38357 | -50.22664 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a074e28-577c-3220-81f4-5bf75d4a79c5 | -3.07573 | -50.56173 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9900dc5f-4f7e-35e6-a12c-c9e7240da0dc | -3.81595 | -50.78657 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1f8bdea1-cd83-3a05-b7a3-bd987a6d7674 | -3.24904 | -46.46394 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e3c8b28-16d6-3f23-a33b-217a2429cde8 | -3.97361 | -48.18764 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 69e84d8a-c3ad-3ed4-8662-a31ba2ec34fb | -2.87187 | -51.47037 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ebb21446-a4cc-35b7-bbee-bc20a7b4df1c | -4.01984 | -46.187 | 2024-11-09 04:33:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04538861-5882-3796-b318-17842459f219 | -4.38893 | -48.57542 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7920c403-dff5-305c-b9da-7f9f5db05c09 | -7.0103 | -45.61811 | 2024-11-09 04:33:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 859cb590-15cf-32bd-8825-f062ca8d7ecc | -3.98334 | -49.49622 | 2024-11-09 04:33:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3ba36a78-25a1-3518-bc63-ad5685203863 | -3.11566 | -50.13346 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 993aa43b-62db-3f48-aece-9c5861638c80 | -4.37352 | -48.17574 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1542930a-a45b-31f4-a26a-8dd483a22936 | -4.14146 | -46.89392 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c613861-6909-3146-b123-d86ee642165f | -11.08588 | -43.3345 | 2024-11-09 04:33:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05c4ad8e-9952-3619-9005-b726dd5ca29e | -3.16056 | -54.47807 | 2024-11-09 04:33:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8c80bb6b-a7c9-3018-a3ff-b24ebf35c72b | -3.64819 | -50.13535 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2572c0e9-d3e7-34f3-a96d-4eff68e9b288 | -4.08061 | -48.32962 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62865121-67bb-37c0-927f-b3cad1fca6af | -3.54037 | -51.02976 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a7bc7e0-5bca-3d74-b80c-358a784967ed | -4.78454 | -48.67711 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1645fd6-5890-31c4-9dfc-eb6c9714936f | -3.74723 | -51.0958 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7af8df99-0585-3d17-ae9c-5ae8ba527c1f | -3.06497 | -48.05911 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 37e1f27b-614c-3d7d-8951-e37411567590 | -3.1813 | -50.58126 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb5466a7-f708-3c89-a448-99f9268a2e13 | -2.79639 | -51.5963 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b918b580-b07c-3549-a6cc-01d192a82379 | -3.88413 | -49.94954 | 2024-11-09 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1ddfa396-8fb6-309d-a90b-b773660c0418 | -3.15195 | -51.12175 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b7a5099-f462-3c7e-aeaa-aa00fea6da35 | -3.08095 | -50.57562 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 878998c0-8527-3c5d-b2be-9eb2855ae3d4 | -2.90137 | -49.23416 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2893233f-4515-337f-b810-83ac1c4b731e | -3.19197 | -48.6598 | 2024-11-09 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4a4f98a-18d2-3a0d-9291-81662dbddffb | -3.65476 | -50.13966 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8259b3ed-ef0d-3bfa-bbaa-eb6f1459b88a | -3.04407 | -50.35627 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67789ef2-2d08-3446-a805-338ef48e6429 | -3.83495 | -48.87749 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4f2b2d4-0b55-3f5a-8ef4-a3a9296d7959 | -4.20202 | -48.55309 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6c73d27-e498-3c34-ae9b-77797952e1d3 | -3.85307 | -49.89689 | 2024-11-09 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1379f138-88d0-3526-ae0d-d1ddc22b3621 | -5.98681 | -45.36783 | 2024-11-09 04:33:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2926746-071a-3c39-89f6-d98778583fed | -3.96128 | -48.13587 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bc494cb8-019d-315e-8d60-e32d32afd55b | -4.15085 | -46.89891 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0538a10b-ba77-3a69-9370-6b1bd8e24cbd | -3.06832 | -54.77793 | 2024-11-09 04:33:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 57567919-9b02-3de7-9312-b270b2084566 | -3.62054 | -51.54464 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c2303d0-7ac5-333a-aa23-92044e5de0d9 | -9.26465 | -43.19822 | 2024-11-09 04:33:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cf99f691-8ab2-33fe-b68b-2d481dbec36d | -3.3244 | -49.9126 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4765c4fe-b915-3614-8293-f6145ad0c8bf | -2.98595 | -53.20689 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 940a7d10-7c16-3519-a1d2-c7f1a1b11b14 | -4.54202 | -48.64245 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 46ea605c-bfe9-3b44-a3b6-d8557f611f4b | -3.11693 | -48.64109 | 2024-11-09 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f90b3258-299f-3b0f-945a-b6f6c1c9da37 | -3.96753 | -48.18314 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 07eee464-f16e-3c09-a668-4430158f86f6 | -2.85345 | -54.10509 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bab93d5-db29-38bb-9793-4b5586f41040 | -3.61012 | -48.92323 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a91ed0d8-264c-318c-aa59-d26439a2e75a | -3.16795 | -49.101 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa25cb85-0379-3a80-8da8-7342b878828a | -3.24417 | -46.4952 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d07d6efe-0068-3c70-a877-0a9951b84df3 | -3.53562 | -51.10632 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e07e2183-fb28-3fae-9d75-e6c87409ba68 | -4.20882 | -50.62585 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9596c673-77bd-3f16-b073-69cc7ae42c59 | -4.22663 | -48.61091 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43b26536-eadb-3710-8a9e-b4edede88772 | -3.68235 | -51.30575 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5137469b-4fe1-34d8-8642-65b2cc92e672 | -4.44048 | -43.64521 | 2024-11-09 04:33:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bd6f2e4-66c7-3eb4-8cde-f6711bda45d0 | -4.37629 | -48.17973 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9dbc395a-ca5e-335e-bc56-536c8561b4f6 | -3.90887 | -46.134 | 2024-11-09 04:33:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35255e3b-5b73-35de-8d60-1296f513c775 | -4.08171 | -48.32264 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eba7d2ea-3e7d-3de4-b1f5-f1f179bafb88 | -4.01752 | -48.2978 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7a950548-6dec-3b46-a042-d49bf63cf461 | -2.8748 | -50.41191 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3b09d3a5-ef82-3db4-863b-1b3c2f801238 | -3.88951 | -50.23657 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3dfd6766-99d8-3e6a-bf7e-3d8920959b49 | -3.63372 | -51.81887 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd50d279-5019-3d84-be06-99f944df5d31 | -3.23526 | -50.45243 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65e74b69-95cc-33cb-afc9-98bd7950236c | -6.49834 | -39.55558 | 2024-11-09 04:33:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| aec87d5f-cb3e-32d0-8882-c67a26cdfc25 | -3.55259 | -47.38011 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3489d637-4fa7-30e6-b618-37fe4ef0492e | -4.39764 | -49.84994 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 189ff1a7-4d87-36e3-b46f-5401e2ed0e57 | -3.09821 | -53.31974 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d846a369-9606-3955-8bf2-f87a2af584d9 | -4.63205 | -46.53797 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03693677-fac1-3348-832b-f184b5f5caee | -2.88916 | -51.74435 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 1314457d-c295-3401-8f04-923544dbdd06 | -4.26754 | -46.91334 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5588f4e-8ece-3e34-982e-f23b4dfdc437 | -3.28011 | -53.67511 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 627b75aa-bbf1-3086-9657-d0568b182f20 | -3.95635 | -48.14573 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0e666f73-f5a1-3d84-9073-37e6d320f08c | -4.08976 | -48.8514 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b122fa5c-de92-3132-b817-65bddf2df3c5 | -2.91874 | -54.19541 | 2024-11-09 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53e185d7-390a-35fb-a131-6e385e6a9fd9 | -2.97711 | -47.92456 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 399e9a17-9074-3b9d-a41d-08f3d447f36f | -4.13984 | -46.90428 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 677fbfdd-c9a0-3ad4-aa4c-2c2c6645c482 | -2.8464 | -49.44908 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94859511-02ad-3f9a-8fd8-b49d2ffd9d7d | -4.40731 | -48.61066 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a22242b-a8fd-3f4f-a816-5f39b4e80b0b | -6.92985 | -50.33196 | 2024-11-09 04:33:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5aa2a29-41e7-3163-bbff-7c852f491db1 | -5.58942 | -42.80867 | 2024-11-09 04:33:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ae10ede5-b87b-392d-ac76-ae470764cc6a | -3.84958 | -49.89635 | 2024-11-09 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b58a9ba3-5928-3f80-b42a-fb1a1e2cf875 | -3.97964 | -49.98782 | 2024-11-09 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f1e1e99-b334-3eb3-86c7-7d64c5987cf8 | -4.60963 | -49.57804 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6b1b1293-769f-3148-9192-b0e51227e830 | -6.69216 | -48.90026 | 2024-11-09 04:33:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8b944ec-aaae-37ad-8fe5-9aa1ec33a0b2 | -3.23887 | -50.453 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08e70447-4c10-399d-af08-a2b8d087a936 | -4.21488 | -48.68498 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 6878f317-889d-3475-91f9-670ce95cf584 | -4.39494 | -47.64933 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f0e6840-ad63-36fc-b90e-99bf2dcf3635 | -3.24248 | -50.45357 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README56.md)
