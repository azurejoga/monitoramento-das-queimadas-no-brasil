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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 440f8f46-a1eb-3623-84dc-cd52bafd8880 | -9.93995 | -53.99065 | 2026-09-16 00:22:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 01fd4140-644f-3c9d-b184-a3d57ec86dea | -6.27418 | -55.28942 | 2026-09-16 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2079435a-8846-348a-bdec-c0d90c56f0d2 | -10.4511 | -50.98829 | 2026-09-16 00:22:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 390d5f6e-ab14-3019-b0f9-0e4d7dead095 | -9.60224 | -49.33406 | 2026-09-16 00:22:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 681744e9-1110-37f5-ba05-9bb060b73908 | -5.97132 | -55.35878 | 2026-09-16 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6820fce0-92ee-3bf9-b7b5-fdde5af85dc1 | -6.0014 | -47.38675 | 2026-09-16 00:22:00 | TERRA_M-M | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 2c3991c0-7649-39cf-a5b4-bbbb532c7436 | -9.37478 | -58.00091 | 2026-09-16 00:22:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ecf6d5f2-a55d-3f39-952b-3a7942fcbe85 | -9.85985 | -49.82692 | 2026-09-16 00:22:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a82016eb-1d01-33e9-89a2-7beaece78833 | -9.70639 | -52.00755 | 2026-09-16 00:22:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d913ce5d-d7e4-3697-81e9-6844c511e878 | -6.36616 | -55.83059 | 2026-09-16 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 813fd59d-63f7-3df1-a3d9-2cb9445f2964 | -10.6898 | -52.50351 | 2026-09-16 00:22:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fa21852c-47cd-3b07-9049-bd5128731f8e | -5.76797 | -45.10016 | 2026-09-16 00:22:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 2cc64f19-9c42-3711-ad92-0cfd0872f88c | -10.6005 | -47.76681 | 2026-09-16 00:22:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 94d87156-3140-3fe1-9d2d-ba0eb76f5a9d | -9.14365 | -51.57228 | 2026-09-16 00:22:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e9aa1b56-ad81-3770-98bb-692cb8781b57 | -11.49818 | -45.85713 | 2026-09-16 00:22:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 40b5f203-beec-39b9-9267-d4f2823187e3 | -5.81637 | -49.8728 | 2026-09-16 00:22:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| fb3cfff6-e099-3513-b878-97e27b8548e7 | -6.2258 | -55.60937 | 2026-09-16 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a3c23eed-81d8-37d1-97ef-0d436bed2adf | -9.70781 | -52.01745 | 2026-09-16 00:22:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 908fa5d5-0530-3ef8-9c87-32614104959a | -11.51242 | -45.85448 | 2026-09-16 00:22:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| e3e91300-8a64-3fd0-91f2-8402214919cc | -10.45339 | -44.94096 | 2026-09-16 00:22:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 46.0 |
| e5709c39-036b-33f9-ab5e-3ef27b5f14de | -6.72486 | -48.1092 | 2026-09-16 00:22:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 9406168a-6b73-30a8-b682-bb524fe786be | -8.7865 | -50.55013 | 2026-09-16 00:22:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 9b175d29-12d1-36ff-bfb7-4f4446d539f3 | -10.69401 | -54.17812 | 2026-09-16 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| c32b84cf-c358-313e-93d3-5456a3df7046 | -9.2601 | -48.53175 | 2026-09-16 00:22:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 31c5d9cd-9cb2-3d01-9886-04cb4e468de0 | -6.32496 | -55.24897 | 2026-09-16 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cc73740a-a6c3-32a6-85f5-3e096c41da12 | -10.40813 | -48.6532 | 2026-09-16 00:22:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| a2257d53-69b7-3a9f-86f6-a55279b3cc62 | -9.39731 | -60.29897 | 2026-09-16 00:22:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 58d09b24-00fe-3ae9-82f5-501669ed46cb | -9.08843 | -45.72472 | 2026-09-16 00:22:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 076e3b02-07b0-3d07-ac38-116a32715809 | -9.42688 | -49.54562 | 2026-09-16 00:22:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b2e82dd4-7e76-3459-91a8-e41bb2cc36bd | -11.41879 | -51.42609 | 2026-09-16 00:22:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d48918d4-d2e6-3c4d-aa23-216d116e7f9f | -6.78333 | -48.66473 | 2026-09-16 00:22:00 | TERRA_M-M | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 8ea0a0dd-fe6f-3b6c-a14d-8c6ac14dad96 | -6.00503 | -47.41104 | 2026-09-16 00:22:00 | TERRA_M-M | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 3da53d5e-3926-37d0-9b9a-e9b108f59649 | -11.20195 | -54.12911 | 2026-09-16 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ab9cb7b6-6fb7-37f2-abe7-1f8e90cb4556 | -10.87764 | -50.82196 | 2026-09-16 00:22:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f4ce0eb8-6961-3619-8e01-d35b83c43bfe | -6.26537 | -55.29063 | 2026-09-16 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 3c4195a7-beaf-3e48-9a40-4175e622e70c | -11.20073 | -54.12018 | 2026-09-16 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a4888550-05b2-3a53-973b-43dc5a7d8007 | -6.85772 | -55.31552 | 2026-09-16 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7bd470c6-3a10-3b0a-8597-5c312d48e9ec | -10.88363 | -54.02054 | 2026-09-16 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 210459b0-b8af-3018-aa37-a71fc39ff45d | -8.5396 | -44.48103 | 2026-09-16 00:22:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 85c480fb-a4cb-34a3-b29c-3b8db6da2df8 | -6.31495 | -55.24138 | 2026-09-16 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5303159c-4ac7-3301-9413-99be9d4bf05f | -10.68033 | -54.14374 | 2026-09-16 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 29206391-8013-3f87-ba2b-75911fd5592c | -8.33718 | -51.32066 | 2026-09-16 00:22:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| efb64653-c15b-3cfa-83e1-d5067520c043 | -9.8726 | -49.83882 | 2026-09-16 00:22:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 74204431-6f98-3cbd-af2e-dde2053f59a9 | -6.32617 | -55.25779 | 2026-09-16 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c04f5f6a-c8d8-371a-b8e5-1f98526824ed | -10.89547 | -51.50077 | 2026-09-16 00:22:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 0451ce4a-6a42-3b1f-8781-21214a4a48c4 | -5.63449 | -51.67771 | 2026-09-16 00:22:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d0894659-dcc1-300a-b3c5-274de70abd86 | -11.98421 | -52.46321 | 2026-09-16 00:22:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 130746f8-289f-36f6-82d1-4dc26a4e889e | -10.47722 | -50.96127 | 2026-09-16 00:22:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 13faee94-f738-33f3-8638-c7ee9e5d9c95 | -6.1113 | -46.11119 | 2026-09-16 00:22:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 0f65a3fb-5743-337f-a02d-e86268589a52 | -9.40974 | -62.70075 | 2026-09-16 00:22:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 6ec9b18d-682e-381a-9d6f-5dac3969a1b2 | -5.13729 | -47.60394 | 2026-09-16 00:22:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 6cf1ef58-d905-3316-b810-fa1b83db805c | -11.71759 | -47.60089 | 2026-09-16 00:22:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 7cb0bb9f-43c6-3314-a3d4-c005861688b8 | -7.50261 | -50.15601 | 2026-09-16 00:22:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 72caeb12-607f-3312-bbb8-ebba8a1eceb1 | -8.33759 | -51.31442 | 2026-09-16 00:22:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 35a695c1-19d6-30ec-8b5d-0813277e01ef | -9.41313 | -62.72997 | 2026-09-16 00:22:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 42.8 |
| acc7cdac-8f0b-3756-9ba0-3b98f08df6f1 | -6.61403 | -51.44181 | 2026-09-16 00:22:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 90174516-a2d0-3ff1-acea-efa13dfc1195 | -9.79552 | -46.5059 | 2026-09-16 00:22:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 129.0 |
| ef7eda23-d5fe-3cc0-9dc6-ce0da7ac373c | -6.70268 | -56.88265 | 2026-09-16 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 32cbbe57-ccc9-3297-a509-764ca9b01c9f | -6.16918 | -53.27042 | 2026-09-16 00:22:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 797744a8-39ab-39c8-bce2-7acde7c3ed75 | -11.71951 | -47.59487 | 2026-09-16 00:22:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 71bc1c44-f6dc-3958-9326-f1b6a10e6f32 | -6.00587 | -47.38031 | 2026-09-16 00:22:00 | TERRA_M-M | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| b428c342-9292-3908-895d-db41f03c3805 | -6.31615 | -55.25021 | 2026-09-16 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| ec0bb5db-7c8b-37dc-ba0d-b22135b7ee83 | -7.58255 | -49.68419 | 2026-09-16 00:22:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b208aec6-23d7-380e-8768-9e6ad86906df | -9.78595 | -46.50101 | 2026-09-16 00:22:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| e0375bc0-f0f9-36dd-92c2-6d1489be64d1 | -6.66057 | -50.91818 | 2026-09-16 00:22:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ea30e5d1-001b-3f19-b706-939c3af7be7d | -8.54563 | -44.51611 | 2026-09-16 00:22:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 8b4d9ce6-990d-3d10-867b-f093af3d29e8 | -12.11925 | -57.20083 | 2026-09-16 00:22:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 3622f4d3-b9e8-3e09-ba57-8a6b47b3df03 | -10.46901 | -44.93839 | 2026-09-16 00:22:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 36.9 |
| e14a0940-406a-3cf8-8e2f-9d2c53145254 | -8.33556 | -51.30934 | 2026-09-16 00:22:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| f4363761-be05-37a0-9c7a-187bcabf2c5c | -6.27297 | -55.28058 | 2026-09-16 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 5a0da3e5-7adb-3dc2-9612-b4c8bc1bc1c6 | -9.22653 | -60.29483 | 2026-09-16 00:22:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.9 |
| ba97ded0-f12b-3961-9e83-2004bb670ff5 | -8.89326 | -50.77419 | 2026-09-16 00:22:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a453daf4-17ab-310c-9812-22f0b6239102 | -10.66179 | -58.76204 | 2026-09-16 00:22:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 30.7 |
| c8082faa-2ebc-3377-bdbe-5bc731cdb2de | -9.38488 | -60.30051 | 2026-09-16 00:22:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 6d2d829a-b731-3467-bc9d-74729b7313f4 | -6.86532 | -55.30535 | 2026-09-16 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1f173dc3-027c-3199-8491-665f85d3d0eb | -11.72257 | -47.61334 | 2026-09-16 00:22:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| f405447a-d0c6-3f80-9a27-661dcb8bbff4 | -5.10933 | -47.60849 | 2026-09-16 00:22:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 80.5 |
| fbc43e66-b8b0-3d77-9cb5-111d8f8b16f3 | -6.09721 | -53.54447 | 2026-09-16 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 43304848-eea9-31e1-b75c-c97dd464758f | -8.02016 | -54.84097 | 2026-09-16 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4dd137d2-85b7-3e5a-b80b-01bec9d24bf6 | -4.52623 | -50.73399 | 2026-09-16 00:22:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3d07aa93-8bf9-38e5-86a0-ea4a1bb01d0b | -6.26658 | -55.29947 | 2026-09-16 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 094594e1-dcc2-3b88-b7a3-a1f5b2481fe9 | -10.36624 | -45.13168 | 2026-09-16 00:22:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 0185de65-ee3b-3c16-92c0-a75e949a25f1 | -6.34312 | -49.4025 | 2026-09-16 00:22:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 27f3a3eb-2a11-3fda-b534-bffa094d815f | -9.79999 | -46.49882 | 2026-09-16 00:22:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 60ee8891-dc01-3ef5-a03d-5b9ec3c47c8a | -11.26749 | -54.13202 | 2026-09-16 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a6bc652b-4b66-31f4-aaab-6cd4197c553c | -5.12332 | -47.6063 | 2026-09-16 00:22:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 110.0 |
| ecb9a40a-c98e-3192-b6bb-480a84394f4a | -8.79687 | -50.54859 | 2026-09-16 00:22:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 5aebe166-56da-3294-acd4-5262282bbd10 | -10.43963 | -50.97857 | 2026-09-16 00:22:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 403f051e-da30-34a8-91bd-d5a475a7cf20 | -6.63056 | -55.1341 | 2026-09-16 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7ecde494-3365-3eec-b680-c6de13999161 | -2.70291 | -57.61895 | 2026-09-16 00:24:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 3447e008-e532-3e80-969f-b6b72a0790c7 | -1.28022 | -55.71479 | 2026-09-16 00:24:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 0a226936-12e5-3678-96dd-7c3cee02b87f | -5.12947 | -55.94425 | 2026-09-16 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6752af06-bf18-3c46-b129-015a86fe2c09 | -1.29021 | -55.72231 | 2026-09-16 00:24:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 742bd335-6315-3e6b-bf26-e73896692022 | -3.21143 | -53.94163 | 2026-09-16 00:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 05bdc1f2-77f1-383c-9e6d-ea48c2f3a8ee | -4.37609 | -55.02397 | 2026-09-16 00:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 487c7852-afae-3f33-843a-7d8a149202cc | -4.57202 | -54.91263 | 2026-09-16 00:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 036f0362-37e3-3922-b2f8-24860b837abc | -3.38103 | -50.84409 | 2026-09-16 00:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 0b53eb5c-d925-30ee-b27e-3d4932049746 | -0.92986 | -47.19946 | 2026-09-16 00:24:00 | TERRA_M-M | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| fb3bf7ac-f0c9-3aa2-8816-004e26ea2009 | -1.28142 | -55.72354 | 2026-09-16 00:24:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| df5fb9ae-99fe-3f9d-b859-900119b59ec9 | -3.43597 | -57.98656 | 2026-09-16 00:24:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README5.md)
