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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89b70c1d-dbb9-3107-850d-34c31202479d | -9.9081 | -36.0224 | 2025-02-20 00:04:00 | METOP-B | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ea070c3a-cd54-3f8b-968e-73d0434c5d82 | -20.2276 | -46.505901 | 2025-02-20 00:04:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9f521f21-fced-3272-99a7-f6f92ad3eca7 | -20.2414 | -46.524799 | 2025-02-20 00:04:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8e1eaee8-8421-34f9-8b43-321a7e5eee7b | -20.215799 | -46.497398 | 2025-02-20 00:04:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a736e7b8-dd6a-3dd9-a2f1-4a6b7d4d1406 | -15.8669 | -41.8466 | 2025-02-20 00:04:00 | METOP-B | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b0a5775d-4bf1-3f92-8174-7d2cf5f20012 | -14.4386 | -45.6409 | 2025-02-20 00:04:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 96e39e7c-f836-3f86-a2a1-1147437f1612 | -6.2153 | -48.050201 | 2025-02-20 00:04:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d5f67043-f6e5-365c-a925-9fb27178b431 | -20.2138 | -46.487 | 2025-02-20 00:04:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d58972aa-952b-36e2-a004-86809915c5c0 | -14.4271 | -45.635101 | 2025-02-20 00:04:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a6e54f03-aa4c-3294-839c-b3468ad9964c | -20.227501 | -46.451698 | 2025-02-20 00:04:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 77f6b84e-579a-35ae-9eaa-0e2a8cac343d | -14.4255 | -45.627201 | 2025-02-20 00:04:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 288320ca-bea2-3c69-a8f4-7d2efa5806d0 | -12.3526 | -41.410099 | 2025-02-20 00:04:00 | METOP-B | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a874ad07-80d4-3b58-a458-5ef0f8d4abcc | -14.4305 | -45.6511 | 2025-02-20 00:04:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7f2b9d73-5c5a-3cdb-b860-0de114c5b9fb | -14.4288 | -45.643101 | 2025-02-20 00:04:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2de3631c-d774-36dc-b48b-ab1a1ffe7d3e | -14.442 | -45.656898 | 2025-02-20 00:04:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 47020eb3-b423-34db-9902-01c547c3e7b8 | -15.8685 | -41.853802 | 2025-02-20 00:04:00 | METOP-B | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 81099e6d-26bb-356f-b334-0ad4f121bd75 | -10.6534 | -44.477798 | 2025-02-20 00:04:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8d82be53-ff64-3646-82ca-303fab5ba1f1 | -17.461399 | -46.989399 | 2025-02-20 00:04:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 414422d6-252e-3807-87e8-6c5a53a9a714 | -12.805 | -45.005299 | 2025-02-20 00:04:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 974f70ed-e162-3745-b72e-2e19acb9700f | -20.2372 | -46.449699 | 2025-02-20 00:04:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f8144126-b2d1-3fac-bdb2-93fb7fb26896 | -12.7935 | -45.000099 | 2025-02-20 00:04:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9957dfa6-ab21-3d62-bb21-a535dd7c7ea0 | -14.4436 | -45.664799 | 2025-02-20 00:04:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 30080565-bf92-3cce-b13d-9b4802eeeb09 | -10.5474 | -45.211399 | 2025-02-20 00:04:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 73ee4adc-ec95-30b7-b40b-0005e82814dc | -11.1126 | -45.115799 | 2025-02-20 00:04:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a9a7186b-8bbf-3f8f-9bbe-4572f2dcc713 | -22.919399 | -43.7174 | 2025-02-20 00:04:00 | METOP-B | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e2eb008f-aece-3d0c-ad36-6a696112ce1f | -10.655 | -44.484798 | 2025-02-20 00:04:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d5d32ccd-042a-3493-9778-9f434a6b3857 | -14.4157 | -45.629299 | 2025-02-20 00:04:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5061821d-23c4-33a6-9bf9-343cceb47e46 | -20.2327 | -41.601799 | 2025-02-20 00:04:00 | METOP-B | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f7aef280-13e8-33e4-9fd6-12a54f632da2 | -6.2171 | -48.058498 | 2025-02-20 00:04:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 73d9c5c9-359c-30d4-a96b-3591ec439400 | -20.243401 | -46.535301 | 2025-02-20 00:04:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fc1597e8-71ac-36b2-ba69-1f5ccf363f2c | -16.0387 | -43.372398 | 2025-02-20 00:04:00 | METOP-B | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a8308f16-df7f-30c8-8b8b-e2600d88f528 | -20.229601 | -46.516399 | 2025-02-20 00:04:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4d1d92f9-ba6b-364b-8771-086432855bcb | -8.1252 | -43.1306 | 2025-02-20 00:04:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 674460d3-f62b-3e5b-aaf2-7a902165de93 | -8.1268 | -43.137798 | 2025-02-20 00:04:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| aabb313c-2394-3243-a595-ec1aeee1b216 | -20.239201 | -46.460098 | 2025-02-20 00:04:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| db3d6507-c833-394c-aee2-bbab27e02655 | -12.8066 | -45.0126 | 2025-02-20 00:04:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 03fd4c46-0691-3c0c-b3a0-c13b30d0fc93 | -11.111 | -45.108601 | 2025-02-20 00:04:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ac409999-b088-3aa6-a021-e0ba63980148 | -17.4634 | -46.9995 | 2025-02-20 00:04:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dd011554-cab5-319e-9ffa-99891f89ca1a | -19.9723 | -40.424999 | 2025-02-20 00:04:00 | METOP-B | FUNDÃO | ESPÍRITO SANTO | Brasil | 3202207 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ec4e45c7-a1f5-32ca-b52e-8464020c9fe1 | -14.4534 | -45.662701 | 2025-02-20 00:04:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9184d7fd-ea93-364f-baa7-a9a5d1ee1e78 | -20.6479 | -43.917 | 2025-02-20 00:04:00 | METOP-B | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c7f7c5b9-e622-3811-93a4-8f116f4b99e5 | -11.9251 | -43.113201 | 2025-02-20 00:04:00 | METOP-B | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3deba78d-16e2-3d2f-b650-cd078c62c3d8 | -10.7623 | -44.9249 | 2025-02-20 00:04:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 83f446f0-f58f-369b-b9be-db761f500af8 | -11.9682 | -44.655201 | 2025-02-20 00:04:00 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 183503a9-00f3-3206-9d66-0191ed6ae66a | -20.2295 | -46.462101 | 2025-02-20 00:04:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| df56e2cd-d5ee-3c08-9c99-44b37ef8a273 | -16.0403 | -43.379601 | 2025-02-20 00:04:00 | METOP-B | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ed7caa40-578e-3fd1-a313-b99c99dbf200 | -11.863 | -46.937099 | 2025-02-20 00:04:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d0842b29-c26a-3ac4-a023-817b8df495ed | -16.0418 | -43.386799 | 2025-02-20 00:04:00 | METOP-B | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fc5c29f6-8671-3bd0-9248-d309dbc807c2 | -20.2178 | -46.5079 | 2025-02-20 00:04:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1b6156c8-9468-3b77-927a-57fdc92b99db | -21.2012 | -48.745201 | 2025-02-20 00:04:00 | METOP-B | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6687c63a-b17c-3f8b-80f5-70c345594e2d | -11.0366 | -45.050098 | 2025-02-20 00:04:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9fdec6a8-ee2f-3be4-9598-423038990a9c | -20.2316 | -46.526901 | 2025-02-20 00:04:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c36da142-ab93-357c-876b-8c903010b78a | -12.8034 | -44.997898 | 2025-02-20 00:04:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7e25670c-ed48-3e2f-a96c-818b7a5755ff | -20.23706 | -41.60958 | 2025-02-20 00:09:00 | TERRA_M-M | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 0732f8cb-0594-38ea-b882-5670d848b42b | -20.22772 | -46.48027 | 2025-02-20 00:09:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 8c0d31c6-1dbd-3e73-9662-8adcf3ce64ab | -16.04066 | -43.3827 | 2025-02-20 00:09:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 2722929b-9e71-39bc-aba1-88c615926a90 | -12.35495 | -41.41542 | 2025-02-20 00:09:00 | TERRA_M-M | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| e7f402fd-e393-3904-92c2-dd23cfdb24f2 | -15.86567 | -41.85945 | 2025-02-20 00:09:00 | TERRA_M-M | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 1c511ea0-c2a3-35ee-943b-0d906eb6d456 | -20.22429 | -46.5246 | 2025-02-20 00:09:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 8e4c2284-e114-3c9c-a10b-4b907bd7156f | -16.03673 | -43.38964 | 2025-02-20 00:09:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 9d5b8ffa-2ea0-3fd5-8d76-5a4ef0b26bb4 | -12.79948 | -45.02627 | 2025-02-20 00:09:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 307f5b79-b420-3870-9d41-c1560933fd00 | -20.23745 | -46.48515 | 2025-02-20 00:09:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 53484597-6f78-33bc-9083-a5769b6807a4 | -12.797 | -45.0044 | 2025-02-20 00:09:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 94814a5a-c19d-3b18-bc10-eb4cf44608ae | -7.40247 | -35.26185 | 2025-02-20 00:11:00 | TERRA_M-M | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 900aefa3-3c3d-398e-91cc-fd88197751ec | -9.56186 | -38.28894 | 2025-02-20 00:11:00 | TERRA_M-M | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6643c60e-f53d-30ac-b9e6-bc281e9d359b | -10.74755 | -37.03465 | 2025-02-20 00:11:00 | TERRA_M-M | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| dec8b83b-0762-338a-8d9f-490d04d58590 | -9.22278 | -40.51252 | 2025-02-20 00:11:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 65925316-af20-36bd-a409-67f25d18b16c | -10.58318 | -38.68019 | 2025-02-20 00:11:00 | TERRA_M-M | BANZAÊ | BAHIA | Brasil | 2902658 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f6c8a05a-dcb5-3988-a77f-ddff9f8a176d | -10.65051 | -44.48756 | 2025-02-20 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 51170a18-f702-36a9-850f-9bfe37065f81 | -9.22407 | -40.52205 | 2025-02-20 00:11:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 659501e3-f14b-3871-9d95-8080558d9a08 | -17.8586 | -40.1002 | 2025-02-20 00:20:00 | GOES-16 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 98.7 |
| 84ad068a-2179-3e47-91de-cdf297d74ef8 | -17.4741 | -47.012001 | 2025-02-20 01:01:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 901f0347-d5a9-30b7-9f1c-b7f02f707a39 | -20.2362 | -46.521999 | 2025-02-20 01:01:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 39b37928-a1b8-3b2d-ba8e-98e8ef3a0822 | -20.2442 | -46.469799 | 2025-02-20 01:01:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f9cd800c-1c87-3650-8819-9cd5e9f8ae31 | -12.8081 | -45.015499 | 2025-02-20 01:01:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 91ea2603-e853-3eb0-8a2b-da83ea84b565 | -20.248199 | -46.528801 | 2025-02-20 01:01:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bb203e54-bca8-367d-9958-a621e30cf952 | -14.4396 | -45.649101 | 2025-02-20 01:01:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0bad008a-4729-3b10-b525-f3d064c9497f | -12.8043 | -45.000801 | 2025-02-20 01:01:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 53409e9f-5d9b-3ace-a8ce-b2f0c7e84d7b | -20.241899 | -46.4604 | 2025-02-20 01:01:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 43ba9c69-038b-3ac8-a4c9-7274990335d9 | -20.2339 | -46.512699 | 2025-02-20 01:01:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2e08c9f4-daf2-3a85-8c36-c7f27d29c61d | -17.471701 | -47.002499 | 2025-02-20 01:01:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 35b8e9c0-f525-3db7-8c63-06bcfcda8908 | -14.4267 | -45.639198 | 2025-02-20 01:01:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b3fd2c44-5302-304c-810e-ecc943f295b1 | -20.239599 | -46.451 | 2025-02-20 01:01:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dc07a664-6730-3d27-88ab-35b6a6c7a907 | -16.048201 | -43.378399 | 2025-02-20 01:01:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 721e901c-a995-3ed0-b17b-21557bc39632 | -20.224199 | -46.5154 | 2025-02-20 01:01:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bd0b99af-cd80-3a92-a5c6-38a4e24766c9 | -11.94806 | -63.95591 | 2025-02-20 01:49:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 226f57f9-a54f-35b6-b20b-86ec79c9b5fe | -11.9468 | -63.94668 | 2025-02-20 01:49:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| cc4ad535-5687-3792-acf2-8d8b7dbdd9d3 | 3.04597 | -60.08895 | 2025-02-20 01:53:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 38.6 |
| c06086d4-18fb-3781-b81d-916dac0d84b8 | -20.2363 | -46.4447 | 2025-02-20 02:00:00 | GOES-16 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 1c5d2ee1-bb05-3141-b650-66a669892bf1 | -6.33271 | -35.08077 | 2025-02-20 02:47:00 | NPP-375D | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 1f985ac3-1bb5-38e8-9f5f-28ec473ba25e | -6.3331 | -35.08811 | 2025-02-20 02:47:00 | NPP-375D | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| f78e9667-69a5-39e1-82dd-888e0d62ad8f | -6.76815 | -35.17944 | 2025-02-20 02:47:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| e52adcda-156e-3fb5-a95f-94196c752e30 | -6.32589 | -35.08673 | 2025-02-20 02:47:00 | NPP-375D | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 334722d6-03b2-38f6-b25f-8ea4102a8c72 | -6.33445 | -35.08108 | 2025-02-20 02:47:00 | NPP-375D | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 3afc9c80-c473-3ffa-8e87-a52b154ed35e | -6.33137 | -35.08796 | 2025-02-20 02:47:00 | NPP-375D | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 5807996b-2493-3ade-9461-5f090bd8c4eb | -6.77529 | -35.18117 | 2025-02-20 02:47:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 4c393cc5-5ccf-3302-a28f-875605038319 | -6.77713 | -35.18119 | 2025-02-20 02:47:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e857676e-dd56-397b-940e-a26ae71ffd81 | -6.76997 | -35.1796 | 2025-02-20 02:47:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| fe9a7417-01fa-3fdb-8dd9-c08ec9d14291 | -10.75787 | -37.0521 | 2025-02-20 03:10:00 | NOAA-20 | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a91335c9-c0c0-3f16-a2fc-47f63db7e1fc | -18.58243 | -39.84118 | 2025-02-20 03:12:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |


[Clique aqui para ver as próximas entradas](README2.md)
