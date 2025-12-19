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
| 63cdeae0-0cca-3146-a33a-375351fa5258 | -9.4648 | -57.8449 | 2025-12-19 02:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| dd154719-ec4c-329a-8813-bc1bc23e5bdd | -1.2944 | -53.0491 | 2025-12-19 02:50:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| ba9dd237-e989-3d08-9dc7-7b5b85c96175 | -8.25603 | -35.27592 | 2025-12-19 02:57:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 85c66cf9-5736-342d-b1bf-555d40616330 | -8.06556 | -35.13956 | 2025-12-19 02:57:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5e3e9423-470e-3ddc-86dd-050310982eb8 | -6.08109 | -37.32331 | 2025-12-19 02:57:00 | NOAA-21 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e6096813-74c2-3540-9202-a2654832c72f | -6.75594 | -35.1678 | 2025-12-19 02:57:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 39b2ba81-3e83-3fc7-a225-83393e78e517 | -7.96541 | -35.09782 | 2025-12-19 02:57:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bad98155-1a7e-3b5b-89aa-2e856844afa4 | -6.08211 | -37.32119 | 2025-12-19 02:57:00 | NOAA-21 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8ad54eb5-f24f-375f-b291-7dbd1ada43ea | -8.06481 | -35.14367 | 2025-12-19 02:57:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 46cf46b4-d13e-3c87-9b0d-bb2a7c72dbff | -9.7374 | -36.3208 | 2025-12-19 03:00:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 160.7 |
| 1e64b468-d750-3d5f-b99e-847c66039e64 | -9.737 | -36.3477 | 2025-12-19 03:00:00 | GOES-19 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 86.7 |
| 1b9b7ae3-51cc-3717-ab14-28197eb55ca2 | -9.7567 | -36.3174 | 2025-12-19 03:00:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 96.7 |
| 500bf5e3-9215-3b1d-aa8a-d0568b4b9c0b | -9.74406 | -36.32692 | 2025-12-19 03:00:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 50968fda-0cc6-32de-bad9-a4b6ddb668f1 | -12.90149 | -38.46674 | 2025-12-19 03:00:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 448eae59-1411-3b22-9d65-bd5b51e9dffa | -9.74214 | -36.33673 | 2025-12-19 03:00:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 7dd6b9eb-1cdd-3061-bc5b-72d9fe61c6a7 | -9.52223 | -35.99459 | 2025-12-19 03:00:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f2dbf9a2-35cd-3efb-acb4-ad1f89ae0e2f | -9.74916 | -36.33311 | 2025-12-19 03:00:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5baa917d-ed88-38ff-87ca-1fb7e3407b81 | -9.52308 | -35.99012 | 2025-12-19 03:00:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 68afe554-0163-35e0-ae8c-5e11f3794a74 | -9.74311 | -36.33179 | 2025-12-19 03:00:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| fa6887f3-5c15-3aab-8f1e-cb0dc7fa5cb1 | -9.40134 | -35.9293 | 2025-12-19 03:27:00 | NPP-375D | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 59648e02-a3a0-31f1-acb9-331660de52a0 | -7.10003 | -37.39765 | 2025-12-19 03:27:00 | NPP-375D | SANTA TERESINHA | PARAÍBA | Brasil | 2513802 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f0c2177f-0a3f-308b-b235-5eb30b46fb01 | -9.03692 | -40.64313 | 2025-12-19 03:27:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 95548662-6eb7-333b-bfc1-b9015f740e89 | -9.0315 | -40.64206 | 2025-12-19 03:27:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e69ea5da-8be6-359b-88be-f9c85d00e81e | -6.32486 | -39.71416 | 2025-12-19 03:27:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7d6e4a3d-f4af-3d85-beb7-2656b14dccdb | -2.94238 | -40.44279 | 2025-12-19 03:27:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e42763bd-05de-36ce-a57b-97667f454e31 | -7.10009 | -37.40077 | 2025-12-19 03:27:00 | NPP-375D | SANTA TERESINHA | PARAÍBA | Brasil | 2513802 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| baef0149-9f81-39b6-8c53-2822431cce99 | -8.95828 | -35.18398 | 2025-12-19 03:27:00 | NPP-375D | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 66013e68-efa5-318e-a0bb-e8f96e656b7b | -6.08553 | -37.32275 | 2025-12-19 03:27:00 | NPP-375D | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b512cfb5-2588-3748-b603-f00457b99290 | -9.96074 | -36.55212 | 2025-12-19 03:27:00 | NPP-375D | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fd0af375-ca79-3ac3-94c1-3f74fc9ef8e2 | -6.10723 | -36.75191 | 2025-12-19 03:27:00 | NPP-375D | FLORÂNIA | RIO GRANDE DO NORTE | Brasil | 2403806 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 29eba6e6-a471-3bea-ac5c-e70ab7bf9523 | -7.38735 | -35.25244 | 2025-12-19 03:27:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9a79f196-f416-381e-87d2-86326a94013b | -9.95728 | -36.55184 | 2025-12-19 03:27:00 | NPP-375D | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| eadc6273-dca3-3271-a23d-3ccb925e61f2 | -9.11192 | -40.21156 | 2025-12-19 03:27:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 56cdd7d5-0b4c-3963-bc84-f3e952e22a12 | -10.56695 | -36.78119 | 2025-12-19 03:27:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 10dc374c-fa31-35bc-800f-d9894d188220 | -9.17087 | -35.70271 | 2025-12-19 03:27:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 7bcf3552-2526-3524-be8a-38b9175619a2 | -2.94528 | -40.44589 | 2025-12-19 03:27:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 82211cac-c2bc-32d1-a324-af80a7ddd202 | -6.75616 | -35.16863 | 2025-12-19 03:27:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7b7bfe8f-df42-372f-a9fa-4295edd51c51 | -8.23919 | -35.38349 | 2025-12-19 03:27:00 | NPP-375D | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f9194713-bc24-35f2-a74f-e64a86fa0180 | -7.19866 | -34.8668 | 2025-12-19 03:27:00 | NPP-375D | JOÃO PESSOA | PARAÍBA | Brasil | 2507507 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 03df1793-1944-340a-9bf0-08f9a5db8d5b | -9.74603 | -36.32582 | 2025-12-19 03:27:00 | NPP-375D | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 09752e67-1c5e-32fd-a074-183adba8dca7 | -9.52554 | -35.99173 | 2025-12-19 03:27:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d56dc6a8-66d4-3911-829a-fb6c67f58270 | -2.94164 | -40.44707 | 2025-12-19 03:27:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a3c090cf-c135-3f38-af6c-5c6d210f018d | -8.95907 | -35.17935 | 2025-12-19 03:27:00 | NPP-375D | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ae2ab9bc-2ba3-3571-9461-e0675cc4363a | -7.96647 | -35.09886 | 2025-12-19 03:27:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 781f9073-5db8-321a-acf8-d0f463f2304d | -7.22436 | -35.49002 | 2025-12-19 03:27:00 | NPP-375D | MOGEIRO | PARAÍBA | Brasil | 2509404 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 370a4fae-130a-3fe8-a869-11dfb91c67c5 | -10.5697 | -36.78215 | 2025-12-19 03:27:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| cc1eeb23-4896-3c30-9926-c704ffffdbad | -9.95979 | -35.98781 | 2025-12-19 03:27:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| a3f4f105-86af-3e3a-bfa3-5985a561b05d | -5.69798 | -35.27095 | 2025-12-19 03:27:00 | NPP-375D | EXTREMOZ | RIO GRANDE DO NORTE | Brasil | 2403608 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9b615c53-50c2-3753-93f7-a5b0641b3437 | -7.22583 | -35.4917 | 2025-12-19 03:27:00 | NPP-375D | MOGEIRO | PARAÍBA | Brasil | 2509404 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6ac92296-f718-308a-9417-d00c41eb6b32 | -10.57104 | -36.78199 | 2025-12-19 03:27:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a8642639-fedd-3424-b79e-ed61ecc5eda4 | -7.38819 | -35.2475 | 2025-12-19 03:27:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 547a3deb-aa2d-3734-aeb9-5d5c9e254924 | -9.95741 | -35.98567 | 2025-12-19 03:27:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 2d40e2d1-0e5d-3436-9e7f-a55bb3517958 | -2.94457 | -40.4502 | 2025-12-19 03:27:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8103c4c9-6c7b-31db-8e75-c8302a957520 | -6.76008 | -35.16931 | 2025-12-19 03:27:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 444e0a93-0e50-3025-a96b-2c82be4bd25f | -10.3379 | -36.53834 | 2025-12-19 03:27:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8533ed74-75e1-3b49-a030-a57a15df1a44 | -6.32549 | -39.71057 | 2025-12-19 03:27:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b3da5dc2-c8bb-3776-b15b-70d94a5540e6 | -6.08096 | -37.32194 | 2025-12-19 03:27:00 | NPP-375D | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a0506486-5b8c-3697-8785-e7b4f32f8124 | -11.75984 | -43.32382 | 2025-12-19 03:29:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c8ca08e-c487-33c2-a626-94baf9b905b1 | -13.37684 | -41.3479 | 2025-12-19 03:29:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| db8b8de6-c705-37fe-b2df-b74ed8b4dbc5 | -15.90879 | -39.30053 | 2025-12-19 03:29:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ab92af8a-3af5-334b-b03c-a685a348a3fa | -13.38689 | -41.88014 | 2025-12-19 03:29:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8e5e9b2e-a799-31b3-af83-d1acb90af140 | -13.39123 | -41.88698 | 2025-12-19 03:29:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7ed79c27-7dfc-3a2c-841f-04973a8abd2b | -11.85268 | -43.7309 | 2025-12-19 03:29:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ee3f186-7b00-3700-9fd8-2ae7eeae5b09 | -13.39192 | -41.88355 | 2025-12-19 03:29:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7d54e300-9fb9-3da0-bea0-aae44b8072a1 | -13.39206 | -41.88272 | 2025-12-19 03:29:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5b9f0d2e-9a46-39ae-86e9-76faed84448e | -15.3833 | -39.21306 | 2025-12-19 03:29:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1ada04be-37e8-36fd-8284-9f9ed4a04aa4 | -13.39278 | -41.87934 | 2025-12-19 03:29:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 52f94a3d-3a9a-378f-909c-6cb95fc12c52 | -11.75372 | -43.32251 | 2025-12-19 03:29:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b5006ccd-40f1-3b04-9dad-6a0cd6f6616d | -15.38246 | -39.21752 | 2025-12-19 03:29:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 630e134f-3576-3ea4-95e1-9a4c332da0fe | -13.39107 | -41.88776 | 2025-12-19 03:29:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 35a2a906-dac9-3881-8898-4501aff9a329 | -13.39287 | -41.87853 | 2025-12-19 03:29:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 30566981-a1bf-346b-a467-f064ac075627 | -13.39359 | -41.87535 | 2025-12-19 03:29:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 37234090-a6f6-3680-a047-024fe36a5ce4 | -11.85163 | -43.736 | 2025-12-19 03:29:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f07f2c45-8b4c-33cd-86f2-508719bde411 | -13.94316 | -44.35839 | 2025-12-19 03:29:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5a5a263-8d55-3d2e-8416-a1f30fa9f67a | -13.94425 | -44.35316 | 2025-12-19 03:29:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5c61162-e0d4-368a-a835-ba8cc1d91d9d | -12.9039 | -38.46504 | 2025-12-19 03:29:00 | NPP-375D | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| d22c65cf-cfc4-32a6-a248-1d73900954ab | -13.39365 | -41.87455 | 2025-12-19 03:29:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 829986a1-5ccb-3b3d-b7a2-d7cb3065905d | -13.38605 | -41.88448 | 2025-12-19 03:29:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2658b892-6629-32e9-b9b7-ab423d5d186d | -27.98503 | -49.06562 | 2025-12-19 03:34:00 | NPP-375D | ANITÁPOLIS | SANTA CATARINA | Brasil | 4201109 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7ddfc3d1-036b-3184-8b34-f7327e77e088 | -6.08675 | -37.40682 | 2025-12-19 03:46:00 | NOAA-20 | MESSIAS TARGINO | RIO GRANDE DO NORTE | Brasil | 2407609 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3c122d2b-81c4-366f-9803-290d081740f3 | -3.74097 | -49.73171 | 2025-12-19 03:46:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa21ebcd-4081-3d0f-959f-a848a5a32781 | -3.74926 | -49.73383 | 2025-12-19 03:46:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 081c4ed0-7a40-300b-b815-e52b229f64f9 | -2.94363 | -40.44637 | 2025-12-19 03:46:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1b017767-d553-3940-9f44-936cd6fb8d2b | -5.52943 | -36.80788 | 2025-12-19 03:46:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b7f7b43b-33c0-312c-85a3-cbfcd3ba78b1 | -6.08343 | -37.32084 | 2025-12-19 03:46:00 | NOAA-20 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b03313f3-5292-30ac-a7f1-ea4e32695054 | -5.30216 | -37.55463 | 2025-12-19 03:46:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 68d26c59-9e20-39d5-be37-19a1bdf45721 | -5.08328 | -37.62776 | 2025-12-19 03:46:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 95a9542d-c8a1-3361-be4f-8eaf642cf299 | -1.02766 | -46.63901 | 2025-12-19 03:46:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f95eb08-2cd4-32ce-b2c6-78389ad6dac9 | -4.97537 | -39.02244 | 2025-12-19 03:46:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e99818a8-76ab-324f-9808-9b860aea2a55 | -4.81158 | -38.57929 | 2025-12-19 03:46:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d5300aa8-fedd-3de6-96fb-563dfea8c2fc | -3.7479 | -49.73311 | 2025-12-19 03:46:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00f1669c-b5da-3ab2-9729-923fd6164260 | -4.99757 | -38.05596 | 2025-12-19 03:46:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8f42cdc9-6e73-359d-a856-d447efb208f0 | -1.02838 | -46.63456 | 2025-12-19 03:46:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 269d04d0-a1fe-3b86-a0c8-357d3dede46d | -4.05925 | -38.26441 | 2025-12-19 03:46:00 | NOAA-20 | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 553926d6-3971-3228-bc62-4e3309729bb4 | -6.10913 | -36.75132 | 2025-12-19 03:46:00 | NOAA-20 | FLORÂNIA | RIO GRANDE DO NORTE | Brasil | 2403806 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6ba3ad78-0250-35c5-9a57-0483592d8463 | -5.7 | -35.2696 | 2025-12-19 03:46:00 | NOAA-20 | EXTREMOZ | RIO GRANDE DO NORTE | Brasil | 2403608 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 552b2a29-3e1c-3227-a3d3-c36ce5174efb | -3.74238 | -49.73211 | 2025-12-19 03:46:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 450208a3-14b5-3ec6-8852-cf1ed2984e02 | -6.10582 | -36.7508 | 2025-12-19 03:46:00 | NOAA-20 | FLORÂNIA | RIO GRANDE DO NORTE | Brasil | 2403806 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7144d17b-141e-3e9b-91ee-23668d5a4371 | -5.82049 | -39.08585 | 2025-12-19 03:46:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ad45c10b-f01c-3809-9c7a-b679aaec098d | -5.18343 | -40.49199 | 2025-12-19 03:46:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |


[Clique aqui para ver as próximas entradas](README3.md)
