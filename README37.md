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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3aaf89b3-c551-3801-befd-4f392d24e94a | -8.58641 | -54.78321 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74089510-a061-3eec-8d24-53977b8c857f | -7.22773 | -51.68401 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 925dcf4d-1c95-3d76-9428-f31f0532d4be | -6.84108 | -59.45341 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8142908e-f174-3f18-a353-2db8f9034877 | -6.10107 | -57.69722 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e2f9fb7-93cb-392f-9d6a-a9ae0d5de909 | -8.03481 | -51.79427 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1fd9a34-0149-39e1-9d05-382f8c246d88 | -9.10184 | -60.92273 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dda35dc5-de53-3267-a318-de25d8557d3f | -6.94051 | -59.31346 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 711c1d5b-632b-3889-ac82-04fb54e13fe8 | -9.05849 | -60.43348 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a9a2736-82c3-3870-a232-e55ca43c2a98 | -9.19726 | -60.88307 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2596c639-be83-348d-8e91-782b83a4a6a1 | -6.78541 | -58.63461 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1d9a469-e52e-3fb4-b0a0-7336a178d18b | -11.16453 | -54.01137 | 2026-08-22 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a4762b3-0774-31f5-b9e0-331d2edfe3a3 | -6.14014 | -59.89503 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2e8e190-d3a7-3eff-9d37-424eaa7df099 | -9.05283 | -50.88305 | 2026-08-22 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a8d920c-0d4c-3f43-8732-0f2285b12b41 | -12.78979 | -48.45993 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9418f45f-b8de-327f-8a79-d940dda90aef | -8.61617 | -54.72828 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88ef1a0f-609d-3a8f-961a-9681aaa52519 | -12.27568 | -43.17228 | 2026-08-22 05:04:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 19b9302f-f45d-39e5-9519-1d38ac3e2333 | -6.96202 | -59.05754 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d6828c0c-c889-39e7-9de0-c5688bbadc6a | -6.81954 | -59.41737 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cf3934b8-2175-3770-8d2a-7978cd1020b2 | -6.78833 | -58.64333 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 429743a1-4439-3e73-a10a-7a571497289d | -9.16797 | -57.01482 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6626aff0-83f5-362b-93e7-b2d21bb61e4b | -9.52088 | -51.63482 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3785f085-795c-3730-9ffb-7c4bc51e6d55 | -7.4904 | -43.81526 | 2026-08-22 05:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a06876f0-8d8d-3a61-8865-ed96fe8339ab | -9.16872 | -57.01038 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee1ada9d-be28-3638-8dd6-16d4f1920de1 | -10.79782 | -50.98589 | 2026-08-22 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35395266-8017-3e15-8e63-ad7029992dd2 | -10.28022 | -50.38901 | 2026-08-22 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e040f2a8-03d3-3b3b-9a71-52f8f71951ae | -11.43507 | -44.55808 | 2026-08-22 05:04:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6976bb3c-dd98-37ec-8717-48b04227e30f | -6.86724 | -59.03423 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cf269617-3618-391f-8f31-18df539c89a8 | -8.08973 | -50.03316 | 2026-08-22 05:04:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b07051a-c5ea-38e3-9b8e-465379d03e71 | -9.41185 | -60.40712 | 2026-08-22 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57829456-0ee5-314f-ac48-c380bc3ff424 | -6.02501 | -57.68063 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f65b6c2a-06d2-3cd9-b888-ac01f63baa42 | -6.85758 | -59.4378 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8c5e021-53c9-3b82-8679-d10ded8e0fe7 | -11.10628 | -49.89128 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fc54504-3ec3-398b-a5a9-c03523e7e79d | -6.13228 | -57.68449 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| acbbebb2-5648-3593-90d4-7e789e4668f7 | -5.99942 | -57.80807 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb3f944f-5f73-37bc-9345-f098b19a3d45 | -12.77779 | -48.39043 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 43417fd2-9d97-312d-a61a-3a432e78853c | -8.39511 | -62.68946 | 2026-08-22 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 27.5 |
| c258e6d4-1b5a-3b59-8787-14e777ec19ae | -6.00122 | -57.79739 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e8208c6-3fad-3413-9c47-a9bc1c8db7ec | -6.3847 | -54.95632 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1be762ef-5a84-3aa6-a19e-e6f9c79f42ef | -6.77637 | -55.69847 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d8c3766-dcd9-3370-b685-ae5c1ccb34a7 | -6.85475 | -59.46253 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6d06cdf9-8c88-3043-ac1a-0dedf7081e5c | -6.43282 | -54.95571 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03d56a13-f995-31fe-bd78-da72e5650254 | -9.04932 | -50.88255 | 2026-08-22 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 996607e7-33e7-3580-84b8-63b894761e6d | -11.16117 | -54.03246 | 2026-08-22 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f787f430-0456-3b41-b07a-4e9cf620eb6c | -6.76861 | -58.65661 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9381b6bf-2781-3360-b059-1aca4cd7ea99 | -8.51949 | -55.32628 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7bf3725-108b-3166-bb49-1631348032cb | -6.13285 | -59.90899 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b83f02d-1d28-369e-afed-07187e53ac98 | -9.2079 | -60.76823 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d4aafd2e-0a83-36ce-8d66-e29914e93445 | -6.85563 | -59.02345 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26d3e7d4-f718-3e98-8734-0603761f974d | -6.724 | -48.11094 | 2026-08-22 05:04:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 015995fc-69d2-308d-83f0-fba936a86958 | -7.01665 | -59.55347 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd6eabaf-f6ce-3bd7-b88f-91fe87890c05 | -6.22615 | -55.42377 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fa2f6f1-efb9-30c3-b4c1-f84a89ca0224 | -8.59423 | -54.71344 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac5300e5-7ad1-3fb7-b6be-5a2730b8a7eb | -10.79488 | -50.9813 | 2026-08-22 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 70128612-01d0-39db-b552-9295496cf84c | -7.51646 | -47.64198 | 2026-08-22 05:04:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 091787fb-8675-32b3-9e53-aa3cccb8671f | -6.93984 | -52.78167 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82b2ebfa-9463-3221-a855-4623b4060b54 | -6.12003 | -59.91917 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 897b834c-5457-3e85-b2f3-01919ab293bd | -10.04152 | -59.45875 | 2026-08-22 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa81c103-a569-3a71-b597-819ee0cf8923 | -9.17318 | -57.00651 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aaaf25c5-b133-311b-8450-50157c251c23 | -6.78006 | -58.66671 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 12bfb0cf-c186-3f06-b348-7c3b751528ca | -9.43998 | -51.61863 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76fc0061-d8c0-3497-b212-735b62ef5aaf | -8.53395 | -54.82718 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 79dd8d27-01eb-37cd-88bf-f350fd7715cc | -9.16575 | -57.00535 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff03642f-4f4e-3407-9257-44c4d145f197 | -6.54462 | -58.52225 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f070116-d202-3472-ae86-8cfbafaec04a | -6.79188 | -59.41722 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| a9f958fe-03bd-361b-bbb0-db8c036b6ab3 | -8.09217 | -51.66962 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63947115-b247-3e14-8235-0acac7e12315 | -9.40554 | -60.41576 | 2026-08-22 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f18c5f9c-832a-3bc2-8fab-a9cf2c799799 | -8.54075 | -54.8283 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d4b899a1-faa4-3476-a29d-943727247689 | -6.43289 | -52.75828 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e3bbb4d-7212-3d26-8ce2-a1f2123f78ac | -6.79127 | -58.64248 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a8b3bfa6-63b8-3d38-8739-174976dc4f8a | -6.76728 | -58.66449 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b267ebfa-35cc-39d7-b453-d0c42109c5eb | -9.43768 | -51.63344 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d2a887f2-a2ae-306b-922d-fbb54f5a2969 | -8.1074 | -51.66089 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c4f9e65-1517-3291-b213-400cb389de22 | -8.03085 | -54.02625 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 258fdec6-cb0f-30b2-93c1-10a37ef95b94 | -8.45883 | -51.55315 | 2026-08-22 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27a294aa-4194-3ef6-995f-f0a39e784b65 | -8.5317 | -55.3166 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c04a2c96-fb76-3b37-9345-59213a0d18bc | -8.62692 | -54.72627 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 351a5173-3d30-31c4-b312-39bcd6feed01 | -11.16229 | -54.02542 | 2026-08-22 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9a88e6a2-1bc5-3036-825d-c7d889fcbafd | -8.53963 | -55.32508 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4adc19c2-18bb-37c3-97bb-e52a7696790c | -8.88976 | -60.54312 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 911ab191-fbc3-312f-b07c-f456ec6152f2 | -6.77302 | -58.69687 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ada9e39-a4be-30b5-b697-fd4eb7cceacd | -6.06595 | -57.70928 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f77a24df-a495-38af-ac7c-da53250ff852 | -6.6691 | -56.34596 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 731e3866-9e8f-304b-a889-e6079146bd68 | -6.76462 | -58.6804 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a67ff787-cfc7-31b5-b358-fcb4758d75ba | -12.76762 | -48.40164 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a4164fec-bfec-3a2d-822c-e1d3cb2694bd | -7.60708 | -60.94482 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98d3f489-3dbe-3620-9b90-cbf400dbe111 | -6.79827 | -58.62732 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29bc0232-a442-325c-b4e2-90e565740286 | -6.13198 | -59.91393 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b51e8bb0-9c20-30de-806c-8f833c71db6a | -5.80235 | -57.54596 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6203eb36-2ea5-3124-840e-36875912575a | -6.81288 | -59.40249 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14b5d066-9ec3-3364-8bb8-ba81ac1ef296 | -5.80176 | -57.54946 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c74b1962-317f-3600-bfa6-59f00898790d | -6.48948 | -51.60283 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14d1ed45-f9a2-31a5-84ac-fc851fab3e2f | -6.87102 | -59.44017 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fd4dc2c-678b-3563-887f-ffd2253ba2db | -10.51643 | -50.82202 | 2026-08-22 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57addcda-35a4-3698-bca9-8041656184a2 | -6.81744 | -59.67536 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 6db47669-4435-3952-99d7-a3857321abe5 | -6.60595 | -58.38913 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d69f697-5330-3be8-ba9b-0c0c6cced1cd | -6.43821 | -56.18204 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ced1164-efee-3db7-8dd3-45e153d9a0d6 | -6.77372 | -58.69287 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2cd8eee4-b409-3cf3-ac7f-2d47fc888883 | -8.99125 | -50.74075 | 2026-08-22 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c620f809-d33c-3eba-a982-b7b72d00ac6c | -6.7874 | -59.41645 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 7961d101-50d9-33a1-b507-de087b7109df | -9.16198 | -59.46194 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |


[Clique aqui para ver as próximas entradas](README38.md)
