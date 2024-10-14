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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6902bc92-7b82-3604-a999-f24dd70a8a6a | -18.2368 | -56.4597 | 2024-10-14 00:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.0 |
| db33b511-d775-3505-9662-d8a0c8f3af7a | -18.2371 | -56.4389 | 2024-10-14 00:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.0 |
| 702c2300-50c7-3b0d-9085-5c5df43f46c6 | -18.2566 | -56.4571 | 2024-10-14 00:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.9 |
| 7bb3eff3-4ae7-39cb-b6c9-affbe7cff898 | -2.4344 | -46.9195 | 2024-10-14 00:15:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| a8d7532b-993a-3442-a4a0-78379a977a96 | -2.4529 | -46.919 | 2024-10-14 00:15:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 0aeae856-3cbf-326e-b550-9417199fca91 | -2.6117 | -49.1198 | 2024-10-14 00:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 4e5b7969-a1a8-3b64-a6b1-79fac8f171fe | -2.6118 | -49.0985 | 2024-10-14 00:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 907a2c85-83cc-395f-ab6d-c18544f2ed7d | -3.1791 | -50.476 | 2024-10-14 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| bb43cdbd-ae4b-3b34-81af-197249e27ed6 | -3.1792 | -50.4551 | 2024-10-14 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 8c3fdacb-802a-308b-a465-dff4cb7189d4 | -3.2889 | -42.8561 | 2024-10-14 00:15:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 49c7e174-3bda-3f56-af46-be942543869d | -3.289 | -42.8327 | 2024-10-14 00:15:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 74a2084a-8dae-3b63-b551-db66a14bc6c4 | -3.3076 | -42.8553 | 2024-10-14 00:15:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 215.5 |
| 8a267cd1-e3f0-3224-b908-d356e606d897 | -3.3077 | -42.8318 | 2024-10-14 00:15:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 335.1 |
| 14b8d9ae-e94f-355f-9a80-cbda35c6ee30 | -3.1982 | -50.3077 | 2024-10-14 00:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 67da0cbf-fe8f-3665-aa28-bed4a7d64cea | -3.3274 | -50.3245 | 2024-10-14 00:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 18513b30-9187-3387-a342-7d8637043783 | -3.3275 | -50.3035 | 2024-10-14 00:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| c1031f82-e116-3557-b94d-0f2a25d108c9 | -3.3643 | -50.3233 | 2024-10-14 00:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| d03396e0-44d0-350a-8670-96d039afa095 | -3.4279 | -52.782 | 2024-10-14 00:15:26 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| d5a7526c-78b5-36d6-9674-6cb0d13984a6 | -3.428 | -52.7616 | 2024-10-14 00:15:26 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 80c12262-2dc3-39bb-ba07-28f4f0a40c2a | -3.8723 | -52.2769 | 2024-10-14 00:15:28 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| fc7f1285-99a3-3670-b7e0-91e46ff1e4a7 | -3.9103 | -48.3466 | 2024-10-14 00:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| ce10cf00-7f8a-3991-94ad-537d4e757948 | -4.1145 | -48.2947 | 2024-10-14 00:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 23d189be-2c68-3053-b9ff-40ea4be64b94 | -4.1146 | -48.2731 | 2024-10-14 00:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| d570e836-97f4-315f-a53e-3ee6d951c5c6 | -4.3428 | -50.5172 | 2024-10-14 00:15:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| fc89cb8c-b2a1-3bd9-8af3-afce7d0772ec | -4.343 | -50.4962 | 2024-10-14 00:15:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 84205555-9663-3d8e-b2d3-689db126008c | -4.6197 | -44.8626 | 2024-10-14 00:15:32 | GOES-16 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 24b4d167-3ac0-3d9b-bf1f-073ebd11e909 | -4.9097 | -46.0163 | 2024-10-14 00:15:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 77.5 |
| cb96de31-ba8b-3b0f-8b1b-cc5b66452c9f | -4.9099 | -45.994 | 2024-10-14 00:15:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 75.0 |
| f89fda8e-955c-3118-967e-7f9e8bf3d248 | -5.0625 | -48.0745 | 2024-10-14 00:15:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 45.0 |
| d1e7180d-af9a-353a-b657-1208df957397 | -5.0627 | -48.0528 | 2024-10-14 00:15:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 50bf94f5-9ed2-397a-b41e-cfc2c1f30d6b | -5.7065 | -57.5243 | 2024-10-14 00:15:39 | GOES-16 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 011c7804-4372-3b93-9098-cc980535ad75 | -6.1342 | -42.7906 | 2024-10-14 00:15:41 | GOES-16 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| d26b2a42-116a-32b4-a9e9-f5151df1e2e6 | -6.3749 | -59.9936 | 2024-10-14 00:15:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 5c10ced6-19e1-34d3-9a74-1b73ce75ca4a | -6.3933 | -59.9929 | 2024-10-14 00:15:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 0fa789fb-154c-3992-814b-4a42ce399a0c | -7.9437 | -49.0623 | 2024-10-14 00:15:51 | GOES-16 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 1776d89b-b7f0-39bb-803b-021093993634 | -7.9623 | -49.0823 | 2024-10-14 00:15:52 | GOES-16 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 01de889b-9112-3138-ae89-5c3cbbfc3da0 | -7.9625 | -49.0607 | 2024-10-14 00:15:52 | GOES-16 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 279.1 |
| a456ba68-8f67-3599-8718-5a2b78e013e3 | -7.9627 | -49.0392 | 2024-10-14 00:15:52 | GOES-16 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 79365e5c-06d5-3c19-952f-4b18155fe1e2 | -7.9418 | -63.6365 | 2024-10-14 00:15:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 91da65f8-73fe-38bd-b463-cc5b59979a69 | -7.9419 | -63.6177 | 2024-10-14 00:15:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 20f6a106-c369-364f-bff4-94f9e03e10b3 | -7.9603 | -63.6359 | 2024-10-14 00:15:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 8c02bfa1-accd-3593-8732-415301377585 | -7.9604 | -63.6171 | 2024-10-14 00:15:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 1d15dce1-da6f-353e-8940-401e752f331c | -8.3207 | -42.7394 | 2024-10-14 00:15:53 | GOES-16 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| f1fff6a8-aa41-3548-921b-27d635ba45fb | -8.3396 | -42.7372 | 2024-10-14 00:15:53 | GOES-16 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 69.6 |
| 71faafb5-1125-3f64-b37d-f1ad28dd72f9 | -8.5097 | -41.398 | 2024-10-14 00:15:54 | GOES-16 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 62.6 |
| c65bb277-2435-399e-a694-85a34bbfbd48 | -8.4734 | -48.6276 | 2024-10-14 00:15:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 8e914344-87bd-3fc8-8cc3-fd491cb2b3f1 | -8.7377 | -63.4952 | 2024-10-14 00:15:57 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 8deff9cf-5c8f-30b7-98cf-59e5d1315c4d | -9.1021 | -47.9355 | 2024-10-14 00:15:58 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 4b53a278-4bc9-3b84-98e0-07ea762c293e | -9.1042 | -61.1811 | 2024-10-14 00:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 80b3346f-1a3c-32cb-ba94-bead05611677 | -9.1043 | -61.162 | 2024-10-14 00:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 106.6 |
| dcb5bc62-b52a-38dd-ba6b-bd3f1d94e51b | -9.6928 | -47.4774 | 2024-10-14 00:16:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 5ccff961-54d0-3af7-b7dc-99f8719dc9ef | -10.0622 | -44.2391 | 2024-10-14 00:16:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 140.6 |
| e0a3cffd-881e-33e6-b347-efef916391a8 | -10.0626 | -44.2158 | 2024-10-14 00:16:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 6f009a73-39dc-348d-9ce6-f05aa1310633 | -10.0629 | -44.1925 | 2024-10-14 00:16:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| ed8fc611-0dda-3cc4-b074-1080fe42d64f | -10.0813 | -44.2366 | 2024-10-14 00:16:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 193.2 |
| 71b558ab-55d7-3bf6-bfd2-21c3c54b6430 | -10.0816 | -44.2133 | 2024-10-14 00:16:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 181.6 |
| 0ed58cc0-07be-3625-b127-68fca24abf35 | -9.9973 | -47.3329 | 2024-10-14 00:16:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 8a932a14-1431-3000-916d-3b33d33ca133 | -9.9976 | -47.3107 | 2024-10-14 00:16:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| e4101a52-0d2b-3a96-8a20-151268b6b58d | -10.016 | -47.353 | 2024-10-14 00:16:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 722614e7-2842-357b-861d-c9241a32fd6f | -10.0163 | -47.3308 | 2024-10-14 00:16:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 199.9 |
| 605d5b72-7a76-3e80-b345-78499df2d3ca | -10.0166 | -47.3085 | 2024-10-14 00:16:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 9c803626-53d7-3cf9-adec-3fe1d4bac2dc | -10.0352 | -47.3286 | 2024-10-14 00:16:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| b0538c1e-6cb2-3303-bf0c-df825ae0c6d8 | -10.2641 | -47.2134 | 2024-10-14 00:16:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 6e8cd8fb-6b20-3f69-842e-97f50a035af9 | -10.2828 | -47.2334 | 2024-10-14 00:16:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 88aa3c84-d6e0-3d63-affc-4de5df1ccafc | -10.2831 | -47.2112 | 2024-10-14 00:16:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 171.4 |
| c177a9fc-48a9-35c3-873d-cd57ff15f97a | -10.4313 | -44.9541 | 2024-10-14 00:16:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 85ca474b-c4ef-30d7-9d3a-45ce8e3b8ee8 | -10.4317 | -44.931 | 2024-10-14 00:16:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| d3585213-04b5-3cc1-b928-fd9cba1ce680 | -10.4918 | -42.433 | 2024-10-14 00:16:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 123.5 |
| 3e163c36-c5d3-3726-8d35-6bfd0e882f21 | -10.4453 | -61.2664 | 2024-10-14 00:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 93f32943-c063-3570-b704-78060f994eb1 | -11.1705 | -39.894 | 2024-10-14 00:16:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 53.3 |
| a2ced410-9a2a-34f1-b030-3e40c25592e5 | -12.0925 | -50.7023 | 2024-10-14 00:16:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 92356bc1-9075-31be-bfd5-a4bae4c54020 | -12.0928 | -50.6809 | 2024-10-14 00:16:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 199.9 |
| f763c9e3-4627-3a1e-a66e-aaf84ed92ee7 | -12.1115 | -50.7001 | 2024-10-14 00:16:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| ea8b945b-3454-3290-a65e-dca13360dbae | -12.1119 | -50.6786 | 2024-10-14 00:16:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 113.5 |
| f11ac32c-c56b-34dd-a0db-8fb54e633fa7 | -12.4981 | -63.0148 | 2024-10-14 00:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 1e9ced98-d5b5-32b3-8504-8f4b2612fcb0 | -12.4983 | -62.9956 | 2024-10-14 00:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 3cd24e8d-ccb4-306b-a2db-77d2562b1169 | -12.8699 | -53.5423 | 2024-10-14 00:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 39c66949-c5ce-3b0e-be9b-3fc16774bd40 | -12.8702 | -53.5215 | 2024-10-14 00:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| b22835ac-ded8-3b58-b1ef-5a18cfea3094 | -12.889 | -53.5402 | 2024-10-14 00:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 0451d5bc-8c12-3e20-9dc8-5a248cc471a0 | -12.8893 | -53.5194 | 2024-10-14 00:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 6d387264-ffc6-366d-9ed2-fe95c2eee212 | -14.55 | -43.127 | 2024-10-14 00:16:27 | GOES-16 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 9bcf1b0b-c7b1-347a-94fe-3f3401e601f7 | -17.0001 | -57.4381 | 2024-10-14 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.7 |
| f222785e-2129-3de4-8c35-8e46533c5033 | -17.0004 | -57.4176 | 2024-10-14 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.6 |
| c4b22c2b-f7a1-3cc6-9ccd-e10f95214d3a | -17.0197 | -57.4358 | 2024-10-14 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.4 |
| 0d4cd5b5-a0d7-3740-9ff0-93f9e48e940c | -17.02 | -57.4153 | 2024-10-14 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.4 |
| e87e2a28-88e7-36f7-bde8-086798abf5ac | -17.0626 | -56.01 | 2024-10-14 00:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 56.0 |
| 5f225026-662e-395f-bba8-39cfe8f53bfa | -17.0823 | -56.0076 | 2024-10-14 00:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.7 |
| ec273eeb-7d75-3a69-acc8-4e1d81013beb | -17.0826 | -55.9868 | 2024-10-14 00:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 59.9 |
| a1e81ec7-37a4-39dc-83a3-9340919a81a3 | -17.1267 | -56.8693 | 2024-10-14 00:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.3 |
| 944c4f3d-d2c7-3034-8e9e-bc6ab20b4cd3 | -17.1464 | -56.8669 | 2024-10-14 00:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.2 |
| 28c2741c-530c-357a-8cc9-9a58391cafb3 | -17.6471 | -56.3084 | 2024-10-14 00:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.0 |
| cf2b8a6c-84d8-390a-b974-37b74c6717c3 | -17.6474 | -56.2876 | 2024-10-14 00:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 01cbc388-42a9-360d-92d0-43c259d6e8e3 | -17.6668 | -56.3059 | 2024-10-14 00:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.2 |
| a31939c0-0218-378c-bba3-7d84b3bf7066 | -17.6873 | -56.2617 | 2024-10-14 00:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.2 |
| 256fef25-a982-36bf-9ee7-fe2ecd8359c9 | -17.6876 | -56.2409 | 2024-10-14 00:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.7 |
| 3136ba40-7ddf-309e-8087-24e2ba3b4d8c | -17.7074 | -56.2383 | 2024-10-14 00:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.6 |
| 32aede4a-1355-3868-a508-58633d2808e7 | -17.7264 | -56.2774 | 2024-10-14 00:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.7 |
| 2f75202a-4e3c-3e1e-972b-7c90a349748e | -18.0811 | -56.314 | 2024-10-14 00:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.6 |
| 80a40a8c-bad7-3579-94b0-beb0d534ab9f | -18.2147 | -56.5873 | 2024-10-14 00:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.8 |
| 0ccbecea-56c2-39e0-a133-e4604c86d74c | -18.2346 | -56.5847 | 2024-10-14 00:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.3 |


[Clique aqui para ver as próximas entradas](README3.md)
