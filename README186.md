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

## Dados Diários - Página 186

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 932621bf-a5da-3633-a588-73a2d99a9f2f | -7.4761 | -43.8839 | 2024-09-26 13:15:49 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| a19f6d9a-9d21-31df-b216-5ffbf973f8d0 | -8.073 | -42.8855 | 2024-09-26 13:15:52 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.3 |
| 7af99a56-499b-3f42-8bae-83face9b8545 | -8.3805 | -45.3994 | 2024-09-26 13:15:54 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| d6470ddd-631e-3c83-8821-e73da7915fe8 | -8.3155 | -54.9956 | 2024-09-26 13:15:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| a661d42b-7113-3b46-aa9a-be837962c020 | -8.4831 | -62.6549 | 2024-09-26 13:15:55 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 9f88d8d1-5753-3563-97b7-f9c9e447087e | -9.4165 | -51.4846 | 2024-09-26 13:16:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| cf4566bc-06e3-3b1a-b097-c13f2288a081 | -10.0136 | -53.467 | 2024-09-26 13:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 1a1b87ee-2e5a-30a4-a7b2-58f8ab1e19e8 | -10.0134 | -53.4875 | 2024-09-26 13:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| f6f201da-2971-3d8c-ba18-e90afc2cde72 | -10.204 | -46.1451 | 2024-09-26 13:16:04 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 72d7ab01-1d3c-3082-8af7-363bb413fff4 | -10.032 | -53.5065 | 2024-09-26 13:16:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 108.6 |
| c8aef9e0-2dc5-3099-8398-443d7b062d76 | -10.4562 | -45.7968 | 2024-09-26 13:16:05 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 9ba41e83-9679-36e5-98a0-39971c61b90f | -10.4371 | -45.7992 | 2024-09-26 13:16:05 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 7f2ebc30-38cf-3686-b50c-743284c76bf0 | -10.8352 | -45.8843 | 2024-09-26 13:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 220.6 |
| 736f32b9-189e-3725-8670-941051b617ed | -10.6073 | -51.1196 | 2024-09-26 13:16:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 8c3fa077-e225-3845-9bcf-e5b15fc680f2 | -10.8161 | -45.8868 | 2024-09-26 13:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| bdf18993-af38-3a7c-9918-b6d19c891498 | -10.7359 | -47.3795 | 2024-09-26 13:16:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 111.9 |
| e8b505a4-4b1a-358f-8534-f8fc6391dc7e | -10.7168 | -47.3818 | 2024-09-26 13:16:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 86b0511b-6655-3028-8fa7-1aa6d30ae993 | -10.7165 | -47.404 | 2024-09-26 13:16:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 73015d2c-068b-385c-b89e-4d6be121ca4f | -10.8165 | -45.864 | 2024-09-26 13:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| f9d570e0-94b7-3bb3-be59-25901b2e9d91 | -10.5878 | -54.2375 | 2024-09-26 13:16:07 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 51d2459b-ca24-3ddf-a4c7-f05b6f636391 | -10.8525 | -51.1581 | 2024-09-26 13:16:08 | GOES-16 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| b2e462c9-f14e-3db3-8b36-f22dee9d95fe | -11.1542 | -46.1824 | 2024-09-26 13:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 53df7a8e-85d1-35a3-b793-7bdf3e9c482e | -11.1545 | -46.1597 | 2024-09-26 13:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 5c8bcac0-d570-3fab-9f15-189234e8f800 | -11.1354 | -46.1623 | 2024-09-26 13:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| c2a34695-3cc3-3643-a66d-a83bc183c42e | -11.2508 | -46.1015 | 2024-09-26 13:16:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| e43310e5-fa2b-35bf-af07-23ccfcf397d3 | -11.212 | -51.1627 | 2024-09-26 13:16:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 8d7981ec-88bf-328d-940f-558558ac1601 | -11.2123 | -51.1415 | 2024-09-26 13:16:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 4aae4d5d-d164-35d2-af65-6feb5991cd38 | -11.7179 | -47.8551 | 2024-09-26 13:16:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 157.4 |
| e5078faa-9a8d-35d3-a517-394a996c3a96 | -11.8613 | -49.6327 | 2024-09-26 13:16:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 8268c3ae-89dd-3ea5-b413-ecab2e0d6dbb | -11.8422 | -49.635 | 2024-09-26 13:16:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 8497e582-d61e-3a4c-9167-284690a41ab6 | -11.8609 | -49.6544 | 2024-09-26 13:16:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 969a2077-e036-392b-9a2a-945569994b23 | -11.8616 | -49.611 | 2024-09-26 13:16:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 3a9e3881-d872-3450-aedc-841ed31490b6 | -11.9365 | -47.3367 | 2024-09-26 13:16:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| aa36faf3-1394-327a-88a9-e3c99f006ebc | -11.9369 | -47.3143 | 2024-09-26 13:16:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 98ff1ebe-2b48-3ecb-b8fe-89afd431c6ed | -12.4835 | -48.9224 | 2024-09-26 13:16:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 0ba5899e-c9f1-3d1e-8f11-3e1cfd1765c5 | -12.5026 | -48.9198 | 2024-09-26 13:16:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 4c1f2ded-9fdd-3769-91bd-76b5fa895e81 | -12.5464 | -53.5147 | 2024-09-26 13:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 97f5817d-5fd4-3c95-a84b-b0fbd74ea9a8 | -12.8462 | -51.3164 | 2024-09-26 13:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 3f26b839-971a-310d-9214-7ff748bc96b4 | -12.9516 | -45.3242 | 2024-09-26 13:16:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 0dacaee1-74d4-38c7-a24b-d83aa069da21 | -12.8852 | -51.269 | 2024-09-26 13:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| cd877c39-2467-3ff0-adb6-60c640f6771b | -13.1796 | -45.4952 | 2024-09-26 13:16:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 1c574e28-f585-3732-8d0f-854fbd1c1f6c | -13.3179 | -46.3216 | 2024-09-26 13:16:21 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 103.0 |
| e39ba2b1-91c0-3371-9aca-2bca75304c66 | -13.2985 | -46.3247 | 2024-09-26 13:16:21 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 92275d85-7fa3-317c-9446-5c987927798b | -14.5705 | -45.6973 | 2024-09-26 13:16:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| efa8c4a0-d529-307f-9052-c6d417ea1910 | -14.57 | -45.7205 | 2024-09-26 13:16:28 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 76fc2084-e9f4-36b9-ba41-36590625ab62 | -15.6998 | -41.0835 | 2024-09-26 13:16:33 | GOES-16 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 441.0 |
| af79143a-718a-3aad-918c-9a48ff4bc52b | -17.8068 | -43.2338 | 2024-09-26 13:16:45 | GOES-16 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 6b533ad4-2b6f-3fb9-bc6f-0d2feb12ac5b | -17.9929 | -44.4514 | 2024-09-26 13:16:46 | GOES-16 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 71b40e07-8293-3d61-8715-577eb3e3c5e7 | -18.9102 | -49.1674 | 2024-09-26 13:16:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 117.1 |
| ef958703-431c-379f-9e14-6c96cfa9b6bc | -21.2733 | -51.0061 | 2024-09-26 13:17:04 | GOES-16 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 348.2 |
| 1d46523f-806a-39df-998e-e390434f1811 | -21.9583 | -48.5638 | 2024-09-26 13:17:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 269.3 |
| 20b2a493-b6c7-36de-9895-8b4e4a30c2ef | -21.9374 | -48.5688 | 2024-09-26 13:17:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 196.3 |
| bdec4647-0be7-3cd7-953a-079eef8661e9 | -21.9381 | -48.5453 | 2024-09-26 13:17:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 179.6 |
| bd4a42a1-37ca-3cad-a3bf-d4735d26708c | -21.9576 | -48.5873 | 2024-09-26 13:17:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 155.8 |
| d80633ac-e3d0-375f-bb63-4b565d80a9b1 | -5.8808 | -48.0908 | 2024-09-26 13:25:40 | GOES-16 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 551e58a4-b228-3d86-b645-4c1390461944 | -6.7908 | -41.2254 | 2024-09-26 13:25:45 | GOES-16 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 124.8 |
| e5b666d3-f991-39b8-803c-564fda8d7d1b | -6.8024 | -59.3044 | 2024-09-26 13:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| dc071d21-021e-3d2b-ad64-f9647750c60f | -6.8023 | -59.3237 | 2024-09-26 13:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| df25b116-668f-33b8-a73f-932efe6975de | -6.784 | -59.3052 | 2024-09-26 13:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| b4d52240-2c6f-3dcf-a259-6721bd7cff41 | -6.9306 | -63.1053 | 2024-09-26 13:25:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 000e94d5-63f9-31cf-b54b-6b7c90070e4f | -6.949 | -63.1048 | 2024-09-26 13:25:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 85b3cdac-b838-3f64-a76c-cba601a8cb71 | -7.2906 | -61.0869 | 2024-09-26 13:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 64b2e8b1-8fdc-3ccc-be3b-d43fff0baef9 | -7.3606 | -44.1035 | 2024-09-26 13:25:48 | GOES-16 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| a9aa9713-53fc-30d8-bdfc-3a3fd1bf9ba9 | -7.3637 | -55.5134 | 2024-09-26 13:25:49 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 443c6ef3-d772-31cb-85fa-1cbe25ba66af | -7.3639 | -55.4935 | 2024-09-26 13:25:49 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 78d33dcd-7f3f-366c-a776-e4f1e69c0378 | -7.3824 | -55.4924 | 2024-09-26 13:25:49 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 69f46d0c-6193-3f79-bf5f-48c2ae893e7e | -8.3805 | -45.3994 | 2024-09-26 13:25:54 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 38fb702d-abe8-3802-bc9f-0f4e52184cf7 | -8.3153 | -55.0157 | 2024-09-26 13:25:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 8c65826f-be6d-3035-a36e-eb3df7b84637 | -8.3155 | -54.9956 | 2024-09-26 13:25:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 19cad8b7-b01a-3945-91cd-c1dfb0ee286b | -8.4646 | -62.6556 | 2024-09-26 13:25:55 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 29c1bec4-2898-3c05-bb42-6275d63d3010 | -8.4831 | -62.6549 | 2024-09-26 13:25:55 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 51991352-8890-3ce8-883d-e9cecc2f6989 | -10.0134 | -53.4875 | 2024-09-26 13:26:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 7d9d9dec-fdc9-397e-978b-5c4e4e372946 | -10.0136 | -53.467 | 2024-09-26 13:26:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 5f62304a-56b9-3ee4-a9f1-213db6b1b6ed | -10.0139 | -53.4464 | 2024-09-26 13:26:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 4a552186-d553-37b5-b7b3-0cf2d62e9c2d | -10.204 | -46.1451 | 2024-09-26 13:26:04 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| df7b3bd9-db33-3810-a32b-6108f27b41aa | -10.032 | -53.5065 | 2024-09-26 13:26:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 159.8 |
| 055ec38c-2923-31f9-a94f-05b118a37496 | -10.4562 | -45.7968 | 2024-09-26 13:26:05 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 5481b792-8ee1-35b7-8a57-ed9bf70f71fc | -10.4371 | -45.7992 | 2024-09-26 13:26:05 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 53acb799-3db0-3b68-ba03-67b24e54a75a | -10.6456 | -45.8407 | 2024-09-26 13:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 38737d6c-92fc-3eea-8411-219902f9804a | -10.6073 | -51.1196 | 2024-09-26 13:26:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 0cd8b210-54f5-3eb4-ba30-4b3f34ff5e65 | -10.8161 | -45.8868 | 2024-09-26 13:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 361cc76b-32e1-3a85-9f49-6947ba828044 | -10.8165 | -45.864 | 2024-09-26 13:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 7df96b85-7175-3bd8-800b-14850011ec7b | -10.5878 | -54.2375 | 2024-09-26 13:26:07 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 20399bfc-9918-3edc-b557-d5ed713e88c5 | -10.8352 | -45.8843 | 2024-09-26 13:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 31956180-8da7-33a3-ad04-23c40a0c99f8 | -10.8525 | -51.1581 | 2024-09-26 13:26:08 | GOES-16 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| e4e274dc-8187-3aea-abda-51b6ea51c79f | -11.1946 | -46.041 | 2024-09-26 13:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 312ab1ff-ddda-3b7b-ba80-811bafb173d3 | -11.1354 | -46.1623 | 2024-09-26 13:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 62abaf41-3e0b-32a4-b776-1722d140a53b | -11.0569 | -51.4328 | 2024-09-26 13:26:09 | GOES-16 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 8dbe7c85-870a-3f06-aa6e-8ce95304752d | -11.1542 | -46.1824 | 2024-09-26 13:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 075937fd-9e5b-3dec-9ee3-d950a6bbe016 | -11.0758 | -51.4308 | 2024-09-26 13:26:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| ac0c1fcd-1291-3987-89aa-fbdf7d9ba888 | -11.212 | -51.1627 | 2024-09-26 13:26:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 77be2be5-2609-3c75-8ffb-9fb839ccaa8e | -11.2123 | -51.1415 | 2024-09-26 13:26:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 97619d15-b849-368e-bac1-930e037a44e5 | -11.2508 | -46.1015 | 2024-09-26 13:26:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 05251661-0718-30cd-8d0c-19f519ef0c60 | -11.1847 | -54.7565 | 2024-09-26 13:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| eada7482-3135-33d6-ae4c-467e3c0079bc | -11.4793 | -47.2858 | 2024-09-26 13:26:11 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 546622ee-4194-3efe-933f-13e1ec79f1db | -11.8613 | -49.6327 | 2024-09-26 13:26:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 71eb0c7c-fa60-383f-894d-8bec5c095fc3 | -11.8422 | -49.635 | 2024-09-26 13:26:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 5c27e434-285a-3a5c-8fc5-da717af1e260 | -11.8609 | -49.6544 | 2024-09-26 13:26:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 93e1c8f1-bec2-32e8-96cf-81dc9d200434 | -11.8616 | -49.611 | 2024-09-26 13:26:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| e42e9178-246f-391a-9386-7c1e09098c53 | -11.9365 | -47.3367 | 2024-09-26 13:26:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |


[Clique aqui para ver as próximas entradas](README187.md)
