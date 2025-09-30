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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9943ebe4-6345-3b01-b2db-9933a29521f5 | -14.31546 | -39.25587 | 2025-09-30 03:49:00 | NOAA-20 | ITACARÉ | BAHIA | Brasil | 2914901 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c8494746-5828-3971-968f-363d70d01da1 | -6.70536 | -44.56151 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 435c2239-a494-30cb-9b63-6149c7fcf6fa | -5.82214 | -42.77958 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 2dffd4ec-f23b-3c4e-8a3a-05af3fc20d5a | -6.36768 | -45.64774 | 2025-09-30 03:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52ed058d-f1de-33c7-ae8b-9247091f3ffe | -14.04805 | -44.95537 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 107ce54f-942b-3ad0-8895-5cf7d1eefc7b | -13.57772 | -48.0559 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f9494924-6640-3388-b710-34b4880fac13 | -14.50996 | -48.44304 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f999269d-5715-3609-80d8-1f9889a8f455 | -13.3524 | -46.38188 | 2025-09-30 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0516db79-c2c2-3fe7-8de0-e46aa9060b02 | -16.72872 | -43.11328 | 2025-09-30 03:49:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1955635c-aec8-39da-bc87-b08347eec7dd | -5.74726 | -42.87481 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| da7e9b1a-0bd5-3253-9861-dea254011dfa | -6.4972 | -44.11899 | 2025-09-30 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17d588e7-f95a-3389-854b-b48e457ab8ab | -12.95677 | -46.40248 | 2025-09-30 03:49:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9962d38d-e8ed-3d80-857f-ced2cbd7e647 | -11.2001 | -47.21776 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8d446e7e-c38e-3572-b66f-ee010ca055f3 | -13.20768 | -50.95372 | 2025-09-30 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 0504de50-35f8-32a7-b76f-8cd5cdcca610 | -12.69687 | -45.29019 | 2025-09-30 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c63483e7-281b-3ab6-b041-912a9d9893c9 | -15.10909 | -46.48818 | 2025-09-30 03:49:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4910293a-a6fd-3e13-8000-90f20c2e2600 | -15.48643 | -48.5564 | 2025-09-30 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81c34410-f275-3d01-89d1-3bd0b12e9cd6 | -13.6061 | -48.03261 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c897c543-2f8d-3bbd-90ff-c8ac5f5ee59f | -12.84828 | -47.01516 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a2f82b1c-f66b-344d-8105-85158f3be33e | -15.28022 | -47.8619 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| dd6bfbc0-1db0-31d8-9035-d70c5e7c5867 | -14.58841 | -48.28128 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f05c681a-b9dd-3260-8716-e4a5eea587fa | -19.52846 | -41.36383 | 2025-09-30 03:49:00 | NOAA-20 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 762fbe70-a7b5-3dc1-a201-8fd140b3e9b7 | -15.91859 | -46.20304 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce1ceb0f-1300-3cbf-86bd-31a4424b2c04 | -14.52301 | -48.49282 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2415db09-c94e-39b1-8f30-d3206e88352d | -6.72339 | -47.2098 | 2025-09-30 03:49:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a00d249c-90d5-3374-9c76-9fe291f67cde | -14.57614 | -48.28635 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23bdfaef-3a3d-3116-b9e2-fad72953dcde | -13.20525 | -50.9599 | 2025-09-30 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6da4d4e7-817c-371e-bce7-059472c10beb | -12.84256 | -47.01715 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7964ec4-aee4-3dc1-9020-ba9cb7c64218 | -13.41024 | -48.15419 | 2025-09-30 03:49:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 28670a42-2138-33de-87c1-a6928f941682 | -11.74886 | -44.74676 | 2025-09-30 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6b0edd94-2843-3df4-8379-a4587a484706 | -13.01436 | -49.44678 | 2025-09-30 03:49:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2adcd93a-d2fb-33a7-8487-7dad91085791 | -19.35946 | -40.20153 | 2025-09-30 03:49:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9d215049-8f02-340d-9d71-653ada27d707 | -14.71319 | -45.67605 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3805b3cb-a9e9-35d4-918b-ad719c443c8a | -13.73845 | -47.90128 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 730685bb-7599-3083-b733-ea3c0e801818 | -14.53495 | -48.49022 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1c6a2f39-6a5a-3024-9f3d-a92c26c66d79 | -14.53198 | -48.24549 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8fe02241-75e4-3b6b-9aa2-fe372d30d5db | -13.23477 | -47.3126 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 621acc97-a3cb-3735-a12a-627696427042 | -5.9084 | -43.70908 | 2025-09-30 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9fa5dd3e-4aac-309b-831e-91a3a580fd4f | -11.93584 | -43.91851 | 2025-09-30 03:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ccdf2505-a259-315d-a163-49773747fca4 | -7.11856 | -45.55164 | 2025-09-30 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42e7b3ec-b61a-3fd3-aba7-4567a8b463c0 | -11.16587 | -47.23939 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59eb8fa8-f92b-3af9-bb13-d8fc4c97e911 | -5.77724 | -42.85746 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4f9950c5-7aec-3771-9961-8040594c69db | -13.23779 | -48.44705 | 2025-09-30 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0d361d32-a808-3082-b34e-5edf2a9cc464 | -6.09957 | -42.65795 | 2025-09-30 03:49:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 38175c89-ff75-31c0-b9e3-fd0a1b4cd4c4 | -13.21446 | -47.33338 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1e4a8a7f-8d06-38da-bc67-79cbf681df59 | -13.66495 | -44.3112 | 2025-09-30 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 41d81308-94ea-36ee-aa0c-ec4fb4fb1072 | -14.71103 | -48.23786 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1e13aac-fa8f-30fe-a824-8e8c90386455 | -5.8527 | -45.75455 | 2025-09-30 03:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcb75496-128e-361f-b6c0-87ef2c09a31c | -13.20767 | -50.94865 | 2025-09-30 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 2db575b6-4b24-3177-a000-6564894bd618 | -19.35003 | -43.97205 | 2025-09-30 03:49:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dfd8f9c6-8c40-301a-903a-050764def7c8 | -16.36261 | -49.12801 | 2025-09-30 03:49:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd9a45b8-18bb-3a52-93d8-2208189b778d | -13.58957 | -48.0529 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7fc47645-c263-3c60-b9fc-3c50ce7d7fc7 | -14.53683 | -48.25836 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c8087206-7f05-3d51-9445-134cece83ef1 | -13.49851 | -47.40495 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85db2483-9159-3310-9e1b-3227e20bab71 | -6.56098 | -43.41921 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 4.5 |
| dfc17b0f-db10-39f3-988a-1cf5cac5bc1e | -14.51397 | -48.42545 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2151c81c-e75e-3827-9582-60a66798bd23 | -6.08333 | -42.46725 | 2025-09-30 03:49:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f678a0d4-2be0-334f-ac3c-bce1f2ec6b43 | -15.04549 | -46.96546 | 2025-09-30 03:49:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d9d2414d-6886-3281-bd6c-cf22eee7d1e2 | -15.93064 | -43.30932 | 2025-09-30 03:49:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cbd3c277-3d4f-3c65-b98c-44153ee343a5 | -11.71435 | -44.44288 | 2025-09-30 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74074a24-cfc1-3937-9468-985ad79d2a26 | -15.23038 | -48.02987 | 2025-09-30 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3640a2ab-50a6-34e2-8460-bbda49bec97a | -13.07448 | -47.0773 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e207fa7-80b8-3bc6-ad88-ad87b6cddf15 | -19.30807 | -43.81484 | 2025-09-30 03:49:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9cb3b3a2-925a-3cd1-b228-1d15ee36a7ab | -16.41558 | -47.9661 | 2025-09-30 03:49:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed55fd72-5dd3-3949-8336-9a95faf27392 | -6.55656 | -43.41798 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 7de18cf7-a594-3505-b1e5-d0500b39f275 | -12.8401 | -46.87954 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3d1221d-3bbe-3eb5-8e51-d4d5b2dd16d0 | -6.89492 | -44.52409 | 2025-09-30 03:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28b97e60-bb2e-3309-bed3-0d20d1b433e8 | -13.77715 | -44.24677 | 2025-09-30 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f3d3643-b08d-3dca-8241-5267884d38f8 | -6.87428 | -45.09452 | 2025-09-30 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5a1cde5-a646-3aaf-a735-e9ec0f86a4bc | -13.59998 | -48.03504 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04d5832c-fbc6-348d-a8a8-8a006fb8cc5f | -12.86883 | -46.96426 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2911879-10a8-36df-a3c4-2a2ac9058530 | -5.98043 | -42.56354 | 2025-09-30 03:49:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b2fbe040-4e18-3be8-ac49-43d936d45781 | -15.91481 | -46.24853 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7384b6af-6198-38b4-ac70-0b0fcf595632 | -15.26398 | -47.85888 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78af2e22-99e2-355a-bfb2-e235ca24f314 | -14.68587 | -48.16884 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 146f55cf-7ef7-3412-87e5-d178779f3eb8 | -14.68747 | -48.24373 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c3887a7-63dd-3323-8884-d1138de5fc84 | -14.53477 | -48.23136 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec5fccac-6b3f-3c41-8683-fd98fb4f8afb | -11.75506 | -44.73843 | 2025-09-30 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ee3112de-fdad-38f1-a285-c7d99c5177f8 | -18.30544 | -42.89268 | 2025-09-30 03:49:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fa560db2-5367-3238-9370-ce12b1709b16 | -11.16302 | -47.23688 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49d1e725-38b9-3e15-b2cb-ed7280a9fdbc | -12.96453 | -46.4152 | 2025-09-30 03:49:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d690e68-8654-3b69-b94a-ee3c72e45ebb | -13.83992 | -47.49 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77d9e7cc-48e4-3138-8fd2-6cb1e512543a | -5.51181 | -43.87495 | 2025-09-30 03:49:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2d595118-92de-3af4-8733-4970b7a25601 | -14.7141 | -45.67135 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed07c488-167a-3106-9f37-aa48770fe848 | -13.48862 | -47.40013 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21185a5b-06e7-3edc-971f-966bbe4f0a42 | -5.74527 | -42.67226 | 2025-09-30 03:49:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 60afd094-b128-3381-b2b9-5ba9e06fb9a0 | -11.74836 | -46.8412 | 2025-09-30 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fd74bec-0fa4-38f7-b2c5-7dcbc6821490 | -6.68647 | -42.79754 | 2025-09-30 03:49:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bc4cb359-f5bb-3cae-b040-a4dcc7580837 | -16.06329 | -51.04119 | 2025-09-30 03:49:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| acd69fca-853e-3763-8ec0-35546a3e0aa0 | -7.23288 | -46.76554 | 2025-09-30 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8c9ca929-f270-34eb-a4a0-e013a2fad14a | -13.77857 | -47.85335 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e55364ff-4b91-335a-a92d-56f6181e7e2a | -6.55532 | -43.41472 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 7662d7d3-a260-3538-93fa-93405ded7719 | -11.06159 | -47.82706 | 2025-09-30 03:49:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 871972b7-932d-376f-97e6-74a4fd42e47c | -5.74661 | -42.66435 | 2025-09-30 03:49:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 983515f9-5073-39fb-ad35-6e606f318ece | -13.38519 | -48.07796 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1911d20f-de31-3e6f-b87f-8336945dd7c6 | -15.91599 | -46.24216 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 008e8fe5-4a9c-3dd1-913b-396f5b59566f | -15.27054 | -47.85632 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a8f1432-0afc-3d7b-876e-cac16aa3dcfa | -17.61259 | -40.67788 | 2025-09-30 03:49:00 | NOAA-20 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c40a3f39-c009-3e7f-8a36-92a05a5aa64e | -13.82158 | -47.47084 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbba613d-ae30-3b70-9a03-e3f059eefa1a | -12.87521 | -44.63273 | 2025-09-30 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README43.md)
