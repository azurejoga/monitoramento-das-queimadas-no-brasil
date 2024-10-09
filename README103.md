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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4936223f-a72a-385a-af8e-619788eabc00 | -17.32733 | -54.99666 | 2024-10-09 04:19:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6a1501db-220f-3a2d-a221-7465dcc12ee6 | -17.32729 | -54.99727 | 2024-10-09 04:19:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c81e03a8-6179-30ce-9274-c6bf6a468933 | -17.32666 | -55.00001 | 2024-10-09 04:19:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 3054e014-14d0-3856-a5cb-aa2ec6c9c589 | -17.32659 | -55.0006 | 2024-10-09 04:19:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e5a10861-fe29-3702-9aa3-cca95ba73d85 | -17.32589 | -55.00394 | 2024-10-09 04:19:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a9d084d3-ebe5-374c-8b59-c515dcc9f1ba | -17.3253 | -55.00671 | 2024-10-09 04:19:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| fc072ea7-606a-3499-9d85-9907a99a9315 | -17.32519 | -55.00728 | 2024-10-09 04:19:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d3e6a99e-1514-307f-8333-b4e5cc4ca9e9 | -17.32463 | -55.01006 | 2024-10-09 04:19:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2be9f104-e0b3-3220-8014-7c2e25961ad0 | -17.32449 | -55.01062 | 2024-10-09 04:19:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 294bd55a-cdce-3834-979b-ee1c20023d63 | -17.32395 | -55.01341 | 2024-10-09 04:19:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 7234b20a-134a-3acb-ad22-6bedc76c1cf8 | -17.32068 | -55.00279 | 2024-10-09 04:19:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| b44218d3-aaf1-32e3-b7a1-76be7cd77943 | -17.3201 | -55.00555 | 2024-10-09 04:19:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| eced8e9a-ac07-3ad7-89dd-04ccb016c43e | -17.31998 | -55.00613 | 2024-10-09 04:19:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| e880ed10-383b-3b37-8152-623802684f79 | -17.31942 | -55.0089 | 2024-10-09 04:19:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 150b7d76-838c-3cd6-aea0-643bb5b37587 | -17.31928 | -55.00947 | 2024-10-09 04:19:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| f4cb8f94-dcbc-3fa2-a34b-a6e5ed59cf0e | -16.43111 | -55.93276 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| fe2ceecc-120f-346b-b978-43f987146834 | -16.42779 | -55.94863 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8dbb112a-0042-34c9-9c2f-16fddcbca53d | -16.42695 | -55.95261 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e068b067-0713-32c0-8928-31745f941a92 | -16.42612 | -55.9566 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a4b9e2e6-1053-32a9-8d9f-e62e0bb69ea5 | -16.42551 | -55.93149 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| dddd9a22-9a2c-3db1-8cfb-ecf8e4f64d6e | -16.42468 | -55.93544 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 894277ea-762d-3f4b-a6fe-42b5bada7815 | -16.42385 | -55.9394 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 8567d336-78a1-3f28-bec0-04c38065c318 | -16.42302 | -55.94337 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| fcad5955-170c-33a8-bab9-7324cd6ec962 | -16.42134 | -55.95134 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5b4aed90-1935-3988-8037-29f8d78d7633 | -16.41991 | -55.93022 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5c4d36a3-0ccd-317c-91a9-1ab92f99aeaa | -16.41908 | -55.93417 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 0e8e4e54-2f0e-364d-9ebb-eeab78bacac8 | -16.41824 | -55.93814 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 9ab56755-e48d-34da-8efa-1e5821f13e30 | -16.4174 | -55.94212 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 23f2456f-c4a2-3c65-a54c-b6555068d73b | -16.41347 | -55.93292 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 9f02bdd5-f23f-3f2d-bc4b-ff45b78cc181 | -16.41263 | -55.9369 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| eff9958c-8597-36f5-85ba-b1d24b94782a | -16.41179 | -55.94089 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 0ad3ad94-274c-35cd-886a-80910b701fbd | -16.41095 | -55.9449 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 508da569-50f2-363b-a876-2fdcda365ea8 | -16.166 | -55.93552 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 50795b8e-2329-34c3-922e-63f876e52397 | -16.16329 | -55.93583 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ec772777-206b-35fe-95c8-ec297b128f23 | -17.16036 | -56.11236 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| cf615c97-58b8-301f-bf7c-ce58df70a2b2 | -17.15952 | -56.11631 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 8f30ac4e-6e88-3c75-91bd-dcb0778de948 | -17.15869 | -56.12025 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| d2dc2112-9dc6-326e-9f44-0125dc0c4750 | -17.15785 | -56.12422 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 62451def-9a5d-319e-9a61-cdae8b1266b8 | -17.15701 | -56.12819 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 19e2b73d-d13f-307d-be88-43b954480320 | -17.15618 | -56.13216 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 1dd57774-0baa-38e0-9c54-f1f893d7e08c | -17.15393 | -56.11507 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 8140e9b0-57fc-3983-b238-39edd8ded906 | -17.1531 | -56.11899 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 589234ef-81e5-38a4-a723-9514bec84c99 | -17.15226 | -56.12294 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| f0deceee-96b0-3ad2-9d37-b011bc129831 | -17.15142 | -56.12692 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| e05f07c5-7718-3f75-9f2b-13f60ec4d716 | -17.15057 | -56.13091 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| e734ef07-5c14-30b8-b929-d7368ba43c89 | -17.05866 | -56.02396 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 18bff475-23a1-3001-a3f8-d3437367a390 | -17.05784 | -56.02788 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 23.8 |
| 0dc69350-9bd8-3d3e-af7b-8e02981e2009 | -17.05226 | -56.02662 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| af2977e3-6480-3e54-9e0e-da3dc3ca0281 | -16.92162 | -55.80565 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0d3b7192-fb51-38e1-904c-22d38017779a | -16.92083 | -55.80947 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4f8ed861-70a2-3c6b-9cc0-37e383d650ab | -16.9169 | -55.80059 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| a63c80bf-2cf5-39cf-b012-fdcf73abce31 | -16.91611 | -55.80439 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 6a398595-db7f-3961-9cd4-2ec57dd3ea33 | -16.91532 | -55.80821 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 0da29030-b278-3c0b-a1d0-aa76783c09bc | -16.91452 | -55.81205 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 28e02fbc-43e8-3926-8de2-633a2c0c99df | -16.91372 | -55.81589 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 5790bb3c-ce00-3083-866d-2860d8b0bf1a | -16.91292 | -55.81974 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 5e74378c-9380-3442-80b0-865c88e561ff | -16.9114 | -55.79933 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 3ec3ae32-1792-31dd-8554-23510dd68cad | -16.91061 | -55.80313 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 2b1f7105-4673-38ee-af45-535424b39ac7 | -16.90981 | -55.80696 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 24263e9a-e8f1-37f8-a988-536b9417e601 | -16.909 | -55.81082 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 8a4b52cb-973c-394f-919b-4e6ba64590a1 | -16.9082 | -55.81467 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 71fb0760-a02d-394a-bd3e-af92739e5e92 | -16.90589 | -55.79808 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| eaf6e1b9-e9ff-3a99-b857-c3528da68e4a | -16.9051 | -55.80188 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| de5676bb-fcb9-303d-a100-a1fd16d7d294 | -16.90429 | -55.80573 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 7871301c-564d-3891-b5a2-8dd88f1917db | -16.90349 | -55.80959 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| f94700e5-5403-33d2-9ab0-24c5313cc963 | -16.90268 | -55.81345 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 294c6e0a-cce6-3160-bc1d-f0eea044c764 | -16.89958 | -55.80067 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 46f25bc7-0d8e-3e4f-8769-862db515cbf1 | -16.89878 | -55.8045 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| bcfe305b-d671-3c97-9ad4-13708f7abe38 | -16.89797 | -55.80836 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 05e14f16-a3b0-386c-9a0f-7ebf8d1a31f8 | -16.89717 | -55.81221 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| af2d2087-19bb-3e87-9797-0fd8f646ec4e | -16.89636 | -55.81605 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4cf79e17-807f-338d-8b11-8a1491ff2333 | -16.89618 | -55.87231 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 81ed3f72-cbe5-3e27-8915-389d55329fe6 | -16.89556 | -55.81988 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2fc16a2e-f701-37f4-8264-3d70e6aa316c | -16.89538 | -55.87618 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1d26ed0f-7ea7-30ba-b160-cf5158378336 | -16.89406 | -55.79947 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 1aef9d21-af7c-3553-b20e-092f2eea09f2 | -16.89326 | -55.80329 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5b8e32a0-05e7-3c0e-9297-58dd2b704395 | -16.89246 | -55.80713 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 763344bd-06c6-34cd-b667-f924f0344573 | -16.89165 | -55.81097 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 38615532-daf6-3dfd-bca7-4ff6319badbb | -16.89085 | -55.8148 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 27a28263-52ef-37ae-b0f7-c37ecd377924 | -16.88854 | -55.79828 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 1d4eddbc-3c81-3b9a-ae0d-527ac8f72a77 | -16.88774 | -55.8021 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7c47fc4e-b42b-342f-8eb6-a1e840635d84 | -16.88694 | -55.80592 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| cb357e42-7e8c-3569-ac82-d917bb178bb8 | -16.88613 | -55.80974 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 91507e32-81ac-3f3f-ba39-d201e68998ef | -16.88533 | -55.81357 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 06b5597f-80e8-3e9a-811c-15184c523f5c | -16.88453 | -55.8174 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 46011e04-36f6-39f0-b852-1d507ccfb0b2 | -16.88222 | -55.80087 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f99b1acf-42b4-3210-8227-a909b1b660c2 | -16.88142 | -55.80469 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a8c95927-0b51-330b-bab4-4e5843cdd131 | -16.7054 | -55.95684 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1be39205-b3b3-3854-9066-2bd938f34b4f | -16.70485 | -55.93204 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| a2762552-0b44-3c47-affc-4407e648f9ec | -16.70457 | -55.96076 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e0f1ace9-c55e-3c49-9852-a647ea7abe2b | -16.70185 | -55.92967 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a2407a79-1733-3d45-817a-affad8634576 | -16.70104 | -55.93359 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 1cc6ac83-bfe3-3349-bab9-dff5cd453e4a | -16.7001 | -55.9269 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8b8c3fa4-3694-3ebc-be47-76719d9c054a | -16.69927 | -55.93081 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 25421214-5e44-364d-bb99-f929988836af | -16.91297 | -55.79177 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 27.0 |
| 27f4638a-19fa-3f06-a9ad-d1993a9679dd | -16.91219 | -55.79555 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 27.0 |
| f79e70dc-3fb6-32e0-b588-ac2bc767db71 | -16.90905 | -55.78295 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 5a88b4b7-457b-311b-8f2c-82d0be59a1b8 | -16.90825 | -55.78674 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| e94b8881-c97e-3317-9f24-1fb149b1f38b | -16.90746 | -55.79052 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| 9f39c3e6-59eb-3561-ba5c-ea45b17dfe2d | -16.90668 | -55.7943 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |


[Clique aqui para ver as próximas entradas](README104.md)
