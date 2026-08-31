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
| 395528ed-2267-344d-962d-c9bd7dfe3956 | -12.94482 | -45.91822 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c90b0387-9529-35d5-91ff-7f44db13ff09 | -15.23515 | -53.87727 | 2026-08-31 04:17:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 266a2e02-76d1-3711-bf90-e81f6f6e0a46 | -15.11595 | -40.04428 | 2026-08-31 04:17:00 | NOAA-20 | ITORORÓ | BAHIA | Brasil | 2917102 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9fef6bb9-593a-33c9-83d6-158cb027a320 | -14.1966 | -44.58541 | 2026-08-31 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11644f06-8a41-343a-a259-bb578cc69c25 | -14.58259 | -54.10009 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c74523d-0244-3548-a051-957902f87dd9 | -15.63433 | -50.101 | 2026-08-31 04:17:00 | NOAA-20 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 358d8ddc-91c5-3842-9028-134a8544912d | -14.4264 | -56.27959 | 2026-08-31 04:17:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40fdbf68-7dad-3ac3-b211-4b77d94fd8dd | -16.2775 | -42.58313 | 2026-08-31 04:17:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83520d44-84e8-3490-9e55-bca0950d6574 | -17.25065 | -44.86821 | 2026-08-31 04:17:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e91fa5f0-b55c-3308-aa3e-b0e71c0510a8 | -13.0844 | -45.18023 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| afcbe585-28a8-30ff-81fd-07d261c41872 | -14.59544 | -54.12353 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e6cd2031-554f-3cc8-8a21-85f7c653b0ba | -15.19641 | -46.23094 | 2026-08-31 04:17:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c33d536-ae7e-3410-a636-9fcd99d6e591 | -14.59968 | -54.10312 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6f75bb94-7b4a-33b7-a772-5ce284713868 | -14.59507 | -54.11636 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9f27ca75-d07d-3c0a-ab1a-300534aae617 | -14.41 | -52.53006 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 70881ded-7c37-340f-b287-039ffd371e00 | -14.58126 | -54.1263 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 28838cf2-5ed7-3a1f-bd5c-0fcb1c3e9ce8 | -14.58323 | -54.12532 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ffcf72d8-90e1-3dc5-b4f0-9697c7154239 | -15.24613 | -53.87983 | 2026-08-31 04:17:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ec83efc-eb13-375c-ac86-ec80e05a921d | -15.41034 | -52.708 | 2026-08-31 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 775d5296-755f-31f0-9731-b8e32d0bd161 | -16.98719 | -40.93423 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 944801ea-688f-33ca-9313-92eae27467c9 | -14.59718 | -54.11515 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c0b06d6f-7df9-301b-aaf7-61bff94022e9 | -14.6028 | -54.11654 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f46fc1f-d65b-350c-8c7e-6b1f56e8ccfc | -17.9915 | -44.31154 | 2026-08-31 04:17:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7211c50-b818-3da4-a6ab-fd47d078cdcc | -14.58205 | -54.12239 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a69be1de-d117-37e8-9e30-e1dbebdfafe1 | -13.48172 | -42.47937 | 2026-08-31 04:17:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 58876051-22a4-3d1f-9326-7687388f4f0e | -15.23592 | -53.87348 | 2026-08-31 04:17:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76d6970c-ac99-35e1-a9a8-907fd48b28b2 | -17.53941 | -44.61312 | 2026-08-31 04:17:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d6ef05d-bd6d-393a-8434-0e5c83437263 | -15.1999 | -46.23154 | 2026-08-31 04:17:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95733b5c-38d6-306e-8537-d97bef1621a3 | -12.94415 | -45.92226 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2316c4d3-ff1f-39fb-8337-8acc51132655 | -12.7201 | -49.07775 | 2026-08-31 04:17:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2f52e447-c4a7-36a9-bcdc-75151e06ebd6 | -15.08802 | -48.10716 | 2026-08-31 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 7e157331-b52b-38dc-a6d4-9fb382ead02b | -14.22131 | -52.85093 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55d00ab9-bce0-350b-aaa1-a8d758ca522c | -15.91626 | -56.22975 | 2026-08-31 04:17:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0173c14f-53ba-3aa5-b476-0e42cc5a9e35 | -15.71165 | -48.25264 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f95dea2-6774-351e-a6b2-91d3ce40390e | -12.89171 | -45.84675 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab07ced1-dec7-399e-bb92-848431ceaedd | -14.60608 | -54.10073 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c4dd99df-2f3b-354b-975c-da3a44ed26c8 | -15.6281 | -50.08683 | 2026-08-31 04:17:00 | NOAA-20 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a54aa24-6bb3-3676-a9cf-7f4810623005 | -14.38822 | -52.55891 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0071bf8d-9521-3b94-a3bb-ecb12d1eb2a7 | -13.36387 | -46.92468 | 2026-08-31 04:17:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f844ebd6-e3a9-31b9-9288-c941fd047979 | -15.20338 | -46.23215 | 2026-08-31 04:17:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2170bb24-4cb7-3eb9-b0b9-eb53a8f53c52 | -14.19719 | -44.58179 | 2026-08-31 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af898394-4c4d-335f-a5f0-dc5ff4f34a41 | -13.63992 | -51.84209 | 2026-08-31 04:17:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e9b8dd88-19f2-3f0d-a573-ca4375ddc155 | -14.57957 | -54.1054 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc4d1a7f-dfa0-3576-8b72-64048ef262af | -18.28255 | -52.69217 | 2026-08-31 04:17:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9eed8892-4775-3d54-8c6a-9878607523f2 | -12.87768 | -45.84427 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 486dbc37-9094-3d38-a1b3-c4db6f3117c4 | -15.39676 | -52.696 | 2026-08-31 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f71e0a3f-e178-3a56-af85-9e2f055e47b5 | -14.17716 | -52.87936 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fcc8464d-5811-3cda-8782-7c3436e59e2e | -14.30186 | -52.90882 | 2026-08-31 04:17:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d14ce3b2-7bbc-33a2-b356-3c558f4f95ec | -14.40427 | -52.53196 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5bd87809-5ce6-3dc1-91f8-bc286565b14b | -15.4097 | -52.71124 | 2026-08-31 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 168b4659-4735-3bc3-8b2c-4bac6fccf90b | -13.96517 | -54.40316 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 67760b21-7025-385e-be5c-f02344a50c57 | -14.5963 | -54.11937 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 045d8b71-63f6-37bb-aadf-4ce8a9f564bd | -12.78298 | -46.46255 | 2026-08-31 04:17:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6bb60873-01ec-3fb1-a747-0e6a0ceae039 | -14.4427 | -52.52688 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5bbc8312-3bb5-30bd-94e5-07e020036e54 | -14.20269 | -44.59018 | 2026-08-31 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80705a06-166c-375c-af79-635f1b4f9446 | -12.95093 | -45.94757 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5dd98e93-333d-32f5-b026-bd5c579e71a6 | -15.40339 | -52.70175 | 2026-08-31 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 79de1596-0df4-3d48-ac5b-004d0d70b374 | -14.59017 | -54.1114 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 723922a4-8048-38a6-8e53-ecb9d21ef217 | -12.72421 | -49.07626 | 2026-08-31 04:17:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef8f3ad3-ba62-32d2-b725-eeb1e03d6a33 | -17.0873 | -47.20138 | 2026-08-31 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 68e7c802-5fe0-3416-a441-d981fbb3a6e2 | -14.23114 | -52.85663 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd014552-6653-3fc8-ace6-91e3e5704d3d | -14.58613 | -54.10215 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8058f7a4-5a13-3616-bac3-b33d8510052f | -15.2414 | -53.8748 | 2026-08-31 04:17:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa9785a2-a592-3657-916e-f29101a68cd2 | -12.94948 | -45.93487 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc81f4c9-0573-3130-9a2d-76ae594b8218 | -14.20029 | -46.55892 | 2026-08-31 04:17:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 83d340f0-7905-3cea-8261-543e060bbf1f | -15.40584 | -52.70382 | 2026-08-31 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d34c6f49-f756-31ed-8557-5aa12227a45f | -16.28592 | -42.57319 | 2026-08-31 04:17:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9b32fd5-c3a1-3743-83f7-328bcd388c01 | -14.42719 | -52.52424 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0fafb8dc-4d70-3ef9-a76f-9376516655b2 | -16.28423 | -42.58429 | 2026-08-31 04:17:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45c42a46-ba12-31c7-ba04-f0aee011b98c | -14.45714 | -42.6464 | 2026-08-31 04:17:00 | NOAA-20 | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 816d6186-404b-308e-908f-a9fd06ecad4c | -14.44973 | -52.54563 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd73bbf1-bd40-33f5-876f-b297355783de | -15.51337 | -56.03291 | 2026-08-31 04:17:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5316bb59-bfed-3a85-a000-26e2d52c6b8f | -15.41166 | -52.71336 | 2026-08-31 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9bab6af2-3684-3cb6-913a-52ac3fbe20cd | -14.19529 | -46.56662 | 2026-08-31 04:17:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dcf1ca5f-63a3-3516-9828-416e72ce7f7d | -14.43173 | -52.52833 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fc8697e9-8050-3fca-9f72-6670b0f527f7 | -17.79696 | -39.7035 | 2026-08-31 04:17:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0e4152ca-d11b-3873-b2df-a3d788643046 | -14.38759 | -52.56205 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3000466b-6ecb-39db-b309-f7ad7cc51fcc | -14.57286 | -54.11836 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d0d6e767-dbfd-3697-9d59-e5a8e5121112 | -14.5781 | -53.08163 | 2026-08-31 04:17:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9ade8ba-1323-3759-987a-261660fe6766 | -19.95214 | -42.30849 | 2026-08-31 04:17:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 58c4feea-a389-3139-9985-3dcecf6399d4 | -18.27546 | -52.70225 | 2026-08-31 04:17:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d65d572d-0a0b-3178-bcbe-e109fe9f67ec | -16.27976 | -42.56827 | 2026-08-31 04:17:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c3bdd3a-6c22-347d-9e86-e3b44085a5f3 | -14.38701 | -52.56494 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe729969-e9c4-3c69-8629-58557174df68 | -12.9481 | -45.94291 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 526d6954-881d-35f7-a512-d772a9d76e2e | -15.77406 | -48.52736 | 2026-08-31 04:17:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b495b105-7df8-34a9-aca4-23b462e0127e | -15.19368 | -46.24685 | 2026-08-31 04:17:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 927ba9b8-1ba3-3eba-9e18-d01701809a08 | -13.62877 | -51.847 | 2026-08-31 04:17:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 355f2312-46be-335d-b506-e71197806edb | -12.9398 | -45.90489 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| edccf288-e223-3e2c-8b0e-63e969e8b3a1 | -15.61721 | -56.41967 | 2026-08-31 04:17:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c2a41d3b-3fec-34fd-b9a4-049a40c2513a | -15.66915 | -45.93462 | 2026-08-31 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4885028f-85a4-33b8-a9f2-ab0af6650414 | -14.12634 | -52.8111 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b3cb76b6-447d-3b94-83af-447dc1948e92 | -15.24065 | -53.87852 | 2026-08-31 04:17:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80a8042b-39bc-3cbe-9bf5-e181f6a2c711 | -15.33886 | -43.67106 | 2026-08-31 04:17:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c2907ba7-a690-3e68-a998-31b3af89c8b5 | -14.2364 | -52.85777 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3803b9a7-a0c0-3e34-bc4a-786125f3900f | -15.91118 | -56.22292 | 2026-08-31 04:17:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 3ed9450f-c558-30f5-acb6-d4490e21d883 | -14.60135 | -54.0951 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3ceaaa76-6f6f-3bb6-904f-98a77c0eaef2 | -16.27414 | -42.58255 | 2026-08-31 04:17:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| da972970-6073-3951-ba13-ec8daa041ca1 | -15.4147 | -52.71288 | 2026-08-31 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 55e9d552-c1b7-33b4-9109-906a0d506635 | -13.3884 | -41.32796 | 2026-08-31 04:17:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e7012f42-e659-39c5-bff3-adab0129dea4 | -14.29865 | -52.89752 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README33.md)
