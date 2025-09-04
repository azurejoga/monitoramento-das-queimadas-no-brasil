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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59e535cf-5ee3-382f-8850-966a0f108740 | -18.20315 | -49.72321 | 2025-09-04 04:29:00 | NOAA-21 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0a88546-93a9-370e-a7a6-51eccb82670d | -16.46346 | -49.51365 | 2025-09-04 04:29:00 | NOAA-21 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53463e56-84be-370d-a22d-14755edd2d0f | -15.54622 | -48.34134 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2d93770-fde1-37be-9ea1-a0b42bcc95e5 | -15.24519 | -53.79839 | 2025-09-04 04:29:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47798075-7a10-32c3-9f6d-4b13cd4f5910 | -16.46014 | -49.51307 | 2025-09-04 04:29:00 | NOAA-21 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85021fd1-5121-3c9b-bfd2-756b7118645d | -17.1714 | -46.22782 | 2025-09-04 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 50aa6331-875f-3b7b-a4ad-5018ba41dcdd | -17.04663 | -46.49045 | 2025-09-04 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 842027a3-e822-3ff1-8718-f6cadbfd7494 | -15.86138 | -52.3049 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4ba75678-b428-3b5e-bea7-3b9b0395b8cd | -20.10125 | -50.00521 | 2025-09-04 04:29:00 | NOAA-21 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 1bf065d3-55b5-3227-a96e-a94e8bf6b02f | -20.29794 | -46.71975 | 2025-09-04 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1d56f9d-96f8-30bb-a37d-f3c2307dd826 | -16.07653 | -43.62379 | 2025-09-04 04:29:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 994f27b7-ff1d-3fd8-837f-73002f57c02a | -15.53795 | -48.35093 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f22d83f3-1232-3ac0-a475-3a538300b828 | -18.06022 | -45.99159 | 2025-09-04 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f1ae0f3-8453-3d4e-901d-98726b963e09 | -17.17727 | -46.26212 | 2025-09-04 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e2dec50-a3b8-3dd6-b6a1-742ea2e7506f | -14.5821 | -53.02415 | 2025-09-04 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5e4e222-90b8-3e46-b371-766aae5bea9e | -20.30551 | -46.04707 | 2025-09-04 04:29:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0790e9a6-9953-390f-91c8-64f19c94993f | -14.56893 | -54.55 | 2025-09-04 04:29:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 720500a4-7419-399a-98e3-9ec0bf377869 | -15.55059 | -48.3786 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f49612c-ca7b-367b-9812-fa43039b2090 | -15.46466 | -53.01041 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97773003-c088-3205-80a0-0e991581d808 | -15.7409 | -53.63557 | 2025-09-04 04:29:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 435392ee-9a96-3df2-98df-9d245a25c37c | -15.53245 | -48.34271 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2a357170-bcca-31f2-ab92-a39eca268c0a | -15.54074 | -48.31121 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b133e38-7b45-330b-ba22-d4ad388adf0e | -15.57677 | -50.31909 | 2025-09-04 04:29:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f0ebbb8-dad3-3b04-95df-e79654a68cd9 | -16.4701 | -49.51478 | 2025-09-04 04:29:00 | NOAA-21 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 73032c37-7bb2-3166-9b7c-6a068f606df8 | -19.63997 | -43.98076 | 2025-09-04 04:29:00 | NOAA-21 | CONFINS | MINAS GERAIS | Brasil | 3117876 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0dd9fe82-494b-3297-9959-2837f807254c | -20.97023 | -46.09327 | 2025-09-04 04:29:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c96ff3f7-695f-3f6f-8258-53ad43f70605 | -14.57673 | -54.55585 | 2025-09-04 04:29:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3db6ad76-0aa4-31be-b00d-612fa491139d | -15.73194 | -53.68491 | 2025-09-04 04:29:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5405dea-e3cf-3b00-9f02-d8be91e85e2c | -20.164 | -46.5923 | 2025-09-04 04:29:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b0e32c1-2b8d-388b-afde-c2d3ed44eb63 | -16.85179 | -52.10994 | 2025-09-04 04:29:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11d0de8a-f483-3b7c-a12b-6e24e55cb2db | -15.4127 | -55.94373 | 2025-09-04 04:29:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 484b6a8f-b009-3d76-ae0d-8a6167ed54bd | -19.69726 | -49.34961 | 2025-09-04 04:29:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 14ea0392-5dae-31ee-af6c-0a530a752633 | -20.1646 | -46.58798 | 2025-09-04 04:29:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d45e6a69-50db-3e22-9e87-9aced62c012a | -15.54948 | -48.38573 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a701038d-ad8f-3831-afcd-a7f0f08858c0 | -15.54349 | -48.31532 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b19b2a2-d55e-305f-a3ca-da5bcb4bf1e4 | -19.2585 | -46.53646 | 2025-09-04 04:29:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 69b096a1-070b-395e-8822-0a3d23ab5c30 | -19.64406 | -43.98141 | 2025-09-04 04:29:00 | NOAA-21 | CONFINS | MINAS GERAIS | Brasil | 3117876 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b876e85c-4789-3a55-a9fa-6e9a5176b637 | -19.35307 | -45.2532 | 2025-09-04 04:29:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c288d486-d605-31bc-9e38-0f93c86a51dc | -15.55495 | -48.41585 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f3e65254-6828-31b1-a440-495dda0cb77e | -19.46744 | -44.77069 | 2025-09-04 04:29:00 | NOAA-21 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eed8751f-150f-3f25-bd5e-1d7f3d1507d6 | -14.56908 | -54.53675 | 2025-09-04 04:29:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83bac866-ee75-350a-a4ef-e3435b5d6e58 | -20.10009 | -50.01254 | 2025-09-04 04:29:00 | NOAA-21 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 66b5ea9f-42b2-3790-b6ec-f8af0184ae64 | -19.47429 | -45.09296 | 2025-09-04 04:29:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ecdc820-1f36-3848-b051-c046a8fc62e4 | -19.68838 | -49.36305 | 2025-09-04 04:29:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 033d2a48-663e-3cfd-816d-768d1f092c68 | -17.15738 | -46.25068 | 2025-09-04 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44114b11-91d0-3b23-b7a8-1a298708db37 | -14.58599 | -53.02489 | 2025-09-04 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 824fa17e-4ddd-3d6c-a219-431dd2226e4f | -15.46935 | -53.00631 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7a97477-ac78-3407-98d5-9104e9dd5bde | -17.71941 | -48.64335 | 2025-09-04 04:29:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 301b937e-2cfe-3295-9aad-c055afc49363 | -16.46288 | -49.51726 | 2025-09-04 04:29:00 | NOAA-21 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef6d153b-33db-34ff-82db-e49ff16dd89d | -16.53788 | -55.09081 | 2025-09-04 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a776e69f-6a98-35a6-98c9-4b1daf44592b | -16.30135 | -45.69059 | 2025-09-04 04:29:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| aa953454-8f68-34d7-a53a-35752093c2fa | -17.0501 | -46.49101 | 2025-09-04 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9144e923-b02f-3c36-abe7-2e166f11ebfd | -18.32661 | -50.97781 | 2025-09-04 04:29:00 | NOAA-21 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a89ec0bf-e75d-3659-aa07-d8f1dfe8d353 | -15.41299 | -52.81694 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed230cb4-9ebc-35d2-a863-5c9ec54f91c5 | -20.51953 | -54.70474 | 2025-09-04 04:29:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bff30464-5c27-308b-8aa5-732e38c3f079 | -19.72305 | -49.09528 | 2025-09-04 04:29:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7567ef70-8e00-3a3f-ad73-3f68212c63d0 | -15.55004 | -48.38216 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24a73f81-9fac-3841-82a8-e66870df3cce | -20.10456 | -50.00579 | 2025-09-04 04:29:00 | NOAA-21 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| c57bc49c-0c17-3d10-8047-22e48f5cd3c5 | -20.09349 | -44.1304 | 2025-09-04 04:29:00 | NOAA-21 | SARZEDO | MINAS GERAIS | Brasil | 3165537 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fbac7684-423c-3780-9760-a7f2106dcbfd | -15.60126 | -52.89783 | 2025-09-04 04:29:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bc2f720-898b-3ce1-8647-73ecf0aea9da | -15.6106 | -52.88944 | 2025-09-04 04:29:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d2b6bf2b-46bb-3175-881c-5cdf98547ff6 | -15.87073 | -52.18689 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0700b73c-2624-34c4-9df2-1b5d6f1d6f61 | -15.88027 | -56.89509 | 2025-09-04 04:29:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 188f3d8d-8b2f-32d3-8526-47844801338e | -18.68633 | -48.18071 | 2025-09-04 04:29:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a8668e9d-c7d7-382f-8f16-0aac94f06d1f | -18.34771 | -47.02459 | 2025-09-04 04:29:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cbbe757e-68af-3b59-8572-263400e5fa8b | -15.55332 | -48.40462 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da0a686f-31fe-3447-adb1-f5418a1a3343 | -15.55001 | -48.40408 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43f18570-57ea-3491-9cd8-78127a928d1a | -16.30638 | -52.96263 | 2025-09-04 04:29:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11961234-d60b-327f-b433-d81f671365b0 | -19.83561 | -54.37654 | 2025-09-04 04:29:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 20ee2c77-e8d0-30c1-aa11-9791a5d91ac0 | -15.41177 | -52.81899 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 222b1d9e-7af0-3a1b-bb92-f394a08b8418 | -17.06341 | -46.47274 | 2025-09-04 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cab493d4-e1d0-3f30-b31c-097bb831bbfd | -16.47067 | -49.51117 | 2025-09-04 04:29:00 | NOAA-21 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e704164-2b7d-3fe8-ad62-f181df072bc1 | -15.58735 | -54.32399 | 2025-09-04 04:29:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7bd7a95e-7fe8-3e02-bf2a-e9fc758ee0bd | -15.60974 | -52.89438 | 2025-09-04 04:29:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c5a2af17-2aee-33e9-974f-549d9b047339 | -18.20257 | -49.72685 | 2025-09-04 04:29:00 | NOAA-21 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12dc62b6-4022-377f-b3bc-dd5fdd3608d8 | -15.57284 | -49.54777 | 2025-09-04 04:29:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51111244-c0db-3549-ae5c-e0994e4bdaf7 | -15.24425 | -53.8055 | 2025-09-04 04:29:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92eed55f-f77f-301f-99ee-2f359a423d94 | -19.23975 | -48.67997 | 2025-09-04 04:29:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97792696-e165-33f4-a7ca-6e0a27c44b04 | -16.536 | -55.08911 | 2025-09-04 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0a9ff45e-759f-3ed3-aa32-59cfca6d3aeb | -15.55276 | -48.40818 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1fa4eecc-f4ab-3f33-889d-a2c953b568b7 | -19.25551 | -46.53192 | 2025-09-04 04:29:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e26cd925-a41c-3917-ac82-d2127e9d227b | -19.25906 | -46.53239 | 2025-09-04 04:29:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93e4aa14-818c-3c51-9d14-0fb2db6b5eac | -16.3055 | -52.96758 | 2025-09-04 04:29:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da1466b1-837f-3ca2-b3aa-de4800011841 | -20.10398 | -50.00946 | 2025-09-04 04:29:00 | NOAA-21 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| d624ae80-8104-394d-908f-b689bb9ab7fe | -19.23586 | -48.68307 | 2025-09-04 04:29:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0de7cf71-b77c-3847-8e77-fdcd839c417c | -17.05704 | -46.44307 | 2025-09-04 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a6f1a07-b902-32e6-81c0-84ea6172b26f | -15.54618 | -48.38518 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e7ba5013-f3d9-307d-b696-9033fb3faa73 | -18.68911 | -48.18496 | 2025-09-04 04:29:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 66e892e8-97c5-31e0-a130-0cde67c72082 | -15.1999 | -52.34349 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 482078e0-ffe1-30f6-9d4b-83917dbbe097 | -17.61097 | -46.64641 | 2025-09-04 04:29:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b14c46c-d6ca-31f1-b3ec-c487a81aff78 | -15.55609 | -48.38683 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cce32139-685f-37cb-a14a-0b2bdead0bab | -15.61771 | -52.88802 | 2025-09-04 04:29:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6eef63a0-8fde-3e50-8714-fdf8e0deea64 | -15.98416 | -55.98132 | 2025-09-04 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f236c194-9f95-3f26-9f4b-41aa9121b61e | -16.474 | -49.51174 | 2025-09-04 04:29:00 | NOAA-21 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2630d062-5bb8-32ec-952c-3f1239819749 | -20.09736 | -50.00829 | 2025-09-04 04:29:00 | NOAA-21 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 9f65b45f-5164-31f8-a03c-451fdd2b8356 | -16.5395 | -55.09407 | 2025-09-04 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a3a3319a-3ce9-35a1-a005-64fd162869b2 | -18.13455 | -50.6936 | 2025-09-04 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6ea2d0c-10cf-3f2e-8c84-1cb458cb28a3 | -14.57323 | -54.55076 | 2025-09-04 04:29:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a8f1972-536b-3399-91ba-4dc8dfd721ad | -18.13165 | -45.49811 | 2025-09-04 04:29:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0668b208-c8cf-3ef9-854e-31e04fbe4e9a | -15.54946 | -48.40764 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README51.md)
