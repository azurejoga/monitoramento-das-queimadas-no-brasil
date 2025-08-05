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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c787c264-0f31-36a1-9b3b-8d9455853d38 | -6.78797 | -43.048 | 2025-08-05 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 565759ba-aabb-3031-89ed-f1dade22ffaf | -6.84994 | -55.11591 | 2025-08-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be14fd2d-cd53-30fd-821f-e000fccbd964 | -8.00029 | -43.13894 | 2025-08-05 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 5de81ea4-5b25-3951-9c4c-242fe78c7e23 | -9.18118 | -48.84316 | 2025-08-05 04:38:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9f1420f4-644f-37b2-ac55-94d2186af212 | -7.09006 | -44.68858 | 2025-08-05 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66dd9dd9-f1df-3c8e-8591-39f40b6a1891 | -6.42722 | -44.8186 | 2025-08-05 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ea22c611-5170-3bde-9cb1-1ab5d0ffcffd | -8.24156 | -45.05843 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 230b4ce6-c024-3061-81a3-f8b94a8f0855 | -7.47877 | -46.57932 | 2025-08-05 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26d2beb6-e44e-35cb-9451-2bc5010f38b4 | -8.95932 | -46.74523 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7502ab3f-e24a-38e4-9eab-45599c980e40 | -3.77802 | -41.68395 | 2025-08-05 04:38:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cb50b7aa-a1c2-3e90-babc-80b136ca770e | -8.71482 | -46.42933 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ec799a6-fe1d-3ccd-9ef9-1378e5818aa2 | -7.57103 | -44.88871 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d3ef0c7-5572-3641-b09c-3183e594b7d1 | -6.95953 | -44.49849 | 2025-08-05 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0704bdc0-7ff2-3fe9-91f6-4b77e4fe0856 | -7.52907 | -44.86802 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62a8a307-e236-319a-8c57-1d90d6047256 | -8.945 | -46.74118 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ffd8539-644d-3192-b214-db26b88ad6c9 | -7.9076 | -45.53622 | 2025-08-05 04:38:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f9410336-72ac-37c3-b07c-d8d839db0aa1 | -7.39197 | -44.63786 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d69ca38-4f41-3ffb-a694-ac54039f5a1a | -4.12545 | -38.18931 | 2025-08-05 04:38:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6cd05cbd-3547-3750-add1-9dad3d74e96c | -8.73266 | -46.43661 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4f57908-af1a-3f43-ac7e-3fc135aaffa8 | -8.91347 | -48.93439 | 2025-08-05 04:38:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe663354-9841-3c23-ab55-a4d50190fd13 | -7.13725 | -44.08195 | 2025-08-05 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f090c0c-e16c-38ec-bddd-fb9c702f44db | -2.98157 | -54.50575 | 2025-08-05 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf1d086d-72d7-3284-8380-129504822592 | -7.98681 | -43.16919 | 2025-08-05 04:38:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| dcf29f38-00b7-31b4-90c7-d9a277374fc4 | -5.77843 | -51.66405 | 2025-08-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69d7df63-0764-3018-a0bc-3e9eb56b95d0 | -7.11093 | -44.02678 | 2025-08-05 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b361d1d-fb33-3a00-ba8f-f49340df92ec | -7.94683 | -47.59565 | 2025-08-05 04:38:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62067a09-e2ba-3a0a-b369-d8b0f8a52dd0 | -6.73979 | -45.30586 | 2025-08-05 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 850409a7-0990-3dfd-95bd-e40e0ad47b85 | -8.26104 | -45.06488 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5dcbb27f-3e54-333e-ae78-721d58e51d19 | -5.9853 | -49.91296 | 2025-08-05 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e908db2-e11a-3bf1-9f49-51f847a19c03 | -7.56458 | -44.87703 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7cc3bc4-bec9-3f95-8816-c54aa7085ae5 | -9.31787 | -44.84971 | 2025-08-05 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c89b4c0b-e80a-3d0b-ae8d-d2afe36ccc56 | -9.32911 | -44.85122 | 2025-08-05 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b057b25-5c59-3772-be87-a2df0321253c | -7.9932 | -43.15656 | 2025-08-05 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 2204d4c7-164a-3566-8dee-179f13c8cff2 | -6.73522 | -45.31009 | 2025-08-05 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce01a918-9e45-3c22-b4f1-d841885a07d9 | -7.05792 | -44.39367 | 2025-08-05 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef41501c-6cfd-3270-8d44-55e012521496 | -6.90996 | -43.894 | 2025-08-05 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88c5803f-d3df-32c6-96e8-b41b9503ea14 | -6.65467 | -59.09917 | 2025-08-05 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8da0f57-2b0e-3828-9d61-15721b1ebb21 | -6.67706 | -49.79255 | 2025-08-05 04:38:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ae677312-1343-3f8c-898e-5ebc4c9b07d0 | -8.13269 | -49.58651 | 2025-08-05 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3d1f876-5309-3495-90d4-f07586c50309 | -8.85004 | -47.60704 | 2025-08-05 04:38:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef94b64a-52e3-3b4c-ad10-82294328a1ce | -7.98869 | -43.15581 | 2025-08-05 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 4074f509-76ff-3998-b64c-7526529dd675 | -2.90568 | -40.13173 | 2025-08-05 04:38:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a6350a02-4a02-3919-a990-6fdea27df8f2 | -7.08344 | -44.69882 | 2025-08-05 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24102808-59a5-3993-8083-e84c81214060 | -6.15658 | -57.91905 | 2025-08-05 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eabf9563-3ae6-3add-ad19-06c1b780f11d | -8.24906 | -45.06306 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4091a44f-04d5-39fb-93c2-9f0a7483c51c | -8.94106 | -46.74257 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 0804bf42-e329-32bd-b46f-da8f56965390 | -8.95265 | -46.73986 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c4fbd017-c69a-3b93-8d98-a44d97f548fd | -8.95995 | -46.74091 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75285f51-0d0e-37b0-aa27-19d84d1ffbe2 | -6.23014 | -45.86391 | 2025-08-05 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5115528a-59ec-3670-8c94-a69f3c2662b7 | -8.01649 | -43.18771 | 2025-08-05 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7f52fcdc-5e8c-3880-9b27-ba5407907e1a | -6.89766 | -52.86768 | 2025-08-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 07c356c6-1dc8-37f2-9468-1eb4f6435f30 | -7.75542 | -45.23901 | 2025-08-05 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ad927856-0387-38b2-8f2b-3e47b06a00f4 | -8.84655 | -47.60649 | 2025-08-05 04:38:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83c27523-c913-3a97-8760-5b523f65f073 | -8.15429 | -49.14262 | 2025-08-05 04:38:00 | NOAA-20 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e809328-4dbc-3c83-9d37-163294c80db0 | -8.24955 | -45.0596 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72afe700-b47d-3500-9ab2-78f563a76c56 | -5.86033 | -49.56407 | 2025-08-05 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b786cdb-1a89-3baa-9396-360e7b54a726 | -5.80039 | -43.62881 | 2025-08-05 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e50a2103-8ec0-3755-97f8-98f7523eae24 | -6.46286 | -43.03003 | 2025-08-05 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce8b93ac-f026-3633-971e-a09c4dc606a5 | -7.94526 | -43.89981 | 2025-08-05 04:38:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89bf3a71-b534-3d0d-84cd-746d43a42dae | -7.8101 | -55.22387 | 2025-08-05 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 306562a5-cfbe-3da8-9e90-241b9bd737ae | -7.98293 | -43.16396 | 2025-08-05 04:38:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 4ad015fc-f890-322b-93a9-c717894b6bb2 | -8.25255 | -45.06714 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b8259bc-9e32-3b58-881e-40db407d48c9 | -6.63831 | -60.00025 | 2025-08-05 04:38:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bd62780a-89a9-33f4-8b0e-83fda2cfaed2 | -8.38378 | -46.54653 | 2025-08-05 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a55a3779-8923-3241-8186-950bd9766b7c | -5.6551 | -42.58119 | 2025-08-05 04:38:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a0103fcf-3d9c-32f7-9865-33d4665d41f1 | -7.5695 | -44.89907 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e73a748-54f1-392d-bd2c-55e5c8422dae | -6.57606 | -43.49292 | 2025-08-05 04:38:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce12e207-307d-3f64-b4f5-aeb3bdf33769 | -8.71352 | -46.43811 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d3ca849-9b2f-3e5d-b92a-3ef537a90c63 | -6.67597 | -49.79946 | 2025-08-05 04:38:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f55351e1-32dd-34c2-8e48-8fa34d17454e | -6.19428 | -43.7688 | 2025-08-05 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a24491a3-ab36-33d5-b39d-896e9413f3da | -7.21949 | -44.48403 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af517a33-b601-3f92-b7a9-c1d7c28e9522 | -8.87774 | -44.791 | 2025-08-05 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70f00930-2685-31ae-a9b4-32ebae1ca6b2 | -6.42463 | -44.81636 | 2025-08-05 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0c8f5b41-57bc-371b-b2d7-2551f44b5bd2 | -6.67652 | -49.79601 | 2025-08-05 04:38:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa8ac4e6-b5b6-3894-8c31-71e5df7b77ef | -3.489 | -59.37001 | 2025-08-05 04:38:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06574fac-fb4e-3e0d-938b-c1e1e298729c | -8.0412 | -49.88853 | 2025-08-05 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| da7717ab-9d39-38ec-af03-cdb2cdd84eb4 | -6.15151 | -57.91826 | 2025-08-05 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d3dfe0bf-0c19-358e-b2ab-950f923f3d28 | -7.39032 | -44.64895 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 144fa676-1a25-3cbf-866f-6d18daab9e98 | -6.20138 | -43.74986 | 2025-08-05 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 45216dd2-15d8-30da-adbc-41fc86520558 | -7.53464 | -45.05233 | 2025-08-05 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9f8da754-f99e-3a7a-ac96-9c1e9be8bcba | -7.14201 | -44.07871 | 2025-08-05 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a21162b9-218f-3d26-bc4c-c4c511474485 | -6.008 | -52.15356 | 2025-08-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0f13d64-dbc1-3fc3-80d2-4c21d809de79 | -8.94899 | -46.73932 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5f05eb92-0e51-3767-81ce-6192ef07e4e8 | -8.01779 | -43.17857 | 2025-08-05 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6b64eb3e-68c2-3e4c-a091-d40a80ed6e7e | -6.43515 | -44.81963 | 2025-08-05 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| edbe5017-b0ca-3169-836b-c595b3465d4c | -7.085 | -44.69518 | 2025-08-05 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da94146e-916d-3a72-af21-4967f3a46307 | -7.39252 | -44.63414 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62fac908-d39a-34b7-8d07-33a11135ebf8 | -7.60015 | -55.19881 | 2025-08-05 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5aa01a05-2f53-3d81-bd35-fff20abb4492 | -6.90123 | -52.86189 | 2025-08-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12929073-9163-3e78-a6c9-89deace65a52 | -8.3928 | -46.56134 | 2025-08-05 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f618598b-70cc-3047-9c29-0e0749e708fa | -8.00685 | -43.22313 | 2025-08-05 04:38:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 16f5d4f6-c7cf-3134-87b6-4ba5b13549dc | -5.10503 | -42.92199 | 2025-08-05 04:38:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4403a8c-7f91-3567-b8fb-59493bf4a0b3 | -6.28664 | -45.75222 | 2025-08-05 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a213917-2583-36d5-96f5-96345e6a1eb4 | -8.39345 | -46.55703 | 2025-08-05 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2b1f813-5991-393c-809f-d7a7f055d984 | -7.09216 | -44.36039 | 2025-08-05 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3171326f-b35c-3758-859d-6c2032e37ae4 | -7.36566 | -43.75447 | 2025-08-05 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb9c66d0-cf61-3639-bef7-13c09a523b56 | -7.53933 | -45.04798 | 2025-08-05 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a2e9549f-eab1-3c0c-8e4e-55bfb5d10c12 | -7.1905 | -44.16335 | 2025-08-05 04:38:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 832b0bd4-9b8e-30ef-a98a-6360f60520b1 | -8.22108 | -45.05894 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 175a6f72-1ca9-348b-8fdb-f2f8cff66a2a | -8.25754 | -45.06081 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README22.md)
