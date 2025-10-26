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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cab1da33-f93f-3135-b8a5-5c09ab7c06bf | -2.94553 | -51.52956 | 2025-10-26 01:13:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| cdd57a97-9e4e-34b8-986e-598e2b8a51c3 | -3.79794 | -51.33968 | 2025-10-26 01:13:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| ee8dc3bc-f52f-3857-b60c-900944681519 | -2.12575 | -56.8489 | 2025-10-26 01:13:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 67e4ea7a-68f2-3b10-9047-9bec7ca32e3b | -6.58324 | -51.11275 | 2025-10-26 01:13:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| a09dded3-948d-39b1-ba11-11cc64895bc5 | 1.61398 | -55.76554 | 2025-10-26 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ad0ab92e-4ee8-3610-a569-eb566df41f3a | 1.61639 | -55.74828 | 2025-10-26 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 907d0b4b-ef65-3cf4-860d-36bb573a767a | 3.3432 | -60.01384 | 2025-10-26 01:17:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 26.4 |
| eef1f5a2-3a3c-3cc7-ac4b-b539c81a21bb | 3.3327 | -60.02215 | 2025-10-26 01:17:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fdcd9533-b086-36e8-80d9-57fa5c338115 | 3.34453 | -60.00427 | 2025-10-26 01:17:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 965bf48d-8cad-3a60-a934-1e73e807cde1 | -6.725 | -42.0499 | 2025-10-26 01:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| 3c8f815a-088b-3998-883f-fd8813e8014b | -2.7754 | -45.1061 | 2025-10-26 01:20:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 41ff5b88-599f-3733-8925-f1738d902b8e | -6.7061 | -42.0517 | 2025-10-26 01:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 129.0 |
| fb418530-7b11-3075-9492-dbd687afa7ba | -2.7755 | -45.0835 | 2025-10-26 01:20:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 113.7 |
| c5c802b6-f1a8-3523-bc41-45a62f90739c | -2.7569 | -45.0842 | 2025-10-26 01:20:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 378494d9-e955-3704-8a39-3fb2693c455f | -4.8933 | -43.2349 | 2025-10-26 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 70721d84-d54a-3523-9c9f-e3a5b95aedd3 | -4.7206 | -46.4276 | 2025-10-26 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 28c04f07-965f-3e80-81a0-33cca82ef65b | -9.4568 | -56.6396 | 2025-10-26 01:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| bfb26d2b-ccff-3c1d-a9fb-ccf2d3a1ad04 | -4.702 | -46.4286 | 2025-10-26 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 1ca1af46-9909-33b4-a447-37237fe8a9c8 | -4.0346 | -46.063 | 2025-10-26 01:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 8907008b-aeb1-3dd4-8b68-8a6bf0bb5eb0 | -17.3165 | -43.643 | 2025-10-26 01:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 5f5246c1-730f-39f3-9619-8d003689fc06 | -6.7064 | -42.0278 | 2025-10-26 01:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 102.9 |
| f5564bf8-9342-3eb1-b800-d930869264a4 | -17.3365 | -43.6383 | 2025-10-26 01:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 1055e54b-2625-3da6-9083-308237bad0f3 | -6.725 | -42.0499 | 2025-10-26 01:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 77.8 |
| 72fc4ec2-c4e3-3994-94d2-049e618c5b66 | -4.8931 | -43.2582 | 2025-10-26 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 9a38bf94-c783-318d-9772-c112f4bcb850 | -2.7569 | -45.0842 | 2025-10-26 01:30:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 57.5 |
| aa655e6d-5109-3c3d-922a-a0eabf8ab43e | -6.7061 | -42.0517 | 2025-10-26 01:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 135.6 |
| 27501feb-f94e-3cf9-86b3-101baf7d3a27 | -6.7064 | -42.0278 | 2025-10-26 01:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 86.7 |
| cc44efe7-c94a-3b6a-9b2d-047d7faa61ca | -17.3365 | -43.6383 | 2025-10-26 01:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 111.7 |
| f8ff6470-e664-316e-8f01-3c59401b15e3 | -4.0346 | -46.063 | 2025-10-26 01:30:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 61.8 |
| a411c459-6af7-3082-9862-590df5a2c4b5 | -4.8933 | -43.2349 | 2025-10-26 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| ff0c7bdc-8c1f-3556-91aa-f60f5f97d95d | -2.7754 | -45.1061 | 2025-10-26 01:30:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 69.3 |
| eb38c468-361f-3f19-ba33-62fa530c689d | -14.4461 | -49.9606 | 2025-10-26 01:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 02d4dc71-c3df-3d8d-b756-e24efc3354a7 | -17.3165 | -43.643 | 2025-10-26 01:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 6b591897-341f-3cd4-a727-20ee958b43a2 | -4.7206 | -46.4276 | 2025-10-26 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 56.0 |
| ba05f7f8-9a6b-3d57-8ae0-a0c0806b957b | -4.702 | -46.4286 | 2025-10-26 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 075c900f-3d16-3db1-a41d-bd220c87a742 | -2.7755 | -45.0835 | 2025-10-26 01:30:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 9a79b8fb-20bd-3a0c-a4b1-0d25874828cb | -14.4267 | -49.9635 | 2025-10-26 01:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 8c3fe14a-dcb3-30b4-b98f-44c6bd89487b | -4.0346 | -46.063 | 2025-10-26 01:40:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 1f9bf23e-b117-3c5d-a4c5-944ddf2800da | -6.7061 | -42.0517 | 2025-10-26 01:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 112.5 |
| e9ee1153-51df-38cb-b9a1-34c70a951013 | -17.3165 | -43.643 | 2025-10-26 01:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 47374555-af31-3429-a18d-96536409f560 | -6.725 | -42.0499 | 2025-10-26 01:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 95bdaf3d-bb1b-3a74-90dd-e57d9928b02c | -17.3365 | -43.6383 | 2025-10-26 01:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 92.4 |
| ce4c9936-dedb-33ed-95e5-0bd2493e61c2 | -6.7064 | -42.0278 | 2025-10-26 01:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 424ff674-ca61-3cda-9aab-577e38e858bd | -2.7755 | -45.0835 | 2025-10-26 01:40:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 4f657058-1925-3405-9b0c-379b77383934 | -2.7569 | -45.0842 | 2025-10-26 01:40:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 1b9fe04c-a364-3219-99b2-a97b99e081ef | -2.7568 | -45.1067 | 2025-10-26 01:40:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 46.0 |
| be27903e-5cca-30fa-9b85-e4883f81b8ac | -2.7754 | -45.1061 | 2025-10-26 01:40:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 2b2a83f2-313a-37ea-b492-06cb161f28bf | -17.3158 | -43.6674 | 2025-10-26 01:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 772489a3-0920-340a-9ec4-3f855906d8c1 | -4.8582 | -42.9332 | 2025-10-26 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 5d2c6203-8160-394c-8b10-02809e787183 | -14.4461 | -49.9606 | 2025-10-26 01:50:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 62f41e0f-fb01-38a4-af9a-8d323eb53467 | -2.7755 | -45.0835 | 2025-10-26 01:50:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 049619ca-021c-3a81-9097-bca01679dea6 | -13.0564 | -45.8829 | 2025-10-26 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 119a6801-98a3-3c34-b861-c5ee6e8752b1 | -2.7569 | -45.0842 | 2025-10-26 01:50:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 678ff9e5-975e-391c-b043-4bbf42c8e67e | -4.8933 | -43.2349 | 2025-10-26 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 6e91229b-b626-3565-be9d-9113e424ae59 | -10.6165 | -63.4735 | 2025-10-26 01:50:00 | GOES-19 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 47.5 |
| eabbb95f-36c2-38bb-8d49-3b279c96a54a | -17.3165 | -43.643 | 2025-10-26 01:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 145.6 |
| a6946980-1be4-30f2-b3b7-dbd5e6650889 | -6.7061 | -42.0517 | 2025-10-26 01:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 107.8 |
| 1b4979f6-6f34-3ae9-a84c-de863a8171c1 | -4.8767 | -42.9554 | 2025-10-26 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 427a14a6-ffab-3c2a-8ee9-ec0d0f319f47 | -3.7661 | -47.5727 | 2025-10-26 01:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 9b6da37e-3253-3e00-9f80-3ddd390b42ba | -2.7754 | -45.1061 | 2025-10-26 01:50:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 63.8 |
| ac744721-ee6e-3a02-b24f-72696185143b | -2.7568 | -45.1067 | 2025-10-26 01:50:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 1c949da0-05f8-304d-8440-5a44740a4733 | -4.7206 | -46.4276 | 2025-10-26 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 7760a5f4-2d97-3ce0-bd5a-c9504dcc4931 | -4.912 | -43.2337 | 2025-10-26 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| ce5dc194-db59-360c-8973-464450bf3fd1 | -17.3158 | -43.6674 | 2025-10-26 01:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 13a42497-7e4e-323f-bfe5-56e6cb7497e1 | -6.7064 | -42.0278 | 2025-10-26 01:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| d39dd24b-fa76-3408-826f-8b6e49329194 | -4.8769 | -42.9319 | 2025-10-26 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 09395115-fdd5-389f-9fe9-c462690eef1c | -4.702 | -46.4286 | 2025-10-26 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 584e89fc-c3d5-35aa-8107-42177f9aafd5 | -4.858 | -42.9566 | 2025-10-26 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 307.3 |
| 8f31c00c-d021-35b4-928c-fd4e117b74d8 | -17.3365 | -43.6383 | 2025-10-26 01:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 72c64552-4ccb-3399-9e85-78e40eebadce | -4.8931 | -43.2582 | 2025-10-26 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| b7dc58e8-81f1-3d0c-a89a-9541c1ff4f57 | -2.7568 | -45.1067 | 2025-10-26 02:00:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 33.8 |
| c27c8b78-63cb-376f-94af-de5f3f31a161 | -12.3165 | -47.4855 | 2025-10-26 02:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 9d246518-61f1-3dbd-83b1-cfa2b73960a1 | -2.7569 | -45.0842 | 2025-10-26 02:00:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 766b783c-6da9-3b4f-9233-69c798c91ca7 | -4.702 | -46.4286 | 2025-10-26 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 59.9 |
| e0bf5270-2c72-3c12-8a7e-438a5033600e | -2.7755 | -45.0835 | 2025-10-26 02:00:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 61.8 |
| e10428b2-e34a-3158-8d84-2540c23ce879 | -4.8767 | -42.9554 | 2025-10-26 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 83291920-f45e-35f3-8719-3adc6f4b038e | -4.7206 | -46.4276 | 2025-10-26 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 62.2 |
| c7c4ef33-d57c-3268-a740-7bdfa39c8603 | -4.8931 | -43.2582 | 2025-10-26 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| ed225aa3-6570-3927-814c-82cd113db468 | -4.858 | -42.9566 | 2025-10-26 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 200.7 |
| 56477702-4618-3e0a-9c31-1ad749b0b7c0 | -17.3158 | -43.6674 | 2025-10-26 02:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 80.5 |
| e25b87de-1471-3480-b954-45c5eb795510 | -17.3165 | -43.643 | 2025-10-26 02:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 176.0 |
| 1d6d693e-ced9-3352-a445-fb873fa0576a | -4.8582 | -42.9332 | 2025-10-26 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 0469556b-aac3-3d5b-894e-33e63342406b | -4.8933 | -43.2349 | 2025-10-26 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| d5c6d523-5d87-3f2d-bda7-8fe2d69be33b | -2.7754 | -45.1061 | 2025-10-26 02:00:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 85d828fe-2497-32a5-978b-0520bfdd77af | -6.7064 | -42.0278 | 2025-10-26 02:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 73.0 |
| 91a86e6d-94bf-3a6f-b37a-21f5ae6041b0 | -4.8769 | -42.9319 | 2025-10-26 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 0910af7a-7ff6-36c1-9b68-261da9640bb1 | -5.1181 | -43.1964 | 2025-10-26 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| e10d908c-ce6f-313b-9ef6-199263e7b454 | -5.1183 | -43.1731 | 2025-10-26 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 51dc802f-4a54-3bbd-84c9-fcb00d024f8d | -17.3365 | -43.6383 | 2025-10-26 02:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 125.8 |
| cf4f8a43-6253-38a3-ba45-8baba87a8b42 | -5.0994 | -43.1977 | 2025-10-26 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| aeaeb5d9-0366-3573-984e-c1309a688f3f | -6.7061 | -42.0517 | 2025-10-26 02:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 108.0 |
| dcc54c93-73cc-32dc-bb49-99ff6428fd99 | -5.0996 | -43.1744 | 2025-10-26 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| b440c06f-bc85-3467-afc8-cd8c1aba338c | -3.7661 | -47.5727 | 2025-10-26 02:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 060272f4-6a55-3ba7-bba4-63fa548d03cb | -13.5405 | -43.0077 | 2025-10-26 02:10:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 80.6 |
| a0db7214-9322-3cf0-8540-8c6fbdbf2118 | -5.0992 | -43.2211 | 2025-10-26 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 8f133dfb-3356-3cfa-84ea-8c55a0dbbc9f | -5.0994 | -43.1977 | 2025-10-26 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 188.0 |
| 5e8e0f91-371d-3026-8821-d8ef8ca7ff56 | -17.3165 | -43.643 | 2025-10-26 02:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 4b2a3919-8958-317a-b469-e602a7d8176d | -5.1181 | -43.1964 | 2025-10-26 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 147.2 |
| c7180451-2f19-3f20-a2d2-dd60db9a7f32 | -3.0908 | -49.4671 | 2025-10-26 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 75cee9d4-6a19-34cf-93d3-c41b8c3effe9 | -4.8931 | -43.2582 | 2025-10-26 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |


[Clique aqui para ver as próximas entradas](README5.md)
