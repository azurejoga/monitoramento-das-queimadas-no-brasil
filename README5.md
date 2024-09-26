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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d73a02c6-a266-3c28-9de4-1bdc5c561398 | -5.62 | -43.6261 | 2024-09-26 00:15:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 39.8 |
| cce2fc12-3b53-3040-bd59-10bbe9906307 | -6.5772 | -60.0437 | 2024-09-26 00:15:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 86f87faf-f065-3a26-bd5d-1835d7735576 | -6.7902 | -44.7296 | 2024-09-26 00:15:44 | GOES-16 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 53c7c807-f558-36ae-82a5-01565d8c50dc | -6.7839 | -59.3245 | 2024-09-26 00:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| ad0641f3-729f-366f-a90d-46de69023445 | -6.784 | -59.3052 | 2024-09-26 00:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.5 |
| e1831e0b-ed02-3f99-9a24-7b17f66f19c9 | -6.8024 | -59.3044 | 2024-09-26 00:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.0 |
| e655f015-d9b0-3079-9e84-56da03e2b385 | -6.8384 | -63.1457 | 2024-09-26 00:15:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 216426ca-b58a-34e1-8368-9ed8685a2aff | -6.8385 | -63.1269 | 2024-09-26 00:15:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 03463382-59f9-3be8-ab69-b3c38e5a7155 | -6.8568 | -63.1452 | 2024-09-26 00:15:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 5317de06-54cc-3bb9-b0ed-415ae35481e8 | -6.9305 | -63.1241 | 2024-09-26 00:15:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 0cd2d65f-fa81-361c-83a9-651ebba25e64 | -6.9306 | -63.1053 | 2024-09-26 00:15:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 83ed6337-fb0c-365a-a9f1-4fe7955557de | -6.9489 | -63.1236 | 2024-09-26 00:15:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| e9145d1e-103f-306c-af8a-c61ac3628e4c | -6.949 | -63.1048 | 2024-09-26 00:15:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 67e96aca-9b55-3dee-8a79-52ea07885d8b | -7.0912 | -46.4412 | 2024-09-26 00:15:46 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 8493f14f-069c-345d-b44b-cdd9253a7160 | -7.1099 | -46.4396 | 2024-09-26 00:15:46 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 9bb34ad9-14f2-3def-b4a8-3ba162824253 | -7.2905 | -61.106 | 2024-09-26 00:15:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 22b5a0da-9b76-3a80-bfa0-017568c6f2f7 | -7.2906 | -61.0869 | 2024-09-26 00:15:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 87c78fe3-3c76-3bfb-8027-ff2f709650a4 | -7.3089 | -61.1053 | 2024-09-26 00:15:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| f0c772a1-6ae5-3dd4-a05e-98a831abf5dd | -7.3637 | -55.5134 | 2024-09-26 00:15:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| a1ad3e61-98c5-3527-97df-7bd0158600db | -7.3639 | -55.4935 | 2024-09-26 00:15:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 5b000fed-4f43-3af5-b1dc-560c5db61c99 | -7.3823 | -55.5124 | 2024-09-26 00:15:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 93a9840e-616b-367b-97c4-d319d850531f | -7.3824 | -55.4924 | 2024-09-26 00:15:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 3e9eeede-226b-3522-a63a-b17eb6087911 | -7.5705 | -55.1617 | 2024-09-26 00:15:49 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| ae92b7a1-90bc-390c-ac79-be773e2a319b | -7.5889 | -55.1807 | 2024-09-26 00:15:50 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 09347e0a-15d8-36bb-ba6e-00d2caf7fec1 | -7.797 | -54.7263 | 2024-09-26 00:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 98cbac7b-7502-3b69-896b-54543af0a0ac | -7.8156 | -54.7252 | 2024-09-26 00:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.6 |
| bf30dbec-e517-3747-b30a-94880419ea64 | -8.0561 | -67.2657 | 2024-09-26 00:15:53 | GOES-16 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| ed1995d1-f836-3b61-93b7-9bd4bad67d51 | -8.0561 | -67.2472 | 2024-09-26 00:15:53 | GOES-16 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| bb08f2f4-292b-3e70-bdaf-d66d078f8bfa | -8.1572 | -61.3953 | 2024-09-26 00:15:53 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 5eb54e14-78b4-3964-b064-f33795499ca8 | -8.3153 | -55.0157 | 2024-09-26 00:15:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 08be0c60-7769-338e-94bf-492d5afad067 | -8.3155 | -54.9956 | 2024-09-26 00:15:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| d37cd3fe-6605-307f-9986-68e1adf22b83 | -8.5187 | -55.1834 | 2024-09-26 00:15:55 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| d1d22184-7e92-35af-b034-e1b36377f5f2 | -8.5542 | -63.1814 | 2024-09-26 00:15:55 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 155acca5-22b5-3580-acdd-57b38017135f | -8.7085 | -54.8083 | 2024-09-26 00:15:56 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 19e9f9df-6ce4-3348-99f0-120e298c1115 | -8.7087 | -54.7881 | 2024-09-26 00:15:56 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 043bd13b-5f0e-3139-969e-b02edec9b831 | -8.8098 | -58.2172 | 2024-09-26 00:15:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 82bd8d0c-51f6-31fe-b6f1-999e17eafeb1 | -8.8292 | -63.7179 | 2024-09-26 00:15:57 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 62577d62-5338-3dcd-8efc-91c050412ac6 | -8.8293 | -63.699 | 2024-09-26 00:15:57 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 2d379a5e-31a5-3131-9101-222c83985797 | -8.9301 | -57.1488 | 2024-09-26 00:15:57 | GOES-16 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 736cb375-3ac7-3510-84db-91be4dbd4f37 | -8.9244 | -67.1889 | 2024-09-26 00:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 8bb24419-00e9-3e05-944d-19fcf4114aa5 | -8.968 | -62.1415 | 2024-09-26 00:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 9881e5c1-1de8-3dc6-a571-0202ab02bd56 | -9.033 | -67.8714 | 2024-09-26 00:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 9e2495b7-39bc-3f9e-853c-01a8abf8808d | -9.0657 | -61.3743 | 2024-09-26 00:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| b829c3bc-327d-345c-89ff-bd9530f74c1c | -9.086 | -61.1245 | 2024-09-26 00:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 66b62541-a791-3069-b8c6-2eb9de41017f | -9.103 | -61.3534 | 2024-09-26 00:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| defb632b-33e6-380e-b1b7-d5a6a2d71eb2 | -9.1032 | -61.3343 | 2024-09-26 00:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 125.7 |
| b21307ac-b4bf-3499-a30d-82696760c933 | -9.1033 | -61.3152 | 2024-09-26 00:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| d8542b36-fdd1-3ea6-a665-0d6b1b5901d8 | -9.1035 | -61.2769 | 2024-09-26 00:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 53da462c-0520-3f58-b85a-42ae74b74594 | -9.1046 | -61.1237 | 2024-09-26 00:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 0095678d-2e31-3c6f-a4af-38a82de65b5f | -9.1216 | -61.3526 | 2024-09-26 00:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 176.0 |
| 92a40463-4951-39f2-bc97-d981793d1389 | -9.1217 | -61.3334 | 2024-09-26 00:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 164.0 |
| d1a5b049-a5a0-3577-a457-9567a1295ea2 | -9.1219 | -61.3143 | 2024-09-26 00:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 65130933-17e0-3a7f-987f-ea586d969e20 | -9.1349 | -65.564 | 2024-09-26 00:15:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 3ce56885-4ee9-326d-9ef1-55530412f244 | -9.2417 | -66.5673 | 2024-09-26 00:15:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 0110b686-f547-306c-96c6-653858133bca | -9.2602 | -66.5668 | 2024-09-26 00:15:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| ba4713c4-9482-3615-9aff-eba4f4ea74c9 | -9.2603 | -66.5482 | 2024-09-26 00:15:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 8808554b-3a47-32fa-8d19-16d6876d5eb2 | -9.3801 | -56.8631 | 2024-09-26 00:16:00 | GOES-16 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 7e3ac5d7-6c77-33f3-aa12-8f4a18fa13cb | -9.5827 | -50.1584 | 2024-09-26 00:16:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 3065a5d0-edc7-3f4e-a1b1-562d9f580f2b | -9.6015 | -50.1566 | 2024-09-26 00:16:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 171.9 |
| 808f658d-9a56-3f87-9a40-c98bc3e86aa9 | -9.6018 | -50.1352 | 2024-09-26 00:16:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| e8aed6a4-9f4c-30ee-849f-ddd881ff3fd8 | -9.8058 | -53.5869 | 2024-09-26 00:16:02 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| e736fa09-93c9-3c31-abac-283f51500fab | -9.806 | -53.5664 | 2024-09-26 00:16:02 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 5cb5d90c-c5d2-3dcf-b5a9-fea48df79398 | -9.8083 | -68.8152 | 2024-09-26 00:16:03 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 77c4218a-544f-3c06-93e1-2f69671ea3ab | -10.0506 | -68.5875 | 2024-09-26 00:16:04 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 4989dfb3-3e15-391a-b4e1-fff9242d71f4 | -10.0692 | -68.5871 | 2024-09-26 00:16:04 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 56.3 |
| b5918335-97d1-3e63-a69b-4b73cd3ba357 | -10.3674 | -53.7652 | 2024-09-26 00:16:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| b8c17e01-faac-37db-b4bf-bdee2cd60f21 | -10.3713 | -58.9056 | 2024-09-26 00:16:05 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| e4d66de8-072f-3639-9ae4-7f34a8beb761 | -10.39 | -58.9044 | 2024-09-26 00:16:06 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 2315c8ae-5ccc-38f1-a384-181d5a2673d5 | -10.448 | -53.3058 | 2024-09-26 00:16:06 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 82564988-6dfa-3258-b256-36d732dd2942 | -10.3882 | -67.8737 | 2024-09-26 00:16:06 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 84.5 |
| b99644f1-a99e-3845-b166-36465933301e | -10.4068 | -67.8732 | 2024-09-26 00:16:06 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 63.8 |
| ce8b1765-e8da-3ef3-8ece-c898c2489411 | -10.9924 | -44.4383 | 2024-09-26 00:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 04bfb520-caa8-30bd-94ff-3437a3a4a7b6 | -10.9928 | -44.415 | 2024-09-26 00:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 54aae5a9-c7a0-3252-a77f-0022886f9b6b | -10.8915 | -57.4521 | 2024-09-26 00:16:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 215f00a0-8119-35a5-bcb0-66f5f6fec094 | -10.8917 | -57.4322 | 2024-09-26 00:16:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 124.1 |
| a3eb91a2-b4f1-30a1-82dc-fa52f1a58449 | -10.8919 | -57.4124 | 2024-09-26 00:16:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 367c6697-efde-3219-aad4-02ae263db973 | -10.9264 | -54.2692 | 2024-09-26 00:16:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 0507bb73-bb90-3f58-bb65-c6f3e7e166d4 | -10.9105 | -57.4308 | 2024-09-26 00:16:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 208.0 |
| 2a1b8ffe-97ff-3f8e-afc0-f0444f1ec0ca | -10.9107 | -57.411 | 2024-09-26 00:16:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 156.2 |
| bd03ca26-f0b6-36ab-a070-354bd37030b2 | -10.9453 | -54.2676 | 2024-09-26 00:16:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 4c644555-157f-3f21-9370-785d42e15ef7 | -11.1845 | -54.7769 | 2024-09-26 00:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 865f88fa-0f67-3c14-b35c-c183e0b0cbec | -11.2034 | -54.7752 | 2024-09-26 00:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 5ae84c5e-b467-36f6-8a0b-9f1b355d9233 | -11.2036 | -54.7548 | 2024-09-26 00:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 1409fd51-d363-3fc2-854d-1f725ee5cbbe | -11.2599 | -65.299 | 2024-09-26 00:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 117.2 |
| f3b58738-dfe0-3850-b1ba-41ad3853b169 | -11.26 | -65.2801 | 2024-09-26 00:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 156.4 |
| 4ddeac65-366a-364a-9551-9fbb24f637cc | -11.5972 | -60.3475 | 2024-09-26 00:16:12 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| c30c352d-e7d2-3c91-afd2-3db3a155c2f8 | -11.616 | -60.3463 | 2024-09-26 00:16:13 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 46.4 |
| d1fb2cae-db62-38cd-8dfe-4a0bae70594b | -11.8422 | -49.635 | 2024-09-26 00:16:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| c4e2a26c-0754-3aae-b6df-47ad04ef529f | -12.2175 | -45.5074 | 2024-09-26 00:16:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 13234d46-cbb1-3d0c-a240-17d97a6e2436 | -12.2179 | -45.4844 | 2024-09-26 00:16:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 9cd4256a-a562-39c7-b825-4b9ef24457ac | -12.2367 | -45.5045 | 2024-09-26 00:16:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 3202fe5b-4ac8-35d6-8407-9e0c6cb6ea32 | -12.2371 | -45.4815 | 2024-09-26 00:16:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| ca5f505f-bea2-3c97-8652-225501cea995 | -12.5085 | -53.498 | 2024-09-26 00:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 82770cb9-d324-3a94-a7f4-480e5c4371d4 | -12.5088 | -53.4772 | 2024-09-26 00:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 615f1f1e-e40f-3aca-b5e7-92e955359cb8 | -12.5273 | -53.5168 | 2024-09-26 00:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 11e3ae3c-9e51-3ab2-b5c7-7a4b81e30bf1 | -12.5276 | -53.496 | 2024-09-26 00:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 200.6 |
| a315178b-6370-39fc-9a65-b38e84c6bd80 | -12.5279 | -53.4752 | 2024-09-26 00:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 13b23c01-1826-33cd-a411-633c9385efb6 | -12.5467 | -53.494 | 2024-09-26 00:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 420d0d83-f49e-35b0-ae97-d5fda616ecbe | -12.7709 | -51.2403 | 2024-09-26 00:16:18 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 4067b342-9faf-35e5-b0c6-0038d07a93f4 | -12.7713 | -51.2189 | 2024-09-26 00:16:18 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |


[Clique aqui para ver as próximas entradas](README6.md)
