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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46cb5f9b-551a-33d6-b3ca-1e628482b1da | -4.6085 | -46.5002 | 2024-11-23 03:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 134.0 |
| b1aa9ffe-c3a1-38f8-9ac7-83e2902f722c | -4.2605 | -48.697 | 2024-11-23 03:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 142.5 |
| eaff7169-0ee9-3234-b5ac-b87f7b011ce4 | -1.6075 | -52.5977 | 2024-11-23 03:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 63304d91-3df0-3006-9f2b-6c34b898e5a1 | -3.2768 | -53.8199 | 2024-11-23 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| d9df965b-e738-36f2-b0a2-29bd83d559e6 | -4.5216 | -42.9078 | 2024-11-23 03:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 865ca8a0-2925-3b52-8630-b74e59549474 | -2.4456 | -49.0816 | 2024-11-23 03:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 41aeb57e-fa8d-3b8f-90b9-4ce8b8b29315 | -1.7359 | -52.7385 | 2024-11-23 03:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| e6066d9e-80e1-373e-8429-e389816f485e | -4.2606 | -48.6755 | 2024-11-23 03:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 00301c81-e4dd-3279-83d1-0bef7527177c | -1.7359 | -52.7181 | 2024-11-23 03:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 124.1 |
| fd18eb8a-99bb-3a79-90e6-bfaf8559199b | -1.2596 | -51.762 | 2024-11-23 03:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| bf4d81cc-298e-3015-8e5a-5654046f0653 | -2.70404 | -46.2733 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c2d3a72-92dc-3565-8ee6-500d3c849b6f | -2.93858 | -48.01738 | 2024-11-23 03:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0236e1df-a212-3ea5-9e79-3d88db2a8c21 | -2.4756 | -46.03274 | 2024-11-23 03:53:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f8a9b903-63b4-3d71-aabf-f52c55f0bd13 | -2.76462 | -45.93552 | 2024-11-23 03:53:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 652cf362-8f58-3c89-a6a8-35593802ad28 | -7.95844 | -37.90788 | 2024-11-23 03:53:00 | NPP-375D | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a4a16343-f534-3514-a02f-68e27201d586 | -1.96207 | -48.38544 | 2024-11-23 03:53:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1be9eca7-4fd3-3f9d-81bb-ef38be3aea17 | -9.24699 | -39.17816 | 2024-11-23 03:53:00 | NPP-375D | CHORROCHÓ | BAHIA | Brasil | 2907707 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9906611e-346a-38dd-87a2-f475e1763c3e | -3.33154 | -45.35156 | 2024-11-23 03:53:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f224bea2-eda9-344f-bd14-e408f6958254 | -3.95392 | -41.49666 | 2024-11-23 03:53:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7e20ecb3-1b78-30f3-9418-b7382d58fa9c | -3.14137 | -44.48526 | 2024-11-23 03:53:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abd42c6e-e155-398f-a8ec-16a2c21d10ca | -2.82378 | -45.15812 | 2024-11-23 03:53:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b93621cb-70bd-3cb9-be54-9f10badca3ee | -6.32924 | -46.03665 | 2024-11-23 03:53:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dc81c20c-40d4-375d-8c6d-b5df4d75a7ad | -2.71607 | -46.10178 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc681523-6071-3a4e-8c95-a28e301a6ea2 | -10.5808 | -36.98265 | 2024-11-23 03:53:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cd622f4c-4234-3bd9-8902-8d33dcf03e27 | -7.30047 | -39.6218 | 2024-11-23 03:53:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 16aa34fe-3d38-39f3-91e5-f038b09d7e4a | -2.64879 | -46.24732 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 451ead6b-41cf-3730-9493-6f0e56009055 | -7.21417 | -47.05893 | 2024-11-23 03:53:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02f30612-1949-3e68-a5e5-7f90d8d420ea | -3.26627 | -45.13099 | 2024-11-23 03:53:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c001fb2-a8bb-30c6-85b5-26ae0c4c93ba | -9.38402 | -35.9318 | 2024-11-23 03:53:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 7570503f-0917-3428-aa42-0a3df703ce7e | -10.59659 | -36.80679 | 2024-11-23 03:53:00 | NPP-375D | PIRAMBU | SERGIPE | Brasil | 2805307 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 10c4e843-85a4-3b52-967f-c071d0d100ad | -9.73037 | -37.02853 | 2024-11-23 03:53:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 27204472-3b8b-348f-9547-305651827dff | -8.15303 | -38.24319 | 2024-11-23 03:53:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7a259798-72b8-3a5d-9af5-24fff9c211cc | -2.13053 | -46.40264 | 2024-11-23 03:53:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2e1a7ee-f3ab-3e78-ab40-e6c15f5ecc23 | -2.67954 | -46.16035 | 2024-11-23 03:53:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13768b94-743d-396d-919a-74c8949aede7 | -5.56855 | -50.9492 | 2024-11-23 03:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| baf1e258-628a-3669-8a76-210c1674213a | -2.68036 | -46.25273 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8e37fc3-5855-3c5d-bb55-a0b2b21def2b | -7.30383 | -39.62234 | 2024-11-23 03:53:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b667fc49-200c-3301-a1ef-d96c3a14858a | -6.14621 | -46.68264 | 2024-11-23 03:53:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cbab955e-f86b-3aa0-8871-a84abfddab29 | -8.68612 | -40.47347 | 2024-11-23 03:53:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dcff8204-0c1a-3e12-8a9f-d7fd70093347 | -2.69929 | -46.2692 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91a90bf6-0ae0-350c-b552-c4eac5b39558 | -3.34197 | -45.17178 | 2024-11-23 03:53:00 | NPP-375D | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fdcc41e1-64f1-36e6-ad20-40a07d5cacf4 | -7.07118 | -40.00101 | 2024-11-23 03:53:00 | NPP-375D | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c3ab305f-0b79-3799-b4cc-f5da4e5f64a4 | -2.71354 | -46.28144 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a90cc05-ca45-37cc-975c-007036666ab1 | -3.14484 | -44.48441 | 2024-11-23 03:53:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f8fab1d7-dcbc-34c3-ab73-e40a21cfcd60 | -3.16193 | -45.90668 | 2024-11-23 03:53:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b85d89b-7ae9-3e21-81c6-d9466099ebc5 | -6.36559 | -47.14972 | 2024-11-23 03:53:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3a1af93-fc0f-3818-84a7-f68171d4640b | -2.68423 | -46.16444 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 689010e5-2274-31dc-bc48-3b754c7a4995 | -2.70298 | -46.27973 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ea6f71e-6182-319c-9f4d-db6e9bac1345 | -2.68586 | -45.66393 | 2024-11-23 03:53:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16bd3fbb-7249-3386-a514-365347818f84 | -2.65878 | -46.25234 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e2db1be-163d-3fc6-b5ff-47fd95bcd265 | -2.65931 | -46.24912 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aec156ec-350e-317d-bd38-b1ba659edbee | -2.94399 | -48.05763 | 2024-11-23 03:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c863a22-cd4b-3d20-900c-5eb2ab674184 | -2.7067 | -46.09372 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8660192b-38f9-3947-a939-1179bd33e64d | -2.93738 | -48.06082 | 2024-11-23 03:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70e87b44-7643-300a-83f3-3dba13db5404 | -2.74736 | -45.9763 | 2024-11-23 03:53:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28e2cea8-4c47-3dae-be30-c14cd9d8d8fc | -2.74687 | -45.97929 | 2024-11-23 03:53:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9367c43-52ae-364b-be62-5e90fd2e7d0e | -2.18886 | -45.67983 | 2024-11-23 03:53:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61869759-a036-31eb-9354-ccdc3e47c37e | -2.93218 | -48.05558 | 2024-11-23 03:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a34ffd24-ed46-35e2-86c4-468935ed37ab | -2.70619 | -46.09681 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 539bcf3e-46b3-3b0f-a910-0108c22ca4c6 | -2.00762 | -48.10369 | 2024-11-23 03:53:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 890c7150-1d54-32d6-af73-a534618d3d11 | -3.95056 | -41.49396 | 2024-11-23 03:53:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f2cd49d0-c829-3908-bbd6-a1f1bca700dc | -3.84886 | -43.93525 | 2024-11-23 03:53:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7cc57bf9-e65c-3615-9c43-c1b9af0750d2 | -4.11224 | -42.47546 | 2024-11-23 03:53:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| ec6e4fa9-600d-301f-8751-81f55cc65f4c | -3.88479 | -43.15659 | 2024-11-23 03:53:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 107ad09b-763c-3ef3-986a-498bdd0568b4 | -3.16759 | -44.40522 | 2024-11-23 03:53:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bec21b6c-e708-3e15-9fda-fb2092ec0567 | -2.70034 | -46.26281 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c982a86-cd74-380c-a623-5e3596518781 | -2.80161 | -48.68324 | 2024-11-23 03:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 469d2c6d-9b83-3fa5-b83b-6951840a197b | -2.68892 | -46.16858 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23bb7c9b-197f-3764-a7c9-9bb73fc98aa3 | -2.18328 | -45.68196 | 2024-11-23 03:53:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd2909bb-db64-397f-adfa-2e4d67733714 | -4.39074 | -40.76415 | 2024-11-23 03:53:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 87152455-377b-3911-8ca9-19996f8da17e | -5.56724 | -50.94958 | 2024-11-23 03:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0f30a3e-ba31-3dc2-86ce-68044001247d | -3.85562 | -39.33682 | 2024-11-23 03:53:00 | NPP-375D | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a65f856b-2413-32b3-87c2-136016c58eed | -3.26981 | -45.44201 | 2024-11-23 03:53:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62092446-8aee-3dc8-9a04-2cceb959416b | -6.15237 | -46.67756 | 2024-11-23 03:53:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4547c4a-043c-3394-924f-8a93d800bc4a | -6.14675 | -46.67955 | 2024-11-23 03:53:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a064b481-5b75-3f10-b327-2bdf1ab6949f | -10.07198 | -36.49 | 2024-11-23 03:53:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 15b2eb8d-387f-34ef-8bfb-d111c03e032e | -2.69599 | -45.66555 | 2024-11-23 03:53:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4b90403-70c2-304d-94d0-c931d7ebfd1c | -7.635 | -39.82253 | 2024-11-23 03:53:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 613864e0-9b51-3f47-87e0-26816a65afb8 | -4.10667 | -42.47268 | 2024-11-23 03:53:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| c50dccbc-2a3e-36be-91ca-fc4c40fa4147 | -2.70984 | -46.27092 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bb2eea7-c423-3562-9c26-e6ad187a5953 | -3.146 | -44.48603 | 2024-11-23 03:53:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8a8eeb57-f4da-382c-83de-6410699b42f6 | -7.05022 | -40.41681 | 2024-11-23 03:53:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bf5c4f5f-b9f3-3cfb-a8e2-06fab50b5422 | -3.26487 | -45.44119 | 2024-11-23 03:53:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6142e6b2-9c9b-323c-a903-66cf563d3445 | -7.07145 | -49.20817 | 2024-11-23 03:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0c195c9-611d-3345-910b-d969519dfa12 | -7.64152 | -40.38696 | 2024-11-23 03:53:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| eb2fa489-edc9-324f-901b-21910bdada2e | -3.23051 | -46.42942 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b966733-86d4-3785-9ebd-67b676ee1e06 | -2.70931 | -46.27414 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a49961b6-a6f1-380f-b20f-63e747383651 | -2.94329 | -48.06184 | 2024-11-23 03:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea3be8be-0fd3-3f62-bdfa-39b8ca71d09d | -3.6052 | -41.67506 | 2024-11-23 03:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 281392a6-6233-3cda-9ec7-1a579d9e2498 | -3.60723 | -41.67859 | 2024-11-23 03:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| de3567a1-d9b0-3bdf-bad7-dcddab8e66e1 | -2.68634 | -45.66102 | 2024-11-23 03:53:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ef2504b-265a-36e6-8c3e-b3ee0748c321 | -3.40662 | -46.24218 | 2024-11-23 03:53:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70979e39-9904-35c6-a653-e33441a334a5 | -2.12999 | -46.40596 | 2024-11-23 03:53:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de6c0fb1-eec4-34df-b63d-1803c489bdff | -9.72693 | -37.02801 | 2024-11-23 03:53:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4988c1d0-60bf-3045-8ecc-8938f8dead80 | -4.11065 | -42.47334 | 2024-11-23 03:53:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| d01f7a40-87d3-3773-927c-7f5ae437632e | -8.31868 | -35.23669 | 2024-11-23 03:53:00 | NPP-375D | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9da3e94b-5962-30de-b73c-1e6904a52406 | -3.34409 | -45.17114 | 2024-11-23 03:53:00 | NPP-375D | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 689248ee-9e12-39fe-9661-9b3118fc4c89 | -2.64594 | -45.1609 | 2024-11-23 03:53:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ffa98ea3-d11f-32d3-b896-f960d577f54e | -3.63258 | -44.34378 | 2024-11-23 03:53:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f400d5e-bf63-3985-82db-9cc040ca21bb | -2.82778 | -45.1644 | 2024-11-23 03:53:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README22.md)
