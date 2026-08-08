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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b0daba9-03dd-3c5d-8372-ee201123a8b8 | -14.42382 | -45.65874 | 2026-08-08 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50c8e3ba-d4c2-3764-806d-8f0a0b572923 | -12.13875 | -48.26592 | 2026-08-08 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39b24a75-416d-38bb-94da-f73c7f2fc122 | -15.70327 | -54.85728 | 2026-08-08 04:46:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 2440785f-950d-37aa-bb84-b0f2a3b1a2c0 | -11.7306 | -50.13355 | 2026-08-08 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8d5c3780-39d7-3f45-8eab-8eca3dd35057 | -14.32566 | -54.94339 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39b0c782-bc97-3cf1-932a-32bdb8e08017 | -8.1622 | -55.41467 | 2026-08-08 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c293b06-a763-33e9-8ca4-a8d61988776d | -12.86033 | -52.81867 | 2026-08-08 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53d97145-cc0d-346b-8f42-1714f6b09f26 | -11.15685 | -54.84956 | 2026-08-08 04:46:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4658f742-20f5-3229-a90f-49b1e478ed98 | -15.15136 | -52.7406 | 2026-08-08 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3119ab18-424f-31ff-bfe0-2b92f09a273b | -8.14792 | -55.42372 | 2026-08-08 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7639279c-9f9b-349a-a299-7e8237ea3efa | -14.15695 | -54.00603 | 2026-08-08 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c480710f-150d-3677-8fce-b64be4ce9cbe | -15.70188 | -54.84393 | 2026-08-08 04:46:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49c5ae25-189e-3438-aa98-6bbb17b9d97e | -15.1486 | -52.73642 | 2026-08-08 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a4eeb34-6970-3416-974e-8fa18bcd6fe5 | -15.70591 | -42.18171 | 2026-08-08 04:46:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a31dbca1-85e4-32f3-a22f-ba77bd109dd6 | -14.36891 | -54.91081 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 546acb13-fdcb-35e0-aa53-0b888b797060 | -7.55174 | -61.15537 | 2026-08-08 04:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1e4d112-11b3-3886-ac3d-9daf9dc06351 | -11.79451 | -40.92588 | 2026-08-08 04:46:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4841032c-91e3-39bc-b2a8-6d4f8014def0 | -16.68903 | -49.38715 | 2026-08-08 04:46:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5dd909fd-e5af-34e6-bf11-cde63d3dcd38 | -14.16045 | -54.00666 | 2026-08-08 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 40addff3-b54b-31b3-bd12-bdef80b2313b | -14.92576 | -48.24766 | 2026-08-08 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7bea2770-24e2-3f74-84ed-078221fa2ee4 | -14.9391 | -48.25826 | 2026-08-08 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 624a6330-0bdf-3ba4-8ee7-f2203e23ccd6 | -12.53197 | -46.98573 | 2026-08-08 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 962a188a-cca0-35d2-8b2c-78fa7d8ad316 | -14.93304 | -48.24862 | 2026-08-08 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| be3a699b-4a19-3a0c-a482-a185d14e023c | -14.37003 | -54.96978 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1e2dcc51-4afd-31c8-ab41-144f1abd0bc0 | -11.15104 | -45.93625 | 2026-08-08 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 168d48c4-7c48-304e-8353-b2e0029b94d4 | -14.93088 | -48.2587 | 2026-08-08 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b05a0712-f77c-3095-a572-aabd7eead47e | -11.03866 | -44.28126 | 2026-08-08 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9fc9e776-c2a5-3743-b579-11bbeab9cf67 | -15.71129 | -42.18274 | 2026-08-08 04:46:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d907410-741e-334c-877c-38210777b047 | -11.68341 | -50.1334 | 2026-08-08 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72706bb6-b32d-30ab-8051-541e97b6d6bc | -14.16112 | -54.00272 | 2026-08-08 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3578cf2d-8d25-3b24-84ed-08ce112af744 | -11.72673 | -50.13656 | 2026-08-08 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bfd09541-a69f-3376-90ab-5cf46c1b193f | -13.92909 | -47.36558 | 2026-08-08 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9153e167-01be-318f-924d-f2c41d62f167 | -8.14445 | -55.41932 | 2026-08-08 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8db8ed6f-2b54-3725-bed6-6a248d2e4a17 | -11.19341 | -54.8415 | 2026-08-08 04:46:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a3cba4e8-5919-38fa-af3a-5e325ede5d01 | -14.93241 | -48.25311 | 2026-08-08 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88a7a648-a88a-3e28-b126-cdebb37b583c | -15.704 | -54.85306 | 2026-08-08 04:46:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 4c6f7c10-4257-3351-b4b7-4aa1c215e1c1 | -11.30734 | -44.85572 | 2026-08-08 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c43974e6-3911-3d32-9a66-c1818a4a7077 | -13.3726 | -41.35172 | 2026-08-08 04:46:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fdc6b3c4-26b8-35f7-9d67-b700de461f6d | -14.41961 | -45.65815 | 2026-08-08 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69664a4d-2bc0-324f-a9c0-4b231b1e6d62 | -11.68064 | -50.12932 | 2026-08-08 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 747e2c66-0ad7-3756-bcad-76c8f569e8b3 | -10.52628 | -46.62111 | 2026-08-08 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2f174ef-b974-341a-b044-60c0a45881c7 | -14.4233 | -45.66275 | 2026-08-08 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09418ef6-f687-38f2-8149-75d6fd09133e | -13.83443 | -53.74097 | 2026-08-08 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2bc3abb-ac3f-3e8d-9dc3-184703c9cdcc | -14.31277 | -54.9955 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1354e9b2-6e38-3ae1-8d19-ac7342aa2f79 | -15.10228 | -52.73211 | 2026-08-08 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63930206-f0e8-3854-a03a-1e75a941cdc7 | -13.82428 | -53.69475 | 2026-08-08 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02365c19-ba1c-38c2-bbab-5801e3b66319 | -11.70945 | -50.1412 | 2026-08-08 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88d55a49-66c6-3dd9-a257-435c756eb3fd | -16.40178 | -49.93451 | 2026-08-08 04:46:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4675f506-eda7-3c3c-8d5a-89caa1d6d536 | -14.93281 | -48.24549 | 2026-08-08 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| be9a96fa-1447-3f25-a6d4-40eb2d2106f1 | -20.17767 | -43.69413 | 2026-08-08 04:46:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4c6af202-e166-3519-8695-4d2644892012 | -14.32086 | -54.99244 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4bf9519b-4807-3c70-ae77-021cb0c88295 | -14.42279 | -45.66325 | 2026-08-08 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 715c9094-5048-32e8-8574-3d31927ef584 | -10.2653 | -45.81135 | 2026-08-08 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b0c6ce0-d7ac-3645-8224-32b09c2d2956 | -12.55951 | -46.92749 | 2026-08-08 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 81ff6eec-a747-3fd7-9b9f-7e1b2c53c296 | -20.27039 | -41.78508 | 2026-08-08 04:46:00 | NOAA-20 | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7ece1594-7d70-34cc-af5d-a1ca8142b534 | -11.24452 | -54.02045 | 2026-08-08 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3ba09105-704f-3202-acbf-f514665a2ce0 | -11.03485 | -44.27633 | 2026-08-08 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 6b8c18b5-3b93-32d8-9c3f-f0ce5715f452 | -14.37368 | -54.97046 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 13b31bdd-fe66-3fe7-8d81-52d0bfa1a6c8 | -15.16139 | -52.74228 | 2026-08-08 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 763b2bca-075c-3304-b247-1d709ae197f3 | -15.38091 | -53.79065 | 2026-08-08 04:46:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba07c9a2-b55c-35d6-ac60-0eea1aeb26a0 | -11.03545 | -44.27199 | 2026-08-08 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a2511abf-6c69-3a05-b58c-4e4f3ea694dc | -15.16079 | -52.74595 | 2026-08-08 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b0cc512b-15fd-377b-88ec-248a5b655727 | -14.16461 | -54.00336 | 2026-08-08 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 6f5a28df-f02f-3180-939a-5e617cf9453a | -15.81873 | -48.09624 | 2026-08-08 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fde3d1e3-328d-3e8e-913f-0458fd511d5a | -14.34508 | -54.98332 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 773e0305-1066-3630-bea1-4fc7e477c854 | -14.32795 | -54.93024 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 480d67a8-07ff-3631-ab7c-b0ef0e772cee | -8.14857 | -55.42001 | 2026-08-08 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11a8dc12-729c-3e5b-ac28-d232e3fa87c0 | -15.1553 | -52.73751 | 2026-08-08 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| be20abbc-2b3f-3ed4-af29-ad864d3b6f9e | -14.34873 | -54.98399 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 43a07a33-902f-3a6c-a50d-231a61d0bed1 | -11.61045 | -54.65179 | 2026-08-08 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec7d9149-f28e-36a0-82ba-bcf9e79ed951 | -14.92816 | -48.25697 | 2026-08-08 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| a7d576e8-b071-36f1-b265-0315e863f295 | -15.11015 | -52.72597 | 2026-08-08 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 952695cd-37d9-3e52-ac45-758d386658e6 | -12.6104 | -52.45881 | 2026-08-08 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e8a16b05-9352-328f-b700-e1c010ee276e | -15.07903 | -52.7695 | 2026-08-08 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 80fcaa2e-6ce9-3aa2-9ca4-cbe530117ee9 | -14.32606 | -54.98423 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 48a4c68a-616f-37af-b1dc-febd12c47aa4 | -16.68956 | -49.408 | 2026-08-08 04:46:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d924af2-1a1b-33d8-a590-db2cc88ae763 | -12.53724 | -46.94823 | 2026-08-08 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b8f77794-9164-32cb-a43c-3fe947700c71 | -14.41437 | -45.66206 | 2026-08-08 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e48d9441-b127-3e5d-a2de-19a0817e72c2 | -8.16156 | -55.41836 | 2026-08-08 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a2f2f0f-b67f-3911-ac89-e8078bdfb9f3 | -14.00839 | -53.83102 | 2026-08-08 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f795d56-af98-3715-b717-fb0ab58c186e | -11.30211 | -44.85843 | 2026-08-08 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c701318-4a53-3846-be72-9f5b8e572a94 | -13.83037 | -53.67966 | 2026-08-08 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0aab9b12-71de-3bba-9469-a8e54e745b22 | -8.49818 | -54.77311 | 2026-08-08 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77bc4650-60c9-3a52-97b1-36d3064b07c5 | -11.198 | -54.8375 | 2026-08-08 04:46:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3049b52d-57ab-34b7-bc7e-1609ce1ba8cc | -14.32489 | -54.94778 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b70e28c9-f5ab-363c-99b8-51bab9250d46 | -15.82041 | -48.09363 | 2026-08-08 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17692876-bdec-3a33-8faf-ec411e67c67b | -10.28635 | -49.94719 | 2026-08-08 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ce4e31d-6c8f-35c7-aed7-db78f2acf89a | -14.41909 | -45.66216 | 2026-08-08 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63118d6b-29af-351d-9f66-ba0a940daa48 | -11.1926 | -54.84616 | 2026-08-08 04:46:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05813ccd-7f6a-301b-a6af-77e89015e705 | -15.97186 | -48.07016 | 2026-08-08 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e98ed6ec-5bf6-30d8-8ec7-3fe99de4d2a2 | -13.83685 | -53.70506 | 2026-08-08 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 702af1d6-aab3-3db0-8f74-b0deff1c3768 | -12.53213 | -46.95706 | 2026-08-08 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5502fd86-39ea-39bf-ac0c-83be11652657 | -14.93061 | -48.26587 | 2026-08-08 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dfde0c10-7973-373b-a119-cc1b2b59256c | -17.30729 | -42.66138 | 2026-08-08 04:46:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f83e1ef7-f9ea-3b11-b9de-f6ace15baf43 | -12.61317 | -52.46304 | 2026-08-08 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 81eca30b-a637-3f8c-9fda-d26ec4becd10 | -14.35737 | -54.89072 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d2ce48d-a7de-3509-b59e-459176a40b92 | -14.41803 | -45.66664 | 2026-08-08 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98b7aea2-ca11-318f-bdfd-214502ec5335 | -13.42614 | -57.04197 | 2026-08-08 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a07ca1a-ddc2-3486-a315-4b69aa625d77 | -17.30536 | -42.67884 | 2026-08-08 04:46:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 869f75b3-7f8a-3034-8ee2-31267db9ec27 | -11.30252 | -44.85915 | 2026-08-08 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README19.md)
