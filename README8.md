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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59ba5e5d-855f-333f-bedd-a32b2ffee02c | -3.259 | -53.659 | 2024-12-04 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| d7c22b1d-b150-3351-9dfe-b6486d440f63 | -2.9608 | -45.2123 | 2024-12-04 00:30:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 39ff0aec-d0d5-309a-a800-06567006ed94 | -3.1969 | -50.6428 | 2024-12-04 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 0b8316e9-e813-374f-ab77-f6b447decb1f | -5.5695 | -45.1425 | 2024-12-04 00:30:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| df4a8f66-baa1-30b0-8e78-01ae5a487e3d | -3.0764 | -53.2796 | 2024-12-04 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| b1f035c5-61ad-344e-b245-8b5d8d010d99 | -10.0112 | -36.0836 | 2024-12-04 00:30:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 111.7 |
| b7cb00ca-6c05-3f58-b3f7-7c025c3b1952 | -5.588 | -45.1638 | 2024-12-04 00:40:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 4787b4c8-a231-3fb5-9b41-d7777619c882 | -2.6428 | -45.7394 | 2024-12-04 00:40:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 137.0 |
| f935db27-eca8-3576-b1c5-d3c4234b4e51 | -3.1969 | -50.6428 | 2024-12-04 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| d9186a7d-bb1d-3961-816a-76a4cc03fe74 | -2.8197 | -53.0425 | 2024-12-04 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 2e6ff3e4-0fa3-38e3-979e-b6c4b0a30a32 | -3.5675 | -50.3164 | 2024-12-04 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 7ddab6dd-fb91-33d1-b67b-b1c7d8abdad1 | -2.8012 | -53.0633 | 2024-12-04 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| c6f55afe-f4bb-3546-9a4f-76b5fb0fc45a | -4.0501 | -46.5947 | 2024-12-04 00:40:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 47774d7d-a2a8-3ff1-83e4-c87addb8f19c | -3.6757 | -47.1395 | 2024-12-04 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 62abf6f4-d1ce-39a5-b4e4-9540e20fe77f | -2.879 | -51.8138 | 2024-12-04 00:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| da4c63cd-fb5f-39f7-8d66-d89f922a2cca | -3.2153 | -50.6423 | 2024-12-04 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| e83c35c8-0189-3db2-8c42-70603a3a081b | -1.5087 | -46.7647 | 2024-12-04 00:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 163.5 |
| 90cd68f6-55dd-3f73-8a67-584dc3eefd9a | -2.6242 | -45.7399 | 2024-12-04 00:40:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 6b3144b1-45ea-3d6f-b06d-cd58963e7590 | -2.6947 | -51.8597 | 2024-12-04 00:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 48463cfa-7a79-3315-9eb3-64a0a4f2231f | -3.1454 | -54.6059 | 2024-12-04 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 96d33182-5f5a-32bd-8881-39a14530b5ef | -2.7561 | -45.2646 | 2024-12-04 00:40:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 768d75b0-36bf-330c-98c3-f2385cc46cca | -2.0682 | -45.4871 | 2024-12-04 00:40:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 0543466d-08a8-3487-a0a4-881aa63e7577 | -4.3874 | -43.3827 | 2024-12-04 00:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| e0518e08-5a0b-363e-baf7-0fe996ef8e90 | -2.8975 | -51.8133 | 2024-12-04 00:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| f6dcb920-8934-378d-8740-1b2f1bcae513 | -3.1269 | -54.6263 | 2024-12-04 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 657.0 |
| 4ecde306-d7ce-316e-876c-eacddfdb4f78 | -2.9608 | -45.2123 | 2024-12-04 00:40:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 9964ee51-cb42-38df-b315-4fbc1d471d12 | -1.5087 | -46.7427 | 2024-12-04 00:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 63363c1e-013d-334b-91a0-13a4ca01a738 | -1.6623 | -52.7599 | 2024-12-04 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| a98e8fed-ec06-3d11-bdef-dafca38b4c72 | -5.5693 | -45.1651 | 2024-12-04 00:40:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| fa882dfa-f4a2-31fd-907a-0979f9d6cdd4 | -1.7545 | -52.6159 | 2024-12-04 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 745cc440-d0b6-3b26-8751-a393404bf014 | -3.1086 | -54.6268 | 2024-12-04 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 213.5 |
| 387384f4-b848-3078-af7f-2e76212634e2 | -3.127 | -54.6063 | 2024-12-04 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 695.7 |
| 526a716d-6c96-3a0f-a6f0-30593aea03f3 | -4.3689 | -43.3606 | 2024-12-04 00:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 280474b4-34ef-3c32-8326-25436fc1f4a4 | -2.8196 | -53.0629 | 2024-12-04 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| e5e33f74-f34b-30f8-9765-7dcd48a9ad16 | -3.058 | -53.28 | 2024-12-04 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| fda8a948-b524-39ab-9c6d-62e9ce27c540 | -5.5882 | -45.1412 | 2024-12-04 00:40:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| b3e3bac9-b3da-351a-ae4f-7ae1641c278a | -2.8791 | -51.7932 | 2024-12-04 00:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| ed54acc2-a3af-3ddf-a879-ffef5045be4b | -1.6241 | -53.5308 | 2024-12-04 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| a4702690-309f-3fcd-9d04-1fe227755a64 | -5.5695 | -45.1425 | 2024-12-04 00:40:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 45bd650c-1ec0-313a-ac23-c578f9ff524a | -2.8013 | -53.043 | 2024-12-04 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| ef79f34d-6dd2-3991-ad1b-dfd85b95b46e | -3.586 | -50.3158 | 2024-12-04 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 4b32f356-df92-32cf-8a02-62ebeca44296 | -3.6572 | -47.1183 | 2024-12-04 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| e9df7dc8-2dcc-3f98-b883-5d67bd5470f6 | -4.3876 | -43.3595 | 2024-12-04 00:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 6f93271d-5f47-3d98-a1a3-30f9e674a732 | -3.259 | -53.659 | 2024-12-04 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 30df7f3f-1087-37ca-99be-bcc2005844fd | -3.259 | -53.6388 | 2024-12-04 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| aedd7dad-95bc-3467-9656-c4e6dbf68996 | -3.6758 | -47.1176 | 2024-12-04 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 0a1282b3-32e0-3e14-82fc-a9f730e7f020 | -3.1453 | -54.6259 | 2024-12-04 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| a8d2efe3-f43a-35e0-b2e3-f1500a2fd517 | -1.5272 | -46.7644 | 2024-12-04 00:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| ce6b8267-f47c-3918-a744-14410fa43014 | -3.1968 | -50.6637 | 2024-12-04 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| efe96596-ce59-3bf1-a947-8cb86ffad838 | -1.6623 | -52.7396 | 2024-12-04 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 61ab946c-3315-388c-9534-9508cf59c85b | -2.9794 | -45.2116 | 2024-12-04 00:40:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| f21ab0b2-a71f-36b2-bd5b-cd447dca8a12 | -3.6571 | -47.1403 | 2024-12-04 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| d1206b90-1f0b-30f7-8cde-40e955d4252a | -3.0764 | -53.2796 | 2024-12-04 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 67cc4caa-1e9c-35e6-a5f7-216febb794d4 | -3.0581 | -53.2598 | 2024-12-04 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 51ee0bcf-3617-32fa-887d-3b3e9c4f3dd0 | -3.1086 | -54.6068 | 2024-12-04 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 203.7 |
| 300e0116-d41e-3a41-a450-e43d61f90def | -2.756 | -45.2871 | 2024-12-04 00:40:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 58d2c979-1bd7-35b7-a6ec-7691b35b5b5c | -1.7544 | -52.6363 | 2024-12-04 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| f30d855d-8019-3799-b1d3-fc9dbf2ee051 | -3.6571 | -47.1403 | 2024-12-04 00:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 44d147e3-9c13-331b-8176-aa889390248a | -2.8791 | -51.7932 | 2024-12-04 00:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 5f34bbf0-d44e-3f4f-b2d4-57f702a034e8 | -3.586 | -50.3158 | 2024-12-04 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 636b38ed-19c1-31e8-ac17-5ba50023251a | -2.7561 | -45.2646 | 2024-12-04 00:50:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 75a1ea9a-bab2-3379-adc8-a387c0a26238 | -1.6623 | -52.7396 | 2024-12-04 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| c59efd79-5531-324a-a77c-f0b0167df89f | -2.6947 | -51.8597 | 2024-12-04 00:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| c96afd6c-0b89-3675-8e56-f383c8b1b2e2 | -3.0764 | -53.2796 | 2024-12-04 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| f673d468-cc46-32a9-930c-79a74c753c07 | -4.1225 | -43.9068 | 2024-12-04 00:50:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| ea7c7865-9ca3-331f-ade6-7e53ccb70dda | -2.6429 | -45.717 | 2024-12-04 00:50:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| cdb79bc9-4549-3c78-bd4d-25ec66cca23e | -1.4768 | -53.8148 | 2024-12-04 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 8802c2ff-73a5-3573-b862-21aafd476fa3 | -2.8197 | -53.0425 | 2024-12-04 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 5e37e9f3-0292-3836-b750-1e651545a186 | -3.6758 | -47.1176 | 2024-12-04 00:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| e1b4cae1-f396-30ee-bd3d-1b3347cf6a88 | -1.5087 | -46.7647 | 2024-12-04 00:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 188792a1-93ae-36a1-8f6d-830b269bb838 | -2.8196 | -53.0629 | 2024-12-04 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| ab143112-6195-332e-8ece-6b741b48f06b | -3.058 | -53.28 | 2024-12-04 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 639c86f7-3581-34c3-b323-5c6c571d2bc4 | -3.259 | -53.659 | 2024-12-04 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| c31025f1-7b1c-3a9d-bc7b-13134aa06ac8 | -1.4768 | -53.7947 | 2024-12-04 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 77f4e551-03ef-397e-a237-ecc151e9138a | -1.7545 | -52.6159 | 2024-12-04 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 1e66a85b-be69-3f7a-98b6-e53fb26cb4a7 | -3.5675 | -50.3164 | 2024-12-04 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| a837ab45-cdcf-3eff-aae7-f2550a998f4c | -2.6242 | -45.7399 | 2024-12-04 00:50:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 63.9 |
| b2c1c93e-712d-3df0-afc0-12604c4ae56e | -2.6428 | -45.7394 | 2024-12-04 00:50:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 4f5a37bd-2a71-3dea-83a5-3363ae8161f5 | -4.0499 | -46.6168 | 2024-12-04 00:50:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 73.5 |
| c967e4d5-e015-3f76-a526-82bb093c8830 | -3.2153 | -50.6423 | 2024-12-04 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| a22975b6-cd8b-3a07-8286-9164005f12cd | -2.0682 | -45.4871 | 2024-12-04 00:50:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 47f45a09-b38b-3a1b-b4c6-feda33f62475 | -3.259 | -53.6388 | 2024-12-04 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| c50d9caf-9576-36d7-bdbf-d4f43510905e | -4.1223 | -43.9299 | 2024-12-04 00:50:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| fc6bf6be-e945-30b7-92e5-1aa48362212f | -3.0581 | -53.2598 | 2024-12-04 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 71e246fe-4538-3ca0-b403-7a520e9b9e47 | -1.6241 | -53.5308 | 2024-12-04 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 0a17bc3f-b884-3fa5-a084-43199140a08d | -5.5695 | -45.1425 | 2024-12-04 00:50:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 50d322b4-94a0-3cf3-b674-6776baf7ad86 | -1.7361 | -52.6162 | 2024-12-04 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 2ca02976-2fce-3402-9e38-7ef24edd3b0f | -3.6572 | -47.1183 | 2024-12-04 00:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 70b43402-42f6-33d8-b7a9-128ac9e50e26 | -4.0501 | -46.5947 | 2024-12-04 00:50:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 87.1 |
| a07c86dd-d846-309b-97f1-8845ab6f1b88 | -2.879 | -51.8138 | 2024-12-04 00:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 04c14150-b3ae-39e0-a6e3-0af48327c496 | -3.2774 | -53.6585 | 2024-12-04 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 1525bb81-7239-38ed-b822-470458c6d6a4 | -2.756 | -45.2871 | 2024-12-04 00:50:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 0f3a1d50-83fb-3d28-acda-c87f9b817a30 | -3.1969 | -50.6428 | 2024-12-04 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| bad4a47d-5e2d-35c5-9085-29f41e3647eb | -1.7544 | -52.6363 | 2024-12-04 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 596296a1-ce78-3481-88a2-68f7e37e190e | -5.5693 | -45.1651 | 2024-12-04 00:50:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 77a2c256-91fc-3f37-810a-7262ab2478f8 | -1.6623 | -52.7599 | 2024-12-04 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 20d44104-37b4-384f-87c3-35e1e84252b9 | -2.8012 | -53.0633 | 2024-12-04 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 3e355461-dfcf-3513-a439-e6ffd8ee531c | -2.8975 | -51.8133 | 2024-12-04 00:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 52e1f1cd-d180-3695-a123-7fffe06e35df | -5.5882 | -45.1412 | 2024-12-04 00:50:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 1870a243-ddda-3747-b89c-830b2f1a9318 | -5.588 | -45.1638 | 2024-12-04 00:50:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |


[Clique aqui para ver as próximas entradas](README9.md)
