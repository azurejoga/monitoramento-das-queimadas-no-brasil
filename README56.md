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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70ac200f-18d1-36e3-ac46-aa3f62e37504 | -8.051 | -43.1237 | 2025-11-15 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.3 |
| 31517bf1-1359-333c-8a24-15a6fbbf659a | -8.0513 | -43.1001 | 2025-11-15 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 303.1 |
| 14d120ac-48f0-3552-8b8d-95e93d5cd179 | -8.0516 | -43.0765 | 2025-11-15 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.7 |
| df5b62e8-0996-3cb8-ae34-c0bbe3a78c53 | -3.821 | -44.4041 | 2025-11-15 06:00:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 87b6dd5c-d9b9-3328-aabf-3025079f6181 | -8.0706 | -43.0745 | 2025-11-15 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.7 |
| d2ce5c71-f5cd-3ed2-874b-2c5f8c9048fb | -8.07 | -43.1216 | 2025-11-15 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.6 |
| 5d67b63c-3d26-396a-b91b-106e8015abab | -3.8209 | -44.427 | 2025-11-15 06:00:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 6ca8730e-0bbb-3dde-8c38-c501127d13c1 | -8.0703 | -43.0981 | 2025-11-15 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 332.0 |
| d47f1b93-7088-3d11-b285-bd7a8351c9a8 | -3.8396 | -44.4261 | 2025-11-15 06:00:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| b4854274-7d45-35a4-853c-52bf7c62aef0 | 2.75053 | -60.36861 | 2025-11-15 06:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bfbf67d3-ed01-3b23-b931-ece011e5446a | -3.8397 | -44.4032 | 2025-11-15 06:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 4a7b19aa-950d-3b7d-aa81-9e0efe4020cd | -3.0357 | -45.0967 | 2025-11-15 06:10:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 56.5 |
| a3853801-008b-3663-9690-d79d2be0ae8d | -3.8396 | -44.4261 | 2025-11-15 06:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 8c0e1018-817c-39bd-b9ca-971e48a736a1 | -8.051 | -43.1237 | 2025-11-15 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.2 |
| e48422e2-7ddf-3a77-b269-4ae12d38e83f | -8.0703 | -43.0981 | 2025-11-15 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 220.9 |
| 7eab4e72-d12b-30da-81eb-6e3b3724d3c7 | -8.0516 | -43.0765 | 2025-11-15 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.4 |
| e0d538a5-54e9-330f-bbac-d2bbc71f5b15 | -3.821 | -44.4041 | 2025-11-15 06:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 5f7b4686-8732-34f8-9ac8-676f3910f452 | -8.0513 | -43.1001 | 2025-11-15 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 256.0 |
| 5ab9ba87-f19a-30e9-9046-2d869fdc09c5 | -3.8209 | -44.427 | 2025-11-15 06:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 1919fa2d-9c5e-311b-8d91-8ddbb74476c8 | -8.07 | -43.1216 | 2025-11-15 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 7ee54e35-740b-3d1c-8e6a-edb259b83d76 | -2.88007 | -51.42213 | 2025-11-15 06:18:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 75d66440-d3cb-3478-a0c3-ac1ab59a6d37 | -3.83425 | -44.4141 | 2025-11-15 06:18:00 | AQUA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 9d3ebaa3-43d4-3a1c-bd8d-c65eae4962ba | -3.4655 | -50.11807 | 2025-11-15 06:18:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b8ca2bca-78fe-3f48-9e42-55bb3cf2e458 | -3.1449 | -45.38313 | 2025-11-15 06:18:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 044955da-c39a-32c1-baae-4e411e7f8351 | -3.52762 | -50.87203 | 2025-11-15 06:18:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 70bcf43c-ec4c-3774-abf7-cd058b08c675 | -3.65558 | -44.81023 | 2025-11-15 06:18:00 | AQUA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 7a0fb874-2525-3f85-bba7-58abd09922b4 | -4.55204 | -43.20878 | 2025-11-15 06:18:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 67942de3-e878-3b0a-8410-f7ecaeb9dd71 | -4.10323 | -48.00975 | 2025-11-15 06:18:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8eade8d4-bd67-3e78-a617-eaa9a8ddc8df | -2.95006 | -45.14888 | 2025-11-15 06:18:00 | AQUA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 2d875b80-d431-3476-b6da-a8e71b0cbd3f | -3.83687 | -44.39547 | 2025-11-15 06:18:00 | AQUA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| e2df7274-90ca-398e-8f03-6e165e67148c | -4.53491 | -43.23069 | 2025-11-15 06:18:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| be93a417-d198-3718-b362-bacfc836a53b | -4.54372 | -43.22403 | 2025-11-15 06:18:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| ad081da6-1de1-3d18-8464-270f42f19bc8 | -4.00176 | -47.67676 | 2025-11-15 06:18:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| dc12bc32-e775-3901-b518-1a6e4abd87bf | -2.51546 | -47.81063 | 2025-11-15 06:18:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 5ba5af87-abe7-3dbb-8cb4-ada48179328e | -5.0375 | -43.6112 | 2025-11-15 06:18:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 324e5702-d086-3af0-8e6b-a707633708c9 | -4.53814 | -43.20702 | 2025-11-15 06:18:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| e9d93e50-7a6d-3ce4-aec8-a16e37dbffb0 | -3.82185 | -44.4123 | 2025-11-15 06:18:00 | AQUA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| ebad883f-1487-318c-95f5-82e3c280f4f0 | -3.03641 | -45.10405 | 2025-11-15 06:18:00 | AQUA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 60a6a8c2-ae70-3c36-88aa-ddc2aa8bcf2b | -3.99208 | -47.6754 | 2025-11-15 06:18:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 153043f0-6ec3-3ab1-a2b0-3810f03f8ac8 | -4.54716 | -43.2003 | 2025-11-15 06:18:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| d37ab560-ad51-390e-987d-68a792d640c1 | -3.82444 | -44.39378 | 2025-11-15 06:18:00 | AQUA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 808184d0-cfc6-3fa9-81ff-41e7075e8da8 | -3.45673 | -50.11679 | 2025-11-15 06:18:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7f65892a-de9f-3f8b-a6e2-cef2accea8ba | 2.34663 | -51.6475 | 2025-11-15 06:18:00 | AQUA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 129a249d-275c-3fad-a644-efcdf402d4b6 | -4.85063 | -43.24271 | 2025-11-15 06:18:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| fa395813-eccd-396b-bc94-512a97ccad8d | -2.79277 | -52.96804 | 2025-11-15 06:18:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 33a14100-766a-318a-ad4b-3f1f64594864 | -8.05142 | -43.09716 | 2025-11-15 06:20:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 356.7 |
| 8467cbd1-f42a-3da9-9e43-f3e486e9444f | -7.87105 | -48.40531 | 2025-11-15 06:20:00 | AQUA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a5ff95d5-919b-3207-8090-98c9d89d88b6 | -6.16183 | -48.04491 | 2025-11-15 06:20:00 | AQUA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f73a4800-f0ff-3305-984a-a5a217b1e806 | -8.07 | -43.07035 | 2025-11-15 06:20:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 37.6 |
| 5641de87-5208-3c33-8785-320220fd998f | -8.05515 | -43.06823 | 2025-11-15 06:20:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 37.0 |
| 4424f525-eccb-3e88-a8e9-80ff24407ef8 | -4.72222 | -48.55956 | 2025-11-15 06:20:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3a7cc2f4-6e3f-3c0d-9877-dc1e42cffb35 | -7.88237 | -48.39563 | 2025-11-15 06:20:00 | AQUA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 867d4000-517b-3acc-afcb-2208248eb1d5 | -6.1521 | -48.04343 | 2025-11-15 06:20:00 | AQUA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 59c805a8-53e8-3539-8714-fc75d4e4b98c | -3.59705 | -54.67266 | 2025-11-15 06:20:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 58215df3-d032-3932-a9f7-f238574ebaa0 | -5.23256 | -44.34983 | 2025-11-15 06:20:00 | AQUA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| a38d3609-4b60-3a1e-8a0d-94fa5eaadd4d | -5.03418 | -43.59479 | 2025-11-15 06:20:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| edefb184-95d4-3bf6-a4b2-96b03fa29214 | -7.8808 | -48.40661 | 2025-11-15 06:20:00 | AQUA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 91caddb6-7df4-3ce1-aaa6-08dc2ae94de6 | -4.72162 | -47.15593 | 2025-11-15 06:20:00 | AQUA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 847f2f64-206e-36c5-82b6-a519cdd0997e | -4.73173 | -47.15751 | 2025-11-15 06:20:00 | AQUA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 88309a1b-0eef-360e-8163-88712d03ea56 | -8.06625 | -43.09915 | 2025-11-15 06:20:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 214.9 |
| ff12dac9-5e41-35c1-90bb-888c8fc2c394 | -10.93136 | -48.69464 | 2025-11-15 06:22:00 | AQUA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b118adde-ba0d-305b-9dd9-3c30694e06b5 | -11.84023 | -49.21503 | 2025-11-15 06:22:00 | AQUA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| e2db10bc-de14-3181-8657-221baad5a997 | -11.85158 | -49.20524 | 2025-11-15 06:22:00 | AQUA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 73db1c0e-c904-3371-9c70-129c36f0f260 | -11.91712 | -46.20692 | 2025-11-15 06:22:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 15ec6528-e19a-39fc-b60f-74cf46ac11e2 | -11.91459 | -46.22589 | 2025-11-15 06:22:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b6e1f0ce-b2a3-3a69-b3b1-fc6000763c1a | -10.35365 | -48.72805 | 2025-11-15 06:22:00 | AQUA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 320c846c-5819-3ab7-a85d-036c9799a4b7 | -12.67292 | -46.77899 | 2025-11-15 06:22:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a9d096af-7439-3762-b2f4-e1987eb8f1f9 | -12.66011 | -46.73511 | 2025-11-15 06:22:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 811ef2ce-3ea1-3658-9659-993e9b7f17d9 | -11.92095 | -46.21282 | 2025-11-15 06:22:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| f770e89a-77d4-324d-ad2d-cd0127bb1407 | -12.68699 | -46.7634 | 2025-11-15 06:22:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 71db2957-7ccd-3a17-bba1-463a27f7c81d | -12.67509 | -46.76184 | 2025-11-15 06:22:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 4c33cdce-1f9f-3312-9b0a-09a0ffc5f697 | -11.91945 | -46.18939 | 2025-11-15 06:22:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 09f872e9-70bf-37c5-9c76-373d1244c95e | -11.91093 | -46.19297 | 2025-11-15 06:22:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| b3a23146-a6df-3532-8fbc-837d68bdf0a5 | -10.34764 | -48.9102 | 2025-11-15 06:22:00 | AQUA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 04b83498-5549-31c8-8806-b07f51c6fd5a | -11.17225 | -48.14339 | 2025-11-15 06:22:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1e03b1cb-33a7-3957-ab9a-53a3105790a4 | -11.84179 | -49.20391 | 2025-11-15 06:22:00 | AQUA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 674858c3-2bd8-33d0-a111-d25dedac0a62 | -9.48876 | -47.28212 | 2025-11-15 06:22:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0080689d-7af0-373a-a502-e34e4bdadbac | -11.84999 | -49.21646 | 2025-11-15 06:22:00 | AQUA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 8ad2b8e6-78d3-3584-918f-1171648ad5ca | -11.70782 | -48.38992 | 2025-11-15 06:22:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9aeebea9-7e84-3ec8-8132-06da1b677bfb | -10.34871 | -48.9171 | 2025-11-15 06:22:00 | AQUA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d18e0a97-de22-3284-9f59-30b771ab2250 | -10.93049 | -48.70075 | 2025-11-15 06:22:00 | AQUA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f9bb22a4-8bbf-3eac-92e4-7c95a49cafb2 | -3.721 | -42.4119 | 2025-11-15 06:40:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 53.4 |
| 09979d03-5cc4-3238-9e17-9d5ad1e7f089 | -3.7024 | -42.3892 | 2025-11-15 06:40:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 88.1 |
| 461ef41c-cdf0-3fef-a149-da9062578632 | -3.7023 | -42.4129 | 2025-11-15 06:40:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 56.9 |
| 47bbe943-5b3d-3656-8498-78c483fd2a35 | -3.9292 | -45.0128 | 2025-11-15 06:40:00 | GOES-19 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 49.9 |
| e50ced91-8120-3e52-94f1-77f48b21cc3c | -3.7211 | -42.3883 | 2025-11-15 06:40:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| 5a1312b5-ea3b-3fed-8c7d-bf9bfd82e0da | -3.0908 | -45.23 | 2025-11-15 06:50:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 49.7 |
| a464face-0527-3d23-853c-b41b1fc8ff84 | -3.7211 | -42.3883 | 2025-11-15 06:50:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 66.9 |
| 400ad7f5-c725-3235-8a56-af9442376a18 | -3.7024 | -42.3892 | 2025-11-15 06:50:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 624905c7-5692-35a2-81c2-456bb2e676b3 | -3.332 | -45.333 | 2025-11-15 07:00:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 49.1 |
| e80c882a-1c5f-33dc-9420-debfcc56fd15 | -3.332 | -45.333 | 2025-11-15 07:10:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 6a3e32ce-e73a-3423-878b-231b03f57c59 | -3.3134 | -45.3338 | 2025-11-15 07:20:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 85.4 |
| f2da382a-52aa-36e9-9328-595872bc51ca | -3.332 | -45.333 | 2025-11-15 07:20:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 72.4 |
| e5d5f7b0-9a48-3bcf-93c2-34163ef40b3c | -3.332 | -45.333 | 2025-11-15 07:30:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 0ca1f932-4513-39aa-afff-993674af8846 | -3.2584 | -45.1783 | 2025-11-15 07:30:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 05a4d4af-28dc-3f60-8b24-edaf449b017e | -3.1006 | -43.1912 | 2025-11-15 07:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| a655b907-7912-3479-904c-484e40376b45 | -3.3134 | -45.3338 | 2025-11-15 07:30:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 88.8 |
| cd88a113-ed12-3415-bc70-30c9e8af95cf | -3.3134 | -45.3338 | 2025-11-15 07:40:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 0f41ac06-4284-30fb-8a6f-8adef1de3066 | -3.2025 | -45.2031 | 2025-11-15 07:40:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 52bccdb3-cffb-33c6-be48-2ac5ca15a72b | -3.332 | -45.333 | 2025-11-15 07:40:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 78.3 |


[Clique aqui para ver as próximas entradas](README57.md)
