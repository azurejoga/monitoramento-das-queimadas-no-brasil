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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ec19a09-6117-3556-b527-42106344a41f | -2.31073 | -49.75595 | 2025-11-24 04:36:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58210e71-e3e2-3141-a0ff-d16747728f22 | -3.74237 | -50.96528 | 2025-11-24 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d82f5361-ac66-3d84-b062-2181159f50cf | -3.83671 | -42.75752 | 2025-11-24 04:36:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4e632ac-24dc-3835-841b-7827e6838529 | -3.95491 | -49.52087 | 2025-11-24 04:36:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1acc9410-2149-375c-9f06-4d7fdc65edd2 | -5.26997 | -44.37369 | 2025-11-24 04:36:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29e514ba-7150-326d-89e4-d3cb0a3b12f7 | -3.45428 | -49.24664 | 2025-11-24 04:36:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a820170d-383c-38cb-a0ab-6296f76cc187 | -4.7173 | -46.45871 | 2025-11-24 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57191df1-b3af-3bbb-90fa-95f968da4360 | -4.82582 | -43.82932 | 2025-11-24 04:36:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9f7131ec-0644-3c27-9eca-ff0fe64c6607 | -4.39161 | -45.73051 | 2025-11-24 04:36:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf22797a-d35e-3d97-a919-fd27d69d0653 | -2.13595 | -46.41066 | 2025-11-24 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56c83cce-49d2-36d7-bffc-a2ef0450f2f9 | -2.45297 | -45.3799 | 2025-11-24 04:36:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a671f79-f3b3-352e-b8d3-e9c4aa0202a2 | -1.82876 | -45.57072 | 2025-11-24 04:36:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 036d78da-ce3a-39a3-a186-aaff2d1fd7e3 | -4.39443 | -45.73473 | 2025-11-24 04:36:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b873866b-5914-3a2e-b289-7bbec5ab5664 | -5.71533 | -42.74787 | 2025-11-24 04:36:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 80a8daa8-dfcd-37ae-bf7e-636ae0fac12f | -3.8633 | -42.44627 | 2025-11-24 04:36:00 | NPP-375D | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 18b932c7-8c9c-3082-86fa-29388a25e37c | -4.71786 | -46.4552 | 2025-11-24 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c58448ad-39be-3fc4-9b95-b29e689a0f8f | -12.289 | -51.20749 | 2025-11-24 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79bee6f9-7e8c-394e-bd96-a0cc83fede5b | -9.62257 | -49.65327 | 2025-11-24 04:38:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 37d7c1f8-731a-3f88-ab13-b23ce94b6a4b | -11.52079 | -49.67844 | 2025-11-24 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de3c2742-9efb-37bd-ab5c-37c3333b3ab4 | -8.65916 | -47.85477 | 2025-11-24 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba17ec9d-3f1c-3c3e-84c0-7e411e65cdab | -8.67521 | -47.83937 | 2025-11-24 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 476f76cb-f4eb-3664-a6f8-0a055f452835 | -11.79127 | -49.3201 | 2025-11-24 04:38:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ecab9921-91b6-3ee9-ade5-507926917e65 | -11.7946 | -49.32064 | 2025-11-24 04:38:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55706f4d-d35d-32e0-9b1f-20930136ee48 | -12.96291 | -49.03685 | 2025-11-24 04:38:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7986214-10db-3258-8c83-9f471c133e02 | -8.66249 | -47.85531 | 2025-11-24 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0de5cff1-fbb4-3562-b0f9-7ba82ac5d6a9 | -9.61922 | -49.65273 | 2025-11-24 04:38:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d2ce316d-1dc3-3c7d-b401-c4297d1a1244 | -8.67189 | -47.83884 | 2025-11-24 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e51b2a8-ca20-39c6-8e89-a9b1444faf91 | -11.78463 | -49.31902 | 2025-11-24 04:38:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cffa61e6-98f6-365f-aced-f0ebdcfddba6 | -11.52413 | -49.67899 | 2025-11-24 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3620eb3c-ee4d-399d-8af7-99bd4b93d19e | -12.4048 | -57.41956 | 2025-11-24 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 515e1e33-dc5a-3778-8262-a38e169b4901 | -11.52022 | -49.68199 | 2025-11-24 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ca401fb-6dc1-3aa3-ba97-c00bd72b4d6d | -10.68173 | -51.83984 | 2025-11-24 04:38:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63862ae7-a4f6-3a00-89db-f133252b8434 | -11.3335 | -49.02942 | 2025-11-24 04:38:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cdc36c6c-375f-3a5d-bc00-58f3807d2bf3 | -11.78795 | -49.31956 | 2025-11-24 04:38:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 54dd7cef-bf63-3570-97cc-09828db5ed05 | -11.78851 | -49.31604 | 2025-11-24 04:38:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0b12ff4a-8f97-3e5c-a665-64e9d7f9a1bc | -9.2951 | -40.36506 | 2025-11-24 04:38:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 69933da4-2a3a-35d4-bd15-0ded3ffb58f0 | -9.29515 | -40.3662 | 2025-11-24 04:38:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 25e2d18d-fbcc-32c3-a4c7-e4460a418cc5 | -16.76851 | -51.35478 | 2025-11-24 04:40:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 932a29c1-62e2-3683-aebb-bb09fef0eb97 | -17.13692 | -50.26262 | 2025-11-24 04:40:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca0bdeec-788b-3ecb-929d-4538b93a5801 | -19.17843 | -57.33057 | 2025-11-24 04:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 133cefa0-59d5-3318-91e3-d7a7a383f094 | -19.18275 | -57.33151 | 2025-11-24 04:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 636c35c5-d9da-330a-864f-fea5e5ad9816 | -17.54843 | -54.03893 | 2025-11-24 04:40:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae6ae146-2f8a-3b55-8435-6effa5769850 | -19.18361 | -57.32716 | 2025-11-24 04:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9830eff4-6e6e-37f6-9bf5-811f95de5c0f | -18.62827 | -50.86947 | 2025-11-24 04:40:00 | NPP-375D | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7744acb0-383e-39d5-9173-a03bd2330a42 | -19.21903 | -57.33035 | 2025-11-24 04:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c82ab770-96b4-3948-9162-bb080b7ebe3e | -17.54476 | -54.03822 | 2025-11-24 04:40:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ad429be-f05f-39a9-8323-e14b5a755a3e | -16.76516 | -51.35418 | 2025-11-24 04:40:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 394256b9-f22e-305b-99ff-64f6449346e0 | -15.67473 | -52.63809 | 2025-11-24 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 09d86186-e22e-3659-8fc0-c5ac6739aff5 | -16.76241 | -51.34991 | 2025-11-24 04:40:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7b74dd5a-d841-3eb9-9465-805a133e3a09 | -16.51765 | -52.37775 | 2025-11-24 04:40:00 | NPP-375D | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9644998a-f99b-39ef-a353-957f92e18b06 | -17.13412 | -50.26263 | 2025-11-24 04:40:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fbee7414-439b-3957-ae86-a510d9fc42ca | -19.18708 | -57.33246 | 2025-11-24 04:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 48cdd20b-c308-3f69-a720-f3c2a5f31e10 | -29.08078 | -50.73056 | 2025-11-24 04:42:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cccd6e02-d514-3130-9222-d3532ae402be | -29.08018 | -50.73495 | 2025-11-24 04:42:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8bf5af65-e46a-39e5-b746-6cd5cfcf0f59 | -29.90904 | -51.69417 | 2025-11-24 04:44:00 | NPP-375D | TRIUNFO | RIO GRANDE DO SUL | Brasil | 4322004 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| c9b1d026-9858-3797-8b3b-7fa0821a2f90 | -3.03347 | -47.79123 | 2025-11-24 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5042251a-3a1e-38db-8baa-1c824873358c | -3.21795 | -45.93707 | 2025-11-24 04:55:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79a5fd7a-d3c5-37c3-86af-91d78290c063 | -0.18686 | -50.10357 | 2025-11-24 04:55:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0683a2f9-a323-3468-8466-384d64bd55e4 | 3.10781 | -60.77419 | 2025-11-24 04:55:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49f49514-322d-3d4f-84d0-725fcb09e12b | -2.88147 | -51.81666 | 2025-11-24 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1675c78e-a056-3031-b9b6-98e4263b2213 | -1.77039 | -53.97746 | 2025-11-24 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a079722c-731f-3315-a863-f02aa39f3e39 | -4.26211 | -40.86185 | 2025-11-24 04:55:00 | NOAA-20 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 90bf3894-42cf-34b1-ba1a-fe92f959ff2c | -2.46572 | -48.11627 | 2025-11-24 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ccec674f-05f3-316f-a4e5-e32456d17575 | -2.79982 | -45.36623 | 2025-11-24 04:55:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cca1285f-e640-3c81-a7df-4ed74ab2f772 | -2.13979 | -46.41592 | 2025-11-24 04:55:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d16cd209-6164-32a5-b9a6-92e54c03b150 | -2.79656 | -45.3541 | 2025-11-24 04:55:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cb1578e5-079c-3c76-acbd-5c14cb4296ea | 2.33511 | -50.77929 | 2025-11-24 04:55:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82dc5dd2-9e5f-3f7b-98d9-385764f52f9e | -2.87977 | -51.80526 | 2025-11-24 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fcadc1e8-9548-3528-baa2-af24f47e2f89 | -2.13521 | -46.41527 | 2025-11-24 04:55:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0c3aad89-3d5a-367b-b105-cd35f5af0ed0 | -3.71335 | -44.00592 | 2025-11-24 04:55:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 73fd2bdb-60ce-3c47-b6f6-9ac947f2ab5c | -2.87074 | -51.79641 | 2025-11-24 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53bbf6bc-ee05-3f7a-a872-0c4f5950bcbf | -3.71354 | -44.00557 | 2025-11-24 04:55:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97953865-1956-3a3e-a514-c10ad438da78 | -3.21949 | -45.92665 | 2025-11-24 04:55:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 59f302b1-c906-397c-8c25-6f848a86e84f | -2.76747 | -48.95569 | 2025-11-24 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 173bee94-d684-311c-9ef5-a6dbfcc8cfe4 | -3.17296 | -50.24275 | 2025-11-24 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| efa11ded-eaf8-3e1e-b229-89ef02563459 | -2.29409 | -53.9107 | 2025-11-24 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8901ee8-cdec-3540-8802-0ccf2234400b | -3.21872 | -45.93187 | 2025-11-24 04:55:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ce7a78a9-d966-385c-9283-a33da5ff44a8 | -3.21385 | -45.93423 | 2025-11-24 04:55:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9aa4293c-3c3e-3427-80c9-d66ddb9e7e3a | -2.22446 | -51.78272 | 2025-11-24 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 887b9310-10d3-3349-b43d-e2b2b7201ddc | -1.75979 | -53.89377 | 2025-11-24 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1913e6e3-933b-3dfa-b7ec-c5e3b473857e | -2.93522 | -51.76164 | 2025-11-24 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dec8aa2b-c309-3089-b43c-6bb5155d0fc8 | -3.2183 | -50.16746 | 2025-11-24 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 068540a8-ea2a-3106-b560-49a539a31693 | -2.93073 | -48.234 | 2025-11-24 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e675523c-e267-353d-be9e-4bb912ef7891 | -2.87865 | -51.81252 | 2025-11-24 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3082dfc-36e0-3c46-8849-32e014f9b555 | -3.5956 | -40.97909 | 2025-11-24 04:55:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fc4128b5-8bfb-3342-baba-c068a0c27a07 | -2.71484 | -51.89087 | 2025-11-24 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33056b38-8bb5-36a7-91b1-894de7402b26 | -1.33997 | -53.17564 | 2025-11-24 04:55:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb194f6a-d16b-3539-b920-8804055fa412 | -3.28868 | -43.4054 | 2025-11-24 04:55:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 42024af2-60a9-3654-a271-5e3392c475cf | -2.88316 | -51.80578 | 2025-11-24 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e84edbae-0b52-3529-9c33-43d47855461e | -2.25056 | -50.65571 | 2025-11-24 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21fcb6e5-e7f6-33fa-95c2-5445180e8e07 | -2.87017 | -51.80004 | 2025-11-24 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e6b5282-2ed3-3fb8-aa4c-3f70c6408f87 | 3.80531 | -60.19085 | 2025-11-24 04:55:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9a7c490-b26e-3e12-b371-02444dd1e9fa | -2.1056 | -47.10032 | 2025-11-24 04:55:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ae6817f-16de-365b-8b15-27cfcb361a34 | -2.86961 | -51.80368 | 2025-11-24 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a0f66ce-d6c2-3b47-8dee-2cfe0414399c | -2.7012 | -49.51864 | 2025-11-24 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45d9e095-9c3c-3079-998f-454f2d1dce9f | -4.26126 | -40.86768 | 2025-11-24 04:55:00 | NOAA-20 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8529e333-e4c1-32b5-a42f-491ae974defd | -2.88542 | -51.81356 | 2025-11-24 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ecb51fe-0247-3b61-a726-2458eed358be | -2.88151 | -45.26583 | 2025-11-24 04:55:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0501068-45da-3a37-a1d6-a52de09d52ca | -2.87639 | -51.80473 | 2025-11-24 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c2b33b3b-783a-3d13-80e5-db29ba0ab4e6 | -4.26895 | -40.86246 | 2025-11-24 04:55:00 | NOAA-20 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |


[Clique aqui para ver as próximas entradas](README11.md)
