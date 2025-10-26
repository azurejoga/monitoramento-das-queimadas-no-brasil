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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5fa9681e-7326-3b36-8af9-b5ac332c03fe | -5.13196 | -41.19215 | 2025-10-26 04:00:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c68da053-38fc-355e-966a-79e752a3cf39 | -3.71076 | -42.40853 | 2025-10-26 04:00:00 | NOAA-20 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 25b188a5-f57e-3bf1-967a-7fa4d255ec6b | -2.80969 | -49.15248 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 358126ba-cfbe-398e-ab3d-5f81df7f7d68 | -7.61983 | -44.99634 | 2025-10-26 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7bad896-0a25-3019-b2e1-af0bfb2e7974 | -6.54397 | -41.5982 | 2025-10-26 04:00:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9e974e61-d764-381f-8fb3-b08e39730b59 | -7.46291 | -46.64014 | 2025-10-26 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 771b7c28-d555-362f-89f6-76b7e2b48f94 | -6.1641 | -43.13163 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 119273f4-ea06-35bc-b57f-199fb6849603 | -7.09453 | -39.56821 | 2025-10-26 04:00:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 338f2aef-ef13-38f6-b9d2-02a6456f50bd | -6.22398 | -41.38707 | 2025-10-26 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 46ebc8cf-2dd5-3b7c-ac12-78040c97d7cb | -6.13442 | -41.7235 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5b32d6ba-618a-3dff-a629-2a9b3ed16d05 | -7.12461 | -44.85787 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d17efd8-f285-3d50-8b7d-1b61c359fb21 | -5.10058 | -43.19796 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 0652dc50-cacc-3e50-a5aa-4d746479e26c | -6.55195 | -41.59195 | 2025-10-26 04:00:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4e3e5e40-c014-312e-8134-c8122b9dc372 | -6.32449 | -41.87327 | 2025-10-26 04:00:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9f814d5c-3e81-38ce-95d8-4e238acb2c3c | -6.26818 | -44.39502 | 2025-10-26 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b9e4f19-b31e-387c-b67a-656194e38312 | -6.70991 | -42.0493 | 2025-10-26 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| d76c1752-b9c4-302e-8032-2b110b9e10b5 | -7.64232 | -42.31395 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 43051525-0c7c-325e-bd87-ace37e0f683b | -5.76126 | -42.54007 | 2025-10-26 04:00:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2eb9461a-54a4-35f0-8d40-f5f9114afd8e | -5.13139 | -41.19577 | 2025-10-26 04:00:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bf3fbf25-39b7-3004-a0c8-6ba33b3d1ea0 | -9.5436 | -40.64826 | 2025-10-26 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 84eea248-ccd0-3faa-8826-5a3a7ed71d2c | -6.16841 | -41.55804 | 2025-10-26 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bf4c8d7c-44d7-3b92-81aa-76447168c75c | -5.24495 | -45.2106 | 2025-10-26 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 116c857c-4dd7-317d-b09a-da3c6fc33747 | -6.06467 | -42.14863 | 2025-10-26 04:00:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9c614ccc-b5eb-3870-afbb-397d6b2d9d81 | -5.11241 | -43.19543 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 2bdd979c-9ffd-373e-b339-c041d06b22a6 | -4.83971 | -40.71857 | 2025-10-26 04:00:00 | NOAA-20 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| eba803dc-2a53-31e5-8c22-522304946f39 | -3.78342 | -43.4075 | 2025-10-26 04:00:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35343d0f-c9c6-3fb7-b99c-dce42eb5319a | -6.43238 | -42.33325 | 2025-10-26 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f2a2e4db-e568-31e7-9464-c75cef9f5577 | -4.79941 | -47.88839 | 2025-10-26 04:00:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a41139bc-34ba-33e1-8694-33007b0cb43c | -3.12211 | -49.10495 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 345b316c-ed1a-3e3a-85a5-3b35c9172cd5 | -8.23755 | -42.36167 | 2025-10-26 04:00:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e75d876e-e01d-359c-9460-7c7cfb88bab1 | -6.7024 | -42.05195 | 2025-10-26 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2e216c0c-5ac2-309d-8b10-f81e69d7fa11 | -8.78588 | -46.56433 | 2025-10-26 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68cbc60d-b846-34cf-8b77-d3784cda19d0 | -6.98425 | -44.01404 | 2025-10-26 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 46cd5a80-1fff-3c83-9c1f-f8ae7bb8a8d9 | -3.96199 | -45.41811 | 2025-10-26 04:00:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 21d9e39e-6457-379f-931d-147353baa9e4 | -8.15778 | -47.75239 | 2025-10-26 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddefbb34-952e-394c-a19c-eea9fe6d58f3 | -2.32162 | -48.58148 | 2025-10-26 04:00:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e637ff6b-d759-3556-b1cc-97fa53a240f0 | -5.1246 | -41.19473 | 2025-10-26 04:00:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2517eb4a-8fc4-3d8f-8f4e-3e60de59afd9 | -3.46229 | -47.68842 | 2025-10-26 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49925bdd-d180-3d9d-91ac-1646e73f086b | -6.17621 | -41.57449 | 2025-10-26 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 92ec6491-703d-3dbb-a931-0bbb129bab6d | -8.06355 | -40.87493 | 2025-10-26 04:00:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 22676e50-4813-33cd-8b97-03399d637f22 | -3.38248 | -52.37518 | 2025-10-26 04:00:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 13fc3538-4d31-3a5f-8a84-288fdb71adb3 | -6.83223 | -41.55423 | 2025-10-26 04:00:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fefc07ff-2989-3e36-85cf-22665c686737 | -5.11469 | -43.20494 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1aa2563d-c9d1-3759-a218-ef76346f6f74 | -2.63242 | -47.30465 | 2025-10-26 04:00:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d71e7500-cff8-3796-a19b-81a3f69aae78 | -6.36012 | -38.37383 | 2025-10-26 04:00:00 | NOAA-20 | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 36ecfa5d-dca4-3a8e-abf9-a8c436e42e57 | -5.47209 | -40.88746 | 2025-10-26 04:00:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2f2b8baf-e260-31a2-8c8e-fd9216e8ad48 | -5.10285 | -40.64721 | 2025-10-26 04:00:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6e993575-92e8-31e0-a4ca-33ae8edee706 | -8.33157 | -48.18344 | 2025-10-26 04:00:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f3fdac67-f5d9-3851-8dac-9ac1b55a08d6 | -6.23595 | -41.83201 | 2025-10-26 04:00:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 41ff8633-9c48-3caa-bd6e-6db43d501353 | -5.06855 | -40.47561 | 2025-10-26 04:00:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 862d70a2-65e4-3c73-9088-694a434854f6 | -6.82944 | -41.55 | 2025-10-26 04:00:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8eacdad3-9a2a-3fc7-9fc6-9e6789c0b943 | -7.14442 | -44.85083 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 27d534cc-440d-314e-b4db-02bc9e99b9ad | -8.41095 | -46.92142 | 2025-10-26 04:00:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8dbae5d1-b7cb-34af-a9e2-1f3fa953741c | -4.47994 | -48.67698 | 2025-10-26 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 88d295be-b94c-39de-9fd8-ccc349af810f | -8.15289 | -47.74899 | 2025-10-26 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b72cd18-a468-34f2-8000-fe7bc218cc27 | -6.55031 | -41.58045 | 2025-10-26 04:00:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 06d9f4e0-f285-3b04-8a50-fddf3f6927eb | -6.30498 | -42.9582 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82ec69a6-e046-3bc3-99bd-08021b3b572d | -6.55384 | -43.77748 | 2025-10-26 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ac247a4c-91f0-3718-994b-fb8473d26949 | -4.1502 | -47.66264 | 2025-10-26 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f095b0ff-e118-38e8-951b-b3e55afdf3c0 | -3.75796 | -47.57533 | 2025-10-26 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f08a37f9-7c55-3414-9ef2-2d557a56ecf5 | -2.32592 | -48.58982 | 2025-10-26 04:00:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f1417e0-5154-351c-a720-eb2bbeb473aa | -5.57199 | -40.92084 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f20f89ce-8db3-3089-92f2-a8c52f14e31d | -4.87141 | -48.65098 | 2025-10-26 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b9f76f1-975f-3329-9701-4724f19588c0 | -3.83654 | -50.20569 | 2025-10-26 04:00:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e927bed0-1efe-3461-80fc-499e7456294e | -6.89202 | -38.28047 | 2025-10-26 04:00:00 | NOAA-20 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c8df1342-e23e-3e34-9e8c-cd5b5bf0fdb1 | -3.93998 | -42.47286 | 2025-10-26 04:00:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0860061a-17db-36d4-abb4-f5f15cf41d81 | -5.88894 | -49.66123 | 2025-10-26 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 220ab500-80f2-3065-b864-33e687956bc6 | -6.46977 | -47.56059 | 2025-10-26 04:00:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 92926d87-308c-3ad8-aaa6-bd50717fefee | -8.0493 | -46.74568 | 2025-10-26 04:00:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c3d2217f-6f33-32ab-a762-c3cbf1a0e344 | -5.70793 | -49.27694 | 2025-10-26 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ac169754-0823-3fe7-938e-d587f2a5955f | -5.54556 | -41.23835 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d565c249-4414-3247-b8c8-c75dccb488f9 | -5.58918 | -41.31997 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d370907a-dcd8-393a-a7b9-4c7859e39199 | -6.20157 | -41.52575 | 2025-10-26 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d377dd9c-7197-3831-ab50-c35e20330633 | -5.59258 | -41.3205 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 14a198eb-408a-32c7-9030-6ce19e796e70 | -8.66776 | -44.76762 | 2025-10-26 04:00:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eee900f2-8586-3a0c-9880-e041ac7dc483 | -7.88159 | -45.71296 | 2025-10-26 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 395c7d04-7947-3a21-970d-9a56961d6418 | -6.60312 | -42.05978 | 2025-10-26 04:00:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 68b3f9a5-a14a-3340-ae52-9ba3c14494bf | -5.43184 | -40.8811 | 2025-10-26 04:00:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 467ced36-39dd-31f1-8b9a-ebb02a5a22e7 | -7.29282 | -38.13764 | 2025-10-26 04:00:00 | NOAA-20 | ITAPORANGA | PARAÍBA | Brasil | 2507002 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9f708040-94cc-3b50-b9fe-03fa6d04c9c9 | -8.15591 | -41.10523 | 2025-10-26 04:00:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 38128ca5-dba4-3290-b76a-3f96375da734 | -4.90297 | -43.24237 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dadb607b-ea3c-3a85-9d9d-d2abcb38eb53 | -5.40954 | -45.28865 | 2025-10-26 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a657ed62-c85c-3b0c-bfd5-a19010c9ef27 | -8.04593 | -41.11346 | 2025-10-26 04:00:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b9b9c6a1-48be-307e-8751-9550025d9afa | -6.79036 | -45.41046 | 2025-10-26 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 62fcb1be-e264-3d93-bf1a-004120346949 | -5.01858 | -37.82822 | 2025-10-26 04:00:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 503c5947-73c5-355d-9717-8c2e1549e927 | -5.8829 | -43.93609 | 2025-10-26 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 760ea1cf-7b5f-32a7-ba75-11dbf8695f6e | -6.70646 | -42.04873 | 2025-10-26 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 0782bedb-001b-3a3f-884b-2c22e27b683e | -7.16437 | -45.63844 | 2025-10-26 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8862ff6-512f-3603-83d5-473e8eb76018 | -6.58263 | -48.77028 | 2025-10-26 04:00:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 249ff872-945d-3e79-adb6-80e7a6f3894e | -3.82581 | -41.11497 | 2025-10-26 04:00:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| c106f109-2890-3115-a14c-e1790c7d819d | -7.49314 | -41.76101 | 2025-10-26 04:00:00 | NOAA-20 | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a28c9d6d-2f91-3d40-bb8e-87b8e3d0f641 | -6.47828 | -44.1447 | 2025-10-26 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 31b03374-cd21-3287-a30d-23af958e8847 | -4.32033 | -41.79215 | 2025-10-26 04:00:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 48b5f56c-be9c-38bc-8538-590a9b596a9a | -6.70767 | -42.04122 | 2025-10-26 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 5813f29b-b016-36cd-bebf-5a88091ac922 | -4.09362 | -51.05747 | 2025-10-26 04:00:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6664f55f-2e3a-34f6-958b-4fe9dc00ce67 | -9.51916 | -40.30902 | 2025-10-26 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 44e023a0-8185-36b9-b08d-dadd4b5835a0 | -5.7128 | -49.28147 | 2025-10-26 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2031deb-3f09-3b5b-b219-c5296b8d41d8 | -5.86682 | -48.26276 | 2025-10-26 04:00:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0141ee6-d884-3647-b0cf-20995550f4cd | -3.73161 | -42.30121 | 2025-10-26 04:00:00 | NOAA-20 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0d207521-a718-3858-a831-dcf27a68d21c | -4.88963 | -43.25391 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README15.md)
