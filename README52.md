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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9359e91-ae14-319a-88cd-25392c9ffd21 | -3.0534 | -45.2764 | 2024-11-13 06:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 0f5c2409-371f-3c9d-b59d-c6c51f1ef0b5 | -4.658 | -47.4434 | 2024-11-13 06:10:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 596fdc99-93e1-3cd2-b807-3cf3b3be461b | -3.8692 | -49.1202 | 2024-11-13 06:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 82b71488-2148-3988-8bdb-a2183cd39368 | -4.6767 | -47.4206 | 2024-11-13 06:10:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 39955b92-548a-3b9f-be6f-21a4f96c9967 | -3.0535 | -45.2539 | 2024-11-13 06:10:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 68.2 |
| a0ba54b8-f6ce-372a-b501-0f1f6f8adda0 | -3.9483 | -48.1724 | 2024-11-13 06:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| d185c780-b2da-3b88-bf66-ba88d05b44b6 | -3.0504 | -50.3332 | 2024-11-13 06:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| f2551816-b5b6-36f3-939c-61a8827b4688 | -3.0689 | -50.3326 | 2024-11-13 06:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 2221a4b3-8df0-3a10-a6ee-6641b08428ba | -3.0721 | -45.2532 | 2024-11-13 06:20:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 2dda9c8d-acf4-3002-9240-371859453147 | -3.0535 | -45.2539 | 2024-11-13 06:20:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| c5b0c2bb-f6fe-3944-9a45-1b96094573a8 | -3.9483 | -48.1724 | 2024-11-13 06:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 3ecd862b-96aa-35ce-8088-6ebb5bb5af4b | -3.0504 | -50.3332 | 2024-11-13 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| d75d044b-a807-3e8f-9c50-279b90d20621 | -3.0534 | -45.2764 | 2024-11-13 06:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 9eb9cdcf-6328-30e6-93d9-bce2118da7bf | -3.9483 | -48.1724 | 2024-11-13 06:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 8046c898-ad96-32b0-9ebf-57c48934bf15 | -3.0534 | -45.2764 | 2024-11-13 06:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 51868639-36e9-3434-bf5e-9514e53409ce | -3.0535 | -45.2539 | 2024-11-13 06:30:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 63.2 |
| aea74fff-747c-3ae5-8c6b-e0361e3d1d0e | -2.25163 | -53.73825 | 2024-11-13 06:33:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 9297744d-d0a8-37a8-8b65-d7f4ad4b9b2c | 1.06091 | -60.60258 | 2024-11-13 06:33:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 30.2 |
| bbca39de-d911-30bd-8995-a91d57ea0869 | -2.24733 | -53.73022 | 2024-11-13 06:33:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 4f585112-2249-35c6-85a4-e972ba14cf3a | 1.05009 | -60.59404 | 2024-11-13 06:33:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 20.7 |
| a62b8671-75d4-3a4b-962b-fc35ed622963 | 1.05156 | -60.60393 | 2024-11-13 06:33:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d167d655-5812-39e4-8a1f-93eb03cb1c2c | 1.05944 | -60.59269 | 2024-11-13 06:33:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 18.5 |
| c75ea942-d4a8-3134-b2aa-0de7a18ba8b3 | -3.0721 | -45.2532 | 2024-11-13 06:40:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 45495c15-7790-33ae-b58e-7ab4fce99dbb | -3.072 | -45.2757 | 2024-11-13 06:40:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 61.9 |
| f0679c24-1165-38ae-9133-f97a99c7cac9 | -3.0721 | -45.2532 | 2024-11-13 07:00:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 58.8 |
| e1a0b3c4-9030-3f42-9752-f669bee98f14 | -3.072 | -45.2757 | 2024-11-13 07:00:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 13ae36d0-160b-35ad-942a-93020d2626cb | -2.9052 | -45.1692 | 2024-11-13 07:10:00 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 1f113b48-d990-30ab-aeb4-ea6158211fd8 | -2.9238 | -45.1685 | 2024-11-13 07:10:00 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 0faa570f-374f-31a7-b90b-abb5558531bf | -3.0534 | -45.2764 | 2024-11-13 07:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 5593dd83-2f13-31a9-84f0-ef7a25b6f1b7 | -2.9238 | -45.1685 | 2024-11-13 07:20:00 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 147.2 |
| 33b21544-3d3e-3180-9cdc-be2471ebe439 | -2.9238 | -45.1685 | 2024-11-13 07:30:00 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 24d0f858-734b-33ec-a3e8-6c2a91cff1d5 | -2.9238 | -45.1685 | 2024-11-13 07:40:00 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| a73ab758-e67d-3e68-bc66-8e833451f7cc | -3.2495 | -43.2547 | 2024-11-13 11:10:00 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 93f1eb20-4d4a-3287-aa0b-0f500e37b476 | -4.2078 | -42.3141 | 2024-11-13 11:30:00 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 118.0 |
| 93ab00fb-26b4-3bce-b3e3-b45cdeecadbc | -4.2077 | -42.3378 | 2024-11-13 11:30:00 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 155.7 |
| 78293da2-dd4f-3ca8-8f5f-478b64a35e15 | -3.2495 | -43.2547 | 2024-11-13 11:30:00 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 1119f0cd-76af-34d4-8418-3e55968e90a5 | -4.2077 | -42.3378 | 2024-11-13 11:40:00 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 108.5 |
| d71b4c51-5cdf-3213-a51c-cdf39e0f3c3a | -4.2077 | -42.3378 | 2024-11-13 11:50:00 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 120.7 |
| dae176d9-0fa3-3a6c-95f0-29f75225a498 | -4.2077 | -42.3378 | 2024-11-13 12:10:00 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 29c9b5d1-308a-398c-a763-ac9443a28c89 | -4.2077 | -42.3378 | 2024-11-13 12:20:00 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 1d7312f6-8693-3b11-9152-ecb8bf59e882 | -3.57701 | -42.08938 | 2024-11-13 12:25:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 4121fcfb-430d-343c-9c13-ca264ba602d7 | -3.42914 | -41.44686 | 2024-11-13 12:25:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| c2ea0e56-b393-3aa8-b652-393ea48df42b | -4.20617 | -42.32865 | 2024-11-13 12:25:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 325274f9-275b-30e8-8be9-b65e15561491 | -4.2049 | -42.33744 | 2024-11-13 12:25:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 31.5 |
| 5c9f5200-8bd8-3f43-81cc-b09962dad40f | -7.64137 | -37.70346 | 2024-11-13 12:25:00 | TERRA_M-T | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 41.4 |
| b2533342-7641-3f4f-8bfc-d8e5abcb9c5b | -3.37186 | -41.5928 | 2024-11-13 12:25:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 62db103d-b73b-3c2b-b51f-0dec438d3da6 | -3.49113 | -42.10719 | 2024-11-13 12:25:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| a826b8fc-9ded-316f-9921-ce59f4ccdf83 | -4.34581 | -43.78141 | 2024-11-13 12:25:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 067a1c0e-db8a-3bc9-b111-17b9c22c778e | -6.45765 | -44.29162 | 2024-11-13 12:25:00 | TERRA_M-T | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 963173de-cf0b-3d63-92bf-71060033d2f5 | -3.07573 | -42.42751 | 2024-11-13 12:25:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 1a141920-6be3-3ee5-8d1e-e8f701bda510 | -7.74542 | -37.94135 | 2024-11-13 12:25:00 | TERRA_M-T | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 4bbec6db-92a9-3881-b3ca-d22f097f3c07 | -6.70104 | -38.7208 | 2024-11-13 12:25:00 | TERRA_M-T | BAIXIO | CEARÁ | Brasil | 2301802 | 23 | 33 | nan | nan | nan | Caatinga | 15.1 |
| f04e5a39-5d72-3277-83c2-11a1b2e54a09 | -4.34941 | -43.82011 | 2024-11-13 12:25:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 963212f7-edc2-372d-a816-adacb1f47d95 | -3.06689 | -42.42628 | 2024-11-13 12:25:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 559ef130-8b3d-3963-a97a-9e5b2b59da02 | -3.4924 | -42.0984 | 2024-11-13 12:25:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 33.4 |
| 467d17c2-45fe-3eb7-a84d-99edd98cf897 | -4.38632 | -43.12106 | 2024-11-13 12:25:00 | TERRA_M-T | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2e76a770-2193-3a0f-bfbe-73411486986b | -7.34482 | -38.54764 | 2024-11-13 12:25:00 | TERRA_M-T | CONCEIÇÃO | PARAÍBA | Brasil | 2504405 | 25 | 33 | nan | nan | nan | Caatinga | 35.3 |
| 19ecae7e-7a6d-33fe-8c7d-d7da7f923d28 | -3.37886 | -42.18359 | 2024-11-13 12:25:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 21.2 |
| 88cba674-468f-35f8-8bf4-259c1f52c031 | -6.46642 | -36.23793 | 2024-11-13 12:25:00 | TERRA_M-T | PICUÍ | PARAÍBA | Brasil | 2511400 | 25 | 33 | nan | nan | nan | Caatinga | 28.5 |
| 57b4b735-5b7b-3b94-ba96-6d797c7328e3 | -3.24963 | -43.26324 | 2024-11-13 12:25:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d5ad658a-253a-3642-88f9-4aad6a91996c | -3.57574 | -42.09817 | 2024-11-13 12:25:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 51.0 |
| 4a05787a-455d-358b-94d0-32f0bbfad5ae | -7.63675 | -37.70895 | 2024-11-13 12:25:00 | TERRA_M-T | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 42.1 |
| b815be9e-3488-3e88-9c09-f4dc142029da | -7.40154 | -38.53961 | 2024-11-13 12:25:00 | TERRA_M-T | CONCEIÇÃO | PARAÍBA | Brasil | 2504405 | 25 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 63da49d6-c616-3ceb-8df0-c6bb90dd6f75 | -7.81572 | -37.77016 | 2024-11-13 12:25:00 | TERRA_M-T | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 48.5 |
| b4425a00-52a8-3122-822b-c5b85856cc4a | -5.95753 | -43.23808 | 2024-11-13 12:25:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.5 |
| b05769a0-a6fc-321d-b65d-291310d73f81 | -4.87189 | -38.38484 | 2024-11-13 12:25:00 | TERRA_M-T | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 0d344e58-d507-3d91-aef6-1c2d186989a2 | -4.85074 | -44.48243 | 2024-11-13 12:25:00 | TERRA_M-T | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| efa5fce4-5df6-3b03-b0e6-14004dcb7fe0 | -3.46682 | -42.97484 | 2024-11-13 12:25:00 | TERRA_M-T | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f0080cda-e198-3812-88dd-7fd376f1e12d | -6.23486 | -41.89043 | 2024-11-13 12:25:00 | TERRA_M-T | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| e70d9dd0-8d01-3665-8085-9af4e6b78f7b | -6.94292 | -42.80806 | 2024-11-13 12:25:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 46316538-16c8-3948-8cb7-15fe9b31d58a | -4.07166 | -44.13592 | 2024-11-13 12:25:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 08ebe61c-03f3-3769-945f-9745ac270d20 | -4.65387 | -44.75836 | 2024-11-13 12:25:00 | TERRA_M-T | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| cdb88e35-0338-3f3a-b927-9421ed2a9569 | -3.29673 | -43.51067 | 2024-11-13 12:25:00 | TERRA_M-T | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0ea94217-3dbc-3ef5-bf9e-54b23306f741 | -3.55735 | -41.58592 | 2024-11-13 12:25:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 0c1cf301-e8b7-3a34-a02e-dfa8a2382d2f | -3.71955 | -42.76595 | 2024-11-13 12:25:00 | TERRA_M-T | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| c3395292-e099-31d6-bb8a-42294b70f72f | -4.44935 | -44.63366 | 2024-11-13 12:25:00 | TERRA_M-T | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e06d0116-7b1c-3f46-8e65-aef178420eef | -3.16433 | -43.53281 | 2024-11-13 12:25:00 | TERRA_M-T | BELÁGUA | MARANHÃO | Brasil | 2101731 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| bdeb6373-8b7a-3fea-be3d-9175a587d1af | -8.13272 | -35.04448 | 2024-11-13 12:25:00 | TERRA_M-T | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 53.8 |
| 4e33c6c3-ce59-3b83-aa31-2162d72a539f | -3.31064 | -42.20378 | 2024-11-13 12:25:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 66.6 |
| db8a39d7-069c-374e-ab7b-2afeff20186d | -3.68511 | -42.43065 | 2024-11-13 12:25:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| 94196b58-5026-3d89-a611-959e60ff9359 | -4.56093 | -44.26637 | 2024-11-13 12:25:00 | TERRA_M-T | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 4376fff8-e341-3227-abfa-16423ab1e001 | -3.68793 | -44.85364 | 2024-11-13 12:25:00 | TERRA_M-T | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 94747293-9c9c-3f28-bb4e-10df771242cd | -3.2898 | -43.11813 | 2024-11-13 12:25:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 47778f04-1425-377b-827b-4354bd8b9eb4 | -5.45821 | -43.23852 | 2024-11-13 12:25:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 4b29d72b-0f55-3c23-b9d5-8e75bc53bf02 | -5.32028 | -42.97986 | 2024-11-13 12:25:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 15.7 |
| ce9b4b8c-e330-32a2-bc96-64ca0a717933 | -7.34091 | -38.55533 | 2024-11-13 12:25:00 | TERRA_M-T | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 0ea5435a-76e4-3f7d-aef3-ea6b7ad7f388 | -4.34033 | -43.81881 | 2024-11-13 12:25:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 8fd95182-3cb7-3c57-a518-32d4367eb093 | -5.01081 | -44.0891 | 2024-11-13 12:25:00 | TERRA_M-T | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| b1412c4b-2a92-36cb-955e-779a9c60090b | -8.13374 | -35.05012 | 2024-11-13 12:25:00 | TERRA_M-T | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 43.2 |
| 7a08f043-1769-3644-9748-994ce4537215 | -3.42786 | -41.45575 | 2024-11-13 12:25:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 410505ed-a52e-32e9-8485-6025fa6cba08 | -6.6109 | -38.19059 | 2024-11-13 12:25:00 | TERRA_M-T | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 13.8 |
| d74640ac-1aa8-3af4-9119-3997728bc248 | -5.56582 | -44.20628 | 2024-11-13 12:25:00 | TERRA_M-T | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ce9f1c15-d64a-3055-923b-3b20af3fdaab | -3.4151 | -42.38333 | 2024-11-13 12:25:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 8.5 |
| c15e0627-33fd-3bf2-a193-dd0ee8cecab3 | -8.2022 | -44.47203 | 2024-11-13 12:25:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 880c4f4a-ba34-39ba-8660-8204a1b774bd | -7.34279 | -38.54166 | 2024-11-13 12:25:00 | TERRA_M-T | CONCEIÇÃO | PARAÍBA | Brasil | 2504405 | 25 | 33 | nan | nan | nan | Caatinga | 15.8 |
| b22d4c07-175a-303d-b68f-00912c04e14e | -3.31191 | -42.19501 | 2024-11-13 12:25:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 7.0 |
| e65c7ac1-76ad-3acc-b023-9f9a917c5129 | -4.88016 | -42.071 | 2024-11-13 12:25:00 | TERRA_M-T | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 6be60fa5-045e-36ed-a4cc-fb4def61138d | -4.66385 | -43.81371 | 2024-11-13 12:25:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e894e207-9901-3647-9bab-6d5b3fc85ad1 | -5.4679 | -43.93147 | 2024-11-13 12:25:00 | TERRA_M-T | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 79458fa8-9bc0-352b-bdb2-3847fba3e730 | -6.70285 | -38.70735 | 2024-11-13 12:25:00 | TERRA_M-T | BAIXIO | CEARÁ | Brasil | 2301802 | 23 | 33 | nan | nan | nan | Caatinga | 46.8 |


[Clique aqui para ver as próximas entradas](README53.md)
