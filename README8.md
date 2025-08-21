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
| efc1a514-1456-3419-968e-83d3b2c512b7 | -8.6158 | -62.1184 | 2025-08-21 01:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 172dae81-6fd5-319f-b0bd-794d1ecd3041 | -8.6344 | -62.1177 | 2025-08-21 01:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 708775a3-451b-32ea-8838-99224f78fc35 | -8.8735 | -62.4305 | 2025-08-21 01:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 2101b6d7-fd2f-3233-a2c0-23cd2ee9cfd3 | -7.0354 | -44.6167 | 2025-08-21 01:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 173.9 |
| 6ef88f02-3d1c-3517-be6f-c1b211b6085a | -12.9537 | -46.219 | 2025-08-21 01:40:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 4fe9777a-7408-3527-9dc6-03991db15e3f | -15.8849 | -49.0076 | 2025-08-21 01:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 6572e1d9-551c-3ba3-849f-636e34ff314d | -8.8922 | -62.4107 | 2025-08-21 01:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 36.2 |
| ee1d57a6-854d-321f-b4f2-7128cfe690d7 | -7.0164 | -44.6413 | 2025-08-21 01:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| fec532e3-b4ab-327b-b02b-2435d9e3bf0d | -9.6254 | -40.5875 | 2025-08-21 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 270.2 |
| bb7ee84c-4105-349f-a5d1-193a54c8f980 | -7.0166 | -44.6184 | 2025-08-21 01:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 187.5 |
| 7703fcf7-41b0-3ccc-afe1-591b2af8164c | -9.6254 | -40.5875 | 2025-08-21 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 60.2 |
| 2f3ad5ca-20cf-30f2-b237-f7a078bff75f | -7.0169 | -44.5954 | 2025-08-21 01:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 38d5afb5-be61-306f-97bf-0cf87b7dec79 | -15.8849 | -49.0076 | 2025-08-21 01:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 5059aa87-ae85-3a38-8eac-83adb9c81de3 | -7.0352 | -44.6396 | 2025-08-21 01:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 94008d64-5d99-3848-b6c3-6715233cb439 | -14.8538 | -47.9504 | 2025-08-21 01:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 5eb40497-2427-3ed7-ac86-c00cec9f7e63 | -8.6158 | -62.1184 | 2025-08-21 01:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 901066cc-8d23-3843-b444-da45ecdbd3a7 | -12.9537 | -46.219 | 2025-08-21 01:50:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| ea04524a-4897-3941-962a-793dfdd9de39 | -8.6157 | -62.1374 | 2025-08-21 01:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| e8308461-615f-3992-976d-7dad96a80b94 | -8.8737 | -62.3925 | 2025-08-21 01:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 660d20da-12f2-3910-88d5-de59cb183209 | -14.8543 | -47.9279 | 2025-08-21 01:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 48.2 |
| d10f9861-4744-3ec4-a6fa-9230124ff954 | -7.0166 | -44.6184 | 2025-08-21 01:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 262.9 |
| 5b01af2d-423f-3a53-a69b-94b10b70e4b2 | -8.8736 | -62.4115 | 2025-08-21 01:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 82.1 |
| e8e0ed93-15e0-3f3c-b47b-0a997e58603a | -8.6343 | -62.1367 | 2025-08-21 01:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 646f5d66-0e66-3bef-a05b-3ab275c4dac8 | -12.9533 | -46.2419 | 2025-08-21 01:50:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| e026f543-a668-34c7-be49-ad42a2a62d95 | -7.0164 | -44.6413 | 2025-08-21 01:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| e5ec7713-8f52-3980-bf79-08cd6f7efd3c | -7.0354 | -44.6167 | 2025-08-21 01:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 204.4 |
| 2fad0f52-d131-38c4-a571-ead5b5d9ba64 | -8.8737 | -62.3925 | 2025-08-21 02:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 1b451dae-18e8-363e-880b-1a5a79c79266 | -8.6343 | -62.1367 | 2025-08-21 02:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 913c39a7-6a92-3f9a-83e4-8c3ccd88d98f | -14.8538 | -47.9504 | 2025-08-21 02:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 49.0 |
| cc8120e9-a681-393f-8a7e-b470db6cbb4c | -7.0169 | -44.5954 | 2025-08-21 02:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| c96ea5d6-0628-3751-8787-d41ed4ffb0f3 | -7.0354 | -44.6167 | 2025-08-21 02:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 227.7 |
| a5d2820a-6b4d-3b02-9e72-95bfff09b93b | -8.8736 | -62.4115 | 2025-08-21 02:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 246e7492-f7dc-3942-8b6d-8a56e196ec17 | -8.6157 | -62.1374 | 2025-08-21 02:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 5a4742ce-8bec-3788-bd4a-f08998c64679 | -8.8551 | -62.4123 | 2025-08-21 02:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 220e18ba-6739-3d25-b6b7-05500246e3c8 | -8.8922 | -62.4107 | 2025-08-21 02:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 57e37dff-e526-394d-ad29-b36ddb00e6d0 | -7.0352 | -44.6396 | 2025-08-21 02:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 9304d18b-2a21-38a7-8ede-e71abe6112b1 | -14.8543 | -47.9279 | 2025-08-21 02:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 54.0 |
| eba56820-6ae3-3b54-970a-fb38f8a8063f | -7.0164 | -44.6413 | 2025-08-21 02:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 80bfddd7-190e-3e4a-aff4-615f5cefbe55 | -7.0166 | -44.6184 | 2025-08-21 02:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 537.4 |
| 3237e5a4-7377-3f00-b85e-339706ec7858 | -15.0193 | -54.832 | 2025-08-21 02:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 03b5b2ab-4eba-3306-b4ec-ae32cb9a04ef | -12.9537 | -46.219 | 2025-08-21 02:00:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 771666d4-8a3f-3464-8811-6f02771f037e | -8.8735 | -62.4305 | 2025-08-21 02:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 6f512d78-058a-3c3c-85e8-042b2e3887e4 | -8.8635 | -62.41674 | 2025-08-21 02:06:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 46.4 |
| afdae063-eb8c-3fd1-a60c-d22ba569bef3 | -8.87102 | -62.42237 | 2025-08-21 02:06:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 127.9 |
| d8b7893b-7d46-3b27-a178-6f85ca250e23 | -8.62822 | -62.16189 | 2025-08-21 02:06:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| e20239cb-b9e7-3c1b-a951-71bdd70474b1 | -8.88692 | -62.41954 | 2025-08-21 02:06:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 84ef89bf-0562-3c03-b30e-b840cd0558b5 | -8.86556 | -62.38933 | 2025-08-21 02:06:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 2a68d773-8aa0-3ae2-9b73-05c924323712 | -8.8794 | -62.41392 | 2025-08-21 02:06:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 4ea2e04b-e362-3323-9b1c-d68ed7a96ba0 | -8.62235 | -62.1267 | 2025-08-21 02:06:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 9bdbc4cf-eec1-385e-9dac-98efd7512538 | -7.78398 | -66.96175 | 2025-08-21 02:09:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e2434e95-ed7f-393d-b98a-946dad58d03b | -8.56851 | -70.04064 | 2025-08-21 02:09:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2a4ef2de-5ade-39c0-83bb-bc0c8132cce6 | -9.04803 | -67.46458 | 2025-08-21 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8db35bbf-9497-3c36-984e-1e2dc4d6ff73 | -8.33519 | -70.27829 | 2025-08-21 02:09:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5fb4a253-f895-3050-a31d-9e239e99d24b | -8.9851 | -69.48973 | 2025-08-21 02:09:00 | TERRA_M-M | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ba336709-8ca6-3c77-9158-4efa0110d8de | -7.7822 | -66.95557 | 2025-08-21 02:09:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 2c77cb2a-b6e3-3967-b1c8-aba9f71fc7ce | -8.55121 | -66.93955 | 2025-08-21 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 31a40dc1-ce12-344d-98dc-4c663a07c6c4 | -8.55348 | -66.95438 | 2025-08-21 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 6056a8d9-6811-33af-82b4-39a2f995c91e | -8.32609 | -70.27963 | 2025-08-21 02:09:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 68b583c7-cbe4-3359-a696-74f94a2ee0d4 | -7.0354 | -44.6167 | 2025-08-21 02:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 367.7 |
| d4cd1b2b-5a8b-30dc-8634-ed73c92d921b | -7.0357 | -44.5938 | 2025-08-21 02:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| a7c02489-ea6e-34b9-92e2-ba813f6a27c1 | -8.8736 | -62.4115 | 2025-08-21 02:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 5de6e310-59fd-312f-89af-23777848f0a6 | -8.8735 | -62.4305 | 2025-08-21 02:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 571c6a10-39f6-3926-b3c9-ddb0af190cf0 | -8.8737 | -62.3925 | 2025-08-21 02:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 50efb67f-aee3-33cb-acfb-5e9a76bc71f4 | -7.0164 | -44.6413 | 2025-08-21 02:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 203.6 |
| b316336a-05db-364f-a3f7-422ba00901c9 | -8.8922 | -62.4107 | 2025-08-21 02:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 7f53b727-13a5-3bcd-82bf-930b22daa78a | -14.8543 | -47.9279 | 2025-08-21 02:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 54.2 |
| dd62fc90-b9e1-3d44-8cd0-20e463671108 | -8.8551 | -62.4123 | 2025-08-21 02:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 36.1 |
| ad57634f-cada-325a-b3e2-d8931dd4c142 | -7.0352 | -44.6396 | 2025-08-21 02:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 614a8f13-f279-353c-925c-13661c2ff975 | -7.0166 | -44.6184 | 2025-08-21 02:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 492.1 |
| 793711e9-d372-3cd1-924d-8b1d98612829 | -7.0169 | -44.5954 | 2025-08-21 02:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 9448ebd1-9d50-3cef-b394-fa20672609dc | -15.8849 | -49.0076 | 2025-08-21 02:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 2bb3890d-a662-3b61-ad95-49b8f1574c45 | -15.0193 | -54.832 | 2025-08-21 02:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 9e252f87-1e0a-35fb-aab8-cc7dc4c31477 | -7.0164 | -44.6413 | 2025-08-21 02:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 273.3 |
| e56a293e-8c0f-3b85-a757-d0a5d1e8af75 | -7.0352 | -44.6396 | 2025-08-21 02:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| b5dcecf6-8f58-37d7-b94b-160b4af83f49 | -14.8543 | -47.9279 | 2025-08-21 02:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 9174dd91-b215-362f-bc3e-4a08cbb9aa69 | -8.8735 | -62.4305 | 2025-08-21 02:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| f8dd4fd3-82b7-37df-a8c6-6cd219075ee6 | -7.0169 | -44.5954 | 2025-08-21 02:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 131b29ea-5c9c-3290-87a0-f0becc9c1a1e | -8.8736 | -62.4115 | 2025-08-21 02:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 156e17a3-7d1b-359c-a873-0da4741a1274 | -8.8551 | -62.4123 | 2025-08-21 02:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| a984a60d-98c8-3626-8c8e-f35b570618ba | -7.0354 | -44.6167 | 2025-08-21 02:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 307.7 |
| 4dc36f11-f3d1-39eb-ab21-e14ab482bbf2 | -8.8922 | -62.4107 | 2025-08-21 02:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 41f0df67-2826-3ee5-b100-70751d83604a | -8.8737 | -62.3925 | 2025-08-21 02:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 0fb84f72-3f5c-3ba8-8c40-7eb00cc53445 | -15.0193 | -54.832 | 2025-08-21 02:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| e0bfe589-a4d7-32d0-a9a1-f01570e4660a | -7.0166 | -44.6184 | 2025-08-21 02:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 858.1 |
| c1e4fdc1-a6c0-370d-9ceb-8d50ed0fff0f | -14.8538 | -47.9504 | 2025-08-21 02:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 43.6 |
| fb786961-ef42-3ec0-9c9c-f21d3dc99cc8 | -14.9999 | -54.8343 | 2025-08-21 02:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| a98812ff-b04d-345a-ba1a-9f60d9857686 | -13.0321 | -45.1492 | 2025-08-21 02:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 2e68747b-9a80-39ad-9639-c89e9a9b3132 | -13.051 | -45.1693 | 2025-08-21 02:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 994f91bb-c98a-3be7-b488-89a197c4b373 | -14.8543 | -47.9279 | 2025-08-21 02:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 9a0cf152-8f02-3e8a-b9f5-0dc8e3db464c | -8.6157 | -62.1374 | 2025-08-21 02:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 39c6b9ed-6897-377b-bdf3-a4a6dec746c6 | -8.8737 | -62.3925 | 2025-08-21 02:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 5f9366aa-21e7-39bd-8d10-9a1a64718dd8 | -8.8735 | -62.4305 | 2025-08-21 02:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 270b133f-0444-3af0-b074-4662d30fea82 | -8.8736 | -62.4115 | 2025-08-21 02:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 6303fcdc-1eb4-3a94-b184-0a52904bfba0 | -13.0123 | -45.1756 | 2025-08-21 02:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 82de827d-a05f-3d03-a40a-3d21ca2ec028 | -13.0128 | -45.1523 | 2025-08-21 02:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 8047a6bf-3743-3f7e-805b-45e44708eb6a | -14.8538 | -47.9504 | 2025-08-21 02:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 440d426c-87a0-38a2-8b34-d01b2fee74d0 | -15.0189 | -54.8528 | 2025-08-21 02:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 62f1662b-1df0-3ba7-91d0-eb2272f19c6d | -15.0193 | -54.832 | 2025-08-21 02:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 1ace0fab-ee0c-3f3f-943d-6538df42a316 | -8.8922 | -62.4107 | 2025-08-21 02:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 9bc3a635-582a-3efe-9ea2-845850698b39 | -15.8849 | -49.0076 | 2025-08-21 02:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 46.2 |


[Clique aqui para ver as próximas entradas](README9.md)
