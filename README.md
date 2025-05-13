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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58e97f54-7671-3877-8478-0be464233ad7 | -13.971 | -56.8077 | 2025-05-13 00:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 3281900a-8225-35dc-9c53-1f0a6dd39848 | -13.9905 | -56.7855 | 2025-05-13 00:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| d191a8e9-14b6-3566-a82a-93ee90b51c44 | -8.0889 | -43.1196 | 2025-05-13 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 75ae963d-bd84-393f-ad6c-1e9598fb5cfe | -13.9713 | -56.7874 | 2025-05-13 00:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| ce6be27f-be9c-3bfb-880c-fb68729f2a94 | -8.07 | -43.1216 | 2025-05-13 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.1 |
| 31a085af-9456-3252-aad4-5c5662fdf77b | -12.1548 | -47.9968 | 2025-05-13 00:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 1a032889-daa3-38cf-8599-0e40177d44eb | -13.9902 | -56.8058 | 2025-05-13 00:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 118.0 |
| f03992b3-3521-37fd-ab55-3f83696199b3 | -12.1544 | -48.019 | 2025-05-13 00:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 6a3ca6b8-9297-3b0a-a959-a41ccada95c9 | -8.0889 | -43.1196 | 2025-05-13 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 8a4a9d64-8d1e-3212-a4c5-c32dd3fd0207 | -8.07 | -43.1216 | 2025-05-13 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.5 |
| 9f80e434-16f3-3d22-a431-da51f04a424d | -13.971 | -56.8077 | 2025-05-13 00:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 3847e058-86b4-31ca-92a4-b651ed50b0b2 | -13.9902 | -56.8058 | 2025-05-13 00:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 024cba38-91a9-3103-b116-4df68495294f | -12.1544 | -48.019 | 2025-05-13 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| ded35e90-b450-301b-99a8-223d09c885a0 | -13.9905 | -56.7855 | 2025-05-13 00:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 068bc119-1c66-30b2-b863-564793ad14ca | -14.19403 | -45.48037 | 2025-05-13 00:13:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| d80dad21-6888-3842-8cbf-9f86aa393545 | -11.5865 | -47.60981 | 2025-05-13 00:13:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| e9fb8970-7316-3377-8b69-44a9e17af0e3 | -11.7974 | -47.4171 | 2025-05-13 00:13:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| b36e58a8-ec30-365f-a11a-e30d0fe976b9 | -11.5858 | -47.62503 | 2025-05-13 00:13:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 8e79a754-bb58-38c4-a9f7-a88889f58d74 | -10.65545 | -44.40907 | 2025-05-13 00:13:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0acab81f-bc5b-3fec-9e92-b21223d2ac3b | -10.53946 | -42.44675 | 2025-05-13 00:13:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 24.8 |
| fb9f36f9-b137-3a17-b919-1dd346a51d95 | -10.66559 | -44.41353 | 2025-05-13 00:13:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1ddc8c6b-611b-3289-ac6f-b4202ba74565 | -14.1806 | -45.4657 | 2025-05-13 00:13:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| bf97556e-7146-358b-8739-f68d0cffd385 | -11.80108 | -44.27655 | 2025-05-13 00:13:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| ea3b7745-33b3-34df-9e1f-2fcc39d4ed48 | -14.18367 | -45.47086 | 2025-05-13 00:13:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 0c978201-f1ff-396f-944e-629828a36a98 | -12.19665 | -46.71938 | 2025-05-13 00:13:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 5f352ca2-6707-3dc4-8108-8263a1fffb5e | -12.15553 | -48.03038 | 2025-05-13 00:13:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 42.1 |
| cff158f3-8be2-3352-8675-4df72c8bceed | -12.18425 | -46.72086 | 2025-05-13 00:13:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 55402bdc-df0d-3906-be15-05a4a4aaaad1 | -12.15281 | -48.00673 | 2025-05-13 00:13:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 123.2 |
| e638ca80-b022-33c3-8429-11e2d97ee7b1 | -14.18565 | -45.48692 | 2025-05-13 00:13:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 9c26cb6d-baed-30ef-aa25-0b1090b85160 | -14.18245 | -45.48178 | 2025-05-13 00:13:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 30b8c01d-9e5e-3ae1-8ab9-5778f16f7850 | -10.53819 | -42.43736 | 2025-05-13 00:13:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 7f506c91-7d82-36c8-8b91-bdcc35a99271 | -9.22203 | -36.87497 | 2025-05-13 00:13:00 | TERRA_M-M | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 3eb6ad62-1996-38de-a6bf-b74aba822351 | -11.77892 | -48.71145 | 2025-05-13 00:13:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| ae8138d7-a9c6-3f8f-a82f-4354bfbd3205 | -11.619 | -48.112999 | 2025-05-13 00:14:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc3cb387-1a95-387c-80ee-5d95f8333601 | -6.1787 | -48.066002 | 2025-05-13 00:14:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f3f37cda-4a8c-3da9-89dc-3b0d51c4064f | -13.5651 | -52.875999 | 2025-05-13 00:14:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7b463470-0be4-32f9-aade-aba061386b8c | -10.6599 | -44.408199 | 2025-05-13 00:14:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c681ef69-6e4a-34fa-b505-b40cbf2558f4 | -13.5498 | -52.849098 | 2025-05-13 00:14:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 11b35000-d602-3a40-9204-10efd8589be4 | -14.1886 | -45.471699 | 2025-05-13 00:14:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 14f64b84-7056-3c85-83d6-3ac068c45bd6 | -7.5885 | -45.860699 | 2025-05-13 00:14:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f39cf10-3bde-3af8-88cc-0a660495c3ef | -14.1854 | -45.4576 | 2025-05-13 00:14:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 89bfc6ee-400d-3cdc-9c54-37c5a440a2c1 | -7.5901 | -45.867802 | 2025-05-13 00:14:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e7d3f6d3-918b-3249-b06c-c8341eb51b0c | -13.5595 | -52.847198 | 2025-05-13 00:14:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 884f436c-45fe-39e8-9509-2abb8b359aab | -6.187 | -48.0569 | 2025-05-13 00:14:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a12d61f-dcf6-3f85-ba8f-15041bf64bdc | -13.9809 | -56.794601 | 2025-05-13 00:14:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 41dae13a-ff7f-3288-85ca-90a56f27cdb3 | -14.1999 | -45.476501 | 2025-05-13 00:14:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7e18fd91-ee5d-342b-8b0e-bcb6243d6155 | -8.404 | -43.842201 | 2025-05-13 00:14:00 | METOP-B | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4911ed78-790b-3f81-a16a-08ac70318b8e | -11.6174 | -48.105598 | 2025-05-13 00:14:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e75062c2-0837-3002-abd6-f76ecdef2ac8 | -13.4033 | -47.625401 | 2025-05-13 00:14:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b96543b1-1b7c-337c-b9e3-1fe862737b5a | -13.976 | -56.767502 | 2025-05-13 00:14:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7445da62-220f-3f30-bac3-3e1443433b61 | -13.5526 | -52.863499 | 2025-05-13 00:14:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2bd2f9db-01c8-33df-9b70-1f9f4e269796 | -8.0721 | -43.126499 | 2025-05-13 00:14:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3761d7b1-b4c5-39b2-84ea-50eabe37da4b | -11.6288 | -48.110901 | 2025-05-13 00:14:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 81f03f5c-0cd3-3150-ba88-f1c2dbfbc8df | -11.8033 | -44.2663 | 2025-05-13 00:14:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eda01870-4efb-3196-aba0-3c6b183b099a | -12.1873 | -46.710499 | 2025-05-13 00:14:00 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2aa67642-ecee-38fa-bfaa-7553644a42d4 | -12.1971 | -46.708302 | 2025-05-13 00:14:00 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dba26596-e83f-30cf-8b04-9d91ee7f66ca | -11.5812 | -47.6068 | 2025-05-13 00:14:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39b9e080-669a-3dab-ad43-a395c3e8fd99 | -11.8051 | -44.2738 | 2025-05-13 00:14:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 20ba66fd-ecfb-3154-9594-f87433545806 | -12.1858 | -46.703499 | 2025-05-13 00:14:00 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46828ce5-0a8a-3c51-96a1-61baa5bce1a3 | -10.5397 | -42.431599 | 2025-05-13 00:14:00 | METOP-B | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5ea6d9c7-a16c-3f22-ac95-f904172e9319 | -11.795 | -47.408401 | 2025-05-13 00:14:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 058557ae-9d44-34e4-8e52-be00394c2007 | -13.5623 | -52.861599 | 2025-05-13 00:14:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 45f6918d-01ae-324d-bbff-19d6ffb10bbf | -12.1613 | -48.009201 | 2025-05-13 00:14:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 29c773c5-4895-3f6f-8095-608f73ae8ba1 | -14.187 | -45.4646 | 2025-05-13 00:14:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f550d922-ade3-3051-8e2d-f4ebab031ea1 | -6.1885 | -48.063801 | 2025-05-13 00:14:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a990ee1-7652-3b85-aafd-be0a2643333a | -13.9712 | -56.740398 | 2025-05-13 00:14:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7400e22c-7379-3b41-8127-78b926ad4687 | -13.5749 | -52.8741 | 2025-05-13 00:14:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b846c506-c55b-3c20-952a-a98c648cd074 | -13.9663 | -56.769199 | 2025-05-13 00:14:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3afce64c-89ac-30ba-8480-f7ae9cc9f623 | -13.0475 | -53.707802 | 2025-05-13 00:14:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b4b0cdd4-9b47-3fd7-b685-f02c4cccd02a | -12.1597 | -48.001701 | 2025-05-13 00:14:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8961d370-6a0e-3dee-bbf2-ca89f9c8d289 | -8.0796 | -43.115101 | 2025-05-13 00:14:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 094466cd-1223-358d-a750-9d299287ee31 | -11.6145 | -47.997299 | 2025-05-13 00:14:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ab8f979-8a53-39fd-a723-6590f8c81ec9 | -11.7843 | -48.692402 | 2025-05-13 00:14:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3da5c508-c793-34d3-9191-45589e0ca557 | -8.0818 | -43.124199 | 2025-05-13 00:14:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8696206c-bf05-31c8-87b6-5092dd76afef | -13.9857 | -56.765701 | 2025-05-13 00:14:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6b9ab734-4748-3c46-a16d-a06cbd222384 | -12.8435 | -47.409801 | 2025-05-13 00:14:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| adc748f6-4d8b-38ec-a55e-8c49427f1bd2 | -18.2717 | -50.284302 | 2025-05-13 00:14:00 | METOP-B | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b4858b3a-ca91-396a-a554-4e722a996958 | -14.1901 | -45.478699 | 2025-05-13 00:14:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fd3eb913-d337-342e-ae6b-b288d2f1eea9 | -8.0742 | -43.135502 | 2025-05-13 00:14:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 098fb228-ac85-371e-b615-8e7273843217 | -13.0689 | -52.001801 | 2025-05-13 00:14:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ed52721f-b54f-3b51-8cc0-e2a50459d01d | -11.7923 | -47.3489 | 2025-05-13 00:14:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c6c9ccea-1129-3317-89d5-164e74ee7312 | -13.5721 | -52.859699 | 2025-05-13 00:14:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d97dd044-7766-3690-a06b-fbc64593c6c0 | -12.1987 | -46.715302 | 2025-05-13 00:14:00 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5fd65959-a918-3363-9004-3b1157791fcc | -11.5828 | -47.613998 | 2025-05-13 00:14:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b731b30-b667-32f4-be10-a74f682b17df | -13.3935 | -47.627499 | 2025-05-13 00:14:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9f797d8a-ffd2-3723-a6ad-c5c2fe7d57a2 | -13.0949 | -52.287201 | 2025-05-13 00:14:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| deed13bf-8b9a-3258-8c23-ef0d42ba5594 | -8.0699 | -43.117401 | 2025-05-13 00:14:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b951889f-01a4-344d-a6ce-324185509037 | -12.1515 | -48.011398 | 2025-05-13 00:14:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a734ad5-5437-3f53-99de-9515d38dc58a | -10.5441 | -42.4501 | 2025-05-13 00:14:00 | METOP-B | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e420ef25-dd64-39f9-9abf-0a6d4bfe5b23 | -12.1483 | -47.996498 | 2025-05-13 00:14:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eaae4023-2316-3240-86a3-d58059cb2fe0 | -10.4944 | -46.179401 | 2025-05-13 00:14:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 16c3c232-99fe-33fb-9955-feaa406816ab | -10.5419 | -42.4408 | 2025-05-13 00:14:00 | METOP-B | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 90399c5a-3ee2-372a-9a15-c5ab0a7efd2a | -14.1984 | -45.469398 | 2025-05-13 00:14:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 97127fdd-b3d1-35ea-bc4b-40b7528538f6 | -13.0924 | -52.2742 | 2025-05-13 00:14:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 91fc1b52-a2b6-30e1-b4dc-819fb6bf420d | -8.0839 | -43.133202 | 2025-05-13 00:14:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a905abce-9b14-3bbb-bb9d-58c3d8489e46 | -13.3919 | -47.619999 | 2025-05-13 00:14:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cc995ec6-5588-3f85-b29d-5567db7134a6 | -11.7934 | -47.401199 | 2025-05-13 00:14:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 070c0be8-c2c3-3431-a5b8-497fa8db1f57 | -13.5693 | -52.845299 | 2025-05-13 00:14:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| faeaedab-9644-3490-91f8-e702ff41e226 | -11.7745 | -48.694599 | 2025-05-13 00:14:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4119b670-b7c6-3b15-90df-a9c0c2f6206a | -13.6727 | -53.913101 | 2025-05-13 00:14:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
