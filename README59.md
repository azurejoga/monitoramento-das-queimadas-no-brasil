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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 069bbff7-155c-34ee-8503-40b016acf006 | -27.16536 | -51.17556 | 2025-10-24 12:23:00 | TERRA_M-T | TANGARÁ | SANTA CATARINA | Brasil | 4217907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| c497b16b-37e4-30d9-a1d3-d249b77ffa84 | -27.05869 | -52.89367 | 2025-10-24 12:23:00 | TERRA_M-T | PLANALTO ALEGRE | SANTA CATARINA | Brasil | 4213153 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 498091df-d32d-32f9-ab46-e9724392c155 | -29.86199 | -51.91465 | 2025-10-24 12:23:00 | TERRA_M-T | GENERAL CÂMARA | RIO GRANDE DO SUL | Brasil | 4308805 | 43 | 33 | nan | nan | nan | Pampa | 12.9 |
| 562e194e-5117-30d9-940a-e6eeff7900d4 | -27.0246 | -50.92219 | 2025-10-24 12:23:00 | TERRA_M-T | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| ba2b4e09-bc42-37ea-8f72-bb561effce2f | -29.8634 | -51.90427 | 2025-10-24 12:23:00 | TERRA_M-T | GENERAL CÂMARA | RIO GRANDE DO SUL | Brasil | 4308805 | 43 | 33 | nan | nan | nan | Pampa | 14.4 |
| e60a52aa-8e08-39d6-abec-24018ab9d5cc | -25.61807 | -50.57407 | 2025-10-24 12:23:00 | TERRA_M-T | REBOUÇAS | PARANÁ | Brasil | 4121505 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 27e49535-5d12-39b0-a210-0e8f1cf26d5d | -27.30983 | -49.9431 | 2025-10-24 12:23:00 | TERRA_M-T | POUSO REDONDO | SANTA CATARINA | Brasil | 4213708 | 42 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| a424e2c1-fb04-3f7a-aef1-a574d9f8c196 | -28.97323 | -51.06441 | 2025-10-24 12:23:00 | TERRA_M-T | SÃO MARCOS | RIO GRANDE DO SUL | Brasil | 4319000 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 05fbf017-a412-315a-b0b6-6fa2168e7f7d | -25.61943 | -50.56396 | 2025-10-24 12:23:00 | TERRA_M-T | REBOUÇAS | PARANÁ | Brasil | 4121505 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| c98528c2-4648-39c3-9a70-148587df1ed9 | -31.31424 | -52.1964 | 2025-10-24 12:23:00 | TERRA_M-T | SÃO LOURENÇO DO SUL | RIO GRANDE DO SUL | Brasil | 4318804 | 43 | 33 | nan | nan | nan | Pampa | 5.0 |
| a9e6000a-3eba-35eb-8841-e4fc83324533 | -31.20583 | -51.97558 | 2025-10-24 12:23:00 | TERRA_M-T | SÃO LOURENÇO DO SUL | RIO GRANDE DO SUL | Brasil | 4318804 | 43 | 33 | nan | nan | nan | Pampa | 3.7 |
| 987ef37c-e3f9-326a-8d04-18a1657724d9 | -27.30843 | -49.95406 | 2025-10-24 12:23:00 | TERRA_M-T | POUSO REDONDO | SANTA CATARINA | Brasil | 4213708 | 42 | 33 | nan | nan | nan | Mata Atlântica | 40.2 |
| 6e18c3da-9588-34a8-bac7-1697ef5efd32 | -27.16673 | -51.1654 | 2025-10-24 12:23:00 | TERRA_M-T | TANGARÁ | SANTA CATARINA | Brasil | 4217907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 670f55c9-03ce-322f-ba68-5c5c58f1aa08 | -27.34682 | -50.56935 | 2025-10-24 12:23:00 | TERRA_M-T | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 063fe037-405d-3d8a-9788-d73862a8f027 | -12.7786 | -47.3752 | 2025-10-24 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| ac277718-7f87-31fc-a7ec-5e59dc6a2ad9 | -24.8231 | -50.2312 | 2025-10-24 12:30:00 | GOES-19 | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 166.6 |
| 283952eb-a468-3ab3-9bd4-64ce0e10112f | -10.8857 | -50.111 | 2025-10-24 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 29d9c821-11a3-3e05-a544-f10e0b323807 | -10.9387 | -50.3835 | 2025-10-24 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 26cb0810-f0b0-3bac-a045-78fd435b8635 | -10.9047 | -50.109 | 2025-10-24 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 4bcc521d-b784-327e-9264-583e22590891 | -13.8958 | -48.3919 | 2025-10-24 12:30:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 76.2 |
| aa6c0b3a-2cb0-3ba2-bf72-5740dfe1b894 | -12.067 | -46.4189 | 2025-10-24 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 2d132c11-57aa-3b64-8d8c-323c53e6636f | -12.7786 | -47.3752 | 2025-10-24 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 7a3122a2-9392-3d59-8642-c83ee3e49cab | -10.9387 | -50.3835 | 2025-10-24 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 714e46a0-07a4-39ae-8111-5c951141709f | -12.067 | -46.4189 | 2025-10-24 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 6bedec95-1933-3bc0-befe-2dba810e1eac | -10.958 | -50.3601 | 2025-10-24 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 53f01b05-1468-3d47-89ec-901ca78e1633 | 1.6569 | -55.7255 | 2025-10-24 12:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| fb944559-0c91-34db-b296-40de79613616 | -12.0862 | -46.4162 | 2025-10-24 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 3e620711-531e-36ab-8a77-886250dddcf8 | -24.8231 | -50.2312 | 2025-10-24 12:40:00 | GOES-19 | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 241.3 |
| 8bdbef19-03a5-3ce6-b4bb-9c7b0d7ae03d | -10.9047 | -50.109 | 2025-10-24 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 40877edd-12cb-34c1-aeba-f728836bbc2f | -24.8016 | -50.2367 | 2025-10-24 12:40:00 | GOES-19 | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 117.3 |
| 4b6f73b6-c56e-3a1c-a576-526f5ace5352 | -24.8238 | -50.2077 | 2025-10-24 12:40:00 | GOES-19 | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 124.5 |
| 0a93287a-4162-3d34-9f24-54fc4c98acc0 | -22.4729 | -51.5855 | 2025-10-24 12:40:00 | GOES-19 | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 110.2 |
| 1c458e77-6cec-3070-956a-8de948bb0ab7 | -22.4723 | -51.6082 | 2025-10-24 12:40:00 | GOES-19 | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 109.6 |
| cf99dbf8-daf7-311e-9b1e-69d42eb19595 | -13.05 | -47.2455 | 2025-10-24 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| eb3f8403-ac02-38bc-8afd-2286ae6a82df | -10.9577 | -50.3815 | 2025-10-24 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 9209ae57-9398-3934-b5e2-e11eeee11ddc | -22.4723 | -51.6082 | 2025-10-24 12:50:00 | GOES-19 | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 129.2 |
| 46592aa4-6bcd-3aa8-b1d1-65ae2f5b970b | -12.0862 | -46.4162 | 2025-10-24 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 07cc7600-59ef-349b-b8f8-7ff2bf66e845 | -13.8958 | -48.3919 | 2025-10-24 12:50:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| a8eb65e0-ed4f-3f1d-be72-96c42f2930fb | -12.0858 | -46.4389 | 2025-10-24 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 374a4019-f39c-3cb9-89b3-82710f752dc4 | -10.8857 | -50.111 | 2025-10-24 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 50dea43c-a138-3bc6-9c3b-41c5281feca8 | -13.9151 | -48.3889 | 2025-10-24 12:50:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 2fc35f52-1366-3e86-bac9-174970678156 | -10.977 | -50.358 | 2025-10-24 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 715fd5d8-e698-3e43-a3c9-7c1362a430f0 | -24.8231 | -50.2312 | 2025-10-24 12:50:00 | GOES-19 | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 176.8 |
| eec73d81-fe69-35b7-92dd-877808acf80b | -10.9044 | -50.1304 | 2025-10-24 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| a1a912c9-816c-37a0-b227-8c78e8b4f7a0 | -12.1696 | -49.4211 | 2025-10-24 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 06da429f-2216-343c-a1e7-5ac2bc431a6f | -10.9047 | -50.109 | 2025-10-24 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 52817dd3-9eaf-3d54-b01a-b2b550713592 | -10.9387 | -50.3835 | 2025-10-24 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 2e376e17-1746-3831-a1f1-0585092d410e | -12.7786 | -47.3752 | 2025-10-24 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| b6c324c2-7570-37a0-97ae-befa3513af68 | -12.067 | -46.4189 | 2025-10-24 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| db28730b-4361-35c5-8ed8-1ea9fb83cf17 | -10.8854 | -50.1325 | 2025-10-24 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| d7d29b46-93d9-3a8f-8dc1-19ebe28799ba | -14.3792 | -51.5255 | 2025-10-24 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 2c88040a-c8ce-3b92-b9ea-3762bd2d2691 | -10.958 | -50.3601 | 2025-10-24 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 3b449d76-9617-34f7-9834-5675818c950f | -22.4729 | -51.5855 | 2025-10-24 12:50:00 | GOES-19 | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 108.0 |
| 8458cbe4-690e-3cbd-b075-5ac679cffdb0 | -12.1696 | -49.4211 | 2025-10-24 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| e506de4e-324f-3884-af1d-7eb0591c56d5 | -12.0674 | -46.3962 | 2025-10-24 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 91c5caff-7644-37d4-b23a-a11865120498 | -22.4729 | -51.5855 | 2025-10-24 13:00:00 | GOES-19 | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 112.4 |
| a953fcba-80fb-3547-a909-765dffbbd83a | -10.9577 | -50.3815 | 2025-10-24 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 8e022558-1d09-354d-a227-406ebcdfb351 | -12.067 | -46.4189 | 2025-10-24 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 5e0d7fb3-5d57-31f4-9995-63cb946e7f73 | -13.8958 | -48.3919 | 2025-10-24 13:00:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| d1bfa40b-493e-313c-bae9-81e020cb427b | -12.0862 | -46.4162 | 2025-10-24 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| adfde1d4-9fbf-3035-a8b9-9513509db623 | -14.3792 | -51.5255 | 2025-10-24 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| a691706a-8d7c-30a6-b588-20a94dd52105 | -12.8328 | -50.9552 | 2025-10-24 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 4a89ac77-4ca7-3078-aa3d-27df4ac65aff | -10.9387 | -50.3835 | 2025-10-24 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 820b8508-31e9-3080-8216-5886a24c6b54 | -13.9151 | -48.3889 | 2025-10-24 13:00:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 91f36c1c-358e-3de0-8253-f7aa875fd722 | -15.1405 | -43.8014 | 2025-10-24 13:00:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 67d49ca3-d5f3-3f6f-8865-9f61055cdc71 | -10.958 | -50.3601 | 2025-10-24 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 976a182a-0908-3a3f-bc4e-f12beb16dac2 | 0.3589 | -50.9414 | 2025-10-24 13:00:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 8c21a4d6-3fcc-345f-9560-34e37d110d2b | -22.4723 | -51.6082 | 2025-10-24 13:00:00 | GOES-19 | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 120.4 |
| 5ced2352-04f5-3e83-9d20-13f09ad7493d | -14.7456 | -46.6096 | 2025-10-24 13:00:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 71.4 |
| c5c9a57e-a988-3d59-b753-313c7dc0c2ab | -10.977 | -50.358 | 2025-10-24 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 5fc0d0de-08be-3454-89a2-a15f4694e316 | -10.9047 | -50.109 | 2025-10-24 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 184f60a2-3df6-38a7-b8c2-e7f89ce880b1 | -10.8857 | -50.111 | 2025-10-24 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 0d28c7b7-2f61-3751-88f9-0e1e47051abc | -11.0222 | -49.8383 | 2025-10-24 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 164fe25e-556c-3e3f-8e70-50ab8234d40c | -12.7786 | -47.3752 | 2025-10-24 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 38950274-c3e3-394c-b736-9db455936144 | -22.4723 | -51.6082 | 2025-10-24 13:10:00 | GOES-19 | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 115.6 |
| 06d99caa-c74e-3ea2-8d14-a19021f74f8d | -13.8958 | -48.3919 | 2025-10-24 13:10:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 69.6 |
| c3fe1141-2f99-383b-8c0d-05bb06fadb00 | -10.9044 | -50.1304 | 2025-10-24 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| d0e55252-4b16-355c-8f57-bf2043850454 | -22.4729 | -51.5855 | 2025-10-24 13:10:00 | GOES-19 | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.3 |
| e97daf3f-0fc3-3f21-9a16-28f77dd4ae38 | -12.067 | -46.4189 | 2025-10-24 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 1228a075-9d64-38b6-8f34-94890f86c7ba | -11.0219 | -49.8598 | 2025-10-24 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 35dcbbfe-d486-30d6-a49f-49563945f1de | -17.3353 | -55.0156 | 2025-10-24 13:10:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 66.3 |
| 01d98ae6-06df-3843-b5cb-93c257f6b798 | -12.1696 | -49.4211 | 2025-10-24 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 3b3a2f9c-5cbc-3446-b92d-e7201a1269c0 | -14.2727 | -52.1152 | 2025-10-24 13:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 828d36d3-4cfb-3830-b672-e5d90360e905 | -10.8857 | -50.111 | 2025-10-24 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 6d8a83f4-ac28-3649-8fc8-98712b5f3bd0 | -12.7786 | -47.3752 | 2025-10-24 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 0c8ea97c-acc3-36e8-826c-de50a834613c | -11.1583 | -49.6073 | 2025-10-24 13:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 739e0a37-a852-369d-8f78-860ad3ac7a73 | -10.9047 | -50.109 | 2025-10-24 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 635b016b-cec9-3c15-9ec7-e877f5699889 | -14.3792 | -51.5255 | 2025-10-24 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 77b04f68-e538-3897-8a3a-26e47d87075d | -10.8854 | -50.1325 | 2025-10-24 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| f93319b3-1ea5-3a87-9a9c-4c360ee632fe | -11.0222 | -49.8383 | 2025-10-24 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 135.7 |
| c06be6ab-3380-3634-a70c-ba6aa0547321 | -12.2781 | -47.4908 | 2025-10-24 13:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 03d3d777-52dd-336c-acd9-a1fd0264f207 | -12.0862 | -46.4162 | 2025-10-24 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 59aa8cdb-7f38-31a5-9038-6fe833ea6f73 | -12.0674 | -46.3962 | 2025-10-24 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 2148887f-d7a7-35bb-82f9-fac56997dc49 | -3.3926 | -44.401 | 2025-10-24 13:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 63ced7b8-3844-3f19-a695-4ed12ee5cab3 | -10.9047 | -50.109 | 2025-10-24 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| a2cb19c5-317c-30bf-9a48-c3aedaa783f3 | -22.4729 | -51.5855 | 2025-10-24 13:20:00 | GOES-19 | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 144.3 |
| eef12953-6b42-313e-8d36-e6aa681716da | -12.0674 | -46.3962 | 2025-10-24 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| ad84d60b-22c3-3e71-b807-29bc869e4930 | -13.8958 | -48.3919 | 2025-10-24 13:20:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 73.4 |
| a1ea29af-0f23-3444-bf67-2849353ca6a9 | -12.02 | -46.9219 | 2025-10-24 13:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| f79d6b8b-89fb-3531-90a9-03e21d9ff302 | -19.0319 | -57.5382 | 2025-10-24 13:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 56.9 |


[Clique aqui para ver as próximas entradas](README60.md)
