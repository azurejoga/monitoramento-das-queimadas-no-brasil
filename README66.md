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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c12462b-5aaf-3ada-9f97-0e21dde03aa0 | -17.16013 | -56.13318 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b136c44b-a7f4-363f-8a73-0fcc95391164 | -17.15383 | -56.14414 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f0e90e68-a108-3a0f-9fea-7f11b30f495d | -17.14751 | -56.15516 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1bca1fc9-16cf-3aaf-b729-b71d2527f7ca | -17.14409 | -56.15038 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 35ee4f56-d699-3c23-8a5e-0a4d19066fe7 | -17.04819 | -56.05473 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6b786e13-366b-38a8-a844-1534a9b4b2ae | -17.04406 | -56.0539 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a504b6a0-978d-3c5e-8d2f-106482f2d65d | -17.04244 | -56.08604 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 10bee705-dc61-339d-a380-22ec454fa4f4 | -17.03415 | -56.67259 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| bfe040c9-0e81-37ef-a5f2-f5728dd45694 | -17.02716 | -56.66234 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| b431611b-3dcd-37c8-b82e-e3d24941a4ba | -17.01777 | -56.66486 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9c1a2396-45ba-38ab-8dd5-21d209d9632b | -17.01697 | -56.66911 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8008ac9e-7ad3-3e5c-b2b7-3e14ae793fec | -17.01537 | -56.6776 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d563584e-57cd-3044-9348-f4c4c9c2df33 | -17.01187 | -56.67249 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 3d0911d2-b55e-30d9-b426-68f8f253f236 | -17.01027 | -56.681 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 93f60d42-e5ea-36aa-8741-d5ed31e1679b | -17.00757 | -56.67163 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 4bab5fb4-d4a2-3d2f-ba5f-e5c1d62f38f3 | -17.00677 | -56.67588 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 75d73c89-482d-3a8c-b8e1-4e9d4fc33056 | -17.00597 | -56.68013 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| d001b908-0c14-3b4b-a0dc-251127ab3cba | -17.00355 | -56.69293 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 4bf47dc4-a59d-3d90-943e-567043da797b | -17.00167 | -56.67928 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 22f811e8-e525-3a1b-b1ab-c757d88de11a | -16.99925 | -56.69205 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| e32cdbc2-f29a-3470-8a31-b453ee46e09a | -16.99656 | -56.68267 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| f8a76289-e78f-369d-b04f-cfefd73ca144 | -16.99392 | -56.60282 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 7302b5a3-fd1f-37c4-966a-1e6c814d8830 | -16.99312 | -56.60704 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f34fd742-fe61-320a-bbe4-48f5d9cb6863 | -16.99063 | -56.69035 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 97cbf5ef-786d-3f1b-a994-a2873915f2c0 | -16.98294 | -56.61377 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 673caf77-3056-3324-8d44-6c6bbe7a65b1 | -16.97704 | -56.62135 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4b4f9b0d-1b59-39c3-b43c-f15b376ad4ad | -16.96362 | -56.13977 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3ffa0daa-72bb-3f94-9053-e30b004a2df2 | -16.93505 | -56.61869 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b0810e26-caac-302f-86e0-0a98c62e70dc | -16.93426 | -56.62294 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ba3ef4ab-d3f0-3c21-bbaa-c654e5710a9d | -16.92997 | -56.62207 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| b25ab902-dc4d-31da-88bd-f4e12d246265 | -16.68639 | -55.96336 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a43776d5-0b72-38e9-a144-6431515934b4 | -16.66916 | -55.89558 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ad1498e9-6dac-315a-85b7-e118d2a5789f | -16.63235 | -55.89607 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 061263cc-7167-32d9-bb55-3a3f0cf80cb1 | -16.63164 | -55.89994 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b2efb37c-e990-3978-a4b9-84a13a6ed1bc | -16.63093 | -55.90381 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d2ca4db8-32f8-3671-8e48-ee7bbc32e693 | -17.04747 | -56.05863 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4164e462-9eae-3e93-97b4-56cba7a582a7 | -16.96437 | -56.1358 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 85b200a9-5e66-3d61-89cb-3d05cf4787c4 | -16.89702 | -55.86805 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 91eb533d-6c92-3d93-b592-fce0fae37343 | -16.8963 | -55.87186 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5433f1eb-4b03-3d9c-a9db-11289543e2e9 | -16.87159 | -55.80426 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| bf56f41c-79b5-393d-9968-22345df00f92 | -16.8325 | -55.85574 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ba1d0dcf-831e-3cfa-bb5b-e124fe4669f6 | -16.83179 | -55.85957 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 1542bef0-49e5-36e2-9954-533a849f5168 | -16.82503 | -55.8503 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 070e0879-f6fa-36bb-be1c-e072b4d83082 | -16.82432 | -55.85413 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 6c2b8a76-d61b-3de1-925a-20e88092df66 | -16.69053 | -55.96416 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| bac32ea8-c281-388d-a3e6-4f42515f5072 | -16.65294 | -55.9001 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 276d6b21-fd98-321d-97f3-72cf7bd9ae48 | -16.63576 | -55.90075 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 83c159a7-b94a-357c-b74c-1425dd7fc285 | -16.63376 | -55.88834 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4a151675-26f7-38e3-ae14-9e210b12d15a | -16.63305 | -55.8922 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 94baa4e5-4258-32b8-a725-1972fdde8140 | -16.62823 | -55.89526 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 71bbedb0-7a82-3cc0-9dbd-c808e0d5773b | -16.62752 | -55.89914 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| def2a52e-71d9-38d6-a1b8-38c31d3155fd | -16.62681 | -55.903 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 31dc56c4-0a08-32a1-86d9-225d38e06b9f | -16.62411 | -55.89446 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a4e21353-2bf4-3fa6-aa80-4be4cda65cb0 | -17.06499 | -56.67445 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ad82269e-1d6b-3827-9513-2e8f6d307eee | -17.03335 | -56.67686 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ceb34af2-78da-3438-aea2-b14d1724db88 | -17.01617 | -56.67336 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b3ebde3b-15b9-35c1-80ae-0742e815e1af | -17.01348 | -56.66399 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ed1e7c74-8f04-304f-8216-4482f104e30a | -17.01107 | -56.67674 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0a17187c-a209-3924-9690-4b7a0b308fea | -17.00516 | -56.68439 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| c5c431c3-6581-3a83-9373-deff5f2d2c3f | -17.00436 | -56.68866 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7d2c9836-0e2a-3d1d-8cda-1a5107073b1b | -17.00247 | -56.67502 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| d1516e81-cfc7-3e83-878d-41caa709e86d | -17.00086 | -56.68353 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 08317cdd-ca6e-39ae-b154-31536039350b | -17.00005 | -56.68779 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| ec0be92d-82fb-3cba-bd43-201a6eae4155 | -16.99575 | -56.68693 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| d02dbd84-cd67-36f2-a250-8565c64a9c2b | -16.99494 | -56.6912 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 5d44d86a-5bfe-351d-a062-c9191d8f0ad1 | -16.98803 | -56.61041 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| cdccbdfa-0d04-386d-9dc6-63a7af38ef23 | -16.98722 | -56.61463 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 715c955b-7b34-315e-8e47-8b4a08bdbc46 | -16.98642 | -56.61885 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| cb65b97c-7599-3daa-8018-e36dff42828c | -16.98213 | -56.61799 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 1f7a29c4-20a6-39e4-914c-771e3ba9bf1c | -16.97866 | -56.61291 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7537ee04-483e-30cd-ad87-62939cefb0a0 | -16.97785 | -56.61713 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a1e8ec37-51ce-33d1-83e7-cd222af97cf2 | -16.82912 | -55.85111 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| c4426994-01f6-3f9d-8786-9f5f62b3f17d | -16.82841 | -55.85494 | 2024-10-08 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 8663cf6a-aadd-3166-9135-d380666d3621 | -12.09511 | -56.8828 | 2024-10-08 04:36:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cef2f1c9-0735-3010-a8c8-62af0a0b165b | -16.5498 | -57.72068 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 53de1d2c-66f6-3dce-a961-bf9131a8b0a3 | -16.51948 | -57.71228 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d8427ecb-4892-3452-b23e-85059e27afc3 | -16.49827 | -57.69727 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a75e9d52-36e4-3927-9d77-a2e030e2d046 | -16.49328 | -57.72312 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 58ea968f-0c77-3145-a5a7-b2614e002630 | -16.49129 | -57.73343 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1fcd7279-82a3-3760-8b47-573693c01979 | -16.49031 | -57.7385 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 941e94a3-330d-3859-8c37-bfcf6f4cfbc2 | -16.38432 | -57.69817 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 34669794-62c9-3b1a-8f93-57ad81eb3d6b | -16.65256 | -57.13349 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| c14c29d3-c614-37ef-8eaf-06ec915100d3 | -16.6517 | -57.13812 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| a65f3eb2-f6dc-3014-bcaa-03469e4657b9 | -16.64664 | -57.13018 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| bc87264c-5c8b-3370-9da1-910f78a3f1f1 | -16.64452 | -57.12703 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 808423c3-f9c8-36f2-a261-8ccbfc28cfce | -16.63203 | -57.11969 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 471b40f3-9e08-3377-b2f8-356fbb7e7bfb | -16.62758 | -57.11878 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| db3a7440-1a44-327d-8489-143f5f3f7a6c | -16.60895 | -57.1438 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| f3518d58-98d7-3f33-a08f-730ca373bb91 | -16.5938 | -57.15033 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e6669b6a-2bdb-3bff-a7b3-daa154af8538 | -16.58934 | -57.14941 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b9bb983d-1df0-3bed-a2c1-91a2467179f6 | -16.57062 | -57.15027 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 8c97b84a-f658-34ce-a393-da680d42fdfa | -16.48056 | -57.24589 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 144f9349-dff1-31d5-90af-d64c21b68875 | -16.44881 | -57.33841 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 397f2009-3269-3976-a25d-3c9f4e4512c3 | -16.44789 | -57.34322 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 249b04fb-b4f5-34b8-a626-9eeaf866d8ff | -16.44696 | -57.34803 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| bb0ecaab-b7d8-3625-866f-9438ee8dc68f | -16.44335 | -57.34229 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a9fa3c6d-bbfb-3823-8be6-c91a4e3cd81d | -16.44243 | -57.34711 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 304e9211-2ad0-3e10-80e9-4770710b5957 | -16.43642 | -57.2564 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| eabd6440-a8df-33fd-8999-4186b194844d | -16.43069 | -57.33468 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 497065d2-7a7a-3af4-9572-7a519efe6c9e | -16.42256 | -57.32803 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |


[Clique aqui para ver as próximas entradas](README67.md)
