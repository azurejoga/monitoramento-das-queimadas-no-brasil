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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 938cf1f1-f023-3b94-9db8-1da600f021b9 | -6.0784 | -44.6961 | 2025-09-11 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| e577e5b7-571c-3cd7-b607-fc83fad524cf | -6.2087 | -41.0137 | 2025-09-11 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 107.7 |
| 8edc28b3-ea18-3a2a-82d5-b92fc2f6a6cb | -6.3614 | -44.4908 | 2025-09-11 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 0bab58ca-eb79-3a5e-bf76-4236183650c5 | -14.5125 | -53.9367 | 2025-09-11 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 71177f00-f43f-3888-9ea2-d904c09c8240 | -11.7786 | -46.5047 | 2025-09-11 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 304.9 |
| 9e3d4a8c-2de8-3a86-9b8b-c90a8c9a759c | -7.559 | -48.2723 | 2025-09-11 14:00:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 51f6319c-662b-3bcb-b727-846fa187ba7d | -13.2606 | -51.7335 | 2025-09-11 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 274.0 |
| 3940a25f-c828-3f20-a2e4-f6036a96fc62 | -8.8755 | -49.5613 | 2025-09-11 14:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 186.4 |
| fa23f711-bba9-32f3-9b6a-c30f680ef348 | -13.2407 | -51.7784 | 2025-09-11 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 00f57cca-101f-34d3-9bc9-e89c55172617 | -9.0793 | -49.7997 | 2025-09-11 14:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 9607f0bd-2fc9-3bac-ab81-d0a170d6d0ff | -6.1944 | -53.2585 | 2025-09-11 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 00dc5650-10b3-37c4-95ac-7657e019722f | -13.49 | -51.7688 | 2025-09-11 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 029dc247-8ca3-35d1-8b69-5425f9823ae2 | -13.2602 | -51.7548 | 2025-09-11 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 312.7 |
| bff8e781-9488-338f-b549-de573a17799d | -8.1649 | -46.0983 | 2025-09-11 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| b69d65dd-6914-34ea-a0a7-d3c1cedf4583 | -7.4349 | -45.8519 | 2025-09-11 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| aff96063-df97-3a10-8523-da5d7b898b2a | -7.4347 | -45.8744 | 2025-09-11 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| a26360a8-1491-34f2-887e-4aa5c8638e70 | -6.3226 | -53.4553 | 2025-09-11 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.6 |
| c044a66b-4e78-36e7-ae44-04d4d5d3c5c5 | -14.7334 | -60.2337 | 2025-09-11 14:10:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 31f5f19b-3188-336f-b9fd-7e9d0749ee5d | -15.5628 | -54.7453 | 2025-09-11 14:10:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| df36b319-fb01-39ef-b4cc-08a4f6225c0a | -9.0567 | -47.0577 | 2025-09-11 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 18339a90-6411-3eb3-bb39-b2f72b6867fa | -6.3158 | -43.4081 | 2025-09-11 14:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| e021b545-8667-37d4-894d-f1fd2d167838 | -15.8014 | -52.2258 | 2025-09-11 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 0edf8c11-2c26-38ca-8dc3-4a4a01821591 | -9.0127 | -46.1014 | 2025-09-11 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 174f0d6c-00e8-37bd-818b-5d1ceefa1f3c | -8.994 | -46.0808 | 2025-09-11 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 2e35a042-d46c-35c9-8482-345db9133564 | -10.6793 | -48.6415 | 2025-09-11 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 93e1afb9-dde6-3189-85e3-92567b552f3d | -8.8755 | -49.5613 | 2025-09-11 14:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 189.4 |
| 9dc423c6-8743-365f-a457-4091fa1b826a | -7.4349 | -45.8519 | 2025-09-11 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 135.7 |
| a65faf12-cdce-3d74-b9f1-f9d357488c7f | -12.1335 | -44.8508 | 2025-09-11 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| e4340758-9c32-3d22-b990-8688f4898a1e | -11.1685 | -45.3144 | 2025-09-11 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| dcc02c4e-ae8c-3991-b799-88b5d4188afd | -14.4464 | -53.2544 | 2025-09-11 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 8943d5c5-93ed-3b48-bc47-2f090a6b99ad | -11.4089 | -43.581 | 2025-09-11 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.4 |
| bf9b886d-4af3-3bb2-972a-c3e340053600 | -11.0997 | -48.4392 | 2025-09-11 14:10:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 1dc8e95f-db41-3824-b30d-25264fef877b | -8.9752 | -46.0829 | 2025-09-11 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 350.5 |
| 1d53746a-612c-338a-b80e-e86baaefd49a | -11.779 | -46.4821 | 2025-09-11 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 232.2 |
| ec43ba61-8b08-3740-9fd0-08e0e5cd34e8 | -10.1365 | -48.1993 | 2025-09-11 14:10:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 467fc6a2-defb-3e11-9dca-ae1204729b83 | -6.5812 | -41.4151 | 2025-09-11 14:10:00 | GOES-19 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 111.6 |
| 6ebaa700-93bf-321a-9046-74053623bf13 | -9.0753 | -47.078 | 2025-09-11 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 188.8 |
| d50fdd6b-ae6d-3ea7-aa07-bd51b0639b53 | -6.8525 | -47.8707 | 2025-09-11 14:10:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 5edbcbf0-81ea-3fd4-9c2f-caf0bef4f357 | -6.5038 | -45.2539 | 2025-09-11 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 43968d60-16ee-3e64-972a-c545482f6bfb | -6.2228 | -43.3226 | 2025-09-11 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 0dc62249-b382-3b03-882c-df88379de7ed | -10.859 | -45.5851 | 2025-09-11 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 51ffa3ab-5787-38a3-964a-a6f55bb27ae8 | -6.3041 | -53.4562 | 2025-09-11 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| c78b2bc2-f49c-3647-8f87-e2cf57c43ec5 | -9.0979 | -49.8194 | 2025-09-11 14:10:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 209.0 |
| 68bb8883-cc4b-31f4-8abe-ca378a09ef47 | -13.2606 | -51.7335 | 2025-09-11 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 361.8 |
| 2e7e146c-363c-36ae-8e7e-ba24c28ffbcb | -4.553 | -43.7439 | 2025-09-11 14:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 2e10b463-9f75-388a-a907-2b715b8f5497 | -11.4285 | -43.5544 | 2025-09-11 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 391.4 |
| 64d9aa99-3c7e-3676-ae8f-20423bb8f01e | -9.9026 | -50.17 | 2025-09-11 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 194.8 |
| d5617ede-fe6c-35df-9fe4-d3c7f57b2beb | -6.485 | -45.2554 | 2025-09-11 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 42a410f1-d735-39ae-ae2a-94b8ef01fb24 | -11.0962 | -51.3231 | 2025-09-11 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 131.9 |
| f90dcfc3-e886-398b-91c3-5d7a68bdf251 | -6.2087 | -41.0137 | 2025-09-11 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 124.5 |
| 28c2ae43-6940-35f9-9523-c3cff870c1c1 | -9.0129 | -46.0788 | 2025-09-11 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| ad99309d-737d-36a2-a549-853a855f5119 | -8.8758 | -49.5399 | 2025-09-11 14:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 9d8bfc36-941f-3b5a-a7bb-3bdad6c3678f | -9.9762 | -50.3121 | 2025-09-11 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 161.1 |
| 3d2aecb6-ce28-3bfa-821e-425a5424a091 | -9.0976 | -49.8408 | 2025-09-11 14:10:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 216.2 |
| bea2b964-e2e3-388a-942e-13c7e982a34f | -9.0788 | -49.8425 | 2025-09-11 14:10:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 126.0 |
| bde3360f-464e-3ab2-9c93-83f17047f5ea | -6.9319 | -45.5352 | 2025-09-11 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 21717ace-5c91-3250-9e5b-757ec4a2cd48 | -6.8374 | -45.6108 | 2025-09-11 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 5a81755a-d3cf-3d7e-8530-af0b32b8fbd7 | -9.7445 | -47.8468 | 2025-09-11 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 61209f5b-bee8-3cf5-9b61-78db16e4a552 | -7.4161 | -45.8536 | 2025-09-11 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 269.7 |
| d9bb7c6e-888d-315d-9422-9373ad27e746 | -11.4836 | -43.6875 | 2025-09-11 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 14559729-3f63-3968-8128-4399b10a3469 | -14.3122 | -45.046 | 2025-09-11 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| f8678e8c-c7d3-360b-8ecd-c3442a394d37 | -14.7527 | -60.2321 | 2025-09-11 14:10:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| d68b3c3c-0934-316e-aea6-08e8fb3c5fde | -9.0265 | -49.5046 | 2025-09-11 14:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 548d7e9d-0de6-3b74-ab38-bffb89ff31e3 | -7.4159 | -45.8761 | 2025-09-11 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 329.8 |
| 3708f5f5-cb01-3080-90dc-c1e22dd1ea60 | -11.4281 | -43.578 | 2025-09-11 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 186.9 |
| 3ffb9a76-906d-3ba9-b5a1-2c377593777e | -6.684 | -44.1189 | 2025-09-11 14:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 0447fbe7-69c1-3829-969f-1c8fcc245530 | -9.976 | -50.3334 | 2025-09-11 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 3c904ced-a89a-3126-b374-26c1728e84a7 | -9.8838 | -50.1719 | 2025-09-11 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 4fd1b8ad-de2c-3238-9a6b-8fc62fd610e5 | -11.1 | -48.4172 | 2025-09-11 14:10:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 4763ca52-6f43-37af-9af3-1cdd4cfae469 | -6.3228 | -53.4349 | 2025-09-11 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 51938cb6-67a2-3f3c-8eda-1b7b06cfb499 | -10.5482 | -49.8899 | 2025-09-11 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 206.5 |
| 14023d98-4833-3bd5-9757-710f219df1ec | -15.5433 | -54.7477 | 2025-09-11 14:10:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 118.7 |
| b722a52e-048a-33bd-9d9c-a58b0abc5028 | -11.7786 | -46.5047 | 2025-09-11 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 331.4 |
| c1529891-be03-3720-a4f3-d39b4c8a44c9 | -11.7115 | -48.2536 | 2025-09-11 14:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 2c04a06f-cd26-3db6-b036-ec1c9965d206 | -15.1211 | -50.1438 | 2025-09-11 14:10:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 963ceedd-1bea-3931-857f-24dfeb6b322a | -14.3071 | -54.7699 | 2025-09-11 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 76e814e0-1c22-3d2d-9179-4c02f69c4c00 | -10.7366 | -46.1011 | 2025-09-11 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 015be75e-df5a-3a98-8c2e-b597b1f77a87 | -15.801 | -52.2472 | 2025-09-11 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 110.8 |
| f7197465-3165-3d4d-baa9-9dc2972a5a4b | -9.075 | -47.1002 | 2025-09-11 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 227.2 |
| 79dc1bff-ce48-33a5-b9a7-2cdc8c67ace4 | -11.7399 | -46.5326 | 2025-09-11 14:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 3d827f3b-2b35-3aa1-a2a3-d4027a85b1cb | -9.9004 | -51.8811 | 2025-09-11 14:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| ae2c3cba-71e2-3d3b-b1c0-8eb65baf507c | -9.0565 | -47.08 | 2025-09-11 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| d618dd7e-f0c7-3257-84df-2ab02a0abc45 | -5.5502 | -43.0484 | 2025-09-11 14:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 81c72289-dd1b-34e7-a592-e9ffc2d2441f | -8.1101 | -49.2634 | 2025-09-11 14:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 21bccbb4-1562-32e1-b79d-6dc763c47445 | -8.1103 | -49.2419 | 2025-09-11 14:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 1be8542c-c939-3107-99f3-4976af2cda14 | -10.1844 | -46.1927 | 2025-09-11 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| f05ab675-adf2-3e0a-b842-682ecc549964 | -8.1235 | -44.8559 | 2025-09-11 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| adfc5c1a-6a9d-33e5-93bd-455a73261fbe | -11.7211 | -46.5127 | 2025-09-11 14:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 199.4 |
| 54cb1048-f36d-31c0-b99f-ea1a5597a332 | -17.3366 | -46.6951 | 2025-09-11 14:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 168.2 |
| 1c810c4e-417a-3536-8500-f2f52eebf7e0 | -14.7524 | -60.2519 | 2025-09-11 14:10:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 89d44954-dd7b-325c-a25b-d32a424ad302 | -10.5671 | -47.2442 | 2025-09-11 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 11848599-cc84-3247-a341-7ccfe238be8d | -11.3905 | -43.5365 | 2025-09-11 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 172.9 |
| c94b874f-2336-3e49-9c15-df8774c1017b | -6.6149 | -45.3807 | 2025-09-11 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 490177c7-f5d7-3bd3-9b71-dba2069e40c5 | -11.4845 | -43.6402 | 2025-09-11 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |
| d675bf9e-d56d-39e5-857e-4bbb0a8fe62e | -14.6652 | -44.0617 | 2025-09-11 14:10:00 | GOES-19 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 108.0 |
| b2c9eeab-bc0b-3a11-9387-e9d94c9c2356 | -6.2226 | -43.3459 | 2025-09-11 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| e95740c3-cacb-3ff9-be9d-a91665245630 | -14.3074 | -54.7492 | 2025-09-11 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 119.6 |
| b6af9b5b-989f-3eda-8d9a-38df9f3cb6f3 | -9.0939 | -47.0983 | 2025-09-11 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 136.4 |
| f0e6e022-bf06-3563-b45d-b10a13ce5c4d | -11.3718 | -43.5157 | 2025-09-11 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 3943600c-9efd-32fa-be35-23c76da5e456 | -11.077 | -51.3462 | 2025-09-11 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 160.9 |


[Clique aqui para ver as próximas entradas](README146.md)
