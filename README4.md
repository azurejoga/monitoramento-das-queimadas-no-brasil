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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bab921c-405a-356d-a1d3-f65ffd6c1d70 | -3.1397 | -60.66083 | 2026-09-07 01:05:00 | TERRA_M-M | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 98aa9258-d679-31b5-af50-1337283e2d76 | -8.80708 | -63.90296 | 2026-09-07 01:05:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 714d6580-2469-3fcd-85ed-ddcc567d566e | -5.36299 | -56.04834 | 2026-09-07 01:05:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 56c7cda3-f511-3ad7-b23c-b9080680042a | -3.13506 | -60.6292 | 2026-09-07 01:05:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f0749e0a-44a5-351e-8869-f7ea8128dee6 | -6.38316 | -62.81324 | 2026-09-07 01:05:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e4b02515-add2-35cd-9548-f30cfe6a8a80 | -3.14664 | -60.6276 | 2026-09-07 01:05:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c71411c6-cdc0-38e2-bbb3-310c120481f1 | -5.2961 | -60.14526 | 2026-09-07 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 34e2772a-1ed6-3893-877c-c63cc9b6645e | -3.60872 | -60.56167 | 2026-09-07 01:05:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 37.8 |
| c41b5f37-39b2-3f6b-9297-9feb62a0188a | -5.99471 | -57.70125 | 2026-09-07 01:05:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 132.6 |
| e4d5afa3-64fa-32a7-91cc-7128bd97201b | -5.98571 | -57.69614 | 2026-09-07 01:05:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 74ac4bc7-2b1e-3d60-9151-443bec77ce89 | -3.142 | -60.67657 | 2026-09-07 01:05:00 | TERRA_M-M | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| ee5180bf-6a75-36d4-9b46-a711b095f588 | -5.99962 | -57.69363 | 2026-09-07 01:05:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 404136fd-7829-30eb-ab0c-0dbbb87c0c13 | -6.63825 | -59.43808 | 2026-09-07 01:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.5 |
| f2723282-34e4-3664-ab78-eb29aa0196cb | -5.59811 | -60.24212 | 2026-09-07 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d1803ebe-c99a-3201-a908-5461260a13a5 | -3.77122 | -61.76098 | 2026-09-07 01:05:00 | TERRA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 86c889fa-104b-367c-abe9-42092f58d00f | -7.05883 | -56.46757 | 2026-09-07 01:05:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 69c3f557-64e8-337b-831c-8cbea559519e | -5.26478 | -60.15647 | 2026-09-07 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 70aab940-0950-3047-9fcc-34549c694e83 | -4.28122 | -59.96092 | 2026-09-07 01:05:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1412a884-110b-3655-934e-4f149096f1a1 | -3.61101 | -60.5774 | 2026-09-07 01:05:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 508acab7-10cc-36e6-8870-798d6280493e | -6.63288 | -59.44514 | 2026-09-07 01:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e266c0b8-c848-3d25-96ac-fd524efb979c | -7.42183 | -64.61672 | 2026-09-07 01:05:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6b69615a-a91c-3129-b8c1-c133293c5ec3 | -6.1274 | -57.74227 | 2026-09-07 01:05:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 88482dfc-2427-39c4-820b-f9cf98bd4bf4 | -4.28369 | -59.97792 | 2026-09-07 01:05:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 2135ef32-e39d-3f82-a490-c1ff4ec532eb | -6.95211 | -59.76162 | 2026-09-07 01:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| df7e7a4e-adfb-35a5-88c0-a1f3f26ba107 | -5.29374 | -60.12931 | 2026-09-07 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 26.9 |
| b8d55b5c-ae3a-3464-9600-ada2937939b3 | -3.14894 | -60.64339 | 2026-09-07 01:05:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| af769433-d1a6-3425-8e41-4e97e07663c5 | -3.15124 | -60.6592 | 2026-09-07 01:05:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| a1ad8505-d013-3950-b40e-10d7897e4a73 | -6.64939 | -59.9617 | 2026-09-07 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 9035e498-66cf-3c8c-9381-fb3e9fd839a6 | -3.42222 | -59.65034 | 2026-09-07 01:05:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0faccf29-433d-35ca-8c36-6d16fd80799f | -7.05667 | -56.46108 | 2026-09-07 01:05:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 1b9a63a1-d764-3983-851d-c7ecc800c8b6 | -8.52837 | -63.88845 | 2026-09-07 01:05:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 0b20c274-c69a-3ac3-bcf4-55f0073014ef | -6.64081 | -59.4548 | 2026-09-07 01:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| bfd5588e-4f38-3aea-9edd-8d92666e08e3 | -6.05623 | -57.78313 | 2026-09-07 01:05:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| b503f835-b5bc-3268-921c-47dbee61b8ce | -5.4884 | -60.20095 | 2026-09-07 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 521f7100-d3fc-3221-90d3-74fc895850d2 | -3.37662 | -59.42271 | 2026-09-07 01:05:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 30.7 |
| f4663ba7-799e-39b1-abfa-78e3598da52a | -8.52711 | -63.87946 | 2026-09-07 01:05:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 626e2f8c-7b90-3d36-8753-84bfe805ca7d | -6.95345 | -59.75069 | 2026-09-07 01:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| b9e1daef-3fe9-3de1-b3e2-2f8722ff93ce | -5.35782 | -56.01453 | 2026-09-07 01:05:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 545ca744-4315-38e4-9749-dea98a3eb92c | -3.1462 | -60.6506 | 2026-09-07 01:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 1cd28332-41bb-3bc6-9f30-4247dfb5160c | -2.6388 | -46.7597 | 2026-09-07 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 4077c806-2fce-3f80-8302-3d2dab8b068b | -9.7328 | -43.4168 | 2026-09-07 01:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| dde87378-a931-3c87-aa86-24b07eb8ef0e | -2.9645 | -48.7036 | 2026-09-07 01:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 7d483021-8aa0-37b1-9496-909657461890 | -6.0002 | -57.7079 | 2026-09-07 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 35176e88-d5ee-3b4b-ae38-da64e5a86e87 | -9.7519 | -43.4143 | 2026-09-07 01:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 6f83db47-7937-3ece-9c7a-814b4ee30449 | -13.2477 | -61.7342 | 2026-09-07 01:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 0e5a5f10-71a0-3bfc-9a76-e60d70769e70 | -9.2503 | -46.6811 | 2026-09-07 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 9e06db27-114c-3767-bcde-92f0e47c4ed2 | -2.6202 | -46.7822 | 2026-09-07 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 3d0e02a0-edd5-3459-9eb8-f8d2aa560f9d | -6.0004 | -57.6884 | 2026-09-07 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| dc4a0612-6253-340c-81cc-e8518ec331ec | -9.7332 | -43.3932 | 2026-09-07 01:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 94.5 |
| 041497a2-5e97-3a17-aedf-56e016ed7e9e | -2.6203 | -46.7602 | 2026-09-07 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| e246954e-24d6-301b-aa55-1e4f82f46f5c | -4.1102 | -49.0675 | 2026-09-07 01:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 715ea2e7-b21a-360b-b9ac-eacc7078627c | -2.8839 | -50.4638 | 2026-09-07 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 0bd403c0-519c-37ea-891a-89fc1a3bf24d | -2.8655 | -50.4434 | 2026-09-07 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 68855713-4fdf-34d0-9d80-7e4c864bed2e | -6.6514 | -59.945 | 2026-09-07 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| c092d0f5-6e15-3126-b861-d01484eaa12a | -9.4968 | -40.2839 | 2026-09-07 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 117.1 |
| f9c22e71-f1e8-37fc-a3f5-8d78265ad776 | -6.6513 | -59.9642 | 2026-09-07 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 7ad8bf0f-9914-333e-9c6a-7c2d801d260b | -9.7522 | -43.3907 | 2026-09-07 01:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 82.0 |
| c6baa1ac-9294-3d11-a276-404c1421105e | -2.8839 | -50.4428 | 2026-09-07 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 41964c2f-2ce9-3fa7-8c5f-f818e042c9d4 | -13.2287 | -61.7355 | 2026-09-07 01:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 8a0008dd-ac1c-3a9a-bf87-e80859835d6b | -3.6215 | -60.566 | 2026-09-07 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 87.4 |
| c11d4e24-04c5-3611-91b2-2e6bd1b378eb | -3.1461 | -60.6696 | 2026-09-07 01:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 9dfec34c-6c13-3223-8db9-075d091b0903 | -2.6387 | -46.7817 | 2026-09-07 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 32c18e73-1a58-37b2-9588-03ed41d69b43 | -9.47 | -40.26 | 2026-09-07 01:15:00 | MSG-03 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d4bddc45-4270-3945-88c9-8455956dd4a1 | -9.5 | -40.26 | 2026-09-07 01:15:00 | MSG-03 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 747536e3-af3c-34bb-b7a9-f7a2760a7f97 | -6.6514 | -59.945 | 2026-09-07 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 817b47b0-0831-3edf-a941-e1072aca4093 | -2.6203 | -46.7602 | 2026-09-07 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| f2b64aad-844c-35f4-8e96-26d137e3b162 | -6.055 | -57.8032 | 2026-09-07 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| f8fc0421-bc69-3f28-a478-708ad27a7bd1 | -2.8655 | -50.4434 | 2026-09-07 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| bb71317a-04c5-367b-bb5c-2d3399bf7e99 | -13.2477 | -61.7342 | 2026-09-07 01:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 71.6 |
| b76bf82f-11c2-32b2-88f7-8e0453dc724a | -2.8839 | -50.4638 | 2026-09-07 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 369c1709-faff-3ada-8887-f9c2a04e7609 | -13.2287 | -61.7355 | 2026-09-07 01:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 1ab9e8a0-e00b-39fe-a843-3db2d04da905 | -2.6202 | -46.7822 | 2026-09-07 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| df27d289-14dc-38ad-b69d-4b0306b75aaf | -5.9819 | -57.6892 | 2026-09-07 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| e49196c8-5002-3b00-971f-8645ce34baf5 | -7.0605 | -56.4629 | 2026-09-07 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 2041ee83-827c-38a2-88a4-bdd13931cdef | -9.7519 | -43.4143 | 2026-09-07 01:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 121ff6f0-5c30-3796-bca7-a8bdaec9bd8f | -9.7522 | -43.3907 | 2026-09-07 01:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 79.7 |
| f2f291b8-cf86-3317-81ca-de3ee33dbc65 | -9.7328 | -43.4168 | 2026-09-07 01:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 135.9 |
| e7981b16-1e83-37bd-aef6-4aadb5b1cd00 | -2.6387 | -46.7817 | 2026-09-07 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 55b4e806-4280-34e1-8af2-672b0329baa7 | -6.6513 | -59.9642 | 2026-09-07 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 5c395bc6-d2b4-3c40-9951-9ed0c09721da | -4.1102 | -49.0675 | 2026-09-07 01:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 1ef59160-1ba3-3f7a-8843-6d976e1015ba | -9.7332 | -43.3932 | 2026-09-07 01:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 88.2 |
| 106f030b-77ac-346b-9423-bd3bffd4a414 | -6.0004 | -57.6884 | 2026-09-07 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 185cb16d-c9f9-359a-a827-8a664d073ee6 | -6.0002 | -57.7079 | 2026-09-07 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 329a3a36-64f6-3cb1-8d8a-2412f4db943b | -2.6388 | -46.7597 | 2026-09-07 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| bebcd9ee-3984-3f82-8beb-179f8c4a928d | -2.9645 | -48.7036 | 2026-09-07 01:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 463eaebb-70ba-3845-8d0c-95e7755deca3 | -2.8839 | -50.4428 | 2026-09-07 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 127d3ec6-4767-3743-838e-f03fcfcbdea7 | -6.6698 | -59.9443 | 2026-09-07 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 1db54dce-5ef4-3be4-921c-54d31593c64a | -3.1462 | -60.6506 | 2026-09-07 01:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 95.9 |
| a2429894-59f9-3de3-9477-324255291f5e | -3.1461 | -60.6696 | 2026-09-07 01:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 88.4 |
| ddb54eb5-30aa-3ed8-809c-41b4895a0300 | -3.6215 | -60.566 | 2026-09-07 01:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| a780e16e-f2fb-34e3-a40a-d41fba9f43e1 | -14.5287 | -59.807499 | 2026-09-07 01:29:00 | METOP-C | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 442e597a-113a-3b06-bd02-9501212c133a | -7.0591 | -56.478699 | 2026-09-07 01:29:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ab5cfe5-f0b0-35c9-b367-b640eae3fea5 | -6.0533 | -57.801102 | 2026-09-07 01:29:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8db2b65a-7efd-310c-8220-63fe82f99edd | -4.2989 | -59.959599 | 2026-09-07 01:29:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 737b9666-730d-3825-bdf3-2085bbc069ef | -5.3642 | -56.033298 | 2026-09-07 01:29:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 093134db-32f2-3302-8231-ef0c68e5c8a2 | -4.2874 | -59.954498 | 2026-09-07 01:29:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 01f45278-5607-3193-b989-23d6cad4c9ed | -4.2908 | -59.969299 | 2026-09-07 01:29:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8d89000d-166a-31e3-8901-13b30cbce939 | -4.6703 | -55.630299 | 2026-09-07 01:29:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c7be1e6-6398-362a-90bd-5365f9483784 | -5.1535 | -55.971001 | 2026-09-07 01:29:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fed45e1-6cc5-3e14-b1d2-14234de7d949 | -5.9941 | -57.681702 | 2026-09-07 01:29:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
