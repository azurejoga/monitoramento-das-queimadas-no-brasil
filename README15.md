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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 804f4ba5-42a5-3b9f-ae24-50923462b32a | -9.7367 | -46.955601 | 2024-10-13 00:58:03 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f289e5e4-cbf5-3a73-8ed3-821a23391b7d | -10.6406 | -51.133801 | 2024-10-13 00:58:04 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8624c70a-1414-3fc7-9c53-3eb51e44a92c | -10.6422 | -51.1408 | 2024-10-13 00:58:04 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f59a06f1-6bb6-38cd-b6fa-20876909398e | -10.5499 | -51.0504 | 2024-10-13 00:58:05 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 90fa8373-cc5f-3c95-a9a8-a535f15cd07a | -9.7015 | -47.766201 | 2024-10-13 00:58:07 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6611ff5-9fae-3e59-98d9-35ab585f1d6c | -9.7034 | -47.773998 | 2024-10-13 00:58:07 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c43bbaf0-d6e3-3799-8ff8-55bc28254710 | -8.8084 | -44.403301 | 2024-10-13 00:58:08 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ca10ffd2-ae83-327a-800f-c111e957b75f | -8.7169 | -44.116402 | 2024-10-13 00:58:08 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0b1623ed-4295-3a41-95ce-55ae03b9b2ea | -8.7201 | -44.129398 | 2024-10-13 00:58:08 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 610791cd-cefc-3dd3-97cf-81ed710e7d87 | -9.7322 | -48.292801 | 2024-10-13 00:58:08 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 074d6850-62ca-3bb2-adc8-7e317594345e | -9.5236 | -47.799999 | 2024-10-13 00:58:10 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2184528e-a2d6-3230-9da9-23c24cee074e | -9.5255 | -47.8078 | 2024-10-13 00:58:10 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3c3e4550-1e9c-36b9-bb4b-5a54b041fb22 | -9.5138 | -47.802299 | 2024-10-13 00:58:10 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9bde5266-8f5f-3fb2-9df6-1295e66cd3bf | -9.5157 | -47.810101 | 2024-10-13 00:58:10 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d88410fd-bc25-3a88-9bf5-eb979781c236 | -9.5175 | -47.818001 | 2024-10-13 00:58:10 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 16f1cc98-eb96-3760-8b2d-ef7dff62c8fe | -9.5059 | -47.812401 | 2024-10-13 00:58:10 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39700876-407c-3dcf-88c1-4b17a1004d08 | -9.225 | -46.6726 | 2024-10-13 00:58:10 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a344f0a-4639-31f7-8548-2b00e151bc9e | -9.2271 | -46.681499 | 2024-10-13 00:58:10 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d49b303f-6238-3584-aab7-01977bd56f04 | -9.9434 | -50.054699 | 2024-10-13 00:58:11 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42bf9014-62aa-3bc2-bc76-c8f763433c3b | -9.945 | -50.0616 | 2024-10-13 00:58:11 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db4b2c26-2191-3edc-a5a0-5fb0246212c1 | -9.6244 | -48.982399 | 2024-10-13 00:58:12 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dfe3e774-589c-316a-94c3-aa7958e01cb1 | -8.1311 | -43.004299 | 2024-10-13 00:58:13 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| eaf7010e-dff3-3f67-9b54-d0577cfab9cd | -8.6879 | -45.260101 | 2024-10-13 00:58:13 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c22722a2-b0d7-3ad3-8c17-b92f1982f3fd | -10.0632 | -51.404999 | 2024-10-13 00:58:14 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 69134a82-ef35-336d-85c8-e12a6cdd3ba6 | -9.1664 | -47.599098 | 2024-10-13 00:58:15 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 02543c67-0452-3399-a181-890940660484 | -9.4459 | -48.879601 | 2024-10-13 00:58:15 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de133e61-56e5-3e66-9521-818000b5a35f | -9.4475 | -48.886902 | 2024-10-13 00:58:15 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ef47b7fe-b720-3488-a0be-4691fb6fe0da | -9.4492 | -48.8941 | 2024-10-13 00:58:15 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b013aee-7868-3489-8ef7-4b04802329b2 | -9.0292 | -47.674 | 2024-10-13 00:58:17 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7a59c7ca-9caa-3dd5-8fc0-c6600fe147b0 | -8.6988 | -46.588501 | 2024-10-13 00:58:18 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d2b8d69-a474-3cd4-89bb-e31266c75bbf | -8.701 | -46.597698 | 2024-10-13 00:58:18 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2474f152-6e2c-336e-be97-f50932fdb1cb | -8.7032 | -46.6068 | 2024-10-13 00:58:18 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 49e9968e-2bbc-3bfe-80d0-e4f1fe384833 | -8.6913 | -46.599998 | 2024-10-13 00:58:18 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9df18633-d5b0-3e06-a2b1-94b4e8117df2 | -8.6935 | -46.6092 | 2024-10-13 00:58:18 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a268b72c-32da-3f0a-a5a1-c72b5fe6a147 | -8.6957 | -46.618301 | 2024-10-13 00:58:18 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4075aa1-0961-31fe-acc3-85d5c6880d26 | -9.2998 | -49.631599 | 2024-10-13 00:58:20 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f883a65-4410-35aa-9033-d894abd96a65 | -9.3014 | -49.638599 | 2024-10-13 00:58:20 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b09da83f-805e-3a8e-b061-b09adb0bbdfc | -8.9079 | -47.903801 | 2024-10-13 00:58:20 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8279b442-7af7-3020-a659-08ea7f559517 | -8.9097 | -47.911701 | 2024-10-13 00:58:20 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71401816-b92d-36a9-bee3-4df51ab672f9 | -7.7046 | -43.194 | 2024-10-13 00:58:21 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5b1553eb-8763-37cf-a60e-03fddc123e6b | -7.7276 | -43.286598 | 2024-10-13 00:58:21 | METOP-C | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 88c01955-687b-3ace-a140-6b936356e315 | -8.8547 | -47.9412 | 2024-10-13 00:58:21 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e46619ab-f172-30d3-988b-73e944738f53 | -8.8566 | -47.949001 | 2024-10-13 00:58:21 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 84b96d04-770e-33c4-90aa-d0f549cd26e2 | -8.8584 | -47.956799 | 2024-10-13 00:58:21 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3fcd170a-7a0a-37dc-bdbb-207f8563e8c8 | -9.1823 | -49.6586 | 2024-10-13 00:58:22 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 50d8a437-df6a-3da0-a706-e5b67780dcbc | -7.8974 | -44.601101 | 2024-10-13 00:58:23 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| beae33eb-bbc9-3c8f-811b-82d930fca282 | -7.9005 | -44.613499 | 2024-10-13 00:58:23 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 33b29d3c-1fc3-3218-ba63-74d422f3ce59 | -7.9035 | -44.6259 | 2024-10-13 00:58:23 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 451fce23-2685-3caa-9059-bf87bbba9580 | -8.9646 | -49.029499 | 2024-10-13 00:58:23 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 059fed58-b084-3d4a-8481-6b6a2bdd40b4 | -8.9662 | -49.036701 | 2024-10-13 00:58:23 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68b40a94-f698-3e19-9ab4-5d2558c546bf | -7.8877 | -44.6035 | 2024-10-13 00:58:24 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8c2c9468-0ec6-3e6e-b656-db446372a78e | -7.8908 | -44.615898 | 2024-10-13 00:58:24 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ff22998a-f12e-3f8c-a87f-730c34903311 | -8.5268 | -47.252998 | 2024-10-13 00:58:24 | METOP-C | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd29f7d0-9a46-30ae-9909-21d1951c4036 | -8.5288 | -47.261501 | 2024-10-13 00:58:24 | METOP-C | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 803e6de0-ee75-3018-868b-725f1aef7350 | -8.5325 | -48.769001 | 2024-10-13 00:58:29 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 712839fd-331d-3dc4-bf58-e6505b75346e | -8.5342 | -48.776299 | 2024-10-13 00:58:29 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 1d7f3b62-d4f8-3a56-9127-65c475789915 | -8.756 | -49.7785 | 2024-10-13 00:58:29 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a00f167-d2fe-3fd3-8d70-3967ca322413 | -8.7576 | -49.7855 | 2024-10-13 00:58:29 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 963cf35d-93ba-3bf5-aa65-aeb607c19639 | -8.4553 | -48.615101 | 2024-10-13 00:58:30 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| a9e2ac74-14ee-3bc4-909a-ccb3ab743522 | -7.9879 | -46.854198 | 2024-10-13 00:58:31 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a1089568-41f2-35f5-9f1d-97ecf3091e63 | -7.6997 | -46.6413 | 2024-10-13 00:58:35 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7df8aa1d-d177-32fb-8ca0-81ffbc358772 | -7.7019 | -46.6507 | 2024-10-13 00:58:35 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39fbec5d-a7c4-32d0-aaa7-cfd90a26f782 | -7.2735 | -44.960098 | 2024-10-13 00:58:35 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 63fe9e5b-8085-36bd-9a23-7ca79af54bcf | -7.2764 | -44.972099 | 2024-10-13 00:58:35 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 57a453fc-aee2-3824-b244-07ff596bbaf1 | -6.3882 | -41.590599 | 2024-10-13 00:58:36 | METOP-C | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1b16717b-90ff-3a14-ad13-f53dcc13d40a | -7.408 | -45.685001 | 2024-10-13 00:58:36 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 60c402b1-ac01-3860-addd-6d26a3b02920 | -9.0473 | -52.9874 | 2024-10-13 00:58:36 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b2544c5-3c1c-301a-972e-a3844b40d094 | -9.049 | -52.995201 | 2024-10-13 00:58:36 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f289329-0688-30e5-af64-8ff1c6376046 | -9.0375 | -52.989498 | 2024-10-13 00:58:37 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25ef62be-7244-33fe-8cb7-869dd47546b4 | -9.0392 | -52.997299 | 2024-10-13 00:58:37 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3471cf43-0f5d-36c2-8044-bc0575da3be3 | -7.25 | -45.373001 | 2024-10-13 00:58:37 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a9cf2f9-1ec3-3f01-9060-a9c2b42209da | -7.2527 | -45.3843 | 2024-10-13 00:58:37 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c945bda9-7171-3166-8a70-577c3ce17fca | -8.3343 | -49.9631 | 2024-10-13 00:58:37 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e291719b-bea6-39a2-89cd-5ed145926e88 | -8.3359 | -49.970001 | 2024-10-13 00:58:37 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 607bf7ca-dceb-3b60-b649-f79a792700fe | -8.3375 | -49.977001 | 2024-10-13 00:58:37 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b44acc3e-82a4-35a4-b112-d7345f3a404b | -7.243 | -45.3866 | 2024-10-13 00:58:37 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2cf876fe-d2bc-3cf0-a9d7-3a7e0853e410 | -7.5209 | -46.584499 | 2024-10-13 00:58:37 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 478d9e7b-05f9-34cc-aec3-75478f1d162e | -6.7222 | -43.551102 | 2024-10-13 00:58:38 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c3b3ceb-9583-3ece-b00f-a91929018020 | -6.7259 | -43.566299 | 2024-10-13 00:58:38 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 827df9f2-f2a1-3993-bcb7-4e74116667b1 | -7.6732 | -47.310398 | 2024-10-13 00:58:38 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 412bcc8b-ef5c-3070-98b0-87024613f489 | -7.6634 | -47.312698 | 2024-10-13 00:58:38 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f6dbee0-3e25-331f-b4dc-701117c9bae0 | -7.5343 | -46.8564 | 2024-10-13 00:58:38 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f3154a34-adff-3e4d-8501-fe968fe350dd | -7.5365 | -46.865501 | 2024-10-13 00:58:38 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 27fd68d9-86b4-377e-ba14-8c1be420a1d8 | -7.5104 | -46.8428 | 2024-10-13 00:58:38 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86f08376-8b97-3798-874e-babe94d51d51 | -8.8577 | -53.012798 | 2024-10-13 00:58:40 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 967ecabe-3d2c-30e7-9edc-b904d4cab8ac | -6.7614 | -44.171501 | 2024-10-13 00:58:40 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4fcb5510-e400-392c-aaae-c84d6be950e6 | -6.7517 | -44.173801 | 2024-10-13 00:58:40 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab441a03-c602-3e29-ab61-3843172b0abe | -6.7551 | -44.187599 | 2024-10-13 00:58:40 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b5d5cd8c-6847-3007-8f70-95a43a3de055 | -7.6084 | -47.7342 | 2024-10-13 00:58:40 | METOP-C | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a414db8-f7c3-3ab7-9809-2b381c20b96a | -7.6103 | -47.742401 | 2024-10-13 00:58:40 | METOP-C | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d7506e7d-d161-3f40-a0fb-418889c96101 | -6.7419 | -44.176201 | 2024-10-13 00:58:40 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00d7b0e4-cc15-3dba-8ffb-581c7e4275f2 | -6.7453 | -44.189999 | 2024-10-13 00:58:40 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c8c2829-bb8f-3a3e-84d1-d5f79bac3e69 | -7.9678 | -49.448101 | 2024-10-13 00:58:41 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80458758-6da5-32b5-bc5d-d2197636de91 | -7.9695 | -49.4552 | 2024-10-13 00:58:41 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c661c6fb-9702-3bcb-874f-c2ff746f7135 | -7.9711 | -49.462299 | 2024-10-13 00:58:41 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e5f02b4-a545-3563-8c59-b776429fa7dc | -7.981 | -49.683399 | 2024-10-13 00:58:42 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a56d05c-b3e3-3d81-a89c-bd732b2ba4c5 | -7.9826 | -49.690399 | 2024-10-13 00:58:42 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9781b891-900a-3fcc-8a9d-e03704812e03 | -7.3784 | -47.2425 | 2024-10-13 00:58:42 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28605bb8-81ab-3a6f-8000-752d58dc593e | -7.3805 | -47.251301 | 2024-10-13 00:58:42 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 026f9254-9f29-3626-b6be-613fe8619adf | -7.3826 | -47.259998 | 2024-10-13 00:58:42 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README16.md)
