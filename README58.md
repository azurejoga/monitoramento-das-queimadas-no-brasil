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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74e520dd-62e5-3c90-8988-46aed0f6f5dd | -3.72114 | -50.16794 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d40bc650-dced-3cf8-9f74-749acd4fa8f3 | -7.87628 | -48.41656 | 2025-10-29 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dd1cdcce-ebb9-361d-81a4-3b13b8d449bd | -6.53941 | -46.76225 | 2025-10-29 04:44:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 685c95d1-b8c8-3f45-9015-c942d3d07e18 | -4.66793 | -46.4009 | 2025-10-29 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd6c8ff8-ca0b-323c-9b81-119391ddbe8f | -7.95364 | -47.8442 | 2025-10-29 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f8bb115a-e199-3b11-9f9c-13a5e9cd109f | -7.75695 | -44.71975 | 2025-10-29 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cf384d63-4f1d-34f3-8cf0-5a0a185b6cd9 | -6.24387 | -42.55864 | 2025-10-29 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aee341ca-fdec-30af-84f4-d2d8d29d2216 | -6.10332 | -42.47398 | 2025-10-29 04:44:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 77e5a1aa-79ad-3696-a8b3-1b4cea02bebe | -5.33928 | -45.54939 | 2025-10-29 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f59ccb25-a3a3-3521-8421-37979c1e7ee8 | -3.0911 | -49.50748 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ae509875-fe00-3b5a-8ffd-464301878d4a | -4.06554 | -49.35905 | 2025-10-29 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5efad59e-0e51-3949-964b-edac34c6014b | -6.52133 | -44.5657 | 2025-10-29 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0827c8ff-23d1-3318-b314-6982af6f666e | -4.47753 | -43.44543 | 2025-10-29 04:44:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 975a6537-7336-31c1-8aaa-2192b42293b4 | -7.34834 | -47.64442 | 2025-10-29 04:44:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6241e15b-2269-3d56-aa0b-811f6fdf879b | -4.21678 | -50.08347 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c5fb9b2a-c910-39b7-982b-56bd348a1f15 | -8.18052 | -44.4515 | 2025-10-29 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd1de2c7-6092-34c4-bee5-361fa066838c | -6.96633 | -46.23884 | 2025-10-29 04:44:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dbd446d5-d912-3e73-887f-fd933a5d49de | -7.79071 | -46.45895 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0da890b7-5895-3bbd-abb0-716bf1d0ea61 | -4.52684 | -46.04483 | 2025-10-29 04:44:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 335899ee-3ca8-35d8-aa6e-0f2004a0a6ee | -7.74675 | -44.72736 | 2025-10-29 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f0aae28-fcf7-3e4d-9967-681dcc0c39eb | -5.53194 | -41.7124 | 2025-10-29 04:44:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 41425744-a9d5-31fb-bcc1-902452283a21 | -6.13633 | -41.71078 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5d3180af-ed17-3b1f-a300-984218e45d1f | -7.70088 | -46.90557 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cee08b45-7642-345a-8232-e5d6b6f4bee5 | -7.98221 | -45.53509 | 2025-10-29 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39f1eaaa-afea-377c-a5b9-76cd80987002 | -7.30086 | -44.9878 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd35c1ba-35fa-35bb-8bdd-d96b33016f10 | -3.33926 | -44.1954 | 2025-10-29 04:44:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e91bd250-0499-3fe2-af2f-5689a5819495 | -7.80012 | -46.45014 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a4fb5be9-8d5a-322b-ad00-85d1a3be48d0 | -2.77125 | -45.40578 | 2025-10-29 04:44:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22cf103d-f5c1-3c05-a930-993875c977d1 | -7.07805 | -44.9454 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3ebd336f-b71d-369e-aae4-68559a0ea777 | -4.14571 | -50.68579 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9461e4df-3e36-3dab-b544-bf6fa0e5a086 | -6.81074 | -48.64622 | 2025-10-29 04:44:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ec84e27-a10e-3a58-aeda-f0fa815bd270 | -7.95534 | -45.45363 | 2025-10-29 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f747d06-3541-3231-88d7-b7bc1f95f8ee | -8.55804 | -47.01528 | 2025-10-29 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b7403f1-918c-31a0-857b-a66c0390a0c4 | -1.27817 | -52.92462 | 2025-10-29 04:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17e4cc54-2c52-3f00-a3dd-25224ccd1b4e | -3.7855 | -45.58925 | 2025-10-29 04:44:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 833159e1-543d-3343-9845-832ad79b866a | -4.32263 | -55.61488 | 2025-10-29 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f664b04-fd26-340a-9cb3-ce9e590f8d1c | -3.52386 | -53.06612 | 2025-10-29 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc5b27bb-74a5-3247-bc92-ed982dfa07a4 | -4.65959 | -46.40449 | 2025-10-29 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d75bc9f-97ac-39da-987f-d53e9c9cac3b | -7.30556 | -45.68165 | 2025-10-29 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48781c1a-a345-3dcf-988a-cd96c205ada9 | -6.22793 | -42.53421 | 2025-10-29 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f7075129-db30-320f-9ad9-3391041c4660 | -6.10977 | -41.72102 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5a7aff84-d336-3f23-adb7-bde0e2061726 | -5.54133 | -48.12759 | 2025-10-29 04:44:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76cc4363-bd3d-3bba-a4b3-91016a543980 | -3.34358 | -44.19603 | 2025-10-29 04:44:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b75925a1-6789-3b61-896e-b6cd14232ef0 | -7.98293 | -46.20129 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9e4bc23c-e7ad-3ef9-b965-86e0714a5d04 | -6.46886 | -42.24352 | 2025-10-29 04:44:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ca06e3fd-be4e-3f6a-a7bc-4bb03cf7a370 | -8.33376 | -46.15695 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 396c76f4-acd5-3fa6-8d0f-1984efa3f33f | -7.79862 | -46.46024 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 44dc129e-9649-3882-80a2-17771debaeda | -4.72392 | -46.81672 | 2025-10-29 04:44:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46d82404-1940-30e6-9fa7-92a336484af8 | -2.13613 | -47.99979 | 2025-10-29 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1125c1b-1c3f-3e63-8a6f-d1955eca4b59 | -5.35788 | -46.1129 | 2025-10-29 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66b03d83-6a35-30bf-9228-e238c7bb5f62 | -4.29545 | -49.64878 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 58caa278-dde1-37dd-b980-ccf89f399e12 | -4.14518 | -50.6892 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9ccf1ef-99b6-3cbc-bfb4-c27049dbc0ed | -3.98283 | -56.2193 | 2025-10-29 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 991700dc-6862-3077-8af9-727e757542ea | -7.90122 | -45.67706 | 2025-10-29 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2d803e7-8d42-3216-9978-f9b103dc908d | -6.14331 | -41.56367 | 2025-10-29 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6875b99c-e053-3c24-8a50-cdba1740b051 | -7.43763 | -45.12369 | 2025-10-29 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 856eb27d-5bb6-36a4-8970-cd33d7e001d8 | -6.96063 | -49.40338 | 2025-10-29 04:44:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3a33bb30-ce89-3057-9269-f569b2598250 | -7.79787 | -46.46528 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3b9eb688-62e1-3031-9a1b-01f3fe3573c1 | -4.86364 | -45.77753 | 2025-10-29 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60f2706d-b7a0-3cab-b4e0-0e4bdc7587a0 | -5.42827 | -46.12561 | 2025-10-29 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86e7bfc8-0305-30ab-865e-c1d09da27d9f | -5.61154 | -47.1186 | 2025-10-29 04:44:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 500a2dac-0b10-3bd1-adc5-7792477e0444 | -3.40481 | -52.72503 | 2025-10-29 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 305288db-15a2-3559-a8bd-568a86a925fe | -5.55018 | -51.32245 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b66000dd-4f62-3bf9-aeea-029e80aaf595 | -2.80499 | -49.14539 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc7c3fa5-e26e-3db3-a843-a16f47fe68ce | -3.42311 | -50.11755 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1a650c0-c54d-3f36-8c66-ec44e4c52749 | -8.40202 | -46.92848 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fb5208f9-6543-3d13-8a54-ed1aac0cc91c | -7.07793 | -46.10493 | 2025-10-29 04:44:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df3e7824-a3ff-3eba-a5b7-c41cb35d4881 | -7.33831 | -42.46814 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7d02bf35-9a62-37b3-8b45-f5b3007ce360 | -8.22048 | -50.47991 | 2025-10-29 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa60c31d-4609-3a07-a7bb-86c4ef644112 | -6.96174 | -49.3961 | 2025-10-29 04:44:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2448920a-6b64-391c-b199-f6858597c8d9 | -6.24424 | -42.55598 | 2025-10-29 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6bfbeaa4-dc9d-3a81-9b4a-26cf67eaf718 | -6.12232 | -41.70955 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8cdcfc40-5fa7-35c3-8b6f-dbdeb8e9a77a | -6.94347 | -47.00817 | 2025-10-29 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6bddbd67-48c7-3523-add3-0ac973f75243 | -2.02497 | -46.99926 | 2025-10-29 04:44:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d57030d1-ca91-3f86-ab37-6aa7d408260a | -2.76414 | -45.39953 | 2025-10-29 04:44:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 912b6374-a27d-3bc3-8175-43e2aa2f5143 | -6.28059 | -47.88135 | 2025-10-29 04:44:00 | NOAA-20 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d34f2cb4-c1d9-3095-8e08-1f238e59c1e8 | -7.94884 | -45.46846 | 2025-10-29 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dfa82f9c-b2b2-3f86-a0e4-82a407956f6b | -6.29519 | -41.88442 | 2025-10-29 04:44:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| ba3ec386-91be-3d51-ab6f-78686edf7f9e | -7.30463 | -44.99246 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5336a568-2727-33c7-a7b2-a81b39c8b21a | -7.80238 | -46.43486 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a8afa2a3-6846-3f53-993c-0064478d8d58 | -7.79638 | -46.47534 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f8dff92-f494-332d-a6d1-1bd9aecfc4e4 | -5.33578 | -45.54509 | 2025-10-29 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e9c25d3-b537-39f8-95aa-1c5eb985c084 | -5.65266 | -47.82653 | 2025-10-29 04:44:00 | NOAA-20 | AXIXÁ DO TOCANTINS | TOCANTINS | Brasil | 1702901 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7dfa648-8c2c-3523-b2ec-faced9473aef | -8.1867 | -46.94714 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d100871e-982a-311e-bc59-a82dffe114c2 | -3.14709 | -49.21666 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea76c23c-140f-3a86-a8d7-f8eec92d069d | -3.04379 | -50.26174 | 2025-10-29 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b996504c-b807-38a3-b58e-b5290b583c99 | -8.05892 | -46.94515 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a49a9aa-2108-3527-a9cb-abfd427aace7 | -5.92996 | -43.3343 | 2025-10-29 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5e0222e8-a69d-3750-a91a-1417a15364f8 | -3.47793 | -50.02749 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aeed4eeb-d456-35de-b961-bf51fc954081 | -3.03995 | -50.26466 | 2025-10-29 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 309d25d9-2195-317e-8edd-8a1862d242a7 | -3.16878 | -48.61629 | 2025-10-29 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a6a9412-bec6-3217-b397-9643a07a39a3 | -4.22063 | -50.08054 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb774fc5-0b91-3144-af17-2b07f34b11d3 | -8.18211 | -45.70695 | 2025-10-29 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fa084a5-840e-35d8-9a1f-f5cad1993450 | -1.29226 | -55.68427 | 2025-10-29 04:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50b31e20-e603-3639-8784-ee15a1a86e19 | -4.65482 | -42.52052 | 2025-10-29 04:44:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e38d5d99-dd40-3c8d-b289-45a3ba58d99a | -2.83288 | -49.3995 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7176dc5-9ee7-3155-aa98-a50e04513214 | -6.13305 | -41.71075 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 767270c8-9f06-34c7-be3f-b4081c35c87a | -7.07922 | -44.93712 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ce40bbeb-e47c-3234-998e-5c5740d68377 | -7.27185 | -46.90648 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 137c3a0d-e3dc-3aba-b4ad-d8515457fc0c | -7.90208 | -49.17671 | 2025-10-29 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README59.md)
