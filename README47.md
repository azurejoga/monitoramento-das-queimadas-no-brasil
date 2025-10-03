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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f64f5b8f-38ef-34c1-915f-19b311604f0b | -5.56129 | -47.22511 | 2025-10-03 04:10:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c9f6506-78ed-32f6-bcdf-b9ac1ccbddd7 | -7.31121 | -45.26565 | 2025-10-03 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 816b3534-cdab-3e7b-9a4f-0735b12d3040 | -7.75825 | -46.27883 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 3556e413-db27-3ce7-9d52-f207b404f790 | -6.27418 | -44.04991 | 2025-10-03 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6d6b01f5-42a4-3306-9522-2192b0480eec | -7.84952 | -42.85898 | 2025-10-03 04:10:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e8879f54-f760-38c7-9ed4-f655e988c48c | -4.0489 | -40.50689 | 2025-10-03 04:10:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cbf4458d-e8a1-31c0-938b-a0838544e6b0 | -6.5339 | -43.37288 | 2025-10-03 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 160c8666-7cf4-33cd-a9f6-610bfc2246c0 | -5.64257 | -43.91719 | 2025-10-03 04:10:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c176fbae-2a9f-362a-afa1-704bcd91f614 | -7.76259 | -42.5989 | 2025-10-03 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d6e404a3-70a3-300b-a4c0-a0c6cf536d37 | -6.67511 | -42.82103 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| af002764-ea0e-3929-bc23-e5660300d5c5 | -6.27748 | -42.42717 | 2025-10-03 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 77edc28b-3894-370b-84cd-11e4b1bb38cc | -5.26309 | -42.91285 | 2025-10-03 04:10:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 73759d90-7dad-3025-bda6-ad151c3bac41 | -6.68207 | -43.71156 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0097ab48-9e2a-370a-b785-65eaed581685 | -6.57703 | -42.12208 | 2025-10-03 04:10:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| efd220e6-e26a-3e47-9558-39d511164c43 | -7.31611 | -42.87605 | 2025-10-03 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7558e7de-e65e-3e27-a49a-9ad9af1b59d4 | -6.97231 | -44.39363 | 2025-10-03 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 320418ad-8e8a-3090-ad2a-7e46e57303c0 | -6.66341 | -42.78632 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 55f6c7a3-59f6-3362-a803-afa5387e7c72 | -7.76372 | -42.59184 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 366ea330-c977-3648-b388-d89259ebeb00 | -6.33833 | -44.03144 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61ae40fe-cec8-3f4b-8720-52fc6c906a8d | -7.7894 | -42.55988 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a38798ae-69ed-33eb-9552-b67009d0316a | -6.34627 | -43.40824 | 2025-10-03 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5461c328-fac7-3564-90ed-7e0937a44205 | -5.34349 | -43.7585 | 2025-10-03 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0f40d0c-55ff-36bf-b3ec-72f80fdd5363 | -7.56134 | -42.39705 | 2025-10-03 04:10:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cc11b9c4-6b1b-3382-a27c-419021d4bca5 | -2.92158 | -48.30891 | 2025-10-03 04:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 940fd8b7-f7a0-3ae4-a1c0-c3ffcbc2234a | -5.62628 | -44.70486 | 2025-10-03 04:10:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 88f5eb2d-b99f-3239-8d9e-6b46b438286e | -3.67029 | -38.80787 | 2025-10-03 04:10:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 647f2dce-c2fc-3036-ac02-2e2b9ce629a9 | -6.52988 | -43.37601 | 2025-10-03 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9697a26c-9081-34ab-8e58-e5639a4f5398 | -7.55508 | -42.39971 | 2025-10-03 04:10:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4c6ae9ba-cdba-35f5-a66b-97be5767857a | -7.77266 | -42.57883 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bd56de13-0a24-375e-9f26-7b3506c4cf30 | -7.75374 | -42.56859 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| d86ef692-1e03-328a-bbd9-ab51d4ffd6a3 | -8.54214 | -41.15051 | 2025-10-03 04:10:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 79352e7c-d575-3cc4-97bf-6acd4d118540 | -8.25028 | -47.03817 | 2025-10-03 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2b0fa720-3c8f-3213-b1f4-955404abc07d | -6.64736 | -43.59736 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b1bfe3b-456b-3401-ab99-60e1734a4f2a | -5.63617 | -43.91209 | 2025-10-03 04:10:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4385b2e5-b083-3227-98ef-8cc492e5f654 | -6.5187 | -43.94389 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1eb33aa6-93e8-3447-89b3-08d10a30ec52 | -7.42467 | -40.07519 | 2025-10-03 04:10:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4691b4a3-e61a-3243-9f99-54c7953bb26b | -6.03084 | -44.62674 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be79958f-5a01-3d06-bc53-ba0dac95711d | -7.76231 | -46.25449 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 42a5d019-d92e-3e5c-9bff-e3dbb9792beb | -8.5841 | -44.77104 | 2025-10-03 04:10:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40fefbba-40b7-3be5-81d7-2de85caa61e1 | -5.71548 | -49.25632 | 2025-10-03 04:10:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 20b4a063-f93e-3df2-b90d-c4354fc3aa17 | -6.64028 | -41.27318 | 2025-10-03 04:10:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 22865876-e0d0-3018-9d41-126d98128311 | -6.33214 | -43.89151 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 136bc405-5668-30b3-97b8-76054e028db8 | -6.70662 | -42.7969 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c097d883-ce92-3ff6-8a9c-39de07108c8e | -3.66683 | -38.80732 | 2025-10-03 04:10:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e81999ba-e4aa-3063-b2b8-09692d57690a | -6.2373 | -45.36383 | 2025-10-03 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34d84458-7ce1-3920-a7e0-af21656bc0cc | -8.59276 | -44.78468 | 2025-10-03 04:10:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 039d264c-ed3c-351f-b470-db436bf101cc | -3.6697 | -38.81164 | 2025-10-03 04:10:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6908895c-7ac2-332a-b0e5-bfabc19eb6cf | -6.72667 | -44.15305 | 2025-10-03 04:10:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efb22eff-c130-3127-8c13-01b5100c69f2 | -7.68425 | -47.7654 | 2025-10-03 04:10:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adc6ceae-37ac-3510-afdc-6dbde4b359e4 | -7.75925 | -46.24894 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 7672a47e-3a92-3239-9e68-5bcbb6e08021 | -8.305 | -44.84862 | 2025-10-03 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5579b6e7-bd1c-3073-99db-788f20b4d231 | -5.78099 | -45.76587 | 2025-10-03 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f17d2e48-775b-3cb4-bed2-9eea4e497355 | -6.35176 | -43.4396 | 2025-10-03 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6756750f-10c9-3829-a364-257c9b3af725 | -7.7704 | -42.59293 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3c4829cb-a913-31f3-95b7-4732e32b92a1 | -6.22776 | -44.24587 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0ebf8fbd-b72d-3f21-a527-99d1a2cdc111 | -5.40025 | -41.33004 | 2025-10-03 04:10:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| eaba5d8d-7bce-3083-b6c8-dd3c1dac6a4f | -5.40303 | -41.33403 | 2025-10-03 04:10:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| dab9b797-8588-369a-8fc1-234f21d1e96a | -6.35976 | -42.8894 | 2025-10-03 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f5ad5e71-56b2-37d5-a0bd-2c1e808f1f84 | -7.71997 | -46.19821 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7618e817-09e7-3d64-a1d3-3363dde63fa0 | -7.76601 | -42.55615 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8a44c54e-cb51-34f4-959a-305f82dae7bc | -6.37974 | -44.64029 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfff9618-423e-3a24-b784-31f6396c5ff1 | -3.55931 | -51.12577 | 2025-10-03 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ec666ae-d533-3e88-b28a-1f09ede20002 | -6.95021 | -45.35138 | 2025-10-03 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| eefa1341-1402-3aaf-8271-c5923df8ca42 | -5.91134 | -43.90514 | 2025-10-03 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c842d198-7bb2-3a9d-843a-2f9f6d9d2c25 | -6.95393 | -45.35201 | 2025-10-03 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 608614bd-ac9f-319f-acb3-eaebbe79bc97 | -4.3161 | -48.09873 | 2025-10-03 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc4db948-a8e7-35a9-b5a1-1a47921dcccf | -8.23526 | -39.02795 | 2025-10-03 04:10:00 | NPP-375D | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ef1f4ebd-271d-3de2-b3ff-1bada3155a11 | -6.59036 | -42.10272 | 2025-10-03 04:10:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7644c02b-03b3-3603-831e-49d258149370 | -3.84699 | -41.56846 | 2025-10-03 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| bd113c98-273e-3f34-bda8-56a6b78e5e79 | -7.7588 | -42.53698 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a786d625-b224-3d20-bd17-a257655b6da1 | -5.97797 | -44.07336 | 2025-10-03 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49bc615a-c110-3357-8eff-caeef8779175 | -7.78268 | -42.58045 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 360a1e4e-a526-32ee-bf92-a8eae14de16c | -7.80224 | -42.52233 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 5e81f650-9cef-3ea0-a451-c67d34e6e91c | -7.1574 | -44.99509 | 2025-10-03 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5c9304c0-a3a8-3f4f-9d01-87eddfc185eb | -6.87938 | -45.4777 | 2025-10-03 04:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d735d582-fdb1-3ed2-b4a4-f32e9713f37f | -7.55757 | -42.65607 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2a5f167c-dcc0-3831-b8c6-ac899b3cac10 | -6.33276 | -43.88769 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5dc6b8eb-0dd3-3636-b9c2-89131022b224 | -6.33659 | -43.03398 | 2025-10-03 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f459e1e-4ea5-3934-afe5-be688a2912a1 | -7.87857 | -47.34073 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73165573-2e9e-3d2a-bcb0-f721fb4fc2da | -7.07426 | -45.81755 | 2025-10-03 04:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c562f378-a60f-33c7-a095-38be277dafba | -6.04899 | -44.62962 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43b12d9a-402f-3cd1-a55d-18adf790c0a6 | -5.94122 | -42.88599 | 2025-10-03 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3fb12cba-b038-3c4b-adfd-fe47c4e0ae10 | -6.70713 | -42.81531 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| abc82f71-32eb-3fe4-8ce5-f8ea0649111b | -5.33087 | -43.52739 | 2025-10-03 04:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e416e29-1acb-3aa3-9dd5-b2fae0d709bf | -7.90726 | -43.54151 | 2025-10-03 04:10:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 63bac8ae-0aba-35db-bf26-5b7fa8def8e1 | -7.90444 | -43.53726 | 2025-10-03 04:10:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1f4201ee-8e9d-3852-80b1-121754bdb998 | -6.24107 | -45.36442 | 2025-10-03 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6e028ca-4aa1-38f4-842b-75d8d8e63bd8 | -6.20047 | -45.91814 | 2025-10-03 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8c48ad24-b9cb-3b3b-a391-a9ad88c98e07 | -5.63201 | -43.91541 | 2025-10-03 04:10:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e2b94ec-5e17-31dd-8556-364bf4ffeeae | -4.8084 | -46.81608 | 2025-10-03 04:10:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eedb18c3-25ad-398e-8781-a5aaab3f8f6f | -6.23815 | -44.22684 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1f708528-9199-3d88-9418-b6fef3005284 | -5.64158 | -43.90101 | 2025-10-03 04:10:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b8b9a5e8-0e15-3971-aac5-ef9268232d36 | -7.78493 | -42.56638 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ca27d13b-4e7a-3a5e-a869-1b25a25bff10 | -7.75541 | -46.22425 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 705fd4a2-edcd-3576-a482-4d80dfea8928 | -7.77656 | -42.57585 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 594648ed-0cc9-3627-a66a-1cfed14833ca | -4.65473 | -47.54863 | 2025-10-03 04:10:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd881d1b-dd03-3a45-977c-b245416f9893 | -7.76094 | -42.58778 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 08d7f7ba-3ba5-3cb9-a0ea-597d7ab49b35 | -7.78217 | -47.37151 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 028bf4ec-6f2c-3885-be0d-d44d055a56a1 | -3.99695 | -38.9872 | 2025-10-03 04:10:00 | NPP-375D | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 54f4cbbb-d0af-39dd-a04d-6686e336a194 | -6.56145 | -43.88326 | 2025-10-03 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README48.md)
