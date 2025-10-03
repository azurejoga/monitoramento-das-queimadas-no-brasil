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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90e5a32c-60ef-35e7-b223-f2a820821b9a | -9.9563 | -43.7162 | 2025-10-03 13:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 9c2b4ac5-3b8b-373e-ab5b-a6bd1f15e712 | -11.458 | -45.1357 | 2025-10-03 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| b2acad18-2b61-3dbf-9783-0fddaa12055e | -7.5749 | -46.7778 | 2025-10-03 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 26929dea-109c-34db-8424-f3672467d728 | -9.4548 | -45.5545 | 2025-10-03 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 2e2c5a8e-88e0-3de3-9ac8-43527acc1740 | -9.8769 | -47.8324 | 2025-10-03 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 303f585a-ef4e-3ddc-b1ca-d082915c09ab | -14.0032 | -44.961 | 2025-10-03 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 27363923-7b08-3c3c-b72e-664ba5eae034 | -16.0583 | -51.0454 | 2025-10-03 13:50:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 92.9 |
| b11712f6-b593-30b6-99a3-1414c9d878fa | -12.7435 | -50.5591 | 2025-10-03 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 54d52099-7bc1-3dd3-841f-7628afdc58b2 | -7.7682 | -46.2703 | 2025-10-03 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| ec2e133d-1589-3e13-bf3b-5d25c67f725c | -11.9155 | -46.3272 | 2025-10-03 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 323.6 |
| b866c8d0-64c1-3b7d-9418-99e6e8d52a73 | -13.7954 | -47.5812 | 2025-10-03 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 37723df1-c5e0-3e04-9e73-854fd8036294 | -8.5959 | -44.7833 | 2025-10-03 13:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 90a575f8-034d-3797-8768-4c579ece3806 | -9.0989 | -46.7195 | 2025-10-03 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 58b61f7a-53e6-3fb0-b671-381dc76846a6 | -11.9159 | -46.3044 | 2025-10-03 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 58e8a464-f705-3b52-ae99-afdd0be678e6 | -7.646 | -45.4489 | 2025-10-03 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| e659b8c7-f7c5-34f4-93f3-13663cbcf136 | -7.7496 | -46.2496 | 2025-10-03 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 125.2 |
| ec3c2986-0215-3e1a-9d19-9e080458fee4 | -7.2913 | -45.2548 | 2025-10-03 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 147.0 |
| abec21b0-0367-393f-b836-b55df622d5cc | -11.8046 | -45.0161 | 2025-10-03 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| ce40213a-04d6-3f74-93df-920639afff36 | -7.7687 | -46.2255 | 2025-10-03 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 118.7 |
| ba40d543-c7ce-397e-9f7e-8c85cad0084e | -8.1699 | -44.1608 | 2025-10-03 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 132.8 |
| ecc383bc-3cbb-31bd-99e9-79fdc287687c | -14.7341 | -48.1045 | 2025-10-03 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 308944db-2f0b-3f99-b47f-303465a0bbeb | -14.6497 | -44.7499 | 2025-10-03 13:50:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 57da156f-ef07-3154-b6cd-21e9e921d393 | -11.5687 | -47.6526 | 2025-10-03 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| b0702958-4a5b-34da-858c-ae2247ef37a7 | -7.3031 | -44.2013 | 2025-10-03 13:50:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 40acd6dd-d480-3f8f-aecf-ffb5243c13d4 | -10.127 | -50.3184 | 2025-10-03 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 433ad1cf-be93-3a52-8805-060dde97afa6 | -8.9948 | -47.4845 | 2025-10-03 13:50:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 9d349bee-e111-36e1-a36e-93a1fe035507 | -13.38 | -48.1354 | 2025-10-03 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| b194c7a2-54f4-30db-b84b-82f185823e3c | -13.3418 | -48.1188 | 2025-10-03 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 196.2 |
| 9cce12f3-1bf5-3628-8d2b-d43586e303d1 | -10.9554 | -46.7044 | 2025-10-03 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 3a8fdc94-281d-372d-8568-e31a14fd8b98 | -13.6724 | -51.1911 | 2025-10-03 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| a3fa9532-85bd-395e-ab55-9aa41d22093d | -11.9085 | -46.7349 | 2025-10-03 13:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| a0026c49-411e-3fa5-ae40-fe1347ddbff8 | -9.3389 | -45.7266 | 2025-10-03 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.9 |
| e1ee07da-4979-3258-92cf-e0aebcdea9be | -11.8626 | -44.9844 | 2025-10-03 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| a1f30dd7-454d-347d-8f79-e43b1a5bc4cc | -9.3386 | -45.7493 | 2025-10-03 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 195.4 |
| 7ff6f952-2294-3550-847a-d27711004f31 | -14.0227 | -44.9576 | 2025-10-03 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 08174eb9-28cd-33d1-a8e3-ddfa7a34436a | -10.345 | -48.176 | 2025-10-03 13:50:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 56e78302-d242-3cb8-b091-63756e78c3ca | -7.7494 | -46.272 | 2025-10-03 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 0a391793-376e-3507-806a-da05c54c7946 | -12.7627 | -50.5567 | 2025-10-03 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 17e47fec-973c-32d1-9d68-6faefab43823 | -7.2845 | -44.18 | 2025-10-03 13:50:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| c08a85bf-4630-3546-8749-20d9c92724ae | -9.9369 | -43.7422 | 2025-10-03 13:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 110.0 |
| 404678b9-7aa9-3fc2-a185-a43f225b2530 | -11.8818 | -44.9815 | 2025-10-03 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 004f1997-2c26-3543-8950-41cd757076e9 | -11.863 | -44.9612 | 2025-10-03 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 9dbbda55-fdcd-37a5-964e-cb4e3302f13f | -12.5305 | -47.2988 | 2025-10-03 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 197599d0-991f-3e6d-ba78-7181e5c8ef17 | -12.6131 | -46.9725 | 2025-10-03 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 131.4 |
| df9f3f91-b354-3b4c-bddf-e5e1cb1513c4 | -12.1088 | -45.1554 | 2025-10-03 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 37441865-d66f-3415-bd12-b40471192d4b | -8.6908 | -47.7126 | 2025-10-03 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| d9201713-e8b2-3014-a8b6-8fa3bec6e1ff | -15.7905 | -43.7155 | 2025-10-03 13:50:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 629.8 |
| 6baaa472-e661-353a-bc8a-164d053d767c | -13.8051 | -51.3022 | 2025-10-03 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 70a3fdb6-24ac-3d72-af44-c1f92ad0da17 | -6.679 | -42.8136 | 2025-10-03 13:50:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 78.5 |
| 4b55497f-8dbd-32d2-9402-e3faf1d52b30 | -9.9035 | -45.9553 | 2025-10-03 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 467c5011-4a39-3460-81fa-ef80013805c5 | -11.8622 | -45.0075 | 2025-10-03 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.8 |
| e2cbe29f-6661-3ff5-b88e-2da6c9131071 | -7.3101 | -45.2531 | 2025-10-03 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 7068f62d-129e-3afd-8025-3446125cf285 | -13.1152 | -47.8848 | 2025-10-03 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 3e582017-5943-33ae-8f07-a6ba483cf275 | -10.948 | -51.0846 | 2025-10-03 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 8a504c5c-269a-33a3-a23f-7fd6b7d785bb | -10.8524 | -47.2094 | 2025-10-03 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 00fd7e90-01bb-3c87-82da-554d5efc8aae | -9.3547 | -45.951 | 2025-10-03 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 17174436-b21f-3a6f-8f28-2ec8d9f6bfb4 | -11.8814 | -45.0047 | 2025-10-03 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 80406cdc-683d-3d29-90d8-9486720f0bb3 | -8.8543 | -46.6781 | 2025-10-03 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| b26fd192-122e-3944-b675-06613a7085e7 | -13.1534 | -47.9015 | 2025-10-03 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 1843bcaa-5752-36cf-b3ab-e8ec5afb3d79 | -11.1275 | -47.8634 | 2025-10-03 13:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| e22d5dec-2924-374c-92f6-8e695b05b68a | -10.967 | -51.0826 | 2025-10-03 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 49756887-bf80-3f8e-a738-fd68a4c3ea09 | -7.7684 | -46.2479 | 2025-10-03 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 179.8 |
| bcc8e152-087e-3dfc-b133-1f013977d283 | -14.6344 | -48.2324 | 2025-10-03 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| c919ebe9-3781-3549-bfcb-76289573fb5a | -6.0806 | -42.5118 | 2025-10-03 13:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 88.2 |
| 0eabdc68-da43-3ea9-b111-d95e3929089e | -13.1341 | -47.9043 | 2025-10-03 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| bc15e547-7945-34fb-8464-efcf812891f2 | -15.7707 | -43.7197 | 2025-10-03 13:50:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 185.9 |
| 42563f2b-7999-323d-9fce-e2692eef721d | -18.9673 | -48.4968 | 2025-10-03 13:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 480.4 |
| 5be31aca-4d02-36ff-9e45-fcf347adeaf7 | -13.1973 | -50.9095 | 2025-10-03 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 195239e7-5268-3b55-8580-e5ad24c2ca72 | -6.0809 | -42.4881 | 2025-10-03 13:50:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| a48cfa62-2c8d-3318-9ec8-6dc0fcd63cfa | -13.1345 | -47.882 | 2025-10-03 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 574f90f2-f86e-3a1d-95a7-f5b0cc679b7b | -7.3033 | -44.1782 | 2025-10-03 13:50:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 6cb9f6d6-b7c4-3014-9d90-8defe499c847 | -6.6787 | -42.8372 | 2025-10-03 13:50:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 286c165c-76ec-3ac8-b5d4-dc5f259a915a | -18.9667 | -48.5198 | 2025-10-03 13:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 164.0 |
| a4211512-5102-32ed-ad43-ea419519fe12 | -9.8772 | -47.8103 | 2025-10-03 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 134.2 |
| ef55c5a9-5d75-3a8b-808f-21e16ecb79e3 | -7.7499 | -46.2272 | 2025-10-03 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 1e01b6d8-3015-3eea-94f8-677e6f842ab4 | -9.9182 | -43.7212 | 2025-10-03 13:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 171.0 |
| e90e5c82-db17-3011-85c6-150b8c45e6e8 | -13.155 | -47.8121 | 2025-10-03 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 78fd293d-6f0d-3e96-b68e-be581434cf51 | -8.1702 | -44.1377 | 2025-10-03 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 120.9 |
| d77df81f-1522-3d18-bec8-26a3e1d5b3b6 | -12.763 | -50.5352 | 2025-10-03 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 42b5c46f-235c-3718-a173-6acc3fcc8473 | -6.6978 | -42.8118 | 2025-10-03 13:50:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| afc86747-8a8a-3d36-9f45-67c2b17b3214 | -6.0621 | -42.4897 | 2025-10-03 13:50:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| aa6c11b4-f86a-3d57-b435-095f0b6afd32 | -13.8055 | -51.2807 | 2025-10-03 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 0b384776-31e9-357b-99df-bfae3b5c3702 | -9.8995 | -43.7003 | 2025-10-03 13:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 96.2 |
| 8db97067-172d-3176-86b8-a51a4072df9d | -14.0037 | -44.9376 | 2025-10-03 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| d7e62c70-d125-39d0-ab4c-35fbe14304b5 | -11.1271 | -47.8856 | 2025-10-03 13:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 145.0 |
| ae1ced5e-1fa9-393e-95d0-5ad07b6bc4d0 | -13.2165 | -50.9071 | 2025-10-03 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| a3afea76-07eb-32c3-8769-946d27f6307e | -13.7673 | -51.2643 | 2025-10-03 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 1412bfe8-4b10-3ecc-880f-e05348d155e4 | -15.8097 | -43.7355 | 2025-10-03 13:50:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 52fcf9d9-d60e-3692-b848-805ed6ace835 | -9.9394 | -43.5777 | 2025-10-03 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 7298fd37-5144-3600-bb03-18addcaa262c | -13.7862 | -51.2833 | 2025-10-03 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 6ad33e05-8461-3641-8db7-a181203a9a6d | -14.2939 | -45.9076 | 2025-10-03 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 6d5306d1-925e-30e7-9e1a-64f219050085 | -9.9031 | -45.978 | 2025-10-03 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| b4fd408d-0ebb-3135-bbd1-ca03cfcbb65e | -6.6416 | -42.7934 | 2025-10-03 13:50:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| 6d0a75a4-0db0-39a5-9caa-13b341894879 | -11.8104 | -51.7746 | 2025-10-03 13:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| f9c3e279-94fd-3714-b9d2-b8785d74316f | -14.8063 | -51.424 | 2025-10-03 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 0a11dd6d-c75a-36b8-a39b-785890e8c58a | -11.8104 | -51.7746 | 2025-10-03 14:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| ec52f7cc-23b1-3407-a0b8-5046ae007f26 | -9.3386 | -45.7493 | 2025-10-03 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| fc957ee6-e4c6-33c3-809f-8fbdb0666df8 | -9.9365 | -43.7657 | 2025-10-03 14:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 124.9 |
| fb1e6eaf-cf23-374d-9136-1ba55d5ae95b | -5.7133 | -43.6655 | 2025-10-03 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 2a1dbf6c-2340-3ec6-845f-814d400221a8 | -14.8393 | -51.7409 | 2025-10-03 14:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |


[Clique aqui para ver as próximas entradas](README151.md)
