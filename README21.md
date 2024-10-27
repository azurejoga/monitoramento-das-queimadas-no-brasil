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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0e1d1d7-e75d-3ed8-8136-75cb990eb145 | -0.9815 | -53.7192 | 2024-10-27 01:25:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 04e7f03f-2af9-311b-b0cb-b3a4f7b6be37 | -0.9815 | -53.699 | 2024-10-27 01:25:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 279.3 |
| c2bb4577-f6b5-3bf9-9680-a559b6320a13 | -0.9815 | -53.6789 | 2024-10-27 01:25:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 46557c87-7217-36c2-a304-59e7a87043cc | -0.9998 | -53.719 | 2024-10-27 01:25:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 9a6f01fa-934b-36df-910c-fc8e95b207da | -0.9998 | -53.6989 | 2024-10-27 01:25:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 166.8 |
| 149c860d-74d6-33c3-853f-92134ecf4979 | -1.1831 | -53.8985 | 2024-10-27 01:25:12 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 84155598-c501-371f-9c2d-e586d0833752 | -1.7874 | -46.4065 | 2024-10-27 01:25:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 5f6cdacf-4600-350a-bac0-3653c5d2dc44 | -1.7875 | -46.3844 | 2024-10-27 01:25:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| b17ec2df-51f2-3c86-acce-0d0fb79be0df | -1.806 | -46.384 | 2024-10-27 01:25:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 41d76830-e859-37ee-9709-f368fd009fc4 | -2.4567 | -45.8567 | 2024-10-27 01:25:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 39.5 |
| c5645948-e076-3eeb-98c1-097f0f2c0304 | -2.4568 | -45.8344 | 2024-10-27 01:25:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 0756a8e6-1fea-3bda-bbc7-2426946cf335 | -2.4598 | -50.412 | 2024-10-27 01:25:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| ead7df0a-c5de-3d91-9a38-a0118cd96248 | -2.4753 | -45.8561 | 2024-10-27 01:25:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 9ac064ee-b874-320c-a95a-7b33a6d9c690 | -2.4753 | -45.8338 | 2024-10-27 01:25:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 156.4 |
| 8280dec6-a57d-37f5-b9bf-eeaa6a80f718 | -2.4786 | -50.2858 | 2024-10-27 01:25:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 9b0c5424-9ad6-3fa4-a8eb-b290a23d1c7b | -2.486 | -48.0507 | 2024-10-27 01:25:19 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| d65d730e-3008-315a-8b35-c61f35256ffd | -2.5045 | -48.0502 | 2024-10-27 01:25:19 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| bd7194bf-340d-3a6a-9ab0-21c402c13b07 | -2.6297 | -49.247 | 2024-10-27 01:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| a1dd78f1-18d0-308e-ba3a-a13388023857 | -2.6321 | -54.2975 | 2024-10-27 01:25:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| fc6d4f94-da9f-36c0-9072-5510f5d33e1b | -2.6505 | -54.2971 | 2024-10-27 01:25:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| f9877bc5-ca92-329d-afad-58fbd1c3831b | -2.7033 | -49.33 | 2024-10-27 01:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 528d2586-64d8-36dd-8012-08dffced65da | -2.7034 | -49.3088 | 2024-10-27 01:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| c4eeb32d-5fec-3d80-a8b8-4f7b428c9956 | -2.8145 | -49.2418 | 2024-10-27 01:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| dc7cad65-3bec-3ed0-9d1d-3097d3f495dd | -2.8329 | -49.2626 | 2024-10-27 01:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 199945a8-a38a-3927-89c0-2421437ce5b3 | -2.833 | -49.2413 | 2024-10-27 01:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 85a50e60-314a-3a02-81f7-4ddccd2521da | -2.8397 | -52.5532 | 2024-10-27 01:25:21 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 59083b4b-4ba4-37f8-9424-2fe34115b095 | -2.8422 | -51.8148 | 2024-10-27 01:25:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 5180cada-0d19-39f7-884c-966c8d1f0515 | -2.8515 | -49.2408 | 2024-10-27 01:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 561fb095-18af-33b9-9af3-d9c816d10bf1 | -2.916 | -51.7716 | 2024-10-27 01:25:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| eca908af-941a-36b9-9e26-b9b616c602c4 | -2.9161 | -51.751 | 2024-10-27 01:25:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| a6021896-4f93-3c3c-90ef-104fde3fd0fa | -2.9214 | -50.295 | 2024-10-27 01:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 9961ac28-fedf-3619-b99b-ef42dd10e60d | -2.9215 | -50.274 | 2024-10-27 01:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 0df51bc6-fe88-3d4a-8ff1-ec10a6c6495f | -2.9345 | -51.7711 | 2024-10-27 01:25:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 0960ad16-bcc2-357f-abfc-5da39f9d6294 | -2.9345 | -51.7505 | 2024-10-27 01:25:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 520b4c2d-bc8a-3724-bb7a-19f4bd12b167 | -2.9399 | -50.2735 | 2024-10-27 01:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 993f810a-9765-36bc-a7c2-3b666965f32f | -2.9669 | -53.0389 | 2024-10-27 01:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 4f72304b-dacd-3618-b962-894184da83c7 | -3.1106 | -44.9809 | 2024-10-27 01:25:23 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 56.4 |
| cb05847b-c27c-3ac3-800a-b16b62ebf070 | -3.1242 | -50.3519 | 2024-10-27 01:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| a02c72d4-6919-36f7-9c57-caf38c0c8b8d | -3.3256 | -50.7641 | 2024-10-27 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 38db22a1-fc06-37e5-b37b-909fdf796303 | -3.344 | -50.7635 | 2024-10-27 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 48ee19cb-ee15-36dd-a6a7-79a2103ac9cf | -3.3441 | -50.7426 | 2024-10-27 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 047ee273-cac4-39b9-8f50-20c9db29fc0d | -3.4762 | -54.5772 | 2024-10-27 01:25:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| ad9c5763-70b1-35b0-87ac-b572c6e2305f | -3.5202 | -52.7384 | 2024-10-27 01:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 62100b57-d89e-3c9e-b95a-a1bf2bb994f3 | -4.2799 | -45.5138 | 2024-10-27 01:25:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 0fbdd627-55d1-3b60-905e-0be2ff3456a8 | -6.1674 | -47.2638 | 2024-10-27 01:25:40 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 9610e415-82c4-37d1-979c-a2f19dabc1fb | -6.1676 | -47.2418 | 2024-10-27 01:25:40 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| fb0238c2-c912-3a42-b88b-b6589e55d9c0 | -7.2264 | -46.0498 | 2024-10-27 01:25:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 61b71f12-f70e-39ea-895e-286c2a9f1298 | -7.2452 | -46.0482 | 2024-10-27 01:25:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 04ead6ee-06ec-371c-9154-1eb3e473d11e | -10.5424 | -45.1463 | 2024-10-27 01:26:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 91f62f3f-6055-37fe-9b51-7d3efa41df27 | -0.9815 | -53.7192 | 2024-10-27 01:35:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| b6cbf859-7ca4-3299-a200-88c6b5828179 | -0.9815 | -53.699 | 2024-10-27 01:35:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 243.1 |
| 199189ed-1aa4-3fb4-a3dd-cd3a67223f41 | -0.9815 | -53.6789 | 2024-10-27 01:35:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 2e8e8ba2-0c1a-3183-9d70-3ac96f9a92b8 | -0.9998 | -53.6989 | 2024-10-27 01:35:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 156.0 |
| 20600adc-672d-331d-b6e0-ece333130fd4 | -0.9999 | -53.6788 | 2024-10-27 01:35:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| fb062db0-9604-3b48-8657-4f2e1b1c00cc | -1.7874 | -46.4065 | 2024-10-27 01:35:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 234822f3-b013-337c-b00d-70a4c079e3ee | -1.7875 | -46.3844 | 2024-10-27 01:35:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 1bfbcfee-a108-3ebb-866a-9a38fc8e3148 | -2.4598 | -50.412 | 2024-10-27 01:35:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 3b02e062-eea9-3275-aae5-53643ef656a9 | -2.4753 | -45.8561 | 2024-10-27 01:35:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 739d9540-65dc-33d9-8931-8da89f48bdc1 | -2.4753 | -45.8338 | 2024-10-27 01:35:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 940b906c-9b23-350d-b3b5-8dbce0a1060f | -2.4786 | -50.2858 | 2024-10-27 01:35:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 756f4db7-ef6f-3e35-8ba9-32229c1c5e79 | -2.4824 | -49.102 | 2024-10-27 01:35:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 7832f143-69ad-392c-92e8-0c0fb71e0dfe | -2.5045 | -48.0502 | 2024-10-27 01:35:19 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 18d23956-3306-33be-9617-b240aabb37d7 | -2.4568 | -45.8344 | 2024-10-27 01:35:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 981d9f43-3878-3e07-b893-caf3709fbb50 | -2.6297 | -49.247 | 2024-10-27 01:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 7cd0c2c0-4b19-3e89-8360-63ea37c43446 | -2.6321 | -54.2975 | 2024-10-27 01:35:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| fd3b7a4e-f8f2-3132-b1ff-639c8b848a2c | -2.6505 | -54.2971 | 2024-10-27 01:35:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| e24a7dbc-d0a7-3c64-86b5-e63a9dedfc1a | -2.7033 | -49.33 | 2024-10-27 01:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 03036932-ea10-31e0-b266-9cefb61df008 | -2.7034 | -49.3088 | 2024-10-27 01:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| c337dd3a-0b10-33e9-b395-6edf99f0e570 | -2.8145 | -49.2418 | 2024-10-27 01:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| bbd1ac06-6a06-3731-a401-b708a68dce5e | -2.8329 | -49.2626 | 2024-10-27 01:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 2382ece3-12c5-392d-8da7-f880aa80526c | -2.833 | -49.2413 | 2024-10-27 01:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 052f4329-84f7-32f0-8c64-29f0fa1d8786 | -2.8397 | -52.5532 | 2024-10-27 01:35:21 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 507d25ca-5f61-3d2c-ba95-c0a1ebd8c1b7 | -2.8515 | -49.2408 | 2024-10-27 01:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| e553007e-1858-3abf-9d63-bcea9defd26c | -2.916 | -51.7716 | 2024-10-27 01:35:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 7027b668-2ff5-336c-b508-9518d75aecc7 | -2.9161 | -51.751 | 2024-10-27 01:35:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| a87036c7-2d82-3167-811e-e938ec179347 | -2.9214 | -50.295 | 2024-10-27 01:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 5159fe8e-ca78-30bb-84be-e54344e99807 | -2.9215 | -50.274 | 2024-10-27 01:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| d3d466ec-becd-3e33-b7ef-11c45fd91a8c | -2.9345 | -51.7711 | 2024-10-27 01:35:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| e20b04c1-8730-3286-8cec-a7db289242f7 | -2.9345 | -51.7505 | 2024-10-27 01:35:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| e471d5e4-9feb-39da-aafa-12a03159795a | -2.9399 | -50.2735 | 2024-10-27 01:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 6349d5fd-cc77-3159-ab2a-70e629da37c4 | -2.9669 | -53.0389 | 2024-10-27 01:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| d3e44015-0894-37ad-82ec-1a86549cad6e | -2.9845 | -53.2617 | 2024-10-27 01:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 77d13233-7149-3346-8a1b-0a9eadb36950 | -3.1242 | -50.3519 | 2024-10-27 01:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 746adbe3-fbb9-31bf-ad02-3a1b0f79c65a | -3.3256 | -50.7641 | 2024-10-27 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 578c4fa2-ff98-36ed-bb5b-3105254b4112 | -3.344 | -50.7635 | 2024-10-27 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 05231240-e3bf-3585-99cc-70e2130752a9 | -3.3441 | -50.7426 | 2024-10-27 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 001ba118-0ed0-3e50-b8c0-bdd995698777 | -3.4392 | -50.0896 | 2024-10-27 01:35:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| ad2c4929-9f2a-3c50-b4c2-09992fe0b87c | -3.4762 | -54.5772 | 2024-10-27 01:35:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 6b8ccd1e-84be-3d70-9d44-6e5d6f4abb7d | -3.5202 | -52.7384 | 2024-10-27 01:35:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 52fc4004-ca57-368b-b885-c6b6ad39468c | -4.2799 | -45.5138 | 2024-10-27 01:35:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 264f25a3-9b30-37e4-815c-811f487ae929 | -4.3522 | -45.8462 | 2024-10-27 01:35:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 34.8 |
| b040ac7f-091c-335a-8242-d0b9e9642437 | -4.426 | -45.954 | 2024-10-27 01:35:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 37.1 |
| e5a22466-6615-3b48-9542-ff182ddf05d6 | -7.2264 | -46.0498 | 2024-10-27 01:35:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| b5504855-56b5-3a29-b3ca-7f8b33575bc4 | -7.2452 | -46.0482 | 2024-10-27 01:35:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| bd5a1953-33db-3d0e-9a84-1eda9eb0410a | -10.5424 | -45.1463 | 2024-10-27 01:36:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 57684612-b4f6-3b69-b259-ca4ba7fd0ad1 | -0.9815 | -53.7192 | 2024-10-27 01:45:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 8c4ffbfc-b270-3f33-9b2e-0bdc718a8ec4 | -0.9815 | -53.699 | 2024-10-27 01:45:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 234.9 |
| 8541bb2c-6729-3d6d-9326-d3f9ed9f578e | -0.9815 | -53.6789 | 2024-10-27 01:45:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| bfba0fa1-a3ca-3c79-bc36-96545569c93e | -0.9998 | -53.6989 | 2024-10-27 01:45:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 146.6 |
| 27eb7514-770d-3357-a681-06d0846b9a30 | -2.4598 | -50.412 | 2024-10-27 01:45:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |


[Clique aqui para ver as próximas entradas](README22.md)
