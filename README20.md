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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b11fa4d6-6b36-3a1c-87da-f93688a28753 | -3.39405 | -49.52261 | 2025-11-26 04:21:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c082c91-e513-30f4-a955-749fb56136e4 | -3.16851 | -45.0878 | 2025-11-26 04:21:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b157a1af-2293-31f0-90b9-8193c7db7082 | -3.48779 | -50.44478 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6254bf88-c0ea-3a07-8d7f-9bd7ce98c276 | -3.14197 | -40.18296 | 2025-11-26 04:21:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 78dae176-8914-36ef-8d88-201fe706b6e8 | -3.82468 | -48.99172 | 2025-11-26 04:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6307bd22-4eec-3fe5-a0a9-ba878104b8d5 | -4.11961 | -44.83438 | 2025-11-26 04:21:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f065cf49-3625-3509-b857-887ab40ac004 | -8.06384 | -43.13271 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 019a3f6d-3d8b-344c-8bed-eb716aa650dc | -3.21748 | -45.14603 | 2025-11-26 04:21:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08b40baa-030d-351f-945c-1c30007909a9 | -8.05813 | -43.12418 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 70ecb44b-b6a7-3c18-8f28-f0a516f2d3d6 | -7.04103 | -46.58022 | 2025-11-26 04:21:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e20517c9-7ea9-3d63-98a6-5096ebc5486d | -3.20462 | -50.22076 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5bfbb95-248f-3d6c-a7a1-43fb0dcde664 | -4.14385 | -43.64767 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c8990c0c-6711-32f0-979f-3141de371355 | -2.93019 | -48.23729 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f7898252-d834-3d75-b543-5b1e5bfc04b2 | -3.66352 | -42.23022 | 2025-11-26 04:21:00 | NOAA-20 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 027c187a-700c-3ea4-b1f8-b69a1e624f79 | -2.99035 | -51.06213 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d52f02d-ae37-3711-8034-45cb17cd1b56 | -6.0343 | -43.50438 | 2025-11-26 04:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1fcc05b-df1d-3c2f-80b2-e2d8cdfe56e1 | -2.85879 | -42.44365 | 2025-11-26 04:21:00 | NOAA-20 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 392a9ff7-a455-35b6-aeea-566674968ef3 | -5.45664 | -42.46025 | 2025-11-26 04:21:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 05ca1777-f8da-3eb3-a8b1-1936baf091b5 | -4.37614 | -49.76936 | 2025-11-26 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16e1288a-caab-3478-8941-176150185e00 | -4.56553 | -43.29895 | 2025-11-26 04:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bbdace27-6b66-3519-a6d8-1db9df438818 | -3.20595 | -50.2127 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd59ec84-96c7-3609-adb1-e6f39b16fc90 | -3.52272 | -53.06592 | 2025-11-26 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6eaf09f1-f76c-3b6f-ab4e-23146063acfc | -6.51851 | -37.80184 | 2025-11-26 04:21:00 | NOAA-20 | JERICÓ | PARAÍBA | Brasil | 2507408 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b622a4dc-6818-3f33-ae57-db097f8d717b | -6.31287 | -43.7864 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17849897-58a9-30e0-83f5-5e619421ffd7 | -6.06579 | -43.25721 | 2025-11-26 04:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ce66c9dd-845c-3aab-97f3-8f56be902ccc | -5.17271 | -41.14669 | 2025-11-26 04:21:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cef096e1-4c64-35f1-8153-cbba9d1782e1 | -5.56966 | -46.28377 | 2025-11-26 04:21:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa1ad1bd-5147-3722-9e3f-67e30e6f1eac | -8.05584 | -43.13914 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| f30f0598-d946-3af0-a9d5-a9c2e5bf5a66 | -6.57287 | -47.89163 | 2025-11-26 04:21:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3a956be-285a-3a6c-9f2e-56b3f12f390f | -3.02451 | -51.22078 | 2025-11-26 04:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44958a20-df54-3502-92e3-558f83e966a0 | -2.96161 | -49.53262 | 2025-11-26 04:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d6c0bc4-9d54-3cd9-923b-b9e413a7a350 | -4.67793 | -49.38119 | 2025-11-26 04:21:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05b7abc9-7179-3720-a7e2-c7c91aaf72e5 | -3.60346 | -40.98965 | 2025-11-26 04:21:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 325628fc-5c9d-3a9b-a980-62b9385a0248 | -2.49481 | -47.83262 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2a30c61e-8062-3540-84e0-93435df7a95e | -2.92711 | -48.2319 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 66e1ebc7-fe81-3cf8-b07b-2008405c0c2f | -2.71045 | -45.69498 | 2025-11-26 04:21:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9691c237-5769-3728-bf28-b21bc6ce6cd2 | -6.50429 | -38.82135 | 2025-11-26 04:21:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3d26955a-8133-3482-8b22-ce7c313447c6 | -8.03756 | -43.12101 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 87944447-aec0-3800-a73a-49b4e06b6ce7 | -6.07408 | -39.55323 | 2025-11-26 04:21:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ad6c8bcb-57a9-381c-bf69-80e0a5d168c5 | -4.16117 | -43.73184 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d2bca2bf-1a99-37f1-9373-9e637fd4ccd4 | -3.48852 | -50.44038 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad7cab21-ba32-375a-a8dd-c1705bf0c7e1 | -2.49858 | -47.83323 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f76d4e44-6556-3f4b-a5e9-e8d3d80ed7d2 | -2.41031 | -49.35239 | 2025-11-26 04:21:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a33cfd56-4f84-3813-b461-16acb4cc55d6 | -8.04784 | -43.1226 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 9efde89a-aedc-3f91-b5d8-2576f484608b | -6.54743 | -44.458 | 2025-11-26 04:21:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c119843d-c82a-38e5-ab81-fca7570176a8 | -2.85935 | -42.44005 | 2025-11-26 04:21:00 | NOAA-20 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 408fa710-585a-3ea9-aff3-b3fac61acef0 | -3.85494 | -49.36389 | 2025-11-26 04:21:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0389f51f-6c8d-3d54-bab7-34c6368f9fbe | -3.23269 | -50.59396 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0fe9cf5-0611-31c8-b69d-dee969e05bae | -6.3079 | -43.79639 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 59347bc6-638a-315a-a71c-75cd1a9d48e3 | -4.2639 | -45.1241 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 048176a9-5b27-3403-a725-6919d882f39d | -3.32662 | -49.71663 | 2025-11-26 04:21:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4e2a49b0-5c9f-3806-b964-5fb02b923b52 | -4.14046 | -42.54217 | 2025-11-26 04:21:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9d1af83d-7fb4-3521-949d-60966e6fd2bf | -4.78625 | -48.28787 | 2025-11-26 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d4be317-6393-3a11-a5a2-b8be42d61725 | -8.04099 | -43.12154 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5edeb93c-134c-3a8b-9013-20ae1d8441f7 | -8.06556 | -43.12149 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 498a1291-9da1-3162-8778-d9f5aff8e8aa | -6.48422 | -47.49975 | 2025-11-26 04:21:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| adbd0009-973b-3a6f-b8d6-aa8d4aea3a9a | -4.04644 | -48.89076 | 2025-11-26 04:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c6febb9-93a4-33c1-b8df-591dc4dc771a | -4.37146 | -45.3892 | 2025-11-26 04:21:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 379230fb-f0a1-3598-a3b1-bf036b4be660 | -5.68488 | -42.82069 | 2025-11-26 04:21:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 811eeb29-4840-342b-ae81-f87709771fc7 | -3.4371 | -50.17865 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1fcec1e-c694-36f4-8285-ae655c895e3b | -4.45566 | -44.30066 | 2025-11-26 04:21:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49636e10-d0cf-3273-a778-a57f3ce22225 | -8.05013 | -43.13061 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.8 |
| cc3e5d86-ae4d-3313-9c16-4ae31e3977d5 | -3.96249 | -46.4845 | 2025-11-26 04:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d291f4fb-5709-341c-a394-aa60c204342c | -6.3007 | -43.79882 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5e6f51ed-a932-390f-ac44-dbc49ba30cf6 | -8.0467 | -43.13008 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 3d5b8f39-d93b-3a25-ac59-4bd4d13a7e62 | -7.51287 | -45.72009 | 2025-11-26 04:21:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d583424f-68b9-33a4-848c-f18842bd046d | -4.53551 | -45.55276 | 2025-11-26 04:21:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e00d40e-39b3-3681-a568-6788f1a6167a | -3.6732 | -38.81014 | 2025-11-26 04:21:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b0772455-2967-39cd-9833-1f518e273ddc | -2.74317 | -47.1316 | 2025-11-26 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 925c1971-f9a8-3a46-96b3-72c913716107 | -3.52827 | -41.49987 | 2025-11-26 04:21:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3b8c235c-af72-3c8e-935d-41f14d52be9a | -2.93897 | -49.35508 | 2025-11-26 04:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| f0e966c5-fb95-3aa3-ba23-70f7c6702e23 | -4.64212 | -48.12848 | 2025-11-26 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55c06d06-a586-367f-83f7-9913c29be44d | -7.5675 | -45.869 | 2025-11-26 04:21:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5933a634-32a3-3608-9dee-1a8043a55e11 | -5.96156 | -46.15607 | 2025-11-26 04:21:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| abd76dfe-55c4-3c10-a26f-a4455be0f47c | -3.98482 | -49.285 | 2025-11-26 04:21:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8362d263-beda-3e78-b792-657867ac1068 | -3.14268 | -40.17849 | 2025-11-26 04:21:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5795d9dc-ea4a-3740-8591-4210df3bdd76 | -6.70596 | -41.46175 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bc5321b6-316f-363e-b21f-6023830024a2 | -3.03838 | -45.11393 | 2025-11-26 04:21:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef6e0ce0-dbb9-3348-b000-31e8c4984dd1 | -2.93631 | -48.22358 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbc2f2ed-832e-3ba0-8f2f-3780caf0298c | -3.39982 | -50.5705 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d792904a-e3f9-345c-97ff-7e70e88a7a33 | -8.06786 | -43.10648 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 43bf464a-2cbb-34f8-91d9-727a040aa828 | -4.26002 | -45.12707 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed676037-a45e-3139-b6f4-d26ca031b78c | -4.15389 | -45.15301 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 511c8638-bfe9-3323-a16e-76a803f30e72 | -4.16335 | -43.71801 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 46cf3770-e8be-3411-a558-b1e4b6be0a0c | -3.32734 | -50.26846 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7d60a6f0-323f-334f-8b7e-f56b083138cc | -3.73993 | -42.71067 | 2025-11-26 04:21:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d64da80-9f4e-383f-bc56-b5ee6374082f | -2.44545 | -49.02896 | 2025-11-26 04:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b04e99e-c9e9-3802-93ec-0982018b0cf1 | -4.15509 | -43.72734 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa565695-9108-325a-a794-f29aed955ea3 | -4.15949 | -43.72095 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ce50fb7-01d9-317f-b67f-8ce38fa9c485 | -4.5383 | -45.55685 | 2025-11-26 04:21:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3c76d2d-55c1-3188-8568-f1182f6d0c91 | -5.25105 | -44.14767 | 2025-11-26 04:21:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 820da17c-70f9-347b-9e25-165f5288e324 | -6.4974 | -47.48559 | 2025-11-26 04:21:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a00dffa2-ff6f-34be-8fe7-b161a7fb8ef7 | -2.4752 | -47.83419 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5569d5e-9af5-3466-8d5e-fe94abcc4ff2 | -4.59552 | -45.70777 | 2025-11-26 04:21:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d17088b-0072-31c4-9903-6769dc17d8c5 | -5.63923 | -43.92432 | 2025-11-26 04:21:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7fa45db-2a44-3f90-b9d0-f36c6e170a6e | -4.72058 | -46.45863 | 2025-11-26 04:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 12916a5b-1056-3fda-ba60-a5e0eabff2d3 | -8.04213 | -43.11405 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8d1cff5c-8e3f-3947-ab84-e80bfcd9223b | -4.2461 | -46.95412 | 2025-11-26 04:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f3a5013-39f4-3562-80c8-c962c2c97d84 | -5.38428 | -46.75505 | 2025-11-26 04:21:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d1a1a4e-2b3f-3d88-b5a3-0fa3e72ca549 | -3.69612 | -50.9479 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README21.md)
