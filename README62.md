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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3207bcab-5540-334e-a73c-d6f9f8e54749 | -2.38444 | -57.16169 | 2024-10-11 04:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 495bafbf-5a7d-3c50-abdf-4029f13212b7 | -2.38354 | -57.16698 | 2024-10-11 04:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06a98e76-b80e-3166-a3bc-17b292d49ad7 | -5.8399 | -57.71932 | 2024-10-11 04:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dafd9ee9-e95c-3c34-ba59-fb543018a7fc | -3.63509 | -58.62989 | 2024-10-11 04:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7836098e-f2c1-31cd-8ddd-98e6bb171c8c | -3.63616 | -58.63245 | 2024-10-11 04:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0ec121d6-508b-3a70-8c80-f2a597f120d8 | -3.47024 | -59.51077 | 2024-10-11 04:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3fd4d448-88e1-3a66-9dd0-4a55b3c90962 | -12.11936 | -50.53165 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 14598e54-2245-3db1-9c99-0e8da5fda4a0 | -12.11867 | -50.53579 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 644bdec6-4486-3136-8a8d-91d57e6d2baf | -12.11788 | -50.51863 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7bc40a7-0822-336e-b7ee-0c0fd974c200 | -12.11718 | -50.52276 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fb5b1ad-90b1-3b8d-b103-367f29e938d2 | -10.86469 | -49.76605 | 2024-10-11 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f7995f9-065d-3751-9383-a6a9d1d02e17 | -7.68025 | -50.25182 | 2024-10-11 04:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d23668a-b9b3-3a13-a3e7-e9b29ed86231 | -7.67653 | -50.25122 | 2024-10-11 04:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1a55d79-a6f2-382b-87eb-77984c7f83c7 | -7.67282 | -50.25061 | 2024-10-11 04:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5409d9a5-2cb8-345e-a47e-ff829de5bf66 | -7.17511 | -50.76602 | 2024-10-11 04:25:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 729e8f8c-bdc7-31da-8a69-dfdaa8ab21e4 | -7.09583 | -51.26351 | 2024-10-11 04:25:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e3bd101-21c7-36be-bb1f-f66763c34d08 | -7.179 | -50.76647 | 2024-10-11 04:25:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6865ec98-b9a8-39d8-8135-9bbd80c93b85 | -9.19644 | -51.52387 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e85e8f0d-6ba6-33b7-bbb7-3e861866e862 | -9.19556 | -51.52896 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2c10c449-1c7d-3053-8205-73d6c183576c | -9.18152 | -51.49302 | 2024-10-11 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3a82861-b6c7-3b5f-bed8-eaa04a23585f | -9.17729 | -51.49482 | 2024-10-11 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0b884412-6454-3197-8924-6bdb9d5cff32 | -9.17338 | -51.49415 | 2024-10-11 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2ddb151a-e69c-3f75-ae90-ae5f31e20304 | -9.10277 | -51.29661 | 2024-10-11 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37bab24e-b5d2-3a27-ba88-8fdaa00c1cac | -9.09733 | -51.29866 | 2024-10-11 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc16c550-04bf-310e-acd4-c04e2eed605d | -8.89615 | -50.78104 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dbf35807-aade-3de8-8ed1-8b74608f7a8a | -8.77355 | -50.72285 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db0bec28-85cb-3e79-bbd7-7d9db4b5c17a | -8.73441 | -50.77247 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 73b7317c-fe52-330d-ad3a-24a7c7254e7d | -8.72987 | -50.77649 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a30535d-1117-3ab8-9a70-f26cd2bceb76 | -8.57105 | -50.53883 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40739785-a64d-357f-8925-0d3af7223f3d | -8.5688 | -50.52919 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd40d24d-e272-3f7a-a50c-6f4fd3481bf9 | -8.49327 | -50.79867 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2760274d-cdfa-38b3-82cf-4414b7c5d9a6 | -8.48946 | -50.79812 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b30427a-52cd-38f1-a6f1-ee82b46af89a | -8.48728 | -50.24823 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d59dc5b7-9951-3132-9456-bcb687365f64 | -8.28429 | -50.27596 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6c79028-f695-30e8-8efd-3eef8a2d7ced | -8.27285 | -50.39232 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2887847a-6b76-3549-930e-4e2c1ba3902f | -8.10445 | -51.10252 | 2024-10-11 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 024244c0-5012-3dc3-985b-7f3fda780d2a | -9.38197 | -50.75326 | 2024-10-11 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c6e57475-f614-3983-a524-42c5a0e311c8 | -9.3536 | -50.76211 | 2024-10-11 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca2e02bc-94b5-3738-98b8-3acad017179e | -9.18317 | -51.31541 | 2024-10-11 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a48ebe3-baba-3303-8c2e-43701ed28271 | -9.1812 | -51.49546 | 2024-10-11 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b930c5e8-38f9-3e6e-9f23-11926b918d68 | -9.18067 | -51.49815 | 2024-10-11 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 978b4688-0ecd-3311-ad24-0304edbba107 | -9.17762 | -51.49229 | 2024-10-11 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c163a98-cb5a-39cb-b05e-af2b6d2500d3 | -9.17371 | -51.49158 | 2024-10-11 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c914cfbc-f720-305c-9550-0edd8ff3e1d0 | -9.14059 | -51.30825 | 2024-10-11 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75f64d18-f1dd-38b1-a020-0f4cff7ee808 | -9.10587 | -51.29512 | 2024-10-11 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83be2cfa-f06f-3dbb-88fd-d8a4ebc45187 | -9.10201 | -51.29443 | 2024-10-11 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ad7289b-4a20-32dd-b259-cd5023844578 | -9.10119 | -51.29934 | 2024-10-11 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b52aca53-89ba-38ef-9a2c-3b31cb214c36 | -9.0989 | -51.29593 | 2024-10-11 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f61c8c4a-a477-3db3-8d10-7b6eb27e6472 | -9.09814 | -51.29375 | 2024-10-11 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc5fdb1b-f3fe-3e1c-8bd6-1504faac1066 | -9.0333 | -51.46574 | 2024-10-11 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf27c72e-68d4-3ce7-9bbc-eb019aa6523f | -8.75114 | -50.81115 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fa66260-e190-3884-aa2d-ae81bfee9469 | -8.75091 | -50.81359 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ffd2554-4c9f-3b5f-b715-b6d84e6cb6ec | -8.61026 | -50.27666 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64ae12fa-893f-3d0f-b57f-1aee0b432e65 | -8.57975 | -50.41622 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bb10e44-20f8-3b65-9d5d-c6f13bd92551 | -8.56807 | -50.53368 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28d4692c-a3a3-3917-8114-f93f05fcb227 | -8.56508 | -50.52854 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99afe472-7d56-3d3f-9604-d12981bc5889 | -8.36969 | -51.6575 | 2024-10-11 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac2d9e9c-0532-396d-a276-cb16b652bddd | -8.36571 | -51.6567 | 2024-10-11 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cf98236-48bb-3191-849c-bd08e1e68ac3 | -8.1036 | -51.10758 | 2024-10-11 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2376dfe9-e8a8-39e1-8171-49db09731019 | -9.50144 | -50.99078 | 2024-10-11 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15b0613a-19ce-3fcf-ab94-5d1a79b01726 | -9.49469 | -50.98481 | 2024-10-11 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9a518a4c-881e-3cf6-9497-4551668328bd | -9.62646 | -51.76454 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80223b55-f3b1-3693-82f9-f8c064b1570f | -9.62558 | -51.76965 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eadfb7ab-1dd2-3418-b7ee-b30a22efb132 | -9.62251 | -51.76384 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a275efa-172d-3789-baa5-134e2b86700e | -9.62163 | -51.76896 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ce0c3b30-ec6f-3374-b345-7f4a1721592a | -9.50224 | -50.98613 | 2024-10-11 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a8c3d42-9e81-3a49-9c6c-4cae86080c66 | -9.49012 | -50.98883 | 2024-10-11 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e431dd9-67f6-3b9d-a05d-54d0b47c9e81 | -9.48632 | -50.98827 | 2024-10-11 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa537b75-0948-3fa1-9a3e-8bf61088a006 | -10.79962 | -51.14663 | 2024-10-11 04:25:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b88fc34c-e907-38e3-8c20-bbbc78b04016 | -10.66742 | -51.53647 | 2024-10-11 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d87d15b-84c0-39ba-9c1a-533a216357a4 | -11.48535 | -51.86462 | 2024-10-11 04:25:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d5afca7-199b-3615-bd08-5f6fde1d3666 | -11.48148 | -51.86398 | 2024-10-11 04:25:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69aebf43-dbe9-376a-a6b7-be0c17d6d907 | -11.48065 | -51.86886 | 2024-10-11 04:25:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ef6ba95-a739-3eee-bb97-8740c2b2fa57 | -11.47844 | -51.85849 | 2024-10-11 04:25:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 48541a0b-291a-37e9-a78c-3e13937bbf53 | -11.47678 | -51.8682 | 2024-10-11 04:25:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20021b5d-ef1e-34a0-bde3-1c5785c3aeb1 | -11.47456 | -51.85789 | 2024-10-11 04:25:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b199b555-7c10-36ff-b984-3fd7371eece4 | -11.28158 | -51.30265 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d95b9a0f-d170-38f8-a4c1-1e88efe4845f | -11.24703 | -51.03068 | 2024-10-11 04:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c1a94ae7-9a77-3556-a0fc-6045fe9b406f | -11.21558 | -51.04592 | 2024-10-11 04:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4b24f89-de3a-3f09-a573-7827c2befb28 | -7.91415 | -52.35298 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51aff26d-2d88-375b-b1a7-31bcd06ec4fc | -7.90165 | -52.37548 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b471a9ad-4958-31ec-858a-3693e70de2c8 | -7.90092 | -52.37974 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae00486d-40a2-3d23-b953-3161951c8921 | -7.91898 | -52.35011 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f378aca-ab52-31c4-9c19-cc36b7c534e4 | -7.91481 | -52.34911 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8029be08-7405-3d08-800b-5d6241391abc | -9.03837 | -52.95153 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99679e4e-0f8b-3010-a99a-c488eb54c948 | -8.86256 | -53.02056 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7c11d4db-15bc-3d78-9b9d-4fccaf20841f | -8.86181 | -53.02487 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d9a485c9-4164-357a-8b09-c085270df10f | -8.86099 | -53.05538 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea2daacb-4df5-367e-9f81-268c29772ac9 | -8.86023 | -53.05975 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 637c7e0a-403b-34bf-8c3c-80315072d131 | -8.85903 | -52.98955 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47bd0e23-f660-3b85-9fed-49752cfce3a8 | -8.85828 | -53.01947 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6b3a9824-d779-32c8-b3bf-c97050f32763 | -8.85521 | -53.03708 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6c3a9cb5-3a47-3c30-8724-40140399b3ec | -8.85471 | -53.01429 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8c16098f-a6a9-3438-8086-f074d3d9ba53 | -8.8547 | -52.98878 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d236300-e34f-3194-924c-ac748761776f | -8.85445 | -53.04145 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f35fcf92-9010-30b6-8316-d49c6aacbe56 | -8.85105 | -53.00964 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 64354de2-dd93-3482-932e-75af5996feb5 | -9.33917 | -52.55352 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aadb7c4e-6d76-318e-8cb2-eadd5ceef90b | -9.04227 | -52.10154 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c796c3a-c97e-35b3-b2ae-df1fd4fe18ee | -9.03915 | -52.94711 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfa1b98d-b45c-3969-bb63-f421f7a53474 | -9.03885 | -52.09702 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README63.md)
