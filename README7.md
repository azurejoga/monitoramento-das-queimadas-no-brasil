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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce87ef10-5a7e-3881-b3d1-f8571792b724 | -3.2349 | -50.3695 | 2024-11-06 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| ddd8f700-8096-3079-96ba-cb7ab11fc078 | -3.6603 | -50.2291 | 2024-11-06 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| ee8a101b-0c8c-34ea-82b5-4900da0712d0 | -2.8065 | -51.4855 | 2024-11-06 00:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 0e2252ba-8183-3ec6-8ef6-f4c05754acfc | -2.138 | -53.6639 | 2024-11-06 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 96fde14a-7f2a-3b67-adaa-e3586b7db206 | -3.2163 | -50.391 | 2024-11-06 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 3ad4fed9-a9e1-3d47-b4b8-e4007e0fc3cf | -3.1213 | -51.1036 | 2024-11-06 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 818eb4ed-e51a-3a29-8ca7-e725cd70dab8 | -6.1039 | -43.9824 | 2024-11-06 00:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 778445d5-1182-3a8c-a5aa-7c3d4858f9f1 | -3.0396 | -53.2805 | 2024-11-06 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 51fb70af-f95f-3ddc-94d3-fdd7ebd2f6eb | -6.4827 | -47.4827 | 2024-11-06 00:50:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 166.7 |
| d2a6e7f1-0edc-3bcb-9d8f-654e2ed2f1eb | -2.1563 | -53.6838 | 2024-11-06 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 937f220c-4449-3376-9a8f-c9265f4190f9 | -3.1393 | -51.2069 | 2024-11-06 00:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| b6f8b801-1f72-34a7-8331-456fb3109802 | -2.7243 | -54.1552 | 2024-11-06 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 7f97875b-23e0-346c-8d62-0ec3c3b0e7d8 | -3.6788 | -50.2284 | 2024-11-06 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| afab1425-71cd-322c-95c9-88a46b3096ce | -0.8539 | -52.8501 | 2024-11-06 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 0df936b3-5999-3625-8078-cec8b8f07efe | -6.1226 | -43.9809 | 2024-11-06 00:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 164.6 |
| f39a477e-03bf-3446-acf1-e1c8f0c4581a | -6.1041 | -43.9593 | 2024-11-06 00:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 124.8 |
| c2390e26-0468-3173-8ffd-f95f1cc60d06 | -23.9306 | -54.0564 | 2024-11-06 00:50:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 130.6 |
| 0d7d65c0-a65c-3f30-a411-ffcb980d7c1b | -6.5012 | -47.5033 | 2024-11-06 00:50:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 156.6 |
| e72c2839-aae7-3922-8612-ddb5a56303b1 | -2.7244 | -54.1351 | 2024-11-06 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| a10364db-2545-3ef1-9f75-e7910fe2d95f | -3.0023 | -53.4232 | 2024-11-06 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 1b0beb3e-40ce-33cf-ad9d-5b2e184246bd | -6.1416 | -43.9563 | 2024-11-06 00:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 37168834-3c93-363c-94f4-2991bc20d2ff | -3.0207 | -53.4227 | 2024-11-06 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| f143c09f-a54f-3383-b88c-a71e66c40601 | -23.9512 | -54.0744 | 2024-11-06 00:50:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 91.4 |
| 7a181fdd-2083-3820-9324-001fee20c57f | -3.7068 | -41.6758 | 2024-11-06 00:50:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 52.2 |
| c3f798a5-4d9d-3ea2-a6f1-c3facda9df50 | -2.706 | -54.1355 | 2024-11-06 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 2e0d27d0-4504-37f1-a459-1fdf37f6cd2e | -4.1431 | -43.6054 | 2024-11-06 00:50:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 0f4b98f0-4b96-3aaa-b24a-f7802816e66a | -5.5632 | -43.6998 | 2024-11-06 00:50:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 58488c88-0366-3956-bc0d-fc3a65b36f99 | -6.4909 | -44.6633 | 2024-11-06 00:50:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 9ef52f2d-729b-3f9f-8409-b4383b0b8c0f | -3.0023 | -53.4434 | 2024-11-06 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| a77fdfda-b0c1-30a9-851e-1c3ecb10f8b2 | -4.0674 | -53.9371 | 2024-11-06 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 3e335687-df7d-38b3-b06c-81fa9269e30f | -2.6764 | -51.8189 | 2024-11-06 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 15bb52f4-3130-3595-afee-33919cba20b3 | -5.6563 | -45.9244 | 2024-11-06 00:50:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 397e2acd-f9b6-31e9-be08-affc1c17d940 | -2.706 | -54.1556 | 2024-11-06 00:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 78685389-32d8-3d84-8e03-c9a82011f2fc | -2.1747 | -53.6633 | 2024-11-06 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 3ef25cbd-f162-338b-8fa8-de6e7a663250 | -4.2166 | -53.5483 | 2024-11-06 00:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| d79be3ea-4440-3927-8f17-ea848db12ada | -3.967 | -48.15 | 2024-11-06 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 18d56f26-628a-3b04-ad5d-c3d331a9acfa | -3.2348 | -50.3904 | 2024-11-06 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 600ae113-055a-382d-936d-5fe815735360 | -5.6748 | -45.9456 | 2024-11-06 00:50:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| e6aea152-ed14-3a82-87fa-622f3ec4028a | -2.1746 | -53.6834 | 2024-11-06 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| de2bafb6-cd13-30ae-bbd7-6e3c3dc15947 | -3.7066 | -41.6997 | 2024-11-06 00:50:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 59.2 |
| 9db6353b-f884-31ab-994d-4448910b67e8 | -2.7639 | -53.2265 | 2024-11-06 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 7e5ae836-77fc-3481-b655-d004dddf23e4 | -6.5096 | -44.6618 | 2024-11-06 00:50:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| e12154e4-fe79-3464-b557-eda90ff049e1 | -5.6561 | -45.9468 | 2024-11-06 00:50:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 33e45962-61db-370c-8952-e3f269e215d5 | -23.93 | -54.0787 | 2024-11-06 00:50:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 151.8 |
| aeb1026a-0cbf-352e-a75a-92760732ff9f | -6.5094 | -44.6847 | 2024-11-06 00:50:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 9159fa5c-4932-3a5d-bfda-d356ff63f351 | -3.7254 | -41.6987 | 2024-11-06 00:50:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| 14f5d17e-285c-3d69-bce6-d983ffa2b3eb | -3.0212 | -53.281 | 2024-11-06 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| e3802afa-1c55-33d2-a2cd-0fc183faedd1 | -3.5262 | -51.3193 | 2024-11-06 00:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 6185ddac-c271-3f05-92b1-44a06cc10aea | -2.6764 | -51.8395 | 2024-11-06 00:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 86d2f6c8-315b-3954-b3f6-918b4170eded | -3.0207 | -53.443 | 2024-11-06 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 6e40bc73-a001-3137-9f3a-864f07de30cd | -6.1414 | -43.9794 | 2024-11-06 00:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| de6d014b-0f0d-3b64-bf99-106b09fb5606 | -3.1212 | -51.1244 | 2024-11-06 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 6ce949d9-3541-3c41-acff-e2d0bb943b1b | -6.5014 | -47.4813 | 2024-11-06 00:50:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 271.7 |
| 24e92daa-fb0c-3797-9c13-6c306ea21b7a | -4.1246 | -43.5833 | 2024-11-06 00:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 237.6 |
| 047f7322-d104-3e58-920d-76891fd10e8e | 3.6184 | -51.3162 | 2024-11-06 00:50:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 82.3 |
| fe635bf7-6daf-37f5-be95-577129019311 | -2.3999 | -46.1699 | 2024-11-06 00:50:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 18b59e79-ec59-3377-88f8-8116f965367a | -4.1432 | -43.5822 | 2024-11-06 00:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 249.4 |
| 61fd66a4-cc60-3b75-b6b1-4e93d036fd22 | -4.0667 | -46.9246 | 2024-11-06 00:50:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 1158d272-b055-355c-89a0-428988fa39d7 | -0.8539 | -52.8298 | 2024-11-06 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 7be9f9d1-93d4-3172-8571-590ed6f314c5 | -4.1434 | -43.5591 | 2024-11-06 00:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| a11b2799-8ee6-37f9-a7cb-fb55517e50a3 | -6.4825 | -47.5046 | 2024-11-06 00:50:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| cfd13e49-a90f-30db-9398-dcc8a2ffef52 | -3.7255 | -41.6748 | 2024-11-06 00:50:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 51.4 |
| 65a684c7-fdb1-3c82-9d8c-309bc64e055b | -6.1395 | -43.9548 | 2024-11-06 00:54:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a55a9099-cc7c-34f6-940a-c545e55de35f | -4.2774 | -50.714699 | 2024-11-06 00:54:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 118b9127-c3aa-3ae4-8e72-0711c28b0a51 | -4.5524 | -48.008301 | 2024-11-06 00:54:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51bf92ec-95f4-3918-a06a-863fe272d3a8 | -2.6077 | -54.541199 | 2024-11-06 00:54:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8574df9e-ff30-368b-9554-4dfcaed997f8 | -2.4516 | -49.028198 | 2024-11-06 00:54:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e300675-ff0a-3a60-bbe2-6f240818a6a0 | -2.9343 | -52.542099 | 2024-11-06 00:54:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ac37b3a-8531-3636-89d1-af1a2bdf09a4 | -3.2453 | -53.404499 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 848cfefb-68d9-3e91-8d4a-8e83b8e3ff94 | -3.5299 | -51.319801 | 2024-11-06 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f9a966c-8c32-3c33-a1f6-aee9da37903b | -2.8522 | -51.781399 | 2024-11-06 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9393b6be-03db-3c0b-8ab9-24017d51c911 | -4.245 | -48.541401 | 2024-11-06 00:54:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46d8caf8-f885-3439-8ead-7f8d47345fee | -4.0768 | -48.308601 | 2024-11-06 00:54:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4b66bbd-f77d-36c1-8bc1-a56417998337 | -2.4347 | -53.9188 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b2c7129-0b66-38ff-90ae-f4748d9f4c77 | -6.4955 | -47.502499 | 2024-11-06 00:54:00 | METOP-C | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 013a3835-2de9-31ac-857f-9dafe529d5d3 | -2.7839 | -52.875999 | 2024-11-06 00:54:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b63253dd-0f83-3a37-b311-a4527629bfaf | -3.9606 | -48.165699 | 2024-11-06 00:54:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a647046f-2c55-3f6a-827b-61f95b5d4559 | -2.9466 | -54.128799 | 2024-11-06 00:54:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79259d09-2fea-3b7b-8815-edd293df8f42 | -0.8541 | -52.828201 | 2024-11-06 00:54:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca298bf2-f6bd-3b44-80e3-ae6fd0f1992f | -2.9553 | -53.7155 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fffa0a3d-0270-3602-b517-18e8b3708c8a | -6.1298 | -43.9571 | 2024-11-06 00:54:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 674b7d5f-ea27-3dbf-b54a-95c36051635b | -3.0587 | -51.066399 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc6d3ab7-6644-362b-b462-966822f9551f | -23.942499 | -54.073799 | 2024-11-06 00:54:00 | METOP-C | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a62e5c63-c3c3-3284-816f-c7108d78ed9d | -2.3917 | -50.3237 | 2024-11-06 00:54:00 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96647746-46a3-3307-b001-0f9a0e05c4ba | -4.4475 | -50.691299 | 2024-11-06 00:54:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 039a3cd7-e381-32e0-a7fe-d8c8b2f52865 | -2.8305 | -52.944302 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0375ab86-f3c9-322b-8cbd-e366cdf3fd3f | -5.2352 | -48.147999 | 2024-11-06 00:54:00 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 36184fdd-6134-3258-b524-65b04b78438a | -6.4909 | -47.483002 | 2024-11-06 00:54:00 | METOP-C | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1f154990-d19b-3db6-a5c7-14e63ba96794 | -2.4801 | -53.9818 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9683b6d9-3b71-3faa-8e86-39b99103ff8a | -3.5283 | -51.312698 | 2024-11-06 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e41ed9b9-d524-39b0-ad2e-4d52113c042f | -3.229 | -50.3759 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f1c433c-b1b3-3f58-9ef5-a6d5cf5047a7 | -6.4983 | -47.471001 | 2024-11-06 00:54:00 | METOP-C | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9cd310a3-ff2d-3edd-a61c-bff98789391e | -2.9707 | -53.872799 | 2024-11-06 00:54:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39a6488a-6de5-32a1-a361-d38ac09a5c77 | -0.3539 | -51.4146 | 2024-11-06 00:54:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 40e87005-d8b0-3be4-8e5a-bfdd0c901c49 | -3.0991 | -53.7127 | 2024-11-06 00:54:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 994bd746-4e51-33f6-9ba1-48bac8f4b547 | -2.1654 | -53.688301 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abc199db-d0a4-35ad-800b-29e764edb633 | -3.0231 | -53.425098 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e8e9af0-4ab6-3d83-8cb9-c21bcb6efe08 | -4.1337 | -43.6063 | 2024-11-06 00:54:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f2cd1142-5867-352c-b529-04ba88e12b68 | -2.1685 | -53.702 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c56d124-b6d2-35d2-b231-21c89327add9 | -3.1571 | -50.1991 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
