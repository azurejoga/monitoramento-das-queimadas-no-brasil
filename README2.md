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
| 637f0a88-8581-33c8-a779-85d590034914 | -14.0877 | -58.144 | 2026-06-02 00:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 52b3c854-d886-361e-99c1-485916cab610 | -11.614 | -55.1861 | 2026-06-02 01:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| c44a83a6-fac0-37c0-a336-002771413d88 | -16.1584 | -58.4702 | 2026-06-02 01:09:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 32e2a8d1-ee2e-3491-9cc8-cc8dc0a8e6c6 | -16.1563 | -58.461399 | 2026-06-02 01:09:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 033c9228-2380-36df-ac93-2f89fa21dc19 | -12.2984 | -57.396801 | 2026-06-02 01:09:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf878b7a-e011-3e7d-a238-fc9b11a2cc47 | -14.0829 | -58.142601 | 2026-06-02 01:09:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 404293ae-baa7-3fe0-bf2a-e39e205c9ad7 | -10.5632 | -57.316502 | 2026-06-02 01:09:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7aed302-06a2-3fc5-96c9-63274c9878a3 | -14.0806 | -58.132999 | 2026-06-02 01:09:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 100e8e03-53dd-3b7e-8728-e9d5cf864384 | -11.6108 | -55.178398 | 2026-06-02 01:09:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf38117f-92ed-32dc-b70f-11f29f4dc781 | -11.8811 | -61.033901 | 2026-06-02 01:09:00 | METOP-B | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f28ff425-02a3-3945-aaeb-45c055ff949a | -14.1804 | -52.858799 | 2026-06-02 01:09:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4afaa9d7-e00e-315d-9194-3a7b0bb3ef37 | -16.1542 | -58.452599 | 2026-06-02 01:09:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c78ec7a3-f0d2-3b66-a01c-0284d511cc54 | -11.6204 | -55.1758 | 2026-06-02 01:09:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52facf92-a34a-36a8-b2da-939a98e12b2b | -10.0272 | -59.3353 | 2026-06-02 01:09:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce4556fe-4beb-3ce3-8920-4e3cbab9ade4 | -11.8828 | -61.041401 | 2026-06-02 01:09:00 | METOP-B | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 79fe2222-3969-3776-859e-23b6c9e758f5 | -11.6163 | -55.159698 | 2026-06-02 01:09:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7940255d-9cad-32f7-9663-b90e9e9c55ec | -11.6067 | -55.1623 | 2026-06-02 01:09:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 11c47755-f8cd-3307-805c-6b3675eba816 | -14.0877 | -58.144 | 2026-06-02 01:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 65cf7dd1-257a-3419-826d-6d5d0a9b78b5 | -11.614 | -55.1861 | 2026-06-02 01:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 570c9415-1eb9-3de2-add3-2cf28696840c | -11.614 | -55.1861 | 2026-06-02 01:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 6b053a54-392f-3f87-a0a9-185e23ec49d3 | -8.9884 | -47.9906 | 2026-06-02 01:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 58574671-3ca7-3a07-8777-da71f99c154d | -11.614 | -55.1861 | 2026-06-02 01:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| c94a2f99-e3d6-3a28-9a2b-b8cf69d8167e | -9.4964 | -40.3088 | 2026-06-02 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 82.1 |
| 31012159-0bd4-3267-b567-722dada8d5a1 | -11.614 | -55.1861 | 2026-06-02 02:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 441965a8-074c-3b0c-84fc-158c5f4f15be | -11.614 | -55.1861 | 2026-06-02 02:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 39.7 |
| e43426fb-4f4c-3de0-8573-7d06aa2175ae | -14.0877 | -58.144 | 2026-06-02 03:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 49.1 |
| d2baefdb-c856-36da-b557-f2cde2eb4153 | -8.72486 | -47.98087 | 2026-06-02 03:57:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f3e342d6-b013-3e04-8bda-70c3ae613f95 | -8.69112 | -49.08323 | 2026-06-02 03:57:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a78e31a4-035b-3480-9cd1-b30bcde99280 | -8.60164 | -45.9216 | 2026-06-02 03:57:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 696a7a83-e1ba-39a0-9646-e92697723644 | -5.52138 | -37.48323 | 2026-06-02 03:57:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0937ff9f-78d0-3011-b631-3bb37f96be18 | -9.34298 | -37.30812 | 2026-06-02 03:57:00 | NOAA-20 | POÇO DAS TRINCHEIRAS | ALAGOAS | Brasil | 2707206 | 27 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0ca2481d-ea41-3f5c-8f36-231258ff916e | -8.97937 | -47.97968 | 2026-06-02 03:57:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 8e2e4384-94be-3a47-a06a-da8e2ad37d88 | -8.12478 | -45.89689 | 2026-06-02 03:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe4022ad-6bb3-3163-ac35-b1a6d3aa2bf7 | -8.6904 | -49.08714 | 2026-06-02 03:57:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9410fff-f6f1-34e1-9cb4-4c9e3ab6919b | -8.72549 | -47.97753 | 2026-06-02 03:57:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 31c0afcf-be18-3433-b326-51567ddf3604 | -8.68762 | -49.07042 | 2026-06-02 03:57:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c7722cf5-af42-336f-9624-4c010f24bb71 | -5.52083 | -37.48671 | 2026-06-02 03:57:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| eaf60fee-f2b6-34c3-82cb-2d38ca888a5b | -9.55335 | -36.58757 | 2026-06-02 03:57:00 | NOAA-20 | IGACI | ALAGOAS | Brasil | 2703106 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 57cf1384-78b9-30ba-ab93-54ae95642e4b | -6.77026 | -45.02387 | 2026-06-02 03:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb3a62a3-490d-3617-9692-ad85a2244f43 | -6.76579 | -45.02311 | 2026-06-02 03:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 223b01fc-f710-3de2-be64-6e71dbd502c8 | -5.49482 | -37.24312 | 2026-06-02 03:57:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ef4ca1bf-7b68-3e70-8362-d6edb0324d3e | -9.08453 | -50.60047 | 2026-06-02 03:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1fef859c-6792-3476-bb3a-a22b58ad596e | -8.97876 | -47.98299 | 2026-06-02 03:57:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 4c9cc537-948a-35c8-83c6-4f5a4e2388a3 | -7.05854 | -42.12511 | 2026-06-02 03:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f9f2cbc3-b727-3b0a-bd0f-ed19942a074b | -6.60806 | -47.54129 | 2026-06-02 03:57:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf05f982-0c6d-3b9c-a7e4-886c5bf350cf | -9.08302 | -50.59929 | 2026-06-02 03:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5bec39e9-f96d-3a61-9c9f-24bf8a75e763 | -6.76502 | -45.02749 | 2026-06-02 03:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b438cad9-11d3-35e0-9105-d4af9506ac48 | -8.69329 | -49.07143 | 2026-06-02 03:57:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9f96592-9908-319d-a09b-a6650a830392 | -6.06681 | -42.5149 | 2026-06-02 03:57:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 57306fcf-08d5-3ce9-9772-ce07370462fe | -6.27997 | -44.64523 | 2026-06-02 03:57:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1bab3fa-d232-3c8e-a35d-4b7f73f219a0 | -8.68688 | -49.07438 | 2026-06-02 03:57:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a4128ef8-0b75-3b01-8e9d-618f80a41586 | -9.12616 | -47.65319 | 2026-06-02 03:57:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2da143b-9590-3f6f-9da4-51393904824d | -8.72424 | -47.98425 | 2026-06-02 03:57:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| af23cdc5-8339-3edc-b58e-f37c91f6c063 | -8.12392 | -45.90171 | 2026-06-02 03:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31efda07-7460-3ab5-8500-3d1a831c850c | -6.7695 | -45.02824 | 2026-06-02 03:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7b42469-4216-3a28-b50e-d612ebe39ba7 | -7.54984 | -37.25801 | 2026-06-02 03:57:00 | NOAA-20 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 10be5057-dc82-3a4e-b2d1-c16bb5fd1473 | -9.08545 | -50.59559 | 2026-06-02 03:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f582b28b-e319-3003-b78c-c9a5120b1b74 | -9.13125 | -47.65432 | 2026-06-02 03:57:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64a21152-b06e-398c-940c-12cb7e3ac487 | -9.39996 | -47.36966 | 2026-06-02 03:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c1973de-1ce2-3928-a9b5-e980350dcc4d | -5.51998 | -37.62178 | 2026-06-02 03:57:00 | NOAA-20 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ce42fe3c-4913-30ed-b025-97f13fb6d1b9 | -5.61261 | -37.5299 | 2026-06-02 03:57:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 538950ce-aef8-3031-bcd0-415acc3c3522 | -5.4567 | -37.72186 | 2026-06-02 03:57:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1f624a3a-31c0-357b-8fd9-64ae4abe16fc | -11.84432 | -46.64126 | 2026-06-02 04:00:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64dc160b-eb97-310c-a5fb-59f31f6f2a69 | -10.74673 | -46.90485 | 2026-06-02 04:00:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e540e8e2-e655-3442-adf1-24cd47c2c13c | -14.18782 | -52.8831 | 2026-06-02 04:00:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f6d6e56-2495-3c7d-b1ed-30f1f0551e04 | -12.00167 | -45.3541 | 2026-06-02 04:00:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbea306c-8417-358b-ad9c-62efd9ddb770 | -9.88844 | -52.44497 | 2026-06-02 04:00:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66d59d76-47aa-341a-9d62-fc8a82b0bc01 | -10.4035 | -49.44815 | 2026-06-02 04:00:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87bd656d-02fc-364b-be5a-55d173ffc5d1 | -12.31921 | -47.90602 | 2026-06-02 04:00:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b35462fd-117e-3f37-bb73-46aedc553c9f | -14.18905 | -52.87734 | 2026-06-02 04:00:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b13023ba-a92b-3ef0-9849-b83c6f1a9b30 | -14.05195 | -46.32969 | 2026-06-02 04:00:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 828fa083-0c17-3426-94ae-6db30231e3c4 | -13.97295 | -46.02548 | 2026-06-02 04:00:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cec4fcea-752d-3805-97fe-32f15afb12d8 | -15.55269 | -42.64318 | 2026-06-02 04:00:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4bad73cf-ce8c-3cf5-8491-4bbcddb3da03 | -12.00626 | -45.84342 | 2026-06-02 04:00:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d5f0111-b616-3960-9d88-4a0df059b086 | -11.93479 | -49.30129 | 2026-06-02 04:00:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05b11f0e-3f7f-3781-b21d-f808fd13096b | -13.96872 | -46.02473 | 2026-06-02 04:00:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff612b40-49cc-34be-8319-2afc06fe2c19 | -12.00248 | -45.35326 | 2026-06-02 04:00:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 471b0277-2fbf-3ebd-86fb-889f1962a9d1 | -12.29655 | -47.91096 | 2026-06-02 04:00:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f00991e-da85-3da6-b213-64e12f964344 | -11.59331 | -47.4468 | 2026-06-02 04:00:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dab026c6-8d31-374a-982e-b14e76c2e99a | -10.98341 | -45.09336 | 2026-06-02 04:00:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 128325f4-7b6e-3468-9a68-91116598c381 | -11.3449 | -47.18819 | 2026-06-02 04:00:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39163189-1671-33e7-b429-b3656bf2afe9 | -11.96755 | -47.36872 | 2026-06-02 04:00:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3de37410-af89-3501-8f8d-4df44816fc1d | -12.01356 | -49.27271 | 2026-06-02 04:00:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 128a989f-2298-3e1d-8cf4-e83b6906cad5 | -14.18809 | -52.87826 | 2026-06-02 04:00:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a1bb0eb-f34d-3331-b032-c0567f2e030d | -14.18684 | -52.88398 | 2026-06-02 04:00:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bd59904-88b5-38db-bbec-04f1a9f709cb | -11.33237 | -47.2021 | 2026-06-02 04:00:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31f61144-788f-36f3-bfe0-e40739fca7ee | -10.97922 | -45.09264 | 2026-06-02 04:00:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1495be10-5ebe-3a27-aaf5-afec74233737 | -11.96778 | -47.36557 | 2026-06-02 04:00:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28021b24-b752-3191-941b-c4c252663b24 | -11.93409 | -49.30489 | 2026-06-02 04:00:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7cdde7ad-081a-3a9f-94eb-61dc2ce5c00c | -11.58364 | -47.44494 | 2026-06-02 04:00:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d9d590c-a707-3534-8a16-4fcbf9a956d6 | -11.96677 | -47.37086 | 2026-06-02 04:00:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7618194-f914-367d-9846-48d2491e7115 | -16.58407 | -45.87986 | 2026-06-02 04:00:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ec2e36a4-794d-318a-b135-c943674787a8 | -11.58946 | -47.44051 | 2026-06-02 04:00:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d392f5dc-2903-376d-a1d9-1fe6c93b2edd | -10.03614 | -51.68721 | 2026-06-02 04:00:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15adf814-4b86-3bb7-9b89-4cc8f6908ce6 | -14.05271 | -46.32555 | 2026-06-02 04:00:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86d01e7e-beaa-3794-bd76-a7ed747e69bb | -14.05118 | -46.33384 | 2026-06-02 04:00:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2628c5d0-433e-337a-9eb8-dab51a6501c0 | -14.05626 | -46.33045 | 2026-06-02 04:00:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd48b60e-1007-3bed-adb4-77d64043e64e | -10.74621 | -46.90358 | 2026-06-02 04:00:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b175e422-1688-359b-9615-4d82302e3175 | -11.58848 | -47.44582 | 2026-06-02 04:00:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bac7c3dc-4b4f-32b5-baf5-de31ffb0b3bc | -10.40427 | -49.44419 | 2026-06-02 04:00:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README3.md)
