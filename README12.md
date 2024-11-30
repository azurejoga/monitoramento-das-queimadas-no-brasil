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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb9a02bd-e885-3b3d-a895-d185086e78cb | -3.2407 | -53.6191 | 2024-11-30 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| fb841e81-9700-33e7-bfbf-fd32aa4d9f1e | 1.1805 | -55.9671 | 2024-11-30 02:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 304180c8-aaa0-3921-bcc4-59d8f6f56ecb | -4.8711 | -41.3157 | 2024-11-30 02:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 210.8 |
| de07579b-ee90-3871-a37b-0871c9ba124c | -6.0862 | -48.0339 | 2024-11-30 02:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 8b3f3fb5-a429-36ab-82cc-3593007bfed4 | -6.9344 | -43.5401 | 2024-11-30 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| e76fb0aa-42d9-39ee-9201-21e8221cafcb | -3.9886 | -41.5165 | 2024-11-30 02:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 60.5 |
| 86c288ba-9a8f-36eb-be0d-37b452e21db0 | -3.259 | -53.6388 | 2024-11-30 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 149.4 |
| eaf1a9c5-8cec-30c8-b0a4-e4159842b09b | -6.0674 | -48.0569 | 2024-11-30 02:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 1d850cb5-b02c-3cea-a453-057a4b390b62 | -4.8901 | -41.2902 | 2024-11-30 02:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 212.0 |
| 74f27efe-ece5-3f4e-9539-58708d90a2db | -6.086 | -48.0557 | 2024-11-30 02:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| ed43683f-1c45-31fe-8462-76485cb83529 | -4.8713 | -41.2915 | 2024-11-30 02:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 295.5 |
| 46125f10-02f2-3975-af9f-aa4bc4afe05d | -17.6654 | -57.5645 | 2024-11-30 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| fa5e2d2b-14ad-3bce-88fe-9615ed3fc43a | -3.6758 | -47.1176 | 2024-11-30 02:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| c30eeb2d-19ba-3b16-a0bb-7b26d7a0fa21 | -3.9699 | -41.5176 | 2024-11-30 02:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 62.1 |
| cc8a927a-4332-38d4-9a1a-85e56dbcb5df | -2.0163 | -50.7768 | 2024-11-30 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| c60985dd-eeb7-3dc2-b6cb-1ad739710075 | -1.6419 | -53.8731 | 2024-11-30 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 2c0a0edc-703a-3b0f-8138-0294950ced00 | -3.2591 | -53.6186 | 2024-11-30 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 146f7941-d59f-3723-a9b4-0b66e882239e | -6.9158 | -43.5185 | 2024-11-30 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 01a84045-961b-3d29-ac82-8df987f668dd | -2.0163 | -50.7768 | 2024-11-30 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 601932fb-bb86-3838-96f7-941d65df7cb9 | -6.0674 | -48.0569 | 2024-11-30 02:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| eeb49aee-69ed-36de-b9db-6fb0eec74b7e | -4.8715 | -41.2674 | 2024-11-30 02:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 158.2 |
| 28e9f90c-4239-317c-b324-5d43c85232dc | -2.1351 | -54.8861 | 2024-11-30 02:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| e2740d02-b58f-3728-9682-4e2c4a7bd45e | -3.017 | -45.12 | 2024-11-30 02:50:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 0fde11cc-ce4a-3c3a-86eb-aa0b1d41dd9f | -3.4976 | -53.7935 | 2024-11-30 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 2cfb9e62-6dd8-309d-8d60-bc83ebefa17c | -6.0676 | -48.0352 | 2024-11-30 02:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 46ec5838-c2ae-3807-9d95-173c3bd08e76 | -6.8967 | -43.5436 | 2024-11-30 02:50:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| a43b72ef-d749-3ca2-9d6f-da94493d7484 | -4.8903 | -41.266 | 2024-11-30 02:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| bb77b0ce-1a37-3e62-915f-ecac5b3d2676 | -3.259 | -53.6388 | 2024-11-30 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 153.1 |
| a1bd4cd3-eed1-31d9-bc88-b7cb219361a1 | -1.0733 | -53.6378 | 2024-11-30 02:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 4e6ef0f4-9405-3397-8fd5-7c0040289768 | -3.2406 | -53.6393 | 2024-11-30 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| a122364b-9214-3d1b-8523-2b55e4e7044a | -6.086 | -48.0557 | 2024-11-30 02:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| deb3e918-733d-3801-93a1-407c566373d2 | -4.8901 | -41.2902 | 2024-11-30 02:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 162.2 |
| 54604b66-5103-316c-bf66-177e3616ea34 | -6.0862 | -48.0339 | 2024-11-30 02:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 0e81d901-206c-394e-8d22-6453e186253e | -6.9341 | -43.5634 | 2024-11-30 02:50:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| ea3c739a-da72-3708-8094-a5f2fe51a493 | 1.2172 | -55.9274 | 2024-11-30 02:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| fc1c4d84-8892-3699-a28f-ec844b8e8c7a | -3.6757 | -47.1395 | 2024-11-30 02:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 7ab99025-d0a8-360c-bb2f-81ea27aa5e4d | -4.8713 | -41.2915 | 2024-11-30 02:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 249.8 |
| 4dbd3c84-d254-3ed2-b6f4-bd6fa74d60da | -17.6654 | -57.5645 | 2024-11-30 02:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 70ddfb6c-b3fb-3e7a-b94c-15b124d6c02a | 1.1805 | -55.9671 | 2024-11-30 02:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 1c02bd0d-520f-3acf-ba85-8bb11719ea95 | -4.8899 | -41.3143 | 2024-11-30 02:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 85.2 |
| e6900d23-eda4-3f6f-b4f9-04d2a4742e7d | -6.9344 | -43.5401 | 2024-11-30 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 111.4 |
| c077adaa-6114-397e-8b82-4c93676e162c | -3.2591 | -53.6186 | 2024-11-30 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| bb43eb7b-8f63-35e3-8c75-44d8be5581ce | -6.9156 | -43.5418 | 2024-11-30 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 458.8 |
| b097b19c-f325-3625-b2c5-e1791bf81e6d | -3.4791 | -53.8142 | 2024-11-30 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| bf771449-dd0a-3fbc-ba61-40313b85fb70 | -4.8525 | -41.2928 | 2024-11-30 02:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| bea6210e-f5af-3aae-82af-695878a1d6f7 | -1.6419 | -53.8731 | 2024-11-30 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 580ddd59-32d5-390e-a74f-27af095cd343 | -3.4975 | -53.8137 | 2024-11-30 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 97a1a9b6-f1ee-34ec-b4af-43ee01de80c1 | -3.0171 | -45.0974 | 2024-11-30 02:50:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 2937f756-8878-3d40-8d59-fcf00f7c1a25 | -1.6938 | -46.7833 | 2024-11-30 02:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 59029b97-43c5-3576-8717-8f0759921c94 | -4.8711 | -41.3157 | 2024-11-30 02:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 154.6 |
| 884ff524-c45f-332d-ba94-8921779e3c10 | -6.9153 | -43.5652 | 2024-11-30 02:50:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 290.8 |
| dcc7332c-4284-30bd-af5b-c1af9daa5b31 | 1.1988 | -55.9472 | 2024-11-30 02:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 94dfebf0-7cd5-32dd-8df9-200da08daf8d | -17.6651 | -57.585 | 2024-11-30 02:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.8 |
| e0f30034-861b-354e-a2f3-b9d3486c5cf5 | 1.2171 | -55.9471 | 2024-11-30 02:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| e08d1a12-9e7d-329f-8bb2-7a3e6ac59d0e | -3.0171 | -45.0974 | 2024-11-30 03:00:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 3fa242e6-a8f1-3c97-8ff6-6eeb2e69788f | -3.259 | -53.6388 | 2024-11-30 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 92281dcc-d452-3143-b47f-37e3cd23a36f | -1.6938 | -46.7833 | 2024-11-30 03:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| ca121a49-211c-3669-bd01-73ca88b490fd | -3.2406 | -53.6393 | 2024-11-30 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 82732a33-4646-34ed-92d4-9c7176715c3b | -3.6757 | -47.1395 | 2024-11-30 03:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b2f8b6f1-66fc-3481-aa3e-e92f39f88c6f | -17.6651 | -57.585 | 2024-11-30 03:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.7 |
| 679773ed-c442-3f67-9c36-30f1a13efe77 | -3.4976 | -53.7935 | 2024-11-30 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 33213fe5-6ce6-3d50-ae48-740172e82ea0 | -3.6758 | -47.1176 | 2024-11-30 03:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 89faefe4-2c5a-3d37-a60a-b60f57ff0025 | -4.8713 | -41.2915 | 2024-11-30 03:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 214.8 |
| e278a48f-c991-301d-9da7-a15d5c0e280e | -2.1351 | -54.8861 | 2024-11-30 03:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 41cd04dd-ec09-33c3-bfdc-0567155ba410 | -1.6419 | -53.8731 | 2024-11-30 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 45b199cf-f2a5-32f4-a8ff-faea7f7f3545 | -4.8711 | -41.3157 | 2024-11-30 03:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 114.0 |
| c851468b-7d3c-35cd-a8a7-ee88a6ecd5af | -3.2591 | -53.6186 | 2024-11-30 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 47159c4f-8434-3ec4-b8ce-9c3926b73ed0 | -3.4791 | -53.8142 | 2024-11-30 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 967c76eb-febd-3fea-966c-6a7501f95a78 | -3.4975 | -53.8137 | 2024-11-30 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| faf2253a-763d-3114-bf8f-27dd84fdddec | -1.2015 | -53.8581 | 2024-11-30 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 56a6e116-8fa9-3d78-b37c-b02822e328ac | -3.017 | -45.12 | 2024-11-30 03:00:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 808a8161-eaaa-31af-9050-5b4f8a60baa1 | -17.6654 | -57.5645 | 2024-11-30 03:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.4 |
| be290045-849e-3bec-91a6-369c4c7df5e9 | -1.2015 | -53.8782 | 2024-11-30 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 244e879e-30b9-3000-898c-a5e06aa125f5 | -4.8715 | -41.2674 | 2024-11-30 03:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 139.2 |
| ec3090ad-a218-3564-8c7f-db52963d5442 | -3.4792 | -53.7941 | 2024-11-30 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 73ef1a00-80a3-3708-a3f6-53ec8261502b | -4.8901 | -41.2902 | 2024-11-30 03:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 114.9 |
| 43384105-f75e-312b-98ce-474805c3b993 | -2.0347 | -50.7765 | 2024-11-30 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 87230bc0-8856-370a-a3d7-545ea10ab7ac | -6.9 | -43.56 | 2024-11-30 03:00:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c3f35b66-aadc-336d-843d-2b4658bb9fcd | -6.9 | -43.51 | 2024-11-30 03:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bc845a7f-82d8-355e-850c-0dfa907d11e5 | -4.88 | -41.28 | 2024-11-30 03:00:00 | MSG-03 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 652ebf75-b06f-3d8d-a3b0-a670ae841300 | -6.93 | -43.56 | 2024-11-30 03:00:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e29c31c3-e9b8-37a4-88fb-638f97d8074e | -6.92 | -43.52 | 2024-11-30 03:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 868a34be-dad2-399b-8b44-4a8c696d1925 | -7.49834 | -34.88561 | 2024-11-30 03:00:00 | NOAA-21 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 455636c2-1a06-31ac-96a3-95439a5f2795 | -7.50007 | -34.88506 | 2024-11-30 03:00:00 | NOAA-21 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 8e9a9db5-e748-3a86-adf1-442fe6de45c8 | -6.66896 | -34.97413 | 2024-11-30 03:00:00 | NOAA-21 | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 691543ee-0e54-3ae3-b95a-0c3ed31f1d0a | -9.6477 | -36.12593 | 2024-11-30 03:00:00 | NOAA-21 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 47918634-189e-31f2-899d-951f5f5afbd0 | -7.49905 | -34.88165 | 2024-11-30 03:00:00 | NOAA-21 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| e61f6a09-3692-3a69-baaa-705f1271884f | -6.66312 | -34.97321 | 2024-11-30 03:00:00 | NOAA-21 | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 44c66fbd-b6f3-303b-9514-0aadac970e45 | -19.17266 | -40.14583 | 2024-11-30 03:04:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 6acfb7d8-9712-3332-a9da-5761abdd7574 | -19.16931 | -40.13797 | 2024-11-30 03:04:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 5a3fe05c-a3b4-309c-b86f-6106b020260a | -19.17393 | -40.14026 | 2024-11-30 03:04:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 82afc316-4a70-347d-8b5f-026170b40335 | -19.16798 | -40.14355 | 2024-11-30 03:04:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 8ecc4773-91d7-3ce9-9b1c-311894554c41 | -4.8715 | -41.2674 | 2024-11-30 03:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 108.0 |
| 2469200d-9c9b-39a1-a5e7-c64922106c51 | -3.6757 | -47.1395 | 2024-11-30 03:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 8c66d016-27d0-3c52-9c24-3ca5196cf7cc | -3.2591 | -53.6186 | 2024-11-30 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| a77691cb-8113-31f4-81af-df41d7cb6748 | -2.1535 | -54.8858 | 2024-11-30 03:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 66218926-e5b5-3041-8aa3-a6378c4ccc06 | -1.2015 | -53.8581 | 2024-11-30 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 267d02a5-d0ea-35bc-8a27-a4fd3a3395b3 | -2.1351 | -54.8861 | 2024-11-30 03:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 118.9 |
| f5d95417-6245-3569-8528-00d30279d2c4 | -1.6419 | -53.8731 | 2024-11-30 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| e417cfa6-b497-3f3b-94e6-4abb3407ef24 | -3.2406 | -53.6393 | 2024-11-30 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |


[Clique aqui para ver as próximas entradas](README13.md)
