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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 805e0a78-dece-3ba1-9840-90409abaeb25 | -20.31945 | -46.54285 | 2025-10-26 04:53:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe6c7b45-b111-3f38-a580-43007dc77840 | -14.43695 | -55.91657 | 2025-10-26 04:53:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 855bc3a5-5035-3709-a03a-8ae7bc3e67e5 | -15.45681 | -50.47763 | 2025-10-26 04:53:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2066616a-cc93-3679-a587-b082beab4e30 | -17.32038 | -43.65567 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1850ea5b-ac9d-3130-9227-8cb87d847258 | -17.32105 | -43.63107 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dad68aac-6445-33b1-b799-36377e203eb2 | -14.50166 | -57.33744 | 2025-10-26 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 894e6bbd-d668-30c9-b38c-b448a7e75287 | -19.40436 | -45.87572 | 2025-10-26 04:53:00 | NOAA-21 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6332199-a09f-39c7-9998-aad83bd8534e | -14.27805 | -49.92323 | 2025-10-26 04:53:00 | NOAA-21 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c921ba72-bded-39dd-a2d5-c5ae06d4c859 | -14.4427 | -49.95584 | 2025-10-26 04:53:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e27947fd-0cbf-3264-a395-fa0af672870f | -15.17445 | -51.2751 | 2025-10-26 04:53:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41ffcbdf-878f-367a-a6c3-01e22e1820a9 | -15.29462 | -50.76261 | 2025-10-26 04:53:00 | NOAA-21 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0a07771-28ae-331e-8a4c-4eed19ad617e | -18.24032 | -55.38293 | 2025-10-26 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 390605ea-7a54-3ec4-8f99-5dcfbd791714 | -18.48553 | -44.43472 | 2025-10-26 04:53:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 257ea0cb-652d-35c5-b180-a78893b58dd7 | -19.32734 | -49.80502 | 2025-10-26 04:53:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a283f6c0-10e3-3839-9c6c-1be61b94eaab | -17.01325 | -55.9053 | 2025-10-26 04:53:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7cd7b307-ae73-3122-9700-f56df95e5e79 | -15.46439 | -50.47859 | 2025-10-26 04:53:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6c09a8d-c5af-374a-b632-fb73d1370734 | -21.76651 | -50.04659 | 2025-10-26 04:55:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 2174bb0d-546e-3366-9879-7ea22c374a72 | -23.30119 | -50.80844 | 2025-10-26 04:55:00 | NOAA-21 | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 4d430150-ea1a-3af5-8a06-5d335a1c0ce5 | -20.83142 | -49.49865 | 2025-10-26 04:55:00 | NOAA-21 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c1f94ec2-9901-3cc0-8c48-0d85e2695cec | -21.92675 | -50.9451 | 2025-10-26 04:55:00 | NOAA-21 | PARAPUÃ | SÃO PAULO | Brasil | 3536000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fe7e0701-c891-3fa2-9a96-c661654d6b40 | -21.76278 | -50.04182 | 2025-10-26 04:55:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 4f95282e-ac92-397d-8f32-ad54ecebbe08 | -20.20278 | -56.07763 | 2025-10-26 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| aa3c71e8-7759-3ba1-a1e9-75a85dbf7512 | -21.76602 | -50.05078 | 2025-10-26 04:55:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 90e34ca6-f7aa-3e78-b7ed-d8588d223263 | -23.78001 | -50.03568 | 2025-10-26 04:55:00 | NOAA-21 | PINHALÃO | PARANÁ | Brasil | 4119202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 98d6b296-dd84-38f6-8292-54925143c1c1 | -21.76699 | -50.04247 | 2025-10-26 04:55:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d47becc5-6491-39f1-8642-e7c722f60f72 | -21.76326 | -50.03772 | 2025-10-26 04:55:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| ac04f2b7-c171-3e0f-8c26-91628a626e8e | -20.8294 | -49.49671 | 2025-10-26 04:55:00 | NOAA-21 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 15be4bba-b472-3627-97b9-062003203e44 | -23.77062 | -50.89868 | 2025-10-26 04:55:00 | NOAA-21 | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 69e5cfdf-0955-3be8-bbba-49e732be9320 | -20.8289 | -49.50103 | 2025-10-26 04:55:00 | NOAA-21 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c0d834d8-297a-37a5-8f96-952732d99b61 | -22.25714 | -49.93191 | 2025-10-26 04:55:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5eb09050-7983-3bbf-baf3-e41a7a2133c5 | -21.33827 | -46.56316 | 2025-10-26 04:55:00 | NOAA-21 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3264ab84-3745-3ea8-a551-1656bd1559bc | -23.23335 | -50.79043 | 2025-10-26 04:55:00 | NOAA-21 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 8fbcaa75-0488-3825-a20d-b490862b443e | -23.76648 | -50.89831 | 2025-10-26 04:55:00 | NOAA-21 | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 686542cf-8ee9-3bdd-95f4-2ea84c5673dc | -21.76748 | -50.03835 | 2025-10-26 04:55:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| aa678e39-50d5-3412-99ed-22f0341e499c | -21.7623 | -50.04594 | 2025-10-26 04:55:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 43270f28-197b-3f78-951e-fee5e0fb4538 | -21.62098 | -46.92371 | 2025-10-26 04:55:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| af1b12d4-6520-3bba-919d-50aff00f700f | -23.78292 | -50.03474 | 2025-10-26 04:55:00 | NOAA-21 | PINHALÃO | PARANÁ | Brasil | 4119202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5397a691-de88-3188-bec6-46ac8feae905 | -5.31991 | -35.93648 | 2025-10-26 04:57:00 | AQUA_M-M | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 30.1 |
| 6e9e327e-bc15-34b9-bcbf-ab6e988c9aaf | -5.3224 | -35.92038 | 2025-10-26 04:57:00 | AQUA_M-M | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 32.0 |
| 4d50e7e8-1740-3181-b409-d2d6e2af8723 | -5.31984 | -35.92568 | 2025-10-26 04:57:00 | AQUA_M-M | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 49.9 |
| cdbcad72-fe75-33e7-b4d7-515775036f73 | -13.53018 | -42.99793 | 2025-10-26 04:59:00 | AQUA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 63.5 |
| 09e68b55-1245-3bb9-877a-635a3df27d7f | -13.52969 | -42.98945 | 2025-10-26 04:59:00 | AQUA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 71.6 |
| 42d54d8c-9e4d-36da-9088-23d14c696541 | -14.50551 | -42.97053 | 2025-10-26 04:59:00 | AQUA_M-M | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 37.4 |
| b646ef4f-c318-325b-a905-03518b8599f8 | -14.5078 | -42.97911 | 2025-10-26 04:59:00 | AQUA_M-M | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 49.2 |
| 3e769c8f-c95f-3359-b53e-1a58fc129c7f | -14.49802 | -43.00968 | 2025-10-26 04:59:00 | AQUA_M-M | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 43.3 |
| 5b65b208-84c2-3459-a8cb-4825a047228a | -5.0994 | -43.1977 | 2025-10-26 05:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 22d1998f-956f-3191-889c-729b93a9360f | -6.3864 | -45.7819 | 2025-10-26 05:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 01a35586-1733-3017-8aec-2144745120d7 | -5.1181 | -43.1964 | 2025-10-26 05:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| a571e891-0aeb-3117-baea-e9f4f26cc565 | -4.8933 | -43.2349 | 2025-10-26 05:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| d8003525-9179-3c65-a183-702ba1bf11f6 | -6.3864 | -45.7819 | 2025-10-26 05:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 0e7fe504-6af7-3317-ac0a-2a9f9b824de0 | -5.1181 | -43.1964 | 2025-10-26 05:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 37e836a3-8b84-3eb2-aed4-948eb2d6a186 | -5.0994 | -43.1977 | 2025-10-26 05:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 9c07458e-4401-3db3-a997-46ffc53e4032 | 1.63771 | -55.71371 | 2025-10-26 05:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7835afff-515d-394d-9768-b94e07f2180c | 3.34399 | -60.08841 | 2025-10-26 05:18:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 62b5f41d-8ab9-378d-915b-ae7b90f8dbbf | 0.43388 | -51.01117 | 2025-10-26 05:18:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b39b217-962d-3ee9-97f8-d92f1a0370a0 | 1.61798 | -55.74261 | 2025-10-26 05:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 176947b7-c4d3-3895-827f-32a7e7df8e30 | 1.65501 | -55.68927 | 2025-10-26 05:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| b7a7bbd7-58cb-3c9c-832c-87ec4b21d1bd | 1.60953 | -55.75499 | 2025-10-26 05:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81e3f9a0-550e-3bb4-b2d8-2e0e7647dc45 | 1.62079 | -55.73847 | 2025-10-26 05:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc7f2bd7-e1c0-3d66-9acc-717c5e533ab0 | -1.18912 | -53.38484 | 2025-10-26 05:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dffa553b-e24f-3990-8c35-f9ec016386a5 | 1.95277 | -55.76394 | 2025-10-26 05:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34048831-c2a1-3b01-b64b-89a619c11d6b | 3.63696 | -51.82693 | 2025-10-26 05:18:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1345ea3-c399-301f-9055-75cea02ae1fc | 2.46644 | -51.17346 | 2025-10-26 05:18:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e09f806b-4eda-3a67-bbb2-4e58c2db6252 | 1.62925 | -55.7261 | 2025-10-26 05:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36e6db0b-3690-3551-bd2e-bdcf5c4f201f | 1.62868 | -55.7225 | 2025-10-26 05:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daf313d5-6933-33cd-b797-c7f1c489a495 | 1.43269 | -50.89387 | 2025-10-26 05:18:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57e20cf2-61f8-3f10-8571-b2de0a7734ca | 1.61516 | -55.74673 | 2025-10-26 05:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1b86be5-bb57-3b8e-9900-418dec163880 | 1.65219 | -55.69341 | 2025-10-26 05:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5146167c-d96f-33be-8f43-254f52c3d343 | 1.63432 | -55.71424 | 2025-10-26 05:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60593953-c93c-364a-94b1-0e74c0041fa6 | 1.64095 | -55.70992 | 2025-10-26 05:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bfd90c2-f9b6-3571-80ce-8a182f11f607 | 1.64376 | -55.7058 | 2025-10-26 05:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7435f5c-6df1-3126-9e40-1e1fc74f3825 | 3.14168 | -61.01093 | 2025-10-26 05:18:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca22674a-40bf-3167-b6e6-94ba086df38f | 0.67838 | -59.54418 | 2025-10-26 05:18:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06b23bd2-0227-3220-975f-96347dfd8164 | 1.60672 | -55.7591 | 2025-10-26 05:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 41d93bc3-43da-34e2-82a8-f135f172d224 | 1.62643 | -55.73022 | 2025-10-26 05:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e4e3e8f-91b4-3a0b-8afe-3def41078b49 | -1.18989 | -53.37998 | 2025-10-26 05:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc52c2a4-6831-3996-b323-cc3f7b83333c | 1.61459 | -55.74314 | 2025-10-26 05:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96616256-433a-3db9-9b2c-2b1551eb8c86 | -1.19691 | -53.38615 | 2025-10-26 05:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ae49ec2-e446-35da-beab-180aa867dd9e | 2.46709 | -51.17743 | 2025-10-26 05:18:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d7ab03e-3208-307b-ab09-051cbc0e2fd6 | 1.63814 | -55.71405 | 2025-10-26 05:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f229b0d-f179-3093-9b50-5e5e8cea72c1 | -1.19301 | -53.3855 | 2025-10-26 05:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8df25ab9-ceb1-3b39-a4e9-d64745d752cf | 1.62136 | -55.74207 | 2025-10-26 05:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6569aad-0f9a-3945-bce1-95a331cb0018 | -1.01609 | -53.72425 | 2025-10-26 05:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 612ca3b0-896a-344d-bed4-92f1aec5b90a | 1.95221 | -55.76037 | 2025-10-26 05:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| caaeb8b9-bd68-3a3e-aded-012cbcd4c20d | 1.62586 | -55.72663 | 2025-10-26 05:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c3a297e-94ed-35ee-b421-ec0ec729633a | -1.18522 | -53.38421 | 2025-10-26 05:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c78e6216-b413-3592-8b25-52c36c85d35e | -5.0994 | -43.1977 | 2025-10-26 05:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| ffaf3908-87b8-39a6-9080-457c52ca65a6 | -5.0996 | -43.1744 | 2025-10-26 05:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 4397229e-ed48-30c1-8af7-aaac7ff58723 | -5.1181 | -43.1964 | 2025-10-26 05:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 0c6a8430-13c0-3b39-8139-bc17f8a91601 | -3.47878 | -50.08138 | 2025-10-26 05:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a40a5d9-22c7-38d1-943a-fbbcd43bcf75 | -3.54412 | -53.31582 | 2025-10-26 05:21:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a8573350-648a-323e-82c1-5d53eb6b8086 | -6.53947 | -54.97194 | 2025-10-26 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d71de1f8-5485-3b7d-8e4e-dbdda6ac4f50 | -2.78619 | -54.41669 | 2025-10-26 05:21:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 62b8d847-b356-3918-8e22-2c68598da40d | -6.38881 | -45.78423 | 2025-10-26 05:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 29c405d8-8359-333e-a38c-7b4386bcede3 | -4.29766 | -49.29176 | 2025-10-26 05:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ea58ae0-69dd-3511-aba1-12bc00a23682 | -4.48311 | -48.67244 | 2025-10-26 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55698675-5ec7-32a1-8b02-a596db39fe73 | -3.83331 | -50.20186 | 2025-10-26 05:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7afa1ea9-1da8-342e-b58d-c08141db33b1 | -6.79459 | -45.41257 | 2025-10-26 05:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ee75b6f-5890-39e1-aff7-c5b65f6a7ba3 | -2.32398 | -48.58714 | 2025-10-26 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d6e98140-3b1c-3026-8e45-609d44110d43 | -3.26947 | -50.05002 | 2025-10-26 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README47.md)
