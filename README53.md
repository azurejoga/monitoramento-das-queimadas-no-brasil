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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3263cf8-503b-36c6-9ed4-6853575c4b50 | -14.02767 | -44.95707 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82225739-e9ec-3618-87bf-263cc093eba7 | -8.71332 | -47.98591 | 2025-10-03 04:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7908d66d-6a04-3164-b307-e7e6b325c695 | -9.07268 | -46.65508 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a6fba68a-4cba-37c6-8422-52fe9c266496 | -11.49233 | -45.00584 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 247304cd-5f3d-3b5e-93bc-480946f610da | -13.18976 | -47.82377 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a918070d-8226-37d2-ab2b-76d92ea235f4 | -12.63381 | -46.97961 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a0379d0b-233e-383e-811b-7cf665e25700 | -11.90729 | -46.26601 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47ee0e9a-d3af-38c0-be53-c74c7d4c82e8 | -10.97254 | -51.09309 | 2025-10-03 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9f4e8d6-1184-345f-bc8c-aa61bbee7508 | -10.28589 | -44.33244 | 2025-10-03 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c22efe83-6d7d-337b-9383-07f5b2be031d | -12.1172 | -43.44511 | 2025-10-03 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a0ae2d21-6f03-32c6-b29d-39c7620c1014 | -13.15937 | -47.90294 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 25582e0e-62c6-3105-a142-62ea60862f12 | -12.63632 | -46.96484 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfc08a3f-ec80-33e9-bc49-540ce346fc67 | -11.86489 | -44.97593 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89205017-a143-310b-9e0a-aad0e39b58c9 | -11.21986 | -41.60497 | 2025-10-03 04:12:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9e17b06e-25fa-3144-8a94-2dc49cece7fe | -13.54705 | -47.2492 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 765e3667-40d1-3b8e-8079-6624aa3c4a44 | -12.42329 | -44.08432 | 2025-10-03 04:12:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46cc91d7-047b-3ce1-afb4-c9f6af0415cb | -10.82291 | -41.26247 | 2025-10-03 04:12:00 | NPP-375D | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 971f06aa-01ea-3865-bc53-416e54ebe737 | -13.3069 | -47.59315 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 374e2fab-c6d2-33e5-83ff-4c14be98ca78 | -11.34936 | -44.97142 | 2025-10-03 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b190e3f4-3a61-3d90-920c-5878f1607967 | -12.62258 | -46.97696 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| d23905bd-dd71-3c78-a7f9-5b9ec8f825b0 | -8.71403 | -47.98187 | 2025-10-03 04:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 890eb48d-f5f1-3bf7-9875-9c3019b1fe51 | -9.952 | -48.77445 | 2025-10-03 04:12:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| abe38234-79c0-3a1c-a565-876736562f88 | -14.63965 | -44.7406 | 2025-10-03 04:12:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b05b858b-f938-36a1-8b3d-33b627396d13 | -11.84385 | -44.95243 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ff25fe7-bb9f-3b32-9276-36e471de4079 | -14.59691 | -46.72758 | 2025-10-03 04:12:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 83308512-bcbe-3ee8-a7cd-494a6e7043f9 | -10.8091 | -46.74922 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 547c4b79-db26-3167-8aa8-98e1ee9c2f41 | -10.94317 | -46.71177 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2f9cfacb-a7d3-3e9a-8d0c-aea057e0fadd | -13.80937 | -51.30463 | 2025-10-03 04:12:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f953ed8-1346-305d-907c-be61a5f1bb00 | -12.75753 | -44.90364 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 086f9e80-6306-357d-9c87-75938f29a732 | -10.86848 | -46.67682 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61cd5f74-9da2-3fa5-8ae1-2f570c039f91 | -11.6336 | -45.06497 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 48d37733-2276-38ca-abe2-5228df24191d | -14.70114 | -43.89122 | 2025-10-03 04:12:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 7e112021-652d-331c-a2f8-a8a1e1a09856 | -12.91332 | -46.36642 | 2025-10-03 04:12:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e699688a-f0c8-33c0-844a-5f3cd9a3ef24 | -11.10011 | -47.83407 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d934792-0c3f-3af1-9672-bf5ffdf6e92d | -14.46035 | -48.40933 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc8663f5-ed56-3418-80d5-d1509b139b4e | -11.63773 | -45.06162 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 815c3608-d6c6-3be0-8f3d-673b150b0f36 | -14.29249 | -45.96875 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fac92ec-cae2-3f5e-bd4c-99874bdb3b6b | -10.45773 | -45.84567 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45d434bf-48b3-37a8-a776-4fea7178679e | -11.4908 | -44.99361 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90106c68-b61e-353d-9e36-8b82af5852b8 | -12.6242 | -46.96751 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 616c0129-8b92-30e7-bc46-d39e74370cfa | -13.35215 | -47.33903 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a3d6cc5f-8599-3674-abf8-ba6628267630 | -11.8014 | -47.92101 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd6b63b2-1e2e-3482-bacc-649a6e53780d | -13.27687 | -47.26346 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 59bc432b-de57-3d61-a955-7bf6e509bbc9 | -11.10696 | -47.84273 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01dd9fc6-f415-3843-b334-0713fbe395e0 | -11.84667 | -44.9569 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e52cd6d3-5ad5-33cd-ada5-4036e9aa540a | -11.11454 | -47.87106 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea520848-f941-3615-b81d-c70e874d2ea5 | -13.23669 | -48.4973 | 2025-10-03 04:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4e046009-ec8d-3934-bdc2-f6fe2b07b453 | -13.74729 | -47.98697 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 26b5263b-da51-3a28-b9e2-d347e1365d39 | -12.22658 | -43.77045 | 2025-10-03 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3e294da-6ee9-3a39-94a0-a938f57f27b0 | -13.9659 | -48.11494 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7970548e-467d-3c23-8212-3d2db0fbbfc3 | -14.59987 | -46.71033 | 2025-10-03 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d271cc05-4e4c-3284-bcde-3309bc4da3a3 | -9.91516 | -50.50879 | 2025-10-03 04:12:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f0ba3e4e-9105-3d39-85ae-92aec8f28b61 | -9.90065 | -45.95098 | 2025-10-03 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6136caf5-b6e2-3e6e-80fc-d9b189e0fdf8 | -13.77027 | -47.58326 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 776a0d60-f583-3e54-b1c5-f6b38227a7cf | -10.01019 | -48.50223 | 2025-10-03 04:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e90f207c-3422-3716-8537-c3cb25166f89 | -8.83975 | -48.85807 | 2025-10-03 04:12:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 102ac1a0-b1b6-3ec5-9dc1-4861a7fa1404 | -9.91916 | -43.772 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 26cc9969-1746-3455-98a2-efece2a92758 | -11.61769 | -47.99301 | 2025-10-03 04:12:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17878891-688b-3a03-9504-625f7acb3949 | -11.8586 | -44.97089 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce41f660-e44a-3674-a7af-08fd7d439e7a | -13.24251 | -47.34658 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7cb9d94f-4262-3fcd-9777-d92445ee8bdb | -13.32038 | -47.58474 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fd3a1c69-f529-34f5-81de-5b09e72ebc11 | -11.4352 | -43.49789 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 020dd1b8-476d-3f6d-b0e8-4668cff6906c | -12.41115 | -45.16563 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72ae259f-f87c-3de9-a1c2-f58dc892d8e6 | -11.83874 | -45.04771 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b507c9a5-9a04-33a1-b753-6455659e0b66 | -13.22221 | -47.36073 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bdb2cfc4-4c73-3f6d-80c4-1b1400877ca3 | -11.0723 | -47.80708 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c692d9b-3b27-398d-99d8-063781b963a8 | -13.39673 | -47.55868 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a1a0b8ea-9d83-3cc0-baa9-706b963de4cd | -13.9659 | -44.86629 | 2025-10-03 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eccbc780-effc-35a2-bda6-574372385444 | -12.12166 | -43.43864 | 2025-10-03 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 08374265-f1c8-3d95-911a-a4e3a35bc7e8 | -8.80692 | -46.66533 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0cd62f77-d937-3779-b4ed-bd02c4d3189d | -11.86142 | -44.97535 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38e54c69-8762-358f-a3b8-2cb82b5a3471 | -12.125 | -43.43916 | 2025-10-03 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2e636a0b-2b7d-3c5e-88ed-3065f8a893f3 | -13.96561 | -48.16353 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88028151-ae76-3e54-b5df-82d0b78b1b31 | -11.86771 | -44.98043 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75a526f8-864f-370a-bcbf-8f196a46df96 | -13.75833 | -48.06358 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b272a712-8321-3bca-8fdf-633c24fbba2c | -11.87422 | -45.00582 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e35abca5-7d60-3e7e-9021-26a607b52089 | -9.41299 | -47.53643 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cdde99bf-067d-3d52-9d2e-04fec9ca5d64 | -14.30315 | -45.88407 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cb4342d-d11b-31b6-914b-2dc32dc158dd | -13.31081 | -47.24863 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 781e753e-8065-3283-9cda-215c705241c8 | -8.803 | -46.66466 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a4f93a3-25e5-376a-b99e-1bf892f37d52 | -11.05735 | -47.79667 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9a89d75-2e5c-39a4-9600-06537e6767e6 | -12.86692 | -46.99595 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a186907-c22a-3249-89a2-5a31ed3a5f19 | -13.77288 | -47.56853 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3b058206-87f4-3dac-b536-2c61c3b09df8 | -9.06792 | -46.65943 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d3a5d7f8-4fab-394e-a50d-273c64d43ad0 | -13.98246 | -48.12645 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b9302ec-cbc4-3cc7-a613-26cfa650ffb4 | -11.87486 | -45.00198 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01270aa5-d3e3-38ea-b26b-9c8633d93cad | -11.90627 | -46.3097 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 859271ec-c7d0-371e-a5c8-abf0ed90a417 | -11.86553 | -48.007 | 2025-10-03 04:12:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40b3dfb4-e144-34c6-8d01-f5c89880f23c | -11.61146 | -45.02579 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb40f952-182e-3303-b505-f7e4be14b474 | -14.19849 | -46.05741 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| d22bc8f1-4ee4-30ee-a0e3-c93cd25bffca | -13.35436 | -47.33757 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2719330-3c7f-3e29-aa66-aef9692f063a | -13.23257 | -48.49668 | 2025-10-03 04:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94157171-0948-3597-b223-1b56073c23a7 | -13.96158 | -48.10639 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 93c1176f-b2b4-37af-99e5-593edcec831d | -12.64753 | -46.87649 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 291e215e-1711-3291-bbf6-fb4725c9bfd4 | -12.29893 | -46.87992 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0a8d939-cd66-3553-b937-3d70e4fea4fb | -8.70976 | -47.98113 | 2025-10-03 04:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5efc5ed-66bf-3526-bbc1-e3165ccaa62e | -8.70905 | -47.98516 | 2025-10-03 04:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0183a7f-dbf3-3190-aeaf-87c6eceabae9 | -12.65644 | -46.89227 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fda93d0-8992-310b-a0ce-b47a0b40ecd6 | -12.61798 | -46.98113 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 138be2df-b308-3a2f-be34-b3dcb31ccab6 | -10.01026 | -50.23524 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |


[Clique aqui para ver as próximas entradas](README54.md)
