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
| d0323893-7f49-37bb-b778-fa8cde22213c | -8.71682 | -48.01535 | 2025-06-23 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 882d5339-6977-393d-9a7e-161fe6282bb8 | -9.41625 | -48.42029 | 2025-06-23 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 912bbcc1-4cfb-3454-bddb-33d061974b41 | -8.38029 | -47.44098 | 2025-06-23 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 87bbd69d-5086-3eef-afb2-e98afa3ae64b | -8.11871 | -43.14556 | 2025-06-23 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f0105e97-1f5f-3778-bba4-5b01677ced46 | -8.11105 | -43.14429 | 2025-06-23 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 166022a9-811b-354b-b2f2-35c6c869be0c | -8.11026 | -43.14906 | 2025-06-23 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 5432f0bb-29ce-386a-a8c0-9499c0ca613f | -11.58495 | -44.65481 | 2025-06-23 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7dbce584-b876-325e-829d-0ee355667982 | -7.47054 | -45.56355 | 2025-06-23 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 41d026d3-46bf-35b0-af79-054f7aed39c1 | -17.67312 | -46.76115 | 2025-06-23 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a633f510-8607-3070-a95f-aa6f76abfe54 | -13.27616 | -46.82136 | 2025-06-23 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67af2384-e580-3b7d-a7e8-1131eef4d66e | -16.68218 | -43.88367 | 2025-06-23 03:57:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a32e5703-e1ff-3c0f-8545-d462e37e44f9 | -19.83369 | -40.11256 | 2025-06-23 03:57:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 58e6eea2-864a-314a-b565-7353be49bac9 | -20.33729 | -41.18644 | 2025-06-23 03:57:00 | NOAA-21 | VENDA NOVA DO IMIGRANTE | ESPÍRITO SANTO | Brasil | 3205069 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 46fefff9-89d2-310a-9e17-87edcafb593a | -21.62782 | -43.46601 | 2025-06-23 03:57:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2c116775-bc1b-3c77-9808-b352cc6bc966 | -19.5138 | -44.27593 | 2025-06-23 03:57:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff333268-bf04-3ec6-a43b-868ee229f54f | -19.23641 | -46.45809 | 2025-06-23 03:57:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10f266aa-979c-35e9-9275-4b9692c29d01 | -17.3918 | -42.63338 | 2025-06-23 03:57:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 0bab6f77-1f36-35d1-86b7-ad4c0b39bf43 | -13.2414 | -49.83371 | 2025-06-23 03:57:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2fd6e36a-6dcb-3bf5-a6fc-dd880bf313ee | -21.66434 | -41.94846 | 2025-06-23 03:57:00 | NOAA-21 | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 98df0a41-ff26-3ad0-99c9-57aa3779afe3 | -19.48938 | -44.14411 | 2025-06-23 03:57:00 | NOAA-21 | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4655a31c-fb9a-3316-9d83-824a45caa414 | -19.71887 | -40.35267 | 2025-06-23 03:57:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ea2c8d10-1f59-3820-aff1-e159235b755e | -17.67687 | -42.74125 | 2025-06-23 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e98e709-3e97-3776-a6be-8995855a0f89 | -19.23503 | -46.46082 | 2025-06-23 03:57:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8b8ed7dd-8491-38d8-bf28-8ea18ffc161b | -19.23547 | -46.46326 | 2025-06-23 03:57:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| af38d76f-875c-3db2-87a3-c6eabbd28985 | -19.51446 | -45.31774 | 2025-06-23 03:57:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0ce1fb33-1745-3bff-971c-c9e5ffe8b93c | -19.51609 | -45.30856 | 2025-06-23 03:57:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68235abc-91c9-38e6-89ff-c62451e708d0 | -20.02891 | -48.19679 | 2025-06-23 03:57:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 31dfb6f6-a904-3563-a12a-e982d8bdc7e3 | -17.5005 | -43.94718 | 2025-06-23 03:57:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98efd505-e5c6-3423-a49c-7b2703f1a35f | -17.50404 | -43.94782 | 2025-06-23 03:57:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e8698ff-09ef-3225-9903-976d25a8fc96 | -17.39604 | -42.63741 | 2025-06-23 03:57:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9715cd5-06ef-3883-ae98-50f3ba01e061 | -17.75006 | -42.89481 | 2025-06-23 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d925ec6-a63c-32c7-80f1-8deaed1e0f2b | -17.39456 | -42.63774 | 2025-06-23 03:57:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2f0cf8e5-059e-3150-bf0f-2ad0f8c69436 | -20.73215 | -41.90651 | 2025-06-23 03:57:00 | NOAA-21 | CAIANA | MINAS GERAIS | Brasil | 3110103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 86c6e95c-4dd0-3d0c-8ca8-f83b17f167db | -21.66764 | -41.94905 | 2025-06-23 03:57:00 | NOAA-21 | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e3c9e292-fe5a-3e6f-ae4e-37a5a4584743 | -17.09586 | -43.80452 | 2025-06-23 03:57:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 368237db-e81c-3c84-bffb-fa40277684bc | -20.76491 | -46.76911 | 2025-06-23 03:57:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4fe2f67e-bb7c-30c5-ad2c-4a5ace9f47cb | -14.01922 | -43.84021 | 2025-06-23 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9c29727-b983-3d56-959e-0b484b92e875 | -17.39303 | -42.62583 | 2025-06-23 03:57:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 21d96472-62b9-3d0e-8a2d-35ca0b488a99 | -17.61966 | -44.48683 | 2025-06-23 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36ccd80a-aeff-3fbe-b7f2-0e8dfa7c0b2b | -18.14716 | -47.80386 | 2025-06-23 03:57:00 | NOAA-21 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2eeb6a4d-d466-39e3-95e0-731e125a5b9c | -19.4556 | -45.30646 | 2025-06-23 03:57:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2c30186-c714-310a-a4c7-2cbaced8b44b | -20.02978 | -48.19236 | 2025-06-23 03:57:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| cb90fd96-a774-36fc-8519-5538c4f27e26 | -16.38892 | -41.16309 | 2025-06-23 03:57:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3c97b385-f3c9-3324-a740-f78690cc4cba | -19.83821 | -40.08211 | 2025-06-23 03:57:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b618b037-8d8f-3852-b703-ccf40dc57bbd | -16.98233 | -50.24717 | 2025-06-23 03:57:00 | NOAA-21 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2ffb0f33-3d4e-3626-90ff-efd4874fd629 | -16.98752 | -50.24837 | 2025-06-23 03:57:00 | NOAA-21 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 070abbb6-1dc6-36d1-bdc4-2a2a3f55ea0d | -20.02547 | -48.19142 | 2025-06-23 03:57:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2e151c1c-8ef9-3145-8061-01c409b1caaf | -19.64177 | -45.19419 | 2025-06-23 03:57:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e7dce9d-4940-382e-b7f8-b90987384dc2 | -20.03064 | -48.18797 | 2025-06-23 03:57:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d59814cd-3db2-37b6-b4b6-6516e4d3a30f | -17.5041 | -43.94906 | 2025-06-23 03:57:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 714e7313-5c08-36be-bd99-c18fa4a8f07b | -20.37767 | -45.60511 | 2025-06-23 03:57:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e32afc24-5dda-3a5b-b4c7-8b77db51ad72 | -13.24457 | -49.84024 | 2025-06-23 03:57:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b7f21e8-bf76-33a4-b550-1ad057cf4751 | -17.39667 | -42.63364 | 2025-06-23 03:57:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 26471a02-63b2-3ce1-b000-5123f0f73574 | -19.43776 | -44.33908 | 2025-06-23 03:57:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54577d63-b614-3f93-b3d5-c88f7d23b6fd | -20.31403 | -45.58451 | 2025-06-23 03:57:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2dc9f21-e17f-393d-a9e8-0646a5f99849 | -13.24527 | -49.83661 | 2025-06-23 03:57:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a96c0c55-a692-3e45-ab1b-dfda5ff857b0 | -19.51896 | -45.31382 | 2025-06-23 03:57:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71906990-c342-390d-8d3e-17bfec333561 | -16.0867 | -41.98223 | 2025-06-23 03:57:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d6e20776-7b8e-3527-a767-67e37ad575ed | -12.30642 | -53.26831 | 2025-06-23 03:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 561373b5-7afb-3287-8aa3-011870f37e6c | -17.5033 | -43.95204 | 2025-06-23 03:57:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12401cff-bd65-3d58-8aa8-d0c745233545 | -13.27166 | -46.82076 | 2025-06-23 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 56dc55a3-a919-3b90-87c8-eec76a28c3a7 | -13.24068 | -49.8373 | 2025-06-23 03:57:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 9882d8ef-02c4-364e-a318-6db9f9469808 | -18.0409 | -39.92555 | 2025-06-23 03:57:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f84cdb8a-858f-3e20-9b64-801af831380a | -13.7601 | -47.74521 | 2025-06-23 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4efd0922-c7d9-319b-a818-22b0018a5ec0 | -17.86043 | -41.34697 | 2025-06-23 03:57:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dd60df25-5d41-353c-98d9-ffbabc9b1de2 | -21.62719 | -43.46983 | 2025-06-23 03:57:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 19136892-eea0-3549-9af6-0838cfa42e4b | -17.39517 | -42.63397 | 2025-06-23 03:57:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 97ed74a3-1ee6-3b82-9f26-6a03611b34bf | -17.39792 | -42.6261 | 2025-06-23 03:57:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f5335d11-1b5f-3904-bae5-21178e331b47 | -19.51528 | -45.31313 | 2025-06-23 03:57:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 660ed1d9-7729-3796-b604-a78a9c2c8c67 | -19.5116 | -45.31245 | 2025-06-23 03:57:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3d483325-dfe7-306d-9d0c-870ae38aabca | -19.23898 | -46.46152 | 2025-06-23 03:57:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67a70120-68bd-3e8f-91ab-ca4974948213 | -13.23985 | -49.83542 | 2025-06-23 03:57:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 305cfd79-6f59-3ef6-97e1-1a8f94886ded | -13.23915 | -49.83904 | 2025-06-23 03:57:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0e12544c-b056-3452-8db7-958059219dca | -17.39241 | -42.6296 | 2025-06-23 03:57:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 23.2 |
| b3659a7a-34a0-3131-ba42-ddf31174b428 | -17.50057 | -43.94841 | 2025-06-23 03:57:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9226ed42-cdfe-3bac-930c-043b25bae16a | -20.02459 | -48.19589 | 2025-06-23 03:57:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| faa6af67-a6ca-3057-bd4a-1f9c21052eda | -17.38748 | -42.65981 | 2025-06-23 03:57:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f1637dd-cf21-3217-8d1a-94404873e93e | -15.57041 | -47.85471 | 2025-06-23 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a8012da-26e5-3b46-a656-5fd629e3e97e | -13.83171 | -44.45745 | 2025-06-23 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4c2b6bc8-b863-3d99-8b33-3fa876421032 | -17.3964 | -42.62643 | 2025-06-23 03:57:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b3b53c1f-dd59-37ea-9cea-190a2e198d0b | -21.86129 | -42.89473 | 2025-06-23 04:00:00 | NOAA-21 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 929b01ca-8ddc-30d2-bcf9-1d6adff9d4d7 | -20.7085 | -50.06876 | 2025-06-23 04:00:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| a329cc47-6f12-30f6-ae09-1363416c6fbf | -23.33799 | -46.7725 | 2025-06-23 04:00:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 17695aa4-7bb9-3506-bf28-b24947839abc | -23.04567 | -49.89425 | 2025-06-23 04:00:00 | NOAA-21 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7a64a584-9e6c-3920-ae93-8b6e8c87298c | -23.59297 | -47.43632 | 2025-06-23 04:00:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1bddf1ac-28db-3795-90b5-cddf146c2f37 | -23.40564 | -46.55447 | 2025-06-23 04:00:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3e153da4-6822-3843-aadc-90c8a649ad86 | -19.69502 | -54.61301 | 2025-06-23 04:00:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0701e96a-83cd-339b-bb5d-471432f720e2 | -22.67801 | -42.85522 | 2025-06-23 04:00:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 22751ed1-8504-3bfd-9e53-238bf59b988e | -23.04419 | -43.63958 | 2025-06-23 04:00:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 205f0cb8-070f-30d2-af10-4b0d03916734 | -23.33727 | -46.77515 | 2025-06-23 04:00:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e196ae58-29dc-3240-8809-5f142af7d2b1 | -22.25538 | -50.03937 | 2025-06-23 04:00:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 93796d5a-2f68-3fbc-a8b0-6ea7f51bed9d | -22.25815 | -50.03829 | 2025-06-23 04:00:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 995f582c-9c0e-3915-a6f9-731d0ac56673 | -20.99865 | -51.79434 | 2025-06-23 04:00:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5cdf10ad-64c1-3e3d-93a2-e4f58690e667 | -21.86189 | -42.891 | 2025-06-23 04:00:00 | NOAA-21 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cd7b6253-9529-3589-93a5-8fbe4121029b | -22.25243 | -50.04238 | 2025-06-23 04:00:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7c49baac-6f45-338f-b879-5a54ddfb3c39 | -23.33816 | -46.77028 | 2025-06-23 04:00:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0c69bf4c-7b71-329d-841d-e01b020dd246 | -21.39416 | -45.5078 | 2025-06-23 04:00:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4a8cf053-12f9-3d1d-bedf-33f86f0c6665 | -21.39498 | -45.50323 | 2025-06-23 04:00:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a010860d-4eb2-3178-bd94-ea3c57484b70 | -19.69647 | -54.60931 | 2025-06-23 04:00:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 35984d8f-3af9-3901-8090-0c2fca13917b | -19.69518 | -54.6147 | 2025-06-23 04:00:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README5.md)
