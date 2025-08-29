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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 648b043b-bbd5-3de3-9b49-e62f971b35d7 | -9.55295 | -45.84538 | 2025-08-29 05:06:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e43756c-06cf-3fa9-ae6b-60f4676fb3c6 | -8.56695 | -51.31656 | 2025-08-29 05:06:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45bda867-8e71-3cee-ac88-c407444de356 | -6.98043 | -59.34097 | 2025-08-29 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e76c86a-228f-3664-b16e-03fb69bd7e7c | -9.43788 | -47.64353 | 2025-08-29 05:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60981e3f-d819-3a75-a3cc-8686ec036855 | -8.6907 | -50.38943 | 2025-08-29 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c139ff3-861e-3059-ab28-a9854f320237 | -5.61775 | -45.01266 | 2025-08-29 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| aa9f3940-b92a-383c-9720-837e5390115a | -7.02735 | -44.67623 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cbf25ff5-7e37-3805-9dff-23f9fa2cac3a | -9.49156 | -45.39119 | 2025-08-29 05:06:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd8ae90e-cdd3-3934-a117-92c4fd083a35 | -6.98551 | -59.34418 | 2025-08-29 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3843b7b-bbf5-3a0c-82f5-8ae634180ef2 | -6.13388 | -44.42845 | 2025-08-29 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbdd4a16-aec4-3d51-8999-ecd02ed42b78 | -5.62615 | -45.00356 | 2025-08-29 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8c801317-a4a8-343e-966f-76f32876eaec | -3.4198 | -49.05249 | 2025-08-29 05:06:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1d6e0621-5635-362d-aad1-ff286f26608f | -7.16075 | -44.14688 | 2025-08-29 05:06:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4ea526f-5a78-3d5f-8d3a-32b231d46d63 | -5.62089 | -44.9985 | 2025-08-29 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fbc1f290-2c65-3219-8fba-ac0980bb2135 | -8.90541 | -47.32721 | 2025-08-29 05:06:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a4cb4f3-1145-3ea3-a7b4-9c20f32d7a1e | -3.74447 | -53.80758 | 2025-08-29 05:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d07a0de4-213a-3bbb-80ee-698cddd615f4 | -6.98853 | -59.33784 | 2025-08-29 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c26397b0-5730-3856-ab3c-d7dc70bdea0f | -6.98342 | -59.34593 | 2025-08-29 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71e7d615-1a47-335d-a3ab-3525d382ecac | -9.50533 | -45.37929 | 2025-08-29 05:06:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a0c3a97-4ea1-37b3-949d-2d49e5f83e58 | -6.3924 | -62.9077 | 2025-08-29 05:06:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2408377a-af6b-3ad8-97a3-3de83509908d | -3.62344 | -53.64547 | 2025-08-29 05:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d35983b-3216-346e-9806-1eabad6cc01f | -9.04404 | -47.01528 | 2025-08-29 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 28104812-2744-326e-85e3-6cf55663a188 | -5.32936 | -51.32986 | 2025-08-29 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f432e47-9668-3ac8-bbee-93016853f0d7 | -6.13422 | -44.42484 | 2025-08-29 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3178fb76-f628-32a3-900c-8e8ff72f5e07 | -7.5646 | -47.49823 | 2025-08-29 05:06:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b6323a2-87d6-3dca-b8cc-5c68b50191f2 | -5.17884 | -46.07203 | 2025-08-29 05:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 24d8527b-c6bf-3072-bc3c-68395be088fd | -5.86588 | -42.95267 | 2025-08-29 05:06:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 61c0a1f5-3369-3bd7-b488-6b242238f86c | -8.69554 | -50.38608 | 2025-08-29 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66c27fb3-5fa4-33e2-8885-920a1d21a9f7 | -3.42259 | -49.04298 | 2025-08-29 05:06:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 22529da8-7603-3bc2-ab74-86d7558260db | -8.6935 | -50.39252 | 2025-08-29 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6a9ecd5c-0a9b-35c5-aaeb-33101b2cd3fb | -3.42198 | -49.04707 | 2025-08-29 05:06:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 98844f38-c861-3fbf-9eb1-827798a5b867 | -3.76213 | -54.8104 | 2025-08-29 05:06:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d0c9578-ec0f-349f-bae3-04f5d9dc811d | -6.16602 | -47.27978 | 2025-08-29 05:06:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ffeb5e92-3d08-3c76-acd2-783332a850bc | -7.72272 | -50.27658 | 2025-08-29 05:06:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1a477fdb-ccd4-3b36-8f33-f6f703ae028b | -9.4331 | -47.63956 | 2025-08-29 05:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f43cf007-cdf5-371d-bc0a-5729fe6eee05 | -8.08265 | -45.02398 | 2025-08-29 05:06:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 24caa5a1-1d96-3f48-b47e-dd3db17ecc49 | -7.40844 | -43.3838 | 2025-08-29 05:06:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4b11152-d5af-384e-b647-e9a36ee23594 | -8.70836 | -47.87 | 2025-08-29 05:06:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1177705b-d70c-3d52-a67e-9df1fee4695f | -6.22207 | -43.33304 | 2025-08-29 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07aed3cb-99ae-3f2b-8806-4c216a66908b | -8.90585 | -47.32403 | 2025-08-29 05:06:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 903a7ca0-c5f9-3215-a652-f423faad42b3 | -9.49803 | -45.38181 | 2025-08-29 05:06:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 996cb176-0e77-3665-881b-f127b9c03575 | -6.33736 | -58.18541 | 2025-08-29 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d0082d4-14e7-3c73-83e3-45b00e134482 | -9.43185 | -47.64908 | 2025-08-29 05:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 76a6e66b-4912-336e-a0b4-22a4baead96c | -3.66601 | -50.95282 | 2025-08-29 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dabb9f6-30b1-3a82-bc60-1cf2c107818f | -3.53029 | -52.99029 | 2025-08-29 05:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b9e31c7-5467-3f81-aea3-e29b2fbfd7f9 | -3.76159 | -54.81385 | 2025-08-29 05:06:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7765d69e-25af-3276-ab2f-f0e796a74abd | -7.02182 | -44.67508 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30ec9782-f6f8-3270-ac20-07ed04777d02 | -6.88298 | -43.61369 | 2025-08-29 05:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0d51e5f-360e-363f-9ed0-de70b43f1cbc | -6.38926 | -45.58158 | 2025-08-29 05:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bdaac051-1b52-32cf-b339-e2dd0def5b5c | -9.49816 | -45.38751 | 2025-08-29 05:06:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 527049fe-b0fd-3c1f-9332-08829c0f6276 | -5.61946 | -45.00027 | 2025-08-29 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5611280b-23f2-34ca-88c0-ee53a49347fc | -7.72586 | -50.28468 | 2025-08-29 05:06:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 843c9fa0-bdb5-335b-a0ca-4e41ced05131 | -6.70546 | -49.45707 | 2025-08-29 05:06:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 89c939a5-7dd0-37fe-84b3-7e3ffaac185c | -9.49024 | -45.39431 | 2025-08-29 05:06:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c512d32e-d221-3f95-aa0d-5fcd3c82f693 | -6.72348 | -43.57455 | 2025-08-29 05:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2fb196ad-7d67-373e-8a28-359a146fd066 | -8.08327 | -45.01922 | 2025-08-29 05:06:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 85f01af3-9f61-3222-8e82-0826cd9d794d | -6.98483 | -59.33724 | 2025-08-29 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5fd5860-42ef-374e-aee9-5d6c710e8f5e | -4.09791 | -48.19811 | 2025-08-29 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3228657-730f-349f-8405-fd19bb3f4d02 | -3.4263 | -49.04772 | 2025-08-29 05:06:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| aff3491b-1a02-3c4d-839b-21a069f335c1 | -8.45099 | -43.71472 | 2025-08-29 05:06:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bafabdb7-f89e-38a4-a1a6-0a33b010357a | -6.70865 | -49.46629 | 2025-08-29 05:06:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3029b221-e62d-3f29-9f75-1f2bda312b89 | -6.45152 | -44.56142 | 2025-08-29 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82cd2288-4a1c-31c9-8d1f-d02264160899 | -9.69862 | -47.06576 | 2025-08-29 05:06:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dbbed8e2-a74d-37a8-a345-98009f56ff4d | -6.44356 | -44.57418 | 2025-08-29 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09fb391c-f52f-38eb-861d-9dbce97907cf | -6.97973 | -59.3453 | 2025-08-29 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a745cc1e-4ee4-3ede-b0ae-ed6c19a15cda | -5.86779 | -42.96489 | 2025-08-29 05:06:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 063b3cd4-47f8-33b8-96f3-dd147e86c29c | -7.04555 | -44.36342 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a7f2c4b-2b33-3e6e-aff6-977e137c0136 | -8.55695 | -51.3117 | 2025-08-29 05:06:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4ca02a88-b3a5-34d5-afef-08152faf25e4 | -6.45761 | -44.56242 | 2025-08-29 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e64512f4-d504-36d6-a044-95831ef62403 | -6.88251 | -43.61436 | 2025-08-29 05:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92067118-da9c-39ad-a2de-87246040273b | -9.86644 | -44.68568 | 2025-08-29 05:06:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f673b111-5894-3c8f-9f17-d8600ad260a8 | -8.55491 | -51.31502 | 2025-08-29 05:06:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 04634dc6-5b12-3c0e-bfbe-ca3d1ee567c3 | -4.5871 | -43.3184 | 2025-08-29 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27277edc-fbfe-3a1e-862a-005923c2539a | -5.78843 | -42.60408 | 2025-08-29 05:06:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 693f00c4-6d9a-31f5-b56a-577d2c7a6991 | -7.3924 | -45.93244 | 2025-08-29 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea008ecb-2e70-3830-aa20-2a2f7708607e | -3.82469 | -54.12793 | 2025-08-29 05:06:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21bbba1f-8973-3dcf-9a17-f6d613622e9b | -9.68862 | -47.05746 | 2025-08-29 05:06:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5768ee79-dcf7-3982-aca4-e7055f34fb1e | -9.86011 | -44.68474 | 2025-08-29 05:06:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4fcc5637-8b7c-38bd-9c01-2eebf7c01630 | -3.76105 | -54.8173 | 2025-08-29 05:06:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| abedce50-5e87-3490-ae7f-0ac1e4223379 | -6.44481 | -44.56493 | 2025-08-29 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f49bd0b1-9e7f-3827-8afe-819275f7e05c | -8.70591 | -50.36576 | 2025-08-29 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8e76d990-1e92-33ae-8b1b-febc6e3e99e7 | -8.44581 | -43.65181 | 2025-08-29 05:06:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e543c6c-553d-30e2-a0a7-3dd3e6f48c23 | -6.44292 | -44.57889 | 2025-08-29 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 38b26177-e6ec-343d-94e4-c7766452b8a0 | -5.61967 | -45.00689 | 2025-08-29 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 92c36e12-e88f-3c12-9016-dd6e94931c69 | -7.02742 | -44.67962 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c932943-9c3d-3bb0-8d3a-4e2aa83efdd1 | -9.68818 | -47.06092 | 2025-08-29 05:06:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b63583ab-59f0-3842-9695-6e9654929d00 | -6.54413 | -43.92396 | 2025-08-29 05:06:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ea98f16e-fe4b-3b71-b1d9-c53344411470 | -6.97149 | -59.32607 | 2025-08-29 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 906825a4-a257-3c2c-9039-59f455dc2d6a | -9.68769 | -47.05796 | 2025-08-29 05:06:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 085db63b-efe9-3a91-801e-8fc6eab397e7 | -4.13043 | -54.90001 | 2025-08-29 05:06:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4b9ac90-2908-3da0-a98e-f4b874aad050 | -8.43498 | -43.65878 | 2025-08-29 05:06:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a51548ab-d2e7-3635-96c3-6de18061a5ca | -6.38777 | -45.58081 | 2025-08-29 05:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 957577c9-20b6-3d8d-9e3e-9161c3baaa77 | -7.4018 | -43.38274 | 2025-08-29 05:06:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 117a385c-966d-3647-aa63-f3f9af29a543 | -5.6943 | -45.95935 | 2025-08-29 05:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b3dcf3ef-86ed-3ba9-823e-c370355b2dac | -6.3872 | -45.58473 | 2025-08-29 05:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de2c1256-ec95-3f59-a198-740401e39702 | -7.21561 | -45.31228 | 2025-08-29 05:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9e33e9f-2d2f-3d55-a941-0c3e7fc5898f | -5.33005 | -51.32518 | 2025-08-29 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 102e677d-1262-3949-819e-3a51c92bdbbb | -5.62004 | -44.996 | 2025-08-29 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f97e883c-8a64-399b-9215-aec5746b498d | -3.76383 | -54.82128 | 2025-08-29 05:06:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 0154d82c-7d14-3157-aeba-d1941fccc501 | -8.69614 | -50.38202 | 2025-08-29 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README60.md)
