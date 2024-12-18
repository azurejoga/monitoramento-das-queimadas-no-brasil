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
| 2be6384b-2610-3a47-ad3e-95c50f12d614 | -3.77312 | -51.97471 | 2024-12-18 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7261c181-ae7c-39eb-aa4b-cf65e28b0523 | -2.08267 | -54.23251 | 2024-12-18 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6755060-cfee-39d2-904b-08d13967c658 | -4.01455 | -46.93003 | 2024-12-18 04:48:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef905a5b-65cc-34e3-bcb7-bace2f8514a3 | -4.04379 | -46.68119 | 2024-12-18 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42178ed6-a119-3b84-91f2-51e10573abc8 | -4.59342 | -47.9792 | 2024-12-18 04:48:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14455ed2-4cad-3942-bd59-84907660fb8c | -1.62889 | -45.85293 | 2024-12-18 04:48:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6a5eea31-868c-33fe-a4e8-ce018452b2a4 | -3.49927 | -53.95678 | 2024-12-18 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 326f4fe5-489e-376d-816d-58afff987ae1 | -2.9281 | -45.24751 | 2024-12-18 04:48:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6b1e004-23be-3927-a065-0447fba698dd | -1.62293 | -45.86378 | 2024-12-18 04:48:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6144f50-8d95-341e-b1c9-1403422ea107 | -3.24805 | -46.87427 | 2024-12-18 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0a7bc071-955f-32fa-97b2-52846cd80c54 | -2.76707 | -47.3935 | 2024-12-18 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31846d5d-bc57-3937-9c58-41753fad7a06 | -1.11011 | -52.25552 | 2024-12-18 04:48:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a3df91e-4248-30eb-9df4-8388334823d1 | -4.93342 | -45.0954 | 2024-12-18 04:48:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d2b864d4-2611-32b3-aea4-83cbe9eaf0f5 | -4.54538 | -43.29227 | 2024-12-18 04:48:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e68e3b75-18fd-358d-be96-aac87df46aa5 | -3.34964 | -53.84148 | 2024-12-18 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1d7fa7c-3a0e-3c8e-8378-ff0893e7ca49 | -4.97676 | -43.72028 | 2024-12-18 04:48:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ef88fcac-358f-3251-8667-1dee1084ae26 | -5.21897 | -44.90578 | 2024-12-18 04:48:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fff54a71-6077-3207-9280-855587872282 | -4.11402 | -48.12693 | 2024-12-18 04:48:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ad1cc1d-df84-32b5-b63c-2c881d94ba08 | -1.10956 | -52.25903 | 2024-12-18 04:48:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fff96c07-32a6-38ac-9369-6713afb894b5 | -2.14231 | -46.46392 | 2024-12-18 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90318bb9-1cef-3ce4-ad5a-a8cc73b3742b | -3.5777 | -54.55262 | 2024-12-18 04:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3afe12fa-e10a-3566-a524-75284471cd85 | -4.00946 | -46.93658 | 2024-12-18 04:48:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7401b06f-7da3-389f-9c09-5ae1c3ea2536 | -4.01336 | -46.96589 | 2024-12-18 04:48:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c2c26898-825c-3627-a077-6faabd85e9a9 | -2.87346 | -45.24808 | 2024-12-18 04:48:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 379b8e79-7d8a-3404-b1b6-ea69fcd29b5f | -1.54403 | -53.72852 | 2024-12-18 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a196799-bf5b-323d-8c6c-afa3d4e1568c | -2.53204 | -53.95667 | 2024-12-18 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e7f8766-3e29-36f8-bd52-3d206553c5e3 | -3.2395 | -46.87658 | 2024-12-18 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6c41a54a-c41c-351e-90d4-36fa45e71b41 | -4.57582 | -45.88828 | 2024-12-18 04:48:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d5314ad-4c98-3365-8d32-f1cb18cca519 | -3.95158 | -46.9307 | 2024-12-18 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ed63338-dd2a-3636-89e4-dab53fcb55cc | -4.9643 | -43.7182 | 2024-12-18 04:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 00eae51b-d773-3326-b9ab-75ca7ae16cde | -4.983 | -43.7169 | 2024-12-18 04:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 1a2e014d-9cc7-3ed3-9230-7e63ec935c39 | -4.9832 | -43.6938 | 2024-12-18 04:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 0ba698dc-36f7-38f2-b5a3-7264605c1511 | -5.93766 | -48.06004 | 2024-12-18 04:50:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8ba53291-32db-3af3-ba88-74678d5cfe11 | -6.21669 | -46.22155 | 2024-12-18 04:50:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfda069f-bfd3-3d05-a5cd-23ecdcfb3696 | -11.86245 | -43.83277 | 2024-12-18 04:50:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b2801766-21bf-3e88-88be-df11ce59ef0c | -6.63008 | -47.34237 | 2024-12-18 04:50:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b50aea9-163f-3f30-ad79-6ab7b856f3c3 | -6.32855 | -46.13246 | 2024-12-18 04:50:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7cee0054-9d3b-3b82-b298-5d511d8860a5 | -5.94151 | -48.06064 | 2024-12-18 04:50:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 78cd0582-aebd-3dc6-a815-7d2d5c01fbab | -6.6347 | -47.33933 | 2024-12-18 04:50:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1b3fa9ad-eeb5-37aa-a308-c239aa2aa398 | -6.20856 | -46.21601 | 2024-12-18 04:50:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1726accc-ef43-3f6b-928a-f245df848d7c | -6.63416 | -47.34296 | 2024-12-18 04:50:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 975dc103-68bc-3525-843a-cf86a929d68e | -6.19439 | -44.4248 | 2024-12-18 04:50:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 008a1a0b-7a2a-39e7-badc-0f524f3b76c1 | -9.11445 | -49.46803 | 2024-12-18 04:50:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea60f8a8-176a-3840-a765-8fb22a43fa43 | -12.41491 | -43.80265 | 2024-12-18 04:50:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae246f8c-1261-3b04-b18b-3b7986f998b0 | -6.62954 | -47.34598 | 2024-12-18 04:50:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a8e7b3b-b7df-3375-86ba-5531a00a5a82 | -6.22105 | -46.22228 | 2024-12-18 04:50:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6d3d9bc-e499-38ae-a0a1-38ac27bc9593 | -6.18945 | -44.42406 | 2024-12-18 04:50:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa2d78e5-7d33-374a-96f8-b5ca6e64a594 | -7.85957 | -43.0884 | 2024-12-18 04:50:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0c3ccf05-4165-3d31-ab77-9a2ef6af81b2 | -6.63361 | -47.34658 | 2024-12-18 04:50:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d8a8196-3dbd-371f-9e07-fa3d11ef6d1a | -5.94466 | -48.06599 | 2024-12-18 04:50:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e91b096-d8a6-3cbe-a884-3a0174f29872 | -12.40926 | -43.80204 | 2024-12-18 04:50:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a390022a-72ec-3864-9406-9c22a7cdcf61 | -5.94537 | -48.06125 | 2024-12-18 04:50:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 565270f6-6796-3156-934e-0cffe6cb1143 | -6.21172 | -46.225 | 2024-12-18 04:50:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28a8c568-5450-355a-aade-6066ce1bdfee | -9.11074 | -49.46745 | 2024-12-18 04:50:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a71d5e1-a631-35aa-80f4-e15241df5ef2 | -7.15339 | -46.69645 | 2024-12-18 04:50:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3116d082-4ac2-3071-99d2-e409854344d9 | -9.92347 | -59.94041 | 2024-12-18 04:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d97a1d6-71bb-3acd-a462-42d5ac7ff11d | -6.63824 | -47.34355 | 2024-12-18 04:50:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8a77043c-85e4-3e7a-9cd4-2f6ab66f04bc | -11.85731 | -43.8283 | 2024-12-18 04:50:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fc4fd3b0-35e8-3ec2-8cc4-ef209d39624e | -11.8629 | -43.82901 | 2024-12-18 04:50:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 50b9b6b4-8458-3b93-a0d8-8cb869573285 | -6.63769 | -47.34716 | 2024-12-18 04:50:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dc5380ea-e38a-3af0-8923-ce4f3e224565 | -11.85776 | -43.82454 | 2024-12-18 04:50:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c69ce287-3389-323c-b634-ad06af4c3d94 | -5.9408 | -48.06542 | 2024-12-18 04:50:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9bce8d7d-645c-3eb4-96f1-82b76d70cd87 | -11.85686 | -43.83205 | 2024-12-18 04:50:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 82be7f77-2387-3fb4-8783-d93635e92130 | -12.33486 | -43.6781 | 2024-12-18 04:50:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 822aeb61-4876-3152-ada9-c9e9761e5d40 | -7.15279 | -46.70053 | 2024-12-18 04:50:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0c39b46-2e6d-3861-aada-18917628ab21 | -6.21729 | -46.21745 | 2024-12-18 04:50:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94726fbd-6f36-3681-aa72-4bed96c34c05 | -9.92137 | -59.92616 | 2024-12-18 04:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 33e786b3-d14b-375a-9a68-252ed32876f4 | -12.34054 | -43.67878 | 2024-12-18 04:50:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5bbcd0d-d058-33e5-ba3c-08de056083f9 | -6.19347 | -44.42347 | 2024-12-18 04:50:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 819d4b10-2af2-37af-b69d-829dd4af4150 | -18.15171 | -54.63533 | 2024-12-18 04:53:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c7ecc6f-85af-3fcb-8c5a-bf2044425aa3 | -20.77219 | -49.84798 | 2024-12-18 04:53:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a410ca4e-c0be-33ed-9458-71179761f6f8 | -15.24007 | -59.92809 | 2024-12-18 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3eb95268-c3e6-39e3-8d01-d5729896fd32 | -20.15757 | -47.39572 | 2024-12-18 04:53:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9dc0782d-2f12-30b1-b6a9-5402247fe520 | -17.76759 | -56.32454 | 2024-12-18 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 157e4800-a37c-3700-8b20-05debc049cb3 | -20.78016 | -49.85308 | 2024-12-18 04:53:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3a69a007-97d7-3a71-9e96-45d690737ea1 | -15.23872 | -59.93555 | 2024-12-18 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02d6c95d-0fc8-3423-976f-cfabc376dc54 | -15.23398 | -59.9385 | 2024-12-18 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a808cf92-5464-3ccf-ae33-f1e941085b6a | -15.23465 | -59.93476 | 2024-12-18 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09ce1d8f-577e-3bba-828f-54f46e7fb78d | -15.24074 | -59.92436 | 2024-12-18 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4c96710-f51f-3264-87a8-e313ec002c96 | -19.06104 | -52.85867 | 2024-12-18 04:53:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d590aa0c-5d2e-328f-bdb2-863d47817fa9 | -13.32288 | -52.41493 | 2024-12-18 04:53:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d16862c6-b824-3073-9acd-4b4c0b72f159 | -12.01612 | -62.79813 | 2024-12-18 04:53:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79e77713-c0d1-3820-a50f-1ebb4c28b1b0 | -19.06454 | -52.85921 | 2024-12-18 04:53:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1dbf0f5a-3e9b-33aa-9c32-bb11dbde9726 | -19.66783 | -49.15102 | 2024-12-18 04:53:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eddbb864-e1e2-384d-b8dd-90dc3f6535ea | -19.05753 | -52.85815 | 2024-12-18 04:53:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4272e3e-0c4b-314b-9dda-f021fd963565 | -19.76588 | -50.95338 | 2024-12-18 04:53:00 | NOAA-20 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ecd1d2ac-12fa-38d7-876b-f610ddc20b7c | -24.24287 | -50.74202 | 2024-12-18 04:53:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 76628e42-4f2f-393a-9069-847da20c939d | -15.07727 | -59.64587 | 2024-12-18 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a32b8f4-4f2a-349f-bcec-6c3905449a08 | -15.4563 | -51.81372 | 2024-12-18 04:53:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9e59867-2d63-3618-be99-aedce44f1c31 | -12.90814 | -55.04865 | 2024-12-18 04:53:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| bed2dbf5-4bda-363e-868f-21536ebaf830 | -18.89625 | -56.05132 | 2024-12-18 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 39e95ee6-4f0c-3aa0-b184-db27e98b8036 | -19.06046 | -52.86278 | 2024-12-18 04:53:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab291863-9921-319a-b011-b9193ae2855b | -12.90479 | -55.0481 | 2024-12-18 04:53:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 125787bc-1ed2-3da6-89eb-ba937dbbeb43 | -15.87715 | -53.27328 | 2024-12-18 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9406a7de-c90a-39db-bdbe-97222a225141 | -19.47599 | -54.89327 | 2024-12-18 04:53:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13348305-5374-3edf-b4eb-7c2f3671e41c | -19.05695 | -52.86226 | 2024-12-18 04:53:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb2dd40f-adc5-32ec-8dd8-a55c257be41a | -15.23532 | -59.93104 | 2024-12-18 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed04a72c-876a-387c-b831-34de1eaaca45 | -15.08528 | -59.64746 | 2024-12-18 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d00ba3d6-fd12-303b-b8bf-8ab464bfd5bf | -15.45277 | -51.81318 | 2024-12-18 04:53:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92f08660-c5f0-3f5b-a9af-e2cb55ce7958 | -15.09122 | -59.63737 | 2024-12-18 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README20.md)
