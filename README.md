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
| 13e64fc0-8531-3553-a9a3-5f3bd01654bd | -7.0755 | -44.3836 | 2025-04-30 00:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 0864ddb3-ff06-33e1-8bc6-70e1da545434 | -8.9434 | -44.2373 | 2025-04-30 00:00:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 14e2f8f7-748b-3eb0-8d98-9a0ba415788e | -8.9434 | -44.2373 | 2025-04-30 00:10:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 53.8 |
| b0ddd5f2-6639-329d-b0c2-8733d0b3143c | -7.0755 | -44.3836 | 2025-04-30 00:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 114b646c-3683-30e1-8c00-8037e23a8880 | -11.39446 | -52.94706 | 2025-04-30 01:30:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 9e252254-f04b-3164-a17b-7e7265443c30 | -12.68302 | -58.08472 | 2025-04-30 01:30:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0022a7c5-bf24-33ab-b31e-0b92742b5f6d | -12.68437 | -58.09412 | 2025-04-30 01:30:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b8591d5b-2688-3348-ac75-0e6e2cf33e4d | -12.66633 | -58.09689 | 2025-04-30 01:30:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 3a7a537d-8a82-3fca-ad52-5db7642e4f68 | -12.66497 | -58.08751 | 2025-04-30 01:30:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 73be5dd9-ab61-368f-a4ea-92db7574c329 | -9.933 | -37.1939 | 2025-04-30 02:00:00 | GOES-19 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 82.4 |
| 2836549e-8a90-3704-8eb3-d44a2c4393a2 | -9.93485 | -37.18698 | 2025-04-30 02:53:00 | NPP-375D | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 7.1 |
| bbb90bcd-e643-34df-98b4-5faab3fc3fdf | -9.93351 | -37.19347 | 2025-04-30 02:53:00 | NPP-375D | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 7.1 |
| c660137c-732e-394b-970d-a8be23a92569 | -9.61717 | -37.03609 | 2025-04-30 02:53:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 3.3 |
| efca14fb-9ae3-368b-92fe-365f64d9f7d8 | -9.9371 | -37.19594 | 2025-04-30 02:53:00 | NPP-375D | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b0874ecb-7106-31d0-bf4d-58703d18554b | -9.93842 | -37.18933 | 2025-04-30 02:53:00 | NPP-375D | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 935a2b72-a8d7-3dbf-babd-9f22720caca6 | -9.93019 | -37.19379 | 2025-04-30 02:53:00 | NPP-375D | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 41150088-ec50-3f3b-9647-66e632eee028 | -9.93148 | -37.18731 | 2025-04-30 02:53:00 | NPP-375D | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 5.2 |
| a6e986ff-f453-3171-a4ac-edb0b2773a94 | -9.61578 | -37.04284 | 2025-04-30 02:53:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4572581d-9e73-3c08-aeda-4c609cb1df0c | -6.87975 | -35.02852 | 2025-04-30 03:13:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| c3c6a836-67be-3a4b-9355-881737c5e068 | -5.65883 | -35.75545 | 2025-04-30 03:13:00 | NOAA-20 | BENTO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2401602 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 052c500a-4b84-35ec-b90c-5c738bef690c | -6.87904 | -35.03269 | 2025-04-30 03:13:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 176e99c8-0f73-3ee5-8cb9-b211ecfdb768 | -6.88409 | -35.02928 | 2025-04-30 03:13:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| e7479745-7b01-3e74-8f2d-f4cc8d977261 | -12.69997 | -40.17862 | 2025-04-30 03:15:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9c24f5be-c133-3173-b928-7ec7e2fd322a | -9.93347 | -37.19596 | 2025-04-30 03:15:00 | NOAA-20 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 04fb6647-e127-32ad-ae5f-7e9cd096f8cc | -13.27757 | -39.87751 | 2025-04-30 03:15:00 | NOAA-20 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 0628fd01-d759-3f65-9393-48a1e17bf815 | -9.61699 | -37.04105 | 2025-04-30 03:15:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 1c4f6913-f3e5-3171-a95b-dfa8fb6abd7e | -8.07279 | -34.97723 | 2025-04-30 03:15:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 24c02bb0-2854-386f-88f1-939c08e10899 | -9.36193 | -35.82972 | 2025-04-30 03:15:00 | NOAA-20 | MESSIAS | ALAGOAS | Brasil | 2705200 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 034dede8-8ef2-3670-87c4-ecfc506b8568 | -9.9344 | -37.19088 | 2025-04-30 03:15:00 | NOAA-20 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 04db761e-f2a3-3f74-82fb-548fded6b9a1 | -12.69923 | -40.18232 | 2025-04-30 03:15:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b25954d1-39b4-392d-b179-9290e21934a8 | -13.27268 | -39.87402 | 2025-04-30 03:15:00 | NOAA-20 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c8ecd1fa-c57b-38c6-963e-7d75115ed1ee | -9.92967 | -37.18983 | 2025-04-30 03:15:00 | NOAA-20 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 18c0997e-a787-3d5e-a7e9-6ec5ce6d4d5c | -13.2782 | -39.87429 | 2025-04-30 03:15:00 | NOAA-20 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 3febbd2b-f9d1-3ab6-af04-d11c31c62862 | -9.61681 | -37.03855 | 2025-04-30 03:15:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 5.1 |
| cb21613a-879a-3db1-b662-6f12e26e10f8 | -9.92874 | -37.19489 | 2025-04-30 03:15:00 | NOAA-20 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c7f065ca-300c-3ffd-945f-f13dbd43b347 | -5.79265 | -43.61689 | 2025-04-30 04:06:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7209b920-cdb1-35a3-a390-4459431473d9 | -5.35237 | -38.72924 | 2025-04-30 04:06:00 | NOAA-21 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| fa5b6216-e195-3943-b5db-49ccca29729c | -6.30609 | -38.91165 | 2025-04-30 04:06:00 | NOAA-21 | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 751a5ac0-a401-3cdc-9252-4e80f56520e6 | -5.83011 | -44.44151 | 2025-04-30 04:06:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d186336b-ba99-3881-868f-854ca9b8d72e | -5.83079 | -44.43734 | 2025-04-30 04:06:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4574396-5519-366d-a313-7d59b37d25dd | -6.62759 | -44.67828 | 2025-04-30 04:06:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb433f22-96b6-399f-a72f-9d8c62aab82d | -6.20803 | -42.17858 | 2025-04-30 04:06:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ac01d5a8-f3c4-38f9-a132-c7ae59f65416 | -5.83439 | -44.43795 | 2025-04-30 04:06:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf7a6260-323e-30c3-ac2c-1f22e691a925 | -8.07386 | -34.97773 | 2025-04-30 04:06:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b30fe6f3-a6a2-3546-84d8-ce86be09ec02 | -4.90424 | -37.41408 | 2025-04-30 04:06:00 | NOAA-21 | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 490fba94-4763-368d-a683-dbb67d67d68e | -5.8337 | -44.44213 | 2025-04-30 04:06:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29e9f907-adbf-3931-bca4-20340cc6321b | -5.79325 | -43.61309 | 2025-04-30 04:06:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be66e56f-130f-3a9f-94ca-79e34b912d9f | -5.65974 | -35.75761 | 2025-04-30 04:06:00 | NOAA-21 | BENTO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2401602 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ce9a55d2-4da7-3a7d-9ba5-e1444d13c2f4 | -5.42036 | -43.19875 | 2025-04-30 04:06:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dfc961e3-13ab-3aee-9354-a8b30267d448 | -5.66029 | -35.75381 | 2025-04-30 04:06:00 | NOAA-21 | BENTO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2401602 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cf7ca8c7-b2e1-37de-84aa-13abd41bf0f0 | -5.77598 | -42.58329 | 2025-04-30 04:06:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 57dce451-1cdb-3b73-a9ad-08c1eae9b2b0 | -4.82121 | -47.32367 | 2025-04-30 04:06:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f195ae1-1717-33fe-9fde-b0cfcd0ce40d | -8.90285 | -44.78577 | 2025-04-30 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 90421267-29db-310e-a169-da5781f7c6ff | -7.08533 | -44.37959 | 2025-04-30 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4d89013e-4460-3588-9fc9-cdff21c94e14 | -12.10581 | -51.39565 | 2025-04-30 04:08:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79ef8bde-967b-3502-900f-4f149fea84cf | -7.07054 | -44.3812 | 2025-04-30 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5217308-248c-31f2-bca8-7d2d43bd1e0c | -13.3523 | -44.60109 | 2025-04-30 04:08:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03ca1458-bfe3-3e02-8e30-a0d9e4a9a99c | -7.08597 | -44.37563 | 2025-04-30 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 23d48169-f2ca-3e13-9427-23a8c8f3d6d9 | -7.07213 | -44.39381 | 2025-04-30 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1c8e9ea6-30f7-3fc9-aa8d-2e313cc9d58f | -11.40334 | -52.95395 | 2025-04-30 04:08:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9da0f1d2-d749-3261-99e9-200817780733 | -8.55487 | -40.84633 | 2025-04-30 04:08:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 10cb501e-d0f4-3526-a44d-4e03ed766708 | -12.10522 | -51.3987 | 2025-04-30 04:08:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3604355c-db22-3a4c-97d4-379af0d34092 | -9.6177 | -37.04013 | 2025-04-30 04:08:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 8e14dbb1-1836-3140-9895-639edac8857f | -12.10404 | -51.40486 | 2025-04-30 04:08:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e93e27ae-f86e-32e8-a9a3-3fd7e61e2764 | -9.93258 | -37.19405 | 2025-04-30 04:08:00 | NOAA-21 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 8.2 |
| b0be9203-35c8-358b-83b6-be3bff1b071e | -11.80123 | -47.37238 | 2025-04-30 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db3c3fb2-dcac-333d-8e45-1ce05fc659cb | -10.22089 | -39.50375 | 2025-04-30 04:08:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 94d72663-b33f-36f6-92b4-5363f66fad38 | -11.40489 | -52.946 | 2025-04-30 04:08:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5f27a0a-1274-35e3-9493-1af5d2f554b2 | -9.61113 | -37.02824 | 2025-04-30 04:08:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7256df8c-88a9-3ab0-9d50-1f42469e6f50 | -7.07278 | -44.38977 | 2025-04-30 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1d98ed51-5ef9-3d6b-8b9a-8601f920898f | -8.94548 | -44.2347 | 2025-04-30 04:08:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c01f4bb5-4036-3e06-b5e1-15983e7cda7d | -11.79731 | -47.37173 | 2025-04-30 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 98c265a9-2320-3721-87c6-b73a1c4a5621 | -7.08469 | -44.38356 | 2025-04-30 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3dbcb1b3-2079-31f3-949a-587025424cb5 | -11.80427 | -47.37817 | 2025-04-30 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 505d92b2-6296-319d-bbe3-77012e561446 | -11.80035 | -47.37749 | 2025-04-30 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f892cfff-f73e-3be8-ab12-dddb298f4380 | -8.94203 | -44.23415 | 2025-04-30 04:08:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d1cf7131-3585-3958-b8fd-bb4566577bde | -13.82448 | -42.69802 | 2025-04-30 04:08:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e0400e9d-fac5-3177-81e0-72680c158ceb | -11.40255 | -52.95801 | 2025-04-30 04:08:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6140a51a-5265-380e-987e-4e0f5aa469cd | -7.07567 | -44.39439 | 2025-04-30 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7e1879c0-6956-3ac4-8a9c-47efc0346d05 | -8.9461 | -44.23087 | 2025-04-30 04:08:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6251f40d-414d-3803-a484-5b75f2d63f2e | -7.07343 | -44.38576 | 2025-04-30 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8b48b7b6-a1a0-332c-9477-0955b7df6f6e | -8.90298 | -44.78542 | 2025-04-30 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e8e21a84-2b19-3842-adf1-cd3e9d09bdc1 | -8.47685 | -49.85713 | 2025-04-30 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 611f2d14-f551-3151-971f-2368dbd1cb71 | -9.9331 | -37.19045 | 2025-04-30 04:08:00 | NOAA-21 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 70772ad4-fff2-3759-b970-3f33838c869a | -7.07762 | -44.38238 | 2025-04-30 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 874cd66e-8a8e-3045-b0f4-6def8abaab62 | -11.40076 | -52.93702 | 2025-04-30 04:08:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77002e54-29be-3309-b499-269c2ac51f66 | -12.1729 | -40.32159 | 2025-04-30 04:08:00 | NOAA-21 | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7940cd1e-9b5e-3c59-a9c6-a4cfce6a70f4 | -7.06924 | -44.38919 | 2025-04-30 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16e9218b-5c0a-3607-bbbc-8f9f17343323 | -12.78028 | -38.49729 | 2025-04-30 04:08:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 5b3e5d83-741d-358c-83bb-7d8928487f94 | -13.82503 | -42.69448 | 2025-04-30 04:08:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 70512c26-cda2-3b1a-96b2-651452d2def5 | -11.79643 | -47.37682 | 2025-04-30 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 91ceb4a2-f661-3c47-b9c8-32bb7ff8c6a1 | -8.94265 | -44.23032 | 2025-04-30 04:08:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8b047227-fc2c-34b3-bafb-4029a5233c74 | -7.0818 | -44.37899 | 2025-04-30 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 73f4e76c-a965-3bc4-9b6f-c97643188017 | -9.61063 | -37.03184 | 2025-04-30 04:08:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 496ec0bf-9134-3136-ae05-f97074fa18a6 | -7.08115 | -44.38297 | 2025-04-30 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6bf2cc55-e29a-3a51-a9b4-bdc56ce8e37b | -8.47435 | -49.85835 | 2025-04-30 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a06bf576-ca1c-3ce6-9444-5093bd301206 | -8.94893 | -44.23526 | 2025-04-30 04:08:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e0791655-ed62-3fc3-afd3-ee71a27ff10f | -8.89932 | -44.78518 | 2025-04-30 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 89693420-646a-3f26-8244-9a9ec585875f | -8.95239 | -44.23581 | 2025-04-30 04:08:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3391eda7-f526-303d-8b11-b254ddd67ef3 | -21.23953 | -47.62091 | 2025-04-30 04:10:00 | NOAA-21 | SERRANA | SÃO PAULO | Brasil | 3551504 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README2.md)
