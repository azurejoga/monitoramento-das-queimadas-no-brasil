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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b051a1b3-56d6-3b59-a748-b5ab60836344 | -17.70378 | -57.45623 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a555e16e-929f-3cfc-b1e4-d0fab7c56f1a | -17.69291 | -57.42949 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| d6f77249-c380-3023-8231-60d96ce9ffd8 | -17.69231 | -57.43447 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 06ad1eb1-c174-34b3-bbfd-e702828d09b6 | -17.69172 | -57.43945 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2d073db5-7d95-37a5-a49c-fd0f9c688245 | -17.68829 | -57.42887 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 6b0f4e50-6201-3700-9eab-2ecc7ec0688e | -17.68367 | -57.42824 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| c18072b0-e4b1-3b8d-aaa7-1b660ceba953 | -17.25086 | -57.30328 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| a1c62de4-cfdd-3efc-93c4-c080719f7628 | -17.25027 | -57.30828 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 4ee7e606-120a-3b79-82fc-102d64ff3317 | -17.24968 | -57.31327 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 56c5934e-9975-3dbd-976c-1daa1fb3ffad | -17.22559 | -57.32443 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f94265e8-d951-393f-abb8-52eceafb0a20 | -17.20807 | -57.50744 | 2024-10-21 05:33:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b1747269-60ea-35cb-b698-03c39865ee54 | -17.02393 | -57.3298 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 48742304-0151-35bc-ac3d-908fbef2c680 | -17.00592 | -57.52032 | 2024-10-21 05:33:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3e80fc26-c491-339a-a1a7-3b76c452378a | -17.00535 | -57.52511 | 2024-10-21 05:33:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7110bb35-e86f-3c70-9e5a-8ff8fe1289cd | -16.9974 | -57.51426 | 2024-10-21 05:33:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 46a43ee0-24f0-3f1b-98c9-7707d39bf38e | -16.95318 | -57.52654 | 2024-10-21 05:33:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 501ada6b-a648-3274-a5e7-89432bb5a8cd | -2.4824 | -49.102 | 2024-10-21 05:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 8488e62f-d7be-32b4-acab-22be4a5ccceb | -2.8069 | -51.3613 | 2024-10-21 05:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 4ad73c80-73aa-3016-b6d8-8bbfcbc9a9e3 | -3.2146 | -50.8093 | 2024-10-21 05:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| eefe7a6c-8650-3806-b91f-9800822edd8e | -27.23632 | -52.57152 | 2024-10-21 05:36:00 | NOAA-21 | CHAPECÓ | SANTA CATARINA | Brasil | 4204202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f4fe311f-7c63-3729-9d04-cfa875d95803 | -27.23603 | -52.57691 | 2024-10-21 05:36:00 | NOAA-21 | CHAPECÓ | SANTA CATARINA | Brasil | 4204202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5d8a0bc7-e454-3ce3-9b62-a23db3d16fae | -27.23601 | -52.57471 | 2024-10-21 05:36:00 | NOAA-21 | CHAPECÓ | SANTA CATARINA | Brasil | 4204202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e69d38c0-eb41-3ce3-b1bc-ef83f0de2e9d | -2.4824 | -49.102 | 2024-10-21 05:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 13f3b5d3-6316-3bf3-9ef3-15b2ead65f2e | -9.81641 | -64.74574 | 2024-10-21 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7c873b4f-1f0c-3acd-a9a4-54eb3c9b29c3 | -9.76804 | -64.72359 | 2024-10-21 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73e1221d-3c78-3d18-b213-bd4cce40b09a | -9.76486 | -64.7181 | 2024-10-21 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 168e6f99-477f-3f23-a45e-ca934de5237c | -9.76416 | -64.72299 | 2024-10-21 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f309c1c6-cffb-346b-aab6-8b26335542de | -9.76346 | -64.72789 | 2024-10-21 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d12ef642-b3a3-383d-95fa-3acccd04cc95 | -9.76098 | -64.71751 | 2024-10-21 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 724f49ff-c7a7-3402-a93b-f935a862cae9 | -9.76028 | -64.7224 | 2024-10-21 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae772408-467f-32c4-921c-d272bf36bdce | -9.75958 | -64.72729 | 2024-10-21 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 905998c1-f3c5-3875-81d7-cf07abf16676 | -9.75639 | -64.72181 | 2024-10-21 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5a6efbe-d004-3e40-a84a-7efe5a881a0a | -9.65397 | -64.95543 | 2024-10-21 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5116b7ed-6da8-3500-ae22-0b0f6098e0d6 | -9.5719 | -64.70027 | 2024-10-21 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c77b617d-ef7a-3d6e-aedd-88557041a906 | -9.37578 | -66.48768 | 2024-10-21 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 91c46226-64e4-38d9-bc34-2120d28d89d1 | -9.37284 | -66.4832 | 2024-10-21 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9c09e016-c96a-3c90-8006-3a7d79508530 | -9.37226 | -66.48715 | 2024-10-21 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| de543de9-3a51-3189-bc11-0325e5fdcc1c | -9.37167 | -66.4911 | 2024-10-21 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce2e96fb-91d0-33f4-8208-6708184458c9 | -9.36932 | -66.48267 | 2024-10-21 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fcf5f2a4-463e-3cd2-a732-be966fd8564a | -9.36873 | -66.48661 | 2024-10-21 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9c04747-f5e7-38c0-8282-1bdbb7fca5b6 | -9.36521 | -66.48608 | 2024-10-21 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5d25402-3567-3963-a994-78e8e8a2e700 | -9.36463 | -66.49003 | 2024-10-21 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01b831f4-cdeb-3e06-8546-310bef269bb5 | -9.34602 | -65.91005 | 2024-10-21 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a14a28f4-9485-3d8d-86fc-57293457ed5d | -9.34478 | -63.22297 | 2024-10-21 05:53:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 749ebb56-1284-315f-bfef-3159fd17968a | -9.34052 | -63.22237 | 2024-10-21 05:53:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fe32d83-72f4-3132-96fc-17dc0289a90b | -9.17808 | -62.65634 | 2024-10-21 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27799ffd-043a-35ce-825c-432f762f5631 | -9.17302 | -65.44677 | 2024-10-21 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cb7689c-ef7b-3cae-a59c-062ab9374574 | -9.16932 | -65.44622 | 2024-10-21 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f8a46d1-9f63-3ab9-a9f6-d3c52e0bfe89 | -9.02857 | -63.36034 | 2024-10-21 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7b93d8b-b7a5-3d62-9308-088d8d889715 | -9.01171 | -67.71918 | 2024-10-21 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff50df1a-028f-3c9e-8014-e12ef67828d4 | -8.12573 | -63.87779 | 2024-10-21 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff8b1ff1-9440-37db-becc-12dbeaa2a847 | -8.12368 | -63.87368 | 2024-10-21 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddab5139-1dee-366b-a06f-c9ad978c832d | -8.12294 | -63.87889 | 2024-10-21 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8abca502-f193-3a9e-b975-b2b77591a3f1 | -8.12173 | -63.87719 | 2024-10-21 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be0884ac-a08c-31f7-944c-fe85f74441f9 | -7.87581 | -63.77836 | 2024-10-21 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ac48e22-e55d-3067-b3d3-9dadda593d8c | -7.87179 | -63.77777 | 2024-10-21 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15aa801d-47bd-3c02-bdd9-8ae084fe8b52 | -7.86727 | -63.78067 | 2024-10-21 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 077bebf1-fe4d-3afb-9fa3-4231cf2d6aa0 | -7.86325 | -63.78009 | 2024-10-21 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28099fb2-9573-3ce8-8b6b-19d1a2e50c15 | -3.10976 | -54.17498 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d5d6a58a-f18c-372d-9a8c-47f3524646fb | -3.10718 | -54.15821 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8234ed9c-b270-37b4-8183-a8ba641fb79a | -3.10609 | -54.16552 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| c75c2239-513d-3107-84dd-1469e845863b | -3.10578 | -54.15247 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76a8711c-0f3e-34cd-930f-bb1495578199 | -3.10503 | -54.17262 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 7776f605-3e7f-3297-a11f-fe32e386b7d7 | -3.10474 | -54.15974 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 385077f3-a703-36df-b8d6-2965e47f22a1 | -3.10403 | -54.17933 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 61b856b1-b7c9-3bd1-a9ad-888dc31c2ce0 | -3.1037 | -54.16708 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9e27a8ea-e94d-30c2-a6e3-154d257b17ae | -3.10308 | -54.18566 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| ab819d66-1af2-3b7f-a350-eec0b9351261 | -3.1027 | -54.17411 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 638fca76-8205-3092-b3a0-b5ca34461904 | -3.10223 | -54.14309 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05d43fbe-fd46-396c-99c2-34149130e715 | -3.10212 | -54.19212 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 709b7ae0-06aa-3479-8c38-ad875e5cf322 | -3.10175 | -54.18078 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 49a92fc3-f24b-3b2f-9376-384fc7d9fd98 | -3.10122 | -54.14992 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 772c03cb-bf4a-376e-9bbe-259b6218b0dc | -3.10083 | -54.18719 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0f3e39d4-d86b-3e9f-9481-82478b23dec0 | -3.10016 | -54.15704 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f5aaf9e-173b-36d6-8b1f-639eb9dc3d83 | -3.0999 | -54.19375 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bcaf76a0-a511-340d-8bb4-1d80c4866a60 | -3.0997 | -54.14454 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7692fb3-2561-31e9-a126-f291551aa39f | -3.09905 | -54.16443 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 2d29dbf3-c935-3309-989f-72458d0b94bd | -3.09873 | -54.15136 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75535d17-2514-329c-a7bd-920c0bc43f7d | -3.09798 | -54.17162 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 4244d696-c077-3d38-a0a0-7a5dd20198d7 | -3.09771 | -54.1586 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 3d13add7-9baa-39c1-82e7-39c109652d39 | -3.09697 | -54.17846 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| b49777d9-d85c-3384-bb42-3c8e8c7e2b2e | -3.09666 | -54.16596 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| eea56054-fd5f-3c61-a9c7-727e17a5d2d9 | -3.09598 | -54.18507 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 8be0c047-7261-3e37-b79b-a951224ea9b1 | -3.09565 | -54.17307 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| df4114fe-cc29-3761-b545-6f99d0656234 | -3.09513 | -54.1424 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b9730cf4-bf07-3dd6-a9de-a98fd2ffed51 | -3.095 | -54.19169 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 671c2309-35ee-3539-8a33-e2ca4cfbd564 | -3.09468 | -54.1799 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 345cf313-fe9d-3efc-8938-5c79ec505af8 | -3.09414 | -54.14902 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b35b3130-a76b-30aa-bb37-92be6c0f8e41 | -3.09401 | -54.1983 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cd80fc47-ba4f-33aa-8cbf-78ba7d694ba1 | -3.09374 | -54.18651 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 8f859271-6dcf-3b76-aea1-2c546e1d8768 | -3.09311 | -54.15596 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 647f8481-1a95-320b-8d83-acfa883ed892 | -3.0928 | -54.19315 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| d47a114e-8a16-3a71-84dc-18730cdd9731 | -3.0926 | -54.14384 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fcf2eb6-8639-3440-ae5f-e42ac28b3505 | -3.09204 | -54.16321 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| a9aa3297-9c43-3a95-b40b-87976cde6893 | -3.09186 | -54.19978 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c7896dc4-36c2-3a4a-abf2-3e952b9c94ad | -3.09166 | -54.1505 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 180eead9-df9d-3a9a-b689-858f331e4c66 | -3.09097 | -54.17041 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 45d827a1-465e-3dd9-b04d-86d32416a842 | -3.09067 | -54.15744 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 8b40368a-0b61-38cd-aafc-35a81d6273db | -3.08994 | -54.17735 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| ed2449d3-9b23-37fe-9a66-dee15d9850fe | -3.08966 | -54.16462 | 2024-10-21 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |


[Clique aqui para ver as próximas entradas](README60.md)
