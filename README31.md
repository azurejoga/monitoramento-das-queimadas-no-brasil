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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77b5f026-4be5-31fd-8f33-6ed29ad1db6a | -2.22787 | -46.42596 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 037179ff-7265-388d-956c-328e2ec54e4d | -2.57642 | -48.17974 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fc107e1-04be-3d3e-93cb-5c6d1f9a06c3 | -3.52461 | -40.91496 | 2024-11-09 04:31:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 73a452ff-38b0-3939-9c4f-fe848fd20231 | -1.81079 | -52.26518 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e28ea7f6-e074-3584-b5a9-0745bf0ee390 | -2.41368 | -48.5209 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 157418c1-229c-30ab-bc8b-4b365f3c852b | -2.17945 | -48.32753 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2fb0c67a-33fb-3194-9b7e-a6a996dd05a1 | -2.14024 | -46.66295 | 2024-11-09 04:31:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| eace1e34-e111-3fe2-a689-e05c31bf33dd | -1.67996 | -53.18249 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b6f7964e-d20a-328c-b033-69c66685e4a9 | -2.26025 | -48.98009 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd705e4a-7717-36d8-98d3-ccc0a90ab372 | -2.59771 | -46.10225 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6aee380d-18ff-3f4b-92b9-3af37d9964cb | -1.52379 | -52.18251 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1af69fb5-3a44-3ad3-8352-44d98bd55ce2 | -2.36776 | -46.86049 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 36a050f8-9c6b-38b1-ad87-6726ed10e73c | -2.51409 | -47.46985 | 2024-11-09 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f951353a-7829-3148-9fc1-1b92ff461955 | -2.6009 | -48.19789 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 91d9baac-e0c1-3d8e-bb70-b2ef9aaa4aa9 | -2.10707 | -50.56689 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f9f123a-1b03-3b58-bca4-86e9304d0424 | -1.52614 | -52.19411 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9a4d6139-b8b9-3ee1-b354-41c83761fed8 | -2.89461 | -45.38602 | 2024-11-09 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8422a86b-04b2-395e-ab48-f96a089140b4 | -2.68723 | -46.70988 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36c691ac-3126-33d0-86c0-cbb4ddfed22f | -3.14459 | -45.95166 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40eac5d9-28e7-38b1-92c2-d18a9ae50670 | -2.10185 | -46.20795 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2c616aa-2e5c-357a-b63c-1fc08561b3b2 | -2.22338 | -46.54186 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e7525eb0-aa9e-3063-ad56-b79cc311650f | -2.30382 | -46.48433 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c62be856-49a1-3cd2-a654-c4beb8261f83 | -2.34111 | -46.57129 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5384b454-1695-3c6f-828d-d5990fdc7987 | -1.13844 | -48.23547 | 2024-11-09 04:31:00 | NOAA-21 | SANTA BÁRBARA DO PARÁ | PARÁ | Brasil | 1506351 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56a1976b-48b9-33f9-a7d3-772adb6c2885 | -1.12594 | -48.38048 | 2024-11-09 04:31:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1049627-9a65-3e3b-aa8d-fd886ab1b120 | -2.17551 | -46.43561 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfa6f442-cb5f-3fe0-919a-9a213c8d0405 | -2.20685 | -48.3644 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d199e170-5507-3176-b4a1-7c14cc09988b | -2.15899 | -46.67287 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26d2141c-4e2b-3ddb-b48e-4fd6f898fa53 | -2.37171 | -49.36146 | 2024-11-09 04:31:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72077133-2c3a-3c79-8341-58b83e1b441a | -2.16304 | -50.70803 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdc23392-1e6c-3933-91c4-ddde7e26cde4 | -2.23201 | -48.42292 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26f429b5-f064-3d21-8baf-86185aef0af6 | -2.42633 | -50.49374 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58c5d37b-bd2a-32c8-a041-6f37be658f2f | -3.12673 | -45.95619 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db7aa568-5809-310d-8068-3d1920796da7 | -2.36888 | -46.74464 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ec9e4a7-9f07-3665-9e1a-1af353ee5647 | -2.6245 | -46.1494 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b9dea8f6-7830-3248-af65-e7e465e1a6bd | -1.62879 | -47.3668 | 2024-11-09 04:31:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b87093c3-2be1-387f-b15b-13eea0112365 | -2.31222 | -50.64437 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfbe7f7e-de04-315b-bdc9-f784524acfed | -1.64572 | -47.8231 | 2024-11-09 04:31:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 053cb29f-2994-32ce-9de4-383eed2751c9 | -2.37486 | -46.72795 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cce8a526-0bd8-3e53-b7da-3da843beb66b | -2.09671 | -48.90262 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5f3fa25-83f9-39ff-8ec7-2da0cc918b39 | -2.1226 | -50.13288 | 2024-11-09 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c8b3a2e-720d-3730-9520-cd77e9c728ee | -2.15302 | -46.68955 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d79ad19-e468-3c2e-ab3d-68fbe93772ef | -1.83423 | -52.01804 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8f59b13-16ba-3a6d-a8ad-e6309e5a8914 | -2.23704 | -48.36905 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1c5bcf4-8d52-3196-b126-d08b7b22e840 | -1.22726 | -51.75615 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f04daac-1c46-3087-a9d8-a072df231d1e | -0.38373 | -51.44128 | 2024-11-09 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 36ac13b7-c48a-3826-b3f1-d2be029919d1 | -2.28629 | -46.50992 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ade41a6-3b5f-36df-b659-bc5917f91b46 | -2.3453 | -46.65299 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b59764f8-e04b-35d0-a7d5-dc087a3eab6f | -2.07919 | -50.33982 | 2024-11-09 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5cb16717-9102-3961-afdc-0aa470e1880b | -2.1722 | -46.4351 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 853999fc-0978-3959-877a-7f2cd66559d0 | -2.14179 | -50.13976 | 2024-11-09 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0de319c8-11eb-33d4-8458-a0227b269cab | -2.54786 | -47.12362 | 2024-11-09 04:31:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 51880be6-812c-3d2b-bebd-25b8070f3f1b | -2.56418 | -46.18667 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6af4de90-b226-3368-a6a7-f0ba58880348 | -3.59452 | -42.83857 | 2024-11-09 04:31:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa6da5c2-b56f-372a-8007-078c52309bf8 | -1.46265 | -52.56544 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2dd5a9fe-930e-32ce-bc50-a806ddfec8bb | -2.23393 | -46.56109 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 306f756f-bae5-35ff-a8bf-e7ab846b7a42 | -2.17999 | -46.45044 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a99eb434-cb9b-3fbc-9c95-e92c0a2e4196 | -1.10837 | -51.7439 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbfa7344-e6c4-3854-849f-e6e9624ccd4b | -2.56913 | -46.17671 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aed0fac7-ccb5-3527-a96d-9a0d2fb0545f | -2.4303 | -46.30522 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8258a4f5-d490-3708-8948-97cc32eaf410 | -2.22977 | -48.48106 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee00588a-9345-3e10-8a56-09cad801eef2 | -2.34665 | -46.5792 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d613b80-6a65-3514-8819-6012944234ce | -2.21873 | -50.45496 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c41661c1-c737-3588-9e6c-a117b246970a | -1.34662 | -51.42585 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64261177-44db-3b5a-b4df-ad23cf26fc8a | -2.24526 | -50.71624 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 067548ae-d960-3bb5-8333-29eaed0d2496 | -2.15355 | -46.68612 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c800d08-b994-3238-bcfa-70ba3ed13f95 | -2.33109 | -48.5736 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57deb1e3-1088-3791-9ec4-4c381e5948ab | -2.2669 | -48.07035 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37fe8906-f5e5-31fc-b150-e9e72d8aa6fb | -1.19134 | -51.98935 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| deaeadfa-191c-3e96-94c7-6d69585519eb | -2.52804 | -47.38052 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d84117a-80da-3bf3-9160-17aa129cfa9c | -2.17273 | -46.43164 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f1e41cb-6cda-3cf6-b8e0-f188f9c4a331 | -3.29673 | -43.54541 | 2024-11-09 04:31:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 916dd368-c465-3b20-bdc9-36d1eb65575d | -1.68064 | -53.17825 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 32ef075e-1a6d-383f-8e73-0cb9a21fbe16 | -1.51618 | -52.1776 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 34b45a04-0a7e-3a16-ba22-7c9008e44dc9 | -2.46009 | -50.39923 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea3490c1-f387-3003-bbd2-fe093ba9bf09 | 3.3625 | -51.27542 | 2024-11-09 04:31:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c8f6e7f-ebce-3032-9864-80acb355ec05 | -2.58146 | -48.21287 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8790f885-6ea3-3f8d-a722-f2c513ca5416 | -2.41154 | -48.4038 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b70cf308-5cdf-32e3-9599-c57c5388c626 | -2.36499 | -46.85654 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 74357fa1-258d-3425-8e7d-948ddc8c74dd | -2.45942 | -50.40344 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c594eed1-7f20-30c0-9b1e-63f7d9c5b65e | -2.34245 | -46.62789 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6bf9046f-d1ab-369d-bfe6-1cf1b63267b2 | -2.61314 | -46.24423 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb6fe7ca-bb2a-31f9-875b-fa494f293eb4 | -2.18176 | -48.3788 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 864d2055-fede-31b1-b935-3e08c2547013 | -2.63213 | -46.77816 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 796e6a52-7d52-306f-a573-27d089b9a912 | -2.31482 | -46.47895 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78da8f6e-0f8d-3f11-92a1-199e3830d11c | -1.51266 | -52.17332 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3fbace5f-47a4-3c5e-8bc1-848881434115 | -2.79512 | -48.28243 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5c713f28-7960-3e5a-8082-99dca2fefd48 | -1.89171 | -48.79944 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 404511ae-154d-329c-a2c8-3e81b9afe936 | -2.05127 | -51.95844 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c347d80d-7761-38d6-bd9d-af314fa0a1de | -2.52474 | -47.38001 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbcfd725-cb28-31f7-82df-afcfa5717c76 | -2.39557 | -49.84646 | 2024-11-09 04:31:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b4b13bd-d2e0-34c3-b461-c852aa23c743 | -3.23513 | -45.38439 | 2024-11-09 04:31:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0bb146d-0632-39fe-8785-f4ebed509d70 | -0.60079 | -49.52457 | 2024-11-09 04:31:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbb5e584-72f8-3f06-b789-ad6c6e08387d | -1.72136 | -52.4641 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 224f3dba-a34f-3132-a703-3282e61e8fd0 | -0.40507 | -51.47738 | 2024-11-09 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6aed3bad-bb83-3ee2-8020-ab9ae3292d46 | -2.29045 | -50.47478 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c860c750-5e61-37b8-abb8-c1daaf1481cb | -2.51904 | -46.36853 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 585372c3-3fd6-3ba1-9773-6dc5a95cb1ba | -1.45842 | -52.56497 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67f42068-0dc4-3f98-9bc0-b29c38293330 | -2.31272 | -48.31891 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a75719d-cf7d-3fb1-ade4-281aa62b8dae | -1.52321 | -52.18617 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README32.md)
