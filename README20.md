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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 370b8733-0c86-3848-b4f1-0e771bd2468f | -1.2755 | -53.3936 | 2024-11-03 03:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 158.6 |
| fcd20e16-4097-3235-b713-70880c11b937 | -1.2755 | -53.4138 | 2024-11-03 03:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 161.2 |
| 3190cdbd-8230-3015-9f7b-1f18d2f64ba2 | -2.1746 | -53.6834 | 2024-11-03 03:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 1b342b85-75fb-3f4d-ae3a-f178f80c601a | -2.2986 | -48.8078 | 2024-11-03 03:15:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 7d73ead7-9259-3bd6-85e3-33fc83537e67 | -2.7218 | -49.3295 | 2024-11-03 03:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| d62a801e-e809-3d87-b963-193da3f980a6 | -2.6507 | -48.5629 | 2024-11-03 03:15:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| edb04891-f811-3cc2-82b7-30714e8e107f | -2.6506 | -48.5844 | 2024-11-03 03:15:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 77e3b3aa-f98d-39bc-b4d5-de46e247169a | -2.5797 | -53.3724 | 2024-11-03 03:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| b5a0ed99-a732-3c15-b11e-ca0bcb673105 | -2.5796 | -53.3927 | 2024-11-03 03:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 408d0471-6807-32ab-9cbe-8d92f064bdf4 | -2.8333 | -49.1562 | 2024-11-03 03:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 5795d15e-c4dc-3eb3-b550-10a986a2309d | -2.8148 | -49.1567 | 2024-11-03 03:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 91dd1efa-0c70-33bf-949b-db1ebda37d76 | -2.7876 | -51.6099 | 2024-11-03 03:15:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| c8d6d8e6-c848-32f0-a4db-6cdb8e31f00e | -2.7603 | -54.4149 | 2024-11-03 03:15:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 5375296b-b32f-3d23-aba2-3ed07056ebcc | -2.7602 | -54.4349 | 2024-11-03 03:15:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 18a66158-5747-3c7b-9c67-152069c49863 | -2.7419 | -54.4153 | 2024-11-03 03:15:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 31520f4b-8fc4-3dfc-aea9-5359fd48a919 | -2.7419 | -54.4353 | 2024-11-03 03:15:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 129.7 |
| 6237b364-e058-398d-b3f3-7885d5b53cf3 | -3.055 | -54.1474 | 2024-11-03 03:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 9cf15b45-3b12-3b66-b5af-52a0e3a6b3d4 | -3.1501 | -48.5689 | 2024-11-03 03:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| f63edfa0-0b49-37d6-8d0e-ced161878750 | -3.1245 | -50.289 | 2024-11-03 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 849beeb5-c0e2-3b17-907c-17d43206849f | -3.1061 | -50.2686 | 2024-11-03 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| f31b5e03-0702-3914-8ecc-1fc12bd02df0 | -3.106 | -50.2896 | 2024-11-03 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 6350a508-cf38-3790-94af-4ca1ed0597bd | -3.1059 | -50.3105 | 2024-11-03 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 2bd213ae-01cb-3cba-819b-eb6094d9a2c3 | -3.0734 | -54.147 | 2024-11-03 03:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 5c76d812-c27f-3efc-b4ec-79520c53f44c | -3.0734 | -54.167 | 2024-11-03 03:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 490accc5-9bd5-309d-b0a8-39554245f669 | -3.4749 | -50.3826 | 2024-11-03 03:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 09d43bb5-53cf-3847-ac91-6d85a0e02e35 | -3.475 | -50.3616 | 2024-11-03 03:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| a1f6c41b-b59a-3acc-b55e-6247925033fa | -3.9473 | -48.3666 | 2024-11-03 03:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 6cf6122e-b8e7-309d-be0f-be4ac74592cc | -3.9474 | -48.3451 | 2024-11-03 03:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| ae5bc001-71be-3a5f-9a27-d915d0a104c2 | -3.967 | -48.15 | 2024-11-03 03:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| d3824c45-ca73-301f-8747-b43aa3669a54 | -4.4241 | -43.4735 | 2024-11-03 03:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 40f38593-a7dc-385f-ab6c-bd0ba3467ad7 | -4.4056 | -43.4514 | 2024-11-03 03:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| d6492b86-d9c7-37ea-ba98-23d119195cd1 | -4.4054 | -43.4746 | 2024-11-03 03:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 5ccaef7e-6b97-3bee-9bad-ec8cf3c07b73 | -6.5241 | -41.4688 | 2024-11-03 03:15:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 756539ae-a837-3f1b-85ab-19b6ab1ca59a | -6.5239 | -41.4929 | 2024-11-03 03:15:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 4592bfe8-7582-3bf0-9444-abc2f567663f | -1.2755 | -53.3936 | 2024-11-03 03:25:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 237dae6e-2caf-3077-bf6c-4be10f3ebf43 | -2.1746 | -53.6834 | 2024-11-03 03:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| a894190d-5626-37ac-b08d-1ef438a613f3 | -2.5796 | -53.3927 | 2024-11-03 03:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| b547d3f4-1ab0-37b0-9cfa-d9212c127314 | -2.5797 | -53.3724 | 2024-11-03 03:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 99f3019a-da5b-314a-b111-9e3b6d38b565 | -2.6321 | -48.5849 | 2024-11-03 03:25:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| c6155475-cbcf-37ba-b4ec-1599a90df6b1 | -2.7218 | -49.3295 | 2024-11-03 03:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 7f60d251-6908-355c-ba50-3ce391a0cbef | -2.7419 | -54.4353 | 2024-11-03 03:25:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| e896a967-352c-3b87-acb5-10d465e85165 | -2.7419 | -54.4153 | 2024-11-03 03:25:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 94826b3b-113f-327f-ba0f-477c32ab4e20 | -2.7602 | -54.4349 | 2024-11-03 03:25:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| f0f6356a-e2fc-3676-8e8c-56670077e2b1 | -2.7603 | -54.4149 | 2024-11-03 03:25:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 47849ad0-9043-31b4-b356-33f98e5864ef | -2.8148 | -49.1567 | 2024-11-03 03:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 55228599-7dec-3f48-a940-d286b28e3174 | -2.8333 | -49.1562 | 2024-11-03 03:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| d6e3fd05-e43f-39d4-acb3-c093886a51df | -3.055 | -54.1474 | 2024-11-03 03:25:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 56dd1aac-0b45-36f6-a58e-c1646a45c6ed | -3.106 | -50.2896 | 2024-11-03 03:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 44f2c288-1686-3ec4-9632-93995c03e084 | -3.0734 | -54.167 | 2024-11-03 03:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 6b124355-0f93-3a96-a8f4-3a27a1649a5c | -3.0734 | -54.147 | 2024-11-03 03:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| bde74f6f-5378-333b-ba5b-65b9bfeddff4 | -3.1059 | -50.3105 | 2024-11-03 03:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 7d9123c4-73e0-38a5-a8d5-a241a480e707 | -3.1501 | -48.5689 | 2024-11-03 03:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| aac3dc5f-7cbd-3093-90c7-4ecd8e6f2aa0 | -3.1061 | -50.2686 | 2024-11-03 03:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 94724ab9-0182-392f-85c6-e8db55a74b2f | -3.3276 | -50.2825 | 2024-11-03 03:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| e24760ff-9db0-3153-8484-73b67a6d2243 | -3.475 | -50.3616 | 2024-11-03 03:25:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| c30b8ee4-9e81-3bef-bd9a-7f36b7cf34bf | -3.4749 | -50.3826 | 2024-11-03 03:25:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 7e2646bc-6ccc-3033-8c6b-87783af66e29 | -3.967 | -48.15 | 2024-11-03 03:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| a17bf8cd-9921-3c3e-9221-52a5d9ab7640 | -3.9474 | -48.3451 | 2024-11-03 03:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| ec13a1bb-1848-3520-9051-9e7840b3a619 | -3.9473 | -48.3666 | 2024-11-03 03:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 60059896-2fd9-3a04-8643-f1fdcfd31a05 | -4.4054 | -43.4746 | 2024-11-03 03:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| e3f42d5c-1c56-3fa6-9127-ef5bf9d34ad1 | -4.4056 | -43.4514 | 2024-11-03 03:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| da746040-249a-372f-8ed0-58617084508c | -6.5239 | -41.4929 | 2024-11-03 03:25:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| abf3849c-4cb9-37f0-917f-e29f3da917d4 | -6.5241 | -41.4688 | 2024-11-03 03:25:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| 4cfa5628-2310-3ed1-8904-b7bbd418eed3 | -7.28049 | -44.69105 | 2024-11-03 03:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0bfcba3e-7d5b-3b15-8d16-6462a2765ba3 | -7.27938 | -44.69693 | 2024-11-03 03:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9106500-bdf6-34a9-a9bc-5172a70d4d26 | -7.27609 | -44.6781 | 2024-11-03 03:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f507ea6-8f8a-3c1e-94c8-05283870cc3b | -7.25706 | -44.68691 | 2024-11-03 03:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57d65591-7333-3ee4-bec5-6c5bf37c2a82 | -8.18254 | -35.36959 | 2024-11-03 03:27:00 | NPP-375D | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2e87067e-62d5-3eb3-b2f7-a43d99131f68 | -7.98918 | -35.27331 | 2024-11-03 03:27:00 | NPP-375D | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 33061f18-278b-3aae-92aa-6694d8ba4403 | -7.83735 | -35.12445 | 2024-11-03 03:27:00 | NPP-375D | ABREU E LIMA | PERNAMBUCO | Brasil | 2600054 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ce582356-aae0-3fb4-b875-3921aafa3e5a | -7.69773 | -39.51519 | 2024-11-03 03:27:00 | NPP-375D | MOREILÂNDIA | PERNAMBUCO | Brasil | 2614303 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3ac93c07-3182-3db4-9b7a-6e41597172eb | -7.30434 | -34.80157 | 2024-11-03 03:27:00 | NPP-375D | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8f2086e6-514c-32d6-a236-c912e85badf1 | -7.26707 | -39.07752 | 2024-11-03 03:27:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8d65159b-8ff6-3fd9-85e8-461d41820e48 | -6.73024 | -38.52029 | 2024-11-03 03:27:00 | NPP-375D | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 735c05fd-63a3-30e3-8563-6d870cd50936 | -6.72773 | -38.52064 | 2024-11-03 03:27:00 | NPP-375D | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 48109ea4-e94b-3c15-87c3-6d45b68e29e9 | -6.69365 | -38.317 | 2024-11-03 03:27:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 758f79aa-ce95-3aa7-aa03-a63118e075d3 | -6.6929 | -38.32133 | 2024-11-03 03:27:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 9.4 |
| db8ea528-5edf-3f5c-98cc-00a709d3e9bc | -5.94157 | -44.7203 | 2024-11-03 03:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| caacf235-9145-3eaf-8354-8e14cb3e693e | -6.68478 | -38.42214 | 2024-11-03 03:27:00 | NPP-375D | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 42f4ef5f-86e1-3dc6-8f2b-7809c171dc34 | -6.68404 | -38.42648 | 2024-11-03 03:27:00 | NPP-375D | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e58c9328-a60f-3183-ae7f-da039979d730 | -6.60774 | -37.50149 | 2024-11-03 03:27:00 | NPP-375D | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c93d8e6c-4f8e-3fbd-8d59-fd1b8abf1a3c | -6.60709 | -37.50536 | 2024-11-03 03:27:00 | NPP-375D | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 26ecbd41-27ff-3667-9af1-3dbdc4cc4dca | -6.60357 | -37.50078 | 2024-11-03 03:27:00 | NPP-375D | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8527b166-f4bf-3cfa-9b09-209a1c69f757 | -6.60005 | -37.49622 | 2024-11-03 03:27:00 | NPP-375D | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 811d0c5e-7c18-3df9-b77d-85ee5de786fc | -6.59939 | -37.50009 | 2024-11-03 03:27:00 | NPP-375D | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c69da1c8-f1e6-331b-9c42-5251f7055d28 | -6.5952 | -37.49941 | 2024-11-03 03:27:00 | NPP-375D | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 54f56d1a-5885-3c45-be24-e38ce01b5ff8 | -6.55124 | -34.97778 | 2024-11-03 03:27:00 | NPP-375D | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 84f8d0e9-4b02-3497-9c6c-b6f0aad28b72 | -6.53472 | -37.44723 | 2024-11-03 03:27:00 | NPP-375D | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 91077678-23d2-37db-a056-e5bc3c88efc6 | -5.94267 | -44.71445 | 2024-11-03 03:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 986c8e68-0f7e-3f02-a719-e91030e2a084 | -5.94024 | -44.72062 | 2024-11-03 03:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5fd3abb5-c023-305a-9db0-4b1363b6edb2 | -6.53119 | -37.44275 | 2024-11-03 03:27:00 | NPP-375D | SÃO BENTO | PARAÍBA | Brasil | 2513901 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 63188368-7b85-3820-943f-d0e9f6383c4d | -6.52765 | -37.4383 | 2024-11-03 03:27:00 | NPP-375D | SÃO BENTO | PARAÍBA | Brasil | 2513901 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 41de7145-0923-3507-ae06-f88835538577 | -6.52702 | -37.44205 | 2024-11-03 03:27:00 | NPP-375D | SÃO BENTO | PARAÍBA | Brasil | 2513901 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c1b1276d-05b5-3f56-8e2f-6102ee7e452c | -6.35233 | -41.44331 | 2024-11-03 03:27:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| fc63471e-616f-3a86-9ab5-7a76f90e4f3b | -6.3517 | -41.44687 | 2024-11-03 03:27:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 7c47f4df-d7f6-3d11-bcb3-a4d4991d5bcf | -6.35106 | -41.45044 | 2024-11-03 03:27:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 66df2276-aacf-34ca-9007-cfe3f5c1cb45 | -6.34557 | -41.44955 | 2024-11-03 03:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 3b2a9f46-d19b-3e54-b9de-bbb67a6ab655 | -5.51992 | -38.00043 | 2024-11-03 03:27:00 | NPP-375D | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4cf1ed5c-d4df-3b42-8d3f-52ae0e83b1b4 | -5.51982 | -37.99868 | 2024-11-03 03:27:00 | NPP-375D | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 01ecaff4-6be6-3be1-997e-e0ab88a7dd6e | -5.51906 | -38.00307 | 2024-11-03 03:27:00 | NPP-375D | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README21.md)
