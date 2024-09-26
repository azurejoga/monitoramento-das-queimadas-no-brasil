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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3691b55a-97b6-35ee-b2b8-8e9c337187f4 | -12.83191 | -62.69793 | 2024-09-26 02:21:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| ecf66e03-9749-32c5-b64d-34cb21764d57 | -12.83476 | -62.71527 | 2024-09-26 02:21:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 28.8 |
| bab63a06-43a5-3c07-b054-abeef8c7866b | -12.84388 | -62.69584 | 2024-09-26 02:21:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 220.1 |
| 7e753def-632c-313b-ac02-a8447072af6d | -12.84672 | -62.7132 | 2024-09-26 02:21:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 7b906164-f3b5-3c86-a088-b98a04db77a4 | -6.79356 | -59.31693 | 2024-09-26 02:21:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 139.5 |
| b75f867f-0d40-3258-8e12-156c2c06f928 | -6.79456 | -59.30961 | 2024-09-26 02:21:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 149.4 |
| ad768591-8553-3fae-8791-e9dd9431a28b | -6.94265 | -63.11736 | 2024-09-26 02:24:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| e1f0c24c-fff6-34f6-a202-29b28d4b3cc1 | -6.9664 | -62.92268 | 2024-09-26 02:24:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 78f6f142-700b-351f-b1c8-3b289cb4d6be | -7.5456 | -69.92897 | 2024-09-26 02:24:00 | TERRA_M-M | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cb642cc6-4ea3-3482-bf81-c64782889a7e | -7.72327 | -72.77088 | 2024-09-26 02:24:00 | TERRA_M-M | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 47c5fa21-b570-3f0c-ab8a-74c6e88098ea | -7.72407 | -72.77634 | 2024-09-26 02:24:00 | TERRA_M-M | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 42896bd7-e410-31d7-9389-af49b89ccef8 | -7.72485 | -72.78249 | 2024-09-26 02:24:00 | TERRA_M-M | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 8a0aabe3-9d13-3555-ab10-577c69ff3636 | -7.84666 | -72.77737 | 2024-09-26 02:24:00 | TERRA_M-M | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c7097846-6a88-3ac7-bef0-6eb180efbe19 | -7.95387 | -72.97297 | 2024-09-26 02:24:00 | TERRA_M-M | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 9.0 |
| eabd27d4-af3e-36c3-888d-781bcdb5e17c | -6.9297 | -63.11943 | 2024-09-26 02:24:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 8cc2b78a-58cf-3de6-a448-245775d1aaca | -6.93949 | -63.09695 | 2024-09-26 02:24:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| deccd306-65e5-33e0-b97a-8262c8c3de7a | -2.6785 | -57.531 | 2024-09-26 02:25:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| b168b54d-c520-393f-91d0-30ef90550600 | -2.6968 | -57.5307 | 2024-09-26 02:25:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 78d05512-d5f4-3561-ae7b-a49838457510 | -3.5488 | -50.38 | 2024-09-26 02:25:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 7afa3a1b-e7f6-36d5-b26f-a682e9981e10 | -3.5673 | -50.3794 | 2024-09-26 02:25:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 6fd7754f-be44-3d7e-b05e-98cb8a914993 | -3.9208 | -46.4459 | 2024-09-26 02:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 69067e4d-ae6c-39eb-81c5-ee7d0de12b7e | -6.784 | -59.3052 | 2024-09-26 02:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 0ac7d2ee-c51e-3453-a1b9-ab635bf53982 | -6.8024 | -59.3044 | 2024-09-26 02:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| ccfd7f1c-397e-3a44-9cde-4d70b0e77f4c | -6.9305 | -63.1241 | 2024-09-26 02:25:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 53fa0338-f076-320a-8722-4983fc53f07f | -6.9306 | -63.1053 | 2024-09-26 02:25:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 2ee8cd80-0c31-3caa-a8b6-56aaa4581b44 | -6.9489 | -63.1236 | 2024-09-26 02:25:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| c018bf84-3748-39a8-b8f3-8109bea1f300 | -6.949 | -63.1048 | 2024-09-26 02:25:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| ed235c2c-4f89-391e-bf3c-968839e3a4de | -7.2905 | -61.106 | 2024-09-26 02:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 74ce23ee-0d13-3ac5-9131-2e155210f275 | -7.3637 | -55.5134 | 2024-09-26 02:25:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 215.1 |
| f3da40eb-9985-3c6e-90f9-efca7be470e0 | -7.3639 | -55.4935 | 2024-09-26 02:25:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 159.8 |
| 02af1927-56d9-3b40-ad61-89470e955202 | -7.3823 | -55.5124 | 2024-09-26 02:25:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 215.0 |
| 69655298-3b6d-3dfe-91ab-ef6e93afb6bd | -7.3824 | -55.4924 | 2024-09-26 02:25:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 168.8 |
| f1930c1e-23ce-3593-a279-99b1b57931b0 | -7.5894 | -42.2971 | 2024-09-26 02:25:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 92.9 |
| 1852ab23-4e38-33ff-831c-009e905dbbb6 | -7.5769 | -62.7828 | 2024-09-26 02:25:50 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| e8b5091b-eac5-329b-9a4e-849de62cfa71 | -7.7968 | -54.7464 | 2024-09-26 02:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| a69ee2f3-54ba-32f3-96e5-09f286218876 | -7.797 | -54.7263 | 2024-09-26 02:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 5194d8d7-f99a-3dd9-946f-d2aebc49b11f | -7.8154 | -54.7453 | 2024-09-26 02:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 183.9 |
| 7c263b70-b20e-3a05-bc04-8cef4304f364 | -7.8156 | -54.7252 | 2024-09-26 02:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 265.9 |
| f3f77972-6bbb-3ea5-aab8-020d837aadfe | -7.834 | -54.7442 | 2024-09-26 02:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 8067defc-c57c-35b3-829a-77447d0d3024 | -7.8341 | -54.724 | 2024-09-26 02:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 162.3 |
| 9b37ba8f-e20c-3d59-9bbe-42a7bf2223c4 | -7.9353 | -71.4725 | 2024-09-26 02:25:52 | GOES-16 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 47.6 |
| e84cc1f8-500b-345b-8906-32d0b12f7b7b | -8.1394 | -61.2817 | 2024-09-26 02:25:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| a38f1014-7666-3a62-938b-b239b95d0a74 | -8.1757 | -61.3946 | 2024-09-26 02:25:53 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| ceb16b91-bc34-30fb-b5c2-e25bbdec640b | -8.3155 | -54.9956 | 2024-09-26 02:25:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| c44950a3-8862-3ca7-b3ff-7c54a3315442 | -8.6847 | -67.0097 | 2024-09-26 02:25:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 3c98956e-263a-338e-a5bb-e8b9671c3a3f | -8.7912 | -58.2182 | 2024-09-26 02:25:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 4420dcd9-03ac-3cb1-81b0-ef6b2bfe5cc7 | -8.8096 | -58.2367 | 2024-09-26 02:25:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 021330f5-ae71-3223-98cd-07518346667a | -8.8098 | -58.2172 | 2024-09-26 02:25:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 184.8 |
| 9fbfb980-ff66-3ea9-9d2d-cae74ce1aa18 | -8.8099 | -58.1976 | 2024-09-26 02:25:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 9b021135-6a5f-3fb3-ac64-c79b1f1cf042 | -8.8282 | -58.2357 | 2024-09-26 02:25:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 25.0 |
| e276a445-6145-3b7f-963a-cbf59ac23e86 | -8.8284 | -58.2161 | 2024-09-26 02:25:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| afb5a7b9-ed8f-3fe0-ad6f-ac79b144cc58 | -9.086 | -61.1245 | 2024-09-26 02:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| fd54d9f5-faef-3986-9035-723795806647 | -9.1046 | -61.1237 | 2024-09-26 02:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| c5754090-8e45-3707-a116-b54e53ce748b | -9.1349 | -65.564 | 2024-09-26 02:25:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| bfc31af6-c873-3711-8b38-8891c1e71b0a | -9.3961 | -50.0267 | 2024-09-26 02:25:59 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| e0232b47-8e5b-3cd1-819a-ab3c2c28047b | -9.6015 | -50.1566 | 2024-09-26 02:26:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 5a40924e-01c0-3c69-9a8e-3eaa945c771a | -9.6018 | -50.1352 | 2024-09-26 02:26:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 16f368b3-f375-3cb8-97b6-e0786501dc94 | -10.3882 | -67.8737 | 2024-09-26 02:26:06 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 28356800-eb99-38c9-950b-b5ef268b9473 | -10.9105 | -57.4308 | 2024-09-26 02:26:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 44e44643-f66c-3f08-8b5c-8fac96272612 | -11.2224 | -45.5131 | 2024-09-26 02:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 101634f6-de71-3d9d-a302-1a4752073e57 | -11.2599 | -65.299 | 2024-09-26 02:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 219f6a3e-696c-3643-b97d-83ce62e0876c | -11.26 | -65.2801 | 2024-09-26 02:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 1f78a0de-e991-3d54-b62c-9155f03b3075 | -11.2786 | -65.2982 | 2024-09-26 02:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 39.9 |
| e2763c45-e1e6-3de1-854d-e2fb5d985037 | -11.2788 | -65.2793 | 2024-09-26 02:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 41.0 |
| f8c98ac8-cf87-3828-b9f7-6e72685adec3 | -11.4824 | -56.7692 | 2024-09-26 02:26:12 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| a443fc8f-3a14-3032-a7ca-262c4cfb9955 | -11.955 | -60.363 | 2024-09-26 02:26:14 | GOES-16 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 9e37de27-1531-31e3-b45c-d0e0c1ae2677 | -12.2175 | -45.5074 | 2024-09-26 02:26:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| b108d5da-242a-3e7d-ad4f-8f79ae470a7f | -12.2367 | -45.5045 | 2024-09-26 02:26:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 46444b34-076c-30af-9530-c05e55f14cbb | -12.5085 | -53.498 | 2024-09-26 02:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 1e77002d-6192-38b1-86dd-17f54aa369fc | -12.5273 | -53.5168 | 2024-09-26 02:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 279faa30-1cce-37c8-b91f-de09f84463d6 | -12.5276 | -53.496 | 2024-09-26 02:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 207.0 |
| 8f43a99d-289d-3a2e-a10d-60751b73bde3 | -12.5464 | -53.5147 | 2024-09-26 02:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| e6868fc6-eedb-3a43-a2bc-d7453ec67b9b | -12.5467 | -53.494 | 2024-09-26 02:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 118.1 |
| d8b6c329-b33a-3d2f-9ed1-755c655f6e45 | -12.822 | -62.7078 | 2024-09-26 02:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 37.7 |
| e11a4519-8c22-37ed-8420-d85dbb7d57d4 | -12.841 | -62.7067 | 2024-09-26 02:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 190.6 |
| af336600-a9d9-3aa5-825d-c5897da214cd | -12.8411 | -62.6874 | 2024-09-26 02:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 33f8273e-8e23-3d67-a1f3-e06653358707 | -12.8599 | -62.7056 | 2024-09-26 02:26:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 2077df78-c278-36c3-8149-344b3c95e4b0 | -12.8601 | -62.6863 | 2024-09-26 02:26:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 54e9b899-bd92-381a-8467-ad25a94a474b | -13.2863 | -51.326 | 2024-09-26 02:26:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 59a7f6ab-d5c4-3a3e-a25e-26e15f2439ea | -13.3052 | -51.3449 | 2024-09-26 02:26:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 89d956a0-ef24-3fe0-9948-9264638b983f | -13.3055 | -51.3235 | 2024-09-26 02:26:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 33b61866-7884-387c-984e-0eadec57f553 | -13.4993 | -61.2698 | 2024-09-26 02:26:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 73e90209-e027-31df-9b25-a37ce1238c54 | -14.4439 | -45.2555 | 2024-09-26 02:26:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| b9225a01-22c3-3906-9da4-007eadc56fdd | -14.8828 | -51.4777 | 2024-09-26 02:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.3 |
| ba00e911-479b-3b05-8e32-f9ee2bc3d183 | -16.098 | -52.0111 | 2024-09-26 02:26:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 137.1 |
| c35d4138-5f4c-3b89-a957-bdf1be186e5d | -16.0985 | -51.9896 | 2024-09-26 02:26:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 177.0 |
| 5dc63743-204f-3b7d-a9bd-41dff9422b97 | -16.1176 | -52.0082 | 2024-09-26 02:26:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 189.1 |
| 140cd406-654d-351e-99d6-9a4a106c095b | -16.118 | -51.9867 | 2024-09-26 02:26:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 226.9 |
| 35d578d1-c9e8-33b1-bb6f-ee0708b6db05 | -16.593 | -56.0067 | 2024-09-26 02:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 106.8 |
| a0dfa155-8683-3db6-9ac1-da607a3f8102 | -16.5735 | -56.0091 | 2024-09-26 02:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 56.1 |
| afa7f155-cb44-3530-8808-44b413315ea5 | -16.5927 | -56.0274 | 2024-09-26 02:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 62.9 |
| 4cbd6d1c-fdaf-3774-a4b5-dfd0da720806 | -17.0995 | -56.1504 | 2024-09-26 02:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 66.1 |
| 2bf0c923-6e00-39a0-b35d-28873046da6b | -17.1188 | -56.1686 | 2024-09-26 02:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 54.2 |
| 3f3fac6f-e50d-3aa6-b8f1-8fa5a3bae806 | -17.1191 | -56.1479 | 2024-09-26 02:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 62.8 |
| 3f759899-8beb-3487-b91b-d48fa7b1a026 | -20.4197 | -41.8798 | 2024-09-26 02:26:58 | GOES-16 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 56.0 |
| 297925d8-0bd4-3e45-bea4-1de0eb4e34df | -20.5876 | -51.5026 | 2024-09-26 02:27:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 112.7 |
| ff06ee01-07a2-3af2-9de0-f308006fa5be | -20.5881 | -51.4802 | 2024-09-26 02:27:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 104.0 |
| 2adbcc7c-9464-30bc-926b-e768ee5d2981 | -20.6074 | -51.5209 | 2024-09-26 02:27:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 134.2 |
| 537cfab1-ef1d-3557-953e-b8a727a638df | -20.608 | -51.4986 | 2024-09-26 02:27:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 263.4 |
| d416e013-10c5-3823-bbc3-0ecc51eeb497 | -20.6086 | -51.4762 | 2024-09-26 02:27:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 110.7 |


[Clique aqui para ver as próximas entradas](README46.md)
