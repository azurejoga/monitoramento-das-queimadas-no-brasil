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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5da1dc58-8c03-323b-a546-54b2f2f70e18 | -15.89635 | -59.39182 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22a03532-6df3-3e24-b653-8e23bda1779b | -18.74203 | -53.33069 | 2025-09-21 04:38:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9cf5fac7-099b-3a1a-9c61-afe7ad956892 | -14.43599 | -47.57323 | 2025-09-21 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0edda57b-7a3d-3877-b33c-9d787f309d2e | -15.53124 | -44.31552 | 2025-09-21 04:38:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7b46c29c-f3d4-3ac3-a5b8-2a0da34bd233 | -14.97284 | -44.42388 | 2025-09-21 04:38:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8bbf73f4-8392-3747-aaa7-84bdc8e7e62c | -13.35767 | -44.28418 | 2025-09-21 04:38:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33de8a90-48dd-3e17-ab82-b510fb471e93 | -13.25349 | -47.28098 | 2025-09-21 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4b8ef6b-2578-3fdc-89d5-b65b6c265eed | -12.42212 | -45.1212 | 2025-09-21 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eba01011-4c6b-31f7-9752-ff37ea8475f1 | -15.96617 | -59.42016 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| bbd32703-e55e-3eeb-a7ab-47d3f37d9032 | -15.90719 | -43.05185 | 2025-09-21 04:38:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 46778561-9fd1-3737-8a78-5318cba5d459 | -15.82215 | -59.51476 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8f8e28fd-829b-38da-a911-7ffab9d8954f | -14.46541 | -46.51195 | 2025-09-21 04:38:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c7ef7f5-59a7-373f-ae76-39fef9069238 | -14.28638 | -47.416 | 2025-09-21 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38b06e4b-ef43-3712-b356-8ba13eb5d9c8 | -14.02668 | -43.74096 | 2025-09-21 04:38:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58f47b81-2f6a-3de4-9d83-01ab8b2ba690 | -14.79536 | -51.38049 | 2025-09-21 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b67d71f8-3aea-3ea9-bf39-ed4ed451fc0a | -15.76997 | -59.45813 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 145f9331-dd10-3e47-955d-738ea1bae477 | -14.81855 | -51.38839 | 2025-09-21 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bcf3441a-99ba-3572-aa3d-581883facb20 | -12.88421 | -46.78551 | 2025-09-21 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 918767c4-9b9e-3a1f-8c19-e57bd45b5864 | -14.60609 | -49.76482 | 2025-09-21 04:38:00 | NPP-375D | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0743b95-5976-3c1e-8226-9f816175a026 | -14.97183 | -44.43148 | 2025-09-21 04:38:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58612085-452c-333e-b074-f846e134d206 | -15.95343 | -59.42891 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af7cd3ee-60a0-3966-ae67-84fe622ac7e2 | -12.41967 | -45.11106 | 2025-09-21 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f257da3-ca02-3e65-b7f8-54b13819b585 | -15.81532 | -59.52114 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0b798705-83f2-3363-b051-e3bc9372f6d9 | -15.93054 | -59.43342 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebdc1792-c1e4-38c3-abcc-0761d2909833 | -14.16872 | -49.10358 | 2025-09-21 04:38:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 708df1c4-04c7-3132-a7d5-c9ebd30bde78 | -15.95277 | -59.4322 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c859677a-deb6-3de5-afb2-4c41e907db92 | -12.4284 | -45.13181 | 2025-09-21 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5700a923-cb46-3b5f-9db6-3034957ce207 | -14.97798 | -44.41689 | 2025-09-21 04:38:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47a174e4-e848-30f4-8e1e-25d8a0550f37 | -15.97622 | -59.42478 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 853dd971-99ce-3917-9263-59e849b53538 | -13.25252 | -44.11509 | 2025-09-21 04:38:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0cdbb33-d63e-3d1f-b0e4-48b2af7e20d7 | -12.26953 | -50.13753 | 2025-09-21 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f26d2e8a-cdfc-3d67-93ee-b835fecefbda | -14.46178 | -46.51146 | 2025-09-21 04:38:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bf28dec2-58c4-3c74-993b-760d530cb2fe | -14.43484 | -47.58088 | 2025-09-21 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c20c897-d9f6-3b31-b30d-2789d790960e | -15.27691 | -56.86463 | 2025-09-21 04:38:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b2ff3b60-d300-3100-945b-d7f4a75d2787 | -15.8951 | -59.39811 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe33a50a-44b2-3424-b1de-22928b3a9362 | -15.93711 | -59.4281 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb71b0a1-453f-37de-b689-e0d637e0d25c | -15.53514 | -42.17152 | 2025-09-21 04:38:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20a2c922-439e-364a-918e-b4cc10384864 | -15.89382 | -59.39806 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f6a09c8-bf2b-393d-bd42-c9d727f1c948 | -15.77396 | -59.43803 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abcb60a8-2afd-3346-84a8-d139e8e2c342 | -14.46905 | -46.51245 | 2025-09-21 04:38:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4215457-ad74-3bdd-805f-3d1980b9a0ed | -14.62713 | -48.27312 | 2025-09-21 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d765abf-3ec9-321c-b271-30e879be5462 | -18.10175 | -44.67288 | 2025-09-21 04:38:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f47af758-d22f-38df-bcc3-76f76dba590a | -14.74417 | -49.18915 | 2025-09-21 04:38:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66c54869-2c2d-36f3-930f-0507fe1834fe | -14.43771 | -47.56163 | 2025-09-21 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| db964418-15aa-3022-a6fa-8360a6ecdd26 | -14.74027 | -49.1922 | 2025-09-21 04:38:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1e8a70e-15f2-3617-a4e2-c52876240c02 | -15.27325 | -56.85918 | 2025-09-21 04:38:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fcb2cc19-9149-3018-a9d3-09a167de3543 | -15.96009 | -59.42312 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a4fe46f-c1cf-354e-a11e-52f316e3eed5 | -13.25012 | -44.11175 | 2025-09-21 04:38:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 210df67e-2c4f-3801-9cf2-6bb0980d23c8 | -18.46289 | -47.24788 | 2025-09-21 04:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3665d6d8-f6dd-3b8a-900e-70a4f4a4fb6f | -14.61055 | -49.75824 | 2025-09-21 04:38:00 | NPP-375D | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fe7ded9a-b1f5-395a-b4e9-5eef1d90303a | -15.89512 | -59.39172 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7adc6af4-e048-3c80-aad7-e450629bbde6 | -16.2246 | -46.65173 | 2025-09-21 04:38:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5d9d0e1-f928-3a48-aa83-3d8f2f0492d2 | -15.29542 | -59.42217 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9e00180-63ba-3dc1-b3fd-c097e55c6cc1 | -15.9716 | -59.42045 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8b4b945c-885d-39ac-8461-07b693759915 | -15.76756 | -59.45701 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 252ce8e7-4f8a-3306-abdb-2b23f86251bd | -14.81577 | -51.38405 | 2025-09-21 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b002365-47c7-3675-bbc5-00a4f288f1f9 | -12.27347 | -50.1345 | 2025-09-21 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a19801bb-e19b-33f4-9315-6cc4ffb8797e | -16.54618 | -42.34931 | 2025-09-21 04:38:00 | NPP-375D | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 186465bd-9dca-37e9-af39-60da823abdc4 | -11.62858 | -50.5965 | 2025-09-21 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7b61fa46-c9b3-3dba-8d38-6b4c908d7dbd | -15.81756 | -59.51006 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5c1bd105-bc6c-3839-ae80-af3e30b6a634 | -14.79103 | -51.36434 | 2025-09-21 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 830f426e-4687-3176-bae8-8a51d51f433a | -15.95412 | -59.4255 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 45cb10e2-d525-3fd0-a9fa-1bb2ab0f8fdd | -15.69271 | -46.99343 | 2025-09-21 04:38:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8463effa-86c3-3c02-8267-b3b453941a7d | -13.24917 | -47.21408 | 2025-09-21 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6691fecc-9dc9-3b32-9fb6-912a0317b46a | -15.97766 | -59.41757 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 000a877a-79c7-309e-ab1c-9799480cc657 | -12.89711 | -46.77128 | 2025-09-21 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c85f1b8c-b8aa-3b9b-9eb2-86045dba8ffe | -13.30943 | -47.28675 | 2025-09-21 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e9e2260-4490-334c-b822-abfa21f988eb | -18.94092 | -47.20259 | 2025-09-21 04:38:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d789b049-48bd-3c01-92bd-7580fc947a19 | -12.4735 | -46.69317 | 2025-09-21 04:38:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a740a471-0caf-333c-9263-aa84972c7030 | -11.08063 | -54.2579 | 2025-09-21 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9ac3db5-99d3-364b-b388-60fb23dc5766 | -13.70522 | -47.57377 | 2025-09-21 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a66c3a51-98cc-38be-8dba-036867b3c6c4 | -15.99749 | -47.27145 | 2025-09-21 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdf30fb5-a157-35d2-83a4-370fba9939a7 | -15.27417 | -56.85429 | 2025-09-21 04:38:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 267982ce-3cb8-3eed-b220-d0cae0074d68 | -14.47269 | -46.51292 | 2025-09-21 04:38:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18feca27-7718-32f8-93fc-a0d55e3e24a9 | -14.29118 | -47.41573 | 2025-09-21 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f0021f9-75fc-39c3-9246-6667533e5431 | -14.97697 | -44.42447 | 2025-09-21 04:38:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 701b03b8-c652-3e54-bed5-b3209f9cd58d | -17.11202 | -45.9585 | 2025-09-21 04:38:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8759c0d8-2b1b-35da-a6e9-603ea048b4a5 | -14.44118 | -47.56214 | 2025-09-21 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a186744-94fe-3a6a-a56d-01b599d9ec98 | -14.44349 | -47.57044 | 2025-09-21 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5540225e-da48-341f-be0b-8fb3c60af782 | -14.21044 | -44.66168 | 2025-09-21 04:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 749043bd-bee1-3371-9d0d-839e23ed8097 | -12.42033 | -45.1064 | 2025-09-21 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb1f5545-cdb1-35d3-87ae-50b9ec7c119b | -11.64008 | -50.61319 | 2025-09-21 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 20ba7b58-fdb9-3d73-b400-d31ca0507457 | -15.27321 | -56.83444 | 2025-09-21 04:38:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 81e51565-2997-3f32-a639-695d907b9c85 | -15.66973 | -50.22779 | 2025-09-21 04:38:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5abd44ef-0787-3311-9f8c-5f3a76f45005 | -15.87485 | -47.30085 | 2025-09-21 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10b02344-6df5-36ff-8785-21e4ebc05bbb | -14.29334 | -47.41709 | 2025-09-21 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4aad588c-1650-3e44-9f48-85eb22ba87be | -14.15294 | -44.07815 | 2025-09-21 04:38:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa0015f8-2d1b-3ac5-a92d-6081418c8421 | -16.60331 | -43.68173 | 2025-09-21 04:38:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c821fc3-fe07-3da2-b308-9a04562d0129 | -15.70348 | -46.99516 | 2025-09-21 04:38:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8a5c35a-c038-35d9-9468-44bc914a87bf | -12.41385 | -45.12457 | 2025-09-21 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79210768-debb-3b1f-9117-585eb83e5b58 | -14.46964 | -46.50834 | 2025-09-21 04:38:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec4f2b01-6dc9-3c84-af6e-208d165dc23b | -14.51733 | -44.86316 | 2025-09-21 04:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6c414b0-9502-3f73-b917-95b0becf5c71 | -15.92465 | -59.43534 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6665a5e6-d3ff-3535-82b5-c51857ef8fd1 | -14.21118 | -44.6563 | 2025-09-21 04:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e69f386-cf65-38a6-b38d-367675f25b15 | -14.60665 | -49.76125 | 2025-09-21 04:38:00 | NPP-375D | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ebfed655-d413-3479-88f3-c8a7395eec00 | -14.45813 | -46.51102 | 2025-09-21 04:38:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1eef00b3-73b9-3d1e-9c45-7e63b760f155 | -15.9085 | -59.46055 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68d492e3-bcc8-32fd-ba12-905eecbed6fa | -18.74273 | -53.32659 | 2025-09-21 04:38:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 257a9253-5285-38fd-8b50-459704b97617 | -11.5842 | -50.29195 | 2025-09-21 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4584b794-7410-3ce9-8cf6-596d55040fc0 | -17.44296 | -44.79794 | 2025-09-21 04:38:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README30.md)
