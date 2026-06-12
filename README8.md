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
| 9c5fab12-0fb5-3c72-a0ac-3700e0cfb68a | -12.14994 | -48.45624 | 2026-06-12 04:59:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 993cd424-027a-3890-b6a6-bec03516f475 | -11.45444 | -55.90265 | 2026-06-12 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| feb95e8b-ce34-38c4-b8da-8ed8aeabf504 | -12.35057 | -47.89888 | 2026-06-12 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b370028b-532f-3569-8200-e50fb6182795 | -11.05072 | -56.93075 | 2026-06-12 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa4f20be-e72d-3942-b46a-ec9e6947d034 | -10.82933 | -53.72424 | 2026-06-12 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92d7addd-ae8e-386a-99ef-5ee410567354 | -13.46104 | -55.75828 | 2026-06-12 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| accb4fb2-6ab9-3adf-846e-025dacb6a800 | -11.05012 | -56.93447 | 2026-06-12 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52c9b79d-1f51-3e10-9ddc-b094db0913d0 | -12.42497 | -58.48271 | 2026-06-12 04:59:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 68a7d935-b7f3-34ee-bb73-fb1191277fbc | -12.86432 | -44.36617 | 2026-06-12 04:59:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| bc769a57-ace4-3df9-833b-c84f6942c7dd | -10.57465 | -57.32695 | 2026-06-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a0eb6cf-da06-3227-b000-cfdf263a6d94 | -11.57207 | -54.58157 | 2026-06-12 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b74dcf2-3b02-35db-8fc2-517bf5fd646f | -11.57795 | -47.44945 | 2026-06-12 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44a36a3e-a2bc-31af-b473-d2ab341d745a | -11.57724 | -47.45501 | 2026-06-12 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dad3cb4d-40c7-3ac9-b834-01129bb7f559 | -11.45113 | -55.90211 | 2026-06-12 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5701b17-c9ec-3176-b24d-4f614fd22e3c | -11.62884 | -55.17988 | 2026-06-12 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abed43d3-a701-32e4-9193-d2ddc6115459 | -11.62445 | -55.18635 | 2026-06-12 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c5610b2-07d1-3eee-9d67-714a46057c16 | -11.62391 | -55.18985 | 2026-06-12 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b752e4c-6b62-3efd-82a1-18d5ac4c022a | -10.6252 | -53.90585 | 2026-06-12 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ca1ea98b-d349-3cee-aa60-36b967c08656 | -11.90252 | -57.7818 | 2026-06-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75bd8fcb-2035-32f5-b458-82d863d9671b | -13.45609 | -55.74663 | 2026-06-12 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2db9ced9-f4f0-3698-a499-550a28136f44 | -10.57119 | -57.32636 | 2026-06-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dda59e91-5500-3a7a-942c-1ac07f3852c5 | -12.42854 | -58.48332 | 2026-06-12 04:59:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e641e79c-4103-3e2c-b684-e08cdd095e07 | -12.47596 | -45.44573 | 2026-06-12 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea5afd61-496b-3aee-a2fb-7695800a6032 | -10.83665 | -53.74389 | 2026-06-12 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 084cde6c-6f6d-3751-9d98-e31126f27916 | -12.86382 | -44.37077 | 2026-06-12 04:59:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 3618a994-5ab4-3da1-92a3-825a00bb5c2f | -12.80041 | -54.86368 | 2026-06-12 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| efee7a10-3adb-31f5-a510-6f5b5a9cff85 | -11.62224 | -55.17883 | 2026-06-12 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c0aac70-16e1-347d-b4d7-719d6ba40690 | -13.45884 | -55.75069 | 2026-06-12 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e674268-1f18-3d0d-8075-bb10347bca4f | -11.62554 | -55.17936 | 2026-06-12 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ab9da73-6fdd-35fc-ae80-969081908649 | -10.04148 | -54.58242 | 2026-06-12 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5f22951-bdd6-3f16-beb6-7ec69ed5d049 | -13.45829 | -55.75422 | 2026-06-12 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| df1cf9e5-195e-37e3-948b-8d0cacb5af13 | -10.83659 | -53.72168 | 2026-06-12 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 187688af-e2e2-3722-898b-83dbb1fbe662 | -11.0078 | -55.0868 | 2026-06-12 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3727441-db47-3091-861e-ec64ecc1c85e | -10.82422 | -58.01839 | 2026-06-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79b589b9-3698-363e-8618-bd8479d9e5bd | -11.45225 | -55.89506 | 2026-06-12 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0ca4efc-f797-3636-a09f-afa274f1ade9 | -13.46159 | -55.75475 | 2026-06-12 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f21cff1-c6e1-3844-8e59-cbd24f23d190 | -12.8548 | -44.3625 | 2026-06-12 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| d6ef6b2f-0f93-3388-ab35-be090a4c7857 | -17.46492 | -55.20504 | 2026-06-12 05:01:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bfb24705-cf8f-39e5-925f-6a22fbbc3ec6 | -16.12378 | -58.49852 | 2026-06-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f98430fb-0f8b-3147-a81e-3ec5a7e33d96 | -16.60081 | -58.23371 | 2026-06-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 70a07865-73b1-34e8-aa1e-58bf4cf1f39d | -16.59742 | -58.23311 | 2026-06-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5779183a-c603-3515-b079-b98c017d7ce8 | -18.46299 | -54.70458 | 2026-06-12 05:01:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b0e20cc-d6fb-392d-9193-838f2c00fa5a | -16.12721 | -58.49911 | 2026-06-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 94a428a5-c551-3b89-bc4a-dfc7083ffd1c | -16.60144 | -58.2299 | 2026-06-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 3b7dbc29-ec5b-3bf7-b541-7336429e5e28 | -20.88963 | -47.94405 | 2026-06-12 05:01:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02345087-f018-3dac-bd6b-9f909f483394 | -16.60483 | -58.2305 | 2026-06-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e0cf65d5-d583-3dae-8021-dfdc200b341c | -20.88899 | -47.94128 | 2026-06-12 05:01:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59313907-8ae1-370a-aa1c-4afbdc983074 | -20.88867 | -47.94457 | 2026-06-12 05:01:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e693d9e8-2259-309f-b866-72547dd3c0c8 | -12.8548 | -44.3625 | 2026-06-12 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| b5d883b3-2bae-3bc6-89fb-cf02885432e2 | -7.35035 | -47.01285 | 2026-06-12 05:31:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0212511a-a764-3951-a679-2ada5dc3680e | -3.50839 | -48.04029 | 2026-06-12 05:31:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1ecf7f36-36d3-32d6-ac71-b0a750601dab | -3.50192 | -48.03926 | 2026-06-12 05:31:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| db2845ac-625c-3ecd-ba10-05ea30460c7e | -6.56819 | -47.9143 | 2026-06-12 05:31:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 279d605f-c471-3872-8879-23ac7f75bcf6 | -6.5675 | -47.91956 | 2026-06-12 05:31:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 867e28ee-9bc4-3ab7-8815-f74dfb70399d | -6.56629 | -47.91678 | 2026-06-12 05:31:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00509fe3-bfc9-3e8c-9a8a-9d5e50c922fe | -7.34937 | -47.02047 | 2026-06-12 05:31:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 636366e8-b77a-3cb6-9185-84227a692dda | -6.575 | -47.91526 | 2026-06-12 05:31:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4e9106d-cafc-391e-95a4-fc25a5aa4509 | -3.50824 | -48.03564 | 2026-06-12 05:31:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b156bb9-cfb7-3a0f-871f-245cd96d3e60 | -6.58066 | -47.91321 | 2026-06-12 05:31:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fc18f6e-e2d0-3120-9014-c1548b03bd37 | -6.5731 | -47.91773 | 2026-06-12 05:31:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d40dacac-7568-389d-b7eb-9e0569d4d5c2 | -3.5075 | -48.04068 | 2026-06-12 05:31:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1b322d5-360b-3a76-afe4-c13ae86a9466 | -3.50103 | -48.03961 | 2026-06-12 05:31:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a19843d-8c7f-397e-872a-558362d3118d | -6.5818 | -47.91625 | 2026-06-12 05:31:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c348c614-cacb-3c9f-b1a8-2f4e8c4ee18f | -9.20606 | -47.91603 | 2026-06-12 05:33:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 575ba99b-0c8f-3849-8c57-f9080f3f3ae4 | -8.1516 | -47.54357 | 2026-06-12 05:33:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 485f85c0-c670-300c-8068-46eb98e494a8 | -12.43021 | -58.48029 | 2026-06-12 05:33:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c8d76adb-26b9-355c-9c99-783355a23516 | -12.30178 | -57.40401 | 2026-06-12 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a56e667f-e90a-3393-9b84-ae8c42b1e51b | -11.44812 | -55.90019 | 2026-06-12 05:33:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d28a7547-e035-3e78-bf08-91e89b43b426 | -9.21149 | -48.58192 | 2026-06-12 05:33:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb23b5c7-df1b-3eaa-bd57-41648410b8cf | -11.62197 | -55.18282 | 2026-06-12 05:33:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4c03bd8-48a7-3801-8ee8-e5646c28d86b | -12.42583 | -58.48424 | 2026-06-12 05:33:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7feaf6a9-840e-3c03-92c6-be76bbc1b472 | -9.21224 | -47.92356 | 2026-06-12 05:33:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c7fd199-4184-3069-a763-5108931f4fb3 | -11.44757 | -55.90428 | 2026-06-12 05:33:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3884b8ce-bb8d-3d19-980e-ed8bbf54fe33 | -8.15868 | -47.54469 | 2026-06-12 05:33:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| af358946-1aca-32df-b4b6-68e26a3b0252 | -8.15624 | -47.53933 | 2026-06-12 05:33:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 287c0839-22f4-3c7d-9c4f-d4a4863d42d5 | -12.42211 | -58.48367 | 2026-06-12 05:33:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b01f4c6-88f6-3e2f-882d-f948d373581b | -11.62588 | -55.18808 | 2026-06-12 05:33:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b939db9c-e607-3f4b-adf0-976195d55e61 | -8.15534 | -47.54633 | 2026-06-12 05:33:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| cb344c03-4c27-3107-9313-ab93d7bb9176 | -9.69778 | -47.69827 | 2026-06-12 05:33:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b175f8e0-5bbe-382d-800a-36ef13ca3940 | -9.31067 | -48.97585 | 2026-06-12 05:33:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5628918d-acd4-3ddb-bbad-e7a6a0e29978 | -12.29782 | -57.40346 | 2026-06-12 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9af4af06-5d97-300b-bb46-33b4fb81a9f0 | -10.8394 | -53.74841 | 2026-06-12 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7e33352d-a8c9-3809-8a7d-7c27cb2d8c3b | -12.41839 | -58.48309 | 2026-06-12 05:33:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c87a5e0f-621f-3718-a197-a5c9981a0f8b | -11.48679 | -52.91705 | 2026-06-12 05:33:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c25a5244-5a20-3301-a623-450309aa4df3 | -12.54748 | -57.19697 | 2026-06-12 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3cca7b7-c784-31a0-9534-84430b5a26a0 | -9.21823 | -48.58297 | 2026-06-12 05:33:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c7396be-2cab-33d5-b277-8f900af6938f | -12.8025 | -54.86547 | 2026-06-12 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4c586e34-9c2e-3c2f-8848-847755ef43bd | -11.45298 | -55.89674 | 2026-06-12 05:33:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 844d000d-086d-3065-a174-a9c2e95aacd8 | -8.15246 | -47.53654 | 2026-06-12 05:33:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2b04d7cf-0896-3fac-9ce3-25f3df27dcf7 | -11.62651 | -55.18346 | 2026-06-12 05:33:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01ebb0f2-4692-3012-b6b2-90a95fa91f2c | -12.42649 | -58.47972 | 2026-06-12 05:33:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d110b313-6f1b-3f70-9732-7ca8d8c3eb65 | -10.84016 | -53.74273 | 2026-06-12 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3720059d-b666-3e71-8db9-612d2fceb497 | -11.62134 | -55.18745 | 2026-06-12 05:33:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa465674-e7aa-31a8-a10c-bea65fab6ba7 | -12.80184 | -54.87052 | 2026-06-12 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d88be1ad-72f0-3364-90ff-326229cc34fa | -12.42715 | -58.47517 | 2026-06-12 05:33:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 325837a2-1eef-3a93-ad90-0282f4f6b495 | -10.8995 | -54.1353 | 2026-06-12 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7998e1a-af54-3b5b-a911-a488e787cbd1 | -12.55199 | -57.19398 | 2026-06-12 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0da80a5-2346-3213-b7c7-b75b75045dc8 | -11.73892 | -54.79202 | 2026-06-12 05:33:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b99aacfe-6f5a-32ce-a393-ffc2143232a1 | -12.30104 | -57.4001 | 2026-06-12 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 62d85e8b-9d43-3276-a420-f6026368fbde | -10.90432 | -54.136 | 2026-06-12 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README9.md)
