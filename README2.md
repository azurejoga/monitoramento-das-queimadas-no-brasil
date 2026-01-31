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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07c9769d-3eea-3e07-a493-7e9e839f35c2 | -8.47197 | -35.31918 | 2026-01-31 02:53:00 | NOAA-21 | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 8ee0e8c8-6932-3121-af1f-f972e60af451 | -8.46559 | -35.31789 | 2026-01-31 02:53:00 | NOAA-21 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3d259bf8-4a39-31b3-b411-09781085c7a5 | -1.8058 | -54.4923 | 2026-01-31 03:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 9f0a732c-813e-31e2-b3ee-9ef352fa32ae | -20.3178 | -57.3644 | 2026-01-31 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.6 |
| ee445e29-a786-3768-ba99-e1db9bfc937c | -20.3178 | -57.3644 | 2026-01-31 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.2 |
| f7eac68e-7234-384e-a1d6-5269ceee93c5 | -7.49997 | -37.19104 | 2026-01-31 03:21:00 | NPP-375D | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1ce583ab-b55a-3022-a104-4b69f2544f95 | -5.09099 | -37.55639 | 2026-01-31 03:21:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f84eca79-3916-3e3f-9280-fc07dc10dea6 | -7.6179 | -35.15147 | 2026-01-31 03:21:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bdb93f74-d201-3fd3-b6c4-34ad42c10c92 | -8.21562 | -35.34065 | 2026-01-31 03:21:00 | NPP-375D | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f994367a-2afa-3170-a37a-7543920131cc | -7.65874 | -35.19647 | 2026-01-31 03:21:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e4eb4279-3b79-3b73-8d37-f53bf75b81fc | -5.09154 | -37.55317 | 2026-01-31 03:21:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 76af31aa-9c6c-3bb9-a51e-66f0b4dbc8c1 | -5.35261 | -36.13492 | 2026-01-31 03:21:00 | NPP-375D | JANDAÍRA | RIO GRANDE DO NORTE | Brasil | 2405108 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5879835e-6163-3355-8696-a8d7f3bc5864 | -7.50707 | -38.32616 | 2026-01-31 03:21:00 | NPP-375D | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 35caa8c2-6ea1-3349-bc44-360a82e1fde4 | -10.17427 | -40.94867 | 2026-01-31 03:23:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3a35a322-f408-330b-88fc-757dffb182a4 | -10.18023 | -40.95004 | 2026-01-31 03:23:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b6808e6f-c9cb-3b49-bc6e-7601d98d5a03 | -8.53584 | -35.11916 | 2026-01-31 03:23:00 | NPP-375D | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f57a5bb2-dab1-3bf0-bbb0-68d5921a28ca | -7.82687 | -42.05882 | 2026-01-31 03:23:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 38240b4c-22c7-3efd-bd82-6af60cafb9d7 | -7.82927 | -42.06398 | 2026-01-31 03:23:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c87959fa-697f-3c1d-8001-9b181756193b | -8.47997 | -35.70649 | 2026-01-31 03:23:00 | NPP-375D | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c1582a40-4f68-3f7f-bbdb-a2afa65494e7 | -9.84596 | -37.05918 | 2026-01-31 03:23:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 14db5fe1-6da8-3c4b-b1b3-d642e79c2935 | -9.49084 | -35.97158 | 2026-01-31 03:23:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 75418dbb-735e-3033-8902-3dfdd10b5725 | -8.73993 | -37.18079 | 2026-01-31 03:23:00 | NPP-375D | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 75f8387c-e245-3784-967e-1ae5ad901e7c | -8.74075 | -37.18183 | 2026-01-31 03:23:00 | NPP-375D | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6c9a7a22-68a2-367c-8d3a-a4cacfd055ee | -9.49172 | -35.96772 | 2026-01-31 03:23:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 1d267216-aa42-3560-bb7f-ec0615cf3b24 | -9.81253 | -38.10751 | 2026-01-31 03:23:00 | NPP-375D | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b63e88ff-e3b4-3a16-b02e-f23d44cbf00d | -7.83351 | -42.06026 | 2026-01-31 03:23:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1105a922-68c5-3a71-98b7-6d23584d8f8f | -9.50489 | -35.94376 | 2026-01-31 03:23:00 | NPP-375D | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 1a9eb8ca-db7b-394e-a793-778a2bbfe67b | -9.50498 | -35.9433 | 2026-01-31 03:23:00 | NPP-375D | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| c01e923f-927c-366c-97d1-93942ff57331 | -9.49162 | -35.96723 | 2026-01-31 03:23:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 1673ef30-b464-3ef7-b974-09fed1e143ec | -1.8059 | -54.4723 | 2026-01-31 03:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| ff72709e-9288-30be-80b1-03979e880635 | -1.8058 | -54.4923 | 2026-01-31 03:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| d36304a1-5b29-33e9-be12-c9aac9c15c17 | -1.401 | -45.68293 | 2026-01-31 03:42:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84496d76-dc08-3a5f-9cee-714c7dc911cf | -3.25547 | -42.54865 | 2026-01-31 03:42:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df648b54-bb75-3f6f-ae9b-de92935040f4 | -3.42366 | -43.1665 | 2026-01-31 03:42:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15d344d2-c028-35a4-8edf-4f8dc0292735 | -3.31111 | -43.51145 | 2026-01-31 03:42:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 374aa743-0140-3b61-9e69-feaa4bc36127 | -3.42115 | -43.16689 | 2026-01-31 03:42:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 766fbe0e-f72c-3abb-950a-71cc5a34710a | -4.56695 | -38.4491 | 2026-01-31 03:42:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cc54c72f-767e-3f7e-a191-31e95eba15d5 | -1.39555 | -45.67703 | 2026-01-31 03:42:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 25ab06ea-34db-3a63-8b90-aaf55d45db5f | -4.28124 | -38.15582 | 2026-01-31 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b85ca45c-3594-3a70-b892-743d500ee133 | -1.39371 | -45.67732 | 2026-01-31 03:42:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eab075a8-15fc-3f92-b943-16800f2676e5 | -3.26534 | -42.55014 | 2026-01-31 03:42:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fbe40f51-95ae-314f-9125-45ed087f1123 | -1.39913 | -45.68319 | 2026-01-31 03:42:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26e67b3f-4159-3ad1-ada8-be9f010d3543 | -8.48196 | -35.70204 | 2026-01-31 03:44:00 | NOAA-20 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b9008880-fc95-303a-9fe0-e4cd69313b12 | -5.24694 | -37.49841 | 2026-01-31 03:44:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 203bc9d9-a46c-3265-afd0-6816b56f8c47 | -7.61029 | -35.08979 | 2026-01-31 03:44:00 | NOAA-20 | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 40283879-c772-3223-88ff-e2584a4c3140 | -5.08946 | -37.54997 | 2026-01-31 03:44:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0031c2e4-f985-303b-9bfd-bd0990bad5b4 | -9.81416 | -38.10293 | 2026-01-31 03:44:00 | NOAA-20 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7e199cd6-473e-363f-a92f-b84705ee043a | -9.74138 | -36.86149 | 2026-01-31 03:44:00 | NOAA-20 | GIRAU DO PONCIANO | ALAGOAS | Brasil | 2702900 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 159cb2d4-6e1d-3a08-80fc-52b16eef78a1 | -5.35685 | -38.59206 | 2026-01-31 03:44:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 22584640-2c33-372b-bfe8-3d9ee09d0a40 | -4.58309 | -47.54312 | 2026-01-31 03:44:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42d5cf0b-7a7b-3481-bd95-02da87595d47 | -8.74299 | -37.17824 | 2026-01-31 03:44:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c2adaefd-9ae2-3689-805e-c243b7d7ff60 | -5.33875 | -40.84354 | 2026-01-31 03:44:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dbae7029-5700-312f-9e15-427e16ef91a0 | -6.09211 | -40.314 | 2026-01-31 03:44:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e9862ffc-ae48-3091-af1d-d218a7b47f90 | -10.08673 | -42.402 | 2026-01-31 03:44:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2bcdfb00-fdc8-3e0f-964b-7237ef8933b1 | -8.22606 | -37.40753 | 2026-01-31 03:44:00 | NOAA-20 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3483598a-15b9-315f-bfb5-f2f9572d4a83 | -5.93533 | -39.68878 | 2026-01-31 03:44:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e5f183fa-c1cb-3ca1-972e-d0e8273aca44 | -7.38386 | -35.68664 | 2026-01-31 03:44:00 | NOAA-20 | ITATUBA | PARAÍBA | Brasil | 2507200 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 158a96cf-9043-3e8f-8c7d-676a3350da7f | -10.17639 | -40.94659 | 2026-01-31 03:44:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4a6deb5f-e617-3e97-9843-d3538555647b | -5.09297 | -37.55054 | 2026-01-31 03:44:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1c840814-b915-3666-8273-d829857b2f5b | -8.21633 | -35.33936 | 2026-01-31 03:44:00 | NOAA-20 | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cc5a31d8-c9cf-3d8b-972b-b5e195ebbc59 | -5.26056 | -37.72564 | 2026-01-31 03:44:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c6cab0a7-d531-3251-82ca-8a1df38b0cda | -9.81355 | -38.10666 | 2026-01-31 03:44:00 | NOAA-20 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1a74e4a2-e487-30e0-a9cc-57ee500473b7 | -9.84358 | -37.05236 | 2026-01-31 03:44:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 86b55a5f-6ae6-387b-a53f-e99dc5a9e3c7 | -5.40945 | -39.10665 | 2026-01-31 03:44:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 64c174ff-26e3-347a-8fcb-ec0e56aaaa80 | -5.90779 | -40.66258 | 2026-01-31 03:44:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 62e3207a-24f4-3545-b039-96561e6b47ab | -6.38796 | -37.7705 | 2026-01-31 03:44:00 | NOAA-20 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ea72a23b-7d72-352b-ae75-7eed12580b9d | -7.95387 | -40.15349 | 2026-01-31 03:44:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 199e1e6b-4ebb-357f-9015-2985d53a28d8 | -7.38331 | -35.69011 | 2026-01-31 03:44:00 | NOAA-20 | ITATUBA | PARAÍBA | Brasil | 2507200 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f796a6e3-a755-3300-a6d4-a3da9527066a | -9.46779 | -40.24757 | 2026-01-31 03:44:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4979d18f-10ff-3a09-984c-393060e9a094 | -5.36 | -38.59121 | 2026-01-31 03:44:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b92bdf57-fd80-3d25-ae38-21414dacda82 | -5.26409 | -37.72621 | 2026-01-31 03:44:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 57540831-86b1-319f-bf05-7fa4ef2449e4 | -10.86719 | -40.37741 | 2026-01-31 03:44:00 | NOAA-20 | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 85bd48fb-5d61-3373-b240-4ea7b9191e4b | -8.60313 | -35.53605 | 2026-01-31 03:44:00 | NOAA-20 | JOAQUIM NABUCO | PERNAMBUCO | Brasil | 2608206 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 528dca03-7b9b-3dc5-a579-b342b1666fc0 | -6.66484 | -35.80632 | 2026-01-31 03:44:00 | NOAA-20 | CACIMBA DE DENTRO | PARAÍBA | Brasil | 2503506 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5f6361f3-0d89-30b3-bd1c-1ac5393eef71 | -9.84634 | -37.05645 | 2026-01-31 03:44:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d5fe5e82-4bb1-3170-9fe8-1016d4c9448f | -7.50664 | -38.32865 | 2026-01-31 03:44:00 | NOAA-20 | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 53d7433e-d1c8-3a3d-99ec-f82d39e3c5d1 | -7.82787 | -42.0588 | 2026-01-31 03:44:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8e14557d-ce5f-3356-a0be-50a96c9fe7d3 | -7.65854 | -35.19405 | 2026-01-31 03:44:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3303cffb-0c2d-30c2-96bc-faa2cc3cfb76 | -7.82764 | -42.05748 | 2026-01-31 03:44:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2d73f82d-37b3-3bae-8dbc-ba54ffa5b189 | -7.8328 | -42.05395 | 2026-01-31 03:44:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fd91721e-556c-30f9-bac9-eff873e4b7ff | -11.04212 | -45.41224 | 2026-01-31 03:44:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec4710d3-3323-3d1f-9e0c-f39f8d2e791e | -7.95471 | -40.1486 | 2026-01-31 03:44:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1c5be763-cbdb-3bfc-b2e0-a76f024da863 | -5.33941 | -40.83963 | 2026-01-31 03:44:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 341674c0-838d-3880-be43-311e57a4411f | -5.36053 | -38.59269 | 2026-01-31 03:44:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 68997894-e8b1-3f26-ba4f-95ad9355e0b1 | -5.97548 | -40.3873 | 2026-01-31 03:44:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2144d1c4-a2ac-3c06-9ada-130452b38e49 | -7.89775 | -35.3141 | 2026-01-31 03:44:00 | NOAA-20 | LAGOA DE ITAENGA | PERNAMBUCO | Brasil | 2608503 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| bc482c8c-cf0d-300c-bbcd-6752c17f5e1a | -7.96592 | -35.09644 | 2026-01-31 03:44:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ab1ddebd-4552-3633-871a-c2ffcca8bc3b | -8.47865 | -35.70151 | 2026-01-31 03:44:00 | NOAA-20 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5fb9f0ae-71aa-3309-974c-842056de0b2f | -6.09153 | -40.31746 | 2026-01-31 03:44:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 83dbc1f4-c42e-3f71-86a7-3c6352b3e096 | -9.44411 | -40.54871 | 2026-01-31 03:44:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a664fbdf-4779-386f-954c-6d64460ec09d | -7.89444 | -35.31357 | 2026-01-31 03:44:00 | NOAA-20 | LAGOA DE ITAENGA | PERNAMBUCO | Brasil | 2608503 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 9c6f5517-821d-38e9-a158-2361a94dc225 | -7.83204 | -42.05829 | 2026-01-31 03:44:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3ec86d24-3aef-3f00-8130-f7075569b3b6 | -9.50738 | -35.94105 | 2026-01-31 03:44:00 | NOAA-20 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f3bcc485-9cd4-3ebc-8131-ed7de93b00b4 | -8.15136 | -43.19435 | 2026-01-31 03:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c87b6ab8-adbc-3272-abbd-4d40424c5a89 | -8.53624 | -35.11765 | 2026-01-31 03:44:00 | NOAA-20 | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9090b4d7-a503-3a09-9f4c-383184282604 | -10.17665 | -40.95046 | 2026-01-31 03:44:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f76468eb-5e01-3dd3-a2fc-9a3103c492bb | -5.97953 | -40.38804 | 2026-01-31 03:44:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a7f8f766-9a2b-35a2-a191-7b0e6c8aa605 | -11.02656 | -44.83971 | 2026-01-31 03:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4bbdab3-4152-38f0-9f25-d50d8373b354 | -8.48141 | -35.70551 | 2026-01-31 03:44:00 | NOAA-20 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 97b3462e-36f2-3934-850e-de9928e5a6c0 | -5.53599 | -38.7573 | 2026-01-31 03:44:00 | NOAA-20 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README3.md)
