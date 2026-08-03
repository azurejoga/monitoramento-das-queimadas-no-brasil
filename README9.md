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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc93260f-1d47-385f-971c-a75276548dea | -6.55568 | -55.16273 | 2026-08-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 965db6a3-57d0-39d7-b6b4-627257131864 | -11.25356 | -54.83775 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e5bb5051-5652-328a-b0eb-196a9f69ac64 | -6.56341 | -55.16774 | 2026-08-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9370df95-e9df-37d1-a1f8-f8a3e0ce9ecd | -6.5474 | -55.16152 | 2026-08-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 99e27f90-6b27-38af-b1ea-10b6e8cc0c0e | -6.56287 | -55.17145 | 2026-08-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48ec8cbf-0e14-3ed0-8514-9d0a503652f2 | -15.32086 | -53.93491 | 2026-08-03 05:25:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6260cf85-8d7f-3992-8ddf-ef92f847578e | -6.96293 | -52.82471 | 2026-08-03 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a47fe478-0a99-32f7-b209-0ac1065135ce | -5.77442 | -60.35566 | 2026-08-03 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3e8fde8-735e-315a-aedc-c0a1bbc9c6ad | -10.3344 | -64.46186 | 2026-08-03 05:25:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b27e591-5207-3a26-9e0f-0dfc56449623 | -6.56615 | -55.14901 | 2026-08-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 756925d0-d08b-3d90-b34c-acdd5744fc1c | -11.25419 | -54.83308 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fc0c01d7-305b-3489-b3d9-98dae861f666 | -11.27566 | -54.84518 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a349bd2a-b38e-3093-b164-6eb36702ce26 | -11.2773 | -54.84329 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3c18889-9125-3644-aeef-44cc1fab6ae3 | -6.5546 | -55.17016 | 2026-08-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6ce60c9d-6452-385f-abe1-ad02dd35503e | -11.26308 | -54.8462 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bedaa190-b905-3506-8535-966e97fe25a8 | -11.2779 | -54.83863 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1cfe1512-7aa5-3a57-9f9d-8b6f09a15ba6 | -11.27276 | -54.84272 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2aa66645-5ab6-3415-9580-aa5eb8d05db4 | -6.56147 | -55.1521 | 2026-08-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0bacc944-c600-38d2-91f8-68a88c08243f | -11.9193 | -55.90047 | 2026-08-03 05:25:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09ce73ae-385a-35e1-aaae-9e86711e7969 | -10.33864 | -64.45835 | 2026-08-03 05:25:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5d1fc26-8603-32bb-815d-7e0cb8b7d30e | -6.54686 | -55.16523 | 2026-08-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dcff47e6-fa35-34a1-995d-22bf255cf3f2 | -15.23733 | -52.90957 | 2026-08-03 05:25:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee1689bf-b1ea-36a7-a65a-d79133bf6304 | -11.23108 | -54.86774 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 311413d5-4921-3123-b9a2-d05ad8aae429 | -6.96366 | -52.81941 | 2026-08-03 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 58229c92-603a-3bcc-b75a-1389ca86fcd5 | -11.91504 | -55.89987 | 2026-08-03 05:25:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4bc57ee3-37be-3e15-9f5d-b23cc2240d2e | -6.5681 | -55.1646 | 2026-08-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef046e2a-fe6d-3157-a5ef-eb923d554c03 | -11.26657 | -54.84404 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0041b88a-a383-3a68-9337-cc1180a63108 | -15.23775 | -52.9059 | 2026-08-03 05:25:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d0aa4ff7-d13d-3f5d-8f36-e752ca04c10b | -6.56395 | -55.16403 | 2026-08-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2852189b-1279-370c-8fc8-e53a310e851a | -11.25482 | -54.82838 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c4fc21aa-a440-3463-8ae1-a30537494e51 | -6.57169 | -55.16895 | 2026-08-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46692a69-eed3-3a2c-b378-f7b2e3b64b46 | -11.27629 | -54.84055 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1a3f745-739a-36be-93f7-120570fa83af | -11.25092 | -54.82305 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cbf1aefe-292f-344f-b8c0-399ec25a1175 | -4.15069 | -63.10865 | 2026-08-03 05:25:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68b107dc-ef36-3b39-9d2d-44c142c39e3a | -11.23169 | -54.8632 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 709c4525-ce12-3ca7-969d-eb0386a24b6b | -6.56036 | -55.15965 | 2026-08-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5759421-b6b0-390d-8357-3fe78ff7b18c | -11.26203 | -54.84348 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d3f598f-95ef-3794-9237-530ba6a7ac55 | -6.5645 | -55.16028 | 2026-08-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 359da7dd-7a90-3b66-acd6-daa7e60c3fa4 | -6.55873 | -55.17081 | 2026-08-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 093e6352-a3c0-3466-8fe8-daa968a5e1a8 | -11.25295 | -54.84232 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d633eedd-6293-3c90-9dac-53d456c11e8d | -11.24076 | -54.86434 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5186653c-94ef-37ae-a0d6-f1639d55ffef | -11.27216 | -54.84736 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3370c74-602b-389e-8f67-e5c6457559b6 | -11.23809 | -54.84983 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb1582ab-5332-307f-a260-7fe1837093c5 | -6.56505 | -55.1565 | 2026-08-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 087d6258-ce9f-3c69-a87a-30fc63c51f17 | -11.23684 | -54.85915 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbabfabb-d298-33dd-a37f-c07e83d76ec0 | -6.56092 | -55.15586 | 2026-08-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5832064f-9125-3bc4-b6ba-6f465ba03774 | -11.25811 | -54.83833 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0d7f1e6-6ce7-380b-95e5-21733f546d59 | -6.95803 | -52.82405 | 2026-08-03 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a27b99e1-9a9d-36cb-926c-0da37ab24dc9 | -6.55678 | -55.15519 | 2026-08-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92c029d3-5593-3db0-b0fe-01f331b47393 | -6.551 | -55.16583 | 2026-08-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dbe56adc-2e29-3d98-be63-5d9e29fe28ac | -11.26821 | -54.84216 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20ba4de8-0d60-3c84-8914-ac1d6babc3e4 | -11.25874 | -54.83367 | 2026-08-03 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41646f3d-befb-3c73-b8c4-b14543ba2b36 | -6.55209 | -55.15833 | 2026-08-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2d6846b3-a4b5-3dc3-93a5-2ca6393ada88 | -10.33508 | -64.45777 | 2026-08-03 05:25:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d80fe78-7257-3f86-a3e0-51923270ca0e | -6.95875 | -52.81876 | 2026-08-03 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8564508b-6bbf-3423-84de-977fcaac5b45 | -6.55981 | -55.16341 | 2026-08-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3587d895-0020-3cd0-a1fc-0c437b2af73d | -5.84434 | -57.66166 | 2026-08-03 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b05522c-0f21-3362-a96f-6b5ff4ad7210 | -1.6591 | -54.4543 | 2026-08-03 05:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| f774ad79-6156-36d3-b030-561bd1095514 | -1.6591 | -54.4543 | 2026-08-03 05:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 9b82c1a8-0bde-37b7-9957-4c9ae60069a0 | -1.6591 | -54.4543 | 2026-08-03 05:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 6e70b954-3359-36ad-a87e-c5c88792f6ce | -20.8969 | -45.5371 | 2026-08-03 06:10:00 | GOES-19 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 132585ce-6133-3270-be1a-ce8cf698a144 | -1.6591 | -54.4543 | 2026-08-03 06:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 1e871fb6-76d7-3f8c-878a-1205a8f38f45 | 2.53186 | -60.3638 | 2026-08-03 06:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| afa9f045-57bd-3694-9484-42046215af53 | 2.53714 | -60.35825 | 2026-08-03 06:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb37cadb-66ed-3713-bb02-c48f1055507a | 2.53341 | -60.36358 | 2026-08-03 06:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b05f62b8-5372-3b0c-86cd-5aabdddac282 | 2.53944 | -60.36258 | 2026-08-03 06:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08b12c18-a3e7-3cfc-a8da-dfb98eefadb1 | 2.53788 | -60.36278 | 2026-08-03 06:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eeea8c0d-f7eb-368a-9fa4-c0ede5bb2383 | -7.32293 | -64.70644 | 2026-08-03 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a471af72-fd8f-3b14-b9d5-a6997fc017e6 | -7.31767 | -64.70571 | 2026-08-03 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 92d7db62-13f7-38f6-a6bd-96cb7baa7f47 | -16.3455 | -49.4628 | 2026-08-03 06:40:00 | GOES-19 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 44106ece-deed-3550-9f44-9d12203492c7 | -1.6591 | -54.4543 | 2026-08-03 06:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| ab4fe28d-71c9-3880-8aaf-38dbb18578cc | -16.3455 | -49.4628 | 2026-08-03 07:00:00 | GOES-19 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 8c1e9eb1-e79f-3c39-b2d4-141f4e164788 | -1.65268 | -54.45642 | 2026-08-03 07:05:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 2c5fb344-2c2f-35ba-ab04-6c68160bf48b | -1.64366 | -54.45507 | 2026-08-03 07:05:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1915dab1-9ce3-3e2b-a665-4197b622b772 | -1.64507 | -54.44574 | 2026-08-03 07:05:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9206807a-2a5a-3566-9f78-1da92a05ac2a | -1.63464 | -54.4537 | 2026-08-03 07:05:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 91f6adde-ca80-3271-93d9-5b998c0e3687 | -1.65409 | -54.44711 | 2026-08-03 07:05:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| c5ad1d28-59b9-3bcc-9b0d-8f43bae7e698 | -2.81357 | -52.28907 | 2026-08-03 07:05:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 377445c1-df3c-3650-826b-2d08d014b4f7 | -6.54823 | -55.16715 | 2026-08-03 07:07:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cdad30fe-e193-385f-a932-9b48f5669afb | -6.55992 | -55.1503 | 2026-08-03 07:07:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f74dd117-b2c9-3627-96b7-5b5a33a8aaf2 | -6.23664 | -55.62979 | 2026-08-03 07:07:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| ec2a435e-cbee-3faa-a7ed-587a33b046b4 | -6.22754 | -55.62845 | 2026-08-03 07:07:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f94d85bb-e372-393a-84c3-480285aa3cfc | -6.55854 | -55.15937 | 2026-08-03 07:07:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7498ceaa-fbbb-3d4c-8b4b-0c9d8e68ae67 | -6.95944 | -52.82146 | 2026-08-03 07:07:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 94000f9a-7b7f-3377-a3be-4e28a97fdfcb | -7.24473 | -59.44779 | 2026-08-03 07:07:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 5b42a080-e9b0-3ba4-bdd1-955e8c2db775 | -11.25389 | -54.83175 | 2026-08-03 07:07:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2dfcdb7a-985c-3ebb-bc6b-20d9aac918f7 | -6.54963 | -55.15804 | 2026-08-03 07:07:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| f5906d6d-9d8b-3810-9884-a836442e5b63 | -16.3455 | -49.4628 | 2026-08-03 08:40:00 | GOES-19 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 44.8 |
| e70dac5f-f4fe-37ac-8ef9-ee7ea9058ce9 | -5.9631 | -45.0236 | 2026-08-03 11:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 5b903d90-1f33-3a33-8806-a1d57bc0f049 | -5.9631 | -45.0236 | 2026-08-03 11:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| c8625a51-ac71-3c3c-b43f-b91aa891657d | -4.27121 | -48.19269 | 2026-08-03 11:57:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 9fa1e82f-2137-3081-be04-2dbd3a3b8875 | -17.0616 | -45.0191 | 2026-08-03 12:00:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 54a00bf9-bf93-378b-8ed2-80065133c689 | -7.9721 | -44.9169 | 2026-08-03 12:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 213.5 |
| f1c92d4a-06d4-3bdc-8852-ad4adf999e52 | -17.0416 | -45.0234 | 2026-08-03 12:00:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 3c0f6e99-2fd2-35c7-8ba8-2bc1d0704a75 | -7.9724 | -44.8941 | 2026-08-03 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 0b8bea77-7c0d-3679-b37b-f189687e9e09 | -5.9631 | -45.0236 | 2026-08-03 12:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 232.2 |
| 3ffe354f-28e2-3f6a-b710-a9af4f3d8741 | -5.9629 | -45.0463 | 2026-08-03 12:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 8a4a3517-3f56-3278-b51f-6c724b79b08d | -11.59649 | -50.24257 | 2026-08-03 12:00:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 219db4d5-9c1c-36ee-b188-414470ce5a3d | -6.13954 | -45.22896 | 2026-08-03 12:00:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 54456697-60f3-3a46-a06c-325c231da71e | -10.55052 | -42.53717 | 2026-08-03 12:00:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 22.5 |


[Clique aqui para ver as próximas entradas](README10.md)
