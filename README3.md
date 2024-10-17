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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7b6775e-b621-3912-a6f7-9672fdff5701 | -12.5289 | -46.819302 | 2024-10-17 00:19:25 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f15f0f9-893f-3d08-a9ee-f885ef9fe462 | -12.509 | -47.408298 | 2024-10-17 00:19:27 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 335b17f0-f1a0-37de-9452-75bd889ce3a1 | -12.5109 | -47.4174 | 2024-10-17 00:19:27 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c90bb2e9-4f30-3a3f-b07f-654d6454a751 | -9.4688 | -40.3717 | 2024-10-17 00:19:51 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8a17c536-942d-3286-aa38-2d0ba91a0bf4 | -9.4806 | -40.378399 | 2024-10-17 00:19:51 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a04dd906-07dd-3c52-ba33-1617f2f52814 | -9.9014 | -42.095001 | 2024-10-17 00:19:51 | METOP-B | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3ffbc602-c154-35e1-87ee-5f0ad52f77dc | -9.9031 | -42.102501 | 2024-10-17 00:19:51 | METOP-B | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ca79ede0-34b4-3f03-a3e6-d82d2ba327da | -9.4709 | -40.380699 | 2024-10-17 00:19:51 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| bfb3d98f-6547-32d5-b00b-f0736f43d75c | -12.4913 | -55.148899 | 2024-10-17 00:19:52 | METOP-B | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 19838c39-a8c1-348e-92de-67f22baafd70 | -10.7831 | -48.545502 | 2024-10-17 00:19:59 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ea24a848-39ed-3754-85c1-0dc4fc4b34f2 | -10.7553 | -48.510101 | 2024-10-17 00:20:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 990fb72c-3754-3cd2-8e17-a7f496dd4917 | -10.7573 | -48.52 | 2024-10-17 00:20:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c48d961e-6a9a-31c2-8be7-f81236253eeb | -10.7455 | -48.5121 | 2024-10-17 00:20:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a2acf99-98ab-3e45-a393-efeb4ecc37d0 | -10.7475 | -48.521999 | 2024-10-17 00:20:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eea6cdc8-aa98-3848-b76e-b53cc1169e07 | -10.7357 | -48.514198 | 2024-10-17 00:20:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 52b4f704-07c2-3455-adf5-4f08ed4aca85 | -8.7228 | -40.578098 | 2024-10-17 00:20:04 | METOP-B | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 48c14f2c-13e5-331a-addc-6795b58f3d56 | -8.5081 | -39.9314 | 2024-10-17 00:20:05 | METOP-B | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| bfef9706-e33c-33fa-952c-3cca12d60712 | -8.4984 | -39.933701 | 2024-10-17 00:20:05 | METOP-B | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 2258bf1e-67ed-31b9-8cfa-69e638992682 | -8.8202 | -41.258598 | 2024-10-17 00:20:05 | METOP-B | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| edeb57d5-5756-32df-bd08-f89804d8762a | -8.8222 | -41.266899 | 2024-10-17 00:20:05 | METOP-B | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1529a62b-a176-3fc3-b6ee-80236fb4e883 | -8.7146 | -41.159801 | 2024-10-17 00:20:06 | METOP-B | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2b9c6c61-cf6a-3a08-bc88-8655563ee72a | -8.7029 | -41.153599 | 2024-10-17 00:20:06 | METOP-B | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 378cafbd-59c4-38cd-a5b5-946eb9d92785 | -8.7048 | -41.161999 | 2024-10-17 00:20:06 | METOP-B | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 83590679-ff3a-369e-a886-77c0c986358e | -8.7068 | -41.170502 | 2024-10-17 00:20:06 | METOP-B | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| fbfbaa32-82f0-31c9-9c08-b65a3b321923 | -10.4477 | -48.847801 | 2024-10-17 00:20:06 | METOP-B | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4bae9ea0-977c-361a-8536-37e0fa3db579 | -10.438 | -48.8498 | 2024-10-17 00:20:06 | METOP-B | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d406b532-390c-370f-9bc0-501ef3b3d607 | -8.4619 | -40.259201 | 2024-10-17 00:20:07 | METOP-B | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 94a00feb-b96b-3be9-a529-6b3abe54ef73 | -8.4641 | -40.2687 | 2024-10-17 00:20:07 | METOP-B | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 62e7eb3b-53e5-3bc8-a9bf-0f0f5d75ffa7 | -8.0858 | -41.073399 | 2024-10-17 00:20:16 | METOP-B | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9af58529-8346-342d-b80f-bd9aea7b507d | -7.9425 | -40.638 | 2024-10-17 00:20:17 | METOP-B | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6c12c8c8-343a-3f5b-9c2c-4f85086b9ca7 | -7.9446 | -40.647099 | 2024-10-17 00:20:17 | METOP-B | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 43c57d80-d267-3015-8054-6f5f6fcbf8f2 | -7.9868 | -40.958801 | 2024-10-17 00:20:17 | METOP-B | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| be17adc2-58b9-3804-b547-47304d4f7874 | -7.9888 | -40.967602 | 2024-10-17 00:20:17 | METOP-B | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cd0d91b9-2e7f-36d4-aed9-7308634e4bed | -7.8151 | -40.754501 | 2024-10-17 00:20:19 | METOP-B | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 00468703-cd91-3f51-b01c-1a5d5df3d935 | -9.0483 | -46.470299 | 2024-10-17 00:20:20 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 224e6857-1e0b-3863-9e54-4ef547484bce | -9.0499 | -46.477798 | 2024-10-17 00:20:20 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3220440c-dd84-3f45-86fa-fe04451b753a | -9.0581 | -46.468201 | 2024-10-17 00:20:20 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b17a4da4-8d6c-3456-bb67-62db32b697a9 | -9.0597 | -46.4757 | 2024-10-17 00:20:20 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b60b7144-dafb-3bb6-844e-a2578413df7b | -10.1961 | -52.298199 | 2024-10-17 00:20:21 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 28807f4d-703a-3961-a8f4-d47e983dbf92 | -8.1336 | -42.8862 | 2024-10-17 00:20:22 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0dba832c-d7be-33b4-9b75-d26046240aaf | -8.1352 | -42.893501 | 2024-10-17 00:20:22 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6b07eec8-13d6-3bb1-a8dd-eee661ac5902 | -10.1864 | -52.300098 | 2024-10-17 00:20:22 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07f81543-5137-3317-b6c6-82edbd88fdab | -10.1898 | -52.317299 | 2024-10-17 00:20:22 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 54405ae3-5d56-3825-8aac-50f99e2c4168 | -7.1513 | -40.212002 | 2024-10-17 00:20:28 | METOP-B | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c1757972-c1be-38c6-9751-8aa7c4a35a4a | -7.1537 | -40.222 | 2024-10-17 00:20:28 | METOP-B | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 30f9db21-b84f-354d-a79e-b78007660cb6 | -7.7453 | -42.7668 | 2024-10-17 00:20:28 | METOP-B | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0f396f09-c8d1-335b-9ca4-3b52a2a076e8 | -7.747 | -42.7742 | 2024-10-17 00:20:28 | METOP-B | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 08c7ffbf-61cf-306d-9fb6-fac3261e067e | -8.2936 | -45.9827 | 2024-10-17 00:20:31 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e04f33c2-f2ac-37e5-a465-d8ea16c0beaf | -8.2822 | -45.977798 | 2024-10-17 00:20:31 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2363d0a-59a0-3007-b5e0-9c5f4a2f6977 | -8.2838 | -45.984901 | 2024-10-17 00:20:31 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 045b7657-97b6-320d-8129-ef4bd9cd8ad7 | -8.2708 | -45.972801 | 2024-10-17 00:20:31 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47e9d4db-9635-3000-b133-0f076bcfea7a | -8.2724 | -45.9799 | 2024-10-17 00:20:31 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48aa45d5-7da6-350f-bafb-373bf507846a | -8.2185 | -45.782398 | 2024-10-17 00:20:31 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d881ef1c-3943-3589-98e6-11fc334cc041 | -7.8675 | -45.359901 | 2024-10-17 00:20:35 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1e45a6bd-4404-3b56-bf96-f8b2b081781b | -7.8742 | -45.343899 | 2024-10-17 00:20:35 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 58720cb1-6a37-3f9e-b48d-273786cfc4d7 | -7.8758 | -45.3508 | 2024-10-17 00:20:35 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 90a9ba41-b0e1-314a-a94a-b8eb3b43d3e4 | -7.8628 | -45.3391 | 2024-10-17 00:20:35 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 03220373-172b-3e27-ab50-8645598c3c4c | -7.8644 | -45.346001 | 2024-10-17 00:20:35 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1f2101fd-4d1e-3011-95b8-3fb251a07741 | -7.8659 | -45.353001 | 2024-10-17 00:20:35 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4173c35f-5ba4-36fe-9952-2b95d5ce8ddf | -7.8561 | -45.355202 | 2024-10-17 00:20:36 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c48d3ef9-d020-3d65-b701-5ffd9a8c7f21 | -7.8576 | -45.362099 | 2024-10-17 00:20:36 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 75983390-05d2-39b9-adb9-b945a4d4db19 | -7.5212 | -44.046799 | 2024-10-17 00:20:36 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bf0835b3-c43c-363a-a90f-e9db8d7b5ed2 | -7.2905 | -43.938202 | 2024-10-17 00:20:40 | METOP-B | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 45dbec5e-e865-3e68-a63b-3d4f357796c3 | -7.2517 | -43.903 | 2024-10-17 00:20:40 | METOP-B | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 56a9fa1b-d36c-387d-bbf4-97721b20be9d | -7.1968 | -45.030998 | 2024-10-17 00:20:45 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 37b68f1a-a33d-388a-8048-937ef5ef675a | -7.1983 | -45.037899 | 2024-10-17 00:20:45 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 444e2790-1c14-3b12-be49-0197a7ad28cb | -6.7277 | -43.547798 | 2024-10-17 00:20:47 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f7475ef-234f-3e1d-9ab0-4be6c54b970f | -6.7293 | -43.555 | 2024-10-17 00:20:47 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0ac3556-9611-32c0-bfb3-238b6ddf036a | -6.731 | -43.562099 | 2024-10-17 00:20:47 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 302f8b2e-1d6b-3c43-9034-7a56aad269d1 | -6.7179 | -43.549999 | 2024-10-17 00:20:47 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fedab6f9-ce0b-3936-ac99-e19ecc8df52e | -6.7195 | -43.557201 | 2024-10-17 00:20:47 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45ab6910-6c42-37d4-994a-94a03489dc0d | -6.7212 | -43.564301 | 2024-10-17 00:20:47 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0c1bc3f0-c1b9-35d8-9fa5-eb211fe61a24 | -6.6836 | -43.5354 | 2024-10-17 00:20:48 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 88f8b9b4-f369-35f6-8291-f00c1faa0353 | -6.6852 | -43.5425 | 2024-10-17 00:20:48 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2c0b3dae-f6e7-3a89-a0ce-2e84bbf3ea95 | -6.6868 | -43.549599 | 2024-10-17 00:20:48 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 030abb98-d786-3d28-871f-41fddd2e8b29 | -6.4625 | -43.199001 | 2024-10-17 00:20:50 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 694acf7c-3f7b-3b58-8266-32f3939d3ac3 | -6.4642 | -43.206299 | 2024-10-17 00:20:50 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| abd9d6a4-2049-3be7-8828-30fcb7f31919 | -5.9771 | -42.118 | 2024-10-17 00:20:54 | METOP-B | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 18c6c41a-5464-3ad7-8dc7-e48302923605 | -5.979 | -42.126099 | 2024-10-17 00:20:54 | METOP-B | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fa2a6c50-b226-3ed4-b602-776b4787aff9 | -6.2111 | -43.2715 | 2024-10-17 00:20:55 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ffb0a706-dbbe-3a41-b191-1966034e12ea | -6.2127 | -43.278801 | 2024-10-17 00:20:55 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2edde2e9-fd01-38eb-9ad5-4f812842ae56 | -5.9629 | -43.358501 | 2024-10-17 00:20:59 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 4edc60cd-111d-3362-b8ca-923135c317b3 | -5.9645 | -43.365799 | 2024-10-17 00:20:59 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 43fee2e7-6d83-3792-a6cd-3d23622fd780 | -5.9662 | -43.373001 | 2024-10-17 00:20:59 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 515b6b5d-a29a-3c4b-9441-e89f135f52ac | -5.9531 | -43.360699 | 2024-10-17 00:20:59 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 8811f8b8-dc1c-317c-b4f6-d9ec90153a23 | -5.9547 | -43.368 | 2024-10-17 00:20:59 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| f643f31c-d0a0-35b4-8e12-98d51c48432f | -5.9564 | -43.375198 | 2024-10-17 00:20:59 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 3ca69ddf-1305-3d64-846c-da0b3fcfd07d | -5.9466 | -43.377399 | 2024-10-17 00:20:59 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| ae6b79ab-089d-3e47-9680-66f0514cd32d | -5.9483 | -43.384701 | 2024-10-17 00:20:59 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 296095a3-da52-3ad0-9729-81b09b154c98 | -5.975 | -44.000198 | 2024-10-17 00:21:01 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ed58dbe-6b74-3425-afbb-9b6561c54999 | -5.9766 | -44.007198 | 2024-10-17 00:21:01 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c2963a29-4259-373f-969c-edcb6eb38a9d | -5.6545 | -43.001801 | 2024-10-17 00:21:03 | METOP-B | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 01a6ea3d-6a06-39e3-9963-4d0466a16a9c | -5.6563 | -43.0093 | 2024-10-17 00:21:03 | METOP-B | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 86de9aa1-a3b4-3ac1-a862-61e7ff9759b0 | -5.645 | -43.230598 | 2024-10-17 00:21:04 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1535c3e-5744-312f-9f8c-fd3a1d7ae91a | -5.983 | -45.359299 | 2024-10-17 00:21:06 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eab2a180-6965-3c71-bfba-335c2bcbcf5e | -5.9845 | -45.366199 | 2024-10-17 00:21:06 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c27a38a-6c8a-3a19-beb8-8ac3ac101805 | -5.9861 | -45.373001 | 2024-10-17 00:21:06 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05c0983c-ac3f-3139-a9c2-f033b53e978e | -5.9731 | -45.361401 | 2024-10-17 00:21:06 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d95e1d4-52a0-3e60-96f2-085d9520bc2a | -5.9746 | -45.368301 | 2024-10-17 00:21:06 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6119a562-1592-39d6-bae1-f10fd9bca405 | -5.5412 | -43.905701 | 2024-10-17 00:21:08 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
