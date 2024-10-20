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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9d31cf0-b042-3ab6-b0c2-244fe5ac0497 | -5.86001 | -51.08515 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80e8b71b-2bff-374f-ae32-b93f5d99d788 | -5.85643 | -51.08461 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 54a11ac5-a082-3366-b809-733b9027a888 | -5.8541 | -51.0759 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| f3ef48fb-a65e-3c8f-a86e-99b09d74cc23 | -5.54763 | -50.97478 | 2024-10-20 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b27a920e-fc61-3761-aded-1b6623763599 | -5.5431 | -50.16336 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d389303-896a-3e75-92c3-84cb0a6e5ccb | -5.50975 | -50.58479 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f90767d0-0015-30d3-ba48-9c13447482bc | -5.50909 | -50.58906 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c34b519-a2e3-3b2a-918a-6c9cc35ca378 | -5.50609 | -50.58423 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3a926f9-0e3d-343e-9d55-8d3bb3e8835b | -5.50544 | -50.5885 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e90672b8-dd4a-319b-8b12-9fc5b858178b | -5.50479 | -50.59277 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7a4e02f-1507-3c10-b86c-0280640ee137 | -5.50244 | -50.58366 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 553bf02b-0392-3b77-967c-a740775dfccb | -5.50179 | -50.58794 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9482d8a2-6693-35e7-b723-cba01a4f3f5d | -5.50114 | -50.59222 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b8caf11-ec4c-33e2-90c8-465021cb3917 | -5.49879 | -50.58309 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a06ac7b1-1338-368e-9035-f8c18f5a58f2 | -5.49814 | -50.58737 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c8b9395-4f18-3a46-beb5-9bef04164bb1 | -5.49749 | -50.59165 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7efb6e42-3198-3c0d-8551-04d029a7c08a | -5.49384 | -50.59109 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cc844f7-da87-3ce7-9663-772ca48d05b5 | -5.49083 | -50.58626 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34031f50-8221-3048-bb36-75a645fececc | -5.49018 | -50.59055 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7f26de6-8afe-3461-a483-beeef4469700 | -5.47771 | -50.5492 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8190e8b4-e8ef-31ff-9dad-2a2c4543b68d | -5.47533 | -50.54008 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8629908-c610-3078-a119-443896a42bd7 | -5.47405 | -50.54863 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c34ba10-7ab2-3dad-96b3-f3bb017f1200 | -5.47231 | -50.53524 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4cd9cd8-12a0-3f05-b5f0-6a18420ebf89 | -5.36834 | -50.92033 | 2024-10-20 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5677fee-71de-3ae3-9d84-17bd29f2f879 | -5.34398 | -50.98352 | 2024-10-20 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2ca0f844-5e38-3101-b634-588d31dfe138 | -5.34336 | -50.98758 | 2024-10-20 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4190a1ff-9be5-3646-8ec7-b87c5936ae01 | -5.33979 | -50.98703 | 2024-10-20 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7114fbdb-ecf9-3c05-958f-99a1b072b111 | -5.29112 | -50.69342 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1611fd28-f934-3b71-b823-81d44983a896 | -5.21056 | -50.00772 | 2024-10-20 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afd44a33-ab2f-3a92-9efb-9e8d105135db | -5.16451 | -50.71444 | 2024-10-20 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91dd4e7f-176a-3b29-a4d6-d65c5d82c54d | -5.16388 | -50.71852 | 2024-10-20 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5858755c-2322-3e3c-a5c4-a52df6484b66 | -5.16091 | -50.71375 | 2024-10-20 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f18a1c18-bb49-3c6b-b911-e54bc88abab8 | -5.16028 | -50.71788 | 2024-10-20 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| deed990d-4717-3294-9077-93133d6a92d1 | -2.23159 | -50.45054 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfbda710-cb82-3bfc-98e9-6d02c4d1bd89 | -2.22805 | -50.44999 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d2e272c-47ec-316a-bbee-e09b3b140217 | -2.22743 | -50.45402 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6cb74a5-7d1e-3766-9116-668a75881225 | -2.22682 | -50.45801 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b81658a3-4a34-3c82-985d-3e21b83615f5 | -2.22389 | -50.45347 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99e9fc90-4a18-39b4-85e8-b2b6ba89252e | -2.22266 | -50.46146 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 68e907cb-d37d-34f0-9707-a6fbc43a8f0e | -2.22205 | -50.46545 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 16f74507-f7f5-301e-a1ce-1eadfaab90c5 | -2.21851 | -50.4649 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24a0a834-0c93-31ff-b524-c71fe8f1be84 | -2.21265 | -50.45581 | 2024-10-20 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e0a4644b-0d8d-3cc8-8643-2a1eb9922043 | -2.20971 | -50.45129 | 2024-10-20 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 15d477ac-1155-3287-af29-3b5b937d1131 | -2.2091 | -50.45528 | 2024-10-20 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ca59b6f9-72e1-37bd-b64b-4c854ba79731 | -2.20849 | -50.45927 | 2024-10-20 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ede28cac-8f0b-3709-add6-227bc11be2a0 | -2.20788 | -50.46326 | 2024-10-20 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 63800e34-ba94-3f97-bfe5-d1fbef2c9202 | -2.20727 | -50.46725 | 2024-10-20 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3a887e1c-7a9b-3b3a-b3eb-e13b0ebfa389 | -2.20561 | -50.45539 | 2024-10-20 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 687ba534-37df-3b03-b1a2-c70ab68e4fa6 | -2.20555 | -50.45475 | 2024-10-20 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fa37d8b-bcb6-3f2d-9cd8-eb169422f6dc | -2.20498 | -50.45938 | 2024-10-20 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8cde8517-e60a-36a4-a52d-0c35435bf9b5 | -2.20495 | -50.45874 | 2024-10-20 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c2669394-9aca-3aff-ad90-b896908ce184 | -2.20435 | -50.46337 | 2024-10-20 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 69cd25f3-01fa-356b-bb59-8f789206940b | -2.20434 | -50.46273 | 2024-10-20 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ac28c08e-cf1a-3635-9fb0-7b6db2384fe0 | -2.20373 | -50.46672 | 2024-10-20 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4582e086-009c-3254-98db-246e0e82eac7 | -2.19523 | -50.52236 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 548949f6-864f-3e47-ab8c-3da2c8afc5e1 | -2.19494 | -50.52291 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55db40d0-6260-33be-8ab0-c5c15c584692 | -2.16899 | -50.52703 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdca7ebd-ab3a-3fc9-b918-82108a4ee13a | -2.16546 | -50.52649 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb03a05b-0270-33f8-93f5-2e03df3e0956 | -2.14194 | -50.69955 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6fc0c37-b6a8-38da-9c96-74bf39c096d6 | -2.12876 | -50.8517 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8c604fa-a2bc-3114-84e0-9ac124b3fab9 | -2.12816 | -50.85554 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44030264-0df1-36b5-85ba-6c70c1baa20b | -2.12207 | -50.80348 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1dd4472d-73a5-3bb2-bf88-68df789046ce | -2.11859 | -50.80295 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7c19d09-1277-30ac-9f2a-3e2507ded0bb | -1.74701 | -51.16181 | 2024-10-20 04:55:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff85ec9b-9039-3b4c-87a0-23f68d36b6fa | -3.54939 | -51.17356 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d774e29c-236a-3a14-922b-788e7315fc0a | -3.39391 | -50.79666 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a85d9c4-87b1-3e57-b4c2-0fde5fcc5bb5 | -3.3933 | -50.80064 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7e4b7c9b-997c-3f2a-9c53-eca4c86897ff | -3.39269 | -50.80462 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9ad8392d-aa89-355e-adcb-9ff5c1775f09 | -3.38916 | -50.80408 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a96dd616-5c5c-30d5-8d1a-fc08bdff7287 | -3.30284 | -51.11015 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 024951cb-dc9b-37b5-8bdf-345b24f88ba5 | -3.28462 | -50.94175 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 80a847fa-ff89-3af8-93f5-dbb40c45895f | -3.27823 | -51.05186 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9eecee9d-e9d7-3be1-ab7a-c9636e1ce354 | -3.27763 | -51.05571 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9719f5f0-114b-3a3e-9373-c5ce47a36c99 | -3.26298 | -51.08111 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9cb51500-62d4-309c-bb97-28ac7e451b99 | -3.26009 | -51.07673 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e1d2e23-8e56-3ecb-bfa9-05344f794278 | -3.2417 | -50.84704 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bea172a-ae57-3b4a-8383-3e0dcaca6b4d | -3.2411 | -50.85098 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| badab41b-a318-3a12-b013-b906bebf4124 | -3.23818 | -50.84651 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fadb7edc-e008-3663-958d-87ee2dd41e9a | -3.23758 | -50.85044 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e40fc604-5ab8-3e2c-8062-e5e50de64a8a | -3.22995 | -50.8533 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc7fe1b5-c4a1-3b8c-a454-478ab8e40d16 | -3.22919 | -50.85372 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 642bc038-5316-35a6-aa34-31b421b66349 | -3.2167 | -51.01084 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b77c0c3f-74ff-305d-9a99-84ebb0b0d30e | -3.20794 | -51.0214 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 029e6006-b226-3866-b993-e7a4a3b3425d | -3.20445 | -51.02089 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e799393e-1f0b-30ab-a9e7-bbed68894f34 | -3.15396 | -51.03722 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39ef209b-8ee6-3a93-84bf-147e17112d1b | -3.1483 | -51.14241 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c5ecd06-c7e4-30de-a5a6-1121a7a2df33 | -3.1477 | -51.14625 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f5b0827-a32e-3e08-86dc-5708e24689d4 | -3.06493 | -51.0951 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b728240e-df68-3fd6-851d-6f47ad821e9a | -3.05412 | -51.05034 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a535cb7b-9f0f-3dcc-aeb5-0f80ac84569b | -3.05352 | -51.05418 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fa26f31-b3f1-3f7d-a51b-2ca9e900596d | -3.05096 | -50.97881 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a28999a7-4944-3743-b4c3-f624bd445601 | -3.05064 | -51.04981 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfc23a20-ce2d-3047-ae4f-f89077e09993 | -3.04747 | -50.97826 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed6e6a44-abbe-36a3-aef0-1b9b963c88be | -3.04377 | -51.02513 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 7258f21e-eeb4-39b4-b86e-4dd59a0746a1 | -3.04089 | -51.02073 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| f0d2f275-d117-312b-8c6e-ee26f9b3b6b2 | -3.04029 | -51.02459 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 148c1969-9105-3dd2-b77c-ee1771bbe2fe | -3.03741 | -51.02018 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8dece7bc-120f-3865-8b93-8fda0814b46d | -3.03681 | -51.02404 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef16fee7-e74f-3e77-aa08-54898ba19554 | -2.98569 | -51.03197 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2a1bf16-a16b-358f-a7e5-ca9be1c30b55 | -2.98511 | -51.03583 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README48.md)
