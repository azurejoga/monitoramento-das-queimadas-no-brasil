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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab517fee-57b8-3311-8adc-f6c0cb9fec22 | -4.01285 | -48.06501 | 2026-08-19 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00430f9d-73e1-328e-9903-24e41b2aba91 | -4.00575 | -48.06487 | 2026-08-19 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 910b0dd5-ead1-3d9e-aca8-22e63e534898 | -5.66192 | -43.57249 | 2026-08-19 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a9284eb-fb19-3678-ab95-c2bf7493cb2a | -6.5335 | -43.12217 | 2026-08-19 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fd4e321b-fa7f-32b9-ab6c-9d0632f5920e | -3.67958 | -47.65876 | 2026-08-19 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 8902045d-006e-3910-8461-52c620225df9 | -6.23476 | -43.68903 | 2026-08-19 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 55f90a20-bbb5-3750-ba4f-c4cee521c5fb | -11.31248 | -45.21679 | 2026-08-19 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26add2f4-3d37-3c8f-979b-114e1afd1054 | -7.2882 | -44.07668 | 2026-08-19 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0090d97-e1c9-3008-8c92-b48dbe21c3bd | -11.12004 | -47.26652 | 2026-08-19 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a6ab256-d973-301e-9ec5-b3a6424edcf6 | -7.29223 | -44.08357 | 2026-08-19 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6072c421-d549-351f-b94c-fd415cef9cde | -11.38595 | -46.38723 | 2026-08-19 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82de2863-e136-35cb-8dc3-8d13f2774e0a | -7.1716 | -43.10408 | 2026-08-19 03:45:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8dba287f-eae5-33f1-86f2-647d66be29b2 | -11.38528 | -46.39074 | 2026-08-19 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ddc50c58-765f-3c66-b9fc-40772b8a8d32 | -11.37982 | -46.38927 | 2026-08-19 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03075859-42db-37d4-bfac-da91b128e3cc | -6.83487 | -44.94422 | 2026-08-19 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d679b492-2f89-378a-90ce-bb9ae496912c | -11.49112 | -45.1084 | 2026-08-19 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af739e3e-5625-38ed-b366-ccfb143c1b3a | -11.12793 | -47.28823 | 2026-08-19 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d1a2a93-4689-36fd-a90c-bd90b6af5365 | -8.35354 | -45.9767 | 2026-08-19 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3b16c6ed-5434-3c23-b956-d66e3dac534d | -7.94522 | -44.63143 | 2026-08-19 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3ed5c42a-767b-3039-9525-f6e93da52812 | -12.23822 | -43.1601 | 2026-08-19 03:45:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0e245e32-167e-3ac6-b21f-fb5304a4fec8 | -7.45247 | -45.14334 | 2026-08-19 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24d86015-054d-3abe-a824-f40e7dd233f0 | -8.35925 | -45.97754 | 2026-08-19 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8349e429-63cd-3c71-bd78-ff61d587a3a6 | -13.44052 | -43.84715 | 2026-08-19 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2dea12ec-54b5-32b3-a718-d7efe25fe0f9 | -8.36096 | -45.98058 | 2026-08-19 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ceabe24c-0fd5-390d-9215-529071109140 | -8.17986 | -44.43487 | 2026-08-19 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 86347473-be78-3f8d-901c-4fe37a13931e | -7.19072 | -43.45706 | 2026-08-19 03:45:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4cd158be-0bdc-3dfe-8208-0b15b1d6eb68 | -12.51478 | -47.85825 | 2026-08-19 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51017619-522d-3f67-b455-2f09c8e508a6 | -7.29493 | -44.08266 | 2026-08-19 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c07706d-6150-3368-9810-c960e23ac739 | -10.29197 | -48.23063 | 2026-08-19 03:45:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ccbc6cf9-f366-3a26-bd1c-b9536827b8e8 | -7.21848 | -43.28368 | 2026-08-19 03:45:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e238cb89-f5cf-3547-8d11-5545e68eaf0f | -8.35855 | -45.98147 | 2026-08-19 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b27bd937-ac02-33bd-a879-fdf8863b3e9f | -7.01522 | -45.89988 | 2026-08-19 03:45:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96a01baa-170c-34cd-9a7c-4f0d8fa495c8 | -13.44141 | -43.84237 | 2026-08-19 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 92f1442d-bbd6-361d-bedb-d9b45035401d | -7.64875 | -42.77313 | 2026-08-19 03:45:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 29f790a7-d181-3b03-8162-facea33beca7 | -8.36086 | -46.36655 | 2026-08-19 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7eb0cd47-86e9-3ff3-93de-94217b57d351 | -8.55981 | -47.40833 | 2026-08-19 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7b1efd5-1721-310a-ad72-4e48a5167999 | -9.72763 | -46.78032 | 2026-08-19 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4c49149-e0af-3f06-81bb-bc16062d5693 | -8.18042 | -44.43167 | 2026-08-19 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0663379e-41ff-3be3-b480-347af8479489 | -12.52701 | -47.84368 | 2026-08-19 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8892d0f-94a0-39c8-93d4-11703dadf018 | -11.32032 | -45.21429 | 2026-08-19 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 548563fb-ef46-3e5a-bfc1-728acdb30d96 | -11.31577 | -45.21023 | 2026-08-19 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e415d0ce-4c79-3302-ad37-c4d59312c4b8 | -12.24624 | -43.16607 | 2026-08-19 03:45:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 77443c4b-424c-34c7-a079-7b2c92266100 | -7.28572 | -44.07494 | 2026-08-19 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 665f35d3-ea35-3242-8980-447cfd6fa3d8 | -12.24181 | -43.16539 | 2026-08-19 03:45:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4daafbbd-35dd-3c04-86d0-6c20bba8f729 | -10.76469 | -42.08685 | 2026-08-19 03:45:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ff9d2f6b-0f16-3cfa-b1ca-86981e016587 | -7.17639 | -43.10492 | 2026-08-19 03:45:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d99d7f49-13c4-3ecb-b0e3-f5280175a790 | -11.31518 | -45.21333 | 2026-08-19 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 28cf59c5-74ce-384a-a7d8-9c557b44ad47 | -7.94415 | -44.63755 | 2026-08-19 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1dcf8a9c-7a4f-39d5-b403-c32854ac5712 | -13.4121 | -43.86858 | 2026-08-19 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 790eafea-32df-3bc1-86a5-f7dd517ce189 | -9.1164 | -46.04515 | 2026-08-19 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a16d379f-442e-3ef8-aeba-051ed2f18d76 | -11.31458 | -45.21645 | 2026-08-19 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d2c76854-1cb5-3359-8789-93c98d6124cc | -11.05354 | -46.52083 | 2026-08-19 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 912b4636-b859-3c93-b64d-458522153b57 | -11.06019 | -46.51639 | 2026-08-19 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b073c2e1-2280-3f48-ad01-6f049fb73517 | -13.40895 | -43.86572 | 2026-08-19 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39de5cd6-d612-3e20-8fc7-ce6febfc511d | -9.39404 | -48.24135 | 2026-08-19 03:45:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a40283f4-717b-3788-a096-5c5d12d78360 | -8.35283 | -45.98063 | 2026-08-19 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da3631ff-9da7-3683-85cb-aadfbbe4e0af | -11.62319 | -46.91305 | 2026-08-19 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24a72698-cd8c-3ad0-978d-a58a1a86caaa | -7.95393 | -44.64308 | 2026-08-19 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1c5d5db-3d58-3673-8c50-5ce99b59b8ca | -7.94464 | -44.6347 | 2026-08-19 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b74f1ab0-cbe8-36e4-b210-0d17f94dd879 | -7.29033 | -44.07877 | 2026-08-19 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8598746a-64a9-327e-aa3e-cc0e738b71b1 | -11.0575 | -46.5178 | 2026-08-19 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 188ce30c-f683-3915-8031-a7511eea9060 | -7.44758 | -45.1392 | 2026-08-19 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00f0261f-c1c2-37a8-ac76-1c1b9df3da39 | -13.69396 | -41.6487 | 2026-08-19 03:45:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9fae08bf-eb04-32f0-9791-f4a497d3b81e | -6.64366 | -45.5033 | 2026-08-19 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d83ccf2-3d01-3406-82ea-4ab0fe8c407c | -7.34701 | -44.37602 | 2026-08-19 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45b42f05-74c0-3d2b-97a3-db506d3f77bc | -11.32091 | -45.21119 | 2026-08-19 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5febb318-c77b-302f-bf6d-4a69baa07c69 | -7.21555 | -43.28131 | 2026-08-19 03:45:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0e8e3daa-6b49-343d-a795-8fb43769a1b3 | -9.11139 | -46.04077 | 2026-08-19 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 180ab785-ea4d-37cd-906a-0d1d53a4e67d | -11.05458 | -46.5153 | 2026-08-19 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| faa1ab4a-b4dd-3409-82c6-120ab0c13335 | -10.764 | -42.09081 | 2026-08-19 03:45:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 00daf8a6-1676-3c8b-a6d7-ae4b143d7a54 | -7.94349 | -44.64095 | 2026-08-19 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 65a85ed3-53f3-3487-82b3-0a31b767283f | -12.24793 | -43.15684 | 2026-08-19 03:45:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f03d378e-60bd-3881-ba09-6d8c8407855f | -7.94992 | -44.63549 | 2026-08-19 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c0555609-ca83-3375-984b-4ce04f4f94b7 | -12.23905 | -43.15558 | 2026-08-19 03:45:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a1ce0ed8-f5f8-33fc-92aa-aceae17c702b | -11.10935 | -47.26752 | 2026-08-19 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 070d6ce1-c1b3-3fff-ac79-51288a501676 | -11.31306 | -45.21366 | 2026-08-19 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7826f49b-972e-3ae2-bb0a-37b1daa6a8d1 | -7.28362 | -44.07285 | 2026-08-19 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5a666e4-dabf-310a-a194-1b70c4fe5460 | -9.74835 | -43.30783 | 2026-08-19 03:45:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d88d50cc-0ded-3f7d-85ff-9551b2e434b6 | -12.50884 | -47.85699 | 2026-08-19 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d7ecdad-cff3-3362-84a6-30ca7c2a56c8 | -7.34758 | -44.37674 | 2026-08-19 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 946decd7-9f43-32f9-b073-d9a42ae41acd | -7.94872 | -44.64195 | 2026-08-19 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 24c795d3-28d6-3723-885e-925a1c07b3f3 | -9.73126 | -46.78818 | 2026-08-19 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc9eedb5-0ec1-3a09-8a45-42f10463aae8 | -9.7246 | -46.79129 | 2026-08-19 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 194454a0-aecd-3a2a-86d5-ad17e2438179 | -7.25746 | -44.21752 | 2026-08-19 03:45:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70a45b97-ecc2-3aa1-9fe1-e9d3c084943f | -7.29278 | -44.08051 | 2026-08-19 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3676c89a-2879-34f2-8b78-acd4c339cdad | -9.72685 | -46.78454 | 2026-08-19 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d2053d62-a862-3aef-89a2-a1d13a55e8cf | -9.73289 | -46.7797 | 2026-08-19 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c2c2c0e-3145-337e-bd23-7eb06eb2e633 | -9.7328 | -46.84333 | 2026-08-19 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2e01ba1-3c26-3681-878e-bcef56e3cb40 | -7.94359 | -44.64072 | 2026-08-19 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 44d7c442-3626-3854-a773-1aa90cb9645e | -7.94407 | -44.63779 | 2026-08-19 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1732728d-4d5d-330c-9ae2-09c0af7b4692 | -13.44596 | -43.84302 | 2026-08-19 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2a019379-e0de-31cd-aae5-8c4fd699eb71 | -7.45188 | -45.14664 | 2026-08-19 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 431f264e-c6d5-3452-a64f-ac7427a359dd | -7.94519 | -44.63167 | 2026-08-19 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3d535080-4184-323c-9a21-a035945aebb5 | -12.52109 | -47.8424 | 2026-08-19 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d767773-ab23-3ae4-b1b9-7048fdd012d5 | -11.4917 | -45.10529 | 2026-08-19 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a7ee038-68ea-3ed6-b51a-da72d582444b | -8.35501 | -46.36556 | 2026-08-19 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9b8c408a-e1e1-3b9c-b7df-aaf80f7ba751 | -11.09342 | -49.91981 | 2026-08-19 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ce7a6e35-eace-34ce-8029-376aa14b20d7 | -9.73207 | -46.78396 | 2026-08-19 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b10b6791-a555-3a16-a52f-0c2e11425be5 | -7.28113 | -44.07108 | 2026-08-19 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79275dfa-adb3-338d-a313-c6bd94e47742 | -7.94469 | -44.63446 | 2026-08-19 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README20.md)
