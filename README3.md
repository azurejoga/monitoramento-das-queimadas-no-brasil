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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51f464f7-45f2-33fb-80ca-88c32cb9aacf | -27.68909 | -48.75146 | 2025-02-08 04:31:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d8dbc6e7-c101-38cd-ad2f-18934a00e905 | -30.94161 | -53.34081 | 2025-02-08 04:33:00 | NOAA-21 | SANTANA DA BOA VISTA | RIO GRANDE DO SUL | Brasil | 4317004 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 4816f1f5-ebdc-3508-880d-ca049276e355 | -32.66806 | -52.44397 | 2025-02-08 04:33:00 | NOAA-21 | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| bfbf67c3-5705-3548-838a-5a3ddd2bb8dd | -12.354 | -52.47833 | 2025-02-08 04:53:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28422582-f6e6-3781-ad7e-ee097879eb44 | -7.94934 | -49.76239 | 2025-02-08 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eab02e01-b993-36b1-a8fa-1c231578b434 | -13.62965 | -55.45274 | 2025-02-08 04:53:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5280210f-4ba8-38d1-8ab2-e9ef58bfbbf0 | -14.25325 | -48.1274 | 2025-02-08 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60502dca-0316-37db-b56d-a5e0efaaf643 | -14.25382 | -48.1231 | 2025-02-08 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6316c33-b885-31eb-a847-6a12f4f9d056 | -13.61958 | -55.45103 | 2025-02-08 04:53:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 692fcbe9-71c1-38e7-a397-d1b6682f3956 | -12.35002 | -52.48151 | 2025-02-08 04:53:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c5cf6b4-0957-3170-8da4-4a0f9b82565a | -7.89558 | -43.91571 | 2025-02-08 04:53:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f76a7ae5-7ce4-3ce9-bdc8-f146df0cb02f | -7.953 | -49.76297 | 2025-02-08 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bd50baec-a054-3592-9bbf-c6a3abb2e0ab | -13.62688 | -55.44854 | 2025-02-08 04:53:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb9ca400-97e8-3b5a-b7d3-12215e4ef4df | -13.52561 | -47.54143 | 2025-02-08 04:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2372abd7-b5ed-3b1c-9f2e-8d0a067ed39d | -13.619 | -55.45467 | 2025-02-08 04:53:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b209ef4f-578e-37a0-b10d-6a92d927ee36 | -7.98136 | -50.7045 | 2025-02-08 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2c1e2b9-b93a-3b14-91d3-55072b358348 | -12.35343 | -52.48205 | 2025-02-08 04:53:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0f55055-1466-3fb7-8804-38e509cab630 | -7.98076 | -50.70839 | 2025-02-08 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5570bca7-f933-3781-9b37-aa5caacd12df | -7.94997 | -49.75809 | 2025-02-08 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8176c75f-11de-30b1-b00e-a0ffd943f991 | -7.95363 | -49.75866 | 2025-02-08 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25b052d2-1375-3296-87a0-9a436f9c2860 | -2.80288 | -53.98837 | 2025-02-08 04:53:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e8c1c87-1bc8-3a25-aae5-8d55ec8b053a | -2.80633 | -53.98892 | 2025-02-08 04:53:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c772f7d8-1a72-32d5-8eaf-ca4c1691a11b | -13.62294 | -55.4516 | 2025-02-08 04:53:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 23e39e76-e166-3401-858a-d69f052da640 | -13.62235 | -55.45523 | 2025-02-08 04:53:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d474bc16-72c9-3937-86a1-cbfd738bb7fd | -13.62629 | -55.45218 | 2025-02-08 04:53:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1444954b-9613-34f5-bef9-9d54923b472e | -3.19572 | -52.44384 | 2025-02-08 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a7e1ede-b575-32ee-9897-b76880397285 | -7.98486 | -50.70503 | 2025-02-08 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9451599e-b19b-34ad-a7a3-0dddbb075c41 | -12.35059 | -52.47779 | 2025-02-08 04:53:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1236e04-8ba5-3265-8b3f-14383e4e3ca9 | -11.57609 | -47.62444 | 2025-02-08 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 86f8a6ec-a4cd-38b9-8d15-3fc093351ea6 | -12.7483 | -44.83777 | 2025-02-08 04:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 931b5c11-5551-321d-a9ed-63daef5a2ca3 | -16.36221 | -57.72157 | 2025-02-08 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4167afb2-7417-3bcd-833b-1711f618a171 | -11.74249 | -48.73077 | 2025-02-08 04:55:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c212a95f-0d21-3063-bf8a-38b62d6eaec1 | -11.74471 | -48.73776 | 2025-02-08 04:55:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7689babd-b45b-3cc6-8af2-5a1aca68dd28 | -21.89353 | -53.71978 | 2025-02-08 04:55:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f8c2e523-fd52-3803-b859-069516b9204c | -12.53378 | -48.3293 | 2025-02-08 04:55:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c5b68e9-1a2c-3704-83a7-c9e46713b3bf | -11.88383 | -46.94101 | 2025-02-08 04:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb0ab9de-33ae-34fe-a3cd-6ff5e068d3ff | -10.68939 | -54.34569 | 2025-02-08 04:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86a5814a-1217-3eef-a7c5-60c860bb622b | -11.5777 | -47.61801 | 2025-02-08 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47514ca1-9484-3671-9c45-37e49d549949 | -11.40334 | -52.94729 | 2025-02-08 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aabefc68-89ef-3db6-a75b-101e627efa35 | -11.5733 | -47.61741 | 2025-02-08 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| febce44f-a10f-3521-baeb-c171555e61ad | -11.40614 | -52.95139 | 2025-02-08 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89f0e969-19b0-358a-a757-53ad1169876e | -11.57666 | -47.62009 | 2025-02-08 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 39ac6261-aaa7-365f-a16d-e86a9c146cb6 | -20.76292 | -46.76839 | 2025-02-08 04:55:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2dd2f165-0d57-3332-baaf-7ae3ced3d345 | -20.16385 | -46.67958 | 2025-02-08 04:55:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a407499f-9cdf-35ac-94d5-72a04d8788d7 | -16.46598 | -58.1666 | 2025-02-08 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 931ce6d6-7137-37aa-925a-6cd4049abdd7 | -11.74197 | -48.73442 | 2025-02-08 04:55:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61594eec-2e8a-38b2-a9b8-20a0ac6df313 | -11.57226 | -47.61949 | 2025-02-08 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0838beb2-984f-38f1-bf24-0d5d70945ed0 | -12.74787 | -44.84123 | 2025-02-08 04:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af7dba38-b0f0-3294-a9c4-133697d0966b | -20.1698 | -46.67376 | 2025-02-08 04:55:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8f548b81-eca3-3585-92b2-dd6556d2e2ea | -11.74521 | -48.7341 | 2025-02-08 04:55:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f6e0103-d361-3511-9b8c-3b9d18a593f0 | -12.53434 | -48.32528 | 2025-02-08 04:55:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ecdfec9-fd3e-3fb3-965b-ae8680477f63 | -20.15861 | -46.6787 | 2025-02-08 04:55:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8451aa8-270a-3eb5-bfa0-29115f9f5d00 | -11.74062 | -48.73716 | 2025-02-08 04:55:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 447b0360-6586-32f4-8f95-df7f765629b9 | -10.28107 | -52.83372 | 2025-02-08 04:55:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f10cbfd3-1417-3388-8f4c-c9f90ad8f4e1 | -11.74111 | -48.7335 | 2025-02-08 04:55:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 545fdc02-e774-3243-ae8c-fc99bc08f59d | -12.41536 | -43.80548 | 2025-02-08 04:55:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34fd2d49-6869-38a1-88f7-4c7fd873839e | -10.28441 | -52.83425 | 2025-02-08 04:55:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9d40d62c-37d3-390e-b54a-3b08ec5925e9 | -20.16456 | -46.67284 | 2025-02-08 04:55:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6bef7310-770a-3216-8d60-bbf17a8157e9 | -11.57269 | -47.62172 | 2025-02-08 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c94bff30-44f6-3796-b52e-9d41d0da0695 | -11.40279 | -52.95087 | 2025-02-08 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 548608fc-d137-3b37-9ad6-59f649983c50 | -21.07751 | -56.39361 | 2025-02-08 04:55:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f663b9d4-d612-341d-90ca-a29be4e38b58 | -11.88118 | -46.93921 | 2025-02-08 04:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65dd842e-38c0-32b0-aece-6b29d973ef39 | -20.16421 | -46.67619 | 2025-02-08 04:55:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 84aa6f29-3d29-3d5a-b598-f4d11a2a6617 | -21.88941 | -53.72338 | 2025-02-08 04:55:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed247e60-f44a-3fa3-8485-fae43f276629 | -18.67853 | -47.50811 | 2025-02-08 04:55:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b766d55-8998-37d9-af18-bda1ef71fcc0 | -16.614 | -57.64391 | 2025-02-08 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 184c460c-0947-33ef-bd8e-1912a3e35f27 | -11.73736 | -48.73748 | 2025-02-08 04:55:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4d9a7f7-c3bf-3992-9739-c6cbf95305b9 | -11.10569 | -54.49335 | 2025-02-08 04:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d43962c2-a091-3859-b30c-4a22ebfa38f4 | -11.74145 | -48.73808 | 2025-02-08 04:55:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63d5051f-2e53-3510-bf97-c2e63eb9223f | -20.15897 | -46.67529 | 2025-02-08 04:55:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 365c5ee0-f05e-339b-ae51-8e65309d4447 | -21.89293 | -53.72397 | 2025-02-08 04:55:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05fe608e-5183-37c5-bf02-56c449789d09 | -20.16944 | -46.67714 | 2025-02-08 04:55:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a313390e-019f-3ce4-88ae-e23c4342616c | -16.46239 | -58.16595 | 2025-02-08 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3bef235f-2765-3983-bcfc-a1ba4dd96147 | -11.5771 | -47.62232 | 2025-02-08 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 939ef3c2-8680-3ae8-ab55-3a92d55dda32 | -10.27717 | -52.83675 | 2025-02-08 04:55:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7d4892f0-224c-3a23-b1d1-f8db7cb9a9ec | -16.61819 | -57.64052 | 2025-02-08 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 1a57c59d-8cf4-37a3-8fb3-9e8e01d28cd5 | -20.16348 | -46.68309 | 2025-02-08 04:55:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ce3c21b8-a0b0-3200-baa4-38492ce1f57b | -11.44132 | -52.92393 | 2025-02-08 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 482fb8a9-fde5-3ffa-98ee-2864d2c219f9 | -11.20247 | -55.53323 | 2025-02-08 04:55:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5cc2854-6a09-3368-82dc-d231b07e5fc1 | -29.74439 | -50.33174 | 2025-02-08 04:57:00 | NPP-375D | CARAÁ | RIO GRANDE DO SUL | Brasil | 4304713 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 03b7c65c-94d8-387a-a104-2907b92b9c96 | -20.1637 | -46.67115 | 2025-02-08 05:08:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 243ef8ea-1660-3e9f-a74e-037875905d12 | 3.89745 | -60.18386 | 2025-02-08 05:12:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a96a85e7-f220-399e-b7bc-a1404a6ba25d | 3.89444 | -60.18877 | 2025-02-08 05:12:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8794f3da-159d-34e2-8286-035f04aa447d | 4.29611 | -60.10155 | 2025-02-08 05:12:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 425d4bcc-df28-301e-be2e-ebc281b8cc61 | 2.99444 | -60.61013 | 2025-02-08 05:12:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 466e98b7-446c-3b05-94a1-21a25ebda1aa | 3.60582 | -60.28065 | 2025-02-08 05:12:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ed27cf2-edd1-3771-8922-ce1bf4e5ed55 | 3.89811 | -60.18819 | 2025-02-08 05:12:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2fb5ab2d-7027-3b98-8586-cc856d74b46c | -7.95315 | -49.76479 | 2025-02-08 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 256e9c98-d214-315a-8c8a-15762a3ee088 | -12.35154 | -52.48293 | 2025-02-08 05:16:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acf16ba8-42f1-3162-88ba-ef79538fc54e | -11.1048 | -54.49527 | 2025-02-08 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 961bb66d-804f-343f-bfb3-dd6bf5aa42c9 | -10.27788 | -52.83602 | 2025-02-08 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20eccaec-a7bc-305e-bbd3-26c58d2c5c57 | -7.94767 | -49.7639 | 2025-02-08 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d53308c8-f97a-3b37-aa48-d5aaf6e58244 | -12.35226 | -52.47746 | 2025-02-08 05:16:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce969f75-057a-30d6-980d-c21790a1d55e | -12.35033 | -52.47922 | 2025-02-08 05:16:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2af4946-c5bf-3fc2-bed0-87826370d9a1 | -7.94815 | -49.76032 | 2025-02-08 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 059a211e-d118-3ebb-a1c4-5d8f6e52209f | -10.28249 | -52.83666 | 2025-02-08 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d60bd05-fda0-3fc4-a3b1-416801f70f03 | -7.95363 | -49.7612 | 2025-02-08 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52d7dbbd-14be-314e-b525-c5081882f81e | -16.36173 | -57.72063 | 2025-02-08 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d82ee60b-e2e2-3449-bfe1-fb4fc498fae0 | -16.61511 | -57.64409 | 2025-02-08 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 804e2911-5bb3-3f7a-b65e-8e71748435d3 | -19.90432 | -56.42422 | 2025-02-08 05:20:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |


[Clique aqui para ver as próximas entradas](README4.md)
