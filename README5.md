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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7639c2d3-95a0-3ad8-bf51-bafb02f4a726 | -9.2952 | -46.157902 | 2024-10-26 00:33:35 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae375883-6129-387a-8ea2-30af84476573 | -9.2969 | -46.1651 | 2024-10-26 00:33:35 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba116ef7-7392-3063-9a7f-db533a4a953d | -9.6155 | -47.572601 | 2024-10-26 00:33:35 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a90a1454-790c-31d5-bad8-55b3d908d353 | -9.617 | -47.579498 | 2024-10-26 00:33:35 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a5627ac6-07ff-36ed-b1de-24500889f61c | -9.6186 | -47.586399 | 2024-10-26 00:33:35 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8a6e3a3b-fd6c-3d87-9909-21ce448d5508 | -9.6201 | -47.5933 | 2024-10-26 00:33:35 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 250f06de-9e5f-338e-9229-9d2cd6483d2f | -9.6217 | -47.600201 | 2024-10-26 00:33:35 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f9c7d9ae-a54d-3098-9104-0beaa981c861 | -9.6119 | -47.602501 | 2024-10-26 00:33:36 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08d85b6c-062b-3589-aa0b-b09434aecd55 | -9.4954 | -47.221401 | 2024-10-26 00:33:36 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 94438a62-7fa7-30e8-b292-d82d264757cb | -9.7261 | -48.252998 | 2024-10-26 00:33:36 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0da056de-55fe-3d38-8b1a-58056dbb8767 | -9.7277 | -48.259998 | 2024-10-26 00:33:36 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7bcfe101-4929-3bf2-8dba-399b65c407ba | -9.307 | -46.526199 | 2024-10-26 00:33:37 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86f3d18f-7d19-3060-9c67-2d3d7f9659d5 | -8.7861 | -44.7132 | 2024-10-26 00:33:38 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f0e1186c-b46b-3158-8f22-8fb9c023de26 | -8.7745 | -44.7071 | 2024-10-26 00:33:38 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d6bc0607-e35f-3883-b91b-9614287c6abf | -8.7764 | -44.7155 | 2024-10-26 00:33:38 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5fcf41be-98c9-3e2b-be08-4bd4c9e5a355 | -9.5004 | -47.794601 | 2024-10-26 00:33:38 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f1fbd0ae-d7a1-347a-9a7f-fc19472d582f | -9.502 | -47.801498 | 2024-10-26 00:33:38 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 790328ce-3025-35c3-beb9-483929789876 | -9.5035 | -47.808399 | 2024-10-26 00:33:38 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c0d704f3-18b8-35dc-be0c-28ef91ac31a0 | -9.4922 | -47.803699 | 2024-10-26 00:33:38 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d3d31d85-d8b7-3e96-85b8-a588b61694dc | -9.4937 | -47.8106 | 2024-10-26 00:33:38 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 73709c8e-5ea5-3b66-be1d-f031c4802fe7 | -8.7627 | -44.701099 | 2024-10-26 00:33:39 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d5071278-b65b-3f62-b2ea-c8e73225bb82 | -11.1619 | -56.2579 | 2024-10-26 00:33:40 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d41ee80f-ee2a-3b6a-9989-6e415cc5d1aa | -9.2661 | -47.898201 | 2024-10-26 00:33:42 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1b0b19f9-d4ce-32e3-a3d6-1326c0a7b02c | -9.2676 | -47.905102 | 2024-10-26 00:33:42 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49c4548a-1495-375a-a7fc-54b112f5546d | -8.6287 | -45.279099 | 2024-10-26 00:33:43 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b84d9708-0011-38e6-af7f-aa89a07bfc11 | -8.4932 | -45.6297 | 2024-10-26 00:33:46 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f62048bb-d618-38c4-b8b9-fab64fe0eb0a | -9.0709 | -47.992802 | 2024-10-26 00:33:46 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 87feec49-4d81-3595-acca-74d2587778e5 | -9.0725 | -47.999699 | 2024-10-26 00:33:46 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7151881b-ce46-30c1-a67f-8ddb2b6a11d9 | -8.9731 | -47.739601 | 2024-10-26 00:33:46 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7a44e8ce-1a00-37ae-92f7-e6e34a26d27c | -7.6014 | -42.277599 | 2024-10-26 00:33:48 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d72c5206-3b7a-3092-972b-186937940b9b | -7.6043 | -42.289501 | 2024-10-26 00:33:48 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c87abafb-fccc-3db5-94a8-bb434ce3660d | -7.5946 | -42.291801 | 2024-10-26 00:33:48 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 126b047b-eab1-36b6-86c1-ecaf52766658 | -9.0458 | -48.7127 | 2024-10-26 00:33:49 | METOP-B | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| b65aacf4-d318-30d1-9be0-d8892471c975 | -9.0474 | -48.7197 | 2024-10-26 00:33:49 | METOP-B | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 1292b677-cca0-3e43-98f4-872cf6aff57c | -8.9013 | -48.5252 | 2024-10-26 00:33:50 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 8b5314e7-3e18-3717-be5c-fd7053f58c34 | -8.9029 | -48.532101 | 2024-10-26 00:33:50 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 33c0d53d-1b04-3297-be89-83b4ace21375 | -8.89 | -48.520401 | 2024-10-26 00:33:51 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| eeb2ddf8-e46b-3bcd-bca2-cb2eaa0e4c03 | -8.8915 | -48.527401 | 2024-10-26 00:33:51 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| da1b6349-8ee3-36bd-bd4d-be7d959d1b96 | -8.8931 | -48.534302 | 2024-10-26 00:33:51 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| fb77aa01-e13d-3a8a-9338-f5e1675d5155 | -8.4719 | -47.801899 | 2024-10-26 00:33:55 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 07720ade-5e69-3cbb-a23a-d26d237a4e6f | -8.4735 | -47.8088 | 2024-10-26 00:33:55 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a380b34-4a91-3add-adf0-2150842be0b7 | -8.4621 | -47.8041 | 2024-10-26 00:33:55 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 87bae029-b497-3c75-a50e-2ed274e4c1b5 | -8.4637 | -47.811001 | 2024-10-26 00:33:55 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9811744-67ac-348b-baa0-37b59cbdc1f2 | -8.8149 | -49.671501 | 2024-10-26 00:33:56 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a151ce4a-7b2d-35d4-8723-a553847c490d | -8.8165 | -49.678902 | 2024-10-26 00:33:56 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ad16664-74d6-342d-a255-83d3a5eb9167 | -8.8181 | -49.686199 | 2024-10-26 00:33:56 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4d74e80-0127-35a3-9fed-a04e0412ab5c | -8.8051 | -49.673599 | 2024-10-26 00:33:56 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65bf69dd-5a49-3f31-80ce-13c8a96d7e74 | -8.8067 | -49.681 | 2024-10-26 00:33:56 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af57c853-8fdd-3d64-aff4-e360d04b25a3 | -8.8083 | -49.688301 | 2024-10-26 00:33:56 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 092bb21e-0cb0-366f-b5c8-22592e8271a0 | -8.5566 | -49.1987 | 2024-10-26 00:33:58 | METOP-B | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 426caed1-195e-3b1b-8ca8-e2d8ff07363a | -7.7143 | -45.696701 | 2024-10-26 00:33:59 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c824e821-c398-39ef-a420-cdba02a3b8b0 | -7.7161 | -45.704399 | 2024-10-26 00:33:59 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eceed4c4-71a4-339e-b877-045cd9863477 | -7.8976 | -46.676102 | 2024-10-26 00:34:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0fdebe13-185d-362f-9af9-5aafea9e9c51 | -7.8992 | -46.6833 | 2024-10-26 00:34:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4469515-17eb-3541-8a1f-97d444c34b8c | -8.5395 | -49.541 | 2024-10-26 00:34:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 516c0012-8bd0-3a14-ae57-3477187ef273 | -8.5411 | -49.548199 | 2024-10-26 00:34:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e730a862-5cbb-3f89-85fd-8c875fe7721b | -8.5427 | -49.5555 | 2024-10-26 00:34:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b2201d4-1f27-3ca2-95ab-97a0c715cfce | -7.8878 | -46.678398 | 2024-10-26 00:34:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff74935e-66b1-3a9d-9d6e-9275f6d29320 | -7.8894 | -46.6856 | 2024-10-26 00:34:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5588a539-8c10-3cce-b5ae-162e5ebefee4 | -8.2644 | -48.485401 | 2024-10-26 00:34:01 | METOP-B | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0c1b4d9-2697-36d1-9d3e-bae030c6be1c | -6.5429 | -41.686401 | 2024-10-26 00:34:03 | METOP-B | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f8403aba-3247-38bc-bac1-2029c30c9f78 | -6.5461 | -41.699902 | 2024-10-26 00:34:03 | METOP-B | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3e6d4af7-4aa3-3024-98d7-981fbb0fbc1b | -6.5331 | -41.688801 | 2024-10-26 00:34:03 | METOP-B | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5c174bde-ab9a-3594-83ec-d29b6fe5d0b6 | -6.5364 | -41.702301 | 2024-10-26 00:34:03 | METOP-B | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8306eac7-d9d3-3c02-98bd-688dbea422c5 | -7.5379 | -45.826401 | 2024-10-26 00:34:03 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| edb6fb42-fbf1-355f-bf54-dd2583822c04 | -7.5397 | -45.834099 | 2024-10-26 00:34:03 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a9ab203-3e1d-361e-9ec7-9c26062ff5ee | -7.5281 | -45.828602 | 2024-10-26 00:34:03 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 584b58db-fd12-3e7f-beb0-da23c5aa64e9 | -7.5299 | -45.8363 | 2024-10-26 00:34:03 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2a5a0863-3f8b-3e73-a46b-b14d43c4c104 | -7.5316 | -45.843899 | 2024-10-26 00:34:03 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3884cb9c-c3bd-31f2-aa76-433e87b38ff6 | -7.2953 | -44.9562 | 2024-10-26 00:34:03 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 67b0dd11-67f4-3989-98e3-1ea0485d8c90 | -7.2973 | -44.9645 | 2024-10-26 00:34:03 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87e2c091-67d6-3a4e-b0ae-1bb1aaecc988 | -7.2992 | -44.9729 | 2024-10-26 00:34:03 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 485d1b57-6cdc-3398-ba6d-b9acef087082 | -7.2855 | -44.958401 | 2024-10-26 00:34:03 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94a12bb7-ad5a-36f2-937a-91328be2fa99 | -7.2875 | -44.966801 | 2024-10-26 00:34:03 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa7ab9ec-66df-3ea6-83c7-c78cdd9c15ca | -7.4032 | -45.555302 | 2024-10-26 00:34:04 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2da4a916-8e03-3119-9fb3-9fd49a1e7a3f | -7.405 | -45.563202 | 2024-10-26 00:34:04 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2eb63b2b-0d8d-3be0-800d-e88f1b273476 | -7.4068 | -45.570999 | 2024-10-26 00:34:04 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9bdd1c9-af83-339d-9588-cb0f869c9aee | -8.362 | -49.809502 | 2024-10-26 00:34:04 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a0943fc-b64b-320a-8a06-2e222515c80b | -8.2231 | -49.272499 | 2024-10-26 00:34:04 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06792f69-f886-3899-91a5-0921d53f5d57 | -8.3912 | -50.036301 | 2024-10-26 00:34:04 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4baf8bce-5482-391d-a60b-5945b5bd9a6c | -8.3929 | -50.0438 | 2024-10-26 00:34:04 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76f148c8-0342-3006-a112-195345e1d1bb | -8.1889 | -49.489799 | 2024-10-26 00:34:05 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68ef993a-b412-3323-bac6-904c088f75f3 | -7.588 | -47.082401 | 2024-10-26 00:34:06 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 43a574fb-0012-3cb4-b396-483edb1cbc4c | -8.1791 | -49.492001 | 2024-10-26 00:34:06 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55fa308c-4918-3d16-9e50-de2d02069c3e | -7.5611 | -46.783001 | 2024-10-26 00:34:06 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1ff2e5f-937d-3d2e-b1d6-125a7699342d | -7.5627 | -46.7901 | 2024-10-26 00:34:06 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| db4b3ed3-1dae-37f9-ab89-0826b3e722fd | -7.6781 | -47.297699 | 2024-10-26 00:34:06 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be06c4f4-e8f7-3bde-a652-600f729359fc | -7.6796 | -47.3046 | 2024-10-26 00:34:06 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| acc30d5e-0602-33ee-b5aa-82a2777cf007 | -8.3063 | -50.117802 | 2024-10-26 00:34:06 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9b04a71-a57c-3b87-8321-c30d0f5f66a0 | -8.3729 | -50.422501 | 2024-10-26 00:34:06 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90dade94-8343-3663-b9ba-5853703e4368 | -8.3746 | -50.430199 | 2024-10-26 00:34:06 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1bf679f-2fd8-3f73-9186-9776597fb4a8 | -7.5513 | -46.785301 | 2024-10-26 00:34:06 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 674ca5a8-c134-38fe-90e9-941b59b231cc | -7.5529 | -46.7924 | 2024-10-26 00:34:06 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ec79900-398c-39e1-aef3-8f924f786fae | -7.6682 | -47.2999 | 2024-10-26 00:34:06 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec06d1e9-1170-32a1-8963-0b2d68eb4326 | -7.6698 | -47.306801 | 2024-10-26 00:34:06 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cfcadcd5-95bc-3f22-a8ab-db966862df80 | -7.6713 | -47.313801 | 2024-10-26 00:34:06 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5508792-645f-3b1d-ade2-cecfdb5746b1 | -7.6584 | -47.302101 | 2024-10-26 00:34:06 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 024fa72d-b184-3469-b706-e77f5024dc4a | -7.66 | -47.308998 | 2024-10-26 00:34:06 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aafe8459-0c26-3393-996a-c31e51cfda61 | -7.6615 | -47.316002 | 2024-10-26 00:34:06 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f9a72997-a97d-3beb-b085-db77778e3b91 | -7.5962 | -47.0732 | 2024-10-26 00:34:06 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
