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
| 01cf4ac4-f79f-350b-a4e3-7ae56701fcc7 | -18.4486 | -54.6674 | 2025-07-29 00:40:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 20e85a24-8de6-3092-a788-a81bc1fc6ede | -11.4393 | -45.1154 | 2025-07-29 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 4cb62524-0aa1-31ad-97b2-f5580d6ce411 | -7.9445 | -44.0918 | 2025-07-29 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 12ea5793-9784-391d-8ba1-296980bcef8f | -11.7317 | -48.1849 | 2025-07-29 00:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 8dc56429-a6ee-3867-ae2f-b3a0a2f92341 | -7.2408 | -43.0664 | 2025-07-29 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 240.7 |
| e9aef778-e010-3fae-807e-f7360b699711 | -5.363 | -45.2695 | 2025-07-29 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 086f5504-6b8d-380f-84e4-459410b93774 | -18.449 | -54.6462 | 2025-07-29 00:40:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 2bed2b67-52af-3802-b7ce-30bc2198b004 | -7.8568 | -46.7304 | 2025-07-29 00:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| a9d9c2ab-fa72-39ec-a4a6-3752413c7a59 | -2.8921 | -48.2977 | 2025-07-29 00:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 4a76ec8d-2db9-3d08-a932-86a5575cb0b5 | -7.2411 | -43.0428 | 2025-07-29 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| 1513cf95-ffa2-3f0d-ba58-a727c610ea3e | -7.9256 | -44.0937 | 2025-07-29 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| c034a919-0e0a-388e-8f37-98558a4e9b75 | -11.4393 | -45.1154 | 2025-07-29 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| b78b9819-4c04-31ba-a344-8733dea02c5f | -7.4728 | -49.4004 | 2025-07-29 00:50:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| c47aeb45-4e14-366f-84f2-03b27ab58f88 | -11.4201 | -45.1181 | 2025-07-29 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.0 |
| c378c060-e320-336f-88f2-d618325fdfd7 | -11.7317 | -48.1849 | 2025-07-29 00:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 6f1a67d3-ad38-3dbe-8f5c-3703339ae5d7 | -11.7508 | -48.1825 | 2025-07-29 00:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| efbf4bd9-220e-33f1-adb9-2631895c7d80 | -7.8568 | -46.7304 | 2025-07-29 00:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| ecb85373-500e-3d40-9434-868fba9d3675 | -7.4541 | -49.4018 | 2025-07-29 00:50:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 72d5225f-eb9b-337a-a774-d3890bd6712b | -7.2411 | -43.0428 | 2025-07-29 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| af663de4-d17c-3523-832b-77a2d65f39c1 | -7.2597 | -43.0645 | 2025-07-29 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.9 |
| f89b69b9-51cd-399c-9138-1af12299efa0 | -11.4389 | -45.1385 | 2025-07-29 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 3fd75482-dfc0-3519-a83b-bd33e9c524be | -7.2408 | -43.0664 | 2025-07-29 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 226.0 |
| 5c3097ac-b99b-3232-b4c2-cac746638c8c | -2.8921 | -48.2977 | 2025-07-29 00:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 3fdf620b-cdb6-3502-90da-22135a2876cf | -6.5074 | -56.213 | 2025-07-29 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 8ecdff10-8fe6-3a7c-8f7d-cf9860335c39 | -18.4486 | -54.6674 | 2025-07-29 00:50:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 66.8 |
| cee7ca3a-0831-381b-a1dd-5f3bdf9ed4b6 | -11.3434 | -51.2546 | 2025-07-29 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 995b28fe-bd08-3411-ab9c-6e427102531d | -7.9445 | -44.0918 | 2025-07-29 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| d3dea42c-4910-32c3-8a6e-730f3f9d7f93 | -7.2408 | -43.0664 | 2025-07-29 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 143.9 |
| 11701a5b-eec2-3cbf-bd57-04c2f6152851 | -11.4393 | -45.1154 | 2025-07-29 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| fa8636b5-20ff-3f5c-b8c6-dd539edfa867 | -7.9256 | -44.0937 | 2025-07-29 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 45687d35-9ced-3170-9da2-bc4a1de86bae | -2.8921 | -48.2977 | 2025-07-29 01:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 3a01c998-1bfe-3bdb-af52-80d870e903c0 | -11.4389 | -45.1385 | 2025-07-29 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 29337c1d-49a7-3613-b14d-005424a857d4 | -7.4541 | -49.4018 | 2025-07-29 01:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 3f3591f1-3eec-3988-97d1-1237df078876 | -7.2597 | -43.0645 | 2025-07-29 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 117.1 |
| 61945562-d8c3-3c9f-96e2-8b22a86e6547 | -7.8568 | -46.7304 | 2025-07-29 01:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| ff2c0169-1b17-36a6-b514-ff4b788ee1d8 | -7.9445 | -44.0918 | 2025-07-29 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 3496e3e4-c2ac-3e01-83e9-94bec9c5a043 | -11.7508 | -48.1825 | 2025-07-29 01:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 28cb2d60-10eb-36ca-a72a-1d390db40121 | -11.7317 | -48.1849 | 2025-07-29 01:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| aaabbd88-d41b-3709-b7a2-6d9cae8e7405 | -7.2411 | -43.0428 | 2025-07-29 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| bb858997-5f4d-3e79-8bac-6d1be3712e20 | -2.9106 | -48.2971 | 2025-07-29 01:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 5b0fa50e-e973-359a-bd35-34d617d1f887 | -7.2599 | -43.041 | 2025-07-29 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 50.9 |
| c5b1264e-dc3a-36f5-a677-defa25bf40a7 | -6.5074 | -56.213 | 2025-07-29 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 2d395a52-1bc3-3432-8710-4da23e88219f | -7.9445 | -44.0918 | 2025-07-29 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 085ff5c8-7345-369c-b116-1a58dd3b374a | -11.7317 | -48.1849 | 2025-07-29 01:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 8df6de26-7d36-35aa-af42-4f6cc2ccbfd6 | -7.4541 | -49.4018 | 2025-07-29 01:10:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 425aebe2-74f6-3420-91ec-fea93c976a8b | -7.8568 | -46.7304 | 2025-07-29 01:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| a5294f63-6fb3-3d08-9fb5-aa10aeeefa01 | -7.9256 | -44.0937 | 2025-07-29 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 1d6fa8b2-d204-3f5a-b579-00138b7b20e6 | -7.2597 | -43.0645 | 2025-07-29 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| e5a3a37f-6c65-35d7-8eac-81d347b26b32 | -18.449 | -54.6462 | 2025-07-29 01:10:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 19e03b1b-b215-3f63-8398-6193fcb24787 | -7.2408 | -43.0664 | 2025-07-29 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| 65b7d328-fbd1-337c-9765-5c353a2cc263 | -11.4393 | -45.1154 | 2025-07-29 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 15b6bef5-2250-3e76-a113-7dd86aa9fc97 | -11.7508 | -48.1825 | 2025-07-29 01:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 8e671ec5-31be-3879-b5db-40fe0b7e0306 | -2.8921 | -48.2977 | 2025-07-29 01:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 2743ad95-e87f-31c8-a0a7-4c3a7e62a99a | -11.4389 | -45.1385 | 2025-07-29 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.9 |
| c61cdf2c-55ab-3797-ba86-c2ddc3735caa | -11.4201 | -45.1181 | 2025-07-29 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| d9004814-c06a-3b33-84ab-e4e7f3b7b498 | -6.5074 | -56.213 | 2025-07-29 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 31b7a107-c5f7-3503-a5c5-ca87e502c700 | -18.4486 | -54.6674 | 2025-07-29 01:10:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 7e42fd96-d1c7-30e0-8b90-7b9354f6948e | -7.9256 | -44.0937 | 2025-07-29 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 37f94d3f-8616-3b70-a7a7-f5f6ecc9dded | -18.449 | -54.6462 | 2025-07-29 01:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 6c3ec0c1-803f-3e67-9114-5e026576ca0e | -18.4486 | -54.6674 | 2025-07-29 01:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 041ba42b-87ae-38bd-855b-cf1e2611e5bb | -7.8568 | -46.7304 | 2025-07-29 01:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 1fb5b971-3f24-3891-8126-9befaf7aaa2c | -11.4389 | -45.1385 | 2025-07-29 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 0ef8e889-d149-3d4c-8898-0872e342fb5d | -11.4201 | -45.1181 | 2025-07-29 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 616fe3be-7def-3be7-92ef-a75fda72193c | -7.4541 | -49.4018 | 2025-07-29 01:20:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 11c5d3f8-9556-3335-b569-3100e9630164 | -7.9445 | -44.0918 | 2025-07-29 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 77ddeedd-81af-3707-81da-e60bac1b2cc9 | -11.7508 | -48.1825 | 2025-07-29 01:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| c5fd98cd-a669-3fd5-9d17-c2245675e6f1 | -11.4393 | -45.1154 | 2025-07-29 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 4865ae8b-8eaa-32ab-a2a5-e39eccd98079 | -6.5074 | -56.213 | 2025-07-29 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 7ce3d46d-3179-385d-812d-fa7dc2965bf2 | -18.4685 | -54.6645 | 2025-07-29 01:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 43c97116-4608-3c03-9a34-d749a99f3852 | -11.7317 | -48.1849 | 2025-07-29 01:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| a8ee0a78-711b-3d3c-8316-f1c81a3036e9 | -11.7508 | -48.1825 | 2025-07-29 01:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 239c7dd8-d44e-3e99-9142-afb0bed02742 | -7.2597 | -43.0645 | 2025-07-29 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| f334dc26-0860-3f3f-aaae-1964125c67e8 | -17.0544 | -43.776 | 2025-07-29 01:30:00 | GOES-19 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 2fae8305-687b-3a44-9a4f-b6652afb5ed6 | -11.4201 | -45.1181 | 2025-07-29 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| bbb52dc7-af52-3c4b-a624-e1f94f7be865 | -7.2408 | -43.0664 | 2025-07-29 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| 32e30b5f-90c5-3c80-a1ed-d0cecd2bad00 | -11.4393 | -45.1154 | 2025-07-29 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| e7dbfd15-b989-336d-8b0c-d884e813c8a8 | -11.4389 | -45.1385 | 2025-07-29 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 8e76478c-bcd3-35ce-89bf-033718c45d99 | -7.2411 | -43.0428 | 2025-07-29 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 41.1 |
| 3d44f951-341e-3896-9e38-ca4ff2429917 | -11.7317 | -48.1849 | 2025-07-29 01:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| b33a032c-1b99-373c-9320-29a73a7fd149 | -7.4541 | -49.4018 | 2025-07-29 01:30:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| c5d8a0ef-0c53-356a-8047-968061c0cbc4 | -11.7508 | -48.1825 | 2025-07-29 01:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 37dbc2d1-a4a3-3e99-8025-b3d4fb74641d | -7.9445 | -44.0918 | 2025-07-29 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 239309fa-65d3-3931-bda4-7cb047626a8d | -11.7317 | -48.1849 | 2025-07-29 01:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 82714d2e-23aa-3235-b26c-d52d6a26d2ce | -18.4486 | -54.6674 | 2025-07-29 01:40:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 0b4b4b4c-2ee0-330f-8ec5-bc762a0384ba | -11.4201 | -45.1181 | 2025-07-29 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 0d24dfed-47a5-3c7f-8c81-23ea69dac9b8 | -11.4393 | -45.1154 | 2025-07-29 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 3101026f-769d-3eb3-a62e-1b9ee83664f2 | -18.4287 | -54.6704 | 2025-07-29 01:40:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 59.8 |
| ccea1c98-76fb-3ddb-b366-fee22b8e7476 | -11.4389 | -45.1385 | 2025-07-29 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 4fc054d3-c0d8-38c5-b31a-53f519eb4012 | -18.45016 | -54.653 | 2025-07-29 01:41:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 75.1 |
| b3fa84b4-d5ec-355c-9131-d4a8d108fd4f | -18.43881 | -54.68032 | 2025-07-29 01:41:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 690f3853-0c57-3ae7-b745-5abd4c1bf410 | -18.44786 | -54.64678 | 2025-07-29 01:41:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 53.8 |
| d22654e4-8052-37aa-9c11-80362217310c | -18.4558 | -54.68329 | 2025-07-29 01:41:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 5beb82db-7de0-371d-af47-a8c736b957c3 | -18.43519 | -54.65622 | 2025-07-29 01:41:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 1b3315c8-e9f2-3bc3-821f-89a14c454d15 | -18.45371 | -54.67696 | 2025-07-29 01:41:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 84eb01eb-d75c-3097-af1b-3d5011040b20 | -18.44092 | -54.68677 | 2025-07-29 01:41:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 38defff7-ed22-3993-88d4-d9b7e989d699 | -14.40658 | -59.33356 | 2025-07-29 01:43:00 | TERRA_M-M | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 32.4 |
| fcb4098e-306f-3723-b985-aaf36eb7c950 | -14.40399 | -59.31774 | 2025-07-29 01:43:00 | TERRA_M-M | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 30a21842-c4c8-37cc-b095-8bf4f4d145fa | -6.50197 | -56.22582 | 2025-07-29 01:47:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 644bd669-cf00-3e23-b4b6-cc0681f51174 | -6.49799 | -56.23181 | 2025-07-29 01:47:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 51623a90-891c-36e9-9e35-423643af02be | -11.4201 | -45.1181 | 2025-07-29 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |


[Clique aqui para ver as próximas entradas](README6.md)
