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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9fa2615-7820-3c32-8556-7fae082ceeee | -15.12112 | -52.95514 | 2025-12-03 03:51:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dc1dc60c-9684-37b8-8362-025087df63da | -13.72545 | -48.74197 | 2025-12-03 03:51:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80505eb5-b42c-3993-9ca0-69c50834d8d1 | -15.11412 | -52.9538 | 2025-12-03 03:51:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ff998c65-efce-3d8e-bbb5-d6fabe687a26 | -17.88141 | -39.76982 | 2025-12-03 03:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fce7164a-b2ea-3081-96e0-ff04b58ee271 | -15.11698 | -52.96442 | 2025-12-03 03:51:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bd3f6b8f-e5f3-3849-8401-91374df74cee | -17.87809 | -39.76925 | 2025-12-03 03:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 23a0b75c-0ca3-3f18-b443-c9dbfc85091a | -15.11265 | -52.96047 | 2025-12-03 03:51:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fe4e6a4a-9a92-368c-9aef-7b69cdc41efc | -15.5768 | -39.03032 | 2025-12-03 03:51:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d99895c0-550b-3875-8aee-3842ba49b1c4 | -16.54079 | -45.13546 | 2025-12-03 03:51:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6233f0df-469e-3d49-91e6-2064e29d6ec5 | -15.11155 | -52.95615 | 2025-12-03 03:51:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e2616e26-c2af-3544-9fb3-ec00df6657ca | -16.28497 | -39.17039 | 2025-12-03 03:51:00 | NOAA-20 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ee44a61a-057d-3cf9-b770-0e0adf14a267 | -13.72399 | -48.74939 | 2025-12-03 03:51:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47cfaa8c-c81d-3126-ab30-2185e3f2922f | -13.72768 | -48.75014 | 2025-12-03 03:51:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94eb146f-432f-3c20-8b00-fdeec837357d | -17.88198 | -39.7662 | 2025-12-03 03:51:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a9d55ba1-7455-3ed7-963a-4f6880ead8f7 | -15.11566 | -52.9468 | 2025-12-03 03:51:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 08766659-906a-3059-b3e0-2f21ff2ce46b | -19.63871 | -45.29747 | 2025-12-03 03:51:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a5d5f22-81f6-3e86-8a8e-aa938741e154 | -15.11959 | -52.96211 | 2025-12-03 03:51:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| be5a9c9e-e233-37b0-bcf6-af64c728c2de | -21.18615 | -49.55709 | 2025-12-03 03:53:00 | NOAA-20 | MENDONÇA | SÃO PAULO | Brasil | 3529500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e7802647-a519-3736-a5e9-f97757901cb9 | -21.29101 | -48.55239 | 2025-12-03 03:53:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de6d053d-dfae-35cc-b5aa-f1758eb5e077 | -22.7285 | -49.3514 | 2025-12-03 03:53:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8adb44c6-3266-346f-a605-b6da88321f33 | -22.73003 | -49.35363 | 2025-12-03 03:53:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cef9fe7a-937a-3c2b-a293-b3a556024342 | -27.44573 | -48.44812 | 2025-12-03 03:53:00 | NOAA-20 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c9c9350e-db5f-31e4-a214-d3d0ea71672e | -22.11593 | -46.94012 | 2025-12-03 03:53:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a4beb05-f414-3ccc-a4d7-84253b529c7d | -22.12019 | -46.94101 | 2025-12-03 03:53:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a5a0b124-c1ba-3c08-94a4-bbfd655cabc8 | -22.11677 | -46.93587 | 2025-12-03 03:53:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9efa7ab2-a352-3b4d-b5e0-48fca9365260 | -30.50898 | -52.80282 | 2025-12-03 03:55:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 4be0de48-bec7-3209-b93f-f2f779f3bfb7 | -30.51298 | -52.8088 | 2025-12-03 03:55:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 45809cab-c1d5-3ca0-bcc2-d6f3a650c3fc | -30.51107 | -52.80456 | 2025-12-03 03:55:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| fc15d61b-a79e-3087-b6a3-a5edb1daece8 | -30.51007 | -52.80869 | 2025-12-03 03:55:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 26a9477f-0e77-38b4-92f9-7a122882122d | -28.06182 | -48.67291 | 2025-12-03 03:55:00 | NOAA-20 | GAROPABA | SANTA CATARINA | Brasil | 4205704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d1deadae-007f-3a0e-9eb1-c731ac8f34ea | -29.88291 | -51.21488 | 2025-12-03 03:55:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| bd20b7a3-2fea-3cb5-b321-74894204dfcc | -8.163 | -43.229 | 2025-12-03 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.7 |
| 84422536-845c-32ad-9219-95806e786012 | 1.9866 | -55.7408 | 2025-12-03 04:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 6bcbdfcd-90f9-38ca-a37f-59d227bd4861 | -8.1633 | -43.2055 | 2025-12-03 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.9 |
| cb3cedde-62a4-37ed-b2dc-f115e2742a75 | 1.9684 | -55.7213 | 2025-12-03 04:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 28718a98-4b88-3c9b-97ab-cde1ccfe6df7 | -3.2379 | -45.5615 | 2025-12-03 04:00:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 145.4 |
| c3c6f428-f54e-334e-a264-f71113bfe821 | 1.9867 | -55.7211 | 2025-12-03 04:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| ba61ea0e-a78f-3ad2-b9b2-6bf6ffa1ce47 | -3.2378 | -45.5839 | 2025-12-03 04:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 94a05a9c-75b8-3db2-87c4-9a752eb3f7e7 | -3.2378 | -45.5839 | 2025-12-03 04:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 40368b60-33ac-395a-b691-3c01b316e9bc | -1.2025 | -53.0907 | 2025-12-03 04:10:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| f4a68932-2194-3245-800e-856dfe57370b | -3.2194 | -45.5622 | 2025-12-03 04:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 5693c977-8142-3159-8a31-5603c36b39d3 | -3.2379 | -45.5615 | 2025-12-03 04:10:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 176.2 |
| 50336d59-bc8c-3cc5-8b5e-614dcaf10a76 | -3.2565 | -45.5607 | 2025-12-03 04:10:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 047306c9-8fa7-32d3-899f-b3a20db0c4d7 | -3.2378 | -45.5839 | 2025-12-03 04:20:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 106.8 |
| d4837c84-9d7f-3247-8ba1-e5d75c3da78e | -3.2565 | -45.5607 | 2025-12-03 04:20:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |
| caafa11c-87b8-3948-a442-a2486f4be3dc | -3.2379 | -45.5615 | 2025-12-03 04:20:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 193.5 |
| 73917696-99be-324c-b20b-0ed15870627e | -3.2379 | -45.5615 | 2025-12-03 04:30:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 161.6 |
| c875bac1-cc21-3cc1-a1e0-e46338fbf331 | -3.2565 | -45.5607 | 2025-12-03 04:30:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 86.1 |
| aa42469d-3f75-3ccf-9d51-b434a43de6e2 | -3.2378 | -45.5839 | 2025-12-03 04:30:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 0af7e0b5-fbfe-3c82-8510-461a0d765571 | -3.2194 | -45.5622 | 2025-12-03 04:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 23425176-7af2-361e-9ad8-2700df8cda18 | -3.238 | -45.539 | 2025-12-03 04:30:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 2770267a-1b39-3278-b321-940ae5432bd8 | 4.15137 | -59.93406 | 2025-12-03 04:36:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b990654-0e5b-36f8-94e9-3195cc74707a | 3.47766 | -51.25429 | 2025-12-03 04:36:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f38d5d45-f430-3871-905b-e4c1e71304f7 | 2.53317 | -50.83553 | 2025-12-03 04:36:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4217e741-6d3d-3204-a95f-b65d034d583e | 4.15808 | -59.93272 | 2025-12-03 04:36:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f859206a-448e-3beb-89eb-e8bea05dd11e | 3.67611 | -51.28515 | 2025-12-03 04:36:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39b334aa-300f-3113-abbf-c158fa11e5fa | 3.5412 | -51.44703 | 2025-12-03 04:36:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85fe4e84-2163-3bb1-86d7-bd7f0ad20f1f | 2.55575 | -50.8365 | 2025-12-03 04:36:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 85caef55-e0e6-3ac0-9945-491ee87a657a | 4.15408 | -59.93534 | 2025-12-03 04:36:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e1651dab-bde6-3c00-a8d9-692b9e610f70 | 4.15553 | -59.91526 | 2025-12-03 04:36:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 031927fe-3dc5-3458-a29d-b61877ac6f00 | 2.42529 | -50.86421 | 2025-12-03 04:36:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fc6cab2-6afb-3228-a329-f528dd05e3c0 | 3.48665 | -51.26237 | 2025-12-03 04:36:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3367f587-e06e-3da2-a73b-f3be3fe2653a | 3.48145 | -51.25372 | 2025-12-03 04:36:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc60c3da-a332-3895-973c-8377974d8c9b | 2.53382 | -50.83978 | 2025-12-03 04:36:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 77153b6d-568f-3623-83b9-12895c1fbada | 3.54217 | -51.44522 | 2025-12-03 04:36:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e23c0ce-d6a7-3776-bcdf-ae8dbe43cf72 | 3.5429 | -51.44995 | 2025-12-03 04:36:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5490c14-f573-32d8-89ea-4d3826d6c0f6 | 3.47387 | -51.25485 | 2025-12-03 04:36:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2044b831-e838-3a62-b904-38b54b7ada2f | 3.47079 | -51.26003 | 2025-12-03 04:36:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8385c2b4-9e81-3b9e-9331-afa675734c29 | 4.15252 | -59.92413 | 2025-12-03 04:36:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 332cd1ef-d2da-3968-ad88-a23e9e0f1694 | 3.48594 | -51.25776 | 2025-12-03 04:36:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9db64968-ec67-33f4-a77d-52d9e957767c | 2.52651 | -50.84085 | 2025-12-03 04:36:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7920b915-a3eb-380d-9872-b05091d729b4 | 2.52951 | -50.83606 | 2025-12-03 04:36:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 625c7eb7-4eb5-3131-a362-f5e4160cd34a | 3.47458 | -51.25946 | 2025-12-03 04:36:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5adda7ab-d2f9-318a-b5d6-66a68b7d8184 | 4.15177 | -59.91874 | 2025-12-03 04:36:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b82000a3-a3c9-3a67-8732-557126f61731 | 2.53016 | -50.84031 | 2025-12-03 04:36:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 67126dc8-6baa-3f43-ae7f-fa71f91f80b9 | 3.67991 | -51.28458 | 2025-12-03 04:36:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a4b873a-0596-3496-babd-4d241a881f87 | 3.47149 | -51.26463 | 2025-12-03 04:36:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16a80c3e-111f-3d5d-adcb-43537dd46f84 | 4.1564 | -59.92125 | 2025-12-03 04:36:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f294ebf2-699e-3d8c-b6ef-55d166c44073 | -3.83459 | -50.30665 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 128808b0-f642-336e-bdac-dbf9dadaa518 | -3.23256 | -45.57718 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cc07480f-c205-3f19-8144-b959a1109632 | -3.23876 | -45.54656 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c8c7c747-dbe1-35cd-8e7b-cc93a3a19cf1 | -3.25321 | -45.5488 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3fb1b0d-83ba-3fc4-9ddd-c4dcfce1014b | -3.24223 | -45.57265 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30f4cbb6-6c7c-32ab-98e1-b9272fdec8ee | -1.67584 | -45.79736 | 2025-12-03 04:38:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cd27800-1108-38a9-bebf-50a17fa5677e | -1.19697 | -53.08625 | 2025-12-03 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9142bd15-b615-3ae7-b8eb-d0b99631cf2a | -4.60394 | -48.44458 | 2025-12-03 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0386bcc9-12f1-3dff-8f78-323a02504c90 | -3.23689 | -45.55904 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 85f4a669-7cc9-32ca-8b2a-bf3e5b2aba3a | -3.34229 | -50.0216 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efc7d0cd-9183-34f0-a3cb-ff80083a8569 | -3.24944 | -45.57377 | 2025-12-03 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf8654a2-417d-3919-91c1-1eaa460a0607 | -3.24584 | -45.57322 | 2025-12-03 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d807069-287f-3aef-818f-72f30501c16e | -3.77347 | -50.00572 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3f86744-2526-30dc-b8c6-27d1ca224ed3 | -3.77681 | -50.00623 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16c353b2-36c1-34e7-9640-f5c1cd6625fa | -4.1184 | -50.08521 | 2025-12-03 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d71b38d-fff0-3c3a-a90b-55de8572856d | -2.83271 | -50.46634 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e163e631-a3fd-3446-a5cf-77591cd351fd | -3.23025 | -45.56833 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| df4dc16e-465f-3d1a-9582-f5e4f3740bd0 | -2.84841 | -46.73569 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6a3453b-c2c0-333f-adfe-2c54bc7fcf57 | -2.20475 | -47.99446 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c6151ed9-a033-31c9-b4ed-d82a0157ad52 | -2.39105 | -49.38929 | 2025-12-03 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f0c7b95-fd36-33f7-bfcf-c3f4074e2028 | -2.96264 | -48.58583 | 2025-12-03 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cc2b7b9a-2c52-35a5-bd39-a34e0cafe347 | -1.15202 | -48.09359 | 2025-12-03 04:38:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README9.md)
