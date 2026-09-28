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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e871409-321f-3ffb-8c51-da05f094c326 | -9.28422 | -46.57503 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 64aaf077-d2a8-372d-9ebf-c0a35eea0ff4 | -11.65061 | -50.68116 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 5f74b37d-f8c9-3788-b789-1716c7e9b05f | -10.00007 | -50.12299 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7f190e81-f7ad-3cde-9fb3-5a540574a665 | -11.48242 | -49.75334 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 138acc33-5b5d-3288-9d5f-a2f7729f18ae | -7.26665 | -46.93616 | 2026-09-28 16:26:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 131e9ef8-b9c7-3acb-a941-6cf1cbe2daf3 | -11.47746 | -49.75398 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 397d08b7-02b0-3509-9f85-7767c52c7714 | -8.49059 | -47.70665 | 2026-09-28 16:26:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 20184804-c39f-3f52-8261-40910ccd35f9 | -6.6769 | -46.11657 | 2026-09-28 16:26:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6cc4514d-e95e-33d1-93b0-e8d47ff9e91a | -9.96747 | -50.14474 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 7e6fd52d-5a46-32c8-b044-36c12d089025 | -7.76751 | -54.77962 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| e06108d5-6de2-3b4e-9d3f-91e1d1191dc9 | -10.12191 | -50.1951 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 538fcab9-3120-390f-b1d9-bf93ea3bc30b | -10.20822 | -50.0391 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| be99b852-b5d9-346a-b302-8c3bcd41a99c | -9.50262 | -46.38303 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 46f6a737-550e-381c-ae80-5b9f5d054d50 | -6.35721 | -45.80062 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b0df1619-9fce-340d-b74d-651bfca4aef4 | -7.69373 | -54.76832 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| f45d82f4-4ec0-37cf-8dae-60a40972de6e | -7.02371 | -43.73087 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 0a6d35cf-5227-32ae-9105-73d389535e04 | -7.29666 | -44.31106 | 2026-09-28 16:26:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fbc3ce8a-a7ff-3407-9e50-4db7f8a84f6f | -5.11072 | -45.16377 | 2026-09-28 16:26:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a03512e1-ec90-38e6-b7d6-86273360a5c9 | -7.76821 | -54.78517 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 52fea450-2d23-3871-aa2c-02cbd6b894ba | -8.61024 | -47.12146 | 2026-09-28 16:26:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 991ad6ae-6b21-3bfd-9956-ec1a61c6e990 | -7.28133 | -43.32629 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 7ca79ccc-0503-34ad-9f7a-92a2dd33a122 | -8.56485 | -44.04051 | 2026-09-28 16:26:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0c5d4653-376b-3883-a5f0-bdf7162a08c9 | -6.202 | -41.62103 | 2026-09-28 16:26:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| cc58a177-4d7d-3b36-9347-4652a0447207 | -10.00784 | -55.47765 | 2026-09-28 16:26:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 7473fd96-28bc-3b4d-812e-238427973e03 | -9.53186 | -50.24423 | 2026-09-28 16:26:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| c3d2e090-0a04-3813-8a7f-a2d4e4d2f602 | -7.68498 | -44.8097 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 12539c55-f9fa-38f1-a93e-8b86392261f9 | -9.16444 | -43.08409 | 2026-09-28 16:26:00 | NOAA-20 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| b2334c93-757a-3600-aa72-a2458bf1bd7d | -11.02842 | -49.70543 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| dc3861cf-ee5a-3bf6-98f3-27349adaa8fc | -9.28811 | -46.57452 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 68b27d23-93df-35d0-bca6-b3ce273f7609 | -5.38873 | -45.6772 | 2026-09-28 16:26:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 97b3b8fb-c216-3113-975d-a9dd70200dc1 | -10.49676 | -47.87178 | 2026-09-28 16:26:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4f96a99b-8d6e-3151-a93d-74ff3fd5e1ae | -8.29026 | -54.73384 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 5b3057ed-67d0-3c63-8119-9efd7b404546 | -10.9845 | -50.69036 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c6de211a-cf02-33de-b447-b2c2f77636d7 | -8.01173 | -43.73812 | 2026-09-28 16:26:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 32903b1e-c564-3d99-b95f-6d2840401607 | -7.69442 | -46.95869 | 2026-09-28 16:26:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7b764442-cd4c-3d26-81b2-11b3f14b3717 | -10.63273 | -46.31958 | 2026-09-28 16:26:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| e5be83a4-4bd7-3f57-8125-487fe63d8d2e | -7.38914 | -42.11765 | 2026-09-28 16:26:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 7af0657d-6824-3059-8826-9de2eb0f52bf | -7.70196 | -44.92546 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 077cf31e-0ca7-36f6-8ed4-15ba3f0622c2 | -9.32782 | -46.56646 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| daeb7239-c489-34af-9966-42cc8daa78d1 | -9.82144 | -44.94797 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 1ce795cf-b89d-3b97-b35e-caa662a6b474 | -11.10328 | -51.37531 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 025b9d83-3028-3e5a-ab9a-e5ef683cfe4b | -10.90635 | -50.70712 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 37207fe4-4f25-3ea3-9418-643e4b3f0fda | -6.81724 | -45.05813 | 2026-09-28 16:26:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 13a9b41e-3a74-37b1-98cf-60561391fb6a | -6.13135 | -44.80411 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c81a2670-277f-30b9-9757-002e0a851442 | -6.69057 | -45.66703 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0e4427b4-7fd8-3e4d-a006-2dd1de585425 | -7.34018 | -38.72774 | 2026-09-28 16:26:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| c9285c40-5317-39fe-b5bb-e167ad961875 | -5.41023 | -45.86954 | 2026-09-28 16:26:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| db0a5d01-54fa-3c64-93a8-27af18064bad | -6.78984 | -38.53353 | 2026-09-28 16:26:00 | NOAA-20 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 2e1fab4d-c623-38f4-93eb-7518c6e8b695 | -9.36001 | -46.54209 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d6bcf9b4-1d90-3e7f-8a46-0fd34f191ecd | -9.11381 | -41.70098 | 2026-09-28 16:26:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 6c741f60-c288-3aea-8419-682c8109605b | -11.07972 | -46.07729 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 1fdfb9c4-fbc2-32d3-9382-1b5796442f03 | -10.22004 | -50.01441 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 371.8 |
| 9e26f763-9f8b-3953-a2fd-94cd37897b03 | -11.14014 | -50.06804 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| df3b9071-e1ae-33bb-85db-0e0a13d65bbb | -9.85604 | -44.94336 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 2d8b0a15-8db6-368e-aeac-480d7114094e | -7.31452 | -44.59691 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d5a825f2-2634-37cf-96a5-b02a3aae851a | -11.65102 | -50.68446 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 29777c73-4c5a-3306-8bed-1834e5fe8c78 | -11.34589 | -47.33555 | 2026-09-28 16:26:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 23a8059c-f8b5-3561-9bf7-295a6ae3e1ee | -10.92234 | -50.66567 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3195836a-bec9-3d27-9aa7-c937f64175cd | -6.20059 | -52.90615 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 85d1388f-465b-30ad-ac69-9b3471b6c46d | -7.38872 | -42.09283 | 2026-09-28 16:26:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| e6834fda-cd64-34bd-9468-fdd468e2d49f | -5.06406 | -48.31199 | 2026-09-28 16:26:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 0522f774-760c-3d21-9594-86244388701c | -9.38876 | -46.38516 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e203e00c-803c-396d-868f-8ab1627d161b | -6.35485 | -45.80937 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 608d2ed8-7f68-3734-bda2-cf32056d39cd | -6.89756 | -52.47908 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 880b98c2-d88b-3025-bc0a-6a4fa78e6928 | -9.02908 | -45.01316 | 2026-09-28 16:26:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 73fd9581-0e7f-3279-8ddd-16e8a253b458 | -10.21553 | -50.00817 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 225.1 |
| 240ec58f-d291-3620-953b-1a375b3561f2 | -3.30317 | -43.27423 | 2026-09-28 16:26:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 72d44584-ee9c-3fea-97ad-a2fafbfdbf0c | -5.06353 | -48.30833 | 2026-09-28 16:26:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b35b09fe-3915-3324-b8f7-9770448548a1 | -6.35899 | -45.78797 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ca673c89-829a-325e-b4fa-fb067b43bd4c | -6.20967 | -52.90411 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f696f1f8-5f23-356b-ac13-2f170b3e5e97 | -10.97239 | -50.67875 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| baf339d7-2bb7-3b34-8c42-6f83ca62d482 | -5.63792 | -43.72003 | 2026-09-28 16:26:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1ffa0ad1-4633-3c73-a290-b0ae0c355825 | -11.13043 | -50.0723 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 14db38c5-c923-334d-a7a2-72b435353e5a | -6.36559 | -45.80772 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 679211a7-264e-381a-88c2-1e65c695bbc8 | -5.67983 | -47.48019 | 2026-09-28 16:26:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 67f056be-2cbc-3868-a6b1-716875e3fc51 | -6.33975 | -44.62843 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 098addad-103a-3ea1-bf07-db4756266207 | -6.56048 | -40.38199 | 2026-09-28 16:26:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 32.2 |
| 2e3d4b42-5f77-310d-9f81-0cbd9f347370 | -8.96532 | -44.14698 | 2026-09-28 16:26:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 15b21a7d-3684-3782-aca6-e74c254ba84c | -6.13733 | -53.05515 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 44161547-8e8c-3899-95ef-83dfda561a20 | -6.75041 | -43.04634 | 2026-09-28 16:26:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f53fa5c3-2cd9-33c0-a9e7-e9c986aa3227 | -11.1607 | -50.0684 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fa28b0f8-fdc6-3b7d-b71e-7ec5c33dbd87 | -10.12172 | -50.19231 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 47917434-1248-3b57-9839-6cae3386fa20 | -10.97279 | -50.68198 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ea830c65-dfb1-36c7-843b-0eea8a9760f0 | -11.1293 | -50.06343 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 00f08dfa-a6de-3986-9334-377d373406f2 | -10.59589 | -50.56837 | 2026-09-28 16:26:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ad13fe33-7919-3278-b1a8-e7c0b4dc5a98 | -3.97628 | -40.10717 | 2026-09-28 16:26:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3094d11d-cc9c-34eb-87d4-cdbe0190a4b0 | -9.99226 | -50.13467 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 6e8d9615-0b49-311f-a94d-b3b5920c5300 | -11.06006 | -47.66918 | 2026-09-28 16:26:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 7e0eb908-e32e-35b7-b3f1-cff46a49ec67 | -9.65588 | -42.31684 | 2026-09-28 16:26:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 18.3 |
| c55cbdb8-6949-31a0-becf-43cf31870c09 | -10.38981 | -46.52794 | 2026-09-28 16:26:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7197b0f2-7aed-38e7-afb3-3df659e72594 | -5.73363 | -45.02423 | 2026-09-28 16:26:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| c4e84c81-a132-3c49-b690-e9fabc300a9d | -10.19923 | -49.99882 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 32a35dfc-cf33-331a-95be-0af66d1630a4 | -7.45706 | -44.5909 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5d6619de-3b43-3b17-abe9-470622d513a0 | -10.7761 | -48.74602 | 2026-09-28 16:26:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2dfd74ad-c97d-3197-90c9-9376c8ea47bb | -7.28197 | -44.30573 | 2026-09-28 16:26:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 30cfb69d-aa1a-3eeb-a5cf-bf42d5a48024 | -7.04579 | -42.86807 | 2026-09-28 16:26:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 2411f331-b86e-39b2-b745-9555505fe432 | -10.9116 | -50.70645 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 27852ec4-8b1d-3ae3-ab4b-302af988c4a7 | -10.2438 | -49.99288 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 428f53af-5d89-3722-928f-ce6f4d5abe7d | -7.66319 | -45.47681 | 2026-09-28 16:26:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7f54f10e-4056-38fc-8abe-e395bf770450 | -7.46607 | -45.06326 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README112.md)
