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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e67d6bd3-25a2-305f-bdbd-420b762d72d4 | -6.9602 | -42.9052 | 2025-06-04 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.3 |
| ba34f80b-136a-3fd3-aaa3-2238886829a8 | -4.8033 | -45.2594 | 2025-06-04 00:00:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 7ffb3c6f-27b9-3f88-813b-925b36f27737 | -7.2211 | -43.1388 | 2025-06-04 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.0 |
| c38b1a7d-0605-3e65-afad-10d7fc609b43 | -11.5617 | -56.4221 | 2025-06-04 00:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 66265fe9-b4e4-37e2-920d-f1fa403cc77a | -11.8365 | -51.2854 | 2025-06-04 00:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| c20061e9-e1d9-3ea1-aaf7-643729fd3166 | -10.6056 | -44.7696 | 2025-06-04 00:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 29ffb12c-2f5f-302e-9393-c976af1b0fe5 | -10.6247 | -44.767 | 2025-06-04 00:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| a057c68a-bc63-3098-a0de-96606f339bbf | -7.0169 | -44.5954 | 2025-06-04 00:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 93351fe8-8c73-3c22-9e52-6dd7ab3c8ec6 | -6.96331 | -42.89384 | 2025-06-04 00:01:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 27.1 |
| aabee003-e6b3-39b5-85f4-a8e4def31862 | -7.00739 | -44.61754 | 2025-06-04 00:01:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 311d9ef6-8df2-31a3-9686-04480092083e | -6.96251 | -42.90028 | 2025-06-04 00:01:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.5 |
| 832d8d36-dea1-3ceb-9f3f-8b27bad71bf7 | -5.23224 | -37.66255 | 2025-06-04 00:01:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1cf49ead-7c89-3cc1-9b3d-373a292a122d | -7.01529 | -44.57691 | 2025-06-04 00:01:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 271c295b-9cb6-3213-bb65-d56ccfc6da10 | -7.00506 | -44.60465 | 2025-06-04 00:01:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| bb10302f-cb12-382f-9d30-11b44af2f651 | -4.57081 | -43.20485 | 2025-06-04 00:01:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 943e5a04-ac05-3c4c-a5d9-22fbe5a7c900 | -6.96512 | -42.90817 | 2025-06-04 00:01:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 152.8 |
| 6c371e7c-a134-312e-a444-ddba7751e4ea | -4.00327 | -43.24747 | 2025-06-04 00:01:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 8c3440cd-dbed-3284-83e6-36aac7b41ea8 | -6.24331 | -43.35949 | 2025-06-04 00:01:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 380bfcb5-d727-35dd-b215-4c70fecae6b9 | -7.14314 | -44.03715 | 2025-06-04 00:01:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 6b858f6d-d2de-3208-92bf-bd955cc526de | -7.01519 | -44.58329 | 2025-06-04 00:01:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 05863f28-e0db-334c-9507-487bfada1075 | -3.13175 | -41.79128 | 2025-06-04 00:01:00 | TERRA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 71ca4c6b-b6ae-325f-9c52-697b1b64c1e8 | -6.96443 | -42.91462 | 2025-06-04 00:01:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| 371576e8-1f58-334a-9421-cd8b711a0f59 | -7.01773 | -44.60249 | 2025-06-04 00:01:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 68e990f8-87ba-3dca-a412-b7fc06283322 | -6.97554 | -42.91328 | 2025-06-04 00:01:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 58c56886-da9b-3493-ab67-624b4dc8d2cd | -4.80448 | -45.26487 | 2025-06-04 00:01:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 1d8da752-51ec-3ea0-ad29-27a643110870 | -4.81742 | -45.26296 | 2025-06-04 00:01:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 4f3d1478-b0ed-3068-9327-7a2c64a253c5 | -6.9736 | -42.89884 | 2025-06-04 00:01:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 04471161-315e-35c0-8704-83e00765a76d | -7.01767 | -44.59599 | 2025-06-04 00:01:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| e0dd0224-b87a-3904-8d0e-01967d140624 | -4.81573 | -45.25783 | 2025-06-04 00:01:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 98f54de0-95ea-3a6e-9c5f-7a01b74bd9ff | -6.24528 | -43.37458 | 2025-06-04 00:01:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 9d161477-6846-3bf3-bbb6-4edc24b18321 | -7.0076 | -44.62397 | 2025-06-04 00:01:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5663b6c7-1447-3899-80b6-0236f82d8438 | -7.00501 | -44.59834 | 2025-06-04 00:01:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c5ae0372-b8d9-3de1-99f9-8be986f87547 | -6.96695 | -42.92263 | 2025-06-04 00:01:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 41.2 |
| 55ec4990-7e8d-37de-829f-ddf3de7f2f31 | -4.81839 | -45.27853 | 2025-06-04 00:01:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 862608aa-011d-3fe9-819f-6d2c230b41bb | -4.80277 | -45.2597 | 2025-06-04 00:01:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| ccc580c3-a7bb-3074-b3ed-8a319126aa24 | -6.9602 | -42.9052 | 2025-06-04 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.3 |
| 726f449e-c984-3593-8f16-c85ef6c406af | -11.8365 | -51.2854 | 2025-06-04 00:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| d5834887-25b7-3fc8-b81c-3e14b26b1566 | -7.0169 | -44.5954 | 2025-06-04 00:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| ef0f8b02-9343-3b71-8642-2da8610ca8f9 | -10.6056 | -44.7696 | 2025-06-04 00:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| f107e6ea-4dab-3da2-b116-f2502d8d89d6 | -6.9791 | -42.9034 | 2025-06-04 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| 7b975648-7acf-3f8a-801f-b7ab7ac9858e | -8.7606 | -49.7643 | 2025-06-04 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 65a02db1-82f7-36c9-8097-01a4f658bce4 | -11.5617 | -56.4221 | 2025-06-04 00:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 5cc041ca-761f-37f8-9052-b12a93065d67 | -7.2081 | -43.1343 | 2025-06-04 00:11:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a895e091-586b-31e1-82cd-9aaf56ae411f | -4.2545 | -47.572601 | 2025-06-04 00:11:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7bedd5b-7026-3025-ae19-72d2d6e82a13 | -7.0248 | -44.578899 | 2025-06-04 00:11:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9eb65eb-886e-3f89-b5ec-6791de3a9e3d | -14.7209 | -45.104099 | 2025-06-04 00:11:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3cc35cc7-fdae-30dc-bbb3-3b99469cadd8 | -7.8961 | -46.183498 | 2025-06-04 00:11:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ee593e4-c85d-35f7-ab8e-fe8bb75e4c9a | -7.0171 | -44.590199 | 2025-06-04 00:11:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba553aee-66ce-3360-9dd0-afa60d694ab2 | -8.0763 | -43.1106 | 2025-06-04 00:11:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5e023d6e-d558-3d39-9023-794632dea5e9 | -6.2511 | -43.361 | 2025-06-04 00:11:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc0c0dd1-f1e1-304d-9606-7f4ea57f89c4 | -3.1442 | -41.7859 | 2025-06-04 00:11:00 | METOP-C | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ad95cfdc-4ab1-3a39-bb12-8f15034629e2 | -8.0878 | -43.116501 | 2025-06-04 00:11:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d22f7271-94e1-37ac-924b-6688f660f9c2 | -8.0781 | -43.118599 | 2025-06-04 00:11:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 303e7568-b24c-3e42-ad4f-1e4f0f4b7812 | -7.0191 | -44.599499 | 2025-06-04 00:11:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d59fcee0-0243-3888-9542-702f02179c6c | -10.6265 | -44.760201 | 2025-06-04 00:11:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4a4cb1aa-d90d-3c46-a7d7-64393ede67d3 | -3.1344 | -41.788101 | 2025-06-04 00:11:00 | METOP-C | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dd411bb5-4e20-3645-a2fb-4992e6712a83 | -14.7183 | -45.091202 | 2025-06-04 00:11:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c2e0dbd1-735d-3773-8c81-28e44d62c9ba | -4.569 | -43.201199 | 2025-06-04 00:11:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0915b6d-ca85-31fc-bad3-0d9bcf8f7cf1 | -7.015 | -44.581001 | 2025-06-04 00:11:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9f4ac16-39fa-39fa-8c62-1640fef23578 | -4.0113 | -43.238602 | 2025-06-04 00:11:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d07f8292-c87d-3bd4-8867-f32c9a084fd3 | -11.637 | -41.8335 | 2025-06-04 00:11:00 | METOP-C | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8f1306b6-f8ec-3cb6-ac3e-2f990becd87b | -6.971 | -42.9016 | 2025-06-04 00:11:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d5b49956-31aa-37b9-8f7e-d48ac7efb694 | -6.2955 | -47.000702 | 2025-06-04 00:11:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e6e4f2bb-d5be-394f-adda-fc9bd4b4c738 | -10.6145 | -44.751499 | 2025-06-04 00:11:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ee6a54a3-e7c8-3da7-996f-c82d8c436ef2 | -6.605 | -43.887402 | 2025-06-04 00:11:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1dc34938-1ee9-3a17-acb8-9482885b8be3 | -4.8166 | -45.263401 | 2025-06-04 00:11:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73cd1631-3029-30c5-9d6e-1b2fc0a3c4cd | -7.2197 | -43.140099 | 2025-06-04 00:11:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1b303e78-62b4-3c76-920d-ceeb83577d68 | -6.2129 | -43.328098 | 2025-06-04 00:11:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c915f22c-40f9-34c9-b37d-a80398c270cd | -10.0594 | -44.640202 | 2025-06-04 00:11:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2da3ffd8-4769-37a2-8a63-b270973135f0 | -7.0113 | -44.610901 | 2025-06-04 00:11:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2893304-2648-3c78-bafa-2a7eacd64ce0 | -6.9693 | -42.893902 | 2025-06-04 00:11:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1d7aaafe-bbd5-381c-a035-f9b614bd1b11 | -10.6167 | -44.762199 | 2025-06-04 00:11:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 71056be2-922a-32b5-9ca8-9067d0ddf848 | -14.7281 | -45.089199 | 2025-06-04 00:11:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 07ad6845-678a-3b71-b65e-3c09b6d2d7ed | -6.2529 | -43.368801 | 2025-06-04 00:11:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef5a35af-ed10-31a8-aed4-4d651d2df7e8 | -7.0093 | -44.601601 | 2025-06-04 00:11:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b6444dc-3ced-350a-8f49-eab4f378a1cd | -7.2277 | -43.130001 | 2025-06-04 00:11:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cc3e37e9-2cf4-333f-bafb-c0253a1658c2 | -7.2179 | -43.132198 | 2025-06-04 00:11:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d179cd99-3418-3830-b78b-a0c4f6d918aa | -6.2147 | -43.335999 | 2025-06-04 00:11:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0376e547-c190-3b9c-8ca3-315e49bba235 | -6.9728 | -42.909302 | 2025-06-04 00:11:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ed1f9596-3ab9-363e-bca7-6d4f18123f02 | -6.963 | -42.911499 | 2025-06-04 00:11:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4c6681ea-db72-3927-bd94-df08a7d242b0 | -10.679 | -44.380798 | 2025-06-04 00:11:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 923e3e92-4e9f-3fab-a967-81980f059bfd | -7.2099 | -43.1422 | 2025-06-04 00:11:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fbca35d2-6a72-308d-9828-da260f209d3b | -8.0861 | -43.108501 | 2025-06-04 00:11:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c09189fe-58aa-3f62-bbd3-c87c9675b357 | -7.2242 | -43.1143 | 2025-06-04 00:11:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9aeb93b1-5f9a-3dc8-8d46-7a06dede6df6 | -6.7769 | -43.229 | 2025-06-04 00:11:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 10343502-c441-3f52-a49c-664d49b3f4d2 | -10.6615 | -44.490799 | 2025-06-04 00:11:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a49aa847-6a40-3b54-b7d4-9681580ffffe | -7.5914 | -45.8605 | 2025-06-04 00:11:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2231c7e3-c5de-3255-9be0-e16fcc3ee496 | -10.5565 | -42.433498 | 2025-06-04 00:11:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4f014f06-3918-33d1-8c64-f3de6eefa129 | -10.6988 | -44.811798 | 2025-06-04 00:11:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| feebcd60-9984-3ae9-835a-3da4d99c54d3 | -6.9745 | -42.916901 | 2025-06-04 00:11:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9acbfce3-124a-3ddc-9a43-c8e4ba6e9ee5 | -7.2988 | -43.4501 | 2025-06-04 00:11:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 706f82b5-83f5-3351-828d-17a64f9afd32 | -7.2357 | -43.120098 | 2025-06-04 00:11:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3d0aaebb-94da-3b7b-a489-f7d219a4947c | -7.5889 | -45.8493 | 2025-06-04 00:11:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 10944b5c-cf45-3ac0-9262-d565f9b492a7 | -7.1514 | -44.0364 | 2025-06-04 00:11:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5081e753-61bb-33ba-bbc4-1b21dcda69a0 | -10.619 | -44.7728 | 2025-06-04 00:11:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 13b7d2dd-ab0c-3e37-b3fd-ea3cd11982e2 | -4.013 | -43.246101 | 2025-06-04 00:11:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1baf8e02-4f79-328f-8e88-ce0deee2f999 | -7.2161 | -43.124401 | 2025-06-04 00:11:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9cd54db7-8234-3081-83bc-f4e0a7632993 | -7.1533 | -44.044998 | 2025-06-04 00:11:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 53b7b34a-33bd-3355-85ee-ea8e1240277c | -11.8327 | -51.2528 | 2025-06-04 00:11:00 | METOP-C | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 48fe9bf9-c273-357d-bfb0-b6a432e3159b | -7.2259 | -43.1222 | 2025-06-04 00:11:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README2.md)
