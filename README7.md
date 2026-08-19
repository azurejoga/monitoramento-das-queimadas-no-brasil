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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71b976bc-430e-37af-befe-e83a3fb5554b | -9.406 | -60.5711 | 2026-08-19 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 1a8fa448-37ee-3cd3-b616-47c01128bd08 | -5.92 | -43.6032 | 2026-08-19 00:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 26e327a4-5d15-389d-bc3f-74364acfe43d | -7.0576 | -59.8523 | 2026-08-19 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 1551fc9c-70f2-35eb-9390-039c9ca04032 | -6.6938 | -58.942 | 2026-08-19 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 134.0 |
| f4993f4f-9c83-3f49-a50b-aa3998de40fc | -6.0728 | -57.9194 | 2026-08-19 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| c5063b70-1d03-3309-b920-706145d3305f | -9.3875 | -60.5528 | 2026-08-19 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 1c3a5beb-f715-330b-9d39-f4672714eebe | -9.4257 | -60.416 | 2026-08-19 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 8f2c00cd-cf95-3109-909b-81512f7353e8 | -19.7643 | -57.9399 | 2026-08-19 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 224.3 |
| 49386a47-6cae-3126-a6e6-2dd0f72c4a20 | -9.3873 | -60.5721 | 2026-08-19 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 8511c770-3542-33df-98f3-f20466d7fab1 | -5.4317 | -48.4212 | 2026-08-19 00:50:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 5eca444a-3fb9-3483-8c6d-55e6554f2c92 | -6.0178 | -57.8631 | 2026-08-19 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| e0a3e3b7-d48c-3e76-aa14-c8abea9fb841 | -7.5301 | -55.5839 | 2026-08-19 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| b3486acf-417f-3a84-ab76-d5f4c3649b29 | -6.7486 | -59.0364 | 2026-08-19 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 643fe378-e560-33b7-b526-772d160bff61 | -6.0913 | -57.8992 | 2026-08-19 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 07bebdb4-c726-32a7-aa75-1976e3330ba3 | -6.8777 | -59.0504 | 2026-08-19 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 00335b8d-7348-3bb2-bc6b-a815a5ca1c4a | -5.9198 | -43.6264 | 2026-08-19 00:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 198.7 |
| edc212dc-8ae4-3ed3-92bc-39fa85981a7c | -4.1198 | -60.775799 | 2026-08-19 00:59:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fb412611-94a3-36ca-86e0-9cc0fe725f83 | -6.8493 | -59.022999 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 00963efd-07b5-30b8-be4e-b7bb22d572dd | -6.7496 | -59.037498 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6f7444c-717f-3d8e-b3ba-0551d1df433e | -16.261999 | -57.6581 | 2026-08-19 00:59:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 16e3990c-4ae6-3755-ab37-3f36d7fbf5d4 | -9.3939 | -60.539799 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2603d33c-ac33-3301-b76d-927f45f04865 | -7.5527 | -55.550999 | 2026-08-19 00:59:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 929508f2-2531-3386-89bc-76315663f6bd | -5.999 | -57.852798 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3af3ab5-6b84-3dc9-b42a-ff705ddcbb19 | -9.0222 | -60.491402 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fde69765-fa36-346c-8630-268877edcbf7 | -15.2713 | -56.477001 | 2026-08-19 00:59:00 | METOP-B | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| df652a5e-2bbd-3fd3-87e3-7679dd4d6df6 | -8.5571 | -54.768501 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d988a19-049d-3760-9c62-870fd00b0dfd | -9.4003 | -60.568001 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6ca15280-1dc5-341c-89c1-88f97a7562d3 | -7.0589 | -59.840401 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 10daa7d5-63b4-315d-89de-f461f312d2e3 | -15.8756 | -55.550499 | 2026-08-19 00:59:00 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a51aecc5-a348-3117-b650-1f259acb58fe | -8.9028 | -60.555901 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66a26650-2e31-3ab3-9b9f-f309bc93b36b | -8.5629 | -54.707901 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f951462-bdf4-3546-8139-ef368558e0e1 | -6.8707 | -59.026699 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 22fa73d9-9f5c-3d2f-a6ef-77eeb5ce52fb | -9.0058 | -60.509998 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd8a99ac-5634-3e54-b1f3-d7dd1601e6e8 | -10.8783 | -57.116699 | 2026-08-19 00:59:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e6979988-1f1b-3837-a300-508c3c6f7a72 | -9.0156 | -60.507801 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 55dc4bca-2502-356e-a3ca-bf7eca9eac14 | -15.3179 | -56.4557 | 2026-08-19 00:59:00 | METOP-B | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0ed9794d-efef-3e98-b363-7fca7aed5055 | -21.437 | -48.509399 | 2026-08-19 00:59:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 55d128ad-d315-30ec-94b1-899d5a1bc1cf | -6.8875 | -56.426998 | 2026-08-19 00:59:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 013d8de5-02f4-3a22-9a85-21cd41c01fc1 | -9.2096 | -60.818001 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f665221-9e44-39e3-8909-eff97158f8bd | -19.7644 | -57.947201 | 2026-08-19 00:59:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bd852371-a9e9-3cf2-a78c-06b625557f4d | -9.2759 | -56.888302 | 2026-08-19 00:59:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9de67ef2-2b9e-3a4b-91dd-cf065e799f60 | -7.4645 | -63.644798 | 2026-08-19 00:59:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 65481773-5de2-373b-9e09-8603da751824 | -6.8881 | -59.056999 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c76cee77-e630-3609-8dd5-1e63085eecff | -10.9391 | -57.111698 | 2026-08-19 00:59:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7090e8e9-d718-3d2e-97d2-8e554d6eb52c | -11.2155 | -55.0522 | 2026-08-19 00:59:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 364104eb-e13a-378f-b370-a64ebd0f6493 | -9.1802 | -60.824699 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab87e541-b3f8-3660-8892-4046b81efb23 | -6.7379 | -59.031601 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9d4ba27c-fdd2-3345-9c62-d41db4b50f52 | -8.5789 | -54.688999 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ae030b0-1d95-376f-84af-22862946fc8a | -3.2209 | -61.260799 | 2026-08-19 00:59:00 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 714e993c-ae02-3b71-abe1-43fbc5223e86 | -6.0853 | -57.913502 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce7f5d8d-fcf6-310f-9d21-80c4430088e6 | -8.5212 | -54.747799 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3a33b39-8f82-3e48-b824-e92aa90ae36f | -8.5469 | -54.7267 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8862bd6f-5525-3b1e-b6cd-05a9c66b43a2 | -7.5558 | -55.563801 | 2026-08-19 00:59:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bb767ae-36a8-3666-94e2-0b9e99a1cd32 | -16.263901 | -57.665798 | 2026-08-19 00:59:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 809341ff-0e3d-3d9f-9a22-d0ab17b6db6c | -19.754601 | -57.9496 | 2026-08-19 00:59:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fa22347b-ec4c-31b8-a198-c74ef46fe547 | -6.8048 | -59.4543 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 002bc017-ed80-369f-8885-90bc327901f9 | -7.428 | -59.787201 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 945278b8-2a1e-327e-9f65-84f57e05726c | -7.4629 | -63.637501 | 2026-08-19 00:59:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4111da68-34bc-387a-a773-06600d6899a6 | -8.5766 | -54.763699 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43d434c6-73ad-31c8-88c2-2562db1fed1a | -3.0967 | -61.212898 | 2026-08-19 00:59:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c729e7d3-baf5-373b-b35b-beeb46fec1cd | -6.3006 | -55.866501 | 2026-08-19 00:59:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e80d7ee7-e9e5-396a-981e-4694d03bab85 | -9.4117 | -60.572701 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fda5c3d7-8dc4-3bc0-bb03-c7a0867191e5 | -6.6934 | -58.9291 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1471f883-1942-307f-95ca-f88786feb036 | -5.9944 | -57.8335 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcdc0f2c-a9a5-3cab-ae5d-a6a78c0a834e | -8.58 | -54.777599 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f27fd591-99c1-3eb0-9429-556ef5ed424f | -9.1818 | -60.831699 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 49b70d1a-e047-3433-9786-4db1f9355201 | -6.0088 | -57.850601 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f694c91-ad65-3b8b-b5d2-98ded3fddc82 | -8.5566 | -54.7243 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4fb1221-bac3-347b-bf4d-6ce5d0d5beb2 | -6.1182 | -57.702099 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60257d71-88a9-3b3d-a096-2e7a8515cf9c | -4.1215 | -60.7831 | 2026-08-19 00:59:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f6307d19-97d9-3207-a23a-1ff03e4efa94 | -6.0959 | -57.870701 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69bd6799-da56-3e19-8903-4ae18e7053ae | -6.861 | -59.0289 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 06165b7c-d8f1-3271-8f87-9d05816fbe54 | -4.2821 | -60.854401 | 2026-08-19 00:59:00 | METOP-B | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e5b74b2e-d697-342b-8ce4-4f4b53e37324 | -6.6973 | -58.945702 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0e1eca2d-fb67-3a60-a0d4-ee0526877c87 | -10.4185 | -61.2005 | 2026-08-19 00:59:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 279e338b-0abc-34bd-83be-4688f14c9cc9 | -7.546 | -55.566101 | 2026-08-19 00:59:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5eecaf11-7427-37c4-8700-d1fa38b0c68e | -6.8417 | -58.990299 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8e98c8e4-4fc8-3393-90d5-63e584f9e33c | -8.5595 | -54.693802 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bcef83b-fef4-38f7-ae51-4779c70669e6 | -9.3857 | -60.549099 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bd49e24b-a8d0-3ce5-840e-f0ed64c98fd2 | -9.4253 | -60.4063 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c770efe8-6df0-3e9a-83f6-80174b47896e | -3.095 | -61.2057 | 2026-08-19 00:59:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 993a55e2-28d8-38fb-91ca-86beb5b7c657 | -9.0797 | -50.800999 | 2026-08-19 00:59:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 820c56b8-84f0-3390-b67c-84afd2cb21d7 | -6.0928 | -57.9016 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0b65ea5-2909-3b0e-ab25-4d62abcbe3dc | -7.0491 | -59.842602 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9f0ac097-37cc-3f37-8938-739e18400436 | -6.7417 | -59.048 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 88ef6f67-9ab6-358f-97f4-ff574cb3f2a4 | -21.0401 | -48.470001 | 2026-08-19 00:59:00 | METOP-B | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d7e5c3ab-122b-3b9e-b474-2d0423339ee0 | -8.5703 | -54.779999 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| baff523b-c0e8-3102-8d23-c67907864b3f | -9.45 | -60.288601 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dcaadfbc-78bd-38d1-90c3-2bc4cf6450b9 | -7.5296 | -55.5835 | 2026-08-19 00:59:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dc2ed2b-ccef-3ca3-83e8-49aa3062bcec | -4.2805 | -60.847198 | 2026-08-19 00:59:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5ff0c180-3b10-3eab-8dcf-1dc947f69fb0 | -6.8843 | -59.040699 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b1a09507-5a0b-3bdb-bb9c-c6622b8062bd | -7.4298 | -59.794701 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cb2f8cdc-a2ac-33cd-b6e5-4926617ada99 | -6.8726 | -59.034801 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 65cc7801-979a-3293-ad4f-89e842381e5c | -14.132 | -52.959499 | 2026-08-19 00:59:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 188603d4-2cee-3ec8-9cc7-1691f8d38c95 | -8.5663 | -54.721901 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb25bf30-50ff-37a3-b2ac-e264eac1f5c0 | -10.1055 | -54.2761 | 2026-08-19 00:59:00 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fbe0daea-17a9-3bf1-b01e-651da5ca2582 | -6.1416 | -57.890202 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4283ef7e-795a-3202-88cb-6758afe98d89 | -15.3136 | -56.437901 | 2026-08-19 00:59:00 | METOP-B | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| abf3cbcf-2bab-3b0e-911a-2003646e0c40 | -6.8512 | -59.0312 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5afbe6e6-f420-313d-a073-8eadbc5c4ff9 | -9.221 | -60.822701 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
