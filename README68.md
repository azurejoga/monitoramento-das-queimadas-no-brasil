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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b11f050f-b515-31e6-8659-877d40ad4b49 | -10.09639 | -68.26584 | 2026-10-04 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0d5c8c5-667b-3fb2-b5eb-66eb837a771c | -9.02106 | -65.69793 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89389f99-1e75-31da-a8ef-8400943d321c | -9.09033 | -63.98165 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f2206138-6815-3f6c-8503-0fb7038ac1f1 | -9.89264 | -65.00991 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| beb20040-dfba-3595-9267-9cdbd20fb7f8 | -9.47799 | -64.33015 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da00a120-d825-3e59-9ec8-486a8106aa00 | -9.01347 | -65.69309 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3af07e24-5e6a-3afc-9fde-6a33e9b43f35 | -9.4729 | -64.334 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 443c61c0-55a3-3451-9a04-5deea1598203 | -9.92845 | -65.03597 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18c6ff01-9005-3ecf-9fd6-bb8697723196 | -9.0345 | -67.47117 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d574add1-1432-379f-bc23-f0387626bb91 | -7.75896 | -72.37892 | 2026-10-04 06:01:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c6e53a2-2e66-34aa-a1e4-b4f44e944665 | -8.05002 | -67.2729 | 2026-10-04 06:01:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bdfa4b6-7fbd-31e8-9524-c154b75ecedc | -9.92415 | -65.03539 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7cf5142-6566-3f11-898a-b871ccb7e370 | -9.82164 | -65.05964 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85fd953f-1261-3406-834f-a7fed31b0e30 | -9.01802 | -65.69004 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e9359f3-cb3c-3027-86de-189b8b0f1489 | -8.55553 | -67.0657 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 29b9d5d5-e073-33ed-b27c-d813807a3bed | -9.01752 | -65.6937 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f335bee1-364d-3b6c-9de3-977d530fd12e | -9.46843 | -64.33338 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89b44d77-1d21-38cb-a7ef-73f74c55e548 | -9.1542 | -65.39354 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85191c46-a488-3725-ad7e-21fb18ebd851 | -9.01701 | -65.69733 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69f4835a-0ad9-33dc-a5c7-c114b17f55fd | -9.15368 | -65.39732 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd375caa-892b-34e0-ae63-39660be84edd | -9.47676 | -64.3391 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c288ed9-e183-322c-8c02-82408219ce13 | -9.12959 | -65.89973 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 77d30555-98f3-38b1-a175-62f3984f2471 | -10.9547 | -60.90973 | 2026-10-04 06:01:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d5c18ce7-91a1-3dc0-b9d7-e1897d38db70 | -9.05413 | -65.42872 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0b14ae3-101d-3e8f-bf0c-ef375eddb0ca | -9.26078 | -65.85324 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2dc953d-a468-305a-92d7-05f59b9249a5 | -9.01296 | -65.69673 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47964589-9814-382d-8cb0-b5d36926348b | -8.56973 | -66.99503 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3df7f042-c754-30d5-8bac-462470da0841 | -9.17003 | -61.40757 | 2026-10-04 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 166732b0-4dab-3911-8331-e4c73c047479 | -9.15193 | -65.39317 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b87d3853-51de-336f-b6e7-524bc7ecdec3 | -8.59259 | -66.81344 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6d8257eb-aeb0-31eb-9819-93419493d507 | -8.57998 | -66.82092 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| db1bcfc2-41de-3b17-b609-e325aaad0819 | -9.92731 | -65.04412 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a24d5bc7-9054-345c-8147-cb75afe39562 | -8.52188 | -67.11485 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d634fab-8f39-3008-a0c3-34d48dace1ea | -9.43994 | -68.93493 | 2026-10-04 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb9050e5-1e66-38c4-9d1a-45d4d8cd9a54 | -8.85964 | -66.78942 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f06d5682-e678-391f-a182-88126bbae2b1 | -9.91614 | -65.03007 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7775558-a417-31f0-9845-51d4330ab05e | -9.6252 | -64.17643 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 275c1d0d-ed55-3a4c-91b7-1294281d4244 | -9.60667 | -64.04045 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0422b33f-1955-3bd9-9aad-643eee95a090 | -8.7365 | -66.57097 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ff6fb3e-d60f-323e-a8a3-3256b6658c26 | -9.46395 | -64.33276 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8260e52-ba2f-3563-b9a5-f48205543685 | -9.54525 | -64.81493 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cea5fbe8-4eff-3a9b-91bd-106f4813a0e3 | -8.44192 | -70.11152 | 2026-10-04 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11d6283f-78dc-3b3d-ac85-5741db315732 | -10.03124 | -65.25959 | 2026-10-04 06:01:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a66f355-1a00-3bc1-9f2b-23459968ad65 | -8.74032 | -66.57155 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c136d3fd-fb5d-3f55-90db-72c46b2bd8c9 | -9.92246 | -65.04762 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8f15f78d-fbea-3872-bfba-2ae40c285ae6 | -8.05156 | -72.44056 | 2026-10-04 06:01:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbbda469-d406-3c99-8daf-c2ccde837448 | -9.91671 | -65.02598 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21851304-15fe-3139-8ce1-b7b8748a53c3 | -9.12153 | -67.83897 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05f0e3bd-7032-3417-9a1c-7b40de83a36a | -8.59326 | -66.80886 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5e7c8b6b-1063-3bcc-aa9f-03244478b1cf | -8.89159 | -66.8883 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa5b9ddc-6d16-3d85-9cd8-6d2ab6f462ff | -9.47737 | -64.33462 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 442d0c3f-6ce4-355e-a5d8-60c327d0d79c | -8.89478 | -66.73282 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a7d51bfb-3690-3248-bb5d-1e82bd4d48f8 | -9.92901 | -65.0319 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7793e85-0a20-3880-8dbc-85f868221ffb | -9.13064 | -65.94995 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3d9442b-de07-3e85-be5c-8ca12dc9b44a | -9.5473 | -68.52496 | 2026-10-04 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e920a7f-bf19-38e4-89c7-d54b14671b7f | -9.91129 | -65.03353 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dfa34f7e-6fd4-3094-87d5-a8c656c4f319 | -9.9193 | -65.03887 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 681625a9-f098-3448-863c-9ffef15c130d | -9.37607 | -65.47347 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 979b1af0-9dd0-30ef-bd02-b54bb5073ac0 | -7.42215 | -70.10788 | 2026-10-04 06:01:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd01edf2-eea8-3d07-9c9a-6af184d74ab5 | -8.51514 | -67.10933 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ddf6ac20-4a93-363a-8f20-86a3f3db914e | -9.08934 | -61.15665 | 2026-10-04 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc1d01c1-0e13-3d0c-bf5a-4e13fa7c4184 | -9.59704 | -63.52752 | 2026-10-04 06:01:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf22211d-33e8-319a-8048-58d188cfc405 | -9.08888 | -61.16028 | 2026-10-04 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 39f0454b-ddbd-3954-9305-9c5a41eac22f | -8.61001 | -66.96713 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bb3dc37-0b50-34cc-a3f1-84abc98ff07d | -9.17637 | -67.73108 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da4e4e4d-7dd7-3821-a61d-c118b5274b4f | -8.5769 | -66.81577 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be7b4f0e-4ad0-331d-8eb6-21ca31baab56 | -9.13562 | -65.94353 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4703d57c-97a2-3c20-be74-ea27f6565c3b | -8.65688 | -66.93272 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 121d4fe6-d061-3ea0-8455-84a52fecd653 | -9.13114 | -65.94642 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4abfe101-de1a-3080-a560-88996be91819 | -8.55618 | -67.06127 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c9f8b60-9291-3b86-9ffe-e4ccf85d53e8 | -9.1307 | -64.4045 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83eb59e5-a3c4-3a7b-afa0-3cfa25ead442 | -9.01651 | -65.70096 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23ebf4b7-2548-3a16-87f4-64995cf469e1 | -8.54657 | -67.02348 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11963ffd-edcc-36c0-b97b-71133d165999 | -9.12956 | -67.92676 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44dd67d8-0450-3e99-b64f-ba145ad9a76a | -9.89208 | -65.01402 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a6df00b-c835-3fe9-a78d-1786d5a4ba37 | -8.96286 | -62.3485 | 2026-10-04 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9c1bf64-c1e7-31ba-9775-b363b346f2e0 | -8.58821 | -67.14565 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d89c9e27-d451-368a-9f2f-c7d400888325 | -8.58948 | -67.13686 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3121e08f-33db-3260-872a-9f5ed342d98c | -8.88783 | -66.88774 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 993fa6b7-afa7-3119-8613-c14ca96d63b2 | -8.59702 | -66.80941 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce91655b-3bc8-39dc-bf41-4daae8b951d0 | -9.01397 | -65.68943 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e835df8b-71e3-3345-8f38-3c1f8681e07f | -8.89099 | -66.73228 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 191b9094-f0ee-34a3-a9c6-45b562bcb5be | -8.58885 | -67.14125 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ae1888d-bd09-3e0b-af4c-efcc44c0da46 | -9.13463 | -65.95055 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84e001a6-3bf4-3b78-b459-af601fa19242 | -8.56293 | -67.06682 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f119a06a-674e-3c7e-9010-8cfa753685aa | -9.13312 | -67.9273 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfc3d0fd-13ec-3774-ba1b-854eb0e61f91 | -9.47229 | -64.33848 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5edb8df-8c44-3e53-ac29-3bed4aec3a8f | -9.45613 | -68.04348 | 2026-10-04 06:01:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 983d5469-b6be-3cfb-adcc-8763ab53fc34 | -8.54312 | -67.07289 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94d1e49e-9ffe-3a72-8f57-7e9dc7aba436 | -8.88186 | -66.76902 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0aae61b6-ba76-35d2-b2a2-6582a3676826 | -9.13692 | -68.24464 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77410206-c789-36a0-ba9a-e2fcf71d3865 | -9.11136 | -67.71014 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32ae2c47-d3b5-3de1-89fe-24162223f4dd | -9.54323 | -68.52833 | 2026-10-04 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b40e137-f7e7-3c20-8902-989416c972e3 | -8.51755 | -67.11869 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 171da50b-2bb0-3a4e-bf8b-54ee572afb8b | -8.59635 | -66.81397 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0bbd9c72-6129-3626-92c6-e07eaab77fd3 | -9.8882 | -65.13788 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 72f3f0db-344e-35c2-8c2a-e9d80e5aecc5 | -9.02157 | -65.69429 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 634728ae-970b-3c46-a8e2-91a7242035e5 | -8.34762 | -62.82794 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5fc5f1a2-f160-3be5-bff8-489165e96917 | -8.55248 | -67.06071 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a1c7a410-b10f-360c-b92e-a31b6fa295af | -9.12559 | -65.8991 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README69.md)
