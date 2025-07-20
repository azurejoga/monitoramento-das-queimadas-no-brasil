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
| 22ec24d2-22b7-388a-b0bf-a15db00f8d8c | -3.54029 | -47.37959 | 2025-07-20 04:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 649a6dfb-f9bf-37ae-b6d8-72125c9767fb | -4.59381 | -43.31497 | 2025-07-20 04:14:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee5a6d3d-6d9a-3564-940d-7c6563069555 | -3.65434 | -48.32163 | 2025-07-20 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd765364-c376-382a-bb3e-919fe065c4b2 | -3.82687 | -47.74142 | 2025-07-20 04:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f262745d-fc4b-3ba2-ac82-cb9f081dd72b | -3.51438 | -47.21107 | 2025-07-20 04:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0943e739-53cb-30c6-8b9c-20392abc84ea | -3.13123 | -47.01038 | 2025-07-20 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b025007a-f8bf-3def-be01-baa01713eaa0 | -3.79399 | -41.00403 | 2025-07-20 04:14:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 6ce1bad1-cc55-3d48-b3b2-afc555196389 | -3.13518 | -47.01101 | 2025-07-20 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f181f12-998e-3bc3-9a69-507a7b56693f | -2.90675 | -48.24532 | 2025-07-20 04:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5776f5b7-104a-321e-8118-0280e172d78c | -2.6381 | -47.30599 | 2025-07-20 04:14:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1aa66c53-5cbd-3f90-8480-0580bfe4d69f | -3.83099 | -47.74205 | 2025-07-20 04:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7eef8798-0d9a-3109-b6b9-16f932d53ca7 | -3.03424 | -47.86571 | 2025-07-20 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 66988591-6c53-3fb8-b12c-7aed2797a3c1 | -2.91106 | -48.24601 | 2025-07-20 04:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 72cc10de-1de6-3cbf-8791-14e482a1a721 | -4.96302 | -43.2305 | 2025-07-20 04:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 881e1bd7-bb64-37a6-a5d8-2bec779612c6 | -3.5915 | -47.52537 | 2025-07-20 04:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e59137db-194d-3fcd-aba3-fca546ea101d | -4.12606 | -47.66002 | 2025-07-20 04:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 656c4c4f-8351-3478-975a-191da76725bf | -3.9209 | -42.41464 | 2025-07-20 04:14:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| e8752ef5-9b4b-3004-af53-df340fc35259 | -2.97883 | -49.10978 | 2025-07-20 04:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6369114a-5086-3b8e-bbde-8fc37b366ac3 | -3.11458 | -47.01285 | 2025-07-20 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 78342d5a-78e4-360d-b752-6e1b1440f547 | -2.44328 | -47.32986 | 2025-07-20 04:14:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf33a79c-c07d-39a8-ac5d-98e8921f69d3 | -4.96247 | -43.23397 | 2025-07-20 04:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 870193ed-3f01-37f0-8f38-8c3b42f76d3d | -4.07693 | -48.03764 | 2025-07-20 04:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 073bed53-df8c-3bac-a2c5-b9a35f7e2ef6 | -3.1304 | -47.01542 | 2025-07-20 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef7e9409-5c98-3888-b236-539fc7f0a700 | -3.11062 | -47.01221 | 2025-07-20 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 6bdc8396-c284-3edb-8027-7098185d17b7 | -3.91758 | -42.41412 | 2025-07-20 04:14:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 9cc51d1a-35be-33ba-8a9e-bfead25a6135 | -2.97891 | -49.1069 | 2025-07-20 04:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9389eec7-e24c-3791-b267-6484c0030170 | -4.12664 | -47.65643 | 2025-07-20 04:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63cadf15-abdd-3890-b2e1-ca02c152313a | -2.92394 | -49.0726 | 2025-07-20 04:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93f25f74-5943-30d9-80e6-315f4602ef3f | -2.91604 | -48.24265 | 2025-07-20 04:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff94da6e-862b-35c8-b4f8-d0dc3f8f6b6f | -2.97956 | -49.10516 | 2025-07-20 04:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 00f83d70-0f19-3284-bfcd-ece1d6d8d490 | -3.59209 | -47.52177 | 2025-07-20 04:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30c3b605-d6a9-31c9-8696-83aff187aa7f | -3.65367 | -48.32566 | 2025-07-20 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d6165d8-1f2d-36cc-9d0f-37d1416c30f2 | -3.12645 | -47.01478 | 2025-07-20 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 288b457a-74db-3193-a916-fb57d49cd420 | -4.9647 | -43.24143 | 2025-07-20 04:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6200345-2402-36d2-95df-f240582b20a3 | -4.12332 | -46.32755 | 2025-07-20 04:14:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 860708c2-c9ef-3b4b-94c4-c071787415e6 | -3.93856 | -48.09366 | 2025-07-20 04:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8471ea3-31e2-38f0-96ac-86c18e717c4d | -3.54084 | -47.37618 | 2025-07-20 04:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 047add87-5190-35ed-8767-ca5891445e66 | -2.90742 | -48.24128 | 2025-07-20 04:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4be4cba-568f-3e81-af7d-54ed5db67d9f | -4.59714 | -43.31549 | 2025-07-20 04:14:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e1c3df7-f460-3ab2-9fd5-aa5a6a52003b | -2.91537 | -48.24672 | 2025-07-20 04:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7b85fbe-f776-3b97-bb7c-04b658e4c84f | -4.96635 | -43.23102 | 2025-07-20 04:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| becc520e-267f-3b1d-a651-0edda6e4d0bd | -3.79455 | -41.00044 | 2025-07-20 04:14:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 33ef9df6-52cf-3b12-9838-25b03911a88d | -2.91173 | -48.24194 | 2025-07-20 04:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3607194-8dd2-396b-92ef-cef800294201 | -3.10667 | -47.01155 | 2025-07-20 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b44d2849-4a43-30ec-a6df-50e6e6136daa | -3.11853 | -47.01349 | 2025-07-20 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32d5a25a-8517-336e-ba1c-d2088290b874 | -3.12249 | -47.01413 | 2025-07-20 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 19418240-3543-3bd4-a896-a97e724a7cf4 | -3.88358 | -44.39405 | 2025-07-20 04:14:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c7029741-b9d4-398a-b9bf-d1a48b16a653 | -3.91095 | -42.41309 | 2025-07-20 04:14:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| db59d2b2-d24d-3c4f-a5fc-17cc65bb3b0b | -4.77808 | -45.33799 | 2025-07-20 04:14:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 229d4cae-104b-3308-a3ad-578a7435282f | -8.45647 | -46.02871 | 2025-07-20 04:17:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4a15474-fb2a-3a4b-b247-52984cf01fb5 | -8.08633 | -50.11007 | 2025-07-20 04:17:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 44e3cb4a-06d2-3da2-9b7a-68a7187e4940 | -10.63147 | -45.23577 | 2025-07-20 04:17:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13352d5c-3f64-3606-8383-42aff8919f6f | -10.67529 | -48.46229 | 2025-07-20 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f8d34dd-d64d-3d41-b2bf-6bf47cfedae2 | -5.34951 | -45.26488 | 2025-07-20 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5bd55625-91e7-3d70-9632-70b10ec35cc8 | -11.83642 | -47.51228 | 2025-07-20 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8481b0dc-e4fc-32fa-980a-ccb3796bccc7 | -11.5559 | -47.09423 | 2025-07-20 04:17:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3411ed7d-05b4-328e-b8f0-d363fd988455 | -10.65471 | -46.80334 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 9ce6d371-e0db-3fec-a306-09cfd22ff892 | -7.7031 | -47.28778 | 2025-07-20 04:17:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 94d926c6-d0d4-364a-a776-c4af95d70bef | -10.97379 | -45.1072 | 2025-07-20 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| fea6bf4d-e272-38cd-86d6-4d4e72d6944f | -10.54635 | -49.4916 | 2025-07-20 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2a51206-277c-3e6e-b72f-7b53dff2f55d | -8.35376 | -46.64266 | 2025-07-20 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cc663f9-5121-369e-95cd-3a8710d22272 | -11.57436 | -47.09324 | 2025-07-20 04:17:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| eeba81d9-b322-3e34-85d5-88d7feb6217e | -7.99394 | -43.68726 | 2025-07-20 04:17:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db286eb0-711d-355b-9801-68216a30f2f2 | -9.8029 | -48.56415 | 2025-07-20 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46757846-e777-3884-b2b1-9c161e9f0a68 | -10.4536 | -45.15465 | 2025-07-20 04:17:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2ef0bbba-0d7b-3681-aef6-a48e3dec2c81 | -7.70589 | -47.29444 | 2025-07-20 04:17:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cf24867e-49fd-364a-83d7-702e2bf59e03 | -7.06014 | -44.86931 | 2025-07-20 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4d9795a-7b61-349b-9468-90c08b4c99d9 | -7.628 | -44.28915 | 2025-07-20 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3315e3bb-edb9-34fa-8e31-c60d7af596a2 | -11.8328 | -47.51163 | 2025-07-20 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a52ee65d-cc5c-3516-bd12-a3ebe45013a7 | -9.63332 | -40.60279 | 2025-07-20 04:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9b76d503-44ff-369c-bfd7-19a53f12c6ce | -7.59495 | -45.31929 | 2025-07-20 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2be84523-6458-3253-9599-47d3a73c7bb3 | -9.62426 | -49.02077 | 2025-07-20 04:17:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fbd8c6e5-1c62-386c-90a3-b87ad620aba9 | -7.2677 | -43.10149 | 2025-07-20 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d63d1451-0392-3164-9572-55140591150a | -6.56875 | -41.47655 | 2025-07-20 04:17:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7959ecdf-f053-3630-adab-92ea49bffc48 | -9.61676 | -49.01562 | 2025-07-20 04:17:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e8626e2-90e8-3876-9a91-f9358dfc88b7 | -8.07223 | -50.10044 | 2025-07-20 04:17:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9895756-72ec-33e5-9191-dd4fa47f5dd3 | -10.65337 | -46.81139 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4d277897-5c6d-372c-82fe-07865d377646 | -7.43011 | -44.27975 | 2025-07-20 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 956dec7f-6550-3852-8441-32aae2179174 | -10.96709 | -45.10611 | 2025-07-20 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 69715ba8-da4d-321d-913b-105bb766e479 | -11.95995 | -46.75391 | 2025-07-20 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b9d05be-821c-371e-8bb9-62d399ecfca5 | -11.83352 | -47.5074 | 2025-07-20 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d522ae0-5afa-3baf-a83d-ec430e3e4f47 | -7.26438 | -43.10096 | 2025-07-20 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bcd4f727-8bea-348d-8dbb-26ac849d7ddc | -10.96987 | -45.11024 | 2025-07-20 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| fd9b71c6-ed36-307b-a062-621b69ad9f79 | -7.70232 | -47.29239 | 2025-07-20 04:17:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8012571b-b22a-3282-ab8a-1a837d258273 | -10.64639 | -44.48647 | 2025-07-20 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| adc07f57-b450-3179-ad4c-cf43219efdb6 | -11.82701 | -47.50188 | 2025-07-20 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b4190db-9d14-3063-85ea-606bec9e40dc | -11.80968 | -47.5162 | 2025-07-20 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 134013fb-efed-308d-8f88-9c224601afc6 | -10.63079 | -48.093 | 2025-07-20 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2f976c54-21d8-389e-b6b4-3c31fd4d7dea | -7.70135 | -47.29848 | 2025-07-20 04:17:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 38d6224b-d23d-3959-9fd3-515fe86f06b6 | -10.65825 | -46.80392 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 48164d23-b9b2-35e8-9460-61a08ea2f78e | -12.68392 | -44.3303 | 2025-07-20 04:17:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31c14f51-edb9-3f36-90b0-ce085ea28f20 | -10.66668 | -46.79705 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 559e797a-01b8-35f9-91db-09796ea13c39 | -9.54289 | -40.33482 | 2025-07-20 04:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 29c5a4ef-03fa-32ca-a994-2bbe8651c3bd | -10.69413 | -46.78521 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| aa782cd0-168d-3827-9db6-9cf9fb93dbdc | -7.63356 | -44.29734 | 2025-07-20 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6f0f3b1-d1b0-302f-b26c-446f91484eb2 | -12.00686 | -48.57785 | 2025-07-20 04:17:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4281f2f3-7c1d-3674-b9f3-95273acac26b | -7.12327 | -43.28882 | 2025-07-20 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e2c7d0e5-9ea2-3ce1-a00a-2f9c0e2b0580 | -10.69767 | -46.78582 | 2025-07-20 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 780ef93c-aa4f-3edc-8597-7f1142d831d4 | -12.35695 | -46.42598 | 2025-07-20 04:17:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ce5d50e-2376-3018-b3b5-72539acee905 | -11.63038 | -50.73474 | 2025-07-20 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README9.md)
