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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d521dad-63fe-3096-a557-958c8beb728d | -2.3211 | -53.8821 | 2024-11-25 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 145.3 |
| dc500a36-b874-38cc-9f24-8c2507ba913f | -3.9309 | -47.9784 | 2024-11-25 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 87de8f35-a27a-3da4-b368-0dfc7b11debd | -3.6943 | -47.1168 | 2024-11-25 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| e6cb2d99-051d-3534-895a-c107dc5219d8 | -4.4659 | -45.5488 | 2024-11-25 00:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 71.1 |
| d6909610-89c5-3b30-9301-0694ebe4feb9 | -2.2914 | -45.3689 | 2024-11-25 00:10:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| b0f67302-b8b2-3044-92de-065485584d93 | -3.7057 | -52.426 | 2024-11-25 00:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| b4570ac9-0dc2-3032-893d-d867521beca8 | -2.3394 | -53.8818 | 2024-11-25 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 163.5 |
| 77dd30ca-5746-39fc-a279-758d69ccf5c4 | -2.2483 | -53.6216 | 2024-11-25 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| fd1dd0c5-eaa2-3bc6-b851-158f76bd8924 | -3.2872 | -51.1194 | 2024-11-25 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| b3c36c4e-4d93-3cf0-b843-b444e3cb772b | -3.9493 | -47.9993 | 2024-11-25 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 82b83341-04de-3fb5-b583-15cce5421fdd | -4.0415 | -48.0818 | 2024-11-25 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 9c2beb2c-1bd8-3821-9236-1104722d4924 | -4.0231 | -48.061 | 2024-11-25 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| ee6dbaa9-69a7-3d4b-bae3-7482e2b74c01 | -2.3395 | -53.8617 | 2024-11-25 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 292.1 |
| bc3f0fd3-2fed-3e60-b928-da75b0959f03 | -4.4847 | -45.5253 | 2024-11-25 00:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 74.5 |
| bb2b4f91-2b95-3835-8d2b-9d19183e750e | -3.7129 | -47.116 | 2024-11-25 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 0fbd17f9-a97d-3714-bfba-bc45d9990db7 | -3.7057 | -52.426 | 2024-11-25 00:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| b276c150-91a1-3374-af0b-5674da9c5986 | -0.046 | -50.8171 | 2024-11-25 00:20:00 | GOES-16 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| f48c24e7-d0c1-32a5-8e50-86d05d8616b5 | -3.185 | -49.0599 | 2024-11-25 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 2c6fe078-9b32-308c-bae2-c412471899e6 | -2.3211 | -53.862 | 2024-11-25 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 6737b206-5518-3562-97f6-95a32cb516ac | -3.0735 | -49.1914 | 2024-11-25 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| a2fd3815-c4d4-3ef8-8a60-0cab77de7aec | -2.3211 | -53.8821 | 2024-11-25 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| c43108a0-4c38-37a4-834f-21074673dd3e | -3.9493 | -47.9993 | 2024-11-25 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 81ed3340-6eab-3531-9e8b-d8b25919ad8c | -4.2604 | -48.7184 | 2024-11-25 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 703a1ab9-eab4-30b8-93b3-5f2950c8df8d | -4.0231 | -48.061 | 2024-11-25 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 65ea868d-4933-3312-9b49-2a30012aa25e | -4.466 | -45.5263 | 2024-11-25 00:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 6a0d2924-04e1-3d85-873f-7b9a5914e835 | -4.4659 | -45.5488 | 2024-11-25 00:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 6d5d5f8b-a9b7-3c69-b675-a13a9581264e | -0.0644 | -50.8171 | 2024-11-25 00:20:00 | GOES-16 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| e1775677-4a15-3f83-8258-41507f3b8044 | -3.0734 | -49.2127 | 2024-11-25 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 1526ce9f-b4a1-3009-a6dd-a08c4e8919d5 | -3.7058 | -52.4055 | 2024-11-25 00:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 2351ef21-d33f-3171-8768-f48a64dade1b | -3.9494 | -47.9776 | 2024-11-25 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 36a711d2-740c-3750-9e43-28f2f3eb8d8e | -2.3394 | -53.8818 | 2024-11-25 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 177.6 |
| b551ce52-5b5a-37d4-b67e-1dcc71e4ee22 | -4.023 | -48.0827 | 2024-11-25 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 158.2 |
| 0c9136a4-fdd3-3fb6-b107-abd7c83d59e1 | -3.2872 | -51.1194 | 2024-11-25 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| cc6c79d4-7e04-3b72-83c0-9f06bcd6e27b | -2.3395 | -53.8617 | 2024-11-25 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 264.9 |
| fbab3c28-65e5-33be-9101-01bd42acc800 | -2.3394 | -53.8818 | 2024-11-25 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| b2c37838-9870-331f-893b-b1d7635a2d38 | -3.9493 | -47.9993 | 2024-11-25 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| ff806d91-a153-3a5f-87ff-63494290384c | -2.2483 | -53.6216 | 2024-11-25 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 462d6818-dad7-3a0d-a89a-0f1098e60556 | -3.2872 | -51.1194 | 2024-11-25 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 2d411e93-bd93-3e4a-a1de-f87b861abe55 | -2.3211 | -53.8821 | 2024-11-25 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 07913070-5271-3e36-bc9d-3d85882406ab | -3.0734 | -49.2127 | 2024-11-25 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 5aed2e74-e556-311b-97ba-e1946cc370f0 | -4.2604 | -48.7184 | 2024-11-25 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| f1e99782-1a9b-3168-8665-72d0e6a1a5f4 | -3.0735 | -49.1914 | 2024-11-25 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| ba3b2da0-b91e-342f-9d95-99a2e18e019e | -0.046 | -50.8171 | 2024-11-25 00:30:00 | GOES-16 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 932ad445-d233-35d1-8715-893970dbf00e | -3.4581 | -50.0047 | 2024-11-25 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 5a2dc5b8-2743-30b9-8126-680123a7ffb3 | -3.9494 | -47.9776 | 2024-11-25 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 211b5a36-cc78-3f54-9129-c2f2e6ce0302 | -2.3395 | -53.8617 | 2024-11-25 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 170.0 |
| 1841208f-b452-3e84-bd73-7613977dcf62 | -2.3211 | -53.862 | 2024-11-25 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 190.2 |
| 5503a747-4f56-3d99-a266-db603d35a9a5 | -3.4396 | -50.0053 | 2024-11-25 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 030a9a69-1359-3056-b4f2-8a014772ee82 | -2.5513 | -45.3837 | 2024-11-25 00:30:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 6feeb780-9257-37f4-94aa-2cc37725479b | -4.023 | -48.0827 | 2024-11-25 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 36271e2e-200c-3e6a-8c2c-4da6135c2616 | -0.0644 | -50.8171 | 2024-11-25 00:30:00 | GOES-16 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 9e404206-45ee-3265-9a60-ec48514698e3 | -3.5159 | -53.8132 | 2024-11-25 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 80fa0db7-303e-300b-bd1b-df7ccaa1e172 | -3.0735 | -49.1914 | 2024-11-25 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 9732677e-dca9-3ec1-b4b9-5695725e21d7 | -2.3395 | -53.8617 | 2024-11-25 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 181.9 |
| 7d1b13f8-0b91-3ea9-a16e-0b8e4a53ae05 | -0.046 | -50.8171 | 2024-11-25 00:40:00 | GOES-16 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| f8bed389-9fe4-36cc-bcad-73d0056673a2 | -4.2461 | -47.986 | 2024-11-25 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 120.1 |
| 180a2709-766a-325a-ac4b-b79656f42f09 | -2.3211 | -53.8821 | 2024-11-25 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| b21bda2d-153d-37da-ac3e-c605840809e0 | -2.3394 | -53.8818 | 2024-11-25 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 62ce2499-6d82-3a14-a308-5ff28a9d78d6 | -4.2604 | -48.7184 | 2024-11-25 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| b945604b-8707-361a-9ef1-b48aea52d631 | -4.0231 | -48.061 | 2024-11-25 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 52fc39e6-83c6-3b02-90e5-95be54d5de29 | -3.5159 | -53.8132 | 2024-11-25 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 478829f3-8579-3e3e-bea9-6f86b611d611 | -0.0644 | -50.8171 | 2024-11-25 00:40:00 | GOES-16 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 5bc2ceb2-da27-3939-8f03-faa2301499c9 | -3.9493 | -47.9993 | 2024-11-25 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 345f0689-ac8c-38e3-beec-b351b5917427 | -3.2872 | -51.1194 | 2024-11-25 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| e1c77d74-23e8-34e4-aac6-b8c20c50b88d | 1.8398 | -55.9204 | 2024-11-25 00:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| f66f8ce6-ef8b-3434-beb2-84e4e8d2532d | -3.4396 | -50.0053 | 2024-11-25 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| ea0e612e-002b-33c9-be5b-95b81660d356 | -3.9494 | -47.9776 | 2024-11-25 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 2e5e156a-e286-3caf-a287-a445b0627014 | -2.3211 | -53.862 | 2024-11-25 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| fd4b3140-7409-35ed-bd29-0765db6587e4 | -3.4581 | -50.0047 | 2024-11-25 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| e8b31ccf-67a6-351a-9cd3-54aa6743306e | -3.0734 | -49.2127 | 2024-11-25 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| fed19646-7bd6-3a9d-907d-d36e7509052d | -4.023 | -48.0827 | 2024-11-25 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 7d351ccb-91db-3501-ad62-a805533edebd | 1.8398 | -55.9007 | 2024-11-25 00:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 93833b9a-aec9-36fa-9441-45353d17ab8f | -3.5159 | -53.8132 | 2024-11-25 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| c7342c63-8a54-3747-9f41-2e463131f77f | -4.2604 | -48.7184 | 2024-11-25 00:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 9387aca7-5368-3c97-b949-cf1cdee0511a | -4.2461 | -47.986 | 2024-11-25 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 0dc262fc-a227-3fb7-8bb9-834307b3a013 | -3.9309 | -47.9784 | 2024-11-25 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 2811f890-f68c-3889-900a-e7a2c117f84e | -3.2872 | -51.1194 | 2024-11-25 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| ecf37165-3828-3706-8a85-1ca02b28e91b | -4.023 | -48.0827 | 2024-11-25 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 7f992744-ce7f-3e51-ba22-7bfbf6e69e37 | -0.046 | -50.8171 | 2024-11-25 00:50:00 | GOES-16 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 6a330cf9-77e9-36e1-95c9-a8ed0e757d5d | 1.8398 | -55.9204 | 2024-11-25 00:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 9669d240-c504-31d5-8d21-5608276b91c2 | -3.9494 | -47.9776 | 2024-11-25 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 16652387-b47d-3266-9507-63aa264c8a50 | -2.2914 | -45.3689 | 2024-11-25 00:50:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 9fc21687-dc25-3a7e-9994-6bbd32f70a8b | -3.0582 | -53.2192 | 2024-11-25 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 092e5a55-81f5-3b20-975d-6f53fc30fbe9 | -3.185 | -49.0599 | 2024-11-25 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 7abaa88c-63bc-3737-b9d3-9e4c8e93bae7 | -3.9493 | -47.9993 | 2024-11-25 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 8804e64b-99f7-3496-bdbb-57f014640054 | -2.3395 | -53.8617 | 2024-11-25 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 142.4 |
| 221b2f9b-dd17-340b-9e76-636460e6c2f9 | -2.3394 | -53.8818 | 2024-11-25 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 66eb9b2f-3a74-382c-b1f7-359d179b0f9d | -2.3211 | -53.862 | 2024-11-25 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 1fd282d2-98d1-3850-94be-2e4c17d78680 | -0.0644 | -50.8171 | 2024-11-25 00:50:00 | GOES-16 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 78ed148a-6686-3604-a865-5dac570f28a3 | -0.046 | -50.8171 | 2024-11-25 01:00:00 | GOES-16 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| d3842a05-f90c-3f10-8cc6-0166d0b49e62 | -4.023 | -48.0827 | 2024-11-25 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 518e05d5-8e70-3e82-a70a-e2d0fd319577 | -2.3395 | -53.8617 | 2024-11-25 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 261219e2-351c-3efe-9f9c-8d5d5acae743 | -3.9494 | -47.9776 | 2024-11-25 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| a05c56c3-6bf1-3a7c-814d-72376b2b6a23 | -2.3211 | -53.8821 | 2024-11-25 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 523e75d7-5192-3e89-b5a6-97c8b280c807 | -3.2872 | -51.1194 | 2024-11-25 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 5966e43c-94b6-3d90-b4de-8c2cce6b88a0 | -3.9493 | -47.9993 | 2024-11-25 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 968d76a6-ffe0-3a82-812c-100dff9c083e | 1.3637 | -55.9063 | 2024-11-25 01:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| cf29b4d2-0978-3529-87b8-6fd89aea9fd1 | 1.382 | -55.9061 | 2024-11-25 01:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 66b80e11-d29f-3074-bef5-9c50d237d4d2 | -2.3211 | -53.862 | 2024-11-25 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 93fa5986-efbe-3d00-bf7b-baf94d844002 | -0.0644 | -50.8171 | 2024-11-25 01:00:00 | GOES-16 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |


[Clique aqui para ver as próximas entradas](README5.md)
