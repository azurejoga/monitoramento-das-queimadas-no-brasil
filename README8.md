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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84352b16-9975-33c4-8f47-9738960a8581 | -3.13894 | -44.43692 | 2025-10-21 03:51:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d314085-e49a-313a-9bf6-f8694576165f | -2.85482 | -50.74232 | 2025-10-21 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2c9b369a-aa68-35c5-b8e1-c7bc980c4e95 | -3.50238 | -45.83709 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8256690f-f859-3a10-966c-a8dcdb4cf3aa | -3.22436 | -46.78527 | 2025-10-21 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 344153c5-de64-3d28-aea0-f71820a38328 | -2.87206 | -50.72041 | 2025-10-21 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5b2d5952-b9b1-3686-b0f8-f50e7db0e874 | -3.50028 | -45.81873 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 599b8dbe-c874-3940-beac-49b7f7abe4e1 | -2.25963 | -47.88051 | 2025-10-21 03:51:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5c7487df-44e5-37d3-a657-e553af6cff2a | -2.92382 | -48.30363 | 2025-10-21 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5dd15222-b286-3b8c-8c42-6c9edfb67c33 | -3.50189 | -45.84005 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99670918-50be-3901-b42e-701debfa3eef | -2.72001 | -48.83433 | 2025-10-21 03:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d73d79f5-c0f9-3b14-ac1e-23404f216b08 | -4.42958 | -40.17749 | 2025-10-21 03:51:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2aa67eca-6b3b-30a8-b1cf-144defb927c6 | -3.58665 | -38.82463 | 2025-10-21 03:51:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 033777b1-9e91-3e50-b2c7-cf06cd72bdd9 | -2.86174 | -50.73868 | 2025-10-21 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01a9622f-957a-3225-8d87-2aa580d96437 | -3.58938 | -43.04496 | 2025-10-21 03:51:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6f4329f8-9b2f-3ced-8928-3ee55df547c3 | -3.421 | -43.16738 | 2025-10-21 03:51:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac362ecd-025b-39cc-890b-f257da4491c0 | -1.19188 | -49.08482 | 2025-10-21 03:51:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 53697e41-3601-30f6-9635-5cee7aa33b1b | -2.78832 | -49.62393 | 2025-10-21 03:51:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1f19a7b-88e1-361a-8504-8537684f798c | -2.719 | -48.3459 | 2025-10-21 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76d34c8d-0816-3fa7-b2c9-02580a7993c8 | -3.4928 | -45.83243 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8e873905-62b5-3d0c-9d69-5a8d3ec6d3d7 | -2.71506 | -48.3425 | 2025-10-21 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 788271ff-8b88-3406-81fb-3c33713d27f1 | -1.19989 | -49.08078 | 2025-10-21 03:51:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0ab2a45e-fb6d-30f2-90f8-22982d38f7b1 | -2.55142 | -47.66112 | 2025-10-21 03:51:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 876b6965-164f-3843-beb9-5b84b4f6da90 | -4.25921 | -40.28769 | 2025-10-21 03:51:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c804c2a7-7ea4-3318-922b-b21dbbf37dde | -1.199 | -49.08611 | 2025-10-21 03:51:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ada6ec49-2cf1-3796-b1fc-043caa4f6697 | -3.22494 | -46.78183 | 2025-10-21 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8ab83411-ad56-30c8-87ac-91c27f2f19fd | -2.71921 | -48.83919 | 2025-10-21 03:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 30d0a017-059e-3e00-acf5-71e1a5422166 | -4.25991 | -40.28683 | 2025-10-21 03:51:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ee7e78a8-e4a6-36e7-9f3b-da41795d918c | -4.81379 | -42.75692 | 2025-10-21 03:51:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5174f5ab-527e-3783-bd48-551f24971396 | -3.85551 | -48.96468 | 2025-10-21 03:51:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b612deb8-8c63-33bf-b73a-f7dc54786925 | -2.71759 | -48.83958 | 2025-10-21 03:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f27c27a8-7858-3055-962d-0cc0135a2e80 | -2.86061 | -50.74519 | 2025-10-21 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2593ad5e-6a8b-34f9-8321-25f51e05771e | -3.5877 | -43.0455 | 2025-10-21 03:51:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c22efa01-1cd3-34e2-83d8-addb37d72695 | -2.85591 | -50.73584 | 2025-10-21 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 05a653be-47b3-3ba5-8c47-420f1d71a63c | -2.86285 | -50.73705 | 2025-10-21 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18e7a614-016d-3aa4-877c-c462fbe78bdb | -4.15719 | -38.14042 | 2025-10-21 03:51:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c1c765fc-a5e7-386a-8b01-50ef215dc7f8 | -4.42547 | -40.18077 | 2025-10-21 03:51:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bfefbc7d-7672-397d-a240-fc587919ee0b | -2.92903 | -48.30912 | 2025-10-21 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 6a849f17-877c-3099-a84a-899ddef46d37 | -3.49685 | -45.83918 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 107b2e71-a05a-35e5-a313-70d6a6d0b7a8 | -3.50386 | -45.82825 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d886b8e7-fc89-3881-9ee9-b6330b640074 | -4.1587 | -44.55286 | 2025-10-21 03:51:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ff7c76f-9bbc-3fd5-a203-3ce1974ea3cc | -4.56833 | -44.6356 | 2025-10-21 03:51:00 | NOAA-20 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bee22365-e3d0-3dd5-bc9e-6822af92775f | -2.2574 | -47.8838 | 2025-10-21 03:51:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| e02b3ab7-8e2e-3ddf-b106-fe1821d2b8c1 | -2.98829 | -39.96724 | 2025-10-21 03:51:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fff03316-c488-3e87-80f6-1161d8c43840 | -1.19255 | -49.08503 | 2025-10-21 03:51:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fb26901b-686e-3866-bc82-47f4ea679f81 | -3.50435 | -45.82537 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 8c81884f-cb59-3695-8607-ebdf45b3da7a | -4.3933 | -43.31756 | 2025-10-21 03:51:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfd115dc-fb8b-3539-8c50-3b2672d7121f | -2.86612 | -50.71747 | 2025-10-21 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d635e50f-eb77-3a17-93e8-6e06b2f7755b | -2.86176 | -50.74356 | 2025-10-21 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1e9aa14-5daf-31bd-9536-429fc3ccc8d9 | -2.87195 | -50.72532 | 2025-10-21 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8249490e-f817-3b2b-8f67-2da9d85afdb7 | -1.7587 | -47.26619 | 2025-10-21 03:51:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c523173c-b73d-31a6-b3ad-a0679b55ef92 | -3.22378 | -46.78872 | 2025-10-21 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 944f6c20-2311-3cef-9fd7-80adb0237982 | -2.25894 | -47.88473 | 2025-10-21 03:51:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e7863061-b439-3b98-8c43-e4261492df8a | -2.86066 | -50.75014 | 2025-10-21 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1690c3f-6c6d-374e-865e-e8d3aed923b7 | -3.44919 | -41.85053 | 2025-10-21 03:51:00 | NOAA-20 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e8d8b846-ae2d-305e-b703-a229f539f79e | -3.49882 | -45.82742 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 3ff8667e-d7a5-39c8-80ab-677bfcd71ef5 | -3.32562 | -50.22545 | 2025-10-21 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b8f36d83-3141-30c6-ac31-98b21fc8ab9d | -3.5058 | -45.81669 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 428c1990-0ce8-3694-bb75-0b0692d328d2 | -4.81837 | -42.75405 | 2025-10-21 03:51:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7b20392e-ae5e-340f-b7e3-2c1569a2fd70 | -2.8548 | -50.73751 | 2025-10-21 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56ba0a88-d54d-3595-a893-07385d6087f0 | -3.9726 | -48.07011 | 2025-10-21 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe2c57c6-ec1a-3c48-b699-8a117fb33a34 | -3.30077 | -43.49859 | 2025-10-21 03:51:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42be5b25-1b43-3468-a635-1aefa1fc3cd2 | -2.76981 | -48.02324 | 2025-10-21 03:51:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2ac8c44b-6fff-3700-8b6d-bd70686c2026 | -3.49526 | -45.81785 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ead4faba-9d86-398d-a25e-0578538b4cc8 | -2.71428 | -48.347 | 2025-10-21 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e46d23d5-02fa-3fb3-acd2-fa7acab78856 | -5.38723 | -36.88639 | 2025-10-21 03:51:00 | NOAA-20 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9e95f4cd-a0c8-37ad-bc9c-2c71366fd01f | -4.18484 | -44.20256 | 2025-10-21 03:51:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 539e8250-25cf-34ce-8439-1de08734677c | -2.87092 | -50.72698 | 2025-10-21 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5ddeef30-7752-36b0-ab06-db3fcbc41a76 | -2.9298 | -48.30466 | 2025-10-21 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 05f53ffa-cb4b-3191-94b3-3bace6bee8a8 | -2.77147 | -48.0256 | 2025-10-21 03:51:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a7d60031-786a-3278-821c-cbd5729d67e6 | -2.87086 | -50.73182 | 2025-10-21 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2f8102d-0a71-3133-92f7-a83dc71773a5 | -3.84935 | -48.96362 | 2025-10-21 03:51:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52188877-8429-3050-baf6-af0eb1f873be | -3.5988 | -48.99092 | 2025-10-21 03:51:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44eee10c-b3c5-3835-a247-5938415b62c3 | -3.50483 | -45.82246 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 706d39b0-0004-3796-8790-2b4d2dc95ad5 | -2.25812 | -47.87959 | 2025-10-21 03:51:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 41b2f754-76ec-346e-9529-3e14f5e2fb09 | -3.50532 | -45.81957 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f51367ee-ae93-309e-8aef-b0f5af3d7357 | -6.64632 | -43.43698 | 2025-10-21 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4bb4db15-070c-38e7-b914-ce053df90434 | -8.11782 | -41.18724 | 2025-10-21 03:53:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| de98c696-32a1-3d04-b6e5-5c34b8a6f39d | -6.64693 | -43.43335 | 2025-10-21 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a588256-e9d9-3256-bfcc-41e90cec57ad | -6.9086 | -43.58996 | 2025-10-21 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 83211b26-830c-3137-85e6-89c685ad7b50 | -5.43908 | -41.07476 | 2025-10-21 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2b354902-cd83-3a31-984c-21f2fb0f10f2 | -6.96988 | -43.76771 | 2025-10-21 03:53:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e553c1c1-2210-3178-8734-3eaa68c57d6c | -4.24846 | -50.01248 | 2025-10-21 03:53:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c8134f0-11b4-39c5-8971-6c1e99b9ec5f | -5.54051 | -41.34512 | 2025-10-21 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4a8cb2bd-2b59-3845-9066-599ea650789d | -6.89918 | -43.59587 | 2025-10-21 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d84acc5-3c7d-3ab4-a005-1cc86385316b | -5.66585 | -49.79701 | 2025-10-21 03:53:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dac53427-db42-3f11-832b-2d476cbc00c3 | -5.83618 | -40.82267 | 2025-10-21 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 44370a97-96b0-3858-9f6f-a90926a7323b | -6.90451 | -43.58928 | 2025-10-21 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 56742a43-ce98-3692-b9fd-3904a1faacaa | -4.49395 | -46.47805 | 2025-10-21 03:53:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17163413-95ef-3e6f-957c-72b19488f61f | -5.26969 | -50.24098 | 2025-10-21 03:53:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ff26cac-dfd0-3ed7-b03a-86eccfc891d3 | -8.06081 | -41.05234 | 2025-10-21 03:53:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f3cd2e01-fd87-3ca2-b23f-d39edbc4668f | -6.65099 | -43.43407 | 2025-10-21 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0300712e-68a0-348c-9b4f-11480ce8270b | -6.89067 | -43.6211 | 2025-10-21 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38502f2d-f032-3718-9908-553d54430942 | -6.58012 | -47.54017 | 2025-10-21 03:53:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a77c7b57-4a6c-3180-9636-cd9ff397e60f | -4.65164 | -48.69662 | 2025-10-21 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38bd4e44-8e46-35c4-9b27-7fd43b2e920b | -5.43801 | -41.07167 | 2025-10-21 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b4a03433-0eba-31d3-afe8-e876db34821c | -6.15195 | -43.22252 | 2025-10-21 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ba6f7004-58b7-301a-9cd5-6cedf9ebcae0 | -4.74667 | -44.43718 | 2025-10-21 03:53:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 46292fa0-bfa5-3f58-8cfe-ea0a77cd741d | -4.73769 | -44.43573 | 2025-10-21 03:53:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 299988d7-cae7-3977-bc4f-0ae8e5ac7f1f | -8.20675 | -35.89169 | 2025-10-21 03:53:00 | NOAA-20 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 12bfda7a-beff-3736-a6b9-76dede2fb4c6 | -6.8998 | -43.59223 | 2025-10-21 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README9.md)
