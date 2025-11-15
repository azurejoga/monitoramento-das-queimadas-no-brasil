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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 868c1ec7-ecd0-35db-9a6f-463f4b6c0dc4 | -10.68619 | -45.17962 | 2025-11-15 04:27:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abfdf24d-dc76-37a3-9218-383a84f1a93a | -10.23594 | -48.07264 | 2025-11-15 04:27:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c31cf361-07d8-321f-a3e9-fc4fd8cbd352 | -11.62088 | -48.59382 | 2025-11-15 04:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e6939c8-0b44-3ce1-90d0-2379749baa13 | -10.70164 | -44.49282 | 2025-11-15 04:27:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ca3b0a5-9ff2-3b08-bc38-437fd3a01be0 | -13.26786 | -48.98124 | 2025-11-15 04:27:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bc770b6-0159-3554-90ad-7767ab5aea67 | -12.44398 | -47.88817 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2abe683-9eb6-3b31-a09b-de9eab65159c | -14.65169 | -46.56779 | 2025-11-15 04:27:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0dac8b31-acc9-3105-86c3-7693c204be03 | -12.80382 | -46.4506 | 2025-11-15 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efe26c78-cbb0-39c8-9af5-01e23ecb40b6 | -11.84256 | -49.21752 | 2025-11-15 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 4afa2cc1-c77f-31c6-8846-0685817a3133 | -11.74709 | -45.33688 | 2025-11-15 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7015e01-8810-3002-8ee6-eb83ad653901 | -11.16183 | -47.44569 | 2025-11-15 04:27:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5271ee31-05b3-305f-8e2d-c5e89fe38416 | -10.49767 | -47.9888 | 2025-11-15 04:27:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fce8a4c-b3bf-3952-bf05-bc41b043e1b6 | -11.9194 | -46.19455 | 2025-11-15 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1442177d-5c0c-361f-b78f-58674b27aee4 | -10.55682 | -44.92625 | 2025-11-15 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca4604f4-5112-314d-b98b-4949c285ba9d | -16.56222 | -47.60907 | 2025-11-15 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14ce0a6f-4856-349a-9e89-88b6b4b3ffde | -10.63549 | -51.76838 | 2025-11-15 04:27:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab1e9e93-a998-35dd-9cba-28d95d0e61ff | -10.84512 | -48.02738 | 2025-11-15 04:27:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 934c0cf0-55d4-3bf1-98c6-f151b67e4b57 | -11.01517 | -49.03975 | 2025-11-15 04:27:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ea9674f-ebd3-3e7a-8a09-0c3516823c6b | -12.79649 | -46.38587 | 2025-11-15 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 006281e6-6b9a-3646-94d9-f7b2613881ec | -17.57981 | -46.6848 | 2025-11-15 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| dfd2ddf0-611a-3f37-95f8-859212e922e5 | -12.68016 | -46.77059 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a93b9079-a434-3a94-b091-923d1cda9942 | -12.79168 | -48.81661 | 2025-11-15 04:27:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec33ae09-c676-3b2c-b845-bdf82bfe0a07 | -11.17063 | -47.45428 | 2025-11-15 04:27:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6053fe2f-6b15-396e-9ddb-8686e0f79097 | -10.69865 | -44.51297 | 2025-11-15 04:27:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 006b6adf-7476-312d-b0d4-ad8b3625e16c | -11.31871 | -48.52871 | 2025-11-15 04:27:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69578cea-d712-3e7f-867d-f8d7461c9592 | -13.2796 | -44.27695 | 2025-11-15 04:27:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67a9daa4-19e7-3eea-8228-3f4b53f33fc8 | -11.7551 | -45.3305 | 2025-11-15 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 15c7185b-ac5d-3ce6-aa50-0182048f4dcc | -10.88748 | -44.93927 | 2025-11-15 04:27:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b0ffa38-4f0a-381d-8871-5377e59a5088 | -12.38878 | -48.10674 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23b2d8e0-d654-37aa-94cd-1554daff6f5e | -10.37163 | -44.71617 | 2025-11-15 04:27:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e69272a-5f0d-3e03-a3b5-d5fe54ccda66 | -10.47348 | -44.85471 | 2025-11-15 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 702e4a58-0fc1-3100-bc37-9064af573f0f | -10.93342 | -48.70264 | 2025-11-15 04:27:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1d5158c-a175-3d35-82ff-6141f37179d7 | -12.87743 | -50.15975 | 2025-11-15 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 284e5fc7-c9b8-32d3-908c-8e3f6dfc09da | -11.3967 | -49.19751 | 2025-11-15 04:27:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4bc857d-004d-375d-9eaa-3ed74ec72d78 | -12.38547 | -48.10621 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b7e72be-3e6c-3414-ac09-23da026ed324 | -11.71685 | -48.87618 | 2025-11-15 04:27:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e78ae858-71a8-33c4-826e-d039a0e875f7 | -10.44762 | -45.07116 | 2025-11-15 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 417ca9a7-79b0-38d7-8db6-df6a0125b8a5 | -12.59658 | -48.33732 | 2025-11-15 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db1fd73e-9177-34e5-ae72-9271aee6ea66 | -10.63634 | -51.76342 | 2025-11-15 04:27:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd967827-9650-3eca-aee5-933438b92747 | -14.91494 | -47.37386 | 2025-11-15 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71fe08f6-354e-3161-9839-a553a225b6b9 | -10.34758 | -45.10703 | 2025-11-15 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05f184d2-c9d1-339e-837f-8ff48e41b28d | -10.10332 | -47.52138 | 2025-11-15 04:27:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d44cc78f-5bec-3faa-b942-008f44b57443 | -11.60924 | -45.09255 | 2025-11-15 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52452bf9-b038-335c-9dec-470acbd52138 | -18.30805 | -46.59905 | 2025-11-15 04:29:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49c1ab39-28fe-322e-867e-e940d878016c | -18.6967 | -46.75936 | 2025-11-15 04:29:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 695ba083-5e91-3f6b-9cf9-8c42348b6ba2 | -19.2486 | -46.45617 | 2025-11-15 04:29:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a89c196a-8dcf-3d5d-ac56-e582aa4ddeb3 | -18.51862 | -45.55994 | 2025-11-15 04:29:00 | NOAA-20 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 81e10d8b-edec-3f77-ba6a-f080f8876e5d | -20.21844 | -47.39672 | 2025-11-15 04:29:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 67ae804d-3a80-39ef-a877-3c0723260182 | -20.215 | -47.39616 | 2025-11-15 04:29:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 15.4 |
| df307329-f026-3122-8568-e9df85f0aab3 | -16.9883 | -51.60636 | 2025-11-15 04:29:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb424eff-f4e5-3e13-a9af-c0c5a801c1d8 | -19.24871 | -46.45502 | 2025-11-15 04:29:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f09615a-83c8-31e1-9807-c5f744225942 | -17.62248 | -49.33728 | 2025-11-15 04:29:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46c5882d-482a-31d3-94d6-294f089f219b | -19.08344 | -46.65171 | 2025-11-15 04:29:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ba28e640-dc43-3958-a952-69cacb41c236 | -18.59512 | -43.99123 | 2025-11-15 04:29:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c410f453-21f6-3a46-b006-4c4eff29f2a5 | -18.33743 | -47.18748 | 2025-11-15 04:29:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a28bcb7e-090f-3541-bbfd-9fef5d0eebdd | -18.33402 | -47.18695 | 2025-11-15 04:29:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dcc04c27-d9e0-35ff-83e6-61ee7a65e6f7 | -19.19733 | -47.87249 | 2025-11-15 04:29:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12498405-efb4-330a-b1b5-9d312ee81b1b | -20.21901 | -47.39274 | 2025-11-15 04:29:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 7b0b81fe-87c8-31dc-8156-02e153e0c0a1 | -20.21157 | -47.39559 | 2025-11-15 04:29:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 15.4 |
| ca63763d-9d4d-342e-8e7f-f901f49fab98 | -19.19397 | -47.87193 | 2025-11-15 04:29:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd0afe80-5acc-3ca5-b3d0-1441e9078968 | -18.35151 | -47.25701 | 2025-11-15 04:29:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fe3c9bc-8d02-3aef-963e-9037de27d6d6 | -18.59958 | -43.98838 | 2025-11-15 04:29:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 248d9a08-e216-3e48-ba7f-147b0a7b66f9 | -17.83864 | -50.8157 | 2025-11-15 04:29:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bf98280b-74a8-37bb-b62a-60602812046d | -17.56919 | -50.66278 | 2025-11-15 04:29:00 | NOAA-20 | SANTO ANTÔNIO DA BARRA | GOIÁS | Brasil | 5219712 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fdc22ce-8cb7-3255-8599-7078423feb63 | -18.48424 | -47.51867 | 2025-11-15 04:29:00 | NOAA-20 | DOURADOQUARA | MINAS GERAIS | Brasil | 3123502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30c1566c-64d0-374a-b4e9-142f798d5113 | -18.34811 | -47.25645 | 2025-11-15 04:29:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ab1c91df-6309-36b6-8dab-0be6a787409b | -18.33061 | -47.18641 | 2025-11-15 04:29:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 029ebf6c-4dd3-3193-b286-a6d0968a9e66 | -19.19341 | -47.87568 | 2025-11-15 04:29:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e45364e7-effa-3649-a683-c2d12d7a67b7 | -18.59911 | -43.99189 | 2025-11-15 04:29:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50ff58d3-c4df-3bbc-99ae-058bb12ccb05 | -18.33004 | -47.19025 | 2025-11-15 04:29:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 44a732d4-ad12-3023-b8ac-059ae8aaaac3 | -18.4848 | -47.5149 | 2025-11-15 04:29:00 | NOAA-20 | DOURADOQUARA | MINAS GERAIS | Brasil | 3123502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c525f84-1e13-3e18-b3c5-23cdaa8a4e69 | -20.21557 | -47.39218 | 2025-11-15 04:29:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 91bbc3a7-b0dd-36ba-8506-1b28d147c411 | -18.33345 | -47.19079 | 2025-11-15 04:29:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb13ca77-7cdb-3e27-8125-217d92fe28dc | -18.34085 | -47.18798 | 2025-11-15 04:29:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4f4eb2b1-4315-3bd3-86e5-8f1ac1732158 | -18.27144 | -43.07428 | 2025-11-15 04:29:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 654b590f-0bbc-3472-b043-033de5350e75 | -19.07995 | -46.65108 | 2025-11-15 04:29:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83a010de-0aff-3cfa-8cbc-73a215cbf7f9 | -19.51121 | -45.87148 | 2025-11-15 04:29:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 584d5c3b-19df-356c-8f64-0b84226d551c | -4.5381 | -43.2107 | 2025-11-15 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| ce43421a-999d-3e11-9a3f-96819123b28c | -5.2397 | -44.3448 | 2025-11-15 04:30:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 03cb562a-52d3-3dc1-821d-052259af9937 | -4.7342 | -47.1547 | 2025-11-15 04:30:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 25c28d25-37d1-3180-9f65-8c097576d8b3 | -11.8486 | -49.2218 | 2025-11-15 04:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 5dfde1b8-d501-3f4e-8d7e-7495662ca592 | -11.849 | -49.2 | 2025-11-15 04:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 8492c64e-6023-3d3b-b52a-e00c8433832b | -11.8486 | -49.2218 | 2025-11-15 04:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 818a6fbe-df9b-373a-9200-38a97b5d8be8 | -5.2397 | -44.3448 | 2025-11-15 04:40:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 0e0f5fe9-5392-378d-920a-b02aeb5f8ec2 | -11.9175 | -46.2135 | 2025-11-15 04:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 0d045089-a6c6-3591-916f-f0bfa201810e | -8.0703 | -43.0981 | 2025-11-15 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| 5c0ce2ef-d4d0-383b-8f53-3714670c00b3 | -4.5381 | -43.2107 | 2025-11-15 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 8a26f685-47f0-35d6-bd11-e5d40eeda43b | -11.849 | -49.2 | 2025-11-15 04:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 3b7cf4f6-38f0-3213-b2bb-8ce4cbdd674c | -8.0703 | -43.0981 | 2025-11-15 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.1 |
| a45a81c6-0ebd-3f53-89af-f68299b00e43 | -11.849 | -49.2 | 2025-11-15 04:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| a9bd0c44-71e3-39b0-ae4b-3444b3f2e254 | -11.8486 | -49.2218 | 2025-11-15 04:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| b1a60894-0b0d-3416-a15d-fcecfe55d28c | -8.0513 | -43.1001 | 2025-11-15 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| 5a8eeb44-3159-3463-a918-c95c7f6e324a | -8.0516 | -43.0765 | 2025-11-15 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 49.7 |
| a7b1920a-91fb-3495-a696-510fb3224ce1 | -8.051 | -43.1237 | 2025-11-15 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.8 |
| acbbf8b8-e414-35df-9c64-b38c725edb06 | -11.849 | -49.2 | 2025-11-15 05:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| dd61134b-5e65-37a7-ab1d-0cb5fb5c9c7b | -11.8486 | -49.2218 | 2025-11-15 05:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| a71628fc-e5fa-3fef-ab6b-94dc23faf34e | -8.0703 | -43.0981 | 2025-11-15 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 356.6 |
| bdc6de0c-a97b-349a-942b-77f94b7dfdc6 | -8.07 | -43.1216 | 2025-11-15 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.1 |
| 17e3774c-0003-364d-804c-aaacdb5c9b4c | -8.0513 | -43.1001 | 2025-11-15 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 256.1 |
| 0324f7a2-e01a-3700-b229-13263193b4ea | -8.0706 | -43.0745 | 2025-11-15 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.4 |


[Clique aqui para ver as próximas entradas](README50.md)
