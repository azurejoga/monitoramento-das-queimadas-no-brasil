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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e044cbbf-ebc8-394f-88fc-531611b3fe6e | -11.30614 | -50.92976 | 2026-10-02 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2be85607-a905-395f-9dc7-3ee63fb3443f | -11.6517 | -43.55464 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73ffda0e-f824-3ce6-99ec-bc2734ddb58e | -10.53552 | -53.71549 | 2026-10-02 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bdc6a9a5-449b-30ed-8e48-0e919ab0ac1c | -11.78219 | -43.5661 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1fa581cd-2180-3708-ab6a-57ff1872f685 | -8.54106 | -54.55729 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b61fb694-5e1b-34f9-a142-100f73c497b6 | -11.47536 | -43.43468 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f1d98b54-c6b1-310c-bcc3-f24c30ca6278 | -8.26401 | -55.69602 | 2026-10-02 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f573188a-a9cb-36e7-acbd-035bec39b7e4 | -9.80215 | -54.29776 | 2026-10-02 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 439c1109-eec9-3cea-9656-9197a9a3d585 | -13.55664 | -53.19153 | 2026-10-02 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4774d3ac-8e4e-33f0-bfcf-4918e2d59f24 | -11.79069 | -43.56603 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31c838b7-49fe-3f5c-aaf8-ed3c775c7904 | -9.57778 | -54.62863 | 2026-10-02 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 69f3df5f-8240-3e22-a331-3c64419f4528 | -11.73513 | -43.58104 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 49983bbf-fd13-3201-9dc8-dfeda8c98eb1 | -11.18138 | -58.16108 | 2026-10-02 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe9c5c68-0aa4-3ef2-9f87-9dedecc2c1ab | -10.25269 | -49.67568 | 2026-10-02 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 65415380-f57f-3aed-a3e5-4d0fa56b02a5 | -8.54052 | -54.56076 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2005ba21-9892-3694-905f-7166cbe25f12 | -8.72653 | -54.98489 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32d5b0dd-edcf-3049-ad4b-acde658152b9 | -11.33915 | -51.30027 | 2026-10-02 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 94e1d437-9e20-3fc0-8f35-21eb71c19b8b | -11.1291 | -44.61115 | 2026-10-02 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37ed25ab-23e4-38f5-9f62-2913e33413ff | -8.29391 | -54.72457 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 597e20bd-df52-3274-8667-373097077b5d | -11.66448 | -43.61095 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f9e03565-a4a0-3953-ace4-b9ddc4865143 | -11.72551 | -43.43779 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3dc9c025-9d3c-329e-adb9-24ca6faef332 | -11.66094 | -43.60868 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3afda9a6-6ba2-32c7-b362-b8174e25c37b | -15.51434 | -46.13023 | 2026-10-02 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65bbbe57-f163-37c4-9674-63c2b15ca319 | -11.42563 | -43.39869 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 42acc41c-808c-3447-a898-ba36eb03f5f0 | -10.41443 | -53.76438 | 2026-10-02 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b38b310d-6a52-37e9-95fb-3dd56df057a5 | -15.51793 | -46.12914 | 2026-10-02 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d497d5ea-c5ab-3434-abad-9e1ff1c0e348 | -11.76345 | -43.57816 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 12295def-05ac-3642-85c9-5b84c17aaea1 | -11.45849 | -43.41076 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07593d4d-174e-36d2-b773-f19154849ced | -10.32835 | -45.36193 | 2026-10-02 04:59:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3834fc6-ff76-35e5-8a45-8dd3183ece72 | -13.86713 | -43.64157 | 2026-10-02 04:59:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a721c0e8-39a8-38df-beae-8000173fc38a | -10.30576 | -44.63499 | 2026-10-02 04:59:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b5a3433-8a7a-3acb-96ee-f8fad17ed280 | -11.47319 | -43.4375 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| de0439f6-442e-3d7f-ba72-7c049df4f590 | -11.78368 | -43.57083 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 218b87c2-c624-302e-86c6-a50bf823c1eb | -10.29778 | -44.65163 | 2026-10-02 04:59:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e780666-53c0-3397-aa93-a40ed9d9ce42 | -11.74417 | -43.44576 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9836fe0-6e23-3915-bd30-9fa16f134d8e | -11.80229 | -43.57806 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ce90aa7e-3974-3b94-9fa9-55b7f1ce21e2 | -11.1469 | -44.61357 | 2026-10-02 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a8404025-601d-3224-aaa5-e9ccc10fcafa | -11.25179 | -45.22715 | 2026-10-02 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 532d88e7-a61e-30a6-b042-af6aa2528a82 | -9.65081 | -54.33136 | 2026-10-02 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 896cf975-9aa4-3607-8e72-49ab0d86cff0 | -15.30977 | -42.77448 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 61ee7778-55d1-3424-988f-416b97fdd9c0 | -11.43784 | -43.40581 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 86dff9dd-d610-3a05-8d60-8ab579ebd3e0 | -13.3363 | -43.86352 | 2026-10-02 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4cc7e7cd-7097-3380-9062-913f6fbdd8df | -10.43587 | -53.83898 | 2026-10-02 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 506c507d-c7ae-3b1a-a54e-c027dffd75a2 | -8.41924 | -54.7053 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c2a4b4a-621a-3541-9036-ef7b1f1e5e2d | -11.43143 | -43.40493 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5c521803-5ecd-3a68-ba89-0ed3b46a1280 | -13.34199 | -43.85212 | 2026-10-02 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aaf77d78-ea02-3f27-b81d-fabc99e1f49d | -11.15823 | -44.61962 | 2026-10-02 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| d985c902-8150-3e4d-af57-a0a408c3e8eb | -8.54436 | -54.5578 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fccbd399-e327-3376-a690-8c23103a72bc | -9.86798 | -48.2312 | 2026-10-02 04:59:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a37621d3-1d03-3539-9e79-b21e4c4ffff0 | -9.78196 | -44.80328 | 2026-10-02 04:59:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aad09e60-637e-3987-a2ef-795df623d2d4 | -8.23349 | -55.28669 | 2026-10-02 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5b018c8-8877-334b-a664-ca0265ec6abb | -11.47014 | -43.42308 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f44eb7ff-5442-3820-9ead-ad2e1ddbba84 | -11.80176 | -43.58273 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9ba9c617-282a-3f8f-b56e-31be1c36c5dd | -11.46742 | -43.4313 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d00ac112-ce79-395a-9a5d-4ae234b2d7f8 | -10.20996 | -49.96261 | 2026-10-02 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 814cf410-dde6-30df-a149-63cfcaf931ec | -9.68765 | -54.31248 | 2026-10-02 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 03477e9a-5454-3e09-89a2-8362c553bacd | -10.77966 | -53.7677 | 2026-10-02 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03181545-d12c-363a-bc73-725e9a86dc40 | -9.74752 | -53.89609 | 2026-10-02 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8b3786e-3cad-3bea-adef-f8000c1e52d9 | -11.15281 | -44.61452 | 2026-10-02 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6acf7a28-d5a6-3f95-aa8c-951084326880 | -9.65027 | -54.33488 | 2026-10-02 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0659f98-7a41-34cb-a16e-1405568d88df | -11.45789 | -43.41612 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8134d616-5c6b-3dda-9fbe-39334221efb0 | -10.60942 | -50.04776 | 2026-10-02 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e26b5f87-08c1-3c0a-8df6-968423e23e1d | -11.78839 | -43.56849 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3daa519-8430-3a6b-be18-f2d4841a8504 | -10.61668 | -48.05201 | 2026-10-02 04:59:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 388e77c0-e648-3cd2-9c1a-6aed8111e16e | -8.31049 | -54.7308 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95dd3a9a-f875-39a6-a1c0-3b863d363473 | -10.4325 | -53.83846 | 2026-10-02 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef795428-4a11-3490-a5ac-59b0d849c285 | -14.34499 | -44.73262 | 2026-10-02 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b892c8f1-7d0f-3c80-8da4-964c025fad04 | -8.53392 | -54.55972 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34b1140a-4f4f-3926-8652-0f7c3b74f8d8 | -13.33387 | -43.86678 | 2026-10-02 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1b40d238-9b7e-34c2-b58a-f650040e7d8e | -10.3037 | -44.65189 | 2026-10-02 04:59:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bf5fb80-226a-37fb-a41a-892484bfca20 | -11.46227 | -43.41976 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b72c2382-6476-32da-8b2e-f6813a2c230b | -15.32317 | -42.77679 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f194d57a-17a7-3cf2-bbbd-a95833c750b2 | -11.13022 | -44.61941 | 2026-10-02 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea8e4e5e-b663-3c89-a427-b505868ea603 | -9.80162 | -54.30127 | 2026-10-02 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ad7c24e1-67ee-319f-bbf8-68f6f7b6a4eb | -15.24912 | -46.16893 | 2026-10-02 04:59:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 659898ae-5e3c-374b-bfdd-1b3fe64f10fe | -10.26781 | -49.65818 | 2026-10-02 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 11e26cfd-00f7-3239-b037-f65a30fed9ce | -8.53722 | -54.56024 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c5d85b3-2949-3801-ab96-895dbc70739c | -11.45646 | -43.4137 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1917a9c-df92-324e-9781-8ef4edb56a91 | -10.24904 | -49.67124 | 2026-10-02 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 613679ab-14de-3717-a526-e2e6c0f9c839 | -11.23951 | -45.23302 | 2026-10-02 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0fdb2e1b-15c8-3264-9f6a-76877d101248 | -11.24907 | -45.23132 | 2026-10-02 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 13170987-cf18-34f8-91bc-224e10559e87 | -8.30657 | -54.7301 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41221015-6612-3534-930b-2db6e43de3ce | -11.44426 | -43.40662 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c156f438-8ed1-3162-8200-8365d5fe572a | -13.34268 | -43.86436 | 2026-10-02 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0078609a-37aa-33df-8ce9-628d84e9564a | -9.20898 | -57.71921 | 2026-10-02 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fbec0477-425c-3f50-a02c-3fc74acc55cb | -10.53329 | -50.02536 | 2026-10-02 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c4ab00d-0f73-3713-81ac-7bd116c46ee9 | -11.15772 | -44.62398 | 2026-10-02 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 64bf582d-554a-3c4d-94db-ee8437435ad2 | -14.33178 | -44.74003 | 2026-10-02 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3995c840-5441-35ab-8895-9ac5e2723700 | -11.75718 | -43.57621 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 582881ef-4139-318a-b40a-80a8acf5b6c5 | -10.24106 | -49.97718 | 2026-10-02 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 237dcbeb-a35c-30e0-9dcc-4d7695fde162 | -10.2626 | -49.66529 | 2026-10-02 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ede16d4f-037d-34e5-b3a6-d3d1c1c1c441 | -12.85895 | -43.81261 | 2026-10-02 04:59:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5efb37cf-0c50-37f6-8c1c-e292f80e2996 | -10.26729 | -49.66204 | 2026-10-02 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a0bfd856-1263-35b3-b2a5-afbc62df170f | -10.78021 | -53.76401 | 2026-10-02 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 006bc4f0-9ae4-3587-8c55-34bd3ab8c0a3 | -9.80318 | -48.18969 | 2026-10-02 04:59:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| dfcb50be-04b7-3af7-ad13-e6637c4ecd54 | -11.41859 | -43.40326 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 380e89a3-9c04-35eb-a325-a1fb6bf838c5 | -10.9031 | -51.18383 | 2026-10-02 04:59:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| aa544b44-1a8a-39a7-8a78-67b9920eb172 | -8.53998 | -54.56423 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4324928d-7344-3088-9d53-8a5993c60451 | -9.78079 | -53.83487 | 2026-10-02 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5acf6b3-d74f-3a17-a38f-ed5cdbb2fb79 | -15.52576 | -46.13133 | 2026-10-02 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README70.md)
