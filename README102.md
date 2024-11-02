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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d448857-e320-30d0-a741-cf77c416dcee | -6.75569 | -35.52024 | 2024-11-02 11:38:00 | TERRA_M-M | BELÉM | PARAÍBA | Brasil | 2501906 | 25 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 55594b31-f43e-3ae6-826d-7792c1e15fca | -6.75781 | -35.50623 | 2024-11-02 11:38:00 | TERRA_M-M | BELÉM | PARAÍBA | Brasil | 2501906 | 25 | 33 | nan | nan | nan | Caatinga | 82.1 |
| c1d4a868-2d7a-3e63-ad53-871978b7fb8d | -7.74331 | -38.76392 | 2024-11-02 11:38:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 124.0 |
| 74266532-1ae0-3856-986b-df66e8c53963 | -1.2018 | -53.6568 | 2024-11-02 11:45:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 074ef8e8-d54e-31a1-8fcb-45bd90baf090 | -1.2018 | -53.6366 | 2024-11-02 11:45:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 632c7930-ee00-3f39-b129-a40603b21204 | -1.2014 | -53.9184 | 2024-11-02 11:45:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 8c6c0b8e-8c35-3605-b659-13b424e29b21 | -1.2018 | -53.6366 | 2024-11-02 11:55:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 151.1 |
| 24c984a6-a574-3914-9c9b-6d9c0c5a11e9 | -1.2018 | -53.6568 | 2024-11-02 11:55:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 3f5b145e-5a91-3358-82da-5cf8e7fce0d1 | -1.2014 | -53.9184 | 2024-11-02 11:55:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 33fbcd3a-f76a-3d57-b452-630ff46c01d5 | -1.2018 | -53.6366 | 2024-11-02 12:05:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 71f52abb-bb5c-3ae0-acba-19ede9e70c2c | -1.2014 | -53.8983 | 2024-11-02 12:05:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| d40d2a02-ea4a-3bb0-b7f1-522799c6f11e | -1.2014 | -53.9184 | 2024-11-02 12:05:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 303451dc-16bf-3006-b652-8b8b4ba0b27e | -1.2018 | -53.6568 | 2024-11-02 12:05:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 131.4 |
| d325da2d-ebe7-35b9-88fb-681da1127a3e | -1.2018 | -53.6568 | 2024-11-02 12:15:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 11e2f4c1-36bf-3f17-a452-30605a54b6af | -1.2018 | -53.6366 | 2024-11-02 12:15:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 9c3c19ac-ab31-3004-ac50-411037ffa3b2 | -1.2014 | -53.8983 | 2024-11-02 12:15:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| d72ca4d0-d1f7-3baa-be46-46098e7085d7 | -1.2014 | -53.9184 | 2024-11-02 12:15:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 410648e0-da6b-3238-9c1b-c1a7ad217cde | -1.2014 | -53.8983 | 2024-11-02 12:25:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 127.6 |
| 82e17117-fdeb-3fa4-9089-b9103726ae5a | -1.2014 | -53.9184 | 2024-11-02 12:25:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 52cf4f78-872d-3f87-b396-1dc3b5de6aab | -1.2018 | -53.6366 | 2024-11-02 12:25:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 128.7 |
| d6475626-e952-3a8b-9915-bd5f5a973368 | -1.2018 | -53.6568 | 2024-11-02 12:25:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 138.3 |
| 7f93193d-74e2-3467-be5d-e67afe7eefd4 | -1.5127 | -54.2761 | 2024-11-02 12:25:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 424ebb60-022f-3b97-ad1d-859edb20556d | -1.5127 | -54.2961 | 2024-11-02 12:25:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 880dba68-aa3a-35e1-aa9a-6077d9597b25 | -1.2018 | -53.6568 | 2024-11-02 12:35:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 9ac7d0eb-2e8f-3d5c-aa44-1092c99fd03e | -1.2014 | -53.8983 | 2024-11-02 12:35:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 183.7 |
| a88946e6-5a54-3d56-8bc3-962204f341f3 | -1.2014 | -53.9184 | 2024-11-02 12:35:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 142.1 |
| feb0262a-3b85-3d23-adf4-a3c358c065e9 | -1.2018 | -53.6366 | 2024-11-02 12:35:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 7607c9cf-6034-3416-a7b6-5c0c4ddb83a3 | -1.5127 | -54.2961 | 2024-11-02 12:35:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| a18392d6-beb0-3950-9e61-18572193e107 | -3.2164 | -46.1871 | 2024-11-02 12:35:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 09931318-cd40-39ad-9b32-346699104e3e | -1.2014 | -53.9184 | 2024-11-02 12:45:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 498f3bd3-853e-3ca7-99f9-8b753d238427 | -1.1834 | -53.6569 | 2024-11-02 12:45:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| e1456702-2a44-31a6-a2ae-5d518491f708 | -1.2018 | -53.6366 | 2024-11-02 12:45:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| c1e807b2-b99e-38fe-a122-07e23370c40b | -1.2018 | -53.6568 | 2024-11-02 12:45:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 93857c89-c94a-3f18-a0b4-93f0eeebddbc | -1.2014 | -53.8983 | 2024-11-02 12:45:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 757f2b2f-df39-3d70-a966-47ac4bc26ff5 | -2.2703 | -46.1068 | 2024-11-02 12:45:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 24d40c3b-87f2-3615-9c0b-ae4cc554edad | -1.2018 | -53.6366 | 2024-11-02 12:55:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| d7c1cad8-bab8-3fc8-9088-a01d99f62cf1 | -1.2014 | -53.9184 | 2024-11-02 12:55:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| f4826367-0bcc-357f-86fe-dba24a99de99 | -1.2014 | -53.8983 | 2024-11-02 12:55:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 7aab228c-654f-38eb-8477-4909f5241fef | -1.2018 | -53.6568 | 2024-11-02 12:55:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 92fa2b1c-7e5e-3094-885f-9dbf9225e00e | -1.5127 | -54.2961 | 2024-11-02 12:55:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 18e48081-25c5-3d55-b717-2d20282c29bb | -2.1746 | -53.6834 | 2024-11-02 12:55:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 206.0 |
| b4c6ed8c-82db-3ba5-8e23-80eaf63d76be | -2.1747 | -53.6633 | 2024-11-02 12:55:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 6a4eea05-8280-30df-8596-7eed51a8fd1d | -1.2014 | -53.9184 | 2024-11-02 13:05:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 31ba0b8a-7648-3b8e-8a23-139e1070062d | -1.2014 | -53.8983 | 2024-11-02 13:05:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 1b2a68aa-84cf-30cc-a9be-758e17b6a904 | -1.5899 | -52.1481 | 2024-11-02 13:05:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 9e4314b0-51c9-3575-bb88-c3101db6fba6 | -2.1747 | -53.6633 | 2024-11-02 13:05:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 133ab4dc-18bf-3ad4-9023-e3dcc7862781 | -2.2703 | -46.1068 | 2024-11-02 13:05:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| a2a90fdb-a348-3b6c-9cfe-22f8904dc7ca | -3.2164 | -46.1871 | 2024-11-02 13:05:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 39bb8886-e139-3de4-8871-db4f391d785d | -1.2014 | -53.8983 | 2024-11-02 13:15:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| c49e2842-d8a3-3223-a293-0b64da2817ed | -1.2014 | -53.9184 | 2024-11-02 13:15:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| c1332002-bf7b-3be9-8b0c-6e528f36c168 | -1.406 | -52.1916 | 2024-11-02 13:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 1158081a-5f62-3953-8cbb-1a10993230ab | -2.2568 | -50.4376 | 2024-11-02 13:15:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 33268a65-2e12-39ad-a4c2-6026f2602fda | -2.193 | -53.6831 | 2024-11-02 13:15:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 9b508a62-7d1a-33ff-87da-357555fafeef | -2.2703 | -46.1068 | 2024-11-02 13:15:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 8ac88449-f4bc-3e77-b48b-c74d2dd5e021 | -3.2164 | -46.1871 | 2024-11-02 13:15:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 50ea78f7-f212-3491-abdb-de59b4524b43 | -3.1281 | -54.266 | 2024-11-02 13:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| a7345e34-96ca-30f8-b460-df474473ce9e | -3.1282 | -54.2459 | 2024-11-02 13:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| bfbf6b5a-688f-3744-bd7c-e4d286f558e2 | -5.7267 | -42.2088 | 2024-11-02 13:15:38 | GOES-16 | PRATA DO PIAUÍ | PIAUÍ | Brasil | 2208601 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| f5a63566-2b50-3af3-84e8-265fe00d1554 | -1.2014 | -53.9184 | 2024-11-02 13:25:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| ca592294-3c9b-3b71-9db8-535f7710738b | -1.2014 | -53.8983 | 2024-11-02 13:25:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| a67aa389-fa5e-30e7-b361-004778b715d6 | -1.4427 | -52.2116 | 2024-11-02 13:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| e4d5eb1e-4891-3815-93db-b1706de9e2cb | -1.406 | -52.1916 | 2024-11-02 13:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| ac5b2456-be6a-383b-b05d-c5a879267255 | -2.2703 | -46.1068 | 2024-11-02 13:25:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 3a05d2b3-511a-3978-a52a-8796ff1f3b88 | -2.2568 | -50.4376 | 2024-11-02 13:25:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| b30c5454-38db-398d-8d8f-202c86bf787a | -2.1747 | -53.6633 | 2024-11-02 13:25:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 58aa6a59-d405-3a4d-b90a-6f749ff34c60 | -2.4824 | -49.102 | 2024-11-02 13:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| b8dcb5ac-16ca-341b-a8bd-79cd7dbef50f | -2.4825 | -49.0807 | 2024-11-02 13:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 3ccf9fdf-172b-3e92-b0d1-c7d1fb3f93ef | -3.2164 | -46.1871 | 2024-11-02 13:25:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |
| c0357fe9-4d33-32a2-b464-484ea9fdd38d | -3.9474 | -48.3451 | 2024-11-02 13:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 8609f3f7-83a8-33b2-a7a5-deba12a5bcec | -3.9473 | -48.3666 | 2024-11-02 13:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 4d7e3442-e45e-3696-b786-4ee4639abb09 | -6.3537 | -41.5569 | 2024-11-02 13:25:42 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| f6228ec3-9cac-3c29-9848-ac3a30d2aa93 | 2.2003 | -50.8773 | 2024-11-02 13:34:53 | GOES-16 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 21cc9e99-feca-3cb8-ab74-59beae9b18e7 | -1.2014 | -53.8983 | 2024-11-02 13:35:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 7c656eb4-44f2-3fe0-ae38-d498c0101a87 | -1.4244 | -52.1913 | 2024-11-02 13:35:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 2380876e-cce2-3545-8ab2-bd33393d2d84 | -1.406 | -52.1916 | 2024-11-02 13:35:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 67e69bdd-38ac-3851-92ae-9673f383c6f5 | -1.4427 | -52.2116 | 2024-11-02 13:35:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 74751d54-5e62-3d40-badf-cb5c6b80aeee | -1.4244 | -52.2118 | 2024-11-02 13:35:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 4cdc92a7-b9ad-362e-b772-aa3ab19f292d | -2.0471 | -53.2411 | 2024-11-02 13:35:18 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| c63423b0-3d81-300c-968e-ccf47bca03a2 | -2.2703 | -46.1068 | 2024-11-02 13:35:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 89.8 |
| b22261bc-e7eb-3cec-a4d0-c484c73e2e63 | -2.4825 | -49.0807 | 2024-11-02 13:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 9816061f-b3a5-30d9-af3c-00ede1d11676 | -3.1098 | -54.2665 | 2024-11-02 13:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| decdcb94-fd6b-3ef8-8fc1-527b346c8f9c | -3.2164 | -46.1871 | 2024-11-02 13:35:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 66.6 |
| a199e896-6ade-3738-8a0c-8ae58493f06e | -3.1282 | -54.2459 | 2024-11-02 13:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 2534deda-b81a-37c8-9ac8-f9e93097463a | -3.9473 | -48.3666 | 2024-11-02 13:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 8fd2a71c-6a1b-3eb0-98d0-5fbc06ad9788 | -3.9474 | -48.3451 | 2024-11-02 13:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| e8105f38-b071-3501-b08f-a8389757f766 | -4.4056 | -43.4514 | 2024-11-02 13:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 256b9136-80e8-3e69-9007-b74d553eeb59 | -5.2297 | -48.0868 | 2024-11-02 13:35:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| bfa4408c-1d52-3b4d-b762-26a3c00427ec | -6.9971 | -41.3258 | 2024-11-02 13:35:45 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 74.9 |
| 6bc86076-85c9-372e-be8a-91e68b69a961 | -6.9405 | -41.3315 | 2024-11-02 13:35:45 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| c2797364-f9df-3115-9561-853b8d7e24c9 | -1.4244 | -52.2118 | 2024-11-02 13:45:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| ba0ac007-5fd5-3527-bc15-0b6c5e2aba81 | -1.4244 | -52.1913 | 2024-11-02 13:45:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| e6d84c6c-f0c7-31b1-a929-ffc1bff367fd | -2.2703 | -46.1068 | 2024-11-02 13:45:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 82.5 |
| ed0ed828-b984-399d-b01e-127ef1cb79b8 | -2.4825 | -49.0807 | 2024-11-02 13:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 2422ef87-f477-36d4-8336-550716aa58f1 | -2.4824 | -49.102 | 2024-11-02 13:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 676a6879-cc9f-381e-a676-fc8173718f6f | -2.722 | -49.287 | 2024-11-02 13:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 6e24dfd1-e283-3fd6-9553-d2bc6d166374 | -3.2164 | -46.1871 | 2024-11-02 13:45:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 30378e46-976b-361d-93e4-161ee83c9eaf | -3.1282 | -54.2459 | 2024-11-02 13:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 466260ec-a458-3cae-b76a-f6e62a9a4563 | -3.6421 | -50.1667 | 2024-11-02 13:45:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 5e849b93-1252-3165-af4d-74139f43c750 | -3.9474 | -48.3451 | 2024-11-02 13:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| e69a251c-6869-315d-a4ed-37d9038973ca | -3.9473 | -48.3666 | 2024-11-02 13:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |


[Clique aqui para ver as próximas entradas](README103.md)
