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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 808be1c0-bd47-3cd6-a8b4-7f59c9bcbee8 | -3.0317 | -50.4176 | 2024-10-28 03:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 56d22a00-26b1-3ad4-9208-12c18e502ae4 | -3.0317 | -50.3967 | 2024-10-28 03:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 14728112-8da9-3767-9af7-9fdd1400cfb6 | -3.0501 | -50.4171 | 2024-10-28 03:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 8663b1a7-e9b4-3ab7-8a40-0e05850aacf2 | -3.0538 | -49.4895 | 2024-10-28 03:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 4db032a9-6d6f-3dee-857b-5d7528b4f742 | -3.9949 | -46.4867 | 2024-10-28 03:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |
| d4ce96bb-4e51-3bba-bfc5-4b30f09f02d7 | -4.2797 | -45.5362 | 2024-10-28 03:05:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 0b2136d1-1fee-3ce4-85b7-ae57b77d876e | -4.4094 | -45.6416 | 2024-10-28 03:05:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 4c4a40b4-5824-3f3a-b201-8faf2c4248ba | -4.428 | -45.6406 | 2024-10-28 03:05:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 914b05dc-5383-3651-a3cc-9e46d9ac1aee | -4.758 | -46.4033 | 2024-10-28 03:05:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 83.5 |
| bb56280b-7b54-3091-83e8-dc9fdca242a9 | -4.7581 | -46.3811 | 2024-10-28 03:05:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 50.3 |
| d4d8211d-ac2f-3452-aa76-ec74b608bce7 | -4.7766 | -46.4022 | 2024-10-28 03:05:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 5d33a41c-5df0-3090-a1cc-1ee026ab349d | -4.7768 | -46.3801 | 2024-10-28 03:05:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 62.2 |
| bbc1977f-13a0-33e1-ae59-ddbde087f02a | -3.56208 | -41.39822 | 2024-10-28 03:15:00 | NOAA-21 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a201107b-3cda-373a-9b99-06026db87bf0 | -3.56175 | -41.39771 | 2024-10-28 03:15:00 | NOAA-21 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 21e65215-14de-3818-8841-33b45973d7bb | -3.56085 | -41.40506 | 2024-10-28 03:15:00 | NOAA-21 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 830ae63e-65c0-3197-9933-2242914d46a4 | -3.56058 | -41.40452 | 2024-10-28 03:15:00 | NOAA-21 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 7229f87d-b75b-3655-bcfa-24ecf02c6d15 | -1.1836 | -53.5158 | 2024-10-28 03:15:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| e5f20fd5-7922-384b-a5d8-9e88952c87f3 | -1.1836 | -53.4956 | 2024-10-28 03:15:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| a8fbbd0c-ee85-3a98-bf3b-5e7ae750c145 | -1.9763 | -52.0804 | 2024-10-28 03:15:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 7c5b0726-a795-3571-b461-4e3fceec4937 | -2.2662 | -53.8027 | 2024-10-28 03:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| fe46845b-90cd-3dee-a66e-9f185558fb62 | -2.2662 | -53.7825 | 2024-10-28 03:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 6d606603-5c98-3433-86d0-92b1f76f1664 | -2.2845 | -53.8023 | 2024-10-28 03:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 37a97575-62dd-3e47-b183-a05478de0366 | -2.2846 | -53.7822 | 2024-10-28 03:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 83705cbb-a620-3642-9c1a-62c2b1d5eb82 | -2.4104 | -48.5479 | 2024-10-28 03:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 22369191-2a1d-383e-b429-d9ed7609a411 | -2.833 | -49.2413 | 2024-10-28 03:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 95e2ec63-d5d1-36be-b5cd-17bc6ccfcb72 | -2.8515 | -49.2408 | 2024-10-28 03:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| cb578264-8a27-3deb-aca6-f29ddb428783 | -2.8556 | -53.3256 | 2024-10-28 03:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| b855ea51-157e-3f32-a27d-0f6a08f59665 | -2.8699 | -49.2615 | 2024-10-28 03:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 1e3fb6a0-a915-308c-bea8-1b97f490cc12 | -2.9761 | -50.4821 | 2024-10-28 03:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| f9a33e7d-72fe-36c0-831b-b44545507076 | -2.9945 | -50.4816 | 2024-10-28 03:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 44af9c67-e1e9-34c0-a6c3-c13d1ab3fbb2 | -3.0317 | -50.4176 | 2024-10-28 03:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 118.9 |
| c708d32a-e28a-36a2-b7c4-e977060cf8bb | -3.0317 | -50.3967 | 2024-10-28 03:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| f1bc20f9-b562-3c68-9e35-da86027dd8da | -3.05 | -50.438 | 2024-10-28 03:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 6575e0f2-de67-3fbf-8e73-8b504379bc8a | -3.0501 | -50.4171 | 2024-10-28 03:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 15325c5c-0c32-351c-a775-703cc8877807 | -4.12 | -47.3388 | 2024-10-28 03:15:29 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 53245728-4503-3cc7-a257-431298ebc764 | -4.1201 | -47.3169 | 2024-10-28 03:15:29 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 127.4 |
| 9642f060-5cc2-37f7-8901-675dbfab253f | -4.1386 | -47.338 | 2024-10-28 03:15:29 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 55.2 |
| bcf5796b-005e-3496-82da-d9de84941f6d | -4.1387 | -47.3161 | 2024-10-28 03:15:29 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 57.6 |
| b60f59b4-23fc-367a-96ee-0e56ab2c76d0 | -4.2797 | -45.5362 | 2024-10-28 03:15:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 59.6 |
| d0bd32bc-2b35-3c64-803a-49edfd7fa170 | -4.428 | -45.6406 | 2024-10-28 03:15:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 909df052-b7e0-3f05-bdbb-5ca452bc22af | -4.7766 | -46.4022 | 2024-10-28 03:15:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 2cd3c87a-821c-37fc-8c89-532700ed19d4 | -8.87108 | -41.27144 | 2024-10-28 03:17:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cba95bf2-ab07-3286-8bbd-8d208b3de0c2 | -8.87011 | -41.27649 | 2024-10-28 03:17:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0c08e5c8-6ad8-3e88-ba5e-a2acd56c9a2b | -8.28737 | -40.8898 | 2024-10-28 03:17:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| fe2e9ebe-a455-35bd-ab51-1dc415603205 | -8.07416 | -39.92486 | 2024-10-28 03:17:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 8.2 |
| d0391044-c8cf-3142-b35d-484eab0a5a57 | -7.56584 | -38.76149 | 2024-10-28 03:17:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b634f845-eacf-3c3b-a0e5-2e7baa8c0c71 | -7.56517 | -38.76524 | 2024-10-28 03:17:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8b3bdd7f-6491-346d-99d0-86f21d56c7a7 | -7.56097 | -38.75705 | 2024-10-28 03:17:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 63c4ff8f-47bc-3ede-9722-ff4280828486 | -7.5603 | -38.76075 | 2024-10-28 03:17:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 989b59f7-26e1-36f7-9290-1f981d2b837f | -7.55542 | -38.75639 | 2024-10-28 03:17:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 79025a7e-ba38-31c3-bc0e-89432cd57e49 | -7.55476 | -38.76009 | 2024-10-28 03:17:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| cca73e3d-527d-3c2d-99f4-5d798d5e0a3f | -7.54993 | -38.75541 | 2024-10-28 03:17:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b984500c-6a0d-3d11-a83f-75aaf6d9012a | -7.33658 | -41.86219 | 2024-10-28 03:17:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 60cc7070-b301-31e7-aa1c-58426f8f577d | -6.67869 | -40.89478 | 2024-10-28 03:17:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2829aa92-ad77-3cb0-ab15-a1c41ace4a30 | -6.6714 | -40.89855 | 2024-10-28 03:17:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6fb6b6b4-007f-38af-9c89-6102ba3dbaf1 | -6.60624 | -37.27832 | 2024-10-28 03:17:00 | NOAA-21 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 73c335c8-3ab1-35ea-898f-cd2065876a0b | -6.60572 | -37.28128 | 2024-10-28 03:17:00 | NOAA-21 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8d9d704f-a4cc-3a92-8d83-855987f20faf | -6.59604 | -42.28271 | 2024-10-28 03:17:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 4d8a2479-a563-3553-9f4c-d72ac1e62704 | -6.59561 | -42.28316 | 2024-10-28 03:17:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d63f70b1-ac88-3cfb-bcc9-5b8d34c6fe49 | -6.59482 | -42.28925 | 2024-10-28 03:17:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 48650653-0a40-3f92-8243-50ceb399f72d | -6.59435 | -42.2897 | 2024-10-28 03:17:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b95246eb-76d7-3bfa-b4c9-02f8670ce89d | -6.15988 | -41.86654 | 2024-10-28 03:17:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 458f8fab-b480-39b5-ab8c-d8e00ce058c3 | -6.15549 | -41.85991 | 2024-10-28 03:17:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 656ddba4-9cbc-3396-a716-1316c9bdc139 | -6.15446 | -41.86535 | 2024-10-28 03:17:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| c603406b-6d98-30fc-8293-3b759d717702 | -6.15338 | -41.86363 | 2024-10-28 03:17:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| bff9b958-0d87-36a3-8628-b7a90cab0c85 | -6.09496 | -41.87559 | 2024-10-28 03:17:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| eeb49ea6-bdd3-32f1-aaaa-696d00282f1b | -6.09378 | -41.88194 | 2024-10-28 03:17:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b56b20e2-98d0-3fa3-845c-c4e135f1cb2c | -6.08812 | -41.8745 | 2024-10-28 03:17:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| dbc6aa06-a5d2-3f87-a745-0e8b4b2a97fa | -6.08697 | -41.88071 | 2024-10-28 03:17:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a74f19ec-d1ed-3fa2-9f58-d0fd738361aa | -11.13589 | -42.16877 | 2024-10-28 03:19:00 | NOAA-21 | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4a3a6471-d555-3cff-bc9c-41204bbfe09a | -15.50708 | -42.27318 | 2024-10-28 03:19:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8df01a1-7333-3033-940f-b850a9c75007 | -15.50614 | -42.27763 | 2024-10-28 03:19:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b67f5e3-c0bc-33d7-a964-58ec9c0c26e0 | -15.36658 | -40.18525 | 2024-10-28 03:19:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0c575bd5-8f87-3657-a7e5-6d5b906d5271 | -15.36593 | -40.18843 | 2024-10-28 03:19:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b5f3bfb7-1733-3238-b440-f101eebd8dbc | -15.36529 | -40.19162 | 2024-10-28 03:19:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 5079ec91-1ee1-3fd4-8a0a-cec38301fa8b | -15.36464 | -40.19482 | 2024-10-28 03:19:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3ac7464d-0c62-3333-899d-126fdb885b1c | -15.36399 | -40.19805 | 2024-10-28 03:19:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9709f16d-6c1a-37e8-ab4a-876ee142a7cf | -15.36199 | -40.18095 | 2024-10-28 03:19:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 1410ef3e-8e19-3e30-a08d-b26eef41611c | -15.36135 | -40.1841 | 2024-10-28 03:19:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 59e66298-2573-3a82-9eeb-6e777274a309 | -15.36071 | -40.18726 | 2024-10-28 03:19:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 346a17a7-00e3-3f82-805d-bfb82c67b0ec | -15.36006 | -40.19048 | 2024-10-28 03:19:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| f90294ca-35f1-3985-8304-343c5fb03e45 | -15.3594 | -40.19373 | 2024-10-28 03:19:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8a85dcda-383c-31e9-b1cb-785e934c405b | -15.35874 | -40.19699 | 2024-10-28 03:19:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| aaca445b-c569-3b06-b76d-8918488ca51c | -15.35743 | -40.17658 | 2024-10-28 03:19:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| fc224d5b-d349-3b46-9f80-9b86a02268f3 | -15.35676 | -40.17985 | 2024-10-28 03:19:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| e5b3e6bb-79ac-39b6-b973-1f5a66c36544 | -15.35612 | -40.18303 | 2024-10-28 03:19:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 6fec755f-651b-3207-b088-d3a476df7f27 | -15.35547 | -40.1862 | 2024-10-28 03:19:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| f49852c3-352b-325c-9ab4-149f35f8b7d3 | -15.35482 | -40.18943 | 2024-10-28 03:19:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 9705c348-1652-3981-872d-f9d7a7ee8a0c | -15.35154 | -40.17871 | 2024-10-28 03:19:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e29a1c9d-aebf-36ce-8fd9-25a2d8bfa46f | -15.35088 | -40.18196 | 2024-10-28 03:19:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 85cf68e3-4a37-35c2-80c0-2bc841ece6d2 | -15.3223 | -41.74583 | 2024-10-28 03:19:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 21b2a3ed-b044-3b95-9669-f2aed66cdc3b | -15.32183 | -41.74852 | 2024-10-28 03:19:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f4ae5158-ae4a-3397-80f4-89ccbbe01a5f | -15.32148 | -41.74979 | 2024-10-28 03:19:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 46d535a3-11d0-3694-b5d0-c7b4c787e679 | -13.70504 | -42.8875 | 2024-10-28 03:19:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cc843464-a040-3bb7-a861-5a994612a551 | -13.16937 | -42.9688 | 2024-10-28 03:19:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 24af4bed-df9a-36b1-b815-b0f100b1acc8 | -12.90133 | -44.61031 | 2024-10-28 03:19:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 477a71a0-9909-3e2f-8cde-f92de2fa821f | -12.89895 | -44.60567 | 2024-10-28 03:19:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6bb62f23-e324-3560-8512-6e2bdc72efc0 | -12.89734 | -44.61321 | 2024-10-28 03:19:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c56766aa-6bc9-3682-8b6c-62010a5de059 | -12.89423 | -44.60882 | 2024-10-28 03:19:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 286cebed-00bd-31e8-a723-a145eb81e392 | -12.89257 | -44.61634 | 2024-10-28 03:19:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README23.md)
