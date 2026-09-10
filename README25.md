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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bee6c2a-7ca4-38d0-9a46-8e47585c333e | -7.19928 | -43.63787 | 2026-09-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3cf7ab14-6f42-30b4-ab09-53b7c07d35a8 | -4.01891 | -50.44004 | 2026-09-10 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fc0a58e-c8c2-3d67-a4a7-e4ca90d22ee6 | -3.55086 | -48.18004 | 2026-09-10 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94b145bd-84b7-321d-91ea-3ba75be31c15 | -5.41498 | -41.83641 | 2026-09-10 04:25:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f1d74bdf-299f-39bb-9f91-22a0561aa97d | -8.31578 | -45.11597 | 2026-09-10 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be410cae-4359-320e-947e-6b83359edce1 | -7.0229 | -45.10846 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec323f74-f4fb-3374-9991-72d8e9b4c22b | -4.86281 | -47.4104 | 2026-09-10 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b08492d6-92bb-3f23-999c-54202dab90d2 | -7.19363 | -43.60748 | 2026-09-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 428196ca-133b-3f83-87c8-b37da7b7255f | -6.42918 | -43.06975 | 2026-09-10 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0cbe7820-b247-3a9e-8bf9-b019cf78bda4 | -7.59774 | -46.76267 | 2026-09-10 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61fdcac9-053a-3f64-ad1d-dac843b7a657 | -3.99899 | -51.03056 | 2026-09-10 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d95899b4-e859-30d2-b224-a0041127ffd0 | -6.8655 | -46.01261 | 2026-09-10 04:25:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05a2828a-e047-3074-b5c0-520ca3ae36d0 | -5.27874 | -55.96539 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39880b83-68ac-360c-a15f-2a7413acaf38 | -5.56363 | -45.33404 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1690db4d-2535-36d2-b82b-94fa34c246c6 | -6.42578 | -43.0692 | 2026-09-10 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5e6e2d9-a577-35d6-9df1-f07ddbff1c86 | -5.68173 | -43.39776 | 2026-09-10 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b7e9253-3efc-326a-8c8e-ee97c5878c16 | -5.60578 | -44.85448 | 2026-09-10 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f703808d-a6c3-3ec2-8660-9fd2225481d7 | -9.68279 | -43.44315 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f754435c-5e8a-3bd6-b08a-5d9f4063c5c5 | -5.92459 | -44.94405 | 2026-09-10 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 173611c0-a621-3f18-b873-28dd3a16ecfa | -8.24138 | -44.74703 | 2026-09-10 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5eaf4dd4-39ea-3821-983c-1c82ecbaa91e | -7.53784 | -45.0306 | 2026-09-10 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 306adcce-34c0-34ed-b231-643a37669087 | -4.85625 | -56.00462 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 185a4a12-bd7a-320e-ba46-66e74f202e57 | -5.76184 | -45.09147 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 593db44c-98ec-3729-970e-f0a54510959b | -8.75036 | -47.48419 | 2026-09-10 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87161e3c-cf15-396a-86d5-71e0126a7cd2 | -9.2998 | -44.36311 | 2026-09-10 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9cc7f4d6-77ee-35ab-9c90-0cedfa8aeceb | -5.12003 | -46.0081 | 2026-09-10 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c50c1247-9eaa-32da-9e2d-90c7e9844125 | -6.41896 | -43.06811 | 2026-09-10 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11beb9c2-ac42-34de-b906-dcdfe2d87a46 | -6.76075 | -45.47488 | 2026-09-10 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7806fbf2-1531-366c-a291-453f5659bd81 | -4.85231 | -56.02022 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e292e655-315c-3949-b756-0d85aebd608e | -5.62948 | -45.87678 | 2026-09-10 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af9f8126-8667-3251-b5a1-8075cc794e7d | -6.26104 | -53.11796 | 2026-09-10 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09c760a9-9bbe-3cab-924c-d96774ca7994 | -7.05548 | -42.71213 | 2026-09-10 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5c36e9b2-efb0-3484-8df5-c7bf2288ea37 | -7.51046 | -45.26785 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a831c404-cf0e-360f-bcd5-94c5789b2531 | -5.1017 | -46.94692 | 2026-09-10 04:25:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e3aae83-cf89-3015-9739-286b95d3e539 | -6.359 | -43.36547 | 2026-09-10 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0c4f4a6a-3c53-344f-9387-7ad3800fe0fc | -7.2077 | -43.62813 | 2026-09-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 313e8c1b-71c0-3027-8744-092f26932ed0 | -6.46203 | -46.28004 | 2026-09-10 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fd811d1-ea8c-3ae0-a5a6-30d0c33a336c | -6.2741 | -41.69798 | 2026-09-10 04:25:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aa408add-b622-3a54-b70e-28d50234b030 | -3.99973 | -51.02599 | 2026-09-10 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 055d7bf0-fba3-3d6a-9314-4440085b25a8 | -3.36826 | -50.74934 | 2026-09-10 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4c109ba-6991-3f51-8703-ba05a029f97d | -7.10098 | -42.13386 | 2026-09-10 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fd57bbdf-d713-38d9-b12d-2a0ba32a5aa4 | -5.92735 | -44.94803 | 2026-09-10 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 540fe92f-e3f4-3755-8b4b-7f5b54a91be0 | -5.7657 | -45.08853 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| d3f2d63d-07de-3002-94e1-a5cb521766e2 | -7.57736 | -45.6812 | 2026-09-10 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d9959d0-634b-349c-8ec5-4662d9680c0a | -6.23878 | -51.6785 | 2026-09-10 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f6e3e10-49f3-38f1-b187-bb3d220745f5 | -7.49226 | -45.27561 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15816680-6bcd-3e38-8b5e-54dc410b5a15 | -7.4884 | -45.27855 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7d19c07-e093-371e-a47d-9da28efa8120 | -2.94068 | -50.46665 | 2026-09-10 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d454c582-508b-3196-a15f-1788d047d466 | -2.55716 | -44.21948 | 2026-09-10 04:25:00 | NOAA-20 | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef8d2b10-8600-3262-a07c-16c788101d40 | -7.98175 | -43.97195 | 2026-09-10 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3c395ab4-701f-30bd-8184-ffb53e5a8351 | -8.57284 | -40.81347 | 2026-09-10 04:25:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5f2b31c9-a64d-3491-9125-7396323d0426 | -5.68565 | -43.3947 | 2026-09-10 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d64a7eb9-f3d5-3c3a-93a8-f49f14e6b9bb | -8.31909 | -45.11649 | 2026-09-10 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 124fee12-a5d8-374f-9a93-8b59e692d14e | -8.68661 | -47.98063 | 2026-09-10 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89310546-4722-3654-be05-e7dc97e7c99d | -9.68454 | -43.47854 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2f0427da-4111-3b5f-8595-d80c89917dfa | -5.59506 | -45.3709 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0963974b-fe6a-3575-aa0c-c7e3cf999ff0 | -2.73468 | -57.63002 | 2026-09-10 04:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 37e7dea6-b633-3b42-91ee-e3a3896f5461 | -5.76349 | -45.08109 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| ffd3060e-d50f-3769-b871-6b3b6ffea3e4 | -4.85367 | -56.01949 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 72843e55-ec41-3f38-87da-041a4182338f | -7.48509 | -45.27802 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 967cfb1e-23c0-3fab-b070-3a920f389fdd | -5.80601 | -43.80163 | 2026-09-10 04:25:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fec2d549-b5c0-3cd2-9f4d-ea5705dec016 | -7.9789 | -43.94578 | 2026-09-10 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3936ab79-11be-390f-a7e3-ee6b266222c3 | -6.4676 | -46.28835 | 2026-09-10 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 208c9883-34c6-3171-9f7d-9c43a07fd1de | -8.08942 | -54.85994 | 2026-09-10 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3a7bc82e-8f21-35c5-8dce-136a0bf3d079 | -6.75357 | -45.47727 | 2026-09-10 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f726d94c-bf92-33e1-a618-66d8aaf99ce4 | -7.197 | -43.60801 | 2026-09-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a94c9863-9f8b-33f2-b540-eda14e81cb97 | -6.238 | -51.68314 | 2026-09-10 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7a78a28-1d52-392a-b207-b16d8c1158b5 | -2.93699 | -50.4616 | 2026-09-10 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b49c8547-e19a-3074-85ca-5bd44098fb12 | -7.48721 | -43.81437 | 2026-09-10 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f706ba72-810b-3a03-bbf5-17afb7596218 | -5.77121 | -45.07521 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55e161aa-4ef4-388a-af17-8cdf19b0cf94 | -7.46553 | -45.76344 | 2026-09-10 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ef2dd13-49ac-3cea-89ee-2a2ad437b8c6 | -7.97728 | -43.97859 | 2026-09-10 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73ec7711-8849-3a96-abab-2e11009864c5 | -6.75302 | -45.48074 | 2026-09-10 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c68ca351-6e81-38a8-a5f8-22a37fcfbe5a | -7.72831 | -45.05056 | 2026-09-10 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8cc370c6-dc71-3ff7-b615-336e51532159 | -5.80322 | -43.7976 | 2026-09-10 04:25:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d001425f-e7a2-3c22-8f58-bc7e1e2933cd | -2.73003 | -57.62943 | 2026-09-10 04:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b7dbfe9e-1362-33fc-b60b-f3b525b6f789 | -4.36446 | -47.78026 | 2026-09-10 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| b20fa035-3355-3f05-9dc8-bacf64a53cbe | -6.16262 | -44.64219 | 2026-09-10 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 4b2d0e19-0525-36ad-9275-781dae36daf0 | -2.94438 | -50.47174 | 2026-09-10 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8eb6ec99-3c0d-3973-ba36-d6faa3d11ecc | -7.46295 | -46.14136 | 2026-09-10 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf5c2633-3d93-37f6-b79a-251775eed890 | -7.50991 | -45.27131 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ded0f96c-b4b5-3b74-8765-ce398a2e53db | -6.7257 | -44.04227 | 2026-09-10 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90895c94-f590-379d-b90e-03d22c051eb6 | -6.28429 | -41.70391 | 2026-09-10 04:25:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2a540d4f-6395-3fc4-a89a-fc3981d1bb2a | -7.98899 | -43.94731 | 2026-09-10 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e63e4da-4a88-3899-a491-8e15b3df15c3 | -5.28503 | -55.9651 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ead5094d-95a3-3446-8b6d-a23043fbf22c | -6.16702 | -44.6358 | 2026-09-10 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4687d1ca-c348-3e37-afe1-a921b8901e06 | -2.94296 | -50.4804 | 2026-09-10 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d79c8c29-21ad-35e3-985b-e7b417831b3f | -7.48785 | -45.28196 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 365e5185-9d9e-3e99-973e-4c9af7d98550 | -10.18046 | -42.22629 | 2026-09-10 04:25:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 70da36db-9018-3a87-9c07-f9a2e94b7950 | -7.50384 | -45.26679 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b1ca45c-cec3-3ebf-9aa3-1debc3852906 | -8.98269 | -45.00029 | 2026-09-10 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7ea94861-e61a-35f1-b0a5-face1f157eb3 | -7.49171 | -45.27901 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad9aa116-d36d-391f-baf1-03706e1f23e3 | -9.59668 | -40.36079 | 2026-09-10 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f80f9327-7c3f-3fa0-a2cc-873b7ae30439 | -2.93926 | -50.47531 | 2026-09-10 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57bbb562-8a22-3389-9c05-f83157ef5cb1 | -6.86884 | -46.01316 | 2026-09-10 04:25:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa937a2d-ffd1-3e7e-a35b-c2dc3df666b4 | -7.54146 | -38.44039 | 2026-09-10 04:25:00 | NOAA-20 | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a7640fba-c610-3e47-a0e6-acc6eeb2df58 | -5.77176 | -45.07175 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3249ecb5-fd68-34d4-9504-0a6dab8422ce | -8.08596 | -54.84781 | 2026-09-10 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58aaa1ea-5ee0-35e3-a725-93d5d25fb9f6 | -8.99752 | -44.88436 | 2026-09-10 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d225533d-58ac-3485-98c5-6807c1438369 | -5.32384 | -47.47279 | 2026-09-10 04:25:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README26.md)
