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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d46cec1a-d077-3446-a7d3-ba5b4cadcedc | -3.5407 | -48.1673 | 2026-08-25 06:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| c26ce40f-f16f-3ea8-b59d-25b4b2495b96 | -3.5406 | -48.1889 | 2026-08-25 06:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 1ea5b123-dbc1-387c-923e-be080f38aba3 | -6.9873 | -59.2389 | 2026-08-25 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 5ff3203d-bf03-3b7d-91ea-1c3a7f74f0f5 | -6.9872 | -59.2582 | 2026-08-25 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| ebbf56f1-85ec-3641-93e5-497f00f4d657 | -7.0057 | -59.2575 | 2026-08-25 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.1 |
| cb1bbcc0-cad1-3c04-bb07-52db481842db | -7.0058 | -59.2382 | 2026-08-25 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 52ebe9ca-8720-340b-b193-5673667a472b | -3.5221 | -48.1896 | 2026-08-25 06:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| e02a06e1-2b6b-3ea7-8cca-1105103429c7 | -3.5407 | -48.1673 | 2026-08-25 06:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 060f0e99-3e3b-3ca4-8c72-1a2e5bcc35e1 | -11.1447 | -44.4632 | 2026-08-25 06:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 5d9f3be5-f8ba-3755-bf2c-3ed5dab182bb | -6.9872 | -59.2582 | 2026-08-25 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 170bd3fd-10b5-309f-a793-a3656acaf8f0 | -6.641 | -58.4987 | 2026-08-25 06:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| ed4c0c4b-fd9f-38ac-9ee9-b39eae13e883 | -3.5406 | -48.1889 | 2026-08-25 06:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| ee86b4b3-d8fd-3b72-8eaf-6a720d6ec807 | -7.2903 | -45.3456 | 2026-08-25 06:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 5c95e77d-afc3-3c8e-8285-81035c927542 | -7.0057 | -59.2575 | 2026-08-25 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 5b93394d-ff21-3c22-8f2b-223719dac4ec | -7.2901 | -45.3683 | 2026-08-25 06:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 1e85ea3b-e006-31d0-997c-b28f09e22e6a | -6.9873 | -59.2389 | 2026-08-25 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 71a01fea-217c-3ede-ab2c-fd6e56cba10c | -7.2901 | -45.3683 | 2026-08-25 06:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 3528dd07-8ebc-3072-9225-40d1dde91e4a | -6.9873 | -59.2389 | 2026-08-25 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| ddec5ac5-a37c-3438-b862-970c51c48f93 | -3.5406 | -48.1889 | 2026-08-25 06:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 07e0326d-3669-3dcd-877f-2119e039e348 | -3.5221 | -48.1896 | 2026-08-25 06:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 489dd7cd-e60c-3f5e-8977-b060a3fcda4d | -7.0058 | -59.2382 | 2026-08-25 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| ee1cae6d-2b5c-3935-b5a1-e5d58a60049f | -3.5407 | -48.1673 | 2026-08-25 06:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 5041e687-d569-3129-adfa-c0efaa75612b | -6.641 | -58.4987 | 2026-08-25 06:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| f214ceb3-83cc-3b05-94ca-4a24aa94b9f5 | -7.0057 | -59.2575 | 2026-08-25 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 10d5f044-73d9-3f26-a84f-3d0926819e6a | -6.9872 | -59.2582 | 2026-08-25 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| cddac942-d019-37b8-9192-7a7f152904b6 | -3.5406 | -48.1889 | 2026-08-25 06:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 94b1512e-f024-3bc0-bcf1-73792a7e5652 | -7.0057 | -59.2575 | 2026-08-25 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 1ba4b92d-08c3-3661-8102-d23c6db85481 | -3.5221 | -48.1896 | 2026-08-25 06:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 767e45d4-2828-3203-8a1e-4a23c4397f9b | -7.2901 | -45.3683 | 2026-08-25 06:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| b3a309f3-8e6f-324b-a728-b6b383d6a604 | -7.0058 | -59.2382 | 2026-08-25 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| ba401173-98be-3476-8894-e8001f969078 | -3.5407 | -48.1673 | 2026-08-25 06:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| ea40a053-fb90-313c-9e5e-883b398fd81a | -6.9872 | -59.2582 | 2026-08-25 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 2d2bc49f-ac8e-3cc4-b66b-e5c1417d53bc | -6.9873 | -59.2389 | 2026-08-25 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 9d80f3e0-74d4-3861-9baa-257324fe652b | -7.2901 | -45.3683 | 2026-08-25 07:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| a420969a-2439-30a4-9392-6d1bf6d7c69d | -6.641 | -58.4987 | 2026-08-25 07:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| b6a5e284-2773-3346-87b8-a57421d3edf3 | -6.9872 | -59.2582 | 2026-08-25 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 55b88caa-c3c9-3e28-8125-c79451998096 | -3.5406 | -48.1889 | 2026-08-25 07:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 77735fd0-1a67-33b2-bb68-0b3d88b3d41c | -3.5407 | -48.1673 | 2026-08-25 07:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 5c1b9df5-ea72-3a59-a10b-19caddd6164e | -7.0057 | -59.2575 | 2026-08-25 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| de7f70a0-6d94-30e6-83d9-7531288e3832 | -3.5407 | -48.1673 | 2026-08-25 07:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| cb04b433-77ef-37b5-8a12-462902ed1db4 | -7.2901 | -45.3683 | 2026-08-25 07:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 865251e1-4357-3a6a-ac9b-6f1e52a1b68c | -3.5406 | -48.1889 | 2026-08-25 07:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 0bc43d71-1f63-3d0c-a22e-eb3ccc973384 | -7.0057 | -59.2575 | 2026-08-25 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| cf5b2944-2304-3bd6-b008-d246490cd34e | -6.9872 | -59.2582 | 2026-08-25 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 2cbb3f01-dec7-3bb9-ab70-ec380e1761ee | -13.3595 | -48.2051 | 2026-08-25 07:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 68.6 |
| bdaa7f8f-9c95-319a-aece-1f9732bcb8be | -13.3595 | -48.2051 | 2026-08-25 07:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 165.2 |
| ce663923-b5d7-31ac-aefb-1f66a654689b | -13.3599 | -48.1828 | 2026-08-25 07:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| ad8e2a73-2ed1-389d-87fa-57a84eb3a09e | -7.0057 | -59.2575 | 2026-08-25 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 0a1d1ed7-a0b6-303d-a83d-74b9e1353064 | -3.5407 | -48.1673 | 2026-08-25 07:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 2c03b8bd-fa36-32b6-a060-55e8df16b6a6 | -3.5406 | -48.1889 | 2026-08-25 07:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| b14240c7-452a-3ff6-8484-b4476ba909e4 | -10.8608 | -50.5412 | 2026-08-25 07:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 81338571-9fc5-3008-8fe7-a10230c6cd0c | -7.2901 | -45.3683 | 2026-08-25 07:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 1d8a02b1-6d33-32a2-872d-d22ced17b501 | -6.641 | -58.4987 | 2026-08-25 07:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 9325f677-a354-3b7e-9479-cf1f27a82fd4 | -7.2903 | -45.3456 | 2026-08-25 07:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 47.5 |
| f8622fd6-e133-30ba-8b80-898b8f8a19bb | -13.3402 | -48.2079 | 2026-08-25 07:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 62c6e005-471c-398e-ab64-473ecc9767e7 | -6.9872 | -59.2582 | 2026-08-25 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| d77fc4a5-a49c-3feb-8ffc-998d9decaa29 | -3.5406 | -48.1889 | 2026-08-25 07:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| de9d89aa-ed5b-357f-b0e5-3878c67c67fc | -7.0057 | -59.2575 | 2026-08-25 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 3128d4b5-c173-3909-8ebc-368dd83fbe68 | -6.9872 | -59.2582 | 2026-08-25 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| f4aaac23-f1ea-37b9-b8ca-359cbcdd1fac | -10.5814 | -46.3016 | 2026-08-25 07:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 99883f8d-9805-3dce-ac29-88cedb399de0 | -10.581 | -46.3242 | 2026-08-25 07:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 641bb712-0e3c-3601-b61a-13fca98b1933 | -3.5407 | -48.1673 | 2026-08-25 07:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 2192a2d5-3a70-390d-95d4-b20fe648179b | -13.3595 | -48.2051 | 2026-08-25 07:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 2aae8308-004d-3756-b6ba-0e5dbcef8f44 | -3.5406 | -48.1889 | 2026-08-25 07:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 012fc05d-632d-373a-aef3-e4f6d82ae550 | -7.8985 | -46.37 | 2026-08-25 07:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| b6196bb1-79be-305c-8e64-fa037064a9a1 | -13.3595 | -48.2051 | 2026-08-25 07:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 3e5b2f52-2500-3ae3-b4f5-744f192d1ffb | -13.3402 | -48.2079 | 2026-08-25 07:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 7f8f434a-7833-3dea-a72f-9b3d72bc315d | -3.5407 | -48.1673 | 2026-08-25 07:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 27376d10-0522-3916-b3ca-e5738856f72c | -7.2901 | -45.3683 | 2026-08-25 07:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 07dfbdf0-7f68-3f91-a16a-5038ef8cb8da | -7.0057 | -59.2575 | 2026-08-25 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| ca2a735e-6d28-3284-940f-342802fa60ac | -6.9872 | -59.2582 | 2026-08-25 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 6de0c239-dc4d-323f-847f-5dd414d1588e | -7.8988 | -46.3477 | 2026-08-25 07:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 7e7594bc-47d6-3c88-a90c-79a0b9ea1391 | -13.3402 | -48.2079 | 2026-08-25 07:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 3194054e-2368-36e1-88f4-1893942bc8ae | -13.3595 | -48.2051 | 2026-08-25 07:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| f1c68d79-15ae-38e1-97bf-2ed575df0d41 | -6.9872 | -59.2582 | 2026-08-25 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| cf07695f-4bec-3cf7-a8d3-f09be02bb4c7 | -7.8985 | -46.37 | 2026-08-25 07:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 5502e03b-cdce-3e6c-9745-2a0d3875c8cf | -3.5406 | -48.1889 | 2026-08-25 07:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| c50d09ef-da40-3d5e-a55f-d421f376f15d | -3.5407 | -48.1673 | 2026-08-25 07:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 0e9963a8-2d80-3cce-9b52-d8a54d92b9ce | -7.0057 | -59.2575 | 2026-08-25 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 0143c5a7-bcaf-3ff4-9700-470a50038174 | 2.59588 | -60.68833 | 2026-08-25 07:54:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a9402f09-f157-3da1-9e97-3530f6d3c127 | 2.59753 | -60.69303 | 2026-08-25 07:54:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d990f61d-b5b8-3a59-b94c-0a43bac30bad | -7.00529 | -59.23852 | 2026-08-25 07:56:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 37cbf711-75d8-3de4-8e9c-c3763596bfc5 | -6.62523 | -58.49202 | 2026-08-25 07:56:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 4c9ad7a8-5036-3075-89ab-c758e12ee466 | -6.63905 | -58.49395 | 2026-08-25 07:56:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 14f5ee0c-c5bb-367c-9aa2-a6d280918233 | -7.53539 | -61.36193 | 2026-08-25 07:56:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 17d5427c-b93e-341e-a0af-d6577ef0b76b | -7.20105 | -60.60869 | 2026-08-25 07:56:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 2defa129-94a9-36a8-bf9e-73b0c4850d55 | -7.54536 | -61.35785 | 2026-08-25 07:56:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5d6a60a1-c92e-3262-936f-19b62e7714e5 | -8.81443 | -62.33153 | 2026-08-25 07:56:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b3c9e7c1-99bb-3818-8094-9e93de4513e5 | -6.63189 | -58.49822 | 2026-08-25 07:56:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 1bb6b2a2-9be3-32f1-bd23-e18b72b0a4c4 | -6.99224 | -59.23641 | 2026-08-25 07:56:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 57f049c2-f25e-3781-8ad8-1f66ccf41f67 | -7.00252 | -59.25952 | 2026-08-25 07:56:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| ced18a1b-c4fa-3cb5-952f-c2018d1fd966 | -6.635 | -58.4743 | 2026-08-25 07:56:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 3971fb60-f387-370e-95c5-1862f891c25c | -6.98945 | -59.25769 | 2026-08-25 07:56:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 76564f0e-5383-3138-9815-eb7326675bff | -6.99255 | -59.25076 | 2026-08-25 07:56:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 6f0bf02c-9796-3dcd-91d6-0438a0ee9934 | -7.00561 | -59.25267 | 2026-08-25 07:56:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 4a8d34fd-5a98-34f8-a489-78690cdc3f7e | -7.21277 | -60.61037 | 2026-08-25 07:56:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| a6009881-8bd8-3461-9ae5-f668c18c66ed | -10.89733 | -61.88269 | 2026-08-25 07:58:00 | AQUA_M-M | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 8c32d8b1-c460-3252-a99a-c378e665c093 | -10.5623 | -46.304 | 2026-08-25 08:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 67679755-4dad-36d2-9a1f-21360dd66603 | -13.3591 | -48.2273 | 2026-08-25 08:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 297dbc03-f2ae-32da-aa4d-d4aef1f29df5 | -15.3049 | -52.8058 | 2026-08-25 08:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 102.7 |


[Clique aqui para ver as próximas entradas](README69.md)
