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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0519a0f-d252-36c1-ba48-b09e08d68a62 | -10.45866 | -47.94889 | 2025-05-31 03:36:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 968df81b-428d-3e9e-86fe-f34c23bd2a48 | -10.45188 | -47.94742 | 2025-05-31 03:36:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4ed468f4-2369-3600-9941-f6d8c31a673b | -10.45991 | -47.94258 | 2025-05-31 03:36:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 3fa466a4-fb15-3442-a6d9-0def976a2b92 | -14.06868 | -47.65633 | 2025-05-31 03:36:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1a9d96e-82f7-3bac-9937-96bdd85c6281 | -11.68106 | -48.2618 | 2025-05-31 03:36:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 523228de-6bd0-3600-91cb-d0f1810d648e | -13.63757 | -47.44649 | 2025-05-31 03:36:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e273a49-3cf0-3eb8-84e6-3362b71cb940 | -12.71308 | -44.93727 | 2025-05-31 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b6a54ad-be40-3fdf-b71c-8a79b8efa82b | -14.66693 | -45.40191 | 2025-05-31 03:36:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00f2c5ed-e51a-36a2-9b90-64f059d03720 | -13.08826 | -45.2881 | 2025-05-31 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68c2abea-5bd4-3365-b3f5-18fb0435e221 | -13.08978 | -45.28042 | 2025-05-31 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fcebf34e-4791-3d7e-bf34-c6bf56c4f141 | -11.45111 | -49.09893 | 2025-05-31 03:36:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5b7cc86f-d121-3df5-ac88-c6021f84bd19 | -12.86295 | -38.36738 | 2025-05-31 03:36:00 | NOAA-20 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 82cc99bb-6512-3a08-8e14-603ed157364d | -13.30402 | -44.26881 | 2025-05-31 03:36:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63313002-432b-3852-b752-fd94f02f2484 | -13.64284 | -47.45259 | 2025-05-31 03:36:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3f4764c-745d-377a-9927-c689ed6a171d | -12.27397 | -44.58739 | 2025-05-31 03:36:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 997f298f-e387-35b3-8ddf-d4e86e54226e | -14.07009 | -47.65964 | 2025-05-31 03:36:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff9bc4e9-ce48-3786-9170-837fb4452a56 | -13.0946 | -45.28544 | 2025-05-31 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9a7aaf6-5ed1-39e4-bdf8-bccce9bf03a8 | -13.85503 | -43.52266 | 2025-05-31 03:36:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec07d46e-c354-391e-bcc6-fae3472e6c77 | -14.66619 | -45.40556 | 2025-05-31 03:36:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f78c434-5a7d-35de-980d-e5b2cfbd9372 | -11.68081 | -48.26174 | 2025-05-31 03:36:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be7d6bb8-3832-3ac5-9af7-7ce6d823148c | -11.68789 | -48.26321 | 2025-05-31 03:36:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69bb330c-e3d6-36f9-8497-8a9bec88d826 | -13.30339 | -44.27211 | 2025-05-31 03:36:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5b65d30-6915-307a-9303-87686f1fea8f | -13.10166 | -45.27905 | 2025-05-31 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e758ade4-a2e3-3827-831d-3a8d4c12d870 | -13.64088 | -47.44926 | 2025-05-31 03:36:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4d1c772-473d-37ff-a991-2c70b1708db6 | -15.88717 | -43.45805 | 2025-05-31 03:38:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 2f1fbaea-4aa5-336a-be51-27f2d22acd0f | -16.76288 | -46.56788 | 2025-05-31 03:38:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1eca5bee-4886-3812-9c78-ad9e5ecbffef | -16.58607 | -45.87763 | 2025-05-31 03:38:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aca2a39e-020a-310d-8a93-268f2d7d1826 | -16.02694 | -43.68334 | 2025-05-31 03:38:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac4476f0-7a13-3688-9488-04bb71ea9c4f | -15.88345 | -43.45181 | 2025-05-31 03:38:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 6f559eb7-85f3-32b3-9ca7-96001a5fdf03 | -16.57963 | -40.44479 | 2025-05-31 03:38:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 31679f16-10e8-3791-bd84-9ca75a3a0ad8 | -16.7586 | -46.56961 | 2025-05-31 03:38:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63eabd0b-a0f3-31a4-9fe3-eb6a245e0eb9 | -15.88246 | -43.45707 | 2025-05-31 03:38:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| c4825d9a-1586-3f2e-a054-208e63f946be | -20.60658 | -48.86686 | 2025-05-31 03:38:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6372258e-9ba5-325a-be7f-28b07135c7a2 | -22.62602 | -47.06448 | 2025-05-31 03:38:00 | NOAA-20 | HOLAMBRA | SÃO PAULO | Brasil | 3519055 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 80c10cb8-5210-37f3-a0f1-c94ad58ba54e | -16.76205 | -46.57185 | 2025-05-31 03:38:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 908f9ceb-aacd-3e3e-b414-f07b4e8a8d8e | -16.1193 | -46.82239 | 2025-05-31 03:38:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80bf4004-1526-384d-807c-027845842720 | -16.59147 | -45.87897 | 2025-05-31 03:38:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| edc66904-0df3-3785-b286-c9da28d93b7f | -22.6312 | -47.06581 | 2025-05-31 03:38:00 | NOAA-20 | HOLAMBRA | SÃO PAULO | Brasil | 3519055 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 78551355-6da4-3440-b9c1-ca07fba91886 | -16.58433 | -40.44085 | 2025-05-31 03:38:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1c6a44e3-1298-3772-ba75-e3f7526c3b00 | -15.88321 | -43.45742 | 2025-05-31 03:38:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 718a40ad-9036-3bc4-93c3-430e3495e6f6 | -20.60643 | -48.87141 | 2025-05-31 03:38:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 06ffcd9a-eb2a-38e3-a57f-1ca5ed150036 | -16.58997 | -45.88198 | 2025-05-31 03:38:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f0a1672-960f-32c3-aedb-6e0974da0af2 | -15.37073 | -45.67437 | 2025-05-31 03:38:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bcebca48-9f8d-3ed0-b4a5-8875bb7fe923 | -20.60759 | -48.86644 | 2025-05-31 03:38:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8f5d1af6-f4f0-3c11-b3e7-0faf5e084cf5 | -15.36998 | -45.67807 | 2025-05-31 03:38:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9fc2b0f-0bda-3318-9a9d-84fd86897d6f | -16.59071 | -45.87834 | 2025-05-31 03:38:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c2e0050-4122-31ed-928a-8ccbd27979d9 | -15.88792 | -43.45839 | 2025-05-31 03:38:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| c6a4f9b5-9afb-390b-8dbf-d07ccfff8655 | -21.24934 | -50.31138 | 2025-05-31 03:38:00 | NOAA-20 | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 369ebc3f-4ca4-3936-9cf5-fdd910d949f5 | -20.60544 | -48.87185 | 2025-05-31 03:38:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6c843c3b-03be-3f6e-9e7c-e3c8fe923ef9 | -15.8757 | -43.4566 | 2025-05-31 03:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 98b7bf8c-edd7-3845-a357-48c307bd1b65 | -11.8365 | -51.2854 | 2025-05-31 03:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 0b40b5f0-b7f0-3938-83dc-0b23e8235e68 | -15.8955 | -43.4523 | 2025-05-31 03:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 57045ae1-56e9-34e5-a7dd-a970b7f52df3 | -12.0345 | -49.5248 | 2025-05-31 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 71084b61-b3a9-340c-ba40-7d69c2d2798d | -10.462 | -47.9428 | 2025-05-31 03:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| bf70d73f-3d63-3a25-925d-01b7e3b593fb | -11.8368 | -51.2641 | 2025-05-31 03:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 8afaf22c-e2e1-3926-8952-017f7924a0fd | -12.0154 | -49.5272 | 2025-05-31 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| f5c7a091-a607-360d-ae91-9ddfe8d0cbeb | -11.8368 | -51.2641 | 2025-05-31 03:50:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| b3ee375c-83b3-3454-9fb6-cda9eba71b33 | -12.0154 | -49.5272 | 2025-05-31 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 104bd1fb-c0ec-35ff-bf60-4920ae183b4e | -10.6492 | -49.4267 | 2025-05-31 03:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| fedad316-9017-333c-94b3-8be05d50d716 | -11.8365 | -51.2854 | 2025-05-31 03:50:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 7977e785-9dae-341b-abd6-f7abe0d91768 | -12.0345 | -49.5248 | 2025-05-31 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 3966e001-4366-3243-a3d5-978b0164eb50 | -12.0154 | -49.5272 | 2025-05-31 04:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 0042080c-3006-35b9-bfe0-adfd40042321 | -11.8368 | -51.2641 | 2025-05-31 04:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| ec47abf8-64bc-3422-a358-8ef8701ca762 | -11.8365 | -51.2854 | 2025-05-31 04:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 50.7 |
| a357c81b-1312-33b2-a94b-fc702fa446be | -11.8365 | -51.2854 | 2025-05-31 04:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 49.7 |
| b4a070c0-bb8c-313a-bf6a-ffdfd24f0b3d | -11.8368 | -51.2641 | 2025-05-31 04:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| a61be9de-b407-31c9-a764-73efdf237514 | -12.0154 | -49.5272 | 2025-05-31 04:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 289a3c18-2c1e-3ab1-9706-011adc351e8f | -10.6492 | -49.4267 | 2025-05-31 04:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 86be9f5e-ca67-3d9d-8c03-45b48f081500 | -11.8368 | -51.2641 | 2025-05-31 04:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 8ffd3b12-6d84-36c2-8ead-d316a997379b | -12.0154 | -49.5272 | 2025-05-31 04:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 7656fb19-c905-3cc9-829d-e622f1b67ba2 | -11.8365 | -51.2854 | 2025-05-31 04:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| e775b2f5-7099-3c14-bfb3-97ae4e7adddf | -6.21525 | -43.33797 | 2025-05-31 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23736dd1-2951-3dbe-810c-66fa934cf86d | -3.04193 | -49.43781 | 2025-05-31 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb6b5046-ccf3-3183-9d81-27f80a60e1b1 | -4.82303 | -44.35386 | 2025-05-31 04:25:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fd545d8-63bc-3f5d-849b-b77a24c1c8b6 | -6.2117 | -43.33742 | 2025-05-31 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 84007d5f-92a6-329e-8b72-487fb4f40d6f | -6.27365 | -44.20263 | 2025-05-31 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23f43aa5-c583-3fb0-b05f-70177c46bf2d | -7.20017 | -46.46751 | 2025-05-31 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8fa762d-0cad-35ec-a7ea-bd5c3dc850d1 | -7.25013 | -43.24979 | 2025-05-31 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dea9335b-bae2-3787-8a44-22832d374bae | -8.19706 | -49.81072 | 2025-05-31 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c7c0325-808b-3cd2-9e63-dcf02c1b8330 | -5.83119 | -44.09028 | 2025-05-31 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77a5fe63-6ed8-357b-93c6-ed490abc4abf | -7.15078 | -43.39683 | 2025-05-31 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 94e99984-83b5-3352-bdc1-054133c1224a | -7.31119 | -55.30649 | 2025-05-31 04:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7dc31352-5ab5-314d-b7bd-63a873db6ba9 | -6.69135 | -43.68748 | 2025-05-31 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8b44a8bd-82ab-36ab-82ff-87468cd89e7a | -7.22674 | -43.13359 | 2025-05-31 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 69e5c54b-3b85-346a-ab52-ef7c966add65 | -7.24771 | -43.09296 | 2025-05-31 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 381d03d7-201c-364f-b638-b99110d9dd07 | -8.47835 | -49.60468 | 2025-05-31 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fa543de9-5792-3e0b-9d39-0b338d58088e | -6.3393 | -43.38023 | 2025-05-31 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c9011b9-ea8d-3d63-b8d5-65595699e7ed | -8.47768 | -49.60872 | 2025-05-31 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 33158090-bdd8-3bfd-9d70-13f4691d201f | -5.05184 | -43.24688 | 2025-05-31 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e2293d7-3b0b-33ed-b482-923d5c69cca8 | -6.20753 | -43.34089 | 2025-05-31 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e0fdf02-4ac3-311c-879f-5112d1c5329c | -5.0908 | -47.24347 | 2025-05-31 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7a365aa-592b-3bd7-b87a-db9210e54fb3 | -6.15558 | -42.61502 | 2025-05-31 04:25:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 85d91cbc-2b04-30e7-96fa-be366477df87 | -7.9305 | -45.42051 | 2025-05-31 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e608d63c-92a5-3e7c-9f0f-e55b98ecfe54 | -6.15491 | -42.61938 | 2025-05-31 04:25:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3e548217-43af-3290-8831-d44fc3275c57 | -8.66019 | -47.80978 | 2025-05-31 04:25:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34e2ecd2-2037-3ad5-8bb7-aeff431b71d5 | -9.04611 | -47.02428 | 2025-05-31 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 821283e6-ac1a-339e-a62b-2e42628ab7db | -6.17916 | -48.06882 | 2025-05-31 04:25:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db1d7e66-e34b-357f-bb36-0cf3cda91756 | -8.20627 | -49.79954 | 2025-05-31 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8d16a26-f6ae-306f-b744-b24d07aba80c | -7.00966 | -44.62081 | 2025-05-31 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f978e9cb-8be7-31da-a2a3-acf53768f112 | -8.31619 | -47.91769 | 2025-05-31 04:25:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README7.md)
