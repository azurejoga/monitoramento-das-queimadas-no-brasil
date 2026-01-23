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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe4017d1-76b6-38c5-a286-94b876fc71a6 | -25.17079 | -49.40211 | 2026-01-23 04:18:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 11c74657-9e2c-3caa-a229-c1e81a3eb61e | -20.90947 | -56.38853 | 2026-01-23 04:18:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a82ae18-9d6d-3851-8817-84d1c563214f | -22.60749 | -49.57307 | 2026-01-23 04:18:00 | NPP-375D | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 89d363c4-e405-3b92-a116-d3cb46851c80 | -19.66286 | -56.86945 | 2026-01-23 04:18:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| db472ff8-65e1-3af9-a66b-366f7c8db309 | -21.77715 | -56.28868 | 2026-01-23 04:18:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| efcf58d5-8bd3-35c7-b607-c160969178b9 | -19.68111 | -56.8742 | 2026-01-23 04:18:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5ab79f53-6241-3dc6-a952-91425b3a6b98 | -22.3682 | -48.34825 | 2026-01-23 04:18:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b49041d-811c-3275-ab4c-697fdacfc922 | -20.38332 | -57.88401 | 2026-01-23 04:18:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9866b5f1-efce-39c7-b70c-833d8e79b9c5 | -22.60838 | -49.56817 | 2026-01-23 04:18:00 | NPP-375D | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 83ffe800-b03e-37a1-a5d4-183ae053e53b | -19.68662 | -56.88557 | 2026-01-23 04:18:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 629318e0-7e2a-3466-a23f-f2607dde54ec | -22.02544 | -56.33953 | 2026-01-23 04:18:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 591ac701-b11a-334a-8c2a-c11274448068 | -22.60723 | -49.57529 | 2026-01-23 04:18:00 | NPP-375D | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2a01fdb6-19c9-37ab-9519-07adcd8dde80 | -22.03769 | -49.50611 | 2026-01-23 04:18:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ad65cabf-a96d-3600-b4f7-2857639bc943 | -20.37195 | -57.87499 | 2026-01-23 04:18:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 73353173-8783-3ee2-80a4-a362689c8627 | -22.60375 | -49.57226 | 2026-01-23 04:18:00 | NPP-375D | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 11.6 |
| d6d17d49-56fb-3232-b33b-d1a636c4d85e | -20.90876 | -49.14286 | 2026-01-23 04:18:00 | NPP-375D | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2e94d723-cf25-34c9-a39d-44c5f107fa41 | -20.36561 | -57.87325 | 2026-01-23 04:18:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| a0add051-682a-3f58-9752-76c6528dfdba | -21.77845 | -56.28629 | 2026-01-23 04:18:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a38150cc-4d9d-35ce-8453-f44bf94e6413 | -19.6617 | -56.87439 | 2026-01-23 04:18:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b4c06773-c1b9-3139-b15e-4d8f6c92e596 | -19.65777 | -56.89899 | 2026-01-23 04:18:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 093f5e9e-6449-37a1-92b9-a7d883da8d9a | -22.60815 | -49.57037 | 2026-01-23 04:18:00 | NPP-375D | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 10.4 |
| cd0e4848-fd13-3aaf-91a4-64108f31f782 | -19.68293 | -56.92197 | 2026-01-23 04:18:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 0bb351db-482d-372e-9a30-36b4e384d105 | -19.68774 | -56.88062 | 2026-01-23 04:18:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a699ca4b-a1aa-3ffe-b689-c5861e4eaa90 | -22.61189 | -49.5712 | 2026-01-23 04:18:00 | NPP-375D | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0fcc8c4f-f48b-3763-8450-2f9b26c930b2 | -21.77936 | -56.28235 | 2026-01-23 04:18:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 82842c0a-fe12-3632-ae6e-c704706840e1 | -25.72043 | -51.59367 | 2026-01-23 04:18:00 | NPP-375D | PINHÃO | PARANÁ | Brasil | 4119301 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5b30899f-9c29-3a7c-afcd-e48bc9ec71ab | -19.67669 | -56.87246 | 2026-01-23 04:18:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1be601e5-bda3-3db2-83a9-46ad9d97cbfe | -19.67877 | -56.92039 | 2026-01-23 04:18:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| abe5d088-dadc-3b7a-91ff-b289567a8a0e | -24.00346 | -52.56137 | 2026-01-23 04:18:00 | NPP-375D | ARARUNA | PARANÁ | Brasil | 4101705 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d5dd8943-541a-34c2-b800-c7446efc6cac | -20.37698 | -57.88227 | 2026-01-23 04:18:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4ee6edbc-862f-354b-b97d-eea9136bd5b3 | -23.05829 | -49.06125 | 2026-01-23 04:18:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8df736b-189f-3ea7-aa1b-92df35c18068 | -20.90963 | -49.13806 | 2026-01-23 04:18:00 | NPP-375D | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 36e36c7c-23a7-38a4-9afe-f71a554e1cd2 | -21.78406 | -56.28793 | 2026-01-23 04:18:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a49c4a2-85bf-354f-9de3-9f850d1230c0 | -22.0188 | -56.34244 | 2026-01-23 04:18:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72c2b45a-76c6-390e-8747-3f5055c69906 | -21.77805 | -56.28463 | 2026-01-23 04:18:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93fc284e-20f7-3af4-8d09-fa014835ec8c | -19.67503 | -56.87262 | 2026-01-23 04:18:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8c3c026d-9354-35d8-a665-38b1a8b5dc9b | -19.67061 | -56.87085 | 2026-01-23 04:18:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 72a800a6-7b09-3df7-956b-65dd810dd0c3 | -19.17102 | -57.54823 | 2026-01-23 04:18:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| ff2b3dbd-abc6-3d26-b2be-fe809569dffe | -19.6589 | -56.89402 | 2026-01-23 04:18:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0a0923e7-4c87-3122-9fa8-8c7334c21d8f | -22.60349 | -49.57449 | 2026-01-23 04:18:00 | NPP-375D | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 94765fe0-e004-3711-b4f2-b51cad88c927 | -19.66452 | -56.86925 | 2026-01-23 04:18:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2511ce43-6ee9-3fa0-bb07-23253fcd23d9 | -22.73361 | -49.34948 | 2026-01-23 04:18:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 357bd942-3ffc-302d-bcb6-12a10356d105 | -19.68277 | -56.87406 | 2026-01-23 04:18:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c4ca9329-3a27-36fe-80b0-1df4ec7a7880 | -27.56305 | -48.66069 | 2026-01-23 04:21:00 | NPP-375D | SÃO JOSÉ | SANTA CATARINA | Brasil | 4216602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 978b53d3-c606-3075-b4b4-22fdae2cfe95 | -29.8895 | -51.23357 | 2026-01-23 04:21:00 | NPP-375D | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| f9ef37c5-2f3b-369b-b90f-1d6f288c9956 | -27.09829 | -50.52415 | 2026-01-23 04:21:00 | NPP-375D | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a22c8343-7e68-3475-b344-7b3c8c7831b2 | -27.09737 | -50.529 | 2026-01-23 04:21:00 | NPP-375D | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0494afaf-d6e7-3a25-8ab0-929e2ac3a2c0 | -29.88494 | -51.21716 | 2026-01-23 04:21:00 | NPP-375D | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| f7939a7b-aa2a-3755-bf30-27046e81e0bc | -27.56646 | -48.66145 | 2026-01-23 04:21:00 | NPP-375D | SÃO JOSÉ | SANTA CATARINA | Brasil | 4216602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4ab27f3b-de4f-3bd9-bb77-108e77ed74f9 | -27.09638 | -50.52686 | 2026-01-23 04:21:00 | NPP-375D | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 19acf12d-261f-3f2c-89a5-7ea5f5006cd5 | -31.6153 | -51.41006 | 2026-01-23 04:21:00 | NPP-375D | SÃO JOSÉ DO NORTE | RIO GRANDE DO SUL | Brasil | 4318507 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| ebd9a909-f8e7-3967-8dd6-19bb72b69988 | -28.65038 | -49.46107 | 2026-01-23 04:21:00 | NPP-375D | NOVA VENEZA | SANTA CATARINA | Brasil | 4211603 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9b2c9289-4276-35c8-89f5-ce4f0d9f58e3 | -2.08996 | -53.51862 | 2026-01-23 04:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0660bdf1-9624-3d7b-b40a-21da76089162 | -4.53907 | -40.16523 | 2026-01-23 04:31:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cd890d0e-6cbe-3c32-adfd-e9e37956a5c4 | -4.07176 | -39.82281 | 2026-01-23 04:31:00 | NOAA-20 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 1b06dd14-0d02-35c5-8f06-fbfa9e740930 | -2.17883 | -53.72234 | 2026-01-23 04:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6ec4e91-b75a-36fa-b30b-c58961fa8d66 | -2.88417 | -40.50992 | 2026-01-23 04:31:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c8dd2547-280f-35b0-841c-cadc65be171f | -3.96674 | -42.1683 | 2026-01-23 04:31:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a0242d5b-780a-3003-bc3c-594a80731298 | -3.41083 | -42.46189 | 2026-01-23 04:31:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ec864b61-3c0a-336e-b46f-553d0b1dacd6 | -4.51776 | -38.42865 | 2026-01-23 04:31:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| bce3c1ba-d66b-3ff3-b532-5ed1ba83425d | -2.09069 | -53.51416 | 2026-01-23 04:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2a74034-72ed-3d1f-9bd7-ec87290459f4 | -3.47932 | -39.20453 | 2026-01-23 04:31:00 | NOAA-20 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6b7ced49-aadb-3fad-a4d9-757a1deac270 | -4.77251 | -37.81413 | 2026-01-23 04:31:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a8c92c3d-b8b2-39f4-8cae-a36d26026b54 | -4.77196 | -37.81785 | 2026-01-23 04:31:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 97efc14a-eb5f-3301-a6af-b109ea1b32dd | -4.51725 | -38.43201 | 2026-01-23 04:31:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 29db944a-329b-3c7a-9747-0bc4fcfeadfa | -2.1781 | -53.72685 | 2026-01-23 04:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f74e95b-1809-39c5-93ce-01376c8eb273 | -6.99642 | -42.86637 | 2026-01-23 04:33:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c075a98e-e032-3e63-b09e-83603e1b1f33 | -5.00846 | -37.53933 | 2026-01-23 04:33:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f2aab801-9e0a-38e8-af99-9d8fd6faa0ac | -5.63024 | -44.84338 | 2026-01-23 04:33:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eaac96dd-3e43-316d-b24e-b5857de526c2 | -7.61276 | -35.09289 | 2026-01-23 04:33:00 | NOAA-20 | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 84866db7-62c4-31ae-bd01-f64c3162765a | -5.62371 | -44.83812 | 2026-01-23 04:33:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a03b910-b99e-360e-96a8-18f7fdfec743 | -8.15443 | -43.18692 | 2026-01-23 04:33:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f86b738c-dff2-3c36-a9ef-21d5f71ea16e | -8.38963 | -46.237 | 2026-01-23 04:33:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c63f5c6d-a30d-37cd-87c9-51927b55c638 | -8.1201 | -48.01819 | 2026-01-23 04:33:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1e65fb46-5241-3d09-8fe9-6437b1b61859 | -5.62309 | -44.84223 | 2026-01-23 04:33:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34ed30bb-42b9-3b7e-9912-d64ed2d96d69 | -5.00275 | -37.53852 | 2026-01-23 04:33:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0403bffe-a471-3de1-9b5d-54188bcccaa0 | -5.61952 | -44.84166 | 2026-01-23 04:33:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b28db50c-e5e3-3641-8b4d-0b078e94d776 | -9.38132 | -47.07255 | 2026-01-23 04:33:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6781c01b-d0bd-36ef-8492-d3909215f8ba | -5.30926 | -45.17031 | 2026-01-23 04:33:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c09af65-8005-3733-bfe4-cb16daefc194 | -7.61275 | -35.09244 | 2026-01-23 04:33:00 | NOAA-20 | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| f1d7b530-2817-3ce9-97cd-6f20c34cf7ce | -5.62667 | -44.8428 | 2026-01-23 04:33:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8b13a7c-da13-30b3-8cc2-01eda9bd9e34 | -8.11955 | -48.02168 | 2026-01-23 04:33:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cf31cb4e-8e9b-3c37-b8ef-e069a10b63f3 | -7.61878 | -35.09983 | 2026-01-23 04:33:00 | NOAA-20 | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| f269004e-e211-391d-8ed8-ac11c0cb711e | -8.38905 | -46.2408 | 2026-01-23 04:33:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7f64d67-c71e-369f-9e83-7416dafc3e41 | -5.62014 | -44.83756 | 2026-01-23 04:33:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23fa5614-2b27-3316-bfc5-845b76e61bd7 | -8.12396 | -48.01524 | 2026-01-23 04:33:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3cca69e7-a905-3c88-a9bd-47fab24f2d8f | -8.1585 | -43.18755 | 2026-01-23 04:33:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d03a4630-d1ed-39e8-ac36-aecaf851ce28 | -7.61966 | -35.09373 | 2026-01-23 04:33:00 | NOAA-20 | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 85f8c745-49a3-39ec-b6cf-49dbf9ed0a94 | -6.99233 | -42.86579 | 2026-01-23 04:33:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c73d043c-581f-363e-a1a7-7cdf2f96e1fb | -7.61965 | -35.09325 | 2026-01-23 04:33:00 | NOAA-20 | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 60c11f87-8fd0-3ffe-b3a1-986d14afcc67 | -9.37849 | -47.06837 | 2026-01-23 04:33:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98511fec-4203-33fe-866b-be016169ff09 | -7.57069 | -46.48588 | 2026-01-23 04:33:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73a09d26-20d0-3c7c-aba8-5ba40d4b8801 | -7.93296 | -48.02035 | 2026-01-23 04:33:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64777924-1105-3443-a8a1-70dcd2b03f0d | -5.0033 | -37.53462 | 2026-01-23 04:33:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e761c6df-6771-34e0-8d18-3e70712529ef | -8.15036 | -43.18628 | 2026-01-23 04:33:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fe07e727-4603-393c-9297-7202eb550a94 | -7.5741 | -46.4864 | 2026-01-23 04:33:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06ede850-8098-3afc-80a1-644c7ade8876 | -7.6119 | -35.09889 | 2026-01-23 04:33:00 | NOAA-20 | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 008338f8-0d15-3813-9176-41a66aa3af88 | -8.38847 | -46.2446 | 2026-01-23 04:33:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e46acfd5-6ffd-3f1b-a449-835143a3cc2f | -8.11624 | -48.02115 | 2026-01-23 04:33:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f497bb7-d799-37e3-a4e0-8bb9911364ee | -15.65602 | -56.02288 | 2026-01-23 04:36:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |


[Clique aqui para ver as próximas entradas](README5.md)
