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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f30a93c9-8527-38f9-b115-5ac6cbc2a924 | -17.91599 | -54.68652 | 2025-10-06 04:29:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff018275-a1f7-373c-b9cd-4eb96af6c04b | -17.99353 | -57.60048 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d2a5986e-e991-320d-870a-d22b808120ba | -21.81547 | -43.36474 | 2025-10-06 04:29:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3c406fe7-c9df-3027-b984-41c54ec948ac | -16.15577 | -57.56806 | 2025-10-06 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3f3f149a-7674-3998-ad01-03cd0fe4a9e7 | -16.34537 | -51.45219 | 2025-10-06 04:29:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4573f40c-1d37-3fe9-b4e5-b28727ab49d3 | -21.39334 | -45.08365 | 2025-10-06 04:29:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 5b7cb75a-a53f-36c5-b22d-d48880f143ca | -17.97662 | -51.17472 | 2025-10-06 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99d35787-0bfe-3e74-bec8-355e644e864a | -18.27186 | -53.31878 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a1dd9009-9cf2-373e-9780-2aa86f2a5fef | -18.00155 | -57.6084 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3e293de0-d64f-3f28-881b-d6c8b5b36e5b | -19.779 | -43.83851 | 2025-10-06 04:29:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2bb2d67e-69d2-3b9a-97f6-a0a33aee56a3 | -15.99813 | -56.01543 | 2025-10-06 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4474ff07-12b0-3a47-893e-c85227e0ea43 | -21.6955 | -50.08619 | 2025-10-06 04:29:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 815f255d-cdcf-31fd-8253-499ebb7707ff | -18.1092 | -53.39977 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cb944982-37ba-3f71-a87f-57dcc40ed4cf | -22.07545 | -54.12833 | 2025-10-06 04:29:00 | NOAA-21 | DEODÁPOLIS | MATO GROSSO DO SUL | Brasil | 5003454 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 46446ac3-e885-37dd-b82c-673b87562fe8 | -18.14247 | -53.38926 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b7c4c78e-05e8-30f0-bbcd-a260adf56aaf | -21.68831 | -50.08869 | 2025-10-06 04:29:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8019da29-f168-3fcc-bb1c-7b8b40e9a08d | -23.40432 | -45.38195 | 2025-10-06 04:29:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| f432d482-96f9-38a9-8fef-5e5cbbf8a45c | -21.69336 | -50.0782 | 2025-10-06 04:29:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5a95e288-9a8e-390a-88bf-6e7a2926c0fa | -17.99654 | -57.53629 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 56bf0b66-f924-3259-a46b-b6f02d861a45 | -17.97582 | -57.58228 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| c498707d-b7ea-38e7-961a-854d7719274e | -22.12218 | -45.00748 | 2025-10-06 04:29:00 | NOAA-21 | SÃO LOURENÇO | MINAS GERAIS | Brasil | 3163706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 508f3eb6-33cf-3682-8b34-87d1dc0e0fdc | -17.96391 | -57.53915 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 6a82b4be-367e-3328-9c81-3785c575a61c | -22.85895 | -43.31188 | 2025-10-06 04:29:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 42b1e3d6-4ba9-32fb-9226-3387baf042c3 | -17.99847 | -57.60159 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ab57c3f5-bb66-3d74-8ece-bcd4581001bf | -18.61389 | -48.62083 | 2025-10-06 04:29:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff0bf439-2ed9-333e-b973-9082142b0949 | -18.18717 | -53.37682 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9d14fa68-e9d9-3cde-b5cb-58f64f5499e8 | -18.39994 | -45.22044 | 2025-10-06 04:29:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3284ef08-df56-33f8-903a-ab90efecddb6 | -20.85111 | -49.48065 | 2025-10-06 04:29:00 | NOAA-21 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8ce38ca3-a312-3115-ac5e-6dc959f00640 | -16.45691 | -52.15754 | 2025-10-06 04:29:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f58896b7-626e-3360-a2de-31ee7e50a2d5 | -18.00219 | -57.60857 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 061bf7b3-65c8-3968-b205-b5e7b53e8fc4 | -20.78781 | -43.32389 | 2025-10-06 04:29:00 | NOAA-21 | SENHORA DE OLIVEIRA | MINAS GERAIS | Brasil | 3166006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2668ed1f-3318-36da-8adc-ba882ef0c0f3 | -21.69162 | -50.08929 | 2025-10-06 04:29:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7c2cbdd1-a96d-35e1-860c-eb2068a78b88 | -18.64162 | -50.66843 | 2025-10-06 04:29:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b90a6c3f-e9e4-3578-824b-814767c3f57f | -16.34398 | -51.46033 | 2025-10-06 04:29:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 041df89b-f973-3224-a545-fb0a8b1396ba | -17.99861 | -57.54554 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| b3976d2f-a561-3e35-81e8-3330bee3fdd1 | -17.38242 | -53.59919 | 2025-10-06 04:29:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dfb2bea0-2145-32f0-9738-06db630613a3 | -22.52537 | -43.56692 | 2025-10-06 04:29:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3a687ece-0f5a-37a7-9c45-bb8a835ecb0e | -18.17503 | -53.37894 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 193f243d-0ffc-3d72-b1e2-c0674a5e7eb9 | -15.88034 | -59.37614 | 2025-10-06 04:29:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68612ffa-6476-3960-b53a-df2e41b4d35d | -18.18807 | -53.37184 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2d03b4d1-6ab0-33b2-865e-eb6941c9718f | -18.28586 | -45.4297 | 2025-10-06 04:29:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 776633f4-80ec-3912-ac7b-9af77731de30 | -17.9975 | -57.55108 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 42ef234b-7c78-3413-a5db-7115a7919b73 | -22.70233 | -44.87248 | 2025-10-06 04:29:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 39626f60-0dda-3945-ba7f-62c5fee37d75 | -21.10744 | -44.20987 | 2025-10-06 04:29:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 115df062-3d89-3e55-8d26-7610c37ae4f1 | -19.94042 | -44.64136 | 2025-10-06 04:29:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 7e9e81df-9b2d-34bf-845b-32b31abdada9 | -22.38259 | -50.02165 | 2025-10-06 04:29:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c41ff645-f1c6-354c-bf11-7e91d3c1d042 | -17.93993 | -57.60668 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3c3546f4-d6c1-3123-9781-7536f8189bac | -17.84259 | -57.62498 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 6e285226-4819-3936-9083-762dd6501edb | -22.36821 | -50.02669 | 2025-10-06 04:29:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| d5a973c4-a4cc-3b7c-84f5-ad51839a5adf | -22.16363 | -51.1767 | 2025-10-06 04:29:00 | NOAA-21 | MARTINÓPOLIS | SÃO PAULO | Brasil | 3529203 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| efdbc267-fe0a-3375-9fdb-8b2190654cb1 | -17.94485 | -57.60789 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bee20ba5-b96c-3f05-b1d0-ff1715180793 | -16.3645 | -51.48923 | 2025-10-06 04:29:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37a473d6-89ea-3f2a-878c-2244442a0cfb | -17.99255 | -57.55012 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| a5b76f4b-a653-3ed8-a2ff-142db70f16ef | -18.3956 | -45.22446 | 2025-10-06 04:29:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1b162853-2932-3a35-8b05-62d7416f40e6 | -22.16696 | -51.17733 | 2025-10-06 04:29:00 | NOAA-21 | MARTINÓPOLIS | SÃO PAULO | Brasil | 3529203 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d26f1fa-c58f-32a5-83f2-3a89a7f84c4e | -18.39064 | -45.20503 | 2025-10-06 04:29:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4009dd25-3900-3e15-a802-e9daf0ce489f | -21.40064 | -45.05816 | 2025-10-06 04:29:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1d32848d-652b-3982-a83a-b134b7ae93a8 | -17.60285 | -44.45433 | 2025-10-06 04:29:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fc445841-538f-3479-ae55-03bd05c073c0 | -18.18431 | -53.37096 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6049c2fb-1809-3c37-b25d-fee14d4e37ce | -18.18142 | -53.36528 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57178c39-ba57-33c1-92a0-29beeefa3e4a | -21.73202 | -50.06995 | 2025-10-06 04:29:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7e0b26cf-89e3-3034-8191-c493935c83f9 | -22.3925 | -50.02343 | 2025-10-06 04:29:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 1bd284b0-c311-3d17-b5d7-274d98cfe2d2 | -23.1441 | -46.6814 | 2025-10-06 04:29:00 | NOAA-21 | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b6a823c3-639b-3c9d-bef6-27abb4f20e1c | -18.00064 | -57.53537 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 686ad8d2-db33-358c-a985-b4c1cd0abaa8 | -17.91875 | -57.60913 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3194a05e-fe8a-3fb3-afdb-505e97972139 | -17.96517 | -57.55839 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 5dd8e783-eafd-3f14-a3e5-ee47fffa0af2 | -16.94656 | -52.67616 | 2025-10-06 04:29:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9768b0d-22c8-3950-b01c-a2c76646abc1 | -17.98609 | -51.16023 | 2025-10-06 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e29e1cf2-1782-394a-8201-57d2c9ff52f7 | -19.66162 | -45.92505 | 2025-10-06 04:29:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e5e4540-6c1e-3ec1-be6f-05175ba25244 | -15.98983 | -56.00848 | 2025-10-06 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 2f546fde-334c-3d3e-a768-569a13024b64 | -17.26536 | -46.92033 | 2025-10-06 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eeb21cb9-d3e6-3e95-a328-b9248a678508 | -18.27242 | -45.41846 | 2025-10-06 04:29:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18d39a45-fe0c-30ae-851d-9e803af44378 | -20.70306 | -54.57899 | 2025-10-06 04:29:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53b7da90-f30f-3086-bee2-4149f214b01d | -17.89557 | -57.64639 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ea253069-8aba-3a56-9195-e3925bc00796 | -18.2688 | -53.33574 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b2c1219a-0673-3075-a700-f08280673bff | -18.25148 | -53.32338 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 15e0d0b7-91c0-3c2b-b82a-469acfbbeeb4 | -18.11869 | -53.39063 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 91f01ca3-6edf-3de0-8009-7932e3669f18 | -19.11135 | -43.60839 | 2025-10-06 04:29:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6f18c9b-b265-3564-8892-b07c0f8d6d0b | -18.12344 | -53.38598 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f482a34f-b3f1-306c-b2ec-2ee61c70be99 | -23.22532 | -46.46229 | 2025-10-06 04:29:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5a59ac2f-fb9f-35db-819d-d26eeeba1aaf | -18.11595 | -53.40601 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e33f1431-9656-3ddf-bd34-45804b4d9d0a | -17.98077 | -57.53199 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.5 |
| b8b81052-c8f9-3df8-a2a8-dec69456ab2f | -18.02443 | -44.99682 | 2025-10-06 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15f7a0f4-26f8-39ed-8bd6-ea0c5c53e2c2 | -17.34488 | -46.83049 | 2025-10-06 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 470fdb6c-967e-3457-a196-4a7dfcdf837e | -17.95711 | -57.59836 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| af3dfd4f-e6e0-3eba-a8bd-71d30666c2cf | -21.39591 | -45.03753 | 2025-10-06 04:29:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 38040377-33b5-30e1-b1df-d9b558b22e88 | -18.81533 | -44.47386 | 2025-10-06 04:29:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b75f290-4e84-39a7-8589-af8185c58545 | -20.34837 | -44.08696 | 2025-10-06 04:29:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ad774459-762b-3083-a1a9-ad549589d4ba | -17.70113 | -56.76795 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| c5c9c6bb-dedf-327c-9c0b-25b9f791aada | -18.13752 | -53.41238 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 53aeefb6-fab9-365b-8304-1769f9e14b06 | -17.94425 | -57.61083 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 10cd6343-5f4c-32fd-8998-ed6f869f6d89 | -17.26085 | -46.92741 | 2025-10-06 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58f89fab-4766-3f45-9766-a97abb69723f | -18.39622 | -45.21986 | 2025-10-06 04:29:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 08453d49-3e9d-30cc-854c-8db30648958a | -17.98934 | -51.14067 | 2025-10-06 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b9c5bf68-012c-3323-872f-49be44d18e5d | -21.69822 | -50.09047 | 2025-10-06 04:29:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9e5108b3-cebc-3412-8414-a7d8cf7564bc | -17.87652 | -57.63814 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3cbd2fc4-cf39-38a4-903b-9f7cbbb01528 | -22.07917 | -54.12909 | 2025-10-06 04:29:00 | NOAA-21 | DEODÁPOLIS | MATO GROSSO DO SUL | Brasil | 5003454 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6592f8c5-e491-3402-b701-45ff234ae70a | -23.17618 | -46.80267 | 2025-10-06 04:29:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 273f669c-a95f-38b8-836e-6d5217a60f65 | -15.98887 | -56.0135 | 2025-10-06 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5b3debe1-e2af-37d0-8c82-c09cd52ad179 | -21.86532 | -48.29604 | 2025-10-06 04:29:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README56.md)
