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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80c8c234-acc2-30b8-88b7-1eb910f036e4 | -16.53122 | -57.74467 | 2024-10-07 06:31:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.7 |
| 62ca613b-fd17-3aa4-8255-4a9aae4689a0 | -17.18157 | -57.31314 | 2024-10-07 06:31:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.0 |
| c670178f-f11f-3357-822d-6c5a273cca1c | -17.17844 | -57.34303 | 2024-10-07 06:31:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 131.0 |
| 109a8040-712b-39b5-b3e5-d8dd020884ea | -17.16331 | -57.34135 | 2024-10-07 06:31:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.0 |
| 6c6704cb-1dfe-3b7c-a285-9a1ac7be449c | -17.13107 | -56.82182 | 2024-10-07 06:31:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.4 |
| 90c6c3da-0c97-391a-8ccc-740d6c3c0c19 | -17.11419 | -57.38836 | 2024-10-07 06:31:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.8 |
| 8ff3d465-94a7-339d-bd98-c91526ef8455 | -16.97116 | -56.73099 | 2024-10-07 06:31:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.3 |
| 57400213-edb0-30a5-910b-6bd7735ae29b | -16.96779 | -56.76385 | 2024-10-07 06:31:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 205.1 |
| 106edf1c-4ee0-3d23-90c1-4ffba05bf239 | -16.81057 | -57.39714 | 2024-10-07 06:31:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.5 |
| dcd3a087-63e1-33e3-ac8c-7eb78c8dbdee | -16.79742 | -57.38802 | 2024-10-07 06:31:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 249.7 |
| d016008d-ba42-34c9-88ad-c84f9c0d7d0e | -16.79558 | -57.39547 | 2024-10-07 06:31:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 273.2 |
| 50a4ba2c-a2f7-3160-8087-926866d9a968 | -16.79416 | -57.41702 | 2024-10-07 06:31:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.9 |
| c21cea19-4d7f-3fcf-9ebe-eb0c16946658 | -18.66475 | -57.2298 | 2024-10-07 06:31:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.5 |
| 175c92b9-ac57-3826-a131-0ba5a024b89b | -18.65317 | -57.22391 | 2024-10-07 06:31:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.0 |
| e2132016-5d04-3bf0-9a0c-adcd42c8355d | -18.64995 | -57.25588 | 2024-10-07 06:31:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.3 |
| 4ac79440-1a73-3b74-91c5-a52b0205186d | -18.63441 | -57.25426 | 2024-10-07 06:31:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.0 |
| b24601dd-14ff-38d0-86eb-124c034a21b8 | -10.59883 | -64.40938 | 2024-10-07 06:31:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b215a4fe-a380-3df8-b3fd-090779882bfd | -10.34469 | -64.26088 | 2024-10-07 06:31:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 603c059a-722e-3532-b4e2-6e191fc42fa4 | -11.69739 | -64.03222 | 2024-10-07 06:31:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 14.9 |
| bd52f581-30a7-3603-8081-ea3db900beac | -11.00467 | -63.91459 | 2024-10-07 06:31:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fad34171-1480-34f1-a956-53d341d0380e | -10.92616 | -63.88714 | 2024-10-07 06:31:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 182ba2fa-b0a3-3ef7-bd41-4393f7344e57 | -10.9212 | -63.85884 | 2024-10-07 06:31:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0b4e6f7f-a997-3a1e-a1f0-325149fe11cb | -10.91986 | -63.86795 | 2024-10-07 06:31:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9ad13378-c47a-3080-8453-4a10519358b8 | -10.88697 | -63.89444 | 2024-10-07 06:31:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b447642a-f200-310b-9d73-e50f1ae7ac0a | -10.88562 | -63.90356 | 2024-10-07 06:31:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 0c1ff2a7-9ee3-33c4-b7f6-0a4da4d29e45 | -10.88429 | -63.91259 | 2024-10-07 06:31:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 50e35586-c19c-3be3-8048-28a23cc2f0bf | -10.88294 | -63.92168 | 2024-10-07 06:31:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 31ae1255-0c6b-3bf2-ade2-262db95e8d80 | -10.87807 | -63.89301 | 2024-10-07 06:31:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 02acc182-cb6b-32b8-b411-24a9101111f6 | -10.87538 | -63.91127 | 2024-10-07 06:31:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 2bfd89ea-c095-33b4-9eac-d7ab36181035 | -10.85574 | -64.16674 | 2024-10-07 06:31:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8fc81925-9955-3b19-8619-60f8316f24b9 | -11.53833 | -65.04035 | 2024-10-07 06:31:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 16f3279c-c140-3bb1-aa4d-8f932768739c | -11.52136 | -65.09293 | 2024-10-07 06:31:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bd436ebc-9218-3cd2-bc9c-2775bfa9fe2e | -11.67005 | -65.21095 | 2024-10-07 06:31:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f56c2e62-2454-3f65-bb40-5dd1f1f73d8d | -11.53698 | -65.04934 | 2024-10-07 06:31:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 5f2d9a39-6f45-3190-8fbc-b7dacc89360e | -11.52001 | -65.10192 | 2024-10-07 06:31:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fe687b2c-c50a-3654-ae95-6bdf0afeb1dd | -7.69296 | -73.0637 | 2024-10-07 06:33:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db2e3fe0-3c23-3cf1-b9b9-6a2a3f3f131c | -7.4694 | -72.68353 | 2024-10-07 06:33:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 500c21b2-74c9-37c4-bfa6-70504c814e20 | -7.46885 | -72.68733 | 2024-10-07 06:33:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90960bb9-df66-32b3-8d7a-facaf94d43cd | -7.46523 | -72.68301 | 2024-10-07 06:33:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8fb048f-e1c6-306d-b02d-dcae681e575b | -7.46468 | -72.68682 | 2024-10-07 06:33:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe45c40f-7cfe-3145-a540-c10217754746 | -7.34964 | -72.90623 | 2024-10-07 06:33:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd84f862-1ad8-37d0-9362-9056da7d3564 | -10.82722 | -68.36033 | 2024-10-07 06:33:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3dff0191-7803-38f2-8493-01781346a897 | -10.39571 | -67.89079 | 2024-10-07 06:33:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 986d104b-5993-3b94-be66-0d26258f7b84 | -10.39244 | -67.89073 | 2024-10-07 06:33:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 76dd42ff-745f-37f8-b3ce-8dc11149b6b8 | -10.38972 | -67.88995 | 2024-10-07 06:33:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0c587b85-a7e7-3eff-874b-e10efeee325e | -10.0397 | -68.4624 | 2024-10-07 06:33:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2664066-300f-38e6-a47c-0a959a411c87 | -10.0392 | -68.46638 | 2024-10-07 06:33:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d9f2732-4c45-33db-9c62-acdc265bd2de | -10.8754 | -63.9169 | 2024-10-07 06:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| f0532525-c11e-3a1f-9810-7a4dda4ae698 | -10.8755 | -63.8979 | 2024-10-07 06:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 92fe97f1-18b2-3e6e-94c6-cca791ae55ae | -16.4753 | -57.2735 | 2024-10-07 06:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.0 |
| e4836a7b-0c60-35d9-be5a-332a147f477d | -16.5072 | -57.7387 | 2024-10-07 06:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.0 |
| d8abc9a0-1afa-3564-af72-d2c20a2b795e | -16.5075 | -57.7183 | 2024-10-07 06:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.1 |
| 5f3be745-c207-3346-b4be-c8b5071389b8 | -16.5264 | -57.7569 | 2024-10-07 06:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.8 |
| a4e64bdd-4bbc-36f4-ba50-817e1ef5fbf3 | -16.5267 | -57.7365 | 2024-10-07 06:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.0 |
| e460c7a7-940e-3e14-b132-8a853e46cdc0 | -16.527 | -57.7161 | 2024-10-07 06:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 59e25e48-dcbc-3ef4-95e3-3cb4786a76a2 | -16.6136 | -57.1555 | 2024-10-07 06:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.8 |
| d03e1101-5885-3efb-9549-81d98faaef99 | -16.614 | -57.135 | 2024-10-07 06:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.5 |
| 19420b58-56f4-310d-8ad3-b355e141e522 | -16.6332 | -57.1533 | 2024-10-07 06:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.1 |
| c02eeba0-d194-37af-b5ab-8f4ee450af7a | -16.6335 | -57.1328 | 2024-10-07 06:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.1 |
| bc9e6174-3018-3f24-b378-f587e629322c | -16.9521 | -56.7669 | 2024-10-07 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.4 |
| 61e9f2cf-5974-35ef-bf9b-bc36cc0bc122 | -16.9524 | -56.7463 | 2024-10-07 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.5 |
| c7823574-8a83-3d74-85c7-92902dbf2380 | -16.9717 | -56.7646 | 2024-10-07 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 287.8 |
| e0fb0573-26a3-3aa3-855f-f43bfbbe5012 | -16.9721 | -56.744 | 2024-10-07 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 202.8 |
| 1290fac7-0a33-3130-b454-c8d1344320cf | -16.9913 | -56.7622 | 2024-10-07 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.3 |
| 830f9e08-9236-3cd6-963f-8035424f8284 | -17.1777 | -57.3559 | 2024-10-07 06:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.1 |
| 9477f634-5eda-36ae-94fa-4b1242be75ba | -17.0982 | -57.4267 | 2024-10-07 06:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| b11b92e7-6f4f-363d-87f2-fb32aa1c07ab | -17.0985 | -57.4062 | 2024-10-07 06:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| 7eaa48a4-20f3-39bb-90f5-d8def34352e2 | -17.1581 | -57.3582 | 2024-10-07 06:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.6 |
| ac244f81-3429-3ce8-a031-65cccef603a1 | -17.1584 | -57.3377 | 2024-10-07 06:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 152.9 |
| c5e44eb3-9e13-3b58-a168-b16d4333971f | -17.178 | -57.3354 | 2024-10-07 06:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 136.6 |
| cf34defa-5746-3863-8bf8-5e1969292ff3 | -17.7324 | -57.0833 | 2024-10-07 06:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.5 |
| 54d4f5f4-8ae3-39fd-ac7a-81e7828ae3c3 | -17.7327 | -57.0627 | 2024-10-07 06:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.3 |
| e2afd563-8181-39bf-b192-e4d48e09c887 | -18.6391 | -57.2578 | 2024-10-07 06:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 125.3 |
| 585b0ea3-4528-3d2f-9317-77fca7684e92 | -18.6394 | -57.237 | 2024-10-07 06:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.8 |
| 118039db-381e-3dab-9d11-f65faee7ffef | -18.659 | -57.2552 | 2024-10-07 06:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.4 |
| 54a0b740-f574-3eb0-afba-5f23a2f2a6b3 | -18.6593 | -57.2344 | 2024-10-07 06:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.6 |
| e533ae0e-1e73-3acf-9cab-e41014d2c059 | -10.8755 | -63.8979 | 2024-10-07 06:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 44778094-df5f-376c-9b34-c8d6a31f89da | -16.4948 | -57.2713 | 2024-10-07 06:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.9 |
| 2d261d90-62e8-3d6c-a710-d4da15f6d820 | -16.5072 | -57.7387 | 2024-10-07 06:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.9 |
| ab94f6d0-8717-30a6-b116-1cb3a25598fd | -16.5264 | -57.7569 | 2024-10-07 06:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.3 |
| 1cd9d530-31a8-3a05-b18b-a68a9b4ace96 | -16.5267 | -57.7365 | 2024-10-07 06:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.3 |
| 7f56fae4-8f33-3a35-8e73-9c5017b10085 | -16.527 | -57.7161 | 2024-10-07 06:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.7 |
| 8de7bac0-cf0b-37e2-905c-48cc1e8ff8ab | -16.6136 | -57.1555 | 2024-10-07 06:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.6 |
| f3666e12-dbee-355a-8862-5cf02ecf117c | -16.614 | -57.135 | 2024-10-07 06:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.3 |
| 9a7ab33f-8846-3bc1-b15d-07cdecf19705 | -16.6332 | -57.1533 | 2024-10-07 06:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.1 |
| 0b56ae70-baeb-333e-8a73-3d11d1fcb3eb | -16.6335 | -57.1328 | 2024-10-07 06:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.1 |
| d3cc9d3d-ad38-3989-9fb8-6fe673adaf73 | -16.9924 | -56.7003 | 2024-10-07 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.8 |
| d17cf99e-debc-3231-b745-749fdceb4e8c | -16.9521 | -56.7669 | 2024-10-07 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 2b842212-c01e-35b2-a622-90914827274d | -16.9524 | -56.7463 | 2024-10-07 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 04f74678-fddc-3e92-84f5-631242fba523 | -16.9717 | -56.7646 | 2024-10-07 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 123.3 |
| 31fb8dff-d4e9-34f4-888a-50d9f47ae684 | -16.9721 | -56.744 | 2024-10-07 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.7 |
| 740e7379-5216-35ab-9148-7be18fa97795 | -16.9741 | -56.6202 | 2024-10-07 06:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 49.4 |
| 6de7ec7e-43df-34c9-907b-6e62ccf5e70d | -16.9744 | -56.5996 | 2024-10-07 06:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 57.0 |
| c558e9a6-48e5-3fbb-a5f7-d0fdb0a4cb74 | -17.012 | -56.698 | 2024-10-07 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.3 |
| cdc88bc6-017d-33a8-b8af-582893282dde | -17.0123 | -56.6773 | 2024-10-07 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 177.8 |
| d403b8b7-3e89-371f-bed1-ebea56eb5db2 | -17.0316 | -56.6956 | 2024-10-07 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.1 |
| b61a7316-edb5-3bb4-b411-920b3f5d6d7c | -17.0319 | -56.6749 | 2024-10-07 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 205.4 |
| 8243e62d-4c13-32d8-a44c-338e60657821 | -17.0323 | -56.6543 | 2024-10-07 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.3 |
| 396213a4-fb32-3df8-aa67-7895c1ba9209 | -17.0982 | -57.4267 | 2024-10-07 06:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.3 |
| 1d4ecd41-58dc-37bf-b7ca-3ab9b4587399 | -17.0985 | -57.4062 | 2024-10-07 06:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.9 |


[Clique aqui para ver as próximas entradas](README143.md)
