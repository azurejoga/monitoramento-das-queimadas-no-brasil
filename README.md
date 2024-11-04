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
| c93d7622-6639-3525-834f-4e1f98b40f7b | -10.6021 | -36.983101 | 2024-11-04 00:01:56 | METOP-C | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 71262c13-5f07-347f-8f27-bb8503048ef1 | -10.6134 | -36.9879 | 2024-11-04 00:01:56 | METOP-C | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d0e7e215-341c-3ea9-a886-41771cd15ac2 | -10.6119 | -36.9809 | 2024-11-04 00:01:56 | METOP-C | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0d37a3a8-488d-3eb4-b284-112f933c3696 | -10.6103 | -36.973801 | 2024-11-04 00:01:56 | METOP-C | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d1dc8bf5-47b6-3474-a236-bdcba9d4b0bd | -9.7691 | -36.3983 | 2024-11-04 00:02:07 | METOP-C | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c116048c-1f7f-35e1-bf48-21f127ee9841 | -9.7675 | -36.391399 | 2024-11-04 00:02:07 | METOP-C | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ee9d9f63-19f9-3f67-bc08-c691a50faa97 | -9.766 | -36.384499 | 2024-11-04 00:02:07 | METOP-C | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 480eb02b-fc59-3da2-afed-0f0c9789ddea | -11.1265 | -43.3088 | 2024-11-04 00:02:09 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| fcd1367a-66a5-3b76-a21e-6e72935f506e | -11.1234 | -43.293999 | 2024-11-04 00:02:09 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| fe642d35-eaf9-3ceb-bc50-3b708f854521 | -9.3875 | -35.676498 | 2024-11-04 00:02:11 | METOP-C | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2cc0d62e-f68f-38ec-b32c-e963fb85da2a | -8.9585 | -35.561501 | 2024-11-04 00:02:17 | METOP-C | JUNDIÁ | ALAGOAS | Brasil | 2703908 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4ef8fe24-6f1c-30dd-862e-d1489872f549 | -8.9569 | -35.554501 | 2024-11-04 00:02:17 | METOP-C | JUNDIÁ | ALAGOAS | Brasil | 2703908 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 53699ff6-6490-301f-8f9b-0052acb84345 | -8.3426 | -35.308102 | 2024-11-04 00:02:26 | METOP-C | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4eade8ca-40ed-341a-bc4d-ebeb576853c2 | -8.3409 | -35.3009 | 2024-11-04 00:02:26 | METOP-C | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 53624718-fd01-39bf-9a36-d3f2f8f01661 | -8.3393 | -35.2938 | 2024-11-04 00:02:26 | METOP-C | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 187d2363-bfd4-3764-b696-bf4086f3c819 | -8.6509 | -40.9062 | 2024-11-04 00:02:41 | METOP-C | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 6beda61f-2786-3a8a-a0bb-9bc81b91a0d7 | -8.6271 | -40.560799 | 2024-11-04 00:02:41 | METOP-C | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| ab786ea2-2377-3619-99d2-87e72047a900 | -8.6529 | -40.915699 | 2024-11-04 00:02:41 | METOP-C | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 410d27fe-e544-35d3-b746-6373cf36b7e5 | -8.6432 | -40.917801 | 2024-11-04 00:02:42 | METOP-C | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 6bf25f54-325c-3622-a64b-a0b4a2ee494c | -8.6411 | -40.908298 | 2024-11-04 00:02:42 | METOP-C | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| f9b332d6-5a79-305e-9df7-cc82250ed3be | -6.9965 | -34.9352 | 2024-11-04 00:02:46 | METOP-C | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5fbc9688-d400-3409-90b0-f3debaf777a6 | -6.9947 | -34.927799 | 2024-11-04 00:02:46 | METOP-C | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ba4ac443-7554-3913-a4c5-b2f0455438f1 | -6.993 | -34.9203 | 2024-11-04 00:02:46 | METOP-C | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c3290e7c-3f51-3973-965e-62f92a2084de | -6.7614 | -34.989399 | 2024-11-04 00:02:50 | METOP-C | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8dcfde05-35d0-3f00-b770-6d8e0b943dc3 | -6.7596 | -34.981998 | 2024-11-04 00:02:50 | METOP-C | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 587d7447-3981-3b1b-b1f6-91b8ac0f0dbe | -8.24 | -42.990898 | 2024-11-04 00:02:55 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a9999b0d-809d-3a93-9122-fa3f61281437 | -8.2373 | -42.978199 | 2024-11-04 00:02:55 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 96f209de-140b-3155-b8a4-4dd2ce5dc142 | -6.7737 | -37.552299 | 2024-11-04 00:03:00 | METOP-C | VISTA SERRANA | PARAÍBA | Brasil | 2505501 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 332556fe-eb61-3c8b-bde4-d8f9c046b67a | -6.68 | -37.457699 | 2024-11-04 00:03:01 | METOP-C | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 183e7b32-bb41-3aa8-9fc9-b448e9924538 | -6.6945 | -37.476101 | 2024-11-04 00:03:01 | METOP-C | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| d11f5f2d-dea2-379c-aa2e-bea6abe29a33 | -6.6929 | -37.469299 | 2024-11-04 00:03:01 | METOP-C | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| dbce67f2-12eb-3158-8d31-23853165c002 | -6.185 | -35.262402 | 2024-11-04 00:03:01 | METOP-C | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7650894f-7842-35f1-a641-ed79210dd5d1 | -6.1965 | -35.267502 | 2024-11-04 00:03:01 | METOP-C | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2bfa99b3-8b6e-3e38-bc87-eaf0c68498b8 | -6.1948 | -35.260201 | 2024-11-04 00:03:01 | METOP-C | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 83bd9e74-f6bc-3e0e-8f17-45491cbe1067 | -6.1931 | -35.2528 | 2024-11-04 00:03:01 | METOP-C | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 922e382f-867b-3257-a415-bd580d729740 | -6.7458 | -38.1563 | 2024-11-04 00:03:02 | METOP-C | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| e670a23c-5b20-3060-b529-4ac4940419ac | -6.7442 | -38.1493 | 2024-11-04 00:03:02 | METOP-C | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 8fd61bd9-5d14-3b3d-9a59-41e672d51df5 | -7.6507 | -42.766499 | 2024-11-04 00:03:04 | METOP-C | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 03c4b88a-35d3-3323-b63b-b08dd71117f8 | -7.6605 | -42.7644 | 2024-11-04 00:03:04 | METOP-C | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d54ca14c-b9c6-3f6b-aa54-dac730e144dd | -7.6957 | -43.118599 | 2024-11-04 00:03:05 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 211a40cd-2a38-3d62-a1ac-b7afb7700770 | -7.7055 | -43.116501 | 2024-11-04 00:03:05 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 36b36b6c-74c5-38f4-a142-4c0bc08bfdc7 | -6.9362 | -40.850601 | 2024-11-04 00:03:09 | METOP-C | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6b10b970-72b7-3dc5-963f-7604b2c13dbb | -6.9343 | -40.841599 | 2024-11-04 00:03:09 | METOP-C | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 93e98d6f-975f-34a9-826e-54cc688e35d6 | -6.9323 | -40.832699 | 2024-11-04 00:03:09 | METOP-C | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4e82fca1-05f0-385a-bafd-c247416ca17d | -6.946 | -40.848499 | 2024-11-04 00:03:09 | METOP-C | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d0c1487d-3259-35db-acfb-49f7bf41cbc5 | -6.9441 | -40.8395 | 2024-11-04 00:03:09 | METOP-C | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 269a9f86-5692-3550-9057-85ecb289e2ae | -6.9421 | -40.830601 | 2024-11-04 00:03:09 | METOP-C | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9dc7a375-ba4a-37ba-9b28-9dda9f25b657 | -6.5141 | -41.496101 | 2024-11-04 00:03:18 | METOP-C | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a6356ca6-2d64-3321-9ed9-89f73da59a10 | -6.4469 | -42.076401 | 2024-11-04 00:03:21 | METOP-C | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8253a7e7-d836-3788-bd4a-7bd5829920af | -6.4446 | -42.065899 | 2024-11-04 00:03:21 | METOP-C | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 84776692-b776-3d09-8ac8-a92f2f929219 | -6.3204 | -41.920601 | 2024-11-04 00:03:23 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4cae1fce-4df7-31a1-ad0f-7efe44412379 | -6.3324 | -41.9286 | 2024-11-04 00:03:23 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8dda0e94-911c-3b46-bff1-7187228140d9 | -6.3302 | -41.918499 | 2024-11-04 00:03:23 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 86ea9497-6446-39eb-aa01-bec3fae39206 | -6.328 | -41.908401 | 2024-11-04 00:03:23 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 213151cf-b078-3821-9c5a-3d27d2c98ba0 | -5.9819 | -41.919601 | 2024-11-04 00:03:28 | METOP-C | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1e2f13a9-ee84-3eb8-b024-365995001276 | -5.9796 | -41.9095 | 2024-11-04 00:03:28 | METOP-C | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cefe7cac-287b-3570-8be0-3527f5b58ab0 | -5.9939 | -41.927502 | 2024-11-04 00:03:28 | METOP-C | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ddbdb092-da75-36e3-b6c1-74dffac5330b | -5.9917 | -41.9175 | 2024-11-04 00:03:28 | METOP-C | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ba463f5a-b60f-355b-b104-988de8cc4ef3 | -5.9894 | -41.907398 | 2024-11-04 00:03:28 | METOP-C | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9df10769-984c-320d-9ebd-d1ea9b53046f | -6.2809 | -43.378201 | 2024-11-04 00:03:29 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f460ccc2-c7f1-3926-a918-f5f93f375b6e | -6.2782 | -43.365601 | 2024-11-04 00:03:29 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 023e6421-ef9e-3a8a-b6b0-11154955a1cb | -5.9292 | -43.639801 | 2024-11-04 00:03:35 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4be64a4-c649-32a8-9003-3ef895c6212b | -5.2434 | -41.2276 | 2024-11-04 00:03:38 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 88d0568f-e3d0-3641-a937-9ac30ad8e274 | -5.3376 | -43.738899 | 2024-11-04 00:03:45 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d76abe27-373c-3696-8ad6-db0c8046acee | -5.3348 | -43.726002 | 2024-11-04 00:03:45 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 998aa226-d195-3bf8-b25c-fd69273b7c2c | -5.1824 | -43.963402 | 2024-11-04 00:03:49 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 785e715c-0eaf-39dc-b6e2-8d88aaaf2b93 | -4.7564 | -42.729301 | 2024-11-04 00:03:51 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 71e59d86-08b8-3192-a710-ba87a3469fc8 | -4.8003 | -42.834202 | 2024-11-04 00:03:51 | METOP-C | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f6b2e318-1781-398c-94cb-b82e01c582bd | -4.5129 | -42.4179 | 2024-11-04 00:03:54 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 879bceb3-65cd-3dcb-96bf-5fa5106bf4f2 | -4.6144 | -42.8284 | 2024-11-04 00:03:54 | METOP-C | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7cec7584-3979-3653-b684-fea96597a313 | -4.612 | -42.817501 | 2024-11-04 00:03:54 | METOP-C | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5081751a-09dc-3a81-a968-75ee97ecf6ab | -4.6218 | -42.8153 | 2024-11-04 00:03:54 | METOP-C | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2a5d252c-a5e1-3b5f-984c-6aa6c5367a9a | -4.4238 | -43.492802 | 2024-11-04 00:03:59 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0049f9ec-a393-3dba-898f-8166d339cc04 | -4.4212 | -43.4809 | 2024-11-04 00:03:59 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab3f9786-3d12-3b40-b394-fc1e8ec0834a | -4.4185 | -43.468899 | 2024-11-04 00:03:59 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf0e9cdd-b7e5-3838-9b1e-e5ccecac54f7 | -4.4159 | -43.457001 | 2024-11-04 00:03:59 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0c2491e-46e2-30fd-b5fa-5659b3f0c7e6 | -4.3875 | -43.098499 | 2024-11-04 00:03:59 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0b24664-5393-3c9d-bfd6-5ac7cfec9892 | -4.431 | -43.478802 | 2024-11-04 00:03:59 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b029c881-f7e2-365c-b76f-310dbe66fe97 | -4.4283 | -43.466801 | 2024-11-04 00:03:59 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98ffbaa7-8ca3-3811-9090-58073242758f | -4.4257 | -43.454899 | 2024-11-04 00:03:59 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d87d7c5-dba3-3dc9-8ca5-18aadef995f3 | -4.39 | -43.109798 | 2024-11-04 00:03:59 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c8e0a97a-2264-3325-9b51-6d6f73ddf4ce | -4.4133 | -43.445099 | 2024-11-04 00:03:59 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2bcd1eb9-e1ce-35a4-944f-58a1aa378c9d | -3.9346 | -41.531898 | 2024-11-04 00:04:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| aeaefef5-61a4-33d8-99b7-13b611e9b962 | -3.9326 | -41.522999 | 2024-11-04 00:04:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0ef3b2c9-d6d8-34c7-827b-c4eba543b0ff | -3.9306 | -41.514099 | 2024-11-04 00:04:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ab379dfe-844c-3617-8725-60c292b7bded | -3.9444 | -41.5298 | 2024-11-04 00:04:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 21b26b41-d023-3ff8-9154-80c51393fb37 | -3.9424 | -41.520901 | 2024-11-04 00:04:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9f0ef961-b370-3b11-af89-9bc8d636c1f8 | -3.9404 | -41.512001 | 2024-11-04 00:04:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b3772e3c-0650-337c-a766-de7c8502178e | -4.399 | -43.473099 | 2024-11-04 00:04:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 400d7235-9a49-37ad-b3ac-fe3bbeb4c81d | -4.4114 | -43.483002 | 2024-11-04 00:04:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d472629-fc41-35fa-8285-ec5f3481a18e | -4.4087 | -43.471001 | 2024-11-04 00:04:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d96f1efa-9488-3e67-9149-dad91fe66a59 | -4.4061 | -43.459099 | 2024-11-04 00:04:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2a808db-40c5-34d0-97dc-448a341709f0 | -4.698 | -46.036201 | 2024-11-04 00:04:04 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 575911ae-a544-3574-8ba7-0155c633684d | -4.6271 | -45.6651 | 2024-11-04 00:04:04 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 31e5b9b4-066f-3c55-ad66-edc6d0670a73 | -4.6091 | -45.722599 | 2024-11-04 00:04:04 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 657b7cad-a350-3bbc-9dc8-b62be7824aa7 | -4.6883 | -46.0383 | 2024-11-04 00:04:04 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 751a6ab9-41b5-37d8-b985-06a1e29845e3 | -4.6163 | -46.034599 | 2024-11-04 00:04:05 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6a556306-da4a-316a-b194-d227de706ba3 | -4.6124 | -46.016499 | 2024-11-04 00:04:05 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 43a2e835-9512-3666-9958-6a907b402e66 | -4.3767 | -45.221802 | 2024-11-04 00:04:06 | METOP-C | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 909e658c-28ef-3412-bd0c-739055c8c4ef | -4.6506 | -46.377499 | 2024-11-04 00:04:06 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
