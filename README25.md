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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1adecfb-166f-36a2-80fa-507787ba6069 | -5.5716 | -44.8927 | 2024-10-22 04:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 43.4 |
| a1973dba-3463-3aab-a2e9-f76378e16554 | -5.5718 | -44.87 | 2024-10-22 04:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 55212eed-a189-3732-aaac-5c448ed95fba | -5.5903 | -44.8914 | 2024-10-22 04:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| ba8fae0f-04de-3571-b626-2ef09f6b6045 | -5.5905 | -44.8687 | 2024-10-22 04:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 1636ce86-a510-3ce3-a262-34459ff6cd31 | -10.1226 | -36.3067 | 2024-10-22 04:26:02 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 72.0 |
| 6c983130-bd88-3fba-abec-14fa83169f8d | -19.5473 | -56.6563 | 2024-10-22 04:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 93.1 |
| 728e72dd-8183-373d-8e9b-510b7b965244 | -19.5469 | -56.6773 | 2024-10-22 04:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 53.8 |
| 4c99ff54-a700-369f-a372-bcfd9e9b9421 | -2.7773 | -49.3067 | 2024-10-22 04:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 910ee2de-3130-30fd-9408-ae7b1598a64e | -2.7773 | -49.3279 | 2024-10-22 04:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 3f9bc444-5f19-30a4-b9e1-90dca133d6f9 | -2.7589 | -49.3072 | 2024-10-22 04:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 143.3 |
| 99fa04a0-6581-3fc5-93af-a60c7c72a220 | -2.7588 | -49.3285 | 2024-10-22 04:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 139.4 |
| fc24773b-2544-3e01-bf59-4558f590919a | -5.5905 | -44.8687 | 2024-10-22 04:35:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| ea6b1288-cfee-37aa-bd8f-9564a44fd75b | -5.5903 | -44.8914 | 2024-10-22 04:35:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| a064ec07-6fcf-3b5d-98dc-5014f074271c | -5.5718 | -44.87 | 2024-10-22 04:35:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 843897f5-1253-3190-8f3a-56364d6558db | -2.7773 | -49.3067 | 2024-10-22 04:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 5eee3a83-fcd7-3c71-82b7-471127e1cda4 | -2.7773 | -49.3279 | 2024-10-22 04:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 66cb8191-f767-3884-985e-964773a560ca | -2.7589 | -49.286 | 2024-10-22 04:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| e9938192-d4e2-3132-8709-32b466f0263f | -2.7589 | -49.3072 | 2024-10-22 04:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 216.3 |
| 0c54aa5e-b9ff-3bec-a76a-27af9bc7c6e1 | -2.7588 | -49.3285 | 2024-10-22 04:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 152.7 |
| 790fce5b-a46d-3b01-8f88-6e6f72d5c728 | -5.5905 | -44.8687 | 2024-10-22 04:45:36 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| cb950ab5-8dae-3af1-a3ce-0f6fcf9d565a | -5.5903 | -44.8914 | 2024-10-22 04:45:36 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 9ae98994-7507-305f-813b-7b84db33c5e0 | -5.5718 | -44.87 | 2024-10-22 04:45:36 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 7d0c79b7-593c-364e-9c5b-0595dcf0e547 | -17.0184 | -57.5178 | 2024-10-22 04:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.4 |
| e2da5258-7ac0-3125-b2ee-36925b6183a2 | -17.6868 | -57.4593 | 2024-10-22 04:46:44 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.8 |
| 5944463a-f15a-375e-b465-9418aa6e68e3 | -2.7773 | -49.3067 | 2024-10-22 04:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 2e8bacdf-ff76-37de-a7a4-d1b9144e777c | -2.7773 | -49.3279 | 2024-10-22 04:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 9ea58899-eab7-34d7-aa86-3841e5345f11 | -2.7589 | -49.3072 | 2024-10-22 04:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 178.7 |
| 4ce26cf1-7c14-3311-a5ef-9a3abf2456b5 | -2.7588 | -49.3285 | 2024-10-22 04:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 37188acd-7f89-373f-aef6-da4393cd1113 | -2.7404 | -49.3077 | 2024-10-22 04:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| dc6d6eb4-9cd9-3e08-819c-a70600d4111a | -5.5905 | -44.8687 | 2024-10-22 04:55:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 337a804c-38a4-3106-a9fb-79f9b198d296 | -5.5718 | -44.87 | 2024-10-22 04:55:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| ec8aa495-603e-3291-8960-ff95d9aed139 | -6.2336 | -44.1335 | 2024-10-22 04:55:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| c285783d-997a-37c5-af00-6a37b4c93379 | -4.844 | -42.8615 | 2024-10-22 05:01:00 | AQUA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 2fe68ce3-f513-3298-b205-ae170a1c0367 | -5.24131 | -35.5451 | 2024-10-22 05:01:00 | AQUA_M-M | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 20.0 |
| aa4fb707-b487-3823-a31f-3192417eaaa3 | -5.23712 | -35.53914 | 2024-10-22 05:01:00 | AQUA_M-M | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 5976871e-d030-3cd7-ab8f-6af9e04a1859 | -5.23455 | -35.55693 | 2024-10-22 05:01:00 | AQUA_M-M | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 12b8a6c4-f911-3adf-ac2c-007d741269b4 | -4.45996 | -42.89614 | 2024-10-22 05:01:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a0a2bf94-cb85-3513-a379-678c9870ea29 | -4.45851 | -42.90567 | 2024-10-22 05:01:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| da5ecd82-18aa-3399-9692-ea109aa8cc05 | -5.69683 | -43.13863 | 2024-10-22 05:01:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 051fde5f-0e44-3b32-adea-b3437a3cf57b | -5.69537 | -43.14811 | 2024-10-22 05:01:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 6.7 |
| e1337a11-7d29-3793-8708-08e8bf135375 | -5.23022 | -43.17451 | 2024-10-22 05:01:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5a3bdb83-4563-39b4-9412-363171ac5327 | -5.22874 | -43.18411 | 2024-10-22 05:01:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| fa841807-0f53-325b-8a67-aed6b6c3f596 | -5.22099 | -43.17312 | 2024-10-22 05:01:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a9d5e33a-1903-33aa-9653-8a43c2391559 | -5.2195 | -43.18275 | 2024-10-22 05:01:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f97cf89a-6fd6-3970-88dc-f6d3548e02cd | -3.52027 | -43.61051 | 2024-10-22 05:01:00 | AQUA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c6b237e8-33c4-3005-bff5-0d8a5170e540 | -3.30566 | -44.13858 | 2024-10-22 05:01:00 | AQUA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 21.5 |
| a3a23586-edd4-3714-bd4e-920d9fe26a03 | -3.30395 | -44.14995 | 2024-10-22 05:01:00 | AQUA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 3f0fc795-105c-3a23-9fb5-1fabbee1d5f6 | -4.6158 | -44.54825 | 2024-10-22 05:01:00 | AQUA_M-M | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 937914e8-6cc6-3f59-93f3-a4580be9448b | -5.85636 | -43.73733 | 2024-10-22 05:01:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| cb98f68d-ebc0-38dd-a4f0-ee6830b63d20 | -5.82168 | -43.64955 | 2024-10-22 05:01:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 7fd66632-4970-33d3-890f-9e459e934012 | -6.2373 | -44.14146 | 2024-10-22 05:01:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b0be76f1-8f90-307e-92c4-195cc8977ab8 | -5.58158 | -44.87119 | 2024-10-22 05:01:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 6405d88d-c7ee-3aac-ac6d-3e95e0ecdcf0 | -5.57974 | -44.88313 | 2024-10-22 05:01:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| e61f9c91-f3b4-3fa1-a731-51ebf4634862 | -5.57141 | -44.86967 | 2024-10-22 05:01:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 57c3aba2-a192-32fd-a56c-ace02f47aeae | -2.97956 | -45.61107 | 2024-10-22 05:01:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| cc8dcf6e-94b4-3a93-8458-386d658e5607 | -4.55177 | -45.79922 | 2024-10-22 05:01:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 88d506e5-63d3-3d5c-8ab1-57301f264fac | -4.00956 | -46.02481 | 2024-10-22 05:01:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 8670e938-b00c-3433-9cac-cd78954fc6bf | -4.00055 | -46.00781 | 2024-10-22 05:01:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 16eb1a9f-c746-3132-a723-c54c219a3dc4 | -3.99821 | -46.02283 | 2024-10-22 05:01:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 407bb2c9-b37a-34d2-bd93-491f7b257751 | -3.72424 | -45.34018 | 2024-10-22 05:01:00 | AQUA_M-M | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 66.8 |
| dd642ae0-17bd-306b-8131-14225084fb3d | -3.72213 | -45.35376 | 2024-10-22 05:01:00 | AQUA_M-M | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 20.7 |
| d90f29ce-13d1-33ed-a7cc-9e8a44ed20d9 | -2.47645 | -49.11213 | 2024-10-22 05:01:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 27afc91e-02c5-3f62-b75f-ec630e86158b | -2.47613 | -49.11683 | 2024-10-22 05:01:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 9ec5caaf-a8c8-3838-95c9-89bdc130bcd5 | -10.43934 | -44.8964 | 2024-10-22 05:04:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 36dc29d0-21bc-34af-9aa2-bddd0cbc86e6 | -2.4824 | -49.1233 | 2024-10-22 05:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 4b31f6f9-6c28-382e-b8a1-3b44e95705aa | -2.7773 | -49.3067 | 2024-10-22 05:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 98ba1ad3-efac-3301-ade5-4f5bb6588b90 | -2.7773 | -49.3279 | 2024-10-22 05:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 88177539-31ec-352b-9418-f1aba3b66fce | -2.7589 | -49.286 | 2024-10-22 05:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 3629903e-eea9-3c09-93f9-bc2eabf524a8 | -2.7589 | -49.3072 | 2024-10-22 05:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 163.9 |
| 5adaccb2-cfc3-3377-bf1e-39f8967f1e1d | -2.7588 | -49.3285 | 2024-10-22 05:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 2e5d49a1-e0d7-3407-8418-cfe5269807c8 | -5.5905 | -44.8687 | 2024-10-22 05:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 1646d480-b67e-376c-aba6-38e645fcd2d9 | -5.5903 | -44.8914 | 2024-10-22 05:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 1f2164ac-1fb1-3e81-90c3-a21954b40246 | -5.5718 | -44.87 | 2024-10-22 05:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| fed06609-2d56-38af-b910-f161a93851bd | 2.13424 | -50.78339 | 2024-10-22 05:08:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b9d2a4a-ca66-3ade-86cd-90f998f9901e | 2.13405 | -50.78118 | 2024-10-22 05:08:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef1506c0-3187-3a64-9f81-8d90e6248727 | 2.13346 | -50.77839 | 2024-10-22 05:08:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 100b99a7-54f3-3cc8-98fb-f468b55ae670 | 1.84358 | -50.49625 | 2024-10-22 05:08:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a1b2f497-5153-3030-9530-1b65b04dc84b | 1.84011 | -50.50037 | 2024-10-22 05:08:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0e9e7734-1cd8-326a-8138-5def8556e9b3 | 1.83956 | -50.49688 | 2024-10-22 05:08:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ec4879d0-1400-3d20-839a-24a9c7a0c257 | 1.83901 | -50.49339 | 2024-10-22 05:08:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 92ab7c8f-718e-3cc2-9b77-4b325a0843c3 | 1.83444 | -50.49052 | 2024-10-22 05:08:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f031f04-31c7-3925-ac9d-2288ac70cc01 | 1.81214 | -50.47972 | 2024-10-22 05:08:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e1cbd616-7c0f-3050-9c95-0f9bec6d43ca | 2.44255 | -51.39004 | 2024-10-22 05:08:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c899f12-e192-35a0-ac27-e92b379df971 | -3.52375 | -43.61037 | 2024-10-22 05:10:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9704587-2cbc-3fd5-a03e-8bd2ea397bb0 | -3.52286 | -43.61661 | 2024-10-22 05:10:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 22a6c574-1f17-3326-b7ef-6947331ffa9c | -3.31596 | -44.14447 | 2024-10-22 05:10:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 890d4ee6-44b9-3b1e-9a89-652d7da7fcc2 | -3.3151 | -44.15021 | 2024-10-22 05:10:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fa7f557b-2a8b-3fff-b08a-d589e2836b78 | -3.31384 | -44.14388 | 2024-10-22 05:10:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b34bd703-53ee-318a-b4e8-525569988a6e | -3.31302 | -44.14964 | 2024-10-22 05:10:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d15736f2-2290-376e-8aa9-b2b6165e61f2 | -3.30934 | -44.14349 | 2024-10-22 05:10:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9de528f9-4913-3450-b731-78b9dc997ac9 | -3.30847 | -44.14934 | 2024-10-22 05:10:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a550d26-614c-3b02-9480-c3418ff48c60 | -4.62388 | -44.55064 | 2024-10-22 05:10:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f0d53b53-2b91-3732-a755-d6527fdffc78 | -4.62306 | -44.55637 | 2024-10-22 05:10:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4c84f951-81b2-3f5d-acca-53aab6d1fd3f | -4.62223 | -44.55495 | 2024-10-22 05:10:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 949556bc-4a10-33ce-87ca-49a7ae53cd32 | -4.1092 | -44.23253 | 2024-10-22 05:10:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 577f6b19-90e6-3a45-a20c-a3364577f4a8 | -4.10838 | -44.23855 | 2024-10-22 05:10:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d2b07ea-1b2b-3e03-93b3-fcf948733169 | -4.10473 | -44.23595 | 2024-10-22 05:10:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 88c0bf95-6f34-38f4-953a-45f195080dcc | -5.83122 | -43.65071 | 2024-10-22 05:10:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 334abaf9-1db9-33e0-ae97-f2af7a896798 | -5.83028 | -43.65749 | 2024-10-22 05:10:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 812fb654-937a-3f58-a3b8-9f0b4dead744 | -5.82928 | -43.65098 | 2024-10-22 05:10:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |


[Clique aqui para ver as próximas entradas](README26.md)
