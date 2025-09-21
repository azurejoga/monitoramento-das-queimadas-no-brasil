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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e83be4f8-376e-3ac9-bd4f-aea35d384cd3 | -15.96695 | -59.41629 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 836339b0-745c-39d1-8601-b51ee2d47365 | -15.76827 | -59.45357 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bf38563-72b7-3972-a7d3-115a2b673a6e | -12.42101 | -45.10168 | 2025-09-21 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| abcc8714-966e-3797-a606-a16333dc2dc4 | -14.20642 | -44.66106 | 2025-09-21 04:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4d418a9a-e0e2-3a3b-8ec5-f7c131f53a89 | -18.73852 | -53.33001 | 2025-09-21 04:38:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ce3078f-4897-3b0e-94dc-12ea39b70d8c | -12.41698 | -45.12992 | 2025-09-21 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 408d21ea-f6cb-3d54-b9af-c66028c03b66 | -19.91039 | -44.71972 | 2025-09-21 04:38:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8760028d-c843-33ad-ba35-eab17f3be2ad | -15.94234 | -59.42944 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8daeacab-fd16-3e42-bee4-ede47982a153 | -12.893 | -46.77472 | 2025-09-21 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0574bec-b9da-3d78-8787-e4c426dd5d68 | -15.9468 | -59.46179 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9ea631f8-05cf-31ef-9096-b5609b32fcfc | -15.53448 | -42.17704 | 2025-09-21 04:38:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9eeb680e-b4c2-376d-95ec-bbd8dcc4b4b6 | -12.29256 | -50.12292 | 2025-09-21 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aebbd4d6-e934-3927-a21b-44f2271f3fe1 | -14.77309 | -51.38817 | 2025-09-21 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 889b85f8-6a06-3eef-94f5-f8f4d756ab26 | -12.57008 | -45.14101 | 2025-09-21 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75bd50f7-0d74-322f-a41d-2128cb294281 | -15.89575 | -59.39484 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdad6a9e-578e-3560-8133-c8bd1e8baaf6 | -18.9003 | -44.28244 | 2025-09-21 04:38:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 88cccb6c-99ea-3c94-838e-e2645b95d15c | -15.7734 | -59.4687 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3906dea1-45e9-3bfa-b669-f25371deb0a9 | -15.9755 | -47.27254 | 2025-09-21 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11505a09-94de-308b-8098-eb6b383e32e0 | -12.88068 | -46.78496 | 2025-09-21 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8bee99c-36f4-385d-9631-66c9f0f8cf72 | -13.77352 | -43.70735 | 2025-09-21 04:38:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 771b200d-fdee-3846-bd0a-3edc1522a508 | -13.20136 | -47.26258 | 2025-09-21 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b53ff85-621f-3c92-b413-743ca9c19b58 | -14.43807 | -46.52174 | 2025-09-21 04:38:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30c8d2c5-e560-36ca-a380-06697ddf09a7 | -14.97385 | -44.41629 | 2025-09-21 04:38:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1eec599-a70b-36bd-92b0-d3fb3de0d4a3 | -15.29127 | -59.41524 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c2d5ccc-d79d-35ee-b1b9-3e9a2c5c1c83 | -14.4279 | -47.57989 | 2025-09-21 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34be4913-5853-3080-b8a5-eb882b5a31c8 | -11.62418 | -50.58059 | 2025-09-21 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6eb80ef3-523e-3089-97f3-3392ff4ab70a | -15.9708 | -59.42442 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f276b6f3-e569-3cbf-b055-121c82aeea79 | -14.44407 | -47.56656 | 2025-09-21 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4515e73f-4528-3aae-9c51-62e64300f04a | -19.91096 | -44.71517 | 2025-09-21 04:38:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6063306-539d-3bbb-ba05-d57dface58ff | -12.43287 | -45.12781 | 2025-09-21 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1bf466ef-25e5-3a54-a472-786ed889fd0c | -15.94757 | -59.45794 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34ec2a5a-077e-3b30-8788-34f1929c5d82 | -14.97596 | -44.43205 | 2025-09-21 04:38:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5a82d3e-cb34-3c4a-8828-77f4eb641e26 | -11.62799 | -50.60019 | 2025-09-21 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6311e2ec-5edd-3c59-86f7-d60861de8160 | -14.78702 | -51.36748 | 2025-09-21 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c78cacca-d98c-3a74-b4f5-9b14b77a018d | -15.53029 | -42.17102 | 2025-09-21 04:38:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5080e7d2-45f3-308a-8c47-ff2c142fb69d | -15.96543 | -59.42386 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dcc5df04-5597-34d5-b3d4-8a2c736ddc53 | -16.86931 | -43.89928 | 2025-09-21 04:38:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 784ab326-77ff-3580-b8ef-10495658f01a | -14.43869 | -46.51744 | 2025-09-21 04:38:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d3dddf5-8eb7-3a05-aef8-8d3148544522 | -13.53963 | -43.00632 | 2025-09-21 04:38:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 37.4 |
| 1e11ef7f-f124-3287-9276-895e6727ea5e | -13.38593 | -43.59591 | 2025-09-21 04:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0139a4b8-a9b7-3d7a-8a00-f26a7133e6c6 | -14.31688 | -47.79073 | 2025-09-21 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dfe419fe-ce17-3951-a77f-c3a05d203af2 | -14.45753 | -46.51518 | 2025-09-21 04:38:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a4d0ecf1-bb20-31b2-89bb-88fac5ed74c0 | -13.36632 | -44.28168 | 2025-09-21 04:38:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5fa5b49-9c40-366a-9760-b2a3f00537b4 | -13.89583 | -50.66013 | 2025-09-21 04:38:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 373ec33f-2e34-347b-8169-f85f83720d69 | -15.68099 | -56.12952 | 2025-09-21 04:38:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d4ec0649-4284-332e-95de-0961b3f3510d | -13.31002 | -47.28284 | 2025-09-21 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 122d5655-5808-32f9-a523-b0659c0c5b74 | -11.62918 | -50.59281 | 2025-09-21 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f76dd2e5-552c-3913-a70b-654d952539e7 | -12.41832 | -45.12053 | 2025-09-21 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52072c19-f336-30f1-85a3-e7a0e420b62d | -15.77066 | -59.45462 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54b5ce25-0f92-3bcb-8841-d7f4a3d1a13f | -14.52458 | -44.86954 | 2025-09-21 04:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 388b0a3a-2802-383b-93a0-8ad919f48a06 | -15.70287 | -46.99944 | 2025-09-21 04:38:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6709e6de-5231-3673-b331-b8150254ddba | -13.53518 | -43.00574 | 2025-09-21 04:38:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 50.3 |
| 23c76835-315d-39b2-a458-2e85e56c1394 | -14.62486 | -48.26514 | 2025-09-21 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dad92a06-bf27-32bd-a36b-ddbc35830f9d | -15.89449 | -59.39478 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 603d15c4-4d79-331c-b7bd-3e225d673481 | -14.2906 | -47.41971 | 2025-09-21 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2423f746-f466-36fa-a204-d30dabca35e1 | -12.00536 | -48.6101 | 2025-09-21 04:38:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22c1b13b-1632-3fcd-b0e5-17b4a356f6d0 | -17.11269 | -45.95351 | 2025-09-21 04:38:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ed6e0f6-aeb6-33af-8149-0866e642b223 | -14.25711 | -44.38135 | 2025-09-21 04:38:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 772d0354-dedb-31fc-a5e6-854773d233bf | -11.62978 | -50.58912 | 2025-09-21 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5c8e55e9-1ec6-3b69-aedf-92b0bf148b9a | -15.90747 | -59.4656 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10ff2ed9-226a-3ff5-a1cd-6e6f49e291b4 | -15.82998 | -44.71093 | 2025-09-21 04:38:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0f67996e-4e1e-3d78-b51a-ea2f659d8f9d | -15.87961 | -47.29306 | 2025-09-21 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29b9efff-c41a-3bb1-9150-6d6e7cffc7ce | -14.31631 | -47.79448 | 2025-09-21 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d2820c0-f994-3353-85c0-87af7b3494f2 | -14.28986 | -47.41654 | 2025-09-21 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1e76aae6-0944-3b48-bc81-10547da1a16c | -12.4228 | -45.11648 | 2025-09-21 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d07566c9-64cf-3523-a755-0b6d499da020 | -13.31289 | -47.28736 | 2025-09-21 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f1513de-9f95-3e7e-ae94-d2bfdc46a453 | -12.27012 | -50.13394 | 2025-09-21 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 14532f6e-17a0-3ad3-80e3-07acc09cde10 | -13.30886 | -47.29056 | 2025-09-21 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7fd28886-c246-3fa2-8786-1321801a0514 | -13.89675 | -50.66047 | 2025-09-21 04:38:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f593f00-d75d-3d0e-8e9a-0bd281463cce | -17.44553 | -44.81061 | 2025-09-21 04:38:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35a73008-eb11-3cde-91cc-fa6026926bef | -17.16602 | -46.8432 | 2025-09-21 04:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3e4b5d6d-5a87-3be2-ae15-704d5327324c | -15.99393 | -47.27091 | 2025-09-21 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95fee426-2fec-30a1-a926-7e709eb35fc1 | -19.80349 | -46.67844 | 2025-09-21 04:38:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7f2c243-5d6c-3b10-b7fc-e1ef19c7fa6f | -14.47329 | -46.50876 | 2025-09-21 04:38:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bd478499-173c-39c2-9401-40e76609f0aa | -13.77405 | -43.70333 | 2025-09-21 04:38:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7fe0fe4-dd69-38af-971a-e6a047d4047e | -14.43138 | -47.58038 | 2025-09-21 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75f3fb9e-0ce4-360d-8d00-1d5b3b94d6b6 | -14.2566 | -44.38506 | 2025-09-21 04:38:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6a7d31f4-3a40-34cc-9ee6-a02f485d062c | -15.924 | -59.43851 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97eb32f7-9448-34a6-92c5-a26632d4cc69 | -14.61388 | -49.75879 | 2025-09-21 04:38:00 | NPP-375D | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2a2216af-85e0-3fff-b62f-15bc51292cf8 | -12.42907 | -45.12716 | 2025-09-21 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0657aa1a-7631-398a-8c39-ebfbdd50ef3f | -15.26867 | -56.83371 | 2025-09-21 04:38:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4bcfb096-dabb-3076-b987-b9c45e80b074 | -14.43443 | -46.52135 | 2025-09-21 04:38:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7600baf-248a-3150-b4cf-75e1fda12d7f | -15.77235 | -59.43382 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5308fbb5-98c6-3e4f-ad21-d344b4367f3e | -11.62459 | -50.59962 | 2025-09-21 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 298415bf-573c-3045-8984-94aba0c7f39a | -15.87425 | -47.305 | 2025-09-21 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e498b9f8-b159-3bdc-8cba-ec4a164ee91b | -17.43883 | -44.79711 | 2025-09-21 04:38:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b3d10f6-47a0-3b2f-b574-fcbed630f7c8 | -12.05962 | -48.75674 | 2025-09-21 04:38:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 709bbe45-2ef8-35d7-a9d8-7748967eb4c6 | -14.97848 | -44.41309 | 2025-09-21 04:38:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f85b41c6-07a6-3196-bcef-5fc34760686c | -14.43252 | -47.5727 | 2025-09-21 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a943f06a-bdac-33e2-92f1-0efbd0d607cc | -11.62399 | -50.60331 | 2025-09-21 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 227eb7c1-5299-3af5-b7de-23a56e12944c | -15.95481 | -59.42208 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34e59784-0404-33a2-a3ca-0221b9ffcb34 | -14.466 | -46.50786 | 2025-09-21 04:38:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18edb615-8b08-3fe6-9a88-6c6032e8eacc | -13.8865 | -49.14205 | 2025-09-21 04:38:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9ec79279-1528-39ad-b748-24fa341c95e5 | -11.61958 | -50.5874 | 2025-09-21 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 48b7cb51-166d-3887-b350-6b5032f45fb6 | -14.52058 | -44.86904 | 2025-09-21 04:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ece16fc6-28ab-3ff5-9883-78cdf70158a3 | -15.77764 | -59.43493 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ead7421f-0a14-337d-8e24-c573fc9c62f5 | -14.4739 | -46.50455 | 2025-09-21 04:38:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 62b52c13-679f-30d5-993d-5ffd86f05373 | -14.45449 | -46.51058 | 2025-09-21 04:38:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f174cfdc-36ee-3ab5-aa00-10eac34feb9a | -13.54075 | -42.99766 | 2025-09-21 04:38:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 31.4 |
| 63d8a943-bf50-3a62-8f99-c71066bf0090 | -13.64598 | -45.70197 | 2025-09-21 04:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README29.md)
