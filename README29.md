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
| 76b6aa42-e7fe-3f2e-b29c-ce5a67d0f238 | -9.93346 | -43.70986 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ccf67ae-0c25-373f-8f02-393e2226185e | -11.47817 | -45.00819 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b3b1ef4-a409-3be0-8b31-ba0d7d50e026 | -8.90222 | -46.62172 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 33da1ff3-ba00-3897-9f36-a05423165888 | -12.86738 | -47.01761 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ba545090-2a7c-3928-8f4b-c379eea13d92 | -11.60266 | -47.22703 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96d73656-dfa5-3b64-8dd5-9098ab9e12ee | -12.02079 | -46.63665 | 2025-10-02 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0cf86cfc-886c-3f28-a4de-379bdf294ec7 | -11.81243 | -45.02138 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d59bd50-b4d8-3761-b7f6-06c57d718d21 | -10.84921 | -46.65666 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58c6e986-84e0-3454-b2c3-64f56beec1d0 | -10.47348 | -49.10794 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b180aeb1-9536-3853-aa1c-f54267395006 | -11.47696 | -45.0051 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a5262de-38b7-3fce-86a9-f08f80616239 | -11.80512 | -44.9967 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 91d17a56-6a4c-367a-a274-aaa554428c1e | -11.85303 | -48.03005 | 2025-10-02 04:02:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3b7222de-3bdb-31b6-9f88-3c6949a19d0d | -11.4651 | -45.1279 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f8f209d-93ff-39f9-8be1-4a6759fb12d6 | -8.88437 | -46.5973 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd6c57e7-81dd-30f9-95ff-41dbc44409ab | -11.67678 | -44.28061 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38b3ea49-357b-3a02-a28c-6b3a5356257d | -11.59216 | -47.64465 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d67f1b82-7a73-37f9-8bbc-4312fa096844 | -11.27511 | -47.82001 | 2025-10-02 04:02:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f02f54e2-fd56-369a-9cd4-0be8122f5481 | -10.84129 | -46.60372 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f15d7fd2-d383-3000-a284-99c2ac653d5a | -12.47486 | -47.26926 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| fe17b202-f9e2-315b-9bc2-16975f3f34e3 | -7.77527 | -42.54088 | 2025-10-02 04:02:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| d7435dc3-f70c-3a51-88ac-2203ca513c58 | -11.59325 | -50.17072 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b4a0322-1dc1-3efb-addb-dbd2b1a85382 | -10.25266 | -50.32261 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 84f9d142-64e1-350b-816c-6aeba048d9d3 | -10.20855 | -50.27503 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2a04f74a-bf3e-364b-89e3-cff927bc44ce | -11.79246 | -47.56848 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 488661e7-583d-3dc2-a080-31039d79930c | -9.93633 | -43.71454 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e824fbd0-4a44-3c62-9a9f-f46c829f0990 | -7.41152 | -45.19056 | 2025-10-02 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b098593d-3d42-3b12-a1ab-defbcdef0c75 | -10.24924 | -50.31127 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb041fe1-8a79-3d0f-905e-8b3ed36840fd | -12.8438 | -46.86394 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae0770cc-6f34-362f-83e3-acaff9057df7 | -11.58966 | -47.65835 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4e8d51af-d68f-3e8c-bab6-780266c7cdd1 | -11.43782 | -43.88129 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aaa847c2-f99e-37e6-9ed6-36dc865ee156 | -6.47914 | -44.29155 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 98957279-3261-387c-bb93-6e45dcee83a5 | -6.30385 | -45.92553 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88d1bb3c-e66f-3423-82cf-20bac745e02f | -12.42598 | -45.1694 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13d278ba-75de-3422-bb47-f2ec11a4b39a | -10.2032 | -50.27402 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b1b7cae8-dd3e-3020-b912-9803f3d6e08f | -9.9423 | -43.745 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 8b5fabd6-7347-3957-be3b-9ae8e8a9f8b1 | -9.79572 | -45.9424 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8a64816-594f-34e4-b39a-aa355e227bdc | -6.35443 | -43.3 | 2025-10-02 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3a2486df-fc5a-38b5-ab09-1b165ef514ae | -7.29544 | -42.8755 | 2025-10-02 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| dae26a33-fe48-3a50-add0-c1c08b2f3cc5 | -8.89296 | -46.59859 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 316a8f93-4f84-3284-a035-3e1ecb9f718b | -6.48917 | -44.27811 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 27fc3140-d5f0-34af-837e-96991f30c579 | -10.8414 | -46.62766 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fcb0d6ce-5469-3d82-b8c2-8321904419e1 | -11.52677 | -43.54674 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c219e11-b915-370e-b133-089020542706 | -5.96545 | -45.71223 | 2025-10-02 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23ab2771-f4d6-3149-947e-e220688f7b84 | -10.99601 | -46.59911 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 69db49b4-066a-34a3-90e7-c7adf73734d4 | -7.77465 | -42.54469 | 2025-10-02 04:02:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 50.6 |
| c26deb51-35bb-3052-a9bc-fa8b4f262069 | -11.58745 | -50.17294 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a70a88bc-7547-3aa1-af6d-08e8b88af446 | -10.99188 | -46.59834 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 9757649e-f7c0-374b-9971-a799c8369e38 | -13.15478 | -42.53163 | 2025-10-02 04:02:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 15026f87-0bba-3d5e-9f90-da2fabf2f090 | -8.90358 | -45.04008 | 2025-10-02 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 04df744d-1863-33cb-a134-6b2e44814fa9 | -11.97997 | -47.01405 | 2025-10-02 04:02:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 859a0cf1-ce29-3d1a-9861-213feccb9133 | -11.4657 | -45.02662 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 17271fd3-c837-3cbc-8c3e-d73548137a62 | -10.96317 | -46.65218 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e80f512-e435-3d1e-b372-508daa65a6c8 | -12.68779 | -46.91391 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 780761ee-f944-3da6-b986-66ed1e9008ad | -10.25996 | -50.31327 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c2a0d1e6-9ce9-33e9-87d9-c37c0d7650e8 | -9.9354 | -43.76492 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| dd48e902-e14c-3e28-bcbe-3ff38b4734b7 | -9.93436 | -43.59362 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a78f9b07-4026-3860-94c7-f5d5b2b447ad | -11.26289 | -47.65925 | 2025-10-02 04:02:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 10018944-c4ea-3b82-8611-b4753546e7e9 | -10.708 | -48.00352 | 2025-10-02 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c69ba919-9d54-3cff-a8b6-4557ed46b3c2 | -9.26618 | -45.75816 | 2025-10-02 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bcf7e877-660f-3f39-92bd-82fc42d5327d | -11.7472 | -42.66868 | 2025-10-02 04:02:00 | NOAA-21 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 41064423-8bee-30b4-a3d3-1f6b6b0f8a59 | -11.58288 | -50.16874 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f4c6afc7-8742-3dbc-b49a-dafc7efbcbff | -13.01493 | -45.21629 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1fb16828-ecbb-3b72-9b46-f89a3b6e3855 | -11.85056 | -48.04355 | 2025-10-02 04:02:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| da269dc6-3e42-37d1-b8c6-35803d943163 | -12.42736 | -44.0951 | 2025-10-02 04:02:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11a4c917-044b-3e87-a0d3-3bdbea7ac0c5 | -11.19715 | -47.7506 | 2025-10-02 04:02:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 403966e0-e32f-31be-8fe0-ef2f543f2a77 | -9.93164 | -43.74325 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 34.7 |
| f88ad719-6321-3579-9b40-9e892f884335 | -9.93279 | -43.71394 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6ac6f20a-2e3f-3829-8140-050d4576ed5d | -11.16384 | -47.27234 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a9c44c39-703f-3dbb-ade9-cc5f03904570 | -10.70331 | -48.58074 | 2025-10-02 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4cc9751f-b372-36a4-8722-1f1f210f27e9 | -5.82506 | -42.85455 | 2025-10-02 04:02:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0af11e3f-1d2e-392e-b041-88db49ab2e0c | -7.40753 | -45.1899 | 2025-10-02 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29e75d4b-322f-3c25-8e9c-94511d04a2e6 | -11.21342 | -41.59708 | 2025-10-02 04:02:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4582126c-5b06-3ecf-879f-cb9e5da7e82a | -11.16459 | -47.26806 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4fbad819-a0e4-3108-a26a-385e81b4280d | -12.23601 | -44.04298 | 2025-10-02 04:02:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1b4b6c1-62fd-3c6b-9a5d-1c636801c736 | -13.00526 | -45.2284 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3546837f-875d-30f8-b68a-a1ec654ddc2d | -12.68709 | -46.91782 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66fea8a2-b3ec-3496-98d2-31d7630b94da | -11.44068 | -43.88591 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b741afd8-494e-3d57-80ab-bf6d518a13c6 | -11.13438 | -43.3904 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 46319443-7fc7-39b4-bb3b-c824e3f9dca8 | -11.70262 | -44.30215 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e70f382b-944e-36ad-bd95-5ea6bd3b2b3e | -10.20628 | -50.27478 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 85517959-05a0-38aa-beb4-9cc09d76e7ff | -9.92367 | -50.49457 | 2025-10-02 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 134b2351-8eb0-3bc3-882e-737fc5fdbdb8 | -12.85573 | -47.03555 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29ffb32a-b20b-36fa-8d22-37bc0ac8c778 | -5.8273 | -42.86335 | 2025-10-02 04:02:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 17836387-214d-376a-8301-56ebd03d11ee | -8.58266 | -49.6042 | 2025-10-02 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 848a535f-c2e9-3f0d-a322-092e794fea28 | -9.02164 | -46.68885 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fca7a0be-1bfc-3735-a605-002a9785bd4a | -8.90504 | -46.0655 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3bdbaf47-4a00-3d3c-911d-a9f677e60ccd | -12.20979 | -47.79161 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1c77afae-8740-349a-9ec5-42ad42cc25d8 | -7.39959 | -39.70017 | 2025-10-02 04:02:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f5412546-57e8-3320-a236-a28c0c05a302 | -12.83493 | -46.86647 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c09092d-333e-32ac-8f6c-f42d3ec3c3e9 | -10.33032 | -45.2566 | 2025-10-02 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 37f78374-0311-36c9-a4e6-07834f8b32c9 | -11.09336 | -47.82634 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12927410-fd00-30af-8184-4c27d079fb83 | -11.48224 | -44.99638 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 26cf7d15-4f89-3c06-ab56-bffbc8092887 | -6.96719 | -45.32657 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c34e28ba-5959-3993-8a50-6ab79abb2b9a | -11.67706 | -45.32008 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ba0b2e2-7d0b-3115-950c-1b8945cc905a | -11.90598 | -47.89071 | 2025-10-02 04:02:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5dec4e55-0dab-3de4-a923-4750a3c7f182 | -10.28524 | -36.33637 | 2025-10-02 04:02:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d9d4ff12-4ac9-3b9b-a3be-39ee775573a6 | -10.89697 | -44.27162 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 883fc6c2-4943-3e8b-85b1-73ce2e70cc57 | -9.94276 | -43.71984 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f04686a5-a251-3481-961f-b85439a857f9 | -8.81131 | -46.68679 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f8ed0c8-dea3-3387-a615-582d9a4ab571 | -11.18752 | -47.7532 | 2025-10-02 04:02:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README30.md)
