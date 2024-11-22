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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c4af904-2310-375b-9acf-2f60216b2f5c | -2.71973 | -46.09692 | 2024-11-22 03:49:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0396b5db-0720-3af4-a266-25389ba5d70a | -4.39854 | -44.11792 | 2024-11-22 03:49:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 03ccef29-646a-3d3f-b5d2-b2d3796c1915 | -9.29558 | -43.12629 | 2024-11-22 03:49:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 86fca925-4103-3a59-8ac0-9b7f28e2dedb | -3.46396 | -45.90953 | 2024-11-22 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f2c91128-5e73-302b-89eb-560b5b21bce2 | -3.46482 | -50.01021 | 2024-11-22 03:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 36e95f2e-f855-399e-8702-e68ce09f3537 | -3.45908 | -45.90506 | 2024-11-22 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 647c7b97-79b3-34b4-b440-e27cdfc19f66 | -3.76311 | -46.1194 | 2024-11-22 03:49:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1e75b4e9-eb0d-3659-bc53-01a39cf333c1 | -4.69138 | -45.66637 | 2024-11-22 03:49:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ec3e78c-f50f-3f9f-a416-62f8c86980d5 | -1.5224 | -47.06147 | 2024-11-22 03:49:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1a2a7b0c-e5c9-3b8c-b67c-21ffcdf088c2 | -8.92646 | -44.24825 | 2024-11-22 03:49:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92f26655-91f4-328a-ac85-100bd85bed8d | -4.70094 | -46.07536 | 2024-11-22 03:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb5cfca8-f3dc-3bf8-ad2f-9f916733d2a4 | -5.32518 | -44.7835 | 2024-11-22 03:49:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 336eb2d4-d9a0-34ce-b93b-71f5171ad339 | -2.30204 | -45.50745 | 2024-11-22 03:49:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef23cbd2-8878-3d94-b13a-ba76d6dff491 | -8.21995 | -37.38782 | 2024-11-22 03:49:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2cafc20a-9aea-3600-ac37-205494f0f74f | -5.59768 | -43.74002 | 2024-11-22 03:49:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c12652bd-e6fc-3036-a012-0d7765c43f21 | -3.45848 | -45.90861 | 2024-11-22 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0431d433-e976-3920-90c6-6eb86e3102bd | -5.72531 | -46.18512 | 2024-11-22 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d36ad377-751e-3f20-927e-2cfd9ccfcdde | -6.12084 | -42.52194 | 2024-11-22 03:49:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| c9ec4d34-0d1e-3472-96f8-3bf7aaff4c0d | -3.48453 | -42.29934 | 2024-11-22 03:49:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9e6ba439-ad0a-3217-9274-c19ab2a8e43e | -4.70286 | -48.29899 | 2024-11-22 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dad0081c-da73-3ab5-b974-c42c15ba777b | -5.32646 | -44.7856 | 2024-11-22 03:49:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a88c4a27-4232-33a5-9e6d-0a893cd4a96d | -4.68608 | -45.66552 | 2024-11-22 03:49:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f342c9e-1989-3353-b0a1-6182c6bbe9fd | -6.43437 | -39.27834 | 2024-11-22 03:49:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8baa4778-c620-3587-bd08-fc832299c8eb | -3.00756 | -45.12854 | 2024-11-22 03:49:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc3e523a-d4cf-38ae-8659-9062ca4e7de2 | -7.4606 | -39.22884 | 2024-11-22 03:49:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7a458295-bcea-3fc9-b5c8-7e05b0d831e6 | -3.2768 | -53.8199 | 2024-11-22 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| eae60a2c-bc81-35af-82fa-cea7306ee76f | -3.22 | -54.2636 | 2024-11-22 03:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 5ce8308e-cefb-35c4-9018-5c3866a9da41 | -6.1182 | -42.5086 | 2024-11-22 03:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 55.7 |
| 3bffb151-7b0b-344b-8858-79e18659f228 | -1.1857 | -51.948 | 2024-11-22 03:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| e8b0a0a3-0e88-3813-8ed4-5f2d83e4b947 | -3.2385 | -54.2431 | 2024-11-22 03:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 219.5 |
| 08d17ba4-c3a6-39fb-80d1-9c8aef4a7ecf | -3.2201 | -54.2436 | 2024-11-22 03:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 144.7 |
| 75c4e42e-eb6a-3dfd-b2f3-9d5436075122 | -3.2569 | -54.2426 | 2024-11-22 03:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 7ef30143-64d1-3a71-9713-e4d52826fd17 | -1.1287 | -53.3951 | 2024-11-22 03:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| f80aeb2b-604e-384c-ad2b-93a85fa12166 | -1.2041 | -51.9683 | 2024-11-22 03:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 37897ff6-45bb-3528-9a31-a0a303db05a1 | -3.4778 | -45.9096 | 2024-11-22 03:50:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 56.3 |
| e6e31993-2784-35c9-8312-0af98f8bdbed | -1.5869 | -53.8134 | 2024-11-22 03:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 9e3c86fa-f67b-3a4b-b16f-3c0448380f42 | -3.5159 | -53.8132 | 2024-11-22 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 7e860470-653d-3082-a370-7ba8f8c1f4d6 | -3.2384 | -54.2632 | 2024-11-22 03:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 7b773bf5-376b-3e91-8dbc-27cabb3fa673 | -1.2041 | -51.9478 | 2024-11-22 03:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 2ffab88f-310e-38b9-9641-ba2868b6089d | -3.4593 | -45.8881 | 2024-11-22 03:50:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 85f49a0f-9fa0-3a7f-abc7-242dc8997614 | -3.516 | -53.793 | 2024-11-22 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| d9b29df8-961b-32c0-92c8-767674ddc8dd | -3.4592 | -45.9104 | 2024-11-22 03:50:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 134.9 |
| 2842e286-8003-31fb-b98f-03d6d35b1f3a | -3.2767 | -53.84 | 2024-11-22 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| eec98cd6-ffb4-3c53-a2af-e463ed7f24a2 | -3.2386 | -54.223 | 2024-11-22 03:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| c8d3a0b3-7154-3d76-bac5-da557c0492ff | -10.65727 | -48.11022 | 2024-11-22 03:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cb27eea9-3d92-36e3-9915-9e8e8adf35fb | -10.6636 | -48.10744 | 2024-11-22 03:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61f3dbbd-2ca5-3e0e-b5be-d3ea5e228093 | -10.65802 | -48.10627 | 2024-11-22 03:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a69e6fa-80bb-323f-a486-722bc353a6cd | -10.98555 | -38.16553 | 2024-11-22 03:51:00 | NOAA-21 | TOBIAS BARRETO | SERGIPE | Brasil | 2807402 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3bace130-34b2-359b-aefb-82f0229b5688 | -13.37069 | -43.9258 | 2024-11-22 03:51:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b83a9911-93e2-3a26-99e0-c7b961fd943c | -11.73682 | -47.23884 | 2024-11-22 03:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b55fd11-9e82-3326-9ae5-6e1abf569f3d | -12.13918 | -40.89354 | 2024-11-22 03:51:00 | NOAA-21 | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ba57e226-5cfd-33f8-8c15-6f6f2ae0ec7d | -13.88623 | -43.07636 | 2024-11-22 03:51:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2b7936f8-3106-3d97-8c49-4050b667cbc7 | -12.42584 | -46.63652 | 2024-11-22 03:51:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b2d6b8f-a90f-395b-826c-2262f99dc808 | -10.70946 | -40.51165 | 2024-11-22 03:51:00 | NOAA-21 | ANTÔNIO GONÇALVES | BAHIA | Brasil | 2901809 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7cb0a4eb-9005-3835-bc01-7b263787aedd | -10.84984 | -41.24081 | 2024-11-22 03:51:00 | NOAA-21 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 43b490d9-d0ad-343a-b981-6acc43fc76fe | -12.44133 | -46.66305 | 2024-11-22 03:51:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0cec8c47-5c57-3794-83b2-79680815691b | -13.10156 | -43.32173 | 2024-11-22 03:51:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 82e43b25-1113-3aa7-b29d-5d4f27823d75 | -12.83566 | -43.89608 | 2024-11-22 03:51:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05f7e60b-4a87-3fde-84e4-4fab1830b3c0 | -13.87389 | -42.91995 | 2024-11-22 03:51:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3cc73563-3cfc-3a54-97b2-23e523f9c729 | -12.65449 | -38.10425 | 2024-11-22 03:51:00 | NOAA-21 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 65a01a74-b5ea-39c2-b2bd-907527655f0e | -10.59724 | -38.40778 | 2024-11-22 03:51:00 | NOAA-21 | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8aac986b-88cc-3449-ab92-9b51b2baac21 | -13.8701 | -42.91926 | 2024-11-22 03:51:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c46f99ab-90e8-3866-b5a0-c2bf92eba1f3 | -11.08532 | -40.54839 | 2024-11-22 03:51:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a778b4e9-efec-3a74-b62f-bf917b05e32f | -12.7108 | -40.21534 | 2024-11-22 03:51:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ec7ed5fd-5b7a-30ec-88f5-f9e98a5832b5 | -15.52035 | -43.10355 | 2024-11-22 03:51:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 588b543d-3dc2-3c5b-b790-697c9e409348 | -12.85754 | -43.81968 | 2024-11-22 03:51:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5929e729-a849-30ef-8bc7-1b3b49cfc8da | -11.7362 | -47.24203 | 2024-11-22 03:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da75738a-f844-3e03-a3c4-e519eb2e1a14 | -11.78192 | -41.32013 | 2024-11-22 03:51:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4c687b2f-4c71-33d9-a592-7b5429ee84ed | -12.44626 | -46.66407 | 2024-11-22 03:51:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a9162ec0-7f79-371a-b1aa-4abba42a1aff | -11.8327 | -44.22705 | 2024-11-22 03:51:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96db83ea-8af7-3e6a-9eea-0619089970a3 | -12.40671 | -38.86187 | 2024-11-22 03:51:00 | NOAA-21 | SÃO GONÇALO DOS CAMPOS | BAHIA | Brasil | 2929305 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ae419344-9c74-3f91-a407-20c1fd253143 | -13.87092 | -42.91449 | 2024-11-22 03:51:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 34d35f81-d7b5-3691-a311-93b152630cb6 | -13.01135 | -40.18386 | 2024-11-22 03:51:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b0034dc0-22ee-3dc9-a0f9-6c4ce847417a | -13.10247 | -43.31663 | 2024-11-22 03:51:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d3514e07-6819-3ca7-a9bd-ce548456f716 | -13.29071 | -39.80414 | 2024-11-22 03:51:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cb558020-de30-3bb9-8004-d0a7ccbf428f | -14.13372 | -41.63177 | 2024-11-22 03:51:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 32c9f42f-682f-31a9-9ee5-33322de96a1e | -13.29012 | -39.80779 | 2024-11-22 03:51:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 08e83480-85ea-3567-ace7-164ce91648f2 | -11.74202 | -47.23981 | 2024-11-22 03:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d1737a94-cc03-3d06-9653-d8657e7d14d0 | -14.17618 | -43.70671 | 2024-11-22 03:51:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 354a2908-a9ef-3eff-a783-5133fa569e36 | -10.968 | -37.18067 | 2024-11-22 03:51:00 | NOAA-21 | SÃO CRISTÓVÃO | SERGIPE | Brasil | 2806701 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a0ef91e6-fec9-37da-b902-e613bf3e0c3e | -12.18728 | -41.34766 | 2024-11-22 03:51:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 898a817c-37cc-35b1-bd9e-e9da5bfc2307 | -15.51921 | -43.10485 | 2024-11-22 03:51:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b3bba85c-b8bd-32b0-a35a-997cf7dce204 | -11.74141 | -47.243 | 2024-11-22 03:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 423685ae-ae47-3e8e-b722-4e1f7a824235 | -11.88523 | -44.22304 | 2024-11-22 03:51:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b8f7bdb-14f2-3432-8786-235e895ec8bf | -12.1866 | -41.35169 | 2024-11-22 03:51:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 02540f71-a543-35d3-b140-9fa0118ed8d2 | -11.74263 | -47.23665 | 2024-11-22 03:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53ff8cb1-f85e-3013-b6c7-f92d327896d7 | -11.44679 | -39.5858 | 2024-11-22 03:51:00 | NOAA-21 | SÃO DOMINGOS | BAHIA | Brasil | 2928950 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1ed29607-6c90-355b-8d1b-056a749c48f8 | -21.60363 | -42.9999 | 2024-11-22 03:53:00 | NOAA-21 | ROCHEDO DE MINAS | MINAS GERAIS | Brasil | 3156205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 170b4a65-52d4-349b-9a04-3a7187151627 | -1.1857 | -51.948 | 2024-11-22 04:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 893b1e4a-157c-3cfa-b946-1457089c5dfb | -3.2767 | -53.84 | 2024-11-22 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| ee96ccc1-9a47-36dd-9acb-59eb60213212 | -1.1287 | -53.3951 | 2024-11-22 04:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 4b6582c4-871c-3b0e-a520-ea000df751c1 | -3.2385 | -54.2431 | 2024-11-22 04:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 213.6 |
| 5e611756-9b73-3182-9f16-6d91ab8abcd4 | -1.5869 | -53.8134 | 2024-11-22 04:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| afae9502-be80-34dd-bd9b-253375f37daf | -3.516 | -53.793 | 2024-11-22 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 68264f99-aac8-323c-a179-c0c17e6c4d0b | -3.2386 | -54.223 | 2024-11-22 04:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 4387ea2c-8235-3ea2-a771-559d7dcd9c94 | -1.2041 | -51.9478 | 2024-11-22 04:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 78601b87-b31b-3a0d-8efd-b730ee8f5b39 | -3.2569 | -54.2426 | 2024-11-22 04:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 385b5a25-3566-3f03-a05c-e24d234bce23 | -3.5159 | -53.8132 | 2024-11-22 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| c33d932d-4ffb-35fb-a6c4-ec4edc8af6d9 | -1.2041 | -51.9683 | 2024-11-22 04:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 85dc688c-7d3c-365a-9d0d-b340c1770301 | -3.4592 | -45.9104 | 2024-11-22 04:00:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 97.5 |


[Clique aqui para ver as próximas entradas](README17.md)
