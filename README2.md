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
| cc9d0392-1e56-3ef1-847d-06a6c22d43d2 | -11.2599 | -65.299 | 2024-09-26 00:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 118.1 |
| fe73f6bb-1a44-3593-b17a-54c890b2743d | -11.26 | -65.2801 | 2024-09-26 00:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 134.7 |
| 745aa5b7-4987-314f-a966-d6eaeb10a1e1 | -11.4598 | -47.3107 | 2024-09-26 00:06:11 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 66eed599-8980-32dc-bd19-931f8cbfc750 | -11.2786 | -65.2982 | 2024-09-26 00:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 4b31b1fe-21c8-3793-abd4-893a3e9ad34a | -11.2788 | -65.2793 | 2024-09-26 00:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 71.8 |
| e741658f-df1a-38be-888f-ff3198afcbbe | -11.5972 | -60.3475 | 2024-09-26 00:06:12 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 554dfb89-bc60-305b-ab61-cac2cc8db410 | -11.616 | -60.3463 | 2024-09-26 00:06:13 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| dca916b3-d14e-3ff3-b779-5816da4b0f20 | -11.8613 | -49.6327 | 2024-09-26 00:06:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 5ba8b630-7a1c-3934-b900-80fba584344e | -21.1653 | -42.068401 | 2024-09-26 00:06:13 | METOP-C | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c8018a14-4630-34db-b6e3-1642b20fd5b7 | -12.5085 | -53.498 | 2024-09-26 00:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 158.5 |
| 3388cf79-f20f-37f3-ac32-f91251a28076 | -12.5088 | -53.4772 | 2024-09-26 00:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 3e354962-4df8-3a01-a17e-8421b39a66d9 | -12.5273 | -53.5168 | 2024-09-26 00:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| b8fa9288-510a-3cf9-a1c5-53cb5abd2305 | -12.5276 | -53.496 | 2024-09-26 00:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 237.6 |
| 39797d10-8eb3-3508-bd47-bc9c528cad98 | -12.5467 | -53.494 | 2024-09-26 00:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| b13c8ba6-c115-3eb3-a8ae-b81710714868 | -12.7898 | -51.2593 | 2024-09-26 00:06:18 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 5a072c7f-496d-3497-b1ad-06a4ee92ef21 | -12.7901 | -51.238 | 2024-09-26 00:06:18 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| cb7af9df-faa2-3167-9e0b-bd202b524943 | -12.822 | -62.7078 | 2024-09-26 00:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 01579dda-121a-3613-9709-cfe5859295db | -20.635 | -41.063099 | 2024-09-26 00:06:19 | METOP-C | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f69decd5-2949-3f3a-af79-295b70dc68b2 | -13.0295 | -57.2985 | 2024-09-26 00:06:20 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| f16e0434-384f-3fd4-bccf-4a05b53d0611 | -20.5952 | -41.2286 | 2024-09-26 00:06:20 | METOP-C | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7e1a80fc-d099-3475-8b89-6aa7f0ac8cb8 | -13.4993 | -61.2698 | 2024-09-26 00:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 0f9e0215-849e-3e4a-a69f-200ce5c6683e | -13.7509 | -51.0951 | 2024-09-26 00:06:24 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 6fae9a76-63d8-3cb7-b324-57911e5f1c7f | -13.7513 | -51.0736 | 2024-09-26 00:06:24 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 2623b775-ef33-3d9f-8803-c64fc9816299 | -20.4198 | -41.8633 | 2024-09-26 00:06:25 | METOP-C | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3c626470-9c67-33a9-aad8-05ed0973f401 | -20.422199 | -41.876202 | 2024-09-26 00:06:25 | METOP-C | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 984c0eef-7889-3e58-8b3d-ba6f659dcc70 | -20.4245 | -41.889 | 2024-09-26 00:06:25 | METOP-C | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ca57c7dd-a13a-3269-8bdd-ab6e65698ef6 | -20.293501 | -41.242199 | 2024-09-26 00:06:25 | METOP-C | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 278a7429-9b65-30d9-abea-a38cd1d833b1 | -20.2957 | -41.253899 | 2024-09-26 00:06:25 | METOP-C | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dbf6dba4-ce2a-356d-96c6-332121af5df2 | -20.41 | -41.8652 | 2024-09-26 00:06:25 | METOP-C | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5b53601c-3b33-3795-abc0-98819b265cfc | -20.412399 | -41.878101 | 2024-09-26 00:06:25 | METOP-C | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2cc979de-cf10-3bdc-80c1-f810f8c3349f | -20.4147 | -41.8909 | 2024-09-26 00:06:25 | METOP-C | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 98c26690-a4ff-3325-9fc5-59d14799ac06 | -20.4027 | -41.8801 | 2024-09-26 00:06:25 | METOP-C | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9725d83a-1898-32ec-9262-6e59fd8ab0e7 | -20.3929 | -41.882099 | 2024-09-26 00:06:26 | METOP-C | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e5d115f8-b411-3d59-9200-339ab7b6d28a | -20.251301 | -41.287399 | 2024-09-26 00:06:26 | METOP-C | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 250cb9a8-0e59-34c9-aa32-bc6ccc8efb24 | -20.2535 | -41.299099 | 2024-09-26 00:06:26 | METOP-C | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 268d05f8-0f3f-3b0f-8e8f-432156b4950c | -20.275101 | -41.467602 | 2024-09-26 00:06:26 | METOP-C | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6bc04ae9-7257-3a90-8117-9cc51f03209b | -14.5705 | -45.6973 | 2024-09-26 00:06:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 30cccb12-d31b-38e9-aa48-2f6bdf397ba7 | -14.551 | -45.7007 | 2024-09-26 00:06:28 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 56c5de55-183b-3dfe-81d6-dc755092aad1 | -14.571 | -45.674 | 2024-09-26 00:06:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 4c591950-cda4-347f-ac40-1a5bfc178e82 | -14.9348 | -57.9634 | 2024-09-26 00:06:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 3ec41545-6a94-3db2-b3a7-ec358dda6d29 | -14.9351 | -57.9432 | 2024-09-26 00:06:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| b818548c-72da-3a91-adf5-53a1a291c1d8 | -14.9541 | -57.9615 | 2024-09-26 00:06:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 244ba870-2ea5-3372-b163-9e6608ddcbc2 | -14.9544 | -57.9413 | 2024-09-26 00:06:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 57f45586-506f-3833-aa71-21b005b0860f | -19.910299 | -41.630402 | 2024-09-26 00:06:33 | METOP-C | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5f801bed-5d0d-30c0-9d9a-8370e28ca380 | -19.9126 | -41.642502 | 2024-09-26 00:06:33 | METOP-C | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ab9644d4-305d-357c-8c80-472dd437a249 | -20.198999 | -43.4305 | 2024-09-26 00:06:33 | METOP-C | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 24c51ace-f75c-36aa-925c-e0acdaf9614a | -20.201799 | -43.446499 | 2024-09-26 00:06:33 | METOP-C | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0b5994f4-bd11-384f-a368-d2c1273f0a14 | -20.1548 | -43.522301 | 2024-09-26 00:06:34 | METOP-C | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3572359e-b5c2-3248-905d-d595059ced3e | -20.111401 | -43.4473 | 2024-09-26 00:06:35 | METOP-C | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 988df744-41f9-301a-8f75-a07bae9b9fae | -19.8151 | -41.932999 | 2024-09-26 00:06:35 | METOP-C | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8cf21d2a-0619-3de3-9330-9243d93c4576 | -19.817499 | -41.945702 | 2024-09-26 00:06:35 | METOP-C | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2e88a0ab-9da3-3e69-b3eb-12d088915175 | -20.0124 | -43.1749 | 2024-09-26 00:06:36 | METOP-C | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8b413e94-947d-3552-809e-19b0d0892da7 | -20.0151 | -43.190201 | 2024-09-26 00:06:36 | METOP-C | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| de1f03e6-6ffa-3d44-9024-3aa3c7b2ad10 | -19.7054 | -41.9422 | 2024-09-26 00:06:37 | METOP-C | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6dd06096-4702-3091-be1f-55f4aebe286d | -19.93 | -43.7869 | 2024-09-26 00:06:39 | METOP-C | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 75de9b32-4faa-3633-bead-ebc5f04c124e | -19.917299 | -43.771999 | 2024-09-26 00:06:39 | METOP-C | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9f7b7989-43b3-3f2e-9e40-58ed850145d7 | -19.9203 | -43.788799 | 2024-09-26 00:06:39 | METOP-C | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8d951973-12dd-3630-bd71-70e41305e24b | -19.923201 | -43.8055 | 2024-09-26 00:06:39 | METOP-C | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 394ee5dd-62fd-3509-bb67-dfb24a005d2c | -19.9105 | -43.7906 | 2024-09-26 00:06:39 | METOP-C | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 79217cf9-f166-33dc-bd0d-847b2f5988ac | -16.8036 | -57.5016 | 2024-09-26 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.1 |
| 63b5eb61-db1d-3280-9f1e-fef4a7d867dc | -16.8039 | -57.4811 | 2024-09-26 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.3 |
| 06836a96-0f7a-325b-90fa-878da6a876de | -16.8228 | -57.5198 | 2024-09-26 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.1 |
| 666d3908-8317-36c4-b8b1-b48ca82aad44 | -16.8231 | -57.4994 | 2024-09-26 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 150.1 |
| 5cef1ab0-f1b3-3f9d-bf17-08fd3bbdb783 | -19.6105 | -42.794998 | 2024-09-26 00:06:41 | METOP-C | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 330dc59e-d020-3880-a8ea-41f24e62486f | -19.607901 | -42.780701 | 2024-09-26 00:06:41 | METOP-C | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 12b9ca80-39bb-3d5d-a9cb-a6fb7738c0fc | -19.598101 | -42.7826 | 2024-09-26 00:06:41 | METOP-C | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6650d6d8-229f-32a3-8309-336ecdc3faed | -19.6007 | -42.796902 | 2024-09-26 00:06:41 | METOP-C | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4daccb0a-9182-3672-bfb6-25d415706337 | -16.9729 | -57.931 | 2024-09-26 00:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.2 |
| 3b746fc3-198f-37a4-9c32-53d38f34afa7 | -17.096 | -56.3576 | 2024-09-26 00:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| c62930fe-742b-3995-8b45-cffe42446336 | -19.631001 | -44.144402 | 2024-09-26 00:06:45 | METOP-C | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5e67ce4e-9c4f-3134-bf05-225fed9c359a | -19.634001 | -44.1619 | 2024-09-26 00:06:45 | METOP-C | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e17529d3-fece-3fbd-8219-71e039b47506 | -19.6243 | -44.1637 | 2024-09-26 00:06:45 | METOP-C | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| df042667-0a3f-351b-a79c-8ebc73bd511b | -19.614599 | -44.165501 | 2024-09-26 00:06:45 | METOP-C | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e1aa3f16-e364-33ce-aaeb-9068c57b8ecc | -18.1403 | -42.7818 | 2024-09-26 00:06:46 | GOES-16 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.4 |
| 204a0085-60e7-3bb4-b2be-a3a2eb63eb4e | -18.141 | -42.7569 | 2024-09-26 00:06:46 | GOES-16 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 50.5 |
| d65f2e8c-c33d-3d62-a0a7-9d1c1a2fc649 | -18.1605 | -42.7767 | 2024-09-26 00:06:46 | GOES-16 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 123.2 |
| 53a6aab6-9cd4-3553-8a36-1321baf13f1d | -18.1612 | -42.7518 | 2024-09-26 00:06:46 | GOES-16 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.9 |
| 503c5648-881e-324a-b1ac-d739f4603b79 | -19.1726 | -41.857201 | 2024-09-26 00:06:46 | METOP-C | ITANHOMI | MINAS GERAIS | Brasil | 3133204 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9d8880d7-547a-30e8-83f1-d79d8e098c9e | -19.1749 | -41.869499 | 2024-09-26 00:06:46 | METOP-C | ITANHOMI | MINAS GERAIS | Brasil | 3133204 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e4d2ad90-1d8d-3fbe-aba4-bbf80b6e5413 | -19.253099 | -42.719898 | 2024-09-26 00:06:47 | METOP-C | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b46b36b5-b86a-347c-873c-380b6cf1f1a1 | -19.131701 | -42.447899 | 2024-09-26 00:06:48 | METOP-C | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d84457f4-c698-350a-b252-2ccbf61682ae | -19.134199 | -42.461201 | 2024-09-26 00:06:48 | METOP-C | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eed5d95c-d2f7-33cc-85e9-d8f6a4439e39 | -19.1367 | -42.474499 | 2024-09-26 00:06:48 | METOP-C | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a27e3444-77de-35f9-8694-e5e6b3d810d0 | -19.929 | -43.7959 | 2024-09-26 00:06:56 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| 04adf322-b632-30c5-9f9b-14a4ad571973 | -19.9298 | -43.7711 | 2024-09-26 00:06:56 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.5 |
| 486e8e4f-dbc5-3571-aa7f-2bc083bb1fbd | -20.4197 | -41.8798 | 2024-09-26 00:06:58 | GOES-16 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 444.9 |
| b0cc76a5-14c3-3ea9-bd9a-3309d2092d10 | -20.4206 | -41.8541 | 2024-09-26 00:06:58 | GOES-16 | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | 305.9 |
| 73070f55-1981-3ac0-8023-28222acb9031 | -20.4404 | -41.8737 | 2024-09-26 00:06:58 | GOES-16 | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | 153.4 |
| 7cdfe260-b9e6-3eba-95ad-b3d345123652 | -20.4413 | -41.8479 | 2024-09-26 00:06:58 | GOES-16 | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.3 |
| 4d8429ac-6052-3352-93bf-84b7880c5916 | -20.5876 | -51.5026 | 2024-09-26 00:07:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 118.7 |
| 5ece34e5-3009-3f36-bfda-fb16a0a7765f | -20.5881 | -51.4802 | 2024-09-26 00:07:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 198.6 |
| d710d8f4-40b2-3ed3-9b7f-4816f499488a | -20.608 | -51.4986 | 2024-09-26 00:07:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 201.2 |
| c086838f-ea99-3ada-880c-5c09239b0160 | -20.6086 | -51.4762 | 2024-09-26 00:07:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 244.6 |
| 59e17df3-f7a1-3360-8808-7d27c30ba783 | -20.6284 | -51.4945 | 2024-09-26 00:07:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.6 |
| c3a5bd8f-c510-3c67-b3cb-f0fb6ca07119 | -21.2733 | -51.0061 | 2024-09-26 00:07:04 | GOES-16 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.3 |
| b122ab40-c482-3f4a-bcf0-c4103afdf830 | -18.1471 | -42.7565 | 2024-09-26 00:07:05 | METOP-C | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 929e643f-8419-3524-8f9d-2e342efc182b | -18.1497 | -42.769901 | 2024-09-26 00:07:05 | METOP-C | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 75099b09-9a0d-3d9a-9513-f9cc4e77d1fb | -18.152201 | -42.783401 | 2024-09-26 00:07:05 | METOP-C | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 749439a0-3a89-3fba-baa9-e9edd6855bad | -18.1399 | -42.7719 | 2024-09-26 00:07:05 | METOP-C | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aa39a1f5-5002-341c-a45f-a4c904edf91a | -18.142401 | -42.7854 | 2024-09-26 00:07:05 | METOP-C | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README3.md)
