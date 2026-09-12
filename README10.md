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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8ee372e-ca2d-370f-9c0d-9a2f474a32ec | -3.2313 | -46.9596 | 2026-09-12 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 145.6 |
| 33c85ea7-6e5d-39e3-a2a5-515a46805e3e | -5.7569 | -45.084 | 2026-09-12 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 740f6b1d-40eb-3fea-91de-08efd6462a1f | -12.1501 | -64.1414 | 2026-09-12 02:50:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 68.9 |
| fe041456-b061-38d0-b87c-3f54b5d04d3f | -10.7015 | -54.1663 | 2026-09-12 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 52d4f09e-0be8-3984-bfc6-c4c87f242f1b | -3.2314 | -46.9376 | 2026-09-12 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 124.3 |
| e5b15e30-9a22-30bd-a19a-138ebc7638ac | -6.6206 | -58.8483 | 2026-09-12 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| d54dc704-c991-3114-b682-820996166f5b | -5.7567 | -45.1067 | 2026-09-12 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| d706bb08-5a74-3feb-b46e-785609b10e6a | -10.7015 | -54.1663 | 2026-09-12 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 124.4 |
| c9dab522-9ed4-3113-a16e-e0a9562f13e6 | -2.7331 | -57.6271 | 2026-09-12 03:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 5255c35f-6f74-34ba-8224-e654f9bf758f | -5.7756 | -45.0826 | 2026-09-12 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 166.4 |
| b4ed8267-d962-341b-a746-8353838fd191 | -2.7148 | -57.6274 | 2026-09-12 03:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 9e04ba65-3c07-346a-8088-36c7468bc95e | -5.7754 | -45.1053 | 2026-09-12 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 90ef81c9-f4a2-3dca-875f-80d7c32a3331 | -6.2243 | -51.6949 | 2026-09-12 03:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 6a548b5b-20b5-3415-a3a8-c5cc797c7ade | -3.2314 | -46.9376 | 2026-09-12 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 486f65ef-f4b1-3889-8247-dae34e372ca5 | -4.3587 | -47.7853 | 2026-09-12 03:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 715a8cc4-404e-3c14-b8ab-0da3c80aee0d | -2.7331 | -57.6465 | 2026-09-12 03:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 98.5 |
| bfffcc06-cb46-3e11-8567-834cc31650b0 | -3.2313 | -46.9596 | 2026-09-12 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 81bea88f-4bc4-3bfe-917d-64f0f8ba24f1 | -2.7148 | -57.6469 | 2026-09-12 03:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| a3dbebf3-9bf8-375e-96d1-2877cba1db59 | -18.6668 | -41.9962 | 2026-09-12 03:00:00 | GOES-19 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.8 |
| 41d83225-6b19-394d-b6e5-afd3e6b4956b | -5.7567 | -45.1067 | 2026-09-12 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 123.1 |
| bbb40b26-07f6-3e67-8bdf-4a90b68d1fec | -6.2429 | -51.6939 | 2026-09-12 03:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| ecd05102-f0df-3786-8e4e-8908f20d1b45 | -6.6021 | -58.849 | 2026-09-12 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 4ccf9aff-eaa2-3353-91c5-d5e282697b3c | -5.7569 | -45.084 | 2026-09-12 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 1a0cb8b3-171e-3f2b-b7d5-107e5ce70404 | -10.6827 | -54.1679 | 2026-09-12 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 7bfb4b28-9d61-3578-9575-c15710f7d661 | -2.7148 | -57.6274 | 2026-09-12 03:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 68231c5a-deee-394c-9208-f03d50a5a447 | -3.2313 | -46.9596 | 2026-09-12 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| d5970aab-5d53-3f4b-8200-00f14d0a7021 | -10.6829 | -54.1475 | 2026-09-12 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| bf5bfd6b-dedf-3d94-810d-0e283aa349b8 | -10.7015 | -54.1663 | 2026-09-12 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 9f43f15d-26d6-3afe-be40-d7e5ae35a19d | -5.7567 | -45.1067 | 2026-09-12 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| f7d37285-9b4f-34ab-9ea1-5a9896287838 | -5.7756 | -45.0826 | 2026-09-12 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 207.7 |
| d0d43d51-aaef-32f7-9cea-6f78d72affa9 | -5.7569 | -45.084 | 2026-09-12 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 121.4 |
| af18bd38-b0e7-310a-a930-0574f559165e | -2.7148 | -57.6469 | 2026-09-12 03:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 2d6dd944-c4ee-30b8-bc97-accf3e17cacb | -2.7331 | -57.6271 | 2026-09-12 03:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 7a7c05d7-4b85-3570-bbaf-5c143d08cb93 | -2.7331 | -57.6465 | 2026-09-12 03:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 4191dfae-2306-3f36-a84a-da8552c8c0e8 | -6.2429 | -51.6939 | 2026-09-12 03:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| e2aba16d-4593-3e96-a39b-5e0d75e545a8 | -10.6827 | -54.1679 | 2026-09-12 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 1880e32e-8ec2-3053-947b-d78b3668a112 | -3.2314 | -46.9376 | 2026-09-12 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| c8d0d339-eaab-37ec-8dac-a6eb53533176 | -5.7754 | -45.1053 | 2026-09-12 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 8b5b1314-3486-3f52-98a4-740571472e44 | -3.0 | -50.41 | 2026-09-12 03:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93973e0d-1155-3e56-a1af-4c174436d4e3 | -2.94 | -50.4 | 2026-09-12 03:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 306d8cf8-0fbf-3420-9230-e6bcc10799e4 | -18.67 | -42.01 | 2026-09-12 03:15:00 | MSG-03 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 42396aae-4970-3da9-b93e-a30f5928f60a | -2.94 | -50.46 | 2026-09-12 03:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d0c0c12-abfa-33b5-9d2c-2a42bd288f68 | -2.97 | -50.4 | 2026-09-12 03:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f7f9275-aa7e-3524-9684-ffc29238450b | -2.97 | -50.35 | 2026-09-12 03:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1534188b-2b0b-3c68-9e40-cc3c416eb5ac | -5.76 | -45.09 | 2026-09-12 03:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b1d64747-610f-38c2-8dc4-92ba6cc0d63f | -2.97 | -50.46 | 2026-09-12 03:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12c15f85-38fa-3aac-8c92-cc9dd3e229a3 | -5.76 | -45.14 | 2026-09-12 03:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dfc1cdfe-d2df-3e10-a77f-c6871c69b3cf | -2.94 | -50.35 | 2026-09-12 03:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b2291e9-aa68-371a-a66a-7fabfedc9a14 | -2.7148 | -57.6274 | 2026-09-12 03:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 7c7e39f4-51c1-3345-b4f1-09650d53a5f6 | -3.2313 | -46.9596 | 2026-09-12 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 79a54cc7-2397-3403-ab88-c76436452add | -10.6827 | -54.1679 | 2026-09-12 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 08531121-c091-33fb-b0fb-2e941e88bdca | -2.7148 | -57.6469 | 2026-09-12 03:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| c80dee1b-43e9-31b4-ac9b-d5470a95fde0 | -6.2429 | -51.6939 | 2026-09-12 03:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 1bccdd63-dda9-3f6c-ab9c-564af17b6463 | -3.2314 | -46.9376 | 2026-09-12 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 07c13af8-7e28-332b-b2ab-a46a2d0e5273 | -10.7015 | -54.1663 | 2026-09-12 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| bebccf96-3448-3103-a887-d30cb1d7437b | -6.6021 | -58.849 | 2026-09-12 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 7bb3393b-0a28-3eae-a749-fe1d3a3b38a9 | -2.7331 | -57.6271 | 2026-09-12 03:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 2fc1968c-b84d-3840-ba09-df9df50bfb8e | -2.7331 | -57.6465 | 2026-09-12 03:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 114.3 |
| a91db122-9737-3bb1-b6c0-842f95aa2bed | -3.326 | -42.3032 | 2026-09-12 03:28:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3a209b3f-900b-38f9-88c8-11d178fda960 | -6.91617 | -34.92033 | 2026-09-12 03:28:00 | NPP-375D | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1162c833-9b5b-3222-9eb1-e047c568ee05 | -6.91327 | -34.91134 | 2026-09-12 03:28:00 | NPP-375D | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 8ebb3d78-2b58-38aa-af10-c1617bbaa964 | -6.91755 | -34.91209 | 2026-09-12 03:28:00 | NPP-375D | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| d3954b4d-0df4-3072-928c-4836df965bce | -3.33332 | -42.30421 | 2026-09-12 03:28:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f7e78164-16ef-32cf-b54c-fbf5121dd6a2 | -6.91686 | -34.9162 | 2026-09-12 03:28:00 | NPP-375D | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 13892432-eb48-371c-a01d-3610f83d0e67 | -6.91257 | -34.91548 | 2026-09-12 03:28:00 | NPP-375D | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 8603c0f9-f46b-37b9-80ca-b0f03ac3dda1 | -6.6206 | -58.8483 | 2026-09-12 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 9b01efc5-df48-31ed-97e2-dcc344356f78 | -2.7148 | -57.6274 | 2026-09-12 03:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 4a350347-6c47-36b2-b51a-f9695b62f7b9 | -6.6021 | -58.849 | 2026-09-12 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 8cc240b6-e564-3146-af88-62be144faa34 | -2.7331 | -57.6465 | 2026-09-12 03:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 245ebf8a-2346-3980-b051-774b3dc9e983 | -10.7015 | -54.1663 | 2026-09-12 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 85d813d4-ac2e-3ac0-a87e-e37db4472f56 | -10.6827 | -54.1679 | 2026-09-12 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| e998d566-98ba-3fe9-a2cf-ca757d649e46 | -2.7148 | -57.6469 | 2026-09-12 03:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 742c5bab-89ac-3c76-8182-d8435b59e495 | -2.7331 | -57.6271 | 2026-09-12 03:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| c1f9a109-55c6-372c-ad20-0d7303d75229 | -9.51751 | -40.33036 | 2026-09-12 03:30:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 649f445a-c63c-3ed6-9dfe-147d3a8a8f47 | -9.52568 | -40.33792 | 2026-09-12 03:30:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 28.9 |
| a8a67048-da27-3522-b424-67c8ccc6714e | -9.70391 | -43.45916 | 2026-09-12 03:30:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d99e6a17-bbfa-3dd5-a758-cd3c77c57258 | -12.37442 | -39.59177 | 2026-09-12 03:30:00 | NPP-375D | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 89ad2e6c-cd88-36bd-b5ca-7ec9af5c73d7 | -11.40897 | -43.9431 | 2026-09-12 03:30:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4ae2303e-46be-3895-b0da-52345c9079b2 | -9.51899 | -40.34102 | 2026-09-12 03:30:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 979dd5d3-a5bc-3ae9-a01b-9f3480443131 | -11.1897 | -42.79 | 2026-09-12 03:30:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 489967e8-d9f1-39df-a532-81408bff66a0 | -10.15071 | -36.4537 | 2026-09-12 03:30:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 720f0d22-90ba-34eb-aa7a-c4e9fb699bb0 | -9.52064 | -40.3325 | 2026-09-12 03:30:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 56.1 |
| 8ec59757-4d82-3c67-a43d-dfb0df68e203 | -9.78129 | -42.00309 | 2026-09-12 03:30:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a3a8e35f-4023-3a2f-a46c-f02791561a4a | -9.51671 | -40.33463 | 2026-09-12 03:30:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 43.5 |
| 5f3c2541-1c28-39b7-b057-2621f5ae0221 | -11.18309 | -42.78859 | 2026-09-12 03:30:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 70c8ec72-049f-3c7d-8d2d-878d51ce137b | -9.51981 | -40.33676 | 2026-09-12 03:30:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 56.1 |
| 5738bf09-3cc7-38ad-a7f7-b416765de2da | -9.52651 | -40.33366 | 2026-09-12 03:30:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 28.9 |
| f4bb64be-0779-34f0-8a0c-753f071e2b96 | -7.53301 | -39.00975 | 2026-09-12 03:30:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4a361004-deb3-3f10-b3fd-3da7822e8752 | -9.52338 | -40.33154 | 2026-09-12 03:30:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 25.9 |
| e8578d09-5a6a-35ca-9630-52e1840c38ef | -8.91089 | -37.36118 | 2026-09-12 03:30:00 | NPP-375D | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e4d17fc2-3e06-3c13-9c4b-0f006942c689 | -9.52178 | -40.34008 | 2026-09-12 03:30:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 43.5 |
| 06fd31e0-e42d-3940-881c-3439e38822bc | -7.46168 | -42.11847 | 2026-09-12 03:30:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d2a76d0c-d3a5-301d-9211-3553bcf809bd | -9.52258 | -40.33582 | 2026-09-12 03:30:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 43.5 |
| 9a76b860-658b-308e-b04f-7b8e0b28b9bf | -9.52147 | -40.32824 | 2026-09-12 03:30:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 5aab1465-c774-3cc7-9378-7484d18f945d | -7.53366 | -39.00622 | 2026-09-12 03:30:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 852f25bb-415a-3ba2-a118-2d12748f23aa | -7.45489 | -42.11728 | 2026-09-12 03:30:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 7d3249dc-4f64-3023-949c-4869798f1e8d | -18.66002 | -42.00567 | 2026-09-12 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 753fa7db-3938-350a-8d9c-c9ca1d7604ed | -16.54474 | -41.04518 | 2026-09-12 03:32:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 744a9ac5-8536-3281-8bef-9b41283d204d | -17.71711 | -42.35374 | 2026-09-12 03:32:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c082c301-4734-3f3e-ac1c-8e130bcc43d8 | -16.54542 | -41.04187 | 2026-09-12 03:32:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |


[Clique aqui para ver as próximas entradas](README11.md)
