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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abfa7071-7f96-3a7b-b531-a182f3d5982d | -16.11433 | -43.28558 | 2025-10-09 04:00:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dbd853a8-ec1c-36d9-83f7-0a5f85686816 | -11.24385 | -40.33967 | 2025-10-09 04:00:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| e0b3749c-2198-31a3-8764-e88c2e09735e | -13.8063 | -45.84095 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dacd67a9-5da1-3c13-9334-8497cdff74d4 | -11.7872 | -45.14551 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7601973-ed1c-3f15-8e8c-874d687ceb89 | -15.48978 | -46.86059 | 2025-10-09 04:00:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17707964-8d73-396e-8c85-3026c044dd15 | -15.07021 | -46.61961 | 2025-10-09 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0aa0a497-4d2b-387f-ae0c-10d7a069678f | -11.67068 | -43.89791 | 2025-10-09 04:00:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c501f5c6-2d05-3da7-97ba-e6cc44d80bdf | -15.489 | -46.86475 | 2025-10-09 04:00:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5d1720e-b6c9-3c5a-ad8b-67f34c29215d | -11.87852 | -45.50603 | 2025-10-09 04:00:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5c2b638-d8fd-30df-a99c-cca11b85fdf6 | -16.37656 | -46.38897 | 2025-10-09 04:00:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0f5cd260-d26d-3351-8019-3a0b32dc31c8 | -10.84959 | -49.9448 | 2025-10-09 04:00:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23223dcc-c418-3e3a-92ea-352066d26cd5 | -16.37799 | -46.38121 | 2025-10-09 04:00:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8d0c0a75-c33b-3f08-9f6b-250098fd5296 | -13.79305 | -45.84227 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0096640-b984-3f98-a26e-d1908c1a3b6f | -13.03264 | -43.90287 | 2025-10-09 04:00:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 42c14bbf-20bb-3a40-bf3a-1f9755d98182 | -15.44741 | -47.03666 | 2025-10-09 04:00:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8cecfd29-d545-3ebe-9e31-d22c88e5f5a6 | -15.80006 | -46.24683 | 2025-10-09 04:00:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72db6768-f6d4-3511-9cc3-3f5d7b524bae | -15.83866 | -41.84846 | 2025-10-09 04:00:00 | NPP-375D | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 77a3fad5-ab2c-37c2-b3b6-61dd8cd7cc55 | -14.41138 | -43.9885 | 2025-10-09 04:00:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f03c0093-60e6-399e-8167-9e1f11c649df | -14.42331 | -43.98601 | 2025-10-09 04:00:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 941152a9-2f3c-3967-a31f-d1dbd9ee1b8b | -15.91316 | -44.28541 | 2025-10-09 04:00:00 | NPP-375D | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cdac1ab2-b3bd-3c77-ae87-bc29ede427fc | -11.23993 | -40.34266 | 2025-10-09 04:00:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fe4b6057-295e-3c4a-b6b3-46005ffc4b4f | -12.77431 | -42.96183 | 2025-10-09 04:00:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f94560b2-97ae-31ab-abb9-704bb6582661 | -15.80017 | -41.4612 | 2025-10-09 04:00:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ec0487c3-b2a6-339b-ad8b-2291cb97437f | -13.82536 | -45.80803 | 2025-10-09 04:00:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98edd9b6-e6f0-39a9-b9c9-f99cd84673f4 | -15.78261 | -46.24798 | 2025-10-09 04:00:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f74969b6-4fea-3a87-87bc-27197e5bd701 | -12.00431 | -45.19044 | 2025-10-09 04:00:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88a2af80-876a-368c-8b22-6aadbe15d465 | -15.52261 | -41.85582 | 2025-10-09 04:00:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| f26abc81-5ad0-3f91-b40e-87051ae38fe1 | -14.4196 | -43.98533 | 2025-10-09 04:00:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ed438fda-b416-3557-a020-175fb9826008 | -15.39016 | -48.05219 | 2025-10-09 04:00:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3d8b990b-be95-3f5a-b273-b652ece9af92 | -13.82245 | -45.82381 | 2025-10-09 04:00:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4c2aed7b-8fde-3eee-b9aa-7887b6178e65 | -11.74708 | -45.14652 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00a4f431-bf67-3bf3-95e4-8238995b7901 | -14.84141 | -48.44124 | 2025-10-09 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 81c72025-6b43-37a3-bcc6-63535201a12b | -15.52321 | -41.85212 | 2025-10-09 04:00:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 11917efb-4cad-39dd-b3b5-4dfc8fa75bfd | -11.25054 | -40.34076 | 2025-10-09 04:00:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 39b86b9f-47d7-366c-85d6-7e19d6f0d1bc | -15.92132 | -43.29476 | 2025-10-09 04:00:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 639e3c66-c197-3d11-a8d2-04427fba28c6 | -14.79096 | -46.09659 | 2025-10-09 04:00:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef8291da-0567-3c0b-8ad3-790eef87a9c1 | -13.79994 | -45.82737 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67182488-a6a8-313a-8006-8c60c47ed86a | -11.72498 | -44.29886 | 2025-10-09 04:00:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6377e91c-f150-37d7-8237-8de2d099067d | -11.09527 | -48.55973 | 2025-10-09 04:00:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c5c68d4-3d87-3baf-b7d3-0c304d8947c5 | -16.29103 | -45.24269 | 2025-10-09 04:00:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 750bdfe9-7525-31d4-b3d6-b675821bcbd4 | -15.2183 | -46.38772 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d39f3a58-6d45-3a63-9528-d560c2300c43 | -13.7909 | -45.87814 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7af38148-9c24-3a29-87a7-0b66761f0036 | -13.79232 | -45.84616 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 334ef540-3eaa-3dd0-9dcb-069ddc9f7c20 | -14.53104 | -46.62861 | 2025-10-09 04:00:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 93b42c1d-a2e3-3716-a6cf-b0528ef6ed00 | -13.00219 | -44.05709 | 2025-10-09 04:00:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 765c36b5-680c-35ae-b3a5-60fcba9d36cd | -15.92485 | -43.29542 | 2025-10-09 04:00:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| edc59290-ef2e-33db-91be-086be5718696 | -14.38701 | -46.00551 | 2025-10-09 04:00:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b786b71-973c-31a1-a625-1c849a3f9023 | -11.87064 | -45.52574 | 2025-10-09 04:00:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ded75c47-edd3-3839-b949-0c5aa8a40af8 | -10.85871 | -44.63099 | 2025-10-09 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6135d799-14db-312b-821e-215a39e1aa16 | -10.52315 | -50.02347 | 2025-10-09 04:00:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8d92ad0d-b80e-30a6-afa2-d0fa319036cf | -11.99189 | -45.18811 | 2025-10-09 04:00:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e9733ac-16bb-3ac7-81ae-a150350cde80 | -11.66257 | -47.5344 | 2025-10-09 04:00:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 06eb6c91-3f65-30a4-be1f-e20ff00e41ee | -10.52733 | -50.03304 | 2025-10-09 04:00:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b85d3f96-2fac-330e-bea2-61259b04c58e | -14.51061 | -46.63987 | 2025-10-09 04:00:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 80b21b90-7836-30b7-abd4-4435352d3c25 | -10.65885 | -44.15364 | 2025-10-09 04:00:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72f640be-9105-3797-bb26-c5324c687fb3 | -11.77612 | -45.05301 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6488249f-e461-322b-ad51-c98a132fcec4 | -11.72458 | -45.34919 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4173c8b5-8a4c-36f9-ad49-9b3a41f5385d | -14.84069 | -48.368 | 2025-10-09 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8303876c-0a03-3751-9f93-7d4a7b2e2743 | -11.78651 | -45.1494 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| caad4df2-27c2-3b73-aa5a-7d8c37f3e575 | -13.32945 | -40.90132 | 2025-10-09 04:00:00 | NPP-375D | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d0636bb2-bfe4-3e8a-a496-73b50f86fd0b | -15.8073 | -43.78416 | 2025-10-09 04:00:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1ad78d0d-bae7-389c-b02f-664b74dd4cd1 | -11.23936 | -40.3462 | 2025-10-09 04:00:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1de8371a-7837-3dd4-9f73-10d9b83c0cf3 | -15.38278 | -48.03979 | 2025-10-09 04:00:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54ca0096-7882-368f-bbe8-7a23055ff153 | -11.88841 | -45.54918 | 2025-10-09 04:00:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 639a9fe5-7684-3843-bafc-e99146e08498 | -15.24324 | -46.37166 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9eb8cd14-a983-3b76-9caf-848a7455ee95 | -13.80558 | -45.84485 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ae01bfa-63c4-3d0a-b09e-9ee842b318ff | -13.80557 | -43.93266 | 2025-10-09 04:00:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee61a9b5-2020-3058-ad0f-f4700afab0ca | -11.98019 | -48.89392 | 2025-10-09 04:00:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46cec047-c707-3e00-b542-f1f3f5d5afe2 | -14.42566 | -43.97241 | 2025-10-09 04:00:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f22d4d66-043f-30fd-9871-522ed48fb394 | -10.86022 | -49.92146 | 2025-10-09 04:00:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba33686a-8b6d-3309-a8db-1f1e00912ea7 | -13.80011 | -45.82755 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1562e24f-72a7-39d2-be9a-83f8129a9338 | -11.23658 | -40.34213 | 2025-10-09 04:00:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 57b053f6-c951-34c7-837d-c2706760b3fb | -16.75363 | -43.9799 | 2025-10-09 04:00:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| e053df0c-8b54-34a4-89ee-e6842969c42f | -11.45589 | -43.4883 | 2025-10-09 04:00:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97f1481e-6983-3798-97c7-c0c93069ec65 | -11.79133 | -45.14637 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f32d7013-756b-3f8f-a1fa-53157b3da625 | -16.18633 | -43.66925 | 2025-10-09 04:00:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e83782c-01d4-325a-a58b-5d69b89f2aa1 | -11.24833 | -40.33311 | 2025-10-09 04:00:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 43679923-afd8-3b79-ad55-43f98a259c87 | -11.75408 | -45.13926 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71d50e22-7c98-3787-b2fe-981ef3b79b15 | -11.7879 | -45.14161 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57ba40f9-326f-3396-b184-52439a13f166 | -13.61366 | -44.44144 | 2025-10-09 04:00:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59192fed-f6a3-3da6-81a6-164fc285e2bd | -14.97139 | -46.29459 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8c54c82-79f9-34f3-9c44-c418492bef44 | -15.78681 | -46.24857 | 2025-10-09 04:00:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba2eb761-6b8a-3078-abbd-a09ebd13c1a0 | -11.75189 | -45.14348 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0fcbacc-99ec-304e-885d-1da6f9480e33 | -13.78741 | -45.84902 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25cc810f-662c-3466-a4f3-42cab46099a1 | -11.7918 | -45.04858 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14cbdce3-5cca-3bfa-ae8f-bc6941cfee0d | -15.83926 | -41.84475 | 2025-10-09 04:00:00 | NPP-375D | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4070c6e7-c0e5-311f-ba5a-04e667e4a1d3 | -16.74716 | -43.9743 | 2025-10-09 04:00:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 31.0 |
| ddc3032c-c71b-368b-a51e-d66619541371 | -13.79161 | -45.85003 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af399ce2-7faa-3ea5-9062-ec78057722ad | -11.24663 | -40.34374 | 2025-10-09 04:00:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 5eb1bf5b-5ea0-335c-93f5-9674f2a0b91a | -13.58971 | -48.67058 | 2025-10-09 04:00:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b34ecfe-e9ab-3ccc-8f37-785c892407ab | -15.32132 | -43.8507 | 2025-10-09 04:00:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d975216-7852-3ea1-8979-7b04a76439fe | -15.36814 | -47.10194 | 2025-10-09 04:00:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ddc5d774-0156-3a19-a535-d3c733074e90 | -11.31776 | -44.88342 | 2025-10-09 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d50e7833-fb21-3f60-8555-f04cb1dfea05 | -13.8239 | -45.81593 | 2025-10-09 04:00:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 86e17145-5107-3d0d-9b65-a27b1cd9044e | -14.9298 | -46.78927 | 2025-10-09 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ac5e1768-512d-34bf-ad1d-ef77189feae3 | -14.42194 | -43.97173 | 2025-10-09 04:00:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| b4b73297-fd89-36af-9d50-560453390140 | -15.47057 | -47.96943 | 2025-10-09 04:00:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 255c92c3-47df-3fae-9db5-2d15b662ce49 | -13.79994 | -45.85169 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e7b14e5-1815-302b-af97-5f3f3b87ed02 | -15.46886 | -47.95338 | 2025-10-09 04:00:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ce12e48-c0db-3ce4-ad35-7c6ee488b0ef | -14.79851 | -41.62663 | 2025-10-09 04:00:00 | NPP-375D | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |


[Clique aqui para ver as próximas entradas](README27.md)
