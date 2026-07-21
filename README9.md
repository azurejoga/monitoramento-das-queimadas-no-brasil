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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84675d4c-83e0-3f1b-bfd9-de9403ddf66b | -19.84626 | -49.0704 | 2026-07-21 04:29:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aa5c8eca-09da-3127-a909-46afc22c0f47 | -19.61123 | -47.64634 | 2026-07-21 04:29:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 04b4e645-f240-3a64-b9a6-58a5115528aa | -19.30296 | -45.45865 | 2026-07-21 04:29:00 | NOAA-21 | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88aca60a-1eee-3db3-afda-a9582e768ad7 | -20.43064 | -46.46881 | 2026-07-21 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 044c40d1-1e29-3a6e-87e9-008c65d32636 | -20.70412 | -50.53107 | 2026-07-21 04:29:00 | NOAA-21 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| dca9dccc-b81b-383d-836b-267558b343b4 | -17.45956 | -47.15473 | 2026-07-21 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1b2f19da-6dcd-3c4d-9357-3153c210472c | -17.58582 | -47.51192 | 2026-07-21 04:29:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 04b25948-6e54-30f5-8286-96e7a20dd69d | -18.55444 | -56.81461 | 2026-07-21 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.4 |
| 789b5d63-936a-3689-8ec5-f96532a61c40 | -18.55339 | -56.81981 | 2026-07-21 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.4 |
| f4140ccd-d885-32f8-aa85-63c22c9de1c9 | -18.55233 | -56.82502 | 2026-07-21 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.9 |
| c25210c1-6315-3a1b-9348-4961c5729962 | -20.43421 | -46.46937 | 2026-07-21 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cd827272-c2dd-39a7-9233-ebc663fdd168 | -18.55193 | -56.81748 | 2026-07-21 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.8 |
| ac2c297c-80ff-39d2-8b9b-7e0153d86767 | -19.71882 | -53.24042 | 2026-07-21 04:29:00 | NOAA-21 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc3ef36b-95f8-351f-bfa3-42545be8d1f7 | -18.55549 | -56.80943 | 2026-07-21 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| dfb27c0f-81a6-3154-9edb-c6c11fb24150 | -17.58246 | -47.51139 | 2026-07-21 04:29:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ecf793b-170d-382d-96f3-a22744018f67 | -18.54725 | -56.81646 | 2026-07-21 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.6 |
| a3fee54e-dad2-3130-9131-59666ee4b4d9 | -20.51719 | -48.85905 | 2026-07-21 04:29:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 836b8355-3925-36cf-93f3-cc07e3383a87 | -18.54871 | -56.81881 | 2026-07-21 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.7 |
| 9b0368c5-6972-3a7d-8c26-f24d0c7fd1c7 | -15.4186 | -47.58523 | 2026-07-21 04:29:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 56236ff5-6331-3bf3-84bb-4effe77f24c6 | -19.60896 | -47.63809 | 2026-07-21 04:29:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9be142fb-2f83-30c5-968f-0aeb3f712593 | -17.58693 | -47.50449 | 2026-07-21 04:29:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9843052f-2f32-380d-8ee0-07a18ab27054 | -17.58649 | -46.66832 | 2026-07-21 04:29:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21c0f23d-e586-332c-ad8f-ddbb984e6d80 | -20.35198 | -46.67461 | 2026-07-21 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eeb37eb6-c077-3167-8dcf-d2843c6a02f4 | -16.13959 | -46.63011 | 2026-07-21 04:29:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 799e0acd-e519-3b60-9e63-3af2e299f0ed | -17.46295 | -47.15526 | 2026-07-21 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14138acb-fcc6-3e00-929e-c7922dc60461 | -17.46407 | -47.1477 | 2026-07-21 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11dc68f2-2c57-3cf5-a872-a57df37a40eb | -17.58076 | -47.49968 | 2026-07-21 04:29:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6acad836-9d73-34fe-aecd-11e9e44931da | -17.46012 | -47.15095 | 2026-07-21 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5901220f-1f81-300a-b4da-5eb716c9c2b8 | -18.55558 | -56.82372 | 2026-07-21 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.8 |
| 61af5c37-8b6f-3746-935f-a90ce2c75f85 | -17.58357 | -47.50395 | 2026-07-21 04:29:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a8a222f6-950a-3861-b45e-920e78a8ca0a | -20.37327 | -46.60012 | 2026-07-21 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e335cca-8258-340a-b6bb-0afa74acab7e | -20.37741 | -46.59644 | 2026-07-21 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2406a5d6-b8b9-3da5-ac4f-6bc44cb620a7 | -19.6084 | -47.64194 | 2026-07-21 04:29:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d79c2e1-df8d-3779-8e91-a6489f41309d | -20.7008 | -50.53046 | 2026-07-21 04:29:00 | NOAA-21 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f36fea20-3243-32b1-8679-41b94da8c411 | -18.55091 | -56.8227 | 2026-07-21 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.8 |
| f3175289-decc-31ef-91cf-8bdaa954acea | -18.54977 | -56.81361 | 2026-07-21 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.7 |
| 0da5a00c-1f02-3e8e-a41a-ae4644ba75c0 | -16.80927 | -54.59151 | 2026-07-21 04:29:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 137929c9-5672-3422-8a32-af41d2c1a848 | -20.37797 | -46.59248 | 2026-07-21 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a33bb9e9-aa75-3884-af87-7bc921f2f588 | -17.58412 | -47.50021 | 2026-07-21 04:29:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f0489f2-0202-33a1-92e8-07ef090b6c01 | -20.40291 | -46.49237 | 2026-07-21 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6ea1995-c451-37f1-bca6-586efcbe08d8 | -17.65483 | -48.20429 | 2026-07-21 04:29:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36867df1-5980-3522-bc66-9f8bc2660e99 | -16.92348 | -48.60436 | 2026-07-21 04:29:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 38417ad0-497a-384f-ad53-83cf9471e767 | -20.36556 | -46.60351 | 2026-07-21 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc8bc497-41f8-3887-a781-d953f7d12b9d | -20.3697 | -46.5998 | 2026-07-21 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fffef608-afdf-3278-99ff-10cdcc1d988f | -17.50834 | -47.84723 | 2026-07-21 04:29:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9917c59-36a2-350a-bb88-e567aa031e65 | -20.35788 | -46.60674 | 2026-07-21 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 214973e9-49d5-3a19-bf0d-4df001e81083 | -20.37684 | -46.6005 | 2026-07-21 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4c4f62a3-5a23-3f7c-888a-008162cd487b | -20.36144 | -46.60714 | 2026-07-21 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74412f24-7886-3a78-870e-95bc2255c096 | -18.54989 | -56.82793 | 2026-07-21 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| e103bc9f-779f-3298-9bd7-5473cd733374 | -17.53457 | -46.42228 | 2026-07-21 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79c2f6d1-cb66-349f-896b-31ac8f854b18 | -17.58918 | -47.51245 | 2026-07-21 04:29:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 22cf2344-9bbd-3613-bd97-388f3af6f1da | -17.86588 | -50.51793 | 2026-07-21 04:29:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b6f220a4-2ac3-34c9-bbd6-5f8decb609d8 | -19.61007 | -47.63039 | 2026-07-21 04:29:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d296a26-bc15-395f-a8b3-a3bb4cc31724 | -20.38098 | -46.59683 | 2026-07-21 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 13ccfe06-52ec-364a-9cb4-010f68bb159c | -19.18318 | -47.36269 | 2026-07-21 04:29:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 1923f794-023f-376f-a977-486ebb97da8c | -20.3851 | -46.59327 | 2026-07-21 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79c61d7b-8d5b-324d-a106-349ea284497f | -20.65845 | -42.20499 | 2026-07-21 04:29:00 | NOAA-21 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8d522b83-65ef-3ecc-b11b-6db39e5173f7 | -17.46351 | -47.15148 | 2026-07-21 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b2b4fa0-955f-35d2-8a94-fe64f17f65b2 | -19.18658 | -47.36324 | 2026-07-21 04:29:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 18.0 |
| de190eb0-6512-3070-a086-b819f9121379 | -20.07662 | -50.41158 | 2026-07-21 04:29:00 | NOAA-21 | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 531690c7-e6a5-366e-94aa-c49dd0d472b0 | -20.36501 | -46.60744 | 2026-07-21 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ebe6abb-aa60-3f7f-acc6-250ee7041cbc | -19.61179 | -47.64249 | 2026-07-21 04:29:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 820d82f7-36f1-3d06-a477-cd3beb244c5b | -20.07995 | -50.41217 | 2026-07-21 04:29:00 | NOAA-21 | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d5a65ff4-d4f9-338d-9c42-c1b58d46d75b | -20.51663 | -48.86275 | 2026-07-21 04:29:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 61b776ba-132b-3044-b98f-e2306d914e5d | -20.32965 | -50.34215 | 2026-07-21 04:29:00 | NOAA-21 | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9cb2e56c-2203-3cb2-a7cc-6206631c9ecc | -18.54403 | -56.81781 | 2026-07-21 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.7 |
| 4f9b0331-0396-3ca3-903a-de5c84bd1502 | -13.3023 | -45.1511 | 2026-07-21 04:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 98713753-266e-3096-a660-7609d06938c6 | -13.3221 | -45.1246 | 2026-07-21 04:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 16e8d7e7-f7cc-3e30-b3bc-a57263d2addd | -13.3032 | -45.1045 | 2026-07-21 04:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| c0e0853e-bbf9-3d61-80fd-fe598c3ae930 | -18.5675 | -56.8109 | 2026-07-21 04:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.9 |
| 2e1f0fe5-5bd4-3177-a1fa-fb53144a7e03 | -18.5476 | -56.8135 | 2026-07-21 04:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 150.9 |
| 6d7dff14-0caf-38a2-80f5-f0051c989430 | -13.3028 | -45.1278 | 2026-07-21 04:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 261.6 |
| 6999daf4-b695-3466-bcd1-9ab8e6a6ec39 | -18.5472 | -56.8343 | 2026-07-21 04:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.1 |
| d5f9c844-8354-3365-b4c9-b33fca40cbc3 | -23.78322 | -49.03819 | 2026-07-21 04:32:00 | NOAA-21 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25093f7c-ca5f-398a-8736-e253a8f675fd | -23.14048 | -48.67352 | 2026-07-21 04:32:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4d253956-5b89-3749-bb9b-f316323d5121 | -23.29143 | -46.16114 | 2026-07-21 04:32:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 19725a7e-a43d-3c24-b1fe-948e81a14488 | -20.89038 | -57.48831 | 2026-07-21 04:32:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 3204b8c8-2c20-3ebb-a11f-d694484043d0 | -22.80086 | -49.34593 | 2026-07-21 04:32:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4c3789e-c634-3e65-94ad-bc7676e3982e | -23.19948 | -49.15252 | 2026-07-21 04:32:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2100cbca-fda6-3129-a91e-ea40bddda285 | -22.37983 | -49.78758 | 2026-07-21 04:32:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ad89dea7-05d7-3fba-9796-9892c399af37 | -20.47994 | -54.981 | 2026-07-21 04:32:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4224b9f-5f99-3a09-9116-5f1afbf20603 | -20.47924 | -54.98472 | 2026-07-21 04:32:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddf5d232-cd68-38a6-bbb6-261c0455fb6f | -22.23536 | -42.54225 | 2026-07-21 04:32:00 | NOAA-21 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 08764cc8-fb75-3b79-a8c6-b52338b01f87 | -20.62255 | -55.6983 | 2026-07-21 04:32:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16ebc024-fa3e-36f9-895c-2b5794ec483d | -22.7981 | -49.34158 | 2026-07-21 04:32:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3de2044a-08cb-3d02-aa09-f8e759be71dc | -23.51619 | -48.56584 | 2026-07-21 04:32:00 | NOAA-21 | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 921b1f4a-3c1b-388e-bbda-ed54d7cd6e5d | -22.73558 | -46.81657 | 2026-07-21 04:32:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 20e624ff-bb21-3fef-ad70-250be38f3b04 | -20.87531 | -57.49041 | 2026-07-21 04:32:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 5013dd88-edc7-3c73-bc5a-f1d8a5e2cbc5 | -22.38041 | -49.78386 | 2026-07-21 04:32:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 68493626-a9bd-3950-8d8f-c9929ed6d29b | -23.56514 | -47.52333 | 2026-07-21 04:32:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| f7a1861d-812d-3bb5-b03b-689c274cf892 | -23.82263 | -48.72076 | 2026-07-21 04:32:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a2924aa-f96d-33cd-8ad3-6c4db267c63d | -23.29205 | -46.15629 | 2026-07-21 04:32:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f00b424b-6afd-35d9-93a6-6b22fa6cb89f | -22.90119 | -43.42048 | 2026-07-21 04:32:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 30f9d635-7dee-36f9-a518-4ec70383ab80 | -23.29517 | -46.16171 | 2026-07-21 04:32:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| ee1ffcc3-2c63-30a3-bee6-6018270ce2cd | -22.80029 | -49.34969 | 2026-07-21 04:32:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2220d53-95ac-3de9-9787-ea3ed078a583 | -22.37459 | -49.04132 | 2026-07-21 04:32:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2d94d20e-e153-3b08-a529-ce9ffca0e243 | -25.03539 | -50.72565 | 2026-07-21 04:32:00 | NOAA-21 | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3083b315-afda-375f-8b57-2090541f38e4 | -22.91556 | -43.48954 | 2026-07-21 04:32:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| aea2813b-3166-3ec9-b634-bedbd9d41596 | -23.56221 | -47.5185 | 2026-07-21 04:32:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 84ccd782-0f79-3dd6-947c-c7c6a337b792 | -23.78265 | -49.04205 | 2026-07-21 04:32:00 | NOAA-21 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README10.md)
