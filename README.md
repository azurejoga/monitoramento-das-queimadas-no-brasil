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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 358f641f-9104-3584-9991-501fbd11bc02 | -10.2548 | -36.4443 | 2026-03-21 00:00:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 86.2 |
| c019f4d9-39ba-332a-9331-652d7239c352 | -10.2742 | -36.4408 | 2026-03-21 00:00:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 124.0 |
| 62934d9b-7e73-300f-a3d3-bef5007bb495 | -15.93242 | -38.94633 | 2026-03-21 00:01:00 | TERRA_M-M | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| 00854ce5-68dc-371a-9890-83c9e1912d2a | -15.92869 | -38.93784 | 2026-03-21 00:01:00 | TERRA_M-M | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 32.2 |
| 98242564-f443-37de-8010-653644a5f9b7 | -15.93005 | -38.93196 | 2026-03-21 00:01:00 | TERRA_M-M | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 20.2 |
| d796e98e-215a-3110-bce3-c31f64e6eb91 | -10.26576 | -36.42289 | 2026-03-21 00:03:00 | TERRA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 44.2 |
| 88fcabbc-a343-3583-852d-4c8857dfe5e7 | -14.12435 | -43.42533 | 2026-03-21 00:03:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 5ce3ea82-85c0-3be4-aaa9-bd32110e245e | -10.27084 | -36.45715 | 2026-03-21 00:03:00 | TERRA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 119.7 |
| c0bba791-316f-3fce-b9fa-01c56fcad0d2 | -13.46588 | -41.31392 | 2026-03-21 00:03:00 | TERRA_M-M | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 8c47391c-c9f8-3ef4-9b31-9c2689bca928 | -11.96173 | -43.38211 | 2026-03-21 00:03:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| df099a9f-f7f5-3b45-be68-f8fffd1bff37 | -8.42456 | -44.04018 | 2026-03-21 00:03:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 587d55db-d160-3d64-9f22-379b1b6bee0c | -8.43353 | -44.03886 | 2026-03-21 00:03:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 3043c6c3-dbce-3dae-8abf-f7d0313fe593 | -11.96042 | -43.37289 | 2026-03-21 00:03:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 706b7153-ee65-3621-a73d-659e00d52638 | -13.36202 | -39.90363 | 2026-03-21 00:03:00 | TERRA_M-M | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 99940a5e-7b8e-36af-809b-0e0fa018a190 | -13.39598 | -41.3315 | 2026-03-21 00:03:00 | TERRA_M-M | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 59945afb-0ce6-3302-9dfa-cb47e26991db | -8.43482 | -44.04805 | 2026-03-21 00:03:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 3002e670-822d-3928-a38f-e9c73d80cc98 | -11.65893 | -37.66557 | 2026-03-21 00:03:00 | TERRA_M-M | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 4c365e98-2b2a-3ad1-bd5d-6d34407c36ab | -11.92514 | -40.68047 | 2026-03-21 00:03:00 | TERRA_M-M | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 995d0df6-0365-388e-8c04-79247a5471d4 | -14.12307 | -43.4162 | 2026-03-21 00:03:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 9bbfe4e0-4ef9-384c-b22c-cab02739a6f4 | -10.27053 | -36.45075 | 2026-03-21 00:03:00 | TERRA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 191.2 |
| 4f081922-89be-32b1-9288-f13e3a189694 | -10.26629 | -36.42935 | 2026-03-21 00:03:00 | TERRA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 105.2 |
| edbb5b52-f085-3d72-925e-64bc77503f3d | -11.3294 | -55.2923 | 2026-03-21 00:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| aceb2080-7dd6-35c9-b333-90f91d750206 | -11.3294 | -55.2923 | 2026-03-21 00:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| a8d30659-a795-3cd6-8a17-50d3a07c12b5 | 2.123 | -61.2136 | 2026-03-21 02:10:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 33b0cbec-cf6b-32fc-9cf7-8f75aa71bb5f | -6.00148 | -35.34331 | 2026-03-21 03:04:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 124e4a5d-cda2-3c76-b6c0-8bbfafc28667 | -5.99682 | -35.34055 | 2026-03-21 03:04:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 543e045c-aedf-370d-9c64-c2753750485e | -6.00235 | -35.33858 | 2026-03-21 03:04:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8d48ffa3-307d-3d82-876b-c6c84a828230 | -9.05816 | -36.57737 | 2026-03-21 03:06:00 | NPP-375D | BREJÃO | PERNAMBUCO | Brasil | 2602407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e8a651e7-bd07-3094-a802-938e066a9fcd | -9.06447 | -36.57865 | 2026-03-21 03:06:00 | NPP-375D | BREJÃO | PERNAMBUCO | Brasil | 2602407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3475b4a6-ffcc-3efe-a869-b22f100eca30 | -11.96131 | -37.9525 | 2026-03-21 03:25:00 | NOAA-20 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4101d25e-89ac-3b85-a2b6-53fadd094d32 | -9.05944 | -36.57434 | 2026-03-21 03:25:00 | NOAA-20 | BREJÃO | PERNAMBUCO | Brasil | 2602407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5fa7bc70-c412-32e2-8656-0acd64a8a95d | -8.4338 | -44.04193 | 2026-03-21 03:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 613c6d02-50d2-39b5-bee4-3665f7571f48 | -10.02021 | -38.1307 | 2026-03-21 03:25:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1fddaef7-0157-3824-a84b-b783bdc0b209 | -6.00124 | -35.33809 | 2026-03-21 03:25:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 5699c148-67c0-354b-aba3-c9d8a80cabbb | -11.84172 | -37.93982 | 2026-03-21 03:25:00 | NOAA-20 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ddcf6566-7eff-3107-990e-ff4c556714a7 | -8.4271 | -44.04045 | 2026-03-21 03:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01ee6332-273b-3222-8a42-3870c242d06a | -8.43264 | -44.04797 | 2026-03-21 03:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6124f133-8e97-37cd-8ebc-5a3a8461084f | -6.44616 | -40.9859 | 2026-03-21 03:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e96eb1d9-44bb-3276-9ce6-afb964053987 | -9.84162 | -38.04488 | 2026-03-21 03:25:00 | NOAA-20 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 42236459-2c97-3744-8bbc-d57263e99910 | -8.4296 | -44.04031 | 2026-03-21 03:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9753d96-8577-3a90-8b46-8d3bd0033d93 | -11.5639 | -37.59305 | 2026-03-21 03:25:00 | NOAA-20 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6899db3f-821f-37cd-8141-bc16dcc89e1e | -8.60516 | -36.49245 | 2026-03-21 03:25:00 | NOAA-20 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c23419cd-efe8-3966-a0b4-144d3cf2b770 | -8.86948 | -37.35046 | 2026-03-21 03:25:00 | NOAA-20 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 23dda0f6-b1e0-3bfc-903c-a76d2a0b8b22 | -6.4469 | -40.98186 | 2026-03-21 03:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8266b252-1685-3375-a386-13a6ddf6ccac | -8.4284 | -44.04631 | 2026-03-21 03:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1390966-7b34-3782-a2af-ac611fca4719 | -9.06205 | -36.5742 | 2026-03-21 03:25:00 | NOAA-20 | BREJÃO | PERNAMBUCO | Brasil | 2602407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ea7665ff-0e82-3f73-88ac-555dfbe90d44 | -8.51906 | -35.86465 | 2026-03-21 03:25:00 | NOAA-20 | SÃO JOAQUIM DO MONTE | PERNAMBUCO | Brasil | 2613305 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ab9f4406-4245-3b27-9edb-4e35f4024665 | -11.96372 | -37.95204 | 2026-03-21 03:25:00 | NOAA-20 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b609cd6f-7403-3aa0-943a-b65760314017 | -8.4351 | -44.04776 | 2026-03-21 03:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76bd2b09-f7a1-321f-8874-39205646fb78 | -11.66148 | -37.65612 | 2026-03-21 03:25:00 | NOAA-20 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| db383005-e196-3fc8-be3f-2c5081fc01cc | -11.65726 | -37.65528 | 2026-03-21 03:25:00 | NOAA-20 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f4f643c7-aace-3701-b598-cf2ac163a668 | -15.72662 | -39.19754 | 2026-03-21 03:28:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1fbf4c80-155f-3b4a-bc41-a79764080122 | -15.72581 | -39.20189 | 2026-03-21 03:28:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 58bf50bb-3c47-314e-81eb-c930cc5fa5e7 | -14.12031 | -43.4199 | 2026-03-21 03:28:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e059a4f0-eaab-33a1-8426-c4c8e6ebc167 | -23.58957 | -46.42802 | 2026-03-21 03:30:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 5aa7854c-e860-3476-9c16-84c6bfc1ece3 | -23.59267 | -46.43131 | 2026-03-21 03:30:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 6aa3b281-8402-3109-9045-f02e645e757c | -23.5942 | -46.43465 | 2026-03-21 03:30:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d2573af0-2c22-3ead-83f4-90dbbf438e40 | -23.5953 | -46.43002 | 2026-03-21 03:30:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 827ef854-16b5-336c-a31d-0c53653bc4c0 | -6.45017 | -40.98437 | 2026-03-21 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2a392ad2-d3d7-32d1-a74e-263c5d93dd6c | -6.00125 | -35.34013 | 2026-03-21 04:14:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2eff50a5-0a04-3373-9a01-33ac559a4942 | -6.00202 | -35.33957 | 2026-03-21 04:14:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 22b4efa8-6ae7-3d04-a5d6-507103a6b55c | -6.002 | -35.33477 | 2026-03-21 04:14:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cd3e600e-48e7-3ea9-8707-ef034253f989 | -6.4473 | -40.98009 | 2026-03-21 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8c8b057e-2a15-38c4-8305-2886cbaf85fb | -6.44672 | -40.98386 | 2026-03-21 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a21cf99d-e6b2-3c13-a38a-beafba796bfa | -7.2101 | -35.78674 | 2026-03-21 04:14:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c4c2cfd2-eb62-3958-af76-264675a40d5b | -7.74449 | -40.14069 | 2026-03-21 04:14:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dc291311-5207-3534-9feb-66e46de4665c | -8.43402 | -44.03633 | 2026-03-21 04:17:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efb64d8a-055a-3a32-9839-122bbcde79c2 | -8.43678 | -44.04034 | 2026-03-21 04:17:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 93911931-aed4-3008-8029-0df05166cb19 | -12.49749 | -43.64792 | 2026-03-21 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f357a392-4d29-3d5a-a196-5b5026166436 | -11.96259 | -37.95126 | 2026-03-21 04:17:00 | NOAA-21 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1441264b-d557-3cdb-80cb-b1eb669dcfae | -11.96117 | -43.38026 | 2026-03-21 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b51a0c7-d0e3-3518-822c-db36da3081f4 | -9.06418 | -36.57737 | 2026-03-21 04:17:00 | NOAA-21 | BREJÃO | PERNAMBUCO | Brasil | 2602407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3168e355-8c36-3b3f-b664-b80ca26f193b | -14.12586 | -43.42201 | 2026-03-21 04:17:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bc33eb53-1164-3b96-b4b5-c193182c8f1f | -14.12698 | -43.41463 | 2026-03-21 04:17:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1849bd0c-c163-302a-a8d4-9f18f2d64de4 | -14.12249 | -43.42147 | 2026-03-21 04:17:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3fb7e53f-ffbd-37fb-b749-cc4ebda7a3bd | -11.95838 | -43.37617 | 2026-03-21 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3bf7b5c-c616-386a-a1e3-1cd4883192f5 | -9.06483 | -36.57248 | 2026-03-21 04:17:00 | NOAA-21 | BREJÃO | PERNAMBUCO | Brasil | 2602407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f3e96c0c-c66e-3d6b-908d-316102cbd6a3 | -11.95893 | -43.37261 | 2026-03-21 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0fa2919-4ca8-3cd6-a4b4-44c0312e4534 | -13.39999 | -41.32985 | 2026-03-21 04:17:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6cb3fa29-3a62-33b8-8bec-3b208ff21080 | -8.43568 | -44.04729 | 2026-03-21 04:17:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d15503d-5700-385b-8e42-9d9582288a8d | -13.46625 | -41.30875 | 2026-03-21 04:17:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 34381e92-723c-31c2-a600-a8355f314776 | -8.42686 | -44.03876 | 2026-03-21 04:17:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6933496b-af9d-3321-af91-03db2da09c59 | -8.42962 | -44.04276 | 2026-03-21 04:17:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 613fd7d6-56a5-3f11-9c7b-a903207b12be | -14.12305 | -43.41778 | 2026-03-21 04:17:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c6ca75be-79e0-30d8-9886-f222fa6b9f6e | -8.43072 | -44.03581 | 2026-03-21 04:17:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9d0f9d9-3c55-38f6-b97b-258ca7d0f01c | -11.00126 | -37.33587 | 2026-03-21 04:17:00 | NOAA-21 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 77936d7a-1752-38b1-854b-9c71f78a870b | -12.50828 | -38.95958 | 2026-03-21 04:17:00 | NOAA-21 | CONCEIÇÃO DA FEIRA | BAHIA | Brasil | 2908200 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4417455a-2413-3709-8d23-7c1fe1203849 | -14.45141 | -39.6663 | 2026-03-21 04:17:00 | NOAA-21 | ITAPITANGA | BAHIA | Brasil | 2916609 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7142f219-de8c-37e4-b3a0-939b0fa3bbb7 | -10.02255 | -38.13143 | 2026-03-21 04:17:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 077527b3-9907-34c6-92d3-b3dcb7c7f24a | -9.06067 | -36.57587 | 2026-03-21 04:17:00 | NOAA-21 | BREJÃO | PERNAMBUCO | Brasil | 2602407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| afb0b6ee-4012-31c7-82cb-c5650c3b5022 | -8.43017 | -44.03929 | 2026-03-21 04:17:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| edbb109b-0e3c-37c0-8f85-845d7bbf7009 | -8.43623 | -44.04382 | 2026-03-21 04:17:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79e92338-8fe2-3be2-afed-34f85b18906d | -8.43347 | -44.03981 | 2026-03-21 04:17:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d76b5f50-a3d1-3754-b31d-c001985ce6e6 | -11.96172 | -43.37669 | 2026-03-21 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91d62c0f-21c0-3de2-9c48-ab02360c418d | -9.0653 | -36.57654 | 2026-03-21 04:17:00 | NOAA-21 | TEREZINHA | PERNAMBUCO | Brasil | 2615102 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 651882a6-3220-3191-b5ec-c9d3b5ab6044 | -11.66081 | -37.65753 | 2026-03-21 04:17:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 56f3e98e-de98-3554-9a85-7267dccd356f | -8.43292 | -44.04329 | 2026-03-21 04:17:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02e1e7c6-3d9d-356a-b416-975b0176f56f | -14.12642 | -43.41832 | 2026-03-21 04:17:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ae9ff116-9898-395b-a723-740ca71a5e5b | -12.91877 | -43.01973 | 2026-03-21 04:17:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cf9bbb89-3b95-35a0-b63a-c0ad469a01f7 | -8.43237 | -44.04677 | 2026-03-21 04:17:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README2.md)
