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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 881c2051-cd14-3f8a-8d54-a02957e4e03e | -17.11124 | -48.99557 | 2025-09-08 03:42:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8695a3ce-a712-3cb0-8337-72b8fd6b9705 | -16.91117 | -45.84755 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1493427f-dd5e-3d0c-836b-34ff3414f973 | -18.95364 | -46.80032 | 2025-09-08 03:42:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1d00d79-c965-3828-9958-655b0e521d23 | -22.06821 | -45.20121 | 2025-09-08 03:42:00 | NPP-375D | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 63b1c502-477d-3c09-b1d5-2ca3c61b2095 | -20.46726 | -43.96646 | 2025-09-08 03:42:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e22f13db-29db-3a7a-9b6e-80907a08cfdc | -17.16459 | -44.44916 | 2025-09-08 03:42:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff2523c7-46a4-394c-89a3-e4cfa687b9bc | -18.02788 | -47.11769 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9790202b-4948-357d-892a-04555de031ce | -16.89971 | -45.79159 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06b5fce0-eaa8-3712-970b-f47c8c05574c | -19.95525 | -46.19559 | 2025-09-08 03:42:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 31f63dd3-0023-3221-a734-c09e80b08adb | -17.25216 | -46.69769 | 2025-09-08 03:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b4a686dc-5bf2-3b4b-ab62-658466cc4145 | -17.70991 | -44.48093 | 2025-09-08 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 538ac72e-e633-3958-bca0-e52427dcf2f6 | -20.92379 | -45.26842 | 2025-09-08 03:42:00 | NPP-375D | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f800871d-c868-3900-a0c5-a193883f94cb | -17.25873 | -46.69472 | 2025-09-08 03:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 193e6fe9-dc4b-3797-a0b1-b6eb33ea273b | -19.39938 | -44.50777 | 2025-09-08 03:42:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a85a13f-bff3-34f0-bf6f-3a2e80ce8727 | -19.36976 | -44.507 | 2025-09-08 03:42:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34e009ce-a25f-3d4c-a4fe-a855df46cd8b | -19.92723 | -46.17599 | 2025-09-08 03:42:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b4c4f55-2fdd-3c65-88cd-d9a21f61c0ec | -18.24419 | -46.62479 | 2025-09-08 03:42:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45c7025a-0d7a-39dc-af9f-b117c79d34cc | -16.51922 | -45.10489 | 2025-09-08 03:42:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48ca9dc0-3168-3c30-9571-cf7d31ef784a | -18.24516 | -46.63128 | 2025-09-08 03:42:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 05f254c9-b1c0-3f30-bbbf-7586d277b77b | -18.36142 | -43.92504 | 2025-09-08 03:42:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5cf37e30-440a-395d-9a39-b6c048d2dbb8 | -18.02971 | -47.10793 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f195d493-0405-3520-a020-6288197e0a1f | -18.02864 | -47.11421 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 532e09d6-8af7-3b60-a8e5-10964978034e | -19.52469 | -47.8856 | 2025-09-08 03:42:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 744cdd6d-4bd8-3b5c-a264-e4797c15c55d | -15.96249 | -48.11094 | 2025-09-08 03:42:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6db0b93-b661-3389-9340-fd2be980a83c | -16.52238 | -45.11595 | 2025-09-08 03:42:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97534b0b-3669-3a16-93ba-4ae8dc270a11 | -17.59026 | -44.54056 | 2025-09-08 03:42:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bafe8f83-3d7f-31c3-9044-6a5984d32b47 | -17.26265 | -46.70433 | 2025-09-08 03:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b031d2de-3271-3b35-96cb-774c2f4882ef | -19.69988 | -49.28215 | 2025-09-08 03:42:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c54d5fb-7ac2-3537-965d-114924ed0412 | -19.39348 | -44.51239 | 2025-09-08 03:42:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 430e4b29-16dc-3724-a4c6-94ddeb963147 | -17.71474 | -44.48233 | 2025-09-08 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d034bfc-59dd-358c-8c2e-459b1fad4bc1 | -17.6434 | -44.78452 | 2025-09-08 03:42:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 377fc712-0831-37bc-92f9-be5f9091a106 | -17.25859 | -46.70197 | 2025-09-08 03:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8d6a95cb-d5a6-357e-bb00-ff6b72104734 | -16.9143 | -45.80584 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 014c4b89-0ce6-379d-9509-316c14fd2374 | -18.35115 | -43.92777 | 2025-09-08 03:42:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 137e1c5b-ef65-3b10-ab1e-0c18690aaeb5 | -16.91064 | -45.82107 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b56fdbb-3a2c-33f4-a5fd-750755e97af1 | -17.25786 | -46.69887 | 2025-09-08 03:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 854e8a3e-d5d4-3ce9-9b05-56656a655bf6 | -16.90764 | -45.8358 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db0cd6c1-90f1-359d-a04c-9c1cd38bd295 | -16.90053 | -45.79076 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29f89c04-ee28-3c0b-930c-7da1eb841513 | -17.1658 | -44.44305 | 2025-09-08 03:42:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce582547-aab8-36ef-bb3d-b147e855ed01 | -16.91202 | -45.81665 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50b306cf-1bd1-34da-825f-b248f9681c47 | -18.03902 | -47.09246 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7f5de2b-a056-3ce5-a72a-abda464b0f2a | -20.36861 | -43.91502 | 2025-09-08 03:42:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 19b767a5-c4b3-3d1c-a9e9-eab48bfa52e4 | -16.55109 | -45.10863 | 2025-09-08 03:42:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3d0630c-bc56-327b-8075-0950ca0683b2 | -17.66436 | -44.18913 | 2025-09-08 03:42:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a808a20f-36d1-3736-940b-b82616def4d8 | -19.63541 | -46.57906 | 2025-09-08 03:42:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 767c7e95-b091-3bea-9075-d8d002d5f4b3 | -19.922 | -46.17483 | 2025-09-08 03:42:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61986d7b-4003-37c7-a713-817fbacf6703 | -17.66324 | -44.18446 | 2025-09-08 03:42:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9fec68e3-6a58-3656-bded-627cb9ea6021 | -18.02702 | -47.12156 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 35bbacb1-e620-3926-b840-07b7c4029cc6 | -19.95553 | -46.19744 | 2025-09-08 03:42:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17330391-5184-31f7-9d44-3caaf79b7032 | -17.44596 | -50.2244 | 2025-09-08 03:42:00 | NPP-375D | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf053bcf-d4c8-32f1-9b26-fad24bdf7f85 | -17.96672 | -46.89748 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 46767fd3-43bb-3445-90fc-712e66d12a8c | -21.746 | -46.56068 | 2025-09-08 03:42:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0eddb09e-01ec-32f9-a925-5d6ec25f1570 | -19.95487 | -46.20058 | 2025-09-08 03:42:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70388f20-04c2-33d3-aa6b-6169d47d0637 | -17.16573 | -44.44366 | 2025-09-08 03:42:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c7081a2e-bb06-32da-afa2-9f6cc1a08c58 | -16.54589 | -45.10746 | 2025-09-08 03:42:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a6a8296-877f-3fa1-8d81-de0ec39fc569 | -19.02988 | -43.56923 | 2025-09-08 03:42:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c46e8bdc-53a5-382d-9037-c8341e322200 | -18.43408 | -48.78839 | 2025-09-08 03:42:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 586b63d9-b7ea-3c11-b810-1bf5600ce56b | -17.15734 | -44.4338 | 2025-09-08 03:42:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c00cf4a1-7967-3533-b332-15282e837aae | -17.15611 | -44.44001 | 2025-09-08 03:42:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a88418f3-3f31-3fda-9991-c76574b3416b | -17.69673 | -43.53782 | 2025-09-08 03:42:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e61247d-b30e-3edf-b16c-3e68bad9086c | -18.42778 | -48.78705 | 2025-09-08 03:42:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 18d5df4e-dd08-3a5b-96c5-1d122c66c375 | -17.66219 | -44.18959 | 2025-09-08 03:42:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4c53556d-e916-3018-8123-78c14d5d3fc1 | -19.87363 | -46.15008 | 2025-09-08 03:42:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfe7a8e6-3f9f-3401-96ce-6811b56214a7 | -16.938 | -45.77369 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c79b5719-95d3-3c6b-b109-7da5e01115cb | -17.39743 | -49.31074 | 2025-09-08 03:42:00 | NPP-375D | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7821758-6387-3c76-b4b9-649667d673b2 | -18.95498 | -46.80108 | 2025-09-08 03:42:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| abf66d8d-5504-3f25-b475-27cebe4b3d8b | -18.14746 | -43.40049 | 2025-09-08 03:42:00 | NPP-375D | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1930c384-ce48-335d-9018-3dfb48d2615a | -16.90021 | -45.76157 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f78adc0-d0ab-3c6e-8665-bf5cfafae3a6 | -16.91128 | -45.82016 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 723fa6c0-dd8c-3180-8350-b48f730917bb | -16.91136 | -45.81753 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e1c7ed2-ff34-30cc-920d-0c4c1f05d434 | -16.54456 | -45.11398 | 2025-09-08 03:42:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2a2face-0ba4-348f-a17d-6b9305643038 | -18.14334 | -43.39587 | 2025-09-08 03:42:00 | NPP-375D | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9dece4d3-a5cc-3294-8b86-3b6d4aa2cf26 | -19.92795 | -46.1726 | 2025-09-08 03:42:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1763cd25-6ee4-3ff6-a312-bdb9e3d52904 | -16.90898 | -45.83104 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7925982a-c751-3408-803f-d831c9e8758c | -17.54023 | -43.74341 | 2025-09-08 03:42:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d7203024-ce5a-3a93-a8ad-c437da281e51 | -16.29302 | -49.56026 | 2025-09-08 03:42:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 249eb5ae-fffe-33ee-8c1e-cc6d375d08f6 | -20.53578 | -46.47965 | 2025-09-08 03:42:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 881c3877-16ee-3a1d-9573-bd43bb9de528 | -19.19492 | -42.06448 | 2025-09-08 03:42:00 | NPP-375D | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1322a36a-b0d3-399e-a94e-620f2f68a497 | -20.92563 | -45.26951 | 2025-09-08 03:42:00 | NPP-375D | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| f98a260f-402c-3114-93a7-82d5fd3a3c7d | -19.50653 | -42.57011 | 2025-09-08 03:42:00 | NPP-375D | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d7cfe32e-a790-338a-8003-423bc02b0e21 | -16.63807 | -49.15015 | 2025-09-08 03:42:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43e49ac3-6244-35f7-8600-c970fc97188a | -18.04036 | -47.08838 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 915b42f4-38e7-3ccb-af7b-2e5306e6b0f7 | -17.71098 | -44.48254 | 2025-09-08 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 10cf7091-1612-3d45-87f6-95852f3f7b95 | -17.43911 | -50.22247 | 2025-09-08 03:42:00 | NPP-375D | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e5fc8a05-d7a8-31f9-b98f-91344fd42ecc | -16.52306 | -45.11267 | 2025-09-08 03:42:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aedbd98d-a04b-3f5b-b448-d57699629bd5 | -17.16095 | -44.44154 | 2025-09-08 03:42:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c3d0063-f5df-3266-99e5-9fc2ee65e693 | -16.9082 | -45.83478 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e790abb-2b98-3565-b9eb-30ba0b911e4d | -16.29387 | -49.55814 | 2025-09-08 03:42:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea144de2-7e44-370b-931c-4cb2028f785c | -16.90917 | -45.82832 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3db0a5d7-17aa-306f-8b57-f2e7b5704bed | -19.63487 | -42.03668 | 2025-09-08 03:42:00 | NPP-375D | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0ee4dfc4-2af3-3ce3-8e40-280d515c50a1 | -19.95458 | -46.19867 | 2025-09-08 03:42:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f7d8d1f-f9a2-33f8-a0d6-6f51b79ed190 | -17.25771 | -46.70606 | 2025-09-08 03:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0044e1df-f296-3dd0-be0e-e2f6a285c72b | -15.9613 | -48.11009 | 2025-09-08 03:42:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8673ff4f-a748-34f7-b02b-7140b6ef1a3a | -17.96753 | -46.89366 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5fb8fec7-50f4-3df5-b5ae-488386618cb9 | -20.37314 | -43.91574 | 2025-09-08 03:42:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ae2c53f5-e3b3-3fec-a348-cfe0df017f71 | -17.16503 | -49.02337 | 2025-09-08 03:42:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3e56590-abaa-3f09-99e6-316e7f9bbae1 | -18.10942 | -44.49834 | 2025-09-08 03:42:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19924a2c-c402-3d5f-a532-8f9040fb0667 | -18.95439 | -46.79693 | 2025-09-08 03:42:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0b73878-8a7c-3cc9-b697-822bf5fd3509 | -16.54339 | -45.09315 | 2025-09-08 03:42:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b7e7fd7-9813-3cde-9795-44fb0dfae008 | -21.21623 | -44.02586 | 2025-09-08 03:42:00 | NPP-375D | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |


[Clique aqui para ver as próximas entradas](README28.md)
