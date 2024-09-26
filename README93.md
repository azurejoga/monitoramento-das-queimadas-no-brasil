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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8262a2d0-372a-3d5d-8b19-5fe151fb358b | -9.41266 | -51.51718 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44c096ce-8c57-3a3f-a152-7161170329c5 | -9.41254 | -51.56863 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ce9da8d-578a-38f0-887d-8b18801b1cdf | -9.41221 | -51.46921 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce8f03a2-4ff2-3707-bcd0-70980c3ddec8 | -9.41204 | -51.52139 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fd7d948-2ad0-36cb-8673-b090f8b8de5b | -9.41201 | -51.54695 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3dc9eac-53b6-3f3a-b79e-221423121110 | -9.41159 | -51.47349 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8cd4379-2c34-3c12-a7ca-53f36681c865 | -9.40983 | -51.45995 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e602019-3273-3017-9821-417ca0edc0d1 | -9.4092 | -51.46427 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d8db22c-631b-39a8-b109-153d479bd4f8 | -9.40901 | -51.54213 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d68d9ff3-fbe2-3901-94f4-723c06db5a62 | -9.40893 | -51.56802 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe1e0d30-356d-3053-9241-c0a68d104cbe | -9.40857 | -51.46865 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6e76ab2-2089-3f8d-807a-577b6788429c | -9.40795 | -51.47295 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cabead3-9504-30f5-91ff-006123740879 | -9.40734 | -51.47713 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af61cfb2-92bb-33f4-8e58-95a54df7461f | -9.40673 | -51.48134 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce5c6025-5b37-3644-b63e-ca82236bde13 | -9.4062 | -51.45935 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 89d0ee99-4e64-3abb-bf83-c0877314f46c | -9.40611 | -51.48558 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0522508c-7d6b-3bd1-aeb4-0b73c5449c03 | -9.40539 | -51.54158 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45105417-82dc-3405-8ac0-5e5e768ae762 | -9.40194 | -51.46304 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 892102e9-9253-3d21-91be-5933d6b22416 | -9.39832 | -51.46238 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 871a16b2-7f74-3cfe-ab82-e08204827700 | -9.37996 | -51.84042 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 008cc188-7624-3854-b2d7-905a41f056de | -9.37937 | -51.84437 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9e943a3-2174-3aa2-b803-5a46c13a0f45 | -9.37638 | -51.83991 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 66cb73db-fa88-3ade-9f09-b1a46f76be41 | -9.37682 | -51.45235 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0dab261-f7b6-33cd-9f96-5db12670df89 | -9.36528 | -51.45488 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8132690f-1ce8-3c1f-9c0c-f25bda43d402 | -9.36165 | -51.45428 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b11f0787-f79f-3434-9bee-d255a337a4af | -3.66572 | -50.95211 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34c2bf64-941b-35d1-b14a-f427741c6862 | -3.48824 | -51.19019 | 2024-09-26 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4529aa43-3b99-32c0-9ba2-9f5c8219f255 | -3.47437 | -51.2114 | 2024-09-26 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17f86dcc-376b-3118-9e91-46c830dd3484 | -3.45274 | -51.2205 | 2024-09-26 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ff891ac-22ec-3a1b-a58c-152f7d11a6c7 | -3.41422 | -51.58138 | 2024-09-26 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fe76947-dde9-3684-8812-a1509fcc884f | -3.34319 | -51.56326 | 2024-09-26 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 91d00db6-a6b9-3860-9da0-bcee6c3c2561 | -3.2045 | -51.14445 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b04b9082-6f66-3ff2-9d18-2a4fa53c4113 | -3.20391 | -51.14825 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68064208-019b-359b-9d2a-9f8886712f92 | -3.20163 | -51.14013 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af968d59-214b-31ad-9569-403278027c53 | -3.20104 | -51.14393 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca69883a-0bda-341f-88a5-8fa20ddd572b | -3.20045 | -51.14773 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9705dfbf-9874-3e1d-92fd-921e91c0c745 | -3.19817 | -51.1396 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e52dc95e-27d3-343c-a546-8dc35fa7d454 | -3.19758 | -51.14341 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6ec66b9-498e-3880-b003-40ad8e4175da | -3.19699 | -51.14721 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cad29e10-7c93-376f-9b7f-18e5cf7fa2ab | -3.1964 | -51.15101 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13095ed7-b634-3722-b0e7-fc216e7ec29e | -3.19412 | -51.14288 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0efc4a7c-e09f-3802-a868-03d82e48549f | -3.19353 | -51.14668 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8339633-f0a0-3f44-b1db-023e00944cc3 | -3.19295 | -51.15049 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78941f8b-d153-3eb3-a1a5-d63db83111f7 | -3.19008 | -51.14614 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3876c55d-1f79-3d2c-8213-de3df26135f6 | -3.1034 | -51.25355 | 2024-09-26 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4013fbb-4755-35bf-8b37-710799f7d784 | -3.09996 | -51.25301 | 2024-09-26 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65939f17-abd9-3401-93e4-2bbeae088a36 | -3.09812 | -51.28736 | 2024-09-26 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2e71f0f-43e0-322b-9bf0-a3c0bb6b2407 | -3.09754 | -51.29109 | 2024-09-26 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94529de7-b796-3e9d-bf4f-0ef94542c2d0 | -3.09468 | -51.28682 | 2024-09-26 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a337267b-741c-376b-8488-259a97f4b7c9 | -3.0941 | -51.29056 | 2024-09-26 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f46d1393-3879-31d8-aeed-e870b80b74d3 | -3.01893 | -51.1207 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e3730d7-31d7-3564-ac4a-6c1288645ac7 | -3.01606 | -51.11638 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d2802af-2fc3-345e-b816-e37d37aa65a6 | -3.01389 | -51.08493 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d1f7e54e-c31c-38f8-94ed-5a09c6deddef | -3.01101 | -51.08061 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bb0ac17f-cf25-3e40-b813-607a4e8f90e4 | -3.01043 | -51.08438 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6187529f-e1e6-3101-9ffe-2a94cdb0f232 | -3.00984 | -51.08815 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9524162e-0ffd-3b34-b84d-cd095d23b906 | -3.00755 | -51.08007 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 76990387-3250-37d6-b3ad-34769c8efbb6 | -3.00697 | -51.08384 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fd226351-dd8a-3ade-9674-e57f9d7a03b4 | -3.00638 | -51.08759 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c50c7d8-4fab-30e8-9d22-21dc89f2a50d | -2.87554 | -51.66049 | 2024-09-26 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 95368d3c-33fe-3d8e-a3e7-235dc79183d0 | -2.87498 | -51.66413 | 2024-09-26 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cb350e7d-8a6f-3325-9109-64928e4470eb | -2.87442 | -51.66776 | 2024-09-26 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4360f767-a0dc-34a2-8d72-b39be330b0d0 | -2.87216 | -51.65998 | 2024-09-26 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 64861e07-4863-3aae-9a95-f71681977863 | -2.87159 | -51.66361 | 2024-09-26 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 34966da6-03d5-35bd-a438-968dfd90485c | -2.87103 | -51.66724 | 2024-09-26 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 2da8590f-565f-39df-8d83-ad0116909f2a | -2.86821 | -51.66309 | 2024-09-26 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0892189f-d756-3f0c-b9ea-ef93a263c2db | -2.86765 | -51.66671 | 2024-09-26 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 3d95d5d7-bf5d-3963-b37c-39c48f9854f0 | -2.73433 | -51.36964 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2e866ae-f6ea-3310-a9b1-206c48e4c7f7 | -2.73376 | -51.37333 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7eeec4a-1df9-3ded-8c33-616968bccddf | -3.47559 | -51.77762 | 2024-09-26 04:57:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58829dcc-af71-3935-a669-222bb9225eb6 | -3.47421 | -51.77799 | 2024-09-26 04:57:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc0e5336-13b9-361a-bd14-ec128db0d38d | -2.58644 | -51.92201 | 2024-09-26 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d632a3e1-6164-3fbe-93f5-212bb16c8293 | -2.58308 | -51.92148 | 2024-09-26 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3d9f8c3-9561-3289-9b18-88c3a8dbe7ec | -3.3044 | -50.66241 | 2024-09-26 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d9751482-aa9a-319c-9ad2-db805d477e3f | -3.54871 | -50.79454 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fcc27e74-fc74-3323-847a-98ad0175856a | -3.89285 | -52.14113 | 2024-09-26 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff3d44c1-220d-3e17-9e55-5df7eadd95e0 | -3.89229 | -52.14473 | 2024-09-26 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4debbcf4-9831-3714-9b50-a4028d24605f | -4.05926 | -51.05806 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7763e3d1-f236-3848-9c86-5069aa9aa123 | -4.05866 | -51.06199 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 509ca940-ddd4-3fee-9e73-eed4c8759324 | -3.88576 | -51.02852 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf407b54-b83c-3567-ba72-d5679ce82166 | -3.77519 | -51.01665 | 2024-09-26 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2c5a3fc-d6b2-35bf-9dec-78438b31601d | -9.12391 | -53.29478 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4832790-3b17-3a3b-8b48-19ddb2358d98 | -9.12226 | -53.30564 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6098726b-419e-3d40-8ad0-c7d4e148af0a | -9.12054 | -53.29427 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c25a2b2-6bab-31d7-b399-e106210e2247 | -9.11607 | -53.301 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e97857a-cfd7-3606-a546-2d97eb986190 | -9.11464 | -53.29753 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc47ed42-366b-342a-b17a-7d0075e45807 | -9.11408 | -53.30114 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bad4a7f2-bcf3-35d5-8a87-47f3f9fdfa09 | -9.11127 | -53.29702 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b8bdabe-d986-319a-9c8b-a3d74686d75f | -9.11071 | -53.30063 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d6f34947-cf53-31d4-9c1c-997a12be78e5 | -9.04951 | -52.96915 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 382bd40b-e767-3478-9e09-2a4d4678ed6c | -9.04612 | -52.96861 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 107ab741-8488-397c-a820-6bedf4f18e43 | -9.00198 | -52.12004 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dacae39c-e7cc-3b7a-a5bc-8fadfbd1669a | -8.91515 | -52.77056 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 173cbd80-2084-304e-87d7-c733d928fb9b | -8.91231 | -52.76626 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57fb7738-35ee-3ee4-bd1a-625b1fbc506d | -8.91174 | -52.77003 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 210b76e1-a516-3bc8-a28b-f9347390680c | -8.91117 | -52.77379 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8136c5f-7a5c-394c-b44d-24a0f6d71f48 | -8.90832 | -52.76946 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 271f6ace-4830-3d0b-a7d7-c69999f9366a | -8.89676 | -53.02932 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c4ea2db4-a8f3-3b80-9409-f874ddcc748c | -8.89448 | -53.02151 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef11f3dd-58c2-398a-83ce-7c9b55e10734 | -8.89392 | -53.02518 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README94.md)
