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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| daa53de3-fa21-3f56-ad69-456140364612 | -17.86354 | -47.14265 | 2025-10-01 04:53:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90a5328a-a230-3765-9c2f-6a5a4c5d0ad3 | -15.29692 | -56.78292 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1dc3e595-6aca-3e13-84f3-15cdef800d82 | -15.2538 | -56.77919 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c69de69-51d3-355f-8c16-1a06e6ffdf03 | -17.97254 | -45.02861 | 2025-10-01 04:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b667d5bb-68a9-346c-ab00-df9ae32f3540 | -15.85143 | -54.01855 | 2025-10-01 04:53:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d10ac411-a644-3475-867d-bb51b6825f2c | -16.25121 | -50.94306 | 2025-10-01 04:53:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 04ed2189-e5d3-3a00-951a-77eca9a59244 | -20.49709 | -43.94255 | 2025-10-01 04:53:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0eb4a287-6316-39ff-9ad9-0f105dd253f7 | -20.62596 | -46.21481 | 2025-10-01 04:53:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 997aa155-2d27-3372-9e8c-875beef4965a | -22.11488 | -44.69292 | 2025-10-01 04:53:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 05084cd5-4648-3b9d-bc12-6a0781a46ccd | -17.38626 | -47.14864 | 2025-10-01 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8c47a45a-c5d0-38e4-a2be-b71535eac771 | -15.33981 | -56.95733 | 2025-10-01 04:53:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de66e0ae-9469-3de7-945e-8a226093cb91 | -20.0302 | -44.5424 | 2025-10-01 04:53:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 988c427b-47ec-32d5-8105-306dedc3a5b0 | -20.10811 | -44.37407 | 2025-10-01 04:53:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 635953ed-6233-3c81-bd3f-eec1319905d2 | -20.02509 | -44.53863 | 2025-10-01 04:53:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cfe7ae6b-9614-35de-ada0-5ff8a2b048c9 | -18.71238 | -49.16537 | 2025-10-01 04:53:00 | NPP-375D | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d8e460d-fb25-366c-af8e-c1df2d0c3bf6 | -21.3335 | -45.87732 | 2025-10-01 04:53:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fbd55b02-7d93-3f78-9c65-cc083e3ef816 | -18.95939 | -43.70461 | 2025-10-01 04:53:00 | NPP-375D | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f687bf22-1771-3983-9d8c-4af333e78384 | -22.29347 | -47.75241 | 2025-10-01 04:53:00 | NPP-375D | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f9867fec-acfc-3e66-932b-dd17252500cb | -22.24139 | -43.41073 | 2025-10-01 04:53:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| d6e415ea-5923-3e36-8959-f60310f6b035 | -22.58671 | -46.78012 | 2025-10-01 04:53:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 497cc91e-b6b0-38c1-b1fa-822f84a2f03a | -17.51002 | -43.48891 | 2025-10-01 04:53:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6256c007-f795-3c0a-85db-ca1b20f58bc2 | -15.33979 | -56.95501 | 2025-10-01 04:53:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4fb76da6-887d-32c5-944c-932af75dd950 | -22.62376 | -49.05741 | 2025-10-01 04:53:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 01017fa9-d777-3eab-96b5-713e09daf8e7 | -16.19553 | -57.59714 | 2025-10-01 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 3b5d692d-2531-39ff-9f26-bd61e7578789 | -22.11189 | -47.80532 | 2025-10-01 04:53:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6c40163c-0b13-326b-98ec-022010fd1bae | -20.60109 | -45.88669 | 2025-10-01 04:53:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bba4487d-bb12-3d6e-92b6-bb4fbd8a9091 | -15.30647 | -56.79375 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ec333c9-ef73-37de-b351-9f83dea60645 | -19.93496 | -43.89543 | 2025-10-01 04:53:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 84492968-db40-3d47-86de-d47b63271fbc | -15.85084 | -54.02217 | 2025-10-01 04:53:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13316f68-b60c-3523-a9a3-816ed15db79b | -19.9298 | -43.89007 | 2025-10-01 04:53:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 739f93f3-eb48-36c0-aac2-a24581eb39dc | -18.80582 | -47.54832 | 2025-10-01 04:53:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 038c4dfe-5ac9-34fc-a1b9-5db4736ba808 | -19.86272 | -43.81664 | 2025-10-01 04:53:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 9274588c-92aa-36cc-922d-96407deba22c | -21.3347 | -45.87748 | 2025-10-01 04:53:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 74667258-37c3-3f81-8c6b-8cf85170c72a | -23.36125 | -47.16211 | 2025-10-01 04:53:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d0a176e3-8e5d-328a-8c69-811626199141 | -20.60171 | -45.88079 | 2025-10-01 04:53:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f738e613-ea45-3b70-899d-dcc14ee1d11e | -17.38844 | -47.13081 | 2025-10-01 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 36dfbf8b-6cba-3b7d-9f96-e859c5afb208 | -16.25879 | -50.94016 | 2025-10-01 04:53:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 688e32fd-fb4e-3889-89af-463c497372b6 | -22.10883 | -44.69818 | 2025-10-01 04:53:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| befb20b0-09fe-349b-b52a-5e51b7bca661 | -17.95661 | -45.03199 | 2025-10-01 04:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c47c1b9-f4fa-3065-a628-932d6b35e17a | -22.05997 | -43.08029 | 2025-10-01 04:53:00 | NPP-375D | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ca64df3b-a0a4-33da-b588-d40f6cddbca1 | -17.95789 | -45.02039 | 2025-10-01 04:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a58cbee6-e5ab-3a0c-ac29-8fe8d08bd0d2 | -19.85287 | -43.65953 | 2025-10-01 04:53:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 748d8359-c443-33ff-8cc0-f9643518e0a5 | -18.31316 | -46.61298 | 2025-10-01 04:53:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9de15b32-ea53-37fa-bb3a-39f2ce29db3e | -20.49132 | -43.94292 | 2025-10-01 04:53:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 95305da7-29de-3535-8940-e5f56b646fa2 | -20.48816 | -43.94517 | 2025-10-01 04:53:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c2f1cd0d-8784-3fc3-bfbd-8a70611dc904 | -20.21892 | -43.44416 | 2025-10-01 04:53:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ad022930-e393-3568-a1a5-5fb6ef8bfc6e | -16.25471 | -50.94361 | 2025-10-01 04:53:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec3ead50-f4fa-36cc-a1af-4010c87d3edd | -19.92909 | -43.89715 | 2025-10-01 04:53:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a103927d-86e8-35c2-a1b6-a8be7b273ee3 | -15.27196 | -56.7729 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6080121-0e28-3ff1-be9c-389ca9272f8a | -19.85783 | -42.59208 | 2025-10-01 04:53:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 9ffc4fdc-aed7-399c-8efa-c8c29d6df81f | -20.59685 | -45.88484 | 2025-10-01 04:53:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c92552d8-ddae-3114-9d60-744677b7d2c4 | -20.62169 | -46.20853 | 2025-10-01 04:53:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b8112c8c-3082-3a43-8421-7b2b8453a20d | -15.25018 | -56.84473 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cd57d15-e6c3-330f-8a93-2229fd53341a | -20.49756 | -43.93793 | 2025-10-01 04:53:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 83969597-db86-3b76-8004-322b054401f4 | -22.64121 | -46.75483 | 2025-10-01 04:53:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0f9cd588-b293-315b-965e-0701f4cae887 | 2.26165 | -50.72967 | 2025-10-01 05:06:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 46532d60-69da-3fc9-9fe2-240c728b94f6 | -2.55177 | -48.40588 | 2025-10-01 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 778c2f62-c095-350d-bfdd-5a4664c03a06 | -4.73652 | -43.61027 | 2025-10-01 05:08:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9093760e-dd28-3888-8546-d67a976c0428 | -2.248 | -47.88498 | 2025-10-01 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c06cd2c9-b80e-33fe-a0c3-f8e88d020a63 | -2.63323 | -48.04095 | 2025-10-01 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b821f3b-3e8f-329e-a561-d8cd37640178 | -2.26704 | -47.84909 | 2025-10-01 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 47ca55e2-89e7-34b1-90b6-a966d8c100c1 | -5.63528 | -43.93074 | 2025-10-01 05:08:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 7408581c-6d3e-35a1-b513-9e993351e947 | 2.87555 | -60.2642 | 2025-10-01 05:08:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6456b9b1-97d2-34a0-b96c-77225047d2ce | -3.81259 | -47.58664 | 2025-10-01 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ec83205-4676-3c6c-9660-e30945accfe7 | -3.46823 | -50.0883 | 2025-10-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 86b1a2ba-cd0d-3a35-9d77-5177df55275b | -2.69434 | -54.7695 | 2025-10-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 88292e92-31df-3154-bcbd-ea095d4b9aa1 | -5.80088 | -43.74037 | 2025-10-01 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a62124c3-0025-315b-a86f-b699df1d9850 | -5.85924 | -43.40448 | 2025-10-01 05:08:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b5434fb8-ca9a-39da-8650-3da928bf8fd6 | -5.62922 | -43.92368 | 2025-10-01 05:08:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 46.9 |
| d01003a8-fd3f-3187-a3c2-97da3bd62f25 | -3.46755 | -50.09278 | 2025-10-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| d0fe4111-c8bb-3425-9ab2-b5012ec7aacc | -2.59034 | -48.11832 | 2025-10-01 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9455bfcb-15a0-30c6-9114-5420416e8235 | -3.41655 | -51.22989 | 2025-10-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cdec6544-29fc-3974-bce7-fbd5757899f5 | -3.46311 | -50.09203 | 2025-10-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6328b06e-9241-3fd0-8ef1-5ec32c27ce9d | -2.58945 | -48.12421 | 2025-10-01 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c5ad670d-42b3-3ecf-85b6-0fcda1a1175a | -4.25415 | -48.55735 | 2025-10-01 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68e33ad0-ef98-3bfa-8354-a617c6367fdc | -3.4988 | -52.46502 | 2025-10-01 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e6e12ed0-8daf-325b-ba4f-2a07bdd017eb | -1.14383 | -47.24985 | 2025-10-01 05:08:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fcb93fb2-40dc-3557-afd8-f70c88e78abb | -3.09644 | -47.00777 | 2025-10-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 29e74004-e25d-3aba-817c-d6061092c9f0 | -3.77596 | -54.30133 | 2025-10-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 52e33447-e5a8-3f5b-bb18-aaeb70c23375 | -5.85835 | -43.41127 | 2025-10-01 05:08:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0b8674da-0f3a-341a-bb16-64fe5c906997 | -4.74343 | -43.61151 | 2025-10-01 05:08:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63483782-63a5-3f4e-8986-1e636a7baf4a | -4.63288 | -47.02119 | 2025-10-01 05:08:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fc110539-5a7b-3fd7-b99f-64b8542ce3bb | -0.90769 | -47.54877 | 2025-10-01 05:08:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 056937f0-cdae-3d83-8558-f9b87491cf98 | -3.46243 | -50.09651 | 2025-10-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e719efda-b305-3b59-ab35-b06fa9da5102 | -4.63849 | -47.02198 | 2025-10-01 05:08:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c0db6279-4aa4-38ad-94a6-b2d64932ccda | -3.81209 | -47.5901 | 2025-10-01 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 596736fd-6ecd-3fd3-8b4d-1cca56e273e6 | -2.61554 | -50.92218 | 2025-10-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3639f031-793d-3f99-a0e3-6c93a33ebb33 | -2.30504 | -48.1439 | 2025-10-01 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dc765b6d-b847-3fa9-a2c7-b86ae4b23874 | -3.68717 | -49.05161 | 2025-10-01 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0dc72f5-1044-3c32-a0b5-9380db493137 | -0.09734 | -51.2747 | 2025-10-01 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0790eb01-f274-376e-af12-afe70ebb30b9 | -5.80265 | -43.7356 | 2025-10-01 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e9528a10-8adf-397a-82ad-3eb6a63092dc | -4.40282 | -50.84886 | 2025-10-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 144e11a0-362c-34f2-a594-c00b233c87e7 | -2.61612 | -50.91843 | 2025-10-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3499ba49-3f3f-3d66-a1e4-8e1c6cd4c43d | -3.10138 | -47.01221 | 2025-10-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c61fff4-0c6e-3078-9085-b905962a6b21 | -3.10031 | -47.01932 | 2025-10-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 85fe0bce-82d5-3e67-959e-ed6ac9e9bb85 | -6.27839 | -43.65521 | 2025-10-01 05:08:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 425c9108-59b1-399c-aa41-a46162b90120 | -3.08882 | -47.02119 | 2025-10-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9a9f8967-d7b8-3359-a0d3-ee00f2346b98 | -5.20692 | -45.67723 | 2025-10-01 05:08:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e4052f9-b069-3648-a3a0-9f3a8e0db3d6 | -3.45797 | -50.09587 | 2025-10-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d14b2c90-90c4-3258-82b8-cdc7a2791981 | -1.33047 | -47.57778 | 2025-10-01 05:08:00 | NOAA-20 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README119.md)
