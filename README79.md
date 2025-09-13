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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 905fca73-0752-3bc1-8683-4aff17677161 | -15.11998 | -52.46386 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dcdf74e1-c164-3940-9d7a-cf34a242f0a0 | -14.2946 | -46.06903 | 2025-09-13 04:59:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1cdfe765-ee67-3cc2-ba94-f8e66572afe8 | -11.31227 | -50.78793 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c6da2045-6cb9-3f6c-87be-38ac377f0c4a | -9.27249 | -59.40574 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7e417fde-6dab-3ea9-b059-07413681880b | -12.12921 | -44.83027 | 2025-09-13 04:59:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f7c9c83-d51e-3355-b38c-61d0797dc242 | -15.15523 | -50.12272 | 2025-09-13 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3f7da198-c4b3-345b-8f10-289e2ecccc39 | -12.86334 | -62.12722 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba80946f-998f-360a-a00b-3d38f0e319b4 | -15.05899 | -48.00412 | 2025-09-13 04:59:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 586c74ae-5799-3ffc-9158-e089b731c7d8 | -10.20102 | -51.67104 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbd1df51-306a-3a9b-afad-2296627a79b9 | -14.19271 | -46.27337 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b2f4e39-989f-3ac1-9ffa-2b783236374f | -13.4781 | -48.45 | 2025-09-13 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f5bbcb6a-4844-3278-9bf7-c41ff11265c4 | -11.18971 | -51.41237 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 79894fe6-da21-3261-9931-29b781734ec7 | -14.20496 | -46.2647 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f58547a6-3168-36eb-9dc9-994a0cc5ddcb | -11.18152 | -51.41589 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 39eaa8c1-8d88-3f69-99b0-1b32b96b9811 | -14.20942 | -46.27407 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 925ec2bf-afa1-368e-b489-b9f933bf2485 | -15.28353 | -53.77517 | 2025-09-13 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c298d0e-2c42-3a00-baab-90b2e487706a | -16.14347 | -49.9183 | 2025-09-13 04:59:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b3af9c9-704f-3880-a039-66b582dbe4ad | -14.20379 | -46.27439 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dc9e5a98-a9cf-35c1-82f7-f5350172bfb4 | -12.80441 | -47.99435 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| efdd621a-2151-3f37-ab4f-86f56f057df7 | -12.13239 | -47.59274 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56d039ec-ce4e-31f0-82e9-ef0f91e8c88f | -11.0751 | -51.43101 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b12574bf-f969-3988-95b9-2004b33e7bda | -11.17711 | -55.04111 | 2025-09-13 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a224e02c-b82d-3b3f-a593-e9062bbe49e5 | -14.21973 | -46.28201 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 219151aa-6c60-3aa9-bc9b-2ee45d7a59d3 | -10.61699 | -52.31483 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 505bb15b-b238-392e-b47a-697e01181ca0 | -14.43156 | -47.32402 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ecb4727a-a888-3d49-b964-ee4408adae98 | -14.19805 | -46.27576 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2ea95761-0c8e-3635-9454-b0f0b9393e42 | -13.0 | -46.73955 | 2025-09-13 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91a9e377-b0ac-354d-8474-7ef554d30c7b | -14.698 | -45.14853 | 2025-09-13 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61fcb2c9-8c02-3266-b222-10ca519a44a1 | -10.27152 | -57.79613 | 2025-09-13 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5ddeea9-a466-35e5-b246-11a2582cab63 | -10.00643 | -59.97004 | 2025-09-13 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c2cce19-35f9-3d24-8379-dd68f02b06b8 | -11.87396 | -50.57622 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 849ceec0-deb0-3169-a5a3-b6176abbb48e | -14.18105 | -46.27746 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 9c110d7a-2465-3859-b05c-4be1135b71db | -11.03006 | -51.41777 | 2025-09-13 04:59:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8864ddb5-5c3b-3b0a-b2af-7d58981af08b | -15.14333 | -52.48715 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6db59715-3b59-3d23-bfaf-430e48dc6331 | -16.55864 | -49.2178 | 2025-09-13 04:59:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5c5e065b-4fc7-38ae-8dcd-c181b1870827 | -13.00414 | -46.74978 | 2025-09-13 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c691558-26b0-32de-9ac9-c95487e18e8c | -9.48666 | -55.99112 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78204240-7900-34ef-a8d9-c5d2b6aea95f | -11.14393 | -50.70326 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 40f0f5c4-b931-33a5-9ac8-0e75afb65ffe | -11.87845 | -50.57327 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| cbf27d43-9039-35cf-8a29-58ab769925e2 | -9.83503 | -54.52939 | 2025-09-13 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78d22d4d-1774-3327-8991-4b1068386b80 | -9.48999 | -55.99166 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9aa3e48f-252e-303f-b177-04ca42a2e9bd | -14.20419 | -46.27076 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 295dd406-c54e-3086-82e9-191f2ee6db38 | -12.97898 | -54.75272 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f5f27fe-b646-3455-9a2d-3464f59e0456 | -9.49835 | -55.96041 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9d2024bd-cbe5-3316-bf99-3b97c2c5014a | -14.17988 | -46.28746 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ce5a4a8e-5b2d-30eb-9ea9-996bc36a2427 | -10.70232 | -48.64597 | 2025-09-13 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4419637c-6129-3905-a689-1b958f985f09 | -9.62611 | -64.18295 | 2025-09-13 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef806e29-fa2b-3eb9-801d-9c8910de3a65 | -10.45702 | -50.60228 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b5451e04-2f22-319d-a7d0-dafe65d2199d | -11.09325 | -51.43843 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| b3bc4b76-c8e7-3622-9388-fbf9dc03d986 | -12.85901 | -62.12641 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbf363f1-2171-373d-a3f2-97eaefb4113f | -14.20969 | -46.27205 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cde6e118-e8bb-3ed3-8e4b-1a3c37433ca0 | -14.4375 | -47.31806 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 244aa658-b50f-37a8-86c6-e24849285f8b | -15.76308 | -53.49939 | 2025-09-13 04:59:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6847baa9-412a-3081-a19a-2a446a38b2a3 | -15.05539 | -47.99219 | 2025-09-13 04:59:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7f486cda-f18d-3768-b8d5-3d46c9e29e63 | -13.77601 | -46.28682 | 2025-09-13 04:59:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ec76814-1f2e-3824-9c2e-73a885aa583d | -10.78204 | -50.54049 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 10ac1132-ae90-385c-9ec4-1dc2018ef2ba | -10.75111 | -50.50753 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 07da0504-ab71-31f6-94cc-70f267c84d3a | -15.11835 | -52.50251 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 82251333-20d7-3ca0-9d23-ad59f182c2ce | -12.10941 | -47.59921 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ac58a3e2-b75a-3f83-8607-6c2dd74601ef | -10.1005 | -59.1625 | 2025-09-13 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95510d8a-e27a-3c22-9232-9a461bfecb45 | -13.28538 | -51.62852 | 2025-09-13 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16cf6afa-5542-32f5-9fcc-a9f76bdc16bb | -11.41004 | -50.74738 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00ea2350-902e-32e4-b5d1-c40722138b0b | -12.12644 | -44.84093 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e1941694-1343-37e6-9c5d-4ea3d8479344 | -11.87893 | -50.56973 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 411be359-375b-3962-8741-fd31a7805d48 | -16.56334 | -49.21823 | 2025-09-13 04:59:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2f55dbc8-2373-3316-bf12-1719b7a4f262 | -11.9405 | -50.42158 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7839fef2-f04b-3143-81c4-4db34407330c | -15.38296 | -52.10192 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c17aac7a-2171-31c2-bb20-d3ae6b832671 | -9.83451 | -64.22889 | 2025-09-13 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f73d8f60-5ee8-3b40-92ce-a0ebd9391d8d | -10.50892 | -51.52598 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8bcaf552-cad1-3736-ba15-89599fc588b4 | -12.57173 | -45.66836 | 2025-09-13 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e73583e5-8b96-38a6-bf16-64417e0511ef | -14.1989 | -46.2685 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ae32e910-b96a-3472-bbe3-5dbd68c87f87 | -15.05966 | -47.99869 | 2025-09-13 04:59:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ba1db475-763c-3949-b1e5-248d1967e185 | -16.25464 | -50.07166 | 2025-09-13 04:59:00 | NOAA-21 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d388a26c-6aae-3f77-a98a-2f924d45332e | -11.85939 | -50.56326 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c3dcc633-8987-36ca-82bb-a32a3b9d7005 | -14.21677 | -46.25834 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 391c2158-fb7f-3347-a7e5-b71f24bd2c53 | -14.22319 | -46.30101 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| af9835b3-0a59-3cd1-ad43-37457d96c1bf | -11.07886 | -51.43157 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 93589e1b-8a85-354e-9f44-d9e5c8f2bf25 | -15.77088 | -55.388 | 2025-09-13 04:59:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3680799a-7001-368e-9e47-932dfe234a15 | -15.69184 | -50.57564 | 2025-09-13 04:59:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dea37626-7b77-30bd-a811-97ba8c136d65 | -9.49723 | -55.96747 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 026dff5b-f394-3256-8203-d31d03965047 | -13.25787 | -57.33077 | 2025-09-13 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c5df32d-9e6f-3a82-9de3-e8c11c7b8198 | -14.45008 | -47.34502 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb2aac47-750d-37ee-8062-f7ac725bb376 | -11.42156 | -45.61593 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| cb35c64c-9853-3c28-af2d-b27845ea5745 | -14.21353 | -46.28686 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 82c3a2fa-f2fb-33f3-91d3-70f380bd3fbd | -14.19864 | -46.27038 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 72011cd1-f609-3bcd-b96f-298fb0df5291 | -14.17395 | -46.24206 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3c28ec2e-a5a8-3242-966a-974b78e2aadc | -11.88695 | -50.57089 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c70e6e1c-bbb7-3c3e-af51-8786117e5d8f | -13.17583 | -47.27435 | 2025-09-13 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 595139ea-6bb4-3604-b426-e5e583b0a209 | -10.75581 | -50.50296 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1fc46aa3-8c58-3d64-b83d-1f8360f69a7a | -15.77194 | -53.48812 | 2025-09-13 04:59:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be78d607-0df5-3660-ac03-4d1d7ee56743 | -11.78367 | -47.39611 | 2025-09-13 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 078954d4-3b7d-3fff-b39c-ddf318a1d48c | -14.28344 | -46.06723 | 2025-09-13 04:59:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dc07d79-ec09-32f5-991b-b07654d45ec9 | -14.19168 | -46.28228 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 081a9970-69dd-3a18-828a-45b4e20cd544 | -11.81436 | -50.55024 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 44638ea5-b70a-3677-9485-24a1a72354f5 | -14.20823 | -46.23419 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 912b35cc-7a3a-3b48-b7fa-65b8af999971 | -9.83449 | -54.53289 | 2025-09-13 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 224b795b-42a4-3e17-89fb-a58121109f78 | -13.23563 | -51.73392 | 2025-09-13 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64978729-f2a4-33d3-9251-c858e0e13537 | -16.25953 | -50.06828 | 2025-09-13 04:59:00 | NOAA-21 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 69e6391c-ef0f-3493-bdc7-8a7059d59fd6 | -9.26814 | -59.39756 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5f5936e8-387d-33c7-b066-6397e6624483 | -12.86411 | -62.12298 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README80.md)
