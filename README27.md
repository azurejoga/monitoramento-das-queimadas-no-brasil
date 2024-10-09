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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7002a1d9-76bf-33ee-905f-3768257518ee | -20.55123 | -49.34465 | 2024-10-09 01:11:00 | TERRA_M-M | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ba3ccab6-7124-3be4-9f1c-83ea5756a4bd | -20.5499 | -50.12207 | 2024-10-09 01:11:00 | TERRA_M-M | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 44.7 |
| 09181a63-5bca-3d02-8880-3697ab5b244e | -20.5486 | -50.11263 | 2024-10-09 01:11:00 | TERRA_M-M | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 76403b4b-4001-3267-90a1-5f7731710cb5 | -20.54235 | -49.34612 | 2024-10-09 01:11:00 | TERRA_M-M | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d9bca9a6-9e1a-3fc8-8b24-845c32cb3e4e | -20.47695 | -47.17421 | 2024-10-09 01:11:00 | TERRA_M-M | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8edccc82-915e-393c-ba61-e196ee35865a | -20.43789 | -43.93161 | 2024-10-09 01:11:00 | TERRA_M-M | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| fbad57e6-7f08-3dc9-8900-eb1ff5af07e7 | -20.42677 | -47.98932 | 2024-10-09 01:11:00 | TERRA_M-M | IPUÃ | SÃO PAULO | Brasil | 3521309 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c9515f33-0e55-30b0-b665-ddbb58f21937 | -20.40599 | -48.84735 | 2024-10-09 01:11:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 0eb73d53-4dc0-3b9a-8a5b-c853aec3ee78 | -20.40459 | -48.8377 | 2024-10-09 01:11:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 216d6173-f1d9-3319-ae03-dcee6e1c4549 | -20.39885 | -43.9198 | 2024-10-09 01:11:00 | TERRA_M-M | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 469ad3a6-8c2c-3f13-b1b3-146839da0f8f | -20.3698 | -48.72467 | 2024-10-09 01:11:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 19.2 |
| c761af20-78af-3894-a9bd-a404b2f01a1f | -20.36839 | -48.71499 | 2024-10-09 01:11:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 9e1c9b37-3d5f-3205-888b-d9006cabdd81 | -20.36223 | -48.73589 | 2024-10-09 01:11:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 6341bc62-e5fe-34ae-819a-4ef4fcc33b70 | -20.36081 | -48.72617 | 2024-10-09 01:11:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 7a728e10-70ee-35bc-95ab-f7a9214e3ced | -20.36031 | -48.78583 | 2024-10-09 01:11:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f44ab69e-4869-308e-a1d3-c62d14316309 | -20.3594 | -48.71648 | 2024-10-09 01:11:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 6eeb274e-6dd9-335e-8b9f-32d84ce7fa48 | -20.3589 | -48.77615 | 2024-10-09 01:11:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 86645395-5e10-395d-8e21-06ad10bbdd06 | -20.35183 | -48.72773 | 2024-10-09 01:11:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 170.3 |
| e16b7d89-b207-33b6-9f0a-024584c97e34 | -20.35135 | -48.78738 | 2024-10-09 01:11:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9dccd279-fd56-3ba1-9db7-ea1f444204ce | -20.35041 | -48.71804 | 2024-10-09 01:11:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 303.9 |
| 62da5f3f-9291-3d45-b934-71fb12f0365e | -20.34993 | -48.77769 | 2024-10-09 01:11:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c2429818-c9db-3de9-a3ca-76d241f518b1 | -20.34285 | -48.72928 | 2024-10-09 01:11:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 83.2 |
| f1d747d0-0dda-3e7d-9d51-2152fcb819d9 | -20.34143 | -48.7196 | 2024-10-09 01:11:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 246.2 |
| de896780-1dce-3309-a82c-7619525d5fe3 | -20.33532 | -46.21687 | 2024-10-09 01:11:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 6c47e440-93de-3a27-a965-a664ddd8886c | -20.33386 | -48.73079 | 2024-10-09 01:11:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a59c3444-0082-3b29-9971-adf334fe5df5 | -20.33244 | -48.7211 | 2024-10-09 01:11:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 73b8f192-84f5-32a7-878c-95886fe37476 | -20.28962 | -43.9652 | 2024-10-09 01:11:00 | TERRA_M-M | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| e1b380ba-785f-356c-9cb1-d7b5725a0633 | -20.28682 | -43.94949 | 2024-10-09 01:11:00 | TERRA_M-M | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.9 |
| 94a07860-ff91-3d25-943c-fc2c1e232998 | -20.28193 | -43.95549 | 2024-10-09 01:11:00 | TERRA_M-M | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 54.7 |
| 6d9eb8a4-0be4-3314-ab80-627a3e4875f2 | -20.27778 | -43.96795 | 2024-10-09 01:11:00 | TERRA_M-M | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| b73f317e-0414-3a06-93c6-e08a3d1afd3d | -20.27513 | -50.39556 | 2024-10-09 01:11:00 | TERRA_M-M | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.5 |
| 834b3e49-9e4c-329d-9645-bd49bf382a84 | -20.27491 | -43.95191 | 2024-10-09 01:11:00 | TERRA_M-M | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| a749cacc-0a74-3858-9dc4-2702fe7564e2 | -20.2701 | -43.95839 | 2024-10-09 01:11:00 | TERRA_M-M | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.3 |
| e9700310-06ae-37fb-aaa3-4ea2e7faedbd | -20.17575 | -50.61679 | 2024-10-09 01:11:00 | TERRA_M-M | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 51314c8f-57d7-31f1-a0ab-0c133ef756c1 | -20.12128 | -48.85398 | 2024-10-09 01:11:00 | TERRA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8e6833c3-08e0-3943-96f3-dc891333f3d7 | -20.11988 | -48.84429 | 2024-10-09 01:11:00 | TERRA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e5083ea1-e985-3e7c-8f54-33cc537f332f | -20.11848 | -48.83464 | 2024-10-09 01:11:00 | TERRA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b831e05a-20a8-3c1c-b453-e82b0226f25c | -20.1109 | -48.8458 | 2024-10-09 01:11:00 | TERRA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bbc6d1bf-f000-339a-afeb-0506dfac4c0c | -20.1095 | -48.83618 | 2024-10-09 01:11:00 | TERRA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 454d2c5f-19cf-3b61-bdfb-3d5b2fa484f6 | -20.1081 | -48.82651 | 2024-10-09 01:11:00 | TERRA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 85.1 |
| d7464cb3-6281-36d2-a051-458426e7f459 | -20.10669 | -48.81684 | 2024-10-09 01:11:00 | TERRA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 1ee78819-20a8-35d2-8ba9-ea16ba30ded6 | -20.10558 | -44.21826 | 2024-10-09 01:11:00 | TERRA_M-M | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| 71621df2-55bf-3bbf-8644-5b41c8c31a13 | -20.09968 | -55.96263 | 2024-10-09 01:11:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.0 |
| 027fd264-5c11-3cf4-a284-0265271aa4ac | -20.09772 | -48.81837 | 2024-10-09 01:11:00 | TERRA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 06fe9dab-e6b7-3482-a32f-8a6ef39ffb56 | -20.09765 | -55.94421 | 2024-10-09 01:11:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| e53ace5a-5f4f-3949-9f47-c7eefa766ca6 | -20.0963 | -48.80869 | 2024-10-09 01:11:00 | TERRA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| efdb7cf0-d140-3f2c-ae50-2be885c9690a | -20.0531 | -46.3785 | 2024-10-09 01:11:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 94662497-55ac-3c11-a493-59e4b8873d88 | -20.01215 | -42.44822 | 2024-10-09 01:11:00 | TERRA_M-M | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 99.3 |
| bbf923c0-6fab-3aa0-81ec-8d81fbe76dfb | -20.01205 | -48.23687 | 2024-10-09 01:11:00 | TERRA_M-M | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 0fce277f-6a70-307e-b4e9-25418ca98c2e | -20.01054 | -48.22673 | 2024-10-09 01:11:00 | TERRA_M-M | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ec392fe3-573f-3744-8eea-491058fe52e9 | -20.00779 | -42.42503 | 2024-10-09 01:11:00 | TERRA_M-M | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.5 |
| b8f409e1-3d5c-3479-815f-8b47191c2c7b | -20.00491 | -42.45548 | 2024-10-09 01:11:00 | TERRA_M-M | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 88.8 |
| 1743b91f-46ed-3f57-b613-12943091da20 | -20.00072 | -42.43238 | 2024-10-09 01:11:00 | TERRA_M-M | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.2 |
| 66ab5b33-b0fc-3160-a461-0aa3cf816b19 | -19.99874 | -42.45109 | 2024-10-09 01:11:00 | TERRA_M-M | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.7 |
| 6a302a12-1e7b-383f-a447-9b1473c5ab6b | -19.99549 | -42.20911 | 2024-10-09 01:11:00 | TERRA_M-M | VERMELHO NOVO | MINAS GERAIS | Brasil | 3171154 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.5 |
| b94049b6-92d2-3b74-884d-292d6eb03166 | -19.9911 | -42.18564 | 2024-10-09 01:11:00 | TERRA_M-M | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.0 |
| 30c5c074-cb5e-3aea-a3d5-1f4c1803fd7d | -19.98212 | -46.70538 | 2024-10-09 01:11:00 | TERRA_M-M | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8569d492-b4e1-3570-877f-f410d3a21e9f | -19.97394 | -42.43864 | 2024-10-09 01:11:00 | TERRA_M-M | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.5 |
| 715e4a86-f639-3e5b-b2fc-574b2211d67b | -19.84603 | -42.39888 | 2024-10-09 01:11:00 | TERRA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 9dc2d157-7661-3d7d-b9cb-4efac010502b | -19.83246 | -42.40145 | 2024-10-09 01:11:00 | TERRA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.8 |
| dc62522a-2439-3448-a213-b368c32b2c8d | -19.82844 | -42.37991 | 2024-10-09 01:11:00 | TERRA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.6 |
| 44c4456d-13a1-30ec-8015-78f2a0edc3a7 | -19.82358 | -43.80349 | 2024-10-09 01:11:00 | TERRA_M-M | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| fc8586bb-8160-3cb6-aa63-c50131133981 | -19.82165 | -42.38606 | 2024-10-09 01:11:00 | TERRA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.4 |
| 7193a625-1638-356d-a09e-5c9642e12997 | -19.81119 | -52.24677 | 2024-10-09 01:11:00 | TERRA_M-M | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bc4e6d03-52d1-3aba-9bf3-1b5f7ec04b6b | -19.80531 | -42.40652 | 2024-10-09 01:11:00 | TERRA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.3 |
| d80656ad-7aba-37c3-ad59-a62c33dc0c00 | -19.79852 | -42.41345 | 2024-10-09 01:11:00 | TERRA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.5 |
| 329d33e4-86ae-3ad9-9b46-f2279aae0faf | -19.77605 | -48.2692 | 2024-10-09 01:11:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 05f783bf-0d3f-36a3-bcad-e7a232bdcc89 | -14.08123 | -44.14153 | 2024-10-09 01:11:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| d722aaca-55a7-3130-b974-b46b79596de3 | -19.76915 | -42.83727 | 2024-10-09 01:11:00 | TERRA_M-M | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| df0cd8a7-a80c-36f7-a8b7-69b5c8d6c722 | -19.64671 | -56.57391 | 2024-10-09 01:11:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| bbacdd4b-08ea-3e5f-8045-f02932a2a3ed | -19.28289 | -42.85297 | 2024-10-09 01:11:00 | TERRA_M-M | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 7b5e262e-34a2-318f-8c79-b0bc9087956c | -19.1143 | -40.97821 | 2024-10-09 01:11:00 | TERRA_M-M | RESPLENDOR | MINAS GERAIS | Brasil | 3154309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| fe73d3cf-ce8d-3c18-b069-d896173bdb34 | -19.10838 | -40.94772 | 2024-10-09 01:11:00 | TERRA_M-M | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| 45f8bf66-9594-33f7-a081-6c6519ee1952 | -18.9339 | -54.55376 | 2024-10-09 01:11:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e5602af8-8097-3c57-a74a-9ef8ea3ec3d9 | -18.92313 | -54.55472 | 2024-10-09 01:11:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 13.8 |
| ecc77ab3-29ef-3bc7-8f4f-42361a886cf9 | -18.91573 | -54.5843 | 2024-10-09 01:11:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 9fc6e359-f2f8-3c4b-b413-a1e559ff50e3 | -18.87134 | -54.57751 | 2024-10-09 01:11:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0870f661-99e0-35d6-92f7-3b124508a1f3 | -18.86792 | -54.58382 | 2024-10-09 01:11:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6843ddba-9923-355b-b308-7309bf88f1fc | -18.6046 | -57.28214 | 2024-10-09 01:11:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 1540771c-ad95-3349-ae62-e49b832d1bbc | -18.60226 | -57.26027 | 2024-10-09 01:11:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.1 |
| 6410151e-65f1-3e56-be77-20fa1ad16e18 | -18.6014 | -57.2771 | 2024-10-09 01:11:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.7 |
| 456fd389-f8d0-3883-b7e4-c5beebea065b | -18.60081 | -42.34677 | 2024-10-09 01:11:00 | TERRA_M-M | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.4 |
| 7762f439-d137-36ec-95d4-bb34e0b0c52b | -18.59992 | -57.23849 | 2024-10-09 01:11:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.4 |
| 4ad210f0-654d-3e76-908f-aed688a7921e | -18.59921 | -57.25521 | 2024-10-09 01:11:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.4 |
| 84c3dc91-0ad1-33ed-912b-3bbe046af1b4 | -18.59107 | -42.3416 | 2024-10-09 01:11:00 | TERRA_M-M | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.5 |
| 4ea597f5-847e-3fc1-9961-8281a0597b94 | -18.5891 | -57.26177 | 2024-10-09 01:11:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 48f1bf87-7b6b-3217-8f99-1cb8d0b9095f | -18.49047 | -53.50198 | 2024-10-09 01:11:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 21.7 |
| b5fa6a6e-2d2f-3192-b6f7-fd4abe13345b | -18.48902 | -53.49012 | 2024-10-09 01:11:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0209978a-ac87-3ed3-a882-ac35baf773c5 | -18.48053 | -53.5031 | 2024-10-09 01:11:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 396658a7-b70a-311f-afeb-07e6408cf81f | -18.24361 | -42.22613 | 2024-10-09 01:11:00 | TERRA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.9 |
| df2d3377-06a8-3b92-a37c-992ba6b493d2 | -18.24203 | -42.94653 | 2024-10-09 01:11:00 | TERRA_M-M | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| 64578a19-2099-36c5-825e-cae5c5fad4e8 | -18.23463 | -42.95359 | 2024-10-09 01:11:00 | TERRA_M-M | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.3 |
| 6a4c46a0-1145-3786-ba70-71085a2f2a7b | -18.18881 | -42.58372 | 2024-10-09 01:11:00 | TERRA_M-M | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 61647867-e462-3cf2-8324-f871d8577d5b | -18.18387 | -42.59045 | 2024-10-09 01:11:00 | TERRA_M-M | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.5 |
| 60802692-e14b-32bd-acaa-4d11131a7af4 | -18.01378 | -42.14127 | 2024-10-09 01:11:00 | TERRA_M-M | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.8 |
| 34bb8497-95d7-337e-8df5-5ea4b543be04 | -18.01167 | -42.14819 | 2024-10-09 01:11:00 | TERRA_M-M | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 44.9 |
| ed3c3484-1707-37ad-885c-dfdfa9e8b7c2 | -18.00695 | -42.12217 | 2024-10-09 01:11:00 | TERRA_M-M | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 37.7 |
| 01c9b9d1-71b9-346d-b4c0-8e0eab80598e | -18.0046 | -44.57117 | 2024-10-09 01:11:00 | TERRA_M-M | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 0deaa0db-e490-3c1d-ab1a-7c35b6fa1b66 | -17.99951 | -42.14448 | 2024-10-09 01:11:00 | TERRA_M-M | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 37.7 |
| a8b1063f-1fd0-3eef-9089-ba1de9f14e80 | -17.99265 | -44.57323 | 2024-10-09 01:11:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 39.2 |


[Clique aqui para ver as próximas entradas](README28.md)
