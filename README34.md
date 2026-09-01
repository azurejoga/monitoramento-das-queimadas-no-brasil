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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca4c6e58-37b5-3244-81cd-f8ebd5439e61 | -6.91238 | -59.48192 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e784bdc-45af-348c-8286-4917a33b3fe3 | -7.63532 | -55.29438 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d00a3c7f-899c-3899-9e81-37b4329d3540 | -11.25068 | -45.14592 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06354184-3078-3c91-a7c4-b018d984624b | -11.31714 | -45.17 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4bb1cf0a-961d-32ef-85fb-9605ccc4e71a | -8.12668 | -54.96836 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b1e691c-e814-32c8-9c87-cca3fda789f8 | -11.06318 | -51.52192 | 2026-09-01 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f7b0ff4-3fa9-35e0-b4d0-4d9190371fb3 | -8.45825 | -47.54756 | 2026-09-01 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| adb1fd41-ad3a-31f8-ae6e-cc5c56504aac | -5.04264 | -49.2305 | 2026-09-01 04:40:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1c2b0b9-0589-3e7e-bc58-6ac82bb12d90 | -12.10167 | -44.98256 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6f3c400b-26c9-3e4c-9ca0-bfb5a906c9c8 | -10.05892 | -48.69865 | 2026-09-01 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23da2ffe-1a1c-39bc-baac-4571f45ca4d0 | -10.86754 | -45.36039 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 03b3dd51-9e7b-3e53-82f1-f24d1d3b4419 | -8.7158 | -52.36487 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 674e7e4d-6c9b-3c07-8638-aea4dfa59236 | -10.03323 | -44.68413 | 2026-09-01 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 617276ea-dcf0-3135-bc96-ddac50c83af3 | -5.58043 | -60.23613 | 2026-09-01 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5ad8c618-7ac9-3570-bf41-7e0a6e7e4755 | -6.86471 | -56.57261 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 06cf6125-4cb7-384f-8a15-6ddc773a83e7 | -6.95761 | -55.64404 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e4c3dbfe-17a3-367d-beac-47b866b58bc0 | -7.08703 | -45.80401 | 2026-09-01 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c6a2b0eb-1f27-3f7b-b49e-a5effb943a32 | -11.29035 | -50.57474 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| c8a99d61-bdd9-34ae-b94f-d619a422657e | -10.063 | -59.41024 | 2026-09-01 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa17dd61-2cae-30ca-b968-0c75734610b0 | -7.10304 | -45.77325 | 2026-09-01 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4369091d-d5b5-3ad0-aabf-63f5bb26ae44 | -7.11024 | -45.80304 | 2026-09-01 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5aa9366c-7d4c-32ef-8a48-245c2ef264d4 | -6.96119 | -55.6488 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ed4fb456-d04d-3faa-9611-b421f767447f | -11.25426 | -45.15058 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d57b520-540f-3ae1-b1c1-d8e8036a20b8 | -7.02422 | -55.6389 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1911ca26-b47e-38a8-94a8-f053912b8255 | -7.2931 | -60.57678 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7c820191-c1fb-3542-917f-487baf53c67a | -9.14022 | -60.53428 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76a17d83-963a-38bb-af5f-b8dcaebece97 | -10.51265 | -57.4385 | 2026-09-01 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1675acd3-84b9-32d8-8629-5189485b264b | -11.25064 | -50.56841 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08cbe35e-b35c-3518-b44f-2bb4bb3ea3c6 | -3.79246 | -59.34568 | 2026-09-01 04:40:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4236e9a2-dc5a-3312-9682-b1ff5e047ee0 | -6.92566 | -55.63141 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a67d428d-1d78-3729-8cc2-7283385361e2 | -4.85008 | -55.83143 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c6e7eb7-e98b-36b6-bc55-16e5bdc377cb | -6.81082 | -59.5726 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ce870087-7201-373f-8a37-7d7521f27067 | -8.94005 | -62.36639 | 2026-09-01 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1cdae802-892e-3e0b-b025-03cc2313d08b | -9.40882 | -51.67905 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4baea679-7deb-3b7f-96fe-fbd25e383d26 | -8.50385 | -55.30486 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2dc70f8e-9e24-3a23-b252-d80ff12cb993 | -11.29537 | -50.60784 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a96a8f41-bd0c-36a1-9707-b529ae1653ef | -10.741 | -54.02213 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0e4c2083-e6f7-3b4d-b6b2-2b437fae71cd | -5.24941 | -55.91059 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 68877518-a700-3409-b8ae-1bd5895950bb | -6.70586 | -55.41165 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ac43a14a-15bd-323a-b96d-3dcfcca384a4 | -7.04739 | -51.33886 | 2026-09-01 04:40:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a33dee00-ae5d-3da1-a423-a7a0593fdbec | -6.86389 | -56.57341 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 290e01b1-d225-39bf-bfcb-4d875aa25d48 | -4.96055 | -55.84709 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d29c2fec-8a53-3f8b-b298-13a8db1e6e96 | -11.48361 | -45.08449 | 2026-09-01 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1febc3fe-ae7f-3151-8eec-d9a7dd456bb4 | -9.20231 | -59.55596 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fb30bfc-de0b-329d-b2c0-d587ebd1df5d | -10.7498 | -54.03695 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a7ec1a01-1b98-345d-8826-e7d0aeb29708 | -10.04929 | -48.69338 | 2026-09-01 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 74cd0da2-7945-3400-9721-93e046110500 | -8.0031 | -44.28532 | 2026-09-01 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0168d965-0e1c-3b67-8086-063dc25fb7ea | -5.96262 | -57.67611 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0e1702f7-e0cb-3674-992f-fe385536318f | -10.34597 | -50.00049 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 34ebbc76-95f0-322b-a384-bf9d07b7dce0 | -11.33211 | -45.15336 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9886478-fa0c-3f67-a03f-c3ccc18ad25d | -10.8599 | -45.35556 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3cf2b28b-3479-3423-a5a0-6e146be46fd3 | -10.6939 | -46.26273 | 2026-09-01 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 00933f9b-3e39-34cc-b4ee-07e321e13c5c | -5.24494 | -55.90987 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4eeefdb3-816b-3b76-9b33-6b07f599af42 | -10.7528 | -54.06419 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d5289a5e-f7bc-378c-8fbe-bda637128b15 | -7.40128 | -49.63102 | 2026-09-01 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce03f653-5607-346a-bd0b-161419f2faa7 | -8.84779 | -47.08612 | 2026-09-01 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d167476b-ffc9-3323-8dab-daa3daeb247a | -8.2345 | -54.93854 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1afed0f2-1ce7-3064-a161-62518c5dd60e | -10.87077 | -50.47464 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5359d10a-e0d5-3fdf-834c-6585db2f52ab | -9.20828 | -59.55352 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9acdbbb5-d739-315a-967a-7cdc56c169fc | -8.6173 | -54.69345 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6c7978c9-60b6-38e0-9117-7dda810e6f42 | -10.03584 | -44.69669 | 2026-09-01 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| abec3c66-fa3b-35b2-b9ca-6af63280476b | -9.1692 | -47.829 | 2026-09-01 04:40:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 955e2d79-815a-3fcb-8c97-a9b5c77080f8 | -6.21072 | -53.59086 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e74eda18-0243-3565-8753-12332ed95857 | -7.90008 | -44.25105 | 2026-09-01 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3bba2343-9a8d-33c6-b4a9-be3234cc8c3e | -6.42853 | -53.56585 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51dfc0f4-c2a1-3ca9-a010-3f6a152df8f5 | -11.27271 | -50.5791 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4e611975-1ab8-3185-b2bd-b7c401a01657 | -10.75576 | -47.97929 | 2026-09-01 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9e9fc6b6-7df6-399d-80bb-46e4a4fa74c4 | -6.22816 | -55.61921 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3590a7b0-208e-3007-a0b1-9d0064cf8350 | -7.2731 | -46.8058 | 2026-09-01 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 69a4ca93-262e-376e-8b86-5713249ef778 | -6.70231 | -55.40697 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2b549802-640a-3093-b531-4946b971af68 | -8.62122 | -54.69408 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6bd6c7ee-74c5-349f-81dd-d1d402888bdf | -10.85532 | -45.35869 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 638c8cbe-f3ec-396d-ba57-12dc18edd71f | -6.94688 | -55.62985 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60fe572a-bed1-3b21-b9f0-a97b6af528c3 | -7.33874 | -60.58385 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 69ab83bf-8d19-3fdc-b0b2-737fc1370d32 | -8.71296 | -52.36047 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9abc861d-8cec-3bf1-b0c5-f17bf0a89e96 | -9.79549 | -55.30615 | 2026-09-01 04:40:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 025896ff-a35f-3cc6-8ace-009657589e6e | -4.38734 | -55.15759 | 2026-09-01 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca0b22f9-33d1-3dd5-b349-583f98678457 | -5.85912 | -57.55955 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b272761d-a347-3e9b-9fdf-a6d726b33cc5 | -11.28821 | -50.61029 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29fe323e-fc0b-36d0-96b3-9b4e92676ee4 | -10.16318 | -45.7598 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 303e5a1d-c591-3b54-a270-5dca49c6f382 | -7.69089 | -55.34193 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c26c6848-80da-36a3-82d2-2849ad2f842f | -6.27955 | -53.33591 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba54f17c-ee13-394f-9922-4e48c41f47b6 | -11.11155 | -51.5375 | 2026-09-01 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 42eccaad-0947-3af6-83ed-ad568a401f65 | -9.40488 | -51.6821 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fffbd165-e605-3427-99ca-f703e88e01c9 | -6.93765 | -55.63247 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5bcd22e-05f3-3b2e-8250-02aa8028248a | -11.67378 | -47.59283 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e580b679-0e3d-30e7-bc99-f095daba0810 | -5.24646 | -55.89034 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f393b554-e8ec-3bf9-b294-3f859105ba45 | -10.84083 | -50.71002 | 2026-09-01 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8589864d-b8f9-37f2-a032-12ad7ecf1790 | -10.01113 | -46.44428 | 2026-09-01 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad409197-084d-3cdd-9d42-1fb524fb3484 | -5.89623 | -52.25368 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53651e7d-d9f4-3944-9c90-31cea279a07d | -10.40935 | -48.22639 | 2026-09-01 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dca5d423-c37e-338d-acc8-0dba4a6fd119 | -11.31229 | -45.20557 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b2c4861e-35f4-3b52-a2f2-628827a21ea1 | -10.51179 | -57.44319 | 2026-09-01 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| aadb159c-a5c7-3d3d-997a-09ebc0ec8301 | -10.42016 | -57.23548 | 2026-09-01 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53d94c89-389a-3fe1-a953-41575c7079f4 | -4.22273 | -59.87061 | 2026-09-01 04:40:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1dc23291-9f53-324e-8a0d-c8d238a42046 | -11.25013 | -45.14987 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 778bc20b-fed3-3e7d-8511-70d41ea262bc | -10.75456 | -47.9873 | 2026-09-01 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 80293b97-081a-35eb-8833-5b1579b23e10 | -11.24656 | -54.00876 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b71fdd75-8974-3c1b-828d-fdf50d186465 | -11.26388 | -50.57051 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1610bf49-68cc-305b-b672-2e531e27339a | -7.04545 | -45.39748 | 2026-09-01 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README35.md)
