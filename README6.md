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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 612a8c7e-68e1-35cc-ba99-e47fae28c7ee | -11.1987 | -47.857201 | 2024-10-14 00:36:59 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 762ff9cb-c878-3764-ac02-a92be196914d | -11.0432 | -47.424599 | 2024-10-14 00:37:00 | METOP-C | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c13e15b0-2d02-3900-ac66-6ed33c08eb59 | -9.3741 | -40.411999 | 2024-10-14 00:37:01 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b2bf6fb4-c5fd-3607-b919-cb54e4de018e | -9.3765 | -40.4221 | 2024-10-14 00:37:01 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 13c64016-789a-3f15-883a-3030bf66ae36 | -10.4371 | -44.935501 | 2024-10-14 00:37:01 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e0c75589-3dad-35f0-bfba-e390149fd202 | -10.4387 | -44.942402 | 2024-10-14 00:37:01 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5d8fdde5-8216-38b5-b377-9bea6fe22e60 | -10.4273 | -44.937801 | 2024-10-14 00:37:01 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b1ea1a10-ec92-3486-9922-527a5d9f26a4 | -10.4289 | -44.944698 | 2024-10-14 00:37:01 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c90f0177-cb48-3e74-90f2-28933d19793e | -10.7578 | -46.733398 | 2024-10-14 00:37:02 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 34b0e854-d9d1-3cb4-af59-e8add6b8af39 | -10.1139 | -43.929798 | 2024-10-14 00:37:02 | METOP-C | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7d2852f2-7525-34e5-8a71-b44b878a7f61 | -10.1156 | -43.936901 | 2024-10-14 00:37:02 | METOP-C | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 629b0056-fda1-34cc-8dcc-a12e84f1487c | -10.1172 | -43.944 | 2024-10-14 00:37:02 | METOP-C | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b48210cd-8729-3c29-b2c9-b89c3d313603 | -10.1188 | -43.951 | 2024-10-14 00:37:02 | METOP-C | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bdadf8b0-ea2c-3183-b855-6ad22623a39e | -10.968 | -47.786701 | 2024-10-14 00:37:03 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4d7bd99e-a383-31f8-a66f-0243d4f5591f | -10.9565 | -47.780701 | 2024-10-14 00:37:03 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ffa1496b-1d30-3bce-a508-03839c11c47f | -10.9582 | -47.788898 | 2024-10-14 00:37:03 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b2b96c6b-884a-333e-b6c3-1125cdda42d4 | -10.9467 | -47.782799 | 2024-10-14 00:37:03 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ceb9c1d-2936-3679-a597-951fd8997e03 | -10.9484 | -47.791 | 2024-10-14 00:37:03 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 54c1a065-44c9-3658-bbcc-e8b3809245af | -10.1058 | -43.939098 | 2024-10-14 00:37:03 | METOP-C | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0da723fc-8020-3a03-8830-49e7def25a45 | -10.1074 | -43.946201 | 2024-10-14 00:37:03 | METOP-C | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5a746556-e034-3ef9-92d0-2c570edc3942 | -10.109 | -43.9533 | 2024-10-14 00:37:03 | METOP-C | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2d0579ed-59c6-3c50-bfc7-e9086f4c25ec | -10.1107 | -43.9604 | 2024-10-14 00:37:03 | METOP-C | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3f45bf70-1d88-31a5-90c6-32a674adae13 | -10.9379 | -47.9314 | 2024-10-14 00:37:04 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2f8fd0c3-c502-3be6-8e1e-e00901e93627 | -10.9397 | -47.939701 | 2024-10-14 00:37:04 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec2b9518-65aa-348f-a37b-aa2136d1e796 | -10.0729 | -44.1992 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0ead344e-a337-3a4c-9579-eee17654c715 | -10.0745 | -44.2062 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| be52cac0-f32b-346d-812e-9376d64b4b1f | -10.0761 | -44.2132 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 92f61b19-dbf3-3a4d-a448-a3fe75824f5a | -10.0777 | -44.2202 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a832e5ac-69a1-3195-85d9-02c68dc7260e | -10.0793 | -44.2272 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9ac22142-3421-3f30-802a-d236a5050969 | -10.0809 | -44.2342 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 109c3bf0-a2d8-3855-9dc2-43dd5c50a9b4 | -10.0826 | -44.241199 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a6b43afc-c427-39f7-8816-efd9d586dcdf | -10.0615 | -44.194401 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a4200e7e-ba9f-30c9-b8d7-7d07f8864363 | -10.0631 | -44.201401 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b3c41e52-692d-3d38-85bf-0e53adfa7454 | -10.0647 | -44.2085 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0234a32c-e6eb-3ff5-9d99-61aae6639873 | -10.0663 | -44.2155 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dc522172-584a-333a-b49a-98e4adb739d7 | -10.0679 | -44.2225 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| de8a3380-8fe6-3ece-b81f-4677079e2f46 | -10.0695 | -44.2295 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3f699a5c-f803-3c5a-93c5-c87a686a6ad3 | -10.0711 | -44.2365 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 18644e11-c983-36c5-ac74-420b33aba9e9 | -10.0728 | -44.2435 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cbf62c5a-1119-3012-9221-a2ddb6be0ea2 | -10.0517 | -44.196602 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e34a44e3-7b74-3233-ba10-09b1cab2dfe0 | -10.0533 | -44.203701 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| da1b62c2-52da-37cb-abb7-2579392866df | -10.0549 | -44.210701 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 13abcadf-2d3b-3c5b-9234-10952c9e706f | -10.0565 | -44.217701 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8691b198-d391-35f0-82d9-bbe20355443d | -10.0581 | -44.224701 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2a765327-f201-3882-b7e8-3ea6d83bbd80 | -10.0597 | -44.231701 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 711e5228-000c-3d1d-b3fd-8afca539099f | -10.0613 | -44.238701 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5a3663b0-a9aa-3207-b31c-294fa17fe260 | -10.063 | -44.245701 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 941c063b-4e21-3b45-8f40-84236ce82481 | -10.0646 | -44.252701 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| de8f84da-cbff-3edf-8755-509c616a915c | -10.0697 | -44.185101 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d6d13186-f007-3fe5-b432-0ca3ff02d1c7 | -10.0566 | -44.173401 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bc43b469-2ab7-3570-829c-851f46d2e0a9 | -10.0582 | -44.180401 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 57526d30-3186-3782-bd99-329036314f59 | -10.0599 | -44.187401 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 57daadfe-c75d-3e18-8a11-f0d448d192d9 | -10.0468 | -44.175598 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fa467760-ff0d-31ba-a429-cd64e8b7eaba | -10.0484 | -44.182598 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b895103f-8cc7-3fa7-81c8-b5602c037967 | -10.0501 | -44.189602 | 2024-10-14 00:37:04 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ae98baa9-f52d-36b8-a689-ddd97718fe8e | -10.8398 | -47.8577 | 2024-10-14 00:37:05 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 500e0aba-4ad4-3eea-8722-d33f45f90ec9 | -10.8416 | -47.865898 | 2024-10-14 00:37:05 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 842bccd1-cd38-3bb9-8e91-d8adb89c3c89 | -10.8434 | -47.8741 | 2024-10-14 00:37:05 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 302c2e52-21c4-32d6-b74b-10174c1e1f19 | -10.8452 | -47.882401 | 2024-10-14 00:37:05 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e791d8d-3b82-3f33-9fc3-610dd37477f5 | -7.7906 | -35.078999 | 2024-10-14 00:37:05 | METOP-C | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8172ed33-fc22-3d17-bbd1-d0a167c104c9 | -10.0419 | -44.198898 | 2024-10-14 00:37:05 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 16eb43f5-b464-3461-ad5f-e8ea452970fa | -10.0435 | -44.205898 | 2024-10-14 00:37:05 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c4a815d3-00d9-3138-83aa-aac25c3b61b5 | -10.0451 | -44.213001 | 2024-10-14 00:37:05 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 77c14939-a5f2-31b7-81cd-769d7523796c | -10.0467 | -44.220001 | 2024-10-14 00:37:05 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ba2d9fb2-5387-3a04-82c2-b7796557f840 | -10.0483 | -44.227001 | 2024-10-14 00:37:05 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a362b985-08fd-3864-bb3b-6a26dea07963 | -10.0499 | -44.234001 | 2024-10-14 00:37:05 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 161d96c9-210a-3637-9c94-5fa064e6bd64 | -10.0353 | -44.215302 | 2024-10-14 00:37:05 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cd8e8d5b-803d-3495-bae6-67284227cbe9 | -10.0403 | -44.191898 | 2024-10-14 00:37:05 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 405cdc08-dd5e-3c42-8289-74d19ec2573b | -10.0753 | -44.7048 | 2024-10-14 00:37:06 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f0a3bc07-0f32-312d-b501-059af26980b8 | -21.8635 | -48.9814 | 2024-10-14 00:37:07 | GOES-16 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.8 |
| 2c76879e-6efe-37a0-b827-92ece33771a3 | -11.3985 | -51.226898 | 2024-10-14 00:37:07 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ed9eb522-64e5-31d1-affc-346210fda388 | -10.3463 | -46.593102 | 2024-10-14 00:37:08 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d310fd5e-e99a-315c-8dfc-ed4c809771c1 | -10.3332 | -46.5807 | 2024-10-14 00:37:09 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7229daa-7770-33be-b11d-47306c0f4c59 | -10.3348 | -46.588001 | 2024-10-14 00:37:09 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b7aaf636-2258-3e28-9278-cdcfb6ac89c8 | -10.3365 | -46.595299 | 2024-10-14 00:37:09 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9be3ff38-12c7-3628-b3b4-0006a51cff36 | -10.3218 | -46.575699 | 2024-10-14 00:37:09 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a09a45e9-423b-3e38-a6f5-6b5627fc691b | -10.3234 | -46.582901 | 2024-10-14 00:37:09 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 51a19a72-f7b1-3976-b148-03929cf50a23 | -10.325 | -46.590199 | 2024-10-14 00:37:09 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 857f3e03-49a8-3906-83df-38e8465635ca | -10.0018 | -45.151402 | 2024-10-14 00:37:09 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f7807594-37a9-3843-9eba-3342050cb96c | -10.0034 | -45.158298 | 2024-10-14 00:37:09 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 76943024-6a87-3361-8d0c-c96c86bf466b | -9.992 | -45.153599 | 2024-10-14 00:37:09 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 185e7af8-9d93-3022-9bc1-79b639996ecf | -9.9936 | -45.1605 | 2024-10-14 00:37:09 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a4613669-02fe-31fb-ba2e-2a8d38047840 | -7.4861 | -34.892502 | 2024-10-14 00:37:09 | METOP-C | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 39bc0285-4c14-304e-993a-72eb4bcba4f8 | -10.4712 | -47.861 | 2024-10-14 00:37:11 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1df5b8ce-de93-3dfc-8255-f0a9f0aee3e2 | -10.4614 | -47.863201 | 2024-10-14 00:37:11 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e234124-e07a-3180-99a0-19f7408fb792 | -9.8233 | -45.046501 | 2024-10-14 00:37:11 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0c92a135-fae3-3655-9d95-ec5a6383dae3 | -9.8249 | -45.053398 | 2024-10-14 00:37:11 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9a7025d6-e604-3415-99f6-5156065aae02 | -10.2756 | -47.202999 | 2024-10-14 00:37:12 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9df6f12a-35e5-3313-89f4-530006ac35bb | -10.2772 | -47.210602 | 2024-10-14 00:37:12 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec34bb84-1928-3623-85b4-bdc024e3c8b5 | -10.2789 | -47.218201 | 2024-10-14 00:37:12 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 52a7e1f0-9685-34a5-ac2a-38242f4390a9 | -10.2674 | -47.212799 | 2024-10-14 00:37:12 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f69fcba0-a281-307d-8ce0-a4e79bd5f804 | -10.2495 | -47.224701 | 2024-10-14 00:37:12 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 17c1fe57-2666-3331-8529-17d33029bde1 | -9.5809 | -44.481899 | 2024-10-14 00:37:13 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7fe6de50-75cf-3702-af87-6635be8e8f5d | -9.5694 | -44.4772 | 2024-10-14 00:37:13 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 91e9a810-7097-3cb8-b7bd-0ab1efbbb299 | -9.5711 | -44.4841 | 2024-10-14 00:37:13 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d6a4a907-71e9-3b74-b127-0c632ebbe637 | -9.6655 | -45.213299 | 2024-10-14 00:37:14 | METOP-C | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b9885a9b-bd55-3054-994f-3b7d0b43cd79 | -9.667 | -45.2202 | 2024-10-14 00:37:14 | METOP-C | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 76a56a8b-0c2a-33bb-a347-0f96fd3c1af5 | -9.4496 | -44.1357 | 2024-10-14 00:37:14 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6860ba35-650e-3aed-9cf2-e4cc093c0bcf | -9.4512 | -44.142799 | 2024-10-14 00:37:14 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9b57762a-7be1-32b5-9b69-093bf7bfba95 | -9.4528 | -44.149799 | 2024-10-14 00:37:14 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
