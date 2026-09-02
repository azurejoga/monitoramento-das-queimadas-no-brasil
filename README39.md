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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 482250c4-59b6-3aa6-a976-a95a122842b7 | -11.74889 | -50.54765 | 2026-09-02 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39361df9-2de2-32b7-b037-2f4628e0feb2 | -8.34278 | -50.79741 | 2026-09-02 04:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd473ca7-3265-32c3-abf9-17902f21baa2 | -6.69795 | -55.39929 | 2026-09-02 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f22b9a7f-e38f-3d28-b416-6574cb44b7f5 | -6.20103 | -53.48071 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e598bd78-ba19-3cbe-ad3c-217c119e7980 | -10.68309 | -54.04004 | 2026-09-02 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a96c2149-043b-3470-8f68-039c819dcfe9 | -9.40339 | -51.58025 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e931131-336b-37a0-b9f8-e63851fd5feb | -11.05887 | -51.52361 | 2026-09-02 04:57:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e68d59a-59d5-3f70-99f7-04257bcc351e | -8.76565 | -62.58818 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 557d487b-1b07-3653-944f-f18f843fef09 | -10.43806 | -46.72381 | 2026-09-02 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 743f7dca-06fb-33e7-a490-85468f052cff | -12.37369 | -48.15181 | 2026-09-02 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c862faa-3d68-399a-bd44-baa462f28b85 | -8.44755 | -54.73891 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 27ed3c2a-30a4-3dd4-b147-6723c1d25778 | -8.27467 | -54.94873 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f2ec622-a12c-3760-917e-95069b5a9f5b | -5.33337 | -60.15037 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aeb5101b-e835-39a6-bcf1-f6173997d253 | -8.25858 | -54.9549 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d631128-f7af-3b88-94fe-6f05b5b8f253 | -5.95215 | -57.68558 | 2026-09-02 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83a5aa14-7aa9-3e68-a8db-ce7bda7741b4 | -8.12397 | -54.95574 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 37a772f7-142f-3754-9f87-bdce2214f41b | -6.10452 | -57.86688 | 2026-09-02 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8cebf548-db97-3b04-914e-0c1423ef960b | -9.87893 | -64.97542 | 2026-09-02 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15f0acae-fac9-3e9b-a041-4ab3050d6fad | -8.75013 | -62.5722 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 756a8645-e5fd-3ec2-8167-fbbe3c6daf7c | -9.48231 | -60.46192 | 2026-09-02 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6480ca68-d966-3f9c-8ce6-f257732ec193 | -7.2595 | -61.1111 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6bd5e2ce-a7b5-3f16-82ce-41711031782d | -12.12822 | -47.09418 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8efb7c1b-8dd5-3870-9360-fc8f82e3ffc8 | -11.30129 | -45.16086 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bb1adbb1-8b44-3bdb-b58a-8eba34954030 | -5.97895 | -53.58156 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c112041-571d-347c-b81d-f22dcc6d3630 | -9.38937 | -60.56271 | 2026-09-02 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc78e239-c508-35df-9853-738f893c2306 | -12.14882 | -47.06674 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 083366c1-dc96-3675-b23f-a9acaf4f1ddf | -8.75312 | -62.57354 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eb853392-1ed2-3932-a7d1-346620aedeaf | -11.36473 | -45.41746 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1696283a-25a6-391f-8375-d8b447b4170e | -6.9445 | -56.45595 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bf4e0e2-e0a7-35b5-a49b-656c94730b47 | -8.45107 | -54.71795 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f105bf38-60d7-3f1c-a7f1-a6f050db020b | -10.32306 | -49.94477 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6952f70-edce-38be-8eae-a09b1eb5f23a | -8.9208 | -62.35587 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39ce03e2-1db4-3bb7-af78-2d9e36b656c5 | -7.20928 | -60.67003 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9ea9d9a-194c-387b-94a8-42e8593d95f2 | -9.47501 | -57.03033 | 2026-09-02 04:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5914d56a-0777-3b8e-8bd5-f09bdeac7106 | -6.86029 | -59.48212 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9e89d1b7-29b7-38fe-bf0a-06b1863708b1 | -7.06668 | -52.73083 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f645a6b-e7cf-3699-9095-67125f2eac22 | -10.88608 | -45.34632 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a3679202-53ed-3d14-b1e2-1bc8a63792f6 | -7.34414 | -60.5818 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd6e1a8a-9d00-371d-b205-c67ce2dbc0bd | -13.75369 | -43.83083 | 2026-09-02 04:57:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5760f6f-7396-3a6f-92e4-2d15ef151dc1 | -10.43858 | -46.72004 | 2026-09-02 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 55291ca2-1d16-3f07-b93e-1d11ad9c348a | -6.43384 | -53.55657 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9b5a19e-20bc-37a8-948d-b681b51f0dc8 | -8.44464 | -54.73411 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fa45b31a-fb12-3fb4-a584-33f66987db69 | -12.07081 | -47.1271 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d03ec5a7-180f-31fe-9e67-9fd649643c2b | -8.46052 | -54.72814 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a68b42d3-dee9-30c4-996d-9feb173092ca | -6.27282 | -55.97356 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 490d1acc-8cb3-3354-b994-44c689d510db | -8.43513 | -54.70234 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c58aa0cf-07de-3ef6-b720-930a4cfa1277 | -8.46914 | -54.72103 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b5563671-6eaa-3ca1-9aac-ab737ad6e555 | -6.76033 | -59.4398 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0eb950a4-c97e-322f-be4f-c5f873c85302 | -12.17717 | -47.07451 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9067850-2000-3cad-96da-737149feb3a2 | -10.89515 | -45.34775 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db9f4e3a-1726-3df5-8c60-a0762d0ad0b1 | -9.72254 | -47.77045 | 2026-09-02 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c7bfa38-0b7d-3a7f-9817-2adadc3448c1 | -10.8867 | -45.34179 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 954d973d-ae9f-355d-8795-39f92e078c35 | -8.90831 | -62.35776 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1c05e315-9b12-3c55-921a-ad40db08b356 | -11.35718 | -45.40387 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 607c33d5-0959-344c-8b3f-3717cca3f27f | -11.83873 | -46.03113 | 2026-09-02 04:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7c09533-a398-3ee6-9d7f-4030e6bbcb75 | -6.63908 | -51.87452 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d8e8dec-ecd6-3f30-aa16-c1b141b03c1a | -6.18337 | -57.7369 | 2026-09-02 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57d8d2bf-73a0-3800-b614-ec868dbeeeb6 | -6.4332 | -53.56053 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 722feb2c-867a-3153-af6d-9e7ba391ac61 | -11.67814 | -46.73336 | 2026-09-02 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd1b8fd5-60e3-3529-a561-f2cae115450c | -8.28331 | -54.91905 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbaf926a-852b-38cb-9abc-7b5f714621cf | -5.97607 | -53.57707 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f1ff075-849a-3019-bb63-e75383f6d2bf | -5.97415 | -53.58887 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cde68470-5b3e-39b8-8808-30781849968e | -7.52364 | -47.33137 | 2026-09-02 04:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1bfeda89-1a25-3e18-a83b-41ff3d33b9ed | -12.13799 | -47.14459 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2cf33414-6b1b-3830-a5dd-1e07f268f542 | -6.12248 | -53.54058 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b85d290-1cd7-3ca5-a973-1d8690f9d49c | -10.74707 | -54.03039 | 2026-09-02 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad68dc07-bf1b-3ba9-8e8d-dea0f5b8746b | -8.93251 | -62.35808 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c55ac0a6-c4c3-332d-bca6-cae746b33e8b | -12.08405 | -47.11055 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64b96627-b139-3114-a892-1f2c3f7b46c2 | -9.40008 | -51.60124 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56d5a257-5bdb-3f22-b43b-5e0041766464 | -9.0321 | -65.40475 | 2026-09-02 04:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 89d8cbc9-9202-3e66-a302-7a6765b0bd6b | -8.42791 | -54.70109 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 65bbb352-b544-3aa5-b8f1-ce4c986b0e41 | -12.87222 | -45.82763 | 2026-09-02 04:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fc84dbed-f1c7-3697-89db-2aaa3616992e | -6.94774 | -56.45612 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a013f7ff-4c8d-38d0-acaa-c3fd882b60a7 | -6.9492 | -56.45296 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d67cdd61-b120-3f83-9bd6-c0d4e9687ab5 | -7.73083 | -60.97657 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13a17001-e5f0-3831-8498-b7c64301e1e7 | -12.15295 | -47.06731 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2268f542-7e41-314c-94ed-2b675e4522cb | -11.296 | -45.1652 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 02d7f56b-3fa7-3483-a739-7675eb4d55a5 | -11.12607 | -51.5229 | 2026-09-02 04:57:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0022b79-4024-3166-b4dc-3185e05b68ce | -11.34316 | -50.58652 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9092da69-e1c3-3040-837e-b8f4355dbd41 | -6.85627 | -59.47543 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0a597f83-fcb0-3483-99ec-f1f10acfeada | -12.14518 | -47.12303 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 27053857-7e51-31db-87d9-6a8a65ff189c | -10.30176 | -49.99201 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb892eec-6197-36bf-ae56-5947d8476058 | -5.57551 | -60.19397 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 60962251-85d9-3688-9cf6-d01d1b94a14e | -6.76034 | -56.33556 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c57673c6-e99a-3320-bfb6-14c67b1e4c51 | -6.19014 | -55.27995 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a8c26a1-c737-3fe7-8038-f46658db03b8 | -8.75094 | -62.56784 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b82595a-4579-3714-bf74-fded3c86bbe3 | -7.57652 | -61.29788 | 2026-09-02 04:57:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de09c68c-24e0-34eb-847c-922dc5cac8f4 | -7.641 | -46.70694 | 2026-09-02 04:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4fecac2-3d89-373f-8f7d-a45cc025a948 | -7.76388 | -61.19471 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4ee7a7d-952c-375a-bc1e-10ad1d5dd476 | -11.47905 | -45.0887 | 2026-09-02 04:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 78bbf02b-2266-3546-ac57-06fdb3fd9a84 | -12.37152 | -48.1525 | 2026-09-02 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6aaf78d-fc75-382c-9807-92ffdbebb5cd | -8.47487 | -54.70897 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d9c8b92-66c5-3bc6-b6a7-78fea17e09be | -7.36246 | -60.60312 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fba8dd3-b91c-3a20-b3cd-31b66291c16a | -10.70461 | -46.19888 | 2026-09-02 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 259d1c89-2990-3bd9-bea0-3afea6874eb6 | -12.37897 | -48.14267 | 2026-09-02 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85f09488-87ac-3e2f-a3f7-457639746ed9 | -12.12924 | -47.08674 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc879700-37c1-3de8-af5e-9d17b64962d6 | -10.39157 | -49.99739 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4c141e1-b5c6-34fe-837c-c140fe1fd3c4 | -8.1166 | -54.95468 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e6f2c7f9-4028-3b63-a836-e0fc8f38987c | -10.8964 | -45.3386 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3f75b351-e0ef-3254-bf9b-f41a517c681f | -10.91068 | -45.33593 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |


[Clique aqui para ver as próximas entradas](README40.md)
