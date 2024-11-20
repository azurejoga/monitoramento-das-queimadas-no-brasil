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
| 53cc3ec8-0b2b-3e4b-8331-07f9f08952f7 | -3.7705 | -41.611401 | 2024-11-20 00:09:00 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 32d76583-073b-3b68-a880-875d8e51a66d | -3.7628 | -44.0709 | 2024-11-20 00:09:00 | METOP-B | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3bfbb8bd-a238-3e29-8727-c30e31cee00b | -7.9918 | -44.371399 | 2024-11-20 00:09:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6137ce31-2c51-375b-a841-46d94b82d1d6 | -1.1862 | -46.539101 | 2024-11-20 00:09:00 | METOP-B | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d63e65b2-7067-342a-8f7c-630d0be4cd1a | -3.0167 | -45.333801 | 2024-11-20 00:09:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 64472c39-ef25-30a8-8f62-769806e8c494 | -3.7947 | -47.804798 | 2024-11-20 00:09:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68618120-7360-35ba-8c4e-e64bd18f943d | -2.6682 | -46.1675 | 2024-11-20 00:09:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a8d4d437-a72a-3af1-84b1-9decf5408040 | -5.2464 | -43.8409 | 2024-11-20 00:09:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3119085e-a36a-3f19-83b0-505bb158533d | -2.6552 | -46.155399 | 2024-11-20 00:09:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0dc52d69-6b9b-3fda-98b0-abceaa45b737 | -4.1459 | -45.5005 | 2024-11-20 00:09:00 | METOP-B | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3cc77f48-fc59-3392-accf-80c40bc6cc44 | -4.4022 | -43.1161 | 2024-11-20 00:09:00 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1ea103e-6417-3a46-8bdb-7387d058a997 | -2.9803 | -49.180801 | 2024-11-20 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 892042ab-f86d-3223-8541-182e8a24fdf3 | -2.8169 | -45.1329 | 2024-11-20 00:09:00 | METOP-B | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 65b424b6-2a01-3023-8095-ce93f162909a | -5.8303 | -42.550098 | 2024-11-20 00:09:00 | METOP-B | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| debf7fcd-50b5-3d72-a07b-0b5c8e3281d6 | -1.481 | -47.438202 | 2024-11-20 00:09:00 | METOP-B | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20271533-be95-3112-82f6-37c95b1c1c68 | -5.7099 | -44.803902 | 2024-11-20 00:09:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e31ec74-9182-38bc-893a-13362296273d | -7.7995 | -42.732101 | 2024-11-20 00:09:00 | METOP-B | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 698a03cd-16de-34db-b06c-921e1e72db16 | -4.6092 | -46.424599 | 2024-11-20 00:09:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1c9f662e-9274-369a-b1c7-b0d9f0a3f61a | -2.6288 | -46.221199 | 2024-11-20 00:09:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ab8b3a39-2ee1-3085-9b76-74fe6aab8ae8 | -2.1586 | -48.396599 | 2024-11-20 00:09:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e552a7cd-ac9e-3a95-b00a-1d15e88a247f | -6.5298 | -44.187401 | 2024-11-20 00:09:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 90317491-e2d0-3122-81a7-d30c15183f25 | -2.9795 | -45.443501 | 2024-11-20 00:09:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b4a4044c-2744-31ad-8ff7-0cc2f8e9baaa | -0.9188 | -51.703701 | 2024-11-20 00:09:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 2207f54d-05f7-33b8-bcfd-0b8447b380af | -1.7537 | -46.131199 | 2024-11-20 00:09:00 | METOP-B | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8f6e71cb-bbca-3c38-ab27-72d1f2968857 | -3.8026 | -47.794201 | 2024-11-20 00:09:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4294a7af-19a4-3fc1-87ec-8157d7e73cfe | -3.0004 | -50.986401 | 2024-11-20 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff85fc47-8435-3922-9284-57ccd4440aa5 | -2.9862 | -45.427601 | 2024-11-20 00:09:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 528afffe-6c68-3c2e-9295-e03f9c50bbd2 | -2.5422 | -48.042599 | 2024-11-20 00:09:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1ed0aac-9eb7-3728-85f7-41e78032f319 | -2.9008 | -46.838402 | 2024-11-20 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7035dcf-df0f-3318-8bfd-d79e8108812f | -2.7325 | -51.8102 | 2024-11-20 00:09:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd4dc838-8280-335a-8dc5-33a1bb3d9d14 | -9.183 | -44.733799 | 2024-11-20 00:09:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 707673c4-338a-36ca-8088-fbcc54e84c7b | -2.677 | -46.068501 | 2024-11-20 00:09:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0c7371ca-64bf-38d0-9dd8-3492487f788a | -2.1155 | -48.525799 | 2024-11-20 00:09:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e777385e-2743-32c9-806a-e66f276149cc | -2.7705 | -47.6367 | 2024-11-20 00:09:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bb19acc-1b84-3b51-a895-2380f49d2252 | -3.1681 | -45.2281 | 2024-11-20 00:09:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ffde4213-6554-3f5c-b5fe-d0cddadcc1e5 | -3.313 | -43.085999 | 2024-11-20 00:09:00 | METOP-B | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 627e534d-f8ac-3d80-bec7-1f9dcf2d82ed | -4.068 | -50.023399 | 2024-11-20 00:09:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8295475b-3a67-38e5-a2c1-c700f9865712 | -2.6402 | -46.2262 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1d1da91a-50ce-3293-ba16-27eedc7491f7 | -3.794 | -43.2523 | 2024-11-20 00:09:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d31b9300-7165-397c-ae8b-c38f33f22b51 | -4.1796 | -46.806099 | 2024-11-20 00:09:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e17179c2-8a79-38e2-86b3-e9c9a872aef5 | -3.0311 | -49.4561 | 2024-11-20 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef53f518-93cf-3ef1-86d3-4300291ca755 | -1.668 | -46.024899 | 2024-11-20 00:09:00 | METOP-B | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 270504ae-b85d-3aaf-95e7-3305086a4f29 | -0.9383 | -51.699402 | 2024-11-20 00:09:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 5246a961-2b9b-3c9f-ba74-1ebc6567cd45 | -3.2634 | -50.508099 | 2024-11-20 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9af97c8d-f386-368a-ab47-d4dfabbbeb52 | -3.4733 | -50.299 | 2024-11-20 00:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3eee144-d36e-3495-91c2-809d6af3738a | -3.3713 | -44.437199 | 2024-11-20 00:09:00 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12c90e99-bc78-3d24-9e33-25c8770bd740 | -3.8007 | -47.785801 | 2024-11-20 00:09:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d6593c7-4b99-3aa3-a0cc-c492ffcd798a | -2.923 | -48.321701 | 2024-11-20 00:09:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5a4a9c0-4b41-3401-b2cb-da7d9c70ae53 | -2.7445 | -45.314602 | 2024-11-20 00:09:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7d236c1a-8ec1-35a8-8517-22e9424dd669 | -10.8695 | -44.407001 | 2024-11-20 00:09:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 539fc370-cb51-3120-85cd-3ccb24b94248 | -3.3114 | -43.078899 | 2024-11-20 00:09:00 | METOP-B | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8e5d6c3d-cbae-3e73-be14-be6b52352e0f | -4.2444 | -43.0112 | 2024-11-20 00:09:00 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d927d0f0-59e5-3c7e-9a92-e6a9094b8953 | -2.2096 | -46.464401 | 2024-11-20 00:09:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5772ab75-e8d1-31f8-9f2c-f6458eefa945 | -2.2031 | -46.481098 | 2024-11-20 00:09:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8078ab48-40c4-30c5-bd88-1418d58386b7 | -5.0039 | -41.955601 | 2024-11-20 00:09:00 | METOP-B | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 085b084d-36a5-3f02-9a62-5072edd70f00 | -9.1798 | -44.719299 | 2024-11-20 00:09:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d78ae487-e60a-38dc-bcae-b9ebf6e9d0b0 | -4.1628 | -45.622398 | 2024-11-20 00:09:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 54c41227-f1c4-3b23-b08b-c5d997a20743 | -1.0353 | -51.720699 | 2024-11-20 00:09:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 166b4c65-a420-3978-8e70-b6be010647e1 | -10.406 | -44.402802 | 2024-11-20 00:09:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fde1265c-839c-3ff6-a7c7-301faa1c836c | -1.6105 | -52.5989 | 2024-11-20 00:09:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76c64926-5fd4-381c-9311-f2d8883e02a3 | -2.5464 | -46.542801 | 2024-11-20 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e0317ab-cdc7-37f9-adbc-c73a4eb76c20 | -2.6517 | -46.231201 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f8274e47-613e-38da-a19c-cff33bec0d32 | -3.8583 | -46.0564 | 2024-11-20 00:09:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1e7d6d57-3ce3-34c5-bfdf-0c20ddaacceb | -11.0272 | -44.564602 | 2024-11-20 00:09:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fe989769-be78-3764-9af7-1128f92c967a | -14.8603 | -43.141499 | 2024-11-20 00:09:00 | METOP-B | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 81b165d5-a949-3ccc-860c-c528ba9fa1b0 | -2.6197 | -45.126202 | 2024-11-20 00:09:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| feadab03-4f9b-3b9a-9e00-23f40d58092d | -3.2661 | -50.520302 | 2024-11-20 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac3782d1-ef79-30d6-bfce-6818ef9b9297 | -2.1447 | -47.4147 | 2024-11-20 00:09:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ea4caf4-d87b-3147-8629-740e765e1dcd | -5.9076 | -39.1357 | 2024-11-20 00:09:00 | METOP-B | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 24584e38-2d49-38f6-b046-009939c216af | -3.7687 | -41.603401 | 2024-11-20 00:09:00 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 69b15e6a-8a86-3aa8-b54c-f965aacc4935 | -3.0053 | -45.329102 | 2024-11-20 00:09:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d7992d01-4c6a-3ac3-89d8-67cab5b39934 | -2.2047 | -46.4883 | 2024-11-20 00:09:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a62a3928-0bc5-3afd-9007-dc6856bbb637 | -10.9315 | -44.408501 | 2024-11-20 00:09:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b5b32272-0e27-33a2-a96a-bd7b1b3fa557 | -5.3839 | -46.998901 | 2024-11-20 00:09:00 | METOP-B | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5ca2d60e-a0e9-384f-a696-c9967744fd5e | -3.0353 | -45.737999 | 2024-11-20 00:09:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 496ed097-2ab4-3640-a0dd-a3f154acc63b | -3.3584 | -44.4258 | 2024-11-20 00:09:00 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d7a86ff-0742-3c64-b068-a8bf93eebc82 | -4.5693 | -48.0103 | 2024-11-20 00:09:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c40287ad-1b65-30c4-b318-cf9d3432d6a4 | -4.6711 | -40.686901 | 2024-11-20 00:09:00 | METOP-B | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| bbe7b18d-2723-3b99-9dc9-37407d645120 | -1.4404 | -47.119999 | 2024-11-20 00:09:00 | METOP-B | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 290adb06-4201-3bef-84e4-c1b36bad4aeb | -4.0979 | -43.5928 | 2024-11-20 00:09:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d0a7a87-2189-3804-b584-338311f08de7 | -5.3654 | -44.967499 | 2024-11-20 00:09:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e10ca339-9590-30ce-8e54-ad4a7397b68d | -0.9414 | -51.712898 | 2024-11-20 00:09:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 21983bc4-be44-3605-9742-e0747ce18284 | -3.2201 | -48.873402 | 2024-11-20 00:09:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d8f9362-e88e-3d4c-8a04-560151f27f94 | -10.0533 | -44.717602 | 2024-11-20 00:09:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 20876b66-6130-3e8d-83c2-e631ad5f4377 | -1.7553 | -46.138199 | 2024-11-20 00:09:00 | METOP-B | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5cc643b1-0c34-3d1b-8d62-fa822a7a0589 | -3.7726 | -44.068699 | 2024-11-20 00:09:00 | METOP-B | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9878b89-b969-3dac-9b5c-377d115a202c | -2.6533 | -46.2384 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| be6d6c7b-9685-31e2-819f-eb2f41a31226 | -2.4931 | -47.223999 | 2024-11-20 00:09:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b347009-83cd-3408-9427-33a11a562d09 | -10.4383 | -44.881302 | 2024-11-20 00:09:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d9f3ceff-6f69-37eb-bc13-dc932f4a615f | -2.29 | -48.478401 | 2024-11-20 00:09:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8759aa29-7a26-35df-9f12-0a67b3381d10 | -2.6217 | -46.556999 | 2024-11-20 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 578cbb68-3fbc-3804-98d2-b22375efa0b1 | -2.1136 | -48.516899 | 2024-11-20 00:09:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ef2b8bf-8c97-3f1d-965d-51ead186c08a | -2.3067 | -46.851002 | 2024-11-20 00:09:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79d40628-300f-3697-ba1f-3bd2adf9d754 | -2.5074 | -44.993401 | 2024-11-20 00:09:00 | METOP-B | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6cb2673e-f3f1-3527-a445-1c060a5b8ba5 | -2.6786 | -46.075699 | 2024-11-20 00:09:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| df07f88e-b168-36ab-876c-053a80dc3a0d | -1.1263 | -53.489799 | 2024-11-20 00:09:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 527b15ac-2f7b-3e61-b2ea-a66350794577 | -10.4367 | -44.873798 | 2024-11-20 00:09:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 24c7f8be-a9b4-351a-86b5-08f87fe2c4c4 | -10.9397 | -44.399101 | 2024-11-20 00:09:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 85f8389b-30c2-328f-b2dd-e16014d9e39a | -9.1782 | -44.712101 | 2024-11-20 00:09:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 81dee43f-e558-3199-a8f5-66b6bca06dd9 | -1.183 | -46.524799 | 2024-11-20 00:09:00 | METOP-B | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
