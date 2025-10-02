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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be2240b5-d2a9-3d75-9446-53ea2f75d068 | -12.47769 | -54.42699 | 2025-10-02 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e135ef88-be21-3d39-b6a0-b0ffc049af02 | -12.71202 | -48.59314 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e74017d7-b5c7-348c-88cf-64a810bef7c6 | -15.2847 | -56.77528 | 2025-10-02 04:51:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35169313-4c08-3d63-85a3-fdcaa0848632 | -11.14956 | -47.2001 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3fa1c66b-9b23-3b67-89f1-ead12a13c04a | -10.32676 | -48.18438 | 2025-10-02 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 093c959d-54ba-3f8b-a152-c082ef6c2eb3 | -12.15536 | -46.67565 | 2025-10-02 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a260dcb2-7b9f-3d36-893b-178156bb1227 | -15.36132 | -47.06517 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b66c4269-4003-3457-841e-6b79503571c0 | -11.46668 | -45.06076 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6e2311d1-7822-3e52-84da-e37cd09f195f | -13.87061 | -47.95235 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b31e966-36d2-328b-a324-dd13e4e3df4f | -13.34243 | -47.34055 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 38dc2e36-e0cb-3f0a-9271-a8e7ed9ff882 | -13.00986 | -45.22126 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00c0cfc9-904c-39be-8dbe-fc5265b29ed5 | -9.93244 | -43.77317 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1f26520d-0e24-3703-a0ad-74d58bcf2b4e | -15.00841 | -55.27684 | 2025-10-02 04:51:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 400b8fba-32a7-3552-b365-3cfe86c38f1a | -10.80218 | -44.24408 | 2025-10-02 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8eac9a3e-410b-3dbb-b81a-9c9832d77f6a | -15.20011 | -48.16285 | 2025-10-02 04:51:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b37a428-aead-3ae7-a77b-226145c98bb1 | -9.93189 | -43.73366 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 40.0 |
| b355e2a0-4a66-3db5-a8db-552d9a0c2fed | -11.84943 | -44.98353 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 137e6218-f291-3191-a02e-5b23b6e6cb99 | -11.67268 | -45.32645 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8de4bf9f-7c2c-3fe4-baf0-8d108ae4c213 | -11.60005 | -45.05811 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42957481-fcb0-3aca-a5db-5f40ea06f927 | -10.20156 | -50.27125 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bfd88195-3146-3902-98e8-2c6261f1bdab | -14.40368 | -46.07736 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3af4857d-5439-36c2-8f63-d67bf8b37664 | -12.22111 | -43.76178 | 2025-10-02 04:51:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd656516-5645-381e-a11d-05d64887c102 | -13.29244 | -47.25418 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f419c817-b716-3220-904e-017ac4a70d98 | -10.69477 | -48.57774 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9cbcc1c8-bc51-3c5c-b981-122c6fd8c5e1 | -11.46739 | -45.01339 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cc4b5da-9e20-3c82-bfd6-f94938de90c3 | -9.92876 | -43.75834 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 7ef0dc87-355b-3649-8c44-7f49e227775c | -11.47165 | -44.97928 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b1e4c0d-8920-3a68-8346-48295f6b34e1 | -12.63451 | -44.85319 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 411bce52-ebdc-3759-b1f5-b787c282296c | -9.93966 | -43.7601 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4dbb2acd-9dcf-3348-8f30-f43da63fcca2 | -10.22056 | -50.34208 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ccee077e-4a97-3abf-90b7-669de9eb1f0d | -11.44461 | -43.5052 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e0fdeb1-dea8-3c6b-9032-ac1bd6e1fa70 | -13.36857 | -46.33722 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e440926f-1f38-38e9-9ceb-8eda23050c17 | -14.30964 | -45.8934 | 2025-10-02 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ef4c08e-e4f9-3791-b4f2-3f5077d0d076 | -13.96063 | -48.13119 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c67d3028-b6fe-3ab1-b063-bb1ee75f164a | -13.30319 | -47.84291 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8bca7f35-8502-3874-b13d-b545320adbe6 | -13.3237 | -47.22717 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 606ed5a7-2545-3440-baed-2694710a346d | -14.69553 | -48.117 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5efb26c-02f4-3e4b-9440-3838d77596cf | -11.47018 | -44.97504 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 929d5c9b-245c-31dc-b8e7-aa8154e4a20a | -14.68358 | -48.10696 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1986393d-3bae-36ef-9cb0-1fec4b3b9dd2 | -9.92693 | -50.49739 | 2025-10-02 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5165576c-91f7-3b5f-84d8-1fea4b2a770e | -11.62726 | -52.24601 | 2025-10-02 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a987a830-2c6e-3f53-b0bc-7dc9102ba973 | -11.16689 | -47.26833 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4fb675bd-4734-3e41-964a-ee18cc82f107 | -14.8181 | -51.4025 | 2025-10-02 04:51:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 837dda66-992b-3b57-a631-81fbe50fc187 | -11.67814 | -45.3238 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d214df77-e699-39c4-83f7-a2b829292694 | -12.81982 | -47.05492 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2131465a-344a-3cab-8a83-cdc39c789e2f | -12.80942 | -47.02238 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b93d1b4a-538a-39df-8802-5c255580ce25 | -10.54462 | -54.86966 | 2025-10-02 04:51:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e769fa1-5ecb-3b41-a706-53e48e956aac | -13.30642 | -47.85181 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 646ebec2-d14f-3232-b7f6-20ff3a40c60a | -15.03756 | -48.0697 | 2025-10-02 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4487cff0-9024-3fe5-b1f4-348f2d6d4c25 | -11.67527 | -44.2828 | 2025-10-02 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac74cdd0-31c6-3125-aee6-196d26a546d6 | -9.93136 | -43.64942 | 2025-10-02 04:51:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 402eb838-6874-3ccc-80f7-7ba0b348140a | -12.06571 | -47.98542 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 572b7f9f-4882-3b3e-adfd-29ce8200735c | -13.34109 | -47.80002 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20ab4732-c2f1-3391-9756-19a69032bb0b | -9.40471 | -63.69652 | 2025-10-02 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f155c854-2378-3785-87ec-0023242193cd | -12.58764 | -49.89445 | 2025-10-02 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6a3c27d-4cd9-354c-8114-64b85beee436 | -15.99553 | -50.90402 | 2025-10-02 04:51:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d81064a8-e9ae-32c8-b44a-0f4c85d8993a | -12.41291 | -47.49989 | 2025-10-02 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29b64a9b-c84e-312a-94a4-797121786406 | -15.54702 | -48.1802 | 2025-10-02 04:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88eaec8c-98f8-3de2-ad75-62a65014292d | -13.20226 | -47.32981 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f61f3d98-01d0-3730-8165-e1568393706a | -13.18329 | -47.83711 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 023f4de3-4858-3b1a-9463-0cae61d71b8d | -11.00724 | -46.57001 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc611dd4-0c42-341c-94aa-797857369317 | -14.30675 | -45.99866 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| abcc875e-ebcf-3ae6-aec0-3cb60bfa441a | -15.25135 | -49.30457 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0a1fd88b-cf4e-3046-aff5-47ebf66a5831 | -13.94545 | -48.09521 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf9fa738-b06b-33e7-aa34-0f5f227d8d08 | -14.36147 | -45.9666 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ff9f328-a254-3363-ba58-6c4c1a4a74d9 | -15.26716 | -49.30994 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a314876f-12b5-31ce-bfef-6234acb1304d | -9.4062 | -63.68859 | 2025-10-02 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0c7dd2d-7d9a-32d0-8df1-bdad89230f76 | -13.95892 | -48.11051 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ff3c697-a888-3254-af03-aca8eb4d2dac | -11.46633 | -44.96454 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96549fd5-2899-35b8-a85d-2c6b3bcd8a67 | -10.22781 | -50.31774 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 8d98eb5a-ae39-3fb7-928f-50a8b328b9e8 | -12.89795 | -46.92009 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1ea5c7d1-381d-313e-bdbc-f1bf4402984d | -15.2552 | -49.27592 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 935f820c-8b09-35da-ac3a-05c8afbb7ae0 | -11.17729 | -47.25951 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a406eda2-c59f-37d7-91a3-e4c816351c66 | -15.94249 | -43.34387 | 2025-10-02 04:51:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8bd9d752-dd6e-3c59-a16a-64f64092b6b2 | -11.87125 | -49.08027 | 2025-10-02 04:51:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5a55262-2b90-3be3-a28b-3a54779d478d | -11.46631 | -51.51035 | 2025-10-02 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e67d56e4-6fd5-35d0-9af5-b6acc53b757d | -14.3082 | -45.98705 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 759871d7-a2dc-3640-ab71-be6e38d36e6d | -11.14054 | -43.38388 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 441a7cc7-b692-3129-a858-9841e75af0c4 | -9.93871 | -43.72387 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3d432634-20ce-3894-8491-0d988d0e3fc2 | -13.30928 | -47.19702 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d24c1dec-6a64-35fe-b47a-3d31ba47e197 | -13.05817 | -47.01476 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c5563a1-621a-306b-a781-1861818d36e2 | -12.94321 | -48.43025 | 2025-10-02 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 051b5ccc-bfde-39ea-90b3-5f5227ae061e | -13.2834 | -47.25295 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 440a6976-c93a-30c4-9802-258b3f1af9e4 | -11.26628 | -47.81544 | 2025-10-02 04:51:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f232ce4-394e-31d9-a778-4706d91ad0f5 | -13.05755 | -47.0196 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 589139f5-d83e-36bd-a66b-0ee63234d9aa | -14.47557 | -48.40448 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e57ec85f-0cf5-3982-ac43-6de2eaed31fd | -11.0368 | -47.82325 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf000af7-51a3-3bfb-9db1-6797c9c4b60a | -11.59368 | -50.16771 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5e9582e-7999-3ae5-86e8-d52fd674cf58 | -11.86759 | -48.07923 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 05fabf3d-7ad0-37bd-bf13-636205cb2387 | -11.08885 | -47.8208 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15f2faf7-cf9c-3d01-a1b7-db8477a13403 | -13.65543 | -47.30409 | 2025-10-02 04:51:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 535722e9-085f-373f-a0cb-f2dd4afa1812 | -14.65006 | -48.12615 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4dcbd419-6b83-3d6c-a314-15da6ddc60b4 | -14.41917 | -46.08163 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5b96b27-f20d-36d7-addc-a38303d738f2 | -10.83378 | -46.61004 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2c80bd8-a49b-3a92-94a0-1a51aed3141f | -16.00361 | -50.9006 | 2025-10-02 04:51:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ff42c2d2-7f4c-3ee7-b0b6-75d6573c30ee | -10.99748 | -46.60754 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 40.0 |
| e9be7aad-0df1-35a1-b8e0-3327dbca39d2 | -14.98668 | -46.90221 | 2025-10-02 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6695c86f-3492-315d-8ceb-e47b0b101aa2 | -12.42623 | -44.09863 | 2025-10-02 04:51:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27af989f-3517-3a43-9fea-295f7e8e8914 | -11.08969 | -47.81399 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0061ba8e-fde7-3437-a56c-c5089388df9b | -15.40678 | -47.0462 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README121.md)
