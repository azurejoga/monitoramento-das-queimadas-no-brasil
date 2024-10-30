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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ac2eb55-17bd-393c-9854-b1482fca0946 | -19.48397 | -56.64592 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3d876fe5-de4d-3419-bede-664c3e3dc9cb | -19.48333 | -56.64902 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e8ad824a-d4ca-3557-9bf9-6475e2336653 | -19.48268 | -56.65212 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0d0a57e3-c17b-34a1-b626-437e1766ce33 | -19.4825 | -56.67815 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3fe4f7ef-b088-335f-9125-a1cbbc27605b | -19.48138 | -56.65832 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 03f3aa40-9eac-3833-927a-b5ae29c0a329 | -19.48073 | -56.66142 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| e0083c55-05cc-33b8-b9d1-6707e5a52354 | -19.47747 | -56.67698 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9e29e504-5784-37e0-9f0d-03c37a0b2fcc | -19.62147 | -56.71269 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 59d5f384-a86c-3a95-84d1-47d4c2c44b26 | -19.61643 | -56.71152 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| c8a2df4a-404e-34a4-abaa-8910ff4c338e | -19.61579 | -56.71463 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 1b210784-4d64-3cfc-a526-67040a136c1c | -19.61514 | -56.71774 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 1e6e3610-983c-3144-ad84-7eeb94e16627 | -19.6114 | -56.71036 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| bb9fe414-5814-35ce-883d-c05f05eedf6f | -19.61076 | -56.71347 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| f25c37a8-321a-359f-b2e3-abb07d970b9e | -19.61011 | -56.71658 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 5f8ab2b7-b8ba-3b54-ba93-26cb226cd9f2 | -19.60573 | -56.7123 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 6eda1aff-d949-3156-b7f1-dbd78afe5277 | -19.60508 | -56.71542 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 97c7d9cd-a63e-3947-9c38-4e3216ea4163 | -19.60443 | -56.71853 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| c5c35c2a-4763-399a-b2ed-d30639ab972d | -19.6007 | -56.71115 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| cfef5094-6cef-3346-85dd-a4e1be822c01 | -19.60005 | -56.71426 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 51ed9173-e8c6-3e70-a9d2-10daf2fb625e | -19.5994 | -56.71738 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| b5a61a0c-ead5-3dab-97a8-81f85f5b7223 | -19.59875 | -56.7205 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| f269a152-c68b-3f8d-b15c-a7f35e656d54 | -19.58998 | -56.71194 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 5cdec79f-446f-3885-a5fc-0029cfaacd3c | -19.58933 | -56.71506 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 81b60648-1c3e-3104-b983-516c4644ffa3 | -19.58867 | -56.71819 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 031d3c21-b10c-3dfe-ab89-283c6ea0c2f2 | -19.58802 | -56.72131 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 76ea6763-9f41-3eb7-af14-010244c6c1ed | -19.58495 | -56.71078 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1813f88d-0634-3a8a-b17e-b886926c9783 | -19.58429 | -56.71389 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| d3ce9862-9d3f-3ef7-9d70-10f1fcb8ba0f | -19.58364 | -56.71702 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 79b17290-c920-3c66-9475-81693db56842 | -19.58299 | -56.72014 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 378a2dbf-6253-3381-8407-1de8719b18c3 | -19.58233 | -56.72327 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 777e9157-3215-3fed-98b8-74abcc8c7bcb | -19.57926 | -56.71274 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| ff9848de-600e-30ba-9f13-ab0eeef9b0d5 | -19.57861 | -56.71586 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| c2cdbd5d-e361-37af-b316-9c0e68b8b0c0 | -19.57795 | -56.71898 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| adb11092-3dc4-359a-8dc5-7146269e6cb4 | -19.5773 | -56.7221 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 5232adc5-6158-3937-a2ee-a94bbd813c26 | -19.57664 | -56.72523 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 982de562-5446-3766-8fed-db49c50c1a74 | -19.57422 | -56.71158 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| d882b6fe-8c55-3bb6-b895-b15d8a3ca891 | -19.57357 | -56.7147 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 893544b0-89eb-3a5d-8385-529aed196047 | -19.57291 | -56.71782 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 4c9076e2-c84b-3405-8379-0856e6223e07 | -19.57226 | -56.72094 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| c59b912c-36fd-32be-bc24-d8261328fb0d | -19.54269 | -56.7109 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 6d27fca8-d413-3720-8956-8859e79964e3 | -19.54202 | -56.71402 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| e58455c9-27fe-3dea-83b9-41facbc1f571 | -19.53905 | -56.71082 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| fad9a7ff-b7e6-301f-9a0c-ae7e1d67f5f9 | -19.5384 | -56.71395 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| b4abbe24-1d33-307e-abf7-553a5c26ec0e | -19.53776 | -56.71709 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 7ec8ae14-3538-35ec-8761-1682c976e21a | -19.53698 | -56.71288 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 1172aea6-efdc-34a4-a48b-d0219994f381 | -19.53632 | -56.71599 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| e8e2e8c3-41dc-3efc-822c-db7070db5442 | -19.53337 | -56.71279 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| ec048119-96e1-3834-8a7d-ab6715b769bf | -19.53194 | -56.71172 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| ae7f5255-9c54-392d-8b66-d652f1ddcdeb | -19.52833 | -56.71162 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 6c982bea-18b1-31e8-aab8-a1050b37213c | -19.5269 | -56.71057 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| e99b3b09-05e1-36bd-bba4-3af4bd7ac172 | -19.52624 | -56.71369 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 0195b2ec-533a-3a1e-b320-80872317299d | -19.52329 | -56.71046 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| a99a20a1-9e41-3237-9907-def12e51388b | -19.6234 | -56.70335 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0127fb92-449e-3700-ae3d-bdca102b992b | -19.62275 | -56.70646 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 805f2ee8-56bb-35ee-83ce-9f0b3b05c2c6 | -19.62211 | -56.70958 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 56da550c-d15e-32e4-9296-370b13778fe7 | -19.61773 | -56.70529 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 419b5234-b851-3d2d-954f-84ad1a73ccaa | -19.61708 | -56.7084 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 89a37c58-a852-3142-a697-76206eeceb09 | -19.6127 | -56.70413 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 9debfa52-d600-3eeb-96ea-74cc361fe2de | -19.61205 | -56.70724 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| c8474206-963a-3170-99e5-235d846dd38b | -19.60767 | -56.70297 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 58d06b11-96b4-304a-b5ba-08560782d7a5 | -19.60703 | -56.70607 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 06e7bc61-d143-39fb-807a-39ee6de85b1a | -19.60638 | -56.70918 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 574d356a-30ac-39b2-9a5f-5026ae5c6819 | -19.60199 | -56.70491 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 46a52dc2-3322-305e-8c55-9fae2b864757 | -19.60135 | -56.70803 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 6bda4db4-5ee8-3a9d-8f02-7115c9b97d5e | -19.59696 | -56.70377 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 9fa53543-048f-36e3-8809-280d364a83ea | -19.59631 | -56.70688 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c3a26630-7df8-3dc6-a4f7-2a9a03a8c1c8 | -19.58625 | -56.70455 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7f04e3fc-4e76-370b-8e2f-f297bd7f1b8b | -19.5856 | -56.70766 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 6ee5cd9b-560f-38c8-96b6-e1568bab1731 | -19.58122 | -56.70339 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7d6ba49f-08eb-30f9-992e-fcf5d49f02c5 | -19.58057 | -56.7065 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1c596474-cc9a-3cba-94f6-a7dd14264e73 | -19.57991 | -56.70962 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| e3ac1b41-9da8-3b70-a919-af35f3b0b3af | -19.57488 | -56.70846 | 2024-10-30 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 19fe2d5a-a135-3b80-bb10-1c3a47f22ad6 | -19.54335 | -56.70777 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1707e422-53af-35d6-b4cf-6dca54fc670c | -19.53969 | -56.7077 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| cc1ae841-e37b-35d2-a074-4a5520195b42 | -19.53831 | -56.70663 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| bdeb53bb-b8c5-3df9-8d5d-67aaafb241ca | -19.53765 | -56.70975 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 5334d7bc-a1a4-3b06-beeb-3a66beea1790 | -19.53465 | -56.70653 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 6a4ec2bc-e858-3795-877b-a084e9ffe3d1 | -19.53401 | -56.70966 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 68b12b77-ec89-3d0d-98bb-c9ac70e0f72e | -19.53327 | -56.70548 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 77d7d153-fdf7-330a-8974-14feb329fbad | -19.53261 | -56.7086 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 5ebb01df-6c10-3a5b-ac67-91b922124286 | -19.52962 | -56.70536 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 5a843a9d-1e84-3d9b-a3c0-5d87951e6c8b | -19.52897 | -56.70849 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a4a2092f-585c-3941-872e-9dfbeb3124f9 | -19.52823 | -56.70433 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b156e71c-6168-379f-97c1-d820fd9435a3 | -19.52757 | -56.70745 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| c97c7fb6-8b39-3b07-9663-9e89b02b182d | -19.52458 | -56.7042 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a16099af-46e7-3713-86c3-284f4751f914 | -19.52393 | -56.70733 | 2024-10-30 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 48b5b9c6-9e90-3fd2-8a62-9941f898ab41 | -17.73849 | -57.54353 | 2024-10-30 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2e93a655-7259-33ab-8cb8-25af0473a020 | -17.73395 | -57.54068 | 2024-10-30 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| bca9f1c6-4393-37d8-8db8-5efa7e44d5d9 | -17.73319 | -57.51666 | 2024-10-30 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 5078da85-ab7e-3be2-b68e-b99d445ff0eb | -17.73316 | -57.54448 | 2024-10-30 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 37a2b5f5-9731-35cf-b1a6-176242820bff | -17.73299 | -57.54228 | 2024-10-30 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f519ea26-fa18-3d1e-ad70-3a923bda8260 | -17.7324 | -57.52047 | 2024-10-30 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| f5a24547-26fd-37cb-80f1-6409eaab223b | -17.73239 | -57.51835 | 2024-10-30 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9ccc6beb-12e6-36c2-a8ac-08d99a470cd2 | -17.72771 | -57.51539 | 2024-10-30 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 72066a4d-5112-3ac4-bc64-a747554f82a3 | -17.72692 | -57.5192 | 2024-10-30 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8dc9c090-2eda-3f32-8d2b-c02437f1edcb | -17.72691 | -57.51709 | 2024-10-30 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| ee18abfd-ee70-372d-9ad4-f58d7a3f6715 | -17.72613 | -57.52299 | 2024-10-30 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 34292f61-33aa-3ff4-865c-13613865bb5b | -17.72609 | -57.52087 | 2024-10-30 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 63da928f-44c0-335f-98ad-4a8a6a63742a | -17.72528 | -57.52465 | 2024-10-30 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 5e0ce343-4f0e-3973-89b3-4a3a233d06c3 | -16.8288 | -56.69432 | 2024-10-30 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |


[Clique aqui para ver as próximas entradas](README53.md)
