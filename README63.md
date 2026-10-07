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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0dc4a40-17d8-34ad-8fbb-68b55fbb4709 | -8.90727 | -49.97475 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 859efcf6-07e5-3df5-b09a-987072c15969 | -8.53208 | -55.37689 | 2026-10-07 04:21:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b734f60d-f106-395f-b3b4-20207f83f88a | -12.19643 | -48.42096 | 2026-10-07 04:21:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55102ba0-9dff-386c-a7b9-2ab77ba634f9 | -10.97925 | -45.41113 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f5a3dbd-cc31-3695-9253-2f9f7ad6462d | -8.2369 | -50.56717 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6373b90-035d-3a92-8582-2fedafc9bf71 | -11.11282 | -45.73602 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0aaaf35b-6ee2-3311-82de-259bd6249d1e | -11.37686 | -46.69025 | 2026-10-07 04:21:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 83f20662-fa18-3964-9914-6e0adfc570eb | -11.04831 | -45.80403 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76e328fe-2ce5-3201-a27b-8f29658ba669 | -11.21587 | -46.23781 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2c959470-2cf3-3406-8d3a-c1f1e7c0ce08 | -14.55651 | -46.94428 | 2026-10-07 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78eab8a3-e265-39b4-b06e-64fe7dbd452d | -11.05046 | -49.57652 | 2026-10-07 04:21:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0243b02-deb7-323d-b38c-0890735a1d3c | -11.45625 | -43.38984 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 504552cd-5b87-341b-812c-9fcfe0909c6d | -11.77514 | -46.57032 | 2026-10-07 04:21:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5acbd3c-7bf8-3ea9-9ece-225bfdd8034b | -11.06316 | -45.77661 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52558056-8103-36af-b824-ef6b43d8596e | -9.44044 | -45.82953 | 2026-10-07 04:21:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e68397ae-faab-3d94-adac-d454e31b9554 | -9.45838 | -49.85455 | 2026-10-07 04:21:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30ccfd1d-89bf-3f91-941d-419c0a925a56 | -11.45235 | -43.39289 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebc64674-d2a3-365d-a7a9-8f99a72214d6 | -18.18028 | -42.34507 | 2026-10-07 04:23:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a7e90bd9-36d3-358b-a66d-4222c256b8de | -17.73647 | -42.3757 | 2026-10-07 04:23:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83706bd1-256a-35f0-8a26-3ab418355779 | -17.37161 | -42.1358 | 2026-10-07 04:23:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 30d9447e-48ea-3797-add4-cc9168ec0901 | -16.35937 | -47.22925 | 2026-10-07 04:23:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 47587edb-4eec-3967-8431-3006aca64956 | -18.53522 | -41.91997 | 2026-10-07 04:23:00 | NOAA-20 | FREI INOCÊNCIO | MINAS GERAIS | Brasil | 3126901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b19d8bf7-addd-3220-bfee-c44ea3e153d0 | -16.58002 | -46.76048 | 2026-10-07 04:23:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11be912b-a186-3f0c-847e-093f219abae0 | -18.18397 | -42.34565 | 2026-10-07 04:23:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f8587e1b-f3f9-3702-b16d-8b39d29081b7 | -17.28955 | -45.35877 | 2026-10-07 04:23:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f47a845-2c94-343b-8aea-905a1c9eeb68 | -17.87927 | -45.99216 | 2026-10-07 04:23:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a923d71d-6843-3610-8e93-25c36b6e6225 | -17.87654 | -45.98798 | 2026-10-07 04:23:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cbc0560-09b4-3566-a9d3-a019fb3a7d1d | -16.4135 | -51.86702 | 2026-10-07 04:23:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| defd665a-2385-3747-b95c-3ea3f0addb18 | -17.43772 | -43.637 | 2026-10-07 04:23:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 847b749a-b9ea-3dee-bbe6-c85849efa371 | -17.87596 | -45.9916 | 2026-10-07 04:23:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd177063-c56e-3a46-815a-0847e780026f | -17.43831 | -43.63297 | 2026-10-07 04:23:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6783f012-62ba-3355-9125-f47bebe962ee | -17.43714 | -43.64097 | 2026-10-07 04:23:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdc0cd71-841f-362e-90a4-8dfd6518f178 | -17.43486 | -43.63237 | 2026-10-07 04:23:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86ceb516-200c-3763-b386-b480d90c4fa1 | -18.53077 | -41.92428 | 2026-10-07 04:23:00 | NOAA-20 | FREI INOCÊNCIO | MINAS GERAIS | Brasil | 3126901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9ca4598b-7ac6-335a-9d6f-b902e4046e68 | -17.4337 | -43.64034 | 2026-10-07 04:23:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aad59e66-afea-396f-889c-dc92b427e1c7 | -17.43428 | -43.63637 | 2026-10-07 04:23:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05e08e9d-59a1-314f-8339-68ebeffc05db | -16.74867 | -45.81858 | 2026-10-07 04:23:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a384a154-8367-3b09-a394-47d4f8f03c0c | -17.43255 | -43.64825 | 2026-10-07 04:23:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ad8cfa1-d5c8-3519-a272-8e7b320a4e41 | -18.53142 | -41.91941 | 2026-10-07 04:23:00 | NOAA-20 | FREI INOCÊNCIO | MINAS GERAIS | Brasil | 3126901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 44f6f2c4-670a-3f46-8796-1cda1f247f40 | -17.77395 | -43.00724 | 2026-10-07 04:23:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36bbb044-c186-3bc3-9f49-9d2633a28c8b | -18.18091 | -42.34055 | 2026-10-07 04:23:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7dd3ed8d-eeee-3145-b35f-58e3575860fc | -17.61366 | -40.32135 | 2026-10-07 04:23:00 | NOAA-20 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b0cdd3e5-2340-361a-adcc-1a3135dd04dd | -16.58396 | -46.75738 | 2026-10-07 04:23:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55149294-83d2-3307-b1c5-b71fb0fd9b06 | -17.04496 | -45.70583 | 2026-10-07 04:23:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 061314df-362a-334a-bfb4-7b8ae60ddcd8 | -20.46635 | -42.34073 | 2026-10-07 04:23:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d3dd3d28-d460-3adf-93a9-5d61d06d198f | -17.87539 | -45.99521 | 2026-10-07 04:23:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae8971b2-f25c-3e58-aa1c-b5ad31e8d869 | -16.63512 | -44.34717 | 2026-10-07 04:23:00 | NOAA-20 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c218cab5-bc62-33ca-aae4-d84334194e9c | -17.88561 | -40.35637 | 2026-10-07 04:23:00 | NOAA-20 | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 78a68fd5-a8a2-3595-b4d0-f9d9f9e3ee3a | -18.18459 | -42.34114 | 2026-10-07 04:23:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 69100622-4b73-3d19-888f-394f7556667a | -17.43312 | -43.6443 | 2026-10-07 04:23:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c47c68cb-8221-3f80-9b69-ca9d5037935c | -19.65884 | -43.69527 | 2026-10-07 04:23:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b046a5f8-2d1a-3415-8267-6787142ed973 | -2.7613 | -54.074 | 2026-10-07 04:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| f4c62a9e-4c8c-3395-8e6b-4d7615de6040 | -9.1517 | -65.9554 | 2026-10-07 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| caadc700-99ca-394b-8bd8-4e48c75bca26 | -3.1787 | -50.5597 | 2026-10-07 04:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| e47d7ca6-dabe-3000-ba9b-1acbcecda626 | -3.5127 | -54.6562 | 2026-10-07 04:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 8829b6eb-1be8-33cf-8e13-e1faabe65ef5 | -2.7796 | -54.1138 | 2026-10-07 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 372eb18d-5d5d-34cc-b646-f8e410e049b9 | -3.073 | -54.2674 | 2026-10-07 04:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 5c0fb4dc-05c9-3e8c-a53c-82a4bc784b36 | -3.0914 | -54.2669 | 2026-10-07 04:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| bad85738-30d8-31c2-9a96-4c6185bef146 | -3.5311 | -54.6357 | 2026-10-07 04:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 99d68969-969d-3e4e-8715-3904b2cff75f | -3.1972 | -50.5592 | 2026-10-07 04:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 7949821d-9afb-341e-8910-ccaf3fee2dc9 | -3.4762 | -50.0883 | 2026-10-07 04:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| f84225a8-3e9c-3984-87c1-f0accf1abdd2 | -2.7797 | -54.0736 | 2026-10-07 04:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 24940821-0535-32e9-bf3f-fab88eca5a98 | -3.531 | -54.6557 | 2026-10-07 04:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| bbedc824-fe73-3527-9d7a-c67b29541184 | -2.7613 | -54.0941 | 2026-10-07 04:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 211.9 |
| 1fd7b538-3527-3c7a-a748-9e051e6723d5 | -3.8566 | -55.9967 | 2026-10-07 04:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 6d2aa299-1ef0-31df-953b-4556519361ec | -3.0 | -54.1287 | 2026-10-07 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| af9c6bef-624a-35b1-8020-7b881e4fd48e | -3.658 | -60.6222 | 2026-10-07 04:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 769045fc-0fed-3a07-9b22-bc9adcdb5c7e | -3.1115 | -53.7637 | 2026-10-07 04:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 29521f38-9ddf-34b6-91ee-93a9439a1984 | 1.7121 | -55.6261 | 2026-10-07 04:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 07a515a3-4ab6-3bb8-a862-a01d4addd428 | -3.0731 | -54.2473 | 2026-10-07 04:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 92cf809c-52c0-3e84-81ee-dd6633ec461d | -2.7612 | -54.1142 | 2026-10-07 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 135.7 |
| ed5182ce-9e98-3fdf-a353-903c3a8dbd62 | -3.8567 | -55.9769 | 2026-10-07 04:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 95e3202a-8967-3f6a-acf2-cbd6706e26ba | -3.0913 | -54.287 | 2026-10-07 04:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 5cdbe921-0482-3805-bb00-252293eb79e1 | -2.7796 | -54.0937 | 2026-10-07 04:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 157.8 |
| 66003112-d7d1-34af-b78e-bd407c9a37da | -2.7612 | -54.1142 | 2026-10-07 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| aac84737-ee4f-3f48-92cf-1be412dfd040 | -3.1787 | -50.5597 | 2026-10-07 04:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| e603c33c-50ff-3220-bf03-f2e02e70f3c4 | -3.5127 | -54.6562 | 2026-10-07 04:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| df83529c-ac7f-3c8b-a318-913707d3b456 | -3.0 | -54.1287 | 2026-10-07 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 49a12b71-d2a0-3855-a05a-cf9acbbd1500 | -2.7797 | -54.0736 | 2026-10-07 04:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 5bfe39a8-82a3-3746-8f4d-c5bca8bab1cc | -3.8566 | -55.9967 | 2026-10-07 04:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| e0902071-f20e-3aac-8513-e62005d80452 | -3.531 | -54.6557 | 2026-10-07 04:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 88e231fc-2cb9-3294-be7b-e26c2be5ec05 | -3.658 | -60.6222 | 2026-10-07 04:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 70e039b1-021c-3c86-a714-2c04bcac09f2 | -2.7796 | -54.1138 | 2026-10-07 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 7a69b379-24d7-3d17-bbd0-c49231f43b00 | -3.1972 | -50.5592 | 2026-10-07 04:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 5c6808c6-4b0e-3de7-aabf-b8f924b821b8 | -3.0914 | -54.2669 | 2026-10-07 04:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| b54d5ed0-aa08-3f04-a248-9c700b906ad2 | -9.1517 | -65.9554 | 2026-10-07 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| d25b8c30-d434-3e30-bd39-409c333de53e | -2.7796 | -54.0937 | 2026-10-07 04:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 174.8 |
| 8d12be21-1b16-34ca-9077-e75f9916942d | -2.7613 | -54.0941 | 2026-10-07 04:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 188.1 |
| 719717bb-5ca6-340d-b35a-f04403785dbb | -3.5311 | -54.6357 | 2026-10-07 04:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| f703eb08-3026-390f-b437-2feb554475f2 | -2.7613 | -54.074 | 2026-10-07 04:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 7cc1dd3d-91af-311c-8343-f2b4678a5d42 | -3.0913 | -54.287 | 2026-10-07 04:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| aa3d5e86-42fa-387c-b90e-ce77acd783f7 | 1.7304 | -55.6061 | 2026-10-07 04:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 3e79e8cf-5196-3c01-aa56-6ff0110406f1 | -3.8567 | -55.9769 | 2026-10-07 04:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 7bc9fd57-f43b-3b6f-9b34-c175523c886d | -2.7613 | -54.074 | 2026-10-07 04:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 8c06e0ec-1a28-37f6-8b21-5f8e2acbaaa0 | -3.8567 | -55.9769 | 2026-10-07 04:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 685ec96f-0e7a-397d-9238-da72e92e62df | -3.5127 | -54.6562 | 2026-10-07 04:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 5a709e59-9800-3231-aeed-ba5b5d3861a5 | -3.8566 | -55.9967 | 2026-10-07 04:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 62b6bb14-5f58-3f77-8eff-ce318cabb8a8 | -3.5311 | -54.6357 | 2026-10-07 04:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| e10e924d-50c6-3a98-ae9d-f68d49d7b593 | -2.7797 | -54.0736 | 2026-10-07 04:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 115648dc-73c0-3269-a6b4-f387a8132b5d | -3.2576 | -54.0418 | 2026-10-07 04:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |


[Clique aqui para ver as próximas entradas](README64.md)
