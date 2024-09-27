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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 873dc207-7347-3286-894f-def1e763b9e6 | -8.0886 | -49.5224 | 2024-09-27 13:05:52 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 8a142511-711b-39d0-a8ae-bff017b809e8 | -9.4168 | -51.4636 | 2024-09-27 13:06:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| c054045f-8adc-3810-ba0c-026ff043f7ac | -9.417 | -51.4426 | 2024-09-27 13:06:00 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 147.3 |
| 4c257f93-30dc-37dc-b436-65feeb8eb9ac | -9.6018 | -50.1352 | 2024-09-27 13:06:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| cd837062-f929-34c9-a919-c475c17a6645 | -9.5829 | -50.137 | 2024-09-27 13:06:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 353a93c6-035e-30c5-98c3-1f6a68407705 | -10.0134 | -53.4875 | 2024-09-27 13:06:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| f4588fac-5d02-310a-b747-966ead738df2 | -10.0136 | -53.467 | 2024-09-27 13:06:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 152.1 |
| 6ad6602e-bfcd-3e9f-a423-a2304af6ce41 | -10.0139 | -53.4464 | 2024-09-27 13:06:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 811.2 |
| af758cbb-b24f-34b0-bfa2-e6930506ef70 | -10.0322 | -53.4859 | 2024-09-27 13:06:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 134594c8-faca-378e-a17c-607fcf971bf7 | -10.6438 | -45.9544 | 2024-09-27 13:06:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.3 |
| eceec29b-67c1-3a77-aa54-39668166607c | -10.6434 | -45.9772 | 2024-09-27 13:06:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 5426eeb3-dc13-3ee8-803f-dd4a70576262 | -10.6844 | -51.0059 | 2024-09-27 13:06:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 29a46cdb-08f6-3927-ae3b-dd4a1a321dbf | -10.6846 | -50.9847 | 2024-09-27 13:06:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 254.9 |
| e986cc16-4852-3691-a090-d4a7fabeab54 | -10.9148 | -45.669 | 2024-09-27 13:06:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 183.8 |
| 3d2a6e21-f76d-34ab-a951-66d514e67b7a | -10.942 | -50.1478 | 2024-09-27 13:06:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 28a42881-b873-3014-a10a-7cde29074c5b | -10.9152 | -45.6461 | 2024-09-27 13:06:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 3e51db83-8a5d-3714-a97d-a5400e0f499d | -11.0976 | -46.1446 | 2024-09-27 13:06:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 751d4c20-34ee-3f3c-8167-3d12b341a45b | -11.2025 | -45.5616 | 2024-09-27 13:06:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| c54b2188-ce24-3e92-b696-ad30456db6f2 | -11.0972 | -46.1673 | 2024-09-27 13:06:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.6 |
| b62270fe-2fb0-336f-aa9c-ee2619ad8e81 | -11.1219 | -50.8328 | 2024-09-27 13:06:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 4cf3f863-1eb2-3452-bb74-dcbae2efb69b | -11.1409 | -50.8307 | 2024-09-27 13:06:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 3e96c283-568c-3888-90d1-8d4240d25979 | -11.2531 | -47.1366 | 2024-09-27 13:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 7fb8f4cd-85d7-3480-afdc-9b7cf4e14997 | -11.2721 | -47.1341 | 2024-09-27 13:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| f201bbc2-d357-33e8-b335-8e8192359e90 | -11.2534 | -47.1142 | 2024-09-27 13:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 9ea93818-2e2a-36c7-9f62-4d70709a2e43 | -11.2695 | -46.1216 | 2024-09-27 13:06:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 5e3a9514-e92f-387f-8f77-b8790c8fb23f | -11.1564 | -49.737 | 2024-09-27 13:06:10 | GOES-16 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 8220fe8c-d2e6-33bf-9cce-a0f511dd84f1 | -11.1754 | -49.7348 | 2024-09-27 13:06:10 | GOES-16 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 7f771c42-6cda-30a9-9357-9ac796fc4e6e | -11.6009 | -50.5025 | 2024-09-27 13:06:12 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| cda944d0-85d9-30d1-8aa6-76cdf37806e4 | -11.6605 | -44.5041 | 2024-09-27 13:06:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 236.4 |
| 6b8bfc37-bcdc-320b-a519-35fc6065bd82 | -11.6409 | -44.5303 | 2024-09-27 13:06:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 188.8 |
| b8ad1e4a-c5ef-38b8-b586-eff2a3d0954d | -11.5818 | -50.5047 | 2024-09-27 13:06:12 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 55ea5d78-30e4-33da-8c16-2e03a17360c3 | -11.8338 | -47.7734 | 2024-09-27 13:06:13 | GOES-16 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 692e711e-7762-3181-8b4f-4dc3ae41b411 | -11.8334 | -47.7956 | 2024-09-27 13:06:13 | GOES-16 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| a3c5d86f-6811-37dc-b2a4-59692c592056 | -12.1856 | -50.8409 | 2024-09-27 13:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 3c23b48e-b70e-3daa-a46f-5922c82d4a64 | -12.3242 | -50.5033 | 2024-09-27 13:06:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 1e52982b-bbb3-37e2-a301-f1515f8eb87d | -12.4782 | -50.4201 | 2024-09-27 13:06:17 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 49e15752-fb9a-3e84-8a4c-d51dd9bf5917 | -12.7505 | -51.3279 | 2024-09-27 13:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 9e21aec5-c3c2-3dde-a9c4-3b4e84f81fa1 | -13.1607 | -45.4752 | 2024-09-27 13:06:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 189.5 |
| e15f7604-2f7b-3eb9-992e-65805d652220 | -13.1801 | -45.472 | 2024-09-27 13:06:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 203.4 |
| 7a6a21ab-6b51-3fa2-9847-0254396c56e0 | -13.1612 | -45.452 | 2024-09-27 13:06:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 6736e463-28d9-318f-a472-b8ade7adaa3b | -13.2105 | -51.2714 | 2024-09-27 13:06:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| de80fed4-5663-32f1-b01f-88bdb7673d69 | -13.2482 | -51.3094 | 2024-09-27 13:06:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 8fdb635a-9028-3c7c-8f5e-a380f43960e3 | -13.2675 | -51.307 | 2024-09-27 13:06:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 594646bc-8d48-3400-bb18-9ebd5f3a25ec | -14.7119 | -45.463 | 2024-09-27 13:06:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 92af26de-6204-3fc1-ac78-c25a70349c94 | -14.7305 | -45.5061 | 2024-09-27 13:06:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| f3ac57e0-7380-3125-bddc-f904e93b5cda | -14.7114 | -45.4863 | 2024-09-27 13:06:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| a7bba24f-1b7a-3937-90a1-c6522f2f2299 | -14.9014 | -51.518 | 2024-09-27 13:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 2f7c1375-dc16-3651-b328-d7463e97261c | -14.9026 | -51.4534 | 2024-09-27 13:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 58c9da6d-f49e-36c0-b902-41fe4e0b83b5 | -14.8734 | -48.9062 | 2024-09-27 13:06:30 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| eb2edee6-3747-33b0-a461-20c7b9225555 | -18.0547 | -44.3888 | 2024-09-27 13:06:46 | GOES-16 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 124.8 |
| ea84a805-3a88-3367-8761-26b0218c3c7b | -5.57 | -42.9297 | 2024-09-27 13:15:38 | GOES-16 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 77.4 |
| 3594dfd6-1f44-3414-b35d-344cc70f0f8f | -5.5888 | -42.9282 | 2024-09-27 13:15:38 | GOES-16 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 9188a75e-e1c1-3ebb-8f6a-7a781c76f9de | -6.3251 | -42.4908 | 2024-09-27 13:15:42 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| b2609560-c56f-3e55-864f-cdcaac42c003 | -7.0783 | -44.1299 | 2024-09-27 13:15:46 | GOES-16 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 50b44211-ee92-315b-9e81-2ef49888c542 | -7.3606 | -44.1035 | 2024-09-27 13:15:48 | GOES-16 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 1bee0f7a-9ff2-361b-a94e-52f5d649757d | -8.0541 | -42.8876 | 2024-09-27 13:15:52 | GOES-16 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| 9ab36218-ebad-3b94-9f5f-1d20d22206cd | -8.0727 | -42.9092 | 2024-09-27 13:15:52 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 387.5 |
| b12ec41d-0d6c-3e25-89dc-88ad78a51607 | -8.073 | -42.8855 | 2024-09-27 13:15:52 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 338.5 |
| 053ceaf1-8826-3dbe-b509-9dbdcabb9db9 | -8.3215 | -56.4929 | 2024-09-27 13:15:54 | GOES-16 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 3c648717-c125-3214-a68c-ec431d0adce5 | -8.5925 | -51.4281 | 2024-09-27 13:15:55 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| a40b8bfb-e323-3b2b-844b-68dd941c5b63 | -8.5922 | -51.4491 | 2024-09-27 13:15:55 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 00faec29-490c-3ec7-823d-873e6046eaab | -9.0251 | -45.1707 | 2024-09-27 13:15:57 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| e6cbdb31-9a06-3481-8e99-44be4fcc5eb4 | -9.5264 | -50.1424 | 2024-09-27 13:16:00 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| e8daed52-666c-37bf-bea2-6147119f3245 | -9.417 | -51.4426 | 2024-09-27 13:16:00 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 137.0 |
| 1bd18df7-d498-3696-b133-721118878f99 | -9.4168 | -51.4636 | 2024-09-27 13:16:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 719305a7-c731-3f5b-96bf-9bc158626f55 | -9.6018 | -50.1352 | 2024-09-27 13:16:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 06be2d1a-8867-3639-a9f5-b8e16dd80f5d | -9.5829 | -50.137 | 2024-09-27 13:16:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| e3bef179-9838-301d-9fdb-43cbb29880d7 | -10.0136 | -53.467 | 2024-09-27 13:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 112.4 |
| ed6a5139-df3f-30b5-b254-4678c596d2a1 | -10.0139 | -53.4464 | 2024-09-27 13:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 356.2 |
| f0055787-8356-30b3-bc45-247d92665960 | -10.2824 | -43.5551 | 2024-09-27 13:16:04 | GOES-16 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| eb667620-7622-3ce0-bcbb-d9161a29e001 | -10.0324 | -53.4654 | 2024-09-27 13:16:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 380.2 |
| 210b2f1f-3731-3272-b987-fe97aca2b2a7 | -10.0322 | -53.4859 | 2024-09-27 13:16:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 171.0 |
| cb4a64ee-a788-3832-844f-4ca3bb8035ce | -10.1501 | -49.9956 | 2024-09-27 13:16:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| f82003d2-b2d9-30a3-8425-feba6a9cb2cb | -10.4371 | -45.7992 | 2024-09-27 13:16:05 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| ddf4c5ec-ce1c-3db5-8613-2cfade9205aa | -10.624 | -46.0023 | 2024-09-27 13:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 04b99faf-5bfa-35f1-80a3-97060a50c763 | -10.4864 | -50.2605 | 2024-09-27 13:16:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 55fefd74-64d9-3d25-a041-b3edc098b3e4 | -10.6438 | -45.9544 | 2024-09-27 13:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 161.2 |
| c06fd410-380b-3ed1-80f9-9e0680045f7d | -10.6452 | -45.8635 | 2024-09-27 13:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 77fd8b25-5790-3e5e-8b00-aaa7a3f31fe5 | -10.6434 | -45.9772 | 2024-09-27 13:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 230.9 |
| f18219a5-651d-3ed4-a98b-ef87d65e8183 | -10.8146 | -45.9778 | 2024-09-27 13:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| ce1e2d51-d9d2-3a3e-a800-3e076ca1d087 | -10.6643 | -45.861 | 2024-09-27 13:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 210.7 |
| d158c221-eed5-36ae-aa3f-d8e01f34e9c8 | -10.6844 | -51.0059 | 2024-09-27 13:16:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 7f89354c-34fd-306d-8eec-2f0e52edf401 | -10.6636 | -45.9065 | 2024-09-27 13:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 484c4bf4-f810-3277-b098-6ba2515ae7fd | -10.6646 | -45.8383 | 2024-09-27 13:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| db940171-e04e-3ab4-b2c6-e5a612f22dd9 | -10.8337 | -45.9753 | 2024-09-27 13:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 706db517-3fba-3801-8943-51191c9c9fdc | -10.6639 | -45.8838 | 2024-09-27 13:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 164.2 |
| f246200a-00c4-360e-83bc-dc7c4679e104 | -10.6846 | -50.9847 | 2024-09-27 13:16:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 2ee3bfec-a5f5-324b-83f7-8331254017f2 | -10.8334 | -45.998 | 2024-09-27 13:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 189.7 |
| 40248735-1b39-3264-a44b-c3fd8850902c | -10.8143 | -46.0005 | 2024-09-27 13:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 352.6 |
| db424251-183e-3f9b-a932-2284d18f7f00 | -10.9148 | -45.669 | 2024-09-27 13:16:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.2 |
| f0d3ef6c-0f32-3fd5-951f-6ab6437391d8 | -11.2025 | -45.5616 | 2024-09-27 13:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| ce0c0977-1193-3517-b4c8-0dd30662a17f | -11.1219 | -50.8328 | 2024-09-27 13:16:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 655e4a93-6714-3a14-9d34-8d214f550ba1 | -11.1459 | -45.5236 | 2024-09-27 13:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 09352eaa-dd9e-37c9-94f4-96672d5242c3 | -11.1456 | -45.5465 | 2024-09-27 13:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 53a8c24e-a85a-3da7-828e-a642d309c916 | -11.1754 | -49.7348 | 2024-09-27 13:16:10 | GOES-16 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| ecab5476-daee-35b5-9986-d297a0f6eaca | -11.2531 | -47.1366 | 2024-09-27 13:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 188.8 |
| d0b5fa54-cc6c-31d5-8146-15d724dbe993 | -11.2721 | -47.1341 | 2024-09-27 13:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| d2e50039-302d-35f1-b632-56d7c380de97 | -11.2534 | -47.1142 | 2024-09-27 13:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 214.4 |
| 2031053a-8348-3554-afb8-8e36ef827877 | -11.1564 | -49.737 | 2024-09-27 13:16:10 | GOES-16 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 3f89719b-bde4-3456-8582-7da2f44de96c | -11.6605 | -44.5041 | 2024-09-27 13:16:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 223.1 |


[Clique aqui para ver as próximas entradas](README137.md)
