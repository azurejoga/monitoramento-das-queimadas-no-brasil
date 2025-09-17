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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 491abff2-3ced-32c7-b169-ab53bb7a3972 | -17.04757 | -45.89461 | 2025-09-17 04:14:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a1579363-6f69-3dc2-88e8-ffb2eb56d42c | -19.00883 | -49.9296 | 2025-09-17 04:14:00 | NPP-375D | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4016b875-0cc3-38ab-9530-ae691e650a82 | -17.56454 | -43.78981 | 2025-09-17 04:14:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66f8e3be-a6e1-3e05-bdab-c6b7a0d4e6ab | -17.31791 | -46.82003 | 2025-09-17 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10bd20b2-9ada-326d-8278-669c01992c1e | -17.93925 | -45.25351 | 2025-09-17 04:14:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 348f6fe9-b0e0-3a2a-b028-f0094f5f93a0 | -17.34201 | -46.80725 | 2025-09-17 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4eb6a115-3612-3d06-ba3b-30ef7ef63d4a | -17.5696 | -49.0651 | 2025-09-17 04:14:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0850de9d-0085-31d3-8b0e-ed63cc401333 | -17.33777 | -46.81067 | 2025-09-17 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c7a0f6c-eea3-3ac9-a798-42f6d69abe9d | -18.33515 | -43.3001 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 276f255c-3888-3b06-ae66-35f76e28ac16 | -18.31782 | -43.3009 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 42263508-513f-397e-8f04-e1445f4e7024 | -18.3318 | -43.29952 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 72406655-ea8b-3258-b7d8-fb116d715baf | -18.19173 | -44.53957 | 2025-09-17 04:14:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3b286570-aea3-377c-88f4-f19e41b81bfd | -18.16376 | -45.22483 | 2025-09-17 04:14:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a83b63fa-3723-3701-9bce-3aa9c89937ef | -18.17493 | -45.17725 | 2025-09-17 04:14:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff0c3d37-b55d-374c-b50a-ce88adca1251 | -17.19848 | -45.91472 | 2025-09-17 04:14:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ea6f8ab-0bb3-367c-80c5-3da3737f2f3c | -19.52934 | -50.59336 | 2025-09-17 04:14:00 | NPP-375D | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 498a2da0-de76-3c63-945f-2458c5233de1 | -17.33068 | -46.80944 | 2025-09-17 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 01e03b55-36b1-3a8e-92b7-15d79318dbf8 | -23.45693 | -49.2507 | 2025-09-17 04:14:00 | NPP-375D | TAQUARITUBA | SÃO PAULO | Brasil | 3553807 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf64ad3a-22b8-3014-80a0-4dc5f4cab06f | -17.1944 | -45.91795 | 2025-09-17 04:14:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4295f7cf-50f7-36f5-ad74-548192338bf4 | -17.1957 | -45.91024 | 2025-09-17 04:14:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44e77720-7b82-384a-b169-862a31b4bebf | -17.00344 | -45.86274 | 2025-09-17 04:14:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7277afe8-c1f7-359d-a1e6-2a160995c5b7 | -18.17373 | -45.18464 | 2025-09-17 04:14:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55d212ba-a11c-3992-8cea-9ff2ca08801b | -20.43262 | -40.74632 | 2025-09-17 04:14:00 | NPP-375D | MARECHAL FLORIANO | ESPÍRITO SANTO | Brasil | 3203346 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 314902c7-cb13-3cd9-b30b-32535790e4ea | -22.36049 | -49.03917 | 2025-09-17 04:14:00 | NPP-375D | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e492de5-d896-386e-9793-688942f93314 | -18.53978 | -48.13697 | 2025-09-17 04:14:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fac117f2-c326-37aa-94f7-a3546be91e09 | -17.19766 | -45.90754 | 2025-09-17 04:14:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ab0b4ba-d87d-3ecb-b00f-2dc4edc340d3 | -23.13545 | -49.63955 | 2025-09-17 04:14:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a6e44d5d-f432-3694-a210-de3fb3977a26 | -18.36696 | -43.31704 | 2025-09-17 04:14:00 | NPP-375D | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cfa60a94-dfab-3b38-986d-5b5510912e01 | -17.71759 | -47.94441 | 2025-09-17 04:14:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ac32a64-086b-3710-a4d2-7de5789c7083 | -18.23617 | -46.83727 | 2025-09-17 04:14:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ae24b57-4821-3a26-bddb-cfd0bc93a977 | -18.33013 | -43.31048 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5bcfb538-7251-3416-bb18-e9cfafc3923f | -18.33293 | -43.29215 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 69e8721f-ecba-3f6b-84f3-c3730efc8661 | -17.94321 | -45.25041 | 2025-09-17 04:14:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 632d99f4-96e5-3bff-b63c-d71a0e78f419 | -17.00408 | -45.85888 | 2025-09-17 04:14:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e52b40a-e0f7-3fff-a0f3-411ed1635926 | -23.50867 | -47.04827 | 2025-09-17 04:14:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ffe1adb5-7250-3e38-b966-5a37a8c75814 | -18.37081 | -43.32478 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 8b58b355-efde-3697-97f3-33df06b6ee31 | -17.32855 | -46.82188 | 2025-09-17 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cb8928f-b813-3ba8-90c4-86786b1051e2 | -16.89018 | -45.79143 | 2025-09-17 04:14:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a487aeb-623a-37cd-9f60-79bde050f06e | -18.16977 | -45.18777 | 2025-09-17 04:14:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb8b225b-a728-3fad-b49d-041c448836f1 | -23.48265 | -46.40256 | 2025-09-17 04:14:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6ee9bdd1-d292-3dc0-bdb3-f4cf0b2c70b7 | -17.33281 | -46.797 | 2025-09-17 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a60cf4a-5cb3-38ae-8320-b2163756cb81 | -17.04971 | -45.90299 | 2025-09-17 04:14:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3e35306a-cee9-3f64-aa46-7ac281d116df | -18.32788 | -43.30261 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8c3fb46f-58f3-35eb-b287-691028f5d583 | -18.5505 | -49.24779 | 2025-09-17 04:14:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f85af2bd-a321-3881-8524-c7e8544653d3 | -17.33353 | -46.81415 | 2025-09-17 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed4aca8d-728a-3053-83a6-09ccf95d7723 | -19.54931 | -47.68895 | 2025-09-17 04:14:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7abacb27-aa0a-3d86-9291-56d59c7ccd90 | -18.19564 | -44.53651 | 2025-09-17 04:14:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 993093cb-1034-30ab-9b6d-91a7b52edf1b | -18.19839 | -44.54074 | 2025-09-17 04:14:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6892006-85fd-36c2-b90b-34bfe3f0511c | -17.9653 | -45.24691 | 2025-09-17 04:14:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 659c8fa0-935e-381a-ba47-a2528f7bd2c1 | -17.20386 | -45.90382 | 2025-09-17 04:14:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e58ea43a-0ce0-3753-9cf1-aca9aad26f4e | -18.32622 | -43.29101 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e49fe9c4-c253-3f10-b3fe-664283be1b91 | -18.55145 | -49.24255 | 2025-09-17 04:14:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5b8e42e1-f55b-3522-abc8-2b3e415717d7 | -17.11437 | -43.59749 | 2025-09-17 04:14:00 | NPP-375D | GUARACIAMA | MINAS GERAIS | Brasil | 3128253 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c4c91c4-d933-3403-943e-8b16b9c7a25e | -18.17037 | -45.18408 | 2025-09-17 04:14:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6683204-994a-30f6-8c97-927817026934 | -18.25127 | -43.32413 | 2025-09-17 04:14:00 | NPP-375D | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d726f293-42ee-3820-a802-9b4fe4de808b | -17.31508 | -46.81525 | 2025-09-17 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9634ce0-9ce5-30a3-94c0-f45940469a86 | -18.19506 | -44.54015 | 2025-09-17 04:14:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2c07dc09-5b87-3228-8239-f73f06a31160 | -18.16041 | -45.22423 | 2025-09-17 04:14:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 10aac1b9-ea8a-32cf-ab9b-3d9329859c45 | -18.32118 | -43.30147 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 29c15c62-3d98-3018-92b4-89fa6e8bf59a | -18.3223 | -43.29412 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a7aa12b7-ac28-31f3-b93f-ef8f052cd247 | -18.54686 | -48.14491 | 2025-09-17 04:14:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95ccd9f6-da53-35b3-961f-705417162436 | -18.36135 | -43.33117 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a2c1924c-980a-3c18-b3dd-158173a476c8 | -17.05314 | -45.90362 | 2025-09-17 04:14:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 74064351-41bd-32ee-877d-ec470a584146 | -19.55138 | -47.6983 | 2025-09-17 04:14:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7557e0b3-4d3d-389d-adb3-9eb334dd7c36 | -17.31863 | -46.81583 | 2025-09-17 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce097c1c-04db-3679-9ef8-34ece02ee62a | -17.34131 | -46.81132 | 2025-09-17 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9785ab89-b387-3d34-8465-27f9a68a653f | -21.94672 | -48.00519 | 2025-09-17 04:14:00 | NPP-375D | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be868e75-a73f-334a-a4ab-c2f88040e98a | -19.28044 | -47.42916 | 2025-09-17 04:14:00 | NPP-375D | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4767f980-b54c-3eec-91e3-38d0530fc5d3 | -18.55315 | -49.24418 | 2025-09-17 04:14:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 6c299e83-921a-3bcc-8096-dbb0a676056e | -18.32565 | -43.2947 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4dc1ea41-a90d-36a5-9e35-37b635e253b9 | -23.12947 | -49.71486 | 2025-09-17 04:14:00 | NPP-375D | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 16ded377-27c6-30e8-b286-c9f24de27ff0 | -19.53352 | -50.59436 | 2025-09-17 04:14:00 | NPP-375D | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 1ed622db-7b42-3eb3-a2d8-0f8397db7c03 | -17.19702 | -45.91138 | 2025-09-17 04:14:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40368430-02ef-3f94-ae97-f896b82f70ed | -23.4842 | -50.3702 | 2025-09-17 04:14:00 | NPP-375D | RIBEIRÃO DO PINHAL | PARANÁ | Brasil | 4121901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| de25951c-4729-3731-a708-e11e314c6f3c | -18.32062 | -43.30514 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 932074c8-172b-3e4d-97bb-de504f987f01 | -17.19783 | -45.91858 | 2025-09-17 04:14:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d3878fa-dac6-3c62-b9b6-e6ad929ea445 | -18.32006 | -43.30878 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 25c00fe1-39e5-33e5-be07-d1625a55acad | -18.32174 | -43.2978 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4737cb7f-b92b-39ad-a629-db99be5e4612 | -18.36802 | -43.32053 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1fd99bfc-9182-35c5-9e9c-5c0b76a02656 | -19.28117 | -47.42494 | 2025-09-17 04:14:00 | NPP-375D | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2202367d-f921-3c95-a914-8946f10260a8 | -22.20224 | -48.35652 | 2025-09-17 04:14:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34966f33-4b57-30b6-a6ab-9d66678a7c4e | -17.32996 | -46.79232 | 2025-09-17 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5ce2d105-efaf-3bf5-90ef-9710d209b74e | -17.20043 | -45.90318 | 2025-09-17 04:14:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2793ffa4-9b9a-33c3-8ab1-9dba0dde42eb | -23.50463 | -47.05154 | 2025-09-17 04:14:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ca94195a-595f-324f-b769-038b593f8e47 | -21.5916 | -50.32806 | 2025-09-17 04:14:00 | NPP-375D | BRAÚNA | SÃO PAULO | Brasil | 3507704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| a57498eb-8af0-30f4-b78c-ad28157952a2 | -18.37361 | -43.32901 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7dd66365-2433-324b-8865-7f834a6a401a | -17.19638 | -45.91524 | 2025-09-17 04:14:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 182ebd6d-3967-335a-947b-3d1a96f76012 | -17.32998 | -46.81354 | 2025-09-17 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2120af1-f5ed-3a0a-bb0d-e399cbc8b246 | -17.32501 | -46.82125 | 2025-09-17 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4227d238-114c-3360-ac03-8d468fe6859b | -18.54058 | -48.13242 | 2025-09-17 04:14:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce41a47a-7133-3776-a6fe-505c4cf2a9aa | -18.32845 | -43.29895 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| aefb67b3-e143-3429-b14a-058f8b8881cb | -23.54492 | -52.90726 | 2025-09-17 04:17:00 | NPP-375D | RONDON | PARANÁ | Brasil | 4122602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8a4c99ba-f688-3348-8f61-8cb28d9f0abe | -24.75589 | -51.99069 | 2025-09-17 04:17:00 | NPP-375D | PITANGA | PARANÁ | Brasil | 4119608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1c9428e5-45a9-311b-8dc8-87c95bce9c83 | -23.81047 | -50.97835 | 2025-09-17 04:17:00 | NPP-375D | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 36ce07f3-faf1-346a-99b1-bb08581f6c6b | -25.12074 | -51.99914 | 2025-09-17 04:17:00 | NPP-375D | GOIOXIM | PARANÁ | Brasil | 4108650 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0e8acc52-bbb6-3648-bd6a-266b410f93f8 | -23.8065 | -50.9774 | 2025-09-17 04:17:00 | NPP-375D | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 76404365-5d48-3ca9-9898-1a7a5c132bd2 | -25.18228 | -52.40687 | 2025-09-17 04:17:00 | NPP-375D | LARANJEIRAS DO SUL | PARANÁ | Brasil | 4113304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 2e97da1c-b206-3be0-980a-0674c74e3a58 | -24.75506 | -51.99489 | 2025-09-17 04:17:00 | NPP-375D | PITANGA | PARANÁ | Brasil | 4119608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bdad33e1-c899-3ae6-9c3a-825240222046 | -1.97827 | -47.98349 | 2025-09-17 04:29:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab23a282-6686-3ae8-bdcb-31624f268da0 | -3.07227 | -49.46329 | 2025-09-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README33.md)
