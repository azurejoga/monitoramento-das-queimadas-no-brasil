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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87ace06f-be74-3975-be37-e1213c2db861 | -2.5006 | -47.1022 | 2025-11-23 00:51:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98539241-2a2e-321a-bc0e-b01dc4c70450 | -2.4388 | -49.0933 | 2025-11-23 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d12d6e44-e75c-3f02-94a8-34e01f68dab6 | -2.6492 | -47.385502 | 2025-11-23 00:51:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d6c82c1-a564-38eb-b12d-fff24894c6d8 | -4.7156 | -46.447899 | 2025-11-23 00:51:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 00b578fb-0dc4-34fa-86f8-f0badbbc77de | -1.3078 | -53.1437 | 2025-11-23 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cd4c6bf-f366-30d4-9707-0fb7b408b941 | -2.9517 | -45.434502 | 2025-11-23 00:51:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cf311680-e668-3d87-9672-ef215c5d7370 | -2.8792 | -45.1283 | 2025-11-23 00:51:00 | METOP-C | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 154e38c2-cc8c-375b-a956-73facdffca13 | -2.4486 | -49.091099 | 2025-11-23 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aaf78a30-60c6-3a4c-9f43-142cfc64efe3 | -1.3094 | -53.1506 | 2025-11-23 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3721193-6e6a-396f-8c23-159cba48a1b9 | -2.6372 | -47.377899 | 2025-11-23 00:51:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a5f4f2c-5cd2-3870-ad6d-7f54886b0451 | -4.7083 | -46.460701 | 2025-11-23 00:51:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 39d6addf-bd56-3a00-b3d2-5fc7a397d81b | -2.9614 | -45.432201 | 2025-11-23 00:51:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5093c88b-95f0-37b9-b0a9-cc5410550540 | -4.7181 | -46.458401 | 2025-11-23 00:51:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d885834e-d7bc-36e1-a1f6-2294fbe60ae9 | -1.3192 | -53.148399 | 2025-11-23 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50f28e70-fbfe-3aff-96ea-f4c80c23f2e7 | -4.7206 | -46.468899 | 2025-11-23 00:51:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fc978a94-a7bf-3aef-a11a-c37864ed8eba | -2.647 | -47.375702 | 2025-11-23 00:51:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a2f8523-ba30-3081-a0ba-d58cb408210f | -2.8824 | -45.141899 | 2025-11-23 00:51:00 | METOP-C | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c84ea217-4838-3706-a3ab-cf83dbf84c8b | -1.3176 | -53.141499 | 2025-11-23 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 888770e2-9cc6-375d-8eeb-dd9d85c39761 | -3.8367 | -45.350201 | 2025-11-23 00:51:00 | METOP-C | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 30776d31-57bd-3993-b3cf-563a9300cc68 | -2.9486 | -45.421501 | 2025-11-23 00:51:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 30b42ccd-8edc-395c-93ea-387aa455ffc7 | -2.6394 | -47.387699 | 2025-11-23 00:51:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea0d461c-8d84-3f54-bbe9-25e2a8728eb6 | -4.5609 | -45.495701 | 2025-11-23 00:51:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc869751-eb93-3f62-94be-0b1c124e500d | -3.7094 | -44.0028 | 2025-11-23 00:51:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a1c4fcb8-9c5c-33c3-9f78-736389449e5f | -2.9583 | -45.419201 | 2025-11-23 00:51:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 49c7737a-c76c-3426-b6c5-77a9b5fef44c | -2.9645 | -45.445099 | 2025-11-23 00:51:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 21f4e5b1-00a1-3bd9-870c-4d349bacff2c | -2.4982 | -47.091999 | 2025-11-23 00:51:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57b8e035-31b2-3f35-9ee4-a50f21309092 | -7.47863 | -38.9571 | 2025-11-23 03:14:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3bc91273-07d0-3aab-9e86-b85c27eafc07 | -6.84934 | -35.11207 | 2025-11-23 03:14:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 6b7427da-5b48-3673-921c-3bc7e43fb426 | -6.84774 | -35.10927 | 2025-11-23 03:14:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 21b4ba91-9438-3526-8643-e8b68f6f64df | -2.95572 | -40.55163 | 2025-11-23 03:14:00 | NPP-375D | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 5a87de72-de5e-30f6-815d-22e196553ec0 | -5.98134 | -40.38158 | 2025-11-23 03:14:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| c57fe8bc-93e1-3726-94ed-7b6a86f962f8 | -3.86821 | -40.64343 | 2025-11-23 03:14:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| ee690450-3bbe-3878-a50e-bdd81940e37d | -5.98018 | -40.38795 | 2025-11-23 03:14:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 21.0 |
| 4037d7df-a464-3216-bcfe-195400249538 | -5.70651 | -37.94851 | 2025-11-23 03:14:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4dcc9033-3f58-350a-8ae7-1adef7d34435 | -7.40298 | -40.06554 | 2025-11-23 03:14:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 14e94e11-89f8-341b-8f02-e7b92f7696b9 | -5.70437 | -37.94583 | 2025-11-23 03:14:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7aade778-11aa-374d-8386-ff2d6e428128 | -5.98075 | -40.38073 | 2025-11-23 03:14:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 1abb8f22-9643-300e-a937-4945dfbd80e3 | -5.62212 | -35.37241 | 2025-11-23 03:14:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d411f018-a6f8-38cb-b001-8a49d462ffec | -3.8664 | -40.64562 | 2025-11-23 03:14:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 4fa45977-e0e0-32c6-876b-00ef503a67df | -7.40957 | -40.06686 | 2025-11-23 03:14:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c29a656c-0872-3876-934d-38b6bb7d1427 | -7.41615 | -40.06821 | 2025-11-23 03:14:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 70d5f9c5-7522-33cf-8008-fe450504f590 | -5.70358 | -37.95033 | 2025-11-23 03:14:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d926e5a9-aae0-349f-b610-af4d77473590 | -5.62162 | -35.37533 | 2025-11-23 03:14:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 74df1584-feeb-39fc-ac98-9e5eaac5754b | -6.84678 | -35.11466 | 2025-11-23 03:14:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 31bb15c5-21d6-337b-b020-f4c6a8676299 | -5.97954 | -40.38709 | 2025-11-23 03:14:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 71e32452-f4fd-3cf3-ae03-9b50ad7b5306 | -5.83931 | -38.35871 | 2025-11-23 03:14:00 | NPP-375D | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f3b44e88-f6c5-388b-ad8e-93c2a935578f | -5.84015 | -38.35398 | 2025-11-23 03:14:00 | NPP-375D | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ee1fda3d-d2e8-3260-8b86-31eda6e56f24 | -6.32654 | -35.06269 | 2025-11-23 03:14:00 | NPP-375D | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a533f81a-5b45-3d6f-be7a-35db52ceda5e | -5.70048 | -37.94777 | 2025-11-23 03:14:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e00946db-972a-3261-b3cb-93fdd5213778 | -10.27484 | -36.32076 | 2025-11-23 03:17:00 | NPP-375D | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e514116e-82c1-3314-ad4f-7a4937b957a5 | -10.05887 | -36.45924 | 2025-11-23 03:17:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| aa6d3bbf-e1a6-3fb4-8d21-e1bef17b7e46 | -10.06335 | -36.4631 | 2025-11-23 03:17:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6cb2dfc2-8c08-3c39-879b-00d4e4dcc5d5 | -10.07844 | -36.46593 | 2025-11-23 03:17:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a1dfe156-2d6e-3b01-adee-bf6d3ca078af | -20.38966 | -42.18057 | 2025-11-23 03:17:00 | NPP-375D | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 476218cc-ca68-38fd-8159-50619d1a0012 | -10.06006 | -36.45846 | 2025-11-23 03:17:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| adaccb07-4889-3dc1-b7e2-9522d1b745da | -10.05955 | -36.46133 | 2025-11-23 03:17:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e4c9bd65-ef67-348e-bd36-536e45cc911c | -10.07341 | -36.46497 | 2025-11-23 03:17:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8b05b11f-59d8-3ce7-b1ed-80d8b538637a | -10.06457 | -36.46232 | 2025-11-23 03:17:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2532be35-b15d-3ad9-b1c6-ea2a9ecae6ac | -10.06389 | -36.46022 | 2025-11-23 03:17:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| d55fc62d-cb80-38a9-b4c0-c4223db4ea7d | -20.38895 | -42.18364 | 2025-11-23 03:17:00 | NPP-375D | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1e1ae1c6-4962-3a57-a79b-3c4cf955cfc4 | -17.8206 | -40.12224 | 2025-11-23 03:19:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 27.2 |
| 7514767e-37a3-349f-b0ba-da51162afc2b | -17.81583 | -40.11753 | 2025-11-23 03:19:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 43f786ec-a3a7-3be5-a45c-b006d5acaf6b | -17.82139 | -40.11855 | 2025-11-23 03:19:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| a1c411d7-0508-3711-98ea-a62ba3c3aa51 | -17.81504 | -40.12125 | 2025-11-23 03:19:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| d0c336bc-0c24-3ec8-9f64-b17cd4e3899c | -2.89044 | -45.2643 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 489a9aa6-6007-3529-ba9f-a6a52489b976 | -2.8988 | -45.28597 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b124042c-14f9-36ab-9e77-a66c72e03d90 | -2.88472 | -45.29801 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| befdebf5-6e62-3fef-8117-5a01a92515eb | -2.96095 | -45.43732 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e14e1233-c0ed-3d7a-b34d-bea23a0ccc69 | -2.88464 | -45.33852 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4f06c05-751e-351c-8837-e0faf5f5a8e1 | -2.94766 | -45.43524 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 816963ed-d346-3e7a-a11f-8089f3b6c90e | -2.86788 | -45.27761 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7ac4c612-49b1-393c-a8b1-3e5b4aaee6ac | -2.87158 | -45.29565 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 83b56253-882e-3e51-8586-ba39c3ba5c86 | -2.90442 | -45.30169 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7eda7875-ab1e-3698-910f-e8dbafdc2083 | -2.89979 | -45.28037 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02bf30a9-4f40-39b8-ae49-f663c29f118a | -2.89684 | -45.29712 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0650444f-712e-3a31-b722-2946bbddf274 | -2.86596 | -45.28884 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6c42a331-0513-337b-ab98-b8a677481ffb | -2.9034 | -45.29834 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50b4b763-80f2-3317-b15c-3134020f0eec | -2.87626 | -45.30796 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7e887232-7831-3b48-9255-cd6b161bbf0d | -2.87912 | -45.29111 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 88.9 |
| bb0c487c-2560-3647-a9ff-a70a0f8ba968 | -2.88198 | -45.27433 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 334be2b4-5a9b-3dfd-8a9d-1013b1be0f35 | -2.88008 | -45.2855 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 1535de7f-6504-343d-885e-76548056f5ea | -2.88949 | -45.26994 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 01e4bb47-f1b5-32f3-b013-45768539983e | -3.13493 | -41.47645 | 2025-11-23 03:34:00 | NOAA-20 | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ac39f594-72eb-3aaa-a073-8d20073e6ca2 | -2.88103 | -45.27991 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 99a9172c-1f2c-376b-b6c6-99fedcdf5e58 | -2.85556 | -45.31004 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f3c1bb27-d0c5-31aa-a47f-0eab13fbd2dc | -2.87432 | -45.31936 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5871a1ef-9efa-388d-9762-0b17eecb8472 | -2.89509 | -45.27676 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 95.3 |
| ba67ffd7-aa52-36b8-a22a-0c62741d4826 | -2.88561 | -45.33278 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f9ea23a-e338-3625-8a6c-98287dc69e0a | -2.89786 | -45.30042 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c5fd0ef-1b85-3204-9dc6-fefb9f2b4f84 | -2.86692 | -45.28324 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ac6cbf47-45a8-3184-8e49-08fa6952040f | -2.95282 | -40.5517 | 2025-11-23 03:34:00 | NOAA-20 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 88ebdb90-792e-32ba-bdef-551a7f27aee5 | -2.88366 | -45.34431 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d10a595-9a3f-3ea4-bd5d-fa7ddfee79d3 | -2.87817 | -45.29672 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 4384a6a3-0af0-3ae3-9b3e-25408833edcf | -2.86037 | -45.28196 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0145bd8d-6e56-35fc-b3c9-ab7e9b4494b2 | -2.86501 | -45.29445 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5bfc8f4f-3b67-3821-ba02-01c26b463308 | -2.95431 | -45.43626 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| be6a1171-5bf1-3c6e-b57f-e5d40657252f | -2.8735 | -45.28439 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 88.9 |
| ac2a0093-519d-3b64-9035-7065ba9b3dfb | -2.87541 | -45.27316 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 39.5 |
| ed841913-842c-3971-b7de-c055ca9c7f26 | -2.8753 | -45.31359 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e44b4027-377f-3b4f-94d6-230a4b54117e | -2.87721 | -45.30237 | 2025-11-23 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |


[Clique aqui para ver as próximas entradas](README3.md)
