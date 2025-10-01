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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1186c18-ec3c-31e4-be65-07b66edbaa02 | -15.53741 | -45.22823 | 2025-10-01 04:21:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6c77894b-040d-3ed2-860a-c68a8a37c694 | -12.22319 | -43.75555 | 2025-10-01 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2ecbb0c-e373-383f-9651-84da0a4d30f5 | -14.02229 | -46.32204 | 2025-10-01 04:21:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 446b01ea-4b25-381d-ab13-215ee3820b14 | -11.83748 | -44.96638 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5ba2267d-c4d7-3142-817a-962fe53bb32f | -14.74812 | -45.78329 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48738e35-1ec5-3663-8958-673c8073e514 | -11.62972 | -47.49536 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 03da9e85-06e7-3cdb-98b3-90801287cf25 | -14.39583 | -46.2162 | 2025-10-01 04:21:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da72f401-a167-3af5-a4df-ba1d1321fbbc | -15.80417 | -43.32085 | 2025-10-01 04:21:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d1cabae-3be8-3c90-ba94-4a337b6c530b | -13.81515 | -48.02539 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b45c7184-9f87-3f56-8959-5a59c9a47752 | -13.06811 | -47.08587 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02c5eab2-42d7-3413-b898-42d1205d1abf | -10.96449 | -46.54967 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aeadd8d6-da1b-3e52-8bbd-fad3f6f5a851 | -15.27993 | -47.83669 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2712963-96e3-3901-a892-80721e4625f4 | -12.84376 | -46.86978 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1143760f-1944-329e-b41b-4546988263dc | -12.77622 | -46.86608 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9a9ffece-8ff5-396e-8feb-67f3c2681698 | -11.68152 | -44.28805 | 2025-10-01 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8ed239b-356d-33e5-b08e-b6f466936c3d | -12.78288 | -46.9108 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a98e6bb-2989-3a61-8594-84724de8fda8 | -14.3493 | -45.92459 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 931505a6-acc9-382b-8fe7-410f9d276896 | -9.32302 | -50.62811 | 2025-10-01 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 172bd539-3683-3436-b876-a83df1f96434 | -11.96236 | -46.59045 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a211c7f-5749-3f57-b4c2-bb3bc22c598c | -14.50986 | -48.48363 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a65745fb-9d27-3939-9404-135a60577260 | -15.23444 | -48.73872 | 2025-10-01 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bda27b39-7fa9-34c3-adcd-ce70f67e3ee3 | -11.58248 | -47.65757 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f2a2085-4f5e-30b0-ba72-122763590c37 | -11.54405 | -45.06182 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4f8244f-b5e5-3e73-94b4-90c85f6eea7a | -11.76013 | -46.85508 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c7db70f9-68b4-34a9-a804-04bff888da5d | -15.94712 | -48.11479 | 2025-10-01 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f48d82d-cbca-3f09-9a79-f0bedd2635cc | -14.79617 | -45.80235 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 039cc1ef-a31d-394c-90d2-e4643adf5345 | -13.06536 | -47.08175 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4891d62-62ed-3c51-ae1c-1030f11742d3 | -10.25528 | -44.95224 | 2025-10-01 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0299f668-6a44-3805-90bd-83864b07b24c | -16.57973 | -45.11625 | 2025-10-01 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd6ea2ca-0c1f-3344-ab9b-712dd924e66a | -12.66338 | -46.86904 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ef427803-c7cb-3270-bd1b-372797222296 | -15.25129 | -46.96817 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b781626-3fe5-3940-abef-aaa7b86e1ee1 | -13.8504 | -47.93663 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58a4b334-eb96-395a-af0c-a2d9fe28f9ad | -13.02802 | -48.67738 | 2025-10-01 04:21:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08fafbaf-ee79-3e6f-8cb9-01a4f71fb1d7 | -10.73332 | -48.18034 | 2025-10-01 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c28f033b-d90e-3407-a860-e2126281a388 | -12.01686 | -46.63186 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf23dd41-3198-37d7-971c-858c1bca388a | -13.78101 | -48.0118 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8303eeb4-b98a-30ef-8b46-b78401677162 | -12.86229 | -46.94565 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51050d7b-8f55-34ff-8caa-6a95026490a4 | -12.87669 | -45.26162 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35d3f39b-f255-34c3-8876-7a087c331bc7 | -16.01011 | -50.87401 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bfcd421f-c33a-3f66-b525-4e89e68e338f | -16.19594 | -49.99944 | 2025-10-01 04:21:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19805585-c739-3fb8-a1e0-79e8e9b0cb6f | -14.60375 | -48.31457 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b0bc784e-8ae0-3c95-afd0-588c6f78df40 | -15.23582 | -48.08764 | 2025-10-01 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd834ee9-7610-3d6a-acdb-ec114615a938 | -13.82515 | -47.46115 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8f5fa77-4405-3125-a832-303c4dcfb475 | -15.84753 | -46.24055 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 886479d4-25d0-3011-a1ed-5597444ca973 | -13.93675 | -48.11765 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 10fa5754-1624-3d09-98fe-e484e81a2c86 | -14.75419 | -45.76581 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fca17b1-bdf4-3264-80a2-c7982a1bd2dc | -11.84372 | -48.05844 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c8327d3-39a4-3eef-be1d-fec867f1ac65 | -15.2401 | -56.80593 | 2025-10-01 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87a7cfe8-6ceb-3019-a3cc-f80bff3af5a0 | -10.01902 | -50.22297 | 2025-10-01 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6be3491c-dba1-3e30-aea5-28f9a239b3ef | -15.30593 | -56.79037 | 2025-10-01 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 170d6ecc-3160-3863-9359-01be80e998ef | -12.4265 | -50.17897 | 2025-10-01 04:21:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29a591d3-6e25-30b9-9d1e-c2e61b1636dc | -13.71089 | -48.63488 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe54f691-261b-36df-b49f-d2d7f0b153ab | -13.22356 | -47.32781 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43ce8f00-f29c-3772-b5aa-e7c3c00419a8 | -15.42483 | -47.05573 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c04ef060-ab81-3b9f-862c-619ae6f148ac | -14.70878 | -49.14518 | 2025-10-01 04:21:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3664761a-5ddf-3e43-b5d8-9d1bb9521ab0 | -13.67968 | -51.2242 | 2025-10-01 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aeaf2ec9-850c-31b2-a5e7-43e9264d1358 | -10.92361 | -44.33733 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0eb6c42-0328-3f76-9dd9-6192b25d725b | -11.94679 | -47.07198 | 2025-10-01 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b751bc62-4018-3529-932b-ed32dbb281e4 | -10.93319 | -54.33093 | 2025-10-01 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f8fc5ab-5b54-32bb-98e0-be17e0e49f46 | -14.60839 | -48.20061 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c17a4bc-7c1a-3722-adfc-cce84d619e42 | -12.88945 | -45.26732 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| fd14523d-5787-3860-8ef4-2710a9727858 | -10.04258 | -52.09465 | 2025-10-01 04:21:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0e7d65b-05ee-3e6c-b3fb-c22a026a6530 | -15.31467 | -46.41011 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc9e8302-1165-371f-b17d-b45e30aeb224 | -13.67036 | -48.06552 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 42122e97-4456-39db-9cbc-72d36c6436bd | -11.47061 | -45.09783 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f709cf2-2aed-3ca2-970d-86d1bf51319f | -13.71432 | -48.63549 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65d09aa8-3d70-3ea8-bf4f-3a496e35f523 | -15.49577 | -45.91758 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b9430cc9-3ed1-38ff-bb30-5e3983130ba2 | -13.29429 | -50.65599 | 2025-10-01 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eaaaab40-bfec-3b0c-822a-d1d94ede19c5 | -14.13942 | -49.20085 | 2025-10-01 04:21:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0228e7cf-d2b3-3bae-886f-7bb67c484bdb | -11.8149 | -48.25396 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3a94b45-c401-38b1-8198-03635f51335e | -10.7824 | -45.36988 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d9a8d75-ab5a-3351-892c-8176e73314ba | -11.44917 | -43.51388 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cf4d570-6e70-3e7e-8ffc-4929240d17e0 | -14.18344 | -46.11658 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 00a1d7b2-4cc7-320d-ab4b-498bb5be4652 | -12.69892 | -46.88237 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9550f9ad-2621-3f9d-bffa-8a5f7b384af1 | -15.31852 | -46.4071 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fcc81f9c-3a3f-3ebb-a2d3-3d837502b514 | -15.38694 | -49.19545 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4d35bd2-d0ec-3762-83fc-d01cf689bf67 | -15.92873 | -46.24247 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f340e849-af10-3ad3-8588-19a17ee1b277 | -10.91509 | -44.30252 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b447849-8209-375e-8a3c-d057666ec05f | -11.43925 | -44.94764 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5255f009-d4cc-31a8-ada0-3fa8dbc5d81d | -11.20056 | -47.75451 | 2025-10-01 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f7639d45-491b-3daa-a9c8-9abbeddba7e8 | -12.16162 | -47.89722 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 405a548f-ad26-3650-8f97-a2edecc84e5b | -14.18068 | -46.11251 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74ab8073-008a-380c-9092-518b08d830c5 | -14.18784 | -46.11004 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fd242fc-057d-30a5-b72b-e35a76096cc3 | -16.24475 | -44.05661 | 2025-10-01 04:21:00 | NOAA-21 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbd6c41e-3cb5-34a8-8f1c-4b6aff0a8c03 | -11.8235 | -44.92392 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41d57663-38c4-312f-9fea-ad0add4469b9 | -14.7168 | -48.16179 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb623ba7-00d2-3bdb-a27b-939dc6aae801 | -12.78637 | -46.86768 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80015abd-bde0-331b-8977-23e88e989880 | -14.76269 | -45.21925 | 2025-10-01 04:21:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbf0cdc3-a6f1-35b4-9a00-1470b1ad6a2b | -15.29232 | -48.01455 | 2025-10-01 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c6b4b0a-8706-3ab1-b78b-9f1aaabdfe1c | -12.46266 | -50.24177 | 2025-10-01 04:21:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6277ae2d-c1e4-3a43-8f87-c8f124c344d3 | -12.58377 | -41.28598 | 2025-10-01 04:21:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 7f74a8d6-54fc-35f7-a226-923c6b7e25e9 | -12.37668 | -47.17297 | 2025-10-01 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12d1e3c7-0062-34f9-9ed7-d3d687fdc5a8 | -12.77116 | -46.89803 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a60d3d9-6182-38bf-aced-a47865d6e8f3 | -12.24773 | -47.80164 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0823000b-3e3d-35b7-a793-25293e39b254 | -15.66088 | -51.33099 | 2025-10-01 04:21:00 | NOAA-21 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 957c0a8d-2f0e-348e-b48e-74468635fb81 | -11.46373 | -45.00954 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae845745-f9df-3301-9527-a964858344f7 | -15.28448 | -47.89328 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 783a8b75-b6c9-31c7-9261-6d54e7e7159c | -13.36712 | -47.32273 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a00d8847-a608-3714-8dda-5ed5405ea673 | -14.20993 | -42.15166 | 2025-10-01 04:21:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1eb1c937-acc1-30ce-aaeb-c975c59fcb02 | -13.75931 | -47.9323 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README45.md)
