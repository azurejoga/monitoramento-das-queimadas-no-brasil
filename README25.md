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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b20b232a-c75e-3ee9-90d4-1e4fa6acc344 | -9.23953 | -50.02015 | 2026-09-02 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 495a004d-c835-37ca-a991-a6907e135de2 | -8.71733 | -52.36209 | 2026-09-02 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0fc2e462-6cee-3dc1-8626-d2e499d04ba2 | -14.32581 | -47.22438 | 2026-09-02 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0645006d-9d54-3901-9796-3a2e8f29805a | -6.94093 | -56.45781 | 2026-09-02 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c8323bc-ad47-314f-a587-2170dee3d848 | -8.45445 | -54.70604 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 191ea8b7-a98c-37ed-8371-ca6ea289bd56 | -10.79607 | -44.75943 | 2026-09-02 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22c8334b-9967-3fd4-a70c-1305608b6a23 | -12.13141 | -47.0959 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8194683e-02a8-3803-b533-aef034bdcaac | -9.66637 | -48.26641 | 2026-09-02 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 288e96fb-7744-390d-8027-b21e3531024e | -11.52404 | -46.9154 | 2026-09-02 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30a60329-e36f-3071-b34d-93e26afc1758 | -11.30029 | -45.16964 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 243c7887-3557-39b6-abac-64997fce7ee7 | -12.1493 | -47.06948 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bed9855-0abd-3a24-a399-eb6e72fc0a26 | -12.34616 | -45.6616 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9561bf6-7046-3cf5-92d5-7ae8f08df119 | -12.171 | -47.06206 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9af54af8-a4bd-3bf7-a8ea-67a28b55d134 | -9.46333 | -50.31384 | 2026-09-02 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f6a3d12-009e-34c6-a192-bbaf98f63541 | -15.64705 | -45.91236 | 2026-09-02 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a11e185-a1af-3313-be3b-7a5aded5318f | -12.17426 | -47.0846 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c66f261a-d917-3adb-a89d-6378ad354df7 | -10.90737 | -45.33837 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92bf3257-4d50-375a-a5c6-dc6065f87674 | -8.47848 | -54.71054 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 2fdcc309-28b9-3cb1-b6b2-c2f9b4d3cb15 | -8.90792 | -50.56817 | 2026-09-02 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 848fe18f-e5a3-3d29-95f9-1c293a39edaa | -15.43407 | -41.80395 | 2026-09-02 04:21:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1c336e37-52d8-39ae-91db-08c9e6b742f2 | -11.53052 | -45.441 | 2026-09-02 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aeb348a7-1853-391f-95f5-d62c474e1f5e | -11.90557 | -45.05626 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da8d69b8-b305-33ce-80c6-bb3cafbca356 | -12.10769 | -47.05169 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf6c51ca-b43e-31cb-a4dc-b1a5f8cfaabe | -15.91114 | -42.53942 | 2026-09-02 04:21:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9346bf94-27ef-307b-b7bd-d1c9caee1c8f | -11.3047 | -45.16306 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a45d4311-d672-3543-9e0e-8b5885d7c5b8 | -6.76007 | -56.33825 | 2026-09-02 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3db24c6e-f5ea-319d-bf22-f1f5408ab0c2 | -11.19752 | -55.11442 | 2026-09-02 04:21:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3d2bbcb5-f173-3240-83e9-a3bf48d4ac30 | -8.71274 | -52.3614 | 2026-09-02 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8033a28b-cdcf-34a3-9307-edbd10c33837 | -13.19027 | -44.0764 | 2026-09-02 04:21:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9fd68ec9-2423-3a4b-8682-df0cbd05214e | -11.318 | -45.16515 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4973db45-7274-3a3f-a4a5-f1d65b34dba6 | -10.41222 | -50.00342 | 2026-09-02 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 357c8cd1-3c63-39e5-b988-a419f7b1ede7 | -8.7038 | -47.55379 | 2026-09-02 04:21:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01677a4f-f050-3f47-9508-0b2b31d57d0f | -11.82107 | -46.06676 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 695905f3-97ab-3aee-8862-ca89c5fb77f7 | -12.12808 | -47.09535 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd65b6f3-59e0-36f0-b7db-223601d8885a | -10.70431 | -46.20584 | 2026-09-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 70c85d68-b794-3477-8a2c-7d67053d59f2 | -11.5383 | -45.45663 | 2026-09-02 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04573ca6-1cbc-3ee5-85cb-5dc2d25f61ed | -12.14207 | -47.07196 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0897a09f-0514-34b8-b2a5-3c532e65b062 | -11.3163 | -45.15404 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92f589d3-a70a-3079-a3f1-df813e1c9f67 | -10.78159 | -50.48072 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| bd6b2d00-0074-3594-a77c-703c92cc78b3 | -11.76914 | -50.55281 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fba2743-324a-3702-96f6-dbb9277e5330 | -11.35353 | -50.62431 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2da4354-fc98-3ba7-93a2-e3f3c3a55d59 | -14.96977 | -48.10759 | 2026-09-02 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d35a9e2-400a-350a-b7c4-502ff7609480 | -12.14264 | -47.06838 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 554d6e39-0efb-3403-bb16-f8e54a3ddf81 | -10.74508 | -54.03767 | 2026-09-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0eddac82-ab7e-38bb-b3c2-01fbe535255c | -8.46642 | -54.71556 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c7baecc1-1574-3d20-9b99-59050cdafc08 | -8.11514 | -54.94956 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| dd67a539-a132-36da-a272-cab0feb65dd3 | -9.45366 | -50.30402 | 2026-09-02 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d24787ab-ceca-33ad-bd5b-35a122311cc4 | -8.11453 | -54.95327 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 35d0c810-c7c8-3bf0-bb41-7dec7a9357ea | -11.3361 | -50.585 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 164112f1-c724-3bf8-be8c-14dd266da8ab | -12.17093 | -47.08405 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 166a9b5d-5fb8-3bea-b53f-e3e460d98dc4 | -11.31244 | -45.15702 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| be946e44-03c1-3d1d-b43b-bc7195eba2b9 | -8.43295 | -54.70206 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1da1efee-7156-3e33-8b72-56073a1b07fb | -11.01707 | -48.37712 | 2026-09-02 04:21:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff6af1e2-dd45-39f0-89b7-5ccf350b4f89 | -9.22053 | -47.97694 | 2026-09-02 04:21:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35bfc5fc-ba9a-35e8-8f5c-242e53700104 | -11.82493 | -46.06378 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 84c16e56-807d-38de-9592-4f84470a4993 | -8.4621 | -54.72535 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4aab8fd3-9317-33b1-b75f-daa3907c72ee | -11.3642 | -45.41837 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51184426-9efb-300b-aedb-f391da5f5eaf | -9.00514 | -50.78249 | 2026-09-02 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e2c30e83-cdb0-3df6-bed4-c665f0effc43 | -11.67704 | -50.47865 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c9e48d5-2b9c-3cee-89fe-8ec15349c4d0 | -15.34466 | -47.03961 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef67dae2-b169-3ccc-8098-e9dc9741241d | -11.76527 | -50.55214 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a00bbf8d-92a2-37dc-a25b-755cb7d6a1aa | -10.04601 | -48.69728 | 2026-09-02 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7a360905-b71f-347d-a60a-81cd3330ad00 | -10.8715 | -50.47372 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59e804b9-8a29-39c9-9d5c-b546b541fa4c | -12.13913 | -47.11187 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 645a9ebf-3199-32f1-a619-d74339852f76 | -12.17142 | -47.10249 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31f7c4a0-9dbe-3fd6-865f-32f9d2489bb9 | -8.13196 | -54.95114 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e5200ea2-1d61-3f6a-8ccf-e5aca9850d9b | -8.43704 | -54.71017 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 279e8f45-30ae-313a-bfd5-fd6f2566c27d | -11.66998 | -50.19997 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c0cb1e3-c7bb-38f8-a617-b8b5f214c662 | -11.66401 | -50.19164 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c96fc54f-cea0-3082-95d9-f13af610c1c2 | -12.12989 | -39.41107 | 2026-09-02 04:21:00 | NOAA-21 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3cea69b7-f7fe-31a7-8e66-0338ea10fca4 | -12.14133 | -47.11958 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e88ce0e9-2270-3756-85ba-d2bb6772f1db | -8.1194 | -54.95753 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fa52d415-6e46-3004-9405-1fd9353bbec5 | -8.47601 | -54.70969 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cde544a5-ac0d-3970-87aa-1c75ea96d052 | -11.34965 | -45.42337 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01756d9b-db99-3303-942a-9bb4a92135dd | -12.14873 | -47.07306 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0634108b-53c7-3d35-884d-7837b4ddbc43 | -13.39248 | -51.38063 | 2026-09-02 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 07b08fe0-1b4a-3050-a32c-4ac783e3ca9d | -11.35588 | -45.40622 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 428cb72b-d5a8-354a-a7a8-e3f52693055e | -11.75753 | -50.55079 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d34616f-c76a-312f-bbe0-e1d59128c9d2 | -12.37681 | -48.1449 | 2026-09-02 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5b2e17a-6ad7-37f8-a1a3-82bfc1cf5604 | -11.53786 | -50.93971 | 2026-09-02 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f5eac3c-20f4-305e-a01d-d5bd5e4b45de | -14.99387 | -47.98039 | 2026-09-02 04:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f94a938c-b344-336f-b843-10b082584ca5 | -8.45671 | -54.7244 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f952f6c1-f36f-3354-89e2-1695657e5a3f | -14.98895 | -48.03196 | 2026-09-02 04:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 937ba643-c990-31db-bebb-8bdad2eed012 | -8.42851 | -54.72662 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c53e1992-418f-35e8-996e-afdee5cbb4ff | -8.2807 | -54.91495 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfbabcd9-a107-3577-b343-5300e7963863 | -12.12492 | -47.05083 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 467bafa4-aaa5-337d-98e1-62c4380e922c | -8.11997 | -51.66464 | 2026-09-02 04:21:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8deaa60d-1f92-3a00-9f57-ea8fdb351d07 | -12.1532 | -47.06646 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 037efdad-08fe-3841-90a0-daa1d60b66dc | -11.67459 | -50.1959 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de8ca423-b692-37b4-886a-a4c027c351d6 | -11.34094 | -50.6273 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7af5d27a-5a8f-3f4a-8fb2-447b1f7a270b | -11.66023 | -50.18856 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 046633fa-9a7e-3f37-9b91-852d731fa993 | -12.10826 | -47.28377 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e42b9681-e6df-3662-af31-e16e31b9c7c6 | -12.37218 | -39.58652 | 2026-09-02 04:21:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 268de00c-9be2-3e15-b262-19434199a539 | -8.44305 | -54.70765 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1f35cb9-4052-3782-8566-d58a7929b409 | -10.89966 | -45.34435 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 13916eb8-8f1f-33e2-ae9b-e4abf9e14b2d | -8.46523 | -54.70784 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 83571c6a-5f3a-377c-afae-fdead7e9aa81 | -9.70216 | -47.17779 | 2026-09-02 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14af9499-0892-3b4d-ba61-b65ea3035847 | -12.14694 | -47.10579 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 529206ee-2a5f-3c15-b803-fe2a558ddb6c | -15.36119 | -47.04237 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e70dcd0-33dd-3b23-8887-a752963e91ef | -11.123 | -51.59262 | 2026-09-02 04:21:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |


[Clique aqui para ver as próximas entradas](README26.md)
