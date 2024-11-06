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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 385d61d4-7c7b-3df5-a0e0-09b034e28708 | -3.1393 | -51.2069 | 2024-11-06 02:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 6092ce35-3690-32f5-bb94-8e1bb5859a62 | -2.9186 | -51.047 | 2024-11-06 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 1ca80139-9a89-3fce-bb3e-d008d407c645 | -2.9371 | -51.0465 | 2024-11-06 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| f0eebb72-3642-39e7-9071-143833033461 | -2.8423 | -51.7735 | 2024-11-06 02:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 147.6 |
| 6938b4d6-5d02-3f71-96bf-067a6c3cec0e | -7.3601 | -72.919601 | 2024-11-06 02:36:00 | METOP-C | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d5cbefa5-046d-3bf1-a120-ee76f72a9c41 | -2.8506 | -49.4744 | 2024-11-06 02:40:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 040ff446-f2cb-3037-b7d2-144fc9044ae0 | -2.9186 | -51.047 | 2024-11-06 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 7b2517b3-7b79-3e0d-a2f6-b495dca350cf | -4.1432 | -43.5822 | 2024-11-06 02:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 91d28694-93dd-3711-ad67-847b6954c50d | -6.4827 | -47.4827 | 2024-11-06 02:40:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 4ecc4a3b-28fc-34ba-ad71-cfd2391440ca | -6.5012 | -47.5033 | 2024-11-06 02:40:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 165.6 |
| bd24baf1-b1e4-3ac2-ba60-24c5046f69a3 | -3.0213 | -53.2607 | 2024-11-06 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 3d891691-fb47-3338-af87-651c25bab52b | -3.5447 | -47.3636 | 2024-11-06 02:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 120.1 |
| 2e36976b-c135-3220-9fa2-c9b17c258500 | -3.1393 | -51.2069 | 2024-11-06 02:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| c171a05f-78ce-3c38-ba03-dc2a39e3d236 | -2.8423 | -51.7942 | 2024-11-06 02:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| c606c2b9-997f-3414-9977-a437f2203752 | -6.5014 | -47.4813 | 2024-11-06 02:40:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 219.4 |
| e95e9a41-abbe-381e-b978-12a37a9f1987 | 3.6184 | -51.3162 | 2024-11-06 02:40:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 82.4 |
| fa63e45d-2d8f-3591-bc69-86169ff51c3e | -3.2348 | -50.3904 | 2024-11-06 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| cba8561d-f2e5-3d46-8468-6bb1ee662eb8 | 3.6 | -51.3168 | 2024-11-06 02:40:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 7b227f49-070c-3c11-b13b-cd60cf4dd80c | -2.8608 | -51.7524 | 2024-11-06 02:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 3bfb9e85-2fda-3db3-b18b-7945adb5353c | -3.1617 | -50.2038 | 2024-11-06 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 8b29abe4-b747-3375-9fdd-51b111c06b0d | -3.2164 | -50.3701 | 2024-11-06 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 4e3d01dc-ec3e-3d83-af59-d41b1c2d1c87 | -3.0023 | -53.4232 | 2024-11-06 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 32bb1263-4e51-36d7-9aa5-22ff3dc579cc | -2.8064 | -51.5061 | 2024-11-06 02:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 58825d8d-a2cf-3b8f-b4d3-a4057758dc68 | -3.0397 | -53.2603 | 2024-11-06 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| de02b6b1-cde2-3b07-b45e-b49338874af5 | -2.8065 | -51.4855 | 2024-11-06 02:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 087b00fb-8839-3d84-8ae3-536010b404e7 | -2.706 | -54.1556 | 2024-11-06 02:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 817cc9ef-7982-3c63-b55d-f1fb28585358 | -3.6603 | -50.2291 | 2024-11-06 02:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 31be9568-f93f-3c37-a383-2b09ff421ff8 | -6.4825 | -47.5046 | 2024-11-06 02:40:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 4b353a3a-dd7d-3d6c-8a77-d2954eea2518 | -2.9185 | -51.0678 | 2024-11-06 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 121d2b0d-f64d-3636-8cfe-d9779cb2fd46 | -3.5631 | -47.3847 | 2024-11-06 02:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| bd292556-fc48-3649-952e-b2154c5d6050 | -6.4906 | -44.6862 | 2024-11-06 02:40:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| f4d11da1-fb75-33cb-9b89-7295ef7ed9e4 | -3.0607 | -52.5066 | 2024-11-06 02:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| a4565bf5-c1c1-311a-a5d2-283ec224469f | -3.5261 | -47.3644 | 2024-11-06 02:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 3e46b8e6-e9e0-3405-b3a4-77bab7e58a62 | -4.5614 | -48.0141 | 2024-11-06 02:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 52b279e9-bba9-37c0-a16e-54cc852365a9 | -3.0207 | -53.443 | 2024-11-06 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| b923e915-e1ea-38f9-814b-26aabd598b98 | -4.1247 | -43.5601 | 2024-11-06 02:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 74005271-b097-396e-94ad-e00600062db4 | -3.5444 | -47.4073 | 2024-11-06 02:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 73724177-01fc-35b3-8c5a-c8348396da7c | -3.1616 | -50.2248 | 2024-11-06 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 299af25d-0f8d-3ad2-a9e7-44915943944c | -3.5446 | -47.3855 | 2024-11-06 02:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 331.2 |
| f6aa67c2-2c2f-34c8-a6a3-35f2a76d81b7 | -2.8423 | -51.7735 | 2024-11-06 02:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 2f2e6750-3b85-32fb-9ac0-a6cc22903270 | -3.0396 | -53.2805 | 2024-11-06 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 4422ab71-449e-30c7-806c-45d39daf0999 | -2.8608 | -51.7731 | 2024-11-06 02:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 186.9 |
| 7a8ff523-fa03-3157-94e3-9fde347d728a | -2.6764 | -51.8395 | 2024-11-06 02:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 6c2c70bf-3794-39d1-a64b-4eb2a556fb41 | -3.4859 | -52.1049 | 2024-11-06 02:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 5efc9e88-186a-3774-870b-b5675d80b145 | -3.6788 | -50.2284 | 2024-11-06 02:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 8c85a56f-4632-3aab-aa3f-20be0e018b8b | -3.526 | -47.3862 | 2024-11-06 02:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| d377d615-2a9d-3301-bd5f-ff01f08fc25b | -3.2349 | -50.3695 | 2024-11-06 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 88dcb662-40b6-3f47-a1e1-6b39a7cabbb3 | -6.5094 | -44.6847 | 2024-11-06 02:40:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 191caf18-4c53-30fc-b9ca-376063ab77c3 | -2.9187 | -51.0262 | 2024-11-06 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 4c71c866-aa80-3f5f-9d66-cb839f3c238d | -3.0794 | -47.7727 | 2024-11-06 02:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 3ab70525-60d6-3344-ba26-76cbb00fbc1b | -3.1213 | -51.1036 | 2024-11-06 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 677038fd-5866-306b-ba84-d57e7ed7c529 | -3.2163 | -50.391 | 2024-11-06 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 6d73b857-1070-307a-8809-168493190cc6 | -6.5096 | -44.6618 | 2024-11-06 02:40:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| c4b4a530-a254-3cb2-8043-c3cd000dc5fd | -2.9371 | -51.0465 | 2024-11-06 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 8bdc2812-02eb-3dd8-9066-4b18ddbba08f | -3.0023 | -53.4434 | 2024-11-06 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 4814dba4-ed1f-3a38-bb8d-1907fa5d2ec9 | -4.1246 | -43.5833 | 2024-11-06 02:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 89afe10f-f33d-3587-9ee5-ff8df9f26c81 | -2.8607 | -51.7937 | 2024-11-06 02:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| bf5cf1df-8938-3539-80c8-1fd62ba3ac8a | -3.0207 | -53.4227 | 2024-11-06 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 76c5d92f-4c35-318a-837a-4e1824be9590 | -2.7244 | -54.1351 | 2024-11-06 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 2fbd038a-b421-3180-a46b-89b141a0292a | -2.937 | -51.0673 | 2024-11-06 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 6e0a5a08-2e1c-3469-8c8d-e0dc734bc157 | -2.7243 | -54.1552 | 2024-11-06 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 7a4dd6fa-c694-3f91-91de-7a62457315ec | -2.6764 | -51.8189 | 2024-11-06 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 1840853d-3bd6-3b42-89e6-c7f4001e9e3f | -6.5094 | -44.6847 | 2024-11-06 02:50:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 123.7 |
| ac7fd99c-3450-3be4-8f0a-aa0600198bed | -3.0207 | -53.4227 | 2024-11-06 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| ada8527c-0198-3a20-9a9a-2737eef12f1a | -3.6788 | -50.2284 | 2024-11-06 02:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| ac1635c0-e120-39db-b323-c9adb96ddb13 | -2.937 | -51.0673 | 2024-11-06 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| a263c72a-6f99-3484-96d7-b528d3031238 | -6.5012 | -47.5033 | 2024-11-06 02:50:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 141.9 |
| f7128495-25d2-36b2-9578-8c1beb5e0a6f | -2.9186 | -51.047 | 2024-11-06 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| b04b943a-27cf-36f9-b437-59c95185e5d7 | -6.4827 | -47.4827 | 2024-11-06 02:50:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 7253e893-e543-36c7-ba9d-1c268169d7a8 | -4.1244 | -43.6064 | 2024-11-06 02:50:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 484d154d-ab84-3db8-9553-2d4b67fbe4b2 | -3.6603 | -50.2291 | 2024-11-06 02:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| ff284b44-750b-31e7-8fbb-e806b9f572a1 | -3.5444 | -47.4073 | 2024-11-06 02:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 9cedcee5-4ab4-30a1-95f2-77c6f7e2bbd6 | -4.1246 | -43.5833 | 2024-11-06 02:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 221.8 |
| 404f733a-28e1-3f29-a687-c806a6c06c4f | -3.5447 | -47.3636 | 2024-11-06 02:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 18cef870-380d-3154-9efd-6d8edf783ef7 | -6.5014 | -47.4813 | 2024-11-06 02:50:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 234.4 |
| eed3b4f9-8be8-34f0-9495-aea06cff2013 | -6.4906 | -44.6862 | 2024-11-06 02:50:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| db3d0443-1be2-3f4a-b732-fc5041bde075 | -2.8423 | -51.7942 | 2024-11-06 02:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 40bf4784-0e8c-3789-accb-d417339aa28c | -3.1213 | -51.1036 | 2024-11-06 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 683f14bc-f1e1-3caa-bc8c-9c5dbd5cda33 | -3.2349 | -50.3695 | 2024-11-06 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 2548d4e6-da59-3a5a-a1ba-7c44a41e987a | -2.8506 | -49.4744 | 2024-11-06 02:50:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 4a132b41-3344-3be0-b53e-62a05ee08517 | -3.1393 | -51.2069 | 2024-11-06 02:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 9e961c11-6511-3c0c-9b26-c2731e961ef2 | -2.8064 | -51.5061 | 2024-11-06 02:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 533f8ca9-dfb1-3ab8-a1c4-ace1b6bfd131 | -3.2348 | -50.3904 | 2024-11-06 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 7797a028-0d8c-3109-93bc-68e655d3568d | -3.0023 | -53.4232 | 2024-11-06 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| e6fcfbb8-6038-38b5-991c-3d1ed3c267cf | -2.9371 | -51.0465 | 2024-11-06 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| d0d720de-4200-3d02-993d-c706ebfbb779 | -3.0607 | -52.5066 | 2024-11-06 02:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 214aaa11-2cd0-3470-a032-7850248f651f | -3.0609 | -47.7733 | 2024-11-06 02:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| cfe09e47-410c-3c0a-8546-9236b818c177 | -2.8608 | -51.7524 | 2024-11-06 02:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 1d953522-a292-390f-b3ad-4e6d6e1ce453 | -3.0023 | -53.4434 | 2024-11-06 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 51dde5e9-2507-3532-bb45-c34493a79efe | -3.0397 | -53.2603 | 2024-11-06 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 69d1317f-88b9-3e64-999c-28db6668c770 | -2.8607 | -51.7937 | 2024-11-06 02:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| df5f4aaf-6d96-3de8-86df-42148b936200 | -3.5631 | -47.3847 | 2024-11-06 02:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| d0859189-3e81-39a1-a754-ef32901f2219 | -3.2163 | -50.391 | 2024-11-06 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| e203eea7-465e-3528-beec-75a09ef182b8 | -3.1617 | -50.2038 | 2024-11-06 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| e5fdda07-028f-307c-9123-75aed91e7d52 | -3.2164 | -50.3701 | 2024-11-06 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 0e443f3d-d3c6-3a07-948d-ac3e1cfe8aa1 | -4.1432 | -43.5822 | 2024-11-06 02:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| a183704e-79d5-3776-b451-dc5ab694b2a7 | -3.0396 | -53.2805 | 2024-11-06 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 63f3ec30-fd2e-30f4-95e9-c36a81d82151 | -2.6764 | -51.8395 | 2024-11-06 02:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 8be0b659-a49a-3804-b9e3-4f326ab28d21 | -2.9185 | -51.0678 | 2024-11-06 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 8e48f742-70ed-3799-a234-8c32e2590ae8 | -3.0213 | -53.2607 | 2024-11-06 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |


[Clique aqui para ver as próximas entradas](README20.md)
