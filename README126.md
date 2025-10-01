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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5481b05-3c20-3ff6-96f7-256b1aca4fe1 | -12.94919 | -48.42498 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10af16d6-4aaa-32c5-be56-a4ce140e848c | -9.55525 | -54.59295 | 2025-10-01 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9eec4bfe-68a9-3692-85c9-6b71793b41fc | -12.69071 | -48.56638 | 2025-10-01 05:10:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3d5809a9-bc2d-34b1-b68c-1e46f8c9c488 | -12.85131 | -47.0351 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e7d1334c-2580-3fab-ae5d-47266d85fa3e | -12.71191 | -46.90735 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4cf0eab4-c366-3ea4-96fa-7026b1639b2f | -10.62099 | -51.59708 | 2025-10-01 05:10:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54019260-3c46-39da-a2d8-b8f56d889856 | -12.78262 | -46.87658 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 90fbf766-2051-3bc0-a51f-7f9061a4d1fa | -10.79516 | -45.35598 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00f61066-cb9a-3a70-ab7b-44b886086d1d | -13.33192 | -47.85902 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dfbd506a-269d-3218-94a4-fb2bd8dafe2c | -13.34694 | -47.8074 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52d79d2a-1972-370f-a7cb-2c3e6eaad401 | -11.84955 | -45.01287 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be832a7f-da55-331f-8fa3-003e7e091c0d | -13.29464 | -47.24186 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60d3edab-6d94-3c25-a1a0-df86f54d9201 | -10.43509 | -50.86724 | 2025-10-01 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 194cb9a9-706e-3fee-b97a-d1f24048437e | -11.84813 | -45.01493 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1a33d4a1-9f11-37b5-9fea-dcde06c375d6 | -12.78391 | -46.86521 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 70c360e1-8260-3978-b11c-363c3de2821b | -11.6451 | -47.50047 | 2025-10-01 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f9de7f40-331d-3f08-966b-3bf4f6de1506 | -13.03061 | -48.6763 | 2025-10-01 05:10:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 83ce5ec2-42f4-37f8-841f-792a06194666 | -12.44462 | -50.18362 | 2025-10-01 05:10:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0162d30-eba4-34e6-88c4-39dfae5e8872 | -7.84564 | -47.24922 | 2025-10-01 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41b4449f-507b-3337-ac79-f255d26a78a9 | -9.58536 | -54.59064 | 2025-10-01 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| feb009f1-5eae-3d2f-9362-4d2cfa51aded | -9.81254 | -47.85569 | 2025-10-01 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c5f1acac-2adf-32f4-8532-7944a3e584c6 | -9.5699 | -50.95068 | 2025-10-01 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4fb9ab88-ccee-3d57-a9ee-8902be04a1a0 | -11.15393 | -54.12721 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43fcca60-d76a-368c-9854-fe44851bf414 | -6.95107 | -63.1002 | 2025-10-01 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7c24a6fe-0283-3090-a593-429e2ab6861a | -11.81127 | -44.976 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cdf8c61d-0196-3d46-bb0e-795a55713434 | -11.14797 | -54.1241 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b6f113f-958a-336a-b1b7-437d8dce3b28 | -8.98842 | -50.19983 | 2025-10-01 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3cbd9d8b-6c01-37d1-a3df-6ca0b03a6d4d | -13.20926 | -47.33219 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ee6519c7-b2f5-3442-80e9-630cbd32c826 | -8.75384 | -45.9353 | 2025-10-01 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 389da248-fbdd-39bc-8011-70b33661aa9c | -11.96398 | -46.59332 | 2025-10-01 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5e20dcb-07e7-36e8-9b4a-495c5e855861 | -13.33061 | -47.87097 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f6664e5e-9ced-35a1-9592-f1b346f49325 | -10.18597 | -52.55108 | 2025-10-01 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e38bf55-a6d5-32bd-9910-44a7760d5bc0 | -9.4332 | -54.71442 | 2025-10-01 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 580c9320-6cdd-3a44-8df8-0024e05a7e76 | -13.27774 | -47.22469 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c202594b-5373-3ad2-b49c-53018118dd88 | -11.1532 | -54.11509 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6cb62f4c-c2b1-3f39-a929-10645167c369 | -11.84253 | -48.06558 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f6fc4e60-c949-34f7-b040-b716a4c8605d | -11.83674 | -48.06487 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 315e8f06-7f89-374a-b8de-c9c9cda4fb6d | -9.45512 | -56.64725 | 2025-10-01 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 60aa3bbc-7f07-3dc0-8dbc-6eb3b2878bd1 | -11.83727 | -44.99649 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0ef3ec70-7741-357e-95b3-f1a6dac0aa47 | -13.28906 | -47.23575 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb3de24e-9113-3525-8d8b-9516c6c2bc9b | -13.5509 | -47.27724 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 783ec401-1536-3a64-aad1-9fdcbcf77350 | -12.62151 | -44.8624 | 2025-10-01 05:10:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 34ef5cf9-d86d-3071-b570-6388623e93ff | -13.41854 | -48.20076 | 2025-10-01 05:10:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fde45a52-631a-3eeb-b7f0-b4761a10ba89 | -12.39354 | -44.76855 | 2025-10-01 05:10:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e89e60b7-a4e8-3757-8e60-619e6efa4bf7 | -11.81907 | -44.96941 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7235ea72-5396-390a-9e33-a1ea6e918c61 | -13.37578 | -48.10911 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3704a9b-f84a-3ef0-8ec1-a34bfe24eeb3 | -13.28289 | -47.23468 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| db3ea40d-88a4-392d-9afc-f07690dfff59 | -7.14445 | -47.26463 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cf94602d-ec7b-3ed6-942e-263a128ad4c4 | -8.55651 | -44.75242 | 2025-10-01 05:10:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7674762c-ebc5-33ac-a903-fac88c3589c0 | -12.82885 | -47.00934 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a65c05f6-adc4-3b1a-aa4c-c5cea2dd5973 | -10.62544 | -48.59568 | 2025-10-01 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5a86bc6a-37d9-3be4-882b-4e1e78f0554a | -7.02109 | -44.45923 | 2025-10-01 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad71d933-a298-3a78-9a43-3ad64b87693d | -11.92096 | -48.00054 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24a818c8-bbd8-3877-8047-72dedcbf32ce | -11.46245 | -45.0911 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e6150f8-2a32-38ab-a6ab-5abe102f1205 | -13.22422 | -48.44779 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9c829437-680b-3479-a51e-ebbf0e99e0fb | -11.18833 | -47.20098 | 2025-10-01 05:10:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5554d24-a72a-3c8b-abe2-bca4f5992cac | -10.08633 | -50.20142 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fb5341f5-e1b0-3f76-a5bd-e999e040b0a7 | -11.46867 | -45.09809 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 827efdbc-abb0-333e-904e-e8a73da1e39b | -13.29304 | -47.58407 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 095e21de-eb4e-3e8a-bb05-b39fac2d364c | -6.95333 | -52.55455 | 2025-10-01 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5bb0c86c-7d9e-3760-a5ad-7be6b1ad2720 | -11.79726 | -46.62339 | 2025-10-01 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| a75d3aff-5d27-3165-8176-27e1b367dcaa | -7.05169 | -46.40931 | 2025-10-01 05:10:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49df095b-4a17-3694-8f3a-8e4e4aa3a37e | -10.19327 | -52.55988 | 2025-10-01 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5eab4a73-2ac0-33c2-8459-f26459f14c30 | -13.3265 | -47.3391 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 11448ac4-fbf5-37fe-8105-c57ed8d8365d | -7.01942 | -44.45729 | 2025-10-01 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d546bb3a-a431-39ff-b5f8-4b618fddb5f8 | -11.30929 | -53.95902 | 2025-10-01 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a393e71-af56-3942-8818-f9e9e1178379 | -6.58213 | -51.67899 | 2025-10-01 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e04b2a8f-977c-3c30-92b9-f72c1b483840 | -6.91136 | -55.4533 | 2025-10-01 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15e9bfc5-da0f-3a2b-99e4-8b84975e0e28 | -7.82272 | -46.98302 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5c27685-cd0a-3693-918a-a66109bc52d8 | -11.85011 | -44.99638 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4cde83ef-cf38-3bc9-a3fe-6ac6298b6ea0 | -7.05047 | -46.41859 | 2025-10-01 05:10:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1199d497-6e26-3f39-a4b8-2402c2efb9a5 | -8.89545 | -46.63386 | 2025-10-01 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a58f5a61-e7b1-3b3a-8cb9-e5b2d7106f7e | -11.16609 | -54.12407 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a948c22f-5f0c-3191-9850-be193c412208 | -11.40019 | -44.89922 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3165cb88-5cf7-3a69-a3d9-1c22eed30377 | -13.32916 | -47.85558 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 35fbba6b-e5ce-320b-b657-65d519ca2cd3 | -8.55781 | -44.75299 | 2025-10-01 05:10:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85cecaaf-1602-36d6-8aea-e23b0f371988 | -11.1525 | -54.11988 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 82b8605c-ecd2-3361-8d45-734d96d23980 | -12.43109 | -50.17743 | 2025-10-01 05:10:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc319d5b-0be3-3ee5-8940-009fd81b03b1 | -7.77267 | -47.39134 | 2025-10-01 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c020a2d-bcf1-3eb0-8fc7-6d08be95dafd | -12.42603 | -50.17675 | 2025-10-01 05:10:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb8ca945-f6ea-3fdf-825c-e44d463066a1 | -9.58473 | -54.59497 | 2025-10-01 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34ee401e-a8e6-3619-ab5c-6f603ad7009a | -12.69626 | -48.56799 | 2025-10-01 05:10:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 68c07bef-5fd8-3084-816e-0c84e6e5a122 | -7.01868 | -44.46273 | 2025-10-01 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dfb3b8e7-1481-300b-a217-b32c1897e5e1 | -10.53995 | -58.02761 | 2025-10-01 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0b8f69d-6873-380d-b976-863030e33647 | -10.62457 | -48.60264 | 2025-10-01 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a04360f6-393b-3a26-a4ec-436c1666f776 | -7.04816 | -46.42295 | 2025-10-01 05:10:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12642b90-8e71-31da-b92d-217e6e9016b8 | -11.73934 | -46.86868 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 639aaa07-0b98-35ad-8c94-c04893195a81 | -12.95338 | -48.43838 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47ba8d1a-d923-3b4d-b48c-909a014337e3 | -12.66582 | -46.86435 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c361b40-db4d-3490-a1db-fde22f8a005c | -13.32869 | -47.85961 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| aaf0d1a0-477d-37e5-af71-5309162984b5 | -11.43153 | -55.05862 | 2025-10-01 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 828f010f-c3b1-3052-914f-4c71a792108c | -7.02373 | -46.98139 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1a267a73-0f87-357b-82bd-24a5fab11c26 | -11.46107 | -45.10416 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f2d5b289-0893-36d8-999d-b1ebb4e9a98c | -13.24103 | -47.32745 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36a562af-168e-3780-a3b0-25671b3690fb | -11.80023 | -46.6262 | 2025-10-01 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| e293bb79-2d1c-37ce-98d8-ce2e3f493010 | -11.80147 | -46.61588 | 2025-10-01 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 02cf4af9-e70c-3535-a778-fa47fefec223 | -13.33267 | -47.33978 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8857392f-2c88-36f7-a8b4-915e1ea62dfe | -8.57839 | -44.75448 | 2025-10-01 05:10:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f00b8f1c-48aa-3435-8fc9-eb6a9a5cac90 | -12.70666 | -46.89771 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 125ef37a-b3fc-3838-9ec6-82e1db48ff66 | -13.53944 | -47.26704 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README127.md)
