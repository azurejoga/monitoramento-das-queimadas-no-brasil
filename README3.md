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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc327bb1-f856-35ca-8295-70cc26aa06f3 | -9.3423 | -45.4765 | 2026-06-16 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| d9e0509f-8e77-3733-9542-10c64bde1c8d | -12.8548 | -44.3625 | 2026-06-16 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 68510ef8-1852-3224-ab93-cdac1158695b | -9.3423 | -45.4765 | 2026-06-16 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| a9589bf9-b02d-3985-897c-11256f4de9c0 | -12.8548 | -44.3625 | 2026-06-16 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 0a001c57-ac99-3ab4-b7bc-43b2bc3f00c0 | -9.3423 | -45.4765 | 2026-06-16 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 49.1 |
| ce256cd5-d1c9-3db7-bd6d-29639894d8b7 | -12.8548 | -44.3625 | 2026-06-16 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 5604f0ec-1d28-3acf-99e6-e892afaa79bd | -8.9449 | -46.9582 | 2026-06-16 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| a45161e1-8ddd-3157-ae78-61e3fbc50d8d | -12.8548 | -44.3625 | 2026-06-16 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 7bfbf927-f87c-3d58-920b-155a90f20639 | -12.8548 | -44.3625 | 2026-06-16 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 4f26c0ab-02a4-304d-a5ed-20165820a4b6 | -12.8548 | -44.3625 | 2026-06-16 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.0 |
| bec08f05-45a0-310b-b8c1-a98f21b6061a | -6.2536 | -48.52171 | 2026-06-16 03:42:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c6e6f41-c71b-309e-a2cb-d39dc562c460 | -6.40094 | -44.17593 | 2026-06-16 03:42:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b7bbf478-9bef-32e8-98d4-e6e8c564f2af | -3.5636 | -43.20343 | 2026-06-16 03:42:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b791a9fa-c198-3872-8cc5-38ac35566453 | -6.30953 | -43.64968 | 2026-06-16 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 902bb090-ebe1-3ee9-b465-6ef41e0428ee | -5.44676 | -43.57235 | 2026-06-16 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5bae848-9465-3bab-a955-8b4580a0656d | -5.92758 | -43.4783 | 2026-06-16 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3588823a-780a-32ba-9262-261541cc7d0b | -5.58792 | -43.50448 | 2026-06-16 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc0c7410-5707-3b3a-b844-b4b387784a8d | -5.8398 | -43.4814 | 2026-06-16 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b735a2b-746a-3d57-9b3e-eb6334148ed4 | -6.98063 | -42.88507 | 2026-06-16 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| ccb0b539-c65c-31e5-83b8-bfd1919a3ae0 | -5.9281 | -43.47527 | 2026-06-16 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ca79e7e-9335-3bd2-86f3-0fd45b3ba0ee | -5.8019 | -45.07984 | 2026-06-16 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ffaedb6b-b312-3f6d-a2b0-8d1299013261 | -6.39565 | -44.17499 | 2026-06-16 03:42:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e2998f92-b21a-31ac-9e6b-91bf1d8e4342 | -6.13986 | -48.52108 | 2026-06-16 03:42:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba539a65-7d16-36ed-9dd0-eeeb6e97de34 | -5.44623 | -43.57541 | 2026-06-16 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b7f61e6-bbe6-3c7a-bc1a-36e8e72272d3 | -6.30553 | -43.64251 | 2026-06-16 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 22849dd7-f175-3725-a0cd-f517fdb201f4 | -3.51137 | -48.0356 | 2026-06-16 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f9c1b9cc-1a2e-3602-b319-efde003896bf | -4.35582 | -47.76009 | 2026-06-16 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 647907d9-092b-3948-93e6-63a5db62103c | -3.51372 | -48.03573 | 2026-06-16 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 104e5dbb-17c3-3755-8345-dfc002426a02 | -6.54503 | -44.68825 | 2026-06-16 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08884f7f-51c1-3c05-8ce6-b7c8e98fd15c | -5.52289 | -37.48672 | 2026-06-16 03:42:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 174f391d-d152-3a8f-8efa-681ccbeb05b0 | -5.25124 | -38.17289 | 2026-06-16 03:42:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 611b2b98-ef48-3793-9af7-214b8fd2e353 | -6.30446 | -43.64857 | 2026-06-16 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b4000093-0295-3fba-a06e-39f161a81bc0 | -4.35695 | -47.75882 | 2026-06-16 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1f27bf4f-0494-3134-8dde-2a6cda1a7db9 | -5.80253 | -43.79162 | 2026-06-16 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 86899dd3-3f3f-358f-9446-ee14878d496d | -6.13872 | -48.52728 | 2026-06-16 03:42:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 831ce2ec-0290-35cf-9dee-ca9139e63a24 | -5.80327 | -45.07193 | 2026-06-16 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a52bed9a-fe37-3cb3-a04b-486da23fe559 | -3.50539 | -48.0422 | 2026-06-16 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b639da9b-ef07-3444-b9cd-98cabb25e445 | -4.35581 | -47.76507 | 2026-06-16 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 057583fc-9966-3a7a-a872-6bd7bd2ecd76 | -6.97582 | -42.88765 | 2026-06-16 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 7c72e5e3-ba65-372c-9389-0af95098fe71 | -6.97758 | -42.8772 | 2026-06-16 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 0e1b0e73-f77f-334c-9a38-ad072e52c175 | -6.4674 | -46.90152 | 2026-06-16 03:42:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d6bb94b-145d-3b5b-8667-d19fefcf184a | -5.83927 | -43.48448 | 2026-06-16 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2e7a966f-8e14-3a65-8d13-b772a9ea7efb | -6.97674 | -42.87907 | 2026-06-16 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d2d9e9a8-15fe-3ae8-8df5-d74bf04cea20 | -5.83822 | -43.49062 | 2026-06-16 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d65c4b78-40d5-3b1a-a25d-f75862eaada6 | -6.13754 | -48.53365 | 2026-06-16 03:42:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac70e08e-41f1-3dea-b545-051bc7123df6 | -5.83769 | -43.4937 | 2026-06-16 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 86491e88-efa4-31a5-8c41-2a692522fed0 | -5.83875 | -43.48755 | 2026-06-16 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 56047f94-fc09-3d67-9911-32f1150e3db6 | -5.93317 | -43.47627 | 2026-06-16 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59ad7a06-43b6-3ae0-84c9-28aa9ecf768b | -6.38977 | -44.17744 | 2026-06-16 03:42:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42192481-3639-322d-b4eb-c374ae884592 | -4.35472 | -47.76634 | 2026-06-16 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 60bebc91-d606-314c-a462-caab57790245 | -6.97582 | -42.88428 | 2026-06-16 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 422a5f6c-87c7-3ae1-bdc3-654aec25c439 | -5.3299 | -44.69351 | 2026-06-16 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e07a1aa3-5c40-31d3-911b-14051032bf0b | -3.96191 | -43.1154 | 2026-06-16 03:42:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5f37578c-5949-39ef-93c4-8baf8a70fe84 | -4.58927 | -38.59982 | 2026-06-16 03:42:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8bb83a72-d6fe-3fce-b226-8e7bf5c4ddd0 | -6.53958 | -44.68721 | 2026-06-16 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68147d0f-d858-3cc4-9897-b508f8e33a46 | -6.97971 | -42.89028 | 2026-06-16 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| b7d77511-ae74-326f-8045-8e7beb5a2414 | -6.97766 | -42.87386 | 2026-06-16 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8f8b97bf-33db-3ba7-945f-694f2a1d09fe | -6.9749 | -42.88952 | 2026-06-16 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 46d75457-b6bc-3528-a61a-381b4054232e | -6.13686 | -48.53114 | 2026-06-16 03:42:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6d6ddb58-e268-3133-8d3f-6103be0d17d5 | -5.53086 | -44.41869 | 2026-06-16 03:42:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 32d0dba4-0bf9-361f-b1d5-103744368412 | -6.46436 | -46.90082 | 2026-06-16 03:42:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6374223c-850e-337b-a12e-99734999a93a | -6.30499 | -43.64555 | 2026-06-16 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 46893cb0-03f9-3ae8-bbde-e6220c781b2c | -6.30607 | -43.63943 | 2026-06-16 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77e80a46-de98-3bff-ab6b-01a864e5f980 | -5.98302 | -47.0727 | 2026-06-16 03:42:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41e47e97-94a7-3537-be97-c4c44c97275b | -5.52307 | -37.62083 | 2026-06-16 03:42:00 | NOAA-21 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 20a9c2de-8f7c-33a2-9c65-3b66a96c9f7a | -6.98246 | -42.87466 | 2026-06-16 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e727fcfc-c304-3323-8e44-173b4c1abed9 | -5.35214 | -45.18998 | 2026-06-16 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1d84187c-48fd-36a4-ac82-38ab16a24e80 | -6.39622 | -44.17166 | 2026-06-16 03:42:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| dd8d2bca-8603-3158-b945-16540de3824c | -6.98154 | -42.87988 | 2026-06-16 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f8d4703a-3bb4-302a-9729-801251e878ef | -6.39508 | -44.17831 | 2026-06-16 03:42:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a007d406-49b2-3074-a596-c195f0bef239 | -6.1831 | -48.51473 | 2026-06-16 03:42:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d3547d0c-9a30-3cc0-bebf-c07618ce2f39 | -5.58739 | -43.50756 | 2026-06-16 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 756bb96d-9bb1-3571-b04c-d11f5471d6c7 | -6.13809 | -48.52468 | 2026-06-16 03:42:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2ac702e5-cb96-329c-acd4-1d6628b5fc75 | -5.92705 | -43.48135 | 2026-06-16 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 216373b8-aba5-33fc-b9b8-3edfd84d6830 | -5.80258 | -45.07588 | 2026-06-16 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b5ff4632-4fe4-3204-b51a-c1cee338d6c1 | -5.93264 | -43.4793 | 2026-06-16 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7b57217-c7a2-3ccf-97de-d44be5aa5f88 | -5.25037 | -38.17434 | 2026-06-16 03:42:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4a4af43d-b243-3c42-8980-a2ec8b995c35 | -5.8012 | -45.08383 | 2026-06-16 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18d5bfd3-124e-3c19-8bc2-e257338ed535 | -5.80394 | -45.06804 | 2026-06-16 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 173ed387-efaa-3604-ac4b-cd55bf582699 | -6.40151 | -44.17266 | 2026-06-16 03:42:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4170a2d8-72b5-367d-bbd4-77330321ce00 | -3.9614 | -43.11848 | 2026-06-16 03:42:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 166c88c4-ac0f-37af-9bfb-005badd8ff38 | -13.56052 | -47.86836 | 2026-06-16 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d179f2ed-7efc-3161-9877-a304a76be0f8 | -7.72293 | -44.16286 | 2026-06-16 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2ca99c60-04c1-3746-a14a-2b0b8b818f54 | -8.28101 | -48.22298 | 2026-06-16 03:45:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ac0e8dc-d6e7-3c05-aa12-e5e4cec472f5 | -9.32567 | -45.47867 | 2026-06-16 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bf8a36a-4d50-3f46-9482-895bf662a384 | -13.55807 | -47.85018 | 2026-06-16 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ddd6181-48f8-3193-9a4a-777d5a7ced82 | -10.55077 | -47.02825 | 2026-06-16 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bfa46fd3-aa00-3cc3-9874-b15dcd6fde17 | -9.34921 | -45.47567 | 2026-06-16 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ab319497-8873-39ca-92b7-6c8a78ce5237 | -8.96552 | -46.93554 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0be84147-00ec-3994-918a-731d27ae2c6f | -12.06861 | -47.55526 | 2026-06-16 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cc0c664b-3d4b-3321-ba1d-92e0a30375c3 | -8.94109 | -46.9648 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed451b68-a587-304f-9a72-b30459d9264e | -14.85183 | -43.36739 | 2026-06-16 03:45:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ec676f20-bf09-3abe-af02-fa4a66454101 | -9.22556 | -48.58093 | 2026-06-16 03:45:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b2c2e5e-a982-3edd-982e-a45aa6dea209 | -9.21093 | -47.34127 | 2026-06-16 03:45:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00614f5e-fb73-3554-98d2-650335a89b15 | -7.72051 | -44.56854 | 2026-06-16 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1260096-fa6e-3633-ae72-effca69ec9f8 | -8.94569 | -46.9683 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 807919be-835b-3bc1-bf30-61f3bb10c677 | -13.20899 | -45.48599 | 2026-06-16 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4b4f2fa-c952-3841-81a8-c7b0e22e7bad | -8.99383 | -45.73473 | 2026-06-16 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76874f45-77cd-305f-8d57-aae707cdb1dd | -7.72111 | -44.56516 | 2026-06-16 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8e50ada-e453-3f74-9df8-a1a4bd505234 | -9.32502 | -45.48229 | 2026-06-16 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README4.md)
