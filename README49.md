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
| a870a999-e0b2-34c8-9471-6668b77b1084 | -9.11665 | -61.59814 | 2026-08-22 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aee2a3c7-c41b-3727-8120-04562dc4fd76 | -11.59195 | -46.58143 | 2026-08-22 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8304ff8f-6056-3c08-9cff-bae65fd1e437 | -6.81821 | -59.67079 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 901af04b-91a9-3b89-826b-303dae81d6ef | -12.25094 | -43.12493 | 2026-08-22 05:04:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 77401b58-8d60-3270-82ac-1fce3d970299 | -5.79833 | -57.54535 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d62cc96-0282-3962-9efd-7127f94e1e13 | -6.79363 | -59.59526 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 53f2775e-68e3-3075-9d91-03c882ef7ac2 | -8.09271 | -50.03792 | 2026-08-22 05:04:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6ba89e96-bffc-3935-a991-4c358903871b | -9.24709 | -60.79769 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 486d412f-82db-37f3-8fba-bf5165fcc2b7 | -7.86124 | -63.7732 | 2026-08-22 05:04:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd4ce342-b5bf-3b98-a0ac-9dd4e8724b74 | -8.62014 | -54.72517 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ea1a34c-b726-3ecf-ad72-7870675909de | -10.2984 | -50.39178 | 2026-08-22 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7640d9f-4708-33db-8741-71a91a43e07a | -6.23228 | -55.40837 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c4b3fda-7d9f-3351-8890-fe76f23f5e16 | -8.52763 | -55.31983 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a77c9062-4078-3933-a0ca-e5ad0f8252f5 | -6.93758 | -59.30391 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a876fd8-9e07-3540-ba36-842a7fb830af | -9.21161 | -59.76517 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 898b3820-41d6-368a-b90d-930f8d1010d7 | -6.7617 | -58.67167 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 84418c23-fe97-3699-ba03-70f6f21f26cd | -6.78498 | -58.66347 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0e62c26-ac17-3ec0-944e-eb450a91cd66 | -6.79777 | -59.43651 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| efcd11b1-39e0-350c-abe6-064363e24e6d | -6.75608 | -58.67899 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3500ee9-f3a2-3987-a90e-58acb5919e41 | -8.61676 | -54.72462 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c03953f-a2ef-3d95-8194-c09d0f92b891 | -6.37491 | -54.95078 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2473cce8-cc3c-3f60-933d-34f2487e8347 | -7.25497 | -49.91387 | 2026-08-22 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7197444-3d96-3152-958d-74703f7870c1 | -8.09631 | -50.03852 | 2026-08-22 05:04:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 965d2bc6-4f44-3ee8-aad8-23f8ea311d6f | -6.76688 | -58.69313 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3315a686-72e4-3915-8e9a-e50b8ec35b65 | -6.95012 | -59.31071 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d89eff0-873a-390c-89e6-88dd27f6179c | -8.58582 | -54.78687 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09246db0-60d6-3b4c-a0ce-036c92fab3f7 | -8.11308 | -50.04977 | 2026-08-22 05:04:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7037993b-9436-3df2-bdd8-dd421c8fe305 | -8.5485 | -54.78076 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e519cb00-6ec1-3afa-92bd-d3c66beb7cde | -9.50773 | -51.67469 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8effb4d9-07d8-3037-a926-189f21024e40 | -11.44091 | -44.55533 | 2026-08-22 05:04:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9bda1988-5ea6-3115-a879-53efe5e6af2e | -7.6952 | -46.15345 | 2026-08-22 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 78d56509-0a8e-3569-9994-88824c24632b | -10.53037 | -50.77812 | 2026-08-22 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e86b3e67-f8e8-39bb-ba8d-2452d92664de | -7.07762 | -45.00235 | 2026-08-22 05:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 57f0a5b5-25e6-35a0-9dc9-b92da7f35958 | -9.51401 | -51.63387 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa8350bb-2a4d-35dd-be16-e5b5691f82a2 | -6.82276 | -59.67161 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| a5eab60b-e167-3c29-b50d-5a97d4d62a0e | -9.43371 | -51.61383 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 564dd4a3-52da-3ce8-a1aa-d6bed5c712ad | -6.23517 | -55.41299 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 000c13e6-0efe-33a5-bd68-2128423f65fc | -9.17497 | -59.43877 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fee23cc3-1495-395f-9c1d-93f52bfb0db2 | -7.3438 | -55.69557 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be34dabd-678e-3592-af09-aafd41a5614a | -12.77135 | -48.40589 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 94139ac7-bae8-31bc-b4ea-78e2b422aca3 | -8.53052 | -55.3158 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce05887f-28ca-3a9b-a745-0eaf3c7d65ef | -6.8091 | -59.66915 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b60e793e-6470-3f4e-a74c-b330ac03f523 | -6.12806 | -59.9002 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c53b646-80ea-38df-9c12-e88464bb1908 | -5.99595 | -57.80382 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 11b8eebc-015c-3b27-a995-764300cd78c8 | -9.42229 | -51.64242 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc282b28-5106-38ae-a746-851f81edaad8 | -9.17207 | -59.45523 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 7016d7fb-03b8-3d02-a76d-151d9320ad2e | -7.17902 | -42.75138 | 2026-08-22 05:04:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 937d2387-ff46-3972-b198-115d73dcf80d | -6.76955 | -58.67716 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 85c7929e-1486-3cc6-9018-c64c6d7467bc | -8.10005 | -51.66352 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| da97d69e-e266-3b62-9dfe-2f8595c2ae14 | -8.51258 | -55.32511 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 342ee916-a9db-368c-aa79-b2941cee55fd | -8.40534 | -62.69496 | 2026-08-22 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 467daf23-31d1-3bd6-a071-c8c4389c6cbd | -9.15766 | -59.46115 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 350f5acc-c567-3331-922e-36184f2ac857 | -8.5457 | -54.77654 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f07f631b-b4cf-352a-a697-c8dc1f9b71b2 | -7.33959 | -55.69898 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f54d6dd6-d7f7-30eb-892c-d27ab1277ad5 | -9.05512 | -60.43616 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9579cd1b-44ee-3438-9a8b-ed7199ba406b | -6.75025 | -58.66151 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df20df48-97d7-3f17-a273-ebcc87b1c978 | -9.21525 | -59.77026 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c049ba5-a4d4-359c-a2a5-e320d5cc0c85 | -6.41737 | -52.72741 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7af058cc-4855-3ab8-bb1b-e2d38c1e40b3 | -12.77844 | -48.38566 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04ca51e5-ac4f-3dac-9d33-55a8f9f410c5 | -12.86054 | -48.44553 | 2026-08-22 05:04:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8b72720-8ef1-3889-aab6-fffd2656929f | -7.20699 | -59.40976 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03a1ed09-bbdd-30dd-869e-9ca48341abbe | -9.39971 | -60.55313 | 2026-08-22 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4975c61c-a08b-3617-8f3e-78749db9bf08 | -9.03129 | -45.88814 | 2026-08-22 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b607818-5083-3598-8164-a5fe87730251 | -12.01017 | -53.43264 | 2026-08-22 05:04:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d8b5633-9aa2-3b79-9634-bd59480d8767 | -9.2072 | -59.76442 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5cc27012-bb91-3dc7-9efc-65da1d5a2da6 | -6.71228 | -58.99237 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e985f966-e6e5-3b8a-b5ba-81c2e2560ba4 | -8.62529 | -54.71481 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80ff7baf-5c10-3e34-8825-f502f438767a | -11.16397 | -54.01488 | 2026-08-22 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b30b626-ada8-314f-90ed-ca79ebe1d577 | -7.36415 | -55.68245 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2be19a20-2b51-3311-8958-1c0f710a60b5 | -13.45594 | -51.76411 | 2026-08-22 05:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e32559cc-bd7e-3171-ae3d-896cddcde5ac | -6.77248 | -58.68591 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 57f48679-82c2-32f3-a918-4cc94eac9ab7 | -8.15614 | -46.72191 | 2026-08-22 05:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 45a877c6-60c5-3d81-850a-a2eeed1f0096 | -6.42492 | -54.92768 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bbcf35b-ecce-3b2e-bc19-99f8ea7040fe | -5.98539 | -51.94663 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 749cf441-d8d6-3f08-b519-dd285487e007 | -11.95044 | -45.49243 | 2026-08-22 05:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74d8cc0c-6cdf-3f8f-a471-003cb8f80424 | -7.35195 | -55.668 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| febb37d2-20ea-3cd0-83da-2f29b38239c6 | -6.89307 | -56.43871 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1595e78c-6b1b-35b3-a0f3-89ebd46d99dd | -6.43339 | -52.71219 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f0bb7f5-6e45-3b74-9079-7d7e00076bbb | -7.47492 | -45.14916 | 2026-08-22 05:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aaf2f532-e644-3325-bb79-229d50b94226 | -8.62379 | -54.68098 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aee3d71e-421e-3f11-b7a6-757a866608fb | -6.79265 | -58.63452 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 27a0a3ab-2ebd-3e53-a055-ad0a5460ab1e | -6.81517 | -59.38916 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7383d9ad-be38-37d5-9801-c1fae788cd89 | -6.80161 | -59.41434 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 8e874f44-cc56-3876-a595-66cffc1976c2 | -9.51457 | -51.67573 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea287d02-b104-38eb-81cf-bb3e7cf5eb88 | -12.7138 | -48.41677 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24e83bcd-8bee-34b6-a31c-c671ecb009d4 | -6.22969 | -55.42437 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e859d7b-d892-30e6-b561-c84bc6400fce | -6.54039 | -58.52146 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ae268d53-7009-3b09-9b76-890f990c8ae2 | -10.99193 | -43.70232 | 2026-08-22 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22ef105c-27d2-3d04-9ad3-eb38cec5e8b3 | -9.46212 | -48.29037 | 2026-08-22 05:04:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cf57867-7e52-39d8-9f9c-86db801e2183 | -6.37009 | -62.90683 | 2026-08-22 05:04:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 66717f1b-7d13-3e98-8d9d-2ae90455f645 | -8.67445 | -54.75993 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 675224a9-4c21-3174-b038-35348875580c | -8.99183 | -50.73686 | 2026-08-22 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8a9de33-275f-30ff-92f0-54da959c5bf5 | -12.77355 | -48.38977 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f82996ea-a3d1-31f3-84c8-0f037da66055 | -7.02194 | -59.54969 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b67f044-6c77-37a5-bfc7-60d031a3c036 | -6.17255 | -55.43985 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b25fb418-3cd5-3835-ae0d-928e53432b78 | -6.79442 | -59.5907 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a277a2fb-64a0-3d89-8d27-1dd49fc64c68 | -9.17783 | -59.44778 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2a5ff17e-b4b2-3838-a65a-90c2b4e4c771 | -6.86027 | -59.43127 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b27d658-0ea8-3cd8-843c-fd0aa031eee8 | -9.10754 | -60.91844 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b4249d3-d6a9-3f52-8586-d3352c00d4d1 | -9.15979 | -59.47432 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README50.md)
