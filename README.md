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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9aa1f980-2854-3e56-bc3a-08088eaa4fb2 | -21.2565 | -49.3517 | 2026-01-28 00:00:00 | GOES-19 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.6 |
| cbc657c3-c437-3e17-a221-48c827848cae | -29.6252 | -56.0349 | 2026-01-28 00:10:00 | GOES-19 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 177.4 |
| d1c8d5e8-4d3a-3188-a405-a99aa69e02ad | -9.8131 | -36.3883 | 2026-01-28 00:10:00 | GOES-19 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 82.7 |
| 9a9d8d4a-8589-367c-a2b7-0d0b133bd8c1 | -29.6024 | -56.0402 | 2026-01-28 00:10:00 | GOES-19 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 108.0 |
| 32cca1f3-c31c-3c1c-91ae-579965389c2d | -29.6245 | -56.0582 | 2026-01-28 00:10:00 | GOES-19 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 115.6 |
| 409e202a-b056-3c35-b09d-3466850b7665 | -29.61977 | -56.04595 | 2026-01-28 00:24:00 | TERRA_M-M | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 50.8 |
| ad896e93-7d22-329d-8e88-19cb428159c5 | -29.61244 | -56.04117 | 2026-01-28 00:24:00 | TERRA_M-M | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 63.4 |
| a0b96f9a-3db3-38f2-9d8e-b30370ba5842 | -26.69757 | -50.57322 | 2026-01-28 00:24:00 | TERRA_M-M | TIMBÓ GRANDE | SANTA CATARINA | Brasil | 4218251 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 758db4cf-4ada-352e-b3e2-d096c0806214 | -23.51302 | -47.33577 | 2026-01-28 00:24:00 | TERRA_M-M | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 67b9640c-7de8-3793-a218-a6f6e41122d8 | -22.84119 | -48.639 | 2026-01-28 00:24:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1d40f546-0414-3da1-ba46-216fb398f1c4 | -23.02912 | -50.90876 | 2026-01-28 00:24:00 | TERRA_M-M | RANCHO ALEGRE | PARANÁ | Brasil | 4121307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| a3e4de4a-532e-3552-b844-098fd613b726 | -23.02765 | -50.89611 | 2026-01-28 00:24:00 | TERRA_M-M | RANCHO ALEGRE | PARANÁ | Brasil | 4121307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 8ebbd738-72a2-323c-a802-28221b6ec979 | -22.84249 | -48.64894 | 2026-01-28 00:24:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 677c5c85-7aaf-387e-b00e-cc3c56983564 | -14.47409 | -46.9935 | 2026-01-28 00:26:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a85309ec-7e2a-314e-bc4d-4d669f9d17de | -14.46478 | -46.995 | 2026-01-28 00:26:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b108f9ec-962a-3482-9e1c-3dceab7b2188 | -13.48878 | -46.70862 | 2026-01-28 00:26:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| d1f20542-73c6-3146-955c-0d8230dfd1e0 | -13.49042 | -46.71937 | 2026-01-28 00:26:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 481659e9-7ac2-3dae-9c77-62e1c597b8b0 | -13.50791 | -46.70547 | 2026-01-28 00:26:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8ee7dc07-b1c3-312a-bf54-cd83e345874d | -13.49835 | -46.70705 | 2026-01-28 00:26:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 94e65703-5b4c-3892-a54a-6ad7c69857a9 | -17.82717 | -45.71047 | 2026-01-28 00:26:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 13ab0d08-837e-3f6b-bc0e-2fb24d1320ed | -13.50953 | -46.71622 | 2026-01-28 00:26:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 53a77dd5-a754-33ab-8ea6-637b00230b1b | -12.90256 | -49.21672 | 2026-01-28 00:26:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d1d202d3-9e89-3edb-b90b-aad9b6c65001 | -16.09365 | -45.17412 | 2026-01-28 00:26:00 | TERRA_M-M | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 14dc82e2-7ae9-3a86-90e1-c31b8c5dde95 | -12.89499 | -49.22704 | 2026-01-28 00:26:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 76f70f9a-7596-3a8f-b242-c3f9cd88d348 | -12.89374 | -49.21803 | 2026-01-28 00:26:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 0afefb0b-25ce-3b66-8dc3-95d217f7fab7 | -8.11343 | -48.02015 | 2026-01-28 00:28:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8f2621e1-43e9-34b5-958f-b54ae0dd2a65 | -10.77669 | -44.42212 | 2026-01-28 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| cfcd4d86-b279-33ca-a675-74e7f5787b16 | -10.10357 | -47.55278 | 2026-01-28 00:28:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d3375f2d-c8c0-3cb6-8f66-c4ae13ae8858 | -10.10879 | -47.55639 | 2026-01-28 00:28:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 57e3d4df-e590-3bc8-83d8-d7c0e3a36acd | -10.1602 | -36.3538 | 2026-01-28 00:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 77.9 |
| ef84328d-1081-3e2c-ae00-0c5e9d41d766 | -1.31368 | -53.19902 | 2026-01-28 00:32:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 86ab2c84-c8f8-37dd-bb83-7ee571b03bc4 | -1.31493 | -53.20816 | 2026-01-28 00:32:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a9c0188d-f41b-3712-aec7-8b22f8c3cd74 | -10.442 | -36.7319 | 2026-01-28 02:10:00 | GOES-19 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 91.2 |
| f9b7f735-6ad5-32b6-bf28-a225202e3c52 | -10.4415 | -36.7587 | 2026-01-28 02:10:00 | GOES-19 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 169.1 |
| fe9946e0-82e9-3b50-9574-8f6e09e460a3 | -10.19689 | -36.40335 | 2026-01-28 03:00:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 850d3fa5-06ab-3c6a-a8e3-5fe6c7aeb5fa | -10.1964 | -36.4097 | 2026-01-28 03:00:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 2886b632-1f9f-3d42-98a3-b38506992c86 | -10.19036 | -36.40843 | 2026-01-28 03:00:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| f5707a8b-3b69-3d7f-bee3-0c9da85fc767 | -10.70557 | -37.07499 | 2026-01-28 03:00:00 | NOAA-20 | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 64536a84-aefd-30f4-821d-cabdf8a80623 | -10.20725 | -36.41487 | 2026-01-28 03:00:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1059d7e8-3126-346b-b24d-444d919e1553 | -10.19126 | -36.40393 | 2026-01-28 03:00:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 3b7271dc-3d0b-326b-a951-75d3c4c1f276 | -10.19521 | -36.41208 | 2026-01-28 03:00:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 7629ae5e-40d8-375b-bfb1-cc92a52f34f7 | -10.70345 | -37.07099 | 2026-01-28 03:00:00 | NOAA-20 | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 3b5603d7-4443-3a15-be77-8ac3b94dbdd3 | -10.19603 | -36.40783 | 2026-01-28 03:00:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 88130d5e-abb9-3629-80a8-ff21e6b0bf4c | -10.20155 | -36.41541 | 2026-01-28 03:00:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 29e27bd2-45fd-3196-87a6-cbeada89eb98 | -10.70869 | -37.0772 | 2026-01-28 03:00:00 | NOAA-20 | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a33155cb-d15d-341a-8f15-14e274e1f04f | -10.19003 | -36.40633 | 2026-01-28 03:00:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 899bd2af-b962-3e2e-bea2-c26a16500083 | -10.19725 | -36.40544 | 2026-01-28 03:00:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 1fb16584-1259-324b-9a00-5f283286a63d | -10.70971 | -37.07216 | 2026-01-28 03:00:00 | NOAA-20 | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 6c5cbf6a-304c-3146-9dc4-10aebff17238 | -10.70654 | -37.07002 | 2026-01-28 03:00:00 | NOAA-20 | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 855fab12-b239-363d-9770-57ed0f52a6c0 | -4.28975 | -38.05864 | 2026-01-28 03:46:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d9326f3f-fccb-331a-a386-2ea449aa6f55 | -10.19356 | -36.40538 | 2026-01-28 03:49:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ba5416da-bb2b-378b-a48b-f48b60e2aaed | -10.21091 | -36.40434 | 2026-01-28 03:49:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 70a710f0-9a36-3b3f-8b5b-bd5fb991bbb3 | -10.20309 | -36.41059 | 2026-01-28 03:49:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| af4ed8af-eaaf-3b31-937c-a5d67c58abfd | -10.71486 | -37.59338 | 2026-01-28 03:49:00 | NOAA-21 | SÃO DOMINGOS | SERGIPE | Brasil | 2806800 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 67233fad-177a-3183-bd0d-44580d533f0c | -10.70457 | -37.06673 | 2026-01-28 03:49:00 | NOAA-21 | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| d47190ca-a828-3760-9f26-7eb143225c5c | -10.20028 | -36.40643 | 2026-01-28 03:49:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 032d5871-95af-3845-87c0-9d110ff11d20 | -11.14808 | -43.32098 | 2026-01-28 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 045a86a6-115f-386a-973f-33c89eea529b | -11.14336 | -43.32394 | 2026-01-28 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 410472fc-0482-3da9-a44b-77c2f2e4f6e8 | -9.31177 | -37.99166 | 2026-01-28 03:49:00 | NOAA-21 | PARICONHA | ALAGOAS | Brasil | 2706422 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e1e1bf22-b194-32b0-b2df-1653c599c987 | -10.70789 | -37.06726 | 2026-01-28 03:49:00 | NOAA-21 | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| adc28412-029b-3ba6-a008-165059931242 | -8.4601 | -45.13404 | 2026-01-28 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f33a54e-3e4c-3fca-aab1-6cc02adc939d | -10.71047 | -37.59983 | 2026-01-28 03:49:00 | NOAA-21 | SÃO DOMINGOS | SERGIPE | Brasil | 2806800 | 28 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 671d8bb9-0389-3d83-b3fa-e19a18e0a1a9 | -10.20083 | -36.4028 | 2026-01-28 03:49:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9686f21b-2649-352b-9279-f90bc6755895 | -10.70735 | -37.07079 | 2026-01-28 03:49:00 | NOAA-21 | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| eb2a8a10-9d0b-354f-b2fb-be77169f9346 | -10.94799 | -44.90746 | 2026-01-28 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78544b7d-520b-3950-a6c9-f10127792f28 | -11.14743 | -43.32466 | 2026-01-28 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 61f52b40-fafe-35b6-8eeb-0a3d5e2a221d | -10.7068 | -37.07433 | 2026-01-28 03:49:00 | NOAA-21 | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 29104a89-70db-3e9e-865f-6ee0d7edc6d7 | -10.19692 | -36.4059 | 2026-01-28 03:49:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ebb1643e-c424-3e98-b4d9-848d38acd015 | -9.62463 | -37.75355 | 2026-01-28 03:49:00 | NOAA-21 | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5a35fb04-7588-3194-9dcd-44b11e70ce82 | -10.71067 | -37.07132 | 2026-01-28 03:49:00 | NOAA-21 | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2f1c07c5-6ba8-3848-a86a-f987f87baa1f | -10.71101 | -37.59635 | 2026-01-28 03:49:00 | NOAA-21 | SÃO DOMINGOS | SERGIPE | Brasil | 2806800 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5eaf8522-1827-33e7-ad36-803b6a5f8842 | -10.12778 | -39.99261 | 2026-01-28 03:49:00 | NOAA-21 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 63fe845e-e35c-3e7f-aab5-5e064ae5b653 | -16.09348 | -45.17032 | 2026-01-28 03:51:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d48815f4-8e05-3d46-9571-693e3c8edc4c | -15.84903 | -43.50458 | 2026-01-28 03:51:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ca3db376-a064-3079-b322-fe49e74151ad | -15.85285 | -43.50531 | 2026-01-28 03:51:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d34b52b7-8410-35a9-a204-abdf22adc92e | -17.81043 | -39.70837 | 2026-01-28 03:51:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a71ef0b6-fc5c-3a4e-bc5c-54ba198459e5 | -16.09273 | -45.17436 | 2026-01-28 03:51:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a8d5531-2e4b-3bce-9e07-e85280af7547 | -13.49176 | -46.71219 | 2026-01-28 03:51:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4cc650d3-2bd8-3704-8b99-df839649c5ce | -17.811 | -39.70477 | 2026-01-28 03:51:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c7bfa144-dd98-3434-a135-ccfcc21471c6 | -18.85186 | -40.45853 | 2026-01-28 03:51:00 | NOAA-21 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| de025dbb-5a9c-363e-8834-784f6be26edd | -16.62455 | -45.61872 | 2026-01-28 03:51:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 764fb374-a15f-3278-9c18-feed689bdf7e | -17.87497 | -41.01887 | 2026-01-28 03:51:00 | NOAA-21 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 75034a3a-a698-382f-b507-963f5c3e0599 | -22.80004 | -49.33469 | 2026-01-28 03:53:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b86f32e1-84ab-36b7-8c47-b46b0bf38ba5 | -22.80128 | -49.32887 | 2026-01-28 03:53:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a5170f46-ace9-383c-870e-54ddac853373 | -22.80608 | -49.33013 | 2026-01-28 03:53:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 62c5cc0b-f37c-3f48-97f5-cf452be5f06f | -22.80484 | -49.33599 | 2026-01-28 03:53:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 162a9ccc-4398-3e41-802b-8a61f3597c16 | -23.59439 | -48.34282 | 2026-01-28 03:53:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71a3e957-644b-3435-bffa-c9ba28b07af8 | -20.3043 | -41.39276 | 2026-01-28 03:53:00 | NOAA-21 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d1d77297-dc45-35e4-adf9-82d49325b83f | -22.79646 | -49.32769 | 2026-01-28 03:53:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9f655179-2270-3e19-a8e7-9354959d9135 | -22.79165 | -49.32649 | 2026-01-28 03:53:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdecc838-f4af-3157-bd33-6af023f20e81 | -29.77519 | -51.17908 | 2026-01-28 03:55:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| be3b0c2f-de8d-3fc3-a0da-56915a58e34d | -27.21208 | -48.67861 | 2026-01-28 03:55:00 | NOAA-21 | TIJUCAS | SANTA CATARINA | Brasil | 4218004 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| dcaf087a-57d6-3515-9ef4-352263f29240 | -27.56304 | -48.66134 | 2026-01-28 03:55:00 | NOAA-21 | SÃO JOSÉ | SANTA CATARINA | Brasil | 4216602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 35610027-d367-3b3c-b56d-29f46b9214f2 | -1.31452 | -53.20629 | 2026-01-28 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6859fe6d-e74c-3973-8a2f-2a4d3f307777 | -1.30839 | -53.20541 | 2026-01-28 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0cd33365-b454-3681-af4d-aed196091048 | -1.30916 | -53.20073 | 2026-01-28 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 558aaf25-c1e1-3970-afbc-07c6c46b2b0d | -10.70559 | -37.06879 | 2026-01-28 04:21:00 | NPP-375D | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e2ccd395-9afe-3cad-a1f7-d2e75b15a6f5 | -10.89526 | -44.31754 | 2026-01-28 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 205e61aa-6952-3e68-b5e0-a538e911f36a | -10.95109 | -44.90584 | 2026-01-28 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f374dc2c-804b-3520-813f-daf08e2feb15 | -8.45978 | -45.13353 | 2026-01-28 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README2.md)
