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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 593d9df0-6352-325f-bfa3-49d5895f39d4 | -2.63813 | -48.04446 | 2025-09-25 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1462a863-9528-3d1b-a0c1-9ed491f4c1d3 | -3.74642 | -51.38257 | 2025-09-25 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13a56fbd-6beb-334e-b516-97ff3b83cbcf | -5.93375 | -42.92346 | 2025-09-25 04:59:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 57c2983a-3474-3013-92de-cceb8a13a66c | -5.51744 | -43.87214 | 2025-09-25 04:59:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81fb22d4-34c0-38d3-bb19-8fcb88337cac | -2.92484 | -48.3069 | 2025-09-25 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 22a210a0-2438-30c1-9f84-5c0d2b4f3388 | -3.20703 | -54.95879 | 2025-09-25 04:59:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d5874b8-f3fc-326f-be1a-64ecdee7077c | -4.45547 | -55.25377 | 2025-09-25 04:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c46277d2-4759-39a5-9e2a-8c01cd83e253 | -5.7678 | -44.27468 | 2025-09-25 04:59:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a8d3029-ea2b-31d6-87c5-9c45cb09965a | -2.91723 | -48.30205 | 2025-09-25 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 580e78ed-8663-3a7c-847c-54e78089efb2 | -7.32169 | -45.75623 | 2025-09-25 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8718dcf1-e928-3de1-8543-dbf6d5e45a84 | -6.59669 | -44.62162 | 2025-09-25 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 040acf15-6054-3434-97a2-782fb535b672 | -2.92373 | -48.31404 | 2025-09-25 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 3d3d63be-c808-369b-9dbe-bab8bf829cd4 | -6.34719 | -43.36275 | 2025-09-25 04:59:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f21d109f-62a9-3a1b-94d4-59852958b47d | -6.59859 | -44.61922 | 2025-09-25 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7299a66b-71e5-3650-a23b-221119a85813 | -5.52374 | -43.86915 | 2025-09-25 04:59:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c61d8943-fbb9-3497-9bef-783ff2064c17 | -4.04157 | -49.5324 | 2025-09-25 04:59:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa5829e8-d0e2-3174-aa1e-bd667d44ca1e | -5.79311 | -42.80756 | 2025-09-25 04:59:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c2c6c0b8-07d7-31cb-a898-70ec0ff55b61 | -3.3816 | -52.71413 | 2025-09-25 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 521d3bf7-5bb5-348c-8748-7499aa6c8fba | -5.51802 | -43.86814 | 2025-09-25 04:59:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69059869-40f0-39e4-9526-9ad8e0901df9 | -1.60887 | -54.31797 | 2025-09-25 04:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92f0d0d0-285d-3a42-8ce4-46f39566a515 | -3.78759 | -52.30195 | 2025-09-25 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 116f5e54-6f1d-3680-8b63-e9333fb34e1a | -3.30508 | -42.17632 | 2025-09-25 04:59:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5837216a-9f7e-394b-8ebd-0f203d3336ab | -5.95551 | -42.9022 | 2025-09-25 04:59:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7beb6063-c89e-335c-9389-004932df0623 | -4.76867 | -43.255 | 2025-09-25 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e16758d-1141-3b8a-a041-a5c4ed433751 | -5.23045 | -43.69083 | 2025-09-25 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea8bdb7c-ca90-329f-ac3f-3c34a8420572 | -3.78597 | -41.74478 | 2025-09-25 04:59:00 | NPP-375D | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bc02ee8c-075b-395c-9386-50b08efecebf | -4.15699 | -50.22948 | 2025-09-25 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8311d46b-ec84-3f63-87e1-11fa7d79d6fd | -3.37753 | -52.87095 | 2025-09-25 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d3cfc07-0b2f-3a8f-8d92-6974c4be507c | -5.52316 | -43.87314 | 2025-09-25 04:59:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3859bbf8-e856-33a1-bbd1-2be190a1abb8 | -3.8284 | -50.97348 | 2025-09-25 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 806ac5c5-853f-3cb9-836d-fc1c4798e6db | -6.12514 | -44.00125 | 2025-09-25 04:59:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61267966-3a02-3611-8c13-7404db3cf957 | -3.23707 | -46.7977 | 2025-09-25 04:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb3c5f2d-646f-33f6-8653-2af14b46607e | -6.68847 | -43.1381 | 2025-09-25 04:59:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87f08943-6bb4-3dda-a7b7-104715444251 | -3.31567 | -48.72681 | 2025-09-25 04:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eac986ac-c85b-3dd4-9c95-4474b05d4de2 | -4.34548 | -50.5023 | 2025-09-25 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d645209-3f6b-3f85-a943-cadb263a220a | -6.59617 | -44.62547 | 2025-09-25 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 675b3c61-7360-3fa5-b42e-84c717988b25 | -7.25876 | -43.02459 | 2025-09-25 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f320e394-8e01-395b-982e-b40a8d26e1e7 | -2.68754 | -48.47322 | 2025-09-25 04:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cba9ffc6-3716-3b25-95c3-38b82fc1d6a0 | -4.17063 | -54.63523 | 2025-09-25 04:59:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc12ff60-3c7c-3aa8-a2cf-5a36eb3b1811 | -3.20985 | -54.96292 | 2025-09-25 04:59:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 235ae910-f92b-3b83-83f7-ac29b0718f4e | -3.78672 | -41.73961 | 2025-09-25 04:59:00 | NPP-375D | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5cd22370-ecce-3f0f-b2ca-e48f8dd04988 | -2.6387 | -48.04078 | 2025-09-25 04:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 292b8ca2-c4fc-337c-8501-7bd3ef13c24e | -4.8043 | -43.53767 | 2025-09-25 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 73c40b3b-0272-3f1f-9ad4-d2d810d3a811 | -3.81715 | -50.9758 | 2025-09-25 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a5cf4e4f-3823-3d2d-bcec-944754a23486 | -2.70416 | -54.6526 | 2025-09-25 04:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ffca3d87-4d9b-3314-9903-53563f7d9b5f | -3.82902 | -50.96952 | 2025-09-25 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 84e445b0-c45a-3ad0-9c49-ba879ae18210 | -4.79882 | -47.27658 | 2025-09-25 04:59:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd913b93-596b-33ff-a02f-b968997d4a58 | -3.62879 | -51.91073 | 2025-09-25 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5673d8c3-2e1a-3378-a4fe-a3a1dba33440 | -5.30183 | -44.43624 | 2025-09-25 04:59:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 938779f7-8177-3316-b35e-3cd546852ac4 | -7.04201 | -46.41845 | 2025-09-25 04:59:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4c3925ce-00fa-367c-ba33-656624dbbf86 | -6.55499 | -43.83799 | 2025-09-25 04:59:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce8ae6a8-0b50-3281-b3c9-24b427d7fc50 | -3.58976 | -55.55907 | 2025-09-25 04:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb9f0c7a-2740-3a92-8c95-0b815ddf104f | -3.82486 | -50.97293 | 2025-09-25 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d698200f-195a-355b-a3c8-5b7a06cc6644 | -5.2294 | -43.70138 | 2025-09-25 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb6f05f3-d1ba-349b-a0ce-b3050df17fc7 | -1.09028 | -54.10987 | 2025-09-25 04:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f64021e-e368-311e-91e1-710636fce2f1 | -4.60243 | -43.91456 | 2025-09-25 04:59:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c67d92d2-4185-39fc-a169-7236dfe86759 | -4.80897 | -43.54641 | 2025-09-25 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53636a09-9e6a-3bc8-85ba-3c360038f738 | -2.19537 | -54.46739 | 2025-09-25 04:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e2f8999a-641d-3414-a8ad-534db7a06a14 | -4.01069 | -43.27023 | 2025-09-25 04:59:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97989d6d-1d5f-37a3-a03f-7406d73cf371 | -4.45805 | -55.43619 | 2025-09-25 04:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad0a30a1-0044-34f6-acde-4a1a9eca636e | -3.08953 | -52.91842 | 2025-09-25 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0f107dd-591f-3dd3-b20f-01b06c5b44ab | -2.91667 | -48.30565 | 2025-09-25 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb0c6d5f-3eda-3948-87ca-67fb6775970f | -2.14483 | -53.64933 | 2025-09-25 04:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a9d99f5-7557-3647-8d6b-b3b6bab5dc85 | -3.43527 | -44.48493 | 2025-09-25 04:59:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de9191f9-a755-3cca-9603-ed5eea0d31cb | -4.8908 | -44.95377 | 2025-09-25 04:59:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb5bc34a-b572-3acb-83ed-8544c5e2cb56 | -7.09737 | -44.09728 | 2025-09-25 04:59:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 716dc422-faa4-3508-a6aa-f6a26fa92e3a | -7.32127 | -45.75933 | 2025-09-25 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 358b9430-afd1-3b67-a918-675672459179 | -3.78824 | -41.72922 | 2025-09-25 04:59:00 | NPP-375D | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 83da299e-fded-37fa-8a7d-626a32686d6d | -1.53238 | -51.61474 | 2025-09-25 04:59:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48b8f5a9-95ee-3c81-86bc-e93732130e81 | -4.67509 | -48.1571 | 2025-09-25 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a1952291-2aae-3533-adcd-dd5d1364bd7a | -4.24723 | -53.55418 | 2025-09-25 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75f84b12-0041-35dc-bcc2-935994562b05 | -3.69676 | -49.56919 | 2025-09-25 04:59:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d0ec567-7660-31ca-884c-e58cf2643f00 | -2.26783 | -47.1952 | 2025-09-25 04:59:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08f840d8-92d3-35de-922c-da5a9e8e1c40 | -6.59804 | -44.62308 | 2025-09-25 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4375457-3a9b-3862-a4cf-93a919b1bc7f | -5.61738 | -42.99935 | 2025-09-25 04:59:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c3657922-78f8-3940-b940-462d6c8d21b1 | -3.43578 | -44.4816 | 2025-09-25 04:59:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3c485d7-3637-34b7-af44-0d2884df8633 | -5.95484 | -42.90701 | 2025-09-25 04:59:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a8827ecc-b386-3a53-b975-98bc6dc01a30 | -4.79316 | -50.7405 | 2025-09-25 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67530043-2d2f-333b-8f98-b4d226f2f601 | -5.78635 | -42.81104 | 2025-09-25 04:59:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3dd20986-8a4d-3f6f-b2ba-9076a8ef0085 | -3.78748 | -41.73442 | 2025-09-25 04:59:00 | NPP-375D | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3c86b819-e749-3236-bdee-591542e14b0b | -5.6012 | -45.36044 | 2025-09-25 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6bfdb968-b6e2-3519-bda3-8ff40e1d0147 | -3.35613 | -51.60201 | 2025-09-25 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c1dcc30-9430-30ab-9dd0-66b19405594c | -2.25338 | -47.88524 | 2025-09-25 04:59:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba9aa1c7-3edf-310f-b2b0-30aad12be992 | -3.82424 | -50.97689 | 2025-09-25 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3dd2f48a-ce9b-34d2-b656-6dab7a7739dd | -3.9088 | -54.56209 | 2025-09-25 04:59:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7dfa6336-aa32-33ad-ad3f-82c3310f66f4 | -5.00355 | -45.17361 | 2025-09-25 04:59:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54255c89-94bb-38c0-bf79-c754d41ab5cb | -5.93438 | -42.91893 | 2025-09-25 04:59:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6b7dd07b-b327-3718-af82-2e1489edfd52 | -3.82131 | -50.97239 | 2025-09-25 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8ceb28c-72a2-3816-89d2-fba37469f431 | -5.00878 | -45.17433 | 2025-09-25 04:59:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2e8f2c6-1021-3f9f-a45c-bbc67046829d | -4.60809 | -43.91537 | 2025-09-25 04:59:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51754bb1-b534-306b-af5e-ca0530b0dbca | -3.82778 | -50.97744 | 2025-09-25 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| db5ebb8c-7de2-378e-be11-a7128f50996a | -7.09722 | -44.09498 | 2025-09-25 04:59:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36f62462-1259-347b-8581-02bf95e2adbc | -4.78529 | -43.20732 | 2025-09-25 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2efb16d3-9e88-37fa-ac25-1c3d3373a118 | -2.69104 | -48.47725 | 2025-09-25 04:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd26829f-a4e4-3149-a7fb-c79f06d26bfe | -5.06125 | -44.31699 | 2025-09-25 04:59:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da38096f-32cd-384f-a572-fadaad381933 | -1.76996 | -55.49863 | 2025-09-25 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35a16b6b-4790-33c3-9353-c28191b8c84e | -5.52945 | -43.87019 | 2025-09-25 04:59:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5bd9a63b-6bc1-38ac-b0e0-4178324e19a4 | -5.79372 | -49.13938 | 2025-09-25 04:59:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9fa6965-a893-3a6c-a204-5967a7d9031e | -5.51229 | -43.86716 | 2025-09-25 04:59:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55ecf06e-e29e-3c16-991e-234a4faad6b8 | -5.00307 | -45.17687 | 2025-09-25 04:59:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README29.md)
