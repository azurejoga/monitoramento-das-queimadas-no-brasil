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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f36f3b0b-c884-347e-b7f3-547070d21c62 | -20.12456 | -44.27939 | 2024-09-26 03:21:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3a09d437-db1f-3e65-ac5c-66bfbffa8eb1 | -20.12403 | -44.27839 | 2024-09-26 03:21:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7407f0fe-0ce6-3cd0-ad0b-33cd031c0ca5 | -20.12391 | -43.44564 | 2024-09-26 03:21:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.1 |
| ba4ddbae-cc37-34d5-b2e1-a08d17209c54 | -20.11909 | -43.43984 | 2024-09-26 03:21:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 2e768634-780f-3af9-90da-537d5165695d | -20.1183 | -43.44333 | 2024-09-26 03:21:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.1 |
| b4dad111-d94f-3076-bcf2-c3da3e1f7fc9 | -20.10337 | -43.84594 | 2024-09-26 03:21:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 02324134-2c16-3432-a2e1-1f5c223635f0 | -20.09724 | -43.84521 | 2024-09-26 03:21:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 80fedca1-9af5-3364-9fca-1fef1d442a72 | -2.6785 | -57.531 | 2024-09-26 03:25:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| bb583136-33fb-34a9-ad46-36ba954b1fbc | -2.6968 | -57.5307 | 2024-09-26 03:25:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 33e52cf8-7ce6-3086-9431-fd35129081ed | -3.9208 | -46.4459 | 2024-09-26 03:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 80e83151-6967-392f-8abc-5492c6d2c64e | -6.8024 | -59.3044 | 2024-09-26 03:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| b2aaa331-772d-3f73-9be2-e49664a6d252 | -6.949 | -63.1048 | 2024-09-26 03:25:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 5b91d67e-e3c3-3e08-ad0c-b849f9020f7b | -6.9306 | -63.1053 | 2024-09-26 03:25:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 9e5af998-bd4e-3cc3-827b-982b64303c60 | -6.9305 | -63.1241 | 2024-09-26 03:25:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 63bb02a7-be78-34cc-9616-efb63f0fe407 | -7.3824 | -55.4924 | 2024-09-26 03:25:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 188.8 |
| 7c06b1b1-43c2-31f5-b551-d69df1c9c1b4 | -7.3823 | -55.5124 | 2024-09-26 03:25:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 286.0 |
| 283de1ed-efa0-3ec8-a694-b876e752a4a0 | -7.3821 | -55.5324 | 2024-09-26 03:25:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 11195c1a-d82a-3d7d-afde-ad4903c80a0c | -7.3639 | -55.4935 | 2024-09-26 03:25:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 150.0 |
| f5899dec-4ad9-3f2b-98b4-a90c1c8e487e | -7.3637 | -55.5134 | 2024-09-26 03:25:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 235.2 |
| 61efbdcd-4d78-3067-8d96-551c26bc4d6e | -7.3636 | -55.5334 | 2024-09-26 03:25:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| ddbc9600-f9fb-349f-9b85-98949552a9cc | -7.8341 | -54.724 | 2024-09-26 03:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 05c78d7f-5f55-34ee-8821-606049ada446 | -7.834 | -54.7442 | 2024-09-26 03:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 2b00a413-7c03-3085-9eeb-3cb1481202f0 | -7.8156 | -54.7252 | 2024-09-26 03:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 170.1 |
| fa3abdd4-054b-3e09-bcb8-b495a8cbff56 | -7.8154 | -54.7453 | 2024-09-26 03:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| b1ebeea9-4c80-3d37-b146-174885164166 | -7.797 | -54.7263 | 2024-09-26 03:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| a90abb05-394c-3d34-8def-9d460df877c5 | -8.1757 | -61.3946 | 2024-09-26 03:25:53 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 70fef6c7-d0a2-3b58-88c5-971d443f77f1 | -8.1394 | -61.2817 | 2024-09-26 03:25:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 5594a867-4ac4-3f5f-803c-4332d4923cb3 | -8.8098 | -58.2172 | 2024-09-26 03:25:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| d71fa4dd-c33c-3e79-b5f0-3a77bed572b5 | -9.1046 | -61.1237 | 2024-09-26 03:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 8f092f9d-934a-3ff0-b122-f51cea1c9398 | -9.086 | -61.1245 | 2024-09-26 03:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| ce889bf5-a011-3345-bb21-56e995cc29d1 | -9.3462 | -51.0704 | 2024-09-26 03:25:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| c86d0bc3-f305-3d07-a4ad-fcf3cc95c927 | -10.0515 | -53.4432 | 2024-09-26 03:26:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 73d8984f-f687-3a67-a528-42501d90e0d7 | -10.0513 | -53.4638 | 2024-09-26 03:26:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| ad6af784-3e3b-324b-b5f8-2a31d60378ee | -10.0327 | -53.4448 | 2024-09-26 03:26:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 758032e0-aaef-32fc-9129-9a29ffd0dc0b | -10.0324 | -53.4654 | 2024-09-26 03:26:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 9a38573a-115e-3160-965a-46455525e678 | -10.0322 | -53.4859 | 2024-09-26 03:26:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 9d921109-b260-391b-90a8-3789764ebd52 | -10.0136 | -53.467 | 2024-09-26 03:26:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 6ff4fdfd-14cf-3d4f-8629-5e5ab07f604b | -10.8352 | -45.8843 | 2024-09-26 03:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 63f0fe1a-1b89-3313-9030-193301aee1fd | -11.2412 | -45.5334 | 2024-09-26 03:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 1259b388-4919-37ad-b15a-cda6c673a5ee | -11.222 | -45.536 | 2024-09-26 03:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 155.5 |
| b926200f-4118-37fc-bf4b-9992667b2f46 | -11.2217 | -45.559 | 2024-09-26 03:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| d31a801c-a9f6-383e-81d5-7201f4b70f5e | -11.2029 | -45.5387 | 2024-09-26 03:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 4a256c5d-07eb-369e-8f9d-1cf44f5da4fb | -11.2223 | -54.7735 | 2024-09-26 03:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 923e505a-f530-3f1e-b12e-5b14f5ac77cc | -11.2036 | -54.7548 | 2024-09-26 03:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 04e124ba-f254-3f8d-88f9-2622e05a761b | -11.2034 | -54.7752 | 2024-09-26 03:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 362.1 |
| 9c6774ab-d0fc-3c72-873f-1ee2ebe65b90 | -11.2031 | -54.7956 | 2024-09-26 03:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 265.7 |
| 4d4eb7a3-b8ad-320d-8616-da4571c30b0e | -11.1845 | -54.7769 | 2024-09-26 03:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 76741d2a-9135-3509-a8f4-05ad86a81042 | -11.2788 | -65.2793 | 2024-09-26 03:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 32b26d86-5c9b-3bf3-99b0-5526a3e0b49b | -11.2786 | -65.2982 | 2024-09-26 03:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 36abfa39-7d9f-30a3-859c-b6d4e44284dc | -11.26 | -65.2801 | 2024-09-26 03:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 138.9 |
| 5f3b0fc1-8407-3eb5-a0db-2cf8fe987891 | -11.2599 | -65.299 | 2024-09-26 03:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 136.0 |
| e4a0f7b0-0643-3a6a-b7db-7c760d1896b0 | -11.2413 | -65.2809 | 2024-09-26 03:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 79589897-0031-3b6a-987c-be27e208717e | -11.2412 | -65.2997 | 2024-09-26 03:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 74173b2a-059f-34cc-afe3-149aa9685519 | -12.2367 | -45.5045 | 2024-09-26 03:26:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 4282357c-19ce-34cb-a8e2-58708cc11297 | -12.2175 | -45.5074 | 2024-09-26 03:26:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 82dca839-9c9c-3030-8624-25770bb20bae | -12.5467 | -53.494 | 2024-09-26 03:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 820a5d74-3570-3f57-89b6-f8e0f31d54be | -12.5464 | -53.5147 | 2024-09-26 03:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 5c567dce-55f6-3e8d-b2b3-b503692870b3 | -12.5279 | -53.4752 | 2024-09-26 03:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| dc4ea886-9ba2-3515-9831-6ebaf4e37824 | -12.5276 | -53.496 | 2024-09-26 03:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 213.0 |
| 7280eac1-82b0-3763-9c52-128322ca4ba7 | -12.5273 | -53.5168 | 2024-09-26 03:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 8eea6fc9-71fd-32d8-94ed-51b1026c4618 | -12.5218 | -48.9173 | 2024-09-26 03:26:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| f9293e7e-040d-30eb-af14-017efdeb5418 | -12.5026 | -48.9198 | 2024-09-26 03:26:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 622f8f0a-2d83-3ebc-9fc5-b719daa3e23f | -12.841 | -62.7067 | 2024-09-26 03:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 35eb5119-4c03-385c-8e17-feb8ea49ab4f | -14.8824 | -51.4992 | 2024-09-26 03:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 74cdf1ec-3bae-3f53-9722-abe40d718ccf | -14.9544 | -57.9413 | 2024-09-26 03:26:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 3da71fe8-aed9-33e8-b5b9-36250c02c3c7 | -14.9348 | -57.9634 | 2024-09-26 03:26:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 237f19e8-edb7-31c2-8e31-07f947198061 | -14.9153 | -57.9854 | 2024-09-26 03:26:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| c0ff0783-630d-3eb8-ae88-4511f821f9f8 | -14.896 | -57.9873 | 2024-09-26 03:26:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| fc5c1410-a519-3419-8841-f101ab956191 | -16.118 | -51.9867 | 2024-09-26 03:26:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 5ce95624-13e0-3e46-8f4c-cd8d6f233ac7 | -16.1176 | -52.0082 | 2024-09-26 03:26:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 30d650ea-a007-3844-813e-e14173ded761 | -16.0985 | -51.9896 | 2024-09-26 03:26:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 504cbfcb-b662-3e6d-9598-92cb72c7de82 | -16.098 | -52.0111 | 2024-09-26 03:26:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| a79d9476-2f18-388e-a22b-9af4cbe4b857 | -20.608 | -51.4986 | 2024-09-26 03:27:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 141.9 |
| 4c5c48ad-98c8-3a2d-adb7-3fe4ae10d9d9 | -20.6074 | -51.5209 | 2024-09-26 03:27:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 138.5 |
| bef9c72e-713e-3df8-90eb-e0063149e966 | -20.6279 | -51.5169 | 2024-09-26 03:27:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.1 |
| 54ea7ec0-9b1e-3c45-8b1f-787ba35e0240 | -21.9381 | -48.5453 | 2024-09-26 03:27:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 217f21c3-42ca-3343-b900-1787eddbf3b7 | -21.9374 | -48.5688 | 2024-09-26 03:27:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 5f67a9a2-7b4f-3856-af56-ae7a6bbf78d6 | -2.358 | -47.5989 | 2024-09-26 03:35:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 7d80a760-9ae7-30b5-bb73-f0575451872f | -2.6785 | -57.531 | 2024-09-26 03:35:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| a58492e7-1e08-3dc4-83ee-a5bcdb1937f8 | -2.6968 | -57.5307 | 2024-09-26 03:35:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 5cbae9b7-f428-3fa9-998b-88c969dada7e | -2.8795 | -51.6695 | 2024-09-26 03:35:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 367ade3f-89d6-3a06-9a9d-d9437104bab8 | -3.5673 | -50.3794 | 2024-09-26 03:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 9ac003ce-ad06-33c9-8c86-46973be2ca19 | -3.9208 | -46.4459 | 2024-09-26 03:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 5d9aa3d6-dda4-3707-8814-4310c947d4b9 | -6.8024 | -59.3044 | 2024-09-26 03:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 38375696-381b-353a-a221-5b2f6b21d2fc | -6.9305 | -63.1241 | 2024-09-26 03:35:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 308565f3-67bd-35b9-b084-93469856442e | -6.9306 | -63.1053 | 2024-09-26 03:35:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 50806c46-4c48-39e2-a851-0e2f0edc68ea | -6.949 | -63.1048 | 2024-09-26 03:35:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 1d75ae99-391d-3fdc-82c5-2577864f7ec5 | -7.2905 | -61.106 | 2024-09-26 03:35:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 96b5abba-a2ea-308b-9629-d99f6b534c9f | -7.3636 | -55.5334 | 2024-09-26 03:35:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 53680511-e139-30af-bcf6-0641c0f624fe | -7.3637 | -55.5134 | 2024-09-26 03:35:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 319.7 |
| 84f1539c-6fbc-32b4-bc0a-8b3da72ed921 | -7.3639 | -55.4935 | 2024-09-26 03:35:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 154.1 |
| aed5f83f-9638-3955-9897-a5f9c8aa8782 | -7.3823 | -55.5124 | 2024-09-26 03:35:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 178.6 |
| c1c642c1-ee1c-302b-96c9-8ebd0fc57cdd | -7.3824 | -55.4924 | 2024-09-26 03:35:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 131.5 |
| 8efecb1f-8eaf-394e-822e-2d49f7debeb6 | -7.797 | -54.7263 | 2024-09-26 03:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| e87b9537-4a67-3b82-b4f0-08c993cba0ec | -7.8154 | -54.7453 | 2024-09-26 03:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 141.8 |
| 9aeea484-9f20-34b5-bb67-433464eabc66 | -7.8156 | -54.7252 | 2024-09-26 03:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 174.2 |
| 21469b1f-2e40-3be4-92d9-dd2e2d0c6b08 | -8.1394 | -61.2817 | 2024-09-26 03:35:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| b06f1df6-4a37-34d8-9461-e7a448332a73 | -8.1572 | -61.3953 | 2024-09-26 03:35:53 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 5d69be51-7819-30e2-89e7-8419a49e9410 | -8.3155 | -54.9956 | 2024-09-26 03:35:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 2f48c3fe-8a56-3195-9f55-e55417575688 | -8.8098 | -58.2172 | 2024-09-26 03:35:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |


[Clique aqui para ver as próximas entradas](README54.md)
