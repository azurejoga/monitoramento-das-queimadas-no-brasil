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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6278d984-b834-3deb-9809-b99f652f9299 | -3.35891 | -48.40191 | 2025-09-21 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b210c256-235f-3e7b-ac26-f2c043ad7102 | -4.54817 | -50.87817 | 2025-09-21 04:34:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 385d3bda-bf21-3ea8-a04c-b6e7fcc4960d | -4.94621 | -49.9295 | 2025-09-21 04:34:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b652a2e-40b7-326f-9a81-c0862a58bfcc | -3.6235 | -47.52457 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62dd3e62-df98-3535-b29f-88a95e1ea9e7 | -3.59188 | -43.09529 | 2025-09-21 04:34:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2529491-8e86-3f62-8cbd-a5843cdfd725 | -0.91065 | -47.54478 | 2025-09-21 04:34:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4598d4b6-247a-319f-ab72-982d9ab8c49c | -6.01731 | -44.32557 | 2025-09-21 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c824aa8-ef0a-364f-ab4c-d11a7e440fdb | -5.35621 | -49.20935 | 2025-09-21 04:34:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0756b3a0-55c5-3ba5-979f-6d8f6de9b35c | -0.99385 | -47.06194 | 2025-09-21 04:34:00 | NPP-375D | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c186c016-3e55-3270-be89-4b5fc812a955 | -6.01499 | -44.32743 | 2025-09-21 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2537c26f-0aa8-30a9-a6e2-61fd52648609 | -5.42204 | -43.27243 | 2025-09-21 04:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03a391b7-f397-38fc-a146-089d83998b2b | -1.75356 | -47.17764 | 2025-09-21 04:34:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76e75e3e-b2ed-3f83-9c91-9aaeece04f3f | -5.45154 | -45.4987 | 2025-09-21 04:34:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99fefce9-523d-39b5-b5e7-6ab74074ade9 | -6.09012 | -41.00513 | 2025-09-21 04:34:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9c1080e7-aed0-386f-8fe6-52848baf9024 | -2.30561 | -48.39218 | 2025-09-21 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0902a062-5b5f-37bf-88eb-e75d02ed3422 | -3.59025 | -43.91622 | 2025-09-21 04:34:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aeaab0c3-c795-3e3f-81b5-1acc69c863ec | -4.29699 | -48.27354 | 2025-09-21 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29e125c9-d619-336c-9000-176c8f07b801 | -3.80819 | -47.57516 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62b6ad24-e7c4-36d9-989a-396caf5e48b0 | -2.30601 | -48.15012 | 2025-09-21 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fc9d9a6e-1f20-3ac0-8aa3-b3066922165c | -5.5262 | -43.87072 | 2025-09-21 04:34:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 28831c52-fcb4-3032-9a3f-3ffed4e74b83 | -5.42594 | -43.27297 | 2025-09-21 04:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 287cbd62-c461-3785-8567-63077d7fe239 | -3.59967 | -47.52438 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a5c16e5-eb27-3cda-b548-4328b9debe2c | -5.2646 | -48.90995 | 2025-09-21 04:34:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ec56eb8e-35e2-309c-97c9-f926827b4dfd | -2.74126 | -49.55428 | 2025-09-21 04:34:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80d3f336-604c-3f0f-b016-29250fa21b0e | -3.30212 | -52.5852 | 2025-09-21 04:34:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbf024c9-adfd-3953-927c-7f2af1ed3dd8 | -2.26373 | -47.84245 | 2025-09-21 04:34:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4bc9e17-5cf9-3b2d-9ff3-2d00ce879ad2 | -3.30555 | -48.71398 | 2025-09-21 04:34:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20751d16-4819-3752-83ed-0122f10e3320 | -2.16889 | -48.74787 | 2025-09-21 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f00fbeb-954a-3d88-89f2-12b1a99187fc | -3.81237 | -49.10371 | 2025-09-21 04:34:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f36aba4-93dc-3d10-b3db-c3da7abfe2c3 | -5.66553 | -45.35022 | 2025-09-21 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 421d0db5-d0f2-3b58-b217-32475f9870e6 | -3.59456 | -43.91251 | 2025-09-21 04:34:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80caddde-6f8f-348f-83e1-7cb98fff6bfb | -3.60021 | -47.52092 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 258e1255-9c98-3d5e-ae9d-3ceae1b058fb | -2.92131 | -48.30058 | 2025-09-21 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a2b78289-0952-30c3-9cff-9d3563783f9f | -3.68421 | -43.52097 | 2025-09-21 04:34:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 737f3541-02db-3693-9390-bc51878b2e5d | -5.26123 | -48.90941 | 2025-09-21 04:34:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 89be09a0-b65a-378b-9a0e-357b1115ae22 | -3.75523 | -54.81933 | 2025-09-21 04:34:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bfacd378-1795-37bf-b56a-ed715d0d898e | -4.19708 | -48.55513 | 2025-09-21 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e7bf0b1e-67a9-3ee8-92a7-2399b37fb040 | -5.34154 | -44.90262 | 2025-09-21 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b84e9a11-cb76-34e2-a7c9-25726f7c736d | -5.33798 | -44.9021 | 2025-09-21 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 415c4f9c-fcfd-30a1-9def-45236c875066 | -4.9106 | -43.0918 | 2025-09-21 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f09dcf8-2036-3bbb-871b-af198c3e04ce | -3.62628 | -47.52856 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c30ccc29-8ee2-3ebd-bd07-a58f1a64e110 | -3.84211 | -48.96132 | 2025-09-21 04:34:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d32c5b0e-613f-3401-99c3-3a9c8d8bb26f | -3.51517 | -47.20325 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0fcf100-eb5f-3fcd-b73d-ee1e920be7a0 | -2.92075 | -48.30413 | 2025-09-21 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e40ed3fb-1f2d-372a-b928-3413ddc34429 | -5.78083 | -45.35124 | 2025-09-21 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d5da2b7-2470-3d47-8f58-2ea98cc6030c | -4.68026 | -46.46461 | 2025-09-21 04:34:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4488fab8-996e-3683-bcc1-9687ed358690 | -5.52689 | -43.8662 | 2025-09-21 04:34:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 0e8b4370-6f7e-3596-ba0d-69f6e4122b23 | -5.68234 | -41.39285 | 2025-09-21 04:34:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5a470e48-e990-3178-880b-39145cdc5ac3 | -2.916 | -48.19434 | 2025-09-21 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6425bf76-efd2-399b-b019-8156af4ec53c | -3.79883 | -44.08719 | 2025-09-21 04:34:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9bcce6a-bd45-34d0-b3d2-12b300aa4ac8 | -4.22374 | -50.16324 | 2025-09-21 04:34:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e11513b4-c774-370e-bf4a-09fc481c46b1 | -4.65607 | -43.4861 | 2025-09-21 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9064bccf-3719-36ae-afde-9df7641b81ba | -5.25189 | -45.34526 | 2025-09-21 04:34:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cc93250-2761-301e-97af-7d34cf058372 | -2.83274 | -48.65555 | 2025-09-21 04:34:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50f82d59-8a50-31d1-a680-04dc25fed4b7 | -3.51463 | -47.20671 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2b2fa89-996e-3d0e-86f8-3ec9aedb780a | -2.40957 | -48.33073 | 2025-09-21 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eab5a59e-7bec-3563-a892-8204d871bef6 | -5.4223 | -43.27519 | 2025-09-21 04:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 275fb415-564c-3aa3-bdd1-52ea5d5726c6 | -2.61972 | -46.85386 | 2025-09-21 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5502bab9-a740-3840-8f28-15db41fd0508 | -3.8344 | -50.7751 | 2025-09-21 04:34:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ed51c55-04f2-378e-af7c-c507baece6b4 | -2.61857 | -46.83952 | 2025-09-21 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 522b84d3-60c9-354f-9245-0b687c4cbce5 | -6.08686 | -41.02804 | 2025-09-21 04:34:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0542415f-e2e2-3dea-8b65-1478ac822501 | -5.52384 | -43.86104 | 2025-09-21 04:34:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| dc7e5d44-99cd-3001-87b4-126256ec41d5 | -2.74189 | -49.55038 | 2025-09-21 04:34:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72e24802-45c4-3212-b107-c9b7cfdb8018 | -4.46506 | -44.13721 | 2025-09-21 04:34:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4d89392-d96a-353f-89ba-d9b601177c9e | -3.60354 | -47.52144 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 26bc7cf0-b549-3818-8b78-5d1b4c07749d | -3.51196 | -49.94062 | 2025-09-21 04:34:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7e99d7d-75e7-3263-a802-dcf26ad24955 | -1.79397 | -48.07327 | 2025-09-21 04:34:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 760e166e-35c5-3096-bd6b-aeb49973f0d9 | -5.2713 | -45.05392 | 2025-09-21 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5a9d637d-b79d-3eec-b52f-a09e5e488ed2 | -5.52995 | -43.87134 | 2025-09-21 04:34:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ce6a49c0-1ab3-31ab-8942-05b2f6b75eda | -0.95389 | -47.35806 | 2025-09-21 04:34:00 | NPP-375D | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d08dd8ca-b086-37d5-92b3-5e2a1aff614b | -5.34081 | -43.36342 | 2025-09-21 04:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d24a3bc7-fc5c-348a-9c9f-6f04fd1a29b2 | -2.93325 | -48.01977 | 2025-09-21 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4aa65e2-3a5a-38a1-ae8f-3c48c1f1692a | -3.36172 | -48.406 | 2025-09-21 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c5c6848-5034-3fb7-8952-3283b1154971 | -3.83108 | -51.19846 | 2025-09-21 04:34:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47b95c62-2cf8-3bb2-a067-678674949f89 | -3.608 | -47.53633 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 836ebcb9-0dda-37db-a34c-6cf1e7400f28 | -2.60836 | -48.13861 | 2025-09-21 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98e77204-5ff3-3a9c-9a80-3d732338bfd5 | -3.98536 | -51.05686 | 2025-09-21 04:34:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c38c38a-549b-3532-80b4-30beba9df9ea | -5.35281 | -49.2088 | 2025-09-21 04:34:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efebda16-b1e3-357c-8262-e701d3d0c9c5 | -3.35611 | -48.39782 | 2025-09-21 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bcf0c2be-eb59-3bfa-b3f3-7339b2d4ed4d | -3.64979 | -58.16514 | 2025-09-21 04:34:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| efb586ab-af75-3335-92a7-0e055168fad6 | -2.61639 | -46.85334 | 2025-09-21 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fd9a1615-be60-3a49-9861-f216f7d1e308 | -2.73774 | -49.55372 | 2025-09-21 04:34:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df3e53ae-846b-3f33-afc0-3b70720968cd | -3.8427 | -48.95767 | 2025-09-21 04:34:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03d18b0c-c624-314d-b83c-aa8221ed1552 | -3.32761 | -52.5427 | 2025-09-21 04:34:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f9555eb-8f40-318c-8fa0-15a731591507 | -2.93667 | -54.08521 | 2025-09-21 04:34:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8be486cd-5674-3dda-aac0-5900c0a53867 | -10.29047 | -46.08551 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a5843c2a-2e1b-3682-9a61-1e4a4129e1fa | -7.72472 | -44.46859 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1366e60f-3f64-3c66-a34d-abc20c3e12f0 | -12.06896 | -44.82966 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2be9faf-381c-3a74-abb9-4552dc7c6dd9 | -9.0135 | -44.96302 | 2025-09-21 04:36:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d18660fd-948b-34bb-9532-e4bc678f1277 | -10.23979 | -44.97726 | 2025-09-21 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e15e6561-f032-3172-bb66-8fc089806cbc | -7.92562 | -44.09854 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 69c0e029-8d61-3cd7-abe2-77ffaeb3acd4 | -12.07596 | -44.83582 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f08abad-ac40-3966-90b4-b61723852644 | -7.60675 | -45.48663 | 2025-09-21 04:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1970ae52-42fd-3b1a-a4ba-e1c7b63c2fd7 | -8.35492 | -44.70974 | 2025-09-21 04:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45187266-bfaa-3570-8fb5-b72e7eed06bf | -7.91902 | -44.11686 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa9e0c5a-b68a-3c6a-814a-8035549f88fc | -7.72994 | -44.43285 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fcbf49a-f645-3387-8d8d-0e0e3c462353 | -12.07942 | -44.81197 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89f58300-742f-3833-adf9-2044753e9a7c | -5.69318 | -51.7609 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a5bac5b0-2748-38c3-a1a2-2f5247a8cbbc | -10.03739 | -46.26391 | 2025-09-21 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0d69bd2-93ce-3d30-a916-24c6b7d8ce01 | -7.8267 | -45.6271 | 2025-09-21 04:36:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README23.md)
