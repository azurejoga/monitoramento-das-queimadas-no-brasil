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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42f9b494-80ae-30d2-8ece-2c961234c091 | -15.8859 | -57.1754 | 2024-10-02 01:24:13 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6e2fbc02-e8e1-35b2-8b70-aad3414295f2 | -15.8875 | -57.182701 | 2024-10-02 01:24:13 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 733682ee-3212-3bb7-8e56-7c5f8048395a | -12.4368 | -43.7066 | 2024-10-02 01:24:14 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3117493e-0a99-3f1f-ad27-60568e0d2e95 | -12.4273 | -43.7094 | 2024-10-02 01:24:14 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b973e100-f0f7-32c7-9fcb-8fae2747583a | -12.4373 | -43.744598 | 2024-10-02 01:24:14 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 71fe1955-6997-3eac-ac7d-8147354c001c | -15.9127 | -57.439999 | 2024-10-02 01:24:14 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3265f3a1-496d-36ba-b9b6-4ab030cb3725 | -15.9143 | -57.447498 | 2024-10-02 01:24:14 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0288f13f-4fff-3537-9f4b-4f582e545d9c | -15.9159 | -57.454899 | 2024-10-02 01:24:14 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7cc14f16-02ef-398c-b739-e31f200ac00b | -15.508 | -55.751301 | 2024-10-02 01:24:14 | METOP-C | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a6696bba-93db-36f1-8692-e851b4e41557 | -15.5096 | -55.7584 | 2024-10-02 01:24:14 | METOP-C | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eebc525e-03c5-3bd7-b3ea-4aec6a1736c3 | -15.3822 | -55.833302 | 2024-10-02 01:24:16 | METOP-C | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 91aad89b-6e1c-3524-bb74-1595b69c5921 | -15.3838 | -55.840401 | 2024-10-02 01:24:16 | METOP-C | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6f979699-2fac-37c4-9dcc-cba4ab9eb81b | -15.3854 | -55.847401 | 2024-10-02 01:24:16 | METOP-C | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 56e29003-3399-3ddc-9ee6-c11eec3c7338 | -15.3708 | -55.828602 | 2024-10-02 01:24:17 | METOP-C | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e6e2455b-8840-3055-aba5-931cf6f1fdf3 | -15.3724 | -55.835602 | 2024-10-02 01:24:17 | METOP-C | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c7676e34-f170-3e02-b23c-168cc3cd7fb5 | -15.374 | -55.842701 | 2024-10-02 01:24:17 | METOP-C | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3d085db6-96c9-3588-a5ab-8278aa780e02 | -15.3756 | -55.8498 | 2024-10-02 01:24:17 | METOP-C | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| de813a6d-ec29-3baa-971f-a757db3e79f2 | -15.3626 | -55.837898 | 2024-10-02 01:24:17 | METOP-C | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e5744bb5-2472-3031-9c80-eeeed6887bbb | -15.5468 | -56.8951 | 2024-10-02 01:24:18 | METOP-C | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1e7c1f8e-5d84-348c-bbe6-5f0b24f594b8 | -15.3207 | -56.063999 | 2024-10-02 01:24:18 | METOP-C | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7edae31a-8575-3c8a-aeb3-268593300f35 | -15.1428 | -55.822701 | 2024-10-02 01:24:20 | METOP-C | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 23ba730e-a3d9-3b27-8ddc-c40a368cf47f | -15.1444 | -55.8298 | 2024-10-02 01:24:20 | METOP-C | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 76d2b414-ac1d-3b5f-93e7-c066318e2cb1 | -15.146 | -55.836899 | 2024-10-02 01:24:20 | METOP-C | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8b79850d-9ff9-3241-9eee-034e1f19c86c | -15.1475 | -55.844002 | 2024-10-02 01:24:20 | METOP-C | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 76792f2d-d6d7-3c2f-b60f-b72898492f2f | -15.1314 | -55.818001 | 2024-10-02 01:24:20 | METOP-C | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 12d07413-2bb6-3009-9e6e-a4c5ab943c39 | -15.133 | -55.825001 | 2024-10-02 01:24:20 | METOP-C | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ada1a169-a4d4-33f5-99b0-63229ba5bcbd | -15.1346 | -55.8321 | 2024-10-02 01:24:20 | METOP-C | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cbdf467e-5d6c-344a-8aa6-35adaaf2e8db | -15.1362 | -55.839199 | 2024-10-02 01:24:20 | METOP-C | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9984a80a-8f6f-321a-8aca-ac1816d1c317 | -15.1216 | -55.820301 | 2024-10-02 01:24:21 | METOP-C | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0113862d-b9d7-37b8-b9ec-4f66a714b34a | -15.1232 | -55.827301 | 2024-10-02 01:24:21 | METOP-C | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 289244b5-d181-3063-98ae-21d917374920 | -15.1248 | -55.8344 | 2024-10-02 01:24:21 | METOP-C | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5127be7f-fc42-3870-a018-e8a8862d3d6d | -13.2269 | -48.551601 | 2024-10-02 01:24:23 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3f2832d0-e00b-3653-a0c8-706090ef8dc3 | -13.2172 | -48.554199 | 2024-10-02 01:24:23 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f9d9f60c-e9e0-3689-b522-75057612c0da | -13.2106 | -48.6082 | 2024-10-02 01:24:23 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2ae2bb1d-82b6-3bf7-b687-dd44ac6b30d4 | -13.1967 | -48.594601 | 2024-10-02 01:24:23 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3070ede3-7a51-3fa7-9ba8-2675a42a0c98 | -13.201 | -48.610901 | 2024-10-02 01:24:23 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 20c3ad27-e36a-396c-b48d-ba7be9c49e5f | -13.2052 | -48.626999 | 2024-10-02 01:24:23 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bf7ade73-6359-394e-b9a1-4ad110b81886 | -13.1913 | -48.613499 | 2024-10-02 01:24:23 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c15185b1-2b0a-350b-ad2e-0da737583f03 | -13.2311 | -48.567902 | 2024-10-02 01:24:23 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 648b37bb-661f-3d60-9fc6-803270f8bb35 | -13.2353 | -48.584099 | 2024-10-02 01:24:23 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f91e1be-76e0-3b5e-91c9-e0259811f37c | -13.2215 | -48.570499 | 2024-10-02 01:24:23 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 79ae0cd4-5138-3705-a845-add64d8fa19f | -14.9943 | -56.445702 | 2024-10-02 01:24:25 | METOP-C | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 36a556ed-9ae5-3964-9e5e-870fbe5ae667 | -14.939 | -56.428799 | 2024-10-02 01:24:26 | METOP-C | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 82a948c8-eae7-317b-bab4-468f0b75029b | -15.2714 | -58.179001 | 2024-10-02 01:24:27 | METOP-C | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8d6c306d-ccd6-3e30-97d4-ffec6822e615 | -15.2731 | -58.186798 | 2024-10-02 01:24:27 | METOP-C | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ef979fb9-15b5-3ad5-bb0a-e8795db700a6 | -13.5936 | -51.129101 | 2024-10-02 01:24:27 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 87457aad-1014-39a9-a781-a5e316344022 | -13.5963 | -51.139999 | 2024-10-02 01:24:27 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 092f498b-7425-3e5e-9f3b-211ed0fbe765 | -13.5839 | -51.131599 | 2024-10-02 01:24:27 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 183cec78-bfee-3dba-8b12-95f13e54a66c | -13.5866 | -51.142502 | 2024-10-02 01:24:27 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8a0f701f-825c-3b27-bd2b-7030b1b9bc44 | -13.5764 | -51.226398 | 2024-10-02 01:24:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 30be29c3-e7d1-35ed-8a38-c2a68ea92f76 | -13.5791 | -51.237202 | 2024-10-02 01:24:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d819569-86a6-3621-af07-c12dcc7be6ea | -13.5586 | -51.196301 | 2024-10-02 01:24:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 310502af-dd59-3846-b2a4-eee0ae9c97eb | -13.5613 | -51.207199 | 2024-10-02 01:24:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 77338875-8570-369c-8765-e6018139b77e | -13.564 | -51.217999 | 2024-10-02 01:24:28 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b5206174-1278-399a-b306-cc5051e859a7 | -14.8875 | -58.017502 | 2024-10-02 01:24:32 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 92e87d5a-a553-3f38-b9d2-491d1743c72f | -14.8892 | -58.025002 | 2024-10-02 01:24:32 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5303cd0f-3b32-32ca-9bb3-0df282570864 | -14.8762 | -58.012199 | 2024-10-02 01:24:32 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3be80f6-b09b-3686-8588-c5ddc127d35c | -14.8778 | -58.019699 | 2024-10-02 01:24:32 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bac8f5cb-172f-3cf4-9711-f576f5fd0ff5 | -13.2158 | -51.191299 | 2024-10-02 01:24:34 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 10cc1511-068c-3bf8-af43-9fac23dd7c9d | -12.2958 | -47.642799 | 2024-10-02 01:24:34 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 57156a9e-4137-37ec-ae44-c08889c426ba | -13.2061 | -51.193802 | 2024-10-02 01:24:34 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6d5f6921-caff-3276-bc44-0797d2ed4bd1 | -13.2088 | -51.2048 | 2024-10-02 01:24:34 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 39cf243f-8e81-362f-a41e-295942eff42f | -13.2115 | -51.215801 | 2024-10-02 01:24:34 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c92b7614-6c94-37a8-a413-acbcde0252f6 | -12.281 | -47.625999 | 2024-10-02 01:24:34 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b7cbe70-47bb-3690-a599-7f27903cbccf | -12.2861 | -47.6455 | 2024-10-02 01:24:34 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db3137bf-57e5-33c1-b951-e42696fd3125 | -12.2913 | -47.664902 | 2024-10-02 01:24:34 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c44b9cfb-16d2-3449-b30b-8053482bdb4b | -12.2714 | -47.628601 | 2024-10-02 01:24:34 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14aa3a06-deb3-3281-b57f-50ab845b7bea | -12.2765 | -47.648102 | 2024-10-02 01:24:34 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3679f025-55d0-36c7-aaf4-1cb375a2815e | -12.2817 | -47.6675 | 2024-10-02 01:24:34 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c697bcaf-3ccf-328b-aff2-3cc2fc5a2521 | -14.8408 | -58.6101 | 2024-10-02 01:24:35 | METOP-C | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 485bfbf1-9c09-30ac-b810-e10b89e8ed02 | -14.8424 | -58.617901 | 2024-10-02 01:24:35 | METOP-C | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1a23232c-b311-3ebe-a457-64b93e9f33b6 | -14.8293 | -58.604301 | 2024-10-02 01:24:35 | METOP-C | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 63768c78-e965-3d77-a51b-f3cbb4f681ba | -14.831 | -58.612202 | 2024-10-02 01:24:35 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f734fee5-2cda-39c2-97c1-93a42ad2ccda | -14.8326 | -58.619999 | 2024-10-02 01:24:35 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 393b5648-678d-33df-9a82-bbeca6b244c8 | -13.0953 | -51.373001 | 2024-10-02 01:24:36 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d1c1f7ab-1f25-39fe-8493-d798019f018e | -13.098 | -51.383801 | 2024-10-02 01:24:36 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 572194e3-b605-392a-80e5-9517a68e671f | -13.0936 | -51.407799 | 2024-10-02 01:24:36 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dc6b42bd-7902-3037-b551-e3c097645b27 | -13.0963 | -51.418598 | 2024-10-02 01:24:36 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eeff2ced-bacf-336a-b35f-3340cd11db52 | -13.0989 | -51.429298 | 2024-10-02 01:24:36 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fec205a6-b364-3fbb-9110-2070304920c1 | -13.1015 | -51.439999 | 2024-10-02 01:24:36 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 787f8bc8-9db8-35d8-97f2-ad548600dfaf | -13.0547 | -51.417702 | 2024-10-02 01:24:37 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b3ce6ac3-9aa9-3418-a48b-c0a12547a1e8 | -13.0812 | -51.399502 | 2024-10-02 01:24:37 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 48e76fd6-0e77-3eef-adba-7bb34f9fefa7 | -13.0839 | -51.410198 | 2024-10-02 01:24:37 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5fcb466b-68cf-3ab3-b088-f090341867c0 | -13.0866 | -51.421001 | 2024-10-02 01:24:37 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 478b1d49-506a-3f90-a901-87e8233f78bf | -13.0892 | -51.431702 | 2024-10-02 01:24:37 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dd2eea86-3734-37aa-bdfc-1a0af1e2c4bc | -13.0918 | -51.442402 | 2024-10-02 01:24:37 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1a8709db-6d99-308f-9f5d-75f6b230cb3d | -13.0033 | -51.127701 | 2024-10-02 01:24:37 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 837f0b34-ff39-35ab-b756-198c185d6afc | -13.0527 | -51.326302 | 2024-10-02 01:24:37 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 49e95c68-6768-3f91-b8e3-afd6adf20a7e | -13.0554 | -51.3372 | 2024-10-02 01:24:37 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dac6d079-0b11-3af7-94ab-1b9826a7e61c | -13.0634 | -51.369701 | 2024-10-02 01:24:37 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b96b30c7-e6ba-37e5-a68a-ac52a546005d | -13.0661 | -51.380402 | 2024-10-02 01:24:37 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b4461633-139e-327a-a9ad-55585b6dface | -13.0688 | -51.391201 | 2024-10-02 01:24:37 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 82b0f2b4-02f7-3234-95c4-2da3864e8d23 | -13.0741 | -51.412701 | 2024-10-02 01:24:37 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b58cd8f4-b601-3e52-98a6-d35c675ad580 | -13.0768 | -51.4235 | 2024-10-02 01:24:37 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fcc8b17e-d47a-3b89-a766-6d3a51ceb037 | -13.0794 | -51.4342 | 2024-10-02 01:24:37 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8799b43a-3f81-39c2-a093-90b606f6f589 | -13.082 | -51.444901 | 2024-10-02 01:24:37 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 40132329-66c7-3b75-938e-2c96932aacc6 | -13.0537 | -51.3722 | 2024-10-02 01:24:37 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 56285c2f-9522-31bb-9acf-2c76ffa3aa45 | -13.0564 | -51.3829 | 2024-10-02 01:24:37 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ff411aa8-c418-3531-a1cb-4db8b53932a3 | -13.0591 | -51.3937 | 2024-10-02 01:24:37 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9cbc529a-5c27-35a9-bab2-a79e5d9df86f | -13.0617 | -51.404499 | 2024-10-02 01:24:37 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README30.md)
