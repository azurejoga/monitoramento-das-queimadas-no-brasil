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
| 5e7ef71e-f4cf-394a-8e31-4282800ac88d | -9.2275 | -65.5983 | 2026-09-10 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 0f45d822-3c09-3d8a-9aee-39f298616221 | -8.6311 | -66.5287 | 2026-09-10 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 135.4 |
| 148ee5cd-e9e6-3a81-bf35-0a68d5941ffe | -9.7698 | -43.4825 | 2026-09-10 15:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 7770ee57-b504-3284-8a14-2fd525e2ea14 | -12.169 | -64.1404 | 2026-09-10 15:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 4911f3e2-d376-3180-b89a-a49b453dd1f4 | -17.1078 | -56.8304 | 2026-09-10 15:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.5 |
| 15351d09-1813-38f2-ada6-13ea09f47546 | -10.2358 | -45.3004 | 2026-09-10 15:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 308.2 |
| 2b40f2d9-b089-34af-abfc-307b46e5ead7 | -13.2483 | -61.676 | 2026-09-10 15:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 889915a3-f4f5-33e9-8a6d-da5069dfbd01 | -13.2476 | -61.7536 | 2026-09-10 15:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 57.9 |
| a52be287-0011-3f77-b117-269f5907569e | -10.2556 | -45.2521 | 2026-09-10 15:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 145.9 |
| f142f5cc-3c92-3c9f-8aed-f8623c61be8d | -6.7649 | -59.4216 | 2026-09-10 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| e17c03d4-d8db-3326-bb16-9b6782688ec3 | -9.0059 | -65.4186 | 2026-09-10 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 735fdb0a-e6f9-38c8-8af6-8e56aad189d7 | -13.2481 | -61.6954 | 2026-09-10 15:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 9861b01a-0dc8-3f4d-92de-49c56ef7c11f | -8.6009 | -47.369 | 2026-09-10 15:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 654f31ce-4537-3214-9bc1-6d28241d5358 | -13.2479 | -61.7148 | 2026-09-10 15:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 34d30cdc-7855-3266-8a2b-24b4e7195b07 | -13.2673 | -61.6747 | 2026-09-10 15:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 920cbfbb-4bed-3f7e-bad7-e8d57d7515af | -13.2295 | -61.6578 | 2026-09-10 15:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 2e0e4dbf-4735-3e69-a80c-47aa37fdef06 | -8.9875 | -65.4006 | 2026-09-10 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 11f3c1c0-c081-3996-bd89-c1eb7c1299a5 | -9.774 | -47.0693 | 2026-09-10 15:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 0a6dda26-560a-3b2b-b50c-03c7a49c8fa9 | -8.9428 | -63.2797 | 2026-09-10 15:40:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 452efa2e-a59f-307d-9594-556fd3e178ae | -8.9873 | -65.4379 | 2026-09-10 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 154eba1a-e10a-37d1-bc3d-c025f93abf2e | -7.1198 | -42.1309 | 2026-09-10 15:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 110.5 |
| 60e3e1a8-47fa-34fb-aa67-4c204449e37b | -8.631 | -66.5473 | 2026-09-10 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| b9b8c051-c254-3225-bd59-2da756238ef3 | -9.793 | -47.0672 | 2026-09-10 15:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| c0dbe630-3622-3552-8035-c479c8711f87 | -13.2485 | -61.6565 | 2026-09-10 15:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| b946d013-84c2-3eb9-b3db-f228e16e203f | -10.2362 | -45.2775 | 2026-09-10 15:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 255.0 |
| 66dca9da-70d2-3fec-9453-c1908c8ab5a8 | -3.1462 | -60.6506 | 2026-09-10 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 6d336f4c-3d19-3d01-9b43-0fb25d514656 | -13.2284 | -61.7743 | 2026-09-10 15:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 2b0302d2-ea3e-34af-8f23-0e4d95b138ad | -13.2094 | -61.7755 | 2026-09-10 15:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 6b1c1d2d-3fd2-32cc-ace0-6c6ee341c830 | -8.6012 | -47.347 | 2026-09-10 15:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 309.0 |
| 69bccaec-345a-352c-a474-21489a248fba | -8.6198 | -47.3672 | 2026-09-10 15:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 22b9661f-bd12-3a82-9653-109cae0c0929 | -8.0029 | -43.9467 | 2026-09-10 15:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| f96716a7-6843-37f6-9a13-77110bfa0418 | -12.1501 | -64.1414 | 2026-09-10 15:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 47.4 |
| a772e9c6-6445-3448-91d1-1be89e8c99ca | -10.0697 | -46.2516 | 2026-09-10 15:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| e941197f-6738-3b21-b50a-d43804f53ffa | -13.2092 | -61.795 | 2026-09-10 15:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| a2ff085d-62bb-34a7-9655-b3d5c1d07f30 | -13.3298 | -61.1064 | 2026-09-10 15:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 6f461988-3926-376f-8bdb-4870034e603e | -8.6311 | -66.5101 | 2026-09-10 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 228.6 |
| b4b8b4e6-29e7-3839-b081-051f5360385a | -13.2474 | -61.773 | 2026-09-10 15:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 07bf6257-8f53-3898-adbf-24beba33c9d0 | -10.7582 | -45.9397 | 2026-09-10 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 268.9 |
| c91ebe4f-a01c-3833-b87b-6a5734c4d711 | -17.1081 | -56.8098 | 2026-09-10 15:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.0 |
| baccb1fb-6664-32a1-ae50-65e81e32f2a7 | -10.7585 | -45.917 | 2026-09-10 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.8 |
| b027cea9-027f-3233-aa30-6bd0316b1aa5 | -8.62 | -47.3451 | 2026-09-10 15:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 46f37572-b580-305b-a755-c408f36c7f8a | -8.6012 | -47.347 | 2026-09-10 15:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| ca55f6eb-43c9-32d0-b057-e5fc2e0285f4 | -6.5453 | -62.8914 | 2026-09-10 15:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 219.1 |
| 2a4d6d63-9bc1-341f-a001-ccc1dffb069d | -10.2743 | -45.2726 | 2026-09-10 15:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 258.8 |
| c03d97bc-90f1-33a6-b1a9-83a1930f3f52 | -6.6541 | -59.4452 | 2026-09-10 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 969fc725-4eb5-3b43-897f-0549752b21dc | -9.7698 | -43.4825 | 2026-09-10 15:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 223.7 |
| e2df823e-9794-3e4b-97bf-fb61eb0289c1 | -8.6311 | -66.5287 | 2026-09-10 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 193.6 |
| 5da79a57-615e-38f0-9d97-9c138e839e0f | -10.2559 | -45.2292 | 2026-09-10 15:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 60b2a2cf-5485-3718-8150-1d960fd1e7d1 | -8.9428 | -63.2797 | 2026-09-10 15:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 99c0a739-1019-3868-91b2-4314e8eddecc | -10.6985 | -46.106 | 2026-09-10 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.6 |
| a47be0ba-6fa3-3b3b-8213-2acfdbde50cd | -6.7833 | -59.4208 | 2026-09-10 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 4b666d4f-1781-3b1d-98a0-fe2cd6bb4a72 | -10.2362 | -45.2775 | 2026-09-10 15:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 307.4 |
| c91e12df-9a15-3483-9165-f3125c10d0b2 | -10.6981 | -46.1287 | 2026-09-10 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 373b820a-b4b0-3382-8552-e3370e1637b9 | -2.7332 | -57.6077 | 2026-09-10 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| e748023b-c46d-3e81-86b3-a333252439a4 | -10.6794 | -46.1085 | 2026-09-10 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 473.9 |
| b2d73a22-9924-3fc0-a8d2-656e90f5528b | -6.6726 | -59.4445 | 2026-09-10 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 97d5f4da-4ea8-3523-a517-67945b0cbcd4 | -8.9873 | -65.4379 | 2026-09-10 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 861929ef-a87d-3bef-861a-7a82b9c78500 | -9.2275 | -65.5983 | 2026-09-10 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 49884725-0d28-3436-9227-04cba49e2299 | -2.7149 | -57.608 | 2026-09-10 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 30b37818-797d-3208-b801-2d5ad804e64a | -8.6311 | -66.5101 | 2026-09-10 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 326.0 |
| 8963b85f-4a92-3932-a023-23abf3c9b588 | -2.7148 | -57.6274 | 2026-09-10 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| ac21bd9a-1c65-3223-aff5-ce768fccbd89 | -13.2487 | -61.6371 | 2026-09-10 15:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 7b54c9e4-8e42-3082-8de9-e063d7498cb2 | -10.2556 | -45.2521 | 2026-09-10 15:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 143.2 |
| fe1cbcd2-b354-35dc-99e9-90c0a029e6ee | -13.2293 | -61.6772 | 2026-09-10 15:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 334e1a2b-dd5e-3bb7-b3f9-862c88486886 | -10.2552 | -45.2751 | 2026-09-10 15:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 373.1 |
| 75d0f4bf-67ea-3edc-94e9-fe093cf01a50 | -13.2673 | -61.6747 | 2026-09-10 15:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 0b01dd4a-1230-3ff4-acc6-8581c00deecf | -13.2284 | -61.7743 | 2026-09-10 15:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 7967a214-c1df-3ae7-874c-497493cd5b4b | -13.2675 | -61.6553 | 2026-09-10 15:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 5771db3d-0a95-3761-889d-71d2daa4bd60 | -7.5167 | -45.2569 | 2026-09-10 15:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 26acf161-8480-3dd2-8a2d-e7591544ec45 | -6.7077 | -45.4635 | 2026-09-10 15:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 683b5ac8-1f18-3a66-8c85-d04caf41020d | -10.6798 | -46.0858 | 2026-09-10 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 150.0 |
| a8278fdb-aa1d-34cf-9368-8611be7263e8 | -10.2365 | -45.2546 | 2026-09-10 15:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 141.2 |
| bb859d59-9b83-3fc7-b53f-ebb756f274d7 | -10.7582 | -45.9397 | 2026-09-10 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| ddb2f587-2b34-3c33-a5ee-7512c44498eb | -13.2289 | -61.7161 | 2026-09-10 15:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 69.2 |
| e7ab7246-2cdb-3bca-bb11-511ef4afbf38 | -10.2753 | -45.2038 | 2026-09-10 15:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 112.1 |
| cb148fbb-1a4b-3d2e-a92f-3f890f67ca57 | -10.2358 | -45.3004 | 2026-09-10 15:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 255.0 |
| 8eb19dc1-cf4f-36e8-859b-77b1203ab59e | -13.2293 | -61.6772 | 2026-09-10 16:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 38537e2f-42f5-3332-82df-35bf588a0bd1 | -10.2556 | -45.2521 | 2026-09-10 16:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 5c699619-3f54-3939-af3b-fb9a4e0d91b9 | -9.2275 | -65.5983 | 2026-09-10 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 6984b231-0ef0-3b45-8da0-da1843c365f6 | -3.3688 | -59.4079 | 2026-09-10 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 7a93c13d-522d-33d1-b9d8-12c753d8912b | -10.6981 | -46.1287 | 2026-09-10 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 217.0 |
| 390cbe45-6ff1-36d2-ae34-8ee9b57e9a5f | -8.9257 | -66.8549 | 2026-09-10 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 1c4895d7-1f60-339a-9e2c-d6423ac6ffb9 | -13.2287 | -61.7355 | 2026-09-10 16:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 04d4adb0-2c74-31e8-b713-391eb6388fc0 | -10.2362 | -45.2775 | 2026-09-10 16:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 255.1 |
| d3ad819f-12b0-3b33-a2fe-faa7ba35edcd | -10.6985 | -46.106 | 2026-09-10 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| a41594fb-4cfa-36fa-af83-c085223dcaa2 | -6.5637 | -62.8908 | 2026-09-10 16:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 180.0 |
| 5cc5803c-ef85-38a8-994c-eba5a163b8b8 | -8.6311 | -66.5287 | 2026-09-10 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 139.3 |
| d0e32242-db0a-3674-b9db-fa7a1c867f6c | -13.2481 | -61.6954 | 2026-09-10 16:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 827fc0e2-c457-3095-9254-44bf9fb31c27 | -13.3298 | -61.1064 | 2026-09-10 16:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 73aec673-c6f4-31e6-a13a-b5f184a2742c | -10.6794 | -46.1085 | 2026-09-10 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 239.9 |
| d909fe06-f6f5-3276-9cca-2bda9289bdd1 | -8.6009 | -47.369 | 2026-09-10 16:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 2f08a4bf-f6d2-3742-9fba-35deaf60a184 | -8.6012 | -47.347 | 2026-09-10 16:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 3be7f605-479d-327b-87d1-cc47bd77504d | -13.2487 | -61.6371 | 2026-09-10 16:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 0815f276-96e1-37d2-8ff2-4da6880d019d | -10.2552 | -45.2751 | 2026-09-10 16:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 479.9 |
| bb49bd75-fa5e-3ad7-aaef-8a6cef65360c | -6.6357 | -59.4459 | 2026-09-10 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 6eaab3cd-e308-3940-9bb6-8e5e97c46e44 | -3.3687 | -59.427 | 2026-09-10 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 104.7 |
| c159360c-a169-3bd0-8b6c-a4d9959ebf31 | -13.2852 | -61.7899 | 2026-09-10 16:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 58f26e61-7625-3e18-b9eb-7f297341d4e3 | -13.2297 | -61.6384 | 2026-09-10 16:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 94.0 |
| f0585f8f-c075-3781-8816-c0293531a497 | -13.2485 | -61.6565 | 2026-09-10 16:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 3c2c8476-51bf-37e2-8b00-ed5b12723828 | -10.2365 | -45.2546 | 2026-09-10 16:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 233.4 |


[Clique aqui para ver as próximas entradas](README53.md)
