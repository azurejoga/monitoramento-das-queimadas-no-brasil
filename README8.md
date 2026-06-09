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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a61af88-9f36-32ef-88c5-f8356f67be00 | -18.52156 | -43.63005 | 2026-06-09 04:19:00 | NOAA-21 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e6a3068-f3c2-3b42-8424-9344a9a6bbea | -23.78844 | -49.03445 | 2026-06-09 04:19:00 | NOAA-21 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0baaeeab-8a75-3671-a566-39a8c5112c24 | -23.7803 | -49.0411 | 2026-06-09 04:19:00 | NOAA-21 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6004373-0d5a-3609-a9eb-03ff4a3d4b8b | -25.27028 | -50.65591 | 2026-06-09 04:19:00 | NOAA-21 | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 54c5a684-561a-30dd-9e25-2f9f8fe3f1cb | -17.44888 | -47.18763 | 2026-06-09 04:19:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90803eff-65e6-3b43-987c-1d4dd22b0292 | -23.78437 | -49.03778 | 2026-06-09 04:19:00 | NOAA-21 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75242819-9edf-34bf-9802-5d77c13b9de7 | -17.58633 | -46.6543 | 2026-06-09 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 40ac6a16-12e1-3d9f-9a7f-181ba2ba3180 | -29.7434 | -51.19497 | 2026-06-09 04:19:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 1bcc115d-18a6-32eb-bd9e-de675adb27bc | -23.7837 | -49.04178 | 2026-06-09 04:19:00 | NOAA-21 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98284693-4ea2-3244-8370-b6f3fdd04700 | -23.56398 | -47.51308 | 2026-06-09 04:19:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 8495a2f1-edc6-3718-a309-aa47d42a5bef | -16.87291 | -49.43192 | 2026-06-09 04:19:00 | NOAA-21 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4f78558-158d-3ab1-9e04-d339e89ef2da | -19.8683 | -41.9924 | 2026-06-09 04:19:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1b4842c0-9c2d-3bc8-96cd-dbc62be41f91 | -23.56458 | -47.50933 | 2026-06-09 04:19:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| ebe39a4a-e023-3934-baa9-ce6c5b730c4b | -17.59419 | -46.64812 | 2026-06-09 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 80a5e367-7461-395c-a71e-7032a378a06d | -17.45226 | -47.18822 | 2026-06-09 04:19:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72f3ecb4-d0c0-3b19-8165-c5ce341cc272 | -18.58075 | -40.11907 | 2026-06-09 04:19:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5334430e-fa4f-397a-8308-cd3c408ad540 | -23.51552 | -48.56388 | 2026-06-09 04:19:00 | NOAA-21 | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e8d0caf-90b4-38c6-964e-f8360626aa9e | -17.5924 | -46.65915 | 2026-06-09 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c5d53107-fcd4-3894-b4c7-d191f536ce6b | -17.59145 | -46.64387 | 2026-06-09 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4672e6ef-b24e-3a85-9bcc-c2ea5be2c21b | -10.6498 | -49.3834 | 2026-06-09 04:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| ab81c8fe-f19b-399c-bafa-22873d642692 | -10.6498 | -49.3834 | 2026-06-09 04:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 1691c8c8-56c4-35aa-9647-2ded507dcacf | -5.93153 | -43.47993 | 2026-06-09 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 31145c76-18ab-35b9-a986-07e967b93b50 | -6.85691 | -45.00577 | 2026-06-09 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5609215d-6a07-37e7-9b40-86ea25d53503 | -6.64114 | -43.91618 | 2026-06-09 04:46:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80bffa09-ad72-30df-85d7-647c85c8e95e | -7.71551 | -44.566 | 2026-06-09 04:46:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e5acacb4-1bc3-3f03-9127-1b0c425d357a | -5.83649 | -43.48429 | 2026-06-09 04:46:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54964511-ea23-38ec-9a00-58c94bfc2c79 | -6.72324 | -44.37586 | 2026-06-09 04:46:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 89760266-1a9c-3bfb-9bbb-79aa0196576c | -3.50269 | -48.03876 | 2026-06-09 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e275c091-5b98-3bf7-a20c-3c4a4acd9083 | -3.49989 | -48.0347 | 2026-06-09 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08a381b4-2cd4-3e7f-ae7b-7c9e46bb3600 | -6.11779 | -53.08248 | 2026-06-09 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93486432-419a-35fa-83fb-6c571dd99143 | -3.49934 | -48.03822 | 2026-06-09 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2d1155f1-c904-326f-a716-8b1324b3a04b | -5.04475 | -43.26768 | 2026-06-09 04:46:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9818d812-30e7-315e-914b-00110ad9594b | -4.91442 | -46.81966 | 2026-06-09 04:46:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 059bc92e-535c-3649-972b-907ec67d51d7 | -3.91683 | -47.81961 | 2026-06-09 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6406dc09-61c8-3293-bc80-0d31e36157f4 | -5.80033 | -45.11354 | 2026-06-09 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 20df70cc-b935-3496-8092-7a730ded19fd | -6.57492 | -47.91633 | 2026-06-09 04:46:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4322a53-0568-3fca-918f-8287ff622a89 | -6.85293 | -45.00514 | 2026-06-09 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89f4bb28-195b-33b8-8bb5-e240496810ea | -5.80498 | -45.10915 | 2026-06-09 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 15ec85b3-9f8a-3e78-b734-73c6dff4e13b | -7.09942 | -46.51209 | 2026-06-09 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcc3ba81-deff-3769-84fa-109b754808eb | -5.80423 | -45.11407 | 2026-06-09 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bf2a64e8-e5d1-37ca-b20f-b3faf391982e | -6.72477 | -44.37519 | 2026-06-09 04:46:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fea19736-e537-3bd0-b411-5e953f87c924 | -6.57149 | -47.91579 | 2026-06-09 04:46:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16a7fd2d-5aef-3895-9c69-13606a76067f | -5.80814 | -45.1146 | 2026-06-09 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c563f26f-3df2-32cf-bfca-e48cca82190f | -5.81205 | -45.11513 | 2026-06-09 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f7b3ffc1-2bdb-3eb3-8fff-10c01e8b78d9 | -5.79642 | -45.11301 | 2026-06-09 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 207087cd-4553-3cf9-ad13-c32986829d1e | -5.8035 | -45.11894 | 2026-06-09 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a856a309-e059-31c5-b207-10d5621c9c3d | -7.10673 | -46.51323 | 2026-06-09 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 7f9e6c2e-9d52-39a1-b726-aff166926a8d | -5.8081 | -43.79292 | 2026-06-09 04:46:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 247ea356-a26a-3b0c-83eb-68c8e82dd93d | -5.2843 | -43.96173 | 2026-06-09 04:46:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2b7c5d6-2dd0-3aea-ae60-1f61c2ca82c2 | -6.64541 | -43.91678 | 2026-06-09 04:46:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ba1f8ef4-482b-3de7-a0f6-533a5f7c33c2 | -5.73016 | -49.09978 | 2026-06-09 04:46:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21cb9302-d635-39d8-b6bc-6d91c1c82265 | -5.84022 | -43.48902 | 2026-06-09 04:46:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fcde508a-5269-371b-b75f-597217360573 | -5.84143 | -43.48085 | 2026-06-09 04:46:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 36fd3373-ef51-3e08-a5f1-68b6154596b1 | -5.92717 | -43.47936 | 2026-06-09 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1f28ae3-def6-3f4e-acf0-4e06dd49c049 | -3.49654 | -48.03416 | 2026-06-09 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b659b61-0287-3e5e-b24a-1505a0df5ebf | -5.84083 | -43.48493 | 2026-06-09 04:46:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 480493c4-4cf4-3b18-88de-03c51a485f79 | -7.10006 | -46.50784 | 2026-06-09 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54dbf037-c807-31e7-9ffa-67652d2933b1 | -4.63928 | -43.04638 | 2026-06-09 04:46:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d1944aa-892c-37b5-ac50-f0899fd82b19 | -5.80107 | -45.10862 | 2026-06-09 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 097e9dfb-01b0-3d26-8e78-45460509895f | -3.49598 | -48.03769 | 2026-06-09 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 74a60796-0d15-3cb1-8f9b-73a6af830bcf | -3.49263 | -48.03715 | 2026-06-09 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6e298314-42a3-3c2a-994e-52284fe13dd7 | -7.10609 | -46.51749 | 2026-06-09 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 9d901c4a-9c4b-36aa-b7ee-ea1277e0b7f6 | -4.91794 | -46.82024 | 2026-06-09 04:46:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58de316a-dfca-3ff8-bf79-7db929921cbb | -3.60246 | -49.46021 | 2026-06-09 04:46:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b45bc067-39a0-387e-93a5-7db9e38737a9 | -3.98954 | -47.93661 | 2026-06-09 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5459f9c0-6be4-3ca5-8f17-8d1498e388ff | -5.79569 | -45.11785 | 2026-06-09 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bcba8b49-cc7a-3350-bf8a-bd697f53ecad | -7.10179 | -46.52118 | 2026-06-09 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4af43b26-a389-3998-943e-34453100c8bb | -4.63864 | -43.05059 | 2026-06-09 04:46:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d516448f-4841-3f0f-a76a-8ff844e775ba | -5.73071 | -49.09631 | 2026-06-09 04:46:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63805ec4-8057-3a49-8af9-1af59359711b | -5.7996 | -45.11839 | 2026-06-09 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7971811b-1d18-3508-9bb4-45692f3c05a2 | -5.81596 | -45.11564 | 2026-06-09 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4dcd8580-ff7f-3922-a569-3aa8e6bf0371 | -5.28903 | -43.95858 | 2026-06-09 04:46:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63ac6039-33ee-3ff7-9344-0fe812580297 | -7.10307 | -46.51268 | 2026-06-09 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 4d1d8588-1923-3f35-adf0-46e6fb5066bf | -5.04103 | -43.26288 | 2026-06-09 04:46:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| badad5f6-34bf-3e77-bf46-0432ee395d71 | -7.10243 | -46.51693 | 2026-06-09 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 09fca078-81de-3e47-97bf-fbd98bcb227c | -6.11905 | -53.08371 | 2026-06-09 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8bb1eb33-24dc-3da0-861b-dc89521417c4 | -5.04041 | -43.26698 | 2026-06-09 04:46:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 930d4c09-7973-3f80-923c-afedddddc53d | -6.64483 | -43.9207 | 2026-06-09 04:46:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8f0c7c42-a9de-3197-80cc-19b49af6a223 | -5.83709 | -43.4802 | 2026-06-09 04:46:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a239304-8487-3df1-a701-48f914c454e0 | -5.80888 | -45.10968 | 2026-06-09 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cb2707a3-05c8-3b07-b70b-00534d103746 | -10.89639 | -49.35429 | 2026-06-09 04:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed8a6719-a823-3c88-b04f-664ea2012a06 | -10.90316 | -49.35536 | 2026-06-09 04:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1750513-dff1-34b5-8bbb-c46fd83d8f86 | -9.3147 | -45.48566 | 2026-06-09 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fa2d974a-1b6c-32d4-8545-e5ed28e31885 | -11.05114 | -56.93116 | 2026-06-09 04:49:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d7cf11c-9a51-30ec-ac2f-c275709cb8f4 | -12.03199 | -47.80271 | 2026-06-09 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b3b4348-69b2-3c2c-9ba6-f71b5d226a55 | -9.76885 | -47.43987 | 2026-06-09 04:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1abd7e9b-53a5-3697-9a36-651ed0974b79 | -15.17639 | -43.85686 | 2026-06-09 04:49:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c8beec4b-5c34-3be4-aac0-496500e44d32 | -12.04136 | -45.28654 | 2026-06-09 04:49:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecf942be-f41c-352f-93cc-e2c747bdaeb1 | -9.21621 | -47.333 | 2026-06-09 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4fb113b-8517-3b6d-98a7-a9d8425c3892 | -12.85219 | -44.37368 | 2026-06-09 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 28e76141-91f4-37dd-8738-d717db0eac1d | -11.53956 | -52.78641 | 2026-06-09 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 93f946a1-8e7f-3bb1-ac35-9675c817d534 | -8.43702 | -47.89244 | 2026-06-09 04:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98b1de3f-37fc-34f3-ae3f-c056121228ff | -9.08377 | -50.60526 | 2026-06-09 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fa4ebac-13d7-3b37-8c7a-cd4832c03b28 | -11.64959 | -52.86305 | 2026-06-09 04:49:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad78b300-9d96-393f-9380-826aa0cf9c87 | -8.97076 | -47.98254 | 2026-06-09 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa6b413b-879c-3ad0-a1a6-b5f3ec355281 | -10.90372 | -49.35172 | 2026-06-09 04:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 229fa099-f215-3fee-9c93-f235c2eaef99 | -8.97773 | -47.98365 | 2026-06-09 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d8598337-838d-3177-bde0-d4d8ee0e57f1 | -13.25799 | -44.3925 | 2026-06-09 04:49:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9fe7883e-49b4-308d-89ea-ceb5f6c5c0e1 | -11.26786 | -53.97055 | 2026-06-09 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5add976e-b515-3d92-b7c9-0cc7d448c1a8 | -10.58058 | -49.64171 | 2026-06-09 04:49:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README9.md)
