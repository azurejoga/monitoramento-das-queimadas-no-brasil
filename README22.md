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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1d8c27c-7150-300c-988d-0e33e1121ce2 | -3.89403 | -47.17889 | 2025-11-08 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61f85600-7919-38a4-b8cb-77f05f5bc49c | -2.52306 | -49.45183 | 2025-11-08 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fa9f68a-438d-339d-bc28-83e2a0cca12e | -2.46899 | -49.23064 | 2025-11-08 04:36:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| add5c690-628f-3492-b2c7-41e5836501dd | -3.52534 | -47.54186 | 2025-11-08 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 87654207-eb3f-3615-86ec-a8cc5b2ef45e | -4.7581 | -45.78049 | 2025-11-08 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36927048-2ca3-3b9a-883b-34433fcd3fa4 | -4.42705 | -47.599 | 2025-11-08 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b4351ba1-c81f-37fa-97ad-fd9ad188c475 | -3.98721 | -45.96018 | 2025-11-08 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| acc80aab-3ab6-33bb-9902-1a4ed161b848 | -7.48551 | -45.92294 | 2025-11-08 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33a5f913-ff1d-3225-95ba-6603804e5eff | -3.35495 | -45.28936 | 2025-11-08 04:36:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f52726f-7a0a-3958-a9a8-7f8609faf484 | -3.09015 | -50.32281 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0550ace1-450a-3100-8f76-8b920a0b619f | -2.98669 | -48.70601 | 2025-11-08 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b789f10a-928f-3ded-8110-0285c08d2cae | -7.79928 | -46.65182 | 2025-11-08 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54481b96-c5b9-36a5-a138-4a7cf55cd44e | -4.83064 | -48.55203 | 2025-11-08 04:36:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d19bc5dc-48a1-3751-9dcc-c1f1c88a2d22 | -3.87091 | -49.91167 | 2025-11-08 04:36:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07c47380-5570-36e7-ad20-a9fb7ad947a7 | -6.05324 | -39.14569 | 2025-11-08 04:36:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3f98c0cf-b5a2-3928-8615-ae302f03a637 | -3.40247 | -45.43236 | 2025-11-08 04:36:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b1cdfc4-0f15-3687-9f76-08f94d73df2d | -2.63078 | -49.18632 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0b6dbee-417f-3bc8-99a7-92f2c40e92c0 | -3.14844 | -50.60873 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fcaacec4-d62e-3a64-84ae-766661b7b4a6 | -3.59184 | -51.23222 | 2025-11-08 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62446d6e-c2f0-34c8-b0ac-5bb8182c7311 | -7.55169 | -41.65935 | 2025-11-08 04:36:00 | NPP-375D | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| b2d524a1-b213-3ab7-bb81-334aef5fbc5d | -3.35452 | -50.20981 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa765a1a-607a-3717-9ef1-40af9a6cc94e | -3.77016 | -44.29004 | 2025-11-08 04:36:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6a1864a-a6e9-3fb7-a967-81bca027a33d | -4.90826 | -45.10514 | 2025-11-08 04:36:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7029ea6f-578d-3729-a0a3-a0e7c63b1bfb | -4.38677 | -45.67889 | 2025-11-08 04:36:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2697c32-8a63-36ac-9d79-69ba697cf51e | -5.03439 | -45.17537 | 2025-11-08 04:36:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1364e6c4-122d-33f9-a8cb-b1db461ba00c | -4.2262 | -39.17273 | 2025-11-08 04:36:00 | NPP-375D | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 60296a42-5aeb-3603-a4f0-1f523d538c5e | -4.63721 | -46.19904 | 2025-11-08 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f3d418f-7ac9-347e-98ef-e0c1309d84b7 | -3.0603 | -48.7251 | 2025-11-08 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47cdf937-22bd-3e15-a47e-10a2d3f495c5 | -5.28273 | -44.41382 | 2025-11-08 04:36:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5ee0316-82c3-3efd-a4a6-5f5ba41d08c7 | -3.25751 | -50.14001 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c1d063c-aaca-3178-9d32-81e0e45aa7a9 | -3.39313 | -52.65384 | 2025-11-08 04:36:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d98def4-c5d6-31d7-a243-ec519ad2c802 | -7.79588 | -46.6513 | 2025-11-08 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3baf045b-54ef-3e1f-a8d9-9404ab5f7ef2 | -3.40468 | -50.271 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e6eae28-c0e4-3258-8a06-5c76f811843a | -3.40532 | -45.43657 | 2025-11-08 04:36:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8b93fccb-211b-3f5e-8592-aa008efe93e7 | -5.91362 | -44.5268 | 2025-11-08 04:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1089a98b-c280-374c-948b-49f680c23cf1 | -3.52813 | -47.54576 | 2025-11-08 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ffb22db4-10bc-3dd2-849f-9db44cbe4ef9 | -5.16348 | -41.22645 | 2025-11-08 04:36:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 995de5e3-771d-39db-a5d0-64e57590a996 | -3.45162 | -49.84828 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d57c1330-497c-3151-ab78-4aa341c7b11b | -4.46868 | -45.50936 | 2025-11-08 04:36:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e55d555f-228b-3a0e-86f5-c7c9ff415d8b | -3.8428 | -45.85328 | 2025-11-08 04:36:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d75a5173-db58-3fdd-b766-648ec5dfe3e3 | -3.41215 | -45.43763 | 2025-11-08 04:36:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f0e48f58-3312-33f8-b8ea-d594d5f86ab9 | -3.65168 | -50.26541 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcdb1f71-6f79-32ca-9646-7b1dd44a8d0b | -5.10235 | -43.98973 | 2025-11-08 04:36:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3365d7a2-160e-34b8-8f26-5ab8008fe699 | -4.53604 | -45.61858 | 2025-11-08 04:36:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ab0a1c3c-f19d-3648-b253-0fd1fbbcbbef | -3.35191 | -50.18008 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5038be3f-4708-3a45-a65e-cf1034972210 | -4.68224 | -45.84396 | 2025-11-08 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb076327-5d04-31c6-8254-aa9fbb9af91c | -8.0742 | -47.12246 | 2025-11-08 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26e9d687-4da4-3748-9226-885412884fe0 | -4.90048 | -45.62784 | 2025-11-08 04:36:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a788ae3-487e-31f3-8d4c-16494282d02a | -3.3361 | -52.56021 | 2025-11-08 04:36:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca3595c6-ba41-3de4-abb9-a2d6ca1f7bda | -4.69301 | -46.4004 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8f0e3537-2998-3047-a3d5-fa656d2b7824 | -5.37629 | -44.72986 | 2025-11-08 04:36:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86a72b9a-2b6b-3230-a410-af88277b8380 | -2.5081 | -48.26351 | 2025-11-08 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5643737-4353-3bcb-8f81-2b524cb32cbf | -7.79195 | -48.52742 | 2025-11-08 04:36:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96c4dfe8-b47c-3bfa-9e74-e4b6a7ad21ea | -2.4157 | -48.86927 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08d8e341-d586-31ca-85d6-fb5eb6e7ac7d | -4.83067 | -45.60598 | 2025-11-08 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d3f0668-e653-3691-814d-5b7b10460080 | -6.34328 | -39.84571 | 2025-11-08 04:36:00 | NPP-375D | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 131621bd-c27e-366c-85cc-a98054bc9918 | -5.65077 | -43.01285 | 2025-11-08 04:36:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fd15180d-79cc-371b-b947-a4bd18b78997 | -4.28785 | -45.88808 | 2025-11-08 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f6c98e4-f6c1-3ade-aed9-e0c1790a6b0c | -3.63848 | -43.65346 | 2025-11-08 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 606a5071-ec66-305e-8d23-7d905e69d727 | -4.65155 | -46.86106 | 2025-11-08 04:36:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bec5fd0e-493c-3f1b-9a5e-3a71e23f31c6 | -2.62632 | -46.85244 | 2025-11-08 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6facf3c9-c1b9-3fd7-b7cd-6936d2713b8d | -5.2422 | -46.17054 | 2025-11-08 04:36:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ad795f3-79b4-3c4f-809d-aea0d8047970 | -3.34144 | -50.19933 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e9c492da-ca4e-3b05-a6bc-d0d5fb10a013 | -5.94018 | -38.18325 | 2025-11-08 04:36:00 | NPP-375D | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3c1e2e2a-538f-3336-95af-2636c208255e | -2.52367 | -49.44795 | 2025-11-08 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d42cc57-cfb8-3acb-9c5e-c66c82670056 | -5.91413 | -44.52519 | 2025-11-08 04:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7ffb45f1-d24c-31dc-bfc2-2d2f4358252b | -3.67923 | -52.09503 | 2025-11-08 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4540f44-58d4-306c-8125-234d93ad464d | -3.51606 | -49.94399 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ba0f5965-7866-3f8f-87d1-a5470f2c2106 | -2.97035 | -44.58779 | 2025-11-08 04:36:00 | NPP-375D | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 06f5e1f4-3781-3cad-b1ad-45a8e714ad64 | -3.63544 | -43.64851 | 2025-11-08 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| caedae6b-5497-314c-88ac-a9371f5f52e0 | -2.93487 | -48.76914 | 2025-11-08 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28c27aa8-8111-3206-93fb-0a001ee696ac | -9.09744 | -44.31863 | 2025-11-08 04:36:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3f921c8-9252-380f-b5ab-acc07f22dcc8 | -3.47483 | -48.97654 | 2025-11-08 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b9851fa-bfc3-3d66-baba-4b6b51207fe1 | -3.15417 | -50.29457 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5071be70-7c63-31e9-951d-59d79ea24ec9 | -2.46652 | -49.90215 | 2025-11-08 04:36:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 916bae0e-2bf3-3b50-aa64-eb8f20609c15 | -2.98329 | -48.70546 | 2025-11-08 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7bec9945-d5b5-3081-bcf2-614f81b11f08 | -4.27559 | -48.33788 | 2025-11-08 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3bff73fa-68ba-3d43-8d64-bd77508cfc71 | -4.27826 | -46.30719 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6c9d91fd-a2f5-3ce4-a583-7279eb1c1897 | -4.55208 | -46.16051 | 2025-11-08 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0dc0140c-ce00-31a9-9c85-c6705cd9ae87 | -4.601 | -49.36063 | 2025-11-08 04:36:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bf60f7e-fd33-32d0-a485-dbec68353622 | -3.3578 | -45.2936 | 2025-11-08 04:36:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2808d8b4-8a36-3c9e-a102-82936146bd7a | -3.73406 | -49.68723 | 2025-11-08 04:36:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b9c95dc-a118-397f-80ce-b0d14f96599c | -4.07806 | -44.57686 | 2025-11-08 04:36:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c078780f-6c0b-3e78-b0ae-3432f485ca7e | -5.91049 | -44.52466 | 2025-11-08 04:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7de7c3a4-5c41-3804-923b-b5140012addc | -5.08517 | -45.10323 | 2025-11-08 04:36:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10ec7043-6733-35c8-9ced-5c60ac57bb3f | -3.93622 | -45.41508 | 2025-11-08 04:36:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca99799b-c103-3335-b17a-0c00f8c950aa | -2.70048 | -48.97068 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7806b985-afee-3819-8835-0cd60df4c085 | -5.41622 | -44.82708 | 2025-11-08 04:36:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 951193de-7142-39f9-960b-badc7a2b5d2d | -3.87133 | -49.91213 | 2025-11-08 04:36:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fea2ace-7a3d-3912-b6b2-d3b62b078243 | -4.97811 | -44.81736 | 2025-11-08 04:36:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0ad5d7e-5a86-3d19-8157-5da2c66efb73 | -3.14397 | -50.28864 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e22771f-73bd-3945-9b32-28d935f23529 | -2.72038 | -49.16872 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73543edb-e58d-34b4-92b5-4a6ce4fcea9d | -5.6161 | -45.04694 | 2025-11-08 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75481bd7-e10d-3588-8a5f-02d5f5757fa4 | -6.36872 | -42.38469 | 2025-11-08 04:36:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d7961911-25d3-3f7f-a1ec-263e06639b21 | -4.35993 | -48.65932 | 2025-11-08 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 728b726e-98e1-30a4-8bb1-ae70174c59bf | -6.07619 | -44.0527 | 2025-11-08 04:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 31bf7f77-b23f-351b-bec9-a7edae7d98a7 | -3.06515 | -50.4311 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 217a47ce-0575-3d6e-b091-704a9d1913a5 | -2.61371 | -49.22631 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbb4d80c-c216-3d69-8e2d-da9bd9117653 | -3.25836 | -52.84518 | 2025-11-08 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e82a1da4-afc8-3d20-89ec-d74f99f7d19b | -8.33037 | -46.25792 | 2025-11-08 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README23.md)
