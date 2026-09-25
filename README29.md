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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63de2233-b09f-3c9a-929a-5303146e3454 | -10.62979 | -51.35131 | 2026-09-25 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2475dcb-6bcd-347a-b483-2b1cbeec54e2 | -10.90236 | -53.94406 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 927c79fb-68cc-35e6-ad89-41dacd4a8f62 | -6.67102 | -58.57507 | 2026-09-25 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f64d9e7a-cc1b-34bc-8a47-2054c3496a25 | -6.13858 | -57.79903 | 2026-09-25 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98a955fa-d187-3e95-8e17-41b531b3b077 | -12.24573 | -50.76002 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33d139fd-93cd-3b45-b5d0-935cc01c22a7 | -12.18498 | -50.75736 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7a2f42d2-ca8f-374e-8244-3a96c38c58d3 | -8.77786 | -45.59109 | 2026-09-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ca6f65b0-19cb-3b50-8667-11afc881e8a2 | -12.23194 | -50.73971 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36f8f883-b75a-3a42-a0d2-92210c2effc6 | -11.28642 | -51.30343 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fceac3b-b1da-3135-b64d-1d93ffbe57e7 | -19.91411 | -45.53809 | 2026-09-25 04:49:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6964940-e5d2-30a7-a6ab-c2f26a71af6d | -23.00499 | -48.61954 | 2026-09-25 04:49:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 595315af-7826-3932-a9d8-f6cbd7cc8b72 | -21.05103 | -48.47614 | 2026-09-25 04:49:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1ae023e-2725-3315-adff-01fa29ccdc99 | -23.27286 | -47.68203 | 2026-09-25 04:49:00 | NOAA-20 | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a56873cd-934d-31dd-9d7c-9feb18ae615b | -21.05077 | -48.46868 | 2026-09-25 04:49:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3bf2731f-4506-36e1-aee3-acb4882daf76 | -19.91427 | -45.53557 | 2026-09-25 04:49:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 946c7d40-08e6-3fd1-a8d6-28635a9180d9 | -21.05008 | -48.47383 | 2026-09-25 04:49:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3ff21e26-dc08-3383-a295-ec1c8dfd901e | -21.20038 | -48.27097 | 2026-09-25 04:49:00 | NOAA-20 | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f40c97e-f6e4-34f0-9e08-19b47988057d | -19.30279 | -47.44184 | 2026-09-25 04:49:00 | NOAA-20 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6c1d4f5-38ca-3e82-9d23-0d19685aa386 | -21.05169 | -48.47101 | 2026-09-25 04:49:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 088fe404-a2e0-3487-ad91-2f37fb430231 | -14.21997 | -48.5099 | 2026-09-25 04:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21b71463-67e0-390a-ba39-caf4c3d65c7e | -14.52257 | -49.57701 | 2026-09-25 04:49:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3ce3df83-25f3-3172-9583-e570cc286388 | -13.7003 | -48.80349 | 2026-09-25 04:49:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b851eb50-c4f4-3044-8264-793453746c20 | -14.51421 | -48.34004 | 2026-09-25 04:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b7fe118-17e2-33e3-ae33-ac708cedc962 | -14.52199 | -48.33714 | 2026-09-25 04:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6778a39c-1072-30cf-a056-42aec38b1a2e | -13.70436 | -48.80022 | 2026-09-25 04:49:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11d63c4b-0923-33f3-a778-d0294f583a67 | -12.99659 | -49.04599 | 2026-09-25 04:49:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f37d4c6-542e-3d73-8b69-0eca46aa0063 | -12.766 | -52.82417 | 2026-09-25 04:49:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 793e5cf9-2aa6-32f0-9ebb-b29c7e0520cb | -13.45187 | -48.62494 | 2026-09-25 04:49:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c07bf558-1a89-33a4-9707-83cdffe9bb4a | -13.70845 | -48.79676 | 2026-09-25 04:49:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93f9707d-ded3-3777-90e9-a7e71243b828 | -14.73094 | -46.22565 | 2026-09-25 04:49:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 50528d7e-6963-398f-a70c-3999582506d1 | -13.44777 | -48.62833 | 2026-09-25 04:49:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30be1741-a717-34ac-a07a-4634da08f776 | -14.11849 | -49.86477 | 2026-09-25 04:49:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0c98a7c-1217-3a8a-845f-e58b3015e6ff | -14.51901 | -48.33224 | 2026-09-25 04:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ce12e48-8296-3241-a268-ba87a3dc5d5d | -14.5178 | -48.34068 | 2026-09-25 04:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b38ec9b-68bf-3281-a700-2a13f67911ba | -14.51481 | -48.33583 | 2026-09-25 04:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e11dcea-4011-3f07-8ed3-14fe7401c67b | -11.99393 | -57.58986 | 2026-09-25 04:49:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d0f8bd9-e4e2-38d3-b7d5-6db74abb24a3 | -11.80513 | -58.16205 | 2026-09-25 04:49:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98663a7c-89f4-3f0c-8795-64d652d06d67 | -13.73215 | -48.97329 | 2026-09-25 04:49:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f1614c2-604c-3fb9-be96-6c1a73389b3c | -13.84183 | -49.68172 | 2026-09-25 04:49:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50117ef7-1d80-3b98-9dc5-6a4c21bddaf9 | -12.99602 | -49.04982 | 2026-09-25 04:49:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c6e4b9c-e5ff-32fd-8e60-43a2a6961f69 | -13.69739 | -48.79898 | 2026-09-25 04:49:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a19f90b4-3bc6-3d20-ad26-51d66e4c846e | -14.37499 | -47.24675 | 2026-09-25 04:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97a42d81-3604-3bcb-8e5d-4d8ed9b20d97 | -14.74869 | -45.57768 | 2026-09-25 04:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5465756-75af-32d7-b264-02f92df3d5fd | -13.44717 | -48.63231 | 2026-09-25 04:49:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02b1baf2-2505-3d5b-82e5-9e60ec02759e | -14.36377 | -52.1128 | 2026-09-25 04:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48933f53-9306-38ec-afdc-914ec333bdf8 | -13.22634 | -51.81276 | 2026-09-25 04:49:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 907405b2-e1a9-3eee-ae03-920f6401ab77 | -13.71956 | -48.79427 | 2026-09-25 04:49:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fff5af0c-d3ed-3f56-8bac-7d85056a45fc | -13.4536 | -48.63744 | 2026-09-25 04:49:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6d4973f1-d281-31cf-9045-063dc17102e6 | -13.71547 | -48.7977 | 2026-09-25 04:49:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c0f6631-15a2-36e0-8f96-aff5881b4a39 | -14.12131 | -49.86903 | 2026-09-25 04:49:00 | NOAA-20 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a00d973-e895-3fd0-a969-f2de91ae7a05 | -12.14467 | -61.17559 | 2026-09-25 04:49:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 728a265a-5cf1-3c82-bf4a-6a4265022f28 | -13.77821 | -54.03996 | 2026-09-25 04:49:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8c9c4faf-8a1b-33b1-993c-265047f748b3 | -13.00636 | -49.05139 | 2026-09-25 04:49:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 194f113f-1ca0-33bf-92b1-afdb4d63415c | -13.69682 | -48.80285 | 2026-09-25 04:49:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e645cb5f-4767-3ae6-9068-e58f602fb049 | -14.5184 | -48.33649 | 2026-09-25 04:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 934b486d-bd8d-34d5-bf4a-bf5ba18d5060 | -14.22058 | -48.50574 | 2026-09-25 04:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 062c8b93-2752-3758-a796-6474d099d78b | -13.45128 | -48.62891 | 2026-09-25 04:49:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31a23959-90e7-3d2c-ba78-387a3a12f6d3 | -13.44425 | -48.62779 | 2026-09-25 04:49:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c327bd9-ef12-3b62-bdc1-93bc80e8a5ff | -11.80422 | -58.16691 | 2026-09-25 04:49:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4db88c8-d777-36d3-8fc2-8de4b004a4de | -13.34258 | -51.31958 | 2026-09-25 04:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11347937-4634-389a-b0e5-c685e8a3a5d9 | -13.45538 | -48.62549 | 2026-09-25 04:49:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2d23b28-d9df-3415-ae18-ccdbf1fae1b7 | -11.56172 | -61.24359 | 2026-09-25 04:49:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 596dea1d-5661-3f4b-9bb5-ca2a31c640c1 | -13.77753 | -54.044 | 2026-09-25 04:49:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 42f40955-9ac0-3623-90a2-f64c7f2be5b1 | -13.73156 | -48.9772 | 2026-09-25 04:49:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25c13b32-9d88-3560-b665-c5c3be57460a | -13.45479 | -48.62947 | 2026-09-25 04:49:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6106ba6-a383-3f27-8ede-e23db690fd93 | -14.22353 | -48.51046 | 2026-09-25 04:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1cc14806-5846-3e6c-9915-1e20830f00ab | -11.99312 | -57.59442 | 2026-09-25 04:49:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a83f0151-2b36-3567-83c5-b928c3be3047 | -13.78172 | -54.04059 | 2026-09-25 04:49:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9860c240-f23f-3d41-a06a-72b1572408a7 | -11.99198 | -57.59145 | 2026-09-25 04:49:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a786f070-6f07-3c30-b6b3-002ba9b57f85 | -12.76261 | -52.82357 | 2026-09-25 04:49:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c4a3502-32a2-3f7d-bbe6-d5cb745f53d5 | -14.72736 | -46.22136 | 2026-09-25 04:49:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7cee6645-a1e7-343f-ab79-9e7d37736759 | -12.14542 | -61.17178 | 2026-09-25 04:49:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c51b45f6-faf8-35af-8e71-515145b6b3f2 | -13.00693 | -49.04757 | 2026-09-25 04:49:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0ede5da-de13-3122-8be8-c64d823cfa84 | -14.74815 | -45.58165 | 2026-09-25 04:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edce9bc5-5ba1-38a4-83bf-474499a5d4e0 | -13.84126 | -49.68544 | 2026-09-25 04:49:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d746995a-b3f7-35ec-b189-4a035e81076b | -13.69446 | -48.79452 | 2026-09-25 04:49:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32f0732d-e3be-366b-a022-a708291212a2 | -14.5214 | -48.34129 | 2026-09-25 04:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 536bb39a-0509-3beb-af00-3f5f59d519ad | -13.6939 | -48.79838 | 2026-09-25 04:49:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e84f5b1-eade-3b22-b47d-836c076b1113 | -14.74762 | -45.58562 | 2026-09-25 04:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28d8deec-4c0d-3097-bedf-d5fce4c25521 | -13.33927 | -51.31903 | 2026-09-25 04:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 274e89b2-df70-3f53-9e00-13dffbdccd40 | -13.45009 | -48.63687 | 2026-09-25 04:49:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 74b93fce-31ce-356b-b45b-e6c2b7b90964 | -13.45831 | -48.62998 | 2026-09-25 04:49:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1b895f1-9298-3b22-8fff-125a1c530f2e | -13.32989 | -51.31385 | 2026-09-25 04:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78dcbc17-5f3a-3a13-b33b-7d68d4f2c3f5 | -13.70379 | -48.80413 | 2026-09-25 04:49:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1451e0b1-7952-3159-822b-3930ae9a1cfc | -13.32933 | -51.31739 | 2026-09-25 04:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff0add25-8589-3c76-8598-d963b899e372 | -14.51542 | -48.33159 | 2026-09-25 04:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e39ac0d-512b-339c-9f88-27251fead773 | -14.72686 | -46.22505 | 2026-09-25 04:49:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1298cb6a-b8d4-36ff-806c-562352412b3b | -14.12188 | -49.86531 | 2026-09-25 04:49:00 | NOAA-20 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af6a1e83-17f2-311b-94ae-eeea5494e305 | -13.71899 | -48.79815 | 2026-09-25 04:49:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87097809-ff40-3f2b-b1a0-1118eb9e808a | -14.72636 | -46.22874 | 2026-09-25 04:49:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f1e50e43-b370-356c-b2df-33e309cbd1fd | -13.22042 | -51.55311 | 2026-09-25 04:49:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4aeb07ea-a6d3-3b02-821a-82522361c203 | -13.70787 | -48.80073 | 2026-09-25 04:49:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98604519-a39b-384e-b790-bdc199024f63 | -13.21654 | -51.5561 | 2026-09-25 04:49:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21d3992a-9028-3a48-81ba-9fe31b54e734 | -12.75859 | -52.82671 | 2026-09-25 04:49:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d66d2ca-2120-3dba-8ec3-468709954c64 | -13.21986 | -51.55665 | 2026-09-25 04:49:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9156a32b-44a1-3753-9e7d-0ada739fd0e6 | -13.45068 | -48.63288 | 2026-09-25 04:49:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c5a1b227-a0ab-3761-a956-b2a1a0dbd98d | -13.78104 | -54.04464 | 2026-09-25 04:49:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a2815c2f-52de-3a26-9a79-6d7919631668 | -11.56253 | -61.23946 | 2026-09-25 04:49:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cc672e7-d1a9-329b-955d-b90707cc03e8 | -13.4542 | -48.63345 | 2026-09-25 04:49:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 597424fb-02ea-3f4c-a122-e8336c30b096 | -14.73144 | -46.22197 | 2026-09-25 04:49:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README30.md)
