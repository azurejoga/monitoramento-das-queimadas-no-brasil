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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b05846af-9995-3913-aa4c-d5d6447456ac | -11.85425 | -46.87075 | 2026-09-20 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6fd9ac70-b840-36fc-be46-fcf47f31bd44 | -7.68329 | -44.66402 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 68d44ccb-1fc4-3de5-ba1c-242c56950bca | -10.87914 | -54.08585 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 332af897-998b-3660-b4aa-b8dd319e238d | -8.44597 | -45.86703 | 2026-09-20 04:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f5c1bbf-c295-36c2-a275-68f4c89ac5f6 | -9.12421 | -45.73241 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0dc06f44-a574-358d-bc53-79d8d0d832cf | -9.02352 | -48.74578 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 289d5d0b-5243-3f15-8028-6f041a551c1b | -11.09862 | -54.02797 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 23.9 |
| d4ed4d40-6f78-3ba2-8f39-5aab8e51fef2 | -5.86234 | -51.93719 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e0f09fcd-f523-3b5b-a1d2-a3b428ec7eb6 | -11.98715 | -52.47868 | 2026-09-20 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 967ea290-a44b-32e4-bec0-3fae260003d3 | -6.34298 | -58.30621 | 2026-09-20 04:40:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51f1fcfb-9cd1-32ef-9d5f-fe7130f9b651 | -8.60477 | -54.61165 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23dbb3a1-4e77-39f7-a6b2-bc8c3f8ec2e1 | -11.38811 | -51.38162 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee3d1979-6fb5-3d64-b85b-53e24717aa43 | -13.23918 | -46.95629 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b56f3f20-0d7f-3eef-9752-e878e106de27 | -6.00264 | -52.33415 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88aa420c-6203-3d77-9f9f-149e881d0793 | -7.53195 | -45.43737 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 74c3fbc0-bbd6-3555-a6da-206dbeda1557 | -10.66455 | -48.69847 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9851c194-3ab0-36f5-9c86-1d71d6dccae5 | -5.84426 | -53.53003 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b4a0cb4f-639f-34b9-bc0b-2ecc9d109ed7 | -5.85391 | -53.5238 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bdbd5c01-5c78-352c-9442-fb7804cbfb0f | -13.02454 | -46.91838 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a7e308b-5de9-35ea-9023-fbcfddc86e9b | -8.37126 | -47.19247 | 2026-09-20 04:40:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 655b1ca3-0757-35db-8dd2-e2258135e483 | -8.45107 | -47.65667 | 2026-09-20 04:40:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b27ffbf0-2589-37d3-8f86-e22f5a002a71 | -8.17952 | -54.76569 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 014323b1-7d84-3d2d-8bd9-ea57db5d3ed9 | -11.72501 | -54.55406 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 835b8487-3c1b-37bb-9252-6064cd5d86dc | -13.02809 | -46.91872 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0aa5768e-939c-3b8a-b436-770499e8fa78 | -11.87548 | -49.00853 | 2026-09-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2b31799-488c-3aa6-bf21-e73d951c95dd | -11.3252 | -44.17952 | 2026-09-20 04:40:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b68e3f3f-09ba-3a43-99d5-ca539c8b4ffc | -9.72785 | -47.21113 | 2026-09-20 04:40:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 273c6694-0f0b-36d7-9194-35677a037148 | -9.56821 | -45.46501 | 2026-09-20 04:40:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82042f44-4266-3cca-a097-a96e629c60e2 | -13.32027 | -51.78864 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd79a964-0cce-3085-9e16-18fe30a95578 | -7.55267 | -45.44475 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 05e5b68a-b214-36c4-88fc-3a520d0ef32f | -10.77715 | -46.31858 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 702c622e-1367-31c1-ab34-83bcc8267870 | -11.8702 | -47.66646 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d05514bb-e41c-3b29-ae90-5d91e7c85b3b | -5.85626 | -52.07029 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 415e59df-b851-33ea-b6b5-680b810caf47 | -9.82603 | -46.44743 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba82dc6d-6987-3e07-8d49-bcb6b8c2372b | -5.84156 | -53.51469 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4deec042-a2e5-36cf-9c6d-04901ca9e405 | -10.87758 | -56.22702 | 2026-09-20 04:40:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e1c49043-3261-39dd-af7d-27318668add3 | -9.12372 | -45.71148 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f462786a-c7c1-3036-8555-de81f56ff41b | -10.87759 | -54.07121 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68e4e7c1-2e1a-3923-917b-0680716996a0 | -6.49621 | -58.38173 | 2026-09-20 04:40:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d28bbf4-6f48-38f0-bcb8-b692dda23631 | -11.23229 | -54.14293 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07cec056-d2b1-3ab1-a62b-d8d0212aefd5 | -10.90531 | -53.98351 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0ea8ad3-dbea-330a-a51b-a554173ca179 | -11.36843 | -47.33201 | 2026-09-20 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb65c621-0012-3a24-8205-93c0427e8bc5 | -11.04715 | -54.17887 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9142dade-3bea-3a05-942e-29020a6baea4 | -7.49852 | -46.13243 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 95c5e48f-d7cc-32da-be04-d7901bfda34e | -9.29946 | -62.3205 | 2026-09-20 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ffcc067b-5ccd-346d-8237-17749ee5051a | -11.48287 | -47.75366 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75a7b8bb-40a0-3dd8-bc6c-052ee3e1f92a | -5.84713 | -53.53833 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5f960b98-deba-3306-9666-9e7f28604b9b | -11.03458 | -48.30997 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0b777e3-e636-3a7e-89aa-901f81edefba | -11.44779 | -45.32343 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca206c4c-e527-33cc-9ec6-0587ae66a0a6 | -11.44713 | -45.32796 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2393ace6-022a-3b3b-a6b9-d14b032c81f9 | -11.13616 | -54.02394 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1464f6d2-ceb5-3461-9d4b-3dbfde558404 | -11.88266 | -49.00608 | 2026-09-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f6bb9c7-9a54-3d6c-9741-fc28475b0467 | -11.84787 | -46.86565 | 2026-09-20 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25869e21-6933-3779-a556-8e8936a8a173 | -7.75431 | -49.20436 | 2026-09-20 04:40:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a620836-2939-3512-a16a-71321d8e39d9 | -12.31462 | -50.71961 | 2026-09-20 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c2821d5-4979-3852-abfd-74a23a5c7d91 | -8.23823 | -61.37389 | 2026-09-20 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 66117084-a2fd-372d-920a-ed6fe5ce885e | -7.52083 | -46.67308 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c2fe296-413a-3bda-bfed-751146356500 | -9.80432 | -48.31674 | 2026-09-20 04:40:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3453046e-0e04-3e1f-a17b-bd4367671b65 | -11.21494 | -54.07765 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e4ac36eb-69f8-3a16-9bfb-c81db2635966 | -11.23482 | -54.0812 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f3af741-745d-391b-9c93-ab4f220a1f03 | -10.98176 | -49.69593 | 2026-09-20 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05aa5209-cde6-38c8-86cf-163a4bb1c107 | -6.79486 | -47.82486 | 2026-09-20 04:40:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 753ed9e6-1a6d-3f8c-8260-3633bba297db | -8.17446 | -54.74302 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a0b5ddc5-b75c-3297-a2f2-adc62dcacf8b | -11.20913 | -54.08739 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f03084c7-540b-32e3-8b1f-d7c023a1224e | -9.03898 | -48.77676 | 2026-09-20 04:40:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e849f3d-7786-39b6-b321-2b05a5069fc6 | -7.44363 | -44.74001 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c25bd3f3-5a2b-327b-8d03-3692511e6487 | -9.24391 | -46.18326 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8779ba32-86d8-3fb5-9b21-244e287cc243 | -13.28563 | -51.32425 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f403b0ca-b715-345b-8f5b-01903b474121 | -7.42694 | -44.75066 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4ea6662-e4e9-3b2c-8c32-71633033e337 | -11.72031 | -54.55697 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aef9a4d7-b612-34ad-af56-10a4958f2e66 | -12.65643 | -49.48249 | 2026-09-20 04:40:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4aeb100e-5848-3fde-8d21-6b8d5843adb2 | -13.3889 | -49.44629 | 2026-09-20 04:40:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31143546-1f84-3102-b4c5-2cd4bb11ea35 | -12.7569 | -46.21806 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 14622358-544d-341a-9bed-6c4616faed17 | -11.21096 | -54.07697 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9b1c1385-3561-36f7-8eb1-ee2783596bfc | -5.87236 | -52.04321 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4d99ae5-cacd-3c11-b75a-4b145a810249 | -11.20195 | -55.03637 | 2026-09-20 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4613bb06-e6b8-322e-97ae-6b2c1e3db06b | -9.54751 | -46.58416 | 2026-09-20 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3691a8a-d1b8-3097-9112-107c71025221 | -11.83918 | -46.82809 | 2026-09-20 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70f25a77-18f7-3be6-8f8b-e2e4706f731d | -8.50301 | -47.43266 | 2026-09-20 04:40:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90662bb1-3c17-3798-842b-764314f9e56d | -12.26669 | -49.17639 | 2026-09-20 04:40:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27c5ee28-989f-3cd7-b2e7-f28fcc644a2f | -5.84779 | -53.53452 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 317f66ca-66f1-3d20-a589-7833a8bd7b52 | -9.56758 | -45.46928 | 2026-09-20 04:40:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd054316-2062-3e5d-9db4-1c7413bee1ec | -8.61049 | -54.60429 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3367ccf-723d-3193-85ff-524b9c54a6dc | -11.85834 | -46.86728 | 2026-09-20 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14000f14-667e-3790-96cd-ad05803cf649 | -11.34381 | -43.38822 | 2026-09-20 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e86a8f1-a80e-3712-8e76-a7144e7f475b | -7.01371 | -45.25599 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 3651dc8d-cb3d-36f5-9326-accc43091833 | -9.26253 | -46.20226 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 86862a1e-4e62-328c-9d9d-e38a27d4d70b | -10.32025 | -50.21212 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8600f7ae-03a4-3e08-a21f-e34fcdf742b5 | -10.54833 | -46.73887 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2232f11c-8696-3901-a5b0-104b2dca85f1 | -12.75028 | -46.21267 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 454e84ed-f178-39a3-b6a0-655fdf47980c | -7.43664 | -44.76115 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2612f558-3fb2-3279-b498-56020234e1fd | -11.21936 | -48.36483 | 2026-09-20 04:40:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4df811d3-f7b3-3494-9194-4e6bb640bc49 | -9.7737 | -46.07249 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d29680c4-8701-3d63-a516-9921565d5672 | -10.31118 | -50.22543 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a0a35f16-25d3-3d58-aa67-d2f6c9c4460f | -12.75639 | -46.12086 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69e069c5-86a1-3879-ab20-c06d34ecf09d | -9.25456 | -45.92007 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53f91a24-153c-343d-932f-c6788cd9f51a | -7.5403 | -45.43036 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 9f9a4061-f885-3dc7-be74-90cc3fc9b4c5 | -7.55205 | -45.44881 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c599864-0566-33c9-9f3b-30532f5db326 | -11.04693 | -47.67539 | 2026-09-20 04:40:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7edbbd1-91c5-3d42-97b1-001be7f3a03c | -10.86683 | -57.14888 | 2026-09-20 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README67.md)
