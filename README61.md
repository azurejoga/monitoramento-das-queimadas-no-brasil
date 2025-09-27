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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 314e91ac-64dd-3205-8cf0-8fae6818447d | -9.73237 | -48.29639 | 2025-09-27 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| ddfdce4d-ecb5-396d-bffb-d1124ce31758 | -9.04952 | -46.73523 | 2025-09-27 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| cea3b7f6-be88-3c54-99dc-99ebc5f1b32d | -4.75391 | -49.52467 | 2025-09-27 12:36:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 3e52523a-32a0-3e43-86c0-5251dfda2d56 | -7.55695 | -46.70884 | 2025-09-27 12:36:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 6b676d0b-7c9b-37ab-b6ac-0d1552cd8dde | -11.35888 | -45.04613 | 2025-09-27 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 30e6e546-58bb-3124-8394-82756de44cf6 | -8.62102 | -54.9836 | 2025-09-27 12:36:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e3c1be73-8042-3909-af8a-bc5058dbddd2 | -11.44826 | -44.92944 | 2025-09-27 12:36:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| fda316c0-a459-3dea-b914-a92e444c26a3 | -9.34055 | -48.94041 | 2025-09-27 12:36:00 | TERRA_M-T | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| f1a434cb-93ff-3d41-bb1c-32b09a2aede0 | -10.01429 | -46.72307 | 2025-09-27 12:36:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| fd1ae9e9-8076-3f3d-aa3f-122ef9aa1311 | -5.9146 | -42.93341 | 2025-09-27 12:36:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 25.7 |
| 2f727163-4e2a-3318-89db-656da40b76c9 | -8.63777 | -44.85623 | 2025-09-27 12:36:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 7bfa6bbd-c085-304f-8eb6-591a13f0315f | -10.61991 | -53.88215 | 2025-09-27 12:36:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 4d0f537e-b3ac-345b-8dbd-5aa7a2df12f3 | -5.8109 | -42.8161 | 2025-09-27 12:36:00 | TERRA_M-T | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 69.3 |
| 2c9a9bef-27b2-35a6-a2b7-d13aa80653c1 | -8.83128 | -46.25212 | 2025-09-27 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 644d26c6-3a1f-3a1f-adc7-74140a744709 | -10.28979 | -45.21884 | 2025-09-27 12:36:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 8fcf3e1e-74f4-3287-8bc6-e70f919653fe | -11.43597 | -45.00455 | 2025-09-27 12:36:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| badba2f2-4acd-3e5c-94a0-aff1744977d5 | -4.45652 | -44.13407 | 2025-09-27 12:36:00 | TERRA_M-T | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| c26165f2-f2e5-3ac8-8c95-74fa995e76ef | -11.43923 | -44.97699 | 2025-09-27 12:36:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 371a2030-2b47-3d91-963b-222aa6e16557 | -7.22472 | -44.76477 | 2025-09-27 12:36:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| c566a7d6-2296-3649-8d93-550a69fb9c67 | -7.2277 | -44.74229 | 2025-09-27 12:36:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 856c9e0f-e3bd-3595-a1ec-da8c6748d00c | -7.81979 | -46.89066 | 2025-09-27 12:36:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 860c84b1-120c-309d-b043-7ec2c418397d | -9.0533 | -45.53013 | 2025-09-27 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 24.4 |
| e5a30e4d-6217-3fe0-a221-cdf4943615bf | -9.05588 | -45.50911 | 2025-09-27 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 8c4ff07d-fbf5-3d1c-ad31-d7bad6706553 | -10.12255 | -45.32516 | 2025-09-27 12:36:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 22.7 |
| e40c9717-d86e-367d-b7a3-5d8e3dec0f4f | -7.15069 | -45.51515 | 2025-09-27 12:36:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 5eed7735-acc2-3e5c-a02c-42629d6056e9 | -10.86488 | -47.77939 | 2025-09-27 12:36:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| cf4ec42b-63ea-3f2b-a649-be164e27e08e | -9.33898 | -48.95231 | 2025-09-27 12:36:00 | TERRA_M-T | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 7b59b9cb-0f51-3be9-80e0-23e014a763b7 | -11.55662 | -45.28305 | 2025-09-27 12:36:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 1adbf151-e60d-3fb0-8f9f-a4809c769430 | -9.4221 | -47.60194 | 2025-09-27 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| a79b9a13-f168-3e7c-94c5-ef2e98973c46 | -7.23169 | -44.77264 | 2025-09-27 12:36:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| c14907ae-9e99-3567-be8a-20fb76959891 | -7.77894 | -46.93351 | 2025-09-27 12:36:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| d5ebec18-2f99-3e30-b57c-53615fc1dfc5 | -5.76814 | -42.77929 | 2025-09-27 12:36:00 | TERRA_M-T | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 42.6 |
| e501c1d9-7544-3f89-9f38-4e112f7936b9 | -7.63912 | -45.98292 | 2025-09-27 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 4b3961a8-434f-3713-99ee-de30e85d0c94 | -11.36959 | -45.04143 | 2025-09-27 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 1eb46795-fdda-3977-b880-829e57226844 | -9.0439 | -46.72878 | 2025-09-27 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 78b97543-a98c-3e5c-8e7b-6e22213f891a | -9.3514 | -47.61673 | 2025-09-27 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| f2624ef9-1628-32d9-bfd2-83fe5408113c | -11.5397 | -45.30662 | 2025-09-27 12:36:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 6ac60078-42ba-36a7-a82c-bee334cf32cd | -9.03194 | -46.72723 | 2025-09-27 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 9fc75058-b056-3edb-ab49-6461b17bf76b | -7.7769 | -46.94919 | 2025-09-27 12:36:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 0ea9057a-d3f8-3d9c-8130-d129f67f0047 | -11.43931 | -45.01031 | 2025-09-27 12:36:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 48800d6b-ca85-3e57-b9c6-4b932d0a2a29 | -7.3177 | -46.70886 | 2025-09-27 12:36:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 4051d9df-0704-3c21-ba0f-0915829e47c6 | -8.82891 | -46.27037 | 2025-09-27 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 5b68fefc-ac58-3a55-838a-d4584313ed97 | -9.35714 | -47.57234 | 2025-09-27 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 68b35dd6-0e26-3caa-b0be-834f32a8def3 | -9.11483 | -45.87732 | 2025-09-27 12:36:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| b7bd5196-c667-3c22-9dac-e362ab29ae92 | -7.54526 | -46.70735 | 2025-09-27 12:36:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 41887144-9bbe-35d0-83d5-ef5e0fc36312 | -5.51872 | -43.86711 | 2025-09-27 12:36:00 | TERRA_M-T | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 4b99bda6-048a-3e02-956f-4704ad3686cf | -10.01647 | -46.70568 | 2025-09-27 12:36:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 42d16ac8-7272-3d70-a2d6-03624eec3b21 | -10.72084 | -48.00675 | 2025-09-27 12:36:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 2d8f4adb-dfa8-35e1-b6b4-54f350e51f87 | -8.81888 | -46.25061 | 2025-09-27 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 8a22545a-e76b-30d7-a3c0-b722f62c2b76 | -7.30605 | -46.70737 | 2025-09-27 12:36:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| dfdd4901-07cf-396b-b4e9-a4c89ada28e0 | -6.60404 | -44.89922 | 2025-09-27 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 5fa04d10-3958-37d3-8038-1c8bffe76ce6 | -11.59816 | -45.46464 | 2025-09-27 12:36:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 192fb0fa-3b1b-3b1b-bb42-04c507e0075a | -11.34737 | -45.02004 | 2025-09-27 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| e5151d3b-f5dd-34cb-b49c-d1454e24ca35 | -9.88564 | -47.73737 | 2025-09-27 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 52217778-78ed-3937-83a5-0323d026b9fe | -10.41932 | -48.12314 | 2025-09-27 12:36:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5d649470-3eb5-3baa-8bc3-d6582c187825 | -6.49213 | -44.24272 | 2025-09-27 12:36:00 | TERRA_M-T | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 82019719-f326-3f4c-be10-bb2783400314 | -11.03252 | -47.99397 | 2025-09-27 12:36:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| be709b1f-8206-3987-a9ef-ffe6aa31879d | -3.55399 | -49.47486 | 2025-09-27 12:36:00 | TERRA_M-T | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| bd6fe1d7-3f0e-3180-8318-ab78110253e2 | -11.44229 | -44.98339 | 2025-09-27 12:36:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 23ad0af2-79b1-3f1e-947b-50cf67d9ab66 | -11.60097 | -45.44015 | 2025-09-27 12:36:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| f49836c9-c731-3b6b-afe9-f6a71ac948ab | -10.00432 | -46.70393 | 2025-09-27 12:36:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| ac3011f1-56ac-3a12-af33-98bbddb71da5 | -10.69471 | -47.32274 | 2025-09-27 12:36:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a2aa5d6d-fa28-362c-a043-c2b129caa498 | -8.64588 | -44.85043 | 2025-09-27 12:36:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 29.5 |
| c29eaf2b-e7f0-3557-9b88-9f2681a4d1d9 | -10.23342 | -50.25726 | 2025-09-27 12:36:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5f81ce9e-c324-386d-9dd5-53d429d25ec4 | -5.51527 | -43.89251 | 2025-09-27 12:36:00 | TERRA_M-T | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| ed391647-0985-3785-9e5f-ec7cdab13f8d | -11.35539 | -45.03946 | 2025-09-27 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 191.3 |
| b0b78151-5f4e-3cf5-b92e-ae51e5d97928 | -11.6147 | -45.4428 | 2025-09-27 12:36:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 34.3 |
| ae0de6b7-81bb-3e73-a032-1ec3f44557be | -8.16627 | -46.34474 | 2025-09-27 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| d0e7d343-21aa-3a04-a8bd-139a6527ecb0 | -6.04857 | -44.74601 | 2025-09-27 12:36:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 9ee360fc-88bf-3756-bf07-29b0d719236d | -7.05878 | -46.40949 | 2025-09-27 12:36:00 | TERRA_M-T | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 651b5b18-e1ff-3626-afa7-fec555d737b3 | -9.61958 | -47.57947 | 2025-09-27 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 3567411d-22c3-3aab-b57b-b500a7b15ec5 | -9.87953 | -45.91863 | 2025-09-27 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| b6332c20-8784-38d5-8d36-5e82218e0384 | -9.42399 | -47.58705 | 2025-09-27 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 4a67eb7a-8bfd-396b-bcad-7e0254ecc6f7 | -11.5537 | -45.30805 | 2025-09-27 12:36:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 91ad1673-5983-383f-a092-af46b21e10b1 | -5.5219 | -43.87445 | 2025-09-27 12:36:00 | TERRA_M-T | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 4e16a399-82f8-3a11-b954-ed3f0a8061bd | -10.45853 | -53.60049 | 2025-09-27 12:36:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 848d0256-efb3-3acc-9e2a-af7a7078ba27 | -8.47688 | -47.82494 | 2025-09-27 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 78f37053-af79-31bc-82eb-35f3c6d2dc0f | -5.76423 | -42.81007 | 2025-09-27 12:36:00 | TERRA_M-T | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| 009657d4-a3a2-3c0a-9b4c-c71efe22c635 | -9.04169 | -46.74569 | 2025-09-27 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 0d6f4d04-0241-31b2-9735-a703a166f0d7 | -5.80615 | -42.82198 | 2025-09-27 12:36:00 | TERRA_M-T | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| d1171da7-ec66-3baf-8356-01d6e46cb4dc | -6.85249 | -43.17843 | 2025-09-27 12:36:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.0 |
| 542ab6cf-2d63-3576-bb47-52a365c700fb | -9.36453 | -47.60334 | 2025-09-27 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| cdef3bdc-9319-3f7e-9e18-12875a7d6278 | -4.75527 | -49.5149 | 2025-09-27 12:36:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 0d13a6df-3941-3c00-a148-1562644fbf2c | -10.40839 | -48.12164 | 2025-09-27 12:36:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| aa24631e-6f0a-32b9-8823-def716c341bc | -9.88068 | -45.90322 | 2025-09-27 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 746e3cfd-49f6-342f-be09-46fb992ba5ab | -11.54258 | -45.28167 | 2025-09-27 12:36:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 9217f55e-0c3e-360f-9760-542f6e77d9a7 | -8.81651 | -46.26901 | 2025-09-27 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| c74791bb-eccf-37cb-ac46-3b879c476e1f | -7.31363 | -46.71499 | 2025-09-27 12:36:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 5ef47c9f-9695-31dd-9b70-fbe323e22d3f | -8.22487 | -49.40625 | 2025-09-27 12:36:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 86ae37a4-cf27-3e6c-a427-f6da720455cc | -11.36162 | -45.02184 | 2025-09-27 12:36:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 201.4 |
| 07fc9d37-ee29-37f5-b234-aef926af9f0e | -9.38937 | -47.50071 | 2025-09-27 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9a74845a-0836-35fc-8f54-259b6595e928 | -11.6089 | -45.43623 | 2025-09-27 12:36:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| b9409940-19d7-3ee0-b32a-3956342ae1bd | -7.23454 | -44.75002 | 2025-09-27 12:36:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| ca2f2775-4d17-3c33-8135-855d93b79faf | -8.83392 | -46.25871 | 2025-09-27 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| be280be6-8a3a-3b7a-ac0a-ac9d504909ff | -6.2713 | -47.32522 | 2025-09-27 12:36:00 | TERRA_M-T | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 110fa808-dced-3671-849d-15bb1cefbc41 | -9.76028 | -46.13919 | 2025-09-27 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| d7861272-c927-3a5e-9133-772d0e901088 | -11.44551 | -44.92381 | 2025-09-27 12:36:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| ff7033ac-077c-304c-8213-5d983653a3ca | -3.33318 | -50.24774 | 2025-09-27 12:36:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e9d17f97-4550-3e47-8758-7c2dab2c13e6 | -6.57624 | -45.11284 | 2025-09-27 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| bc4d77d6-47d6-3636-938f-078f663055d4 | -8.83613 | -46.2147 | 2025-09-27 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |


[Clique aqui para ver as próximas entradas](README62.md)
