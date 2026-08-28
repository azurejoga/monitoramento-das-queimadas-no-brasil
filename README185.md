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

## Dados Diários - Página 185

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce41e2e7-9841-3dc4-80f9-8a239c190811 | -5.2448 | -43.7225 | 2026-08-28 20:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 198acb9f-e561-3229-883b-947dac267ab7 | 0.1367 | -60.393 | 2026-08-28 20:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 08cb4c70-5742-37cf-b4c4-b3463f456f04 | -10.5711 | -59.6149 | 2026-08-28 20:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 9b7b8b36-06b0-3dca-abca-5a36de3c0fe3 | -8.0113 | -48.0161 | 2026-08-28 20:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 209.9 |
| 3e8dc80f-fc87-3b57-938f-35d7416dd631 | -4.282 | -48.2007 | 2026-08-28 20:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 2817cb35-973f-3850-a44b-0c2b31d56838 | -6.3467 | -44.0782 | 2026-08-28 20:50:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 212.8 |
| 9d946f17-afe4-3f4f-ad85-24c6ca65d930 | -9.1525 | -49.9639 | 2026-08-28 20:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 34f5f2ee-c857-3335-8d29-acbfe0027563 | -14.1835 | -52.8456 | 2026-08-28 20:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 0b2206b4-6603-3b23-ac90-00ca0802d1e6 | -5.7799 | -57.58 | 2026-08-28 20:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 69278f64-ba61-3d3d-b012-599378ac5d37 | -6.7247 | -60.0189 | 2026-08-28 20:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 168.7 |
| b20d0d6d-99ad-3332-825f-8aa1736f80d4 | -9.971 | -53.9214 | 2026-08-28 20:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| d1e7f519-8515-39d3-a670-eaaad9bc0952 | -14.9015 | -52.6055 | 2026-08-28 20:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| df0a0c95-b3a0-3ef7-b902-d613a15d0f75 | -9.1425 | -61.0069 | 2026-08-28 20:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 940b0568-c1c3-325e-b1a9-1c6eb61e8683 | -14.9386 | -56.3216 | 2026-08-28 20:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 3d964de4-28ab-30fc-a5a1-c93ad1894329 | -6.6396 | -53.1934 | 2026-08-28 21:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 8bf48b11-5af3-3a4c-9a07-9ce2f03c769f | -6.0004 | -57.6884 | 2026-08-28 21:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 8975913a-0514-3e71-bb84-bfc4c8294ede | -10.7598 | -54.0179 | 2026-08-28 21:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| ec71f897-1a1a-3104-81b3-89767868f85e | -7.5516 | -70.0146 | 2026-08-28 21:00:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 3963074c-f264-3065-9a09-ec3bcc028b54 | -4.0574 | -56.2865 | 2026-08-28 21:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| eaa9f1ec-19b7-31b0-9d51-926f26e91e7f | -7.529 | -61.3635 | 2026-08-28 21:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 978d0b15-0f00-3c33-a862-b0a6dd911a67 | -6.6397 | -53.173 | 2026-08-28 21:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 03e33a1c-099b-34cc-bb41-c32c6966bebc | -5.7799 | -57.58 | 2026-08-28 21:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| a9738629-0c94-360a-ad87-f39235550235 | -5.9819 | -57.6892 | 2026-08-28 21:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| b1a78b91-7674-39ac-a677-8dbb0966b976 | -9.9288 | -60.4277 | 2026-08-28 21:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 579.8 |
| d3d313d6-b657-334c-8749-7236657df85c | -8.5971 | -54.7553 | 2026-08-28 21:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 2927fa3d-25b0-3875-8d41-c71fd1534b71 | -14.4856 | -58.5074 | 2026-08-28 21:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 9712affa-608e-33ad-8700-9df0ad4969b6 | -9.9287 | -60.447 | 2026-08-28 21:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 299.7 |
| 954498c4-fd7d-3d23-84c4-a721d371bff1 | -14.9193 | -56.3237 | 2026-08-28 21:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| edb72229-2690-3881-8084-61b97fe41575 | -12.3799 | -50.6038 | 2026-08-28 21:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| fe39e956-f53f-382f-9524-cc777e2b4c5d | -5.8711 | -57.752 | 2026-08-28 21:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 0b79206b-058f-3072-9553-49f6cd45b167 | -7.5661 | -61.3239 | 2026-08-28 21:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 4740da7d-bb81-343a-adc9-1c97624da637 | -7.2993 | -49.9676 | 2026-08-28 21:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| ec7daf08-4294-370f-a3a7-f7ae0bfbf922 | -8.0301 | -48.0145 | 2026-08-28 21:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| e3497fc2-e909-34ae-a939-83cbda4ddbdf | -5.871 | -57.7715 | 2026-08-28 21:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 65361360-c942-3f3d-8de1-f86598721afd | -5.8894 | -57.7708 | 2026-08-28 21:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 272.9 |
| 0c31d935-9e45-392f-a32d-10e88066f70c | -14.9579 | -56.3195 | 2026-08-28 21:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 6f2239e1-ee1e-36dc-b127-bd7a8a565127 | -15.577 | -56.2916 | 2026-08-28 21:00:00 | GOES-19 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| c78ab7eb-58ca-34c0-8b6c-2bba70776bbd | -7.5662 | -61.3049 | 2026-08-28 21:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 313.8 |
| 13f5ea4e-5dd0-3391-bebf-e06a6ac901e7 | -9.9475 | -60.4267 | 2026-08-28 21:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 199.6 |
| 5f7adf28-3e54-3698-be83-c3e6f89e2c5e | -14.2027 | -52.8432 | 2026-08-28 21:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 6c21fa6a-3e17-3701-b1b3-b94424744814 | -9.1425 | -61.0069 | 2026-08-28 21:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 0b86672c-7363-3dfb-aff8-9c441797b1ee | -3.6033 | -60.5474 | 2026-08-28 21:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 1723d5a0-0cec-33df-b763-833316e530b0 | -8.6012 | -70.2192 | 2026-08-28 21:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 991bdd0b-d119-30a6-b2c5-f8c0df876660 | -9.8739 | -60.2955 | 2026-08-28 21:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 1214d43e-fe4e-38a2-ad3a-193980cdb5b0 | -9.8028 | -46.373 | 2026-08-28 21:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 2dff9b4d-ec2b-3375-b3a5-7c26a7eee454 | -9.5375 | -66.782 | 2026-08-28 21:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 5afaa9df-01a5-339f-988e-c4dacf95ecfc | -12.399 | -50.6015 | 2026-08-28 21:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 0b676811-c4d2-33d8-9354-74a5836775bd | -7.5477 | -61.3247 | 2026-08-28 21:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 7934e54f-4734-3092-a291-c82b800b9538 | -11.7167 | -54.5244 | 2026-08-28 21:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 127.6 |
| 547ae279-f554-3825-963e-8746e41ebb2f | -6.8757 | -59.3978 | 2026-08-28 21:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 61f71b28-0c3d-392f-aa98-dd0b1eee59aa | -8.0115 | -47.9943 | 2026-08-28 21:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 184.8 |
| d9c2258a-8523-3d0f-8c8e-46e098757ba3 | -14.9389 | -56.3011 | 2026-08-28 21:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 648027d0-ab0a-36cf-b16d-94b6542841ad | -6.1472 | -57.7995 | 2026-08-28 21:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 6593dfa5-7742-3c27-98c6-495a1ca5a6b7 | -9.9102 | -60.4287 | 2026-08-28 21:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 3c8bc432-8e12-3c09-9aa1-b89db9040724 | -6.7248 | -59.9998 | 2026-08-28 21:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| e5ff2426-11ba-330f-b2f7-3b2c7a622745 | -3.6216 | -60.547 | 2026-08-28 21:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 3f6b76f5-48ec-337f-acbb-f8e1ff40f635 | -6.8572 | -59.3986 | 2026-08-28 21:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.9 |
| ca40e3e1-4b5c-3c0a-bef9-00f0dba5958b | -7.5478 | -61.3056 | 2026-08-28 21:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 299.3 |
| bcac9483-c91f-3216-b099-72b0e8a15a07 | -9.9708 | -53.9419 | 2026-08-28 21:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 109.1 |
| c87dadb2-1faa-3112-b71e-09681e00e45d | -2.7304 | -47.0424 | 2026-08-28 21:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 68fa8d98-1cd5-3439-87bb-0ea87658b18f | -8.0113 | -48.0161 | 2026-08-28 21:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 215.1 |
| 2e9f6efc-b568-338d-a508-12efd1f4bb16 | -14.9582 | -56.299 | 2026-08-28 21:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 99.8 |
| e63540e3-27d2-351b-b063-4341ea66b575 | -6.9336 | -58.9514 | 2026-08-28 21:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 981e1380-23b2-35ff-8c4e-4db4496fee1a | -6.949 | -59.4719 | 2026-08-28 21:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 6569fa28-dff1-32d4-8ef0-c6f9f2833802 | -6.7652 | -63.054 | 2026-08-28 21:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 109.8 |
| f6c96060-9b23-37c6-8316-ca6e104e3656 | -6.7247 | -60.0189 | 2026-08-28 21:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 133.9 |
| 95af5bb4-ed8f-3e08-beef-7532e27ffd0c | -11.7165 | -54.5449 | 2026-08-28 21:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 3c6de4da-18fb-3b56-be0e-a688ad366600 | -6.1656 | -57.7988 | 2026-08-28 21:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 9e6869ef-94cb-3dfd-9280-10e1f35cfa21 | -9.0198 | -57.5574 | 2026-08-28 21:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| c9dc2ef9-a6a6-3da9-94d1-2be875f6e0dd | -9.9474 | -60.446 | 2026-08-28 21:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 0efc8f2e-a7b7-3d1d-9a6f-0e9278485711 | -11.1916 | -51.2708 | 2026-08-28 21:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 71279586-d2e4-3090-a954-7e2fb5d74656 | -9.971 | -53.9214 | 2026-08-28 21:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 65a12b9b-de73-3b58-b7b0-844196801985 | -4.1934 | -54.5755 | 2026-08-28 21:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 70b1c736-b5e6-38d8-bbd0-a3eb03ec2d4d | -14.9386 | -56.3216 | 2026-08-28 21:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 133.3 |
| f1ff4e0f-c65c-372c-bd4f-0eb6dfaa8f39 | -9.8737 | -60.3149 | 2026-08-28 21:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 68f806d9-6924-3cfb-a952-e5bb654ff3ed | -8.5969 | -54.7755 | 2026-08-28 21:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 2059d412-20f0-3b81-84aa-7772f6876a58 | -7.4953 | -55.2862 | 2026-08-28 21:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 1923e805-e427-3f8f-97be-2cd5dc316598 | -14.4859 | -58.4874 | 2026-08-28 21:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 6954c685-60cf-3fff-8031-4f0a7c893a1d | -5.9079 | -57.7506 | 2026-08-28 21:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 98dd068b-1abb-3fbb-836c-f8cc3547755b | -7.5516 | -69.9963 | 2026-08-28 21:00:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 154.3 |
| 67b76f97-5a03-3759-9a05-fefb53470a74 | -6.9521 | -58.9506 | 2026-08-28 21:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| b56123d2-e977-3aae-8a29-33aefc0f6619 | -8.5968 | -54.7957 | 2026-08-28 21:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 13098b9c-19fd-304a-a410-ccadbdb65918 | -5.8895 | -57.7513 | 2026-08-28 21:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 306.4 |
| fb9381ba-ff0a-30fc-8ca0-3beef57a23fc | -6.1657 | -57.7793 | 2026-08-28 21:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 50644ba7-b34e-3d18-906b-e02a98313c6e | -9.929 | -60.4084 | 2026-08-28 21:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 125.1 |
| d40ab8a3-0781-3f2e-80cd-00a41e17b653 | -10.7596 | -54.0384 | 2026-08-28 21:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 139.5 |
| 73f4be45-d165-3075-8075-eb828dd9fe11 | -9.5375 | -66.782 | 2026-08-28 21:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| bcc76cbf-e4cd-38b8-8ae0-971e5404999e | -6.8757 | -59.3978 | 2026-08-28 21:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 34cea2db-4eca-3078-971c-2ed0d52e7602 | -6.7653 | -63.0352 | 2026-08-28 21:10:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 602641f4-236a-3e30-9519-121d882c973b | -5.9819 | -57.6892 | 2026-08-28 21:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 6461d46b-7744-3bdd-80eb-998e035937ba | -6.7652 | -63.054 | 2026-08-28 21:10:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 4fc58776-cc49-313d-bdc9-5ffaed0622a5 | -8.5968 | -54.7957 | 2026-08-28 21:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 67a45e7e-4aaa-3534-87de-de08806610d6 | -7.5661 | -61.3239 | 2026-08-28 21:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 95ca5fce-dd7d-38b6-8d38-2c87771f0be6 | -10.5523 | -59.6161 | 2026-08-28 21:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| dff0b456-395f-3f58-b037-14773d1fdfa6 | -10.7596 | -54.0384 | 2026-08-28 21:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 124.8 |
| e70116a2-2169-32dc-b574-ba5878eb89b2 | -7.5478 | -61.3056 | 2026-08-28 21:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 209.6 |
| ef436d86-9185-369f-a699-2065778fafef | -14.9011 | -52.6267 | 2026-08-28 21:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 12a53d16-03ee-3efe-9953-be94e67a3807 | -6.77 | -55.6445 | 2026-08-28 21:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 166.1 |
| cb491dc0-fc7e-3abd-9486-f119cb21124c | -14.9193 | -56.3237 | 2026-08-28 21:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 00dc6685-d621-3c75-8a18-335cf01b8dce | -8.5173 | -55.3441 | 2026-08-28 21:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |


[Clique aqui para ver as próximas entradas](README186.md)
