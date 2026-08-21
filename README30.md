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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3565ca17-3e74-3990-803d-6b73bef0834b | -14.57148 | -52.99636 | 2026-08-21 04:04:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6fa43ce0-c4fe-3cd3-b978-2d1a6d091a9e | -18.10757 | -40.89273 | 2026-08-21 04:04:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0676cbc9-89e9-3396-8086-70af4442e679 | -20.01702 | -45.53233 | 2026-08-21 04:04:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed1a62f9-c1ee-3ff2-8bdd-de094188fc19 | -19.842 | -43.16403 | 2026-08-21 04:04:00 | NOAA-20 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 85d2e82b-8e59-3b95-ba60-48354ec9b76a | -14.33969 | -51.89167 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 418a7d5a-d74d-3d01-b151-460dfe37b17d | -16.72171 | -47.68831 | 2026-08-21 04:04:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea983817-ec92-354d-81c3-8f3b96e8ad12 | -18.65689 | -43.17585 | 2026-08-21 04:04:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 01378b80-8783-3200-8958-6bd3653686bd | -18.03505 | -46.47 | 2026-08-21 04:04:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14dce8f9-60c2-39f2-9a2e-60f18b35a8f8 | -20.63306 | -43.55938 | 2026-08-21 04:04:00 | NOAA-20 | CATAS ALTAS DA NORUEGA | MINAS GERAIS | Brasil | 3115409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3db9fdcd-673e-30b3-9b9e-263f10117e70 | -18.06001 | -44.42449 | 2026-08-21 04:04:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6d47f96a-99c9-3c75-be4c-d7a980b1d5f7 | -15.55535 | -50.28273 | 2026-08-21 04:04:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 58415f98-2a3a-3f28-af2e-afb3c341d55f | -20.52853 | -44.09453 | 2026-08-21 04:04:00 | NOAA-20 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 27efdb82-f2b4-3800-8bec-f37b06065558 | -15.00132 | -52.67933 | 2026-08-21 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c405d7fd-54d8-3e3e-b6bf-a6b17f8e44eb | -17.9627 | -44.44311 | 2026-08-21 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66c02b81-d715-3b1c-93ec-9baff357c0a9 | -20.04704 | -45.62021 | 2026-08-21 04:04:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3be308a-dbef-38cd-9e42-aefed03638f1 | -19.70477 | -46.91705 | 2026-08-21 04:04:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8926f608-c387-3c04-a157-e5cdc7414e49 | -19.70547 | -46.9133 | 2026-08-21 04:04:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e20c1be8-fc2d-3db8-9e02-381ad0f5145d | -14.43879 | -51.81472 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f62d24a-9b53-3c85-b0ef-6d0964168b38 | -14.20467 | -52.87864 | 2026-08-21 04:04:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5d2a340-1c10-3d20-b599-7ed0c80f1962 | -14.5594 | -52.9875 | 2026-08-21 04:04:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12639277-df57-35ae-a5b8-336f53771ac4 | -19.66598 | -46.05009 | 2026-08-21 04:04:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95ca465e-89ea-3c7e-9f14-7bba5d5f6027 | -20.65633 | -46.19111 | 2026-08-21 04:04:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9374e659-811c-3121-a52d-6feae446b86e | -20.70687 | -44.82809 | 2026-08-21 04:04:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 75256c7e-0086-3cda-9f65-3cd507c3cd9a | -19.93605 | -43.6317 | 2026-08-21 04:04:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d7c0a62e-d3ec-33c7-ae4b-2e4bbf448c27 | -20.83507 | -44.19292 | 2026-08-21 04:04:00 | NOAA-20 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 126853b9-867f-362f-8bcc-ad320693322a | -19.81595 | -44.0841 | 2026-08-21 04:04:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c0e8078a-d3d5-3ac2-aefa-074faf0fad1e | -17.96059 | -49.37666 | 2026-08-21 04:04:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 463b3f9f-f94c-3d4f-9e34-ac1fc8b91bb1 | -21.74271 | -48.55933 | 2026-08-21 04:04:00 | NOAA-20 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a84d8d08-d1e3-33b7-8138-191c768e49a3 | -20.25467 | -46.73888 | 2026-08-21 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8294b6c1-4575-350b-bfb1-f6a3ea976822 | -13.93262 | -53.86339 | 2026-08-21 04:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d3a02473-c1d1-378a-a7d7-7cac1a3531fb | -18.87891 | -42.04388 | 2026-08-21 04:04:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 6de57eb9-e32f-3599-a277-558cabe34aa6 | -16.91389 | -39.43081 | 2026-08-21 04:04:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 55d671d6-fb39-3616-b794-4fee9e5195d0 | -21.5783 | -43.47617 | 2026-08-21 04:04:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 479ac2a7-8a46-31c7-b7ac-9e11bea76c68 | -20.66007 | -46.19206 | 2026-08-21 04:04:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3399d9d1-99aa-3d55-a849-4ad1a51e1c97 | -15.12166 | -48.14351 | 2026-08-21 04:04:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d55e0ae-51d4-3b63-9d33-26a45f1d07fe | -18.06226 | -44.41164 | 2026-08-21 04:04:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4904f7ea-6781-31f4-93aa-e50236ffbbfd | -19.67369 | -46.04344 | 2026-08-21 04:04:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 92e43c7f-cc51-3364-b941-17d8ee2dfeae | -16.09366 | -45.13682 | 2026-08-21 04:04:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98a5a64f-900a-3e75-b537-6c349bd05377 | -16.72083 | -47.69297 | 2026-08-21 04:04:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 926e3ca2-b2d3-3c86-8340-45df5f759911 | -14.56466 | -52.99424 | 2026-08-21 04:04:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b5c8c59c-c916-30a4-856e-4bb605969826 | -14.30159 | -51.8265 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 65251d1c-e532-3a00-9f95-740a9fb4bced | -18.02345 | -44.6118 | 2026-08-21 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6cac269d-b310-34fc-8ec1-cee360ff2cc9 | -22.17934 | -48.74072 | 2026-08-21 04:04:00 | NOAA-20 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b952e4d3-784d-3958-9a5a-edd41e8965d0 | -15.56143 | -50.2802 | 2026-08-21 04:04:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e83e844d-d76e-3b19-9b93-a329c1a7dfdf | -22.58285 | -45.70226 | 2026-08-21 04:04:00 | NOAA-20 | PARAISÓPOLIS | MINAS GERAIS | Brasil | 3147303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 12561b85-fd73-3518-a870-8c30909223f3 | -20.26319 | -46.75867 | 2026-08-21 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 91d2f615-38c6-3488-b9ac-a0acc0502593 | -19.67536 | -46.04179 | 2026-08-21 04:04:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 34e8fc6d-6e13-3833-b41a-00136535d544 | -15.16581 | -48.78171 | 2026-08-21 04:04:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| abc6c3a8-b4bd-3b2a-9489-ba0362405170 | -17.63659 | -42.32462 | 2026-08-21 04:04:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7a4ba412-ca0e-377e-ba24-f47edc6fbcf3 | -15.0053 | -52.67781 | 2026-08-21 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d30d98c8-eda3-3b0d-ba93-420c888cb3b1 | -13.93946 | -53.86468 | 2026-08-21 04:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2d1a71a1-f5a0-37f2-bd20-7d3239e34f80 | -16.9607 | -43.5552 | 2026-08-21 04:04:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbe10420-90e2-320f-855e-a03f1e5c4e67 | -15.71824 | -47.78951 | 2026-08-21 04:04:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aebd9700-f8ea-3625-a734-c9723a1f407b | -17.95758 | -49.37505 | 2026-08-21 04:04:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5ea164c3-5a5a-39af-9857-42e62c162ffe | -20.00459 | -43.97371 | 2026-08-21 04:04:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a0756d3e-ba0d-3036-9048-07686ec6ab95 | -20.25932 | -46.75756 | 2026-08-21 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a03f2f9-d786-3ba2-a9df-ac62a6f6a801 | -15.71107 | -47.80243 | 2026-08-21 04:04:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c713d2bc-59ef-3e65-8940-2d32140cf54b | -14.33492 | -51.91449 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6de39309-8f55-3117-83ba-1b5cc17ba73f | -21.74184 | -48.56367 | 2026-08-21 04:04:00 | NOAA-20 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 78eb4a12-cbe1-3638-9d82-efa03392a2f5 | -14.3066 | -51.89919 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 6d479f1d-e075-3957-8e2c-cacbbf215bad | -19.8766 | -44.95528 | 2026-08-21 04:04:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 199e1887-4b5a-3106-a72f-f5452697734b | -16.57017 | -49.40223 | 2026-08-21 04:04:00 | NOAA-20 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b771f15f-69eb-3fbf-bfc2-9d70a8835f41 | -14.34097 | -51.91571 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f7545f9-e2a5-318c-91e2-d5646177a453 | -19.53554 | -41.99683 | 2026-08-21 04:04:00 | NOAA-20 | SÃO DOMINGOS DAS DORES | MINAS GERAIS | Brasil | 3160959 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 839043fc-c0ce-34ba-8e09-603d5a207c95 | -17.95592 | -44.39708 | 2026-08-21 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97dd14b0-e08f-3ddb-bc1e-4136249e3cf0 | -21.32247 | -43.80624 | 2026-08-21 04:04:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a423cea4-ff33-3fd1-9414-c894f26bfcb9 | -20.83439 | -44.19692 | 2026-08-21 04:04:00 | NOAA-20 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 837197f5-4f06-38d8-9f41-19221d8ced9a | -18.10425 | -40.89217 | 2026-08-21 04:04:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 77cc790f-5125-3469-8b52-8ae43da9119e | -22.51683 | -42.64478 | 2026-08-21 04:04:00 | NOAA-20 | CACHOEIRAS DE MACACU | RIO DE JANEIRO | Brasil | 3300803 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b43c8677-3275-360e-a40f-274c84248b6a | -14.99663 | -52.68768 | 2026-08-21 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 28349366-b770-357d-8e45-226f78a0cb82 | -15.16464 | -48.78767 | 2026-08-21 04:04:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d44c3b7d-45db-37d8-8771-33a389402f75 | -18.03242 | -46.46177 | 2026-08-21 04:04:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ccd6895-73fd-3bcc-ba18-29d93eac4164 | -19.66218 | -46.04935 | 2026-08-21 04:04:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 42d25b5d-271e-3f99-bb5a-5deac4a47949 | -20.95727 | -47.19725 | 2026-08-21 04:04:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f2c1706-d863-3711-ae2b-46a63290a3e1 | -18.88179 | -41.08648 | 2026-08-21 04:04:00 | NOAA-20 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 481e4613-df44-3639-be63-2e340ec3fdf6 | -13.94633 | -53.86587 | 2026-08-21 04:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3da8cb95-b99d-3fc3-81ef-98a5746a285f | -20.48451 | -43.40171 | 2026-08-21 04:04:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8a31b165-05ba-3cfe-814a-a0390283d4bd | -14.32377 | -51.90751 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 61e35634-46f0-3e97-9399-c929a7d0885c | -14.32279 | -51.91217 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4e05f60d-5268-34cb-8394-3bbdf8cf0d66 | -18.65663 | -43.17896 | 2026-08-21 04:04:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| f83f480f-a4af-3fba-a78a-ccba3a7832a3 | -19.93485 | -46.08846 | 2026-08-21 04:04:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d699e6f8-3fd7-345f-aadc-68fb4f097252 | -21.74696 | -48.5603 | 2026-08-21 04:04:00 | NOAA-20 | NOVA EUROPA | SÃO PAULO | Brasil | 3532900 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30f7c239-c350-3b40-8554-36a867ce57a1 | -14.34003 | -51.9202 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 453997a0-84bf-3d37-8d10-230fabca0749 | -16.96138 | -43.55118 | 2026-08-21 04:04:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d285292-6f79-35cb-b36f-f69706c86bed | -22.37794 | -43.02312 | 2026-08-21 04:04:00 | NOAA-20 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 43f0bb5a-3387-34e1-a422-107433b55857 | -14.33078 | -51.90415 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2c4e3cdb-cd31-322c-8fca-23092442e6a3 | -14.33873 | -51.89626 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9b328b9c-57da-3759-89ba-1effb387a959 | -20.31891 | -42.74314 | 2026-08-21 04:04:00 | NOAA-20 | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3b56f9a5-ea47-3e53-8b45-123376f133c7 | -21.01476 | -44.85391 | 2026-08-21 04:04:00 | NOAA-20 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 99641ad0-3928-33e3-a080-c00c2e5f2044 | -19.33813 | -44.15418 | 2026-08-21 04:04:00 | NOAA-20 | FUNILÂNDIA | MINAS GERAIS | Brasil | 3127206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| edba1a69-f384-36fe-84c3-3e905b99aba8 | -14.32982 | -51.90871 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36005636-a4f2-3d93-b893-7718f69ac209 | -22.37855 | -43.01941 | 2026-08-21 04:04:00 | NOAA-20 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 17662a5b-e933-33b0-b74e-9b5951ff7f8d | -18.03068 | -44.61314 | 2026-08-21 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 49bc0ae7-a71b-3bb2-b7ba-16369a5d04cb | -14.31771 | -51.90631 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cd25cbdf-f4e3-371f-b38d-a3158da287f9 | -19.66978 | -46.05087 | 2026-08-21 04:04:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59bf296f-cc23-31cf-9234-49bee2efc7a7 | -16.21553 | -43.50092 | 2026-08-21 04:04:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04f3205e-d0c9-322f-aff8-cf15d6273c0a | -20.685 | -45.26751 | 2026-08-21 04:04:00 | NOAA-20 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 90950ff3-31fa-366f-b05e-0643c921c643 | -14.34573 | -51.89294 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6944017b-dbab-3032-82f3-a203de133d47 | -16.90512 | -49.41063 | 2026-08-21 04:04:00 | NOAA-20 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4177a2f2-c241-3788-9a62-c571eed85140 | -22.51742 | -42.64103 | 2026-08-21 04:04:00 | NOAA-20 | CACHOEIRAS DE MACACU | RIO DE JANEIRO | Brasil | 3300803 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |


[Clique aqui para ver as próximas entradas](README31.md)
