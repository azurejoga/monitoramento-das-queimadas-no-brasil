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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 531f6341-f3fb-3cc4-8e06-5ec57f49f8a5 | -4.4445 | -43.2397 | 2025-10-04 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 359.6 |
| 892460ae-bea9-3def-863a-cdc72b3c51cc | -11.9339 | -46.3699 | 2025-10-04 02:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| d4f8d765-727d-3410-ae7a-ea5f66076856 | -11.9147 | -46.3726 | 2025-10-04 02:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 4642dce6-b4f1-3d33-a38b-0fcef83a184f | -11.5072 | -46.7446 | 2025-10-04 02:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| a806725f-ee96-331f-9073-d51fbdbdf3b5 | -15.0374 | -49.4549 | 2025-10-04 02:40:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 1484b34a-bb80-3d8f-96da-420cffb50a3c | -12.0507 | -45.1872 | 2025-10-04 02:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 7ce03e0e-b24d-3907-854b-d9db01b15e38 | -12.031 | -45.2132 | 2025-10-04 02:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 9f192edf-e899-371a-a2b6-cf0e81fd5b00 | -12.0502 | -45.2103 | 2025-10-04 02:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 39d8d33c-6a3a-3fdf-b1ba-254d56b409e2 | -12.0507 | -45.1872 | 2025-10-04 02:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| cd9fefe2-41b9-3286-a1be-5ee1423cd1bd | -16.0212 | -50.9425 | 2025-10-04 02:50:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 97e3a7e8-8c21-3f2e-8701-0b21992c8f7d | -5.2154 | -45.0529 | 2025-10-04 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 0265326a-cca0-310f-8e30-ac837df7f1b2 | -11.9339 | -46.3699 | 2025-10-04 02:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 523c72cf-76f5-3fd5-8352-ce0edcf7121a | -9.3464 | -54.5201 | 2025-10-04 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 9f2204f0-229c-3a7a-b077-59f9d1a2f0c3 | -11.9143 | -46.3953 | 2025-10-04 02:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| dbab8109-77d2-3b9e-a21b-41abc717f67d | -4.4258 | -43.2408 | 2025-10-04 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| dea01793-e39a-31ac-b4ac-30e213d7266f | -20.1352 | -46.4218 | 2025-10-04 02:50:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 609d5845-6ac9-3fec-b3be-bd8dbc08f67c | -17.7044 | -47.0821 | 2025-10-04 02:50:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 1eb91d94-33c4-3c3a-a4aa-529e4c09883c | -9.3276 | -54.5215 | 2025-10-04 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| e1a6adbc-7b1d-3b81-8eea-fc1bdd8ae7ff | -9.3569 | -45.7925 | 2025-10-04 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 53cc625e-f81f-3e34-b007-1aceab06acf4 | -5.1967 | -45.0541 | 2025-10-04 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 180.2 |
| 6c536d5a-6627-33d7-9ce7-ee5bd20faf5c | -4.4445 | -43.2397 | 2025-10-04 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 304.9 |
| cb105b7b-053a-3af1-9cac-f87c20809d4c | -4.4443 | -43.263 | 2025-10-04 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 158.8 |
| f558445b-f7b7-3729-a213-49e447127c5f | -15.2399 | -56.8393 | 2025-10-04 02:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 1c72338e-f045-32f3-99d1-425c0f64f45d | -9.9172 | -50.5094 | 2025-10-04 02:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| ab7dcab7-9f6b-388c-b078-4dbe12943660 | -5.1965 | -45.0768 | 2025-10-04 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 233.3 |
| 6a1260f1-c31c-3ca6-9974-d98ef18d3229 | -5.1779 | -45.078 | 2025-10-04 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| bf9dc302-2669-3067-9ab0-933feeba062e | -5.2152 | -45.0756 | 2025-10-04 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 6dfa20c5-99e7-3584-9817-285808349b5d | -9.3379 | -45.7947 | 2025-10-04 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 6355c3b8-b113-305b-a274-690ad36e93e1 | -6.2692 | -42.4483 | 2025-10-04 02:50:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 125.6 |
| c370e2d9-8988-3609-bf58-119de3681656 | -4.6133 | -43.1594 | 2025-10-04 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 19bbcd01-1465-3162-82c8-1a7af639e51b | -15.0374 | -49.4549 | 2025-10-04 02:50:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 47c771b9-c5da-3d77-a054-0a80411e902d | -5.178 | -45.0553 | 2025-10-04 02:50:00 | GOES-19 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| f1901233-f479-3364-891e-86bbfe02cf6d | -4.954 | -45.0694 | 2025-10-04 02:50:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 1843d5f7-bf18-3da5-ab90-59553df092a0 | -6.8774 | -47.2334 | 2025-10-04 02:50:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 20a17860-d388-3a95-9c43-189bb18ac01b | -12.0314 | -45.1901 | 2025-10-04 02:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 8519bae7-9e19-3c69-989b-2ce8189e7234 | -11.9147 | -46.3726 | 2025-10-04 02:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 122.4 |
| f6c5a2b7-1806-3816-bffa-6a580f304ff7 | -20.1557 | -46.4169 | 2025-10-04 03:00:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 64.2 |
| afa7907f-a0e0-38b4-a85f-a27aea304338 | -5.2152 | -45.0756 | 2025-10-04 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| eca86c4d-b5a2-3986-8714-215ba014d635 | -12.031 | -45.2132 | 2025-10-04 03:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 287d8e30-2a86-30c7-87dc-d81e1d244d6e | -17.7044 | -47.0821 | 2025-10-04 03:00:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 668318eb-8f2d-306d-8e1e-667829b6b048 | -4.6133 | -43.1594 | 2025-10-04 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 19367d6e-fcf0-31cf-8e57-b24a11cdff74 | -11.9339 | -46.3699 | 2025-10-04 03:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 1d0e4937-f2cf-356a-9ad4-fb61b8430342 | -15.0374 | -49.4549 | 2025-10-04 03:00:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 76.2 |
| fdd9b00a-0393-3b2d-b2ba-4bdf39145321 | -6.8774 | -47.2334 | 2025-10-04 03:00:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 0e0390ae-b8a6-3d5f-832c-2001e6daf630 | -5.1967 | -45.0541 | 2025-10-04 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 205.9 |
| 2d6fea3c-919c-3fe6-b2f5-ccd2bf8ec702 | -4.954 | -45.0694 | 2025-10-04 03:00:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| c551acfb-e665-3ddf-bd01-4487c1d1d5ab | -6.0809 | -42.4881 | 2025-10-04 03:00:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| 18468dd6-de05-3c02-ab12-59ed09fd3542 | -5.1965 | -45.0768 | 2025-10-04 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 249.6 |
| 8520d8da-e30e-327f-8f14-8773c7f9cd1b | -9.3276 | -54.5215 | 2025-10-04 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| adb61781-6337-3ecb-8005-1494b1f34ebf | -4.4443 | -43.263 | 2025-10-04 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 7a65bd06-9fda-35e1-910c-54f8ca492fd5 | -5.2154 | -45.0529 | 2025-10-04 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 0a7af5d4-1ffb-31d5-967b-917fc75a6f6f | -9.3569 | -45.7925 | 2025-10-04 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 7ebd15b7-a075-3306-8732-3435c51f7cdb | -4.632 | -43.1583 | 2025-10-04 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| f83fa812-3de3-376d-82f9-0cb0aaae24e2 | -6.0618 | -42.5133 | 2025-10-04 03:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 111.1 |
| ec140545-41e8-357e-b01b-3c4b8a22bf82 | -9.3464 | -54.5201 | 2025-10-04 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| cfe3cbbc-1207-31e2-934e-26f73ebedebf | -12.0502 | -45.2103 | 2025-10-04 03:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 88e2629c-8ccf-3bb8-9474-3e4e38d02347 | -14.6725 | -48.2709 | 2025-10-04 03:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 8b45487b-565e-33a7-8b22-2b09f0e8ed61 | -11.9147 | -46.3726 | 2025-10-04 03:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| a3f10a18-556c-387c-b1e5-5da6d507a01a | -12.0507 | -45.1872 | 2025-10-04 03:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 1fe5c2e4-76e9-38cf-a57a-82a67c555456 | -4.4445 | -43.2397 | 2025-10-04 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 323.0 |
| 4c32dbed-bbd9-36e4-a061-7a03655f4f7b | -9.3379 | -45.7947 | 2025-10-04 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 38299bc6-b3c3-32d7-bd40-acca38950e63 | -6.2692 | -42.4483 | 2025-10-04 03:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 73.0 |
| c658cec5-0d2f-397b-b2d7-d8ecd9723f13 | -11.9143 | -46.3953 | 2025-10-04 03:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 3f466712-371a-3a05-8972-a4b52cbb8b29 | -10.3343 | -50.3402 | 2025-10-04 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| dcf9b741-8806-3338-bd5e-f074b9d5cd8e | -4.6135 | -43.1361 | 2025-10-04 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| bdefa000-3cb8-3870-b9c2-dd5e895d1837 | -4.4258 | -43.2408 | 2025-10-04 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 6fe55244-f2dd-396a-9673-0491b7aa1c98 | -3.8572 | -41.5719 | 2025-10-04 03:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 56.2 |
| a0632c22-3f29-39e1-8114-979955a29fab | -2.9013 | -50.7351 | 2025-10-04 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 7e63a0f7-6639-343a-8892-0db3a1f85902 | -4.4446 | -43.2164 | 2025-10-04 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 0db5c797-e5d5-3c98-8ee3-eb05831bd886 | -5.178 | -45.0553 | 2025-10-04 03:00:00 | GOES-19 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 32cbc5cb-d3b0-3501-bd85-2ac4c7a9c7c7 | -12.0314 | -45.1901 | 2025-10-04 03:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 704956c1-fa14-3c98-b474-c69fc7e26817 | -10.3154 | -50.3421 | 2025-10-04 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| b5519df2-49d3-37b4-93bb-dd8f8f476f07 | -6.0806 | -42.5118 | 2025-10-04 03:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 217.7 |
| 1b7e3f43-9e7a-37ee-b40f-f63ff7484451 | -5.1779 | -45.078 | 2025-10-04 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 5b92cd04-0882-33e4-af0d-81c7af55dcc9 | -14.672 | -48.2933 | 2025-10-04 03:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 790fffd8-5e9d-318a-ba46-a7ae6a1543dd | -11.9147 | -46.3726 | 2025-10-04 03:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 918c5a42-e904-3c44-b6b0-65277b928b88 | -4.4445 | -43.2397 | 2025-10-04 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 216.2 |
| eb7957f3-b05f-3ebd-942d-c1a10bfc00cf | -14.6526 | -48.2964 | 2025-10-04 03:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 86cdb844-502c-376e-96f8-b9efdb4ece42 | -12.0502 | -45.2103 | 2025-10-04 03:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 94150a11-0d0a-323c-8565-b26b18574b66 | -4.4446 | -43.2164 | 2025-10-04 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 8eec7ade-5792-3cc7-9f85-55fd9fd75e5a | -14.2515 | -46.076 | 2025-10-04 03:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 6af083c1-b951-3bb9-830a-12483d53f519 | -6.8774 | -47.2334 | 2025-10-04 03:10:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 57fe0615-6db9-33f5-814b-1d3d5b4c7eec | -6.0809 | -42.4881 | 2025-10-04 03:10:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| a43ee5a8-5e43-371c-b519-ed2f3d6f24d4 | -6.0618 | -42.5133 | 2025-10-04 03:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 150.7 |
| 70f34d1a-792f-331c-9260-9483edf8c4d7 | -12.0507 | -45.1872 | 2025-10-04 03:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| d9d8d970-0e59-3573-9a5f-00bad953f3d7 | -5.1779 | -45.078 | 2025-10-04 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| a31f11c7-6e6f-3180-9de9-fc22a714c0bb | -9.3464 | -54.5201 | 2025-10-04 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 09ead586-6c7f-3dc4-a161-780814b61e79 | -21.6888 | -50.0559 | 2025-10-04 03:10:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.4 |
| 3a224ae8-a0fc-300e-8f05-e60b4aa41ec9 | -10.3343 | -50.3402 | 2025-10-04 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 262c7ad7-99af-3b87-8937-4055f25dc0d8 | -11.9143 | -46.3953 | 2025-10-04 03:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 0136e058-6343-30e7-9922-0e5ddd9e8651 | -14.2321 | -46.0794 | 2025-10-04 03:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 5b652009-1365-3bfc-b5bd-5622ade6466a | -6.0806 | -42.5118 | 2025-10-04 03:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 226.5 |
| d4870e5d-b546-313c-8c55-d69ac8d9b838 | -14.2316 | -46.1024 | 2025-10-04 03:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 998e3404-62e5-3abb-a8e0-8e25fbda673f | -8.6322 | -54.9949 | 2025-10-04 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| febfc50d-7d0f-3562-8619-69121df54d1c | -15.2205 | -56.8414 | 2025-10-04 03:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| f56b6d6a-0eea-34d2-a9f9-684e6aebeba5 | -4.6135 | -43.1361 | 2025-10-04 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| c9d5650f-ec88-3144-9f32-6d180bb270e6 | -14.251 | -46.0991 | 2025-10-04 03:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| dfd4649f-a28f-3e6f-8afb-4ade88ae0043 | -2.9013 | -50.7351 | 2025-10-04 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 0f2befd5-3f75-3d1c-b6d1-530d27f33a7f | -5.178 | -45.0553 | 2025-10-04 03:10:00 | GOES-19 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 003fde1e-0601-3d87-b088-2eb8e488a9a0 | -11.9339 | -46.3699 | 2025-10-04 03:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |


[Clique aqui para ver as próximas entradas](README9.md)
