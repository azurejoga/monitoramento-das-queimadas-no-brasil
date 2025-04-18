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
| 42179b91-701b-32eb-ba30-a7eb018080a2 | -21.2368 | -48.5954 | 2025-04-18 00:00:00 | GOES-19 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.0 |
| 16705575-1a7c-332c-9ef5-d66d4e88d863 | 1.9959 | -60.8748 | 2025-04-18 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 88d2baeb-7dad-3455-86ce-94cae41c74d2 | -21.2161 | -48.6002 | 2025-04-18 00:00:00 | GOES-19 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.7 |
| bfca2cef-6fbe-3117-8011-7e903bf34a8a | -21.2361 | -48.6187 | 2025-04-18 00:00:00 | GOES-19 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.1 |
| 50d8e8ec-d16f-368e-a7bb-23b98895dd90 | -21.2155 | -48.6235 | 2025-04-18 00:00:00 | GOES-19 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 108.6 |
| fc3a2a09-4cbc-3c66-9d27-6c647d0e6d8b | -6.54674 | -44.4803 | 2025-04-18 00:09:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 945354e3-601a-319b-b363-96d490e793ea | -5.42424 | -43.2018 | 2025-04-18 00:09:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 86ff7acb-5337-3543-9910-c22fb3c6d8da | -5.48189 | -43.33017 | 2025-04-18 00:09:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| e731220e-b817-3eed-8f29-f37dee96eac6 | -11.27274 | -40.73599 | 2025-04-18 00:09:00 | TERRA_M-M | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| e72b39a7-0640-3cd2-bfdd-9fc06faa9020 | -9.61153 | -37.02877 | 2025-04-18 00:09:00 | TERRA_M-M | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 5f80cea5-21a2-3d04-bdb1-96a952661633 | -7.08494 | -44.38799 | 2025-04-18 00:09:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 8b57e657-32b3-3ab2-a679-ebff13890e16 | -7.0831 | -44.3742 | 2025-04-18 00:09:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 490b58d8-2651-3418-9134-0d0cbfaaaa41 | -6.95623 | -43.0501 | 2025-04-18 00:09:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 2f33f2f0-8915-373d-b95f-24349f176fe2 | -5.1633 | -45.10749 | 2025-04-18 00:09:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 6e5d3ac9-8e20-3410-abf1-b25376c1edad | -5.21038 | -39.50264 | 2025-04-18 00:09:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 2df63b71-9118-3e91-9f18-1441b015e431 | -6.54859 | -44.47444 | 2025-04-18 00:09:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 2faf5c8a-b0de-35f7-a903-d9cb73da17d2 | -7.0866 | -44.38208 | 2025-04-18 00:09:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| cc4ac184-0a5e-3a84-a502-d352eebaa78c | -7.07213 | -44.37551 | 2025-04-18 00:09:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 2762ea65-7c9c-3185-bf14-1778a9c748a1 | -5.16404 | -45.1131 | 2025-04-18 00:09:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 859cb13f-5962-3dbf-8197-46dd782a6b7b | -9.61304 | -37.03907 | 2025-04-18 00:09:00 | TERRA_M-M | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 26.2 |
| 7d2948aa-015d-3151-890b-3212ec76be51 | -5.64513 | -43.70816 | 2025-04-18 00:09:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 1a52527c-25d3-326b-bdf9-97e0a0512306 | -6.95473 | -43.0388 | 2025-04-18 00:09:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.9 |
| 213f2337-8ca5-3f2c-b376-a5ddb9f7cd2f | -9.6225 | -37.03759 | 2025-04-18 00:09:00 | TERRA_M-M | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 6e78424d-74e3-3b96-9db8-a07790c9b08c | -6.94481 | -43.04012 | 2025-04-18 00:09:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 01385851-6576-3435-bca8-4ce22d1f34db | -5.78759 | -43.62254 | 2025-04-18 00:09:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 79bad820-a0d7-32e4-9d38-d58b4caf7c53 | -5.79591 | -43.61519 | 2025-04-18 00:09:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cf7e1e8b-9218-315d-8723-76bb31090652 | -5.48375 | -43.33566 | 2025-04-18 00:09:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| ec0e0f91-fa65-3a9f-8883-243beb763361 | -5.6467 | -43.7201 | 2025-04-18 00:09:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c3fe9303-ff51-3644-aea7-884388cfb015 | -8.14086 | -41.18614 | 2025-04-18 00:09:00 | TERRA_M-M | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| c0dada55-5e83-330d-b97b-2a1d52061fef | -21.2155 | -48.6235 | 2025-04-18 00:10:00 | GOES-19 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.5 |
| fd1769ac-d6b3-38c8-bef9-59cf1e2fb54d | 1.9777 | -60.8561 | 2025-04-18 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 72252ecc-cf71-3eb2-9da4-7b01447affa7 | -21.2361 | -48.6187 | 2025-04-18 00:10:00 | GOES-19 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.4 |
| 5acf6090-255b-33fb-af4f-c4af75a941fa | 1.9959 | -60.8559 | 2025-04-18 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 79.0 |
| f6ca0e42-870e-35a4-ac48-0be3810696b0 | 1.9959 | -60.8748 | 2025-04-18 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 133.9 |
| e30cfbb2-c74a-31d8-ab42-df3cb011e79d | -21.2161 | -48.6002 | 2025-04-18 00:10:00 | GOES-19 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.1 |
| 904fc64f-7309-3232-a4dd-a4ff8bc9679b | 1.9776 | -60.875 | 2025-04-18 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 744b9e76-a2c1-3eba-bf36-1bc8686bc70f | 1.9958 | -60.8937 | 2025-04-18 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.8 |
| f679468c-50bb-3f5d-a3a0-f121f416dbc4 | -3.44541 | -43.67442 | 2025-04-18 00:11:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 478175e0-2939-3093-9ca4-ff0ee5b77756 | -3.44391 | -43.66338 | 2025-04-18 00:11:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 79150da8-ec58-3c3e-8b4c-e0b6d734a27e | -21.2155 | -48.6235 | 2025-04-18 00:20:00 | GOES-19 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.7 |
| 02a8a4f0-48af-35df-be60-cd24692e7ace | -21.2155 | -48.6235 | 2025-04-18 00:30:00 | GOES-19 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.4 |
| 05cf9441-e591-33c0-849d-c1cc0cf556ec | -21.2361 | -48.6187 | 2025-04-18 00:30:00 | GOES-19 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.8 |
| c19588cf-9780-3189-9a7a-56f9a44da68e | -7.0644 | -44.380402 | 2025-04-18 00:30:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5cc5ee8d-72a1-3cdd-96cc-0f7406d09bc4 | -6.9383 | -43.056198 | 2025-04-18 00:30:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0ba0fedc-3135-3e3d-8534-138bdd19eff1 | -21.218399 | -48.618198 | 2025-04-18 00:30:00 | METOP-B | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 42d62b76-2623-39de-b3e2-1eada3fb0517 | -5.41 | -43.187801 | 2025-04-18 00:30:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c2f1b01f-3cf7-3e19-b1f7-8b413e262409 | -21.2169 | -48.610802 | 2025-04-18 00:30:00 | METOP-B | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 71d1a40e-7399-3567-a37c-fa9ded16a7a5 | -6.9438 | -43.036598 | 2025-04-18 00:30:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2c9d1067-d7fb-3faa-8814-5b510685cef0 | -5.151 | -45.110298 | 2025-04-18 00:30:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 37ddea06-eebb-3b46-a5aa-f57ed3740ea3 | -5.1479 | -45.097 | 2025-04-18 00:30:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ca158fe8-4392-3646-8e0d-1f1a4a0b9f57 | -5.768 | -43.6082 | 2025-04-18 00:30:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd3e9054-ea83-3bde-bac7-eddaa8573c49 | -21.2153 | -48.603401 | 2025-04-18 00:30:00 | METOP-B | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ad6e68ce-86f4-3af2-8411-406d2dcb8500 | -5.7817 | -43.622299 | 2025-04-18 00:30:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28f9595f-4fcf-3619-8df2-c59968707064 | -6.5327 | -44.479301 | 2025-04-18 00:30:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eca5680c-1e65-3005-8df1-063ef829b8b3 | -21.2071 | -48.613201 | 2025-04-18 00:30:00 | METOP-B | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 044f3b5c-0962-3e71-958a-a848507e566e | -6.9341 | -43.039001 | 2025-04-18 00:30:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6013abad-9b94-3f1b-aea1-a35d6ec2f8d4 | -6.9298 | -43.021702 | 2025-04-18 00:30:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e841ddf0-534e-3580-8568-52ff1e1d6bd6 | -6.5293 | -44.465401 | 2025-04-18 00:30:00 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2b7ab3c-849b-3d31-aef1-c9740a6fc4e4 | -5.772 | -43.624599 | 2025-04-18 00:30:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f01a731-0951-3b9e-a734-746452e4cb7a | -7.0611 | -44.366501 | 2025-04-18 00:30:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0ce58ae-a5d2-3b33-b22c-c4fb3dd3854d | -9.9158 | -59.902901 | 2025-04-18 01:21:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5ba7c35e-fd23-3d82-b497-1d8b6f878f3a | -6.5708 | -51.115601 | 2025-04-18 01:21:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7ada871-1443-34ff-a18e-9cedee680a9c | -9.93001 | -59.90635 | 2025-04-18 01:47:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 559b47aa-3c70-39e9-a813-cdaee5497a87 | 1.9959 | -60.8748 | 2025-04-18 02:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 22121097-90d5-3114-a49e-b8c27c8e3998 | -9.61349 | -37.03412 | 2025-04-18 02:51:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3fdb4bc0-6eae-3ad4-84d8-6477a80f6573 | -9.61624 | -37.03427 | 2025-04-18 02:51:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 05ae8f91-96fa-322f-9f7e-5b2bf9714ab3 | -9.61488 | -37.0411 | 2025-04-18 02:51:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e5cfa5c7-d161-329f-9601-92c4f7f74510 | -9.62047 | -37.03577 | 2025-04-18 02:51:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 2edcfa29-5d68-3059-8176-1f5b22a0d5eb | -9.61497 | -37.0338 | 2025-04-18 03:17:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6cc94831-4a70-3e4e-acab-7f80549faf06 | -9.62 | -37.03345 | 2025-04-18 03:17:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7743483d-6615-3f0e-86a8-fe4787d52158 | -6.95252 | -43.03701 | 2025-04-18 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ef4774c9-46a1-3e9d-92d1-d066e0d3bd91 | -6.95108 | -43.04454 | 2025-04-18 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a9aee432-b896-3506-8ece-7854024e9470 | -6.94536 | -43.03538 | 2025-04-18 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 33f5c289-11de-3d5f-b965-c7bc12c89c44 | -9.6191 | -37.03854 | 2025-04-18 03:17:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.5 |
| dc6c61a7-6a7d-315c-877e-500fbb41e395 | -9.85196 | -37.18804 | 2025-04-18 03:17:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c75e501e-48ee-3032-8c57-f1319c6c009a | -6.94392 | -43.04291 | 2025-04-18 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f3a81829-d383-32af-b7f2-3667220b6f2b | -9.6197 | -37.03476 | 2025-04-18 03:17:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a4b101af-3968-3b80-ba6b-d49e9d2f5f63 | -8.07433 | -34.9764 | 2025-04-18 03:17:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 94bb646c-1b4f-3453-82d7-ceae8acf0e90 | -6.95969 | -43.03858 | 2025-04-18 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45f3a598-0ab5-38a5-8a7a-6be08779baea | -8.14481 | -34.97266 | 2025-04-18 03:17:00 | NPP-375D | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 50614f48-b3c4-3c76-8e87-14a5f056a7cd | -9.61527 | -37.03247 | 2025-04-18 03:17:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a049a041-0a46-3b2e-9ce5-2d0325287c3e | -9.60964 | -37.03662 | 2025-04-18 03:17:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f98733bd-b199-3b51-bb77-0373dd48d7f4 | -9.84716 | -37.18729 | 2025-04-18 03:17:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b7e1feb7-b6f7-339e-8261-ef6b27293d67 | -19.20012 | -40.10443 | 2025-04-18 03:21:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4fbebb84-46a9-3496-9026-aa80c05288a0 | -21.62679 | -43.46534 | 2025-04-18 03:21:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d31f856b-f9b3-3a02-8fb9-7b0160ec01e5 | -21.62582 | -43.4695 | 2025-04-18 03:21:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 27f5b550-6f0c-3ff3-b084-eca1e7e52a11 | -5.15627 | -45.10884 | 2025-04-18 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 27ecc346-930d-39ec-8e7f-22c84344fd7d | -7.0695 | -44.38331 | 2025-04-18 03:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27ee98eb-2653-3fc9-8c53-a0bdc98d9135 | -7.07596 | -44.37789 | 2025-04-18 03:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e267fbf-f8a0-383e-a23b-942ce766a443 | -5.42718 | -43.20074 | 2025-04-18 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34e2a8bf-42c2-3d17-864e-5eefbe74e2c6 | -9.60814 | -37.03475 | 2025-04-18 03:40:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 679365ea-b4a0-316e-8e06-e4a0af352f84 | -6.9477 | -43.04764 | 2025-04-18 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46bb9bbc-1d33-3212-8d6b-c34b68343c6b | -5.6449 | -43.71143 | 2025-04-18 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10ed4c96-fd0b-3049-b1bb-c49a385a3376 | -7.07653 | -44.3747 | 2025-04-18 03:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7cf099cc-bfab-39f9-8040-e075804ffe01 | -9.61543 | -37.03227 | 2025-04-18 03:40:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ad016dce-ecc2-30d7-98d5-0d832cc3d262 | -5.78503 | -43.62331 | 2025-04-18 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6f8cd38e-89a2-3551-8d16-ec9977d81385 | -6.57859 | -47.53703 | 2025-04-18 03:40:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 517caf58-b67e-3838-ac32-09e56c4781d4 | -7.08068 | -44.38218 | 2025-04-18 03:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 14cb3b9e-71cd-39c9-8c23-b1f3a458a808 | -5.65012 | -43.71227 | 2025-04-18 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b4e7cbb-e521-34d8-aa5c-431d309e3d00 | -7.07711 | -44.3715 | 2025-04-18 03:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README2.md)
