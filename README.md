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
| f06c056c-983d-3bd2-9bfd-701338a2f30a | -13.2972 | -54.3655 | 2025-03-18 00:20:00 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| adf6d40d-60b4-3c60-a27b-0503d1589493 | -15.6844 | -41.578098 | 2025-03-18 00:24:00 | METOP-C | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| de363652-b197-3994-b21a-e951a74d0978 | -12.0808 | -45.627701 | 2025-03-18 00:24:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 240386b5-9d19-3f14-ae08-4398a5847850 | -17.627001 | -46.641998 | 2025-03-18 00:24:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fb9ba385-9ddf-3b7d-aafc-26307637f590 | -9.4827 | -40.351299 | 2025-03-18 00:24:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 82ba42ab-7f06-34dd-9d10-859f173c6d9a | -12.0843 | -45.643799 | 2025-03-18 00:24:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 48d7f8ad-4853-30fe-87a2-314d2197e790 | -17.6248 | -46.631199 | 2025-03-18 00:24:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ae6364de-0023-3223-abe1-f28f555df5c7 | -15.9503 | -40.3479 | 2025-03-18 00:24:00 | METOP-C | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 383d5458-3338-30f5-b285-4efe2ccf0395 | -11.4246 | -41.408798 | 2025-03-18 00:24:00 | METOP-C | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 19b9e0d3-f7bc-3b09-b246-0caac7395361 | -18.235701 | -42.355202 | 2025-03-18 00:24:00 | METOP-C | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2b078c21-2a96-3e44-8b30-e84b9a0e66a6 | -16.3414 | -47.5546 | 2025-03-18 00:24:00 | METOP-C | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f0b1c2c6-cfe0-373f-9ed3-e1335c17293d | -15.9486 | -40.3405 | 2025-03-18 00:24:00 | METOP-C | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b94f8c15-6294-3ee3-ab21-b920d802ea17 | -16.3438 | -47.566399 | 2025-03-18 00:24:00 | METOP-C | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5a733de3-f83b-379e-bbc2-674a449e889a | -17.121901 | -39.652699 | 2025-03-18 00:24:00 | METOP-C | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| de51a9e9-5aca-36f9-bd02-93822c5fca20 | -12.9002 | -45.049 | 2025-03-18 00:24:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e609f338-b5ad-33fa-b219-69a48c0875fe | -17.687901 | -39.864498 | 2025-03-18 00:24:00 | METOP-C | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d831b0fe-bd52-3bae-9cef-48c40723ed6b | -12.0825 | -45.6357 | 2025-03-18 00:24:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f97f6ee5-5206-3bbf-879a-4d24e1fee253 | -12.1772 | -39.903599 | 2025-03-18 00:24:00 | METOP-C | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c32cd653-2c91-39df-8761-9a9862c407a6 | -9.4925 | -40.348999 | 2025-03-18 00:24:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f1cc337e-714a-3df0-a71f-332ca38a666c | -16.644899 | -44.037399 | 2025-03-18 00:24:00 | METOP-C | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c9c28d8e-a9f0-3e6c-ae73-1c16d3b38430 | -18.063 | -43.032902 | 2025-03-18 00:24:00 | METOP-C | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cf59ea5a-789e-3cae-8dba-4d181df2ea41 | -13.6849 | -43.001598 | 2025-03-18 00:24:00 | METOP-C | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1ec54877-ed45-3390-a3dc-120607886ef5 | -12.8503 | -43.833401 | 2025-03-18 00:24:00 | METOP-C | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d04e6d5-e7ed-3fc6-82d7-f52fff91159e | -16.29027 | -55.44107 | 2025-03-18 00:58:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 63632f2c-d2bd-3119-83dc-663d81b3b13e | -12.0836 | -45.6364 | 2025-03-18 00:58:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d2d39894-a217-3bb3-8af5-85c0e04b2438 | -16.33382 | -47.56231 | 2025-03-18 00:58:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 49c5c91a-7f19-36f5-ad27-b5a07b202829 | -1.66367 | -55.58348 | 2025-03-18 01:02:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f1e2e90b-8ca9-3eaa-9745-3e06befe7eaf | -20.4555 | -56.554699 | 2025-03-18 01:11:00 | METOP-B | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4cc1e333-6aae-3586-834a-dcb0deb2c33f | -13.3002 | -54.362099 | 2025-03-18 01:11:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f97b47b6-5acb-3371-8e31-132c9c0f6f96 | -20.4538 | -56.5471 | 2025-03-18 01:11:00 | METOP-B | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8b32f40e-e233-34cc-a979-eee4dacdd9c9 | -17.775999 | -56.307499 | 2025-03-18 01:11:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5ef9c6ff-82c0-3192-a978-42a1ae30e17d | -13.2972 | -54.3655 | 2025-03-18 02:00:00 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 1304a3ef-deed-314b-852a-4d75133839f7 | -12.8785 | -58.744801 | 2025-03-18 02:03:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1bc39bca-9c07-3910-9483-a0faf12d9eb4 | -13.2972 | -54.3655 | 2025-03-18 02:20:00 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 0ca1ade2-0031-369e-a15a-e928cb4aba09 | -13.2972 | -54.3655 | 2025-03-18 03:20:00 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 3740fea5-dfe5-3238-b9d6-80628be39530 | -12.84548 | -43.83641 | 2025-03-18 03:21:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9fce7a92-5efc-3988-867f-841b5f73ab61 | -11.18873 | -40.5616 | 2025-03-18 03:21:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b9766e63-47e5-3901-92fc-9d397714df7c | -8.39084 | -35.02485 | 2025-03-18 03:21:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a73e350f-5ab3-3fcc-99cb-a1925ca9109f | -11.1884 | -40.56006 | 2025-03-18 03:21:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ff5ca858-8237-31da-acb8-1cf3e38fe0bc | -11.18351 | -40.56043 | 2025-03-18 03:21:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6e6a4f7b-fcae-39ab-bca2-61e6de4850cc | -12.1656 | -39.908 | 2025-03-18 03:21:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ea9cbba3-463e-3fcd-9630-3c839bddfc1e | -11.18934 | -40.55831 | 2025-03-18 03:21:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 21919c65-f708-382e-b293-f5aca76932f6 | -12.84653 | -43.83134 | 2025-03-18 03:21:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b7b5df4-a030-3be4-9fc4-94947f666bbd | -10.69484 | -37.04837 | 2025-03-18 03:21:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1bb6b3db-2421-30a8-a738-aa2be6bed956 | -12.0728 | -45.63504 | 2025-03-18 03:21:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82a9e23b-1b3a-366a-bcad-e5e1bf0dde54 | -12.07425 | -45.62818 | 2025-03-18 03:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12e00f2a-e1c0-39fb-89ae-2e6f707a0600 | -16.63276 | -44.03808 | 2025-03-18 03:23:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9f64f7a-5eb1-3147-9158-ca420206ea90 | -13.67906 | -42.99906 | 2025-03-18 03:23:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fb4e0b5b-c71d-3872-93f4-a04126458d55 | -13.67819 | -43.0033 | 2025-03-18 03:23:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 657a58db-5a78-3757-b191-6ff9b4b9169c | -15.94262 | -40.3417 | 2025-03-18 03:23:00 | NOAA-20 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e921b291-b59e-3bec-8d03-644704747f87 | -17.67657 | -42.7449 | 2025-03-18 03:23:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7f95aa6-f8cd-3a82-b2b4-2fc06e81e2ad | -15.66974 | -41.58104 | 2025-03-18 03:23:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a0f4baf2-611a-3309-a725-75beb42a045b | -17.67584 | -42.74843 | 2025-03-18 03:23:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2f885dd-939d-3610-b171-394bfbed3df5 | -16.63865 | -44.03946 | 2025-03-18 03:23:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7030ebf3-d7d8-3d34-b53a-47ed8003a0ef | -11.36316 | -40.0606 | 2025-03-18 04:14:00 | NOAA-21 | CAPIM GROSSO | BAHIA | Brasil | 2906873 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b627eff5-5af6-3dd5-91df-682b1d9538e6 | -10.46449 | -39.2964 | 2025-03-18 04:14:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5721eb61-5b23-3f3f-8359-6edf26cbd689 | -11.41995 | -41.41084 | 2025-03-18 04:14:00 | NOAA-21 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 96b1e8b3-bb3a-3a7e-ac04-953ac8fc8344 | -11.50769 | -38.79421 | 2025-03-18 04:14:00 | NOAA-21 | BIRITINGA | BAHIA | Brasil | 2903607 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d76dfbb7-f3a7-33f9-9880-e26622da66aa | -11.18858 | -40.5582 | 2025-03-18 04:14:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 2ca2ae91-c46f-3190-ba0b-1a1e9d1b420b | -12.8949 | -45.04619 | 2025-03-18 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a81a661-479e-3343-b9ae-af21fa82e190 | -14.11963 | -47.68189 | 2025-03-18 04:17:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 292790a7-c4cd-3873-bb01-6bb45200fd94 | -18.03773 | -44.20895 | 2025-03-18 04:17:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e1908b2-f6fc-38c1-9410-dd2da7bd82de | -12.08084 | -45.62811 | 2025-03-18 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 762a6200-5a50-3f77-ae27-7f733f16104c | -21.33335 | -48.64388 | 2025-03-18 04:17:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 91faa373-4b3a-3af3-ac6d-59389fc29b53 | -12.16526 | -39.90751 | 2025-03-18 04:17:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3cb8a7bd-6c67-39da-9bbf-f8454c172abc | -20.44043 | -56.56034 | 2025-03-18 04:17:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f9b5561-ff2a-3c4e-8c9d-e84b14df5bea | -20.44123 | -56.55675 | 2025-03-18 04:17:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a00721f-27e6-3b0e-9b0c-f534b0a9f613 | -21.18119 | -49.04151 | 2025-03-18 04:17:00 | NOAA-21 | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 22719a2b-a198-387a-aa38-2e26818e2f21 | -21.32994 | -48.6432 | 2025-03-18 04:17:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 81a3a130-b3a6-3e7b-9418-3c409da54ba6 | -15.18788 | -39.9448 | 2025-03-18 04:17:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b017e8b5-1c32-355e-9cce-63e21e90419c | -13.03574 | -44.64624 | 2025-03-18 04:17:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e029998d-2095-3936-95e8-ea90e688e7f7 | -15.25782 | -47.6724 | 2025-03-18 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36706cad-8c2c-3538-9fbe-bf3623d266e8 | -15.56845 | -47.85736 | 2025-03-18 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0273c05-4136-3ceb-a416-47b4972c00dc | -16.63752 | -44.04037 | 2025-03-18 04:17:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c00e9fb8-9fcc-345d-bac3-8cbb040adc11 | -12.68867 | -47.37674 | 2025-03-18 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6665638c-ab7f-31bd-9f6b-15f52520f2e0 | -23.21114 | -50.81342 | 2025-03-18 04:17:00 | NOAA-21 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d9313f08-836f-3b1b-9e18-0393cc68005a | -13.71281 | -48.44165 | 2025-03-18 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4181292e-d685-331e-b2fe-ae95842f32f3 | -16.6347 | -44.03613 | 2025-03-18 04:17:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45d58f51-6fde-3873-a999-2deb0b531e14 | -15.88579 | -46.00642 | 2025-03-18 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85258072-5e44-35ac-bbc7-94de9ad237ab | -12.89435 | -45.04972 | 2025-03-18 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d245a10c-d8c0-35f5-a42e-98138c3abfe0 | -12.07968 | -45.63533 | 2025-03-18 04:17:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ee0582b-26f0-3a04-8db9-f2bb1a32cd4b | -16.4013 | -51.54833 | 2025-03-18 04:17:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a983cae-7c43-3cf3-bf85-79819e51d131 | -12.07807 | -45.62395 | 2025-03-18 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e7ce4f7-8cde-3741-8130-66f7df2abd10 | -17.57849 | -45.38416 | 2025-03-18 04:17:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c66b6c05-9908-392e-bafa-57088d9dafc9 | -12.84883 | -43.83327 | 2025-03-18 04:17:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e17321ec-e9fd-326e-814a-1e07b609398a | -13.11257 | -44.85013 | 2025-03-18 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7792003-9fbe-3f0f-90b9-db52261a61be | -20.44659 | -56.5581 | 2025-03-18 04:17:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb7f4fbe-c04f-3293-965e-9a152d2ecc3c | -16.68116 | -43.88574 | 2025-03-18 04:17:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3637022e-5421-3034-a9d7-e19318f94c72 | -20.44481 | -56.55952 | 2025-03-18 04:17:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bd99767-fb09-311f-af50-3acf6b5ef79f | -15.07975 | -48.94659 | 2025-03-18 04:17:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bcb2c81-cde6-350c-beb0-f62ca104d7ee | -20.99549 | -51.79408 | 2025-03-18 04:17:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8f4db513-b180-34bf-a023-2d76d57f2cf5 | -12.89159 | -45.04565 | 2025-03-18 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba00ca38-5a0a-3493-848c-263706ae1b7f | -12.89104 | -45.04918 | 2025-03-18 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e577922e-a9f4-36d7-885e-66cdb085fcae | -20.5597 | -55.32225 | 2025-03-18 04:17:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ba87a43-efa0-361c-83f7-69e9ff3a7e00 | -18.39317 | -44.19451 | 2025-03-18 04:17:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d19d1649-2a96-3e2a-860f-5bc4759a6c51 | -13.68095 | -43.00316 | 2025-03-18 04:17:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fdce001d-4456-39ba-838d-c6243a32d542 | -17.379 | -42.48326 | 2025-03-18 04:17:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0d33941-3f63-3ff0-a943-75c94c4a8472 | -11.96448 | -48.09165 | 2025-03-18 04:17:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79e44307-8d93-345e-a835-2eed2aa80ed0 | -13.21934 | -46.56201 | 2025-03-18 04:17:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| acba0e1a-06ce-39d1-8d38-acb0d4bc26a9 | -11.58212 | -47.62329 | 2025-03-18 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README2.md)
