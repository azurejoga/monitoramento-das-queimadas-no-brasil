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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7580267-5a03-3cf1-990f-45c15c6985d1 | -10.0163 | -47.3308 | 2024-10-14 03:46:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 45d98168-57b9-36c4-b2db-778f5b6a884b | -10.5307 | -49.7843 | 2024-10-14 03:46:06 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 91f270cf-743c-3f70-a51b-9c74872a7c62 | -12.3804 | -53.1376 | 2024-10-14 03:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 0b0abe8e-e9af-3665-ac48-04f29945e08b | -12.3807 | -53.1167 | 2024-10-14 03:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 560af646-b6ff-3636-be7c-7d98ad8daa41 | -12.3994 | -53.1355 | 2024-10-14 03:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| b5c110a2-c393-38f1-bb4b-e90976a8456e | -12.3997 | -53.1147 | 2024-10-14 03:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 96a72d27-ae4c-3b82-afbf-40412f1426bd | -12.8699 | -53.5423 | 2024-10-14 03:46:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| afbd64f4-97a2-317a-a62c-de3bbc5a7604 | -12.889 | -53.5402 | 2024-10-14 03:46:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 3a46dd86-1d30-3f8d-b971-788225ce2370 | -12.8893 | -53.5194 | 2024-10-14 03:46:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 046c57a6-edb2-3d3c-8e5b-64cb665e27e3 | -18.1905 | -56.8394 | 2024-10-14 03:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.5 |
| f1a1e23a-7d1d-3ae2-8188-e394992205c6 | -18.21 | -56.8576 | 2024-10-14 03:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 95aee1a1-0a41-311e-9495-0e515950496e | -18.2104 | -56.8368 | 2024-10-14 03:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.1 |
| bd97e900-2a37-3581-963e-e07a1f39a126 | -18.2555 | -56.5196 | 2024-10-14 03:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.7 |
| a1485725-c613-3c75-8de6-3f0c96bcbd07 | -2.4529 | -46.919 | 2024-10-14 03:55:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 57e1578a-cebd-3f16-b55e-f6c07fdb38c6 | -2.6119 | -49.0772 | 2024-10-14 03:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 19d87797-b86b-3f8b-a0d0-ea36f6ad7a81 | -2.6118 | -49.0985 | 2024-10-14 03:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 4ccb5328-ceac-3690-b2f4-7a63802d1df1 | -2.6117 | -49.1198 | 2024-10-14 03:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| b80f6472-40d1-3b2b-8990-cc367a891f0f | -3.3077 | -42.8318 | 2024-10-14 03:55:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| da93353d-ee73-38ca-bf3e-a31a742a0103 | -3.3076 | -42.8553 | 2024-10-14 03:55:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| e172c7e1-82d2-3a0f-8c3f-79f24f8635f4 | -3.289 | -42.8327 | 2024-10-14 03:55:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| dfb89f15-b13d-3c95-a8e3-6755b6bf1332 | -3.2889 | -42.8561 | 2024-10-14 03:55:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| a0e9ebc3-031b-3d97-93c1-16979d0d0ac6 | -4.1149 | -48.2299 | 2024-10-14 03:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 1740bce7-8018-332e-bc6d-a90d844aca9b | -4.1148 | -48.2515 | 2024-10-14 03:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| a1b3db3a-4ad9-3f32-bccb-41baac1668a7 | -4.3565 | -55.1291 | 2024-10-14 03:55:31 | GOES-16 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 62396073-508a-31e0-8051-a4a2b4eb6363 | -7.9418 | -63.6365 | 2024-10-14 03:55:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 28a3bb74-8c6c-3a83-83ae-b2476aececcd | -9.3264 | -52.8444 | 2024-10-14 03:55:59 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| b51b66c1-f013-3c29-97fd-613a98cd674c | -9.3451 | -52.8428 | 2024-10-14 03:56:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 37af52f9-9d78-35d0-8c6f-56cc69233830 | -10.0813 | -44.2366 | 2024-10-14 03:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 5029024d-d481-3276-b853-339b1b916447 | -10.0809 | -44.2599 | 2024-10-14 03:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 168.3 |
| aeb8e07d-49ae-3d9f-9053-965fdbc050b8 | -10.0622 | -44.2391 | 2024-10-14 03:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 5c59e81f-985c-3747-8356-51a316db5b88 | -10.0619 | -44.2624 | 2024-10-14 03:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 260263fc-ff9c-32dc-a130-26d5189f6343 | -10.5307 | -49.7843 | 2024-10-14 03:56:06 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| d866fb2b-e964-36f0-b8aa-8f5f58695230 | -12.3807 | -53.1167 | 2024-10-14 03:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 136af128-3bcd-3011-88d9-b6a7ac79d6ff | -12.3994 | -53.1355 | 2024-10-14 03:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 1b211e5b-21cc-37d6-8fe4-c12036e6ce37 | -12.3997 | -53.1147 | 2024-10-14 03:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 115.8 |
| c14e20f8-d440-39eb-9cf4-56fe9fd14190 | -12.3804 | -53.1376 | 2024-10-14 03:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 915340a2-8752-33d1-b4cf-275230f0c6cc | -12.8699 | -53.5423 | 2024-10-14 03:56:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 7d1aff7b-faa7-3df7-b733-3b38cb5550da | -12.889 | -53.5402 | 2024-10-14 03:56:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| f17bd5f7-000b-30d3-b95c-c8aaa045a174 | -16.9995 | -57.4791 | 2024-10-14 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.5 |
| ccc78117-3404-3fc3-aa7b-d7503ca4d70b | -17.0001 | -57.4381 | 2024-10-14 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.0 |
| 8007d119-677a-33cc-a1ea-76973554e0f6 | -17.0004 | -57.4176 | 2024-10-14 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.8 |
| a2086ccc-c179-3dba-aeb5-8439d66e4d49 | -17.0197 | -57.4358 | 2024-10-14 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.2 |
| 73871143-7cdb-34ba-b4b6-4fead413b382 | -17.02 | -57.4153 | 2024-10-14 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.4 |
| 8e1caeaf-a630-387b-86b1-c11018164e33 | -17.0393 | -57.4335 | 2024-10-14 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.1 |
| de6ff233-53e2-3889-ad31-b5f76c242fa7 | -17.1758 | -57.479 | 2024-10-14 03:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.6 |
| 2a3636de-3e60-3d9a-a10a-fa14c2bad43d | -17.1761 | -57.4585 | 2024-10-14 03:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.2 |
| b2440cf2-d7e2-3445-8ed6-9f6d1298fa66 | -17.1764 | -57.438 | 2024-10-14 03:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.4 |
| 6906e535-41bd-3517-a924-783e4b5fd897 | -17.1954 | -57.4767 | 2024-10-14 03:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| 4fb7f476-70ae-3874-acec-add47fad107a | -17.1957 | -57.4562 | 2024-10-14 03:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 172.7 |
| 98ca1669-6167-3f03-897e-c4844d180b6b | -17.196 | -57.4357 | 2024-10-14 03:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 140.6 |
| ffda2fc2-63cd-3184-ab11-01babbc3b811 | -18.1905 | -56.8394 | 2024-10-14 03:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.7 |
| 7d4132b5-15c5-3187-9f27-257e319be9ec | -18.2757 | -56.4962 | 2024-10-14 03:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.0 |
| 5c8711a7-4284-3b7e-ba3e-49f2b7230f70 | -18.2754 | -56.517 | 2024-10-14 03:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.2 |
| 77122345-4998-3638-b6b8-ba891c10db35 | -18.2562 | -56.478 | 2024-10-14 03:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.3 |
| 4a635781-0e44-3332-a4e8-75466ffe771f | -18.2559 | -56.4988 | 2024-10-14 03:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.4 |
| 376c0520-a103-3f31-8956-f961f39086a7 | -18.2555 | -56.5196 | 2024-10-14 03:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 208.4 |
| da8210b4-ad03-3adb-a82a-fe955a089bf8 | -18.2551 | -56.5405 | 2024-10-14 03:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.8 |
| 66b36d4a-06cd-368a-a424-cb533748d5f0 | -18.2104 | -56.8368 | 2024-10-14 03:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.4 |
| 12a1f3c4-2ac7-357a-9d53-f6015c8e6842 | -17.87 | -57.34 | 2024-10-14 04:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| af4fdd5e-f1ed-31b7-bed6-8a1431793558 | -17.87 | -57.26 | 2024-10-14 04:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 227e9feb-be4d-37ac-ba9f-bb1fea8a5c2d | -17.9 | -57.36 | 2024-10-14 04:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6154625f-7bde-31db-a39b-9811030aeb29 | -17.9 | -57.28 | 2024-10-14 04:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1e89e751-a85a-32ca-97f2-afcb32dcf963 | -17.93 | -57.38 | 2024-10-14 04:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 06323f0d-5ed9-39d0-8516-d23a263fc16f | -17.93 | -57.3 | 2024-10-14 04:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3a47271d-4c79-3ab0-9dea-212b8ac827da | -17.93 | -57.23 | 2024-10-14 04:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9a1ff6b7-7e46-391c-abdc-9492aace2670 | -17.97 | -57.4 | 2024-10-14 04:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9d97ccbd-db75-341f-98dd-37e44b5d2493 | -17.96 | -57.33 | 2024-10-14 04:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 23df3b0f-9e01-3349-87c9-3dc59e67d187 | -18.0 | -57.35 | 2024-10-14 04:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e81693c0-af4a-3db7-944a-bd09b6e9570c | -10.06 | -44.26 | 2024-10-14 04:04:28 | MSG-03 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b598e6ee-3362-3845-aa1b-3843de10c429 | -2.6118 | -49.0985 | 2024-10-14 04:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| fe06cb28-302d-3a1d-b572-657f02ab4236 | -2.6303 | -49.0767 | 2024-10-14 04:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| a0a51bbf-ea48-3a44-b6bc-f65044d80bff | -3.3076 | -42.8553 | 2024-10-14 04:05:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 121aa54b-94fa-38f5-a4c1-4a6b709e7ef0 | -3.3077 | -42.8318 | 2024-10-14 04:05:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 136.7 |
| a2513bf6-8b1a-329d-8bfa-0c055cac23d0 | -3.2889 | -42.8561 | 2024-10-14 04:05:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 933588c2-5fb1-34f7-8ec9-eba7e4a64536 | -3.289 | -42.8327 | 2024-10-14 04:05:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| dcfa5eaf-45c3-36c5-aa82-efdc6cc2b17e | -4.1149 | -48.2299 | 2024-10-14 04:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 4034ac2e-850c-33e6-9ae1-eb6ea8d68fba | -7.9603 | -63.6359 | 2024-10-14 04:05:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 126837bc-2021-3e89-ac8e-7146441770c1 | -7.9418 | -63.6365 | 2024-10-14 04:05:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| f1f810cf-d8ae-338c-8e4a-da1c3c2a0f45 | -9.3264 | -52.8444 | 2024-10-14 04:05:59 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| ad3d6030-7e68-3f95-9478-fecd8a3bb84b | -9.3451 | -52.8428 | 2024-10-14 04:06:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 7597be81-488e-34d3-ba04-0d7ebaf25398 | -10.0619 | -44.2624 | 2024-10-14 04:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 285.9 |
| c0d16362-ee2a-336e-aff2-bd7bef977fc2 | -10.0622 | -44.2391 | 2024-10-14 04:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 135.6 |
| a45f2a3d-ffae-3f3a-869b-5486d317ccd6 | -10.0809 | -44.2599 | 2024-10-14 04:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 186.9 |
| 8d2a347d-ecde-3ee5-a93f-95fa57acd471 | -10.0813 | -44.2366 | 2024-10-14 04:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 132.5 |
| cad1b33a-3e41-3fd0-944c-ed182b6bdfff | -10.0163 | -47.3308 | 2024-10-14 04:06:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 3411e49c-763b-3add-bf21-a3215c085b85 | -12.3804 | -53.1376 | 2024-10-14 04:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 9fe1a45e-626f-3b8e-bcb5-71aee3ec9349 | -12.3807 | -53.1167 | 2024-10-14 04:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 136.8 |
| b20e5c52-603b-3e06-8b1c-96acdd780a11 | -12.3994 | -53.1355 | 2024-10-14 04:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| fb6cbb60-8dbf-3fd8-bdb6-0e8801aca7a4 | -12.3997 | -53.1147 | 2024-10-14 04:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 177ea887-857e-3b88-9f9d-2a5c8399e48a | -17.0001 | -57.4381 | 2024-10-14 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.2 |
| 06da539a-bd82-3313-b7b4-8df8768dadd4 | -17.0004 | -57.4176 | 2024-10-14 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.3 |
| 8ac3ef9a-ddeb-370c-9962-e20ebaa78c5e | -17.0197 | -57.4358 | 2024-10-14 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.7 |
| 9da5f833-8444-3f5b-90c1-5a3b3903e9c6 | -17.02 | -57.4153 | 2024-10-14 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.9 |
| 6515814e-171b-30fe-a141-9ffdbb200f85 | -17.1761 | -57.4585 | 2024-10-14 04:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.9 |
| b2df094a-1f88-312a-9f16-03ddb9104f86 | -17.1764 | -57.438 | 2024-10-14 04:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 49ef5fb5-99ed-351a-8035-4627698e463f | -17.1954 | -57.4767 | 2024-10-14 04:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.5 |
| b514cc0a-b852-312b-babc-190525696066 | -17.1957 | -57.4562 | 2024-10-14 04:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 123.4 |
| 34692930-9019-37d7-950e-5c31f0533dc8 | -17.196 | -57.4357 | 2024-10-14 04:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.2 |
| 9769341a-a8d1-3738-a2cc-2a677fda8aaa | -17.2154 | -57.4539 | 2024-10-14 04:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.0 |
| 00e59bf6-085e-32b8-abe5-c4b7b38f81fc | -17.6876 | -56.2409 | 2024-10-14 04:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.7 |


[Clique aqui para ver as próximas entradas](README36.md)
