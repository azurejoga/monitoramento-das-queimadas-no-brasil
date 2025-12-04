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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3b9aa45-b1f0-3c0d-a66a-a2066cdccab3 | -5.95707 | -39.70634 | 2025-12-04 03:29:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 05233d39-e857-39f5-80aa-6fd47bfa7bc8 | -7.14743 | -35.16328 | 2025-12-04 03:29:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2ef5454e-4a03-372f-b10a-d3fabb7e4e60 | -4.39706 | -43.13337 | 2025-12-04 03:29:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3d74ec62-16cc-3c6b-bc2c-fb73a76900ca | -5.2453 | -37.70279 | 2025-12-04 03:29:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 90bf3ab6-501e-30e5-8dc5-aee8ab07f905 | -8.16044 | -43.17707 | 2025-12-04 03:29:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1ebc1ce8-766e-34e0-811e-2d180c72ab20 | -6.68015 | -39.50303 | 2025-12-04 03:29:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| bf798f65-6308-30da-9e38-36ef6c322ab6 | -5.00292 | -42.94522 | 2025-12-04 03:29:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cf20ef2-e730-3fea-bd8d-918eb4f9ff3c | -9.32881 | -36.95834 | 2025-12-04 03:29:00 | NOAA-20 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 47324aa7-2881-3599-b718-e31010e990bc | -6.42184 | -44.79664 | 2025-12-04 03:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5527fdf-c92f-346c-9319-e3d6cfebca0d | -5.34076 | -42.11519 | 2025-12-04 03:29:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b1fdbc72-9357-3772-b26d-9bb4d8183cb5 | -7.86261 | -38.72871 | 2025-12-04 03:29:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 509f247d-0f6d-3127-9f9f-284e946353a0 | -9.30525 | -35.63777 | 2025-12-04 03:29:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5998fe5e-f5fb-3498-95ba-bf9537d6c582 | -6.27477 | -35.2821 | 2025-12-04 03:29:00 | NOAA-20 | ESPÍRITO SANTO | RIO GRANDE DO NORTE | Brasil | 2403509 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ffef2066-e8a1-388f-ba9f-7c3160fb6347 | -7.14387 | -35.1627 | 2025-12-04 03:29:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ee117e59-4909-30c2-8a99-d705c09b11d3 | -4.39517 | -43.13639 | 2025-12-04 03:29:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 2128b0ca-1fc2-336d-ae5f-8dfc284887e0 | -6.43244 | -44.79883 | 2025-12-04 03:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7bd5e8cd-6a11-3295-84e4-0cd1f2655b10 | -6.42588 | -44.79725 | 2025-12-04 03:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7c92a90a-ac94-3da0-a964-6847d4ff0acc | -3.32377 | -44.38617 | 2025-12-04 03:29:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c61918b5-5d3d-30bb-a740-8f33e025bdf0 | -5.95564 | -39.70766 | 2025-12-04 03:29:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6ac2f41b-c96e-35de-821e-c3160fb4c8f4 | -5.33937 | -42.12303 | 2025-12-04 03:29:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 69469810-12e9-38e0-9728-45bba3cc1699 | -6.42073 | -44.80271 | 2025-12-04 03:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f0fb593-c084-3c51-875a-77f9a3f43137 | -6.00729 | -42.32873 | 2025-12-04 03:29:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 61a757fe-3922-37f8-a687-5e5493dc2bb8 | -4.50668 | -40.51167 | 2025-12-04 03:29:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a78f231c-3d45-3c3b-8cc4-a8ef5a8d1fc1 | -10.286 | -36.32348 | 2025-12-04 03:29:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3852c30e-b48e-3988-a3be-11eb6049cbb8 | -4.07312 | -43.70139 | 2025-12-04 03:29:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f70114f1-488e-3d7a-a0c8-01e7a597781f | -4.83111 | -43.20294 | 2025-12-04 03:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6137c3bd-d228-3ebd-9b02-5d0248f243c9 | -6.3245 | -39.82487 | 2025-12-04 03:29:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7d10cab3-72e0-3956-ae35-50baa0bad565 | -5.99111 | -35.38722 | 2025-12-04 03:29:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 220f702d-5cb4-36d5-a7dd-aa893b0ef459 | -6.21217 | -38.52657 | 2025-12-04 03:29:00 | NOAA-20 | SÃO MIGUEL | RIO GRANDE DO NORTE | Brasil | 2412500 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 252a45b3-429d-3b93-b5de-f04cb5aea064 | -5.85283 | -39.93599 | 2025-12-04 03:29:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 087ed2bc-f61b-3045-ba2e-9921a2cf5ec8 | -4.40325 | -43.13449 | 2025-12-04 03:29:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 0cb99884-27d9-3020-b20c-f306e4440e21 | -7.86193 | -38.73036 | 2025-12-04 03:29:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 60745f99-408a-3402-bbaf-9c49b4e9d6eb | -5.32748 | -43.56633 | 2025-12-04 03:29:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d633347b-6f85-3d26-9401-1b0d8451ab6b | -4.25992 | -44.1596 | 2025-12-04 03:29:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c6cfcfb-121f-32be-bf99-86901405defc | -4.40223 | -43.13263 | 2025-12-04 03:29:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 154af5b3-fb71-309f-ba8b-b48d702d1be6 | -4.38898 | -43.13528 | 2025-12-04 03:29:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b48a0086-6a33-30af-beb7-7962c940cc2f | -6.27909 | -35.27847 | 2025-12-04 03:29:00 | NOAA-20 | ESPÍRITO SANTO | RIO GRANDE DO NORTE | Brasil | 2403509 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a8a508fe-983a-328a-92ff-26df0d9833e9 | -4.38279 | -43.13418 | 2025-12-04 03:29:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dadec624-3cf1-3e78-83e4-4d73489caa42 | -5.00374 | -42.94059 | 2025-12-04 03:29:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b87a3c21-0e6d-3105-bf91-0a8224c1d1ea | -6.05683 | -43.75296 | 2025-12-04 03:29:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04c6b92f-edfe-3afb-ae67-bcbd48b60a2b | -3.66251 | -43.60936 | 2025-12-04 03:29:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93aca874-c4c5-3850-92d2-ab41c928334b | -7.14847 | -38.86283 | 2025-12-04 03:29:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| b9205aa3-479e-389d-ab54-414a03723224 | -5.34579 | -42.1201 | 2025-12-04 03:29:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 757d594b-98a3-3e87-a4f2-a0855eda85de | -4.63837 | -37.78744 | 2025-12-04 03:29:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bce345f2-23db-33f2-b725-f46d43f4fca8 | -3.32558 | -44.38553 | 2025-12-04 03:29:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc4460ba-225a-3750-bf04-13475e786e29 | -4.21157 | -44.25567 | 2025-12-04 03:29:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d2f370a-bdbf-31e0-95ff-5d6c79051319 | -7.61751 | -39.04434 | 2025-12-04 03:29:00 | NOAA-20 | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 27eb9355-e6c7-3013-bf44-6ef0fb998585 | -2.86124 | -45.25217 | 2025-12-04 03:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7bf0dea4-2f92-3fe0-bac9-fa5afb167513 | -4.38384 | -43.13599 | 2025-12-04 03:29:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3cf6653d-de51-3a47-9c18-e2b826154243 | -6.33461 | -41.40612 | 2025-12-04 03:29:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8e0d9312-00d8-3144-8910-4f1b84827557 | -9.30813 | -35.64246 | 2025-12-04 03:29:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 75353c98-c907-3ada-ade2-04e06fcf8a34 | -5.98746 | -35.38662 | 2025-12-04 03:29:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 111901fc-8db1-34ef-8c25-5df724f7579e | -4.58486 | -38.29733 | 2025-12-04 03:29:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f0759a54-f93d-3a0a-b4da-fa13aa216e25 | -4.50203 | -40.50737 | 2025-12-04 03:29:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7cc40896-c1c8-3712-b6e3-3510b0cee0ee | -4.39623 | -43.13824 | 2025-12-04 03:29:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 03c3d136-6b21-3fbb-b75d-e933a28bcaed | -9.59278 | -36.16452 | 2025-12-04 03:29:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ab248ebe-7bbe-3dc0-8e27-9c5f3c6b0b6d | -4.82494 | -43.20182 | 2025-12-04 03:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51a6f08b-36dd-3e28-b8ce-884e08858af1 | -9.32961 | -36.95353 | 2025-12-04 03:29:00 | NOAA-20 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5a7b72a0-6aa5-3202-890d-091ee6fca769 | -2.85408 | -45.25079 | 2025-12-04 03:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b2da756-d7bb-3e2f-82f4-a15a4d725eb3 | -7.86185 | -38.73302 | 2025-12-04 03:29:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 858e067d-fe6c-313b-97e4-e110b1526718 | -4.97503 | -37.47884 | 2025-12-04 03:29:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cd52060b-093c-3fc3-b66e-0c99a4b2a694 | -6.43351 | -44.79321 | 2025-12-04 03:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 32b05438-c19d-38ed-af03-141eff88b9bc | -5.97482 | -44.60503 | 2025-12-04 03:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd2d1b26-2979-325a-975e-4ce19547a65c | -6.42696 | -44.79155 | 2025-12-04 03:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 34782a17-733f-36c8-9ef4-aff7e4f16046 | -5.98244 | -44.60071 | 2025-12-04 03:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2e4df47-dd8b-38f7-bda9-fe4b9c6c4bb4 | -4.20834 | -44.2576 | 2025-12-04 03:29:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5281b22-1814-38dd-952c-9f96ef536a91 | -5.98811 | -40.37196 | 2025-12-04 03:29:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1bde6176-1a0b-3812-bdd6-79f0f57a59f7 | -6.05775 | -43.74783 | 2025-12-04 03:29:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 525be2cb-d216-309f-8b29-c58db3be09ac | -3.32274 | -44.39226 | 2025-12-04 03:29:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5d9ebdb-c6b1-3efe-8544-2f62580c4522 | -5.85374 | -39.93076 | 2025-12-04 03:29:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 89d63333-cb33-3270-b8ba-097e4d76690e | -6.3293 | -39.82592 | 2025-12-04 03:29:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 170ecbf7-1294-386c-bb45-dbf3d6ed00ac | -7.61674 | -39.04876 | 2025-12-04 03:29:00 | NOAA-20 | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1b0e1c8f-5889-340b-af34-ec8b4388ed62 | -8.16123 | -43.17283 | 2025-12-04 03:29:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| de811ad6-95b1-35a7-bd99-984ff139e9a2 | -6.2789 | -39.68868 | 2025-12-04 03:29:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d64db04e-c9b0-3713-b539-2b77ab590675 | -5.08922 | -37.54781 | 2025-12-04 03:29:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a859b6e1-a5e5-3223-a198-d34792764354 | -5.34648 | -42.11618 | 2025-12-04 03:29:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| da64e3c7-a8f2-399f-9329-4b746107c789 | -5.80969 | -35.57705 | 2025-12-04 03:29:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cdebeb66-11ed-3dd4-9d03-781006fb15bd | -9.30457 | -35.64186 | 2025-12-04 03:29:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1bf22796-f1e3-3edc-9694-5286e8ae9319 | -6.27931 | -39.68768 | 2025-12-04 03:29:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 16baf8c4-be1f-3aed-92df-705805d29646 | -8.16627 | -43.17818 | 2025-12-04 03:29:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ce70151f-9774-3da2-868a-7bede2f6c066 | -8.62547 | -37.00438 | 2025-12-04 03:29:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 42b885d9-d656-345b-8ee4-2d572e734bc1 | -5.02871 | -39.38398 | 2025-12-04 03:29:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d0198544-09bd-34c5-8bbd-f2d2acdd22e1 | -4.73737 | -44.43619 | 2025-12-04 03:29:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b89a459-8ebe-3290-88ab-77999be838e7 | -4.07405 | -43.69595 | 2025-12-04 03:29:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ae83f45-79e4-3cfb-9f5a-acbe3ed1f778 | -5.99213 | -40.37874 | 2025-12-04 03:29:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b055cd62-b137-3a6c-8a54-104a779f1a9f | -9.59282 | -36.16253 | 2025-12-04 03:29:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 299e4575-9f4c-3d7f-b562-f657cd202753 | -9.5935 | -36.16027 | 2025-12-04 03:29:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e1ee6faa-2c7b-37db-990e-933b610a0673 | -3.32451 | -44.3916 | 2025-12-04 03:29:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4001280-83b7-307e-b8ff-795e31b575ae | -5.18166 | -40.15926 | 2025-12-04 03:29:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fce601b7-02ae-305e-935e-2be3f3530a68 | -19.6442 | -56.8311 | 2025-12-04 03:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 108.9 |
| 6d0e3e56-e1b3-3b0f-b39d-f01859c92357 | -4.4079 | -43.1252 | 2025-12-04 03:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| fac037b1-943d-3ea4-a0f0-b05d19fb27ca | -2.5367 | -49.4618 | 2025-12-04 03:30:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 57e9d3ba-beca-3713-aed8-d0ee48feb29f | -19.6241 | -56.8339 | 2025-12-04 03:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 190.3 |
| c7f243fa-017d-375a-aa02-ac5b834160db | -19.6237 | -56.8549 | 2025-12-04 03:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 160.9 |
| a9d410c4-9c8d-3176-92a7-5b43a589f895 | -19.6438 | -56.8521 | 2025-12-04 03:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 94.4 |
| 3a6f7437-b7a7-3b93-8c95-4bc5da8047e2 | -3.7212 | -45.5859 | 2025-12-04 03:30:00 | GOES-19 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 8ca95fb1-c72d-360b-a34a-04592ab8aa6f | -13.00536 | -40.54892 | 2025-12-04 03:32:00 | NOAA-20 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 15f404f0-615c-38e7-869b-34b9f5854d23 | -15.45974 | -39.23628 | 2025-12-04 03:32:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a92d3836-5290-3c59-a5b2-66d23ed08dca | -15.46308 | -39.24062 | 2025-12-04 03:32:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5485487f-d2a8-3ee4-85be-bd2e44c40721 | -15.45576 | -39.23553 | 2025-12-04 03:32:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |


[Clique aqui para ver as próximas entradas](README6.md)
