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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9514e2c8-8642-3f27-ab3f-07c9d1b5f9a0 | -12.38387 | -51.10277 | 2025-10-06 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f819b87b-4166-37b0-91bb-e29ea2d80f3a | -16.0093 | -50.94491 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8171d685-6464-3708-840e-a52ec346d446 | -15.63107 | -52.53567 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a2464779-dd55-3ddb-9c3a-5af2d62cf0a1 | -11.18035 | -47.73196 | 2025-10-06 04:27:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b29b33e-86e2-3dfe-9eff-019d8e2f4772 | -10.32798 | -50.27473 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d660b5ea-2c3d-375a-a28b-e1c3969efae0 | -12.9012 | -47.29948 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee736724-2045-3f72-a361-48bbed4f34ad | -13.35719 | -47.25315 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00bb29bd-e47a-3f0f-bd57-320fbf393f94 | -13.72106 | -48.08705 | 2025-10-06 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f704e14-e2e8-30f3-a124-786d990fed44 | -14.33756 | -47.71013 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f286dde-32a3-3074-8e3d-917a57f24396 | -13.64769 | -47.2886 | 2025-10-06 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e978f3e2-2ab0-32c8-9154-5e39fb4989ed | -11.94218 | -46.43748 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c3105a59-8535-3a02-8cdc-8ffbba60e37f | -8.61381 | -54.97375 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7abcae0a-13a1-391d-8c0f-c2112e971a9a | -11.81684 | -45.10201 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| eaf1a292-18f1-37b0-addb-e2484fce67f7 | -9.79333 | -48.27634 | 2025-10-06 04:27:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8977dd1-395d-37be-8c82-0b232d88875f | -15.56049 | -46.83976 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79377968-a441-35aa-ab66-3557caf611d3 | -14.63308 | -52.51543 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 984dde75-f3d5-3907-9ef1-c71a878dc080 | -14.34637 | -47.71882 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d75f481-5a53-3879-a9f8-8219d48b9878 | -8.62879 | -54.63002 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fd78090f-a863-34a2-a55e-d029980637b8 | -12.89735 | -47.30248 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a886ede-ad84-3f88-9351-4af1e8c61a66 | -15.44116 | -45.87035 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b22e2401-f5d4-32ce-93f3-20dad4a0416d | -13.50162 | -47.24351 | 2025-10-06 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2592a91-739a-3e75-86e3-052de93279a0 | -17.08045 | -43.38861 | 2025-10-06 04:27:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bfd1bd79-09ae-34c5-9184-9cec956a3db6 | -9.91204 | -50.2432 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 346f4972-0a65-3612-ba43-f560e1c692bb | -12.90759 | -46.81681 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d215e74f-e165-38fa-80a8-54b5e4d4c553 | -14.95173 | -49.9852 | 2025-10-06 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdb53c53-25e3-343a-9d8b-447d7bcbbf62 | -11.52075 | -47.68724 | 2025-10-06 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8568ce96-8009-3404-956b-326209d83976 | -13.06264 | -47.89949 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 202b79cf-9ae6-3e1d-b628-0140ea06daaf | -15.50264 | -46.84668 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf3fef26-8a42-3a9a-af75-55bf12917e94 | -12.91225 | -54.74446 | 2025-10-06 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce1fcb00-f1c3-3b76-89c2-915e505de4ac | -16.10396 | -43.62719 | 2025-10-06 04:27:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3812210b-3053-3638-8ca0-556e07774ee8 | -9.33232 | -54.52556 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 170167c2-4e14-333f-a12e-84caa93f4333 | -15.73367 | -46.25832 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cee3b2f-54d5-34c3-8e39-9bd56146ee17 | -13.27169 | -47.63036 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7b5c37e3-e56b-30e8-a308-8ff80b5e7791 | -11.70915 | -45.42524 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 195e1612-d01e-3b62-bdff-03bf9493a649 | -12.57614 | -46.73846 | 2025-10-06 04:27:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a899586d-24d6-3de7-84e5-efe8202cc24b | -12.41803 | -51.12207 | 2025-10-06 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47a7cf44-20f7-309a-9bc6-ff48031dadbd | -10.72645 | -46.62756 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2f2202b-6486-34ea-a7d4-dabfb59d7abc | -8.6171 | -54.96407 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9fcd5135-2938-30a6-8294-6cdf4c37db86 | -14.36563 | -47.72569 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b6dae766-7e88-342d-bf49-f7cb43b44843 | -9.96375 | -43.78119 | 2025-10-06 04:27:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 40992942-360c-36a8-ba27-784a2793ca1d | -15.24278 | -46.66868 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c66bc77b-9ddb-3bea-a2aa-44b2225211cd | -10.75769 | -49.69849 | 2025-10-06 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 472fac39-64f3-3204-bb84-9bb3df3cacfc | -10.76116 | -49.69907 | 2025-10-06 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 89bdaec5-1a90-3f8f-9664-b44f7f0a189c | -11.02592 | -46.53778 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5e00e523-1512-3f04-9c66-5867cfdf9d2a | -16.293 | -45.24009 | 2025-10-06 04:27:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 485454d3-3b7e-3e69-a068-84fe69c29749 | -13.27275 | -47.57999 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d48f3661-32ca-351b-a7c0-a244c11eec70 | -11.8709 | -56.88079 | 2025-10-06 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75eb090b-5cb7-3fd1-abbc-49c56ef440f5 | -14.34692 | -47.71529 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4e68076b-a6bf-322c-ac78-990085eeb6cb | -10.53909 | -53.72928 | 2025-10-06 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 852df3e2-63fe-3da6-95ed-7e0b3fc24d25 | -10.8515 | -47.98036 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53eb0edb-4eb2-398d-8491-6205bfcdca4c | -13.35254 | -48.04814 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4cf9022a-e60f-3d2f-b02d-590fb5b1033f | -13.33877 | -47.5731 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87fcdb61-4b3b-3b83-8b51-3aee76f1ea30 | -10.2883 | -50.2778 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f5495ba-e701-34f5-915d-c0e9eb54795f | -13.68299 | -47.32381 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b97b9a8-f23c-3298-8490-040a5c04d681 | -12.69516 | -45.83991 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63f101f3-ed1d-3168-b21c-989bb29b0480 | -13.10792 | -47.9176 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80c9da62-6a0a-369c-b0fd-f53f7aea4b9d | -14.84286 | -54.78877 | 2025-10-06 04:27:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba18cb4c-e801-3814-b696-55a9c4bfd3ff | -14.54 | -46.96258 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8dbedefa-c60b-38a6-bd5a-a59245807ab3 | -14.93509 | -46.8229 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00400069-25d0-313d-9641-42fdae325ac0 | -15.52201 | -47.34622 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 336e19ea-e691-389f-b140-e46138035e3e | -9.24269 | -51.82769 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bc650ad9-a261-3dd5-ae2a-35b6277011c1 | -10.68359 | -44.15117 | 2025-10-06 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fb6236d-658a-37a4-90f1-ae386ae1d8e8 | -15.57152 | -47.28659 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73f27a3d-2f20-37a9-a548-dd5fb02f65f5 | -13.31293 | -48.06334 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63c2ae17-f66e-3b23-bf50-d60205073c2d | -12.61254 | -48.12518 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3939efad-60ba-3d89-be87-38833f830df3 | -14.69803 | -48.36454 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 309d3d64-462b-3f40-897c-1e0a2ffe25a4 | -13.23273 | -47.81535 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 406dd4c9-932f-38be-9fcc-ff42bc4b7066 | -15.59855 | -52.54424 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4512b302-ee6f-35df-b4fa-34202051c16a | -15.77666 | -46.25331 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c5980ea-13c0-3244-b29d-4825b3b24d06 | -15.29807 | -47.32111 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8d780e2-cab0-30d1-8da8-ae47b8981adf | -11.70627 | -45.42099 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e840c3ee-0d43-3a70-9794-a7cf5b4b034b | -11.80462 | -47.9166 | 2025-10-06 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3791b967-a1f7-3e70-9855-49114b0fd15a | -11.64761 | -47.0262 | 2025-10-06 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29c8733c-96c5-3e40-93e2-14beb225a53b | -12.26334 | -49.19884 | 2025-10-06 04:27:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f2e8c97-f880-33be-9332-87cb47bcd145 | -9.68558 | -48.20424 | 2025-10-06 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a314bc52-abd9-31cd-97c0-1dbde541c0dd | -15.36496 | -47.99432 | 2025-10-06 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38bbb922-c29c-31e5-bfe0-215338572633 | -13.08485 | -47.82738 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a42d85df-c39f-3330-a170-2f4ebb21529d | -11.64815 | -47.02268 | 2025-10-06 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9639933-4104-39c9-9517-8454060b0126 | -11.51314 | -54.45389 | 2025-10-06 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d06fb7b-dca5-3c76-b4a7-5aec5c11f1e9 | -11.81393 | -45.04939 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e12149ba-0fc0-31cc-ade1-d12e16c9de73 | -13.30193 | -48.06878 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7a76cb85-ff52-32e9-848a-4272c2acb998 | -10.45555 | -51.24792 | 2025-10-06 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 466f2bda-d8c4-3c2c-95ab-a4586df1943a | -13.35969 | -48.0457 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 906abc7f-2670-32fd-afec-f9cb475a74ea | -15.9748 | -50.85392 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c6b13ad5-8ac7-3554-8c86-84dc4431f233 | -12.70643 | -48.56113 | 2025-10-06 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c239ff41-72fe-3946-9ee1-a3f137f8e4cb | -14.66887 | -48.37789 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f4c92a8-99e1-386b-887e-7dc479769307 | -11.90751 | -46.2216 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a778be4-13fa-338e-9764-15ab152e13df | -13.3096 | -47.56063 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 59d88d3a-0eff-3a54-a5ed-55c49b5dc0ad | -11.87025 | -56.88418 | 2025-10-06 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 983d7c7d-c3bf-3413-9152-8989d5329ec9 | -10.81493 | -48.82828 | 2025-10-06 04:27:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5827fd8a-9a55-3817-8ecf-d06f4cc02b5a | -11.13189 | -47.76012 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7faebcb7-8b9a-3ad4-8b9e-e8187b90d4b9 | -15.74054 | -46.25952 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7880728-6e95-3ded-8b36-e1f1a304290e | -13.24427 | -47.80641 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75ae9533-b62a-39f5-8aa9-7f61345f007e | -11.8682 | -56.8663 | 2025-10-06 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1dac4a07-f669-3f3c-b5fb-10f231f67695 | -15.748 | -46.25658 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9baace8d-6ece-3b2d-add9-5e22033932f7 | -14.63925 | -48.32945 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a5ab763-8b89-358d-a3da-19b6b8e8b68b | -12.89844 | -47.29543 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 122a3678-20bc-3339-a9b1-c24500c4dfbc | -15.00653 | -56.05026 | 2025-10-06 04:27:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2126d8a-339e-3895-b8ce-57a649a841fb | -11.57193 | -47.88205 | 2025-10-06 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bc91a33-e2cb-3594-9d23-1f1429da443a | -15.99684 | -50.84971 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README52.md)
