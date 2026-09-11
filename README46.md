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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cd6465b-0e13-35cd-9061-5eafdca0e122 | -11.9547 | -49.7512 | 2026-09-11 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| d4b8a7f2-3df9-336e-a3f1-1bd44474a595 | -6.641 | -58.4987 | 2026-09-11 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 86af242e-a67e-370b-b855-061a8a0f51ec | -6.7077 | -45.4635 | 2026-09-11 16:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| e7085745-44c0-3b96-b8f8-f51e6314aa1d | -10.7359 | -46.1465 | 2026-09-11 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 203.9 |
| 6f95da30-2f01-32a2-8999-fd93c3ae72e3 | -3.3688 | -59.4079 | 2026-09-11 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 5525d561-8404-33fd-9f0c-149657c7296b | -10.5478 | -51.3367 | 2026-09-11 16:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 154.8 |
| 0fcd01d7-92d7-3f5e-9ecc-6e0ee68d0974 | -6.8281 | -55.2826 | 2026-09-11 16:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 0ff45d71-d0f3-3d82-8876-2d669848c323 | -6.4047 | -54.9642 | 2026-09-11 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 63e736aa-2fa5-3f7f-b96b-6c73637164d7 | -6.7263 | -45.4846 | 2026-09-11 16:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 187.0 |
| 88630a32-aea4-3de5-969f-9294cd047b5b | -10.7542 | -46.1894 | 2026-09-11 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 0a481ffa-6e00-39dc-adbb-58bc6e5337c8 | -10.5475 | -51.3578 | 2026-09-11 16:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 353.1 |
| 608d1525-24da-31ef-9e9d-ebb5b2a568e7 | -9.1167 | -65.5085 | 2026-09-11 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 372b5650-2881-3f0e-90c4-877775d3423a | -10.4706 | -48.665 | 2026-09-11 16:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 5dda3d19-dfd4-3ce3-a0b2-1dc926ba35c9 | -6.6226 | -58.4995 | 2026-09-11 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| b765a523-4b86-37b0-9184-b02cecde7cf3 | -8.9428 | -63.2797 | 2026-09-11 16:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 97b233a1-0c8a-39c8-a1ec-e1746f5d5cb6 | -6.8247 | -58.6461 | 2026-09-11 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 2e6e7198-9bee-317d-8e44-2ea3486ea84d | -5.9817 | -57.7282 | 2026-09-11 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| cf5abfff-2a81-3ad4-8d71-87e38fca0a96 | -6.828 | -55.3026 | 2026-09-11 16:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 3341575a-3279-3651-8391-5fdad5df47dc | -10.4909 | -51.3634 | 2026-09-11 16:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 5cec370d-c190-3c0c-b3d4-3bdf1b3d94c3 | -6.745 | -45.483 | 2026-09-11 16:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 88d2bc7b-005c-3b02-89e7-84975443fa93 | -11.2488 | -54.1378 | 2026-09-11 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 236.9 |
| 8ef4fd7b-c346-38a5-937b-aeb7eb98c4fb | -13.3555 | -51.7855 | 2026-09-11 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 249cf611-7b7c-35ee-bb5e-2d8e2f6103d1 | -10.7359 | -46.1465 | 2026-09-11 16:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 167.4 |
| efa33012-503e-3fba-8239-0377251d2e20 | -13.3245 | -61.6514 | 2026-09-11 16:10:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 638973cd-96a2-3652-8719-4c3af84147d5 | -9.3931 | -65.8732 | 2026-09-11 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| c2c08a76-6fb5-3c50-899f-c00134e9e0f6 | -8.9428 | -63.2797 | 2026-09-11 16:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 9283076d-d636-3309-8e50-21dd2289c82e | -9.494 | -68.4895 | 2026-09-11 16:10:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 698e45ad-6618-34a1-b08c-c7d5bb4c93d9 | -13.2099 | -61.7173 | 2026-09-11 16:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 25738594-9bfb-3515-aa76-20f6566f61ee | -10.7546 | -46.1667 | 2026-09-11 16:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 128e4cdb-5780-3e4e-a480-bc225007b1d6 | -8.6311 | -66.5101 | 2026-09-11 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 5d70113e-0d2a-3cf7-86c2-6f42686a381a | -13.2671 | -61.6941 | 2026-09-11 16:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 35724847-fef4-38d0-9177-cf7674bfefdf | -5.9817 | -57.7282 | 2026-09-11 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 8f4aa4aa-4503-30cf-a7e6-68af7ed44a94 | -10.7549 | -46.1441 | 2026-09-11 16:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 164.7 |
| c340967b-6c35-34e9-9184-8fb66aec3480 | -3.3871 | -59.4075 | 2026-09-11 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 5eab71a6-bc7f-3957-916b-9cfdb7cc2ca0 | -10.5475 | -51.3578 | 2026-09-11 16:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 465.6 |
| e2d5767c-af5a-36ca-ae05-07d9c64d7601 | -13.2291 | -61.6966 | 2026-09-11 16:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 63.2 |
| c9e09fe1-8468-3151-89b0-c9eff8086f6e | -6.4047 | -54.9642 | 2026-09-11 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 8378f57d-1b9c-39a1-ab19-7a7d1fdd1864 | -13.2673 | -61.6747 | 2026-09-11 16:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 80b5d949-8fa5-30c4-9448-c4f460c4c96a | -9.0981 | -65.5091 | 2026-09-11 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| eaa9fbb0-4061-3f01-bd47-435d60897fb8 | -6.6226 | -58.4995 | 2026-09-11 16:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 435c1460-6179-388c-83bf-f49e038354cb | -13.3247 | -61.632 | 2026-09-11 16:10:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| c5dfe237-c500-38c6-a5c6-8dff0e09784d | -8.0709 | -55.3121 | 2026-09-11 16:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| e309f3dd-7819-31b1-99a9-2aad75170b1a | -6.641 | -58.4987 | 2026-09-11 16:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| fe23b8d1-5d12-3bb6-99fa-5822c3586373 | -13.249 | -61.5983 | 2026-09-11 16:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| fd0f5686-a95a-3b35-93be-b57789ada9f6 | -11.0434 | -49.6851 | 2026-09-11 16:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| de4eee58-53b8-3501-b3f4-ad60a2ead891 | -10.7542 | -46.1894 | 2026-09-11 16:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 333.7 |
| 71b9f860-7674-313e-8fa0-21cb86014477 | -9.6038 | -68.9491 | 2026-09-11 16:10:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 6d5e581e-a658-323f-b5c1-0c1cc69a1a10 | -5.6595 | -45.5427 | 2026-09-11 16:10:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 1509aa9a-27cb-3d8c-8571-169815a465d3 | -13.2481 | -61.6954 | 2026-09-11 16:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 893f9b9a-844e-36c2-b80b-d8a8501b1dc4 | -6.0913 | -57.8992 | 2026-09-11 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 85903bce-0fbf-303d-a5ea-a56c4df501f3 | -13.2485 | -61.6565 | 2026-09-11 16:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 73c99003-6b60-39d6-9a5d-d0b89fdb1970 | -11.9547 | -49.7512 | 2026-09-11 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 05a50381-b450-36eb-9206-019e0989f0ff | -6.8247 | -58.6461 | 2026-09-11 16:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 8a4e0aa0-ae6d-3338-bd9e-9846c3b37b03 | -8.8953 | -70.8938 | 2026-09-11 16:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 0a9ee91b-c4e3-3fca-8951-9f24dbef8f05 | -9.1711 | -49.9835 | 2026-09-11 16:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| e4b1522c-a920-3383-bfd7-aa3d22bbdfd1 | -11.3513 | -45.7922 | 2026-09-11 16:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| a0b330b8-7d91-305d-a36b-770d6cf514fe | -2.94 | -50.4 | 2026-09-11 16:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b2d384d-2e9b-3127-895c-07b5efa7aca2 | -2.94 | -50.35 | 2026-09-11 16:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88537c11-3cee-3456-9eff-a63702f12cdb | -15.07 | -48.5 | 2026-09-11 16:15:00 | MSG-03 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 20c12fde-bc38-3923-ba7a-d1829e57bcc3 | -13.285 | -61.8093 | 2026-09-11 16:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 1e09c6f0-2693-35c4-9dfc-88f255936cea | -9.1429 | -68.2017 | 2026-09-11 16:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 03ffaa0e-c962-33f9-8ed6-46252cb2ba73 | -8.0748 | -54.8499 | 2026-09-11 16:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 22c23cd6-6838-3447-aac5-87e96350234e | -8.9428 | -63.2797 | 2026-09-11 16:20:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 3f47a878-e536-325c-87fe-307cdb72dd98 | -9.1168 | -65.4898 | 2026-09-11 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| c62b1c17-d6ee-3320-a4dc-25b26a3c3747 | -10.5475 | -51.3578 | 2026-09-11 16:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 308.7 |
| bc7cfc06-5c0c-3454-b15c-6e3b95e7ef1d | -9.1167 | -65.5085 | 2026-09-11 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 4b4f24a2-d3c6-3032-a2d9-0112a4c0f4eb | -9.9041 | -45.91 | 2026-09-11 16:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 123.3 |
| c4a2fcdb-087a-3dbc-af14-011dc068f302 | -10.7542 | -46.1894 | 2026-09-11 16:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 459.7 |
| ebc07ad5-21cf-3f10-8930-1d5aa0c49fba | -6.4401 | -58.1575 | 2026-09-11 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 74609fe2-9bf7-3763-b78c-a07a422a9d67 | -3.3687 | -59.427 | 2026-09-11 16:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 111.0 |
| e024da92-00aa-3fa1-8d83-1a4c42670905 | -10.7274 | -50.6192 | 2026-09-11 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 172.8 |
| ae726a9b-52d0-3ae8-9353-7607ebc3f5ae | -8.228 | -73.1676 | 2026-09-11 16:20:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 71.9 |
| eb06b723-d491-3002-98cc-df5b2d77ce0e | -13.2865 | -61.654 | 2026-09-11 16:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 71.2 |
| fd5b0fbc-72a7-3905-83a9-9d8a78fdb7f9 | -8.9873 | -65.4379 | 2026-09-11 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| d243b8c9-b5e4-3aed-b3bf-ae05f099b76a | -6.6036 | -58.5972 | 2026-09-11 16:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| b507afe9-23e2-3de8-bb6a-9b0ef9aa0c35 | -7.1009 | -42.1327 | 2026-09-11 16:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 203.8 |
| aea95a90-b2a1-395b-9c6c-7d0b350ae5dd | -10.7084 | -50.6212 | 2026-09-11 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 028f0632-0a60-31a4-958f-27e60c23071d | -13.4198 | -51.3731 | 2026-09-11 16:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.9 |
| c44fd371-ba7f-354c-bee4-d27ae8448635 | -6.641 | -58.4987 | 2026-09-11 16:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 775a3549-96fb-3587-8d5f-f4ac52fac54c | -6.6226 | -58.4995 | 2026-09-11 16:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| a3ae0fab-a895-363c-a037-9993f4f83d4a | -13.2488 | -61.6177 | 2026-09-11 16:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| a0968a8a-4a91-3865-9b37-c507fd610c3f | -8.6311 | -66.5101 | 2026-09-11 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| dda1c97d-d31b-317a-b512-7d8414613f80 | -13.4198 | -51.3731 | 2026-09-11 16:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 5f41e945-b099-3200-a272-158447dce636 | -10.7084 | -50.6212 | 2026-09-11 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 119.2 |
| b62cd580-2e78-3b30-93db-68896ab0b2d1 | -9.536 | -67.1539 | 2026-09-11 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 93a6b5ee-b5fa-3baf-8bb7-ae97bb62f65b | -6.641 | -58.4987 | 2026-09-11 16:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 3a7c3ff7-6e17-38dd-9a21-47969cdc8f9e | -10.7542 | -46.1894 | 2026-09-11 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 200.2 |
| 22d5c8d5-a5fe-3117-b17a-c9f92f9cea90 | -6.6226 | -58.4995 | 2026-09-11 16:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| dfd9a00c-d228-341c-a2c5-4f341f5b38c8 | -9.9041 | -45.91 | 2026-09-11 16:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.5 |
| d5f315ea-b74d-322e-a3b4-4e4c0862cddb | -10.5475 | -51.3578 | 2026-09-11 16:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 284.7 |
| 7dc8fdf7-0807-301d-af1b-a1050dafa3b6 | -10.7274 | -50.6192 | 2026-09-11 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 220.8 |
| f31086d5-2f22-3a60-8c2f-4525520437e4 | -6.6226 | -58.4995 | 2026-09-11 16:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| d3b1b1be-080b-3c86-8845-dd498afc8d12 | -6.8062 | -58.6469 | 2026-09-11 16:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| d40b6b41-b1f7-316c-93ae-ebe395aa32c0 | -11.2488 | -54.1378 | 2026-09-11 16:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 279.2 |
| bd48b6c8-5f0d-34b4-9f5e-24b0b4bf3b37 | -6.641 | -58.4987 | 2026-09-11 16:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 777d5015-f61b-3107-a92f-04a478a98d3f | -10.2556 | -45.2521 | 2026-09-11 16:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 9bd61190-b4da-3682-80cc-3886ce723964 | -13.3038 | -61.8275 | 2026-09-11 16:40:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 44.9 |
| b697626f-7687-3527-9997-32f170a25ae5 | -10.7542 | -46.1894 | 2026-09-11 16:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 208.6 |
| 4f894c54-10a3-3491-8383-9bae73485b16 | -9.3931 | -65.8732 | 2026-09-11 16:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| a2cfead7-1aa2-3657-bfc6-7e2ab67ec031 | -10.2559 | -45.2292 | 2026-09-11 16:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 105.1 |


[Clique aqui para ver as próximas entradas](README47.md)
