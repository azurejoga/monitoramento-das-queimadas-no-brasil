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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a12cc134-92ce-3b8c-bb72-5dd730d3fc5d | -6.9486 | -59.549 | 2025-08-16 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 2011919a-da1d-3d5c-ae9d-ef0ba8187512 | -3.8209 | -47.7444 | 2025-08-16 01:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 383603e3-c21e-370a-845c-56106433666f | -7.9149 | -61.7288 | 2025-08-16 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 354936fb-3af1-33b0-8a90-3b5397e423a6 | -9.1709 | -59.6374 | 2025-08-16 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 131.2 |
| dc28d22e-f13d-3abe-a9cf-c554737e0f1a | -7.0797 | -59.2157 | 2025-08-16 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| e073a718-df3a-34cc-b1d0-1be0a9812540 | -7.9334 | -61.7281 | 2025-08-16 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 6cf051c8-f22a-3dda-a61e-53ffbddebc10 | -7.0612 | -59.2358 | 2025-08-16 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 8b9b28d5-3b5d-3d07-9eba-c29a1903bc60 | -9.4992 | -60.547 | 2025-08-16 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| b5b94a49-03d4-39da-b08f-1f8841833fee | -11.3466 | -55.4326 | 2025-08-16 01:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 3d4b8e3c-4b01-3ca0-9a15-c5284ac817d1 | -9.1523 | -59.6384 | 2025-08-16 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 9d01daa2-eb87-39bf-aeaa-f4ac8a8bc5ae | -12.575 | -46.9555 | 2025-08-16 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 36a0570d-6f5c-33f4-8e59-20d028eef5d2 | -7.0796 | -59.2351 | 2025-08-16 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 6326ba5e-da29-3d48-86e0-5b513fcd6898 | -14.6018 | -47.9243 | 2025-08-16 01:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 47.2 |
| bd55cca9-aee9-3a7d-9fd1-ec8d65908a2c | -7.8247 | -61.3327 | 2025-08-16 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 6a3debdd-c4e1-325c-8db2-c201aa437c41 | -14.6023 | -47.9018 | 2025-08-16 01:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 58.0 |
| add901d9-f7aa-33bd-af32-b6070229abc1 | -9.0346 | -67.427 | 2025-08-16 01:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| bc7dc259-0117-3382-bc3f-237e6574ce59 | -9.5179 | -60.5461 | 2025-08-16 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| ea35c4cc-abaf-3f43-bc03-684f93ce4c09 | -12.5947 | -46.9301 | 2025-08-16 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 0d4861f5-c7f3-3952-83ed-58073ae4acec | -6.9487 | -59.5297 | 2025-08-16 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 0bb28816-10f9-3863-b2a1-25ba6b2c7f1c | -12.6135 | -46.9499 | 2025-08-16 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| b37c91b6-b4de-31df-bd65-b2860bb696b7 | -7.9333 | -61.7471 | 2025-08-16 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 152c37e6-995b-3567-93b7-4fda09290996 | -9.518 | -60.5268 | 2025-08-16 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| edead085-7ed1-35c0-a677-7c89ed03bb9c | -13.1265 | -57.1494 | 2025-08-16 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 5a0edbd0-d9a0-3b26-8535-aaa4f1f47376 | -12.5942 | -46.9527 | 2025-08-16 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| d5e24c1f-af83-33c2-b296-e322fec8068e | -9.4994 | -60.5278 | 2025-08-16 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 97282fa9-950c-31ad-8044-87b71b4d67fe | -4.9305 | -43.2558 | 2025-08-16 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 2a1bd83b-04d1-347b-815b-6c9499aaa56c | -13.4294 | -43.6733 | 2025-08-16 01:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 51762c9b-bf1a-3ade-a499-d525b64fa13d | -9.1523 | -59.6384 | 2025-08-16 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 2475607f-370f-3adb-9b94-faa522151a41 | -14.9438 | -54.7166 | 2025-08-16 01:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 253.1 |
| da52dd00-f28e-3abc-a393-eb98f0bf518e | -9.4992 | -60.547 | 2025-08-16 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 471e0f41-d68b-33fa-a27c-b13454ee292d | -12.6139 | -46.9273 | 2025-08-16 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| d57728c2-2237-3755-a31b-488169c17bb1 | -12.5947 | -46.9301 | 2025-08-16 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 5c60d675-9403-386a-b036-203c494dbada | -9.5179 | -60.5461 | 2025-08-16 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 52991c4e-3348-39cd-a02d-cd12b0be0376 | -9.4994 | -60.5278 | 2025-08-16 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 589161dc-88e6-399c-a0f2-70ea7932935e | -9.1711 | -59.618 | 2025-08-16 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 5dfab4b2-cc7a-3abb-844f-2800fe018eef | -14.9632 | -54.7143 | 2025-08-16 01:30:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 4fa64c48-fb95-3a74-b900-652d4963b522 | -11.3466 | -55.4326 | 2025-08-16 01:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 88ae6fd2-002e-3ed5-9d44-6cc2fde2b044 | -9.518 | -60.5268 | 2025-08-16 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 95cb93cc-79ac-3e47-84d9-ca7be1387a05 | -3.8209 | -47.7444 | 2025-08-16 01:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 0096cc14-b4a8-33e4-b752-9157d7fc0e00 | -7.9148 | -61.7478 | 2025-08-16 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 106.7 |
| b6aa588c-7a1e-318c-8c35-c5fa9e1dc013 | -13.4294 | -43.6733 | 2025-08-16 01:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| d760978d-3254-3d80-88b3-d45a8a0aab93 | -11.2596 | -50.4767 | 2025-08-16 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| b32fabd0-dafd-36c3-8332-cd740621ab59 | -14.9441 | -54.6959 | 2025-08-16 01:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 8da41439-2388-3f29-8114-7efaf8fe9aa5 | -12.5558 | -46.9583 | 2025-08-16 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 71dfbf5e-afe2-3599-9e3c-b966296d8961 | -6.6327 | -60.0033 | 2025-08-16 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 0d36dd20-2125-3256-8f54-0d9e62a28778 | -9.2082 | -59.6354 | 2025-08-16 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| ca92e9d7-9fca-3c36-822d-ce6249538962 | -7.9333 | -61.7471 | 2025-08-16 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| dd99cd9c-a65d-3d83-8633-5d8b4b8df410 | -19.5549 | -44.0662 | 2025-08-16 01:30:00 | GOES-19 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 4aaadca9-2c28-33e0-9c04-cf0a3506b147 | -12.575 | -46.9555 | 2025-08-16 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| ab2abf70-a26f-3b8b-8e01-522aa9b9d5a3 | -9.0346 | -67.427 | 2025-08-16 01:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 6d736877-3239-3436-ad09-bd972b9b8f9a | -12.5942 | -46.9527 | 2025-08-16 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 786e36e5-2980-3cce-a7d8-86e41b3cb146 | -7.0796 | -59.2351 | 2025-08-16 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 45fb43d0-3319-3e6f-92cd-bb9c9beab8c7 | -6.5638 | -43.0357 | 2025-08-16 01:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 7201148e-e1e3-3437-8eb3-a209078dac14 | -4.9118 | -43.257 | 2025-08-16 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 7d683f69-23d0-350e-9752-630ad2f610b8 | -14.9628 | -54.7351 | 2025-08-16 01:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| faecf8b5-c0e7-351f-917c-b5ee317cae3c | -9.1709 | -59.6374 | 2025-08-16 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 44eb1cce-e9d3-3d8b-8a20-9c264d3c51b2 | -7.9149 | -61.7288 | 2025-08-16 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 28738652-5b8d-399b-84c2-3fc7e96c9a73 | -12.6135 | -46.9499 | 2025-08-16 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 89fcbd04-f2cf-356d-858c-8ec715a895bb | -6.9487 | -59.5297 | 2025-08-16 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 8384fe0a-2476-394a-9d7f-52181209b1dd | -6.5641 | -43.0122 | 2025-08-16 01:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 62e5d5be-9217-32b5-a23f-1f0d214da088 | -7.0612 | -59.2358 | 2025-08-16 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 191441dd-c0bc-3c84-aa67-b7b110f5b67b | -9.1708 | -59.6568 | 2025-08-16 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 37622bfd-b208-3934-8454-3678201d53f7 | -14.9635 | -54.6936 | 2025-08-16 01:30:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 46.6 |
| e5adba44-7e54-3b5c-a497-4a1b665240f1 | -7.9334 | -61.7281 | 2025-08-16 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 958b285c-12d3-37ae-84f4-429347ad39ca | -6.9486 | -59.549 | 2025-08-16 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| c3dc2770-23b3-3d40-9976-3814fcfca879 | -13.1267 | -57.1293 | 2025-08-16 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 31.7 |
| afa6296c-3608-35e4-9e13-14dd24be6352 | -14.9435 | -54.7374 | 2025-08-16 01:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| c0cfb71b-a01f-3350-83a2-3b488f16aa4c | -9.1685 | -59.655701 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 19fb9ab4-31cb-3358-86d6-422b34c36cde | -9.0037 | -60.490799 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 730abc7b-2404-396a-a369-0b0b2322dbfe | -8.1498 | -62.778599 | 2025-08-16 01:39:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bc69a05c-c9d2-322c-a98a-d986f9ad50c3 | -9.0357 | -67.4188 | 2025-08-16 01:39:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 487cb3e6-b27f-38da-8157-d419aba5f7c0 | -7.9135 | -61.751099 | 2025-08-16 01:39:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 38d813ab-9d62-3418-a9c7-cfa66c9fce37 | -10.1192 | -57.758801 | 2025-08-16 01:39:00 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e0e5eb2-c1da-39ac-91fe-5c3811ca156f | -11.3681 | -55.411201 | 2025-08-16 01:39:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98ead01f-aaf0-31c1-a34a-c7f1b61e84ba | -9.0046 | -60.538502 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 599b02f9-9965-3cd6-b723-de6aa3286077 | -13.1296 | -57.167599 | 2025-08-16 01:39:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fcf0be04-cbcd-3336-96cb-6b91fa56a8a0 | -9.1608 | -59.623001 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 073d5482-ac4b-3aa5-8a78-fcaae98e81bd | -18.521099 | -50.749699 | 2025-08-16 01:39:00 | METOP-C | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2c8fea3a-2a1d-3fad-af40-cb28f74a904d | -8.9435 | -62.235401 | 2025-08-16 01:39:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a98f6d54-3edd-3038-a949-3445e69659cf | -6.6387 | -60.006599 | 2025-08-16 01:39:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 34ed8522-f97f-34b5-9273-8ee48ab3c99f | -7.6734 | -63.312401 | 2025-08-16 01:39:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 66b04ad4-9b02-39eb-85ce-a232a8d60005 | -8.9877 | -60.510502 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 77afa715-854e-302c-b32f-69da99f99d84 | -6.951 | -59.537102 | 2025-08-16 01:39:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9c0b391f-ba4f-3fb4-9d14-e26bf48c753e | -8.9865 | -61.7048 | 2025-08-16 01:39:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5d071b69-ad8f-3aa8-80a8-1147456844ef | -10.3432 | -64.471298 | 2025-08-16 01:39:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c63408c7-b0d5-30ce-a439-3d5b189c4517 | -8.1025 | -61.1861 | 2025-08-16 01:39:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a1b9c00b-2683-3c81-906f-c2f501ef1471 | -7.5244 | -61.319599 | 2025-08-16 01:39:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dcaa2cd6-2d8b-3913-925d-6411d14691d0 | -14.9549 | -54.736599 | 2025-08-16 01:39:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d5ed20ac-b441-3fd7-8430-044af399759a | -14.9544 | -54.694302 | 2025-08-16 01:39:00 | METOP-C | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4c2d9256-b7b9-3d43-b18a-608e789f97b0 | -8.906 | -60.735401 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27faef88-b7fa-38ad-830e-0688c5d76178 | -9.1627 | -59.631199 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bdfb85cb-e6b9-317d-8bfc-1bafa74e82b7 | -9.1881 | -59.6511 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| adeface7-2e1f-39fc-a8e1-d35661c63cca | -9.3977 | -60.541599 | 2025-08-16 01:39:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 57587765-633a-3f16-8bda-95bc880f83d2 | -8.9751 | -61.699902 | 2025-08-16 01:39:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 30a2fc7d-bd3f-3992-bfde-37f53cec06d6 | -9.3995 | -60.549099 | 2025-08-16 01:39:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d74533e-0995-3852-8c3b-2f5a2047f0db | -8.9719 | -61.685902 | 2025-08-16 01:39:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7f89f846-f40b-3670-a7fa-4518f96be853 | -9.1803 | -59.661598 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0574cc70-be2d-36fe-8013-900744524589 | -7.4389 | -60.028702 | 2025-08-16 01:39:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 165b961d-7284-348d-9008-44ee772d0317 | -7.6719 | -63.3055 | 2025-08-16 01:39:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a96a28c1-f8fa-3093-b8de-b5f20985ca06 | -7.9331 | -61.746601 | 2025-08-16 01:39:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README13.md)
