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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fc16b95-0421-3b09-b434-c88b659d3352 | -17.3442 | -42.6333 | 2025-08-29 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 175.1 |
| d9581ad1-df7c-3acc-b7a2-c62181bf9f39 | -9.462 | -60.549 | 2025-08-29 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 4092cdcf-c658-3f08-8174-5dbcb37ca06e | -9.4452 | -47.6364 | 2025-08-29 00:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| fca0a0a0-a514-33dc-9cd2-ce2d4a07e85f | -9.4433 | -60.5499 | 2025-08-29 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 173b9ea9-0c20-370d-920a-b1ded519afd0 | -24.1861 | -49.5515 | 2025-08-29 00:30:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 46ff5d20-1768-3dcf-a26e-f26b8f1f3253 | -9.4263 | -47.6384 | 2025-08-29 00:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 98229592-e62b-305b-b2a7-670116c4a4f5 | -3.4254 | -49.0517 | 2025-08-29 00:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| c1764547-e861-3541-b248-8ff5ccce8efa | -10.3624 | -57.8258 | 2025-08-29 00:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 895485c6-388a-330a-9603-1b4105a59f9b | -12.0784 | -44.7199 | 2025-08-29 00:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 4b1f23ce-429d-32e2-8a80-2259794c03fb | -6.5358 | -43.9237 | 2025-08-29 00:30:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 95cc084b-6f41-3de7-b8ac-bff01d0719f5 | -7.0569 | -44.3623 | 2025-08-29 00:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| db1f675b-2595-3e68-9190-b4ec714e8c3f | -6.2244 | -43.330101 | 2025-08-29 00:31:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c3174c6d-5c0d-3b2b-b432-17c4193ec751 | -11.2925 | -43.546501 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6533df2c-2441-385b-87ec-9eef4359a13f | -11.2909 | -43.539398 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9cc72798-c95f-3112-86b1-74f3f1ea27c9 | -7.0416 | -44.357498 | 2025-08-29 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b66a5de0-f601-34dc-9952-aed2ed3d4b85 | -3.7562 | -54.796101 | 2025-08-29 00:31:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee873d98-9888-388b-96af-8e77e4e1dfae | -3.9747 | -43.2411 | 2025-08-29 00:31:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f139c43f-00ee-3937-890f-6b7f36095cc7 | -3.9885 | -47.958302 | 2025-08-29 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8cc17b8-bc1d-3724-8cf7-fc2a4c6514bf | -2.9921 | -48.606201 | 2025-08-29 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 464a8215-2310-36b3-8f66-149a3ab0984c | -11.1231 | -45.108398 | 2025-08-29 00:31:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 65469e66-058a-3572-bc87-ac857ecc0391 | -15.0423 | -45.657501 | 2025-08-29 00:31:00 | METOP-C | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dc4a64e1-c614-30fe-8073-959fc98e756c | -12.0926 | -44.974998 | 2025-08-29 00:31:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9df61d23-8e9a-3143-ba77-9ea49f57f848 | -5.7884 | -44.873501 | 2025-08-29 00:31:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ebac59c8-e93b-3853-9b2e-313c0681cf4c | -11.2399 | -44.986801 | 2025-08-29 00:31:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eccd9d89-19e7-3ae3-a05a-fe81a7a0b1a6 | -17.349701 | -42.639801 | 2025-08-29 00:31:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9510e2b3-935f-3f8e-abda-972c3a79c957 | -8.4297 | -43.666599 | 2025-08-29 00:31:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e57ddf7a-8c09-3c61-af48-38e25e54c6a0 | -11.09 | -44.780201 | 2025-08-29 00:31:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0cad45c3-04f1-368d-b3c1-60eeb03ab24e | -11.0968 | -45.129002 | 2025-08-29 00:31:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aaabaf92-3cbf-31ec-80f7-a0684070e5c4 | -8.4671 | -43.6502 | 2025-08-29 00:31:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bbde6540-c66e-3f1b-b287-429dfa6553eb | -8.7523 | -47.395901 | 2025-08-29 00:31:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca96f3f6-dac4-3712-9bf4-1ea3a737fc6f | -6.2262 | -43.337898 | 2025-08-29 00:31:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ffd63dc-c6da-3672-8106-a898eb265b1f | -7.4317 | -42.056499 | 2025-08-29 00:31:00 | METOP-C | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 54f44ca9-6833-32dc-b20c-a5f276bc188e | -3.7698 | -54.811699 | 2025-08-29 00:31:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93d5ac32-5d2c-3b75-b93d-f09c74fcfd9b | -8.4495 | -43.708 | 2025-08-29 00:31:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 54e0ab8b-7159-3014-86a4-a3ca215f5c45 | -11.4647 | -47.298199 | 2025-08-29 00:31:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 84c834a6-4f51-3661-87d7-6f0279cce443 | -15.847 | -41.853298 | 2025-08-29 00:31:00 | METOP-C | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ea1b7205-fc01-3498-beff-a0a774f0e24e | -13.3754 | -46.8778 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| efdc9f7d-2d81-3ec0-bb6e-ed1dccc19c25 | -7.2309 | -45.448502 | 2025-08-29 00:31:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47330947-c30e-3a11-b065-203af404cf56 | -8.436 | -43.6497 | 2025-08-29 00:31:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fc07b3d9-fbb2-3d1f-8b9c-664743178dec | -11.6203 | -47.305599 | 2025-08-29 00:31:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bae02d98-9599-3514-89fa-baca235dee10 | -11.3136 | -43.549 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 452df4ad-2f3a-3b06-a170-67224b848e37 | -11.3528 | -43.539902 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 298a7d9e-ed5f-3ff3-82e9-37cf3db37b0c | -20.2883 | -41.307301 | 2025-08-29 00:31:00 | METOP-C | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a7edc85f-927d-3d44-8147-d5edf68bfa7b | -17.7712 | -44.495998 | 2025-08-29 00:31:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| be662ddb-68d4-337d-ac47-fbfb5aca836e | -7.6165 | -46.235901 | 2025-08-29 00:31:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af648d38-4406-3269-a62e-74b0d7752c9a | -13.422 | -46.951302 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| de62658c-2c9f-3796-87ca-de22755779b4 | -3.6206 | -43.536301 | 2025-08-29 00:31:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6784ab6b-7f72-340a-b9b7-a0318df9708e | -7.751 | -50.267101 | 2025-08-29 00:31:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07779632-8ace-36fe-a3f4-e5258f35e192 | -14.2623 | -48.066002 | 2025-08-29 00:31:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 82cd9318-aff7-3312-a25a-66b6d2194c57 | -13.5454 | -46.857101 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fe3958f9-85d4-3d08-9ef0-24ad00cc316d | -7.2293 | -45.441601 | 2025-08-29 00:31:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b25a359f-70be-37ab-8b64-d06a7955c1a9 | -6.8226 | -44.347801 | 2025-08-29 00:31:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc90184d-b849-3313-a534-71d6879708cf | -11.5852 | -46.2551 | 2025-08-29 00:31:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 383d29a0-01f5-3bd4-b9f6-d91117393b33 | -11.3578 | -43.561298 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e0f65a8f-5e69-3b99-8f4c-2f7bdf80d319 | -5.7953 | -42.601601 | 2025-08-29 00:31:00 | METOP-C | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9d8d4e10-92da-3a55-926e-b78d36318c2f | -11.5703 | -46.373699 | 2025-08-29 00:31:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c1fc205a-f885-3253-ae6b-d52a48a36781 | -11.6147 | -46.202499 | 2025-08-29 00:31:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08398426-52bf-324b-8cf2-1af4e2f0fd7b | -8.9123 | -47.329201 | 2025-08-29 00:31:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38e12bac-47d8-325f-b223-01436c832f55 | -4.5128 | -43.690498 | 2025-08-29 00:31:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af4a24a9-dff3-3ec8-8c8f-21ec1f9cdb41 | -10.7053 | -47.0676 | 2025-08-29 00:31:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61535f01-3e53-3698-b6a1-47cf6cdf2083 | -11.5605 | -46.3759 | 2025-08-29 00:31:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0bc5bcea-c697-34c1-aa99-4d3358acdb3f | -6.1396 | -44.428799 | 2025-08-29 00:31:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a754cfea-2050-3a9d-801a-3569884660c1 | -7.0465 | -44.378899 | 2025-08-29 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef32a28a-b4e4-32cc-8857-2c212ffc58d5 | -9.6964 | -47.061901 | 2025-08-29 00:31:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 854bba6a-6a8d-3be3-abdc-1a133fe2ed17 | -24.182199 | -49.5849 | 2025-08-29 00:31:00 | METOP-C | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | nan |
| c9373ae9-d483-3b05-9d80-6d9ece7cd325 | -15.0532 | -48.134201 | 2025-08-29 00:31:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 458d7f14-426a-364c-b393-f4363932044b | -13.4237 | -46.9594 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6f56ce9f-2c49-3a1c-a8f0-dbf9d36bf69a | -12.0369 | -50.632599 | 2025-08-29 00:31:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc6a99ae-2baa-3471-b6d2-0250eed2b90a | -11.1247 | -45.115398 | 2025-08-29 00:31:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b6a93c3e-75c4-3ffc-a503-45fd89e322f3 | -13.5373 | -46.867199 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8ab8668f-6756-34ce-87a3-d7820f04b5a5 | -7.0449 | -44.371799 | 2025-08-29 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0311c8f7-9a7d-35ac-bae6-27a0e86b67a9 | -24.189199 | -49.5667 | 2025-08-29 00:31:00 | METOP-C | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | nan |
| d1b3cd4c-c337-3ec5-aca2-ab8ad0b2c5d8 | -6.0269 | -44.477001 | 2025-08-29 00:31:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6be122eb-84fe-3ed7-b351-740649620b56 | -6.6074 | -43.643799 | 2025-08-29 00:31:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f25a0832-c00a-31ca-bd0f-2dde877ed851 | -13.0764 | -46.3508 | 2025-08-29 00:31:00 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 71a7801f-a7e4-36bc-bee3-d9bc90d1784b | -17.348101 | -42.632599 | 2025-08-29 00:31:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 38382a5a-6e6b-37dd-a805-ab37d913bb18 | -10.029 | -48.0597 | 2025-08-29 00:31:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f6271987-36d0-3aac-8395-ce82d59917e3 | -11.3398 | -43.572899 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 36d98996-86fa-3efd-bfc7-160171444c9e | -13.5126 | -46.847599 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9e64530b-b31f-3aa3-9bb2-725ea180e3b8 | -6.2012 | -43.319099 | 2025-08-29 00:31:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 574c0bae-e0f1-310c-816f-519e50559f06 | -6.6172 | -43.641499 | 2025-08-29 00:31:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 285b2882-d056-31f3-9df7-7030a640887f | -7.63 | -42.720901 | 2025-08-29 00:31:00 | METOP-C | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a63c6bc9-7393-3c8d-8661-edb6ef43e365 | -11.5932 | -46.384102 | 2025-08-29 00:31:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1fa1a2c1-4875-3861-96d4-89a3a098b70d | -13.5505 | -46.881001 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 824f51c0-b544-365c-8fca-b0e6fac11e07 | -6.5671 | -43.692501 | 2025-08-29 00:31:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1fee04d9-df7d-3629-a204-f132e3d6ebae | -7.2458 | -45.423401 | 2025-08-29 00:31:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18e98d1b-99a2-3d1d-b866-de8610a6c339 | -9.4446 | -47.643501 | 2025-08-29 00:31:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f4927316-32f7-3655-bfbe-802957037a36 | -17.0483 | -45.8708 | 2025-08-29 00:31:00 | METOP-C | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 56f0f060-179e-347f-aa0b-9e43c978bca0 | -6.7259 | -43.576801 | 2025-08-29 00:31:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c02e1764-2250-3262-a0cf-d189c1f6e522 | -6.5584 | -43.921001 | 2025-08-29 00:31:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ae95570-7d78-3877-9cc3-c5735bc71773 | -13.1938 | -45.294498 | 2025-08-29 00:31:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6226ee56-e70e-3494-954a-55813df63272 | -3.4321 | -49.047199 | 2025-08-29 00:31:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0eacb728-d62f-3705-8df4-dbf82d0671c1 | -6.1379 | -44.4216 | 2025-08-29 00:31:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4e868f5b-635e-376c-9eae-78658121d72b | -13.5782 | -46.8666 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0b60868b-0156-3d7a-af2b-4f1f9e7fa6e5 | -22.6859 | -46.8433 | 2025-08-29 00:31:00 | METOP-C | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 245252ce-e262-3951-bf00-76f4d56da530 | -6.091 | -43.9972 | 2025-08-29 00:31:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a896bcb5-6fd3-39e8-832b-e84749a73d5e | -11.5719 | -46.3811 | 2025-08-29 00:31:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 55609ff0-cd73-3ce6-b5b7-81f7fe4a156c | -10.0319 | -51.087502 | 2025-08-29 00:31:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cbd5c04a-b80a-30d9-aadb-be9b4e7170a4 | -7.7336 | -50.281399 | 2025-08-29 00:31:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a139d7c6-9d3a-34b1-8a24-9f09b423cd00 | -6.2756 | -43.814602 | 2025-08-29 00:31:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
