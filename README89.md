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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c05b5311-caa2-30aa-a9e7-d5512251183d | -10.33972 | -48.22797 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 681324bc-f3f9-33cb-a1ac-b030acc8bfb2 | -9.96396 | -48.80222 | 2025-09-30 05:08:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 580228c9-084b-3b38-a183-c65651f5b5d8 | -9.31436 | -54.51226 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2525a0e-adfb-3ba8-88ce-51d548c739b8 | -13.1526 | -47.42399 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3154d14a-8870-3b0d-8e81-58d074442342 | -12.83663 | -46.97667 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a7defcf-948c-3b2b-8a21-52dd5096f068 | -11.19312 | -47.24335 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5386ae4c-60dd-3b99-8ebd-a575ebb45e35 | -8.86573 | -46.66355 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ecab1081-5370-358d-aa8f-c11d4bbf8a89 | -5.78025 | -51.75595 | 2025-09-30 05:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 717a9025-ab4b-300e-a62d-e847f866f27b | -8.94662 | -51.69336 | 2025-09-30 05:08:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c16a8cab-6142-3c9a-8dff-efb2d3a80ad5 | -7.91432 | -44.62093 | 2025-09-30 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 545f1d42-1bd6-340d-9a1b-f90277fa2d1c | -7.84354 | -47.26156 | 2025-09-30 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22ef0853-c433-32d8-bcbf-aeeabe7bc97b | -13.22449 | -50.92966 | 2025-09-30 05:08:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b28daff0-d4c8-33af-81a4-9b67bd2ec866 | -9.41931 | -54.71607 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39135efb-3758-3e3c-ab52-f99ceaf100cd | -9.51566 | -47.69641 | 2025-09-30 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66839c4d-8020-384a-bbe9-3b32225036f4 | -13.40414 | -47.54701 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0798d1dc-e114-3da7-9570-8bd2b1e7e5ec | -13.21563 | -50.92844 | 2025-09-30 05:08:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 250614f5-89ad-3b9e-b701-b0d1129f8889 | -12.78722 | -46.90054 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1184b443-d40c-38e5-bc7e-c7f617cbb41c | -8.15395 | -46.38594 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1e130a1f-8783-30e3-b4f5-eecd08b012f9 | -12.6966 | -45.2919 | 2025-09-30 05:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2be667fe-98b7-311c-aefb-47fca7940e7d | -12.75233 | -46.84891 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f709433c-850b-3e42-961e-23118f0b24e6 | -9.12835 | -47.64074 | 2025-09-30 05:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0f129d2-639f-3bbb-b583-087070d36301 | -8.89728 | -50.59162 | 2025-09-30 05:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc788460-6cd4-367d-8d92-ba016c4d241d | -11.75928 | -44.74886 | 2025-09-30 05:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f304c043-54c1-37a4-b2ec-0415485750c4 | -7.29913 | -47.29963 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b00d8923-cc30-3c87-923d-94ce85c644a4 | -6.3748 | -45.63195 | 2025-09-30 05:08:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e0a2614-ed35-3e2b-aaf3-0429aced6e37 | -9.42559 | -54.72086 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b09fe54-ab87-3a99-8359-6910a54eb948 | -11.89478 | -48.05024 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 123570c7-5a5d-3b09-8d61-3cad2c827eb2 | -12.83616 | -46.98066 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77f19a87-06b4-3a11-a223-bb67b3e7fa12 | -10.63368 | -53.69365 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7735f129-b84b-3b02-83e0-4c5d0a3b7185 | -11.1534 | -54.12436 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 9c3fad9e-f031-3ddd-a0bc-7194bedc13dd | -10.40978 | -48.17231 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c20df72f-e990-3fa7-b8ef-276b1498a7f0 | -9.4096 | -54.71074 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73af4411-0753-3116-99d1-649dbe9e7052 | -9.75212 | -47.75572 | 2025-09-30 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8986408-57a3-3fd7-81c2-846573a4dc44 | -7.76667 | -45.75754 | 2025-09-30 05:08:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 94375ef3-b0c5-372d-bb30-2c61b7beeb4b | -13.07156 | -47.07408 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7b061e6-4d80-300b-90fd-804bfc0dd314 | -7.91565 | -44.61055 | 2025-09-30 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fd7791f0-51b2-3f22-b907-f5e54b83ae56 | -7.30434 | -47.30043 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e32efc2b-02bb-3087-a1ef-535e65e60348 | -10.95633 | -46.49147 | 2025-09-30 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9085abde-623b-3a18-a55c-be0084a393d9 | -6.52018 | -45.22178 | 2025-09-30 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c30d6197-21d1-3f23-bc8f-fd002042fab1 | -11.17152 | -47.2361 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ee4e4d2-4b6a-3cf7-8502-6421105cf36c | -7.04186 | -46.41483 | 2025-09-30 05:08:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee19cc8b-b2d0-3180-9c77-9c66e0e3c036 | -13.39653 | -48.06804 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c5c51fb4-a12f-3de8-b259-1d6640f4ca7f | -10.75486 | -45.38657 | 2025-09-30 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c57ec00-eef1-397b-8df2-1684ca65e354 | -11.20069 | -47.7488 | 2025-09-30 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 547e8ebb-3307-3c8b-bfc5-8b0bbd98d88a | -11.06719 | -47.82988 | 2025-09-30 05:08:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c952ec10-617d-30dc-9e1f-d4fb454ff938 | -9.31902 | -50.63297 | 2025-09-30 05:08:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7adad0bf-0710-30ea-a279-3f53fe2b2d5d | -12.23441 | -47.80245 | 2025-09-30 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 39ae74df-1081-3958-b979-90ebdae37b7f | -11.20397 | -47.7425 | 2025-09-30 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43dda891-5f45-3e16-9fc6-945a804e0ef0 | -9.41475 | -54.72297 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b3b9dd8-f46a-3003-84cc-4505539d1b2c | -8.44142 | -46.94454 | 2025-09-30 05:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 46433fc4-8984-386a-9c6f-780f16dbb2dc | -6.7414 | -45.62514 | 2025-09-30 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f02e2a2-bc05-3801-b537-b6cb641195d0 | -10.19184 | -44.88198 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0abc5954-947f-3b1d-99de-86b59a57bff2 | -10.18351 | -44.89689 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 51477998-352d-31c9-ab73-f0ae1c3fc6ce | -11.26196 | -47.22171 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de905b76-a260-3c89-aa92-a63548f11f6f | -10.19754 | -44.88795 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a6c570d6-f711-300e-8f5d-e28bd350385b | -9.40901 | -54.69158 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56ded2d5-a092-3744-baf7-26e0dc10849f | -12.2242 | -47.79623 | 2025-09-30 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 388e9932-6aaa-3590-8f24-54eeea936919 | -12.87397 | -46.95767 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c5c7ed13-fd0d-332c-9aa5-01e4d915b026 | -13.15822 | -47.42467 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e66e698e-45b9-3c0e-92ed-272e77ef9a10 | -13.58294 | -48.05464 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| eb703012-ac00-35f4-95ef-c9879a3af392 | -13.36826 | -48.16378 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83c38401-1b6e-3432-830c-9cd04d7d0379 | -11.25575 | -47.2374 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d508a6e8-ce6c-3d32-8442-6edb8e3c243e | -9.06062 | -46.7109 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e1d422e-9adf-3858-b8ed-1528534511dd | -12.22453 | -43.75178 | 2025-09-30 05:08:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6bcef99-8a06-33ee-bd47-437332918d9e | -11.21389 | -57.02088 | 2025-09-30 05:08:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c912d051-e8ce-3d9f-8cad-2aaf695ac589 | -12.44614 | -54.47151 | 2025-09-30 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e187ce55-ff07-354d-8e55-7d9588fad575 | -13.00651 | -44.11864 | 2025-09-30 05:08:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00dfcc0d-81fa-391b-961a-e9b562c1702d | -9.4677 | -45.48974 | 2025-09-30 05:08:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c14296c-07e8-376f-b10c-ab55390ee544 | -6.82114 | -48.70828 | 2025-09-30 05:08:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0626081d-f70f-377e-9eef-12aef9af8bd6 | -11.46059 | -45.01233 | 2025-09-30 05:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 12fc9570-9ee7-3fc7-b18d-f85bd35cdb16 | -11.88713 | -48.02585 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7338979-1f12-3e05-863c-88acce999254 | -10.65934 | -48.54207 | 2025-09-30 05:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad2ec0c3-1de7-3e94-a8e8-67c92c2dcfd2 | -11.74789 | -44.74426 | 2025-09-30 05:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ba4db47b-8855-3940-bf32-13703de1cfb4 | -11.2865 | -47.81987 | 2025-09-30 05:08:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8f6b18b9-610d-3181-9ff0-5e4a5d42ab13 | -5.98895 | -51.90342 | 2025-09-30 05:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2175863b-992e-375d-8809-85fcb80e3952 | -6.46985 | -44.21836 | 2025-09-30 05:08:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fc8b65b-3455-3ea7-86f5-64bb07f16246 | -9.89415 | -57.93347 | 2025-09-30 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8f061bf-e5eb-32d7-b457-d62b798cb400 | -10.39989 | -48.168 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1df37959-ac0e-37db-b055-219e309bb961 | -8.71253 | -47.98928 | 2025-09-30 05:08:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e9da023-a995-32f7-bf99-f5d0c7d7cd03 | -11.14332 | -54.11866 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b830c8f3-eac0-3b96-9893-aab54d2efca4 | -13.22006 | -50.92905 | 2025-09-30 05:08:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f31201b1-0fa3-3b2b-8bcf-8b7c867b6df7 | -10.99611 | -57.05032 | 2025-09-30 05:08:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be1ae687-a1ed-3b15-8def-19a90c9e6f21 | -8.26502 | -45.50842 | 2025-09-30 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 325c0856-ce75-3a77-b853-8e248df42be1 | -6.50836 | -45.21996 | 2025-09-30 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea1139ca-8953-3ab9-a4a2-0d24acf917b6 | -11.88712 | -49.91098 | 2025-09-30 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ee145cc-dd27-3488-aecf-be4d701533bd | -11.28695 | -47.81645 | 2025-09-30 05:08:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c7a7f74f-b68c-3101-b12c-8f6dba26033e | -13.36805 | -47.31694 | 2025-09-30 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 25ebd52d-d9e5-3db7-8b10-916bcbfbe37b | -7.36553 | -47.04862 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdc1f8c9-0067-3bb8-b266-2c1d609ec49d | -12.96149 | -46.86798 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25806aac-7e0f-31d0-b86d-2f22285fe1c8 | -11.39874 | -55.05856 | 2025-09-30 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b4ff0bd-983c-3f79-b4ee-fe352fedb053 | -12.80049 | -46.88531 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1eefd0c5-2e59-3e24-bf1b-244fe0d5a05c | -8.07505 | -55.221 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91fff3d8-3ef0-36d0-a2b7-e8c3cf01b093 | -8.64614 | -50.1987 | 2025-09-30 05:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe7724d0-caa7-3f85-bc0c-dbdf1f024185 | -11.7156 | -44.44236 | 2025-09-30 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dad50268-deab-3507-b297-ad0ad2905ff6 | -13.20559 | -50.93601 | 2025-09-30 05:08:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3276637-17a9-392e-a0a3-92c9569c78d8 | -8.32825 | -50.87604 | 2025-09-30 05:08:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 26dd79f5-5f17-3706-b4a5-4772616a4229 | -10.40706 | -48.16961 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45de813c-9b51-3178-9939-574ef67f2722 | -8.87228 | -46.65692 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e2a2dfb0-02e9-3027-93d8-340e2863883d | -6.86482 | -45.62529 | 2025-09-30 05:08:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ad23eb2-639f-36bf-a3a4-75506a73996e | -9.40445 | -54.69851 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README90.md)
