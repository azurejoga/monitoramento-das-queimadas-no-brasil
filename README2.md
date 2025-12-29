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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0e834b5-309f-3a55-a0d1-61f3686e1156 | -5.97412 | -44.58302 | 2025-12-29 00:32:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 39e71073-ff15-3763-b492-d183ff59d7d5 | -5.28766 | -45.82905 | 2025-12-29 00:32:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 51fad207-6098-3c5a-b497-317455e29199 | -4.1337 | -49.28224 | 2025-12-29 00:32:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 14d8cbc1-fbb3-3bc1-af9e-5a6dc04c85da | -5.23177 | -49.09035 | 2025-12-29 00:32:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 423d7f5e-a2c6-32ce-aa21-ad3547b49af3 | -3.27082 | -52.96316 | 2025-12-29 00:32:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d8134180-482a-366c-8303-f4cce2537e5a | -2.82705 | -52.88398 | 2025-12-29 00:32:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9c390f9c-8aa2-3812-9ebd-1719871c33f4 | -5.97705 | -44.60239 | 2025-12-29 00:32:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 26450c95-22e4-3a88-abb9-4cd99aa73c10 | -2.87098 | -45.51334 | 2025-12-29 00:32:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 33bc6fbf-7ebd-3adc-bd54-a6b594c4a159 | -3.94748 | -50.44738 | 2025-12-29 00:32:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 09396ddd-56d1-3cb5-9993-bf7d87e76d5d | -1.94533 | -50.57138 | 2025-12-29 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 02203821-5548-3d32-8f81-274b0fcff62f | -1.61956 | -54.2239 | 2025-12-29 00:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| af7bca78-324d-3e93-a343-f8b8ba828d3e | -1.61814 | -54.21354 | 2025-12-29 00:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 441ba358-00a4-317a-b115-0f919b508db2 | -1.12027 | -47.74026 | 2025-12-29 00:34:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0d6d1549-9dc5-351d-bc87-351e599413bd | -1.83872 | -54.77296 | 2025-12-29 00:34:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 871e66b4-de7a-3bd4-8db4-220287e6f357 | -1.9385 | -52.1133 | 2025-12-29 00:34:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| db691467-2a2a-3b5e-b953-4847db550a63 | 4.0913 | -60.882401 | 2025-12-29 01:06:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 05e14ad6-3b46-3d25-a6a7-4e9994a7ed44 | -19.3497 | -40.8888 | 2025-12-29 01:10:00 | GOES-19 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 66.9 |
| e38dc4b2-ed6d-3ca9-ac9e-4dc9ee82c411 | -19.3497 | -40.8888 | 2025-12-29 01:30:00 | GOES-19 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 71.4 |
| 083d2399-0e56-3537-ac74-9f137473ace9 | -5.9858 | -44.589 | 2025-12-29 01:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 5c50a7c2-a868-3327-b199-c887cf555345 | -17.5545 | -57.1258 | 2025-12-29 01:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.1 |
| f6ccad59-9964-3d12-8333-982312707ed2 | -6.8847 | -35.1216 | 2025-12-29 01:40:00 | GOES-19 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 108.4 |
| b4e8ec69-75c2-386c-9646-9b5361ebec7c | -6.8656 | -35.124 | 2025-12-29 01:40:00 | GOES-19 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 115.2 |
| e6368f76-c2be-3f60-9da4-d8fe7e937dbf | -6.8851 | -35.0941 | 2025-12-29 01:40:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 89.5 |
| ae6eef03-ebd1-316c-8f7b-ab9e141c971b | -6.866 | -35.0965 | 2025-12-29 01:40:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 97.2 |
| b4c66045-fe6f-3b59-ad49-5ab5fb381efa | -17.567301 | -57.125 | 2025-12-29 01:46:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f4a5aa3a-894b-3617-a4dc-5503cdd99b38 | -17.5576 | -57.127602 | 2025-12-29 01:46:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c7727f2f-e156-385b-9de7-dbde220d602f | -17.564501 | -57.113899 | 2025-12-29 01:46:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a1faa061-ea0c-3bcd-b4b4-5f0aa77112bd | -2.4499 | -47.7919 | 2025-12-29 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| bf2d7c70-be07-3fb3-8b08-e1a4b851ecba | -5.53013 | -35.45757 | 2025-12-29 03:10:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6c535725-54b2-3046-9dbd-4e1dcbad1953 | -8.48093 | -35.40216 | 2025-12-29 03:12:00 | NOAA-21 | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c70c1044-a808-3203-acf8-b6f247dbf2c7 | -8.48212 | -35.39896 | 2025-12-29 03:12:00 | NOAA-21 | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| c232645f-738f-3902-92e8-b71238109506 | -7.74545 | -35.21612 | 2025-12-29 03:12:00 | NOAA-21 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 402be002-f4a6-3e82-b9e4-812a5621a0c2 | -8.89533 | -35.34337 | 2025-12-29 03:12:00 | NOAA-21 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2d3cf5c8-51e4-3a6f-8cbf-d6de528ad610 | -7.40897 | -35.13671 | 2025-12-29 03:12:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a9a14c7f-e2f9-3674-9cdc-4059e166a282 | -5.85624 | -40.3463 | 2025-12-29 03:12:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6464125f-fb25-3131-85ac-2ad676a54fa0 | -17.29079 | -41.82517 | 2025-12-29 03:14:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 84b5898d-592b-3d3e-80f3-bfb0acc001c1 | -17.29667 | -41.82641 | 2025-12-29 03:14:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| fbae7aac-8011-3765-a519-35beded16baf | -17.29056 | -41.82513 | 2025-12-29 03:14:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7cb0b9b0-0ece-3540-b25c-e10ca18f66f9 | -15.96679 | -43.28605 | 2025-12-29 03:14:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c80eadfd-d386-3df3-bf9a-f0cc57bb70fb | -17.29689 | -41.82649 | 2025-12-29 03:14:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a629ba84-2dd8-3fb6-b7c7-80e07c526684 | -15.96864 | -43.28385 | 2025-12-29 03:14:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2cf14514-035a-3f57-8789-c207ba573649 | -15.96195 | -43.28195 | 2025-12-29 03:14:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 152f2e64-7ce8-3f8d-b655-a2f908fdf085 | -19.33644 | -40.90368 | 2025-12-29 03:17:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| d512e5ad-d0b0-357a-ad0f-78a68a02bb09 | -20.38673 | -40.56272 | 2025-12-29 03:17:00 | NOAA-21 | VIANA | ESPÍRITO SANTO | Brasil | 3205101 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2af0b172-6719-34a5-b1bc-03b019e4ef79 | -19.33366 | -40.89706 | 2025-12-29 03:17:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9db79be1-3bd3-347c-9ec5-1813f54b146f | -22.99693 | -45.17989 | 2025-12-29 03:17:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2b15d3ff-e848-333d-979a-bad53982574f | -19.33877 | -40.89321 | 2025-12-29 03:17:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 2bb65c3b-579e-32f1-b145-a80023a3398d | -20.50613 | -41.71582 | 2025-12-29 03:17:00 | NOAA-21 | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a0ca0c9c-7571-3b90-adf8-55e50eac0b16 | -20.18201 | -40.21561 | 2025-12-29 03:17:00 | NOAA-21 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d9f486d5-8843-3df3-b4d1-3fe4a60fbdc6 | -22.99546 | -45.18576 | 2025-12-29 03:17:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 14ca16bf-bfcd-3707-94e9-61404b2320e8 | -19.33127 | -40.90071 | 2025-12-29 03:17:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 840b86f0-9538-346b-88ed-92842fc4619b | -20.2096 | -40.21498 | 2025-12-29 03:17:00 | NOAA-21 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2787ce0a-0b97-3828-ba6c-f78c6cd8ada2 | -20.5053 | -41.71951 | 2025-12-29 03:17:00 | NOAA-21 | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1be1d0db-c435-37b4-89ff-1c9fc7a9e6e8 | -20.21032 | -40.21159 | 2025-12-29 03:17:00 | NOAA-21 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3b706bb3-20fc-33b0-a024-53fb684fb01d | -19.33339 | -40.89123 | 2025-12-29 03:17:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 151c54f5-6d8f-31ab-a146-0d9e658d4c45 | -20.18128 | -40.219 | 2025-12-29 03:17:00 | NOAA-21 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6cca0ba0-b2d8-3a68-b29a-38d806263904 | -19.33243 | -40.89553 | 2025-12-29 03:17:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 557fcad2-fd96-32bd-b508-e0b0431f096f | -19.33875 | -40.90045 | 2025-12-29 03:17:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 96a52eb1-80ab-30b8-862b-b8260a248a0f | -20.38948 | -40.56345 | 2025-12-29 03:17:00 | NOAA-21 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b1fb5d51-f552-33d4-8281-62e1c4fa5308 | -19.3399 | -40.89511 | 2025-12-29 03:17:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 40d332e4-c57f-3a34-946a-212f7b3ac3f0 | -19.33465 | -40.89243 | 2025-12-29 03:17:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b8f98403-8449-3874-a9eb-e04597ac498d | -19.33771 | -40.89797 | 2025-12-29 03:17:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 839860a1-9387-33e8-8f1c-b4a0c583f0cd | -19.33247 | -40.9026 | 2025-12-29 03:17:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ecc8b82b-73ff-3159-91e5-33a353e573db | -5.24627 | -38.22027 | 2025-12-29 03:40:00 | NPP-375D | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 93b2766c-10d4-3424-865f-dcee4a5eafa3 | -5.33382 | -37.05318 | 2025-12-29 03:40:00 | NPP-375D | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dbc8be14-ec6d-3fca-99c1-7fead19048ee | -6.07815 | -40.42222 | 2025-12-29 03:40:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5dd18a6f-fab4-3066-bef9-a3e4431fa1d2 | -5.33311 | -37.05756 | 2025-12-29 03:40:00 | NPP-375D | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5f97a5f4-80ec-34d1-a7fc-30e6ed9b177e | -7.12405 | -35.00121 | 2025-12-29 03:40:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 16fe3a0a-7998-3bba-8100-a5450c023b9f | -7.4761 | -35.26341 | 2025-12-29 03:40:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a6b7fcc1-ba88-3341-b820-94da5acdafa4 | -7.40842 | -35.13789 | 2025-12-29 03:40:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| cd2853e5-47bb-3408-9803-ffcc04bd6f4e | -3.9047 | -42.56403 | 2025-12-29 03:40:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 129939f4-3a66-387e-b356-a7b8c2062637 | -5.33113 | -36.8395 | 2025-12-29 03:40:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d2078b87-06bc-31ba-8525-f778c3f1c895 | -6.986 | -34.94226 | 2025-12-29 03:40:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b6c41b2b-a68f-3e90-8c2a-9812ca08e360 | -3.90529 | -42.56049 | 2025-12-29 03:40:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f9dd92f6-334f-3f10-b1fa-3b9c48e92933 | -5.85689 | -40.34597 | 2025-12-29 03:40:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ec6eec64-12e1-3ce5-8c46-4918b43c936b | -7.25139 | -35.22718 | 2025-12-29 03:40:00 | NPP-375D | SÃO MIGUEL DE TAIPU | PARAÍBA | Brasil | 2515005 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 80382eae-c7af-3995-996a-1104616d0226 | -3.89984 | -42.55957 | 2025-12-29 03:40:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 68eb1d16-702f-3323-a7a9-3816dc8aa960 | -3.21409 | -43.45918 | 2025-12-29 03:40:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5076f47e-1bd3-3f8d-9857-8f72bc018e0a | -3.2134 | -43.4633 | 2025-12-29 03:40:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 594d0cfb-af02-3a79-a0f9-0f392cdd3ea4 | -7.06439 | -39.88199 | 2025-12-29 03:40:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 96a4941d-9d7e-385d-a28b-06b87a75a712 | -5.33479 | -36.8401 | 2025-12-29 03:40:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1ca47890-60bf-3455-9345-76787d74735d | -7.74668 | -35.21391 | 2025-12-29 03:40:00 | NPP-375D | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 312a0640-600d-300d-9773-bd32b3c6f62a | -5.86141 | -40.34679 | 2025-12-29 03:40:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 174c746e-bbaf-3e57-bc9b-c4e4cb9eab55 | -7.56371 | -35.26224 | 2025-12-29 03:40:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f26c1ff1-4eaa-3822-8a4b-79fff62ec7c4 | -5.52724 | -35.45754 | 2025-12-29 03:40:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f459ac0e-12db-3752-80af-007c84322656 | -4.27252 | -38.15072 | 2025-12-29 03:40:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| acc2c8f7-5a10-329e-b0ef-3af72e4801f4 | -11.55536 | -46.3014 | 2025-12-29 03:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c5177d5-bb50-3781-a205-ecf48e68b6cc | -11.55446 | -46.30594 | 2025-12-29 03:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8cafd47-437d-36e7-bdac-8e3448b2ff9c | -10.61549 | -44.87852 | 2025-12-29 03:42:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e10d95e-85fc-32e3-9613-6dbcee1bba00 | -11.54844 | -46.30441 | 2025-12-29 03:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e901365-8b0c-3b44-9ebd-cbd2b5a3343f | -10.61473 | -44.88247 | 2025-12-29 03:42:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da405845-5224-39b4-93ff-49e85ea68208 | -11.96855 | -44.15854 | 2025-12-29 03:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3d9b198-bace-3786-aec7-d3a15872412e | -11.74873 | -44.59195 | 2025-12-29 03:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3de53fc0-b076-3158-b8da-11775d58dc12 | -10.76962 | -37.1428 | 2025-12-29 03:42:00 | NPP-375D | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7313d564-93c2-3640-9043-49b5e6abf786 | -8.54037 | -35.74873 | 2025-12-29 03:42:00 | NPP-375D | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3ab89741-66a9-30d9-9983-7eea9033b4ea | -11.54937 | -46.29976 | 2025-12-29 03:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a170d80-5f77-392e-a19c-e4e468df159c | -7.61168 | -40.00413 | 2025-12-29 03:42:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 1146a1a4-51d0-333a-8d93-4d72de17957e | -11.54657 | -46.31375 | 2025-12-29 03:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c57c5a1d-32ed-3617-ad47-6f128fa65423 | -12.21065 | -38.98391 | 2025-12-29 03:42:00 | NPP-375D | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 06f6f8a0-e491-3b43-9b74-05603ff8ebb5 | -8.27228 | -35.27247 | 2025-12-29 03:42:00 | NPP-375D | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |


[Clique aqui para ver as próximas entradas](README3.md)
