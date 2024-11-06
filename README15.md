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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce28c1b5-90cb-3f17-8294-787a98907205 | -5.5632 | -43.6998 | 2024-11-06 01:30:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 904b30d8-846c-38ba-8939-406aa4f3d359 | -3.3284 | -50.0933 | 2024-11-06 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| c5994d6b-be7a-3239-b1e0-3eb3653db352 | -6.4827 | -47.4827 | 2024-11-06 01:30:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| ba29e52f-001d-3c0e-9ed8-a3d1fae97443 | -2.1746 | -53.6834 | 2024-11-06 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 1e7c52dc-4147-34d3-86d4-4b104c812a30 | -2.7244 | -54.1351 | 2024-11-06 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| a280f9b5-ac41-33a8-8a26-0a084092b429 | 3.6184 | -51.3162 | 2024-11-06 01:30:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 37a8f164-e469-3a76-b519-50a2d774876b | -11.7771 | -64.977699 | 2024-11-06 01:38:00 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c3c17e55-1537-37ec-9d08-ac3f2ad9ad6d | -11.7755 | -64.970802 | 2024-11-06 01:38:00 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 379519a3-c97d-319b-a15c-801b4810eb3a | -4.401 | -59.526699 | 2024-11-06 01:38:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 478ca95f-63e9-3e54-ac9c-1eeaee653826 | -13.8185 | -57.6423 | 2024-11-06 01:38:00 | METOP-B | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f586c507-4c96-372a-b239-98fefbba7083 | -3.6602 | -50.2501 | 2024-11-06 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 29e20350-26ed-3e98-a4d3-06705f5604cd | -3.1393 | -51.2069 | 2024-11-06 01:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 72e433ea-f55d-37df-a72c-3b1fd2246680 | -6.5012 | -47.5033 | 2024-11-06 01:40:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 125.7 |
| f6829d69-2676-3b88-9eb3-f485f642e76c | -4.1246 | -43.5833 | 2024-11-06 01:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 5a11fc07-af9a-3273-b12f-93f319290ddb | -2.8506 | -49.4744 | 2024-11-06 01:40:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| e945a018-b16c-3826-a651-3b56f9cefa1c | -3.1617 | -50.2038 | 2024-11-06 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 7c22ab06-5561-34ea-865d-b4cdfeea5892 | -6.1226 | -43.9809 | 2024-11-06 01:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 6062fc5a-9134-36b1-b425-80d9ae32559c | 3.6184 | -51.3162 | 2024-11-06 01:40:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 07621428-baf5-317b-904f-509824029f1d | -3.0213 | -53.2607 | 2024-11-06 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| f2eca801-195b-3f2d-ad2d-54adc4bb153e | -2.1746 | -53.7036 | 2024-11-06 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 2f1b44fd-fb82-3f5e-8c8e-cdb875787607 | -3.0397 | -53.2603 | 2024-11-06 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 28dda255-1882-38ef-b702-2ea74010cd91 | -3.2415 | -53.3967 | 2024-11-06 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 21d6cbba-67fa-3589-93da-6acf41d50869 | -2.082 | -47.0602 | 2024-11-06 01:40:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 324318f4-ff64-3a2d-bed9-195eb8609e83 | -2.706 | -54.1556 | 2024-11-06 01:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 25034816-0651-3b01-908c-5499c7b0c837 | -6.1229 | -43.9578 | 2024-11-06 01:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 8d39f3ac-df65-3235-85aa-889e44c48f09 | -2.6764 | -51.8189 | 2024-11-06 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 7da979ba-8b4b-3aa2-98b6-2df5cc139188 | -2.6764 | -51.8395 | 2024-11-06 01:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 8cb880b8-f688-3660-a1cd-a157bed4a95f | -6.5014 | -47.4813 | 2024-11-06 01:40:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 202.8 |
| c5cf2ec1-245d-3c38-a75f-abc1e765e41f | -6.5094 | -44.6847 | 2024-11-06 01:40:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 76a24bd3-9dd1-35c0-a0e4-3efd64b99916 | -3.3284 | -50.0933 | 2024-11-06 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 5ad20574-47bc-3951-b48c-f1320aebe57e | -2.8608 | -51.7731 | 2024-11-06 01:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 213.2 |
| 998a1db2-e07d-346c-8321-8b49250d5dcb | -6.1039 | -43.9824 | 2024-11-06 01:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| f046594c-1f3b-3ada-a39f-7e01c6e3df63 | -6.1041 | -43.9593 | 2024-11-06 01:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| b914f288-4fe0-389d-a58b-6ac60c4df4e7 | -4.5616 | -47.9925 | 2024-11-06 01:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| ebcd1c06-5421-326e-a00a-416711d721cf | -3.6788 | -50.2284 | 2024-11-06 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| d37d6e9b-e02f-38cf-93ca-53f216e88d4c | -2.8423 | -51.7735 | 2024-11-06 01:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| a19be73b-97a8-3e36-a036-d5530d38f749 | -2.8424 | -51.7529 | 2024-11-06 01:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| ec1f555e-884b-38fc-83c6-71877aac0e43 | -3.6603 | -50.2291 | 2024-11-06 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 1b02eace-0234-358b-b26b-2d2c3eb9650a | -6.4827 | -47.4827 | 2024-11-06 01:40:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 14ab3c7e-89af-3c4d-b5d2-9561c82899ef | -2.8065 | -51.4855 | 2024-11-06 01:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| ce044515-2cef-3544-ae00-a9566ef3d5c4 | -2.8608 | -51.7524 | 2024-11-06 01:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| dd850718-96e9-36ed-93d1-07f2d17e0a9b | -2.8064 | -51.5061 | 2024-11-06 01:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 44e0d1fb-6bd8-3495-85f5-88ba92339546 | -3.0207 | -53.443 | 2024-11-06 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| a11ddf90-4d43-3eb7-a121-9e22adc9ac33 | -3.0023 | -53.4232 | 2024-11-06 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 0365bcd3-07b0-386d-b52e-4f064944760b | -3.1616 | -50.2248 | 2024-11-06 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 0b3d738f-9206-3fea-9af2-6dee3a7b794f | -2.1746 | -53.6834 | 2024-11-06 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| eca74250-e85e-3b9c-82b6-301ed1b408ff | -6.5096 | -44.6618 | 2024-11-06 01:40:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| a9f77aff-3343-3019-8d81-610320640e1e | -2.8607 | -51.7937 | 2024-11-06 01:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 72cc351b-ec36-31de-9125-6bd3d4e7105d | -3.1213 | -51.1036 | 2024-11-06 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 8bef4253-5f06-3f9b-be08-ecdf5ec18c4d | -6.4906 | -44.6862 | 2024-11-06 01:40:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| edca0630-b59b-33f9-99f0-f4a5c5a689af | -3.9669 | -48.1716 | 2024-11-06 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 10080635-ad5b-3d26-8c14-bfcf8db198cd | -4.1432 | -43.5822 | 2024-11-06 01:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 71204d1a-df10-3fcb-8dc6-bd209e3cc69d | -2.7243 | -54.1552 | 2024-11-06 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 3b0103ff-16d4-3f3b-b15c-a34045884d8c | -6.4825 | -47.5046 | 2024-11-06 01:40:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 979c12ea-ec79-3102-8846-689ca23a79de | -4.5614 | -48.0141 | 2024-11-06 01:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 488c17ea-83e2-340a-b00a-2412e320ebef | -3.1394 | -51.1861 | 2024-11-06 01:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| a67c06f8-87b7-3f75-a7a1-38e4592b434e | -2.8423 | -51.7942 | 2024-11-06 01:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 38eceeda-be18-3391-bd3d-b48e5468bc39 | -6.1414 | -43.9794 | 2024-11-06 01:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 369db6d8-99ad-3d2d-9922-637f060041ca | 3.6 | -51.3168 | 2024-11-06 01:40:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 0943bebe-f742-33e6-9b5e-2cc06fc5592a | -2.7244 | -54.1351 | 2024-11-06 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 3e7118b5-e4b7-304e-8027-6e9a7375bd76 | -3.0207 | -53.4227 | 2024-11-06 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 43f1df83-dcb4-3ec7-90a9-ab8e9d5877b3 | -5.5445 | -43.7012 | 2024-11-06 01:40:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 4766d27c-c099-39dc-a9cc-a3aaa8df8de9 | -3.967 | -48.15 | 2024-11-06 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 35734615-a128-38ae-93a0-550e8a0c77ca | -3.2054 | -53.2153 | 2024-11-06 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| dd07c5ae-d0ce-3df0-9bb6-9867d4067960 | -3.0396 | -53.2805 | 2024-11-06 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 8a46e199-0dca-32ea-b589-f54a090fdf30 | -3.3285 | -50.0723 | 2024-11-06 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 5dbbb1e9-f1c6-3b62-8cd0-5f11617a13de | -4.5614 | -48.0141 | 2024-11-06 01:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| e1bdf321-fd26-3fc8-a781-c4bca71a0d3f | -2.8423 | -51.7735 | 2024-11-06 01:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 159.6 |
| c81c561c-2de3-39e7-ae27-8619ff02e2b4 | -2.8065 | -51.4855 | 2024-11-06 01:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 724701c4-9f92-34af-896e-cbf5bed084bd | -3.5447 | -47.3636 | 2024-11-06 01:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| f2bf08f7-10a0-30c5-91f6-c2462c5629cc | -6.5094 | -44.6847 | 2024-11-06 01:50:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 121.5 |
| f0fd32df-854d-344c-a19b-fd1eb04d44e4 | -6.4825 | -47.5046 | 2024-11-06 01:50:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 6aa566e0-f67c-33df-beec-2f4ca9e228e2 | -4.858 | -42.9566 | 2024-11-06 01:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| d0f12c48-3bd8-3f61-99ad-1367c870a3de | -6.4909 | -44.6633 | 2024-11-06 01:50:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 575db20c-60ef-3f14-9d4d-0a2b3b45682f | -6.1226 | -43.9809 | 2024-11-06 01:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 139.5 |
| ea0cf978-6327-39a2-9f80-a9bff1324230 | -3.1393 | -51.2069 | 2024-11-06 01:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 5efa53f3-7d76-3165-a4a6-39b7b6cb819f | -3.3284 | -50.0933 | 2024-11-06 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 6d4cd6a4-2c03-351c-87f0-aa1fe0c7f1a3 | -3.1616 | -50.2248 | 2024-11-06 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| c5a5850d-b666-38f0-9bcf-46ec8acbca8d | -3.1213 | -51.1036 | 2024-11-06 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| bad1c537-c319-37d0-bfec-dc804799a052 | -6.1041 | -43.9593 | 2024-11-06 01:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 8e7829e7-071d-36b0-b1b2-f0ef6a820136 | -5.5632 | -43.6998 | 2024-11-06 01:50:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 073cd804-ac48-392f-baeb-1294e77894eb | -6.4906 | -44.6862 | 2024-11-06 01:50:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| fdfda66b-db7c-3936-86d8-b4bdc93bd5c8 | -3.0212 | -53.281 | 2024-11-06 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 812b9a3f-c07d-3c0a-9121-27d052876a18 | -3.5304 | -50.3597 | 2024-11-06 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 0ae34cf5-a98d-3694-99e2-4310f008701d | -2.8424 | -51.7529 | 2024-11-06 01:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| afbb4496-2083-3b97-9fe1-9f6cc855f2cd | -2.6764 | -51.8189 | 2024-11-06 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 1200eda3-c4e5-385b-b8f7-4cd0ddfd45c3 | -3.0023 | -53.4434 | 2024-11-06 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| c3dfe5e8-4d70-3738-ab10-9034c972f6f1 | -2.706 | -54.1556 | 2024-11-06 01:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 461343dc-3e6a-304c-a959-ff921771a69c | -3.1802 | -50.2032 | 2024-11-06 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 8f55d3f1-5ec9-38e2-8117-b7d32be6203c | -2.082 | -47.0602 | 2024-11-06 01:50:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 574c626e-3665-30b4-9b1d-5d78b4d38cd3 | -6.4827 | -47.4827 | 2024-11-06 01:50:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 76d8d14d-cee7-3f9a-8d02-f8c834fa4d7f | -3.0023 | -53.4232 | 2024-11-06 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 405b5e63-1e4e-3017-9f95-dd91764f6483 | -2.7244 | -54.1351 | 2024-11-06 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| ad4a02db-21ba-3e11-88ab-aacd87215711 | -3.1617 | -50.2038 | 2024-11-06 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 78fa706c-38d8-300c-9ea4-83d8fa1f8e5b | 3.6 | -51.3168 | 2024-11-06 01:50:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 4404e25c-1e68-3942-97cd-a795d2bb1b88 | -4.1432 | -43.5822 | 2024-11-06 01:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 131.1 |
| ca87765b-d1d5-35bc-9f2b-9b5542a8c4ed | -3.1759 | -51.2681 | 2024-11-06 01:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| da082c85-9103-3613-88bb-fe9ad44ea78b | -2.8608 | -51.7524 | 2024-11-06 01:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 905f9516-5a20-31b0-aea7-5e3caedb905f | -2.1746 | -53.7036 | 2024-11-06 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 2701f28c-f54f-36c0-9c30-97ff9eb77e13 | -3.3285 | -50.0723 | 2024-11-06 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |


[Clique aqui para ver as próximas entradas](README16.md)
