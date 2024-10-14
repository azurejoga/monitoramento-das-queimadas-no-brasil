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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5941251-f9a3-3f54-8e3c-c52ab79eebbf | -22.2787 | -49.113499 | 2024-10-14 00:34:02 | METOP-C | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c6697a59-525f-3ab4-9895-4b33c5ea77f1 | -21.865999 | -48.949501 | 2024-10-14 00:34:08 | METOP-C | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eab7a6c5-a135-3cbb-aaef-200d4b6a3003 | -21.8685 | -48.9632 | 2024-10-14 00:34:08 | METOP-C | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 143ce624-231b-337d-acf8-1ef009d0527c | -21.870899 | -48.976898 | 2024-10-14 00:34:08 | METOP-C | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e5358456-3351-3dab-accd-fb765ac8aaf5 | -21.8587 | -48.965199 | 2024-10-14 00:34:08 | METOP-C | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eae05a40-e115-39ac-9430-db90b5855613 | -21.8612 | -48.978901 | 2024-10-14 00:34:08 | METOP-C | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2b03670c-8a13-37ff-81f9-57d425f64cbe | -21.553101 | -48.010101 | 2024-10-14 00:34:10 | METOP-C | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ec84a829-20d1-347b-ac3c-71b405c47f28 | -21.543301 | -48.0121 | 2024-10-14 00:34:11 | METOP-C | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 05d6215a-64fe-3a69-b5e1-a173e741b45d | -21.5455 | -48.023899 | 2024-10-14 00:34:11 | METOP-C | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0675dee2-081b-31df-b6cd-8febfcdcfbfc | -21.121599 | -45.927601 | 2024-10-14 00:34:11 | METOP-C | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9da20f77-2e9b-3539-b1db-cc8515fc4da0 | -20.5954 | -45.950901 | 2024-10-14 00:34:20 | METOP-C | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 53ce339a-a4b6-33d6-8610-a919ddfcd665 | -20.5972 | -45.959702 | 2024-10-14 00:34:20 | METOP-C | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1383860e-8000-3d85-8311-f035e99fedd1 | -20.5989 | -45.968601 | 2024-10-14 00:34:20 | METOP-C | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| eadb0575-436c-3811-838e-f7ae49c4bc48 | -21.0459 | -48.609402 | 2024-10-14 00:34:21 | METOP-C | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 926c7e57-e7eb-3a7b-9f2f-b31254c65f4c | -20.3216 | -47.1441 | 2024-10-14 00:34:28 | METOP-C | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d2447865-08b5-3126-bbd7-2c974ed3c4cf | -19.062599 | -48.3092 | 2024-10-14 00:34:52 | METOP-C | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7fe9cc59-7cf6-37cf-8816-57c0c5c79c1f | -19.064699 | -48.320499 | 2024-10-14 00:34:52 | METOP-C | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2d0d9cda-d9db-3996-b85d-cb8a7c95948c | -16.630199 | -42.787601 | 2024-10-14 00:35:13 | METOP-C | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c45ab263-34a2-37ee-806a-180e3ed9faf8 | -16.620399 | -42.790001 | 2024-10-14 00:35:13 | METOP-C | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 609f8cb3-59aa-3ff0-a193-fd37e5101419 | -16.622 | -42.797199 | 2024-10-14 00:35:13 | METOP-C | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3da22ecc-7bab-3468-a3b7-78387626264a | -16.6318 | -43.480099 | 2024-10-14 00:35:15 | METOP-C | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a5f1b75d-1f74-3e1e-a423-e378bb5a7b04 | -16.3806 | -43.096901 | 2024-10-14 00:35:18 | METOP-C | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b5548662-1b0f-3c69-973a-f7945791c366 | -16.3822 | -43.104 | 2024-10-14 00:35:18 | METOP-C | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 24d463eb-e2cc-3c18-be46-79c179963188 | -16.127899 | -42.351101 | 2024-10-14 00:35:19 | METOP-C | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7f649d64-cac1-319d-9f55-d87b9d0a5dab | -2.4344 | -46.9195 | 2024-10-14 00:35:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| d5defe2c-b2f0-3561-86e5-4c6113a6a24a | -2.4529 | -46.919 | 2024-10-14 00:35:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 8cb270b1-cd22-39aa-9168-f979042ce562 | -2.6117 | -49.1198 | 2024-10-14 00:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 3b230183-0a0a-34b2-90af-9df336298f82 | -2.6118 | -49.0985 | 2024-10-14 00:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 1e5504f0-266e-394c-b352-926eb8762bc3 | -3.1791 | -50.476 | 2024-10-14 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 35df3c3c-ed98-3b07-b303-fb5d89c03de4 | -3.1792 | -50.4551 | 2024-10-14 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| a38e3406-31a2-3f36-98eb-45ef222aaa8d | -3.2889 | -42.8561 | 2024-10-14 00:35:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| f6150271-571c-3eee-9bdf-e4ecead6f50f | -3.289 | -42.8327 | 2024-10-14 00:35:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 01320be1-6bfc-31ce-833c-7118753951dd | -3.3076 | -42.8553 | 2024-10-14 00:35:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 179.5 |
| aa4ef5cc-120d-329a-b561-c39c7d5219ad | -3.3077 | -42.8318 | 2024-10-14 00:35:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 275.6 |
| 6dfff9b9-0060-354b-91a2-af70be111655 | -3.3264 | -42.831 | 2024-10-14 00:35:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| e3a439da-461f-344c-87a4-5ab09b30802e | -3.1982 | -50.3077 | 2024-10-14 00:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 50da664f-e6ca-38f4-bbfb-d5962cf4b393 | -3.3643 | -50.3233 | 2024-10-14 00:35:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 0137dac5-b6a7-3a93-9a1e-6ef9e2e29675 | -16.037901 | -43.957298 | 2024-10-14 00:35:27 | METOP-C | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 40f8dd5e-4427-30ea-bfd1-a335c595216b | -3.8723 | -52.2769 | 2024-10-14 00:35:28 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 59b66b17-602d-3306-9090-7a4674b3a697 | -3.9103 | -48.3466 | 2024-10-14 00:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 1cde728c-b8bb-3bd1-a885-052dfab8c9ae | -4.1145 | -48.2947 | 2024-10-14 00:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 65548115-6bfc-3abb-9b2b-5a44977b4acf | -4.1146 | -48.2731 | 2024-10-14 00:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 390b236d-627a-35c9-83d1-eb4af02ab8c5 | -4.3428 | -50.5172 | 2024-10-14 00:35:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| ea37595d-35ba-3c9b-86a4-6d4165195df6 | -4.6197 | -44.8626 | 2024-10-14 00:35:32 | GOES-16 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 6a0b594f-7117-3cc1-a215-8cbacc1e4a6c | -4.6384 | -44.8615 | 2024-10-14 00:35:33 | GOES-16 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| aa6cb520-5558-3eae-99b2-67cef83322fc | -4.7224 | -46.1608 | 2024-10-14 00:35:33 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 83.7 |
| a2821355-9137-3620-926e-60089adf76be | -4.7226 | -46.1385 | 2024-10-14 00:35:33 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 69.2 |
| da296c9b-05dc-33e4-9cd9-ba13f4343e18 | -4.9097 | -46.0163 | 2024-10-14 00:35:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 57.5 |
| b34be9c4-11eb-3b94-8691-73bdfe3d19cc | -4.9099 | -45.994 | 2024-10-14 00:35:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 85cefec1-24bc-3ba8-a807-943e02dd6fbb | -5.0625 | -48.0745 | 2024-10-14 00:35:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 3af46d21-c6cb-31f2-bd05-7951ac2be73f | -5.0627 | -48.0528 | 2024-10-14 00:35:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 26.3 |
| c18894c0-f141-3cb6-b684-226421409910 | -6.1342 | -42.7906 | 2024-10-14 00:35:41 | GOES-16 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 1b022c7f-ee8d-320f-8434-77d9a1f6915d | -6.3749 | -59.9936 | 2024-10-14 00:35:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 97853d6b-2579-337a-a2c4-b8b3ae2b9abd | -6.3933 | -59.9929 | 2024-10-14 00:35:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 3fa934d2-0044-35b3-93c1-2a500f2f0bc5 | -7.9623 | -49.0823 | 2024-10-14 00:35:52 | GOES-16 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 97272594-c139-3abf-860e-a343f2407f83 | -7.9625 | -49.0607 | 2024-10-14 00:35:52 | GOES-16 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 191.2 |
| c6d16364-6118-3e01-a751-35a1df7cda34 | -7.9418 | -63.6365 | 2024-10-14 00:35:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 32ff441a-769b-3c75-b406-f3c0451ecb30 | -7.9419 | -63.6177 | 2024-10-14 00:35:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| ffdb1d14-e100-3887-b61e-e4f993c2f3fa | -7.9603 | -63.6359 | 2024-10-14 00:35:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| a87c3281-9f44-3199-a2a8-94737a288c47 | -7.9604 | -63.6171 | 2024-10-14 00:35:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 19f05b99-0c2f-3be6-8a02-0e26fea3e760 | -8.3207 | -42.7394 | 2024-10-14 00:35:53 | GOES-16 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 59.7 |
| 5861e24c-1d6c-3836-82a7-179c2093cd80 | -8.4921 | -48.6259 | 2024-10-14 00:35:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 92.7 |
| bb7abf9f-ea99-36bf-a572-96fe9e6f35b7 | -9.0832 | -47.9374 | 2024-10-14 00:35:58 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 3be00526-6724-37d5-a919-ac8f7898c901 | -9.1021 | -47.9355 | 2024-10-14 00:35:58 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 770e0d2d-2bab-332e-9bf5-67317b7e12ef | -14.2086 | -44.435501 | 2024-10-14 00:35:58 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d8999c26-c8d7-3f73-b838-02f82cc53786 | -9.2701 | -45.2342 | 2024-10-14 00:35:59 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| fed40f6d-fd82-317c-bc55-3a72f44a450f | -9.1042 | -61.1811 | 2024-10-14 00:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| beec20b2-db55-3d44-8467-a2a0c52caac6 | -9.1043 | -61.162 | 2024-10-14 00:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 93be455e-7243-3164-bd4c-1b823218f275 | -9.1229 | -61.1611 | 2024-10-14 00:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 469bfe77-a90d-3f95-b531-ac5124161800 | -9.6928 | -47.4774 | 2024-10-14 00:36:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 15c3d626-1d1e-355e-bc6d-d4f86e45f6fe | -9.7825 | -46.4651 | 2024-10-14 00:36:02 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 1c918411-8ad8-3117-b2a1-40b77dfeaa44 | -10.0622 | -44.2391 | 2024-10-14 00:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 158.8 |
| c67ee030-2665-3ceb-b313-6b26e14c15e3 | -10.0626 | -44.2158 | 2024-10-14 00:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 6feb31ce-05de-395f-a3d6-204068dbe448 | -10.0809 | -44.2599 | 2024-10-14 00:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 5c3df097-0bc6-3fbc-ba37-3700eed62706 | -10.0813 | -44.2366 | 2024-10-14 00:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 278.1 |
| b74abaae-aba4-3fc8-a6fa-1eb75a08d1b6 | -10.0816 | -44.2133 | 2024-10-14 00:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 194.1 |
| 351f6591-b04e-38d3-88b9-0ecf90a33af5 | -10.1003 | -44.2341 | 2024-10-14 00:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 1449d595-95d8-37e4-b103-447ff3a47746 | -9.9973 | -47.3329 | 2024-10-14 00:36:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| a6710560-ca5d-3213-8b88-ae57c53f3646 | -9.9976 | -47.3107 | 2024-10-14 00:36:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 35ddb660-718b-3c51-abc9-ec6fda6f8b23 | -10.016 | -47.353 | 2024-10-14 00:36:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 56383e16-a653-34b8-a5c0-49b9a02a6f30 | -10.0163 | -47.3308 | 2024-10-14 00:36:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 193.3 |
| d3b99191-e825-3306-83a6-edda6ea94afe | -10.0166 | -47.3085 | 2024-10-14 00:36:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 34221851-ec5a-3461-bedd-42b606d77b0e | -10.0352 | -47.3286 | 2024-10-14 00:36:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 5b9a1464-4f17-3379-b0fa-0c78876b5117 | -10.4918 | -42.433 | 2024-10-14 00:36:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 113.0 |
| 347c6538-b276-3dd8-be85-e0ed5be54c07 | -10.3303 | -46.58 | 2024-10-14 00:36:05 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| d1fbab19-3c71-3bc0-a620-f62b0bd0d8f0 | -10.5307 | -49.7843 | 2024-10-14 00:36:06 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 90b93c60-90fc-3f15-9af7-f0b9cd849018 | -13.7039 | -44.3895 | 2024-10-14 00:36:06 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8ab5d15d-314f-311d-a8c6-a814a592b055 | -13.6562 | -44.223202 | 2024-10-14 00:36:06 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 70f5fa28-5cd1-378b-b00d-17447bdea340 | -11.1705 | -39.894 | 2024-10-14 00:36:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 60.1 |
| 3bc0d264-f1f5-3936-ad1d-d69e0a90db80 | -11.1898 | -39.8906 | 2024-10-14 00:36:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 68.5 |
| 8ab62dce-7e7b-3513-880b-f33a8c3457bf | -12.1102 | -50.7857 | 2024-10-14 00:36:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| ed2b53bd-63bc-347a-9df3-5e2e2320105f | -12.1106 | -50.7643 | 2024-10-14 00:36:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| fee1b825-14c6-3ca2-a5b1-1f3d863ba2b1 | -13.0342 | -43.799099 | 2024-10-14 00:36:15 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 30dd7ae8-c1f7-3c88-ad1d-665b7a516112 | -12.4981 | -63.0148 | 2024-10-14 00:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 79.8 |
| eff07762-d926-30a7-bf48-762cc5a605f2 | -12.4983 | -62.9956 | 2024-10-14 00:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| d4a2affa-cfe3-3cd1-b8d6-6f0959f95c2a | -12.517 | -63.0137 | 2024-10-14 00:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| a048fbc9-2449-36fe-a8e4-17f2d05114e8 | -12.7687 | -62.3064 | 2024-10-14 00:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 8d2d4126-bce6-3fbe-87e5-f8d4a013f420 | -12.7688 | -62.2872 | 2024-10-14 00:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 52cc0c5a-8922-378b-8673-3217254524ef | -13.1273 | -51.6861 | 2024-10-14 00:36:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 6b4a4573-6c82-3ca4-8565-af543372bd3b | -13.1465 | -51.6838 | 2024-10-14 00:36:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |


[Clique aqui para ver as próximas entradas](README5.md)
