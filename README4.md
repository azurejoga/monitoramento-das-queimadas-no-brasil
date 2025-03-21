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
| 0a8fc0e9-8dbd-327a-b1b9-4d8935b4d569 | -19.43631 | -54.78255 | 2025-03-21 04:10:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d2cb37e3-e69f-3677-81ad-ad06080c54e2 | -22.92168 | -45.41436 | 2025-03-21 04:10:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bd75fa89-17b5-3494-8bf1-dc4444c96948 | -19.43003 | -54.78494 | 2025-03-21 04:10:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 208c196d-2446-30c2-8d9e-0f789b2b2fc4 | -20.92605 | -56.54726 | 2025-03-21 04:10:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9137e52e-9bfa-36b0-8323-e3abe89129b0 | -23.98597 | -48.9164 | 2025-03-21 04:10:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e13650c0-46c9-3ac7-99c8-a584a370d8a7 | -22.54102 | -48.8112 | 2025-03-21 04:10:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99d3fe84-1099-366c-9f08-4202add74d4c | -19.43089 | -54.78101 | 2025-03-21 04:10:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d0c58ad0-1256-36a3-8521-fda780bf79f7 | -20.7652 | -46.76803 | 2025-03-21 04:10:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f2d613d6-868e-3c4b-bf92-ddb3978c76a0 | -30.70971 | -54.18458 | 2025-03-21 04:12:00 | NOAA-20 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 3.5 |
| 806a0834-63bb-3c43-ae84-63288bc4946b | -28.83884 | -50.63109 | 2025-03-21 04:12:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 33ae311a-5469-38b5-844b-14a0bc99ec6f | -27.96866 | -51.63734 | 2025-03-21 04:12:00 | NOAA-20 | LAGOA VERMELHA | RIO GRANDE DO SUL | Brasil | 4311304 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8e822428-b7b5-35c8-9874-3405548ef789 | -30.73079 | -54.19001 | 2025-03-21 04:12:00 | NOAA-20 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 24424947-cb02-36c7-be65-030c88f81f16 | -27.84728 | -50.1789 | 2025-03-21 04:12:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7c73c283-b8b9-3786-820d-1210df4ad71e | -27.3887 | -51.17615 | 2025-03-21 04:12:00 | NOAA-20 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 20396663-bffa-37e6-b2f3-d2157337026a | -30.7298 | -54.19469 | 2025-03-21 04:12:00 | NOAA-20 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 2.7 |
| 6b32c865-b70c-332f-bb77-d57903e30fe4 | -28.58724 | -49.44141 | 2025-03-21 04:12:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2c64e176-8e51-3c31-9bcd-7e60300159d7 | -27.3877 | -51.18137 | 2025-03-21 04:12:00 | NOAA-20 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1a54db35-5d7b-3613-9996-935693445db6 | -28.78061 | -51.09545 | 2025-03-21 04:12:00 | NOAA-20 | CAMPESTRE DA SERRA | RIO GRANDE DO SUL | Brasil | 4303673 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| faf8f1de-9321-3bbb-9335-d78e5c72adef | -27.84643 | -50.18363 | 2025-03-21 04:12:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ed56117c-5911-3062-988d-50e9c810daa8 | -30.72884 | -54.1992 | 2025-03-21 04:12:00 | NOAA-20 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 2.7 |
| f355ac4e-358d-3535-af4d-bfe4d557dc2a | -31.31787 | -54.15891 | 2025-03-21 04:12:00 | NOAA-20 | BAGÉ | RIO GRANDE DO SUL | Brasil | 4301602 | 43 | 33 | nan | nan | nan | Pampa | 10.2 |
| 8d5c2b52-cc2c-3c1d-8002-b21855910d6f | -29.60702 | -56.09799 | 2025-03-21 04:12:00 | NOAA-20 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 8f79cdd0-d129-33f7-b80a-0c273c8963b5 | -27.38492 | -51.17515 | 2025-03-21 04:12:00 | NOAA-20 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4cea563b-ed3d-358c-a92e-183bead3b912 | -30.71072 | -54.17984 | 2025-03-21 04:12:00 | NOAA-20 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 3.5 |
| 33af502c-130f-3c03-95eb-c8e7244cda7e | -30.71272 | -54.17043 | 2025-03-21 04:12:00 | NOAA-20 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 5b3dfdec-d3ea-33d7-8396-c30e7da3b51d | -28.88683 | -50.3079 | 2025-03-21 04:12:00 | NOAA-20 | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 89ba114c-3803-3fb2-a775-3ff6ed20e4f0 | -31.54828 | -51.36223 | 2025-03-21 04:12:00 | NOAA-20 | SÃO JOSÉ DO NORTE | RIO GRANDE DO SUL | Brasil | 4318507 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 26de7307-ede9-3753-a55b-ca5bc21d988d | -27.84737 | -50.18124 | 2025-03-21 04:12:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0f945f05-e6cf-369c-b79c-f8ab14337544 | -30.71372 | -54.16572 | 2025-03-21 04:12:00 | NOAA-20 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 07594288-7d33-3621-afc3-f824bc084266 | -30.74375 | -52.65972 | 2025-03-21 04:12:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| ec5404e8-8fe5-321c-a904-091c5095b6f9 | -30.72462 | -54.19814 | 2025-03-21 04:12:00 | NOAA-20 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| a39339d4-2768-306f-8562-bf5f3ad8a3d9 | -28.35751 | -51.52098 | 2025-03-21 04:12:00 | NOAA-20 | LAGOA VERMELHA | RIO GRANDE DO SUL | Brasil | 4311304 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b5bd43d6-db70-32c4-a0ae-b1fe12bdfbbc | -30.71911 | -54.1822 | 2025-03-21 04:12:00 | NOAA-20 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| e63a540e-210c-3fb7-a434-6af7ff7123e3 | -30.73176 | -54.18542 | 2025-03-21 04:12:00 | NOAA-20 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 2cb79676-9ab2-3d24-a437-0fe05770521d | -29.60476 | -56.09883 | 2025-03-21 04:12:00 | NOAA-20 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| a126e4f3-fb20-3bd5-8c9a-3f232076511e | -3.11758 | -59.92912 | 2025-03-21 04:57:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c208ee1e-5709-3294-a0de-7672c35fbfb3 | -7.93317 | -61.5551 | 2025-03-21 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e924c10-e6bb-372b-8d34-5c36c8251f8a | -12.27239 | -43.53456 | 2025-03-21 04:59:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8caad696-8cf9-39d2-8a8e-90e8d4865c82 | -11.95359 | -55.91691 | 2025-03-21 04:59:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d46b582f-b097-38ec-876f-abb9b5398232 | -12.27459 | -43.53439 | 2025-03-21 04:59:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0152774-2515-3576-82b5-abc529409fe4 | -11.2023 | -55.52429 | 2025-03-21 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75138be6-bdf3-3516-89fa-992e6fdbeeca | -16.3077 | -53.84113 | 2025-03-21 04:59:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 978e4887-5406-369e-9bac-baf573384021 | -15.59836 | -57.34494 | 2025-03-21 04:59:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47061f70-71ac-3e80-8195-39326ed364cb | -15.60228 | -57.34188 | 2025-03-21 04:59:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eba74eeb-c1c4-3232-b365-92c59f0d725f | -15.88354 | -58.80532 | 2025-03-21 04:59:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d18180d8-b1a4-3ec0-9d22-03b2249e5adb | -13.66675 | -52.13492 | 2025-03-21 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f19e057-9187-3d85-8f8d-3b01000086e5 | -15.59735 | -57.32985 | 2025-03-21 04:59:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 980ebcb4-cd52-3843-b192-89dde749d06f | -15.59677 | -57.33348 | 2025-03-21 04:59:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47e8803a-3ccf-3261-8d75-bd1a950df446 | -15.65654 | -59.1847 | 2025-03-21 04:59:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e27fc44-eb77-39eb-b77e-1576781018c7 | -15.27556 | -60.21094 | 2025-03-21 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bc04ab2-c244-38e9-b239-0ea24a06d9d5 | -13.67046 | -52.13549 | 2025-03-21 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c0bc4a8-f9dd-3398-aa0c-d63659f22c8f | -15.73379 | -58.24518 | 2025-03-21 04:59:00 | NOAA-21 | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8973155a-9428-3238-8e23-1590738945df | -13.67111 | -52.13095 | 2025-03-21 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c617fd47-ef3f-3b55-a3c3-1caca4efddfc | -15.6001 | -57.33405 | 2025-03-21 04:59:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c97b8c0e-8eee-368c-a715-b3725d289974 | -15.5768 | -54.98561 | 2025-03-21 04:59:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a30e0359-e002-3f05-8691-a36a6300e63e | -15.51546 | -57.26782 | 2025-03-21 04:59:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2dc6afb-a00d-3f6c-b415-d2bbcf4757d1 | -16.30418 | -53.84061 | 2025-03-21 04:59:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73ffe532-d168-333e-a037-c39b05219980 | -15.30381 | -54.95464 | 2025-03-21 04:59:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 55393572-df09-3485-86fb-9b2d4d87a5f3 | -15.65584 | -59.18882 | 2025-03-21 04:59:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d580f270-8c12-369d-a28f-667164f26107 | -15.10629 | -53.80307 | 2025-03-21 04:59:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75b0517f-66dc-3665-a4c9-23dfeaa1be14 | -13.67482 | -52.13149 | 2025-03-21 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 768337a2-39c0-34d1-b5c1-d374d3c3db3d | -15.10572 | -53.80705 | 2025-03-21 04:59:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac8a277f-333b-3cc9-97f1-70b78273f10e | -15.55753 | -56.02877 | 2025-03-21 04:59:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6523b2fb-89c2-39fb-871e-53207380094e | -15.28836 | -60.20381 | 2025-03-21 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7edd9437-0873-38a0-998c-65abae2608ee | -19.43124 | -54.78513 | 2025-03-21 05:01:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3afcb096-5c0b-39e0-af12-2b429fcb8094 | -20.21202 | -46.68139 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aee23551-7164-38c3-a7d0-0b964bc537d4 | -20.21935 | -46.66586 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 05ec8259-4ebb-3f3b-99e0-60ee81755bd8 | -20.22057 | -46.66304 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a183422f-f3a4-3af1-8225-aa7385726fe8 | -19.28395 | -55.24972 | 2025-03-21 05:01:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| ad44b337-5655-31f4-afc7-46b0cb09916d | -19.10614 | -57.57761 | 2025-03-21 05:01:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2e045c04-a3f4-36ea-bb4f-dc8068a44ba9 | -24.90543 | -51.03521 | 2025-03-21 05:01:00 | NOAA-21 | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c7dcf853-5248-301d-96df-012d91a6eb7b | -20.1202 | -46.77286 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 59a67586-0037-3004-ac43-514a0fd93e5e | -20.1198 | -46.77684 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1d97b9d7-61ac-3ae6-8b53-3994c4ce10f1 | -20.21237 | -46.67775 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8db73a24-44e0-36b5-acd3-7d2c7ec8e1d1 | -19.69591 | -53.76856 | 2025-03-21 05:01:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c72eef94-08ab-341c-a581-5945a445cf07 | -20.20689 | -46.67436 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 712279e9-4b27-39dc-a095-86b126b9fe8d | -21.26268 | -49.04079 | 2025-03-21 05:01:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 3d956a72-a63d-3ce3-a2e0-8f31cfc187e3 | -20.11459 | -46.77114 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01871312-895f-387e-b188-48817d6229bb | -20.92392 | -55.42021 | 2025-03-21 05:01:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e49c7ce-1538-329e-8f5a-8a6dea2ca10a | -20.92434 | -56.54192 | 2025-03-21 05:01:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 06574553-9822-3cfa-9c79-17ab58b4c345 | -20.20784 | -46.67528 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4604f01-6684-31f0-b878-3ae32ee21627 | -19.4353 | -54.78164 | 2025-03-21 05:01:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 20d12b4e-ac27-30cc-85c4-116c02fa2196 | -20.11941 | -46.78081 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7df2f897-fe3d-3da5-b171-92cec7385e14 | -20.05986 | -55.78298 | 2025-03-21 05:01:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| a00c3b84-9000-34d5-98ef-b542f56652ba | -20.11573 | -46.78092 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 75906f0e-e3d0-37a0-b93c-48437647428a | -20.20749 | -46.67919 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efbc3d83-bf19-3c48-9c74-30285741832c | -20.12176 | -46.77822 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 261d5374-c232-3959-874e-76955b98bd12 | -21.18429 | -56.4991 | 2025-03-21 05:01:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df0f2672-0683-36f6-bd0a-bf91db4d393d | -24.24471 | -50.74183 | 2025-03-21 05:01:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5ea02158-57d2-3ea8-babc-859be75ca0c8 | -20.21336 | -46.67847 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aea2042e-fb45-3bf5-a162-76bed2c6cad8 | -21.24136 | -56.46215 | 2025-03-21 05:01:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dcd14b57-e472-3191-bc87-3e348907e234 | -20.11649 | -46.77274 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6f7839c7-339d-3ed4-8f29-c573c709332e | -23.97499 | -53.38354 | 2025-03-21 05:01:00 | NOAA-21 | ALTO PIQUIRI | PARANÁ | Brasil | 4100707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ce97038f-752a-353d-aee5-bd6f5e0b6f68 | -20.12139 | -46.78218 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f6dba938-7482-3e69-8953-055fabfd1fe9 | -20.23067 | -46.60933 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3012d78b-05b2-365e-8643-c1f6f0a7b790 | -20.14229 | -50.73338 | 2025-03-21 05:01:00 | NOAA-21 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| abffc750-661b-371c-a347-4cacbce3e293 | -20.12667 | -46.78744 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4213b564-1ad8-3125-b72f-5db8a65d2a08 | -19.42833 | -54.78057 | 2025-03-21 05:01:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6dca488d-4c8a-3a7f-be7d-02ccfcc4bf60 | -20.13233 | -46.78866 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 240ede7a-b7d7-3f11-9f9c-3286ec0d442e | -20.11542 | -46.76275 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README5.md)
