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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1b08e3b-5abe-3a33-8b4d-ecf7e023dcf7 | -3.967 | -48.15 | 2024-11-06 05:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 20d40fb6-525e-37f8-8e63-0618863c1ed5 | -2.8607 | -51.7937 | 2024-11-06 05:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 98263360-dcac-3868-bcf5-93acdf462767 | -6.4906 | -44.6862 | 2024-11-06 05:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 9e4e1b1b-fa54-3e16-98be-ef6ff0391c25 | -3.2163 | -50.391 | 2024-11-06 05:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| b93735af-016d-3b93-ab92-c8cfc8252f81 | -2.9371 | -51.0465 | 2024-11-06 05:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| e6600a92-eaa2-3ff5-a857-85389a245f0e | 3.6184 | -51.3162 | 2024-11-06 05:00:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 59.3 |
| eb0b6056-11e2-3e34-affd-928259be5791 | -3.0207 | -53.4227 | 2024-11-06 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 22e0c130-7624-36a0-bb72-2a4eb06ea044 | -6.5014 | -47.4813 | 2024-11-06 05:00:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 739623c7-617a-3241-bb11-37e60f819804 | -3.0396 | -53.2805 | 2024-11-06 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| e50208cb-373e-3936-a555-e6df979de7ad | -2.8423 | -51.7735 | 2024-11-06 05:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 539beff0-ec37-39b0-a1ed-dab1ae4ae8ed | -2.7243 | -54.1552 | 2024-11-06 05:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 08069820-2185-3b16-92a2-8757661fbb3b | -3.0207 | -53.443 | 2024-11-06 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| bb6689df-af56-396f-b8d9-b4d1b357e604 | -6.5096 | -44.6618 | 2024-11-06 05:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 525566a7-d560-3d72-85d3-4ffd9a9cd962 | -2.7244 | -54.1351 | 2024-11-06 05:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| f1a2c0f8-3b51-3a01-a1b6-a3adf65d85a6 | -2.8506 | -49.4744 | 2024-11-06 05:00:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 6c10ad87-2e6a-37fe-819c-25accc5bf134 | -6.4827 | -47.4827 | 2024-11-06 05:00:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 4726a6be-74f4-3291-b1cf-4f6208ad4d7a | -3.1617 | -50.2038 | 2024-11-06 05:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 00011f38-4e62-36fb-9fc3-f5765602c279 | -3.2164 | -50.3701 | 2024-11-06 05:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| c38727f4-9e2e-3870-9fab-b6b70dcb4488 | -6.1226 | -43.9809 | 2024-11-06 05:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 2a9b7dc1-09e8-3b5f-adc2-1a50362063e2 | -3.0397 | -53.2603 | 2024-11-06 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 80845d11-9c5e-3037-8c18-92b4c5db65cb | -2.6764 | -51.8189 | 2024-11-06 05:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 055f9290-e275-3a0d-9274-ad56dcf94d38 | -2.4457 | -49.039 | 2024-11-06 05:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| f6bf8b1f-335b-3c37-8b57-7984f84271c7 | -4.1246 | -43.5833 | 2024-11-06 05:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 8f252ead-7635-3f59-9345-e75cc33a7400 | -4.1432 | -43.5822 | 2024-11-06 05:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 61cc91ed-2469-355a-913c-4a772b225443 | -2.8608 | -51.7731 | 2024-11-06 05:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 3aaf5c97-ba8a-3274-afec-7b1d984ac8f5 | -6.5094 | -44.6847 | 2024-11-06 05:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 5cf2a127-633a-34b6-b4ec-10b06f9c4227 | -6.1041 | -43.9593 | 2024-11-06 05:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 3b5415fc-e211-3f8a-b6ab-be845cbba09f | -0.9703 | -47.8198 | 2024-11-06 05:00:00 | GOES-16 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| cbfc9c29-6a84-3ee5-8895-8c445f4d586d | -3.5446 | -47.3855 | 2024-11-06 05:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 44952f12-a1b1-3227-86b4-0363fc571dbc | -2.937 | -51.0673 | 2024-11-06 05:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| f41f3977-e465-34d9-9e72-8104e9380c8e | -2.9186 | -51.047 | 2024-11-06 05:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 769e3ded-57f7-3eb0-9cc2-f277b518db53 | -2.7244 | -54.1351 | 2024-11-06 05:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 4d55bcdf-aeaf-3068-8ed5-bac89c914e72 | -3.0207 | -53.4227 | 2024-11-06 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| af72d1d4-e586-3baa-94ed-7207bd6bd14a | -2.9371 | -51.0465 | 2024-11-06 05:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 2fca2350-c9ba-3e3a-9b46-8f5d6778b169 | -3.9669 | -48.1716 | 2024-11-06 05:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| b364940c-6241-3e50-8ffe-023d40c06d9f | -4.1432 | -43.5822 | 2024-11-06 05:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 178a348a-838a-3ec0-b6ee-5e1d765976f8 | -3.967 | -48.15 | 2024-11-06 05:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 1c21ef78-f7cf-37a3-aa04-ece8a85564c8 | -6.4827 | -47.4827 | 2024-11-06 05:10:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 190fe11c-50db-3bd5-a370-3e4a148a3fa8 | -3.0396 | -53.2805 | 2024-11-06 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| dff740cf-12f8-3f46-9b3e-9aab584d2b05 | -6.5014 | -47.4813 | 2024-11-06 05:10:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| d39f6a9c-8f25-3c06-ade4-a95f251bc685 | -2.4457 | -49.039 | 2024-11-06 05:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 64c17a11-8198-3189-b1bd-c99d2ac5ddbe | -6.5094 | -44.6847 | 2024-11-06 05:10:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| a15463b8-be5a-3028-8689-8615cf994e5e | -3.5446 | -47.3855 | 2024-11-06 05:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| a40bae57-d769-39c0-8054-23338a61f5bb | -3.0207 | -53.443 | 2024-11-06 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 220564ea-70e5-39fd-b9ca-b114566e1c2f | -6.4906 | -44.6862 | 2024-11-06 05:10:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| b1da3aab-3676-3d9a-b274-d8ab4c7fa378 | -3.0023 | -53.4232 | 2024-11-06 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 45f72c9b-0950-3c7f-b204-c54b33e39bf9 | -6.1226 | -43.9809 | 2024-11-06 05:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 6b736a93-0ca9-3486-93d4-2c25b37abeb7 | -2.8506 | -49.4744 | 2024-11-06 05:10:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 409e356f-b202-3ef1-8f01-59a6a4fc851c | -3.1617 | -50.2038 | 2024-11-06 05:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 120.3 |
| caec7ef6-b428-322c-9ffe-469461d296b3 | -2.7243 | -54.1552 | 2024-11-06 05:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 737bfbb5-82f2-34bb-812c-2c92004a4ceb | -4.1246 | -43.5833 | 2024-11-06 05:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| a6d58c35-92cf-321d-8796-853ed770013c | -2.937 | -51.0673 | 2024-11-06 05:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 578c6732-888e-3a8b-b192-6ff4280c8076 | 3.6184 | -51.3162 | 2024-11-06 05:10:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 54.4 |
| be9bfa83-de31-3d83-89cf-d86a3c378423 | -2.8423 | -51.7735 | 2024-11-06 05:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| a837cfce-9fbf-367b-a274-945f3f8ae283 | -3.5447 | -47.3636 | 2024-11-06 05:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 80ceaa56-aa24-3182-939b-0a17d62519f0 | -0.9703 | -47.8198 | 2024-11-06 05:10:00 | GOES-16 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| f4df754e-2a45-3d09-993d-45c9c9ea3e70 | -2.9186 | -51.047 | 2024-11-06 05:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| cc73dde0-ce15-3142-852c-d29b63927dd8 | -3.2164 | -50.3701 | 2024-11-06 05:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 6db501c9-c611-3f88-bce7-d113ebd8593b | -6.1041 | -43.9593 | 2024-11-06 05:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| c75a3fd1-b19e-3372-926b-b00841694ccd | -3.0397 | -53.2603 | 2024-11-06 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 340e9972-3cdc-3b81-9164-62802cabd67d | -2.8608 | -51.7731 | 2024-11-06 05:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 99c91c01-a4e6-3eb2-ad10-6ab1547ea8a3 | -3.2163 | -50.391 | 2024-11-06 05:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 7c4432e4-bff1-392d-8848-36526ceea8d0 | -2.91275 | -51.05289 | 2024-11-06 05:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 505bdeca-58f3-30c8-8282-946c825828e7 | -5.02397 | -43.60305 | 2024-11-06 05:12:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e7e492d7-6ef4-3327-9a62-c8101e305af1 | -2.82316 | -52.92116 | 2024-11-06 05:12:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 148.4 |
| b12d44ef-1da5-3a3a-855c-7f769832b0c0 | -6.49955 | -47.48822 | 2024-11-06 05:12:00 | AQUA_M-M | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| a3acdef9-2589-33c7-8457-f052e3a2c9b2 | -2.94558 | -51.03844 | 2024-11-06 05:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| dcf9ddc6-6496-33a4-b277-85247d6a9c28 | -3.67682 | -50.2284 | 2024-11-06 05:12:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 7f50940a-cb00-365d-ab0e-82f13c94d350 | -3.14911 | -50.19609 | 2024-11-06 05:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 3984a067-d221-323d-9b72-b436a506a139 | -6.50403 | -44.68818 | 2024-11-06 05:12:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2641d756-e318-3d82-8552-dbfc8d0bc18e | -3.9769 | -48.15619 | 2024-11-06 05:12:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 3fa4920d-4591-3304-88d0-992fe99ed411 | -4.14127 | -43.5738 | 2024-11-06 05:12:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 58235e90-b0c0-3c47-a619-8b40b4fedeb2 | -2.93099 | -51.03619 | 2024-11-06 05:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| cc5c42ce-072c-32cd-b0f2-26d2912b5471 | -3.21932 | -50.38285 | 2024-11-06 05:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| c7e72e47-d189-3aff-bee0-b6b38d488064 | -2.86354 | -51.75059 | 2024-11-06 05:12:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| dbde1800-5d59-3473-a87a-fee1eb5126d1 | -6.49511 | -44.68684 | 2024-11-06 05:12:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2dc92074-474b-34a0-970f-cd19c5f543b6 | -2.82521 | -52.92937 | 2024-11-06 05:12:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| c25160e7-f2fe-313c-ab7b-73a64be6b43f | -3.02115 | -53.41746 | 2024-11-06 05:12:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 5a65cce8-4d25-393b-9e92-42ea42f90161 | -5.55568 | -43.6913 | 2024-11-06 05:12:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cb9b04ca-6345-311c-b255-f70a99149054 | -3.02638 | -53.24996 | 2024-11-06 05:12:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 669564c0-8b91-3021-a9ae-b4d2e13a76ff | -3.07029 | -47.76796 | 2024-11-06 05:12:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| e1491065-1c5f-3778-94bd-cd62cff8aea4 | -5.9399 | -43.77256 | 2024-11-06 05:12:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 207fa66e-cd69-37b0-89d4-6ebbdc0be8ff | -0.96881 | -47.81302 | 2024-11-06 05:12:00 | AQUA_M-M | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 0740f0fa-7c59-30ec-ac6f-a5f83c5d84ca | -4.13242 | -43.5725 | 2024-11-06 05:12:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| fdbd0ad8-fade-31ad-9ae7-caef0553aa8f | -6.10508 | -43.96285 | 2024-11-06 05:12:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 613c0505-5b60-3dd3-a383-55223b649e2f | -4.75665 | -45.90596 | 2024-11-06 05:12:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fe0f5566-ba41-3ec0-a134-96a26f5dfef9 | -2.66772 | -51.83293 | 2024-11-06 05:12:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 0b9e2d95-9658-3195-89ae-5dc9e3ad0ac4 | -3.182 | -50.58783 | 2024-11-06 05:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 232f6af9-1e1a-398c-bad4-f9782c4a4c1f | -3.02989 | -53.25502 | 2024-11-06 05:12:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 8e660390-bb25-3ae7-a09b-c6c0c3fea062 | -6.11393 | -43.96415 | 2024-11-06 05:12:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| a6d5e406-e781-3b33-9833-be6878c96c1c | -3.33284 | -50.08274 | 2024-11-06 05:12:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 82087cc8-2623-3353-8333-8159f0ffaf7d | -5.66564 | -45.93734 | 2024-11-06 05:12:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 231a1795-81ea-342b-b761-eb32e49def26 | -3.71278 | -41.68364 | 2024-11-06 05:12:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| bd5e41f0-acd4-3d59-851e-d8c711003a83 | -6.50542 | -44.67912 | 2024-11-06 05:12:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 909daca3-78c3-3c89-8700-cd48e56c1f1f | -2.8312 | -52.89228 | 2024-11-06 05:12:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 141.8 |
| 6924fec2-3549-3fc8-a66f-0a5d36395200 | -3.53318 | -40.91107 | 2024-11-06 05:12:00 | AQUA_M-M | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 7d113810-b3a6-307d-9de1-031ba3594948 | -6.36345 | -47.91666 | 2024-11-06 05:12:00 | AQUA_M-M | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3dde366b-32f0-3814-9bd5-391538305e63 | -3.53219 | -50.33126 | 2024-11-06 05:12:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 51272c26-d922-3a82-86c1-82cfa8251614 | -4.12225 | -43.58003 | 2024-11-06 05:12:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d00bb7e2-01dd-358c-9f7a-0b4d354b03d5 | -5.06776 | -44.23149 | 2024-11-06 05:12:00 | AQUA_M-M | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README58.md)
