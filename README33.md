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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2e1849e-5fad-3d27-b8bc-f02f2ef5f63d | -11.26869 | -60.40413 | 2024-10-10 01:54:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 37.7 |
| c9c2e2e6-2370-33cd-afeb-151b15499aa6 | -11.26452 | -60.37559 | 2024-10-10 01:54:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 9.9 |
| bd7781a5-3fd3-3107-8a96-c347ffad50fe | -11.26448 | -60.4988 | 2024-10-10 01:54:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 21.9 |
| bb9d56c0-bf61-3dbb-8185-addc0a0487a4 | -11.26312 | -60.48926 | 2024-10-10 01:54:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 0dc7fd3a-b07b-30b5-81a4-0f0221bd5a7f | -11.25955 | -60.40533 | 2024-10-10 01:54:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f4481e16-430d-3ccf-8256-9a7116f9f105 | -11.25541 | -60.50026 | 2024-10-10 01:54:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 80963d36-66e5-3bc6-94d6-5c5bd12bbb2b | -11.25081 | -60.40315 | 2024-10-10 01:54:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8572e62c-074e-335f-be94-00a914926ee0 | -11.23188 | -61.17375 | 2024-10-10 01:54:00 | TERRA_M-M | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d19f4a9b-12c9-3508-ab94-dc77641e5913 | -11.22365 | -60.60137 | 2024-10-10 01:54:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 08210f86-d1a6-3272-aff7-2ad301c623b5 | -11.21819 | -60.56367 | 2024-10-10 01:54:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 73628c97-3146-372c-93aa-ffe9077b9bed | -11.16147 | -60.61681 | 2024-10-10 01:54:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| ae7ba89b-c7b0-3848-afcd-59c0c7821518 | -11.16012 | -60.60739 | 2024-10-10 01:54:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3132970b-644f-3344-aac4-7a4ef1b9e33c | -10.95827 | -61.13054 | 2024-10-10 01:54:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5d690213-ea2e-3c8b-9c91-527bd0201fb3 | -10.95697 | -61.12144 | 2024-10-10 01:54:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8ad04a2f-2432-3da2-9fbf-940cc49dc222 | -10.92309 | -60.94784 | 2024-10-10 01:54:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9d16f322-faf9-3970-8a09-656deee3fdcb | -12.41361 | -61.1218 | 2024-10-10 01:54:00 | TERRA_M-M | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| eafc716e-8e4a-390f-a644-862cc68d27db | -9.17869 | -61.58174 | 2024-10-10 01:54:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0c5f1601-18e9-3403-946b-e12775c550bd | -9.17741 | -61.57267 | 2024-10-10 01:54:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b8797eef-422e-3b3c-870e-00fb568a2dea | -9.16849 | -61.57399 | 2024-10-10 01:54:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b9e2bfee-22fd-3760-8209-2c28ae12282e | -9.15958 | -61.5753 | 2024-10-10 01:54:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ed42a3c8-370f-3675-bb9c-0d51764aadcd | -9.02655 | -61.61636 | 2024-10-10 01:54:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 266fde49-d015-326f-b1c4-dbd75d8495ab | -9.01891 | -61.62674 | 2024-10-10 01:54:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c40ce5cc-d4b7-3c40-a95b-b934d6220c8a | -9.01763 | -61.61768 | 2024-10-10 01:54:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 46.2 |
| d691c9b7-00b0-30bf-a40f-911b46822f74 | -9.00994 | -61.56313 | 2024-10-10 01:54:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6f79be32-30a7-327f-81c6-91e4fcf6d74a | -9.00866 | -61.55404 | 2024-10-10 01:54:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 78b27a9a-1edc-3839-ab28-57f7cb6efdf4 | -8.9998 | -61.62027 | 2024-10-10 01:54:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 90b3d3fc-373d-384a-b64f-364f5fe6fcbe | -2.6533 | -53.3506 | 2024-10-10 01:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 138.2 |
| c8babca8-aa1c-3cbb-a7a7-45d52c4c4cbc | -2.6716 | -53.3704 | 2024-10-10 01:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 819768c8-d036-3e3c-afd5-2197a77cc3e5 | -2.6716 | -53.3502 | 2024-10-10 01:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 392.6 |
| 209e5175-87af-3ed2-9b99-9e65e88a2502 | -2.6717 | -53.3299 | 2024-10-10 01:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| a3903bef-6f7f-37d8-a537-0bb09d25858e | -2.69 | -53.3497 | 2024-10-10 01:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 159.9 |
| ead7712e-4ffd-3dd4-9cbb-2dc3e3735731 | -2.6901 | -53.3295 | 2024-10-10 01:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 3558354e-505f-37a0-9092-8d0e052dd406 | -3.8147 | -45.4918 | 2024-10-10 01:55:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 97badaf0-4deb-3d3a-8668-e642f2fb69e8 | -4.0814 | -51.0292 | 2024-10-10 01:55:29 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| da7c70a6-e58b-3ae4-a9ec-1b05e1ebbb3d | -4.0961 | -48.2739 | 2024-10-10 01:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 153.9 |
| 8c944441-07b3-38c3-99fc-9e01eb8ad197 | -4.0962 | -48.2523 | 2024-10-10 01:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| d94ec97f-da44-39fe-9874-3ea8941ee353 | -4.0998 | -51.0285 | 2024-10-10 01:55:30 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| f000a7e7-a83a-324c-965f-3d162b98c906 | -4.1146 | -48.2731 | 2024-10-10 01:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 192.5 |
| 0854a814-4563-358e-8dbb-9ccf935eda59 | -4.1148 | -48.2515 | 2024-10-10 01:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| ddb863b7-01d4-3059-b813-369f0eaee4fa | -6.5218 | -60.0649 | 2024-10-10 01:55:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| aa2919c7-d941-30ec-9722-55162421b248 | -6.747 | -59.3259 | 2024-10-10 01:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| cdd48f8c-fcdb-3093-9941-934875321a24 | -6.7654 | -59.3252 | 2024-10-10 01:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 127.3 |
| a28212d8-b3fe-3ca1-9cf7-5a240764c39e | -6.7655 | -59.3059 | 2024-10-10 01:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| b4310e72-3e9c-3ab5-90d2-f2b1aeb0e6b3 | -6.7839 | -59.3245 | 2024-10-10 01:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 38c4e1ed-d003-3a22-a86c-0c06db26b311 | -6.784 | -59.3052 | 2024-10-10 01:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| c0a2c2a4-6371-395c-b95f-f1a9d3109caa | -8.7029 | -63.0813 | 2024-10-10 01:55:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 9a614a89-d12d-3840-9e37-5737f6cd5975 | -8.9898 | -61.6261 | 2024-10-10 01:55:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 5a099d17-91a2-3a15-b6ec-e4fd1d2085d6 | -9.0084 | -61.6253 | 2024-10-10 01:55:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| db20d564-da9c-37c3-8751-f53c84ff24cf | -9.0085 | -61.6062 | 2024-10-10 01:55:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 81e9b712-2078-3436-9970-7561a5630f7b | -9.027 | -61.6244 | 2024-10-10 01:55:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| c065f1fa-0599-386b-adf8-54cb4b5b3950 | -9.0271 | -61.6053 | 2024-10-10 01:55:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| ef71ee57-4a38-32ec-991f-0620b8902fed | -9.0656 | -61.3934 | 2024-10-10 01:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 2e08b450-b012-3f33-8c9b-dd77b4fd30bd | -9.0841 | -61.4117 | 2024-10-10 01:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| e80174b3-edd6-3ddd-a65b-693bcf2c58ef | -9.0842 | -61.3925 | 2024-10-10 01:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 120.3 |
| bb383ee4-bec9-3580-b580-7318fbcce0e9 | -9.1035 | -61.2769 | 2024-10-10 01:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| f8e5826e-027d-380c-b468-547d4539542b | -9.122 | -61.2951 | 2024-10-10 01:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 110.2 |
| a0424aa7-1cc3-3ad4-b82f-76d2c52ca479 | -9.1221 | -61.276 | 2024-10-10 01:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 299.6 |
| 19513d35-86a3-34d8-a17a-0c740f1e6fe2 | -9.1223 | -61.2569 | 2024-10-10 01:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 7c3679a9-ed21-3153-ba1b-d8840bfe6c02 | -2.67379 | -53.37115 | 2024-10-10 01:56:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 275.0 |
| d162a74a-d3be-3de7-b893-7e935ec3cdf1 | -2.67342 | -53.37808 | 2024-10-10 01:56:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 220.0 |
| f8aa3da4-fe0d-316a-890a-656dff68f0e3 | -2.6674 | -53.32964 | 2024-10-10 01:56:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 281.9 |
| 51e03c21-2b62-39fb-843d-21f8ee0af01c | -2.66731 | -53.33652 | 2024-10-10 01:56:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 369.8 |
| 4340b32a-c32b-3945-be98-cc4c077eebb1 | -2.65627 | -53.37382 | 2024-10-10 01:56:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 5cd87a27-7326-3e1a-a423-73be149137c8 | -2.65592 | -53.38084 | 2024-10-10 01:56:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 8b19157d-d6e9-3a4a-858f-7bf80e0eab40 | -2.64983 | -53.33234 | 2024-10-10 01:56:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| d327d11b-16f4-388d-b096-d824c4523f41 | -2.64974 | -53.33926 | 2024-10-10 01:56:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 407bc67c-515f-3b8b-beff-1342e6490ec7 | -1.2469 | -55.70257 | 2024-10-10 01:56:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 8d0c999e-cbc0-3e44-a153-6e39910789ec | -1.24496 | -55.69728 | 2024-10-10 01:56:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 190fa164-8a46-3cb3-8104-f4c395d7e3ad | -3.62723 | -60.20777 | 2024-10-10 01:56:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b6aaee6c-a718-3f07-b690-fd972ef44bb2 | -1.48446 | -61.60868 | 2024-10-10 01:56:00 | TERRA_M-M | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aab002c9-bb86-3072-be4e-0fe8035714ff | -3.04662 | -61.68703 | 2024-10-10 01:56:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 28.1 |
| a4d957c6-0cd9-3291-93f9-b606de757bdd | -3.04524 | -61.67718 | 2024-10-10 01:56:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 00e53f0c-6793-3eab-b983-8e4cf46afaa2 | -3.03731 | -61.68839 | 2024-10-10 01:56:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 6d8b1afa-0f7e-33f3-9c02-b61b7b0391a6 | -9.4633 | -63.1451 | 2024-10-10 01:56:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| b76fd99a-3776-3d30-ad7f-987ae23ede87 | -9.4819 | -63.1443 | 2024-10-10 01:56:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 98.9 |
| b3e81a20-c97d-3821-af99-8c8c9a00a97a | -10.363 | -55.8755 | 2024-10-10 01:56:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 37.8 |
| dfd682d2-fd72-35fe-833f-517631089f9c | -10.3632 | -55.8554 | 2024-10-10 01:56:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| ed5b8a8d-cb8e-350f-a2f2-6fd981c37fbc | -10.3707 | -61.2513 | 2024-10-10 01:56:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 045cddb1-b13e-396c-80a0-7ca5cc985bae | -10.4287 | -60.9979 | 2024-10-10 01:56:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 871aa296-e262-328e-8068-04814527617e | -11.0254 | -57.2237 | 2024-10-10 01:56:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 147.3 |
| a413082d-5c1b-3fc5-b03b-62ee2aaa9f9c | -11.0256 | -57.2038 | 2024-10-10 01:56:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 7ab3f264-ed4e-32cd-bf0e-12d43f763738 | -11.0443 | -57.2222 | 2024-10-10 01:56:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 206.3 |
| 66c9b5e8-c8ec-3abf-93a9-67e8f94a0209 | -11.0445 | -57.2023 | 2024-10-10 01:56:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 216.7 |
| 22b2f1ae-31e2-3c14-90fb-a39a06f1154b | -11.8188 | -58.8459 | 2024-10-10 01:56:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 06623013-a53b-3f1c-baa2-c571053b0ccb | -12.3987 | -54.5816 | 2024-10-10 01:56:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 6169f1e3-f882-31fa-aea0-9e3f6dbc082a | -12.4177 | -54.5797 | 2024-10-10 01:56:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| a7a0e475-43a0-306c-b581-d3b80834ccbf | -12.418 | -54.5592 | 2024-10-10 01:56:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 06a7543b-3a52-3f3c-ba1b-c98eb2550ae3 | -13.7346 | -60.6079 | 2024-10-10 01:56:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 2d03bd74-d697-3b9c-b920-137eb8d779fd | -17.0549 | -45.2808 | 2024-10-10 01:56:41 | GOES-16 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 250cc5d7-63be-32ea-ae9e-75065ce4c939 | -13.678 | -60.608898 | 2024-10-10 01:59:05 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ffec81fe-b8d4-36e5-8d9b-be674421370d | -13.6682 | -60.611401 | 2024-10-10 01:59:05 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 247c39dd-f66b-3512-ab4e-465aa6f13970 | -13.6609 | -60.623798 | 2024-10-10 01:59:06 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4ed67434-f781-328a-943f-30d3feae9830 | -12.2367 | -59.181499 | 2024-10-10 01:59:23 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ebc5e79a-8d3f-3956-bdb7-be0d99b7a930 | -12.227 | -59.183998 | 2024-10-10 01:59:23 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 13a8437f-c8f1-3540-bcb0-b032a7f3d08d | -11.7362 | -58.836899 | 2024-10-10 01:59:29 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ec9cf851-85b4-3738-bc03-72a8b7edbdbd | -11.7396 | -58.850498 | 2024-10-10 01:59:29 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d4c02f4-335e-3590-8b66-11b257a18243 | -11.7299 | -58.853001 | 2024-10-10 01:59:30 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9cceefd2-2cee-3221-9702-d72e202d6e08 | -12.6456 | -63.069901 | 2024-10-10 01:59:31 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5b5e55d6-c861-3457-83bc-a5b3b45288cf | -11.5878 | -58.904099 | 2024-10-10 01:59:32 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 806716b0-447c-35eb-884e-9bd6a0f95d20 | -10.956 | -57.200802 | 2024-10-10 01:59:35 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README34.md)
