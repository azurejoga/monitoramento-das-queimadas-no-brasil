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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 217cd047-31dd-3cc9-b856-d2c80edb9dc7 | -11.9623 | -43.34019 | 2024-10-25 04:17:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9122e70b-fffe-399c-80eb-ecbdddd57cba | -11.96175 | -43.34376 | 2024-10-25 04:17:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbb2545a-6c2e-389c-909b-d4435b197126 | -11.9057 | -43.83929 | 2024-10-25 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bf12628-4084-3c22-8663-58f00e396281 | -11.90294 | -43.83524 | 2024-10-25 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f393534-20ac-3d87-ab2d-8560e30632a8 | -11.90017 | -43.83119 | 2024-10-25 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d7f9ef0-ca4c-3be6-8e17-681eea63424b | -11.89963 | -43.83471 | 2024-10-25 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d07253cc-4a66-382d-95c9-790fb542ee64 | -11.89908 | -43.83823 | 2024-10-25 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a19f2cf7-4fd8-3306-8d22-0ed5b381920c | -11.78531 | -43.75901 | 2024-10-25 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c7afec80-f6f8-390c-94f2-300dde27f6dd | -11.78476 | -43.76253 | 2024-10-25 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8bd38911-1d52-3a12-9b1f-46f3704f5b92 | -11.71715 | -43.91383 | 2024-10-25 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14625d79-b3bd-36bf-8ee7-4439d90624c5 | -11.7144 | -43.90979 | 2024-10-25 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bee72508-e24b-333e-9eed-b67004c016fb | -11.71385 | -43.9133 | 2024-10-25 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 504fc6f0-d0a5-3075-88ba-2dca37e0494d | -11.69497 | -43.81667 | 2024-10-25 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2b701430-69e4-307a-848b-63ac50364a95 | -11.69166 | -43.81614 | 2024-10-25 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b809aa5-9ce4-3590-a45f-3f04db328250 | -11.67479 | -43.94659 | 2024-10-25 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3452bb7e-b949-3bd5-9ae4-b8909f90c001 | -11.58134 | -43.9779 | 2024-10-25 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e98a746c-901f-3883-aaaf-b4585ebb6dd2 | -11.58079 | -43.9814 | 2024-10-25 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 674819c3-cee2-3720-8f2c-07ead178dbdf | -11.57804 | -43.97737 | 2024-10-25 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| cc51a164-05ef-39b8-b5f4-4ab247da2025 | -11.57749 | -43.98087 | 2024-10-25 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| d0eea58f-dc52-328e-96bb-06d5d06d5b81 | -11.53857 | -43.98893 | 2024-10-25 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4af1f4e-ac2b-3e8c-b12b-ccd39ea4d2a6 | -11.53582 | -43.98489 | 2024-10-25 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 726ce478-b7dd-3483-b516-497ec86f48cc | -11.53527 | -43.9884 | 2024-10-25 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dac72463-50e7-346a-b5a7-eb84f07dae8c | -11.53472 | -43.9919 | 2024-10-25 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71d4cb47-34bf-3068-9a29-7d57c8ec5539 | -10.90818 | -43.99821 | 2024-10-25 04:17:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a562af1b-2452-355c-b27c-f75790dd57ee | -13.68607 | -44.28625 | 2024-10-25 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d60bd1c-d004-3659-811e-c02f4c42d2d7 | -13.66215 | -44.30794 | 2024-10-25 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75e5357a-3c04-379f-beb0-667674253a3f | -13.62468 | -44.35264 | 2024-10-25 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 141be6bf-0793-327e-ac45-5d163f464a04 | -13.62081 | -44.3121 | 2024-10-25 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36d7dd8b-df19-331b-882f-5c3adde51f44 | -13.52846 | -44.29306 | 2024-10-25 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3fa0ba54-1652-3861-8f32-dedb28d3d409 | -13.50644 | -44.41278 | 2024-10-25 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f99ea5db-1033-39a2-9338-2cc6c8c4f436 | -13.49488 | -44.42174 | 2024-10-25 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53f5e703-057d-3808-9375-5e0a3a2947a0 | -13.49433 | -44.42527 | 2024-10-25 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e97c043-b6fa-3ee5-9eba-a9f31391d854 | -13.49102 | -44.42473 | 2024-10-25 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca8d1a9d-238b-3c5f-bda5-f87d9dfd869b | -13.43394 | -44.35393 | 2024-10-25 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ef9bb2cc-4e81-3634-954c-4c7e94af98a9 | -13.43064 | -44.35339 | 2024-10-25 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 30a0098d-836b-3d1f-9fa2-abc74a8b89fe | -13.42733 | -44.33113 | 2024-10-25 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b26379ec-4cb8-357f-8ac5-e8dde2010452 | -13.29577 | -44.43306 | 2024-10-25 04:17:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eba9b790-6257-3803-a79a-d7c85666d88a | -13.29247 | -44.43252 | 2024-10-25 04:17:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 175d6c25-5b50-3f03-9868-9734bc7915da | -13.24513 | -44.47543 | 2024-10-25 04:17:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4520b3f8-8576-3b1a-9b5f-210aef2836ec | -13.20845 | -44.27379 | 2024-10-25 04:17:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca6497a2-fdc8-37d8-9f9b-326562c03a1e | -13.00583 | -44.65625 | 2024-10-25 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8010120e-cf1d-31b8-acad-653d94659f65 | -12.99887 | -44.39545 | 2024-10-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac56ca92-8d9a-3a93-97ec-d7ff6c3ae528 | -12.72079 | -43.80017 | 2024-10-25 04:17:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee260b3a-1965-3d19-acb6-08cad6e38262 | -12.67464 | -43.43747 | 2024-10-25 04:17:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1251b4c4-ff35-3fcf-a31c-a1ac77c0144a | -12.67409 | -43.44106 | 2024-10-25 04:17:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fd6738a-f777-3f87-867b-b20ce15a22ed | -12.58665 | -43.83274 | 2024-10-25 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 956c23b3-a6b4-3068-8c57-11b6ad94c7b9 | -12.5861 | -43.83628 | 2024-10-25 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 92044c86-0b8b-3b95-9262-ffb3070ceb03 | -12.58333 | -43.83221 | 2024-10-25 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c786e3d3-b1e7-3955-b619-a72db62f8019 | -12.58279 | -43.83575 | 2024-10-25 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6a369fa3-9f40-3379-8557-2b24d9f962b6 | -12.58224 | -43.83929 | 2024-10-25 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cf9e0428-de21-3609-9c7c-9daf601b0161 | -12.49868 | -43.87324 | 2024-10-25 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5dbfcb3-cc97-3dad-8119-92d4acb8a615 | -12.49813 | -43.87678 | 2024-10-25 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89cd9ccf-6dea-3926-b17d-3578f5aac781 | -12.49473 | -43.81094 | 2024-10-25 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 118a6e52-f32c-32ad-a00e-1b3468e45923 | -12.47039 | -43.79255 | 2024-10-25 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f2d1857-9d8a-3761-82ce-91bdc3573b78 | -12.46984 | -43.79609 | 2024-10-25 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 309bed16-49c9-3f4e-b326-f018a9e546e3 | -12.46707 | -43.79202 | 2024-10-25 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b2c14fe-e893-3176-a823-be9ef2f1190d | -13.74146 | -43.66167 | 2024-10-25 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ef9ac23-ceff-3caa-83f4-b924bb4195a4 | -13.69927 | -43.71408 | 2024-10-25 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0d03b49-6f74-3307-a38b-41beed12edfe | -13.63253 | -43.66253 | 2024-10-25 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dc67b9e0-eb21-3d01-b17f-867165ee676c | -13.62044 | -43.8965 | 2024-10-25 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a026992-08c3-3915-9a6a-c1de5af03092 | -13.57948 | -43.89719 | 2024-10-25 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 322befd0-9697-385c-b381-45ea41a9e70e | -13.55095 | -43.72702 | 2024-10-25 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ab15081-ac6b-3fa7-8554-e1a28c020621 | -13.48952 | -43.97411 | 2024-10-25 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e28369dc-bca2-32be-93ce-59073291dd51 | -13.45422 | -44.07053 | 2024-10-25 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 373dc815-616a-31bc-ac56-73ae2fdb6aee | -13.42079 | -43.78042 | 2024-10-25 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a63c2e9-52f5-3f5b-84d3-01465ec3397d | -13.41747 | -43.77988 | 2024-10-25 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d19fb23-c5b9-3970-a27d-054bb3531ac0 | -13.35725 | -43.92757 | 2024-10-25 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3d7f0a2-6f57-3c8d-b17c-a10fe189b31b | -13.34742 | -43.68043 | 2024-10-25 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8dee1f3a-0c63-3b16-a52c-3f8bb74b6620 | -13.29373 | -43.96474 | 2024-10-25 04:17:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 62893778-dc48-3ba2-8964-4dad094a57bb | -13.29096 | -43.96066 | 2024-10-25 04:17:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 965082a0-3d38-3062-94f0-34d1d71e04eb | -13.29041 | -43.96421 | 2024-10-25 04:17:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8c23b169-2227-3362-91e5-28acf8889582 | -13.28776 | -43.95975 | 2024-10-25 04:17:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ff7b79a2-62b6-3ba9-900c-010fdea7bedd | -13.20983 | -43.95815 | 2024-10-25 04:17:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87350f3b-94f8-3cf9-a5a1-bef4950508ca | -13.01983 | -43.75666 | 2024-10-25 04:17:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27b4af73-7d9d-3ea0-a7d2-fd7a77a4ba8c | -12.88383 | -43.60303 | 2024-10-25 04:17:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad9340da-5c72-32a9-9e8c-084016e6507c | -14.31276 | -43.74442 | 2024-10-25 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67dfbb7c-0c98-36d0-91e2-4e692cc5851a | -13.96112 | -43.71455 | 2024-10-25 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a09f4cb-557c-303c-9937-c5e5375fb79d | -14.16568 | -44.17411 | 2024-10-25 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db1540c8-9c9b-32e4-975b-94da52ebc08d | -14.16514 | -44.17768 | 2024-10-25 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbb17f13-5833-3102-852a-38efa4b3e00b | -14.16182 | -44.17714 | 2024-10-25 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f8f398d-f507-3f88-9c23-22f873bbdc0a | -14.15193 | -44.24136 | 2024-10-25 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f5529af0-3fb7-3784-920f-d6cd4a699a9f | -14.14862 | -44.24081 | 2024-10-25 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcb5c8a3-d60a-3eaa-99be-b209dcdc4141 | -14.12439 | -44.30989 | 2024-10-25 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 134c7c93-1e13-30cc-9a93-2660256a5c8e | -14.12384 | -44.31345 | 2024-10-25 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9d878eed-fc54-3d92-a2ba-827bf5d2f7fe | -14.12162 | -44.30579 | 2024-10-25 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b957f9b-23bd-31e7-8356-7db7507e3672 | -14.12107 | -44.30935 | 2024-10-25 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9f1a1992-a98e-3164-971d-f090d8d81d2c | -14.12053 | -44.31291 | 2024-10-25 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5cbde902-431a-33cc-93d1-8ee9ea509870 | -14.11776 | -44.30882 | 2024-10-25 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8f6eb5b3-ddbd-397a-a154-25800c898685 | -14.11722 | -44.31237 | 2024-10-25 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0dbe8714-7d3f-3a38-9f76-207d2ce15502 | -14.10493 | -44.21563 | 2024-10-25 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 652c2e77-2076-3dbe-b272-e7683f5ed1b0 | -13.80227 | -44.34854 | 2024-10-25 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ade41ffa-ac15-3754-9165-4dd5ec06983a | -9.07357 | -45.05036 | 2024-10-25 04:17:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 938548c3-adad-3776-9b5c-0935a8ce31d1 | -10.08221 | -44.78674 | 2024-10-25 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e418b1d2-adde-348b-886b-bdff7ced52c9 | -10.91952 | -44.5953 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2082a1ff-e846-32bd-b84b-2ee5f8de0dd4 | -10.8801 | -44.54166 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e976ed6a-a001-3bb7-9898-86e5a2a67b4a | -10.87437 | -44.79327 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8eca94ee-ad81-3631-9bc1-c9e555ef6013 | -10.87206 | -44.78518 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 938ddd53-bb71-30bb-9851-1f6b194dddcb | -10.8715 | -44.78868 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c1ebf806-c540-3b39-bf3b-da21a84ca534 | -10.87094 | -44.7922 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 77a2ac8c-ab4e-3a61-8ea5-9f9499543477 | -10.86818 | -44.78814 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README41.md)
