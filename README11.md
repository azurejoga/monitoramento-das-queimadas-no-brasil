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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dba0b6a2-a199-3d3d-bd85-507a21928ccf | -6.65844 | -47.58107 | 2025-06-27 04:19:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c9e445c-916a-3f4a-950c-3d762a6e713c | -6.96064 | -42.90126 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 42.7 |
| 1626746b-6002-3599-a7f3-ded8f3b7cdcd | -8.47494 | -48.26396 | 2025-06-27 04:19:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 673e9f5d-32bb-3ec4-ab22-74aa335a3301 | -6.69286 | -43.07018 | 2025-06-27 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9f950d0-c5f7-32f4-94e7-e5f1b2ec3bb1 | -6.27601 | -43.68121 | 2025-06-27 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f78e2456-bf34-3ebf-be65-cd424ef1e269 | -8.06428 | -46.96223 | 2025-06-27 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64f46084-0e9d-310c-bd91-ac9cc67583cf | -7.54352 | -45.82672 | 2025-06-27 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 46ccbe7f-f74b-3f34-9fa0-96cf4bce61ce | -8.37671 | -51.07807 | 2025-06-27 04:19:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 368eee4f-3669-3588-bb2e-588ef3c0db33 | -7.20402 | -43.19175 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 65f0e77b-2300-3a86-847e-e27fde23e105 | -6.68946 | -43.06966 | 2025-06-27 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 63ffc316-db09-384a-a89a-79f4b90d30a4 | -7.55237 | -45.83527 | 2025-06-27 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b4e92a16-ade3-398f-9623-957cddbe87d1 | -8.44589 | -46.97418 | 2025-06-27 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3660ae6d-d459-3d61-9288-de96d66bbb8f | -3.0016 | -48.02528 | 2025-06-27 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30b0f5ef-dc29-3797-b2e9-1021ade51a24 | -7.26217 | -46.94787 | 2025-06-27 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a33ce324-082f-3caf-bbce-73c0785c2590 | -5.9228 | -43.47779 | 2025-06-27 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88240431-2607-342c-bbfa-927c1ec33a9f | -6.17556 | -48.08999 | 2025-06-27 04:19:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 1bdaa5dd-ea5d-3b0d-b760-feffe31ece01 | -6.96923 | -42.89104 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 0a03b827-39f3-3c02-afcf-2dc1daa7f9d1 | -2.90864 | -41.57866 | 2025-06-27 04:19:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9e8a692-2685-3e60-8027-ee890c365ce1 | -7.21974 | -43.08826 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 7639ed82-7c02-393d-93a3-14a41e56501a | -7.20686 | -43.19596 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d4f88ef6-1e13-3351-b3c8-c877ad30d8a0 | -5.85329 | -43.64399 | 2025-06-27 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 345f7d75-439b-34b6-ae99-e034f77145b6 | -6.96522 | -42.89428 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 4ff1f8f2-a41f-3e5d-aed1-4d11d381e3e0 | -8.4425 | -46.97364 | 2025-06-27 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1e0c2b5-53b6-3a3c-adba-d8d7df788e5e | -8.48275 | -48.26099 | 2025-06-27 04:19:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e726b3cc-3204-32ab-bed2-bda47f36b184 | -7.70872 | -47.84231 | 2025-06-27 04:19:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fd46dc5-1906-3492-87ec-615948d48dfe | -5.85662 | -43.64451 | 2025-06-27 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99e80499-1a24-3e25-8eea-c5693f4a0aa7 | -7.22201 | -46.3913 | 2025-06-27 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c0557ba-9bfe-3fc7-9e75-f48316487e1a | -6.50269 | -49.32166 | 2025-06-27 04:19:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76d51815-041b-3474-babd-a8b2db4fa8b1 | -3.03649 | -49.43675 | 2025-06-27 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| df702f78-cb98-3da7-8af1-db9f39b3f7b7 | -7.1927 | -43.19755 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bd57fc6f-4154-3586-bc66-0b41151c93a0 | -6.95779 | -42.89698 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 42.7 |
| 994cea4a-5ec3-37c0-aca4-28e77021f7a3 | -7.20722 | -43.07871 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 85161c93-7e2c-3a84-b15e-d881bf59ceb5 | -7.19666 | -43.19439 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0268028b-d9d8-3615-b535-df92d6d6a5fb | -8.68901 | -48.30959 | 2025-06-27 04:19:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a4fe54a-1203-3e0f-8247-98dac0429c3f | -6.27322 | -43.67713 | 2025-06-27 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 6ee40377-7b90-383b-abf8-55086575d68d | -3.03237 | -49.43611 | 2025-06-27 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c8c5a258-b392-3f67-88c4-0bbacaf78809 | -6.96465 | -42.89803 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.1 |
| bd27f8dd-485b-3da7-8624-f32e04c3e153 | -6.6889 | -43.07331 | 2025-06-27 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 077bf4df-f832-3624-a4cc-4f0a5ac0116e | -8.10268 | -46.74332 | 2025-06-27 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2421bbf7-c7bd-3631-817d-39246e97056e | -7.1459 | -44.10386 | 2025-06-27 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e641556-8510-3aaa-8c49-9e04d4732415 | -7.21007 | -43.08295 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 00f1a59a-2411-32fa-955b-9097f91144ab | -6.57469 | -55.00135 | 2025-06-27 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d960f6d3-2d9b-3a84-9749-cb7425cdf52e | -5.92 | -43.47374 | 2025-06-27 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 59583241-0a37-33c7-ae5f-f4d8ae3b16db | -5.45867 | -47.90459 | 2025-06-27 04:19:00 | NOAA-21 | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cc928a1-4db5-3e4e-b003-33deeed9aadb | -7.20006 | -43.19491 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2cd8cc37-8583-3a54-adf6-901744f53175 | -8.47777 | -50.27796 | 2025-06-27 04:19:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8047d0b8-9881-33fd-89ea-98300302d25b | -11.5779 | -52.115 | 2025-06-27 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 322.9 |
| 003925df-adf7-3e95-932a-ff643c5f43a2 | -6.9793 | -42.8798 | 2025-06-27 04:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 135.3 |
| ada7e23c-fbff-3eef-9a0c-8bcee2c148b3 | -6.9414 | -42.907 | 2025-06-27 04:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| b7bf77f9-ab57-3cd7-b2eb-2809a008da00 | -6.9791 | -42.9034 | 2025-06-27 04:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 174.1 |
| 8b360cc7-b127-3b6d-8993-57d6150895b0 | -6.9602 | -42.9052 | 2025-06-27 04:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 332.0 |
| fdd169c7-4385-3c8b-aa12-29b444b98983 | -6.1789 | -48.0929 | 2025-06-27 04:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 3cf89219-8260-332a-bcff-81f851b8466e | -11.5776 | -52.136 | 2025-06-27 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 3ec9b7f5-8685-3383-86a2-2b83c0a1630e | -11.559 | -52.117 | 2025-06-27 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| c47abaad-1c0d-37bd-b8ae-04c203e9a914 | -11.5969 | -52.113 | 2025-06-27 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 350bbd36-ba2f-3481-8365-2a484acf607c | -11.5782 | -52.094 | 2025-06-27 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 00128fb1-ebe5-3d9e-81f6-21a0cd3c3ace | -6.9416 | -42.8834 | 2025-06-27 04:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.7 |
| 07e633aa-daa7-340c-8c12-c2a32ffc6ed2 | -6.9605 | -42.8816 | 2025-06-27 04:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 266.1 |
| 30ed1f45-1039-342b-bda4-50bb5378c617 | -8.62492 | -51.57125 | 2025-06-27 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c1c3318a-95e1-34ec-b0c4-04116fa6ddf1 | -8.62353 | -51.57205 | 2025-06-27 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ddae2654-36b1-37b8-b025-089c21e639a9 | -12.00819 | -47.1577 | 2025-06-27 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a432a7b7-e03e-333a-a1b2-e811ad7469d1 | -11.77744 | -55.02521 | 2025-06-27 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48b786e1-4ea7-383a-ad48-9e38a7cfce2f | -9.78638 | -48.57153 | 2025-06-27 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 49911185-59ab-35ad-aeba-e3c6089cd564 | -9.82157 | -48.37722 | 2025-06-27 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 069e183b-5e98-3acc-8f3a-41ea9070130d | -10.81516 | -57.75243 | 2025-06-27 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69157a95-f188-3a13-a008-327fb4845893 | -14.53726 | -53.83484 | 2025-06-27 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6627ef00-8451-37a3-884b-915c27913d4a | -11.77685 | -55.02838 | 2025-06-27 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c9d82f0-5b70-3ba5-962a-f63613c4815c | -12.10845 | -54.66229 | 2025-06-27 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e8344fa-f1e9-3e0d-8a9b-35b58e8831cb | -11.8233 | -47.54236 | 2025-06-27 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9ee6c01-010d-3334-af0b-2ceb86cc227f | -12.75202 | -44.41396 | 2025-06-27 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7db1f1c5-7bb9-3b73-9a1d-588f1e965d17 | -10.62692 | -46.70731 | 2025-06-27 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e17a880-e4e3-3294-ae54-6f41c3a64980 | -10.83308 | -54.0453 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c35fe1e-986b-3d9f-98a7-e0c91e4c091c | -11.36381 | -48.71507 | 2025-06-27 04:21:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d2ef5d8a-4d46-3c06-bbbc-8c7bc28bd49f | -11.82452 | -47.53495 | 2025-06-27 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11c86adb-d99d-3a3a-9581-99d34be7b2ff | -11.11372 | -47.00642 | 2025-06-27 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 330fff18-92f7-31f7-a2ca-dd9b4c31c688 | -10.87377 | -53.77087 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d56b80ef-3498-306e-a335-ab231e1a7427 | -10.8673 | -54.30598 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d2e6040b-4a6d-3627-b722-12209421c163 | -11.74846 | -54.23301 | 2025-06-27 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30eba08e-cc5b-38f6-a579-b6b4250309c9 | -10.83228 | -53.75163 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cdd3a7cf-edf9-35fc-a45d-7810aec38b39 | -11.57218 | -52.11818 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 60401e7a-17ab-39c5-80e7-188e37f83003 | -12.04861 | -48.07563 | 2025-06-27 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a6f185e7-cc23-30bf-a9dc-1bfc22ed31b4 | -10.36179 | -49.91728 | 2025-06-27 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 588d5ad2-32ec-3952-a999-cceaf2c21344 | -11.57647 | -52.11892 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 92d1c56c-dfcc-3d4d-9606-aded1ab6681f | -12.00877 | -47.15411 | 2025-06-27 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 117eec0f-6222-32f2-ab44-939624fba04b | -11.75067 | -54.23056 | 2025-06-27 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99ae0c6f-9e62-3bf3-b7dc-0a0fad750f0d | -11.81561 | -47.52596 | 2025-06-27 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4c7fab98-c076-33ac-b0e3-c2683f8c1cdc | -12.02794 | -47.77287 | 2025-06-27 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7d1dd256-24ce-353f-a5b6-84d78409af8d | -9.19797 | -50.49777 | 2025-06-27 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 914bbab9-5c2e-349b-a957-320fe82c71d0 | -11.0847 | -45.28675 | 2025-06-27 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c3bc6dc-e2be-3b55-bc0f-4f481e40ed06 | -9.07372 | -49.43614 | 2025-06-27 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2d1bb13-2121-36bd-9d0a-174d0cdc2dc2 | -13.94168 | -54.48947 | 2025-06-27 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 945aabd8-2201-3423-82e5-a6ecc331a884 | -10.295 | -57.13863 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7e15cef-afc7-3cf3-b79e-48f54a3776d4 | -10.88089 | -47.58379 | 2025-06-27 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e306216e-971a-3d9a-a3d3-5ca072491686 | -10.30259 | -57.12804 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fb9cf698-aa54-3794-857e-76b61266429a | -12.89639 | -43.79377 | 2025-06-27 04:21:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3570247-40a5-387a-b524-e134ed4b951c | -11.83814 | -43.79905 | 2025-06-27 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 32623c0f-fbd9-3320-994f-4f5551541dbd | -11.77505 | -55.03795 | 2025-06-27 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c738753d-f664-3875-8d60-174dc9d916dd | -10.65289 | -44.49155 | 2025-06-27 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 0d6553fc-d3ca-38ee-927f-379bb31d0ddc | -11.57058 | -52.11702 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| a5ef2614-8c08-38a9-85ab-362d952af6e6 | -9.82466 | -48.381 | 2025-06-27 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README12.md)
