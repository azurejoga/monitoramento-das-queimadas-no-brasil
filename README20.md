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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce5d3211-b5b6-39db-82f4-c107f9a70e5b | -2.7243 | -54.1552 | 2024-11-06 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| c6e4a6b9-7f76-3309-9a7c-e3873f537795 | -2.7244 | -54.1351 | 2024-11-06 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| e78786ab-d25e-38ad-a2c0-51c20a175231 | -6.1229 | -43.9578 | 2024-11-06 02:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 05d7a1ae-2767-3eb5-bb59-44830de74a5c | -2.8424 | -51.7529 | 2024-11-06 02:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| c81b7a37-f96f-3c71-8aec-406a279ef385 | -3.526 | -47.3862 | 2024-11-06 02:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 6de0eb18-6e4f-3ef7-b419-7961ee7ea822 | -3.0207 | -53.443 | 2024-11-06 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 3dfe3304-b8c9-37be-bb1f-f0e78d9767d3 | -3.5446 | -47.3855 | 2024-11-06 02:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 38406cd0-767b-3ea7-a39c-beac5da14766 | -2.8423 | -51.7735 | 2024-11-06 02:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| b9c7d2e0-4303-3105-b743-b7a64e3f6efa | -6.1041 | -43.9593 | 2024-11-06 02:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| fe43960f-24c4-37e6-8030-88ab92ae907d | -2.9187 | -51.0262 | 2024-11-06 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 1c61b52e-2ed2-376f-ba9b-6077f1e4cb9f | -6.4825 | -47.5046 | 2024-11-06 02:50:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 8518b536-9ce6-3901-a5c9-6ffb7cb8707c | -2.6764 | -51.8189 | 2024-11-06 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 1c776eb4-3ee6-3fee-9a0e-7bc9f360574f | -2.8065 | -51.4855 | 2024-11-06 02:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 581a3997-27b6-3417-a0a5-37346930032a | -2.1746 | -53.7036 | 2024-11-06 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| da8b64e1-94e1-3ed9-baca-fec40a54cecb | -6.1226 | -43.9809 | 2024-11-06 02:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 164a5f77-45b7-3a7b-b13b-0124e3d3dce9 | -3.1616 | -50.2248 | 2024-11-06 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 3febbec4-b0a7-3e06-8c94-78ca608ac45c | -6.1039 | -43.9824 | 2024-11-06 02:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 78a6d7c4-d666-3bd9-8847-e3f6351bd992 | -3.0212 | -53.281 | 2024-11-06 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| c25dfc72-192d-3334-9c4a-d4d8020b66a4 | -2.8608 | -51.7731 | 2024-11-06 02:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 160.7 |
| 2f29b013-0904-30c4-999e-2cc4029e2ce0 | -7.4714 | -34.82795 | 2024-11-06 02:55:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| de22bc2f-2ef0-3b13-a660-4240c69519a8 | -7.47215 | -34.82384 | 2024-11-06 02:55:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 25.4 |
| e7f50792-7ea1-33ed-b246-3d9f7979b396 | -7.47363 | -34.81584 | 2024-11-06 02:55:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| d5b15935-4aa6-3468-886b-bfac27f91430 | -7.85533 | -35.04851 | 2024-11-06 02:55:00 | NOAA-20 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c1d46fbf-3579-342e-9477-1ed66c0d9252 | -7.47064 | -34.83207 | 2024-11-06 02:55:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 792fc177-b6f2-3571-8611-5c986c11c3ed | -7.4729 | -34.81977 | 2024-11-06 02:55:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 25.4 |
| 08e16867-64dd-3654-9ca9-67b67a5a9af4 | -7.85609 | -35.04445 | 2024-11-06 02:55:00 | NOAA-20 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 497ab37e-1ad1-3e4d-a84f-8bb227d0f425 | -7.46987 | -34.83624 | 2024-11-06 02:55:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fd194785-fe85-36ac-9630-95507d4ef5d4 | -10.74585 | -37.51759 | 2024-11-06 02:57:00 | NOAA-20 | CAMPO DO BRITO | SERGIPE | Brasil | 2801009 | 28 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7b0466dc-58f8-3e9c-a19c-a13597ed924c | -6.4906 | -44.6862 | 2024-11-06 03:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 4b40d0ce-bf3a-3139-99a9-aabc4d71e028 | -2.9187 | -51.0262 | 2024-11-06 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 2eef735d-cde9-3303-80ba-dfe9b75c106e | -3.1616 | -50.2248 | 2024-11-06 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 736b3bc3-25f0-3e62-9a34-ada714787de4 | -6.4825 | -47.5046 | 2024-11-06 03:00:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| d86badfe-a79e-3217-b805-e0287a4c5125 | -2.9185 | -51.0678 | 2024-11-06 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| aa69cc96-c9cf-339b-a470-ac685c6b2c46 | -3.0207 | -53.443 | 2024-11-06 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 771c8186-4c99-3792-97f1-e7fb7130729d | -2.8506 | -49.4744 | 2024-11-06 03:00:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 7bf33ef7-eb11-36b2-9f05-d35314ab630b | -4.1432 | -43.5822 | 2024-11-06 03:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 194.5 |
| e818781b-ca07-3e82-bbc0-5d899ef8e20c | -2.6764 | -51.8395 | 2024-11-06 03:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| eb566112-868c-3f12-a916-a9e99a69a9f7 | -2.8065 | -51.4855 | 2024-11-06 03:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 45117f1d-deed-3990-a74d-641ea2bf292b | -3.2348 | -50.3904 | 2024-11-06 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 2c188543-f398-3bea-b93f-7e63fd9ae272 | -3.0607 | -52.5066 | 2024-11-06 03:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| cdc8d27c-6fd4-3531-a052-595c3547346d | -2.8423 | -51.7735 | 2024-11-06 03:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| a95943ce-a5f7-35b8-a572-67385592e224 | -3.1393 | -51.2069 | 2024-11-06 03:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 016a8486-f0e5-315d-a1f4-8497e5e72947 | -2.8607 | -51.7937 | 2024-11-06 03:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 817813d9-ace9-377a-aa70-ae59a001adf1 | -3.2164 | -50.3701 | 2024-11-06 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| c0c6ef10-4d25-3584-8ec4-d084796d996a | -6.1039 | -43.9824 | 2024-11-06 03:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 7c2b56b8-9a3d-3eb5-a430-005db3373640 | -6.5014 | -47.4813 | 2024-11-06 03:00:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 212.1 |
| 639b5c12-9c09-38ce-b71e-b48e9242b742 | -3.5444 | -47.4073 | 2024-11-06 03:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| f7bc0dd2-5acc-3c6e-b812-8c911883d21b | -2.6764 | -51.8189 | 2024-11-06 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 25be44e1-0e02-3666-a06f-05dd322854bf | -3.1802 | -50.2032 | 2024-11-06 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| ed8b896c-8c29-36b7-a304-5d6687786f58 | -3.526 | -47.3862 | 2024-11-06 03:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 120.1 |
| 8b185b7b-e138-305e-aa39-4ec8476d2e06 | -2.7243 | -54.1552 | 2024-11-06 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 6a797bc6-cfad-3d5a-9d76-2712e233bf39 | -2.8608 | -51.7731 | 2024-11-06 03:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 930f6956-97fd-3e79-b9af-e61cbf3229f9 | -2.7244 | -54.1351 | 2024-11-06 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 4c1389cb-848c-33a0-9e4d-dd117ced2005 | -4.1246 | -43.5833 | 2024-11-06 03:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 8945f76b-f4b7-3c11-8e60-d4d1747b24d5 | -2.7427 | -54.1548 | 2024-11-06 03:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| a32b6ad0-f404-3eb3-82c2-4ca649047a23 | -3.0396 | -53.2805 | 2024-11-06 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 5c8813e5-6b2b-31c2-8934-d26f582618ec | -6.5012 | -47.5033 | 2024-11-06 03:00:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 01c225e6-b264-3e69-987f-99ecb6ea3287 | -4.5614 | -48.0141 | 2024-11-06 03:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| eeaf42c6-6c72-3c60-8e3c-30c2f63b36d7 | -3.0207 | -53.4227 | 2024-11-06 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 5992c3ed-6f97-39cd-a93b-120020607e78 | -3.6788 | -50.2284 | 2024-11-06 03:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 515b3190-c589-39ba-9bb8-7b4336d8724e | -2.8423 | -51.7942 | 2024-11-06 03:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| fb534016-16a6-302d-a88a-bf58d343f4bd | -3.0023 | -53.4434 | 2024-11-06 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 78e4c7f4-7d3e-3716-87f2-a13ba1435ba0 | -6.1226 | -43.9809 | 2024-11-06 03:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| d6944010-0561-38b9-9dcb-aa7a3cc8988c | -3.5446 | -47.3855 | 2024-11-06 03:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 263.1 |
| 3d32d67f-0f14-36b6-88f8-016588126764 | -2.937 | -51.0673 | 2024-11-06 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 8b0db513-b5c6-3884-a4c5-223ca24afc1e | -6.1414 | -43.9794 | 2024-11-06 03:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 7d1d674a-b65d-343c-81ec-77879e0a5be7 | -3.5631 | -47.3847 | 2024-11-06 03:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 3b56e3a6-cb68-3ea7-a27b-101dc03c7055 | -3.0213 | -53.2607 | 2024-11-06 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 1dc02750-8f97-349c-ad10-9c3654c7041f | -6.5094 | -44.6847 | 2024-11-06 03:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 06e9289e-76f2-36ce-89fb-47278d90df4a | -3.0794 | -47.7727 | 2024-11-06 03:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 9deb7ec9-9566-352a-abe1-9529b059936d | -3.2349 | -50.3695 | 2024-11-06 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 5eebc3ca-fbd0-30b8-a490-77a8367bc0d8 | -2.9371 | -51.0465 | 2024-11-06 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| cd50984a-f289-332a-831d-20c982fc2903 | -3.0212 | -53.281 | 2024-11-06 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 95801631-bf09-3a3f-a9c3-c4898d12139e | -6.1041 | -43.9593 | 2024-11-06 03:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| ff05f149-55cb-3fb5-8d65-c5f504fae676 | -2.9186 | -51.047 | 2024-11-06 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| fefa4810-6007-3b61-9df0-495566df46fb | -3.2053 | -53.2356 | 2024-11-06 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| af9873c9-40b7-3b5f-a6fe-b17598406e01 | -3.1213 | -51.1036 | 2024-11-06 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 57540c46-b1e3-3273-b562-2546ad768a70 | -3.0397 | -53.2603 | 2024-11-06 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 1bdc8a7c-6c7f-31c4-864d-d552aaa684c4 | -3.1617 | -50.2038 | 2024-11-06 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 581bd891-b194-3011-af9e-79ba94a56eae | -3.5447 | -47.3636 | 2024-11-06 03:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 35247f87-9e86-3ab8-b637-16eedb0d0fe0 | -3.0023 | -53.4232 | 2024-11-06 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| e8b3d5f2-1fef-3eb3-8d0b-c55da8c19618 | -3.1433 | -50.2044 | 2024-11-06 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| b2c0228c-cc4a-3ad2-b8d4-1a31ed3be05c | -2.706 | -54.1556 | 2024-11-06 03:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| f0ca9154-f00a-3c49-a83c-0e6d4afcf6c7 | -3.2163 | -50.391 | 2024-11-06 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| fcf2d5f6-726e-3839-9d00-5f474d3d35b4 | -6.4827 | -47.4827 | 2024-11-06 03:00:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 5bf4ba10-3d00-38d0-a98b-4427e1656a51 | -4.13 | -43.6 | 2024-11-06 03:00:00 | MSG-03 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c4ac534-6154-3b70-b00d-26f90ac51f5c | -3.53 | -47.4 | 2024-11-06 03:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d667be2-bb41-30df-bd1a-949b582d8afa | -2.8608 | -51.7524 | 2024-11-06 03:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 46d1e76f-92e2-3492-9a25-96c75a413aaa | -6.5014 | -47.4813 | 2024-11-06 03:10:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 203.5 |
| 65cbea6b-86db-36d1-b2fd-80bbba224e38 | -3.6788 | -50.2284 | 2024-11-06 03:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 518b74ae-5769-3cec-a6b1-d667ec90f7f1 | -4.1432 | -43.5822 | 2024-11-06 03:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 2a1d0373-4eb6-372b-9ee7-0466035fa0c0 | -3.5444 | -47.4073 | 2024-11-06 03:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 51bd933a-e50c-3efc-80ea-048a6516faee | -2.6764 | -51.8395 | 2024-11-06 03:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 98085bfe-5bb4-3017-a5bb-203805d4c494 | -6.5094 | -44.6847 | 2024-11-06 03:10:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 3ccfff54-ce84-39ec-b142-aec94b5d1d8b | -3.2164 | -50.3701 | 2024-11-06 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 9cf1f6ea-3719-3472-a474-f56f11950311 | -2.8506 | -49.4744 | 2024-11-06 03:10:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 2fe50acd-0ad4-3ddb-a050-dafdde0fc1ec | -2.6764 | -51.8189 | 2024-11-06 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 87356a1f-7892-38b3-ae4b-dac39108cb6b | -2.9185 | -51.0678 | 2024-11-06 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 13c31773-f268-379d-80ac-1c6b256416ea | -6.4906 | -44.6862 | 2024-11-06 03:10:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 40c9be73-3a35-3e0e-b5c3-efc86433febe | -6.1041 | -43.9593 | 2024-11-06 03:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |


[Clique aqui para ver as próximas entradas](README21.md)
