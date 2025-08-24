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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d231636-4999-3df0-bc21-306d9a43be91 | -11.17755 | -55.02571 | 2025-08-24 05:01:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d316b3d8-3bc8-3bc6-ba8d-977f496ffb5b | -13.62317 | -48.16787 | 2025-08-24 05:01:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6fd7d6e9-df1b-3929-89c0-8ecaaff612a6 | -17.5938 | -46.09635 | 2025-08-24 05:01:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2329b0e0-54c3-33e4-bc01-f8307bc8506f | -9.01593 | -65.69068 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1515439-0ba7-3a6d-8d95-a22ae8d21463 | -13.18216 | -59.17485 | 2025-08-24 05:01:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57213231-83b8-3810-891b-a7aeeb801bde | -13.48867 | -46.89402 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51d7dd08-58b3-3945-afaf-c038c755883b | -15.67515 | -53.87339 | 2025-08-24 05:01:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 98b1a0b4-1618-3d2a-961a-cbde651cbc6f | -14.3355 | -58.59394 | 2025-08-24 05:01:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d56e539-a1fa-32cf-a351-6b322a1f06a4 | -9.52021 | -60.52136 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 498a568d-43e4-32de-8f97-7ea98383b848 | -14.76862 | -59.64983 | 2025-08-24 05:01:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a93920bd-d52c-3ca7-9ca5-b1fd54f99561 | -11.52651 | -51.91707 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecfd3c7b-ebdc-3290-a46e-3e87e8d2a1ab | -9.01049 | -63.63136 | 2025-08-24 05:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37994c0a-e40e-3373-b454-2ab837d15667 | -13.03826 | -45.2247 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63c00a9a-59c3-3965-ae4b-a9d8ce54869f | -16.78641 | -51.35375 | 2025-08-24 05:01:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d9b93594-9341-3183-970d-560a4f13f87b | -16.51723 | -46.73503 | 2025-08-24 05:01:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7166178a-50e6-30d1-85fe-1a507c7b006c | -13.02137 | -56.82566 | 2025-08-24 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c5fd90c-9653-3a49-9cc6-b6fe2a847d20 | -14.2935 | -60.38307 | 2025-08-24 05:01:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b01bb2c8-cffa-343d-88d7-182940c49efa | -11.53142 | -51.9091 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68bc3277-fb84-37a9-9439-a1d021650a06 | -9.47691 | -63.13237 | 2025-08-24 05:01:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9a96b73-382a-3914-a2db-b8753c1c3901 | -11.51151 | -51.86649 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 47e5523c-885f-3760-9e03-576c8119a7c5 | -14.65709 | -56.58602 | 2025-08-24 05:01:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 00162cb6-6850-3e1d-88ef-ec85813f4bbc | -13.01186 | -56.88409 | 2025-08-24 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6873bcbe-3165-3a3a-94cb-d89f41c2b790 | -12.94756 | -46.29181 | 2025-08-24 05:01:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ee97a26-260f-3e60-8594-6f2fc126ca9e | -12.48488 | -53.81851 | 2025-08-24 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cc29666-3980-3c68-a864-a5642c10da7c | -9.023 | -65.3899 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f06d8a19-410b-3b5d-b820-8c1f682740a0 | -13.03298 | -45.21988 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3df13677-06c6-3d5b-aa7a-07f549f982a1 | -12.99745 | -45.2237 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e32be41-5833-38ae-b6c0-4d35af948006 | -11.70401 | -60.18461 | 2025-08-24 05:01:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97297ada-be10-3cf1-b229-7875722bdc6d | -14.46666 | -52.07674 | 2025-08-24 05:01:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2bf4a71-3db8-365e-9615-8505c6addce2 | -13.05027 | -45.22204 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4c56588f-1d09-34bb-81d1-0fa41712f0a9 | -14.32845 | -58.59264 | 2025-08-24 05:01:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 034932ce-890d-3216-af13-647b4df3304b | -15.13114 | -48.63115 | 2025-08-24 05:01:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d93f2c94-5917-386d-a686-945f6cadc584 | -13.62861 | -48.16326 | 2025-08-24 05:01:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1638f650-f02c-377b-b2cb-f2c7d0dfae39 | -15.72701 | -56.0506 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3067a647-87f7-3dd0-ab65-932bfc27c4eb | -13.03778 | -45.22874 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 35436990-ac64-3180-ad13-8ccf02c4982c | -18.40362 | -46.84372 | 2025-08-24 05:01:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de8eef61-8c7c-354b-97dc-f705b84387f4 | -16.79402 | -51.35828 | 2025-08-24 05:01:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| dbbd6d23-896e-3ee0-99e3-95ea373489f0 | -9.02271 | -65.68753 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fca12b07-b7a4-3dda-8cc4-daf2fd6ccc94 | -9.96011 | -60.1817 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba444c27-0d49-389c-8966-18a36f6d1f15 | -12.99076 | -45.23103 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 97144ccb-f7d6-3858-8027-b2aaf29893da | -15.46145 | -55.9771 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8e2aa085-419c-39a3-8ce5-d772daded25e | -11.67034 | -51.59569 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3be727a3-01a6-3054-a060-5516a0653ee3 | -16.42328 | -49.1479 | 2025-08-24 05:01:00 | NPP-375D | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab3902eb-6072-3e9a-842c-730d97877c9b | -9.33183 | -63.19593 | 2025-08-24 05:01:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b05e17b9-79ed-3e7e-86b3-1e34b781d434 | -18.3983 | -46.84844 | 2025-08-24 05:01:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1bf9d07c-3085-315b-8f6d-baff8c483d2a | -13.46835 | -47.01513 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 02f342b9-cb93-315e-9810-832ca7595fff | -18.40402 | -46.83975 | 2025-08-24 05:01:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8f44a42-85e1-3d20-8efe-14c2f881a638 | -9.00465 | -63.63361 | 2025-08-24 05:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 104ab074-8762-3a02-8bd4-da5d13b5884e | -13.16689 | -46.91902 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8f7fb59-8adb-3afc-a657-8ac3d30681d4 | -9.01349 | -65.70383 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e3ee9951-9d2f-32b3-aeb1-c3a765c0ee0a | -10.89379 | -55.78545 | 2025-08-24 05:01:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34660635-f757-33c8-b0b1-85ef727ff388 | -14.28739 | -60.37221 | 2025-08-24 05:01:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8217818-3792-31f2-bd9c-6390d64852ca | -17.39414 | -42.6261 | 2025-08-24 05:01:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6b033dd5-60b1-3a98-afec-d95fcde5543e | -15.11209 | -48.66148 | 2025-08-24 05:01:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7630ea6-5f0d-3908-8562-07f99aa9178c | -9.82227 | -64.26643 | 2025-08-24 05:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05f77a5f-88b4-301b-9792-3fd658b02b75 | -15.12646 | -48.6301 | 2025-08-24 05:01:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f493df2d-80c8-3171-acb7-cc91ae2a5c0a | -15.92021 | -52.20791 | 2025-08-24 05:01:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a1d4279-8405-397d-b9f5-c99775de0d3f | -11.53507 | -51.90967 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e2360bb-70b9-3ba5-aabd-d357b38e547b | -18.39914 | -46.84068 | 2025-08-24 05:01:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f49397ea-f365-3a33-9d35-f795c68b7619 | -11.53016 | -51.91764 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0843a3c-3686-3c76-a6d0-f79920dbb227 | -10.10093 | -57.76691 | 2025-08-24 05:01:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5041bc77-030d-3ac0-aeb6-111848b2b1ed | -9.94564 | -60.16776 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d74ff49a-2ca9-3077-8689-4aa839a4be8b | -12.94507 | -46.29157 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c99b75c8-a05b-3f2b-987c-7057e96e8d3f | -16.50005 | -46.75039 | 2025-08-24 05:01:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9a23a87-0ed0-321c-b147-97813781c59b | -14.40032 | -49.76731 | 2025-08-24 05:01:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 87794d5a-c0de-3755-bbca-70e99257ae7a | -15.32121 | -56.16004 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d96b163c-5f2a-37a3-8837-141994ef7883 | -9.01019 | -65.69874 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e9db6575-1485-3133-a32f-c4376d5ea0d1 | -9.02625 | -65.70192 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1d2a2e2b-d520-39f2-8dc7-a3319d579334 | -9.01263 | -65.70846 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e0b15714-982a-317a-b34e-04585b377e91 | -14.76439 | -45.37566 | 2025-08-24 05:01:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cec3aee5-a769-39cb-8b85-f0877236c81f | -12.99792 | -45.21964 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41abc88e-88ce-3804-8b88-662d2ce340cc | -17.6115 | -44.30167 | 2025-08-24 05:01:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 07439a1b-7f1f-328b-86b7-9615247c8528 | -17.593 | -46.1039 | 2025-08-24 05:01:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6fd2330-93ef-320c-8747-5ff01957af1a | -9.00664 | -65.70728 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4f9ed407-a26f-3cbb-b7cd-4a1dacf9b9b6 | -14.96061 | -54.79924 | 2025-08-24 05:01:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5ea1a53-189e-3858-a156-dc0ac328b3c5 | -13.4167 | -51.80873 | 2025-08-24 05:01:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aaa8d3b8-36cb-38fe-a321-bb01eeb66973 | -13.04499 | -45.21732 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98b9c0df-de3b-37b8-9de6-e26ccbd8b0da | -9.94219 | -60.16336 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 564fc8e1-c2fd-3adc-a725-bcb9c6f38e34 | -14.65941 | -56.57158 | 2025-08-24 05:01:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e95e9a3-e05f-3e4e-99a2-8701cc8d91d0 | -13.46245 | -47.02047 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c6b756a-dcf2-3950-bbad-d88129169040 | -13.57601 | -47.57283 | 2025-08-24 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b0bfb06b-2eda-34b0-8df1-4edc788a615d | -9.95191 | -60.18023 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 194dc656-e5e3-331c-b488-09196bc25729 | -9.65422 | -59.63614 | 2025-08-24 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f045db24-b24a-3478-b83c-a1eb4b68c55b | -15.3084 | -56.17626 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c48bbf4d-4951-3246-97a2-be507652c26b | -15.03693 | -48.18034 | 2025-08-24 05:01:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a15a257a-49da-396d-9ecd-9e546fddfaca | -14.28614 | -48.0224 | 2025-08-24 05:01:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3c3f0b2-ea43-32d6-af9d-66c7df9f54ba | -14.79335 | -47.94244 | 2025-08-24 05:01:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 76e8eb8d-a7a2-3260-9ea4-c97a5db484ea | -16.41536 | -49.94482 | 2025-08-24 05:01:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff48f113-62db-3182-b9b8-4602fcf58d64 | -9.51942 | -60.55379 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d6b63f73-87c3-3101-a2d6-0b375b5109d5 | -11.52372 | -50.48046 | 2025-08-24 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce8d0ddd-b4c1-3dd9-896d-252052a9f77e | -9.95537 | -60.18462 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ea5ff70-6bcd-30ce-8cd3-18759832da56 | -11.54958 | -54.39256 | 2025-08-24 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b2c6271-73f5-3bff-aee9-bdda3bcfb7a0 | -13.41617 | -51.785 | 2025-08-24 05:01:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc546131-8773-3d5c-a328-e309eafbdf45 | -11.90368 | -47.11546 | 2025-08-24 05:01:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3fad996c-dfb8-3ea5-9cf1-4d08d1650f7b | -16.79476 | -51.3577 | 2025-08-24 05:01:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| b22c4b6f-b464-35bd-b9a8-c1b6c9cb448e | -9.94328 | -60.50156 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd3d1d00-28ed-3978-b296-c7c04fd31883 | -14.33903 | -58.59457 | 2025-08-24 05:01:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bcf510fc-1414-3501-ad39-606a3f84b8fd | -13.47898 | -46.88704 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce473f13-acf9-3844-9f73-a435a854982c | -16.96839 | -45.68989 | 2025-08-24 05:01:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 52cbea95-9ce4-3a26-a923-e03d8b5fd67d | -9.80746 | -61.20899 | 2025-08-24 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README69.md)
