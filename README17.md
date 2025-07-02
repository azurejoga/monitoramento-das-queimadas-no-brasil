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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f46cb10-9795-35e5-be09-84272522b32b | -3.03362 | -49.4339 | 2025-07-02 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f17e2397-ae50-31f8-9420-2206843bf5ce | -4.28173 | -48.19088 | 2025-07-02 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac16e0de-9b55-3305-af65-8e7412a3c51e | -3.03936 | -49.43148 | 2025-07-02 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 326982f3-91f6-33ec-aa66-6c73886239aa | -3.03305 | -49.43759 | 2025-07-02 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e9b05f6-20c8-33e7-bd98-a5d95838f9ba | -11.24199 | -49.49197 | 2025-07-02 05:16:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3439d3be-453c-3ca5-bfc4-2e09dc5bf5b3 | -10.88144 | -53.75851 | 2025-07-02 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7dfa4268-45fa-3a7b-bd65-cf55627644cb | -9.24599 | -58.74436 | 2025-07-02 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72c33b1b-f95d-3410-9f8c-b739bed3db0d | -9.7029 | -56.18401 | 2025-07-02 05:16:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5da1ddff-3f01-3a84-b3c6-8dcc96f254d1 | -9.2306 | -50.04275 | 2025-07-02 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb0449bb-a0bd-3999-a2ae-0e7e1d28a952 | -10.04325 | -59.36042 | 2025-07-02 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef1c816a-95b3-32cd-acb9-2a8bb6ff01fe | -9.04173 | -63.99053 | 2025-07-02 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b926731-91f2-3ecb-a0c1-3d2c3df54f49 | -7.61539 | -45.74868 | 2025-07-02 05:16:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 205c9765-aa1e-3be5-949e-822c41bcde62 | -7.60924 | -45.74069 | 2025-07-02 05:16:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f6973748-5936-3512-b386-5f71273c65f5 | -11.23533 | -49.49032 | 2025-07-02 05:16:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa118791-2de1-3004-af22-3d1c42397052 | -7.60839 | -45.74746 | 2025-07-02 05:16:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 114d3d56-056a-3340-bd60-02575cf9a92f | -7.03614 | -55.5038 | 2025-07-02 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b8937ce-5f76-3456-b72a-c079cbe11d95 | -9.23205 | -50.03186 | 2025-07-02 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bcbd49e-0dbe-358f-828f-4d5cdca554b5 | -10.89577 | -54.05295 | 2025-07-02 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d054cb4-3c4a-3882-b083-32a794791d43 | -9.63371 | -61.46964 | 2025-07-02 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5cb98b4-62f0-391a-8d1f-5d0f5c6b44b8 | -9.57287 | -49.10269 | 2025-07-02 05:16:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c64eab3-a8d6-31f0-bead-dafeeaaa0eb1 | -9.81568 | -48.37468 | 2025-07-02 05:16:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3344392a-e493-3559-936e-351843a878ba | -9.9572 | -54.1702 | 2025-07-02 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c13d8ec-ea21-33ce-87ec-1b458178bca6 | -10.3003 | -57.13439 | 2025-07-02 05:16:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2626c52-d761-38ad-91da-d5b629604aeb | -3.1177 | -59.92836 | 2025-07-02 05:16:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ea1d638-008f-34d8-b4f2-6d9a40df8134 | -9.57232 | -49.10696 | 2025-07-02 05:16:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73d4248b-2211-3585-843e-a2d56dddf0ca | -7.91756 | -61.55806 | 2025-07-02 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2100671-8005-3cf5-9e66-98bb15fac57d | -10.87327 | -53.7531 | 2025-07-02 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b6d9af2-787e-3ca3-ad4b-d9d53a3e5c76 | -7.61069 | -45.74816 | 2025-07-02 05:16:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 749a94f3-f8d1-33a8-b77e-6e00bcc25965 | -9.24932 | -58.74488 | 2025-07-02 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df34734a-6295-3a8a-bee4-d45732eca8cd | -11.2356 | -49.49546 | 2025-07-02 05:16:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a206bf5d-91f5-3220-ae1f-6ec4f1310fa0 | -11.32856 | -51.44507 | 2025-07-02 05:16:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96861f2b-ee29-398d-a977-41beaf4ffe41 | -7.6098 | -45.75489 | 2025-07-02 05:16:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d113e936-59df-3bbd-85c2-b3950604ab11 | -9.27523 | -57.82293 | 2025-07-02 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83a9fc47-0688-343d-8ea1-07dda732f666 | -6.54229 | -55.02844 | 2025-07-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 318b9ec0-a606-3634-a5c4-5b2ff2da7738 | -11.33372 | -51.44577 | 2025-07-02 05:16:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 429ddb08-3bd8-3082-92f5-25033484402f | -9.24992 | -58.76309 | 2025-07-02 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd72c29e-f9c9-3344-ac3f-04e685f8c7fa | -10.29676 | -57.13387 | 2025-07-02 05:16:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 433e8938-d3ca-3db9-b2d9-4a95f77f8d6f | -9.2667 | -57.8331 | 2025-07-02 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a5e3a23-577b-3a9f-b16d-896912667c91 | -9.34562 | -58.84715 | 2025-07-02 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82e6107f-0f71-301d-8ec2-f08ff201f1e5 | -9.95662 | -54.17422 | 2025-07-02 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f432215f-80af-377b-bee2-afb254a3e767 | -6.89941 | -52.19481 | 2025-07-02 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 827d41ea-1798-3620-9ddd-be36166b83d4 | -9.25435 | -58.75655 | 2025-07-02 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1daf1d78-ad2f-3297-a8e6-d8d6b3809d01 | -10.94312 | -54.36885 | 2025-07-02 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0dacc69b-862a-323a-85ea-9b87164fdfbe | -9.23157 | -50.03549 | 2025-07-02 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc66774b-ab5b-3817-a443-7f13cc8f0369 | -9.6343 | -61.46597 | 2025-07-02 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba7a8a64-1806-3313-9ba3-398667144aa6 | -6.7077 | -51.41594 | 2025-07-02 05:16:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| aa3f59a5-fcd1-3f54-b834-4b697efa7f34 | -9.23108 | -50.03912 | 2025-07-02 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14ec639c-7c13-3f00-8dc0-291e1b107dcb | -9.04255 | -63.98572 | 2025-07-02 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12b7bb08-b2ca-3007-a0f7-ae9c26e90049 | -4.53662 | -48.02248 | 2025-07-02 05:16:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1b449c4-288b-3983-9c0b-9cc78613dda0 | -10.89521 | -54.05711 | 2025-07-02 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ce8a8b5-7162-37ea-9efa-a6b03b44dde3 | -9.24211 | -50.04058 | 2025-07-02 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1fe0907-52bf-3e58-9519-23b724abc6d1 | -9.2366 | -50.03985 | 2025-07-02 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ba462db-e64e-3abb-95b4-e6747ee2fcb1 | -9.24878 | -58.74842 | 2025-07-02 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4054d86-a857-3e65-bd67-bae9ac0c6f49 | -9.70356 | -56.1796 | 2025-07-02 05:16:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 655cd378-b94c-388e-93ec-c8d4f3d4890f | -9.23805 | -50.02895 | 2025-07-02 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b9e854b-b367-380b-9390-73328e778ec0 | -9.44428 | -57.18175 | 2025-07-02 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f0bf8be-8573-35b9-81b1-6ad89033d586 | -7.30914 | -55.3061 | 2025-07-02 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 162f184b-d68a-3c41-a8a0-1837cf5f5b54 | -9.24823 | -58.75196 | 2025-07-02 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db90acdf-cd70-3336-b299-6ccaee6e8293 | -6.70897 | -51.4139 | 2025-07-02 05:16:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c33efc14-1261-3ce3-846a-6430688d9cdb | -6.70975 | -51.40858 | 2025-07-02 05:16:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d221b205-b789-328e-bdbd-a14dff84d741 | -9.1129 | -59.05567 | 2025-07-02 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 228d19f7-2778-30de-8bda-38db7b566425 | -6.70843 | -51.41062 | 2025-07-02 05:16:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 53e0e24a-2485-3f87-9cb9-34f3736b6ad0 | -7.60753 | -45.75425 | 2025-07-02 05:16:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b01eba1b-b220-3043-952a-2bfcee8ca02c | -10.30385 | -57.13491 | 2025-07-02 05:16:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34b73bc9-f6d9-3417-bf52-760f99a56d3e | -7.92508 | -61.55539 | 2025-07-02 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 125499bd-2451-388b-acbf-dc28e5b91b7a | -7.61455 | -45.75531 | 2025-07-02 05:16:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e6b36d9d-702a-3d63-836c-a2b99d1515f9 | -9.38395 | -63.43541 | 2025-07-02 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3307195-d5ab-3c51-8e10-3a00c04af2b5 | -7.60368 | -45.74699 | 2025-07-02 05:16:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93d3831e-aa4f-37ec-8318-40513fa9a1ac | -9.2538 | -58.76007 | 2025-07-02 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0082750-d9fb-3846-8dc8-597665e4ecb2 | -4.31544 | -48.07836 | 2025-07-02 05:16:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9fba286d-0c40-3b20-ac84-9b712e79196c | -10.87765 | -53.75368 | 2025-07-02 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edcbf23e-6546-309d-8da9-966fd9e3c624 | -9.11344 | -59.05216 | 2025-07-02 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4580299-7310-36e7-89ac-671f4ee12949 | -7.93197 | -61.55651 | 2025-07-02 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f491cea-7050-32d3-a7a5-1a02bd8f303a | -9.25429 | -57.52338 | 2025-07-02 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fed73316-ce5d-3547-a106-a751edfa11e1 | -9.24544 | -58.7479 | 2025-07-02 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 887497ae-f479-37d0-86a9-f8e16b65040b | -6.53471 | -55.02727 | 2025-07-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1aea590-e978-33c3-a7cb-3fb92cb8e275 | -9.82185 | -48.37561 | 2025-07-02 05:16:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a585ce5-2e0c-3168-ab29-807cd4856d31 | -10.29615 | -57.13791 | 2025-07-02 05:16:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9cc97988-5f5c-39f6-b4a3-87412bc40494 | -10.861 | -53.77742 | 2025-07-02 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c348ff4f-b21e-3f82-bf7f-d078bf31e321 | -11.23612 | -49.49128 | 2025-07-02 05:16:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f37fd2c3-c8d1-3814-b8da-b7cea910d20c | -4.37395 | -48.08665 | 2025-07-02 05:16:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad967457-2ff2-3fd0-b23b-2ef096ba0e13 | -9.3423 | -58.84662 | 2025-07-02 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd73c770-f61a-32ff-84f3-348d8b57cfc1 | -11.23484 | -49.4945 | 2025-07-02 05:16:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6147fe6-130a-3b25-8a36-648632b48ff5 | -9.44325 | -57.18326 | 2025-07-02 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 088a303e-e28f-3bea-9347-f6d3b2dd7ecf | -11.24121 | -49.49104 | 2025-07-02 05:16:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fea1608-f595-3652-9f78-58f00dbcb7e2 | -5.2847 | -56.02024 | 2025-07-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 34a13907-50b5-3536-80c5-fbe8c29082d0 | -7.61682 | -45.75594 | 2025-07-02 05:16:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b5140cda-81d9-30ee-8d6c-7d15125cacb2 | -9.70577 | -56.18291 | 2025-07-02 05:16:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9edec747-5b03-3382-a3f1-d42df0a7fcb2 | -4.37454 | -48.08265 | 2025-07-02 05:16:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b9bee49-8f40-321e-ac1c-4da99e822e08 | -2.95344 | -60.01474 | 2025-07-02 05:16:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28d7a384-8290-37e2-ab54-d5d256226486 | -6.5416 | -55.03307 | 2025-07-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f357815-848c-3e25-a9b5-e882370045ae | -10.46024 | -58.6845 | 2025-07-02 05:16:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| db26075e-8098-3317-a9eb-969291782236 | -9.70208 | -56.18234 | 2025-07-02 05:16:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a54d7e7a-f053-319b-b3ec-5955ff15e16a | -10.86595 | -53.77378 | 2025-07-02 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53dd5b21-888d-3a9f-89c3-a2bb2a49fc7a | -10.29798 | -57.12576 | 2025-07-02 05:16:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfc95bf8-b087-3cf8-864c-aefb3d4aeb88 | -7.89334 | -61.47309 | 2025-07-02 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7e2bf37-1b7e-362b-a86e-c8d3d35feed9 | -10.30324 | -57.13896 | 2025-07-02 05:16:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 816b2baa-0159-3b68-b3b2-43fbd9dd81f9 | -4.53722 | -48.01824 | 2025-07-02 05:16:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dfb0ad6e-529e-3988-8505-d79496b6a152 | -6.5385 | -55.02785 | 2025-07-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4658377c-9eb2-3194-8711-a2dfdade699d | -4.3207 | -48.08336 | 2025-07-02 05:16:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README18.md)
