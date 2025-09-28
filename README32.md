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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7bb9f5e0-cd28-3169-9404-8f7ff2f5cf8a | -4.14108 | -39.9992 | 2025-09-28 04:04:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b29d4872-362b-3af0-a17c-0d8afed91de6 | -9.04799 | -45.51285 | 2025-09-28 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c6a477a-5715-3220-babd-72b87401460c | -7.30277 | -42.94212 | 2025-09-28 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1836b282-2fb4-38c1-9a9a-4ee0bb46356d | -2.98359 | -49.53979 | 2025-09-28 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bdcc6081-44b8-3c0b-a444-89a2fc8b83b9 | -7.16984 | -45.4973 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 553ef289-13a6-3374-95af-8a946bcf41b3 | -7.14988 | -45.50551 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29dbe663-6f4d-3882-8b8c-ea18b0e520c5 | -5.78375 | -42.8301 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a2a65326-3e4c-345f-aac7-93fa3afd1eaf | -5.41688 | -42.27215 | 2025-09-28 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8166d853-6287-3407-9a49-09115caaa1c8 | -6.48392 | -44.2526 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 19280d9d-60b8-3c14-80cc-d6b8377697d5 | -5.80197 | -42.78663 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0ddef838-dda1-35bb-98e7-65343d2c4024 | -6.31304 | -43.46421 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 215d38bd-9ce5-38ab-b568-e7d41e2ff02a | -9.28616 | -45.70172 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10d65937-a345-35b6-bbc7-cbaf2d273690 | -6.50036 | -44.12815 | 2025-09-28 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ce81dfe-af27-37f8-b918-a62ae9dd7177 | -5.76149 | -42.83057 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 546e65cc-2a33-381f-a66f-96cf7c79d7d1 | -5.7604 | -42.80643 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b1f4f29d-6ec3-3525-aa33-6de42fad4ee0 | -5.69801 | -42.62478 | 2025-09-28 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b69048e7-9f81-35d2-aa1c-ce03b4a6344c | -6.29221 | -39.82726 | 2025-09-28 04:04:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 58a870b3-a5d4-3685-9f90-518b51ee700b | -9.52461 | -43.50092 | 2025-09-28 04:04:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cf89d824-ac87-35cf-8b15-9d53873a81be | -3.32316 | -52.54357 | 2025-09-28 04:04:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 60991fdd-7ff0-331e-a525-679ed570dd65 | -7.85304 | -43.79509 | 2025-09-28 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9093cb2d-f748-3d41-940e-8051314d2e8d | -6.15334 | -42.80249 | 2025-09-28 04:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f42d160e-189d-390f-9305-a84922500ddf | -9.54572 | -47.77573 | 2025-09-28 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b683cacc-39ce-370d-b62f-adeb2e46b1f9 | -5.14355 | -45.70611 | 2025-09-28 04:04:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 313b8b27-1191-3772-a853-86c0e54a67c9 | -5.82731 | -44.44359 | 2025-09-28 04:04:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 405decc7-ce5c-32fe-9605-2c151c4a5643 | -6.12619 | -43.44602 | 2025-09-28 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e18880a-681b-397a-82f1-2d0c9209d66e | -5.73804 | -42.85347 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 7be0a105-3fc2-3428-ad8f-786f1e3e1289 | -9.11292 | -46.6717 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2dd72738-bc17-3c5d-8bff-369b14791c70 | -5.91103 | -42.93852 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e6c8a738-9377-3329-a7f3-388ef3d6d6da | -8.43404 | -46.8695 | 2025-09-28 04:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b140568-f516-3c78-8006-d2e98da7b845 | -6.56906 | -45.09887 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cbff504c-162f-3990-a468-074cec6347a7 | -6.43187 | -43.51326 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fc3d00a7-00ec-393b-94d8-04b82944a7c7 | -7.74719 | -46.9784 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f2762f47-4636-34de-b447-6a7cdc6797b8 | -7.54628 | -46.10003 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 703cc7b9-609f-3441-a60d-130cb90e7d43 | -7.1514 | -45.50555 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c8bebc7-798e-3e30-a576-f221fe658f70 | -6.02087 | -45.41528 | 2025-09-28 04:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fdb5f06-18a5-37a4-a696-398dc9bcbd16 | -6.42319 | -43.07126 | 2025-09-28 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| f4c011e6-bd5d-320c-a188-2dcbb7464dc4 | -5.30114 | -45.32664 | 2025-09-28 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75cabe43-9189-3aa4-b9ca-b60a7e207f96 | -7.24791 | -44.76658 | 2025-09-28 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bac9d15f-2e5b-3e33-9866-17790b1e00ed | -6.79789 | -46.18739 | 2025-09-28 04:04:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20debf73-8294-3b0f-bcbc-95da48b93cc5 | -4.86328 | -49.46944 | 2025-09-28 04:04:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8033c452-3d46-36e3-8e32-e18d4b2a75e3 | -8.17233 | -46.40948 | 2025-09-28 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 329d2d73-23bc-3d7f-ac22-0cd60b82c7e7 | -5.90603 | -42.94641 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7ec0c781-9426-3935-a09f-a9550cc2e7f5 | -6.20997 | -42.84923 | 2025-09-28 04:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b2b4d9b7-809e-3d78-bb76-7a21da073091 | -3.80305 | -41.56879 | 2025-09-28 04:04:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 573488eb-4bfc-36af-a151-538fd2875cc4 | -5.79251 | -42.84426 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| aa9c0752-2f82-3d23-83b7-667204ac18c8 | -6.57243 | -45.09898 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d221fa4a-bab0-31fb-97f5-df6ce213dfe3 | -8.64972 | -44.86096 | 2025-09-28 04:04:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1ea0018-f399-3321-9f5b-768152cce1a5 | -6.00489 | -43.80474 | 2025-09-28 04:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 468617a4-07a9-3419-a82e-5348b1084233 | -6.42816 | -43.51269 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b4f68471-1550-3aa8-8bee-e0c63a097d2b | -4.48224 | -47.67081 | 2025-09-28 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f3d37a0f-84bd-3f2d-ba16-dfcf9f4bd0ce | -5.94954 | -42.9068 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5a1a5f73-2a30-3630-a4df-c63d21d96cca | -5.51493 | -42.73494 | 2025-09-28 04:04:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ef05f375-d5f6-3a20-9fce-ab43c88d2930 | -6.316 | -43.4692 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7908217f-cc0b-3e9f-98df-f7141f04e0c2 | -8.48556 | -47.81188 | 2025-09-28 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d6c91411-d671-332f-86ed-df0a219a168a | -3.74659 | -39.51785 | 2025-09-28 04:04:00 | NPP-375D | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| de7d2e71-7e22-33ef-bfe4-aedd78403474 | -6.40159 | -44.29384 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7247970-4798-3d4c-b2ff-042993bb5813 | -5.76059 | -42.81368 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| ba542779-3fe5-325d-8061-ee1e44f929b3 | -6.31072 | -43.46569 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0ecadaec-8221-396f-acff-f0b484dd9492 | -7.80842 | -47.00484 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7a990041-41d1-35c4-b75a-aceca265714d | -7.26131 | -42.99357 | 2025-09-28 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 72da9103-27c1-331b-bd3e-96b6f0b535f8 | -8.80821 | -47.64605 | 2025-09-28 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 070b8395-2f7c-3ec1-86b0-5c8998377781 | -9.08697 | -45.8647 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c71fd959-6e36-388f-8406-d2e5e8ff41cf | -6.48939 | -44.24332 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 687b1f93-9d2d-3f39-a56c-a06a95c0a563 | -8.67787 | -49.93733 | 2025-09-28 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| f98cd6ab-2a2f-3206-8c7a-826484dd2330 | -5.82421 | -44.43798 | 2025-09-28 04:04:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 8175f27e-63ca-34e9-8a40-0ca157d1f3b6 | -6.21423 | -42.84574 | 2025-09-28 04:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 8a97ac5e-fb9b-3c8b-8e20-641eb8c03fb2 | -7.42568 | -40.07744 | 2025-09-28 04:04:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fc5a5f41-8f2a-3d7f-b44e-38c20b42bc70 | -9.78334 | -47.76016 | 2025-09-28 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 549e2c16-f8ee-3c5c-bcc7-3f5def8e2cdf | -4.85995 | -49.46943 | 2025-09-28 04:04:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2f9d7e4-6cc7-34f8-b1a8-e5273439f86e | -5.81955 | -42.81453 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c86e3050-3cbc-3c9e-9375-5103ba35b16d | -6.07205 | -43.7722 | 2025-09-28 04:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| db504ed8-235a-3d69-8e44-9370ab081fdf | -6.53446 | -43.82547 | 2025-09-28 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02fb4762-de35-3e67-991c-5f15e15711c1 | -5.74777 | -42.88508 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 36a9af33-2c2b-3550-a2e3-a5cedb6ca1ad | -5.73563 | -42.66367 | 2025-09-28 04:04:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 82ebd388-72db-34f0-8dde-138673a0a2f4 | -6.89927 | -44.76375 | 2025-09-28 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7f89905c-f53a-3414-bca6-fa2e4f30603f | -6.78574 | -44.07817 | 2025-09-28 04:04:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 507030b9-0f3f-3893-a2b4-4a97c1ad3245 | -8.28176 | -45.44321 | 2025-09-28 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d6311aae-b131-3b44-b483-0491df266ee0 | -5.2928 | -43.15813 | 2025-09-28 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 288e6763-04dd-3cf1-96ff-f92eb1787fbc | -6.64697 | -39.50472 | 2025-09-28 04:04:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1b96bb72-9810-3dcd-81d3-8397e1cebf97 | -7.87123 | -44.56343 | 2025-09-28 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c80b54d6-bbc0-3d17-a1fb-429f59678be3 | -4.00454 | -46.96904 | 2025-09-28 04:04:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bbbd67e-a538-3a46-954e-75968b825ff8 | -7.87679 | -44.55406 | 2025-09-28 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ca30f0c-ee7c-3425-8677-e089afb1f03f | -7.16314 | -45.51147 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cef1e15d-4bf2-3317-a8d4-5bda77b02a13 | -10.12577 | -45.32728 | 2025-09-28 04:04:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7b3ec2d-ba21-3749-9b16-c5ac998490a8 | -8.72013 | -47.97976 | 2025-09-28 04:04:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b5c3a1d-9de3-3a06-8ef5-e6f1295ac783 | -6.44937 | -44.22189 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 322398d6-1d11-3426-89f2-21279611a75d | -7.32301 | -45.98822 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b726d26-11ad-32b6-851e-de78c68bde80 | -5.81231 | -42.81362 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| d2101182-00e5-328d-bdcd-20af3eef0ccf | -6.5798 | -43.73891 | 2025-09-28 04:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c21f97a2-af78-3da6-88f0-acc6a48e1a21 | -2.47833 | -47.65427 | 2025-09-28 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abae0b3a-83fd-3562-9d5e-efbca20cb1ee | -6.50113 | -44.12347 | 2025-09-28 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b73195ba-320a-3cfc-b679-eff7d6f0f4bf | -9.10616 | -45.87601 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11d9b498-3a67-32f9-a91c-d78e35bd70e3 | -5.70092 | -42.62935 | 2025-09-28 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d48cc267-f516-3d00-8c80-5f07af2eb9a3 | -8.72396 | -47.98582 | 2025-09-28 04:04:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00b1a4bb-c46a-3df2-b577-a91f2a811cd7 | -6.34498 | -43.34086 | 2025-09-28 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a45eff50-fe75-3441-b36f-a4af93793c18 | -9.21305 | -46.77275 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 590da5b6-b004-3f48-ad11-72ccd96a7c6e | -5.81863 | -42.79755 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9dae4404-4147-3c40-8eba-b4f783a68778 | -5.2476 | -42.70749 | 2025-09-28 04:04:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f0a3a12e-db86-3f71-957f-813f97b3c15c | -6.08863 | -49.40302 | 2025-09-28 04:04:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9f07f1c-2763-30c3-ad4d-372e6c5cadbf | -5.65736 | -43.30581 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README33.md)
