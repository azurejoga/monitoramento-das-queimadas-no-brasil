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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ca8b331-b1fb-3b8b-8151-12d298259365 | -15.14565 | -48.60395 | 2025-09-11 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 506551ee-4799-31c4-93c6-0753860f5cd1 | -8.60793 | -54.69939 | 2025-09-11 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c1f9b7c-0e00-3e30-aa84-c280a7516f19 | -11.21153 | -55.02306 | 2025-09-11 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e024534e-49fa-3f62-8788-3a1c94ed255e | -14.49918 | -53.95079 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f930691-5743-36f6-99d1-e61e0389fdd9 | -15.1396 | -52.43846 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b1b0134b-dac5-3419-9adb-7640032ea0ce | -15.81276 | -52.22877 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4db56348-2363-34d5-b2f9-e1d2f9bbd0a9 | -12.6052 | -56.96183 | 2025-09-11 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7327ae3e-5edb-391f-8e7b-bdea719527d2 | -11.4203 | -43.5508 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8e42446b-4ce8-3974-9344-12e0660ae9b3 | -12.94579 | -54.81955 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62b7eb80-9db4-3a26-897d-97cfefc0d634 | -9.00626 | -49.52702 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df300e4d-2487-3668-b017-9f2f6de36bd0 | -11.78345 | -64.93327 | 2025-09-11 04:46:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7507aafe-9a62-3425-a4b4-19f81d24fd86 | -15.14458 | -52.40624 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03141283-65c4-3a0a-9e83-4afad74e0cbc | -15.56129 | -54.75109 | 2025-09-11 04:46:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d1dff2d3-d01b-3f13-90e8-6c50240c80d7 | -10.55391 | -49.88768 | 2025-09-11 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6055e85c-d335-3d58-b9f0-ad626508c583 | -10.18921 | -46.21331 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4aa131b0-c38d-3756-8eb9-b227479666eb | -14.131 | -45.3883 | 2025-09-11 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1713d1ff-a618-3f95-a53b-d2852fd41eb1 | -15.69909 | -47.89679 | 2025-09-11 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 35d68d79-332d-32e7-9fda-978546d57117 | -16.05311 | -49.99203 | 2025-09-11 04:46:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee0c643d-9323-39aa-950c-da91fa60e0a0 | -11.1236 | -52.05028 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01be44f7-37b5-3c91-8bd0-a7b226378fe2 | -12.91174 | -47.99212 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83ea6207-3226-3601-aea2-b5bccc484c44 | -12.03775 | -47.61402 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a15750ac-b82d-31a3-866b-cb0109d7d0de | -11.22046 | -54.99105 | 2025-09-11 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e167ec6-2b2a-3615-a489-1216303c0d8c | -10.30759 | -48.80225 | 2025-09-11 04:46:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 61923e1a-72eb-31af-83e2-b0fdd5b37457 | -10.54375 | -51.52612 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e02a137a-94e4-370c-9601-622d7044f07c | -10.70931 | -48.30427 | 2025-09-11 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 738f4f1c-44ce-381d-8b29-5d17ab72ce1d | -11.71513 | -50.63294 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e36cdcee-cfe6-326c-bf31-99c739a237f0 | -14.61906 | -48.85144 | 2025-09-11 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2823a989-550c-3bc5-a684-4e58a902c34f | -11.50562 | -50.39582 | 2025-09-11 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e940bf6-ac25-3d4a-93a0-f95d08579e9d | -11.59651 | -52.21637 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50c6ab05-5f9a-3510-a812-0888df6b9341 | -9.46014 | -46.42413 | 2025-09-11 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 1a4766c3-52ab-32c8-895f-08c8f4f7f1c7 | -10.02345 | -51.72646 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 226d05d1-5585-371b-83be-1170a5670f3a | -12.94233 | -54.81894 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0c82a0b-8988-301c-80d9-8bdf58f6141e | -10.74137 | -49.28381 | 2025-09-11 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e320c1c7-01f1-37a2-b0e1-62e3ac9a893a | -10.55275 | -49.87193 | 2025-09-11 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1aea55f-f57b-388a-8961-fba0f8311149 | -9.55409 | -48.24394 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16a3760b-366c-32c7-9493-b6ae452ecaae | -10.37686 | -50.52177 | 2025-09-11 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a39bec2-76af-3506-b209-06312e920b80 | -9.88441 | -51.87563 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd27ab4f-b4e1-30c6-a729-3ff668d9192b | -13.94828 | -48.21288 | 2025-09-11 04:46:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04c8bfa5-6ada-3cc4-990b-193a6f3df074 | -12.00591 | -47.58348 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 9c4bd9ef-c13a-31a7-9d12-225850ad1b89 | -16.70832 | -43.93054 | 2025-09-11 04:46:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d8d65b9-d861-3eca-a570-92df4bf40d22 | -10.56641 | -51.51168 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3658e852-4df3-3789-a26e-4d1bf494f841 | -13.25077 | -51.7753 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1cc02a1-ee00-31a4-99ef-47930aa8e327 | -10.00624 | -51.72701 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ac13e49-04de-396f-9331-1a6c022f8555 | -12.85322 | -52.94518 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce877ade-12ff-3912-94cf-b7fd01cea02c | -14.30723 | -45.03856 | 2025-09-11 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 68344eb4-e2e0-3279-9722-2c9f2dfcfca6 | -11.38952 | -43.52628 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66e62b5a-fb15-3344-91b6-498ec95d5e5f | -9.9676 | -51.69222 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88cfcacc-4668-3d2b-bfea-faca650820d4 | -9.01655 | -49.7818 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f65c0fa-80d2-3d7e-be08-7ec0d0085ead | -15.16067 | -52.32399 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e4c400b6-3454-3c7e-a158-9d048bd07710 | -10.00843 | -51.71305 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d222c32e-f7f1-3337-9fba-0b9b0cc46fa4 | -11.1385 | -52.06347 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa8108aa-9a1e-31df-aa9d-fb97426b9a71 | -14.3018 | -45.03395 | 2025-09-11 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3efedbdc-48b0-36dd-baf1-51da93947e91 | -12.9111 | -47.99666 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3fdab73b-5ce5-3243-b569-871f9c22545d | -11.1948 | -48.39831 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 046e59c4-56bf-3cf7-88f7-55748d0bc096 | -9.08593 | -50.46741 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de2c095f-eb14-377d-bfca-dfe9a1b7de9c | -14.56299 | -54.52403 | 2025-09-11 04:46:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48da1161-e803-3bbf-90f4-a31a54fdcc99 | -15.11661 | -50.14294 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5658d1a8-ea73-372d-a938-d3c82dc7a49f | -11.1523 | -52.04054 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfbac078-3fb1-3f47-8afa-92b5ba04f117 | -12.41645 | -63.89323 | 2025-09-11 04:46:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2257463-5029-3f1c-9dfe-e8f82cbb2f55 | -16.88339 | -45.75445 | 2025-09-11 04:46:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7c204d2-1c96-346e-9b8d-589e38f2cd11 | -9.94272 | -46.06209 | 2025-09-11 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef1b6bac-1f73-3088-9862-29b1e42439be | -9.84329 | -47.78119 | 2025-09-11 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c4557178-8f84-3897-bcf0-9c7793dc5ccb | -15.0985 | -48.04424 | 2025-09-11 04:46:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e6b3010-9e79-3c12-ba53-52e076d89492 | -9.3433 | -48.94759 | 2025-09-11 04:46:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| befe4619-3147-366f-a6a5-9b910bb3f204 | -10.00567 | -51.70904 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93e1991d-f4f3-3d15-bb38-170775cdde68 | -9.99905 | -51.70798 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ed3af97-74bd-34bd-8cd7-a845b79496ac | -15.22715 | -44.04532 | 2025-09-11 04:46:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ac69b45-d64a-314c-bf07-426ad9c01a0c | -11.40646 | -43.53626 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f036ed54-f3a6-37e4-94f3-d0bc11ff7714 | -11.49766 | -50.37928 | 2025-09-11 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fca4b0de-f11d-3ca3-843e-9cae75b91eb8 | -9.45248 | -46.41916 | 2025-09-11 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 11abe6c6-1489-31e9-97cd-5bce086c314b | -14.7805 | -48.23201 | 2025-09-11 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0aecb409-56ab-31d4-8579-8a31e3fb6129 | -12.86317 | -52.94683 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b88335af-35fb-3f7d-a3ce-fe7b9aa889b9 | -15.1313 | -52.42598 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49316862-b1db-3d73-bf5e-1c85f619b0ae | -11.11315 | -48.39819 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 70e22973-f085-34e2-b482-343e94f04094 | -15.27038 | -52.36024 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 62454770-483c-37e6-8497-242bf1a9963e | -9.97753 | -51.69381 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 751d1115-81ff-358c-bb0f-872267ebf174 | -9.0097 | -49.52756 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc4900c9-4fee-32f6-89df-d28ca9720487 | -9.09226 | -49.8125 | 2025-09-11 04:46:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9227d1de-ebab-3f17-93cd-7a68af802320 | -8.62984 | -53.11103 | 2025-09-11 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c1a95bf-aa99-3631-840d-dd77df35a252 | -15.66643 | -47.0312 | 2025-09-11 04:46:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a228d31-6481-35e5-a11c-5d9fa423d619 | -11.13132 | -52.04434 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c095c97-4452-38cf-9d7d-f928704f6ccc | -11.37699 | -45.57864 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afc2a680-b3d7-3eda-812f-4172ca5b7917 | -10.5407 | -49.88175 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02312ec4-b39b-3f8b-be38-5a3a90117a8e | -14.50921 | -53.95244 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b82f261-6fc2-3983-aa46-78e85e93e726 | -9.30662 | -46.77147 | 2025-09-11 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0dfef1d6-cf25-3bec-af1c-50e6971bd38d | -11.35633 | -56.31643 | 2025-09-11 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3a891a1-c3dd-312c-b222-b710351c33cb | -9.71156 | -48.33871 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e25be4f-3d01-371e-bf61-069a43acd113 | -9.07309 | -50.48385 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 889ca9df-4762-3e1d-99c1-9e81f4d3e373 | -15.618 | -52.76619 | 2025-09-11 04:46:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 230edf39-068b-324e-90ba-0b854576e8d5 | -12.24063 | -47.333 | 2025-09-11 04:46:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0517af4-faa5-3609-a336-d6d55b98cfc7 | -11.13188 | -52.04084 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fcabd58-6b17-3dc9-b5f0-810e1a3710b2 | -15.1623 | -52.4239 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 531dd0cb-4eae-38d3-820f-30df3083596d | -16.37736 | -48.87943 | 2025-09-11 04:46:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 278ae384-72e6-33b3-af69-29122e82d1bd | -11.74331 | -46.53194 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a7a866a-89aa-38a0-960f-290b1917ab18 | -11.08954 | -48.43045 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1413dcef-7bfe-3e31-b214-02ff61d61982 | -10.55643 | -47.23238 | 2025-09-11 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe8b49dd-9cf3-3f8c-a905-8fb79e621e71 | -14.91571 | -47.30794 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7211f050-650f-3690-ae2a-308a40b72d1f | -15.14015 | -52.43488 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0caba7cb-7d5c-3bcc-9810-a82b26c7ca31 | -12.11686 | -51.05072 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d7fbf4d-462b-3a2e-9582-6349f86d10fb | -15.56745 | -54.75598 | 2025-09-11 04:46:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README117.md)
