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
| 487f75ed-b2b5-3a9f-9ec6-d38fd4c5b5ed | -2.69495 | -45.10352 | 2025-11-22 03:53:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| d4ac23fa-7220-381b-863a-1d8ff73fe05b | -6.2425 | -44.65426 | 2025-11-22 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f370a71a-e0cd-3c3d-8cff-dd227ad1c085 | -7.31447 | -35.13401 | 2025-11-22 03:53:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f839343c-a99c-3c82-ae8b-7d0414e60e72 | -3.1723 | -48.61985 | 2025-11-22 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15d4c76d-dd5c-3310-a55e-c30366165ea4 | -4.04105 | -42.51485 | 2025-11-22 03:53:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 14bf1f50-a29c-39f1-b62c-449fb0336eb8 | -6.68232 | -39.00119 | 2025-11-22 03:53:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 42a18242-2594-3e87-9f5e-be31438935ea | -3.45896 | -40.81797 | 2025-11-22 03:53:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b4e196b4-87b7-3348-a889-a1f7ee7f0daf | -3.83724 | -45.35196 | 2025-11-22 03:53:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4298dc6d-15f5-3169-97ec-5119109c2ffc | -2.92573 | -48.24411 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 9370fa32-7cc7-3f5d-8f45-a6dfc77e0765 | -2.92197 | -48.23033 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 7c24f21a-1ae8-3dec-8514-5829d59fd4d7 | -2.93232 | -48.24083 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62872b27-a5a8-30f6-a9aa-b51c26d06673 | -3.85754 | -41.57199 | 2025-11-22 03:53:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b56b5924-766d-3d5f-be9f-29b7ad6246bf | -5.86874 | -45.28592 | 2025-11-22 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a1a1eca-cdac-3f91-b6c2-22e4638327a1 | -4.14585 | -43.69528 | 2025-11-22 03:53:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| dfd0dbf0-b0c9-396c-acd6-57543a675f91 | -4.14094 | -43.69855 | 2025-11-22 03:53:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd72c0a2-5fbf-3a99-9a98-8324245c64b0 | -2.90948 | -48.2327 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cbca35b3-307f-3a81-8994-5d8406d7b137 | -5.57007 | -39.83651 | 2025-11-22 03:53:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| da112254-abdd-392c-9b1a-7297a13d9850 | -5.38403 | -46.76445 | 2025-11-22 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 928e23f5-6a98-3298-80f7-698a5e4726f6 | -4.16741 | -43.67043 | 2025-11-22 03:53:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ffff553f-6962-316e-8343-25ffd05a7674 | -4.15074 | -43.69209 | 2025-11-22 03:53:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0ca1e70d-97cf-3ef6-92d9-ecd7fdd63081 | -3.93314 | -39.21397 | 2025-11-22 03:53:00 | NOAA-20 | APUIARÉS | CEARÁ | Brasil | 2300903 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4a8b7db6-5d8f-3361-a0e8-8318877f7a0e | -4.16252 | -43.67368 | 2025-11-22 03:53:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b9b752e4-12ea-313a-9996-31aa2cc5696d | -2.58655 | -45.22268 | 2025-11-22 03:53:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 49406949-bc1b-3661-93fc-732ff19b53e6 | -2.91955 | -48.23453 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 72a1938a-7c69-3382-872e-4de8c40a08f3 | -3.17547 | -48.61482 | 2025-11-22 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b04aca1-a7b6-3104-93bd-b14d9472a70d | -6.30969 | -39.59352 | 2025-11-22 03:53:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 39f998c9-e050-36db-9407-1f745df0340a | -2.91677 | -48.22524 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 363a6cba-799b-347b-90b7-bb050564543c | -3.27061 | -42.20983 | 2025-11-22 03:53:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d96149a1-92d9-37ba-8c7e-0c2d88e70d77 | -4.16318 | -43.66973 | 2025-11-22 03:53:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c765083b-2645-3c70-b93e-840d1a6e5098 | -2.92715 | -48.23552 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| d2dcdbf0-2211-3a60-90be-648e1354f50d | -3.17468 | -48.61932 | 2025-11-22 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ee2082a-bedb-385e-b285-ffe0fe451a53 | -6.26428 | -39.2353 | 2025-11-22 03:53:00 | NOAA-20 | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4ec0e9be-e04f-3d17-9e81-1cd58f5f2727 | -6.75199 | -35.09725 | 2025-11-22 03:53:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d610136c-ea9a-3fa3-8ca3-97db41c3f460 | -7.31513 | -35.12972 | 2025-11-22 03:53:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| be94fb93-1adc-35f4-85b2-24f8bc8e50fb | -6.6769 | -39.50302 | 2025-11-22 03:53:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8744f368-dc15-30df-a4f4-d66becd77d66 | -2.91607 | -48.22945 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a9db039b-e06a-35a7-8c0b-1cb8b224d0c8 | -4.33155 | -40.18817 | 2025-11-22 03:53:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2d63b461-1b1f-3119-89fb-28030faadb51 | -5.64833 | -35.8368 | 2025-11-22 03:53:00 | NOAA-20 | BENTO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2401602 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cf1ecba1-db69-32e5-b78e-27e5b26d6d1e | -6.29218 | -37.87985 | 2025-11-22 03:53:00 | NOAA-20 | JOÃO DIAS | RIO GRANDE DO NORTE | Brasil | 2405900 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2c8bc868-9393-3839-b77d-14facd4b9620 | -6.66853 | -38.91716 | 2025-11-22 03:53:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 23b4401f-60e2-3668-a032-a098bb4cb87f | -3.26982 | -42.21479 | 2025-11-22 03:53:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ebc2a5f5-6e80-3a46-af98-c2d8a428275b | -3.1738 | -48.61085 | 2025-11-22 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 34b694fe-97dc-3975-be46-4c78439e647c | -4.14942 | -43.70002 | 2025-11-22 03:53:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 05dc3294-a4bf-36ce-8787-77aa5ae96d42 | -2.92856 | -48.22699 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 88015237-e7f6-32be-ad39-0250e5c35437 | -2.91538 | -48.23361 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 28274102-872c-3cca-aa95-58c16d2fd8ec | -4.66086 | -42.60873 | 2025-11-22 03:53:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e460ecfd-bd21-351f-84d4-94e77a4dd298 | -4.14716 | -43.68743 | 2025-11-22 03:53:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 17ef6410-f38d-3622-ac80-ce1716b9450c | -2.92691 | -48.22697 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 0f8a80e4-0481-36a5-9167-54b1ecdc09b8 | -4.02801 | -42.4716 | 2025-11-22 03:53:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a45e99b8-f770-326d-8511-3d3217aa287b | -5.28345 | -40.73819 | 2025-11-22 03:53:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 190e0701-6608-3e31-a850-e42c5a604713 | -5.42997 | -40.66116 | 2025-11-22 03:53:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cfe40368-3485-3672-956f-7343749c9764 | -2.92324 | -48.24823 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb125271-2c17-3ff9-a47c-96cb3eb115b0 | -4.03154 | -42.52363 | 2025-11-22 03:53:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| a92c6565-245f-3a34-acec-4c43fbb237ea | -3.86126 | -41.5726 | 2025-11-22 03:53:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ec7915bb-9e54-3950-9e46-b28bb241723e | -6.85776 | -40.16083 | 2025-11-22 03:53:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c5d2d810-19be-345a-9b89-a155955d31df | -5.24575 | -35.60784 | 2025-11-22 03:53:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c1b09a4a-e3cc-34fd-b93b-25e633d2d3d2 | -5.49341 | -39.08407 | 2025-11-22 03:53:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f2d4ffc3-1bd0-3165-b0fb-63dce9c5977d | -6.17403 | -44.55198 | 2025-11-22 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 289aebd0-4b3d-3ba0-a029-d1d7444883f8 | -3.12675 | -44.37617 | 2025-11-22 03:53:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 350577b4-a6b9-3f09-b812-c0aa1228f686 | -3.69615 | -38.86785 | 2025-11-22 03:53:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3f4a1c7b-67f4-3f87-88e8-48187059927e | -2.92471 | -48.23972 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| c3e87081-dd69-3e0b-8bb7-5636c5246c9f | -2.91468 | -48.2378 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9616402-406b-3227-9073-804d0b2e7d8d | -3.24186 | -44.3324 | 2025-11-22 03:53:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e888ecb-bcab-3346-aa2e-157f1b0597ed | -3.83277 | -45.34957 | 2025-11-22 03:53:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 948b7b3f-ca43-36f5-ac0f-452a3ae45ef7 | -4.14227 | -43.69063 | 2025-11-22 03:53:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07f5168e-50f6-3f03-9e3e-74fecf9b865c | -5.42871 | -40.66891 | 2025-11-22 03:53:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c7eed7a4-0601-33d8-a0ea-858c0bfcc325 | -3.86054 | -41.57705 | 2025-11-22 03:53:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2a02fe00-ecf3-3198-82d7-7f1b8c5bf9fa | -4.02718 | -42.47662 | 2025-11-22 03:53:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7000e1d7-82c3-3b54-b95a-f902025ce9bf | -3.82317 | -41.11626 | 2025-11-22 03:53:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d44750dd-1530-34d2-8112-095d1157f7d2 | -2.93374 | -48.23222 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 985e587e-3ab8-387b-a525-ab2ada1c9020 | -3.38848 | -44.0396 | 2025-11-22 03:53:00 | NOAA-20 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71b7f2f1-2211-38d6-936e-1865f2f60540 | -2.91808 | -48.24301 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db98e73a-5c66-33a2-b9d4-1cf7538da28e | -2.92126 | -48.23458 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| da48e177-249d-3870-bd22-1f393407ed89 | -5.57367 | -42.29759 | 2025-11-22 03:53:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 8c4c49c4-56f1-38e6-ad2a-ec2eed729a5a | -4.03638 | -38.24415 | 2025-11-22 03:53:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3170da72-16cd-3add-b0ad-c3084f21a40a | -2.93059 | -48.24072 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fce58c2f-e390-32ba-bde7-a5815263e3d8 | -7.28429 | -38.91255 | 2025-11-22 03:53:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3929c181-2992-3e5f-a256-6d6461caa9ed | -6.07309 | -37.45662 | 2025-11-22 03:53:00 | NOAA-20 | JANDUÍS | RIO GRANDE DO NORTE | Brasil | 2405207 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bc871552-bf44-3f44-93a9-69709cc95078 | -4.14234 | -38.2185 | 2025-11-22 03:53:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 14900888-d488-3a4d-beea-1cec7531e7b9 | -2.92786 | -48.23124 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 99f0a92d-d0f6-3aa2-bdec-7b682bfd3b5c | -5.24225 | -35.60729 | 2025-11-22 03:53:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b8ed43e5-5350-367e-aebb-526d4bab0d1c | -3.83755 | -45.35038 | 2025-11-22 03:53:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d67e87ea-5b5b-39dc-acdb-10af4c652dff | -7.2966 | -39.02832 | 2025-11-22 03:53:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ce11d2ab-730f-3ccb-b3ba-478629799caa | -2.91018 | -48.22851 | 2025-11-22 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 258fb112-7b35-369e-a6a4-1a7fc8561139 | -6.77734 | -39.51174 | 2025-11-22 03:53:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 621a095a-79a0-314c-97f7-c253a217f738 | -8.65356 | -36.81389 | 2025-11-22 03:55:00 | NOAA-20 | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 540d7bdb-7836-3dda-9469-b351417778ba | -3.14494 | -40.17714 | 2025-11-22 03:55:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 87ac50a6-58c7-3d4c-b8d3-959c7aa306a9 | -8.82976 | -35.26193 | 2025-11-22 03:55:00 | NOAA-20 | BARREIROS | PERNAMBUCO | Brasil | 2601409 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 10df9de2-b37c-32ff-9e67-c6eda93c63c4 | -0.96465 | -47.56677 | 2025-11-22 03:55:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddccbade-1fe2-3403-937e-306a28925530 | -9.96999 | -36.04008 | 2025-11-22 03:55:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 69a110ee-aafb-324d-a888-4cf9571e4af1 | -2.45008 | -45.37931 | 2025-11-22 03:55:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e7e1434-3111-33fa-ae66-1ed115c39a28 | -8.82799 | -35.25875 | 2025-11-22 03:55:00 | NOAA-20 | BARREIROS | PERNAMBUCO | Brasil | 2601409 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fa882bd9-18c0-3620-94e9-96ca4afe3d5a | -9.96936 | -36.04431 | 2025-11-22 03:55:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 67.0 |
| feb3c340-d5c0-3026-b85e-cdd42917f133 | -9.97108 | -36.05746 | 2025-11-22 03:55:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 0398367b-6784-3428-a062-9be2750a24fc | -0.96531 | -47.56268 | 2025-11-22 03:55:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b137295-0cc2-3ee4-90b9-b47f9506f23f | -7.36311 | -40.42105 | 2025-11-22 03:55:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 118deab7-b778-3eb8-b0c4-69c1fce6f2cf | -1.85316 | -47.48426 | 2025-11-22 03:55:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| eb84df19-2489-380a-96c3-bfb4657280c4 | -2.53862 | -45.53255 | 2025-11-22 03:55:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4714e5c5-5f0b-380a-b80c-b0a88c76f7a8 | -3.02386 | -41.1265 | 2025-11-22 03:55:00 | NOAA-20 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eda319ff-a95b-3905-849c-8f62759437af | -9.96451 | -36.0521 | 2025-11-22 03:55:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |


[Clique aqui para ver as próximas entradas](README5.md)
