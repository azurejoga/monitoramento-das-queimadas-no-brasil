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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a6b5529-f712-3cd2-8250-33c0ed14a855 | -17.1182 | -57.4039 | 2024-10-06 02:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.6 |
| b198c5e9-2c17-3dc7-a063-edcaddbd8c77 | -17.0207 | -55.0371 | 2024-10-06 02:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 200.0 |
| 3b7be192-0b2e-3cd7-8fba-5253daa3c72e | -17.0203 | -55.0581 | 2024-10-06 02:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 318.3 |
| 26498261-1ca2-3642-a458-056674e2ebc8 | -17.02 | -55.0791 | 2024-10-06 02:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 113.5 |
| f70b5642-3c6a-39e9-bd5e-fc7e0629fdad | -17.001 | -55.0398 | 2024-10-06 02:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 246.7 |
| ecd30d79-555a-3abe-b9cf-8b3581126921 | -17.0007 | -55.0607 | 2024-10-06 02:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 465.5 |
| 718d403f-c719-3882-af70-1e4e24d6f47a | -17.0003 | -55.0817 | 2024-10-06 02:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 913fb642-10c6-3571-862f-c541af8bed0a | -17.1375 | -57.4221 | 2024-10-06 02:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.8 |
| 11f2113c-3a02-34fc-ba50-7835f080e091 | -18.7169 | -57.3512 | 2024-10-06 02:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.1 |
| 588cdc86-ed4a-304f-8c95-c6b24c60059b | -18.7165 | -57.372 | 2024-10-06 02:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.9 |
| fa658655-a9e5-3744-8970-0dcc0b87a478 | -18.659 | -57.2552 | 2024-10-06 02:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.1 |
| eff9e7c7-9d53-3e49-a988-41d3222b1ffb | -18.6586 | -57.2759 | 2024-10-06 02:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.0 |
| 95846469-fa0f-3c35-b560-e80bcfa42062 | -18.6387 | -57.2785 | 2024-10-06 02:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 123.3 |
| df13a42f-1288-3765-94f6-4f84453c2764 | -20.6018 | -49.3821 | 2024-10-06 02:57:00 | GOES-16 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 7e50ee2f-12fe-33f4-ab19-d8859ba9d9b8 | -20.582 | -49.3635 | 2024-10-06 02:57:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 109.2 |
| e3038b5b-ac31-3e6b-b751-e0ccaf8598a6 | -20.5813 | -49.3865 | 2024-10-06 02:57:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 933dd419-0afe-3c0a-af26-a6d953d97c4d | -21.5218 | -50.9088 | 2024-10-06 02:57:05 | GOES-16 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 233.7 |
| 34126d5b-5533-38aa-a71b-eb1a027b40f5 | -20.59 | -49.42 | 2024-10-06 03:03:28 | MSG-03 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 180c04d3-5f21-3ab2-bec5-b346367709a2 | -10.45 | -50.7 | 2024-10-06 03:04:26 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 51bbec27-826a-35db-a866-31abb1766256 | -10.45 | -50.76 | 2024-10-06 03:04:26 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 374748d5-74ed-38b9-ac4d-ce84bf5e0c28 | -10.42 | -50.69 | 2024-10-06 03:04:26 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ee056dba-b0f0-34d9-ae2a-90f7f3ffe373 | -10.42 | -50.75 | 2024-10-06 03:04:26 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c0d62066-5e63-3d42-99c5-d326a3422a6d | -2.8166 | -48.6867 | 2024-10-06 03:05:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 133.0 |
| c6c76dcd-b23a-35e5-9eb0-cbe675d2244a | -2.8165 | -48.7082 | 2024-10-06 03:05:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| eb1a3c5d-8823-373f-9bb8-a68c8d9cc5f4 | -3.1129 | -48.6131 | 2024-10-06 03:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 125.0 |
| b0dcc58a-3a1a-3bfc-97d8-f92b376d698c | -3.113 | -48.5916 | 2024-10-06 03:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| f839893d-b458-3689-952a-a67b0d002eb4 | -3.1314 | -48.6125 | 2024-10-06 03:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 89619638-617e-3ca6-b753-8d46f97815e0 | -3.1315 | -48.591 | 2024-10-06 03:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| c6e28df7-b32b-3d0f-9d59-cad2e279b93a | -3.8008 | -41.5989 | 2024-10-06 03:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 57.2 |
| efaf7a94-546b-31a6-b7d6-b15736bd6940 | -3.8464 | -46.4714 | 2024-10-06 03:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 8e924ceb-0417-3015-875e-2d0f009b3590 | -5.5718 | -44.87 | 2024-10-06 03:05:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| ea271eaf-7881-333d-98b2-aef75d86ed37 | -7.9825 | -54.7752 | 2024-10-06 03:05:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 74dffc94-8724-326c-8844-c5d6966179a6 | -9.1449 | -60.6612 | 2024-10-06 03:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.1 |
| f7510733-616b-35d5-8935-13676835b350 | -9.1759 | -61.5794 | 2024-10-06 03:05:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 1eae50c3-9d6d-3c7d-ae2e-874774bb4257 | -9.3467 | -46.5365 | 2024-10-06 03:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 3456b789-81cd-352c-973a-3ec6670549aa | -9.6779 | -64.6269 | 2024-10-06 03:06:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 98b0ca6a-ec8c-3888-a0e9-8272a32b46cf | -9.8552 | -60.2966 | 2024-10-06 03:06:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 50008bb1-4e0a-33a3-ac9f-05f49dbfe037 | -12.2645 | -41.0969 | 2024-10-06 03:06:14 | GOES-16 | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 103.9 |
| 777b59cf-91db-38d5-980a-d269a7a965bf | -12.6089 | -53.1338 | 2024-10-06 03:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 5fc6e777-00de-34b5-97da-b65abbbfdf65 | -12.628 | -53.1317 | 2024-10-06 03:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 115b275b-33e4-305a-b01b-14ff8ae9ded8 | -12.6283 | -53.1108 | 2024-10-06 03:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 668a6a9a-1a4e-3f55-828f-5bc3a07b511d | -12.6532 | -54.0415 | 2024-10-06 03:06:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 541f9fbf-5bb8-3a26-8eaa-eff4892a7b82 | -12.6535 | -54.0208 | 2024-10-06 03:06:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 0bdf8149-9387-369f-ad73-4571c872ea77 | -12.6723 | -54.0395 | 2024-10-06 03:06:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 3e42eadb-778d-3afd-845b-5091f6fe74db | -12.6726 | -54.0189 | 2024-10-06 03:06:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| c1329a17-495b-3384-b177-5f5ef61b8ab7 | -12.763 | -50.5352 | 2024-10-06 03:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 300.6 |
| e9ad99fd-6955-3ce2-98d0-f63b18358a20 | -12.7634 | -50.5136 | 2024-10-06 03:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 166.3 |
| 7d610a1a-0990-3812-9ea5-35897105c8d9 | -12.7822 | -50.5328 | 2024-10-06 03:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 166.1 |
| cf41152f-2baa-3e13-99c7-301fbdf00fa4 | -12.7825 | -50.5112 | 2024-10-06 03:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 6cb79782-289c-353c-83e7-21da3e82daea | -13.3786 | -61.9582 | 2024-10-06 03:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 37.2 |
| ce88f88a-84c0-3eab-ac38-8088540afb41 | -13.3976 | -61.957 | 2024-10-06 03:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 7ba0859f-cf72-3573-a29d-e17f5e55d361 | -13.6724 | -51.1911 | 2024-10-06 03:06:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 3ffcd9ae-c9af-34df-ab06-be6deb25aee5 | -16.5147 | -57.2486 | 2024-10-06 03:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.7 |
| 85419b77-6bbd-3c2d-bd17-8ed003521910 | -16.515 | -57.2282 | 2024-10-06 03:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.7 |
| a11fe07a-48c2-3530-a5ec-8ec3f3f273fe | -16.5345 | -57.2259 | 2024-10-06 03:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.4 |
| 2511bfcf-fc29-35ec-a050-2bf3d65255ad | -16.554 | -57.2237 | 2024-10-06 03:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| b2c1b01d-dcec-3d63-abac-acffe459333b | -16.5544 | -57.2032 | 2024-10-06 03:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| cef47825-b479-3da4-ac7f-e8886ae7593d | -16.6923 | -55.9117 | 2024-10-06 03:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 96.7 |
| cb2a4259-3407-35fb-8847-cbcb068af7d8 | -16.7647 | -57.4856 | 2024-10-06 03:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.0 |
| 2aec80bb-5b8f-368d-99bd-ddd06b68c79e | -16.9545 | -56.6226 | 2024-10-06 03:06:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.3 |
| feb15516-118e-3c46-beb4-bc5db1f77538 | -17.0003 | -55.0817 | 2024-10-06 03:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 292840ef-0a4a-3d3a-babb-9b7ff61ab0b7 | -17.0007 | -55.0607 | 2024-10-06 03:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 463.4 |
| 1d3afcba-810d-3500-b9b0-de93be32d5c1 | -17.001 | -55.0398 | 2024-10-06 03:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 266.7 |
| ede012fe-8a22-3f3a-9c90-2050a0218fb2 | -17.02 | -55.0791 | 2024-10-06 03:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| beb2d751-ddf2-38f6-b8ff-b35a43f7ae40 | -17.0203 | -55.0581 | 2024-10-06 03:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 350.8 |
| 5caaab7d-66f5-3760-b5f0-7de07961bb6c | -17.0207 | -55.0371 | 2024-10-06 03:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 223.8 |
| c5caaa0d-fce4-3cd8-afdc-64203c8cdf4f | -17.1182 | -57.4039 | 2024-10-06 03:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.3 |
| 5b67322a-bc8a-37cc-811e-ca24c83c7a89 | -17.1375 | -57.4221 | 2024-10-06 03:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.0 |
| 0057cf10-19f3-368f-8b0a-bb2da375a050 | -18.6586 | -57.2759 | 2024-10-06 03:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.9 |
| 8b9bcedb-10e5-38a9-8990-f1d1c87be02e | -18.659 | -57.2552 | 2024-10-06 03:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.0 |
| bfe1973f-3251-321f-8074-0a00ac6697ec | -18.6387 | -57.2785 | 2024-10-06 03:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.9 |
| 3e67c5b2-e3a0-39a5-83b2-de53d1276d1d | -20.5813 | -49.3865 | 2024-10-06 03:07:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 0746da33-ea8a-3be3-b1cb-7ba78d3ec119 | -20.582 | -49.3635 | 2024-10-06 03:07:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 111.5 |
| af2f7919-3c5f-3b63-bb1e-b73e4589a555 | -20.6018 | -49.3821 | 2024-10-06 03:07:00 | GOES-16 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 606390f1-e9b6-3e29-b68f-66c0a3633acb | -21.5218 | -50.9088 | 2024-10-06 03:07:05 | GOES-16 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 138.5 |
| 142bad37-2275-33f1-bf9f-575ff4731360 | -2.7981 | -48.6873 | 2024-10-06 03:15:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 478b0dc6-c9ab-3502-aa0a-e95a573fad76 | -2.8165 | -48.7082 | 2024-10-06 03:15:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 9abb4bdc-e021-3c38-bb14-d2ffc135e0ba | -2.8166 | -48.6867 | 2024-10-06 03:15:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| e273ef31-91e1-3feb-bb45-50c593bd76b0 | -3.1129 | -48.6131 | 2024-10-06 03:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| fe41a1e5-aab2-313c-89b8-9ab3cc2d77dd | -3.113 | -48.5916 | 2024-10-06 03:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 07c957ad-436c-3739-bb62-9a83ba252b5c | -3.1314 | -48.6125 | 2024-10-06 03:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 988d0a76-2cfc-3e36-98f6-1ffcb4042682 | -3.1315 | -48.591 | 2024-10-06 03:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 671e2031-b975-3be2-95c1-419435ab7217 | -3.1432 | -50.2254 | 2024-10-06 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 90f2a2ee-069a-3935-bd69-825ece369c23 | -3.8464 | -46.4714 | 2024-10-06 03:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 030a0a25-094f-3810-9196-6368dd15ee0b | -5.0139 | -49.7696 | 2024-10-06 03:15:34 | GOES-16 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 47a30a49-dfbe-3147-a83c-3b415c3129e5 | -5.5716 | -44.8927 | 2024-10-06 03:15:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| f69d637e-3158-363b-af77-1ca3c4d21fda | -5.5718 | -44.87 | 2024-10-06 03:15:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| dd474a01-6f9d-32ea-82ca-163fe5524f2f | -7.9825 | -54.7752 | 2024-10-06 03:15:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| b9c13d0d-f425-3729-97d5-f0c307493026 | -9.1449 | -60.6612 | 2024-10-06 03:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.8 |
| fd7254a2-23a7-32ac-9030-8936265e9598 | -9.1759 | -61.5794 | 2024-10-06 03:15:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 11ca7210-f5af-3191-a991-d1868f6c7e7b | -9.3278 | -46.5385 | 2024-10-06 03:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 7eac0fd4-2e76-3cc8-bec9-69e9202f2a1f | -9.3467 | -46.5365 | 2024-10-06 03:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| b7c8961b-e920-3106-bdcc-0da6ff3bd8f9 | -9.3835 | -51.0881 | 2024-10-06 03:15:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 98b5cc3e-1a01-3f2f-81c2-4a546b7c356e | -9.3637 | -64.3378 | 2024-10-06 03:16:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 8003aa33-9acd-3687-be0a-ac1aac7d0f7b | -9.3638 | -64.319 | 2024-10-06 03:16:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 9bed9521-8467-355d-88f2-a91076fe2c2d | -9.688 | -47.8308 | 2024-10-06 03:16:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 05b57418-b3dc-31c7-8d4e-2ce3b228164b | -9.6883 | -47.8088 | 2024-10-06 03:16:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| bd03a3a1-70f4-31e7-a843-60491b011ec3 | -9.7069 | -47.8288 | 2024-10-06 03:16:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 46.2 |
| a3531c58-b0ae-3612-b478-78e5f892ad6b | -9.7072 | -47.8068 | 2024-10-06 03:16:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 5cbdc718-2dc0-344f-8acf-d487856c15a0 | -9.6778 | -64.6457 | 2024-10-06 03:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 38.6 |


[Clique aqui para ver as próximas entradas](README39.md)
