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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 469bb2b0-6cc0-336c-b352-853b51a88ff7 | -4.75964 | -46.85457 | 2025-10-30 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6b6faf7-bced-3346-bf66-e9ce0900010f | -10.99121 | -47.86287 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0df4867-8d8c-372f-9afe-08f6d88ef07c | -10.34733 | -44.07013 | 2025-10-30 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b1167b0-dad7-34bf-8bfd-dfe395c08be1 | -7.4876 | -47.05241 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96e10310-f7af-3ca3-94a9-a6c0a3943482 | -7.32188 | -42.48888 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 348e5a38-39fb-3ef3-8448-7a29afb135d5 | -10.29927 | -47.27946 | 2025-10-30 04:25:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11204308-1e12-3f74-92a5-cc96170eef01 | -4.57842 | -45.51 | 2025-10-30 04:25:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 281e7467-1e46-3f5b-88ed-a4e8f861ab2e | -8.16016 | -45.47714 | 2025-10-30 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 74ac9dd9-859b-384c-af15-a309eb55e707 | -11.16087 | -41.1033 | 2025-10-30 04:25:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2545c96d-71a7-3f0a-a74e-1e244386c5d1 | -7.6155 | -43.56723 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 28ad92f7-7388-3713-87c6-005b1c1f1f3a | -7.96111 | -43.79267 | 2025-10-30 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 98f2a1ad-1fb0-3bfd-8733-bb1ba218441f | -7.35509 | -47.62674 | 2025-10-30 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04b8b7b5-90dd-3bcb-a7b3-dc77c6fd7fdb | -7.05671 | -44.94503 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1c209fa-65b0-335e-b440-067e6c6996d2 | -5.38008 | -47.20686 | 2025-10-30 04:25:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec7e1c14-b9c2-3c10-8a01-c2aae835ecf9 | -10.77023 | -47.88446 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34711583-3c3d-375a-afaa-6c10beeb52d9 | -8.03022 | -42.51326 | 2025-10-30 04:25:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bdd435f0-0e58-3760-9113-752545898ced | -5.51351 | -46.23656 | 2025-10-30 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1733508-86c8-33e3-ba18-59bf8e07074b | -9.18396 | -43.02024 | 2025-10-30 04:25:00 | NOAA-20 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e0fea9bc-1101-35d6-b3df-eb821473a11a | -7.15255 | -44.86036 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aeb2a06a-c128-3dd8-8396-30b04c5612fa | -4.69638 | -45.83854 | 2025-10-30 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 921b9d60-c15f-3fec-838e-29f07dae6d58 | -7.45891 | -46.84771 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56c44ff5-5471-3d42-9460-af054388b80a | -10.64976 | -47.89432 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ebdadbe-7374-3ad0-87fa-5bef903fd474 | -5.13262 | -43.81112 | 2025-10-30 04:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac26737b-1f52-39bc-9669-e3b46de1a605 | -6.08656 | -41.78059 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 28d2beab-9b2b-356b-8f15-f613c3fbaad5 | -9.88829 | -44.87883 | 2025-10-30 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86089176-c0da-34b5-96ce-83c4f02792d2 | -7.61489 | -43.5713 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bd07b303-c74d-3d9e-a2b0-467912cdcff9 | -9.26853 | -45.22364 | 2025-10-30 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88d727de-b2cb-349f-abdf-184ec88a6a9d | -4.52651 | -54.96454 | 2025-10-30 04:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bafb30c-cab1-326b-903f-bfde35cc088f | -6.12615 | -42.43737 | 2025-10-30 04:25:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ba5cbe8b-e21a-3785-9407-b1a3ccf0e725 | -10.23525 | -47.63865 | 2025-10-30 04:25:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2e0e146-5384-3459-b010-bacc0b29a604 | -10.61711 | -47.88539 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab57b45e-59e4-339b-9771-1102341e58eb | -5.28007 | -47.23802 | 2025-10-30 04:25:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0565c28-7acd-32b2-bbda-0c03929b01ab | -7.32315 | -42.48649 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 33f17324-37b5-31f0-a910-287a4384a14b | -8.71387 | -47.86364 | 2025-10-30 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d8127af-73d2-390e-a41a-d81978c46fdd | -7.35106 | -47.65194 | 2025-10-30 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4816161-5071-3806-9127-d7a20a80fdff | -7.37689 | -47.61929 | 2025-10-30 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89e78b82-aa78-3706-b6d6-54e3407f575f | -7.78582 | -46.41299 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a2200323-a577-3e8d-824a-c3896531801c | -8.08242 | -49.29318 | 2025-10-30 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b985f356-84e1-3371-b2ba-1b0855ba40c7 | -8.17548 | -45.70429 | 2025-10-30 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 74255154-88cb-33f5-acc8-c96b772400b8 | -9.86235 | -47.6973 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94168e78-bb8f-3b8f-8075-a692149ff266 | -5.70074 | -43.15631 | 2025-10-30 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 1f8b44e5-bcbb-3458-8c3c-13b004b62670 | -7.79904 | -46.41509 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24162df5-4dfb-3df8-a5d6-ce3a9347493a | -10.28038 | -44.57362 | 2025-10-30 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f0c503d3-0726-38b3-8aee-33849f84c5b9 | -5.11361 | -42.62498 | 2025-10-30 04:25:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20741b8e-7738-3784-bdb7-9ac76a14e599 | -10.25859 | -44.56702 | 2025-10-30 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d028c14-4632-315d-a3e8-cada606a87f3 | -5.9646 | -44.72653 | 2025-10-30 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 22024539-502c-3dfd-af97-79b5824e7bf6 | -8.23987 | -49.78144 | 2025-10-30 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| deff0a5a-b475-3fe3-a09c-bd717365af4d | -7.53817 | -47.31181 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6cb1fe4a-4f92-30f5-9593-db9e10c5a15f | -5.79253 | -40.82718 | 2025-10-30 04:25:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 620d6ab9-cdb0-37bb-a0a8-e53f3f70f5f7 | -5.03803 | -46.7687 | 2025-10-30 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8553d3e6-1812-3dd4-bc7f-25a8eee548de | -7.78803 | -46.42044 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| be47aa1f-422d-38a1-ab81-2c9cff5c4d1f | -5.84399 | -40.81596 | 2025-10-30 04:25:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 82b2ba93-82be-3536-916f-2a3385a63d83 | -5.2399 | -44.29529 | 2025-10-30 04:25:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6ac06f3-c7ed-36bf-8683-9f6d32b9002b | -7.42703 | -45.97269 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 471faf3f-dcb1-3992-b439-23fe303db0b1 | -9.31707 | -43.0954 | 2025-10-30 04:25:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f6d5f721-c2ec-3883-afd8-47909e8ae194 | -10.53875 | -45.04511 | 2025-10-30 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0dfd97b9-cf46-3796-ad03-5efdaed0168d | -6.10486 | -51.21645 | 2025-10-30 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 701a48f0-47ff-3baa-accc-05c9ae606968 | -5.72334 | -44.79204 | 2025-10-30 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b6f8c04-98c5-3a14-9cf3-4aaed1ab0c69 | -6.06019 | -44.15589 | 2025-10-30 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 750020a0-3630-3d39-b8cd-e1ccae40b84d | -3.8797 | -51.19141 | 2025-10-30 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1cb2436-7bcf-3de7-bb6f-a758228c4aa4 | -7.21363 | -46.03559 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a62a2a7a-2410-3363-9627-75e6751ec987 | -9.81559 | -47.5851 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56ae841d-2d17-3353-8883-be275a1de431 | -10.76373 | -47.84005 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 655ac2fc-d278-3af8-9f03-ab8bcaab6a3c | -9.94299 | -47.1898 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5909f2a-c9cd-3964-a0b9-d0ca8907feb0 | -6.21953 | -41.82639 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9f2f05d1-5693-3e61-a102-4ceba5ab3a8b | -6.12783 | -41.86156 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 784afc8f-9ef6-316e-966f-870dcd7ea7a0 | -7.96073 | -46.72515 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91cd8d16-3d6a-38e7-92e8-4ba727944a4a | -7.37298 | -47.62231 | 2025-10-30 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14c88219-8995-3010-ac2d-cda148a3f432 | -5.80309 | -40.84013 | 2025-10-30 04:25:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 27270736-4691-32e8-8f0a-81bac600a5ec | -7.38466 | -47.63523 | 2025-10-30 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61b90a8d-d84d-30fe-b9e8-3681af75f3b3 | -4.43513 | -50.10369 | 2025-10-30 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a535ae7b-733a-3325-b7a5-ecede6ebd6bb | -11.18166 | -45.21452 | 2025-10-30 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 494b334e-8083-3b67-ab66-5da40b3322e4 | -5.3102 | -44.85143 | 2025-10-30 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3408f1d7-1d6a-3a87-8f2d-80721f60045c | -10.25939 | -44.57061 | 2025-10-30 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 81041525-2650-36c4-a5d6-8ab8e1c07748 | -9.01401 | -48.65429 | 2025-10-30 04:25:00 | NOAA-20 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 501a5b7a-e16a-3a46-ae2a-47b3f667d598 | -10.48083 | -45.03697 | 2025-10-30 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96dedba1-ca02-3b33-beec-44cbdba151db | -7.08335 | -46.34432 | 2025-10-30 04:25:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f00686c-4237-3bb6-8b23-040043fa2bb7 | -7.76664 | -46.49159 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 91792729-d775-3c97-8c2a-621e30e63ed5 | -10.6631 | -47.68357 | 2025-10-30 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab7984e8-6f2f-31bb-838d-8dcd0eb8b62d | -10.75299 | -44.74277 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d18a40d5-249a-3cac-a0d8-7768afc12316 | -10.77318 | -47.82355 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f33cb76-7977-3999-9126-5c47b585d228 | -5.04081 | -43.61219 | 2025-10-30 04:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 02c552b2-34ec-3b0f-a3a5-e91f69593f37 | -9.8946 | -44.88371 | 2025-10-30 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c382382-4066-3901-9a32-fbee478f46e1 | -7.08469 | -44.94228 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcd832f5-e727-3e2c-939f-b0944322ecdb | -6.52162 | -46.90849 | 2025-10-30 04:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 02b760d8-d09c-38c6-9508-aab64601c060 | -9.89803 | -44.88425 | 2025-10-30 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87055262-3d16-326d-b679-aef8bd2752e6 | -7.32632 | -42.48492 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 730fe05e-ff7b-3652-8775-69826c44be51 | -8.32799 | -47.93356 | 2025-10-30 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 7502652f-59d1-3a31-8b16-f1348cbac318 | -11.70054 | -46.70371 | 2025-10-30 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 319e27e5-09e5-3bac-bfdd-478aa13f7667 | -6.31173 | -42.10901 | 2025-10-30 04:25:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4d992e11-c9c1-380a-a270-1f56f036ee02 | -6.10692 | -42.43905 | 2025-10-30 04:25:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 154239a6-a597-3087-a129-df9ad7e3e604 | -5.82511 | -43.09427 | 2025-10-30 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 98b6efe3-67bf-3230-b240-65f1ae988380 | -6.91614 | -42.25646 | 2025-10-30 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| c1923b92-2c15-3646-b4e6-06d4f9b68b5c | -5.59775 | -49.70714 | 2025-10-30 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f99b247-0ed0-35e4-9026-04eb6a74fed7 | -5.80888 | -40.82934 | 2025-10-30 04:25:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 905dec48-f277-3eb2-897f-6c5bfa7e6f3d | -7.7815 | -46.4833 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 598b7f82-8da8-31ea-a397-a6b0eca61db4 | -11.29268 | -47.54847 | 2025-10-30 04:25:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d2da28a-70a0-3242-b74c-c3bf0365b31b | -11.46168 | -48.53251 | 2025-10-30 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2302ee0-8cae-3164-b095-531498e8521c | -7.38287 | -42.47223 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a4631b37-aa79-32b7-b459-00c2f51a1c80 | -6.91277 | -42.2532 | 2025-10-30 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |


[Clique aqui para ver as próximas entradas](README46.md)
