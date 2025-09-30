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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c354fa3-5a41-3680-b89a-7de45e3408af | -17.50202 | -43.48191 | 2025-09-30 00:30:00 | TERRA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c6b00e10-f677-39e2-8ab5-bf52e8230cf4 | -15.92752 | -46.21335 | 2025-09-30 00:30:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e841fb5c-5641-3316-bac7-95f8c96ff066 | -19.12103 | -44.76332 | 2025-09-30 00:30:00 | TERRA_M-M | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2f47d3bc-b68f-334e-89d8-329ab1ab5d50 | -15.85601 | -46.23059 | 2025-09-30 00:30:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 0377a29d-c443-3882-b84c-573e89728295 | -16.74615 | -44.92595 | 2025-09-30 00:30:00 | TERRA_M-M | IBIAÍ | MINAS GERAIS | Brasil | 3129608 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f652d033-77eb-3e5b-ade2-982d7dce8d6d | -17.39504 | -47.14512 | 2025-09-30 00:30:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 17.2 |
| ba5466df-1f2c-3b76-b328-ea5794f70143 | -17.09877 | -48.57773 | 2025-09-30 00:30:00 | TERRA_M-M | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4e449cc3-64cc-3c7f-b86c-fba2c4bf591c | -13.02918 | -42.80054 | 2025-09-30 00:33:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 37.3 |
| 6956c96f-6d11-36a9-809b-bc228c234eb9 | -11.44489 | -43.50428 | 2025-09-30 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 810e7eb5-0abc-3ced-90c1-30389e614bc3 | -8.14958 | -46.3943 | 2025-09-30 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f92aa793-3d15-3ae7-b622-027a9877952a | -14.79157 | -48.31706 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 343b0ed2-cc05-369a-8545-31731fcd66fe | -13.73505 | -48.6756 | 2025-09-30 00:33:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 25.1 |
| cc7d0137-39a4-319c-985c-f7b5a29b5378 | -10.63165 | -53.71059 | 2025-09-30 00:33:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| fac2b325-e321-3a2f-80bc-e4e01c11b7a2 | -13.45896 | -51.68597 | 2025-09-30 00:33:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 7519619e-6169-3132-a22f-f7886384701a | -13.79235 | -47.87186 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 730cba66-4913-3430-8516-a3850270428d | -15.30114 | -46.41061 | 2025-09-30 00:33:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d1fc58c6-7e6e-38ad-b631-cf30fe5f543e | -15.04112 | -46.98979 | 2025-09-30 00:33:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 01e3ac17-84e3-3cd8-88cb-8708d4e8303a | -9.9511 | -49.29339 | 2025-09-30 00:33:00 | TERRA_M-M | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a949ad62-ea3b-3644-ae09-7162c189c7ab | -14.6343 | -42.37959 | 2025-09-30 00:33:00 | TERRA_M-M | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 31.2 |
| 6c029765-19db-3777-a905-7109b136ccc9 | -10.89812 | -53.74386 | 2025-09-30 00:33:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| cb971185-bbe4-382e-8b2b-c352cc3a0fbe | -13.22597 | -47.3208 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| e2ec1a01-6f23-3345-85ff-136e8e4701ca | -9.3032 | -54.50507 | 2025-09-30 00:33:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 9357ccb8-2e03-3bbf-a94a-0c422d8947ae | -10.66088 | -48.55075 | 2025-09-30 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| dd66339f-a521-3b01-b0bd-fc7547e978c9 | -15.05015 | -42.66269 | 2025-09-30 00:33:00 | TERRA_M-M | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 24b3601c-22aa-3465-aee8-a841576b5653 | -14.55393 | -48.26662 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 90bc5f94-f468-3e9e-be0d-fa0d0b9b2db1 | -9.75635 | -47.75338 | 2025-09-30 00:33:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4c63090e-e621-3c8b-86e5-6d8ac1d01888 | -8.54805 | -44.67134 | 2025-09-30 00:33:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4fcdf485-3c08-3196-8bf7-dd33126a648d | -11.22006 | -47.2117 | 2025-09-30 00:33:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| bd14dab9-b9d9-3fd5-a2c9-7e8f63e81e1b | -15.38509 | -47.07119 | 2025-09-30 00:33:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 37bd18ca-529b-397d-b1f8-b034f7f92460 | -15.06683 | -45.05963 | 2025-09-30 00:33:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 646f92ae-2232-3651-b8ae-8b2d63b52c4f | -12.8877 | -44.69067 | 2025-09-30 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8024c94c-f1ac-36f8-a093-f3a50f2c8055 | -11.65455 | -47.48361 | 2025-09-30 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 322950f1-6387-3d9a-b09d-762cf2db472c | -15.26974 | -49.49859 | 2025-09-30 00:33:00 | TERRA_M-M | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 0831e74f-670f-38db-ace6-f649678abd14 | -8.4429 | -46.94777 | 2025-09-30 00:33:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 9eda3ed4-e215-31e4-b12b-668343d3e81b | -9.39545 | -54.71262 | 2025-09-30 00:33:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 4531cbe4-c66a-30b9-b20a-057909bf4b01 | -12.77164 | -50.53025 | 2025-09-30 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 9eb3b4e6-7350-3547-8152-a1a4d7dec034 | -13.64299 | -47.32955 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9c295935-056c-39a8-b9d6-58acf77ed343 | -14.04645 | -42.15918 | 2025-09-30 00:33:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 30.7 |
| d97af07d-985b-3dc9-8dee-da2c35ae55e7 | -14.39878 | -47.13932 | 2025-09-30 00:33:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| f737a49b-967a-3124-948f-754b60537ac0 | -13.03147 | -42.81521 | 2025-09-30 00:33:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 55.4 |
| 3a933239-ba9b-3938-989b-07412f2e8760 | -13.74062 | -47.90426 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bb8fe924-4d00-3195-9efe-19e829bcf9e3 | -13.65823 | -43.35984 | 2025-09-30 00:33:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| b7d7b30a-6280-321a-92f7-7be581ae33b2 | -16.06424 | -51.03015 | 2025-09-30 00:33:00 | TERRA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5a60157b-14b6-38b8-87ad-db158d87a45a | -13.66259 | -44.39156 | 2025-09-30 00:33:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 18286881-8297-368e-84e2-324a064285a7 | -11.88719 | -48.02296 | 2025-09-30 00:33:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| da374db2-ecf6-320d-8070-6a800dcda340 | -13.23827 | -43.38502 | 2025-09-30 00:33:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 61aa7c31-5395-3457-86f7-15cdddd30a66 | -15.0511 | -46.98242 | 2025-09-30 00:33:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 31a422ca-d976-371a-9b7c-11c8ee2fa800 | -14.54696 | -48.48477 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 785afb33-6588-36e6-9a6b-72e71a01fc50 | -13.63434 | -42.54298 | 2025-09-30 00:33:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 51.7 |
| ed170a44-2845-3b77-a214-40e0340d571b | -14.69502 | -48.14933 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ccede06c-f753-3c76-8dc7-ef82af18e311 | -12.85707 | -46.98669 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4f2babb0-a6d9-30d3-8b86-19f770d7dad9 | -15.02989 | -42.32888 | 2025-09-30 00:33:00 | TERRA_M-M | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| c107b6e0-eb3d-334a-804d-cb563663e2bc | -12.83113 | -47.00587 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 776e20de-fc2d-3a37-9760-be74b8eeb3f1 | -8.87776 | -46.63335 | 2025-09-30 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0bed17d2-0bc6-3084-818f-2be3eb5a7a80 | -13.60936 | -48.02798 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 10343595-ecd3-3a16-811d-1885f97857ff | -14.72064 | -45.21335 | 2025-09-30 00:33:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 42cb8584-0498-3916-a143-6cf70bb0a25c | -12.23285 | -47.79255 | 2025-09-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f756453f-4fdf-3a99-b03b-fe00e8870560 | -8.92853 | -49.83697 | 2025-09-30 00:33:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aa63907c-a316-3f54-b6a9-5c0c6ebafbcb | -13.82053 | -47.4902 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a0251359-7845-3bbc-8f5a-6ec109b25bc8 | -8.26563 | -45.52013 | 2025-09-30 00:33:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 060f5539-59fe-3f24-b979-b7c1d7064fd3 | -11.75823 | -46.84954 | 2025-09-30 00:33:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 69679ff5-9084-33f0-baf7-eed93c3aed6d | -8.32279 | -50.88432 | 2025-09-30 00:33:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| dbae7816-cef5-30b5-a00b-98373580d3f0 | -15.54178 | -47.86995 | 2025-09-30 00:33:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a92d6cfb-aabe-3d69-a2ef-c496955c7cb5 | -15.24565 | -48.75666 | 2025-09-30 00:33:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7a0a8a99-5a53-3a7d-a7b7-487b1c28f03a | -13.45386 | -51.6809 | 2025-09-30 00:33:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a988bda7-b613-314d-b5fa-de0a67e511bb | -9.01157 | -51.70226 | 2025-09-30 00:33:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d495a046-5949-3aa0-b562-8943cd6e46bb | -15.20453 | -49.55622 | 2025-09-30 00:33:00 | TERRA_M-M | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 7ec86c36-cfaf-371d-9c9a-d9a74e65f938 | -9.32022 | -50.6309 | 2025-09-30 00:33:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| b2f8647f-e966-3994-abca-6d29729247c6 | -11.7221 | -44.43773 | 2025-09-30 00:33:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 2abcf2f8-1a91-34e3-977d-d99b7101ded8 | -13.79111 | -47.86288 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c1526b6d-3e26-3ce6-89f3-0898b707ebfe | -14.69377 | -48.14008 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a60d8836-268f-3200-beaa-d04ad1654199 | -10.10296 | -47.78826 | 2025-09-30 00:33:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 36349c23-9dc1-384c-9084-95013cb1a8f8 | -13.73654 | -54.73793 | 2025-09-30 00:33:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| ebfc0821-0a24-3f1a-a917-4f3074f183ae | -9.37408 | -47.59373 | 2025-09-30 00:33:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 82dce406-b030-3af5-aed7-993639a63ae1 | -13.81372 | -47.89648 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 14392f8a-661b-3a09-803f-d59ed4333021 | -10.80397 | -45.36137 | 2025-09-30 00:33:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dd3f1939-d7e1-3271-a868-8e505d93ac5e | -8.14658 | -46.37383 | 2025-09-30 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| de70cd6d-a280-35c7-a629-9f9dde6789d8 | -12.87808 | -45.17117 | 2025-09-30 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b41ad835-13e9-3127-955a-ed8f7ef9ccff | -13.21307 | -50.96037 | 2025-09-30 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 28b333d4-0f2b-3051-a258-0a32ea65ca68 | -13.01457 | -44.11218 | 2025-09-30 00:33:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 13ba8fa8-9868-343f-adc6-1d11a5d88a13 | -8.06749 | -42.94942 | 2025-09-30 00:33:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 5dd76c5b-1afd-35a0-8ffd-9b7a7491da99 | -14.51149 | -48.42373 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ecd8b3ac-608f-398e-abd8-f5f72c203ca9 | -8.00618 | -47.05232 | 2025-09-30 00:33:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 64f74d43-fe11-388c-a4ac-0fc88fb58737 | -10.72885 | -48.17996 | 2025-09-30 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2411a3a4-9413-3df6-bef9-fc2d8c7089e3 | -14.00867 | -49.62545 | 2025-09-30 00:33:00 | TERRA_M-M | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 15989a8d-708a-3734-881c-6060dc2b792e | -13.84889 | -47.95598 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 51d95c32-3018-3b64-a5ee-6765c56d2ca3 | -8.64665 | -50.20443 | 2025-09-30 00:33:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 63378b52-e7eb-3991-9ce8-990c12757a71 | -15.27732 | -47.88952 | 2025-09-30 00:33:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3fab8d01-79af-3f0a-8faa-1d364465e829 | -14.6973 | -48.23334 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| dd1c12e9-0886-3d97-a110-c613c8531f28 | -8.86283 | -46.5953 | 2025-09-30 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ce822151-1938-3fa6-a735-1c86113d75f0 | -14.70741 | -48.24109 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d57b3241-5337-3170-8ad3-4b2f61d32a63 | -7.2801 | -42.86103 | 2025-09-30 00:33:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| e4e658c0-22d0-37be-99a7-05f4c1bddad1 | -15.46743 | -47.93382 | 2025-09-30 00:33:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 2ab60b2b-895c-39ed-8a72-79e1093e242d | -15.27108 | -49.50883 | 2025-09-30 00:33:00 | TERRA_M-M | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1cba18d0-9ec5-367b-87ca-c1facf9fd6b0 | -8.53251 | -44.67962 | 2025-09-30 00:33:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 95cc6131-3654-3249-99ae-cb7e4ef13037 | -10.60463 | -49.63446 | 2025-09-30 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| e348ab57-3120-3777-90be-2d60c8bcc18f | -15.24939 | -49.71298 | 2025-09-30 00:33:00 | TERRA_M-M | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2d7b5504-c631-3135-b313-e8d7c2d992f1 | -13.63183 | -42.52701 | 2025-09-30 00:33:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 42.2 |
| 26dedd1d-00fb-3260-a613-a988e3c1864d | -15.06096 | -42.66008 | 2025-09-30 00:33:00 | TERRA_M-M | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| b237427a-9de4-3576-8d34-4a872c352bd8 | -8.24396 | -45.5113 | 2025-09-30 00:33:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |


[Clique aqui para ver as próximas entradas](README5.md)
