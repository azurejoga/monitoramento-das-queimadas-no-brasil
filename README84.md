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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c66d67e-29f1-3118-9cdc-95dadd56c2cf | -7.82095 | -46.99062 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d7d82c1-ca3f-3722-b977-8ed58068e86f | -12.76161 | -46.86963 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94df33f5-ca0e-31c3-820e-0f910bc8c7de | -13.39874 | -47.54467 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 926ad74e-c899-35bc-b724-ae17c0d54c69 | -10.95579 | -46.49561 | 2025-09-30 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c4f91c17-411a-3231-bb73-109460c7a8fb | -10.40501 | -48.16887 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24cc9789-ee0e-3cfb-a82d-2ff59fba5886 | -10.40674 | -48.17214 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dda1affd-7a07-376c-9314-3fffaa1f4335 | -13.60497 | -47.28264 | 2025-09-30 05:08:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ec48315-51c1-3ebc-8185-8994ed1c86bd | -10.06815 | -50.21599 | 2025-09-30 05:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 96d5d6a4-4c88-32f6-9c8f-4bc46c50b8ae | -11.67423 | -44.29477 | 2025-09-30 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f1af253-f7f7-3e93-b777-7561a9d323c9 | -9.03975 | -46.69721 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 174091be-4903-39f8-990e-e11adfeb9256 | -7.37183 | -47.05131 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fcb10d9-dd05-3fb8-821b-b76993712449 | -10.20258 | -44.89902 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9cb2fb4-3a94-382d-aa6f-676f1e1f8c18 | -7.91498 | -44.61577 | 2025-09-30 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f983c0b4-fdd8-3f30-864c-a13441eff50c | -8.44399 | -46.93732 | 2025-09-30 05:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d145daba-efab-3212-a434-63c486bdf234 | -13.21806 | -47.32901 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3ce0e9d4-02fe-3a03-87d9-fa1d064ff48d | -9.41532 | -54.71925 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bed9dc9-77a2-361e-8424-d94aa24cc72f | -9.23871 | -48.56246 | 2025-09-30 05:08:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8288ccbb-1218-3881-9d65-a9baca618b86 | -10.18538 | -44.90335 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 50c615fe-32ed-33fa-b795-fcf1a49f0121 | -10.63006 | -53.69309 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e9a40b8a-09f4-3e9c-88c7-10db359b513d | -13.38881 | -48.0595 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0738109e-0e3b-30d2-875b-0a1c74dbd403 | -13.38728 | -48.07259 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 547b4d52-fbf3-36e2-91d1-71a133969cf8 | -8.32355 | -50.87936 | 2025-09-30 05:08:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbc7ace1-b8e6-3860-b4a3-e328cef03588 | -12.84225 | -46.87967 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a89a6e4c-7264-37bd-96d5-7056fb51dbbe | -11.16175 | -54.11728 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 8e77a7dc-ce81-334b-8b50-53133294a3a4 | -11.91835 | -51.54601 | 2025-09-30 05:08:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32222f95-5d58-305a-a64f-4e3bb0b8f980 | -10.30282 | -54.13538 | 2025-09-30 05:08:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf0d5f68-643e-3f67-8e08-b81f80695247 | -7.66636 | -47.42287 | 2025-09-30 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c65b308b-ef49-3067-a58f-09cf3c92aac6 | -11.90982 | -48.0588 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a91e6998-acbd-3095-b345-8e2db0de6e12 | -12.84946 | -47.01583 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b8f646c4-7d2d-34a3-990d-cf0962e0e993 | -5.85227 | -50.07034 | 2025-09-30 05:08:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0aeb0026-19bc-373a-b5dc-9008c5c02e59 | -8.54166 | -44.66408 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c284a35e-fc71-3a46-b247-cf1b58f351b6 | -11.1647 | -54.12187 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 4be4c24b-d7ee-34d4-b5ce-e1817ae3a068 | -12.97 | -48.41866 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64fe59b1-88cb-383b-bf0a-1bbd31ce2e47 | -12.89156 | -46.76252 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a202b7fd-f797-35a3-9d82-9deafa8fdecc | -7.01969 | -45.22503 | 2025-09-30 05:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a59ec70a-e286-3c2d-b40b-187739b42d80 | -10.03735 | -50.19152 | 2025-09-30 05:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ff168b6-05c6-370d-8464-dd02677bf489 | -7.91684 | -44.61996 | 2025-09-30 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c522017c-5a53-3a8c-b0f1-0adc4ee25490 | -11.88827 | -48.05907 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 286d84ac-b7cc-3df2-80f8-a4c81598f081 | -8.00848 | -47.05632 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8315e225-6cc4-328c-8f11-769e55f55d79 | -10.51147 | -54.35028 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 590ae2c0-b709-3b45-bc8a-f9dab8927055 | -10.40194 | -48.16875 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22ad03c7-af28-3dc9-98c9-138f575db44e | -9.40162 | -54.71713 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55bd1cc3-577e-31d3-8c84-86cc01252cb4 | -8.17079 | -55.16999 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a37cdacf-7cad-39b0-b3b5-d858c3665fba | -10.19489 | -52.55909 | 2025-09-30 05:08:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b857d5c-ba4f-37e2-b4b4-2bbe9722c7c5 | -11.20224 | -47.2152 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17f748c8-9517-3db6-98e8-ebf19775b666 | -5.24001 | -56.0872 | 2025-09-30 05:08:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c062a3d9-91a9-3d60-9494-3dafd72c779e | -7.85274 | -46.75335 | 2025-09-30 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91a7273e-bf6a-3609-840e-f07199670286 | -11.14923 | -54.12788 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| e4b713b5-5081-32d5-a541-fc3101c239c1 | -12.87252 | -45.17933 | 2025-09-30 05:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b110770a-ac95-3cf2-90f1-4dffbf18a75f | -13.39074 | -48.07048 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f268f381-d9f4-30c9-a56d-ee7c884d1075 | -13.59952 | -43.46556 | 2025-09-30 05:08:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 186f2192-4df5-33c6-b871-a802d06a1354 | -7.29869 | -47.30273 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f73be63f-79f4-344b-9564-13189a758f8e | -11.13111 | -48.35682 | 2025-09-30 05:08:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d135a616-418b-3931-8cb8-cd76083b7f9e | -13.21896 | -47.32143 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1432871a-6f46-39fc-8018-fd36c2af9cb7 | -10.19172 | -44.90415 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 99e0f75f-95e8-34c6-a640-5712609c5e58 | -12.96073 | -46.40924 | 2025-09-30 05:08:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ba12895-cd0a-3836-93c8-5ae9b7fad583 | -7.52012 | -46.68608 | 2025-09-30 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df1aecd1-aa16-3bd5-8386-571a71f4c600 | -10.95215 | -46.47813 | 2025-09-30 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 281e5e0c-8e6f-381c-a1ec-13a5b6abc555 | -11.02484 | -49.82038 | 2025-09-30 05:08:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19e21ce4-c6be-33ad-b82f-67838645f967 | -10.10999 | -47.78962 | 2025-09-30 05:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 283e335e-8b98-364a-bd4c-e63345696250 | -7.19822 | -48.59639 | 2025-09-30 05:08:00 | NPP-375D | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c3a167a-8ad0-3e6b-9848-0ce9b2a918ce | -7.51971 | -45.44246 | 2025-09-30 05:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4f79bb0b-7c4b-3c2f-be50-f61c97f4da85 | -10.99888 | -57.05438 | 2025-09-30 05:08:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3200139d-5867-3d90-a082-18be9a42a67a | -9.06016 | -46.71433 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e5e1467-77f2-3ed9-984c-4893aaf8efd0 | -11.20723 | -47.74043 | 2025-09-30 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aaaa3561-806f-35e8-b807-65a6010c5141 | -8.32019 | -50.91715 | 2025-09-30 05:08:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1b98bdb-312b-309c-8084-323b333f4bd7 | -12.83984 | -46.99874 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 51facb42-4db0-30dc-95b3-1aeee261301a | -11.42577 | -44.9092 | 2025-09-30 05:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a617aba1-d7fb-3b6c-8432-db26f671e4c1 | -11.41536 | -55.06508 | 2025-09-30 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee118dae-8316-30b2-aba5-f1e1f926d6fe | -5.85707 | -50.0671 | 2025-09-30 05:08:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88f56793-56a1-30fd-9fa3-e444a3e557f7 | -8.43768 | -46.94329 | 2025-09-30 05:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d40c1f05-15bc-335d-9406-993065100d00 | -9.37552 | -47.58531 | 2025-09-30 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d69dacff-7eee-3944-a516-dad9719854c8 | -10.03881 | -50.19836 | 2025-09-30 05:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a4036831-6ceb-360f-8a87-6da01355f4c3 | -9.40674 | -54.7065 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd16fc5a-970c-3932-ba1d-634cfe359e14 | -9.39819 | -54.71661 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af5765ef-c950-3690-8a4d-88c178b87f42 | -9.44565 | -50.89985 | 2025-09-30 05:08:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a9f6ca12-307f-3e75-a6e5-fa54d0100925 | -13.39693 | -48.06482 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 116ffcab-9cd8-364f-8d38-8aa97013b9fa | -10.18785 | -44.88258 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 12030dd9-adda-3960-b363-a4558d8bc6b1 | -7.80162 | -48.02989 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d3019e9-d371-3a96-b41d-0382ba997529 | -7.47446 | -47.26699 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17b96a01-9188-3a33-8178-9ab6ed9cb601 | -10.3944 | -47.8082 | 2025-09-30 05:08:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62cb6452-a249-3d74-89f7-0f1809c85a1a | -8.87987 | -46.64264 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fffe23f5-b5f0-34d4-8346-18335be9458a | -8.15443 | -46.38235 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f0415dd1-75f6-3d35-905e-8a9ca7820f6b | -10.62259 | -48.549 | 2025-09-30 05:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a03aaa12-61b3-33c3-8ed2-f6862e557bec | -9.39932 | -54.70918 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e1ae6c9-cce2-36f6-967d-f7e7aad7ec15 | -9.51028 | -47.69195 | 2025-09-30 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 892c5422-5470-379f-9c9b-e204e82024f1 | -10.99832 | -57.0579 | 2025-09-30 05:08:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f7226e3-4cde-30dd-add1-2afff92fa34d | -11.20361 | -47.74541 | 2025-09-30 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40e463aa-8185-3b7e-a239-c49e46f43687 | -6.36736 | -45.64309 | 2025-09-30 05:08:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3b82102c-421a-3dd8-977c-80424d38a4b4 | -11.20568 | -47.75231 | 2025-09-30 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 34bb8560-c7f7-3254-8623-d076c20f82be | -12.8342 | -46.99715 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40061acc-2fe4-3c34-a3f6-54325608decd | -11.15696 | -54.12489 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 37.2 |
| e24eda71-3ae1-3834-b3cf-4c4ce41377e4 | -12.88104 | -44.6906 | 2025-09-30 05:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e00dd6e-8d11-3c9d-9b90-b2d3fad1f6db | -10.31039 | -54.15688 | 2025-09-30 05:08:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1070791f-6047-3fc9-938a-6c4604d8af71 | -10.7624 | -45.37664 | 2025-09-30 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 24120535-cf95-3ae6-b3a7-177385715488 | -8.14334 | -46.37978 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0b2c0aaf-a199-3aff-9853-cb8b39b1856e | -8.32096 | -50.88333 | 2025-09-30 05:08:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ebd6461-dd78-34f6-8f34-a4062a46c6e7 | -11.87894 | -48.04791 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 61afae44-c559-357c-b0d6-f6fc3561e351 | -10.6379 | -53.69005 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ac30cfe-5f45-3e5c-bb10-1b7a464ba6a1 | -13.24253 | -48.44528 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README85.md)
