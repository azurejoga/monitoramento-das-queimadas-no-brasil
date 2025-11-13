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
| c9ec123c-db29-3e87-be73-606a46889291 | -4.2111 | -48.5616 | 2025-11-13 00:58:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6995f71c-1eba-324c-881d-a6f85bd61920 | -2.4587 | -49.258099 | 2025-11-13 00:58:00 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80604b88-3f12-3fe8-a71a-688cb2335a24 | -4.2205 | -50.092899 | 2025-11-13 00:58:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a399784-f439-37d7-a982-480cc67e4388 | -10.3801 | -45.0453 | 2025-11-13 00:58:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 979926c9-6289-3a92-b410-b809ae253f88 | -3.2277 | -45.598202 | 2025-11-13 00:58:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cf004288-dc33-3e22-96c2-871a36b96091 | -9.6459 | -44.548401 | 2025-11-13 00:58:00 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| eedacba3-e5fa-321c-b964-1b672e68ecf7 | -15.6492 | -45.589001 | 2025-11-13 00:58:00 | METOP-C | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9080d55d-d8d0-3c69-9c5e-ed694e40bcb3 | -3.1476 | -50.2677 | 2025-11-13 00:58:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3d8981c-adcf-3575-b56f-61519cbc421b | -3.4041 | -50.173801 | 2025-11-13 00:58:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea5644e4-2d65-3f78-995f-78be6a3e09a9 | -3.31 | -49.462299 | 2025-11-13 00:58:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aed265f7-5321-3fb2-ae27-ca2d1b47c7ac | -2.9013 | -48.072701 | 2025-11-13 00:58:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f0951db-4a21-3189-931e-bb80e526a085 | -4.0192 | -48.796101 | 2025-11-13 00:58:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4aa646d4-19f4-3dd2-9d7a-b0eb464fa83b | -4.1941 | -50.332901 | 2025-11-13 00:58:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9db2594-be61-3da3-a80c-061a36e5951f | -16.4547 | -44.998001 | 2025-11-13 00:58:00 | METOP-C | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 40ba30c6-2c2f-39b2-924c-0bca52c1490c | -20.4503 | -53.0518 | 2025-11-13 00:58:00 | METOP-C | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 80813b3b-b2c5-3a3a-9767-612ce44443ed | -12.6533 | -46.747601 | 2025-11-13 00:58:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c21be95-e62f-3c65-9ceb-1c22be2e9fc7 | -6.1423 | -48.055599 | 2025-11-13 00:58:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a04ed17-9efe-32fd-a197-dd0a149b82ee | -7.668 | -45.883099 | 2025-11-13 00:58:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d60d68a2-ce5d-320d-8888-e201f2ab6fd1 | -10.626 | -45.243401 | 2025-11-13 00:58:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 72e552f9-c78c-35b5-b9f4-1caab1a67c34 | -20.4485 | -53.042801 | 2025-11-13 00:58:00 | METOP-C | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7a8a9a65-b56d-3e61-b661-289d5198c198 | -3.2237 | -45.5816 | 2025-11-13 00:58:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f710e58b-1848-3ed3-b160-5122399b7024 | -7.228 | -47.980099 | 2025-11-13 00:58:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 445af8b2-70d1-349d-9e37-63b6d7a61b64 | -4.5351 | -46.422501 | 2025-11-13 00:58:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ae691ca8-a79c-3213-a090-3706fd29c51c | -3.0915 | -49.2972 | 2025-11-13 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 3d804f0a-b43c-3b78-bd34-e51042519b4b | -4.5344 | -46.4376 | 2025-11-13 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 45b4a1be-a202-30ae-90a9-847b67321855 | -7.6788 | -45.8747 | 2025-11-13 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 96a637e8-3e43-3e6d-a97d-b7b80ed0d7a7 | -3.0917 | -49.2547 | 2025-11-13 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 09e65d53-1abf-3df2-a00f-0aec1d3db877 | -4.7018 | -46.4508 | 2025-11-13 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 60.8 |
| d95ee93f-ecd4-39bd-bbb8-41af503b0038 | -3.8658 | -49.7998 | 2025-11-13 01:00:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| f337628d-fd43-3173-964e-c2c41f8a0bd3 | -2.4449 | -49.2731 | 2025-11-13 01:00:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| be2f6361-7194-3348-9580-551930f08a25 | -12.6557 | -46.7407 | 2025-11-13 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 3f09d0db-5741-3b01-af51-4b81ec53b1ad | -2.445 | -49.2519 | 2025-11-13 01:00:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| fed70232-09ec-3a72-b6e7-13b4382068e7 | -3.2192 | -45.5846 | 2025-11-13 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| f79bd26c-344b-31ff-be15-e0e6e2886ef9 | -21.8957 | -56.7489 | 2025-11-13 01:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 79.3 |
| af07fc8b-ecb9-381c-95e0-3317b5bcbf1e | -3.1453 | -45.4978 | 2025-11-13 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 5a3faaee-03e5-395a-8dc4-07a97486fa20 | -21.8962 | -56.7275 | 2025-11-13 01:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 68.6 |
| cb83eefa-eb99-3760-8fa0-9589df8b4750 | -3.2191 | -45.607 | 2025-11-13 01:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 2223b156-34f6-31fe-b7f3-2fd3a0ec7896 | -2.8297 | -45.4419 | 2025-11-13 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 27964a44-b47c-38f5-8b46-682e64684c27 | -3.1639 | -45.497 | 2025-11-13 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 75.6 |
| b2537553-bcbf-3428-a21a-67c3aa22761f | -4.7204 | -46.4497 | 2025-11-13 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 139.5 |
| 164e32bd-fa0f-34b1-9277-6869933822fd | -3.0916 | -49.2759 | 2025-11-13 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 149.8 |
| 2ae87f14-70ca-385d-8e23-e73ff9d53109 | -4.7206 | -46.4276 | 2025-11-13 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 63.5 |
| d455d9ec-50bd-3c19-a0ae-a3d4d6c0c0ca | -3.0916 | -49.2759 | 2025-11-13 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 90cbca50-339d-3297-9932-0897f0c0c64e | -3.8658 | -49.7998 | 2025-11-13 01:10:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 11b8c740-f609-38ed-85f7-21f563f058ca | -4.7206 | -46.4276 | 2025-11-13 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 27604787-e793-31b9-b9d9-255e5e16113b | -12.6557 | -46.7407 | 2025-11-13 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 8a3e9ff2-9fa7-35b6-a41b-8f7c896f7dfe | -3.1101 | -49.2753 | 2025-11-13 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| d3c60f75-1355-3038-bf82-ddd0bc0c8ecc | -4.5344 | -46.4376 | 2025-11-13 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| e138809d-ec13-3dc2-aaf2-abad9d4d2d9c | -4.7018 | -46.4508 | 2025-11-13 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 71.6 |
| dd1771fc-79e0-3fa3-be99-775b21735fe1 | -3.2378 | -45.5839 | 2025-11-13 01:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 453517ba-6ec4-309b-b70e-4fcf36d8f745 | -4.7204 | -46.4497 | 2025-11-13 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 122.1 |
| c89790b6-45a4-300e-8e54-a468eb1f5702 | -2.8297 | -45.4419 | 2025-11-13 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 5c18ca7d-14b8-341d-a544-edd602b3c30a | -3.0917 | -49.2547 | 2025-11-13 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 19c87d9a-8b50-35de-b520-54f3dd8de947 | -3.3729 | -48.4107 | 2025-11-13 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 5321ff76-db96-3b99-91a7-4a5fc8e496f2 | -5.5721 | -47.1057 | 2025-11-13 01:20:00 | GOES-19 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| b7b6437f-c6c7-3f1c-a8d8-b2e375a287b5 | -7.6788 | -45.8747 | 2025-11-13 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 5b9dfd93-fb16-35ae-9e40-0fb9b769c26f | -3.8658 | -49.7998 | 2025-11-13 01:20:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| ecefa1a6-da11-3b40-9951-9624bda7407e | -4.7204 | -46.4497 | 2025-11-13 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 23d9c964-0324-3983-b1c2-81e590e0e33f | -3.2192 | -45.5846 | 2025-11-13 01:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 6d35a6cc-831f-3f17-b469-43a6860c0c80 | -3.1101 | -49.2753 | 2025-11-13 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 6f8160e7-c7f5-30c4-8284-f245382cd359 | -4.5344 | -46.4376 | 2025-11-13 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 863671a0-1db6-3a00-8127-6afc58e23a06 | -4.7018 | -46.4508 | 2025-11-13 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 6cb03f83-ce54-3fa9-8c1b-e7fa19f6d961 | -3.8659 | -49.7786 | 2025-11-13 01:20:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 2bf40573-8545-31d0-908d-df4bdeadfb94 | -3.0731 | -49.2765 | 2025-11-13 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 1d9f5893-73f7-3326-87bd-13557a2818b9 | -3.0916 | -49.2759 | 2025-11-13 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 58b5c771-810e-3bf1-989d-f8d2cd7f2918 | -12.6557 | -46.7407 | 2025-11-13 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 34299941-75bb-3006-b717-999c1ae767bf | -4.7206 | -46.4276 | 2025-11-13 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 49.8 |
| cf1663f9-38ab-372b-ba4f-92e3af139170 | -2.8111 | -45.4426 | 2025-11-13 01:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 51.2 |
| edfff7cc-fea0-385e-944a-38d8e265006e | -12.6557 | -46.7407 | 2025-11-13 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 11a3ac4b-8327-323e-bcb7-6a4ea51731dc | -3.8658 | -49.7998 | 2025-11-13 01:30:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| e37feab4-3f46-3ce3-80f8-fee9c8677613 | -4.5344 | -46.4376 | 2025-11-13 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 58a0a763-2838-3406-a9b5-4c8f85f0cf68 | -2.8111 | -45.4426 | 2025-11-13 01:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 4be24632-e76b-3dd9-bbec-abec6c20c7d8 | -4.7206 | -46.4276 | 2025-11-13 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 6ba87276-1013-30f7-b6c7-4972e2900902 | -4.7204 | -46.4497 | 2025-11-13 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 309cbd74-444d-325d-bd02-0ab3e96f4796 | -3.0916 | -49.2759 | 2025-11-13 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 56108818-88ea-372e-badb-9c1a0996822d | -3.1101 | -49.2753 | 2025-11-13 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| ed143efb-b9cd-30eb-b2b9-904541b13edd | -3.2192 | -45.5846 | 2025-11-13 01:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 3a5955f5-9c64-3f2d-98f3-4544e60390b6 | -4.7018 | -46.4508 | 2025-11-13 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 2c4e9e78-b08b-3f38-8356-9c2a526e7ab8 | -4.702 | -46.4286 | 2025-11-13 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 49.6 |
| d1ad3711-e02c-377d-b687-7112286e039d | -4.7018 | -46.4508 | 2025-11-13 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 77.8 |
| c7ef7378-ff42-3893-b785-87901198c6d6 | -4.7206 | -46.4276 | 2025-11-13 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 3b875333-55bd-3af9-abbb-98273c1fd204 | -3.0731 | -49.2765 | 2025-11-13 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 42aeb0e1-d802-3dea-aeac-a54ca4aa854b | -3.0916 | -49.2759 | 2025-11-13 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| e5f498bc-1e44-3281-b6da-8c8a27e14732 | -3.8659 | -49.7786 | 2025-11-13 01:40:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 357291c2-0ef7-3a1b-9c8e-90d9a79fcda9 | -3.2192 | -45.5846 | 2025-11-13 01:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 7d3f725a-06a9-327c-a64f-ee1e77a08b04 | -5.3262 | -45.2041 | 2025-11-13 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 8a563b4c-4479-3697-b15b-4fff059f199d | -6.9226 | -35.1441 | 2025-11-13 01:40:00 | GOES-19 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 83.7 |
| 453ebf75-4ce4-3a0b-b65d-81d7082a00ac | -9.4192 | -40.3695 | 2025-11-13 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 121.9 |
| 6687b98f-233f-3d33-b16c-62fd82407b4d | -4.5344 | -46.4376 | 2025-11-13 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 38e13a15-f10d-3b1b-9ed8-2883580ae42b | -4.7204 | -46.4497 | 2025-11-13 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 12469645-c133-35e3-a21e-ae67bce38eb9 | -3.7981 | -45.1548 | 2025-11-13 01:40:00 | GOES-19 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 91.9 |
| f979c9b0-1c8d-31cf-a941-c382f9ea1dd4 | -9.4383 | -40.3668 | 2025-11-13 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 78.1 |
| 7cc412d2-1d90-3ad0-a462-dc054d9c15c5 | -12.6557 | -46.7407 | 2025-11-13 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 991c7115-c56a-3029-98e7-11c1ac496f0b | -3.8658 | -49.7998 | 2025-11-13 01:40:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| b9a055bc-5fb8-3eda-842a-a3851696df0d | -9.4196 | -40.3447 | 2025-11-13 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 83.2 |
| ab1fe34d-7f5d-3b71-915b-9328be81f5c2 | -3.2192 | -45.5846 | 2025-11-13 01:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 56.6 |
| a2511ba6-4e8a-3b3b-98c1-844aa1e5bc05 | -3.8658 | -49.7998 | 2025-11-13 01:50:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 0369db84-f084-363f-9c57-d3f9225d697f | -4.5344 | -46.4376 | 2025-11-13 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 67cba454-02d6-357a-89a2-78427742289d | -12.6557 | -46.7407 | 2025-11-13 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 141.2 |
| fb3bdada-54bf-370c-a4fc-1a3b9f2e01af | -9.4196 | -40.3447 | 2025-11-13 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 138.3 |


[Clique aqui para ver as próximas entradas](README9.md)
