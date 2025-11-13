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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aaa7b1f3-17a7-331e-990b-1f754b2afd6d | -8.8699 | -49.9398 | 2025-11-13 00:58:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37826d18-fbe5-355c-9bb6-026584b3a8ae | -20.4618 | -53.058498 | 2025-11-13 00:58:00 | METOP-C | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| db199d89-9bdb-3fb5-be53-1ffc4566b5f7 | -17.0331 | -46.750801 | 2025-11-13 00:58:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fb94e75b-0fe6-3fb7-8d39-5b978070100d | -3.1593 | -50.2738 | 2025-11-13 00:58:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5297d438-7e3d-34ed-a96a-aee2d45d30ee | -4.1102 | -48.005001 | 2025-11-13 00:58:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc5c3df1-18da-3290-98ec-1feb05710e11 | -12.663 | -46.745098 | 2025-11-13 00:58:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 55456c57-8b5d-38ed-acb3-c6684e213e4d | -12.0667 | -48.212898 | 2025-11-13 00:58:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3540cef6-e8ed-33cb-af2c-904a95488d3b | -2.4489 | -49.2603 | 2025-11-13 00:58:00 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11a330ca-8899-300e-ab58-5e3ce8003503 | -3.2122 | -50.1908 | 2025-11-13 00:58:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b505a669-83ef-398c-b017-d033dba28e9e | -8.5576 | -48.014198 | 2025-11-13 00:58:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fe5329ae-e4c2-37eb-9374-41675e308003 | -2.8313 | -52.867599 | 2025-11-13 00:58:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89f007ca-b28d-3486-bf84-88f1fa49891e | -6.57 | -48.725201 | 2025-11-13 00:58:00 | METOP-C | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b37f6ae-2029-37df-944f-45b949aeda5d | -4.3207 | -48.241001 | 2025-11-13 00:58:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9276a15-d027-3bbe-842d-d46781fa3124 | -3.1693 | -50.626301 | 2025-11-13 00:58:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ee14c53-a499-36fc-a247-092b7bfb940e | -3.8628 | -49.7981 | 2025-11-13 00:58:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57d284dc-80ba-370d-9a4b-d2f5cc005f10 | -3.8504 | -50.053902 | 2025-11-13 00:58:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 201dc048-54af-36a4-916c-aecc6860240e | -10.9331 | -44.616199 | 2025-11-13 00:58:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 940123ae-fb9f-3f14-9710-f978f48b7c01 | -3.4452 | -45.564201 | 2025-11-13 00:58:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6efda8f0-44d4-32ad-bd88-c83cb301bb3d | -9.642 | -44.532902 | 2025-11-13 00:58:00 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9ad56c80-6c5c-36dc-8336-5f0398b2c349 | -3.8685 | -49.7784 | 2025-11-13 00:58:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef8b978f-7738-3cad-a26e-f3b953946ade | -20.4601 | -53.049599 | 2025-11-13 00:58:00 | METOP-C | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e7af7078-2ff0-3a01-9ba5-b13dd1ce241f | -4.8949 | -48.969101 | 2025-11-13 00:58:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f990a35b-c2ac-3ddf-8588-dd9b29513b6f | -3.3552 | -49.831402 | 2025-11-13 00:58:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6691cd40-c617-363b-8a43-68a280b00e72 | -20.452 | -53.060699 | 2025-11-13 00:58:00 | METOP-C | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e0614dd0-c7b0-3ffb-8361-fba4917f390f | -6.1618 | -48.050999 | 2025-11-13 00:58:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0cb29e5b-18c5-3a03-a935-b60733bd4039 | -3.677 | -45.931 | 2025-11-13 00:58:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1a6046d7-e66a-3740-8610-294b5508e53f | -2.8217 | -45.444099 | 2025-11-13 00:58:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ffde7ce4-deea-3cdd-8b48-7f1ec2f2d84a | -3.0934 | -49.285099 | 2025-11-13 00:58:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7808130-2852-3799-af25-76d1703f16d9 | -4.0215 | -48.806 | 2025-11-13 00:58:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c575e8eb-ea69-3b23-a3c0-c441c5d25638 | -5.3383 | -45.1982 | 2025-11-13 00:58:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 52c496d7-8573-3d91-a489-9515dbb88c8f | -12.6606 | -46.7351 | 2025-11-13 00:58:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 55e0706d-a646-377a-ae25-8c82c5abef9c | -18.028299 | -51.0308 | 2025-11-13 00:58:00 | METOP-C | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fa1d749f-8347-393f-abb6-b2c06c38a0a1 | 1.459 | -55.834499 | 2025-11-13 00:58:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4657440-0d9e-3109-a2c2-9aeaa0062fc1 | -5.3246 | -45.1842 | 2025-11-13 00:58:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8dff621c-ef8b-3d11-a0dc-8c13efa30c87 | -3.1554 | -50.257 | 2025-11-13 00:58:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 912a4ccd-0613-333d-aaab-b02c303ce9d9 | -4.1128 | -48.015999 | 2025-11-13 00:58:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb97362b-6f72-3de9-877c-d9c8a890c511 | -2.461 | -49.267799 | 2025-11-13 00:58:00 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a279a163-9360-38b5-b697-8f71abce0d8b | -2.8314 | -45.441898 | 2025-11-13 00:58:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c9c134da-a2f5-38e7-ab5e-dea074485695 | -9.6362 | -44.5509 | 2025-11-13 00:58:00 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 587100ad-352a-3119-a2d4-3cf214257366 | -12.5996 | -48.323299 | 2025-11-13 00:58:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 21af5861-2fcf-3b17-900b-fc5ae1ec0ca6 | -4.246 | -49.673199 | 2025-11-13 00:58:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d817290-143a-373e-987d-69cb044dd25c | -8.8662 | -50.188801 | 2025-11-13 00:58:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bf5f321-2362-3fa0-ae95-4df08f829d21 | -4.3109 | -48.243301 | 2025-11-13 00:58:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 663fe1e7-6a51-3bcc-bfe1-836607a8d953 | -3.1512 | -45.492699 | 2025-11-13 00:58:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2f400649-f8ff-3241-89aa-3d2a039c047c | -4.5254 | -46.424801 | 2025-11-13 00:58:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5fbfd004-5aa3-38dc-8beb-aa6ba50fc508 | -3.783 | -52.1628 | 2025-11-13 00:58:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7f6fb70-a462-3bd0-ba76-259090a685b7 | -1.9421 | -52.0965 | 2025-11-13 00:58:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 979ac0c1-ece0-3073-9018-4a00608cea5f | -3.4731 | -43.187599 | 2025-11-13 00:58:00 | METOP-C | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 432e24c6-7a2f-3158-966f-b212da5b6a1b | -3.8746 | -49.804501 | 2025-11-13 00:58:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| befd2aa6-8b3c-374f-b6df-03805ad28804 | -3.4395 | -45.583 | 2025-11-13 00:58:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cb70318b-3d97-3a84-88c0-eee30c298d05 | -3.4531 | -45.597198 | 2025-11-13 00:58:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d1dd00ff-07d2-3b42-856b-6c19c7d86e94 | -3.1574 | -50.2654 | 2025-11-13 00:58:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 539e9c28-74b9-3b36-95fe-f420b4337352 | -3.8607 | -49.789398 | 2025-11-13 00:58:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34f4d7e0-7be3-3f77-9a45-418ceee23be4 | -3.1674 | -50.618198 | 2025-11-13 00:58:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e5c997c-6de8-3f2f-b501-4819aae077ab | -5.4567 | -47.689301 | 2025-11-13 00:58:00 | METOP-C | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8585166e-5234-318f-a6d2-de9a376c24d6 | -12.0647 | -48.2043 | 2025-11-13 00:58:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 715ba916-a630-35da-9bab-e6693fb9f132 | -6.1716 | -48.048698 | 2025-11-13 00:58:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb307ff0-6937-30e3-a7ce-c689813a48ab | -10.3519 | -47.700901 | 2025-11-13 00:58:00 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5219c13e-4a1d-37b8-b986-2b839192cb3f | -3.1568 | -45.473499 | 2025-11-13 00:58:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2102d04b-bcf6-37c7-a103-4d1a6f6a73e6 | -10.8592 | -44.937599 | 2025-11-13 00:58:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8f9f399a-be3d-37d5-a210-55c71d1fb531 | -10.9234 | -44.618698 | 2025-11-13 00:58:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e2dd995b-56d9-3b37-98bb-926dcea847a7 | -4.0094 | -48.973301 | 2025-11-13 00:58:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3794a21f-e5c1-394e-819d-30c9d88c6dfb | -2.8355 | -45.459099 | 2025-11-13 00:58:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0f79f88c-7fe4-3e36-9133-446e68487ae8 | -1.9404 | -52.089298 | 2025-11-13 00:58:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa9453d0-fd90-31a3-bb31-b34c466c024c | -3.1009 | -49.2733 | 2025-11-13 00:58:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01c3ba89-72bf-3197-967e-aa934750a2f8 | -3.038 | -50.283798 | 2025-11-13 00:58:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 492a5ca8-1220-3646-a123-a9db1923d355 | -3.2374 | -45.595901 | 2025-11-13 00:58:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e5983612-ff21-3097-9a2a-6dfe15c90115 | -2.0068 | -54.444302 | 2025-11-13 00:58:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7b04c2b-47a7-3cbd-9680-57e8a27366bf | -3.1649 | -45.507198 | 2025-11-13 00:58:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a1804aed-7295-31ba-ad68-02c3428ba2bf | -5.3286 | -45.2005 | 2025-11-13 00:58:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b4e28509-f2ea-3412-9d43-c3b5cd1bcedf | -10.3704 | -45.047798 | 2025-11-13 00:58:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 04acb2ca-55c9-3153-9562-6ffd9698e94b | -1.7078 | -54.669601 | 2025-11-13 00:58:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d01918d-20ef-3ded-b5e6-b7c829ae07a6 | -7.6647 | -45.869701 | 2025-11-13 00:58:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2331531f-6b87-3ee8-9518-606c6f60591a | -10.45 | -47.338001 | 2025-11-13 00:58:00 | METOP-C | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f10627da-24d5-37de-95b4-f497a2465d95 | -4.2087 | -50.0868 | 2025-11-13 00:58:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66008582-b746-37c1-9523-9ef139974aba | -10.3617 | -47.698502 | 2025-11-13 00:58:00 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61cab524-d8a0-326c-8301-b00e6c970403 | -3.04 | -50.292198 | 2025-11-13 00:58:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6974273b-8ede-3853-bded-47a1e8c21ce8 | -3.1031 | -49.282902 | 2025-11-13 00:58:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08962ab9-b85b-3d78-88fa-1c5ab71a06fa | -10.4476 | -47.328098 | 2025-11-13 00:58:00 | METOP-C | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fcba9e16-7eb9-348f-95d8-0170e79c8bd3 | -3.0986 | -49.263802 | 2025-11-13 00:58:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ce48dcf-75f9-30a1-8e02-5bb524d9251c | -4.717 | -46.452 | 2025-11-13 00:58:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2c850ea0-b696-39d4-869c-49a77a447864 | -2.8915 | -48.075001 | 2025-11-13 00:58:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31df8e47-f785-3770-99ab-2b4b7bc1cc21 | -4.5384 | -46.436298 | 2025-11-13 00:58:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 86485a70-986e-3f94-9710-2e8fb23feb69 | -4.7235 | -46.436001 | 2025-11-13 00:58:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7a65a51d-0eac-3840-9b69-9bedb54588ad | -10.6324 | -45.2276 | 2025-11-13 00:58:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| de831b21-d9e0-3e3a-aaa3-06030dd0f90f | -3.4492 | -45.5807 | 2025-11-13 00:58:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 52f64968-12ea-3812-b7bd-d66f7c47320f | -4.2232 | -48.5695 | 2025-11-13 00:58:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0cc3e36-0c20-301f-b80a-c85771e95aab | -3.0912 | -49.2756 | 2025-11-13 00:58:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee4e801e-630f-3626-b2be-b00b38d005b5 | -3.6673 | -45.9333 | 2025-11-13 00:58:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9659ccf5-73cf-3204-b82d-d306cc10bce0 | -3.1609 | -45.490398 | 2025-11-13 00:58:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8f5d9890-f1b4-3b2f-9684-38e1c4e743c6 | -10.7578 | -44.904301 | 2025-11-13 00:58:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 75c9af8e-3ea4-3a67-855a-6eb9e82e3b24 | -5.3897 | -46.766399 | 2025-11-13 00:58:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 451a4ca9-34a0-378b-bcfa-40869c58efc3 | -4.5287 | -46.438599 | 2025-11-13 00:58:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b3aa1be7-e855-3a6f-9ed5-2ceaa985c50c | -13.005 | -49.7831 | 2025-11-13 00:58:00 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d3e934d5-1534-30b4-87d5-c075531220cf | -4.7202 | -46.422199 | 2025-11-13 00:58:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f6d9db8f-8884-3e9f-8acb-30e12ff488c2 | -7.6778 | -45.880798 | 2025-11-13 00:58:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d3ea57b-b17f-3053-95a3-ee8c8864ee09 | -4.7268 | -46.449699 | 2025-11-13 00:58:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 892e653e-a060-3c4e-9449-a9608bbbcbd8 | -6.152 | -48.053299 | 2025-11-13 00:58:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca226d00-de0a-3b5d-9a8d-b0067d7dfd9a | -4.2185 | -50.084599 | 2025-11-13 00:58:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cebdc9a-c522-3540-addf-f90a29eab764 | -10.6357 | -45.241001 | 2025-11-13 00:58:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README8.md)
