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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7c7a11f-c9ec-39df-86ba-0e37bd82cd32 | -6.34445 | -43.45599 | 2025-10-04 03:23:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2ae4d7ba-72c1-3984-b297-43c2eb4203ae | -6.67368 | -44.20185 | 2025-10-04 03:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8f52edab-4276-387c-80e4-15fca672ff6f | -6.27641 | -44.04311 | 2025-10-04 03:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e96222bf-b2ec-34ab-b81b-435c729898e3 | -7.75782 | -42.61313 | 2025-10-04 03:23:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| fa1b295d-8a15-3815-9780-7a7ef0296c9f | -6.31309 | -44.27082 | 2025-10-04 03:23:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 88e5f2de-1947-3408-895d-3c42423bec15 | -9.6792 | -37.09147 | 2025-10-04 03:23:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 3fbd70d0-2574-38b5-aa7f-9e1733e48805 | -11.44655 | -43.49886 | 2025-10-04 03:23:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 10cfc19d-67b6-3c2f-9c68-91d00c665df1 | -7.715 | -42.57867 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 94d9d2fb-c5c6-36eb-95ca-98495dc2a628 | -5.98186 | -44.14996 | 2025-10-04 03:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 615ba9d7-84cc-3c94-b4ab-1c189f15eea8 | -11.44751 | -43.494 | 2025-10-04 03:23:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 00dfd6ef-9726-3d92-9d95-31784c24f445 | -11.49741 | -44.99435 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 282ba066-2b2a-35c2-bccb-5cd3f2821844 | -18.66638 | -43.86427 | 2025-10-04 03:25:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8e207f4-ed1c-3741-8f19-fe14e0aae689 | -14.94541 | -46.86747 | 2025-10-04 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| df2ee468-fbd6-3a6a-b9e6-67bad5ccc83a | -11.4773 | -45.02391 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c640ab06-2daa-3082-bb9f-32d14513536b | -17.69901 | -47.08892 | 2025-10-04 03:25:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 57.3 |
| bf64e342-cbcf-358b-86da-80465e930538 | -15.65138 | -46.26016 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5dff8fea-4e49-3bf2-8c74-3e91c8d734d4 | -11.50146 | -45.00925 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 857b60fd-aa8a-3fcf-b18d-5d662bb58998 | -11.84273 | -45.02973 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f046d78-5d63-3ce0-ba72-ef3286850c08 | -17.71366 | -47.09022 | 2025-10-04 03:25:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 5c90a141-e3fd-3438-a78d-114a5a778c5a | -16.75838 | -43.95691 | 2025-10-04 03:25:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3e291f88-9a2a-3d97-9779-6adcaace810c | -14.23927 | -46.07824 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 9f3d4d02-a9d9-3f74-99eb-31504939b918 | -14.24189 | -46.098 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f779b203-9e55-33f4-bdeb-fcda154c9e69 | -12.10961 | -43.45123 | 2025-10-04 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b857093-01d8-32e7-8b3c-fd1355e5cc21 | -15.53055 | -46.82998 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 64d6146a-75f3-33c2-bd8d-d3363052d8d6 | -11.45493 | -45.13666 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 26e7b7f3-537e-312e-8bc8-b9d001bd192b | -17.07851 | -43.35727 | 2025-10-04 03:25:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5f18ad66-2249-37d3-85e1-220e6aaadfa7 | -11.83737 | -45.02168 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef481273-6e11-391b-a616-6b0f088e279b | -12.8689 | -44.63247 | 2025-10-04 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a78549ad-eaef-33c9-9201-7b23fdf95e52 | -15.72677 | -46.28548 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| aee4b81f-433a-301b-914f-4776c6c1bb3b | -15.74287 | -46.2702 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e27f661-9a67-3732-b955-58d8da020198 | -13.40945 | -43.68997 | 2025-10-04 03:25:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3e828656-4a93-3891-8d3a-727e12f3032a | -15.6023 | -46.93583 | 2025-10-04 03:25:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ab58c5c-386c-31ce-90b5-72e84ac3128b | -14.92588 | -46.88764 | 2025-10-04 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 34945472-4e86-36bc-ac3c-66cc394a7b6c | -15.82808 | -46.24487 | 2025-10-04 03:25:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d275a13-3cda-3096-abc2-3bdce6c6870c | -15.95983 | -43.33687 | 2025-10-04 03:25:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4e74bd79-dd42-3e34-898c-880b9899ec8c | -11.45995 | -45.14409 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 959e1a02-abb1-35e5-aac2-aa290ac45af3 | -12.11164 | -43.44173 | 2025-10-04 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 15503ec8-9d2a-312c-aad4-0089665b5ff4 | -11.46538 | -45.15237 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0580e212-621e-391b-97af-2eb5390d7495 | -19.00219 | -43.0197 | 2025-10-04 03:25:00 | NOAA-21 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 88437fbc-72ec-318a-a005-b9ef430059dd | -14.2379 | -46.08453 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 946a0da5-a02d-3795-9076-67cbd42698a3 | -11.82788 | -44.91882 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac9b424e-265a-3c6e-ab88-ef604eae8c1a | -14.93647 | -46.85747 | 2025-10-04 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6118b5d9-672d-3dad-a86e-7de66757cfb8 | -17.71249 | -47.09277 | 2025-10-04 03:25:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b3d6aa50-b713-3cd9-a617-6d813bf2d558 | -15.95591 | -43.32732 | 2025-10-04 03:25:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3798eb30-7a3b-30f4-ae6a-0c89aab32894 | -11.48514 | -44.98533 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f87b8be-4e2c-3fbc-aff3-195d9c5ba7e8 | -13.16331 | -44.6424 | 2025-10-04 03:25:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16b9d9fd-c79c-39e2-add2-7a39644ffcfe | -13.88498 | -46.50987 | 2025-10-04 03:25:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b3f17f86-f40b-3d36-ae64-f4f2d0b31fef | -11.49332 | -44.98767 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8f041326-c0bb-3bd1-b6de-3de8e3a730cb | -11.46707 | -45.1467 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79f3bd36-7bc7-3250-972b-305c0999c4ae | -11.46037 | -45.1447 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 205e81b1-9c85-3d87-a0cc-fef5cefa1589 | -11.51041 | -45.00723 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e330bae2-2e80-3a84-b3bc-77c320b3a041 | -14.93443 | -46.86661 | 2025-10-04 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5ce35f4e-6b9f-3cb4-951c-d446f7ef5591 | -17.07989 | -46.23664 | 2025-10-04 03:25:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ccb84928-64c6-357a-a212-ffb7806b56fa | -11.86853 | -44.97318 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cc6aefb6-bdb8-3f6c-9faa-e7c0b41e4499 | -12.42441 | -45.15703 | 2025-10-04 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41ac1e50-6c55-3668-a0ff-653274cdb845 | -11.48657 | -44.98617 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4506e573-f8c5-387f-8274-0a1f7375d1f7 | -11.50392 | -45.0045 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d24e238-4545-38bb-9284-732d74b0348d | -17.7069 | -47.08838 | 2025-10-04 03:25:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 26.8 |
| c6fb2440-1c6e-3430-adb9-c89427ff5ca2 | -14.21817 | -46.07608 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2aab57e4-388f-3f93-85f6-81441e65325b | -15.73412 | -46.27776 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef16e887-f6d0-3507-9811-47355374d9ad | -17.07767 | -43.36126 | 2025-10-04 03:25:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2e432048-1006-3569-9340-5cf722c49093 | -18.18074 | -43.56679 | 2025-10-04 03:25:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44df3192-28a2-30ed-9cf6-27566d879863 | -11.50772 | -45.02014 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb9d4357-86a7-33c0-96f8-bfde712b1ecb | -12.95041 | -42.42081 | 2025-10-04 03:25:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 8b563294-4191-33e0-8149-2b0227d3ab2e | -17.61517 | -44.46655 | 2025-10-04 03:25:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc970bb0-5163-3be8-b11f-3074bf4aa76a | -16.35432 | -43.41613 | 2025-10-04 03:25:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4b8d5784-09ee-3f2e-b0f2-d42cc7666755 | -11.49632 | -44.99976 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 59ff01fa-50db-37f6-8626-9fea25ec7059 | -15.52311 | -46.83035 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 61ff7467-a356-3f32-b856-3822600a8f63 | -14.91522 | -46.886 | 2025-10-04 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9df0a336-6e5d-308a-a81a-4598293e8e82 | -12.04397 | -45.19791 | 2025-10-04 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a149be89-feea-36b3-a246-1cecbb5a353e | -14.93039 | -46.86808 | 2025-10-04 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f9bd0a05-d530-3c0a-a49b-5380fe47ef29 | -15.00175 | -41.42595 | 2025-10-04 03:25:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8612e2ed-fe79-3a08-bfe8-46549a442234 | -11.49221 | -44.99298 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c015693f-17c4-3706-8605-c95257de86d1 | -17.98214 | -45.00953 | 2025-10-04 03:25:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 500512bc-3c08-3b81-87fd-734dd9f64082 | -11.47307 | -45.01678 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 450bcd3e-770d-34f4-88c4-06b9f3fcdf9d | -11.83457 | -44.92028 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| faf3b774-fdce-3c4a-8b62-72eca49d6d02 | -11.88066 | -44.9823 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0d83812a-df88-3797-9eab-c19a7b94fcd7 | -15.58357 | -46.90857 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 83f701a0-8833-3d15-ba42-773005643bfd | -15.73751 | -46.26956 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b09c5b2-e14e-335e-9e7e-da766ceb71fe | -14.94188 | -46.86649 | 2025-10-04 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0c9a8ab7-9afd-32f0-ab7c-c102199fc9f9 | -12.08142 | -45.16136 | 2025-10-04 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3464ecb-7a4e-3ff5-a5d0-ea4996a2b25e | -17.08367 | -46.25042 | 2025-10-04 03:25:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e25151f1-ff0b-3168-83e0-c269dcc2df08 | -14.93835 | -46.86582 | 2025-10-04 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d50789f7-d247-345c-8755-d1afee15656c | -17.55818 | -46.76001 | 2025-10-04 03:25:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0ee2038d-aaff-347d-a8d0-58ad0bf828fc | -15.72224 | -46.27423 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 960cd870-4746-3de5-802d-d2411d96ac99 | -18.1815 | -43.56 | 2025-10-04 03:25:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 875ca577-7ef3-32d6-9317-7aefc82014cb | -15.19092 | -46.39211 | 2025-10-04 03:25:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 87ff026e-0629-36e8-a680-2e5750451aef | -12.11011 | -43.44941 | 2025-10-04 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1fb760ff-553f-35a0-b14a-4f016ddb031c | -17.58559 | -44.46058 | 2025-10-04 03:25:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 408038e0-82e0-346e-8cd6-098e46d8e157 | -15.53068 | -46.80682 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8c666acf-0339-3da7-b1d6-9d7a595119d5 | -11.47861 | -45.01743 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 891207a6-ba3b-3bae-86ee-ce077952848b | -14.92637 | -46.86941 | 2025-10-04 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 764c47a7-3b2e-3355-9add-2a95ff4af8be | -14.19819 | -46.06884 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 635230ba-6661-3006-a424-6393185bbf07 | -11.44681 | -45.14142 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f0c387a7-5327-37f2-88ad-571a031ca92b | -15.65333 | -46.25814 | 2025-10-04 03:25:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cbbc5a4a-2b74-32ea-85fc-9094e9bb9250 | -14.21672 | -46.08271 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 183fffa8-94f9-3ed6-a914-5d9e8812b43e | -12.02774 | -45.20774 | 2025-10-04 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 9e4a5c25-d8bc-3551-918e-2150a98e9ab7 | -14.23654 | -46.08973 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 6dc3c08b-e63d-3f79-b708-6c43699dc24a | -11.83487 | -44.9331 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd8b3ebc-cdd9-34e9-b5b2-29f1d00722e0 | -14.22355 | -46.08435 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 21.1 |


[Clique aqui para ver as próximas entradas](README14.md)
