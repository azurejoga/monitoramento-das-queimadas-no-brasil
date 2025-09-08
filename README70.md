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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74281a4a-cc09-36d3-a53a-9aea81b30571 | -13.83037 | -46.29391 | 2025-09-08 04:53:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a672f20-7c0c-3202-914b-07b326ed92e2 | -12.62954 | -56.9867 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6684ff83-330c-367e-9aae-5b09418de295 | -15.18953 | -47.97451 | 2025-09-08 04:53:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b666acf2-1012-313c-bc10-2bedba5047dd | -11.22336 | -55.01759 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8cf88f10-5e74-3500-bd95-efddeaf4363e | -9.30188 | -66.61375 | 2025-09-08 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5099df35-c7b7-315a-951b-73417ac914ce | -15.71971 | -53.55165 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1feb4b25-08c2-3d1a-8277-ea06a01f19d9 | -15.15583 | -52.32367 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9196acce-fcf1-3026-8a67-d461df518021 | -12.60972 | -56.97506 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9d4e80d-bf05-3c72-a921-9f3c016b7a2b | -17.15132 | -44.43645 | 2025-09-08 04:53:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b79079dc-6706-37ac-b339-1d04a42aefbc | -12.95094 | -54.79123 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da6fcee6-f128-3afd-aea1-d881acb9d671 | -10.77229 | -59.85309 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d797473c-c0cc-316c-ac71-d29061ea53d3 | -12.62032 | -56.97682 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d5ccda93-c906-325a-bcd6-2d6ab3540229 | -16.35971 | -43.64148 | 2025-09-08 04:53:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78e5ccc4-959c-33e2-92a2-18e0782fe1d5 | -12.47841 | -53.83659 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f1064f6-b213-3087-bb51-9a1050f61565 | -10.99839 | -52.06183 | 2025-09-08 04:53:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 837637a5-523c-3071-a908-87a8161e7024 | -14.80563 | -48.2463 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6918528-5151-3d0f-a6b5-2b39f60a3a42 | -13.90946 | -53.96982 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b5158ab-2361-31a4-9c62-f3238abca906 | -14.87751 | -55.81149 | 2025-09-08 04:53:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c06ee3c5-4f7e-39d6-829a-c515bdb52ce2 | -13.00322 | -45.21109 | 2025-09-08 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 147fd0f6-b80e-3cb0-a787-c8340103502a | -16.29123 | -49.55058 | 2025-09-08 04:53:00 | NOAA-21 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 94154081-fd14-39d2-84bb-549d965a13af | -18.14037 | -43.3992 | 2025-09-08 04:53:00 | NOAA-21 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1d95a658-9d12-39f3-806d-19f28b344d8f | -17.26186 | -46.69585 | 2025-09-08 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7cc1c94-7b09-3143-9927-7051adab3af9 | -16.33044 | -52.93044 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 57aa07a2-9251-34c0-90d6-1428b43a6c2e | -15.83193 | -52.29865 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cde41fe8-5758-3821-a1e7-a60ce2dadd91 | -13.01405 | -54.8232 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ff9159b-8933-3dca-9d25-f480e41137ae | -10.89264 | -55.71452 | 2025-09-08 04:53:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 38d5f65e-d3a1-3dc5-9aae-8ac0a7702ea4 | -11.8729 | -50.95904 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6358914d-ca15-3dab-a097-46f4f1b1ac0d | -14.29288 | -44.86709 | 2025-09-08 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 647abade-2efe-365e-9ac5-2ff39e4b485d | -17.22535 | -48.28524 | 2025-09-08 04:53:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5fecb77-ce0d-3ef5-a86b-a6ea597c5cea | -13.74336 | -46.90001 | 2025-09-08 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d6ef4261-5532-3814-93de-cea3829abd99 | -13.72351 | -46.90466 | 2025-09-08 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ace16e0a-20de-380e-bfb4-e6b36a5e5ab5 | -16.34418 | -52.9326 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4fae98f9-6a65-3940-a4d1-4b561cb2ba2d | -12.94926 | -54.80186 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7dce4bd8-9605-37b3-81ec-f042465ff127 | -14.68648 | -48.19578 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 43b22768-81b9-3d6e-85bb-a6d69e104b81 | -15.24166 | -52.35645 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c85a4b52-c368-36df-9090-4699c5b4b204 | -15.24455 | -52.36107 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f147610-a1b5-3125-a017-68b1f39e55b9 | -17.62415 | -44.83021 | 2025-09-08 04:53:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e7db76f-1129-3e17-9d26-6952c38eedb4 | -14.60649 | -48.0847 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4daed84f-a96d-3524-85d7-6f6405738551 | -14.69589 | -48.19207 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a54a644-e613-368f-8d9e-f4508399257d | -12.9322 | -54.7809 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6f8eab7-ad32-3843-9345-4c5e1fd933fc | -13.89348 | -53.9854 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 26dd3811-39d5-3e84-95ed-44fd8543ce81 | -16.94091 | -45.84637 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4056917-60e2-35e8-99cc-fd7dbde63465 | -11.6451 | -52.23566 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5b33514-fe52-33c4-96e1-5b99396658a8 | -13.74266 | -46.90545 | 2025-09-08 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3ea3abac-934c-35b5-af98-aeb3a97653e3 | -12.62805 | -56.97399 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 343cfd2f-562c-3aef-a938-55e0ca3c2566 | -11.19502 | -55.00193 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 33053664-383f-31b8-975d-f9bcedb85999 | -9.47561 | -60.48802 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e1dd7205-5fd7-33c6-b481-7695d7e93ae3 | -12.81645 | -56.52053 | 2025-09-08 04:53:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fc741c8-72a2-3d29-b241-f9d2f893a34f | -12.94707 | -54.79423 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ef80fe9d-08fc-3818-85d0-9e42201f78c5 | -12.85728 | -47.97874 | 2025-09-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c88a2929-660b-37bd-ba28-5c7db21fe64a | -11.81707 | -46.76865 | 2025-09-08 04:53:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| db7b1fea-2ef3-3a86-aabf-cfb940878a0f | -15.19345 | -47.97962 | 2025-09-08 04:53:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 14dc0c09-2c91-3d29-913f-27c92f57b81e | -9.452 | -61.82294 | 2025-09-08 04:53:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 5c07b1c3-861a-3525-8729-d7e03a0be995 | -9.47394 | -60.49759 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c59e02b-525f-3f43-91a1-acc21a7d69ed | -15.5095 | -52.7753 | 2025-09-08 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fdc5fa9-e2a5-3304-b294-7f2a858514f6 | -15.24107 | -52.3605 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9fb7960-8c1b-379c-869f-03b992e7d2c9 | -11.10845 | -52.05173 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a5062a5-db38-3ba4-8f83-a303d8e480b8 | -14.54612 | -53.27035 | 2025-09-08 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c362bfd-6267-3b1f-b803-205d469316f9 | -15.83581 | -52.30209 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0745e41d-1c05-3d76-8573-ad13d8ad778f | -15.74657 | -53.53329 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33199e1b-79e5-33b2-a2b3-660bf513d5ca | -12.94106 | -54.76783 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b5fb364-4455-3e45-a542-71ca628800f0 | -11.11399 | -52.01446 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 019686c4-cdcb-331b-b178-4199716164f9 | -16.35049 | -52.93752 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5ef72197-eb48-3f59-ace1-828638d7c991 | -15.85572 | -52.31334 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fe0d15b-8511-381b-b991-3677341f5edb | -14.29833 | -44.86799 | 2025-09-08 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fac192c-a203-3dfc-9fc6-dfae12b6373e | -11.452 | -49.25356 | 2025-09-08 04:53:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7af1174c-fba8-30a1-9756-acb79cf64f49 | -13.8215 | -46.25452 | 2025-09-08 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e1742540-516a-3330-b4dc-0d755a05330f | -17.71199 | -44.47862 | 2025-09-08 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0832c6e-1b89-3f3e-aa14-33d46441214f | -10.08558 | -59.17673 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53173c61-e133-3cf0-aa1d-da1a77b8c096 | -11.18299 | -55.05523 | 2025-09-08 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea81cd3a-119d-3b7a-99cd-cc9f14df74ba | -12.93989 | -54.79669 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 029e6e62-4a3b-35ab-933b-55d757ce6107 | -15.83134 | -52.27814 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 630790da-7705-3158-ac22-9ccd4293d39f | -10.42739 | -59.6097 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7602a332-a7e7-3769-a72e-699ff479a077 | -11.1014 | -52.00163 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48184533-a647-3d87-80c9-72e9f63d6daf | -16.35337 | -52.94187 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d252f1d5-3601-3eb8-9680-36cb626c75ab | -15.15289 | -52.31944 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a7cb603-6faf-35cd-b6ab-05bc532dc864 | -13.73382 | -46.89925 | 2025-09-08 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7613a190-6231-3886-804a-ba58972a0f48 | -13.54579 | -48.10564 | 2025-09-08 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe8f51b1-7dd5-3177-b386-392ab3afc481 | -16.06292 | -50.48013 | 2025-09-08 04:53:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88ff30ec-8f78-3af5-a0e0-2c049cd31ded | -11.6475 | -46.64169 | 2025-09-08 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99ef08cd-7834-337e-a353-e605ce7fea21 | -10.87798 | -60.7334 | 2025-09-08 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ceadb9b5-d367-3e22-b5f9-b7440c5f0773 | -13.81461 | -46.25938 | 2025-09-08 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 798ad15d-c948-3ec0-b79d-3b34fc3b6a1a | -12.6309 | -56.97863 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 271f4170-f907-34b3-bb34-36e5a70f995f | -15.13681 | -48.06825 | 2025-09-08 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b670e4d7-894d-30af-a4bd-a02b47e16fe6 | -10.8731 | -55.72683 | 2025-09-08 04:53:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d0a6a67a-d7a5-3f4b-bbac-30d9f83e715c | -15.23471 | -52.35534 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f23dcae-bda6-317d-99d5-9bd796b11ebf | -13.70832 | -46.87229 | 2025-09-08 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 73f599ad-50bc-37d4-9dfa-d6b22c21e1ff | -16.34074 | -52.93209 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 81cd443c-77b3-3106-9092-73e2377be7d7 | -13.81628 | -46.28616 | 2025-09-08 04:53:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2d7c788b-009e-35b7-80ea-811177c482de | -14.99622 | -48.01855 | 2025-09-08 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d329180c-be3b-30c6-8ce8-f44a0f6e1c48 | -15.99491 | -55.95668 | 2025-09-08 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 426d1d93-1e40-3324-9d1d-a9a3d909394f | -16.33331 | -52.93483 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97cdaeb2-ddeb-31e1-ab66-9a0b596eabae | -11.37287 | -50.35992 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5ccd0c08-c6a3-3937-aaa6-6fcfe0e04d1e | -11.61757 | -47.14623 | 2025-09-08 04:53:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ce0405a7-8092-3ab8-89e2-6068d140be0f | -11.2017 | -55.00301 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 75be2939-0623-37d6-8132-0961030c306e | -17.65988 | -44.18406 | 2025-09-08 04:53:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34b2ae85-fe4b-3874-a96d-2ad04da10205 | -9.47934 | -60.49363 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 632fd5db-c752-34f4-a613-a2bb6950d124 | -16.55137 | -45.10815 | 2025-09-08 04:53:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e7543d7-ff38-3f6a-be06-4b91603923e9 | -18.14701 | -43.39605 | 2025-09-08 04:53:00 | NOAA-21 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2a36b9fa-091a-34b7-88e5-b090f65400e1 | -15.83638 | -52.29808 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README71.md)
