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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee6f6bdf-340a-3a83-9dcc-c6019a82913b | -7.0695 | -44.9335 | 2025-10-29 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 6d070963-d505-387c-afb5-79bf687c058b | -7.0883 | -44.9319 | 2025-10-29 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 7430385e-10bb-3f43-8010-abd7ec14586b | -13.725 | -43.4529 | 2025-10-29 14:00:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 0b3ac73b-1699-3a42-82b5-b23ddab8ae4b | -12.3679 | -50.1539 | 2025-10-29 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 272.8 |
| 96b11f70-ce2b-3917-8857-08ab40675cd3 | -13.0639 | -47.535 | 2025-10-29 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| d9f2d13f-9d3e-3839-8292-af11289b8f03 | -7.0881 | -44.9547 | 2025-10-29 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 317bf1e3-70bc-376d-bf7f-b88dfff96be6 | -6.1467 | -41.5514 | 2025-10-29 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 69.9 |
| b16f9e95-6b80-302f-bbd3-c46286b4763a | -7.3418 | -42.4894 | 2025-10-29 14:00:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 219.1 |
| 3007a6bc-9622-330a-8545-366dec9074da | -3.1997 | -42.0582 | 2025-10-29 14:00:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 7cb644df-d14f-32bf-b6ce-f85cc31df785 | -7.0745 | -44.4756 | 2025-10-29 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 948c2985-b672-3428-b02d-df2be7186a50 | -7.6114 | -43.5914 | 2025-10-29 14:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 130.9 |
| cec246f6-b7a4-3885-bf61-43bf578ff3cd | -13.9337 | -48.4305 | 2025-10-29 14:00:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 0d986d5c-2981-37c8-969b-70646d9fd63e | -8.0636 | -45.1359 | 2025-10-29 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| f8755804-b453-3045-b920-2bfd815bf38f | -3.7262 | -41.555 | 2025-10-29 14:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 124.1 |
| 49146686-f0fb-3b0c-b096-ac7ecd99e612 | -13.9332 | -48.4528 | 2025-10-29 14:00:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| abcef4a8-1739-3523-84c1-a33c5ec92f9d | -4.5157 | -38.7741 | 2025-10-29 14:00:00 | GOES-19 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 135.8 |
| 42e1c494-4e01-3ef9-93eb-11229fe2bdbf | -12.6639 | -47.3469 | 2025-10-29 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 50834790-6bad-3651-97e2-8e0b60d2fffd | -12.5489 | -49.5901 | 2025-10-29 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| bb5932e1-0b3a-3744-9a95-04f271ce2954 | -7.3054 | -45.6833 | 2025-10-29 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 158a6d3c-4872-334e-abe2-da1755ec8484 | -3.7075 | -41.556 | 2025-10-29 14:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 129.7 |
| 2651b029-e4f6-3683-9132-a3caae53f1b5 | -7.2943 | -44.9817 | 2025-10-29 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 44f1d601-f55f-3f73-a6de-93161f32e285 | -8.0633 | -45.1587 | 2025-10-29 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 7f9b9859-0088-3542-a2c2-86bb5a470b11 | -6.6414 | -44.6051 | 2025-10-29 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| a74e54d7-d751-36ec-98ae-e034579af4d0 | -13.9522 | -48.4721 | 2025-10-29 14:00:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 3820c428-54f7-3b00-ad0c-fed5779d6398 | -6.8601 | -43.4537 | 2025-10-29 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| ca77cb8b-5c2a-3ba2-a43b-b475dc54d817 | -13.5686 | -47.3242 | 2025-10-29 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 63.7 |
| b3af3008-0e5c-3d8c-a9ba-13775eff65d9 | -15.118 | -49.31 | 2025-10-29 14:00:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 00215c25-8614-38a5-8061-b02001efd2e2 | -14.4754 | -45.5984 | 2025-10-29 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 516.9 |
| 4d29f667-0601-3830-9d37-adef4a6ca4ea | -6.8808 | -45.041 | 2025-10-29 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 239.4 |
| 9a8b0204-687d-3150-92a9-0025c671123d | -15.0706 | -48.7638 | 2025-10-29 14:00:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 88.7 |
| a19e4a0b-1472-3829-b6e7-c364970d01b7 | -7.5928 | -43.5699 | 2025-10-29 14:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 8e968a3a-6a53-318d-b0e4-85591b3be621 | -12.387 | -50.1515 | 2025-10-29 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 170.3 |
| c1ff99f2-bfa0-3104-9fc6-f634847fb50f | -3.6731 | -44.2053 | 2025-10-29 14:00:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 207.6 |
| 90f2c360-13df-388c-94fb-282e11f18f5f | -14.23 | -43.4776 | 2025-10-29 14:00:00 | GOES-19 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 983.1 |
| 9819dc4f-19b6-319b-88cc-2bec252b79d8 | -13.0446 | -47.5379 | 2025-10-29 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 5e6bd49e-24fe-3319-901b-c1294ca0d2ef | -14.8981 | -46.7659 | 2025-10-29 14:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 17f5b335-892b-3845-ac06-380f70ce1b9e | -12.3676 | -50.1755 | 2025-10-29 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 1b0bfc45-4cb5-30a0-a67d-597ebed33cb3 | -13.7348 | -48.748 | 2025-10-29 14:00:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 332d7dbf-1675-356b-bf77-18e2d8f28bdb | -8.5464 | -45.6994 | 2025-10-29 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| a319ddd6-aafd-3a04-9f50-4a0a4568504a | -7.3418 | -42.4894 | 2025-10-29 14:10:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 190.8 |
| a9c9fbea-b353-301c-bd97-a3eca11cff48 | -12.3488 | -50.1563 | 2025-10-29 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 6994ee29-f670-36c9-9ff5-edd22248cd19 | -7.3054 | -45.6833 | 2025-10-29 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 73b6ba94-a171-3347-b122-06ab3eadd102 | -15.118 | -49.31 | 2025-10-29 14:10:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 99c8ebda-e655-3093-950e-c8b06a5856a0 | -8.9504 | -45.1105 | 2025-10-29 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| a3bdd1a5-0be8-320b-9ffd-5cbc446d16ed | -8.0633 | -45.1587 | 2025-10-29 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 9cc9fef3-c969-3f8d-b1b7-28346ead3408 | -7.5242 | -46.27 | 2025-10-29 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 44cc0f06-87ad-35c2-b3da-5a85ec36a6ec | -7.9693 | -46.7423 | 2025-10-29 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 70a42e12-9d92-35e1-866f-30a8ea6f9b56 | -12.3484 | -50.1779 | 2025-10-29 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| b44bb6c1-9558-343d-9f29-2c0b83b89d29 | -6.1187 | -42.4612 | 2025-10-29 14:10:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 102.6 |
| d1f087eb-9916-30c1-b15d-9eca94f5c01b | -3.7262 | -41.555 | 2025-10-29 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 153.1 |
| ce579588-fd90-3643-a12d-bf50193adec1 | -6.6414 | -44.6051 | 2025-10-29 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| f84b9144-8c3d-3c73-ae76-06751333bcef | -12.3676 | -50.1755 | 2025-10-29 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 177.5 |
| a93b41f9-06a0-3fc0-bb13-d39e5965cdbb | -3.7075 | -41.556 | 2025-10-29 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 161.9 |
| 11d61b74-2d23-3d7c-a0ab-7190c06c5ad4 | -12.3679 | -50.1539 | 2025-10-29 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 270.0 |
| 984a2fcb-bceb-3b06-a3fd-eac877ffcf68 | -15.0711 | -48.7415 | 2025-10-29 14:10:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 74.5 |
| b2ac901d-280f-3e66-8a4f-b70c91a90996 | -15.2045 | -47.9368 | 2025-10-29 14:10:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 69c5a6ae-755b-3bcf-a423-6e6283f3e606 | -6.1249 | -41.8414 | 2025-10-29 14:10:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| c0e4b163-06b0-35eb-8b63-205b003f0a35 | -7.3232 | -42.4675 | 2025-10-29 14:10:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 123.8 |
| e3d05094-fdd2-3ec2-bf00-94b07d0e5393 | -13.0442 | -47.5603 | 2025-10-29 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| dfd7c94e-d8c8-3abd-94bc-51e1c23943b5 | -7.4108 | -44.651 | 2025-10-29 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 2d02efb9-e920-34eb-a83d-9c02d12d1c44 | -7.0745 | -44.4756 | 2025-10-29 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| de30671d-db2f-3c11-9eba-bc038951716b | -3.288 | -43.0199 | 2025-10-29 14:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| ce554b8a-4257-353a-aac8-4af228d86671 | -13.9337 | -48.4305 | 2025-10-29 14:10:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| f04db375-8390-3349-a38c-1963a7cc9ce5 | -7.7844 | -46.4921 | 2025-10-29 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| af2bc92a-49af-3aa5-89ef-4c64f431b007 | -5.7966 | -40.8068 | 2025-10-29 14:10:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 81.6 |
| 82206bb3-32ad-3c4b-a07d-096bc877d02d | -14.4829 | -45.2485 | 2025-10-29 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 36ffed2c-3574-3224-8c84-4a52edf81bd7 | -7.686 | -46.9011 | 2025-10-29 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| ff534480-d61d-3460-97d5-f6d863c86f14 | -11.9307 | -51.3384 | 2025-10-29 14:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| cb0830c7-b3ba-348e-a24f-717b098bb23d | -13.7348 | -48.748 | 2025-10-29 14:10:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 3cd1d0d9-923f-3350-9e9a-f82f361eccd7 | -6.165 | -41.5979 | 2025-10-29 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 89.9 |
| 80de72d9-f73a-311e-915d-d9b3ab65c831 | -8.2491 | -46.916 | 2025-10-29 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| a71d6799-e22c-3942-9d8b-63e4720bc1c6 | -6.1189 | -42.4375 | 2025-10-29 14:10:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| aed4634a-2872-3764-8d9c-dc57d2b133bc | -13.5686 | -47.3242 | 2025-10-29 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.4 |
| ab302cc4-cedf-3718-ad8d-b2aa959ffc65 | -7.0883 | -44.9319 | 2025-10-29 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 137.6 |
| f1c51833-1feb-32d9-aca7-e4353ca2d6b5 | -7.6114 | -43.5914 | 2025-10-29 14:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 1d3849e7-623c-36a2-8e2f-a638ec954ff1 | -7.8037 | -46.4458 | 2025-10-29 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 120.5 |
| dee0a8e5-c868-3e50-9743-9d8969a4ea3e | -13.7343 | -48.7701 | 2025-10-29 14:10:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 45e03d40-1fcd-36cd-88de-794fc663c3aa | -7.0695 | -44.9335 | 2025-10-29 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| a2ee651c-d0ff-36d7-843f-0a08874e3f1d | -12.387 | -50.1515 | 2025-10-29 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 3192f502-dda0-39a2-b73b-c45cfab65f3a | -13.0635 | -47.5575 | 2025-10-29 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 1278cfb0-3096-35a1-8dea-e356fd3076a3 | -7.3799 | -42.4617 | 2025-10-29 14:10:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 111.3 |
| 4f63899c-b1dd-3337-935d-0eea58a557d5 | -5.8154 | -40.8052 | 2025-10-29 14:10:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 97.7 |
| 39921c79-7ecc-3baa-89ad-e851797b4b59 | -7.5928 | -43.5699 | 2025-10-29 14:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 11be8b2f-293a-3bdb-957f-439c2180c439 | -7.3421 | -42.4656 | 2025-10-29 14:10:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 196.2 |
| 0e8e468e-d9cd-374b-8568-979ece9163b7 | -13.0446 | -47.5379 | 2025-10-29 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 2ef36595-3717-34ac-8cab-451b80ae3082 | -15.0706 | -48.7638 | 2025-10-29 14:10:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| fd0df565-f30e-3842-9993-afc3e8fb98a6 | -15.2241 | -47.9335 | 2025-10-29 14:10:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 123.4 |
| ad248a73-368b-3a70-b2f8-0677dada2b0e | -7.7847 | -46.4698 | 2025-10-29 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 126.3 |
| b5e487fa-445f-343e-a4d9-86cae187f26e | -13.5682 | -47.3468 | 2025-10-29 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 7ec8bb5a-d05c-3a5a-aee5-9b694b6fbfc7 | -7.5054 | -46.2717 | 2025-10-29 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 83f90653-83e4-386d-8ee5-f5f469cb0804 | -13.0639 | -47.535 | 2025-10-29 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 92e727e6-43fb-348e-be02-acfd8441b830 | -3.8997 | -40.797 | 2025-10-29 14:10:00 | GOES-19 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 156.1 |
| 650c6f1c-8eb8-3d41-8565-fb7c881c963b | -7.9696 | -46.7201 | 2025-10-29 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 041ff409-9281-3ccb-9188-ceea2ef554b2 | -7.6116 | -43.568 | 2025-10-29 14:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 48f6f2a9-afaf-3b18-84ee-a1df92ff042d | -7.804 | -46.4234 | 2025-10-29 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| ce115fc8-d23e-358d-b86e-08d644871aa9 | -3.1997 | -42.0582 | 2025-10-29 14:10:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| e3175079-bdb3-3003-af2d-3ed8eb074351 | -7.3232 | -42.4675 | 2025-10-29 14:20:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 130.7 |
| 8e9800af-5d1e-31ab-ad78-6a35d4c2a149 | -7.804 | -46.4234 | 2025-10-29 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 1f48b684-c5e9-3712-b05e-4a35b532f25e | -7.0883 | -44.9319 | 2025-10-29 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 03ae228d-ff06-3981-bd10-a17e5293eaf3 | -3.7075 | -41.556 | 2025-10-29 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 165.7 |


[Clique aqui para ver as próximas entradas](README88.md)
