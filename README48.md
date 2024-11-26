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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6c5003d-9e43-3ecf-b51d-11a70b15c35b | -3.19007 | -49.05177 | 2024-11-26 12:53:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 55b3bdd5-9752-33e1-8e0f-c43118f7c306 | -2.52112 | -45.29402 | 2024-11-26 12:53:00 | TERRA_M-T | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 80da9758-4806-396b-8294-61ae66da573c | -3.5969 | -50.38828 | 2024-11-26 12:53:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c20ad4df-8606-36f5-ad6e-727c0110f470 | -1.23042 | -48.8891 | 2024-11-26 12:53:00 | TERRA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| bafb4c9f-b0d4-3aa3-942b-1cfb9b1de56b | -3.0827 | -49.35884 | 2024-11-26 12:53:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e09b7559-f1b3-3684-94b0-1e0a06ec0407 | -2.98953 | -42.26248 | 2024-11-26 12:53:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| e0391125-4937-346c-8e15-a90c94b38556 | -3.07632 | -49.19981 | 2024-11-26 12:53:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| f6d9a3db-c749-383b-b5b4-35f912bd17d3 | -3.93696 | -50.08039 | 2024-11-26 12:53:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| e74b7003-0d56-378b-b4b0-2fcc02ccfc60 | -3.27459 | -48.98044 | 2024-11-26 12:53:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 12116012-dceb-36c5-a137-e039b7e7280e | -3.07571 | -40.68669 | 2024-11-26 12:53:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 25.7 |
| 9911dcb3-738f-34e3-9354-04ceaf4cb295 | -3.42143 | -42.05001 | 2024-11-26 12:53:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 2c89bcb0-98a4-30b2-8757-0312e3237d8f | -1.74328 | -46.2924 | 2024-11-26 12:53:00 | TERRA_M-T | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f892d419-2121-3174-8848-9cc22e3f142e | -1.00727 | -47.10203 | 2024-11-26 12:53:00 | TERRA_M-T | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| df0c4149-01d2-3ea3-9072-7e8250ec53fc | -3.51958 | -50.22412 | 2024-11-26 12:53:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5b274a71-5114-311e-acbd-d4b113704e18 | -4.66721 | -47.95029 | 2024-11-26 12:53:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 62cd300f-e2e6-3a4c-a91e-20428674f8a2 | -2.16839 | -47.81929 | 2024-11-26 12:53:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4d959d8c-5d11-3bbb-a207-ee2abf804416 | -7.41043 | -47.49559 | 2024-11-26 12:53:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 0b888481-448c-3d80-a399-8c5cad37bfee | -2.93993 | -44.93664 | 2024-11-26 12:53:00 | TERRA_M-T | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 41.7 |
| a27dd1d7-d535-37e4-ace4-d2d5d49a620a | -17.14754 | -53.87018 | 2024-11-26 12:55:00 | TERRA_M-T | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7bc32db8-5121-3f2f-8695-74f2a3bba742 | -10.84718 | -53.94457 | 2024-11-26 12:55:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 52d660bd-8128-39d1-bfb3-3d1d78e54ec5 | -17.85823 | -50.51992 | 2024-11-26 12:55:00 | TERRA_M-T | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| dfbd1031-ae38-35ea-98e7-95103b81a3cd | -17.5621 | -50.26565 | 2024-11-26 12:55:00 | TERRA_M-T | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a929463a-e953-3a6a-9e39-893646fa9f25 | -17.74809 | -52.43166 | 2024-11-26 12:55:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 483ce685-6bad-3834-9f50-6d8745ef15d1 | -8.40314 | -49.17508 | 2024-11-26 12:55:00 | TERRA_M-T | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 66bda9f7-c224-3746-976b-837284d3c863 | -8.74589 | -50.39745 | 2024-11-26 12:55:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| abd126e7-4813-34ab-b686-397bba66202a | -10.70024 | -49.42196 | 2024-11-26 12:55:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| c0a611e2-e733-3bdc-9660-86cd55c63ca1 | -17.75692 | -52.43302 | 2024-11-26 12:55:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 24aa0f0d-9dda-30e0-b643-9a81562c2fa8 | -8.74461 | -50.40632 | 2024-11-26 12:55:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 44e178e3-9cf6-3712-8453-094854b75a64 | -23.19293 | -51.68678 | 2024-11-26 12:57:00 | TERRA_M-T | ASTORGA | PARANÁ | Brasil | 4102109 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 03307cda-2c93-30f1-8a12-19889de003e3 | -19.06293 | -53.47111 | 2024-11-26 12:57:00 | TERRA_M-T | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 981faa35-960a-31c6-a4bf-68caed74bef9 | -23.47577 | -47.37881 | 2024-11-26 12:57:00 | TERRA_M-T | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| f2cb8b14-a4c5-38e7-9775-824d4fcb76fa | -18.61847 | -51.95722 | 2024-11-26 12:57:00 | TERRA_M-T | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b9f66d8d-b653-366f-9559-3a158393c514 | -23.089 | -52.38747 | 2024-11-26 12:57:00 | TERRA_M-T | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| cdab0632-567c-3023-94bf-be1a071d489b | -22.77367 | -51.86202 | 2024-11-26 12:57:00 | TERRA_M-T | SANTO INÁCIO | PARANÁ | Brasil | 4124509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 8b0caade-4df0-3054-8754-cd7a5b196b08 | -25.11284 | -51.3791 | 2024-11-26 12:57:00 | TERRA_M-T | TURVO | PARANÁ | Brasil | 4127965 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| c8c54562-571d-3203-85ea-86d83aa31786 | -18.25247 | -51.81016 | 2024-11-26 12:57:00 | TERRA_M-T | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3f67296d-6758-3698-8014-cb6d72b70726 | -19.06433 | -53.46166 | 2024-11-26 12:57:00 | TERRA_M-T | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 41.4 |
| f7dd3f1e-3cde-3486-afec-acbe34df85ff | -21.56669 | -54.20116 | 2024-11-26 12:57:00 | TERRA_M-T | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 65824d42-4557-346b-99fc-ab0082dddbf8 | -18.16826 | -51.75334 | 2024-11-26 12:57:00 | TERRA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 6659e6b8-63b4-314f-8fd6-0975ce0e763f | -24.4345 | -50.59706 | 2024-11-26 12:57:00 | TERRA_M-T | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| f9607916-a77e-31e0-805b-11e9cdf8c06c | -23.09037 | -52.37751 | 2024-11-26 12:57:00 | TERRA_M-T | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 8333e93c-eb36-3134-b486-9ea8e779010a | -23.58028 | -51.73255 | 2024-11-26 12:57:00 | TERRA_M-T | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 004a2fcc-59b0-3fab-952d-911ce1b38b7c | -23.4738 | -47.39811 | 2024-11-26 12:57:00 | TERRA_M-T | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| dd9f68dd-0a30-362e-93b3-af83c7bf2d35 | -19.07323 | -53.46307 | 2024-11-26 12:57:00 | TERRA_M-T | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 74801470-3886-3388-bf9b-3af1ac3cd794 | -3.6515 | -41.535 | 2024-11-26 13:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 100.7 |
| 8aab3b0d-e8ec-30e3-a5d3-37c136dc563c | -17.6453 | -57.5874 | 2024-11-26 13:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 143.7 |
| 3e26f477-b5ad-381a-b7de-b59cfaf95b38 | -1.0624 | -48.0134 | 2024-11-26 13:10:00 | GOES-16 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 6c91bdff-1528-3fc4-8c99-7b3b3b50b675 | -3.5921 | -42.0869 | 2024-11-26 13:10:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 123.2 |
| 548f8c57-9093-3163-a7d2-48900846ac96 | -3.1876 | -48.4387 | 2024-11-26 13:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| af78f355-faff-3bf6-b74e-709b8ca8fdaa | -3.986 | -48.0626 | 2024-11-26 13:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 8366c004-38f5-3939-81ab-22a897ac0b35 | -17.6453 | -57.5874 | 2024-11-26 13:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 158.3 |
| 1b909a6e-8430-3030-8f2c-584a7c215cf1 | -3.5741 | -41.969 | 2024-11-26 13:20:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 94.4 |
| 389b1c96-4dd8-3a3b-bd3b-1c6eed40fae1 | -17.6453 | -57.5874 | 2024-11-26 13:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 177.9 |
| 6c7c6ac9-bf5a-3b8b-b2ea-07f3f5c5b475 | -3.5742 | -41.9452 | 2024-11-26 13:20:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 137.7 |
| a9a46f28-e89f-30cd-8902-db3d83182c1a | -3.5921 | -42.0869 | 2024-11-26 13:20:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 95.9 |
| 601a5ee6-1d75-3238-9bf7-782a4ce505af | -17.3021 | -58.1791 | 2024-11-26 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.6 |
| c5a0aab6-6d5b-375b-9893-cdf1930f51de | -2.9569 | -42.0449 | 2024-11-26 13:30:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 1803ece7-73d3-34b8-8111-11d26a0e5665 | -16.9413 | -57.4449 | 2024-11-26 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.9 |
| 65513e0e-7c4d-3518-946d-019dd898c931 | -17.6256 | -57.5897 | 2024-11-26 13:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.6 |
| 88889fb4-7fd5-3f2c-a9ca-e4c8d2a18776 | -3.986 | -48.0626 | 2024-11-26 13:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 121.3 |
| f64879b3-0a50-37b2-8b2f-0f7af9c9428c | -3.5921 | -42.0869 | 2024-11-26 13:30:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 104.6 |
| 4f5e4ae0-c3d9-3c22-b56c-843309e99073 | -17.8447 | -57.4401 | 2024-11-26 13:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.2 |
| 44207395-d679-3559-91bf-3595216af753 | -17.6453 | -57.5874 | 2024-11-26 13:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 251.2 |
| c871667a-532a-37e6-88e6-9911d8f02753 | -3.5921 | -42.0869 | 2024-11-26 13:40:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 89.1 |
| 68d0ae79-bed2-3e17-bca3-d1c0bc63f45b | -17.3021 | -58.1791 | 2024-11-26 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.0 |
| 998a967d-a3c1-3c21-884b-428edf3e96c9 | -17.4048 | -57.8818 | 2024-11-26 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.5 |
| 5f94dbc1-7e6a-3240-b64c-82c6c8a420aa | -3.5741 | -41.969 | 2024-11-26 13:40:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 101.7 |
| 12b545be-3cd4-3442-b8a0-c3e8b85f832e | -3.7005 | -42.7192 | 2024-11-26 13:40:00 | GOES-16 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 206d708e-342e-39cb-89aa-01c39ad689a0 | -17.6256 | -57.5897 | 2024-11-26 13:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.0 |
| 80299bc3-7339-32f1-bedf-008222099bd0 | -3.1978 | -42.437 | 2024-11-26 13:40:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| bfc7c380-1112-3aa5-a922-7973b690239e | -17.6453 | -57.5874 | 2024-11-26 13:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 185.1 |
| 6b33a772-214a-3a93-9717-4e545ce685c6 | -17.6453 | -57.5874 | 2024-11-26 13:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 177.7 |
| b3acd078-273d-3bda-b73f-eef313b4f715 | -17.6256 | -57.5897 | 2024-11-26 13:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.1 |
| 8c8be2cc-4fbd-3fb6-bb45-21ea73ef5b45 | -3.1978 | -42.437 | 2024-11-26 13:50:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 1e13ce21-1609-336b-8a22-962965e68e96 | -3.7005 | -42.7192 | 2024-11-26 13:50:00 | GOES-16 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 208.9 |
| 9796a500-73d1-31c3-a988-7d81d34e441f | -3.5741 | -41.969 | 2024-11-26 13:50:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 132.1 |
| f7809afb-c090-3944-8aa9-24d01f52c8ad | -17.6256 | -57.5897 | 2024-11-26 14:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.9 |
| 5c4212f5-d4fe-318f-9c1a-aff746c819ce | -3.3829 | -42.7346 | 2024-11-26 14:00:00 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 1bb9f171-2cff-3311-899d-22796b60f8e4 | -17.6453 | -57.5874 | 2024-11-26 14:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 197.0 |
| 5320d3e7-3d90-31ab-a35b-8dac3dafbbb0 | -16.9413 | -57.4449 | 2024-11-26 14:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.1 |
| 333b4c2a-b10a-39fe-8cb9-c559f85c9ec5 | -16.9413 | -57.4449 | 2024-11-26 14:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.9 |
| 8ed0f21d-2830-325e-aba1-f6f65eebcd32 | -18.3587 | -57.4175 | 2024-11-26 14:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.7 |
| 536c9f02-0b44-333b-8a1e-1b69981eb6b7 | -17.6256 | -57.5897 | 2024-11-26 14:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.7 |
| 17b4f951-ac06-371b-a27a-deea5f3704e3 | -17.6453 | -57.5874 | 2024-11-26 14:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 174.4 |
| 7ed55185-5bf9-37e0-bea5-dfdc06718617 | -3.5929 | -41.9442 | 2024-11-26 14:10:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 136.1 |
| cc6d55fe-ac71-3eb5-8e57-61576dbad937 | -18.3587 | -57.4175 | 2024-11-26 14:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.4 |
| e3641f3d-0ccf-3205-b59e-810a785c3880 | -17.6453 | -57.5874 | 2024-11-26 14:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 161.8 |
| 0aa2c581-17cf-3328-a519-7243d4af021c | 4.0051 | -60.729 | 2024-11-26 14:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 68.9 |
| f169a5b1-e222-3b5f-84e8-1348a07dc0c8 | -3.1978 | -42.437 | 2024-11-26 14:30:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 5eb626d8-ac5e-30c7-b7c3-bc91477313bf | -2.9949 | -41.9245 | 2024-11-26 14:30:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 80.0 |
| 6c635459-61c1-3444-9754-cd0155e4363a | -17.3021 | -58.1791 | 2024-11-26 14:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.8 |
| 0f8f7af7-14a1-34ae-a0e0-38bedd868275 | -23.95 | -54.1191 | 2024-11-26 14:30:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 126.9 |


