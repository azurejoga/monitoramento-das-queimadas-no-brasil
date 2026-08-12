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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4343263-b1b2-3a2c-8bcc-c90c6325ceec | -11.97494 | -46.397 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d07f5cd3-550d-3fb6-adda-0dbcd15a999d | -11.4045 | -42.07778 | 2026-08-12 04:17:00 | NOAA-21 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7c5a7ce0-76dc-3964-b659-838c09be3b22 | -13.89685 | -53.83662 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abf51803-d11f-3eea-8a65-be2a604f88ec | -19.99643 | -49.67886 | 2026-08-12 04:17:00 | NOAA-21 | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a6fd2f61-f192-35b7-9545-69930adaab1d | -13.8994 | -53.79627 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 27a866d0-bc2f-332f-8428-60a9d93a1435 | -13.52786 | -46.28699 | 2026-08-12 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f59592e4-1144-3180-9a83-8806dc2156ac | -12.31523 | -49.79504 | 2026-08-12 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c2cc077-fa82-3618-8027-6574c9d8f384 | -12.14185 | -48.27066 | 2026-08-12 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| af9023e3-0b4b-3d2a-9976-a6386890c227 | -13.57538 | -46.26052 | 2026-08-12 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1844dd44-74f8-39d8-a038-f85686a7827c | -9.35395 | -47.53717 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54f8ff5e-bee2-3ff2-914f-09e3faffeb50 | -11.9824 | -46.39434 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c5669150-6d3d-33a8-8c92-d4d714c707b2 | -11.98613 | -46.37136 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fa1f0373-8e3e-390f-b7da-1a6fd81c3f2d | -14.28342 | -45.28214 | 2026-08-12 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd62d5d6-e816-3a91-ad0e-b977649e5212 | -10.63967 | -47.48589 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 88a07ab3-19a9-3c9c-bcb7-e3e0743ca423 | -13.89489 | -53.7921 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 783dc0e1-d03c-3404-ba96-b45071b1b5e9 | -11.93389 | -47.35453 | 2026-08-12 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c301e317-5844-32f6-b2bc-ffa588ce1c59 | -9.02745 | -47.46867 | 2026-08-12 04:17:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1e981bf-89aa-3025-9853-c7337d6503aa | -9.34956 | -47.49546 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bb0de2e-ef9b-378c-a86c-979a1e2c9dd2 | -11.96872 | -46.39209 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2bc0b4cc-602b-3f29-a201-141271d159ac | -10.70402 | -47.90434 | 2026-08-12 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8fc68e15-0756-3387-a7d2-a40353899027 | -9.33693 | -47.52526 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91c48b04-e3e9-3016-b9ca-83ace3a1b0da | -14.59333 | -46.76071 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22103ce5-ff3d-3482-849d-80ebbdef41c3 | -15.52209 | -45.85868 | 2026-08-12 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec0fa6aa-06e1-328b-ba95-44602484df1c | -9.34363 | -47.50813 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 019ee46d-e5e3-30eb-a16c-5d563dda624a | -12.10673 | -47.18648 | 2026-08-12 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fbb0d96-5f4c-30a8-9f47-13f1d227d707 | -14.33433 | -54.04126 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5ebdfa63-3f45-3c04-9a28-41f5ab1b974d | -9.35179 | -47.48225 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6c892d7-478d-3053-a5f8-82516d60c5c0 | -14.54926 | -50.4016 | 2026-08-12 04:17:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 18c45362-1172-3ede-aefc-8718b1ec0d1f | -13.86903 | -53.76126 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dba71662-bd24-385f-b4fa-8dd761a2d951 | -11.98208 | -46.37473 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 42c99980-af01-3e28-a59c-ee095f21e9a2 | -13.54372 | -46.2745 | 2026-08-12 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8e72faf6-fe49-33df-afb4-d131c2d121a1 | -11.95438 | -46.35091 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f874f87e-cefc-3217-a651-0613515f6d4a | -15.01286 | -46.57487 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9db697bb-9af1-306e-bfa8-3bee657e7940 | -20.95716 | -48.8941 | 2026-08-12 04:17:00 | NOAA-21 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fce4ad65-faa5-3125-84fc-902e7bd4cf77 | -9.03035 | -47.49669 | 2026-08-12 04:17:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a9d3200-beb6-3530-be75-019f61e71a4c | -11.97337 | -46.38508 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 83af58c0-a4aa-385e-aa38-e3de2fb09901 | -14.98114 | -46.59986 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5445c14-cb30-3ea8-879b-b966d814e25e | -21.59795 | -48.49272 | 2026-08-12 04:17:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fdee4b7-a927-3bd6-a83a-a97e583f6b16 | -9.34063 | -47.52586 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fe731ec-b1c3-3e0f-a6be-cb6887aeb832 | -15.30211 | -48.8765 | 2026-08-12 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 092ed729-055a-3f07-a179-636591b106e3 | -14.98966 | -46.59 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6e9afc7-8b2c-35e7-9510-8fc75a952c67 | -14.53627 | -50.33415 | 2026-08-12 04:17:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70f3c403-034d-358a-8e8c-dbb432f53ac7 | -13.89606 | -53.78608 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 644b7736-e48d-30c5-baae-a591f2a8bd26 | -11.78594 | -51.86302 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4ba73aae-cb8c-3194-9f72-30393f61d827 | -11.97214 | -46.39265 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5c11e79-4114-3d3a-9383-4075816c3bc9 | -21.4993 | -48.63987 | 2026-08-12 04:17:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb3b5971-46f9-342c-b199-44f16274f70f | -13.25513 | -50.3764 | 2026-08-12 04:17:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eab34d22-6b21-3fbc-bf0d-3c166f2df186 | -11.95288 | -46.33868 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9704e8ae-8755-3d89-b0b4-5fd030fed376 | -13.85643 | -53.82493 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8185f600-eee0-3420-a319-db7b9631e9e2 | -12.1024 | -47.19302 | 2026-08-12 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fa26f50-9f1c-38a1-8fd2-eec270d460ca | -9.33172 | -47.53351 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47b59707-95f3-3971-83ae-684e70eb41ce | -9.34512 | -47.49929 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9c342be1-4cbb-3fe0-89fa-be5ac9eedacb | -14.55398 | -50.39869 | 2026-08-12 04:17:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 61911121-a8d6-3237-9bc1-26cdb0cb78e0 | -10.44917 | -44.94371 | 2026-08-12 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c42b2036-ac7e-3f46-8c97-f9045c79d3be | -11.65764 | -50.12967 | 2026-08-12 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 470e8576-a648-33b2-af64-a353b0875f97 | -10.63605 | -47.48524 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7ef417a9-1a53-3849-a4b0-64a9c5c9411f | -10.4696 | -46.61743 | 2026-08-12 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f360696-4452-38a1-bb14-b6bdb3011a74 | -11.82404 | -51.85153 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e4f853b-f66e-3a02-9c7f-f98b817b752c | -11.47054 | -46.6876 | 2026-08-12 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e50b3a4d-e996-3588-b178-5c878ffa69f7 | -12.10255 | -47.1899 | 2026-08-12 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6dcccb0f-045d-349a-b5f8-4f6c61d5f0d1 | -19.87875 | -44.0528 | 2026-08-12 04:17:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f8795b29-ea04-3737-82b1-50c781370bfe | -14.52956 | -50.34813 | 2026-08-12 04:17:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60ecf3ef-4a2d-32e2-a3a9-c8eccec31226 | -14.32859 | -54.04313 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c4795b0-63a6-3f52-8aa6-f72730687cad | -12.17382 | -50.11794 | 2026-08-12 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48a29d1f-ead0-3292-a726-c51a3797c5b8 | -13.90137 | -53.84085 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9636ba31-c3fa-3c0a-a793-7ae4c48c43c7 | -10.22809 | -45.92689 | 2026-08-12 04:17:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6ea0719f-1374-3bb9-8f99-41940c42e252 | -9.34437 | -47.50372 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9f621adf-7c5d-3dc4-bfbb-b6d086592b06 | -11.48767 | -44.57088 | 2026-08-12 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a2f01924-8cc1-3173-8f41-fe1bd69a60a4 | -14.30497 | -51.99423 | 2026-08-12 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7ff3f0e6-e86b-3d89-836e-bee78c2097ab | -14.58438 | -46.75149 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 781ee9d9-9865-3cbf-9478-aa82d4b748b4 | -12.10592 | -47.1936 | 2026-08-12 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07c94adf-2977-3b3a-8685-ef47b23252ae | -21.4199 | -45.94201 | 2026-08-12 04:17:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d1608c1f-5b9c-3ad3-b2bb-e51f06974c4e | -13.89744 | -53.80627 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8c943e5-40fa-32a5-b2ba-4affba992dbf | -15.29226 | -48.87236 | 2026-08-12 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eec8c47a-368e-339f-997a-0aca8428b072 | -16.1034 | -49.88894 | 2026-08-12 04:17:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d1d40cfd-bf14-36d3-ac46-d7e6103fadfd | -11.94692 | -46.35361 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| aa2fed93-8b02-3b3a-8049-ead02c812d27 | -14.4802 | -51.87119 | 2026-08-12 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 065e7455-3534-3641-a622-a5de68ce82d5 | -15.30043 | -48.86891 | 2026-08-12 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cfbba82c-bc68-3ad3-9a78-c612328ffa87 | -11.95481 | -46.32697 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6809c24f-e5a5-3f6a-9fa8-df24d6a150a9 | -11.61072 | -54.649 | 2026-08-12 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0435804e-b0a6-3ea5-ad13-17f0ed59d1de | -11.98335 | -46.36687 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6be852a5-8d8d-3fce-9dc4-5b1305b48ee2 | -14.97993 | -46.60731 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2332a6da-c840-36ab-99b7-3a81fb948113 | -11.78685 | -51.85801 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d7dc9c8a-45c5-38bb-b06d-efe744e54517 | -9.34881 | -47.49989 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb686aaf-0812-3c52-9a02-27d681976ac9 | -9.57127 | -44.58075 | 2026-08-12 04:17:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b5c9865-5036-3baf-9236-c092ff936a71 | -14.39897 | -52.07508 | 2026-08-12 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 9f14d743-544e-3651-813a-24bdefe3a66a | -10.09542 | -46.22306 | 2026-08-12 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39ab1bb5-524a-353b-b6d7-af42a34ee0b3 | -9.34809 | -47.48164 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61c841e0-efda-3ec1-ba4c-2590010ecb94 | -10.10076 | -46.21214 | 2026-08-12 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0462e49e-1253-3829-ad9c-c4d6837881cb | -13.30214 | -49.70256 | 2026-08-12 04:17:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| fb88a390-7729-3a40-93b1-e1d18d59a7bf | -12.55869 | -48.34853 | 2026-08-12 04:17:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 255c3352-f19c-3657-8067-6508bb823035 | -10.10013 | -46.21596 | 2026-08-12 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae42f0fb-4b43-347b-84f1-defe09161ab0 | -13.83318 | -53.82578 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd57cdb5-ee07-375e-bee5-85b24b1679a1 | -11.65625 | -50.1375 | 2026-08-12 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b11ef254-3665-3ebf-93df-a1270512ac39 | -13.90774 | -53.83553 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 199431a3-424d-3822-b86a-0d1b3f4f6e89 | -15.01535 | -46.6023 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6cccff9c-b57a-3935-b663-30974f5470cf | -14.30633 | -51.99335 | 2026-08-12 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08509a5a-6328-3524-a604-2bf7a0fa3869 | -11.97816 | -45.78928 | 2026-08-12 04:17:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e79d580e-7fce-3299-9232-e6f6b2e198ca | -9.56795 | -44.58022 | 2026-08-12 04:17:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b158090f-eb03-3ad3-bfdc-a9a6e86d85d8 | -13.86614 | -53.82986 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README12.md)
