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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ccbc743-a01d-3849-a4f4-63f47dce89ce | -12.43773 | -43.73986 | 2024-11-06 03:51:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 419c912f-0d11-3c03-83e7-bda2e2c66b44 | -10.74218 | -49.02941 | 2024-11-06 03:51:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9dd9f1ae-b1a3-32d9-815d-ed721584c1bf | -11.94097 | -41.62936 | 2024-11-06 03:51:00 | NOAA-21 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 93d290f4-8b7e-3c8e-8172-7ccddb5f8147 | -12.05714 | -43.47481 | 2024-11-06 03:51:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a560638d-6153-321d-9a14-c10760c309a2 | -15.15364 | -43.71537 | 2024-11-06 03:51:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7dec9898-162c-354c-aab0-9aa7e4c8b967 | -10.7482 | -49.03046 | 2024-11-06 03:51:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| feb5922a-64eb-3463-b433-0e1fd7e64e71 | -11.13372 | -44.9551 | 2024-11-06 03:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae018139-caab-3882-bd3b-38ea7797baca | -13.04764 | -41.41692 | 2024-11-06 03:51:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4e3e0c4d-0195-3559-84f7-b3257f71d711 | -12.70574 | -39.07268 | 2024-11-06 03:51:00 | NOAA-21 | CRUZ DAS ALMAS | BAHIA | Brasil | 2909802 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3aabd230-3d05-3e3a-96f1-7b142aaece82 | -13.61636 | -43.30017 | 2024-11-06 03:51:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| de224f93-688e-3286-9d3a-171263bea1b3 | -2.8506 | -49.4744 | 2024-11-06 04:00:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 70dc8d39-3431-37c4-a1c0-4499eb46fee1 | -3.0396 | -53.2805 | 2024-11-06 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| fa53dde8-6ff3-39cd-9df4-0a44346fc979 | -3.0213 | -53.2607 | 2024-11-06 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 5c3a15fd-475b-3505-ad97-60c6838dd41a | -3.2163 | -50.391 | 2024-11-06 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| ef8d6814-acce-3ee9-9696-93d37ee430be | -2.8607 | -51.7937 | 2024-11-06 04:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 5ca6d98b-eda7-3153-8f3a-60ea9da5c4b1 | -2.7243 | -54.1552 | 2024-11-06 04:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 1a6ba2d6-9889-3fc3-ab6f-c9f353e5c06c | -3.2164 | -50.3701 | 2024-11-06 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 80e25241-f03d-383e-a799-43b532a110fb | -2.9371 | -51.0465 | 2024-11-06 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 0a3769f1-3302-35b2-8a0c-848ec4b2f159 | -6.1226 | -43.9809 | 2024-11-06 04:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 2a66e777-e8ff-3d91-a98b-705a8afed745 | -3.1616 | -50.2248 | 2024-11-06 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 7df758f7-f192-37d3-96ea-d3998716c74e | -2.8423 | -51.7942 | 2024-11-06 04:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| df294cbd-9e62-3e06-8d7a-43750609b913 | -4.1432 | -43.5822 | 2024-11-06 04:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 9b7fecea-65ed-35e8-90b8-bd372e1260fe | -3.0023 | -53.4232 | 2024-11-06 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 22de59e1-d306-338a-b5c9-59acf692a385 | -3.967 | -48.15 | 2024-11-06 04:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 5e744e31-9b6d-373b-a13a-d0406ec97eaa | -2.6764 | -51.8189 | 2024-11-06 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 16b0a9ce-c47e-30bd-bc7a-014c9f19ab4d | -3.0207 | -53.443 | 2024-11-06 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 6f04d6bf-9084-3606-9ad1-52cba9fb5382 | -3.2349 | -50.3695 | 2024-11-06 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 02394a75-eb90-3e8b-8670-4bd962144142 | -2.9186 | -51.047 | 2024-11-06 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 5fd4db43-87ef-306b-a1d5-ca2c3afc7327 | -3.5446 | -47.3855 | 2024-11-06 04:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 178.7 |
| 0fc76b88-752f-3db2-babf-c748bcd62430 | -3.2348 | -50.3904 | 2024-11-06 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 3f3118de-a820-332a-a8b1-fa635be61e54 | -2.937 | -51.0673 | 2024-11-06 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| a86ee2dc-1c61-3503-bbc9-fea2d836c4df | -4.1246 | -43.5833 | 2024-11-06 04:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 9726dc45-1295-3d61-9d02-3dcad18d1f52 | -3.0212 | -53.281 | 2024-11-06 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 03cdcc86-3138-38f0-b54e-9bef1004b5cc | -6.5096 | -44.6618 | 2024-11-06 04:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| df578787-9f41-3ae3-8bee-adc2ad7b4273 | -6.5094 | -44.6847 | 2024-11-06 04:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 6d915a80-68f3-348e-bdf8-aa9b0ae4d260 | -4.5614 | -48.0141 | 2024-11-06 04:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| a8ee2bd0-01af-341a-8e2f-fe49bf144df8 | -2.831 | -49.7924 | 2024-11-06 04:00:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 9dafa5a8-3211-3caf-9fdc-96b0215fe04f | -6.5012 | -47.5033 | 2024-11-06 04:00:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| a1f46267-5e61-36e2-b97b-2f1ea0deac74 | -2.831 | -49.7713 | 2024-11-06 04:00:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| b0b5edde-9d3f-3438-b606-07dfa8da6898 | 3.6 | -51.3168 | 2024-11-06 04:00:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 49.5 |
| a7f7fd11-37a7-3aa8-857b-c4bb04b45ba2 | -3.0023 | -53.4434 | 2024-11-06 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 249982a3-a28e-3e8e-884b-3133efacbaae | -2.7244 | -54.1351 | 2024-11-06 04:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 05d20ed1-79a9-3a7f-bfd8-40eec44cd83b | -2.8423 | -51.7735 | 2024-11-06 04:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 24d99a4a-fb18-362c-b198-340ef72871cb | -3.0397 | -53.2603 | 2024-11-06 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| fdfa4d5e-601c-3a02-b131-deaa6ab4df54 | -3.1617 | -50.2038 | 2024-11-06 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 73400cf4-b60b-3a1d-bc85-4be1995d8773 | -3.0207 | -53.4227 | 2024-11-06 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 453ae04e-7a41-3a2c-9b90-7f6a686ad725 | -6.4906 | -44.6862 | 2024-11-06 04:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 673e8143-e057-3e92-af69-b94f75fdd818 | -6.5014 | -47.4813 | 2024-11-06 04:00:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 123.0 |
| b05f6107-0576-3efb-b441-488c684f90f9 | -6.1229 | -43.9578 | 2024-11-06 04:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 00beb8d3-1658-3e9d-b49c-5dce1ce3a3fb | -2.8608 | -51.7731 | 2024-11-06 04:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 150.9 |
| c69c31a0-df5e-3c9c-9730-b98967339103 | -6.4827 | -47.4827 | 2024-11-06 04:00:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 724cdaba-3bc6-3281-8293-1234ba017cec | -3.5447 | -47.3636 | 2024-11-06 04:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 1286674d-3bd1-36dc-aae1-1dbd0f988bfe | -3.0397 | -53.2603 | 2024-11-06 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| a90d2224-df1d-3919-84e5-3b670f48957f | -2.9186 | -51.047 | 2024-11-06 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 900a745a-a2ab-32f3-8907-407f0157a770 | -2.937 | -51.0673 | 2024-11-06 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 13b67c53-991d-36c1-bdb9-4593cee8f6f7 | -3.2164 | -50.3701 | 2024-11-06 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 0833f144-e3a6-3790-8450-0f7c021d095a | -3.2348 | -50.3904 | 2024-11-06 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| c8b36df6-750b-3310-8d54-60b2344d56ff | -2.8423 | -51.7942 | 2024-11-06 04:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 925726b8-4ef3-3f26-af9d-23a9d9df03cd | -6.5014 | -47.4813 | 2024-11-06 04:10:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 0042c152-0321-35c4-a702-378daa7ce3da | -9.8581 | -59.9289 | 2024-11-06 04:10:00 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 843bf3a7-6f8b-3939-8408-b34dceb73f93 | -6.4827 | -47.4827 | 2024-11-06 04:10:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 09a085fa-4180-3637-a4df-2f58f7ed46a2 | -2.7244 | -54.1351 | 2024-11-06 04:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 33ea620f-c093-3351-9721-f6101da9fa3f | -6.5094 | -44.6847 | 2024-11-06 04:10:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 2a9f4424-c49e-3fa7-b51e-155fb49b4b5a | -3.0213 | -53.2607 | 2024-11-06 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 9ade19fc-f841-33ba-b65d-0d89be5c6877 | -3.2163 | -50.391 | 2024-11-06 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| f8c90c10-b700-3b41-b1c6-48648236f187 | -2.8607 | -51.7937 | 2024-11-06 04:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 97363111-7d4f-3fa8-9ee7-a2543d9c36cc | -6.1041 | -43.9593 | 2024-11-06 04:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 15fc8505-9679-3761-b382-4a2b632975fe | -3.2349 | -50.3695 | 2024-11-06 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 20a96742-8779-39d1-843e-55dcd73c9b2c | -2.9187 | -51.0262 | 2024-11-06 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 94bf5a5f-9855-3397-a57c-787da98c2f50 | -4.0859 | -53.9365 | 2024-11-06 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 8f84b2b7-8e30-37d6-800d-4f75f20c71e5 | -4.5614 | -48.0141 | 2024-11-06 04:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| d05ce345-b7c9-33b4-b373-db4f87c7f894 | -2.7243 | -54.1552 | 2024-11-06 04:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 6e40273c-0edd-360d-9ba1-33f9a0935544 | -4.1432 | -43.5822 | 2024-11-06 04:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 7cd540d0-1c0f-3439-8640-ffecdf83e38b | -3.0023 | -53.4232 | 2024-11-06 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| b62cf610-5f51-345e-867c-b46d3787a575 | -3.0207 | -53.4227 | 2024-11-06 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 4d4ecde2-3748-39e3-9531-65a7be684e7a | -6.5012 | -47.5033 | 2024-11-06 04:10:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 17217635-d99b-3988-b12b-b0004afff1d0 | -3.1616 | -50.2248 | 2024-11-06 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 3a7a4c8c-b73d-3c43-9948-9cc02cc472a9 | -2.831 | -49.7713 | 2024-11-06 04:10:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 8a5b3728-d8ae-3489-a2c2-e1a06f4b0319 | -6.4906 | -44.6862 | 2024-11-06 04:10:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 04d00229-06ee-3823-bd70-83cf13b0f931 | -2.8423 | -51.7735 | 2024-11-06 04:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 50813f1f-655a-3590-bfa6-117db3ad39a4 | -3.5446 | -47.3855 | 2024-11-06 04:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 162.2 |
| 5c5f3a00-7b25-330b-b7c9-12265076bac9 | -3.967 | -48.15 | 2024-11-06 04:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| aec1ab90-9ec6-35e6-b585-f39c3157c6b0 | -2.8608 | -51.7524 | 2024-11-06 04:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| d2d0bcf7-3820-3c6d-aae4-3a269a7c6d11 | -4.1246 | -43.5833 | 2024-11-06 04:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 3637f2bb-ba1b-34bc-ac2f-b89e63d55480 | -2.9371 | -51.0465 | 2024-11-06 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 0e957de7-c5c5-3113-aae6-cab08c290c90 | -3.0207 | -53.443 | 2024-11-06 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| d580cc1a-f581-3d11-8bb0-47bb720a30d5 | -6.1226 | -43.9809 | 2024-11-06 04:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| ec09a61b-e12e-36f2-ac6f-843da6557370 | -3.0396 | -53.2805 | 2024-11-06 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 4daad55e-f0dd-3da3-b8c1-059617b3ddb0 | -3.1617 | -50.2038 | 2024-11-06 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 797a9b8d-4d3f-366f-9c90-2abae0437dd1 | -2.6764 | -51.8189 | 2024-11-06 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 261ddc0e-af7e-39b3-84ca-ac7b77a64bee | -6.4825 | -47.5046 | 2024-11-06 04:10:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| a08f4621-85d7-3cd0-9e40-de8fbeb8427d | -6.5096 | -44.6618 | 2024-11-06 04:10:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| a82a9f3d-1e23-3ac2-8c76-8de4ff8590b3 | -3.0023 | -53.4434 | 2024-11-06 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 436db95e-5948-3f87-9163-7822a6efd739 | -2.8608 | -51.7731 | 2024-11-06 04:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 164.2 |
| 14381435-11c5-3c3a-bdfc-ac60270ae856 | -3.9669 | -48.1716 | 2024-11-06 04:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 7a77dd6b-7660-3587-8407-e94490c1701d | -2.8506 | -49.4744 | 2024-11-06 04:10:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 30763e6a-9945-3e30-9201-d08d4e0877bc | -3.5447 | -47.3636 | 2024-11-06 04:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| b1ddda1f-6b1b-367c-a677-c3b41894bb3d | -2.8608 | -51.7731 | 2024-11-06 04:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 149.4 |
| 15df632e-932b-3486-b5e7-1584f7a5e41d | -4.5614 | -48.0141 | 2024-11-06 04:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 9654ec1b-b161-3d84-b11e-cf79ed4a1572 | -2.4457 | -49.039 | 2024-11-06 04:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |


[Clique aqui para ver as próximas entradas](README29.md)
