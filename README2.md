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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3c8f0fe-4b76-3ecd-9aa4-2a3c258bde8c | -8.4082 | -44.0303 | 2025-12-13 00:38:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fab98af2-b25f-3e44-8a70-83d26126140e | -1.7916 | -46.053299 | 2025-12-13 00:38:00 | METOP-C | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d5c23397-643e-3c13-b249-cc325e8391c9 | -3.2103 | -41.856201 | 2025-12-13 00:38:00 | METOP-C | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 931771f5-82e2-3516-92e8-f6c7a24f2b13 | -8.0367 | -43.118301 | 2025-12-13 00:38:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 745e6df4-6a23-336f-8aa1-8c36634a5bea | -3.0201 | -47.086498 | 2025-12-13 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 424475cb-8c37-3356-add2-3670989f53a1 | -3.3056 | -43.5242 | 2025-12-13 00:38:00 | METOP-C | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26fd90b4-aefa-36cc-ba5c-1f6174ddf365 | -5.0712 | -43.668201 | 2025-12-13 00:38:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 14e3aea6-0841-3aac-a7a8-1425d5afa535 | -3.2072 | -41.8433 | 2025-12-13 00:38:00 | METOP-C | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2adb20ac-5f0a-3275-99f9-28487160b3ed | -2.7805 | -45.7812 | 2025-12-13 00:38:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f9652e35-7ce7-3500-9a12-85e88026737a | -3.8242 | -49.699501 | 2025-12-13 00:38:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 842a1f0c-2950-38a5-951e-9c2864b9513c | -2.5431 | -45.202099 | 2025-12-13 00:38:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bef9be61-b6dc-3352-a74f-b5bd7abb3edf | -3.4536 | -44.728699 | 2025-12-13 00:38:00 | METOP-C | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 475b8505-460a-3a76-b272-cb89781b7344 | -2.0919 | -45.613098 | 2025-12-13 00:38:00 | METOP-C | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f18f91ee-0513-307a-85c5-fd648e8b6a7e | -8.0247 | -43.111301 | 2025-12-13 00:38:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c6c9c1d2-4bd8-3345-b524-460fde30374b | -3.2418 | -47.242401 | 2025-12-13 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47793f54-26b1-39b8-bf6a-4aa9b5064719 | -3.4342 | -51.206001 | 2025-12-13 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c62bdb96-cbfb-3f7f-9ce8-c7179257be2d | -2.4318 | -51.9142 | 2025-12-13 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 253f4dbb-dc3e-3c93-8006-19d05ae8db5f | -8.0202 | -43.0928 | 2025-12-13 00:38:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bb4babd9-7b00-3fe8-a797-aca587627191 | -3.6466 | -49.507599 | 2025-12-13 00:38:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a81029a8-1d47-3f01-bede-5a2c7922e654 | -1.8942 | -45.427101 | 2025-12-13 00:38:00 | METOP-C | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9b1dc73c-8e54-37f5-8d97-f7a93c78a94e | -0.6969 | -49.2337 | 2025-12-13 00:38:00 | METOP-C | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7e2c62e-0c29-3df4-b095-c507f8b252a4 | -2.4367 | -51.9274 | 2025-12-13 00:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 066ec5dc-a39d-356d-bf28-2aba2cebb0e9 | -2.4183 | -51.9278 | 2025-12-13 00:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| de3827d6-afac-3132-bb61-515252c4cdb6 | -1.8979 | -54.3309 | 2025-12-13 00:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 4d4fe5f2-2129-3a91-aced-72770202f5dc | -3.1822 | -41.8448 | 2025-12-13 00:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 8d2ee2ff-d5b6-340b-bce5-cb70f341dcdf | -3.2009 | -41.844 | 2025-12-13 00:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 195.2 |
| c8e83409-aa26-3fe9-9559-853e58b97f72 | -1.8978 | -54.3509 | 2025-12-13 00:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 52681616-8e9d-3253-80a7-41ef10b83bcd | -3.2196 | -41.8431 | 2025-12-13 00:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 78d1a279-9cc9-3364-859d-bb6b0697cf8e | -3.182 | -41.8687 | 2025-12-13 00:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 31.2 |
| f9e4a0ea-4342-3722-8ad7-7c48583175af | -3.2194 | -41.867 | 2025-12-13 00:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 807f22ab-287b-34cc-9294-cdb9111bb9d9 | -3.2007 | -41.8678 | 2025-12-13 00:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 151.7 |
| b9892f7c-b996-349b-b50b-28345602a07a | -3.2196 | -41.8431 | 2025-12-13 00:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 48.8 |
| c2ee2ef0-0195-325d-99a7-853f0b15f70f | -3.2194 | -41.867 | 2025-12-13 00:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| e32f40ed-f08d-38ba-8476-7c285b8b54a4 | -3.2009 | -41.844 | 2025-12-13 00:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 27dfe2cc-1e9b-3c3e-9026-be7c604e7c54 | -1.8979 | -54.3309 | 2025-12-13 00:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 69689785-33ae-3f07-9030-92e4563c0e6c | -1.8978 | -54.3509 | 2025-12-13 00:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 684342cf-f478-37ed-960e-fda65f7b3382 | -3.2007 | -41.8678 | 2025-12-13 00:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 9cfcec84-3e33-3f2c-86c7-bc0f62291545 | -3.2009 | -41.844 | 2025-12-13 01:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 122.0 |
| e3dba8cc-6c1e-3ff3-9513-b996bf0afa89 | -3.2196 | -41.8431 | 2025-12-13 01:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 47c32adc-f473-35cc-8de6-33aad1050b48 | -1.8978 | -54.3509 | 2025-12-13 01:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| cc121f58-3400-3022-bfed-46daef7c613d | -3.2007 | -41.8678 | 2025-12-13 01:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 7103cdb2-ac47-3715-b81c-62c5f3bf2dcb | -3.1822 | -41.8448 | 2025-12-13 01:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 33.7 |
| a5a40a56-4c70-38b7-9d6f-44b5f68860e3 | -3.182 | -41.8687 | 2025-12-13 01:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 2d5d24a4-102f-36dd-8b5b-53606977bd2b | -1.8979 | -54.3309 | 2025-12-13 01:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 45c87523-fed2-3ea8-98cc-08ad450bf06c | -3.2194 | -41.867 | 2025-12-13 01:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 55cc0ec2-8a66-3a1b-8583-522a909035a2 | -3.2196 | -41.8431 | 2025-12-13 01:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 69.9 |
| f7ff0b53-fdd1-3122-8247-48e1503c4493 | -3.2007 | -41.8678 | 2025-12-13 01:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 183.5 |
| 5b0c91ae-2d2c-3949-9c59-cb4d68a50bc2 | -3.2009 | -41.844 | 2025-12-13 01:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 183.8 |
| c6def1b2-729c-31f4-95ed-e44fdec57088 | -3.182 | -41.8687 | 2025-12-13 01:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 49.2 |
| f62e6606-40ea-3152-8841-12fe279e17b5 | -3.2194 | -41.867 | 2025-12-13 01:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| ef37b96c-b936-37ed-9acc-2ef618cc9b21 | -3.1822 | -41.8448 | 2025-12-13 01:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 43.2 |
| c80fcd4b-42b4-3e67-ad27-19699ab0bc96 | -3.2194 | -41.867 | 2025-12-13 01:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| fe549101-4296-3d62-9cee-03148df78efb | -3.182 | -41.8687 | 2025-12-13 01:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 41210368-3237-32ea-b571-f2e7ed4b1680 | -3.2196 | -41.8431 | 2025-12-13 01:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 3644cb3a-ae19-3f32-9314-316f8e9cc324 | -2.487 | -47.7692 | 2025-12-13 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 26b56f11-3df8-39bb-ad55-20c53089d686 | -3.1822 | -41.8448 | 2025-12-13 01:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 83b3af56-bdf0-3f5e-b94d-9e00940e12e7 | -3.2009 | -41.844 | 2025-12-13 01:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 246.3 |
| 7b89c01d-9b61-3c89-876e-b83f3ff0c991 | -3.2007 | -41.8678 | 2025-12-13 01:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 233.8 |
| aa63bb47-d298-3e83-9c27-dc1a1e4131f9 | -3.201 | -41.8201 | 2025-12-13 01:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 31.8 |
| bc7ba3c7-6be9-3998-9c7b-3069d18f55b0 | -2.487 | -47.7692 | 2025-12-13 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 598f6b08-a9f4-35f0-ace2-3ce8ac68f99b | -3.2009 | -41.844 | 2025-12-13 01:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 261.9 |
| 42423990-f321-3129-aa2c-27cca02f9363 | -3.2194 | -41.867 | 2025-12-13 01:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 422497b6-1032-3ccb-ad7a-cbd5b38aef93 | -8.0513 | -43.1001 | 2025-12-13 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| bbdb1af1-4994-3f06-be68-1608b7d51083 | -3.1822 | -41.8448 | 2025-12-13 01:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| b3462dc0-9a90-38e9-9d7e-6c5e96e63ec3 | -8.0324 | -43.1022 | 2025-12-13 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.4 |
| 601d163b-62af-3da8-aa30-09d8d2dc48d1 | -3.182 | -41.8687 | 2025-12-13 01:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 201c7dda-a879-338e-9da1-35446e9924f1 | -2.4869 | -47.7909 | 2025-12-13 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| a20c1b7f-a56d-36ce-8cfa-25d657f0645b | -3.2007 | -41.8678 | 2025-12-13 01:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 205.9 |
| ebd1ccb3-79f6-37ba-a06b-81d3d9aa9976 | -3.2196 | -41.8431 | 2025-12-13 01:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 263d2b8c-78b0-3bb8-8d0a-1a8f9027aeb6 | -2.4869 | -47.7909 | 2025-12-13 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| a73f7362-314a-3d70-a446-4c629977b75f | -3.2196 | -41.8431 | 2025-12-13 01:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 0363054d-459b-3cf0-804d-ccbb2a2dbdfc | -3.2194 | -41.867 | 2025-12-13 01:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| b15ffd71-b092-3cfc-8e3e-d20a40790119 | -3.2009 | -41.844 | 2025-12-13 01:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 270.1 |
| 59866ea2-d51a-37bd-bbf1-f004f0461288 | -9.8542 | -36.2465 | 2025-12-13 01:40:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 157.2 |
| d0074d65-fc6e-3a07-ba00-fadb27adb21c | -3.2007 | -41.8678 | 2025-12-13 01:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 187.1 |
| b0a88533-f432-3d92-984d-e935c09f43a6 | -9.8735 | -36.2432 | 2025-12-13 01:40:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 82.5 |
| 81f4f5ef-0086-3820-85ff-de617eef0e1a | -2.487 | -47.7692 | 2025-12-13 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| b30dc3f7-3bc9-3760-8796-383fe0040866 | -3.1822 | -41.8448 | 2025-12-13 01:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 770754c1-4b0a-30cf-affe-55d21d4544ef | -3.182 | -41.8687 | 2025-12-13 01:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| bbf4ff2f-de4d-3e51-b27c-1150ef871b4f | -3.2194 | -41.867 | 2025-12-13 01:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 82d2d753-4ee4-367c-88ba-32d45d864278 | -3.2009 | -41.844 | 2025-12-13 01:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 266.7 |
| 90156a87-caa2-380c-b98d-dca126a17dbc | -3.2196 | -41.8431 | 2025-12-13 01:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 4fc79433-3348-3bec-9ec9-46c13cd9fe71 | -2.487 | -47.7692 | 2025-12-13 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 4aa311e5-6701-328b-9a62-bf32a8d72ba6 | -3.1822 | -41.8448 | 2025-12-13 01:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| d3c135a2-1cc3-3bae-9989-da58781649c7 | -2.4869 | -47.7909 | 2025-12-13 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| f11cd2aa-a192-3d58-b8f6-685f215e5159 | -3.182 | -41.8687 | 2025-12-13 01:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 9da0ece2-12d8-3043-826c-ba4c41d48312 | -3.2007 | -41.8678 | 2025-12-13 01:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 194.3 |
| 3578a3f1-85e3-3002-bd78-2fdff71a11df | -2.487 | -47.7692 | 2025-12-13 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 2655d985-8168-3f84-99ec-cb0db73c7eae | -8.0327 | -43.0786 | 2025-12-13 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| dd68d98d-222e-34b6-9eff-c0d83b8945b9 | -9.878 | -35.999 | 2025-12-13 02:00:00 | GOES-19 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 84.1 |
| 725c3289-fba8-3f6c-9ccb-1a0928bbb766 | -3.2007 | -41.8678 | 2025-12-13 02:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 274.3 |
| 9ac333c5-6ce7-3a7a-8e5f-e08e34059b54 | -8.0324 | -43.1022 | 2025-12-13 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 302.3 |
| 77e0e805-24fb-3e61-8c4d-3904f4a6cc44 | -8.0321 | -43.1257 | 2025-12-13 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 160.7 |
| 80417e7c-e4a8-31b0-9bfc-96a8cebe637d | -3.2196 | -41.8431 | 2025-12-13 02:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 5f5528e3-cca6-3c60-be0b-bbb56dfd77f5 | -3.2009 | -41.844 | 2025-12-13 02:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 251.3 |
| 933d8308-0525-3431-8d15-6edcb2be6770 | -3.182 | -41.8687 | 2025-12-13 02:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 54.7 |
| b92c10b5-f3ab-34b9-9777-701a1d14a951 | -3.2194 | -41.867 | 2025-12-13 02:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| e3f6c524-5224-3c09-aa77-8bfd18d108a0 | -8.051 | -43.1237 | 2025-12-13 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| f79214cf-9590-3af0-983f-ef8f94f15549 | -8.0513 | -43.1001 | 2025-12-13 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 140.7 |
| 8b773a5f-c9ff-3da8-855f-4a6ce35eb078 | -3.1822 | -41.8448 | 2025-12-13 02:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 49.5 |


[Clique aqui para ver as próximas entradas](README3.md)
