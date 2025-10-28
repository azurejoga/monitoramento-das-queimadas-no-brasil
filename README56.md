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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c99cf8ef-6422-3076-836d-4de25a2f3cbb | -7.78052 | -45.38196 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f16cdfa8-6a97-3da9-aed4-f027961ef321 | -7.46822 | -47.15755 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b508070-f32f-3efa-aa2c-e5b7ef782638 | -7.98914 | -46.73863 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6595858e-ce89-33b3-84c6-2c845980d75e | -7.86847 | -46.39717 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 52a446f4-710c-379b-b187-2c038d4f8029 | -7.36493 | -47.78945 | 2025-10-28 04:42:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ff84678-f603-3c5c-a85c-173b0fa48a05 | -2.50412 | -49.05013 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ded7aa13-3571-3183-af58-b0e76164c208 | -7.9503 | -45.53003 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 4605277d-8f73-3f8d-9909-c172ba592382 | -3.70594 | -47.6492 | 2025-10-28 04:42:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4eb428b0-e71c-3b14-b125-dedaa1f87a09 | -6.11965 | -42.4539 | 2025-10-28 04:42:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c65d7ec8-ecf5-3782-acb0-654c5d645e7b | -6.30045 | -44.70434 | 2025-10-28 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 392eec0a-fbc1-3783-99ff-2d5d7f1fe041 | -5.83991 | -43.27034 | 2025-10-28 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07c85f8a-bd3f-3ed1-87af-b246e7fceef8 | -4.41563 | -45.61017 | 2025-10-28 04:42:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a950f893-268a-374c-8e0b-26d6aeec2860 | -3.59766 | -47.51551 | 2025-10-28 04:42:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8400ae53-83b4-39f4-a2ed-c26ac1a15d17 | -1.49772 | -53.12685 | 2025-10-28 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b62b85b0-aef8-3196-8226-8d01692aae4c | -4.75369 | -46.42064 | 2025-10-28 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2545f623-4578-3d9e-b70d-38caace2c6d8 | -6.49384 | -42.22287 | 2025-10-28 04:42:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 052adf64-64a0-3e29-8b71-817bab67962d | -3.47175 | -49.96902 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cffb475-6920-3c46-95d2-dacd65117e60 | -7.25843 | -44.99853 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c875764b-1f61-38ba-a526-72cef877e732 | -3.22594 | -48.76707 | 2025-10-28 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ee874eb-19ce-3c08-838a-93adf5ecf84c | -8.16384 | -47.0118 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 029d7078-1d43-3002-ad69-27b41f1fbe72 | -2.44748 | -49.02658 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 444294bc-c4e5-380a-a2a7-b456f424a2a1 | -3.70649 | -47.64566 | 2025-10-28 04:42:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f48cda19-3889-305b-8d1d-7a1722edbf58 | -7.76065 | -45.40853 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e2d25a56-129d-3ad8-84d5-7065d8707b65 | -6.69893 | -42.04776 | 2025-10-28 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 12c55fb9-ac44-361d-bbef-f0133fe5a13e | -3.24063 | -50.65239 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56f6bb0d-2e62-35ab-a79e-159b5bfb0a90 | -4.42517 | -48.91006 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c334fab-985b-3325-9069-eb142f0f5639 | -6.88661 | -45.03144 | 2025-10-28 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d983ed6-06aa-3fad-a279-135cfd42bb43 | -5.70553 | -49.1962 | 2025-10-28 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1034c22c-874f-3887-9e2a-39770c9bea30 | -7.8375 | -46.41226 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 75882ccc-f9d8-3449-a54c-eccc1e84ca71 | -6.38618 | -45.76717 | 2025-10-28 04:42:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9ebdf0b-e473-385c-b424-dedc25b30d1b | -6.86607 | -43.44717 | 2025-10-28 04:42:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3714233e-bdaf-3624-a417-43be582b7340 | -7.19637 | -46.73848 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86270d3b-acc1-3f7e-93d4-a73a6fde9f58 | -7.07165 | -44.94226 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f65981cd-f11d-3e8e-95ff-9c03047e102f | -8.04438 | -41.11359 | 2025-10-28 04:42:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 25d1e2db-4a1e-396d-9ccd-86d4fc48fa07 | -5.41482 | -44.84155 | 2025-10-28 04:42:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edf49711-1e79-3299-92cb-60c8538dbdca | -6.17053 | -47.8444 | 2025-10-28 04:42:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e80dd7db-763f-32af-80c7-efa096a3003c | -5.48084 | -47.74711 | 2025-10-28 04:42:00 | NPP-375D | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1192bad7-77e3-3252-868f-447a9a37395a | -5.61343 | -47.11038 | 2025-10-28 04:42:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62967da3-5354-3d85-a30d-e89cff856963 | -3.58508 | -43.63546 | 2025-10-28 04:42:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 944c6353-f2a5-3b8b-9245-f553b33ff3c7 | -3.25772 | -44.07676 | 2025-10-28 04:42:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4879336-9a26-3310-9ed1-f312789f4903 | -4.85214 | -46.73995 | 2025-10-28 04:42:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ee76e34-17e6-3792-a33b-5f01ed905866 | -4.72591 | -46.81225 | 2025-10-28 04:42:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 737046e9-0042-3200-9b9d-de6336451a06 | -3.86043 | -43.35241 | 2025-10-28 04:42:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3dacf91-f862-3930-93f1-792f56a3d116 | -3.58951 | -43.60623 | 2025-10-28 04:42:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c90fb848-b6a8-3984-afa4-87d04c2f1f25 | -5.84049 | -47.56575 | 2025-10-28 04:42:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a013756-0cb5-3fe0-af86-771d9a7bfdf5 | -3.54694 | -54.69624 | 2025-10-28 04:42:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c49d86c0-eb40-311c-bbaa-742ad508226b | -5.6518 | -47.63525 | 2025-10-28 04:42:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6e28ebb4-dc1b-3b71-9a2b-c4e82f3c5bf2 | -7.35905 | -47.64277 | 2025-10-28 04:42:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 953ed0c9-527e-31fe-a67b-79863ff3f44e | -2.75592 | -45.4059 | 2025-10-28 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9301acea-ec3c-3cce-8f32-8192e6a0d95b | -3.11851 | -49.10769 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a4fe84b-d429-39b3-8dda-82b70511623d | -3.53127 | -52.96825 | 2025-10-28 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a96445b-e6a4-3819-93f5-35877104eeb0 | -2.19985 | -56.97325 | 2025-10-28 04:42:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed9a4287-36c0-3498-9c50-0eb0c6aac894 | -7.07181 | -47.36829 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cca2ebd2-204c-38b7-87a8-844964afde5b | -7.3077 | -44.10253 | 2025-10-28 04:42:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71ef3ec0-f302-3e99-a3a7-013d63a63ce1 | -7.26239 | -44.99913 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c609a3b-9374-35a0-a45f-10e459bceb3b | -7.41504 | -43.95311 | 2025-10-28 04:42:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ee15790-13a0-370d-8ecf-ae092e309420 | -5.8477 | -46.44888 | 2025-10-28 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4cfc22ef-746c-384d-8452-fc05afcdbe33 | -7.74097 | -45.32598 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a819416-aa94-3964-b6e3-4be81eddade6 | -4.20337 | -48.36366 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5241bdea-86f4-3d3c-9003-fd4bd2a62767 | -5.7974 | -35.60826 | 2025-10-28 04:42:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0ee45b2d-e3be-349c-91ba-2a9620480cbd | -7.25941 | -45.01935 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 496442d7-8550-3491-90b1-ba9ad3c0d813 | -3.79849 | -51.64465 | 2025-10-28 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0f30a5f-f76e-3a2b-82eb-7fa16d87f389 | -9.27522 | -45.5739 | 2025-10-28 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85c3f7fa-1687-3522-af1c-5c4b0ad47435 | -13.22437 | -47.08398 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79eb780b-a2d8-3802-8450-12b944bb05a0 | -8.63323 | -44.79705 | 2025-10-28 04:44:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d659175c-992e-3274-ae88-bd11316014a0 | -14.31256 | -46.52026 | 2025-10-28 04:44:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a288cf5c-4faa-3583-b22d-c65ff90e13dc | -12.52685 | -47.54148 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| deaa19c6-a1c1-310c-a149-fc57de471442 | -9.5875 | -46.89698 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c84546c4-b028-33d4-8686-7b5a5decf1e7 | -13.5423 | -49.57597 | 2025-10-28 04:44:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75f11651-cbe9-3c8f-b689-6c69e5958f7a | -14.75972 | -44.9551 | 2025-10-28 04:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b80d9e3d-2714-3e71-a95c-10d228f6a659 | -9.28993 | -45.23103 | 2025-10-28 04:44:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a06db9ed-4708-3214-a287-938c1eaaa448 | -10.5835 | -49.80275 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5851f53-5c62-346a-9f6e-c868357b5515 | -13.3185 | -47.69175 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dac01783-0bf7-3b17-8e8a-92461da1ba93 | -12.14374 | -50.97169 | 2025-10-28 04:44:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39483c6b-a1d3-3cf7-b23b-81f12ce96909 | -10.41887 | -45.16834 | 2025-10-28 04:44:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 624e14f1-d338-3945-a9a4-9380c2a80fb1 | -10.21165 | -49.88455 | 2025-10-28 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4a1f083-a1e6-33c6-9707-009a847a54f6 | -13.67273 | -46.5105 | 2025-10-28 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 96327d8b-e65a-336e-9b1a-14e8d3e79d84 | -11.79842 | -52.49801 | 2025-10-28 04:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02dd432a-d049-35df-b328-eceeee8acc4b | -13.91302 | -48.47881 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be14f4be-53df-3e41-8175-f45ba7386504 | -14.73411 | -47.36074 | 2025-10-28 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de67edeb-5b75-31c3-bca5-40c8b62532c1 | -13.42235 | -47.39058 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8052fac4-4261-3c31-a1a1-e1d5d9661b68 | -13.74132 | -48.42034 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b93ca0e-eaac-3d07-aa23-83bfdc574175 | -13.87795 | -48.49534 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2522af5f-a7b0-3c7d-ab39-65c99d4221b8 | -8.86634 | -45.40552 | 2025-10-28 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e173d27-f964-38eb-be4a-f30665bda43c | -10.2891 | -47.23384 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7ad2cdf3-274b-31cb-8640-e49e6e7a4979 | -12.23943 | -46.52758 | 2025-10-28 04:44:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89435ccd-f39a-31db-aa3c-93628ad2e823 | -8.64448 | -45.28576 | 2025-10-28 04:44:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 53.3 |
| ff2dde78-466a-3c9c-8a6f-aa1c4c19cf56 | -11.10056 | -44.02471 | 2025-10-28 04:44:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fcf903b-48e4-34e2-b484-e2d55b801b76 | -9.34496 | -51.01648 | 2025-10-28 04:44:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64760baf-3b0e-3531-9ba1-7c8a636848c3 | -10.94 | -48.02852 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e848019d-52ae-3601-81c0-ddc9c9240cb6 | -10.6741 | -48.05046 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c3d0b22-9bd3-3957-ba1c-a81dea906be9 | -8.86462 | -45.40692 | 2025-10-28 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89e2731c-d130-34c3-b9aa-e6fcb622b2b9 | -15.15595 | -46.60894 | 2025-10-28 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 608beae2-c2c9-3909-bf67-550743b99cf9 | -10.768 | -44.75305 | 2025-10-28 04:44:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c1e7f2c-30ef-3f06-8e52-3b0ba7105fad | -12.23978 | -47.92501 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5beb42df-eeb2-34a8-8f5c-80ae5f5e080c | -13.53651 | -47.16125 | 2025-10-28 04:44:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4575d50c-1ac5-3cc9-9d5d-94975a3ab19a | -13.90624 | -48.37723 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5ff85ff-1dfa-3f8b-9aab-b669e7165c3a | -13.34167 | -47.42323 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48b956a6-952a-3a61-8b19-4cb1196118be | -15.23206 | -47.94558 | 2025-10-28 04:44:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd22a298-ae1a-301f-858c-72720d2765c6 | -10.99216 | -50.36248 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README57.md)
