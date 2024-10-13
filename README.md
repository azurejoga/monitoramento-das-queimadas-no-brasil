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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 760a09f2-625f-3c79-814c-6f63eabb73b8 | -18.21 | -56.56 | 2024-10-13 00:03:41 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1db42d41-cb81-3cf8-bab2-b8cd940ab994 | -17.9 | -57.36 | 2024-10-13 00:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d620af3b-96d1-3ca3-9042-6c971ba0c642 | -10.95 | -44.7 | 2024-10-13 00:04:21 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ec290288-2803-3451-83a0-4bda22e1a22e | -10.92 | -44.69 | 2024-10-13 00:04:23 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a1c0c24e-40bb-3a65-9e0a-77b5a249243f | 2.58 | -60.6973 | 2024-10-13 00:04:51 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 9f6d86c4-a0f6-362c-ab9e-bb1e17325ed3 | -4.15 | -45.76 | 2024-10-13 00:05:03 | MSG-03 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 645228ec-87c4-3c33-81e5-ce64c15353cc | -4.18 | -45.76 | 2024-10-13 00:05:03 | MSG-03 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9b9b6f57-3080-30a9-8064-e9952c9bf9e6 | -1.6635 | -52.1265 | 2024-10-13 00:05:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 646aab2c-bf53-397c-b01d-3df810005b7d | -1.9217 | -61.7432 | 2024-10-13 00:05:17 | GOES-16 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 535ec174-adb4-3e25-8e0e-33f083c04b09 | -2.1508 | -48.8112 | 2024-10-13 00:05:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 1e70b1ea-26f4-37c9-9844-d86fc6d9d576 | -2.1692 | -48.8322 | 2024-10-13 00:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 876cef45-81a0-3680-8294-55ef0a783b38 | -2.1693 | -48.8108 | 2024-10-13 00:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 6717cff5-71f8-33ec-b4cf-2347760afe46 | -2.5258 | -47.2674 | 2024-10-13 00:05:21 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| c632b497-6362-314f-8cca-100825dfd4c3 | -3.0731 | -54.2473 | 2024-10-13 00:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 25510a6b-0878-39c7-8305-3706a727d91f | -3.0732 | -54.2273 | 2024-10-13 00:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| bb91ae17-7494-3e11-9472-bc0d54cc2dc3 | -3.0773 | -53.036 | 2024-10-13 00:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| d8a4a983-d552-3961-9af9-138880a70a85 | -3.0915 | -54.2469 | 2024-10-13 00:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| f8832a4b-5aa6-3523-bc3e-3ec77c2bf2b8 | -3.0956 | -53.0559 | 2024-10-13 00:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 117.5 |
| ce467b2c-2ab1-3709-b216-a47a298347f8 | -3.0957 | -53.0355 | 2024-10-13 00:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 247.1 |
| 44814363-a385-3b7e-8b5b-c1ebc9a81a44 | -3.0957 | -53.0152 | 2024-10-13 00:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 1a492991-9361-3117-92d2-f8097a6ae2e2 | -3.114 | -53.0554 | 2024-10-13 00:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 2a32ef82-57e2-35af-9e49-7fa1c5f382ee | -3.1141 | -53.0351 | 2024-10-13 00:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 131.2 |
| 237b409b-781e-3641-8d0b-7073e4a6e56c | -3.2225 | -48.9306 | 2024-10-13 00:05:25 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 4b39412c-013c-3cf4-9181-7ad7f220c80c | -3.2226 | -48.9092 | 2024-10-13 00:05:25 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| c6132557-a5ad-39be-b454-4dcf784c32ef | -3.5172 | -45.4826 | 2024-10-13 00:05:26 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 6f09f5cf-1def-33a0-ae6b-9bc57917ac15 | -3.5449 | -51.2564 | 2024-10-13 00:05:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| b2e92015-77e0-3702-8eef-f7e835c64031 | -3.545 | -51.2357 | 2024-10-13 00:05:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| c87aebc3-4938-35a3-93bb-9a46be23bbbe | -3.7127 | -40.7346 | 2024-10-13 00:05:27 | GOES-16 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 93.4 |
| ca704e21-8a62-3137-908c-df77dc0f7330 | -3.7128 | -40.7102 | 2024-10-13 00:05:27 | GOES-16 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 145.2 |
| f602fe78-e039-3c51-9171-9cbd4634afd0 | -3.7316 | -40.7092 | 2024-10-13 00:05:27 | GOES-16 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 48.0 |
| 0dfa9d52-5ff2-342b-ba99-73e2eaaae327 | -3.625 | -54.132 | 2024-10-13 00:05:27 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 02a57b94-f3bb-3618-b7ac-764b78f23b24 | -4.085 | -43.9319 | 2024-10-13 00:05:29 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 725fee37-e841-35ac-b4b5-9a58c026017b | -4.0851 | -43.9088 | 2024-10-13 00:05:29 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| b890c73e-288c-3061-8b37-acdf98186984 | -4.1037 | -43.9309 | 2024-10-13 00:05:29 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 45807ae7-3cbd-31a3-9fc3-7e339de39759 | -4.1038 | -43.9078 | 2024-10-13 00:05:29 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 681cb625-73dc-3dbb-82d1-cc21c991cbc7 | -4.1148 | -48.2515 | 2024-10-13 00:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 142.5 |
| f95d2e2a-2934-3936-81f9-d8a01963ddf0 | -4.1149 | -48.2299 | 2024-10-13 00:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 129.3 |
| b61fda39-88dd-3993-a85e-9a7a004dba88 | -4.1479 | -45.7896 | 2024-10-13 00:05:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 169.4 |
| 0bbddccc-99ed-3d06-8e4c-1f1048df7015 | -4.148 | -45.7672 | 2024-10-13 00:05:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 129.3 |
| 3b33dba7-ff60-38d6-b681-dc9dc66c30cd | -4.1665 | -45.7886 | 2024-10-13 00:05:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 344.1 |
| 1707ee63-9acb-3d41-b4de-f16c7bb5cc68 | -4.1666 | -45.7662 | 2024-10-13 00:05:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 267.0 |
| ea1e92cd-2692-36ac-b4bf-7c61918a0a11 | -4.4026 | -49.7563 | 2024-10-13 00:05:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 1b435078-b97a-33a5-99b2-f6e31b823f43 | -4.7188 | -60.7882 | 2024-10-13 00:05:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 881bcf75-2656-306f-9eea-0c2a87ad3eca | -4.8418 | -47.739 | 2024-10-13 00:05:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 40.9 |
| cf1b54f2-f486-32d4-96a9-46fefba0df60 | -4.8604 | -47.738 | 2024-10-13 00:05:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 318994e1-e76c-3379-b9d6-28d21053bdb5 | -4.898 | -47.6707 | 2024-10-13 00:05:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 37.5 |
| fc34ab14-c225-3dfb-86dd-94aff1263edd | -5.0713 | -46.8499 | 2024-10-13 00:05:35 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 653f7d38-6522-3fb9-9166-115756dc96cb | -5.1381 | -45.3969 | 2024-10-13 00:05:35 | GOES-16 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| b5ec2f75-fb42-308c-b4a9-e5aadfca34cd | -5.1695 | -46.1569 | 2024-10-13 00:05:36 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 7d6b37b7-da02-3f16-83ac-0d7f9b84c77b | -5.1697 | -46.1346 | 2024-10-13 00:05:36 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 1cc9c50b-36d4-3f63-96b7-62a6bd5c951b | -5.5348 | -47.108 | 2024-10-13 00:05:38 | GOES-16 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| ca72926b-44d2-35b2-b95b-0aa3731e3c31 | -5.8759 | -46.4446 | 2024-10-13 00:05:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| a59022d4-4f93-3911-b7ba-50bfb7df13d4 | -6.1299 | -47.2884 | 2024-10-13 00:05:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 575dd648-5ce7-3c93-a091-856239349c98 | -6.1301 | -47.2664 | 2024-10-13 00:05:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 46.2 |
| cdd10b21-a008-3348-9478-028bc5ace95c | -6.747 | -59.3259 | 2024-10-13 00:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| a382bccb-6290-3369-854a-577e1b54de6f | -6.8734 | -59.802 | 2024-10-13 00:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 1ea96011-4611-3cde-b652-52befe4ce5b7 | -6.8918 | -59.8013 | 2024-10-13 00:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 19534ffb-49af-3411-a1c0-aedfc049215e | -6.9146 | -59.0488 | 2024-10-13 00:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 11e8536f-b06d-3b2e-b4d5-10eacb40b502 | -7.0425 | -59.2752 | 2024-10-13 00:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 0fc80581-975d-34e1-ae04-fe043a1b392a | -7.0426 | -59.2559 | 2024-10-13 00:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 41cf117c-3f9e-3d50-bed2-df2162c1d177 | -7.3823 | -47.2586 | 2024-10-13 00:05:48 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 38799774-5690-37ed-9290-42e7806039ff | -7.3657 | -64.6656 | 2024-10-13 00:05:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 779c884c-53db-3546-b7f6-bf2ee5657c90 | -7.3658 | -64.6469 | 2024-10-13 00:05:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 129.2 |
| fb6d0f75-34ba-3662-8008-c3a06e149b9d | -7.3841 | -64.665 | 2024-10-13 00:05:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 145.5 |
| 263c218d-5cc8-31b9-a812-0f0e69fde6d9 | -7.3842 | -64.6464 | 2024-10-13 00:05:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 117.2 |
| db59000a-12de-3cd6-b05a-6e4af30e842d | -7.6627 | -47.3229 | 2024-10-13 00:05:50 | GOES-16 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 9239d746-90af-3a7a-b527-9c7273ce03a7 | -7.6629 | -47.3009 | 2024-10-13 00:05:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| b47f7464-6010-3a57-9539-9b5ab0a3a628 | -7.6815 | -47.3213 | 2024-10-13 00:05:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| bfba9f13-e031-390f-a076-db80e4158873 | -7.6817 | -47.2992 | 2024-10-13 00:05:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 38e5d153-2441-3c1e-aeb7-2370cf1c32da | -7.9003 | -44.6264 | 2024-10-13 00:05:51 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| dea6137a-fc8b-3f1c-9c21-e9295ff904ef | -7.9006 | -44.6035 | 2024-10-13 00:05:51 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.3 |
| d5523bd4-2bc0-3d53-a39b-b7bf59900b61 | -7.8715 | -54.7016 | 2024-10-13 00:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 05181f4a-4d5f-3390-b33a-8b6566ff82f6 | -8.0672 | -44.8388 | 2024-10-13 00:05:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.0 |
| bd4c76f9-d352-3fa0-b8f9-21b7a066c77b | -8.0675 | -44.8158 | 2024-10-13 00:05:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 204.3 |
| 862e741e-9dc8-3c6a-ab53-653628c229fc | -7.8895 | -63.0171 | 2024-10-13 00:05:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| ad8ed17e-387d-3d41-a2f9-c1b95e2772c0 | -8.2352 | -64.0961 | 2024-10-13 00:05:54 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| cdcac626-3c0c-3ae9-9f2b-8b3cd1dc2808 | -9.5185 | -47.8049 | 2024-10-13 00:06:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 0005ea6d-a884-3b1f-b01f-2136e3370dcd | -9.7359 | -64.2295 | 2024-10-13 00:06:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 1f275736-36a5-3acd-b3b3-0565ccae2714 | -10.1918 | -36.7236 | 2024-10-13 00:06:03 | GOES-16 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 111.1 |
| 389b3967-35ae-3d42-b525-2bc47cda5e17 | -10.9307 | -44.7021 | 2024-10-13 00:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 4a629355-3213-3bf5-aac9-3bdf5e706b40 | -10.9311 | -44.6789 | 2024-10-13 00:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 383.1 |
| c7924a6c-3fa0-3e30-a1d6-369fd46b91d9 | -10.9315 | -44.6557 | 2024-10-13 00:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 2bd25eea-0b4d-3c4c-a448-aa1f0b9dc568 | -10.9502 | -44.6762 | 2024-10-13 00:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| dcb612a3-17f1-305e-9b9c-84d655d9f182 | -10.9506 | -44.653 | 2024-10-13 00:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 28b34acb-7892-3d28-aa74-91c6ab7c36fc | -10.9519 | -61.1226 | 2024-10-13 00:06:09 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 3a05bd42-7109-3b65-bcc1-4dea03eadfb3 | -11.2532 | -50.9249 | 2024-10-13 00:06:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| c534aef1-1294-3535-ac5a-c8a22d200b2e | -11.2535 | -50.9036 | 2024-10-13 00:06:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 300ea376-e506-3edd-8ef2-beddf7ab1138 | -11.2722 | -50.9228 | 2024-10-13 00:06:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| b16645e5-9d67-332d-b278-68448caf324c | -11.2725 | -50.9016 | 2024-10-13 00:06:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| e155654a-e95f-34e9-abad-05024ac211b0 | -11.712 | -64.9777 | 2024-10-13 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.0 |
| b51983f5-02df-39f8-bb7f-fb886e6cdb01 | -11.7308 | -64.9769 | 2024-10-13 00:06:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 38d21088-c048-3433-8bd5-ab7b0b52ac24 | -11.862 | -65.0278 | 2024-10-13 00:06:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.2 |
| c5f117d6-a84c-36ed-9d44-383730b68fff | -12.2754 | -47.6473 | 2024-10-13 00:06:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| f1593fa7-3794-3af9-a59b-b47cf587836e | -12.3792 | -63.7485 | 2024-10-13 00:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 4f6a735e-a767-3f56-b53c-00ef4f36e5df | -12.3793 | -63.7294 | 2024-10-13 00:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 33b13a7a-082e-3eb6-9aa7-3a1452f84895 | -12.398 | -63.7475 | 2024-10-13 00:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 174.3 |
| 71a1eb10-42d8-31b6-b51f-435defbf6b3e | -12.3982 | -63.7284 | 2024-10-13 00:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 270.3 |
| a785eecf-53da-36f1-bab7-d52f05d812e4 | -12.7499 | -62.2883 | 2024-10-13 00:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 80.5 |
| db3bd7f2-a50d-3744-93e8-2ac081218157 | -12.7688 | -62.2872 | 2024-10-13 00:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 369fc3c3-fc99-398c-934a-9dbdf88888a6 | -12.769 | -62.2678 | 2024-10-13 00:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 85.7 |


[Clique aqui para ver as próximas entradas](README2.md)
