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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e73b16c2-4bbe-30f7-93df-704d0eee14b1 | -13.87911 | -48.59713 | 2026-09-19 04:59:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 38e82293-5977-3a21-bbc1-a124ec167aa1 | -11.19886 | -55.03637 | 2026-09-19 04:59:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30fcc4be-89d2-33de-ab20-6f13b1b933e4 | -14.13827 | -45.16549 | 2026-09-19 04:59:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6ab9ece-61f0-3503-b01c-2d27a22e0da7 | -11.81563 | -46.86298 | 2026-09-19 04:59:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be2338b7-fc6a-320d-9ca9-71760487ade0 | -14.66291 | -46.654 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5d3f4862-531f-3279-861e-8fb2bf2f7f08 | -11.40855 | -47.63762 | 2026-09-19 04:59:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05880c83-c743-3b61-a65b-e56f2039db81 | -10.86742 | -54.09614 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5783ec5-12e1-3a57-9bde-e0cee86f13bf | -10.88569 | -54.06679 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05be1a55-768f-3a4c-a872-32b852f872cf | -10.88414 | -53.99111 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1110658-061b-3950-834e-e553562c816d | -10.8662 | -56.20441 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 998d8980-dd32-3562-b8a6-c3abb2f2e7b0 | -11.06521 | -49.76133 | 2026-09-19 04:59:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9975ba1-4f6e-3118-ba10-d6c085583586 | -15.02693 | -48.55862 | 2026-09-19 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9ae40293-87da-34e3-a934-4b0375f95ee5 | -15.54736 | -56.01477 | 2026-09-19 04:59:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca3186f9-32f5-30af-8efe-023ebd16f5f0 | -10.92057 | -53.97555 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d4edc31-4b0d-3522-8985-91750a494e5f | -12.33321 | -50.73081 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ded9f344-ff27-344a-b936-ddb2f1e02c4f | -11.39539 | -47.63587 | 2026-09-19 04:59:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4a8a45cf-5424-3d91-a8e4-623a7ea34a22 | -13.73175 | -48.80052 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26400382-edfc-3782-8874-3410820caf52 | -10.69079 | -60.74424 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 908e9985-5528-31c9-890e-e4b79959253f | -12.1266 | -46.98079 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cd0db24f-5cea-32fb-b07d-600e177c12a6 | -11.4373 | -51.4624 | 2026-09-19 04:59:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71c67a35-23c9-3190-922c-eecc459ce4c1 | -10.71228 | -60.72892 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91e0d1e2-e943-3c53-ae62-c6fc222e37a0 | -12.33879 | -50.71829 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88c4eb09-70d2-30b5-ab86-3fbc141902a6 | -16.3123 | -53.85741 | 2026-09-19 04:59:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 312ae4b6-0500-327b-82dd-903f243e1330 | -12.14948 | -46.97651 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 56b25023-9f9c-3549-8a4b-b1f797972ca4 | -12.33083 | -50.72155 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b571edf-a76d-3a12-ace0-090c55fd687a | -12.60277 | -50.9296 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41a3ebd4-26df-34b8-82dc-be38e9ab84ee | -12.13895 | -46.98497 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2c4b05fe-7e0f-3d9d-a432-f36becaf8622 | -10.71705 | -60.73278 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49ba903f-cf30-39f9-a44b-c5b6964a0e0a | -11.49605 | -47.72161 | 2026-09-19 04:59:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2860845c-bd93-3994-b1f4-363b4d035316 | -10.86967 | -56.20501 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2984360d-8309-36c5-b61c-fea1952119b3 | -10.72134 | -60.73071 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83e8593f-ea67-3b57-a312-54570794f463 | -10.86468 | -56.19214 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2f925f3-cf16-3ae2-84b3-ddf496405653 | -10.89117 | -50.88769 | 2026-09-19 04:59:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5db2003c-b520-3242-bd80-52c737de391a | -10.87464 | -54.07217 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1dc0e02-2c11-39b1-89dd-af78c4a81cb4 | -15.05885 | -48.5849 | 2026-09-19 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7671fb60-efe4-3912-a4d7-a6a0e2b552aa | -14.69236 | -46.6579 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b66fb3b3-6fcf-3f62-8b53-3191647d7fee | -12.34873 | -48.20344 | 2026-09-19 04:59:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd5bfc1b-fc98-3d24-8ea7-228f8932c358 | -15.0248 | -48.57543 | 2026-09-19 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1c64c383-6d93-3262-8e6c-78a98ff24814 | -10.86402 | -56.19605 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e17f2da-80fd-3d88-9881-5f204ae80da5 | -10.92886 | -53.96613 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e006e86-ede5-3d9f-a589-50f526b30ba9 | -14.15703 | -45.16889 | 2026-09-19 04:59:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2445adb-4e14-3026-99d7-92a3fa7071da | -9.39336 | -60.35387 | 2026-09-19 04:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0aeeb192-af90-349c-9f7e-42c90e051787 | -12.9967 | -46.98438 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| e1aa3eec-f7cb-3079-8ba7-3d9b7f2c2076 | -13.59622 | -46.93734 | 2026-09-19 04:59:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f2d071aa-05f3-3c10-8e89-b924a5fd48f9 | -9.33338 | -60.31816 | 2026-09-19 04:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 364cc177-344c-373c-afeb-cd8693ab0ff2 | -9.37124 | -60.32139 | 2026-09-19 04:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5105ae91-91e5-3ba3-8a39-042e38e9b3f7 | -10.92555 | -53.96558 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6b96fce-5f5c-3c20-977d-37a7801ddf54 | -10.86597 | -53.99897 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e1d7e49-4f58-3dc9-909f-22005e795b00 | -10.88745 | -53.99165 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb9343f7-710c-308d-87d4-b089bd612d81 | -13.3859 | -49.45209 | 2026-09-19 04:59:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bd2c6a6-0002-3f50-a6c6-ea17062d9d4e | -10.92443 | -53.97259 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4e103f25-b2c9-386f-bf0c-b92570938b06 | -10.88513 | -54.07029 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0584485e-62bf-31a9-b449-1c1fcbacb4cb | -15.60416 | -56.57184 | 2026-09-19 04:59:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7c76e67-60f9-3406-9e7d-8993e78b5fe0 | -11.06072 | -49.7655 | 2026-09-19 04:59:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9455e1b-7111-3c63-8994-67df54272461 | -10.89792 | -53.98983 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7230d4e9-954c-3952-8451-d6d5dc066f8c | -12.12327 | -47.00512 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6358bbdc-36b1-3b75-8f8d-8b892d56824b | -11.6689 | -54.4395 | 2026-09-19 04:59:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87b4e1d9-21c6-30a1-a282-61d7efe0b7d2 | -10.8807 | -54.07675 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| beda1b01-94b8-36a4-9c71-3b3cb51136e3 | -13.31954 | -51.77494 | 2026-09-19 04:59:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b6294dc-c683-386e-b06e-0309d10ce83c | -11.67441 | -54.44764 | 2026-09-19 04:59:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 190ab71f-111c-32d3-a05c-4ac20f2d24da | -10.90565 | -53.9839 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| feee7fad-5f7c-3490-b663-6baf6bda189c | -11.67272 | -54.45821 | 2026-09-19 04:59:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0755483a-fd3e-3a2b-978f-473cd19ecca0 | -12.5782 | -47.08781 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0ac6a52-50e1-3452-b341-166cc9e93fa7 | -13.00371 | -46.96683 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| caf46cb7-11ca-3ace-a4bc-6902387b1f0d | -11.49984 | -47.72653 | 2026-09-19 04:59:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06277d84-68af-3ee0-b68e-4c73a6f92bce | -13.32246 | -51.77952 | 2026-09-19 04:59:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ecfcfa8-bb08-340c-89d0-c9f2b0e9d6a9 | -11.42098 | -51.45182 | 2026-09-19 04:59:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81e0f6d4-4f27-33c1-8a71-7133a40cea2a | -12.6055 | -50.73041 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56c899d3-c40b-3eb3-bc1a-28e408d72002 | -15.64438 | -52.71347 | 2026-09-19 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d4b7157-a0af-3b81-a576-f8b3abd8da41 | -10.70321 | -60.7272 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4ccfdbfa-ae0a-3fe2-af2c-452eb3a86298 | -11.79012 | -47.69834 | 2026-09-19 04:59:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 867b5bd6-1dff-3f9d-a7ed-3584b07083ee | -14.17644 | -48.75697 | 2026-09-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2ac7443-66ac-363e-8215-80a5105b71e4 | -11.3947 | -47.63863 | 2026-09-19 04:59:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee364905-8847-3655-8f60-95ab14ced927 | -14.68814 | -46.65166 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88dfdbfe-e8e5-304a-af9b-075fc7afa0aa | -10.86816 | -56.1927 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 553ae258-fa09-3502-9058-30d8d7328012 | -11.93881 | -55.91845 | 2026-09-19 04:59:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 795a69e0-1ae1-35c3-af8e-d7d4fb7a86be | -12.13164 | -46.96857 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f3b8a82-272e-3cfe-9775-f643889b79b1 | -11.31487 | -51.74343 | 2026-09-19 04:59:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9d5cf2e-5074-32a3-b590-2d508143baab | -11.02423 | -54.15731 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac4d8a3c-4c09-3cce-a388-6f1189f1bf6a | -10.88018 | -54.05871 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70874cb1-ddd1-3591-bf1d-7bdb17b70f6b | -13.30194 | -51.64898 | 2026-09-19 04:59:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f8e0703-5b24-33a2-bd4a-886e152d0e08 | -11.83636 | -46.83845 | 2026-09-19 04:59:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f8862832-92a6-386a-8365-9412abc22693 | -13.74199 | -48.7878 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6dc916f8-9383-3b7a-bb35-1d8fb6de3f8f | -15.58115 | -56.53706 | 2026-09-19 04:59:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15ebe20c-d3b2-34c9-b6b4-c1eeb948a46f | -15.68245 | -52.76739 | 2026-09-19 04:59:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d374245-212d-3f18-8c3a-7a94614f1a75 | -13.51385 | -48.94653 | 2026-09-19 04:59:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66bcf3ce-577b-3b42-9df8-3cdfc2c51a5c | -13.01041 | -46.95182 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9fd1651-c69e-3f1f-ae0d-978021b3b217 | -11.96663 | -45.78031 | 2026-09-19 04:59:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23d87fd3-d924-36d1-95a3-e3b5f6ae715e | -10.88293 | -54.06275 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0ae587c-0caa-3442-8105-bb5a2206e809 | -15.02461 | -48.56363 | 2026-09-19 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fea68234-ec10-392f-a074-6af64c8f7d3c | -15.02292 | -48.57623 | 2026-09-19 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0ee604d-41be-33a5-a451-729160332d6a | -12.12727 | -46.9759 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00490ba0-9875-3141-aea3-dc7e38f5ced9 | -12.69166 | -45.96489 | 2026-09-19 04:59:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f3f96e18-8541-3971-b3f3-5146f7dd846d | -10.86854 | -54.08913 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4199e6eb-110d-3116-8f93-ba1b406afdc1 | -11.8178 | -48.83329 | 2026-09-19 04:59:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49aab321-a3b1-3152-9111-9e46e8f5bfaf | -12.39248 | -48.48062 | 2026-09-19 04:59:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c12cfbb-4fc9-3215-8d9c-738af378a788 | -10.86491 | -56.2121 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e648a17-61a1-32ca-bc60-dbb12e72dab8 | -12.27726 | -49.16941 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 683d3cc6-d953-3f0f-8fe8-e3ee1f69b802 | -11.97953 | -52.45618 | 2026-09-19 04:59:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aaa4ccb1-4272-3b99-8025-f37a48d1afe0 | -10.85643 | -56.19873 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README87.md)
