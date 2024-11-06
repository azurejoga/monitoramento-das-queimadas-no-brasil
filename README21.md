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
| b58cba3c-c92f-3dd8-801a-3bafebd4fb99 | -2.8424 | -51.7529 | 2024-11-06 03:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 1983cf28-d27a-34f6-a0da-0b0d3ac62754 | -3.0396 | -53.2805 | 2024-11-06 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 9bd5e023-fd92-3677-ad0e-a56595af1a95 | -2.8608 | -51.7731 | 2024-11-06 03:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 63943f6e-e7d6-3e69-afcb-0c57aacfa24b | -6.5012 | -47.5033 | 2024-11-06 03:10:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 23855f64-e421-3ae2-b662-082a156a3cfc | -3.0207 | -53.443 | 2024-11-06 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 09566990-256d-3ba2-90b5-9ac2881190ac | -2.9186 | -51.047 | 2024-11-06 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 6e3a634d-6dc4-3b71-941b-b22e14bea727 | -3.2054 | -53.2153 | 2024-11-06 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 12652469-8cd1-39a3-ad61-6f853e73cf5b | -2.7244 | -54.1351 | 2024-11-06 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| bbd9a84b-83a7-3ef8-b093-27fd64ff67f4 | -3.1213 | -51.1036 | 2024-11-06 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 10fb7293-4951-38bc-abb0-86714d725a17 | -6.4827 | -47.4827 | 2024-11-06 03:10:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 004c4e1f-4cd9-3132-9b2d-32d6c88572f3 | -6.4825 | -47.5046 | 2024-11-06 03:10:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| a84d9892-cec1-32d4-9c62-d0d7b10d4b93 | -3.5446 | -47.3855 | 2024-11-06 03:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 217.1 |
| 2005c5d6-e76a-3e64-a0c0-cc430eafcfdb | -3.6603 | -50.2291 | 2024-11-06 03:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 3b77ac00-ad88-3661-8bb0-4025fca0bea4 | -3.0023 | -53.4232 | 2024-11-06 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 957376b5-8f0f-3f54-805b-16d416eac45e | -6.1414 | -43.9794 | 2024-11-06 03:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| fc4cd351-697d-34df-9815-5aa744aeec05 | -2.9187 | -51.0262 | 2024-11-06 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 427e1f9a-e108-3b92-8d50-be4f44502b20 | -6.1039 | -43.9824 | 2024-11-06 03:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 6454fa7c-41b9-348c-9f39-3a842b3feab6 | -4.1434 | -43.5591 | 2024-11-06 03:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| d24acf29-97d3-3100-af9d-2747e0ad3be7 | -2.8065 | -51.4855 | 2024-11-06 03:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 5477c0ad-3985-3be3-b93c-7add132ddc35 | -2.937 | -51.0673 | 2024-11-06 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| f1b654f9-c3c0-3d0e-85dc-16a2658942e7 | -3.2348 | -50.3904 | 2024-11-06 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| fb6ffe81-eecd-3227-ab64-5d1b57f5c130 | -3.526 | -47.3862 | 2024-11-06 03:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 17b10480-ad68-3db0-99da-870c777f9e10 | -3.1616 | -50.2248 | 2024-11-06 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 4d9ae0c4-d636-3419-a178-1b3b221f3669 | -3.0207 | -53.4227 | 2024-11-06 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| b66e35ef-4775-30f6-942b-eecdb5e745e4 | -3.0023 | -53.4434 | 2024-11-06 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 03b07be8-beb6-387f-825c-11c6c2dace1a | -3.2163 | -50.391 | 2024-11-06 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 7c610880-2541-3c8f-99cd-07efa31bcb11 | -4.1246 | -43.5833 | 2024-11-06 03:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 145.0 |
| dfbf7e0a-1b58-372d-a69b-be63bda67329 | -6.1229 | -43.9578 | 2024-11-06 03:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 719516c4-f52c-3fb0-860c-8ac6243b66c4 | -3.0212 | -53.281 | 2024-11-06 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| a13ec839-d354-314e-a2e2-3b18efb31d0e | -3.0607 | -52.5066 | 2024-11-06 03:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| b4c10097-4f00-3655-bd76-4df099ed1ed1 | -2.7243 | -54.1552 | 2024-11-06 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| c35f4772-7242-3a1e-a76f-50b8ae2108e8 | -2.706 | -54.1556 | 2024-11-06 03:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| a4744885-5103-3ec4-b713-5c7661e4614c | -6.1226 | -43.9809 | 2024-11-06 03:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 880c37cf-7878-3ee8-b2d7-447640f8c0b6 | -2.8423 | -51.7735 | 2024-11-06 03:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 1ca9832e-d964-3dc5-a4df-2c19839c4e35 | -3.2053 | -53.2356 | 2024-11-06 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 7cb27e37-47c2-3d04-bdbd-a3f8168f6051 | -3.1617 | -50.2038 | 2024-11-06 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 853004a8-f1b8-36fa-ac05-dd46dad49fc6 | -4.5614 | -48.0141 | 2024-11-06 03:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| a00ca13c-68d1-31dd-8500-144a5733fe0e | -3.1393 | -51.2069 | 2024-11-06 03:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| fcabf35f-d86a-3cec-a214-be78c62fa855 | -3.0213 | -53.2607 | 2024-11-06 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| f9d6e2d3-1ff5-3f08-ab8e-77b0b696c104 | -2.8423 | -51.7942 | 2024-11-06 03:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 0dfb6400-ea42-3ce2-9c69-f4fc7bbe55b1 | -3.5447 | -47.3636 | 2024-11-06 03:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| bbb1e521-fe01-3b3a-b5c3-a2d4c6d4cbb7 | -3.2349 | -50.3695 | 2024-11-06 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 3bf1191e-b9b1-3a41-960c-c6f3f77b64b3 | -2.8607 | -51.7937 | 2024-11-06 03:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 5409414c-ac99-3a8b-b780-12d320c194b1 | -3.5631 | -47.3847 | 2024-11-06 03:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| c14c8050-b53d-3758-acbc-caa5a6fec3b7 | -2.9371 | -51.0465 | 2024-11-06 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| ec979ace-16e9-3a57-9787-541015d9d109 | -3.0397 | -53.2603 | 2024-11-06 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 8fc2adf1-edbf-34f1-9d05-fdc02a425108 | -3.967 | -48.15 | 2024-11-06 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| b718c30c-8eb8-3278-9d2b-d3e83026e576 | -2.9371 | -51.0465 | 2024-11-06 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 423f1f72-53fd-3720-8a63-33919a0eef6f | -3.0396 | -53.2805 | 2024-11-06 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| f246b83f-26e3-3253-9ad1-f80c26627fef | -2.8506 | -49.4744 | 2024-11-06 03:20:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 7ca14453-729f-3217-8194-6b6238179373 | -3.0023 | -53.4232 | 2024-11-06 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| d3e5fa1c-fa50-3977-b0b3-1721c24b1fe6 | -4.1432 | -43.5822 | 2024-11-06 03:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 124.7 |
| de372c1f-596a-3829-b0a0-5d25fc38a790 | -4.5614 | -48.0141 | 2024-11-06 03:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 0fea85ee-4798-3297-b13e-3be6333a3ebd | -4.1247 | -43.5601 | 2024-11-06 03:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| fec06ec2-15cd-3e4e-86a1-b8d874ec5c77 | -3.1617 | -50.2038 | 2024-11-06 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| ddc99d63-8f33-389b-a619-2dbfa63fec4d | -6.4827 | -47.4827 | 2024-11-06 03:20:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 41010168-d338-32b4-9b68-0f9d0e4184c8 | -2.7244 | -54.1351 | 2024-11-06 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 8538a45d-9821-3839-b6b6-b4fde7df78bf | -6.4906 | -44.6862 | 2024-11-06 03:20:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 32f825bf-fa8e-3d7b-a08a-03c2e5cff035 | -6.1041 | -43.9593 | 2024-11-06 03:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| d161df87-2592-324c-bb31-45216a6a974c | -6.1229 | -43.9578 | 2024-11-06 03:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 4901ccd0-6128-3646-94c9-91222bfb59b7 | -2.9185 | -51.0678 | 2024-11-06 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| f4742b7f-cdf6-3eb2-b1fd-de34b27b3ac1 | -3.0207 | -53.4227 | 2024-11-06 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 0359d827-dcf1-33a0-9587-eeb5f1b717a2 | -6.5012 | -47.5033 | 2024-11-06 03:20:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 149803b6-18d3-3fff-8fad-3a656bd77a36 | -2.7243 | -54.1552 | 2024-11-06 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| c7365fbd-e2b2-3be1-a301-4ea96d5c5ab0 | -2.9186 | -51.047 | 2024-11-06 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| e0b9d8bf-24d6-3fca-b53c-1b555a4c5285 | -3.0397 | -53.2603 | 2024-11-06 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 65f44de8-c4fd-3479-9d26-08c9dfe37ccb | -3.1616 | -50.2248 | 2024-11-06 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 8d622c9c-e6a9-3c92-ae65-9434a5a458a0 | -3.5447 | -47.3636 | 2024-11-06 03:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 06c2a48e-2698-3411-a27a-199e2a088063 | -3.0609 | -47.7733 | 2024-11-06 03:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| b3e663fb-a07a-3e72-b6ca-f2cc0ae66a25 | -6.5014 | -47.4813 | 2024-11-06 03:20:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 186.6 |
| a67cae2c-b810-3abf-95a7-6f8fe0a38124 | -3.2348 | -50.3904 | 2024-11-06 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 26a690dd-6f9c-315a-9e4e-4d614e39ef00 | -3.5444 | -47.4073 | 2024-11-06 03:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 70731aa9-b2e8-3ed7-9f1f-f2250a3a4d2b | -3.2349 | -50.3695 | 2024-11-06 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 379b3136-d3f0-3c35-a97e-eec197b34784 | -2.8065 | -51.4855 | 2024-11-06 03:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 0889848e-081d-398a-908d-39c62877a5b9 | -3.2164 | -50.3701 | 2024-11-06 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 2c0f154d-134f-334f-9284-fcd2ad00a756 | -2.6764 | -51.8395 | 2024-11-06 03:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| e0f34954-c423-3b4e-b56b-3c5eca481cf4 | -3.6788 | -50.2284 | 2024-11-06 03:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| df5544de-14c1-3ff9-ae4e-5b29aeeab33b | -3.0023 | -53.4434 | 2024-11-06 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| b98cd54c-9638-32fb-aa9e-512704f6338d | -4.1246 | -43.5833 | 2024-11-06 03:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 294.5 |
| 99f40a02-490a-3025-a181-2066d1194bfd | -3.5446 | -47.3855 | 2024-11-06 03:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 273.0 |
| 0ad8599c-8d2d-3792-8656-28dbb3a3cc12 | -3.2163 | -50.391 | 2024-11-06 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| d4108465-9641-36ec-8747-f09147b659e2 | -3.967 | -48.15 | 2024-11-06 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 5d80ecc3-8104-3df5-bc06-7b57c7f85cfd | -2.6764 | -51.8189 | 2024-11-06 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| c1b3cb62-7782-3394-bfff-4b075b441fdc | -2.8607 | -51.7937 | 2024-11-06 03:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 151d08d0-08ae-3971-9b83-02d84bf7b432 | -6.4825 | -47.5046 | 2024-11-06 03:20:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 28ee24d8-6b71-3109-a567-e312a903cc4b | -3.0213 | -53.2607 | 2024-11-06 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| edb0b636-7b77-311a-ac12-6ca6c54896c9 | -2.9187 | -51.0262 | 2024-11-06 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 635ade17-d87a-353c-ad57-7580a6df54b8 | -3.0207 | -53.443 | 2024-11-06 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 1e4ac045-84f7-3ec4-a019-ff5e70cdf910 | -6.1226 | -43.9809 | 2024-11-06 03:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 7a7f96e3-13b5-3a33-8c1b-024019a4264a | -2.8423 | -51.7735 | 2024-11-06 03:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 18c2bb5f-2ef9-393c-b862-086b277838c9 | -2.8423 | -51.7942 | 2024-11-06 03:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 304a5611-84ae-34a3-bd14-1850b126fc43 | -6.5094 | -44.6847 | 2024-11-06 03:20:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| df3bc7e4-8999-3a48-a86a-17704a8878c8 | -2.937 | -51.0673 | 2024-11-06 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| dddb81db-2a74-3a21-b2c4-02c4a3b4f038 | -2.8608 | -51.7731 | 2024-11-06 03:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 166.9 |
| f8e0e9dd-5074-3b45-8817-956b99bedabc | -2.8608 | -51.7524 | 2024-11-06 03:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| bdf68b58-dedc-33ff-8b7e-65c1023f2f5f | -2.8506 | -49.4744 | 2024-11-06 03:30:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| f14a39cd-f544-313a-896d-4b8fc65ca551 | -2.8607 | -51.7937 | 2024-11-06 03:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 4739a48a-492f-3d42-b7bf-61babe44fba3 | -3.5631 | -47.3847 | 2024-11-06 03:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| cb14d3cc-1167-364d-b2f5-528aa9b7e9e8 | -2.6764 | -51.8395 | 2024-11-06 03:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| e3a01461-0d86-31b7-8f12-bd04591ca81b | -3.5447 | -47.3636 | 2024-11-06 03:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |


[Clique aqui para ver as próximas entradas](README22.md)
