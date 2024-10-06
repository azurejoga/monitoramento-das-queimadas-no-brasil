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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41bbfda1-7944-3b09-81fd-cbdc7ea62f8a | -22.60299 | -53.04468 | 2024-10-06 03:57:00 | NPP-375D | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| b1bac6db-029e-3f1e-9065-dff53bc57500 | -17.82436 | -53.78019 | 2024-10-06 03:57:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f8f1a351-63e6-3d6e-a0e3-03c7c00fb0fb | -17.81996 | -53.76963 | 2024-10-06 03:57:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8ba924f8-592d-30bf-92e4-20975eae0e64 | -17.81893 | -53.77416 | 2024-10-06 03:57:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4aff4cc2-fb4f-3c61-9d73-d704505276e8 | -17.81781 | -53.77907 | 2024-10-06 03:57:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9d0d99dc-6cf7-345f-9693-89ea40b4e85f | -17.81602 | -53.78699 | 2024-10-06 03:57:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 9bd3023c-f33d-3d1d-b723-758c3dbdc469 | -17.81249 | -53.77258 | 2024-10-06 03:57:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7eecfad8-0417-3fda-baf3-91281cff2131 | -17.8113 | -53.77781 | 2024-10-06 03:57:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 746725c2-cabc-31ea-a5de-922decff7c2b | -17.80955 | -53.78553 | 2024-10-06 03:57:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b8c65be5-411d-3154-8511-3d77f8ae7dd2 | -17.80801 | -53.7923 | 2024-10-06 03:57:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 64d1682d-c07e-3319-9f62-fb6591c27624 | -17.01686 | -55.0647 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 9b7111b4-f154-3673-bd24-bb82ff8d1064 | -17.01517 | -55.07177 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 0b7f1243-3d86-3047-96e3-42a3acb13f99 | -17.01491 | -55.04171 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4480388f-f3b6-36d3-bc3b-8c79202c986c | -17.01372 | -55.05977 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| e261dc03-cfd9-3547-94c0-7e659967ad41 | -17.01324 | -55.04875 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| a5316f3e-234a-3f1c-88bf-604f751a8b86 | -17.01208 | -55.06686 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| f79238e7-3a61-38d3-aab2-532045a1fb81 | -17.01155 | -55.05582 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 17fbf634-a7db-3014-b5c1-827b2fc9896a | -17.01044 | -55.07393 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 5df5e733-90b0-3406-972c-570a359a9a35 | -17.01002 | -55.04378 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| cb2e7638-05d3-34a3-899f-c81c19a804e1 | -17.00987 | -55.06289 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 9c67519f-8e22-3a33-9199-03326fd76abb | -17.00881 | -55.081 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| fe6cdb3b-8966-32ac-afe7-573807e56c85 | -17.00838 | -55.05085 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 8e19b700-3ff5-38b1-9a90-149aa7e642e6 | -17.00818 | -55.06996 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 7c25f54b-03ac-3324-ac08-bde2d1bb7253 | -17.00793 | -55.03991 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cf550998-b7ae-35af-9844-a5caa33acec5 | -17.00673 | -55.05793 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| d0f0066d-0daf-3b89-ba43-b413da49aaa2 | -17.00651 | -55.07702 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| cb8cb3a9-7d4d-37c9-897b-1c0ad5a4b35c | -17.00625 | -55.04697 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d8a9114d-098c-3d18-af3f-d20f46134797 | -17.0051 | -55.06501 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 4f3a2e7f-db23-33ac-af10-87cd7f5a2fb2 | -17.00482 | -55.0841 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 40039b42-de13-3166-8f0c-b9c1b3129028 | -17.00457 | -55.05402 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c365d011-01ba-3e2a-a23f-477157af377e | -17.00346 | -55.07209 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 793ba327-c318-396c-93e8-f8dcdf9f53d3 | -17.00304 | -55.04194 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39986466-ac72-3df9-8517-2af30fdc2f1b | -17.00289 | -55.06107 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 34.5 |
| a6d69101-0619-37cf-89b4-08077bfe2d55 | -17.00182 | -55.07917 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| a4e7c366-cd0a-309c-b329-680759c9fc2b | -17.0012 | -55.06815 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 7e006f6b-fa6f-323e-aba3-77dbaa45a13e | -16.99951 | -55.07521 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 7c59e6a9-044f-3dd2-b666-1ac7ae126ca8 | -16.99812 | -55.06314 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 25cd8d20-5856-3581-b483-607dea8c244d | -16.99783 | -55.08229 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 24.3 |
| a7654b9a-0179-35e0-8147-463f2810cfd4 | -21.02788 | -54.708 | 2024-10-06 03:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1edbee07-8518-38d2-a623-b1f68f3a00c9 | -21.02651 | -54.71369 | 2024-10-06 03:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb045631-6754-32cf-9a5a-fb3ae354f77c | -21.40368 | -57.25547 | 2024-10-06 03:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5ab4848b-46cb-39e9-b320-c018815cc387 | -25.01712 | -54.08424 | 2024-10-06 04:00:00 | NPP-375D | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 07a1a947-2c33-3d6a-a1c7-0b2e11e37fe3 | -20.56 | -49.4 | 2024-10-06 04:03:27 | MSG-03 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 95597864-6b14-3088-a1bd-2719a3278069 | -20.59 | -49.42 | 2024-10-06 04:03:27 | MSG-03 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d07b7acb-7b4e-3dbc-b0f3-4a9cbe1452fe | -12.75 | -50.56 | 2024-10-06 04:04:12 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dabc2d31-4f3f-3878-bca5-0ea06c5cf9f3 | -12.75 | -50.5 | 2024-10-06 04:04:12 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4f551aef-e81b-32e5-bee0-ce44ad880e0e | -12.78 | -50.57 | 2024-10-06 04:04:12 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b6924567-656c-3b5b-ad51-bf1c0d9a6548 | -12.78 | -50.51 | 2024-10-06 04:04:12 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9d999f6-225e-32ff-aea3-654970aaa038 | -10.48 | -50.71 | 2024-10-06 04:04:25 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b8c58bb3-366b-3004-a3d3-318e7b11133d | -10.42 | -50.75 | 2024-10-06 04:04:25 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4cd89b14-7de4-3031-8504-c644b1ae502b | -10.42 | -50.69 | 2024-10-06 04:04:25 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 847f2178-db14-3b42-b9ca-f91fc9a09ca0 | -10.45 | -50.76 | 2024-10-06 04:04:25 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b1f45e71-e5ab-3a1e-8197-466d9d8d08a0 | -10.45 | -50.7 | 2024-10-06 04:04:25 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c2154f5c-ec68-35e8-a927-32ddcaea0974 | -10.45 | -50.64 | 2024-10-06 04:04:25 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e7ddac61-87ab-3508-842d-1d40bb091482 | -2.8166 | -48.6867 | 2024-10-06 04:05:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 893bbd62-bad9-35f7-b2df-8d04df607610 | -2.8165 | -48.7082 | 2024-10-06 04:05:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 3520359f-1f24-3d3e-a3b8-0033afd6d623 | -3.2329 | -50.8504 | 2024-10-06 04:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 0959d9cd-8351-33e0-9a78-cca4a19e0bfc | -3.1315 | -48.591 | 2024-10-06 04:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 3cdcedc7-ae7c-3aee-8659-6d1796dc9612 | -3.1314 | -48.6125 | 2024-10-06 04:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 202662d1-5de4-34b3-9088-611ddaf67876 | -3.1129 | -48.6131 | 2024-10-06 04:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| e8876dd4-f8b5-3c11-8861-a9d35fd579dc | -3.4195 | -50.3844 | 2024-10-06 04:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 0fdeeeff-c743-3e7d-8c53-c427249abb8b | -3.8464 | -46.4714 | 2024-10-06 04:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 15d661f0-411f-399e-8f92-8240ebece064 | -9.3464 | -46.5589 | 2024-10-06 04:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 4df92877-47df-332b-b8b3-b355b7e61b76 | -9.3278 | -46.5385 | 2024-10-06 04:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 70402ec3-1320-38e0-a375-73056ddeeccd | -9.3467 | -46.5365 | 2024-10-06 04:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 5a4c9384-370a-313c-84f9-b8809d2be1a6 | -9.688 | -47.8308 | 2024-10-06 04:06:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 2e39579d-b784-3b76-b0c3-18e1d91e6924 | -9.6778 | -64.6457 | 2024-10-06 04:06:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 7e45edcf-190d-3c65-8aa9-5eb829210314 | -9.6779 | -64.6269 | 2024-10-06 04:06:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 380c0ac7-dee8-3ff5-bdd0-4a6b01f55eec | -9.6964 | -64.645 | 2024-10-06 04:06:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.9 |
| c5c9249b-bc33-369e-ad83-ec9ee738edba | -9.6965 | -64.6262 | 2024-10-06 04:06:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 02be813b-9c65-3299-b193-d73ee3208689 | -10.2148 | -48.0149 | 2024-10-06 04:06:04 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 96faafc1-d610-3bde-a16a-44961e83dd0c | -10.5191 | -67.7399 | 2024-10-06 04:06:06 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 0def6270-79cb-39f4-866b-02663020ed48 | -10.5378 | -67.7393 | 2024-10-06 04:06:07 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 27.5 |
| b56d88bd-0983-3d76-81c7-6b73d64b68ea | -12.6092 | -53.1129 | 2024-10-06 04:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| de07fa2f-bb87-3e73-b2ea-13a8d9343394 | -12.6089 | -53.1338 | 2024-10-06 04:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| a401828f-cd63-3671-b630-b12277c1d32f | -12.7825 | -50.5112 | 2024-10-06 04:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 46f1e94b-2fa3-3b21-b61c-abfa634aad48 | -12.7822 | -50.5328 | 2024-10-06 04:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 162.0 |
| 1e608aa7-9520-3852-bd0d-cb5f0c904413 | -12.7634 | -50.5136 | 2024-10-06 04:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 161.9 |
| c1ea47b9-5a53-3c16-9a9c-39fd8737b212 | -12.763 | -50.5352 | 2024-10-06 04:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 281.0 |
| 1a6bebbf-349d-3f33-862a-63000e0bf4c4 | -12.6283 | -53.1108 | 2024-10-06 04:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 77907c34-2847-331e-bc2a-f4115881a27b | -12.628 | -53.1317 | 2024-10-06 04:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 3540fcee-a865-3b2b-bb5e-6ca9975834b7 | -13.3976 | -61.957 | 2024-10-06 04:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 2020222e-d36d-3932-88c2-3b512375fabe | -13.3786 | -61.9582 | 2024-10-06 04:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 347e61bc-8448-3f35-ae10-0a441bcc29b7 | -16.3764 | -57.3663 | 2024-10-06 04:06:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.9 |
| 03049ea5-795f-3949-9d8a-d7972d1ff8a0 | -16.5739 | -57.201 | 2024-10-06 04:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.9 |
| 91718ed0-5686-3154-af16-30e0b0302793 | -16.5736 | -57.2215 | 2024-10-06 04:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.8 |
| b8d4a08d-e72f-315d-9f1e-85e83bc8e1a9 | -16.5544 | -57.2032 | 2024-10-06 04:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 165.4 |
| 5870c692-1153-36cf-8fc5-0491cb09e0b3 | -16.554 | -57.2237 | 2024-10-06 04:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 143.0 |
| a05c0c01-8a08-34d9-90e1-0e1b07956077 | -16.8238 | -57.4584 | 2024-10-06 04:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.2 |
| 26725324-7325-36e4-a501-c922c6e8116c | -17.1185 | -57.3834 | 2024-10-06 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.0 |
| e9d899e7-4752-31fa-b632-5d5e083b0723 | -17.1182 | -57.4039 | 2024-10-06 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.6 |
| 89b7204b-8258-3bda-bfe9-bfa0c5258203 | -17.0885 | -56.8122 | 2024-10-06 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.7 |
| d00c1dfa-8eea-3fec-a652-7580bd8fa971 | -17.01 | -56.8217 | 2024-10-06 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.3 |
| 68b63ce9-4944-3a12-bd9e-593f3b78e807 | -17.0207 | -55.0371 | 2024-10-06 04:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| bb39bb37-60e3-319f-9a8e-344b77807c7e | -17.0203 | -55.0581 | 2024-10-06 04:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 220.9 |
| e1cde74e-bb01-37aa-8f35-c5288235276b | -17.02 | -55.0791 | 2024-10-06 04:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 104.0 |
| e301b5c5-5cc8-35fd-bb18-79e840effa01 | -16.9907 | -56.8034 | 2024-10-06 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.5 |
| d98a8b56-f665-3ecc-9db3-0fda7953f91e | -17.001 | -55.0398 | 2024-10-06 04:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 126.2 |
| cac026fc-3727-346f-96f1-8677e79f2515 | -17.0007 | -55.0607 | 2024-10-06 04:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 296.4 |
| 85127487-6661-3d31-993d-c0568c5b3029 | -17.0003 | -55.0817 | 2024-10-06 04:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 163.9 |


[Clique aqui para ver as próximas entradas](README62.md)
