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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecfa9667-2f66-3e30-81a2-a7abe6c522fb | -9.15802 | -61.18658 | 2026-09-23 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f8a66690-55e1-3bd1-aa0a-4629636c4de8 | -9.18785 | -65.85777 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3530c031-f673-3364-8084-ffff0453d23d | -6.45757 | -59.97184 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 498ae170-2718-306c-a2cf-116a348937ef | -3.78276 | -60.74865 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23036e0b-c51c-31a9-a5ca-3c735b23c549 | -5.27818 | -60.2075 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 453cbc62-ce8e-3edf-9767-066ca1a467fc | -3.22234 | -61.0591 | 2026-09-23 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7aa95ce7-8694-30e6-b256-277b64e3e8cd | -3.72481 | -60.57694 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f98b8644-727b-378e-babf-58ff69a238ea | -9.11249 | -60.94721 | 2026-09-23 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b10181a-3d59-3bc1-8c5a-67ece4396822 | -3.74741 | -58.86898 | 2026-09-23 06:08:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e45d7ad6-30e4-3801-84a0-3dc3f36dcff4 | -3.7489 | -58.86518 | 2026-09-23 06:08:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4549a4dd-4e3a-3bcc-8382-03a6369018d7 | -8.53158 | -67.00751 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28ee9f08-2924-3554-9572-8879f1baad41 | -3.53157 | -59.61259 | 2026-09-23 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a014fb20-7792-3830-bef0-1cfe10f6b13a | -3.84958 | -58.66936 | 2026-09-23 06:08:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b27fd8a9-83da-3660-91ce-aeac4d2012ad | -7.50468 | -63.87642 | 2026-09-23 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27bada1c-9e78-3c61-9ef3-0be9e56d531a | -3.55032 | -59.04623 | 2026-09-23 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5b0157b-f1cc-3cfb-9fe6-0e2999676c3d | -6.14229 | -59.92905 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25b7832c-ceeb-3020-a8f0-ac53d2ab769c | -3.90616 | -60.59208 | 2026-09-23 06:08:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8058e817-5288-315f-85c3-7f8ee6390241 | -3.07309 | -61.20866 | 2026-09-23 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 15551c41-527d-33b2-9473-cacfc6ea3106 | -9.15072 | -61.19518 | 2026-09-23 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3994821c-6130-31f4-a382-a581b163d8b2 | -6.39069 | -60.0194 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 870bcea6-2d7c-34e5-8d09-d4924d5e1a14 | -6.67049 | -58.5661 | 2026-09-23 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f0202585-a4d6-3fdf-abea-e332863d946e | -3.89435 | -60.59027 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a636eb6-3228-340c-b1e5-56b0decf0bfe | -6.6145 | -59.91568 | 2026-09-23 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 2ba5fa58-58f4-3f6b-baa4-8e5a2315882b | -6.63295 | -59.93913 | 2026-09-23 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b7544961-d19c-3b6c-a197-a0cbf3a4dd5e | -5.27885 | -60.20278 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 871d8363-6557-329c-85e2-b7664a16d140 | -6.68354 | -58.57454 | 2026-09-23 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e2de0daa-b5a5-3575-bfd0-e5047bb65b4a | -3.68413 | -60.5666 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8f598cd0-874b-3274-9dc3-89e551c27aba | -8.93369 | -62.41859 | 2026-09-23 06:08:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58d3c5e0-fcd6-396d-8eaa-5925f28c5c12 | -4.08959 | -62.09398 | 2026-09-23 06:08:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10b80b30-5f26-319a-bcc0-eedc968cd7bd | -6.62223 | -59.92161 | 2026-09-23 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0ebdeef4-7502-39b4-9584-e5de276840df | -8.93224 | -62.41265 | 2026-09-23 06:08:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2c42916-a09e-32d5-8dcf-5cf262441906 | -5.45516 | -60.14817 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63e5fba7-b978-3db0-bfa7-a593f8bb7056 | -6.45952 | -59.98818 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f682a91b-cb51-3c3e-8b89-c9230a92d71d | -8.59059 | -66.97475 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ec722df-4896-3dcc-b2ae-955e406927f8 | -8.23169 | -62.84179 | 2026-09-23 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0930db11-e00c-33cc-a3ac-39ff4eb1781c | -6.46461 | -59.96748 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4de23601-fa8e-3ad2-9caa-35b00424b884 | -3.69189 | -60.5546 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 874af81f-c6df-3170-a526-33c093acf394 | -6.62548 | -59.99587 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d07de949-03d2-3a5e-8a2d-51b0a6396108 | -3.69003 | -60.56749 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a7be7b99-d837-3138-9506-20471c9aa060 | -3.69251 | -60.55031 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b56001e7-a30b-30ef-beba-818d6995be51 | -4.15563 | -60.79578 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9ca16f1-e884-3a03-aa64-1a404527b3ca | -3.7635 | -59.47341 | 2026-09-23 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d910ddfc-372f-3474-9637-396ce0c11e71 | -6.73844 | -59.42752 | 2026-09-23 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 768ae431-09b8-3015-aaba-68378364ea4b | -6.6713 | -58.55965 | 2026-09-23 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e586050-0a39-3126-8848-56163eb5c979 | -3.85965 | -58.82274 | 2026-09-23 06:08:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 83d94bab-7074-3164-8d9d-32ba51f7ed08 | -3.40907 | -61.29248 | 2026-09-23 06:08:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7632ea24-d20e-334b-9313-7f5aa8b1b92d | -8.22672 | -62.8375 | 2026-09-23 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f7bb2bc-3c06-3cae-b625-70c2daed9743 | -8.93176 | -62.41649 | 2026-09-23 06:08:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db1724d2-f8f9-37f4-bb67-dc3af63fd60e | -9.17639 | -67.55965 | 2026-09-23 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd938f04-42cc-3683-acea-1b79f36683ac | -6.61608 | -59.96861 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66d1b752-9bd1-3747-a2f9-ab2edda8f662 | -9.3371 | -65.72461 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 491c703a-6d35-3b3a-b161-b5cf8b36720c | -6.64142 | -59.9243 | 2026-09-23 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 247e3d88-221b-3111-a6b9-e3b18992377a | -8.52444 | -67.00358 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43d1c29e-741d-35a4-9536-b5081941cfa6 | -5.16474 | -60.301 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b30c3dd-2338-3e45-891d-a7fd573c8975 | -9.22078 | -67.39388 | 2026-09-23 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 847c44d2-5b42-33a4-a23a-f96ebaf909b1 | -9.09596 | -61.43534 | 2026-09-23 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd2ecee4-ff9f-3edd-aacc-617e6f673be6 | -3.68756 | -60.58457 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 734926df-c027-33ef-969e-b0bbc9ab3b3d | -3.77692 | -60.74775 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e161cec9-2425-3dff-b0fd-ba3433462383 | -3.68475 | -60.56232 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f09b9e2c-a4b9-3a6b-8c94-5e3dad717402 | -6.62615 | -59.9908 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ad8354d1-ed53-3221-a83a-38d6ac315612 | -3.69065 | -60.56321 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e7b7cf32-aa28-3ddf-a4af-76ef48138d88 | -5.41429 | -60.21606 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a2e2945f-5601-3260-a1a4-1009294109be | -6.39708 | -60.01989 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9bcd9d9-bcb7-3729-89f8-69791fe6fada | -8.85911 | -62.41973 | 2026-09-23 06:08:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff07c954-82cc-3bbb-945c-a93a359c3330 | -6.62291 | -59.91641 | 2026-09-23 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 67c816e1-2f2b-3340-b3e5-7c97955ef0c8 | -6.4619 | -59.98862 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5791951a-743d-32da-bbf2-02f2998dc90d | -3.78215 | -60.75281 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54edc65e-9f38-3c96-a893-be39fcbbeef1 | -6.63432 | -59.9287 | 2026-09-23 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4a7918f5-b9d5-39f4-82fe-0d33d85ca14b | -3.10433 | -60.71679 | 2026-09-23 06:08:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6bf15be-10b0-3715-a588-35b2c4a762cc | -6.4652 | -59.99408 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 47ac5ec5-1fc6-389c-b02a-73913ae4233f | -9.13619 | -67.94797 | 2026-09-23 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a487e17-32b2-3c1b-896e-2af4044cac53 | -6.6639 | -58.56664 | 2026-09-23 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| feae9e66-a4cd-3059-b9b1-9362860c7710 | -6.11612 | -59.88285 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6dc4632a-4ed7-36a0-b40c-33d1fafa7cb7 | -8.64532 | -67.02698 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86686b8a-09c9-38ab-bbbd-f7d2ac549ca9 | -6.67862 | -58.56225 | 2026-09-23 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6ad2dcff-f3cc-3bae-99dc-93bd56a0dad2 | -9.1891 | -65.84868 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 889b82fc-4482-3c74-ad48-bec925df1ede | -9.25972 | -65.43852 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc3f0ce0-073a-31d4-bf59-1665d4b61bb9 | -3.85889 | -58.8283 | 2026-09-23 06:08:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b1191eff-4e2a-343b-ae01-8f6a34f6c8fe | -6.67775 | -58.56869 | 2026-09-23 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 39c28ef9-0467-3af4-809f-d055dd341120 | -3.68106 | -60.58789 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 887cb0dc-a2ea-3a91-9811-302db971a4a7 | -4.25989 | -60.00887 | 2026-09-23 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bea99f9c-a52c-3cb8-86ca-cac1cffc0504 | -6.4659 | -59.98891 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6e4ef1ed-ff61-3dcf-a86a-2532b35dbc35 | -3.7741 | -60.72603 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03d8814f-a02c-3dc5-82f9-06115946795a | -3.78798 | -60.75371 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a47a2a6-503d-3d7e-9d6c-6d9a39d9ec0e | -3.8605 | -58.82912 | 2026-09-23 06:08:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e62a793e-88d4-348a-9247-98894ffc4358 | -6.14159 | -59.93417 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59ed697d-d3f7-3491-9e5b-70b47216c06c | -3.60631 | -60.57508 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2438230-c190-35cd-9f96-38baf5cf549c | -8.93419 | -62.41476 | 2026-09-23 06:08:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d7ba394-40cb-3730-b448-68ba69ae0afb | -8.61704 | -66.72816 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5b8c5c3f-ac27-3d6d-ac54-52f5e5fa045c | -8.5239 | -67.00725 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4d20b1d-738a-3a0a-b1d6-010907b084a5 | -6.27853 | -59.91615 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc265fdb-5d27-396a-b941-6b90b88b88d0 | -4.0891 | -62.09736 | 2026-09-23 06:08:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 959dbbee-54c0-35e1-be59-94da47195425 | -6.14438 | -59.93421 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c0343371-9cd9-3964-a3ad-8c73d4217e47 | -9.108 | -61.43681 | 2026-09-23 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3489f90-d0aa-3629-99d2-2bed8ddc8f0f | -5.16408 | -60.30568 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b2045fb-2ae8-3fb6-a7e6-c71db4a013c1 | -3.46974 | -59.56932 | 2026-09-23 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b2ac150a-3477-3bd9-89b0-19f1bb0c5f4b | -6.61515 | -59.92596 | 2026-09-23 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| e38c5f0f-9943-3351-a9fb-23236edc4ba3 | -5.93153 | -59.91658 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e867b14f-e37f-34d5-b5eb-960b50b9efb2 | -5.92449 | -59.92074 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a4cc6d72-3cbd-3e14-b27a-a52392d59a2e | -8.53107 | -67.01119 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README126.md)
