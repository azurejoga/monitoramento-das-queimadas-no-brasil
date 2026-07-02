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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37268de4-a3b5-33e9-b6cf-75adb1ea0e83 | -21.7827 | -56.2762 | 2026-07-02 00:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 116.5 |
| b99d4377-ccf2-3f09-87ca-ca76af1d8708 | -12.5135 | -48.2802 | 2026-07-02 00:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 0ed783f4-4850-3435-935d-2151d0b9343d | -21.7622 | -56.2795 | 2026-07-02 00:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 75.8 |
| d003f481-2644-3a2b-82cb-2e99a8b3762e | -11.4149 | -56.0525 | 2026-07-02 00:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 035af3f1-5eaa-321e-a6a3-faf0ca0dc87d | -10.9588 | -43.0565 | 2026-07-02 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| ded8caf8-13c4-31b1-8aad-f2442be59cfd | -8.7208 | -48.3441 | 2026-07-02 00:20:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| c9d40c55-0790-39e4-aa02-b28aad962455 | -10.9593 | -43.0326 | 2026-07-02 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 23a990ac-af80-336f-be92-896a96c91ca1 | -3.5228 | -48.0383 | 2026-07-02 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| ad66b9c1-397c-397c-8b7b-978360979646 | -21.7617 | -56.301 | 2026-07-02 00:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 89.7 |
| dee19440-19bb-35f0-9886-f4d235edc2f9 | -4.0046 | -48.0618 | 2026-07-02 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| c7353c47-7ae9-3e48-a9bc-bb98a78883e2 | -11.8007 | -57.0032 | 2026-07-02 00:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| f56a29b3-0415-3ce7-b61c-521bf46b24d5 | -9.1933 | -45.3114 | 2026-07-02 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 33993acf-0591-3b4f-9a54-c2b693739249 | -11.4147 | -56.0726 | 2026-07-02 00:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 7709b05f-9027-3bc1-9d91-4434eb24c42a | -3.5043 | -48.039 | 2026-07-02 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 084f6d04-ced4-31b3-bc15-631673c639b5 | -10.9401 | -43.0355 | 2026-07-02 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 247.0 |
| c7783fe7-a5a2-3f9d-80bb-084e98fc4147 | -3.5043 | -48.039 | 2026-07-02 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 0c3c25e1-c7d5-36fe-99e6-b67a200bdcd8 | -21.7823 | -56.2976 | 2026-07-02 00:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 142.5 |
| ab64d42e-d885-3399-a407-a46cd19943d4 | -11.8007 | -57.0032 | 2026-07-02 00:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| e9a33f19-326b-37ec-ab59-6125829caeb1 | -21.7827 | -56.2762 | 2026-07-02 00:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 138.5 |
| ee11a40b-70de-3c98-a9fb-1b682ed9938f | -12.5135 | -48.2802 | 2026-07-02 00:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| eca3e264-fe02-3969-8895-03930fe7f3d0 | -10.9397 | -43.0593 | 2026-07-02 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 183.0 |
| ae79e10a-54eb-350a-b2b1-791067dbc14e | -8.7208 | -48.3441 | 2026-07-02 00:30:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| cec8be8c-af09-3ca6-b5aa-6e650d1465d9 | -11.4149 | -56.0525 | 2026-07-02 00:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 6321bfd5-a0e6-3edd-b6b1-45f08070d4e2 | -21.7617 | -56.301 | 2026-07-02 00:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 72.5 |
| d7cdc08c-1e8f-3f9b-b467-5bb5f240cf4a | -11.4147 | -56.0726 | 2026-07-02 00:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 8726a929-f0d9-3c6c-8a94-e5b75e427e0e | -10.9588 | -43.0565 | 2026-07-02 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| c0e80563-4e7e-305e-a7a1-0b7c79a7c88f | -21.7622 | -56.2795 | 2026-07-02 00:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 1788978c-a18e-3cf4-b8f3-ac76a29436c4 | -9.1933 | -45.3114 | 2026-07-02 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 3ec7994d-d107-3cce-9ca6-85716b71d5ff | -10.9401 | -43.0355 | 2026-07-02 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 181.6 |
| 3223bbd4-7df7-3134-9b55-a81062c9eecf | -10.9593 | -43.0326 | 2026-07-02 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.1 |
| f917416e-0649-3b71-b0f2-0f0c5ab57073 | -4.0046 | -48.0618 | 2026-07-02 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| c9f447a2-ab18-37ab-9c80-0d1a46ded37d | -11.8007 | -57.0032 | 2026-07-02 00:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 3d110e92-25a5-3b3d-abfc-607663b88c74 | -21.7617 | -56.301 | 2026-07-02 00:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 88.9 |
| d57387b5-8f2f-3e28-8ee3-2f724871536c | -8.7208 | -48.3441 | 2026-07-02 00:40:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 3f5bd430-ce82-32c3-99c1-37df27527c2a | -10.9397 | -43.0593 | 2026-07-02 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 191.9 |
| ab0b0f44-9e15-3bd7-99d3-16f321d17e5f | -10.9401 | -43.0355 | 2026-07-02 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 241.7 |
| a6414ec1-a4de-3de6-a80f-ffeab901d2b2 | -11.4147 | -56.0726 | 2026-07-02 00:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 6e698162-b72f-330f-b00b-7f5c756e8661 | -11.4149 | -56.0525 | 2026-07-02 00:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 3979fbbc-dbd0-3d30-80ed-d2cd4b54f2d0 | -9.2123 | -45.3092 | 2026-07-02 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| d67c728e-1014-3996-8f17-c1836566fc35 | -4.0046 | -48.0618 | 2026-07-02 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 12a0580f-0edb-35d9-a1a1-2f8601c90bed | -10.9588 | -43.0565 | 2026-07-02 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 27fd7a69-0251-3a8f-8e45-390b4ff63df5 | -21.7622 | -56.2795 | 2026-07-02 00:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 71.9 |
| fa293e2c-2b65-3d54-9f52-7d2fc8a0ea0d | -3.5228 | -48.0383 | 2026-07-02 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| f1a325c6-6af1-314f-b9d7-5eaef3df8b4e | -3.5043 | -48.039 | 2026-07-02 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 43373b55-1103-3742-80d3-1f23aa38b326 | -21.7823 | -56.2976 | 2026-07-02 00:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 141.8 |
| ed2111e1-28bd-3c9a-9f20-4d985d6bb1c1 | -9.1933 | -45.3114 | 2026-07-02 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 7b0b438b-f115-35e9-a76d-e0c164a07c5b | -12.5135 | -48.2802 | 2026-07-02 00:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| add39bcc-7f07-337f-b7c3-c3f4a4fb5b87 | -21.7827 | -56.2762 | 2026-07-02 00:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 236695d9-0374-30a7-89f5-0491e70620e4 | -10.9593 | -43.0326 | 2026-07-02 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 409293da-a961-3712-bd1b-82e22c30b912 | -11.4147 | -56.0726 | 2026-07-02 00:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 611d896a-ccce-381b-ad63-113bb041577a | -21.7827 | -56.2762 | 2026-07-02 00:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 111.8 |
| e57d685c-7a3f-3c31-9d01-d24347a48c35 | -9.1933 | -45.3114 | 2026-07-02 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| d253654a-4013-3b19-b40f-139b0b3a5a2c | -10.9593 | -43.0326 | 2026-07-02 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| f229adc1-ea87-369c-bbb1-854d87cf3d2c | -9.2123 | -45.3092 | 2026-07-02 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 9fae9dac-b069-3055-84d8-2f60461f4be2 | -4.0046 | -48.0618 | 2026-07-02 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 5b0afd45-ddec-3bfe-a034-0e9f13ca558c | -3.5043 | -48.039 | 2026-07-02 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 23dfb5ce-d13a-3e52-941c-aeac3ab43230 | -8.7208 | -48.3441 | 2026-07-02 00:50:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| acc9ab03-3bdb-35c1-a80f-80148ec4187b | -11.8007 | -57.0032 | 2026-07-02 00:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 1b0923d8-4c2f-3d65-90f4-6f89bf709d45 | -21.7617 | -56.301 | 2026-07-02 00:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 867fee7d-2218-391b-8a65-1a0732efddf9 | -11.4149 | -56.0525 | 2026-07-02 00:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 34c521ee-3a6d-316b-81a2-2a6c2d6ea188 | -12.5135 | -48.2802 | 2026-07-02 00:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 15530a56-6d65-3d65-8596-99980ca38e3a | -3.5228 | -48.0383 | 2026-07-02 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 2509ccaa-ad0f-3248-94d6-5fe7b146a5cc | -10.9401 | -43.0355 | 2026-07-02 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 213.1 |
| 1bb62556-0a02-310b-b756-34ee934e025b | -10.9397 | -43.0593 | 2026-07-02 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 491c55f2-8893-3c55-b9d4-abdf00a112db | -10.9588 | -43.0565 | 2026-07-02 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| de5adc35-f265-35ed-9175-591dc1fa54a0 | -21.7823 | -56.2976 | 2026-07-02 00:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 5141c34b-5529-3520-91ca-58a3f609ceb0 | -9.212 | -45.3321 | 2026-07-02 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 52.0 |
| f0f97c53-0030-3943-a840-ba19482e8149 | -11.3529 | -55.424099 | 2026-07-02 00:50:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0162d9b5-7f8f-3503-b985-fc34b59aee8e | -9.1916 | -58.046299 | 2026-07-02 00:50:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d5c5f34-15d4-3e49-9925-c25c5dbe418e | -8.3612 | -55.0854 | 2026-07-02 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1dced067-ef5b-3f26-bb2c-92d34ac0e24c | -21.7822 | -56.280102 | 2026-07-02 00:50:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 639eb460-f409-3b45-8cd2-09913d817e4c | -21.774 | -56.289902 | 2026-07-02 00:50:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| cc969de9-8c06-3e08-a265-14f86d8cfa27 | -12.5179 | -48.273499 | 2026-07-02 00:50:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a886054f-4fd9-37b2-a11f-3e9f4635dcaa | -11.4177 | -56.056099 | 2026-07-02 00:50:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79fb7b7b-7d47-321b-aad4-e4983852d895 | -3.4988 | -48.021301 | 2026-07-02 00:50:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16788129-1a83-3ce1-ac65-2a8711fcb1bf | -11.0488 | -56.917702 | 2026-07-02 00:50:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c58054a8-8c52-3912-b0a1-690dc1712683 | -11.4159 | -56.048401 | 2026-07-02 00:50:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07120438-1aa5-3f44-80ea-76171470243b | -4.0001 | -48.034698 | 2026-07-02 00:50:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d1a9cf4-55c0-31d8-bb02-a2777085bada | -22.2187 | -56.688202 | 2026-07-02 00:50:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8cbe82a7-0379-3ab8-a8fc-3159c7af8f4d | -9.0295 | -59.523499 | 2026-07-02 00:50:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 744090ae-5273-3466-82d1-7c83d23a4510 | -22.2269 | -56.678299 | 2026-07-02 00:50:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bfd57dff-9df6-3d19-a103-ba956ba3c41b | -8.7096 | -48.314098 | 2026-07-02 00:50:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d518a5a-e787-3cbb-9a33-122fa8ee15f9 | -11.7956 | -56.979698 | 2026-07-02 00:50:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6cdfdec0-1b6c-3790-9b4b-a896f6f6fde3 | -20.483299 | -50.509998 | 2026-07-02 00:50:00 | METOP-B | PONTALINDA | SÃO PAULO | Brasil | 3540259 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 42edf591-fe52-37d9-8a1a-8e6b085caf1f | -12.5083 | -48.276199 | 2026-07-02 00:50:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c3179429-683c-3141-acfa-67f861ae4f97 | -11.4257 | -56.046101 | 2026-07-02 00:50:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3dd7007e-c413-3c18-bfd7-2fd6fe80594c | -21.451599 | -51.349701 | 2026-07-02 00:50:00 | METOP-B | IRAPURU | SÃO PAULO | Brasil | 3521606 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 654a4c26-0105-33b3-ba56-df10f7386b1e | -21.7806 | -56.272701 | 2026-07-02 00:50:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e7c0d4be-a60f-365e-abc7-07fa317e72b7 | -11.8431 | -48.218899 | 2026-07-02 00:50:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f1ff0c8-f875-3610-9a8d-8f22dc1756c8 | -9.19 | -58.039299 | 2026-07-02 00:50:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cfb37deb-14b6-3c77-ba7e-55b64456eca0 | -9.979 | -54.419201 | 2026-07-02 00:50:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d2f82141-904e-3ace-8176-f16fb15e0321 | -11.7973 | -56.9869 | 2026-07-02 00:50:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0419a69a-d8cd-374b-989d-15c5429ce5e0 | -9.6032 | -56.914398 | 2026-07-02 00:50:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1dd43bcb-8e0b-398e-8855-0b27784fbb94 | -9.1736 | -58.0578 | 2026-07-02 00:50:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1006cf7e-b6be-337b-9f8a-7d60ab840760 | -11.351 | -55.415901 | 2026-07-02 00:50:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 76e47ffd-adaa-3c40-8a0a-d21835fdf356 | -11.7989 | -56.994099 | 2026-07-02 00:50:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d8dd6d04-9426-3f87-b2ca-f36b8e9e56cb | -11.3607 | -55.413601 | 2026-07-02 00:50:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5cc5c163-b4ee-3027-bdbb-01009f2f098d | -11.1576 | -50.0686 | 2026-07-02 00:50:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4f7245c4-d906-3336-ad45-fe17179bcd6f | -21.769199 | -56.267799 | 2026-07-02 00:50:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 452e40c9-cb18-3409-a408-344d8aafcafb | -10.1263 | -52.0882 | 2026-07-02 00:50:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
