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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8428d84-c6a3-375e-9eec-92f263d9d9bd | -11.2118 | -54.0797 | 2026-09-20 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 1be9a49e-8190-36e6-aef3-93dedcdf9059 | -12.7428 | -46.183 | 2026-09-20 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| b6910e6e-95c8-34ed-8cfa-778721aa460e | -11.0989 | -54.049 | 2026-09-20 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 6b7c389a-ab7a-3e0d-ab86-ed8711cad77e | -11.041 | -54.1567 | 2026-09-20 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 5dadeb11-9dd3-342f-b38c-bb78285f5561 | -9.131 | -45.7273 | 2026-09-20 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 1e892e81-9499-3f43-940f-21405e9a8d7a | -3.6945 | -60.6215 | 2026-09-20 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 6054457c-eef2-3f02-b842-009b4f203c36 | -8.1688 | -54.7432 | 2026-09-20 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 6b88046e-2efa-3ffa-b9e2-47499e46d756 | -11.1369 | -54.0251 | 2026-09-20 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| ffc29498-e329-3d62-977d-de9995f152a6 | -8.7911 | -60.7935 | 2026-09-20 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 4b5701db-2f71-30a5-a4bf-28d05f00f22b | -2.4636 | -49.2301 | 2026-09-20 00:50:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 4ac8de02-73c1-3a45-9135-ff77aca05c0f | -6.5079 | -46.776 | 2026-09-20 00:50:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 000a1cd6-f66b-399d-989e-d606095b6abe | -11.118 | -54.0268 | 2026-09-20 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 99fd5883-82e0-384e-8b7e-c4020745427c | -3.3367 | -57.8673 | 2026-09-20 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 4c022375-3160-3a91-b534-f5cc9b005cec | -7.5472 | -45.8868 | 2026-09-20 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 0cc1a80c-fb22-3569-b4fd-d88d61c15c5f | -3.6946 | -60.5835 | 2026-09-20 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 6d097f1d-a067-3e09-bf75-efa018565a6d | -2.4451 | -49.2306 | 2026-09-20 00:50:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 9db3d34e-aa38-3571-ae07-a3226cdbdb2a | -7.3259 | -55.6153 | 2026-09-20 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| dde1f6eb-2ecf-3cb6-a493-ff1251378cf3 | -7.5525 | -45.4123 | 2026-09-20 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| c99619f0-c658-3b7b-80b6-59eb6fa1ec44 | -11.2307 | -54.078 | 2026-09-20 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 7860297d-3a53-3df7-a4be-70c25572c3a3 | -8.1686 | -54.7634 | 2026-09-20 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| b7b515e3-c6aa-32c4-816e-b45f19560594 | -3.6945 | -60.6215 | 2026-09-20 01:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 5980e9c9-c300-3210-ac1f-a9c9e609104d | -11.2118 | -54.0797 | 2026-09-20 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 5656582a-e534-3a94-bd3e-6c223c8d4dee | -12.7423 | -46.2058 | 2026-09-20 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.8 |
| ad1c93f9-9904-3d44-8a37-d422871d819a | -2.4636 | -49.2089 | 2026-09-20 01:00:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 62c13eeb-560c-3dca-afcf-1f92c7e1fb28 | -11.0991 | -54.0285 | 2026-09-20 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 147.4 |
| e0ad756c-8c7a-3b0a-b93d-b88101cba568 | -11.0802 | -54.0302 | 2026-09-20 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 72bc216d-fa87-3e22-86f3-8bb4b088d6dc | -11.8491 | -46.8556 | 2026-09-20 01:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 632546de-fcd6-33ce-994a-ca04bcb0831d | -3.3367 | -57.8673 | 2026-09-20 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 44bd5199-a23e-310f-bda0-b923f7739eb3 | -12.7629 | -46.1343 | 2026-09-20 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 8b018537-c424-3ed9-8dbb-b8b9ad02bc80 | -12.1332 | -47.0185 | 2026-09-20 01:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 9fcd75c5-fd71-3b3b-8723-8999cc21c019 | -3.7453 | -51.8288 | 2026-09-20 01:00:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| a369abf5-ec65-391f-9698-a291a19af5b7 | -12.7616 | -46.2029 | 2026-09-20 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| a3ea53b6-8d29-32dc-92c5-1dfd48779853 | -14.6856 | -46.6886 | 2026-09-20 01:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 69e69c32-d361-3624-a010-e560d5042966 | -15.2284 | -53.8691 | 2026-09-20 01:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 7fff13fd-8bb5-3d9c-a7f7-aeb1e55e840a | -11.4549 | -45.3202 | 2026-09-20 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 6d5f6646-d680-355d-a72e-8c260d915ecd | -7.5525 | -45.4123 | 2026-09-20 01:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 88caf39b-3b8a-34ce-b670-74ec10bd35b4 | -8.1688 | -54.7432 | 2026-09-20 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 199157de-8545-3c25-af27-dc540017e8dc | -2.4451 | -49.2306 | 2026-09-20 01:00:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 88cdefa0-6e10-3b30-b5ce-b3459f455eee | -8.1686 | -54.7634 | 2026-09-20 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| f1d5bf7f-4bed-36e3-8305-f90da3999359 | -2.8974 | -57.8181 | 2026-09-20 01:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| a0d0d9ca-189d-3bd9-a211-2a2041c38fe8 | -3.6946 | -60.5835 | 2026-09-20 01:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| f68916f0-8297-320b-a461-49be143e15df | -2.8791 | -57.799 | 2026-09-20 01:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 04966790-d42f-33ea-b14b-d90e4fb31f5c | -12.5419 | -50.0243 | 2026-09-20 01:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| e20663e8-d806-36b1-8d9d-406cf5b1545d | -11.1369 | -54.0251 | 2026-09-20 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 6d77fca4-c9d3-3393-a4fa-997a70be2184 | -12.7428 | -46.183 | 2026-09-20 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 90fd319b-4c74-38c6-96f0-25cd33cf118c | -2.8791 | -57.8184 | 2026-09-20 01:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 54ff1114-2e10-3ae4-af24-d9a4ec3a28cc | -8.1872 | -54.7622 | 2026-09-20 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 800a9b36-a02d-33d1-b350-bced14bc3d8c | -2.4451 | -49.2093 | 2026-09-20 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 201a6af9-ac80-380a-9d2d-2649e81c742c | -7.5522 | -45.435 | 2026-09-20 01:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 0c6e9ffb-551a-3a37-a8d9-e29d91672efd | -7.3073 | -55.6163 | 2026-09-20 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 7b888751-5f11-36d3-af3a-5cb1f2d27237 | -11.8487 | -46.8781 | 2026-09-20 01:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 2c3c9cc8-5a41-328b-9cd2-d1e38ee6a266 | -13.037 | -46.9096 | 2026-09-20 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 61e49fad-53ec-3642-ba4d-5e2db485e109 | -7.3259 | -55.6153 | 2026-09-20 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 5073f9e2-5693-3a76-a7c6-caca42843675 | -2.4636 | -49.2301 | 2026-09-20 01:00:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 24aafea4-224b-36d6-9339-68737d33efe9 | -11.8739 | -47.657 | 2026-09-20 01:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 7fe5a5ba-9fa6-3942-9783-b299dabf2874 | -3.6946 | -60.6025 | 2026-09-20 01:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 1b5354bc-fce2-30a8-a654-e7459ce07624 | -9.131 | -45.7273 | 2026-09-20 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 1ddff5a3-deef-3fdc-ab64-b07286c7a85d | -11.8547 | -47.6596 | 2026-09-20 01:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| be81dcda-2ecf-3fd9-837b-93401fa36a17 | -8.7911 | -60.7935 | 2026-09-20 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 60969f7e-9411-382e-8ed0-94cef3e49c7a | -7.4286 | -44.7409 | 2026-09-20 01:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 1e236558-c421-3458-92f2-a91e696388e0 | -11.8679 | -46.8755 | 2026-09-20 01:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 0af2a58d-92a2-3f33-bdc2-c131dd6e23fb | -11.2307 | -54.078 | 2026-09-20 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 107335b2-0813-3548-b30c-53521d9a5c99 | -12.7621 | -46.18 | 2026-09-20 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 832ebb5c-b97b-37e6-a517-53b5f6eff93b | -13.0177 | -46.9125 | 2026-09-20 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 1c48feee-75d6-39d2-894f-d273a3f756d2 | -11.118 | -54.0268 | 2026-09-20 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 120.0 |
| d8f57b4d-2012-3894-ba1d-4aa2eefe27b5 | -3.7454 | -51.8082 | 2026-09-20 01:10:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 8b4344f2-d64f-3a64-88b2-dd540eb40a24 | -6.2948 | -47.6274 | 2026-09-20 01:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 400faf57-e451-3840-aedd-2b15c6689119 | -11.4549 | -45.3202 | 2026-09-20 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| fc736fd1-4d12-3f57-bb6b-9604798a5790 | -3.6945 | -60.6215 | 2026-09-20 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 77d10ea5-cdc6-3f1f-8c07-7882a0440a2a | -12.7616 | -46.2029 | 2026-09-20 01:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 8fb65a6d-4a3e-36a3-9bc8-02217068c9c4 | -11.0991 | -54.0285 | 2026-09-20 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 137.3 |
| eaf776c6-788d-3d8a-8bbc-e7e78f50f780 | -2.8791 | -57.8184 | 2026-09-20 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| b9b7fd83-9531-3191-9c98-66237b2c99be | -2.8974 | -57.8181 | 2026-09-20 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 83606f97-a9d6-3a3b-b0be-336284b3cabd | -8.1688 | -54.7432 | 2026-09-20 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 685b538e-5e97-307f-814b-f42490a2b619 | -6.2761 | -47.6287 | 2026-09-20 01:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 8e34712b-de48-34b4-b1fc-dec7603dea26 | -11.8491 | -46.8556 | 2026-09-20 01:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 0e539f09-31d8-3741-bb5a-26a11109b8f8 | -2.4636 | -49.2301 | 2026-09-20 01:10:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 30d49475-1ae4-3b9b-b4ec-8805118f809f | -3.6946 | -60.5835 | 2026-09-20 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 7f0643f8-b443-33c9-80ab-af77ca1b6138 | -2.4451 | -49.2306 | 2026-09-20 01:10:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 568c9fed-7742-3e5d-9b49-e813ffdd4f3b | -11.8547 | -47.6596 | 2026-09-20 01:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 8a4b1a77-3676-3a64-a3ec-fa7e28f73498 | -5.4087 | -44.2644 | 2026-09-20 01:10:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 26583c5d-3042-3acc-8087-29ebca066c62 | -11.2307 | -54.078 | 2026-09-20 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 7d829a0a-7382-3edd-80c9-5b18d83371a9 | -11.8544 | -47.6819 | 2026-09-20 01:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 1f103aa2-1987-3c39-9a5e-330d1c16b9a2 | -11.118 | -54.0268 | 2026-09-20 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 66e3fe6c-e718-3f83-85e5-0634ea4b7962 | -6.1651 | -47.5271 | 2026-09-20 01:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| c8b157d2-7d26-3121-a087-f5536fd0eb8f | -11.2118 | -54.0797 | 2026-09-20 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 6699d7b6-14da-3fa1-9cf5-01c39dd87986 | -7.5522 | -45.435 | 2026-09-20 01:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| d06fdb90-1a39-389d-9870-35937065d251 | -3.6946 | -60.6025 | 2026-09-20 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 836b156b-2378-397c-9df7-024bdc9e9199 | -9.131 | -45.7273 | 2026-09-20 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| a50181bc-f2b5-3fc9-b0c0-7ff411c4e7f8 | -13.037 | -46.9096 | 2026-09-20 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 9c84898b-ecb4-3d3f-a4f4-ef9d3e9655ec | -3.7453 | -51.8288 | 2026-09-20 01:10:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 300919cd-07bb-30f9-89c8-a490693f5ab6 | -14.6856 | -46.6886 | 2026-09-20 01:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 18c9319b-9932-3c5e-81a0-ba0dc3b00c70 | -2.4451 | -49.2093 | 2026-09-20 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 6a58cb1e-0f6f-3cf0-9aa9-2225f8505c0d | -7.3259 | -55.6153 | 2026-09-20 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| f3dde773-f6ca-3622-bbab-d1afc979c82f | -11.8487 | -46.8781 | 2026-09-20 01:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| a0d64af8-7b92-3304-acc2-26ac8b0cf7ac | -13.0177 | -46.9125 | 2026-09-20 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| cfb33a31-9e7c-3b13-9f9d-20fd2efc6811 | -11.8679 | -46.8755 | 2026-09-20 01:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 3f65699d-8af6-309e-ba19-291dcdbc8160 | -2.8791 | -57.799 | 2026-09-20 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 03bc997c-f37d-303c-b817-27a79ae8e296 | -3.3367 | -57.8673 | 2026-09-20 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 1866f051-cac1-3f58-8e21-c0a934537b9c | -6.2763 | -47.6069 | 2026-09-20 01:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |


[Clique aqui para ver as próximas entradas](README5.md)
