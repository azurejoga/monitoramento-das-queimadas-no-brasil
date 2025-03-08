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
| 510cdfeb-f672-398b-acb8-af3049211f33 | -21.2541 | -48.7071 | 2025-03-08 00:10:00 | GOES-16 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 61.7 |
| b306c8ca-0f88-3f89-b01e-c37501b3a54c | -21.2541 | -48.7071 | 2025-03-08 00:20:00 | GOES-16 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.6 |
| 55d0a84f-852e-3687-bced-54bfd5d2841e | -23.1835 | -46.246799 | 2025-03-08 00:27:00 | METOP-C | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3fd80f75-154c-3a0c-afc9-62c3c5e23196 | -6.9604 | -43.009102 | 2025-03-08 00:27:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 83ce2864-4d95-388e-b0be-d1af619b5cf8 | -21.254299 | -48.693901 | 2025-03-08 00:27:00 | METOP-C | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eaf84a71-0096-33e5-84e5-4cc62dd5add2 | -10.3517 | -37.130402 | 2025-03-08 00:27:00 | METOP-C | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a8901879-ea37-30b2-8fe2-a9af02d232e1 | -6.2149 | -48.040001 | 2025-03-08 00:27:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f0da141-5619-31c3-a249-d2723dc56bac | -21.256701 | -48.706902 | 2025-03-08 00:27:00 | METOP-C | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d4e7dfd1-2e59-301d-8af1-87b83a48155d | -20.718201 | -49.417099 | 2025-03-08 00:27:00 | METOP-C | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2eb5baab-2241-39b7-aa10-eb21e73f935a | -19.1889 | -40.122501 | 2025-03-08 00:27:00 | METOP-C | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 041e6458-8e71-3d55-af8b-3553fe01f3d1 | -30.362301 | -51.955002 | 2025-03-08 00:27:00 | METOP-C | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | nan |
| a7a65824-e236-309c-aeb9-5367171f56f1 | -6.9721 | -43.014801 | 2025-03-08 00:27:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 69b8e6a4-56e4-3acf-9349-d6eb116ba2bf | -13.8734 | -44.307201 | 2025-03-08 00:27:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d745e3ca-b572-3c4a-bd9d-be4c37c0f843 | -13.875 | -44.314201 | 2025-03-08 00:27:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e81d9a61-24e0-3093-b8ad-11992129c55a | -21.259001 | -48.719898 | 2025-03-08 00:27:00 | METOP-C | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1cef68c1-4ca5-3009-a1b0-f4b16176953f | -30.3589 | -51.9263 | 2025-03-08 00:27:00 | METOP-C | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 1aaa9d8e-a9d1-3a90-82e8-7991f6536990 | -10.6679 | -44.4007 | 2025-03-08 00:27:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 39bc4bd4-ac15-37f1-92c3-90d5a2e7725b | -30.368601 | -51.9249 | 2025-03-08 00:27:00 | METOP-C | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 2371c615-7efc-3260-9cdf-b7734d7b124f | -10.6663 | -44.393799 | 2025-03-08 00:27:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 179083c6-ac4e-36db-8b09-3f4eebba6e7b | -13.8832 | -44.304901 | 2025-03-08 00:27:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 20016a8f-fad2-36a4-95eb-0c6a6073407d | -21.246901 | -48.7089 | 2025-03-08 00:27:00 | METOP-C | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e3057d2e-2c63-3812-beb9-155e4ec9bab6 | -23.181601 | -46.236801 | 2025-03-08 00:27:00 | METOP-C | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 16f41916-2469-33e3-9c7e-7d2c019fa1e7 | -6.9702 | -43.006901 | 2025-03-08 00:27:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b7611c36-bf26-3a06-9218-b94c2b858369 | -20.720699 | -49.431198 | 2025-03-08 00:27:00 | METOP-C | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e8d3cd9a-9484-3c37-92cf-be7776834c39 | -6.2166 | -48.047501 | 2025-03-08 00:27:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 52067fbf-38d6-3f89-8dde-95c6f4959b74 | -6.9739 | -43.022701 | 2025-03-08 00:27:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5e413df0-81cf-3070-828b-9ba690b72230 | -15.8286 | -44.5341 | 2025-03-08 00:27:00 | METOP-C | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 52455148-29b2-3d7d-b43f-bf328117f0f0 | -6.9623 | -43.016998 | 2025-03-08 00:27:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2bf678a1-7f9b-327d-95c5-d7e51e5ad40e | -30.372 | -51.953602 | 2025-03-08 00:27:00 | METOP-C | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | nan |
| ac52b74a-8fef-3016-bdb9-8ddb83371647 | -21.2541 | -48.7071 | 2025-03-08 00:30:00 | GOES-16 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.2 |
| e0be49b3-f026-3b39-95fa-be2618d0eb67 | -10.9884 | -44.7216 | 2025-03-08 00:31:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7d653190-728e-3b4c-8b96-00526396ae1d | -10.99 | -44.7285 | 2025-03-08 00:31:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9871d1c4-5008-352f-84d7-13e27f94af00 | -10.9869 | -44.714699 | 2025-03-08 00:31:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 19e2bd6a-9bad-351f-b31b-d887025fafe3 | -21.2541 | -48.7071 | 2025-03-08 00:40:00 | GOES-16 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.1 |
| 1158d1de-a21d-3e01-906f-f7baeb36cf3a | -23.18322 | -46.25133 | 2025-03-08 00:52:00 | TERRA_M-M | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 5e8c2964-4129-304c-b83e-bd1e4c3e08d6 | -30.37313 | -51.99015 | 2025-03-08 00:52:00 | TERRA_M-M | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 30.3 |
| 9b487d7a-35a8-3449-b016-7c3647e16e92 | -30.3714 | -51.97163 | 2025-03-08 00:52:00 | TERRA_M-M | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 64.7 |
| 62750a69-2197-3d95-8e7e-2f014de12785 | -21.26311 | -48.70894 | 2025-03-08 00:54:00 | TERRA_M-M | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| e4fe97d7-02bd-3210-b312-3f684bece09f | -21.2644 | -48.71855 | 2025-03-08 00:54:00 | TERRA_M-M | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| e62dd335-ddeb-390a-952d-4119880554a2 | -13.8767 | -44.30952 | 2025-03-08 00:54:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| f6046ecd-3ff7-37e3-b4be-da3b30e35f80 | -20.50744 | -47.50798 | 2025-03-08 00:54:00 | TERRA_M-M | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e9191c5f-6bca-31cc-ad91-bd4ed1e427fb | -20.72418 | -49.4309 | 2025-03-08 00:54:00 | TERRA_M-M | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 09294290-e092-37f0-9ef5-01264f2abb57 | -15.82752 | -44.53899 | 2025-03-08 00:54:00 | TERRA_M-M | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e9a8c273-30d9-30c7-986a-e619441cd8ee | -13.87928 | -44.32522 | 2025-03-08 00:54:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 1ad48cfc-11b2-3ac4-9676-2461b8d9dadd | -21.25418 | -48.71036 | 2025-03-08 00:54:00 | TERRA_M-M | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 49.9 |
| 0db1b69f-ce4f-31fa-8530-3bf8df4b850c | -21.25547 | -48.71999 | 2025-03-08 00:54:00 | TERRA_M-M | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.0 |
| 47a1a6a1-f7d2-35c4-bb39-d6decbfa904c | -20.72548 | -49.44084 | 2025-03-08 00:54:00 | TERRA_M-M | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 15.2 |
| a33d5e4d-8745-31c7-9b39-7f1b1c798af6 | -10.98445 | -44.71973 | 2025-03-08 00:56:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 67f93ef9-021d-3608-8f2a-d37573d11cc8 | -6.96197 | -43.02735 | 2025-03-08 00:56:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 48.4 |
| 8a3c4515-cf24-3411-b778-fa9748406daf | -6.20939 | -48.0513 | 2025-03-08 00:56:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b969b35b-1142-35b6-b107-43d73118e82a | -6.95643 | -43.00697 | 2025-03-08 00:56:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 594a42a2-36fc-3e41-80d7-9876253fb01a | -10.98699 | -44.73627 | 2025-03-08 00:56:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| fe8badf9-75aa-3bbb-8578-334cbf7419e0 | -6.96042 | -43.03305 | 2025-03-08 00:56:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 4de0bb9d-772b-3ec0-b557-76ac1d880cc0 | -10.98221 | -44.73061 | 2025-03-08 00:56:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 56166287-797b-3214-b17d-24d84b83a483 | -30.3827 | -51.974499 | 2025-03-08 01:17:00 | METOP-B | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | nan |
| c8b6ff34-763a-36a3-9483-edc0b8fc65ed | -30.528799 | -53.618 | 2025-03-08 01:17:00 | METOP-B | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | nan |
| c8703f6c-f988-3c30-a042-bc9f42977c81 | -30.379999 | -51.9636 | 2025-03-08 01:17:00 | METOP-B | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 31d14cd2-23e1-326f-a760-7f87bd6c2348 | -30.531 | -53.627201 | 2025-03-08 01:17:00 | METOP-B | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | nan |
| be203ea7-1379-331a-8aa5-3763118d584b | -30.334 | -53.408199 | 2025-03-08 01:17:00 | METOP-B | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 2d470b09-6061-38ef-bab0-9bf70d589155 | -21.446501 | -57.253201 | 2025-03-08 01:17:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| cbf6c1fa-45f7-39d4-8082-e0f04c6c39bf | -30.370399 | -51.966801 | 2025-03-08 01:17:00 | METOP-B | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | nan |
| d81fc8f1-e321-3800-8c3e-7ae34cd1a20e | -21.2565 | -48.696499 | 2025-03-08 01:17:00 | METOP-B | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 353993b6-d6c6-3945-95c1-44e76c8f9dcd | -29.6362 | -51.536701 | 2025-03-08 01:17:00 | METOP-B | MONTENEGRO | RIO GRANDE DO SUL | Brasil | 4312401 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 45408bb3-e993-3265-a885-81f12f0f9363 | -30.3773 | -51.952599 | 2025-03-08 01:17:00 | METOP-B | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | nan |
| f6b3844f-7ab2-3344-acc4-2a66bb0e53a9 | -29.6332 | -51.525002 | 2025-03-08 01:17:00 | METOP-B | MONTENEGRO | RIO GRANDE DO SUL | Brasil | 4312401 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 3cfae1a6-83e4-3c8c-96c8-a138d2e5f80d | -21.2661 | -48.693401 | 2025-03-08 01:17:00 | METOP-B | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e3397033-655d-3240-a37f-ea9b0ed25d42 | -30.3724 | -51.9623 | 2025-03-08 02:00:00 | GOES-16 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 88.4 |
| 08e00f53-2f82-3a31-a02f-d2f8549d863a | -30.3715 | -51.9868 | 2025-03-08 02:00:00 | GOES-16 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 96.8 |
| 73e86fce-0863-3ec3-89b2-5d52767166a2 | -30.3715 | -51.9868 | 2025-03-08 02:10:00 | GOES-16 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 95.4 |
| b5821673-6855-3267-8060-13056b5ccc32 | -30.3724 | -51.9623 | 2025-03-08 02:10:00 | GOES-16 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 92.2 |
| 6a3f2806-e464-35c1-8d69-d584d085f312 | -30.3522 | -51.9519 | 2025-03-08 02:10:00 | METOP-C | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | nan |
| cffa10ed-f50e-32a1-a365-c3f1373bd787 | -30.342699 | -51.956001 | 2025-03-08 02:10:00 | METOP-C | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 7e539a57-a68b-374d-8564-7f7d79ae7731 | -30.3437 | -51.9916 | 2025-03-08 02:10:00 | METOP-C | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 7407e4e4-a7ae-30ff-9c2a-168977284a97 | -30.333401 | -51.960098 | 2025-03-08 02:10:00 | METOP-C | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 6e77c32c-5ce1-307c-a3f4-e2697680198f | -30.3531 | -51.987499 | 2025-03-08 02:10:00 | METOP-C | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | nan |
| cc844a43-6dc5-30b0-9be9-2e843bd31713 | -30.3724 | -51.9623 | 2025-03-08 02:20:00 | GOES-16 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 73.6 |
| e648f722-6cd2-30a6-a506-5fefab6e7892 | -30.3715 | -51.9868 | 2025-03-08 02:20:00 | GOES-16 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 89.6 |
| 0e5c8d89-7b38-3341-ab81-d0643ddd8ecf | -30.3715 | -51.9868 | 2025-03-08 03:00:00 | GOES-16 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 84.1 |
| 75322faa-4c66-3c43-a6ce-ab9e24e6dc34 | -5.00838 | -37.30708 | 2025-03-08 03:08:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8b49a42b-b01c-3739-b417-6790c2599e9b | -5.00767 | -37.31119 | 2025-03-08 03:08:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d0f8012a-35e4-3105-81f8-17fe7ca9efd4 | -30.3724 | -51.9623 | 2025-03-08 03:10:00 | GOES-16 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 76.6 |
| cc774197-667e-3f60-877c-f46a2bdbb091 | -30.3715 | -51.9868 | 2025-03-08 03:10:00 | GOES-16 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 88.2 |
| 517db6e8-36fb-370f-b0ad-1ade7418dea9 | -10.34094 | -37.14751 | 2025-03-08 03:10:00 | NOAA-20 | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 3c884004-a2f0-385e-838c-4ed3333d3a88 | -11.30044 | -37.87395 | 2025-03-08 03:10:00 | NOAA-20 | TOMAR DO GERU | SERGIPE | Brasil | 2807501 | 28 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1705d90b-1078-3fb2-88e2-077e9826225d | -10.34155 | -37.14422 | 2025-03-08 03:10:00 | NOAA-20 | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 2ebd969b-ddb6-3301-88fe-6fb39d65fd6a | -11.29505 | -37.87289 | 2025-03-08 03:10:00 | NOAA-20 | TOMAR DO GERU | SERGIPE | Brasil | 2807501 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 07dcbee4-9f63-3c7f-9094-841d59a5dc1c | -19.66619 | -42.03336 | 2025-03-08 03:12:00 | NOAA-20 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| aaeda0ba-aafd-3be9-8e84-0393552fe1ba | -19.66023 | -42.03197 | 2025-03-08 03:12:00 | NOAA-20 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 309ef2aa-8f7b-384a-9287-c7c62773b3ba | -19.66367 | -42.03411 | 2025-03-08 03:12:00 | NOAA-20 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 268dd5b5-0f36-34be-92f5-f99b70bbfc25 | -19.66467 | -42.02963 | 2025-03-08 03:12:00 | NOAA-20 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 70faf345-01a7-3513-b968-7fb4818544f6 | -30.3715 | -51.9868 | 2025-03-08 03:20:00 | GOES-16 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 88.6 |
| 32837bce-8612-3760-ba14-25600b5961a0 | -5.00892 | -37.30569 | 2025-03-08 03:59:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3c6ca621-f76e-36e5-bc4c-b358fbf82ef5 | -5.01021 | -37.30684 | 2025-03-08 03:59:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 76bdf44b-d458-3d84-bb2b-a71c77f69fab | -5.00834 | -37.30952 | 2025-03-08 03:59:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6c12ffd5-7cd9-32d3-a7a8-f189edd41a92 | -5.30181 | -36.87139 | 2025-03-08 03:59:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3eb940e2-3274-30a9-81ff-2a5a65810c2b | -30.3715 | -51.9868 | 2025-03-08 04:00:00 | GOES-16 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 94.3 |
| 307e0032-501e-3cac-b9e3-a532d66bace8 | -11.30025 | -37.87151 | 2025-03-08 04:01:00 | NOAA-21 | TOMAR DO GERU | SERGIPE | Brasil | 2807501 | 28 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1c880446-2ce2-3ab4-8cc5-fd73a2bcc5ab | -11.21251 | -37.73032 | 2025-03-08 04:01:00 | NOAA-21 | ITABAIANINHA | SERGIPE | Brasil | 2803005 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1bf567d7-f823-32a2-b645-853f2f2970bf | -11.80039 | -46.65281 | 2025-03-08 04:01:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a01eff0-4589-350e-9b43-2f83bfe8a990 | -12.16194 | -43.20288 | 2025-03-08 04:01:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README2.md)
