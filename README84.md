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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9cdcdea4-1ad1-3aba-bfeb-ac871bcff2d5 | -5.09304 | -60.23409 | 2024-10-08 04:55:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1d8df59-3303-37cb-a42a-adba5e22f64f | -3.89266 | -60.59266 | 2024-10-08 04:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7a0f891d-e862-3008-b285-32f8b1df4224 | -3.888 | -60.59189 | 2024-10-08 04:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 734303b7-d161-37c1-b687-5eb99724823e | -9.40182 | -66.54558 | 2024-10-08 04:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cb9d2db1-3330-313b-9828-14b547239cd6 | -9.40085 | -66.55061 | 2024-10-08 04:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 1a089513-2616-3586-a956-eac553527190 | -9.40809 | -66.54679 | 2024-10-08 04:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5130376b-8515-39ed-8f3c-85f576a43d54 | -14.53192 | -43.22044 | 2024-10-08 04:57:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3810849e-2753-3f7d-8435-7a9a9b22145f | -15.60989 | -42.56978 | 2024-10-08 04:57:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c6e1e52-8db4-3ced-9211-1ca82fd62f11 | -15.60812 | -42.56763 | 2024-10-08 04:57:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3c744c60-3df0-3b8f-986c-8fc7226f35cb | -15.60292 | -42.56903 | 2024-10-08 04:57:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c826c4f2-179f-30df-9834-c49e43a3e4a8 | -15.60113 | -42.56694 | 2024-10-08 04:57:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c8207fb0-6541-34d4-a029-abcdd396c1c6 | -9.52776 | -42.99075 | 2024-10-08 04:57:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 27becf2b-c1c4-33bf-87da-c3bc38a34aca | -11.74644 | -44.49054 | 2024-10-08 04:57:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7dd6111e-88bf-309d-9467-e2b444bacc2e | -11.7459 | -44.4949 | 2024-10-08 04:57:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d2419da-0a80-308f-8bce-1130bfefc4db | -11.74377 | -44.49216 | 2024-10-08 04:57:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15cd2df2-cf83-3db1-950a-786c8b2f66b1 | -11.74326 | -44.49654 | 2024-10-08 04:57:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e654620c-da4b-3dfd-b66a-5b536ec9cabc | -13.41988 | -43.79702 | 2024-10-08 04:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf02ac8b-9a69-3b49-921f-07ca1fab7065 | -13.41933 | -43.80216 | 2024-10-08 04:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b3f8867-b9ab-3ca6-89b7-a039dc3a42b0 | -13.41791 | -43.79631 | 2024-10-08 04:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c3b5299-b9d7-32b6-8c29-58eee933028a | -13.41732 | -43.80144 | 2024-10-08 04:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b314716e-bc47-3498-8b97-7c472fa6a354 | -13.3765 | -43.76503 | 2024-10-08 04:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 902666ea-0056-3c8e-8d97-6372c2b324c7 | -13.36959 | -43.7694 | 2024-10-08 04:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a48502f1-3db6-39c8-9264-2f0540a6be88 | -13.86592 | -44.58168 | 2024-10-08 04:57:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c752d195-1666-311b-b685-9a4e837f1ba3 | -13.86093 | -44.58247 | 2024-10-08 04:57:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d8a51db-720b-383b-9af4-62ef2ce061d3 | -13.85986 | -44.58095 | 2024-10-08 04:57:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4a66314-e633-35fb-95a7-576ed8caa959 | -13.85486 | -44.58174 | 2024-10-08 04:57:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83bacad4-a6e0-330d-87b2-6c597c277fdf | -13.85325 | -44.5849 | 2024-10-08 04:57:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ef23fea-b92a-3a5d-a901-1fc2c30ac06d | -13.84831 | -44.58549 | 2024-10-08 04:57:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93e256e5-a6a1-3b5c-b999-5086b4a4c1b3 | -10.46889 | -45.10954 | 2024-10-08 04:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 170f98e6-ff56-30c3-82d5-f2cd3f80a519 | -10.46842 | -45.11324 | 2024-10-08 04:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e89ed77-cd6c-35af-a749-f591a8b7e9b3 | -10.06703 | -45.27509 | 2024-10-08 04:57:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 54da3da9-35ec-3cf4-a066-0682b2cfa05d | -10.06659 | -45.27858 | 2024-10-08 04:57:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4748c4d9-5078-3dd2-a790-23f42fba6180 | -11.91908 | -45.70087 | 2024-10-08 04:57:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44d374c6-32f1-33a0-8975-0f399ffe526d | -11.91878 | -45.69955 | 2024-10-08 04:57:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 276a6200-d166-3c81-a33c-8bb8277facb2 | -11.91358 | -45.70016 | 2024-10-08 04:57:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83795794-d516-339e-81fd-8906745a9181 | -11.91328 | -45.69883 | 2024-10-08 04:57:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d91dcc9-6a14-3cfc-91c5-87a267005ed7 | -13.085 | -46.34474 | 2024-10-08 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89fd0a58-e1ef-3e7d-b323-dc2a38fc898e | -13.08459 | -46.34809 | 2024-10-08 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef93aecc-cddd-3ca6-b51c-8a71653d5f91 | -14.22291 | -46.4481 | 2024-10-08 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df1dbfad-8e49-365d-a416-9d60619c4589 | -14.22251 | -46.45147 | 2024-10-08 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6941e166-2030-3767-9238-c92d775523aa | -14.21754 | -46.4472 | 2024-10-08 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7b2c886-a146-33b9-b62d-6e3b721a88ae | -14.21636 | -46.45716 | 2024-10-08 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 024aa9fd-967e-3e3e-91c5-9aaf682df5aa | -14.21599 | -46.46027 | 2024-10-08 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad566f4d-b832-37d3-9020-d4bd1aff020f | -14.2122 | -46.44593 | 2024-10-08 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d0fa11a-fcd5-3362-90bd-e7225cbafb45 | -14.20723 | -46.4416 | 2024-10-08 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57716bf7-235a-3590-ad1c-d8f42401dce8 | -14.20683 | -46.44507 | 2024-10-08 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3de4d47-a51a-321a-99f5-eaa437a87bb5 | -14.2018 | -46.44115 | 2024-10-08 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd0d9da1-8caf-349a-808b-9526602cc1a2 | -14.12741 | -45.60346 | 2024-10-08 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 67e8f9b6-8b89-38ad-8fe5-2d9c12f41f4d | -8.53345 | -46.59162 | 2024-10-08 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76bb8af3-efd7-3808-85ff-bc8393b2493e | -8.5285 | -46.59095 | 2024-10-08 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70e5f0e3-b6dd-336b-9fba-fe3f033e7078 | -12.16433 | -47.75927 | 2024-10-08 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65c74ad6-2916-3c84-9834-51451c3b283f | -12.16361 | -47.76478 | 2024-10-08 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fc89814-47d6-3b03-9dd3-220fcb9afea8 | -12.15881 | -47.76409 | 2024-10-08 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4374ab7-b520-3966-b7b9-a701430f9a3a | -12.03774 | -46.85433 | 2024-10-08 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 88db35c4-5307-3711-9bb5-3b71ec33c7f6 | -12.03735 | -46.85739 | 2024-10-08 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9332d84b-f9aa-3072-aa56-cfaa44000a95 | -11.73493 | -46.96635 | 2024-10-08 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dc940ef3-fef2-3068-98f1-a5928df3b0b3 | -13.17755 | -47.98777 | 2024-10-08 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3f74b2b-0183-3660-b2c4-61c1f9b8012b | -13.17688 | -47.99298 | 2024-10-08 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c55a47b-6df6-3798-ad3f-ad9a7575642e | -13.17211 | -47.99217 | 2024-10-08 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f931da2-3492-3b3d-abf2-bd47769563bc | -12.46684 | -47.31264 | 2024-10-08 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dc3b0da8-265d-3442-9b96-beae5835807c | -12.46652 | -47.31036 | 2024-10-08 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da21ae67-b7a5-3155-b7f6-9a4d91963446 | -12.46578 | -47.31607 | 2024-10-08 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf73a2a0-a3ab-33b8-b39a-a5a83ab9f691 | -12.46187 | -47.31191 | 2024-10-08 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8228c840-fca3-3b44-a210-b5728e441752 | -12.46156 | -47.30964 | 2024-10-08 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c478d796-c08e-3e29-a1b6-1092e174c683 | -12.46081 | -47.31534 | 2024-10-08 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cddc676c-967d-3ab3-b0ea-190124166f05 | -12.39637 | -47.18375 | 2024-10-08 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bb3be8a-a10e-355b-a240-b4b7592ed09f | -12.36275 | -47.09563 | 2024-10-08 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c383d242-d03b-3e8b-8c08-015f239185f7 | -12.362 | -47.10148 | 2024-10-08 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aeeca6a1-1f93-32f1-ac3d-21bb2276b09b | -12.35772 | -47.09495 | 2024-10-08 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1b0e03f2-4e9d-387b-9291-63253daec280 | -12.28202 | -47.64065 | 2024-10-08 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d58901b-2102-39d5-9513-77f9ddb9d990 | -12.27716 | -47.64005 | 2024-10-08 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a373b685-0874-38a9-895e-d69e12cfd85b | -9.5381 | -47.88918 | 2024-10-08 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4910c18a-ecfa-3b25-aa1a-ac7e900d397e | -10.55768 | -47.78958 | 2024-10-08 04:57:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a75da838-8cee-3683-af64-798b6a36d53c | -10.55301 | -47.78884 | 2024-10-08 04:57:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f31d2bc6-091d-37a7-828c-cb2918dd94c3 | -13.53598 | -49.48137 | 2024-10-08 04:57:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5afbc328-7d29-335a-8d31-cae46f3335be | -13.53162 | -49.48077 | 2024-10-08 04:57:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dfe0de97-af56-3ce4-92c6-e2c4b4cdd540 | -12.53579 | -49.48535 | 2024-10-08 04:57:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b59c82b2-f80e-3674-9333-169b3fa203e1 | -13.53219 | -49.47649 | 2024-10-08 04:57:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1314bdb4-6d0b-3bfa-93b0-39474a6f8540 | -13.53654 | -49.4771 | 2024-10-08 04:57:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 21d14037-d2e7-34bf-a87b-069c43af3a07 | -12.78066 | -48.2145 | 2024-10-08 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c2e9feb4-0cfe-3c49-8cf7-cdd04d16537b | -14.1551 | -49.69036 | 2024-10-08 04:57:00 | NPP-375D | CAMPOS VERDES | GOIÁS | Brasil | 5204953 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ca95672-9299-3ff9-81eb-e65d045b9de7 | -14.15077 | -49.68973 | 2024-10-08 04:57:00 | NPP-375D | CAMPOS VERDES | GOIÁS | Brasil | 5204953 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cce66f7b-f669-3136-9fd3-0221a5c047bb | -14.90851 | -49.59052 | 2024-10-08 04:57:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 38036a95-901f-3cf7-ba6f-af90c1204e71 | -15.07977 | -48.94479 | 2024-10-08 04:57:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8112a578-90bd-334f-a026-caf04db97359 | -14.90907 | -49.5862 | 2024-10-08 04:57:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 92d2a207-1979-369c-a4a9-95f1aca357a4 | -14.90466 | -49.58567 | 2024-10-08 04:57:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 8f9e129d-969e-3d00-a3b3-7f3792a2a28e | -14.9041 | -49.58996 | 2024-10-08 04:57:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 29ef22bb-059f-3f8a-b83f-be88615da7a7 | -9.12604 | -49.66334 | 2024-10-08 04:57:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8a09e9ab-712b-36ec-895c-e1115f1be040 | -9.05337 | -49.71052 | 2024-10-08 04:57:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06a72585-8aaf-3301-9cd7-5056d1ff1bad | -8.75367 | -49.78157 | 2024-10-08 04:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e23b8b6a-e0fa-3a38-990b-fc8b3699736e | -8.74969 | -49.78094 | 2024-10-08 04:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e9248556-fb46-3792-91ed-3529eedf22dc | -8.60391 | -48.84571 | 2024-10-08 04:57:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0bd01d9f-c834-378f-9a0f-97a7e32738b8 | -8.60334 | -48.84965 | 2024-10-08 04:57:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7b449779-9899-3276-a6ff-4d2479e18bbb | -8.59968 | -48.84505 | 2024-10-08 04:57:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 14415e5e-ccf4-3668-9b69-6ff24aeeac23 | -8.16629 | -49.46426 | 2024-10-08 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1ccfa1eb-8300-374b-89b8-93f59f7cdaac | -8.16578 | -49.46779 | 2024-10-08 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 782f8244-c7ca-3c83-8ca5-5d3d7ed396f0 | -8.16224 | -49.46373 | 2024-10-08 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d3fc326e-507f-3a26-baf2-3f67d3c0b777 | -8.16173 | -49.46725 | 2024-10-08 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9fdd1025-5c4c-3299-ada1-ee57526ca1a7 | -8.15821 | -49.46312 | 2024-10-08 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| edfcd046-372a-34e6-871e-5823fa45eb8c | -8.07301 | -49.6703 | 2024-10-08 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README85.md)
