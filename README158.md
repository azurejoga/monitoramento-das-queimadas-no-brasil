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

## Dados Diários - Página 158

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 906e66da-ca4b-3fe8-b158-6bb60de6482a | -12.4813 | -50.2261 | 2025-10-01 14:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 642.9 |
| 67fab18f-907c-39a5-a8d6-d48f5ee362a7 | -13.7691 | -47.9435 | 2025-10-01 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 090a025f-7b98-3bdf-9c27-9115174093a5 | -8.5404 | -44.6975 | 2025-10-01 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 7a1daae2-2040-398e-9e0a-fda518d84fce | -11.8482 | -48.0595 | 2025-10-01 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 53d4245d-f424-3a0b-bd59-9013bcb695d3 | -8.8929 | -46.6072 | 2025-10-01 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 87be128e-62d1-3a76-b6fd-042ba09804c0 | -13.1431 | -47.4113 | 2025-10-01 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 128.5 |
| bef6fdf2-5677-3158-a3c4-05341aaac5f7 | -11.7729 | -46.8435 | 2025-10-01 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 72e391aa-be64-3ae4-8f78-8b891315cda9 | -12.2816 | -44.1275 | 2025-10-01 14:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 215.7 |
| 5cfb8cf8-df30-3abd-b9fb-d5beaf6e4218 | -14.8212 | -45.8143 | 2025-10-01 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| c6856931-8018-3255-91b4-fda736887d4e | -6.7165 | -44.5987 | 2025-10-01 14:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 7cd7a0de-8a39-3998-b6ab-ffadbafda562 | -15.9388 | -43.2979 | 2025-10-01 14:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 211.6 |
| f331a013-3bed-3b89-8a4f-4df83c2aa486 | -13.2973 | -50.6605 | 2025-10-01 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 9ab5d5a8-bdd9-37d8-952d-bc49f16b4781 | -16.0221 | -50.8989 | 2025-10-01 14:00:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 7e8baec9-6adf-376c-8fba-9abdcd2c8693 | -12.8967 | -45.1711 | 2025-10-01 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 151.5 |
| ac2ac6ca-b4b2-3fd6-bd38-6e3ee51d0b6c | -8.8926 | -46.6296 | 2025-10-01 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 165.1 |
| a78f0eaf-ae9b-3dc3-ab26-2ac7e6b719f7 | -13.7876 | -47.9853 | 2025-10-01 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 82.7 |
| d1174a88-d39d-30c7-a461-cebf82c40abb | -5.1512 | -43.7289 | 2025-10-01 14:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 6c50ca02-b762-3cef-972a-d8891511bfb2 | -10.9182 | -44.3092 | 2025-10-01 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| b7662d1f-5096-366f-a3fa-2ebfc3745f6f | -9.4458 | -47.5923 | 2025-10-01 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 109.9 |
| ff058ee4-d1a8-3498-9c7b-320c5433518a | -6.0997 | -42.4865 | 2025-10-01 14:00:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| b72af0cb-f6d6-30d0-8c28-e4eb7991e738 | -5.4967 | -42.7471 | 2025-10-01 14:00:00 | GOES-19 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 99.1 |
| d2267b84-83d5-384d-8173-9ea7508bcc72 | -8.8797 | -47.6502 | 2025-10-01 14:00:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| ca26e3f3-67d5-388d-bda3-f13d0dd103a4 | -6.214 | -44.2272 | 2025-10-01 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 8039fbd0-46e8-3ed2-8960-bc0fe5cc8883 | -13.3607 | -48.1382 | 2025-10-01 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 222.5 |
| 6cfae7fd-8ff8-3cae-a14b-5baaffeba358 | -11.46 | -45.0202 | 2025-10-01 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 89a15a64-6b55-3e29-be6a-44288c8e3b34 | -8.8893 | -51.6758 | 2025-10-01 14:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 131.1 |
| 1d05f3d6-fad8-3728-8cfd-396ad7d906ba | -8.9115 | -46.6276 | 2025-10-01 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 296.4 |
| 2541fedf-3852-345b-aa10-57590ff5f77b | -8.8609 | -47.6521 | 2025-10-01 14:00:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| e80212ec-af36-35c7-b84f-38f711108afd | -12.2536 | -47.806 | 2025-10-01 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 270.8 |
| e65dba71-3933-352a-8fab-477f4aaf7be1 | -14.3514 | -45.9437 | 2025-10-01 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 94f320ff-eaf7-3fc0-a228-6674117eae3d | -15.2705 | -51.4871 | 2025-10-01 14:00:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 1f836e71-f5e0-3902-af7e-5b182f06eab9 | -8.5081 | -47.2676 | 2025-10-01 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 0e80d6cd-4c3c-3fd4-8df2-229ddc5d78d7 | -13.3611 | -48.1159 | 2025-10-01 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 191.9 |
| 86a33f07-38ec-35bd-8b09-9c662d05f728 | -11.8246 | -44.9669 | 2025-10-01 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 098f69fb-b319-34d1-a274-ca9e242c7785 | -14.3524 | -45.8974 | 2025-10-01 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| ada981cf-61be-3872-8702-cd37aa1dff17 | -15.3596 | -47.0724 | 2025-10-01 14:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 3fa9b400-e486-3c72-9bfe-30a74c249e9e | -8.163 | -46.2554 | 2025-10-01 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 94af7cde-1f8c-39b6-9af8-b2f2996626e8 | -5.9557 | -45.8588 | 2025-10-01 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 4fbd59a6-67c4-3a77-ba5c-bf2f76008e33 | -14.3519 | -45.9206 | 2025-10-01 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 162.8 |
| dd835a9a-2d78-3b89-882e-2cbc813cd782 | -9.9383 | -43.6483 | 2025-10-01 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 260.4 |
| 8171d97e-b25f-3d12-b0e3-b6367034d18e | -13.6703 | -48.07 | 2025-10-01 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 3989f221-79b4-38e2-8e6b-e6a8fc7f8439 | -13.7868 | -48.03 | 2025-10-01 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 152.1 |
| de297bd1-10e8-352f-9e73-066ab4b8e92a | -9.4644 | -47.6124 | 2025-10-01 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 4688983e-5b9b-306d-bc5e-26522a3e4e4f | -11.4592 | -45.0664 | 2025-10-01 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 46f689ad-4ab6-3095-a9a8-59183c9b45d0 | -6.2718 | -44.0612 | 2025-10-01 14:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 8b17e104-c1dd-310c-a1ae-8b990c4c0424 | -13.3808 | -48.0908 | 2025-10-01 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 211.0 |
| c56fb95d-f995-393b-95c8-f238f929abf9 | -6.0978 | -42.6758 | 2025-10-01 14:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 0d112672-a2a2-3682-82cc-33c8ed847fd8 | -12.282 | -44.1039 | 2025-10-01 14:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 360.6 |
| 41dd1ad6-bad8-3033-9209-f8daec8b1084 | -13.8354 | -47.5076 | 2025-10-01 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 725fdb6c-92a8-3fa8-bb58-39393217ee7a | -12.2627 | -44.107 | 2025-10-01 14:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 287.6 |
| 4d3a8cf3-c28a-3075-85e3-71e26e607cc8 | -9.9959 | -43.6172 | 2025-10-01 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 8874b5a5-70ec-32ac-9d33-f483746937c3 | -16.0421 | -50.874 | 2025-10-01 14:00:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 4ef49248-57db-377b-96ad-764c61d5c86b | -6.7356 | -44.5742 | 2025-10-01 14:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 9b454107-5f2b-345d-9a7b-d63c03bc95f0 | -12.2344 | -47.8086 | 2025-10-01 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| d1764f03-e062-3520-a943-b6377ecd2d07 | -22.0726 | -43.0806 | 2025-10-01 14:00:00 | GOES-19 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 127.8 |
| 7de771a8-dcd0-3e8a-a4d2-1aaf0131e491 | -14.9738 | -46.8668 | 2025-10-01 14:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 640d3f79-76d3-3091-abe5-eb8d259ff5c6 | -7.7944 | -42.5132 | 2025-10-01 14:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 249d0c15-d71c-375a-84e6-83ee0b241a4f | -9.9376 | -43.6953 | 2025-10-01 14:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 325.1 |
| ee0457b2-439a-3414-bf10-010a017624d8 | -9.9387 | -43.6248 | 2025-10-01 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 24ccbd9d-d5d9-384d-8aee-3d4b30ed0551 | -12.8827 | -46.9328 | 2025-10-01 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 18d2425a-f392-39c6-af9f-3e0bce9b2220 | -10.876 | -53.7614 | 2025-10-01 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 86695677-e8a8-3467-a158-569a309cc067 | -6.5546 | -43.9221 | 2025-10-01 14:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 143.0 |
| a4d79dee-b3b1-3c2c-a62f-25f92d38f2ab | -8.9081 | -51.6743 | 2025-10-01 14:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 144.0 |
| c1ead55b-5037-3e52-a86e-8fae735cebb6 | -9.1434 | -47.6457 | 2025-10-01 14:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 69512283-0bb2-3f38-94ea-0097e34e2cb1 | -11.3834 | -45.0312 | 2025-10-01 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 659e38fc-5b59-3607-9265-efe51ccdd2ba | -11.9272 | -47.8941 | 2025-10-01 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| bf98844f-8967-3076-8116-99ba3b68d7bf | -8.6911 | -47.6906 | 2025-10-01 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 8653fe28-b907-3b96-b12a-7daafd531493 | -5.8418 | -43.9566 | 2025-10-01 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 30a629e6-1289-33ca-a77f-f23a16935953 | -12.122 | -43.4215 | 2025-10-01 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 138.2 |
| b466d892-a541-31a1-a00c-841a40a9a8ea | -11.9411 | -47.0675 | 2025-10-01 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 257.9 |
| 978c8b51-0d1b-3aad-8cb7-fd3e1e7d6efa | -12.254 | -47.7837 | 2025-10-01 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| adfdb612-dd13-398a-97c5-32a2ecd297e4 | -9.9394 | -43.5777 | 2025-10-01 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 7415bf9f-bf5c-3a3c-be06-384f239403d8 | -5.8445 | -45.7545 | 2025-10-01 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 3712d645-0ab8-3a80-81e4-8cb0ce68d5b0 | -8.5587 | -44.7414 | 2025-10-01 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 170.3 |
| a9d2c9df-7cb8-3fd9-b51e-f872179417d9 | -11.8438 | -44.964 | 2025-10-01 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| cbf30f43-504b-3204-9905-1a093112ceab | -14.9733 | -46.8896 | 2025-10-01 14:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 53a424aa-ce44-3f2c-b229-0d5b72270cd1 | -8.483 | -47.7983 | 2025-10-01 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 207.3 |
| 87ea03dd-a9dc-3e3a-ae38-949604cae54c | -5.7037 | -42.6605 | 2025-10-01 14:00:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 88.1 |
| 09ab281e-5c40-3e50-8cf2-2b37643d54f9 | -8.2105 | -47.0084 | 2025-10-01 14:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 2c732160-fef0-34fc-8d28-538edef38186 | -7.6272 | -45.4507 | 2025-10-01 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 14fe9749-59e1-38b6-8e85-c80f79611ca6 | -7.1812 | -41.7172 | 2025-10-01 14:00:00 | GOES-19 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 06b9469a-cdc7-3ec5-bdf2-85b9ba7fb57f | -8.6722 | -47.6924 | 2025-10-01 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 90ad5d2c-c192-372e-99f4-633fd595a538 | -7.8165 | -46.9781 | 2025-10-01 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 3fafab76-625a-35fe-9290-dd716ba0e5bd | -6.2813 | -45.022 | 2025-10-01 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 48b43dee-fa1e-3ae5-bda4-2a8c161d7720 | -8.672 | -47.7144 | 2025-10-01 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 4fdda96b-65ee-3004-bc2d-e582acf49c75 | -15.5384 | -45.214 | 2025-10-01 14:00:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 67e835ea-9319-393f-924c-73c7a8f6837f | -5.9555 | -45.8812 | 2025-10-01 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 178.1 |
| 2afcfbfa-47a8-3eae-b63b-30220f420a29 | -9.9585 | -43.5752 | 2025-10-01 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| a424f9e0-1ebd-342f-a01a-6b69cfcd9f40 | -14.3714 | -45.9172 | 2025-10-01 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 32250177-8255-313b-9109-0c671c680095 | -11.1181 | -49.7629 | 2025-10-01 14:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| a7ed4954-cf9c-3ea2-80ad-9edb87e10adc | -13.3615 | -48.0936 | 2025-10-01 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 110.7 |
| c3ecf3fa-af44-3a75-8c16-06380989bde1 | -5.9414 | -43.3221 | 2025-10-01 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 872057ec-826e-3592-a5f6-c221e804a92a | -5.3276 | -42.7832 | 2025-10-01 14:00:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 86.0 |
| 82be3c12-110f-355c-bd84-755d5e56e354 | -14.5942 | -48.3058 | 2025-10-01 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 3ce9eaa2-35f1-3763-add0-9ceae825983d | -11.3486 | -48.3211 | 2025-10-01 14:00:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 175.4 |
| a7972047-7a1d-35f5-b3f3-1bd4b6ef1325 | -15.5379 | -45.2375 | 2025-10-01 14:00:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 107.8 |
| f706b25a-a30d-3841-9606-2c417d5d1272 | -16.0417 | -50.8959 | 2025-10-01 14:00:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 8772111e-fbbe-3b12-af14-1f0ad8bf160e | -11.7797 | -47.5806 | 2025-10-01 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 0367da7b-b558-3c7a-b698-cf8bb27d5fa2 | -5.9368 | -45.8825 | 2025-10-01 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 45f66a42-7117-3a2e-b048-32b9e4f34b14 | -8.3869 | -47.9824 | 2025-10-01 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |


[Clique aqui para ver as próximas entradas](README159.md)
