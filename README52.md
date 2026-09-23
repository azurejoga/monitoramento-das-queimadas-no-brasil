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
| 75b4713b-0571-3767-85ac-789d0ee78cad | -1.8285 | -55.71526 | 2026-09-23 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f1fb257-2aa3-3631-b7d1-dad423356a85 | -3.07392 | -54.39015 | 2026-09-23 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d723755-e84c-3a67-9401-3e4b57653d7f | -6.89944 | -43.63482 | 2026-09-23 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bcbf8d09-04c5-3421-8ea9-751e297efd05 | 1.43977 | -50.81323 | 2026-09-23 04:25:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bd93d97-dfc3-3f3e-99ce-9a7bf8880a5f | -5.69875 | -47.38931 | 2026-09-23 04:25:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8700343-bd31-357d-a61f-146825e80afa | -5.86928 | -51.94213 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a361a05e-eee4-30fb-be55-297ca09e7c21 | -3.1624 | -58.11926 | 2026-09-23 04:25:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 767dcf60-e68b-3e71-966c-bf04e7a3c147 | -2.55391 | -49.10104 | 2026-09-23 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5baf8272-0c4f-3520-89ba-b488291c6670 | -6.61194 | -43.74345 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 6a41b43d-3db3-3698-adbe-4de26d6989e9 | -4.45429 | -55.07376 | 2026-09-23 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89d285f6-4cef-3dbb-8f06-26a2981150f1 | -6.6102 | -43.73092 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 09976a2f-30b9-34b2-bc3c-395ab71a902c | -2.74344 | -51.54498 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c886898e-0b78-3f40-aeba-ee782045379c | -3.77275 | -51.35448 | 2026-09-23 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc7bbbef-c335-31ab-9007-64f45d467a59 | -3.25185 | -53.96343 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce819f45-fe20-3bd7-b56a-cc1104409e14 | -6.18176 | -45.31996 | 2026-09-23 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0734300c-d0d8-3421-a6c8-80487f4d177a | -4.8349 | -55.76962 | 2026-09-23 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7e6c718-a6a6-3fcc-8649-02c094430e01 | -2.86406 | -57.79131 | 2026-09-23 04:25:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2ade18fd-b84a-32dc-8e8c-b4c0b53152b2 | -6.84948 | -45.55298 | 2026-09-23 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26132e11-38be-39ed-aa09-9b96e50d907d | -3.85922 | -58.82363 | 2026-09-23 04:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| dad902d3-b5eb-3370-96df-77eaa80ba145 | -3.72167 | -49.0444 | 2026-09-23 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a545a079-9d2c-34e2-8689-1588de482620 | -5.60987 | -43.35503 | 2026-09-23 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| adeb53a9-4d4b-3e25-a415-0c31dcbe7f2d | -3.83713 | -55.86353 | 2026-09-23 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7d3ba47-bc2f-3a91-9894-1fe26f6c7d5f | -5.60932 | -44.02431 | 2026-09-23 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a045781-7321-3f5f-9320-38d6ed1de64e | -3.0056 | -54.18011 | 2026-09-23 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b854818-4d4a-344c-9759-acf3abafd7b4 | -4.57783 | -45.66221 | 2026-09-23 04:25:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9b0cedf-ab98-3657-987d-aaf98f97c733 | -6.14988 | -44.77697 | 2026-09-23 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b24ceed5-1d66-3310-96c5-4584910aa417 | -3.52689 | -43.92488 | 2026-09-23 04:25:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eee9c06a-400a-3738-b462-370ad933aa44 | -6.671 | -42.56894 | 2026-09-23 04:25:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 5ee5e742-dd82-373d-9ba1-b5e1d270daf1 | -5.28063 | -47.25742 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 369f56c2-f4f1-3252-b23d-536292a3f07f | -2.97847 | -54.1543 | 2026-09-23 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f12f1cc3-c420-3d1c-afc5-cf0882f142ae | -6.17265 | -47.70378 | 2026-09-23 04:25:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83b63d07-43d9-3126-9d6f-3b83fe646086 | -3.4501 | -50.61497 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 157b0fe4-54c1-32e8-892c-4dd14b60d394 | -6.61254 | -43.73945 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| a3f2a307-fdb3-30ce-b4be-941a240180de | -6.60607 | -43.73439 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c9429d0-e408-3bf1-9f62-d6e52899edce | -3.16144 | -58.12488 | 2026-09-23 04:25:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ffc1f1b2-feaa-3156-a168-22eeefee5aca | -4.56304 | -54.94183 | 2026-09-23 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0056e0e3-d3e1-3392-9a6a-aa1062524cfd | -6.61134 | -43.74742 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 362081a3-10f1-3c57-95b9-fb4c61856392 | -3.00147 | -54.17339 | 2026-09-23 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc12dc5f-2d4e-3163-8d06-a286f0d14c28 | -3.38241 | -50.41122 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4d7b375-93df-39c1-a193-cbb267abcd12 | -5.1178 | -48.79918 | 2026-09-23 04:25:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6ab949d5-5368-37e0-93dc-217a04cb6df9 | -2.88229 | -54.08379 | 2026-09-23 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04294dfd-25ad-3d43-9afc-6532a01dd725 | -5.14153 | -50.05275 | 2026-09-23 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b64c72c1-e4cf-32ef-9f1a-178757dc282b | -6.13595 | -43.85233 | 2026-09-23 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 13854f31-0b58-3f64-9bc4-ea0c6f9165b2 | -7.09845 | -43.06564 | 2026-09-23 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f2001699-74e6-33ad-a7b9-3ee3062b4097 | -4.42556 | -55.08277 | 2026-09-23 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ba8cd03-f776-336d-8c54-62a4edd39d52 | -6.32602 | -47.61902 | 2026-09-23 04:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10023f67-89bc-3a3a-a5f6-da8743d97d82 | -2.9497 | -54.08535 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec0e1386-b5cb-3590-962a-ee330b976576 | -1.22491 | -47.51791 | 2026-09-23 04:25:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2a91fc0-def6-3e93-945a-ad7029dbc307 | -3.46129 | -43.36451 | 2026-09-23 04:25:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4189261f-4bb9-394c-9758-86f19f7bd824 | -6.21434 | -45.37175 | 2026-09-23 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38de824b-b5a5-3707-9fb3-e4e1404bd85a | -4.83554 | -55.76595 | 2026-09-23 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07fd09fa-7fc3-3bd0-a3d2-c055f0a37e5d | -5.2475 | -48.19293 | 2026-09-23 04:25:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d4c1f636-7730-35a4-bfd8-b714ff966187 | -5.57372 | -42.72992 | 2026-09-23 04:25:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f44a1edb-1b97-377c-9990-fce45b99f500 | -5.41229 | -49.2672 | 2026-09-23 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 33dd9f59-a96c-3bc3-b527-140a8b933c63 | -5.04502 | -49.23307 | 2026-09-23 04:25:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f85e8ac9-c344-35ad-8429-0bd16ad53049 | -2.94883 | -54.08202 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e8e09e9-b9d4-3491-b449-4fac9936fdbd | -2.62723 | -51.70151 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bbdd7c8-b3a1-3f4d-9894-90be15e313d5 | -6.00577 | -44.11333 | 2026-09-23 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c9172cd-c1ce-32ab-a2ad-eca747cde36e | -3.22732 | -46.94606 | 2026-09-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a3ec0a90-1d5b-3bb9-b6ff-602c27e37af3 | -5.77546 | -43.7647 | 2026-09-23 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1bdfaab1-140f-3af7-b5c6-1442a5f6f67c | -6.41784 | -43.46816 | 2026-09-23 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07ad3e9c-b170-3232-b9ec-e1dcbee6cbff | -6.61901 | -43.74449 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 7adf1a7d-c11e-351c-ab4b-4898957048c3 | -4.55781 | -54.94099 | 2026-09-23 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42b569af-996b-3f16-afc9-d45f691b44d1 | -5.94123 | -45.37983 | 2026-09-23 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9c214220-f48e-3eb9-a9a9-f3bdbb1c5f6b | -6.05576 | -46.35324 | 2026-09-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07809dde-4750-3a0d-9f54-d4773570a51a | -7.10213 | -43.06621 | 2026-09-23 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 25b18974-2e78-3bbc-bf0b-d16fda493c48 | -5.75842 | -45.11008 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6190fd9b-037f-3adb-a5c0-e17ffe50c462 | -2.40612 | -49.3033 | 2026-09-23 04:25:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9ca25b7-8efc-321b-91cd-75ca593d9bf7 | -4.45822 | -47.9211 | 2026-09-23 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3fd67014-e61e-366d-a275-f548084c9368 | -7.13027 | -43.07936 | 2026-09-23 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fbb2fd0b-17c2-3633-ba73-091a2687ca5e | -5.88767 | -52.04371 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3386da9a-49bc-3b15-abf5-8fd34b696f6f | -5.16424 | -45.43472 | 2026-09-23 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ed65c51b-1b93-31ae-bedf-bd983c33ab4e | -3.90541 | -55.83592 | 2026-09-23 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 41f1d223-058c-364f-986f-636effce391b | -1.39593 | -49.04727 | 2026-09-23 04:25:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cdb6dac5-0c9c-3d04-84d0-ff6bf22e16bb | -1.92257 | -58.26289 | 2026-09-23 04:25:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ce473beb-0360-319d-89bc-3ae2cd012293 | -5.66049 | -42.64737 | 2026-09-23 04:25:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9b255d6e-c073-3059-ad00-49ab038452bf | -5.76511 | -45.11112 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 59d00209-b5e0-34f3-99a4-901537e77bd7 | -2.29779 | -48.58229 | 2026-09-23 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b625f03-8ed7-3e33-86e5-95b4799aef4f | -5.80515 | -52.0943 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f31c7969-abbd-3e62-8459-f9b4c4d25417 | -3.22787 | -46.94254 | 2026-09-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| e54aa61a-ce95-3add-9987-1c5be101f043 | -6.60427 | -43.74636 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e3850d1c-32c7-3690-8e64-78be04d60a30 | -3.76232 | -47.50239 | 2026-09-23 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83e8a420-49d5-3908-84fe-e0a68a84d08f | -5.46269 | -44.31684 | 2026-09-23 04:25:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82fe85dd-d7f8-35f0-ad0e-34e59c21de8e | -6.72445 | -44.1551 | 2026-09-23 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| da9e7ac7-359c-3e8f-aa5a-363bf36e9562 | -5.17711 | -56.17792 | 2026-09-23 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 607cf272-70ee-39df-ac9c-717c24b19bbd | -2.82478 | -49.23676 | 2026-09-23 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fade1cd8-06cf-3035-974c-afae4f30b244 | -6.32641 | -43.93544 | 2026-09-23 04:25:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8b458bf5-3ca8-33f5-a9ea-7ac0208b67c4 | -4.42665 | -55.07643 | 2026-09-23 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 106720e4-280f-3df3-a161-e7bb3894d048 | -6.90003 | -43.63077 | 2026-09-23 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d51c73cc-3d99-301a-85ad-149df96563f6 | -6.31025 | -43.79821 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8e211bf-bebb-3f2b-a95b-eebd5089e2f2 | -4.41987 | -55.47339 | 2026-09-23 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cd64fcc-13f8-353e-9f2c-5b06ed46ac5d | -3.06354 | -54.38877 | 2026-09-23 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e6d2a8f-e85b-3f20-b360-e4e942534c95 | -6.03525 | -44.03587 | 2026-09-23 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e6a9e621-ac50-3b7a-b558-4327463d2fdc | -6.94208 | -42.88428 | 2026-09-23 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 43237b97-0659-316a-a6b6-8a810f14e1ae | -1.22132 | -54.55301 | 2026-09-23 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc1aa641-d7c3-346b-b614-983535caf7a3 | -5.40937 | -49.26252 | 2026-09-23 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10bff163-b580-352c-94a3-dc7297741ae2 | -5.60839 | -45.94785 | 2026-09-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c80e2989-4f60-3a87-a6e6-fb085f50da40 | -4.30044 | -49.12653 | 2026-09-23 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 89f86fe2-051a-3401-9e5f-1560cd32c769 | -5.34439 | -45.28071 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 68adffe0-3d9a-327e-a6e7-88e5cf5550d1 | -4.22172 | -48.6146 | 2026-09-23 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |


[Clique aqui para ver as próximas entradas](README53.md)
