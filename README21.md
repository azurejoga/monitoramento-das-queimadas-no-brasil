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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 914b2e6f-a13a-35e6-86d9-2b1317563518 | -15.17897 | -46.22238 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd9aec10-1b9f-3d9d-83b2-ca92fefec4bd | -8.45548 | -54.73128 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4bf6ef9f-2e4b-334e-8757-49082cf49c1f | -11.66403 | -50.18922 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 38dbbea7-93fe-3f33-ae46-a765de100224 | -9.46381 | -56.7421 | 2026-09-02 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6f700878-a92d-3e61-9aa6-616e21665967 | -8.42952 | -46.90131 | 2026-09-02 04:21:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9cd804d-bfb1-38cb-9ba7-07f8ae8a63c2 | -12.37619 | -48.14869 | 2026-09-02 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f2431db-c5af-3a66-90bf-26aa75d5c21b | -8.11451 | -54.95312 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fdeb036f-d349-33bd-b4bc-3753ae7c3d6e | -12.07623 | -47.11992 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54765f64-1c0c-3492-93bf-406537377caf | -11.82972 | -46.74685 | 2026-09-02 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c61b281e-de18-3b01-81d9-38bb528d6157 | -9.71922 | -48.14061 | 2026-09-02 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7fe9646-f1ae-36b0-a142-3d33179fc480 | -15.37418 | -47.69056 | 2026-09-02 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e8043479-b9d9-3473-9522-0a94f2b0897b | -12.14093 | -47.07911 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7ce78757-3ad6-3c39-a07b-9e677db90e7e | -11.31081 | -45.16765 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ef89c9e-b6b7-3682-bbd0-1b1f4864fd23 | -14.985 | -48.03508 | 2026-09-02 04:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c67e1182-14df-3575-a1b0-005cef2b93a7 | -15.36695 | -47.69307 | 2026-09-02 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 9ea80f15-2e2c-3273-85c7-f10a6ce36b8f | -11.30022 | -45.14782 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 740b5080-48fd-39c7-8d5d-16c42fb18332 | -12.17263 | -47.07333 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32f2e782-27b1-3dc4-8d63-8838e0d831e5 | -11.66236 | -47.59476 | 2026-09-02 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15ead726-0fab-3602-9359-8344c50f3a6a | -8.11519 | -54.94971 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9576f816-64bb-3a40-8162-c82a0fa09d95 | -8.47787 | -54.69925 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 554d5c25-8193-33d0-adc9-43d2a8fa226f | -11.30694 | -45.17068 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1459ddf2-7b9d-3b35-8c89-fccae0293d89 | -8.46384 | -54.72944 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea9e6e6c-5ce3-34f6-9d79-0e0d85b2a1af | -15.67431 | -45.8904 | 2026-09-02 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4c0d133-46cc-3d49-96af-e8a084e93d38 | -13.18737 | -44.07192 | 2026-09-02 04:21:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3962c45-de8c-3337-ac22-b7ac6d08acc6 | -12.13457 | -47.14053 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 76d3b0af-ff06-38b5-8b3e-2490a99ce6f9 | -8.48073 | -54.71434 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 3c88e0ab-fdc3-37cf-ba4c-c10a40b3402d | -12.13751 | -47.10057 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b770bd9-9315-3e33-908f-d1abd07f25b0 | -10.99782 | -45.08204 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ad038b46-efb6-33c7-88da-751fe1800197 | -15.37867 | -47.68387 | 2026-09-02 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 049cf31c-de44-3945-bc39-8f7272537b7f | -12.14654 | -47.06536 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a05116ef-abab-3332-a737-9862e4a34ef0 | -11.83592 | -46.03677 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e6e4566-8fd7-3ce0-89d7-6679708f2da3 | -15.36176 | -47.03879 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 634dec8d-fa09-3939-80d3-c8248a1ba9c5 | -15.67765 | -45.89094 | 2026-09-02 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11c19179-44a4-305c-b189-06894d56419d | -14.97802 | -48.12043 | 2026-09-02 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 581849b5-aacc-30b1-a34b-f86cf9cf4275 | -9.00162 | -50.7784 | 2026-09-02 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 509832f3-19c0-3c38-9b26-859059d89ff7 | -12.14019 | -47.12675 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 14661e22-26bf-3491-b133-dc1027c221c9 | -8.46689 | -54.72968 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fdf128fb-ecc3-3074-9c5f-1c8768ba2ca0 | -10.88587 | -45.34575 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d035e590-6292-3146-967c-5bf4287f0c9a | -8.47914 | -54.70697 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| c89b6fb5-58b5-36ef-b22d-78b6ba884a75 | -11.66321 | -50.19393 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 322120e6-d5d2-389b-ae7e-ba8bae2c636d | -11.72458 | -47.63923 | 2026-09-02 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d6dbaf9-a2bc-316d-bd9b-ccc27bcece13 | -9.39875 | -51.67657 | 2026-09-02 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e753ab60-7f21-30cd-877f-43325f080c84 | -8.43038 | -54.71624 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5c79e66-782f-340c-95d1-e4e3b17dec91 | -8.62193 | -54.85158 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e16f773-0a8f-369e-8464-a8dbdccdc5a6 | -11.30091 | -45.18793 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fc9fe28f-dd43-31f8-8f65-ac5f6cd87c7d | -11.82602 | -46.05676 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 228d3fc0-ac33-36f1-aab0-0b6cc966d2de | -11.29921 | -45.17676 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c1c54de0-a2ff-326f-b242-4275959d2279 | -7.55014 | -54.99701 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5852503a-8aae-3623-a01c-fe5b7e213ef3 | -12.09303 | -47.10058 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa69082c-7a26-3263-9d34-ba0efd68b7ae | -11.33702 | -50.62661 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 41a6f1ef-5473-33af-9515-7b43d1fddaea | -10.88641 | -45.34224 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 71843bb3-2eab-30f2-ac29-f7a40f11e3c8 | -11.35534 | -45.40973 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e488ddb-26d1-3425-8692-28345cf8ef4f | -15.17565 | -46.22188 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fd0b1e8-0b12-320f-a232-aac7552ce115 | -10.67759 | -54.04305 | 2026-09-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| a0b5e19d-ba50-31db-a909-5befbc7406b1 | -12.13733 | -47.14467 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 61560472-9955-3b0c-9176-dbe9585d9e61 | -13.37915 | -41.3507 | 2026-09-02 04:21:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 09283fea-c27b-3038-bf75-5b997276eb99 | -12.13808 | -47.097 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8a9aed0-75db-382e-94ab-0bc56b303f29 | -12.15597 | -47.07058 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50a3a5bc-3930-3681-9cdd-b4377ae23c34 | -12.14466 | -47.12012 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b0f7ee2-1eba-3215-82fd-c4d36a45f12b | -9.72548 | -47.77163 | 2026-09-02 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 077552c9-521e-3f87-af56-608a3009c806 | -6.94713 | -56.45874 | 2026-09-02 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e561e131-709f-3d0d-9113-137105c822c6 | -11.63565 | -54.56118 | 2026-09-02 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f50f0f7-2683-3cab-9a8a-2c8a57c81440 | -12.13102 | -47.05549 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d630b85-b34b-3fde-bb09-f76853f5af6a | -10.49665 | -59.61488 | 2026-09-02 04:21:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f77f33ae-7b54-3f81-9305-2a2a3f0dae65 | -8.43768 | -54.70663 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c9b48cc-e314-34c8-835b-1bc834adf7b5 | -14.98285 | -48.02714 | 2026-09-02 04:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1d917e0-732a-3f9a-b3e2-48c9ce2daff7 | -8.43578 | -54.71715 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45875263-4a3f-3f0d-afae-244e233eaf2d | -11.65104 | -50.19912 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7160fe3b-4910-3aea-aa60-175446ae0396 | -11.32224 | -50.61884 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62359b03-9eeb-37f1-8034-1f9661da284a | -8.45922 | -54.7104 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 374c28c4-0de2-3d89-bac6-ac4f42583f59 | -7.29179 | -49.8137 | 2026-09-02 04:21:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0ab262f9-bc8f-3b20-9470-a9179f10d21d | -11.61893 | -54.56699 | 2026-09-02 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 08c94316-06c2-30c9-b29f-3b13e4d6aadc | -11.30307 | -45.17372 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6cc3e741-8118-3028-9732-2c0ecbcbb6c0 | -9.55611 | -48.38611 | 2026-09-02 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 6ede42a5-67ce-3b35-8d72-fc2ffebdea39 | -8.4615 | -54.72874 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f2555f4-9818-3789-b8db-5d017475a470 | -11.82769 | -46.06782 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 75437237-3931-3954-9f18-06aad0ee765d | -10.90297 | -45.34487 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0faa60f-bd50-3ec9-bb9b-5c38f1970b89 | -8.77323 | -46.45753 | 2026-09-02 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2d02aff-5edd-3dbd-84b6-205fff73a6c5 | -11.53498 | -45.45612 | 2026-09-02 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ef3cd2e1-c4cb-3e3e-bc0a-85a150403d29 | -9.70818 | -47.20511 | 2026-09-02 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0864270-0bc2-3f92-b945-1e713ff42a8e | -8.47979 | -54.70345 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| f9cb2cde-2ba3-3f45-8d4c-beee20d9c5eb | -8.45487 | -54.73472 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bb04ddbc-a0c6-3c02-bfe1-bfd8839381da | -8.44117 | -54.71807 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1e966e1-3851-37e0-a776-fd006998c9c1 | -11.5635 | -37.86732 | 2026-09-02 04:21:00 | NOAA-21 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 24ddea45-2d0d-3fac-a98c-176f17f353aa | -10.4084 | -50.00277 | 2026-09-02 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f63f70e0-0301-35e3-8104-499bd94537cb | -10.75658 | -54.06442 | 2026-09-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cf4ea888-316b-3d96-b24f-a14d248fc0a6 | -7.55518 | -55.00097 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 674b6252-9767-353c-93bb-c37c878dab17 | -9.39394 | -51.60235 | 2026-09-02 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 493d909f-46ed-3124-8b8f-42dea51a6b63 | -8.44243 | -54.71112 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d5d4818-768d-3cf0-bc1e-52c3534f9aa5 | -10.74115 | -54.03115 | 2026-09-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4a7c7c49-69bd-3906-a1b6-68f83dc42357 | -11.5362 | -50.93955 | 2026-09-02 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7cfc5e0e-daae-3c7a-b2ef-beaaddea4167 | -12.1379 | -47.14108 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cd661734-d78e-37e8-b899-2e83100a27df | -8.12002 | -54.95399 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8cf93ddd-2061-366c-81b0-c7d807072932 | -8.76763 | -46.47131 | 2026-09-02 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33652149-463d-368a-bf29-2cd1dd9d9604 | -7.29092 | -49.81886 | 2026-09-02 04:21:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c0237574-f458-3496-a51b-72bc7751c456 | -10.90569 | -45.3273 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 2daf33fc-68af-3b8c-b61c-676e5456af1c | -8.12692 | -54.9477 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a97f76c3-59e7-34ec-b227-bf3d942dec71 | -10.44292 | -46.73916 | 2026-09-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 746e381c-37c1-3f61-906d-69f55c56c33f | -10.69989 | -46.21232 | 2026-09-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 914d63c6-d059-354c-84ac-6b9427bbeee3 | -15.37028 | -47.69363 | 2026-09-02 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README22.md)
