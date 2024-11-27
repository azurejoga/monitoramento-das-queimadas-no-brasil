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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2730ab3-6fc5-32ae-ac56-78ef9f7ff8f5 | -4.22386 | -48.6675 | 2024-11-27 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a489c1b8-ce2f-3a08-b95a-ce8678ed87e8 | -3.16421 | -48.43969 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 02ea6a8d-9b90-39b8-ab39-365d34dc7f33 | -1.52018 | -46.07597 | 2024-11-27 03:55:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 786dfcbb-df46-36a7-b7cb-a7fb8426698d | -3.97326 | -48.06298 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1631b4e7-528e-3a57-8c86-a96acea8c5c4 | -6.91466 | -35.04265 | 2024-11-27 03:55:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 0f1ca62d-fba6-35b7-ad83-4d254479f454 | -4.49756 | -46.59988 | 2024-11-27 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1142423-b3a2-314c-9802-56d76ad18104 | -3.09951 | -50.36615 | 2024-11-27 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8f1c1c8a-5fe0-35e1-aca5-0a14daaee1fb | -6.37128 | -47.35844 | 2024-11-27 03:55:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84a88770-6d6f-37b6-99fe-dff9382e62a6 | -2.53202 | -47.32818 | 2024-11-27 03:55:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| daad8ad3-2199-3fd6-b18f-906a02b8ce63 | -5.83913 | -39.21045 | 2024-11-27 03:55:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| efd3729c-28a0-31dd-a3fc-a73c94857064 | -3.01663 | -48.60318 | 2024-11-27 03:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70c444e4-7e5a-38f3-9a1f-216d4e0a3491 | -3.972 | -46.73588 | 2024-11-27 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66cbcb43-7936-331f-b3e4-a6fb436c4552 | -3.9682 | -48.07735 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 7162cbfc-56b7-3e94-9427-3a3944cdabe2 | -4.6139 | -44.24273 | 2024-11-27 03:55:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aac28e8e-b7b7-3834-bca1-8c211090217c | -5.42557 | -37.61082 | 2024-11-27 03:55:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5c50892c-cf56-3d22-9809-801dfbcd84aa | -2.84185 | -49.40399 | 2024-11-27 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44c59015-a18c-3090-a448-31d22b19da7a | -4.21076 | -50.90689 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| ceed796d-55f1-31d6-8bf7-0857fbfbd63e | -3.34351 | -50.18845 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d68459b5-fae6-3530-9eab-97831b5b6035 | -6.19682 | -44.43084 | 2024-11-27 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c59abac2-5a0b-3c57-9995-c4b04cfbf67b | -8.1387 | -44.48013 | 2024-11-27 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a67f21ed-6bad-3688-842a-ba4908ac6802 | -2.58194 | -50.64258 | 2024-11-27 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9d978d23-9f40-395c-a66a-29523e9e973c | -9.84377 | -35.9974 | 2024-11-27 03:55:00 | NOAA-21 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| 941dd180-191c-32af-8f9d-55719a527211 | -5.90123 | -43.40881 | 2024-11-27 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a298f55d-6138-375b-bd05-2f9a866f529e | -8.13106 | -44.47493 | 2024-11-27 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3972d8f-a2da-334e-90f6-7a976c2ffdd5 | -3.41384 | -50.20649 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2599b218-d86d-3e9b-8ce4-ee41204cf87e | -3.80214 | -45.21976 | 2024-11-27 03:55:00 | NOAA-21 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bad06070-b0e8-3640-8112-9cb6f7b1dd41 | -3.92705 | -45.84603 | 2024-11-27 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9ff469cf-ff7c-3604-b294-dcefa0be9b77 | -3.50977 | -50.31328 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fa932ef9-80ef-334d-8ec4-f3c9cc79ade5 | -4.24115 | -41.92398 | 2024-11-27 03:55:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8325a33e-caed-3a75-bc0d-33106c3a8b25 | -3.28345 | -51.11524 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f1019307-4230-3a29-931e-2956343f2c02 | -3.16565 | -48.43129 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 0cb9e06f-541c-3083-ad1c-af013c9aabbe | -4.14611 | -43.80816 | 2024-11-27 03:55:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 67f9854b-f0a3-374c-9956-8193a39e14f6 | -3.9754 | -46.65114 | 2024-11-27 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc0b7167-0002-3975-98b6-bf5c2ac130d8 | -8.61316 | -35.6942 | 2024-11-27 03:55:00 | NOAA-21 | CATENDE | PERNAMBUCO | Brasil | 2604205 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 253ea2a3-adce-35aa-a120-d1eb8cfada53 | -4.94852 | -45.87669 | 2024-11-27 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 023f1b40-a5bd-373d-a427-e5e36b953073 | -3.14357 | -48.53525 | 2024-11-27 03:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c36a0bc0-5be3-34c7-bd79-e8dfe9a8b61b | -3.82297 | -44.44156 | 2024-11-27 03:55:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef471071-c295-3e43-9d2a-c756deb97416 | -3.18179 | -48.4425 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 79e392c9-ed53-32c8-b615-5f85a6a9badf | -2.93225 | -48.01395 | 2024-11-27 03:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 49ca9a85-9ccd-3cc8-8ae0-6267bd5b4b5e | -5.70373 | -39.54885 | 2024-11-27 03:55:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 34214b60-7905-3c10-add7-bee484671231 | -4.25968 | -48.66895 | 2024-11-27 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b79ee198-759d-33f2-aafd-2b93123e129d | -3.9257 | -45.84338 | 2024-11-27 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 79e26af7-1f9c-3a42-84f2-8bffa88cc4a5 | -2.42208 | -44.64592 | 2024-11-27 03:55:00 | NOAA-21 | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7be4ee3f-8121-3824-8399-2058502a5968 | -2.92478 | -48.63632 | 2024-11-27 03:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be29c03a-caaa-30de-8c3d-1ca273125c42 | -4.20798 | -50.90512 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3c4e77cc-d148-35d0-b138-ead3e31abe2a | -3.16935 | -48.44483 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 6ddbda92-e5a0-36bf-8948-d59339926622 | -2.57313 | -49.09131 | 2024-11-27 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| de0f091e-35a2-31b2-9e06-f41a0476cad6 | -8.13168 | -44.47124 | 2024-11-27 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f24265b4-0734-3d95-9000-aea55973b272 | -4.65909 | -45.04263 | 2024-11-27 03:55:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4c42a383-2125-31e0-a026-7a1177333933 | -4.50314 | -46.59773 | 2024-11-27 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56f49fdf-3b92-3837-b522-2c05c9d6afc3 | -4.00208 | -47.91572 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19f39469-1af7-32e9-b492-59b80e7644c9 | -3.96501 | -48.07763 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| ad42da85-e169-363b-a057-a0a1ed3c06c3 | -4.229 | -48.67251 | 2024-11-27 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0b6c5b8-2564-39b0-a8e1-3c46bfe03824 | -3.26367 | -46.41938 | 2024-11-27 03:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e622540e-cd35-3ec7-80b9-e80835fb881c | -5.70022 | -43.25975 | 2024-11-27 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4babd25-d85d-3cb3-bb78-887565ce2038 | -4.69914 | -44.96899 | 2024-11-27 03:55:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76187395-eaa1-3b9e-b7b0-39205ebdaf43 | -5.83967 | -39.20697 | 2024-11-27 03:55:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2220e9af-a9ff-3978-959f-9ba2875c2d43 | -4.74659 | -40.43807 | 2024-11-27 03:55:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f87e1ae5-531b-3724-8c77-b7ceb9188052 | -5.5028 | -47.16666 | 2024-11-27 03:55:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5761b982-dacc-3095-9de9-eabec8d4ebee | -3.59043 | -44.92769 | 2024-11-27 03:55:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f70b86cb-148c-3198-a444-211611c10d5b | -3.00089 | -45.46777 | 2024-11-27 03:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 2d07f41b-6b4c-3804-bb0f-45d7fc449a4d | -7.93255 | -34.91676 | 2024-11-27 03:55:00 | NOAA-21 | PAULISTA | PERNAMBUCO | Brasil | 2610707 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 4291c291-97ec-325b-8701-b039738b5c45 | -6.19344 | -42.52537 | 2024-11-27 03:55:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3a11816b-c011-3909-a0e8-dc1f16fbfe2a | -3.05065 | -48.51132 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1db52154-0ec2-36a7-bb1f-14583b3ad8eb | -4.72342 | -46.57288 | 2024-11-27 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9b0968ef-9e9f-3b17-b5bb-918508aec5e1 | -3.94031 | -46.89559 | 2024-11-27 03:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 30417f07-2270-3b2d-b209-4dd8d7bb242e | -4.80772 | -43.30062 | 2024-11-27 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 444f03e9-a816-3b80-b525-eb70eb4f8d0f | -2.99484 | -45.47036 | 2024-11-27 03:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0721aaee-d3ee-3ed4-b4bf-c8dd1c7663cf | -3.89896 | -45.62372 | 2024-11-27 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ef9f156-3377-3c53-b839-498510a16bdc | -8.51967 | -37.0593 | 2024-11-27 03:55:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 992ef227-cabf-366e-a672-c7905221c14f | -6.91533 | -35.03818 | 2024-11-27 03:55:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 317a9c18-3a27-3151-9c00-405cbd9a3aba | -2.81657 | -48.60452 | 2024-11-27 03:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b4d41a1-e5ff-3942-9f17-07a2de993a18 | -2.46563 | -48.79466 | 2024-11-27 03:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afe533a0-6ca8-3b31-a192-12298b7b9c76 | -4.21944 | -47.21958 | 2024-11-27 03:55:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 560575c2-1393-3bac-ad4c-a7eb429c2afd | -2.84012 | -46.83373 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5c3aee5e-4c2c-32de-ae8b-a3dcfc37469b | -2.92553 | -48.63174 | 2024-11-27 03:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9feadf0e-33d6-3b8b-bd5b-1f4a91208d1a | -2.54147 | -45.39115 | 2024-11-27 03:55:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 8a8388c8-47c1-3f69-b624-6ba77483aa38 | -5.90924 | -44.61663 | 2024-11-27 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fffc6fc-f0b2-3ae9-8e54-8ba9c8b2fabd | -2.93404 | -48.63651 | 2024-11-27 03:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 050b4881-5445-3ef5-ab2a-96219525ec28 | -4.28091 | -37.99504 | 2024-11-27 03:55:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 365c8f75-cdf3-393e-b1b8-989835b9e6ee | -3.96519 | -48.06129 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1c6aae4-4947-3a06-80d0-cd542d01ea92 | -2.82897 | -46.83535 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 394063ca-e52e-3a30-a58b-f71c019ea7e5 | -2.34895 | -47.64526 | 2024-11-27 03:55:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dafb6bca-a861-31a8-8321-99bb216e8156 | -2.9281 | -48.63544 | 2024-11-27 03:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4793b11e-432f-3321-b350-6131b185e270 | -2.0938 | -46.31952 | 2024-11-27 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da7eb63c-2f96-37c8-bf24-ee7f4244fc61 | -3.96438 | -48.08146 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 98ad20a9-12de-347a-85d5-ee5a8dc648ba | -2.82476 | -46.82796 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8230beed-d3d5-3c53-bbef-d3083db72759 | -7.6955 | -39.02115 | 2024-11-27 03:55:00 | NOAA-21 | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d7301110-1dce-3775-bab9-e11c38d2ce3a | -3.17593 | -48.44157 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| a6794da0-c3a4-333d-9f0f-c705a7236c59 | -4.22068 | -50.89018 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| eb6e8f54-6077-3c80-89f4-a5283f063142 | -2.61062 | -48.36712 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0cf8ced8-ef60-3fa4-b279-66f75e85ccb3 | -6.13037 | -41.98418 | 2024-11-27 03:55:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0611a8bf-00a5-37ef-bc54-c34640d439fb | -8.51757 | -39.48331 | 2024-11-27 03:55:00 | NOAA-21 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 49797c57-b59e-3910-aeec-9a44169d6ff8 | -2.11553 | -46.45543 | 2024-11-27 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| d509e4b1-c41e-3dd1-b5cd-54f7e0eba305 | -6.91162 | -35.03766 | 2024-11-27 03:55:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 28e52ecc-abdd-311c-81bf-842432a82e64 | -4.00148 | -47.91915 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa816545-dab4-3f4f-8234-55e312345fc7 | -3.39399 | -44.16682 | 2024-11-27 03:55:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 723007dc-814f-30df-a178-082511331fdf | -4.21988 | -46.44681 | 2024-11-27 03:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2673a3cb-7b83-3c71-9638-6449ea91a0af | -3.24621 | -50.61529 | 2024-11-27 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d857760-45c1-37be-b8b3-5e6cc54b4836 | -4.83303 | -45.83231 | 2024-11-27 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README24.md)
