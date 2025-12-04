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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f74982e-30d0-3088-b285-7d2446863cd8 | -4.25777 | -48.88515 | 2025-12-04 04:50:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 779619e9-e33a-389a-bdd0-b615dd05aac6 | -5.57144 | -45.41842 | 2025-12-04 04:50:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8599e947-b3d3-375d-98f1-e79b20bb20cf | -6.43292 | -44.79395 | 2025-12-04 04:50:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7db46b68-563d-3502-9d5c-570a8bdadf5e | -6.43796 | -44.79026 | 2025-12-04 04:50:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a94e0354-7ecf-3a91-b1dc-c3f928826c58 | -4.70196 | -45.69934 | 2025-12-04 04:50:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b407fe7-bab9-3ef9-ae72-9cd4398bd547 | -4.73072 | -45.70051 | 2025-12-04 04:50:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efa573c4-bed3-38fb-b65d-ad1c4e527c99 | -4.94477 | -44.9179 | 2025-12-04 04:50:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d00212a-7523-3d4c-8a4c-23e984a9e07a | -5.83393 | -43.26965 | 2025-12-04 04:50:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1b2148b-fc0f-3564-a5ee-627f058fd017 | -4.77293 | -46.1295 | 2025-12-04 04:50:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 858c3407-20a1-3a6c-a9f4-e32678d652d8 | -4.67821 | -46.3853 | 2025-12-04 04:50:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8fa6d436-b656-3892-8fe9-e5aaf60d3aa6 | -4.69419 | -46.43639 | 2025-12-04 04:50:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6b7c261a-d2ba-3620-b46c-21fdd663d489 | -4.03422 | -50.38514 | 2025-12-04 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 155ec52c-2d82-3f52-9453-608ad3079e9c | -10.54229 | -47.7336 | 2025-12-04 04:50:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 083b4884-d456-3abf-b51f-0fb55b5a748c | -4.77688 | -46.12996 | 2025-12-04 04:50:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 54695091-f32f-38bc-925b-62cc436c061e | -6.00378 | -42.3258 | 2025-12-04 04:50:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 711889c6-4df0-3628-a576-3cb69504f612 | -7.22006 | -45.04251 | 2025-12-04 04:50:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e49fc941-f3a6-3ec1-90f9-79ba8ab12906 | -6.41823 | -43.47075 | 2025-12-04 04:50:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b8cf9bb-8009-30b0-a93a-023a3f17947f | -5.79735 | -42.99361 | 2025-12-04 04:50:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 59df398c-fb5c-3a38-95d1-8878a8bc58b4 | -6.43415 | -44.78542 | 2025-12-04 04:50:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 69e2b7fa-6968-3f97-8c3a-41f502ebca6e | -5.34522 | -42.11471 | 2025-12-04 04:50:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fdb478b9-8964-3d8f-a761-5367c5a7fc34 | -6.43354 | -44.78967 | 2025-12-04 04:50:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8c6b4bd3-5887-3eb7-9b08-7c2313f312dd | -4.60078 | -45.99314 | 2025-12-04 04:50:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e38ded91-f41b-3363-9380-3cb31cfced43 | -5.97802 | -44.59938 | 2025-12-04 04:50:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4aa230a4-e3c7-3569-ac1a-9a3bbb75ec39 | -5.98311 | -44.59565 | 2025-12-04 04:50:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4ebf5b4e-be94-3f18-8c25-688a3717daeb | -3.84759 | -50.90041 | 2025-12-04 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74fec864-938f-3a43-b6e4-d3d0a717b579 | -5.22261 | -43.96813 | 2025-12-04 04:50:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 718a133d-d8cf-352d-818f-63b5666c96bb | -12.62959 | -47.42539 | 2025-12-04 04:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 489a8126-ee35-3177-b7be-2472160453be | -21.62304 | -56.13315 | 2025-12-04 04:53:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9bc80d12-5e31-399c-ad81-a3cab154d921 | -22.90792 | -49.68931 | 2025-12-04 04:53:00 | NPP-375D | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 980203c0-259d-3c05-95f1-40435dfdc9e0 | -13.04277 | -53.71105 | 2025-12-04 04:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecbaed02-4080-34ae-b0b7-c115dc60c66d | -21.62706 | -56.12996 | 2025-12-04 04:53:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 742686fb-2c18-3fb3-afa9-e4ddecca8386 | -21.62368 | -56.12931 | 2025-12-04 04:53:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9e684409-e217-3b75-971d-8c19bd975813 | -21.62691 | -56.13271 | 2025-12-04 04:53:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e598d77f-cf27-31aa-9453-c85d49c52260 | -21.08627 | -56.1214 | 2025-12-04 04:53:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ba54ba0-4957-3827-a328-7a711cd79692 | -12.63364 | -47.42599 | 2025-12-04 04:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 057a9cb1-981a-332e-8cef-93fb845524f6 | -21.62642 | -56.13379 | 2025-12-04 04:53:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 758acb09-f7ec-3966-920d-541993e1364a | -21.62756 | -56.12888 | 2025-12-04 04:53:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7e34b02-822a-313a-b7b2-4d966caeb9d8 | -12.62909 | -47.42899 | 2025-12-04 04:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd4b0574-f977-3018-ab85-15bf71105b7e | -21.63029 | -56.13335 | 2025-12-04 04:53:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b6e3c84e-5fc7-3671-bdb7-09466111682a | -19.63121 | -56.83467 | 2025-12-04 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 21.8 |
| 57b9bd01-6abc-3248-9cb8-8faf500dcc6e | -19.62907 | -56.84708 | 2025-12-04 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 0224a40b-ac2f-3841-86a2-8e32071f4924 | -19.63192 | -56.83054 | 2025-12-04 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| b9d91a74-baad-37cf-b89f-dcb496a472d1 | -29.55213 | -51.47467 | 2025-12-04 04:55:00 | NPP-375D | SÃO JOSÉ DO SUL | RIO GRANDE DO SUL | Brasil | 4318614 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 80c7ffb9-97b4-3d80-99d0-4bfd0420a8a3 | -19.6305 | -56.83881 | 2025-12-04 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 21.8 |
| be8a715f-540e-35c1-a47e-86db25f7a7bc | -19.63401 | -56.83949 | 2025-12-04 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 21.8 |
| 5ade583d-f078-39d3-a236-94541b0b7de0 | -20.9151 | -56.37429 | 2025-12-04 04:55:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efa9fe3a-79bb-30c1-920b-6ed8d6eb5bf4 | -20.91852 | -56.37494 | 2025-12-04 04:55:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 00f36126-f325-3d49-b980-f5327900638b | -19.43866 | -54.12729 | 2025-12-04 04:55:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c75c3084-2a03-3ac6-a553-903ecb627e81 | -19.63263 | -56.82641 | 2025-12-04 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| e5e7b7e4-6fe1-3a01-a4a5-f7a80ed8ddce | -27.68953 | -48.75058 | 2025-12-04 04:55:00 | NPP-375D | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5b6ef2bb-81b7-3878-ac27-cb3e17b7a541 | -19.70188 | -49.20315 | 2025-12-04 04:55:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8a69012-a3b3-3b2c-b28b-e04afe84bcd2 | -19.63472 | -56.83535 | 2025-12-04 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 21.8 |
| 8133ff73-ea22-37aa-93db-d16f4e6e941e | -19.62556 | -56.84639 | 2025-12-04 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| caf3638f-d4ba-3b65-bbb6-3c73a1c067c6 | -19.63543 | -56.83122 | 2025-12-04 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 13ae7543-700e-373d-84ca-c4424a204824 | -19.63553 | -56.76741 | 2025-12-04 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 74e40e9b-ee23-33a2-b4ef-43e321ee694b | -19.69861 | -49.19711 | 2025-12-04 04:55:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa8213c4-9961-3d04-9a44-c8a7a2624ccb | -27.68497 | -48.75 | 2025-12-04 04:55:00 | NPP-375D | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 52e45642-8aba-331b-adb3-438a248708fe | -19.70261 | -49.1976 | 2025-12-04 04:55:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 541f2329-5b39-3abd-bf93-68cd1f95eddd | -19.63973 | -56.76398 | 2025-12-04 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b7303e81-0e94-3b60-9084-1527ba74ec51 | -19.62978 | -56.84294 | 2025-12-04 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| b6191ea8-c8ab-3434-8619-8e2feba84528 | -20.91984 | -56.3671 | 2025-12-04 04:55:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 38b49b1e-36a0-319b-94c1-090347e3db97 | -19.61925 | -56.8409 | 2025-12-04 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ba02e102-fbdc-3bb3-8ac8-9c5f008b9564 | -19.63614 | -56.82709 | 2025-12-04 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 44c75af9-bc12-3f45-8351-901e29fc958a | -19.61574 | -56.84022 | 2025-12-04 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9affb1d1-b79c-32dd-b2d5-bdaee21b507b | -19.6333 | -56.84362 | 2025-12-04 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| c9e7112d-ac8b-39f1-ae63-877e8d16bf0c | -19.62627 | -56.84226 | 2025-12-04 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 1a548dab-4d85-365b-9a2a-7d651d0a682f | -20.91918 | -56.37102 | 2025-12-04 04:55:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d32cbe2e-57d7-3c82-ac35-ba1fb990e395 | -20.90322 | -56.3193 | 2025-12-04 04:55:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2324b8a-0e88-35f1-9bd9-9db24557263f | -19.62205 | -56.84572 | 2025-12-04 04:55:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 84d0b059-c258-3b79-a95d-57a276e25b7c | -19.6241 | -56.8339 | 2025-12-04 05:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 90.7 |
| 496d85a3-4bc3-3617-9748-6817e89c20ee | 3.48261 | -51.25053 | 2025-12-04 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f686352-db35-3c35-9fb3-ff9d763d9877 | 3.49089 | -51.25389 | 2025-12-04 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d458cf38-8dbc-3374-9e34-3b4466232b37 | 3.48712 | -51.25451 | 2025-12-04 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0fff7ee-5c5e-3f0d-b511-8f8810fea59f | 2.91829 | -51.01596 | 2025-12-04 05:08:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 44ab8916-3c5d-347c-b773-8789898abaf8 | 2.91753 | -51.01115 | 2025-12-04 05:08:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8f5716bf-8c89-3cc8-9e11-43795ff30b8e | 2.52871 | -50.83976 | 2025-12-04 05:08:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05be3b93-fbc9-3150-93d8-8a97abcefce8 | 0.41026 | -50.75929 | 2025-12-04 05:08:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4998d7d7-bf8a-3c0c-b881-ce81c8b7b075 | 3.67758 | -51.28014 | 2025-12-04 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 68170854-9284-37f5-8af5-bfa18534b714 | 3.58564 | -51.28731 | 2025-12-04 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 699236ea-e3b7-3a96-b25e-a9d72070613e | 3.4713 | -51.25235 | 2025-12-04 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b1b1551-84e5-38d4-85d2-27c543f272d0 | 3.49162 | -51.25848 | 2025-12-04 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4d14b91-d02a-3615-9f95-69eeb83267d2 | 3.46753 | -51.25295 | 2025-12-04 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2cfbc80-57a6-338c-826c-4eaffdac59d9 | 3.67081 | -51.28588 | 2025-12-04 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 735d73c7-7fe6-3216-af99-4033d4e04e1d | 3.67383 | -51.28074 | 2025-12-04 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e964e29-275b-35a4-bd0c-05534f291317 | -0.18207 | -49.0671 | 2025-12-04 05:08:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df7ffd07-1e09-3aa3-b90f-a7fcb3d9bc14 | 2.91444 | -51.01658 | 2025-12-04 05:08:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 90ba44b2-95a8-393f-b9a2-d2e5f7a394af | 3.67456 | -51.28528 | 2025-12-04 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d2f3431-dd7f-33ce-8a66-dbd49d5f7551 | 2.91876 | -51.00875 | 2025-12-04 05:08:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98174861-2cef-38b1-8c78-38aa12be2f24 | 2.52951 | -50.84476 | 2025-12-04 05:08:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9ed1ac8f-eef2-3519-b129-15f0cca9ba37 | 3.67832 | -51.28467 | 2025-12-04 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e325970a-7807-30aa-84d4-09b26dfd7b86 | 0.32516 | -49.73069 | 2025-12-04 05:08:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a20ed87f-9411-3050-970a-59bcd66ee513 | 3.48638 | -51.24992 | 2025-12-04 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73d04950-2656-301b-b137-b1a356f526cb | 0.40968 | -50.7557 | 2025-12-04 05:08:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 97d68872-bd81-3824-8c02-3dd93b16162e | 3.47507 | -51.25174 | 2025-12-04 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02909ff3-a5c6-3dee-b34d-a27f210be2ee | 3.46827 | -51.25753 | 2025-12-04 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43f67f3f-f9bd-33b0-be07-8e3bb35a4abb | 3.47884 | -51.25114 | 2025-12-04 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b24f0c7a-3b45-3884-b864-3dfaac677afb | 3.67155 | -51.29041 | 2025-12-04 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ee4c820-8ca5-3df7-9da8-c93116739b94 | 2.91367 | -51.01177 | 2025-12-04 05:08:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 567b37c9-0eb7-3d8f-b41a-751d4720838f | -19.6241 | -56.8339 | 2025-12-04 05:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 83.1 |
| 453e33c0-a938-38fa-b16d-b8a99b5c7278 | -1.42383 | -53.00964 | 2025-12-04 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README19.md)
