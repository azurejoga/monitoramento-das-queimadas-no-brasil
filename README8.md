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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2bb9fa6e-b207-30ae-bec8-ba3935ad5768 | -5.6963 | -47.13611 | 2025-11-07 04:25:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e56d2aa2-3b02-3891-8e58-d40d7c84d29e | -4.45234 | -46.43914 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 77c1e642-575f-3eee-bf11-6848a1f46305 | -5.65361 | -46.5906 | 2025-11-07 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d5b4fc5-751c-3a9d-b3be-8efa94c2b02e | -4.48656 | -55.80058 | 2025-11-07 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59aa6366-969c-3019-8cca-fd9bf1605ad5 | -5.09722 | -44.79567 | 2025-11-07 04:25:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5bf6f51f-d475-31d3-8e1b-ab6bc4ea3826 | -9.05798 | -48.83913 | 2025-11-07 04:25:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1fe0c693-ff2a-3752-a0d7-14a90e3e7c3c | -4.91815 | -44.10749 | 2025-11-07 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 058b2e04-cf1b-3aab-bc45-a0a1d78ad984 | -5.44524 | -46.35842 | 2025-11-07 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec018f57-9104-3b8d-8d8b-cd143217c5df | -6.17895 | -39.94035 | 2025-11-07 04:25:00 | NOAA-21 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7dc60e20-67a1-393e-92e3-3cf6777b872f | -4.75174 | -49.74961 | 2025-11-07 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9578876e-555e-39c1-963f-d87f523b159c | -7.98867 | -46.8033 | 2025-11-07 04:25:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d10b6025-3780-3028-9e5b-4841e9b4c51a | -6.74107 | -39.65525 | 2025-11-07 04:25:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d37e3890-49fc-3c40-a644-b649ffc61ba8 | -3.77727 | -50.03868 | 2025-11-07 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bf5d52be-82b3-3261-98a2-fd682aee9918 | -4.39815 | -46.43784 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b71cb09b-a24d-3ea3-b85d-adcf0990c6bf | -4.67066 | -46.30673 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 60c9f6b7-d8cf-387e-82ca-116909fc7f7b | -6.74047 | -39.6595 | 2025-11-07 04:25:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3ecd404b-3795-383a-9afd-7740a76e8545 | -3.34896 | -53.22321 | 2025-11-07 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| bf4744a9-40da-3105-8ec0-84bd32c75adc | -5.44193 | -46.3579 | 2025-11-07 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dfcf18f-23cf-39b2-8584-2e5058291ede | -3.52124 | -52.89418 | 2025-11-07 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 789520c8-21bc-3b8f-a7ef-768fad45ec77 | 1.36788 | -50.71941 | 2025-11-07 04:25:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a462584a-975f-3b30-8c20-50d9f3b0e34c | -4.67397 | -46.30725 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6e740fed-ecaf-3b5d-afba-1ccd68d3bc7a | -5.63499 | -43.25711 | 2025-11-07 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1bc0172-fabd-35aa-8cfb-46bfbd11f822 | -6.12017 | -41.61515 | 2025-11-07 04:25:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 3ac8f087-7c02-3a8d-99e7-ae75ec78d478 | -6.65364 | -44.48536 | 2025-11-07 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9464b488-e8e0-3290-af44-20a4a9fe04e6 | -6.42722 | -44.68046 | 2025-11-07 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f265c735-4412-3796-8a77-36b2219ffd40 | -4.44682 | -45.69597 | 2025-11-07 04:25:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab1eae37-887b-36a1-8be1-87fe43c8dbc3 | -5.28 | -47.16489 | 2025-11-07 04:25:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b7095218-6e2c-39ac-95ec-0730e19a397d | -6.63162 | -39.50428 | 2025-11-07 04:25:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f254f58c-82eb-37bf-9dab-d08416b460e1 | -5.11758 | -45.88644 | 2025-11-07 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f89ee5c8-5bea-3ed8-8877-66709ecaf551 | -4.45344 | -46.43215 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c14f6771-4063-3377-ab6c-cba7db13d98b | -4.67121 | -46.30326 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 16181239-d856-3f64-8055-4e01ec5b55ae | -4.49224 | -55.80153 | 2025-11-07 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48f0c41a-465a-3928-b8ec-c3e7ec98f2e4 | -6.88414 | -42.8559 | 2025-11-07 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 38b507da-e428-3fae-ad5e-6b56b1e5ccca | -9.00855 | -51.10035 | 2025-11-07 04:25:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b01aa51-3092-3333-80b5-6a4aecd64165 | -5.6161 | -45.04776 | 2025-11-07 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f411628-0ef0-3568-9954-ff65aa28978f | -5.77011 | -40.83529 | 2025-11-07 04:25:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 12a71b06-e6c1-3f80-9b4e-5680f13d00cb | -4.11015 | -48.02412 | 2025-11-07 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e047ae74-e171-31a2-8caa-fab2c9e79597 | -7.7441 | -42.26475 | 2025-11-07 04:25:00 | NOAA-21 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 90236fb2-653e-3bcb-93c6-27934abac637 | -4.63004 | -46.54243 | 2025-11-07 04:25:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee4c9578-c787-3c09-bd23-c115fa1df490 | -4.5941 | -45.9943 | 2025-11-07 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0cb7d3d9-bc0f-3584-8bc1-826d05ab3774 | 2.55382 | -50.99564 | 2025-11-07 04:25:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9314495c-4326-3e6b-958a-c4601c971d60 | -7.38678 | -39.63117 | 2025-11-07 04:25:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 21ebb92a-fa99-3153-b545-cc5283f0e784 | -4.31318 | -48.07122 | 2025-11-07 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5becce70-936e-303a-a86a-c6600d045e00 | -7.74352 | -42.26645 | 2025-11-07 04:25:00 | NOAA-21 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cde399d4-33be-372c-9e18-38f9f6cb1d91 | -6.83846 | -39.42151 | 2025-11-07 04:25:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3f384991-6ddd-3ee0-83d0-5a42b87dd876 | -5.75928 | -40.7968 | 2025-11-07 04:25:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 938253d1-b9cf-3c1f-b591-3f41fc9b39cb | -4.63878 | -45.40213 | 2025-11-07 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d2d7ad3-efd9-39bf-9f7a-60569d5690cc | -4.91532 | -44.10336 | 2025-11-07 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13d9e06c-1a4b-3449-80de-5f22bd3917d0 | -4.73501 | -45.37534 | 2025-11-07 04:25:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 751121c1-bf6c-3c4c-bad7-66a81ec22385 | -8.05193 | -49.63663 | 2025-11-07 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f76fad10-ddf1-3b2b-b7e0-faa45f19fdb8 | -5.80047 | -44.51168 | 2025-11-07 04:25:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 167b718d-584e-34f3-8308-b718c61ae9c6 | -7.14135 | -40.46151 | 2025-11-07 04:25:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0d84b738-7815-3b57-8761-7391a6e4947f | -5.07321 | -45.75978 | 2025-11-07 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64bdc430-43d4-34e5-9e82-37ce4e7cce47 | -9.44147 | -59.20952 | 2025-11-07 04:25:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 60f505b9-b196-31bf-a301-5d9c920ca15d | -4.41086 | -45.62355 | 2025-11-07 04:25:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 858c129a-540a-314f-b5a2-1eeca91c6858 | -12.03578 | -43.96552 | 2025-11-07 04:25:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8dc603b-87d6-3b42-82a0-68b5cd4fbeed | -5.27608 | -47.16792 | 2025-11-07 04:25:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 48544925-6e2d-3f00-ac9f-ef8a7ffe9bd6 | -9.00469 | -51.09967 | 2025-11-07 04:25:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f07841e4-6576-3643-b9c1-f95ff22e8fa5 | -5.75982 | -40.79316 | 2025-11-07 04:25:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 54591e78-2b46-3910-9e4b-0da11432f31a | -4.49369 | -45.13588 | 2025-11-07 04:25:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 53efc3b8-a5ef-3346-8413-d5d7b9dc85d2 | -5.23186 | -45.986 | 2025-11-07 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b6f21c5-d9b4-34a7-8f6e-d8fd3764da73 | -6.64979 | -43.61113 | 2025-11-07 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6fc544ac-7b36-3ba1-ad53-6cafc82c04a6 | -5.76736 | -40.79819 | 2025-11-07 04:25:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 30f740bf-a9cb-3532-9afe-70e535cf6394 | -4.67452 | -46.30378 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 752704e7-e56d-3bcf-896c-149ba8e067b5 | -5.69687 | -47.13256 | 2025-11-07 04:25:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8a1c967-4acb-3b3f-9879-ce8e92681481 | -4.45179 | -46.44262 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e3db50e8-7e0e-3b44-98e7-5bd69952e00f | -6.65235 | -44.48558 | 2025-11-07 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9a17230-f8bb-3861-99b8-f0ccc69a9568 | -5.75121 | -40.79531 | 2025-11-07 04:25:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3ca9ba83-ccd6-35d9-b77b-fb7441cd56f4 | -5.27665 | -47.16437 | 2025-11-07 04:25:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2b9ce005-6e51-39c3-9044-b2aebbd07138 | -4.60609 | -46.43529 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 80d1b83e-3ad6-33d2-a303-3b60fbf5b72f | -5.09002 | -44.79811 | 2025-11-07 04:25:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 647d86b5-6d51-332a-b642-9f24c5691c44 | -9.00387 | -51.10454 | 2025-11-07 04:25:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 019f2011-967e-383e-bf05-7436154d0daf | -6.33296 | -41.69589 | 2025-11-07 04:25:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c3698f51-0473-3171-a2ed-6717a745ab1b | -4.91476 | -44.10698 | 2025-11-07 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0db8f98-cc13-3ec0-97dd-d92e3d6bcccb | -5.24002 | -42.92735 | 2025-11-07 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6b35cef0-966e-368a-b4eb-eb8c3e8a258f | -6.43058 | -44.68095 | 2025-11-07 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06ab8cdc-d69e-3681-a1ec-52775190c954 | -6.58965 | -35.25275 | 2025-11-07 04:25:00 | NOAA-21 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 16629d71-1e3c-3eb7-835c-be71ff74ccb7 | -6.685 | -43.5518 | 2025-11-07 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2eca0761-25d3-3e8d-8cc1-292f298427c1 | -6.55962 | -44.35893 | 2025-11-07 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4429cc86-1ebc-39f1-8cb0-732309dbf1c2 | -8.06747 | -47.12243 | 2025-11-07 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83c0515c-d99b-36f2-9c19-35c57db97716 | -5.19913 | -47.48819 | 2025-11-07 04:25:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63522b72-a81f-353c-98c0-93125a33bd1a | 2.5577 | -50.99028 | 2025-11-07 04:25:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b3f64bf-e185-388e-8fca-256723fa43f8 | -6.12543 | -41.60615 | 2025-11-07 04:25:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6ec76fa9-0cab-3e5d-bfc8-981e9225c597 | -9.91537 | -47.74546 | 2025-11-07 04:25:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fccdf3b7-d89c-38c5-8a8b-43b8706a5b5f | -6.46142 | -44.45615 | 2025-11-07 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ffc37aa-065d-39cd-99d4-1b7d62aa5eae | -5.61664 | -45.04426 | 2025-11-07 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bbbd106-a71f-35c0-99cf-60f0da6ec003 | -5.7507 | -40.79879 | 2025-11-07 04:25:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7b5c4fe2-d2c0-3fbc-abfd-97fc88e2d8a2 | -4.31581 | -55.84822 | 2025-11-07 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d4877a2d-64f4-3f83-9d01-e22e4e9a0b7c | -5.08372 | -46.14553 | 2025-11-07 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7c22f6c-e64b-31b0-a912-4cb9300d7f32 | -5.57929 | -46.30585 | 2025-11-07 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0bd71e1-f6b8-383b-aacf-5e60305fe78b | -5.12415 | -44.88588 | 2025-11-07 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c1406512-1b9b-3618-b553-392b99c25f0b | -10.05897 | -39.42994 | 2025-11-07 04:25:00 | NOAA-21 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 308a9b37-d187-3dea-a143-1f092be53bec | -7.7924 | -40.16886 | 2025-11-07 04:25:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 2fe0627b-8b94-3c60-ad1e-c7f2d0ea3eb1 | -7.51023 | -38.01288 | 2025-11-07 04:25:00 | NOAA-21 | NOVA OLINDA | PARAÍBA | Brasil | 2510204 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6c858bf6-5223-3952-8eea-cee981e9ee1b | -5.09705 | -45.82337 | 2025-11-07 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f266a1f2-5bfe-3e99-b536-78a417a0b817 | -6.45803 | -44.45564 | 2025-11-07 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80e5f8e5-7032-3626-92d7-7ed0e3bfb206 | 2.55629 | -50.98091 | 2025-11-07 04:25:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a766459d-b343-366e-b25e-c7e20a5db5b6 | -5.36542 | -46.15152 | 2025-11-07 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ff3cc86-b2e5-3a0f-a997-e8d33d1f8b47 | -5.26716 | -47.15921 | 2025-11-07 04:25:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 37be8c9f-69bc-3b25-9d9e-45bae3c32342 | -8.01134 | -46.87442 | 2025-11-07 04:25:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README9.md)
