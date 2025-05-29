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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9507168-bd42-3124-a74d-6e3db6b8402a | -10.95584 | -48.15749 | 2025-05-29 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 21f226e1-9805-32f6-9aa2-2f71caef3a28 | -10.82764 | -54.02967 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b62a7032-a757-3bef-b097-d0766d93c6e3 | -11.80311 | -55.07484 | 2025-05-29 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffb32830-f8ca-3dae-9532-253148328833 | -11.46439 | -48.15941 | 2025-05-29 05:06:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 300210f2-5598-3dd5-a5c6-35a39d726049 | -11.80025 | -55.07055 | 2025-05-29 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56b68f78-a124-3e2d-ab31-89f38835c5b2 | -12.42735 | -53.32011 | 2025-05-29 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 945a071f-b1a3-3271-8da9-ccb27d970e33 | -10.8241 | -54.02913 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46d135f2-03ba-3ed1-b1c8-7989d3c6ab7f | -10.94065 | -55.32896 | 2025-05-29 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e17c12a7-bbf0-306b-b664-2d5b94803422 | -11.80709 | -55.07161 | 2025-05-29 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88c014a7-827a-3926-9cbf-8d1a965649df | -10.71929 | -49.54586 | 2025-05-29 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79882fe9-a1dc-3363-ba47-197be1ee969f | -10.73413 | -49.29527 | 2025-05-29 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0aa43450-9d9d-302b-b125-725a791c6c17 | -11.81472 | -44.27045 | 2025-05-29 05:06:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d134c47a-719d-3b0f-a79b-6705bdefb05b | -11.91923 | -51.0953 | 2025-05-29 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c649951-545b-3059-98a2-5677f3cc194d | -12.2805 | -49.53403 | 2025-05-29 05:06:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04b889dc-f15c-3734-bb97-fd890ac0e492 | -10.83584 | -54.04734 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fecd06c5-6253-31db-af65-6d22bd58137f | -12.343 | -53.2587 | 2025-05-29 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc677955-169f-39a8-9fbf-d6f75dc7739e | -10.81523 | -54.04015 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ef0512d-01aa-3f9d-a2e7-86ca0d5697f6 | -12.3193 | -49.99117 | 2025-05-29 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ca60250e-afea-36e1-9b9d-31cecda89307 | -14.20667 | -47.72617 | 2025-05-29 05:06:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5f75fb76-9f5b-3f3c-8469-eb3265445065 | -10.79895 | -55.87761 | 2025-05-29 05:06:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c0344c1-8b7c-3d32-ad7a-39c53f9c05d2 | -11.90478 | -54.79343 | 2025-05-29 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 25fb14ff-3d82-303d-a79f-8e10b3c72b84 | -11.90882 | -54.7901 | 2025-05-29 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a40db09b-612a-33e3-9b26-9d1d53281335 | -14.21218 | -47.72712 | 2025-05-29 05:06:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cf91ee9e-aaf7-3d25-bd09-795a894b4618 | -10.82877 | -54.04633 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13e31eab-aeca-3cf4-a2c6-f820717d46c8 | -11.14401 | -53.94468 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bf8dd2af-0722-384c-bfbf-3fd8b27fad5c | -10.8223 | -54.04122 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1a18b52-5053-39fe-a902-9a065bb2bd2b | -10.95705 | -48.14801 | 2025-05-29 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7882909-66e0-35a0-b318-8a54fcaf8200 | -10.73006 | -49.2896 | 2025-05-29 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5142b340-e38e-3878-9bdf-703bfed99f16 | -11.07757 | -55.05098 | 2025-05-29 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17191ea5-8a48-3cf0-aa3c-4de4ba917f17 | -11.80995 | -55.07593 | 2025-05-29 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 070540cb-c87a-3bcd-8499-e509dc07128f | -11.97583 | -52.45978 | 2025-05-29 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 02c32423-156b-3142-b0c5-ab167c6fbcbf | -12.41549 | -53.32301 | 2025-05-29 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1fc1a92b-36ff-326b-bf54-88a9e1bb426b | -11.82205 | -44.26542 | 2025-05-29 05:06:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3fb1427e-f880-377f-b77b-14dc25079491 | -13.08883 | -45.28067 | 2025-05-29 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 70e14089-ea16-3d54-8551-dff4e33cd336 | -11.81393 | -55.0727 | 2025-05-29 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef5c94a0-c5fb-3ef6-9b5f-a86ef511a278 | -12.10328 | -51.04816 | 2025-05-29 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f919ec98-edca-377e-95fa-769c4142e3b4 | -10.60421 | -52.84176 | 2025-05-29 05:06:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50d9b97a-698d-3a6e-ae39-fc880d30c8d3 | -12.39145 | -49.97258 | 2025-05-29 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3dfc5534-2ca5-36c4-9714-6601a54c92e7 | -10.96141 | -48.15494 | 2025-05-29 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0e601536-0400-358d-8222-70f798ce81ed | -10.73648 | -49.28583 | 2025-05-29 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8e513a43-e34b-38f7-88c3-b070682689c7 | -11.03965 | -50.77821 | 2025-05-29 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d04afad3-107c-30e7-a208-b129c6653f47 | -11.78413 | -54.77969 | 2025-05-29 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8550a1e-38dc-3437-b96c-f4ed84528d0d | -14.20709 | -47.72252 | 2025-05-29 05:06:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8f4fc398-7a6c-3687-8106-1a7dd6730ad2 | -10.82584 | -54.04174 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d53dbbf-de43-3d89-a543-621398374ae2 | -11.077 | -55.05471 | 2025-05-29 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba71eb29-c80e-3baa-92c0-657f91ddb39c | -10.82938 | -54.04227 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3444f380-2b18-3e3d-9035-c8e68ff63bdd | -14.21261 | -47.72342 | 2025-05-29 05:06:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ef314a02-e58f-34f2-9df4-e2413e3afdbc | -12.32456 | -49.98695 | 2025-05-29 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8c4637d6-ae71-3904-ac47-ffdc8447298d | -10.83609 | -54.04606 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b66e3d5a-8d57-32b6-a2c1-c2464976be87 | -10.82704 | -54.03368 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77e28ad6-ef94-316e-b73c-4d26ed20e7b3 | -10.54011 | -56.38807 | 2025-05-29 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5625a459-b292-3339-8769-cc2bdfd380ec | -10.72939 | -49.29462 | 2025-05-29 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 742fe908-2ae0-301a-b70f-d327f280e122 | -11.97974 | -52.46039 | 2025-05-29 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c14d53b-9307-31ae-80ae-bbbc13f4d8a6 | -12.10931 | -54.66364 | 2025-05-29 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a675d94f-dbc8-3353-ad2d-1692ace722b1 | -12.32393 | -49.99185 | 2025-05-29 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1105db47-3793-3c09-9a61-d9325e25660b | -12.28119 | -49.52868 | 2025-05-29 05:06:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c460124e-21c4-34a1-8a51-357a6633eaae | -11.90536 | -54.78957 | 2025-05-29 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5051c87-4ca5-3e9e-9ea3-058712318bda | -14.61924 | -47.94037 | 2025-05-29 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11f94c69-f907-3dc8-912d-ab54dd32dd00 | -11.79104 | -54.78079 | 2025-05-29 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19d78907-6252-35c3-883d-fa221729ab29 | -11.78471 | -54.77581 | 2025-05-29 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a6c7db1-ff01-3001-8024-28f7e50c8014 | -11.13398 | -53.91367 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f9b0f7c-949f-35c5-90e5-2a6cd8135acb | -11.13929 | -53.92718 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9e7fd46-f78c-3f37-8348-d069d43dd53d | -11.90132 | -54.7929 | 2025-05-29 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af4e03b0-ffeb-3c46-85ca-adfc40841d1b | -10.83938 | -54.04786 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7feb6730-28a2-3199-8dad-9c1ef15d681e | -13.08825 | -45.28597 | 2025-05-29 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3f44c9e4-59b7-394e-b50d-403a5da9a3fd | -11.13694 | -53.91837 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ff3e53a-bf74-3397-8021-2aa1a0c61fcf | -13.6556 | -45.4245 | 2025-05-29 05:06:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a0cdb994-c171-340a-b72a-57684e0f0950 | -13.08131 | -45.29047 | 2025-05-29 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c17d4ae8-e8f4-3f95-ae46-e18e5e27abf6 | -11.14111 | -53.91479 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1dde4c1c-6531-3cd0-a316-a74aa7245f5c | -11.1405 | -53.91893 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe2774c9-a321-37e6-b48c-e4c5f7374426 | -11.80653 | -55.07538 | 2025-05-29 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62c0ce5a-a0c4-316e-88db-19620597bc55 | -12.32856 | -49.99252 | 2025-05-29 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4e4fd73-5bb8-32c0-964e-656d70333a58 | -12.11222 | -54.66811 | 2025-05-29 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a7e30c5-dd76-32f1-af91-430f291af459 | -10.8217 | -54.04529 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 258a1f34-7a4a-351d-8d09-6cb053f78259 | -11.29678 | -53.98565 | 2025-05-29 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e91b325-5705-3471-886d-acce973379b9 | -10.82616 | -56.95211 | 2025-05-29 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8a0ce1f5-9aa4-3234-99e6-70086793f779 | -13.66832 | -45.4261 | 2025-05-29 05:06:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e40d063f-4ff8-3a3f-a61c-23ff465e2c7a | -12.30268 | -47.27247 | 2025-05-29 05:06:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a726ed3f-a584-38da-8be1-2aa90797e6b6 | -11.14462 | -53.94057 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2c62c6ec-b214-31be-a669-0e4496e73780 | -10.72283 | -49.54217 | 2025-05-29 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5ff4a47e-4317-3366-a217-9bc1dc7ff8a3 | -11.03909 | -50.78236 | 2025-05-29 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0bc02cec-c735-37f8-982f-884b2bb81fac | -13.08189 | -45.28516 | 2025-05-29 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9c47dc68-e67b-3f1e-ab81-c27607442615 | -10.80817 | -54.03907 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6fd7269-5514-3b76-9647-83eeebf2367a | -10.73584 | -49.29094 | 2025-05-29 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4b04a2c5-c85e-3d1b-9ce1-8aa547641966 | -11.13815 | -53.9101 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4a51789-8c9e-33ad-996a-031a0d684005 | -10.81703 | -54.02805 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8af66bc-0f14-344f-99f2-8c0570b99dc7 | -12.11628 | -54.6647 | 2025-05-29 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9552f60a-6bd4-3c6d-a120-cc5f9038bb70 | -10.8267 | -56.94862 | 2025-05-29 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5ca8d24-9d71-3ab6-b7e8-259e72d17244 | -10.961 | -48.15813 | 2025-05-29 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9623fed2-97cb-3dce-b47c-4697a0d45138 | -12.1157 | -54.66864 | 2025-05-29 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e21fe14a-ef0d-3109-8fec-79cb34290c1d | -10.3327 | -57.49284 | 2025-05-29 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2f38a40-af77-367f-8a91-f3648558d270 | -10.95624 | -48.15433 | 2025-05-29 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ccfca2e4-5f60-31c6-a9fc-ac2f86ccc458 | -12.30209 | -50.08785 | 2025-05-29 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f057f99-4257-3889-8b7b-942e78f2ce62 | -11.28914 | -46.43584 | 2025-05-29 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2e4b1443-a531-3504-8cb4-6a9fca13a0cd | -12.11164 | -54.67204 | 2025-05-29 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18859dad-6597-3728-bc41-de7d3ae58dff | -13.08768 | -45.29127 | 2025-05-29 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 584b358c-bfa9-3733-9bc2-11eeb16fa783 | -12.38743 | -49.96695 | 2025-05-29 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5dd77f77-9df1-3443-995c-72399e18597b | -12.10873 | -54.66758 | 2025-05-29 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58e916b4-f527-3a6b-b7da-71ea355bffbf | -10.73481 | -49.29023 | 2025-05-29 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4f86abd9-4561-3f5a-83aa-7b77c327d1b4 | -10.73519 | -49.29599 | 2025-05-29 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README16.md)
