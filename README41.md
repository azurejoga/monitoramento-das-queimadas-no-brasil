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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0e26896-e391-35e3-bc14-52e78c3d10ef | 0.66245 | -51.79459 | 2024-11-16 04:48:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13e88ce4-6a07-3b85-a399-435be6524304 | -2.29295 | -48.18492 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 461c4c53-e976-3f89-8c1c-9daef25c4f62 | -3.28036 | -45.5073 | 2024-11-16 04:48:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 2f159814-b0ac-3d45-ad9a-648a3b42289a | -2.9086 | -46.85796 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c679223-2658-3cef-9d34-7cf436092865 | -2.45912 | -53.69681 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 234e3bb3-695c-3c35-adfa-5a68383c29ef | -2.08413 | -50.33533 | 2024-11-16 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a373ea33-2e5f-39ec-a196-e013d398e97c | -3.74428 | -45.65297 | 2024-11-16 04:48:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 82b679e9-4960-3167-bb2b-a69aae9a60da | -2.6383 | -46.56019 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9eb09d0-6c91-31af-911b-b53679ee7178 | -2.68077 | -46.82444 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29d7074b-cd04-39a2-ac7f-120093878b7a | 0.84584 | -51.83743 | 2024-11-16 04:48:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 064eb58e-bf14-3f32-b54a-72fa81a2eafc | -1.69087 | -48.46693 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e23bde12-1e50-31e9-baf6-4a35f75a8181 | -2.90254 | -48.30913 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4de4e762-c991-3a3c-95de-3bd27d27d3ca | -1.6765 | -48.46474 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22d1fbe2-d8e2-330d-aafc-f09848c76f52 | -3.97218 | -46.70918 | 2024-11-16 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b32e2427-a41d-3932-8880-5a326e9e4e98 | -1.69758 | -50.20287 | 2024-11-16 04:48:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 576678b9-27d6-3daa-8de3-60e9353246a4 | -3.27594 | -45.50663 | 2024-11-16 04:48:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 5e25e8d8-9e1d-31b0-9835-fb1962b5d941 | -2.17487 | -48.44131 | 2024-11-16 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e37c3124-f5ab-3940-a007-a19ddba396c8 | 0.04786 | -49.52896 | 2024-11-16 04:48:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e41d676d-d46a-3a25-9b28-585b7bb9d88d | -2.13833 | -46.40093 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f692098-953e-318b-b113-cd978ca2dbb0 | -2.90513 | -46.8539 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82738cf2-c883-39d6-9ed2-584e973207e4 | -1.70924 | -46.16422 | 2024-11-16 04:48:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fb0f7c7-3b39-3484-8c0b-c35a172b6279 | -0.23979 | -48.57322 | 2024-11-16 04:48:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 759be1da-939d-3a11-b5f5-22f304ec5be1 | -2.89564 | -45.34594 | 2024-11-16 04:48:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 545d24f7-e237-3efa-9ad3-c30d49c182ec | -2.22645 | -48.37209 | 2024-11-16 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12aa278f-322b-3a22-84fe-af2d70bedeb7 | -2.21818 | -47.21633 | 2024-11-16 04:48:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75cca921-130b-3c50-8c1b-b8a8197e1bdd | -1.19054 | -53.71913 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b556caf-820f-307f-b64d-2cf74129d749 | -1.74946 | -50.47879 | 2024-11-16 04:48:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 783e51a5-259f-3653-bd72-67f0977606c7 | -2.35713 | -49.11351 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 000fee43-f82b-3f88-a671-044f99f84563 | -2.28257 | -47.91603 | 2024-11-16 04:48:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f0134392-06ae-3305-a776-f30cf1343ecb | -2.25516 | -48.38396 | 2024-11-16 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7dc439f-5095-30c8-9aeb-b9cf873f5d87 | -1.95819 | -47.83644 | 2024-11-16 04:48:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e66cbd6e-a4e3-3566-8cce-08ccf5ce13f7 | -2.64937 | -46.16356 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48b7f0c4-75dc-33cc-89bb-bb643b0bf438 | -2.11188 | -50.13495 | 2024-11-16 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1262e39a-8045-3a40-97b1-f8c3b4b4d95c | -1.63883 | -48.51764 | 2024-11-16 04:48:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee25cdaf-9152-387a-9ce9-7c0bcd3a47cd | -2.08748 | -50.33585 | 2024-11-16 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e6fe15a-5c4f-3111-acbd-693234311d4a | -2.66559 | -46.84307 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5322a7e4-34ee-3b18-b858-b4f4f2541627 | -2.61201 | -54.53814 | 2024-11-16 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e1fa6a4-01d9-36db-93a6-8605656c34b2 | -2.44856 | -48.02386 | 2024-11-16 04:48:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b132a44b-abf3-3117-8bcf-27babe15b99f | -2.90164 | -46.8499 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ffbee38-46f7-3abb-88fb-aa63ee9ef457 | -2.02828 | -50.08551 | 2024-11-16 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16ffa463-8552-30a3-a0f0-8d6007927b23 | -3.72973 | -45.65969 | 2024-11-16 04:48:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7b114d52-7ab4-370a-a119-abf0b7c99ed9 | -2.11197 | -50.81031 | 2024-11-16 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4283b8c8-af9f-345f-98c3-f5e6ef4ef381 | -2.81445 | -54.01959 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08ee54d2-4184-378c-842b-5ededa4aef52 | -2.14791 | -53.71497 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 091fa22b-8161-3554-995a-f757232b5c86 | -2.6461 | -46.83664 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5065454d-2b8a-3126-af42-7e4a2f408871 | -2.35653 | -49.11742 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e630f442-b8ed-35fe-bd0b-e736f8c793ed | -2.77784 | -48.58507 | 2024-11-16 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35578579-c94a-3513-a49d-e6c5402ec748 | -2.66435 | -46.17756 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 584b8cbf-ee77-3716-819c-52b92e3085a5 | -2.57348 | -54.41566 | 2024-11-16 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2456aaa-271b-3eb7-b4f7-1539e51407d0 | -2.57575 | -54.42413 | 2024-11-16 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66056cca-f2f4-37df-b0f1-7abc7ae4bc21 | -2.66612 | -46.83963 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e96a46f-5bf4-3359-8e29-2a8070e528f6 | -3.73804 | -45.66407 | 2024-11-16 04:48:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b5a2ed34-4da5-3978-9153-2967c3b36dee | -2.20607 | -49.28622 | 2024-11-16 04:48:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60a4f74d-2bd3-3d7a-b284-2fe85310ac7e | -2.70702 | -47.72628 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 583ff2b7-91b1-3e04-afe7-711ad432822e | -3.73867 | -45.65977 | 2024-11-16 04:48:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 9141b417-eec4-39bf-993b-1d8eb9e9d805 | -2.13797 | -48.12455 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30352942-b5c5-3dec-8ba2-146883758ec3 | -1.6933 | -47.97474 | 2024-11-16 04:48:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81b4c8e4-f2bb-30d9-853f-d66b67ec2c3e | -1.46016 | -48.19997 | 2024-11-16 04:48:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d2a8519-66b4-3f40-b4e5-100acc7e4cb7 | -2.40535 | -48.47405 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c56473be-dd6c-352d-b395-bc76b3a1be8a | -1.58494 | -50.44658 | 2024-11-16 04:48:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96abc63c-560f-3f93-b714-75c790e3371b | -3.02992 | -47.99338 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e46fce5-a67e-3456-8332-db9f61963150 | -1.99868 | -46.58072 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 849c36f0-386b-37c9-854f-3af3a36a7f72 | -3.01396 | -47.97248 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65cbb7f3-4ac6-37ea-90e0-12e5f3ecdfae | -2.22019 | -50.51164 | 2024-11-16 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0050a969-43a1-3faa-93a7-3be7892de144 | -2.05012 | -48.89705 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a057c66b-66e6-3845-ab72-f3e7fd9b1238 | -2.14328 | -46.55976 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bc4a1c04-fc60-3572-88b4-5f199a7bf7c2 | -2.94138 | -48.32254 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54f8b14b-9b9f-3c93-ad3d-20b3f1d518ce | -3.92916 | -45.85598 | 2024-11-16 04:48:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4b29fc6-754d-39c3-a6d1-70991e72c54e | -3.98725 | -43.72243 | 2024-11-16 04:48:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e8f06589-9720-3a18-aa16-fc1b99a202ae | -2.0812 | -48.95337 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3548ac0f-390b-3350-bf54-5715243a389d | -4.00299 | -44.34269 | 2024-11-16 04:48:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 991c366c-7611-35c8-8c25-2a8815bd817b | -1.6911 | -53.47681 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0736e408-be10-3e05-8d6d-bf753e4f98c1 | -3.40757 | -50.25388 | 2024-11-16 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba30531d-189c-33a1-9a6e-9d434aedb51a | -2.15602 | -50.46201 | 2024-11-16 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc9618d4-258a-360b-9b6e-97c234c75355 | -3.98262 | -43.71872 | 2024-11-16 04:48:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 671ca27c-d83e-3921-8121-1909ec5cc1b5 | -2.66375 | -46.1814 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49d34b8b-002d-393e-ba43-57c3e1a927c2 | -2.16039 | -48.90891 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e319b6f-ab20-3b4d-8031-0f025d580516 | -3.12251 | -45.89651 | 2024-11-16 04:48:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74d642f4-06a4-339c-b7ed-919449150b65 | -1.68433 | -48.46173 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 355b41a7-71e7-3cf2-bbef-3cca9f800a76 | -3.59023 | -47.35209 | 2024-11-16 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e448396-4671-32c3-8c14-ddd0f2366638 | -1.63106 | -53.27974 | 2024-11-16 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e33f1a8c-c406-3a54-ab01-96f11f34cf5d | -3.08417 | -47.76798 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db43425c-ca8d-3b34-a559-cfdb5d8a83a5 | -2.22431 | -53.60755 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| e9a5be71-6a4c-3ae6-9486-0d70ad14b8d3 | -3.4947 | -47.21662 | 2024-11-16 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8bc93f93-44e0-34ee-97a1-da79744dcea2 | -2.81243 | -52.9238 | 2024-11-16 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ba3de17a-8a27-3ec8-b08f-b3b0dcea7223 | 0.84791 | -50.20802 | 2024-11-16 04:48:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0829da85-d858-32a5-9c45-bbbeea443cec | -1.68793 | -48.46227 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cc46b0b-4193-3555-8697-0b85f524d943 | -2.50873 | -47.47659 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| de3cdc6b-359d-3591-ba3a-b9a962f7f9e7 | -3.52077 | -44.72018 | 2024-11-16 04:48:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 919fe4be-1c62-3324-9019-a3fcbd02c27c | -2.45674 | -53.9734 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 679ec9bb-e12e-3b89-b371-a1c8873682fc | -2.23739 | -46.83706 | 2024-11-16 04:48:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00e913d5-aaf0-3166-bbb0-2b15b77642ee | -2.34389 | -47.47084 | 2024-11-16 04:48:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7d204321-0e62-3191-85fe-b6bcf483b6d2 | -3.11822 | -45.89586 | 2024-11-16 04:48:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a78bf81-f386-368c-93b7-3d3fc78d3cd4 | -3.40813 | -50.25025 | 2024-11-16 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0949c02e-30df-388e-93b2-a12632f05e17 | -2.3519 | -49.11785 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 518510b1-3bf8-3116-8dd7-4d53f2bdc853 | -2.45903 | -46.36907 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 969565f7-1ec4-363a-a76c-cfb82328ab0a | -1.16448 | -53.50237 | 2024-11-16 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14948e24-9bbc-3c68-87cc-0126afba29e7 | -2.39862 | -50.32156 | 2024-11-16 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0803f35a-201f-3a18-a0cf-4cc7c400a36c | -2.25532 | -50.45556 | 2024-11-16 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60762f5a-530a-315b-a602-6a2ae2689f1a | -2.54674 | -53.98738 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README42.md)
