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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a85d1d23-aa27-3ac6-8279-65d56efd20bc | -12.76379 | -52.85174 | 2026-09-07 05:23:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b529543-ea42-3620-a047-31d335608f08 | -4.03245 | -52.07502 | 2026-09-07 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f83dfbd-aeb5-3250-80f5-4c126c88829a | -6.06245 | -57.79117 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cb6f5acd-bc4a-3601-94c3-8e03feb8f128 | -6.12987 | -57.74683 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4e4ca119-4d22-3c17-a95f-4316d5496647 | -5.99396 | -57.67783 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 879d914d-23e8-31d2-8787-e135735c60f2 | -6.136 | -57.68525 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53ccd3d7-c694-3201-8ff8-940c2cd814e1 | -2.9606 | -48.71165 | 2026-09-07 05:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9ad2824a-4329-3063-8727-2a64009eda05 | -4.67845 | -55.63833 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6edf91e0-7b9d-3b5e-8885-fb490161ab66 | -8.76262 | -62.42041 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4431ecf2-fe15-3690-8433-80ed9c2ab3bc | -6.13043 | -57.74323 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 82aa3378-cfb4-336a-90ea-adbbe825f5c9 | -4.66524 | -55.62804 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4b31d02-7427-31ec-8f84-8f2f657e6ea8 | -5.36105 | -56.02803 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5807f40-cdbe-33e4-add3-89eee9131da8 | -3.9592 | -55.40145 | 2026-09-07 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10ee749f-2762-3937-82c6-da341adce410 | -3.63629 | -59.55562 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13adfc5d-57db-3fdb-a11d-c60d2ec66fb0 | -2.56017 | -54.74777 | 2026-09-07 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 953f2506-c966-3e17-b3ac-ee6078053f49 | -9.24873 | -60.26313 | 2026-09-07 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85175de9-67ef-3da6-9925-ec3b811e3805 | -5.35098 | -56.0224 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bae15e67-493b-37b9-adca-6ba76bef3ef5 | -3.14657 | -60.6368 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e39d69e-a706-376f-92b1-5dcc77d82732 | -5.28537 | -60.12115 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 065a21a3-bf22-321f-8da6-e51a23840dcf | -4.21632 | -48.56835 | 2026-09-07 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1064873-6317-3a73-9fee-1e32a31dad1c | -4.28424 | -59.97002 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b35429d-f455-3e95-8b03-6d97ccc6dd8a | -5.15715 | -55.96711 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 071e9c18-9a38-3563-8a45-12f892219f71 | -3.38923 | -61.33293 | 2026-09-07 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 228020e8-ba19-3111-b878-c4552f3483ee | -5.36566 | -56.04527 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a87a0571-0861-356c-88e0-b51f75d84132 | -4.29265 | -59.9604 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| caa7f7a5-6958-35ad-b3cf-d76d59190ffd | -6.06021 | -57.80544 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cccf6b2d-9d23-3aa2-9189-56d20dba3e2c | -4.34789 | -56.281 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| efbeec9a-2698-3f33-8a39-5749310600c3 | -5.96872 | -57.69681 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c68e80c-8ed1-38d6-bfbd-c7e1ddee4835 | -4.43137 | -55.09605 | 2026-09-07 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5bdd3937-f441-30b2-84fd-8dac26e8b600 | -4.43072 | -55.1004 | 2026-09-07 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e0f3e33-ea01-3886-b730-85907b459294 | -8.72331 | -62.4385 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c50de9f-a975-3278-91c9-5a9dfc7572d0 | -4.50549 | -55.71202 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 123e11e0-9ff3-3c98-b4e8-ae2b6cf66bc0 | -5.5942 | -60.25002 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 262722ae-cc5a-35d2-82ff-6d48181bf69a | -1.19813 | -55.71692 | 2026-09-07 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 968fe163-ed54-3204-a175-c2e2e86bf2ee | -3.39279 | -61.33349 | 2026-09-07 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d498bad8-d97c-387e-a843-fbebc055b78d | -5.14289 | -55.96487 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63f21924-e9cf-3087-b381-840907e22093 | -5.99681 | -57.70403 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb972e79-9534-36bd-90a7-77d5a4871f71 | -5.30149 | -60.14926 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67781691-ab26-3b45-bc96-b9e4508385f0 | -4.4289 | -55.09752 | 2026-09-07 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ed19797-b6f7-3084-90eb-a3700c8ef688 | -6.05741 | -57.80134 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b897c2b0-0e28-3b70-8b22-f0c270360766 | -3.9224 | -59.2326 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e43d887e-20b7-3f76-b89f-0a5fff111f2a | -4.06746 | -50.64119 | 2026-09-07 05:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa76bbe4-8ab3-3902-a43b-67b67ace31cc | -3.41023 | -61.31569 | 2026-09-07 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b743e6d-7764-3951-aa85-ecf478347d54 | -3.61392 | -60.56646 | 2026-09-07 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c8d1e904-f5e8-38af-8b40-1fd1274f8158 | -2.63547 | -46.78024 | 2026-09-07 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 87658ae0-65e1-3cb5-9284-22f5c77a574a | -4.47917 | -55.08073 | 2026-09-07 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| edb00f90-7a67-3b18-b06f-742a32a0c0ea | -8.75998 | -62.4364 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f17118e-9b2b-3bac-b582-c127dab3952b | -5.6829 | -60.80674 | 2026-09-07 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a537d6a6-6142-34e3-8c55-42ee77ad67be | -3.0806 | -61.53307 | 2026-09-07 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c99ac9f8-66bc-3b7a-b8d2-69f3a80f11a7 | -6.15674 | -59.94523 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b5e6067-3d16-3771-b2a1-6468ec793a96 | -8.76902 | -62.42562 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 537b2c5f-43c3-3cba-a91a-ce34e3803dc2 | -5.45805 | -60.04313 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb31c703-7ef0-3a11-bc6a-8462909b865f | -12.76447 | -52.84638 | 2026-09-07 05:23:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 818d7470-1b5e-3e3c-9253-487c759e7207 | -6.44544 | -58.16333 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4d1dee7-d82b-3dc6-9a02-37dbfeaa0c80 | -6.01136 | -57.67686 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a8fbf68-d99f-3ded-934a-2a0a332536ab | -5.16093 | -60.21798 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e710c085-b61f-3f85-9085-e858b170a52a | -4.0318 | -52.07944 | 2026-09-07 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 003c33f8-d82f-3aeb-af1a-b79a4d222a80 | -4.54685 | -55.98116 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7fb425af-425b-3799-9ed5-ade6d9431d1b | -5.43162 | -60.12254 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d612686-dc74-39a9-9bed-ff1bafc6e604 | -6.00017 | -57.70454 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00a5e1c9-8065-35b8-8b29-150606dc8c4e | -4.20737 | -59.99801 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e7dfe355-280d-3af1-8c1b-f40e7921c6b3 | -5.16701 | -55.96668 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ff81dd2-db76-3ab0-9ec7-28ac80913cf8 | -3.90114 | -59.70969 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a14b3be-8ccc-3f9b-8b9b-d6689f46687d | -3.64018 | -60.49044 | 2026-09-07 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32c2a65a-a544-3c60-b1ef-f314271c1eef | -3.49247 | -50.60856 | 2026-09-07 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fbe9fd8-9d82-3195-82c8-e98de62834eb | -6.20672 | -57.77317 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26a882f0-c620-3a7d-af00-8a7ad17e7c52 | -3.11676 | -57.69088 | 2026-09-07 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f93e5435-0eed-300c-9d2b-bfc76052c248 | -8.86836 | -62.35154 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3c03b6dd-099f-36d0-9c09-8ff12ce5ff9c | -2.30216 | -48.59203 | 2026-09-07 05:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26396f41-0390-3458-8d8b-9b5dd822c627 | -6.10962 | -57.69957 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0e9f3dd-564f-358a-8100-37ecc81967a3 | -3.06061 | -51.24696 | 2026-09-07 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3a058a3-124f-3980-a3ee-937cac1a6bc6 | -3.38826 | -61.31628 | 2026-09-07 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a049beb-843b-3866-a293-374573f2e903 | -4.67247 | -55.62901 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3f2e0d9-e5a4-3031-aa1b-207516589620 | -4.28031 | -59.97305 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| caa6c737-c167-312c-80fd-99cb6a2109af | -3.14189 | -60.64386 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4af3094-2ea9-3cd1-be50-c418b0b97bff | -5.65077 | -60.24081 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47ae6433-fa1a-3b15-97cd-78137a7edc5d | -3.51194 | -59.05761 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f970b0e2-fc00-3b5e-b83d-e745d40efcac | -5.36273 | -56.0407 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9371b2ab-33ee-38f5-aea0-bd402e4d1f09 | -5.36963 | -56.03643 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32e0d811-4951-329b-881d-5bd74e5abd27 | -6.43704 | -54.70674 | 2026-09-07 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a7e08ad-4f69-3276-9b25-8934d030ec03 | -3.56966 | -54.55151 | 2026-09-07 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0957e8f9-9073-3033-a8bf-2da4ba6c9301 | -4.40917 | -60.07407 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 510d02ef-a01c-3d49-9e91-44a144d6ab5e | -2.4565 | -57.91327 | 2026-09-07 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7936e254-cbc6-3f98-b3b9-26ddf7b2a8c4 | 1.10266 | -60.51365 | 2026-09-07 05:23:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4871187a-b750-3593-9e08-c648c059acd5 | -5.14121 | -55.95217 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7608b930-cbbf-38f4-aadd-ea8ad51e80c1 | -3.13904 | -60.63951 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f34fa24-6def-3542-a0be-f9f9b42ca4f0 | -4.0331 | -52.07059 | 2026-09-07 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c53f7ad1-1c97-3f54-b7a1-8f4a1c24a2e2 | -6.18537 | -57.75523 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0db3edaf-e192-3005-be15-bf24148bd55d | -4.67969 | -59.59843 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5da2a3bf-5e96-3b1c-b0f9-40f891b9d4f9 | -5.48996 | -60.20123 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a7a67d0-f0ee-3655-84d0-d8d9a7860d71 | -3.37765 | -59.41054 | 2026-09-07 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2cbcd80b-0cde-35b4-9b31-6cb71e16edda | -4.28537 | -59.96289 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4a71a75-8297-3b74-bed7-88f3e8c1e8b2 | -4.12337 | -56.35003 | 2026-09-07 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f123313d-f415-3d93-a3ec-0c0079f0fa30 | -4.21336 | -48.56387 | 2026-09-07 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c10222f-783e-3f1b-88a5-6f95d9680780 | -3.81213 | -55.89162 | 2026-09-07 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6e4146fd-fdd8-398f-be9a-6c5aa75a273a | -3.74936 | -55.96714 | 2026-09-07 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6e0b6a92-bf23-31da-8bf5-0dfce4f2ab97 | -3.54704 | -59.41186 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bca6a83f-d053-3aac-88e4-da1c36faa6f2 | -4.50846 | -55.71655 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f87d485-0fb2-335e-a93c-c2cbe053bbee | -6.51335 | -58.29266 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19991360-b01a-325d-85b6-adb1809caf55 | -3.004 | -59.36574 | 2026-09-07 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README30.md)
