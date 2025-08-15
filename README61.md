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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfba22dd-def3-3e4f-8992-74b9e23e1f84 | -9.90651 | -60.4367 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e666967-8f52-3db9-a51d-c6ef651b3581 | -7.60318 | -63.52264 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5c9e6b16-f905-34dc-a035-b82a4ae5f2d2 | -13.11803 | -57.15623 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bb43779-6a4a-366e-8b53-53d965a9e7fa | -7.60914 | -63.52326 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd8e991b-018b-3b33-bf1d-e1133a47d478 | -9.53595 | -63.57628 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f7162fd-314f-3d89-9dbb-776dc69af8a0 | -9.14623 | -59.4259 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f4ceffe-da71-34bb-b7c4-3052e4cef17b | -9.052 | -60.65205 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5512dfc-5b05-3ef4-95a0-0b9119e0ea84 | -10.32155 | -63.62239 | 2025-08-15 05:44:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5c4606d-7b65-3abc-aa1f-7af04da6e602 | -9.15845 | -59.65764 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91bea98f-d334-3009-92fe-76713b14cc9f | -9.92176 | -60.48343 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 28698497-d815-373c-b055-9ab93adfaacd | -9.93446 | -60.48518 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abee8f8d-0bd5-3118-a48f-24a4c0ec1b0f | -13.11349 | -57.15183 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6d103d3-a4e9-366a-9f20-fefa35b2fe0c | -8.11367 | -55.58485 | 2025-08-15 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0615f8dd-c60c-3f77-b5e7-3cdfd9cf4b57 | -9.1808 | -59.69205 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 247e2c7c-2f55-3535-943c-07f089b02669 | -9.1673 | -59.65889 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b05f89d4-0117-3602-9cf9-a51dd2952172 | -9.15786 | -59.66198 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dccef337-308c-35b9-aa1b-6b2f4abd3c23 | -9.16492 | -59.67637 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c1a3656-12b3-351d-abb2-d029701a5c20 | -9.39008 | -60.55147 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9866cdd3-c34b-36da-8f30-3f4338c48e5a | -10.16774 | -59.66376 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 788f2061-fa80-37c2-beb8-c227a6220c9b | -9.15757 | -59.69744 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20736de4-106f-3521-87f9-108723c5acac | -9.15551 | -59.67935 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bc89703b-d097-3d22-b86f-6c9e6cbf9571 | -7.9685 | -71.37505 | 2025-08-15 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 823bc696-c138-33af-9e57-92dbbf3374d1 | -9.50664 | -60.51987 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b5ced053-6472-3437-9bce-11a67c80a35f | -7.9455 | -61.74483 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 824edccb-aa71-33ff-9d92-c2b83e52cbc3 | -8.40314 | -70.43417 | 2025-08-15 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b54c91b1-42ac-37fb-b45f-5c9376587f85 | -10.05481 | -59.11589 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09740941-8697-30fb-91ad-9d85dc651c82 | -13.1177 | -57.16346 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d53221ba-dcfc-341d-a1b3-17a4147466a4 | -7.52673 | -61.37739 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| fdc21a6b-1076-3762-9352-5cf885e053fd | -9.54298 | -63.57735 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0e3f0fa-8963-319c-b4bb-aa5ad5129edf | -9.39952 | -60.54492 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5ccb642-9151-3169-a2d2-6d7716aebe13 | -7.53547 | -61.34426 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7705adbc-2cf9-3950-9be0-561e7a7f80be | -7.52603 | -61.38225 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c49f7e41-c838-3c70-98d3-2bcfb5aebd3a | -8.47025 | -64.06644 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a285f24-57be-3fb0-9871-7356be8f0549 | -11.34282 | -55.41364 | 2025-08-15 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 321d8bca-31c6-384b-b1d7-affb53c42381 | -9.17758 | -59.68269 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ffb97b7-07bc-36d3-939f-c4e37b5c6aab | -15.39819 | -55.78139 | 2025-08-15 05:44:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bdde9120-e82f-37b7-9cdb-dabedf0a57b1 | -9.2063 | -59.63786 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| be0d72a1-9ef2-3fd7-8846-6b3f8993c027 | -8.60421 | -62.6541 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a1b93ce-da51-3a46-89bb-ade0e9f80379 | -8.10799 | -61.18119 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 174f179e-1839-3dcb-b520-f74baa251b53 | -11.72649 | -64.89772 | 2025-08-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5cd4aef6-bc81-399d-80d9-f0bfde2d39de | -7.55072 | -63.49512 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aedf37c0-0421-3117-ab18-ffdd797f9311 | -9.18199 | -59.68335 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f00a592a-5d09-370d-ba46-7a759fc6fd70 | -9.19262 | -59.67157 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4c4db4c-42ca-33bb-85d6-9f7d1ae2beb1 | -7.60609 | -63.50357 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 9317c6d2-333d-31ff-aac5-8fbbe5eae383 | -7.87903 | -61.82955 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e7c62bd-7d89-3717-b046-e6342063ed29 | -13.12036 | -57.14167 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68e79692-d1ea-3282-9933-5b3bcf61407a | -7.61663 | -63.5205 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe82b8d9-61a0-3b24-b0f9-389347425c6d | -12.88946 | -62.09037 | 2025-08-15 05:44:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3188bc30-4f44-3363-9d3b-69d7d5f82321 | -8.10509 | -61.20139 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 838cc1bf-006d-368f-ad8e-c29a143345fb | -9.90956 | -64.23482 | 2025-08-15 05:44:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36181086-4bbf-37c0-b5c3-67f7f0b3fcee | -7.95171 | -61.75527 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1078cd95-2525-3253-b46b-c892833b5d90 | -9.15285 | -59.66568 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aeb6951e-f1c3-381a-a447-2bd9610f6f1e | -11.7367 | -64.89931 | 2025-08-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7eb4b3a-1dfd-3cd8-a302-c8cec2a4f653 | -7.90021 | -63.5268 | 2025-08-15 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46611145-27e8-387b-b608-a81eabbbf0c3 | -9.19143 | -59.68025 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8304b0c1-3e7e-3ac3-b563-dd59be531bf0 | -9.63033 | -63.09229 | 2025-08-15 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af191ad5-7469-3a1a-947e-deb13d9cb0ee | -11.34724 | -55.4283 | 2025-08-15 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8da2d420-8b8c-35fc-9026-531d9556a88a | -9.17138 | -59.69511 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4493b1a9-35c3-304d-9c79-aa0448fee374 | -9.15199 | -59.41745 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75fa3ca2-e98f-30a7-9a5e-a9dbe1fbe066 | -7.60663 | -63.52318 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17f74003-732a-3f09-be93-26f3c6040195 | -8.60326 | -62.65595 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d65da3e3-f02f-3c09-ae02-099821fbb458 | -13.13424 | -57.16206 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e185eb3-6f65-3724-9d4b-db90f8694159 | -9.63171 | -63.09568 | 2025-08-15 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| beb6f313-2447-3a45-972a-d64d1b59f9ba | -9.90227 | -60.43607 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f70c27de-0408-36a9-ab15-591ac5c2780f | -8.56444 | -66.96112 | 2025-08-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e845b5d-c9b2-3171-8aa6-d4e6e66c890e | -9.5019 | -60.52318 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 24faba38-326e-36d2-bb9d-4924a82d1537 | -9.90239 | -60.43768 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb4528aa-f7a5-30bd-a98b-3babe2d8593d | -7.43282 | -67.73702 | 2025-08-15 05:44:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84879198-0908-3913-99f8-777520e5840d | -9.21093 | -59.66959 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b1953589-4991-399e-987c-979609dad3cf | -12.88874 | -62.0956 | 2025-08-15 05:44:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88d61e80-2ad4-3969-b57c-418abcb38ecc | -7.53371 | -61.32906 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d7ae7c4f-0232-3e31-8d18-dbb6a8f46c0a | -13.47947 | -56.66496 | 2025-08-15 05:44:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 5d39bea2-c13e-333d-ac7f-7df504b83210 | -7.94792 | -61.75469 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c24fb007-09e5-352f-a5f0-a839d33c3450 | -10.00795 | -59.21807 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2cc3bdc0-f8af-3e72-8336-2b01b9ada6c0 | -9.1195 | -63.9202 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2db18687-be11-3f0c-bc93-3a7019f91ac3 | -7.59056 | -63.466 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0e21c90-fdb7-32e4-980c-e605e5001281 | -11.41086 | -58.53614 | 2025-08-15 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 354d96c7-e77f-3334-8260-79d66badc825 | -13.11678 | -57.16718 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 150679a4-b865-3e6a-973a-9559b331466f | -7.63047 | -63.52262 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 909d0356-270a-3cc1-84ea-eab1a05b5f34 | -8.55612 | -63.91488 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8758ab7d-4faa-3927-b3fa-031792951346 | -9.20329 | -59.65965 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3b38fc45-30cd-3b75-a225-5f554734fd98 | -7.52984 | -61.32848 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 8b7bc667-44cf-36e5-bd63-626600c4e350 | -11.7333 | -64.89878 | 2025-08-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b07deff-afef-3537-8d29-b414636516fa | -9.9223 | -60.47944 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 743b2587-4ece-3cb4-aa3a-d0480ced0dd0 | -7.89207 | -61.47769 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 036838bb-577a-37f4-b26a-6a8cbdf5678a | -8.05169 | -61.59877 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2bb25e60-cd87-3e98-8efd-dccf19d07c96 | -9.89644 | -68.5942 | 2025-08-15 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf611d6a-9aac-327f-aa0c-1fddad5a8403 | -8.11295 | -61.20255 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d63b2da1-d919-3ab1-98b7-963bcb2418a7 | -11.35491 | -55.41548 | 2025-08-15 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9d71f8f5-8a89-3a85-a04b-c39f4d90fbae | -8.1144 | -61.19246 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1a2151d5-a037-3b20-89e7-7618bf31e481 | -9.17877 | -59.67399 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c5083a6-92d4-36b6-a162-54eca34d1496 | -7.53745 | -63.48918 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c3d80d4-fd30-30f6-9194-3bcf3d303aa1 | -9.915 | -60.43787 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89dc8bc9-1797-30b2-b8e2-9d7a9780a889 | -9.19441 | -59.65856 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40954836-3d0a-33e5-8bca-198bf1e8034f | -7.62298 | -63.52538 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e75f199-28e8-3fac-af94-2bad8e8d779b | -7.9593 | -61.75643 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 18cb11ea-6e6c-3a3f-a34b-8f4f359eb6b7 | -9.50555 | -60.52763 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 51e2ac36-a4bb-3c2e-a897-b2591e118a8a | -7.81745 | -61.3305 | 2025-08-15 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 07e4288f-cbea-3242-b117-d75b454e1d93 | -10.25116 | -64.31659 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3b03c5e-3cb9-3914-ade4-850fa724f436 | -10.11779 | -57.76735 | 2025-08-15 05:44:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README62.md)
