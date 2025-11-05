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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85e7a7a8-b9e3-3695-895a-318b014716db | -3.48886 | -43.62266 | 2025-11-05 03:51:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aad63f8b-d22e-309f-a422-f173ed864d38 | -6.52018 | -39.68958 | 2025-11-05 03:51:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ba933bb1-23f1-362a-9dba-604bfa4866ae | -4.58434 | -43.33489 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cda5b249-799d-3171-9f94-7ad710c4745a | -2.98272 | -48.7072 | 2025-11-05 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 581edd52-7609-3480-9bfc-2d7a9c515de3 | -4.41394 | -48.94364 | 2025-11-05 03:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 39ffca8d-def8-3522-a1db-f38d2c7cc7ac | -5.26551 | -44.13876 | 2025-11-05 03:51:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b01377e0-a29f-3389-ae7e-b31094407baa | -5.13638 | -38.54142 | 2025-11-05 03:51:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ef35b34d-49b8-3cac-bb44-34e39fcefa42 | -4.89916 | -46.85735 | 2025-11-05 03:51:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2e80eae0-9629-3e1c-8e9c-c4fa8e1d4f98 | -7.72712 | -46.59072 | 2025-11-05 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84126f35-af6c-38cb-9fd2-362706de04fe | -2.82205 | -45.14698 | 2025-11-05 03:51:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 19.9 |
| eac94502-4c66-3500-bfa9-dc3daf908a20 | -6.21954 | -46.13858 | 2025-11-05 03:51:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b2853243-4b3f-3938-befd-dc5aea4fabc3 | -7.4407 | -46.61009 | 2025-11-05 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c04a090e-892a-36c6-bb9b-07f6203e6b3d | -4.11618 | -43.88301 | 2025-11-05 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2467f176-ca97-3456-bfe5-17f4a1cd8aa4 | -3.67025 | -44.80534 | 2025-11-05 03:51:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 467d07b3-40e2-3564-936e-794cefd9710a | -5.69759 | -35.33366 | 2025-11-05 03:51:00 | NPP-375D | EXTREMOZ | RIO GRANDE DO NORTE | Brasil | 2403608 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e2735728-21f8-399e-9720-e9fdb2128bc5 | -4.4695 | -43.23555 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 160c17f4-a5bb-31cf-8a32-e62e35cb393f | -2.39656 | -47.14941 | 2025-11-05 03:51:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 136199f8-5a04-3897-b288-f9bdf4ed807d | -6.50389 | -38.20942 | 2025-11-05 03:51:00 | NPP-375D | LASTRO | PARAÍBA | Brasil | 2508406 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b93530c2-87fa-3696-9941-72d86e75520a | -4.92287 | -46.72429 | 2025-11-05 03:51:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60182b22-fbe1-30bd-980b-a51664e5cee0 | -6.06595 | -38.1515 | 2025-11-05 03:51:00 | NPP-375D | FRANCISCO DANTAS | RIO GRANDE DO NORTE | Brasil | 2403905 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dbe7f2b1-117b-3534-bae8-e0fb61bfe58a | -4.29354 | -43.78391 | 2025-11-05 03:51:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3499551d-2e0a-3ea7-b5e7-e8f2e3925702 | -4.29268 | -43.78902 | 2025-11-05 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4dee1f0-2cfb-341f-9fc3-247b655cb4e2 | -5.26518 | -44.8152 | 2025-11-05 03:51:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6cb60e8-b678-32ea-8940-a759ffa4fb9f | -7.12898 | -41.33446 | 2025-11-05 03:51:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7cb58e22-a943-3ca9-9402-b52c470321ce | -8.05752 | -49.64428 | 2025-11-05 03:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7186bbb0-a068-3b60-a8f8-02092406b57b | -3.48153 | -43.63733 | 2025-11-05 03:51:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 35330b8e-1cd6-397a-adf3-6512d58b984a | -2.84146 | -49.40674 | 2025-11-05 03:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8a8bc8e3-c00e-3dd9-aed7-18949a66b2bb | -7.03081 | -43.80733 | 2025-11-05 03:51:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86bab7e6-feac-3bd4-a54c-b57dec15cbdc | -3.49676 | -43.63447 | 2025-11-05 03:51:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a8ba1cf6-4ce1-3d2b-9357-aeb88ceb3934 | -4.46257 | -46.63708 | 2025-11-05 03:51:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4edf5271-ff96-36a9-9c47-126412d46cc5 | -4.29747 | -43.78971 | 2025-11-05 03:51:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dafb07f0-2073-3a75-a04b-cf8ea57da892 | -8.39288 | -38.80117 | 2025-11-05 03:51:00 | NPP-375D | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1595f599-0379-3abd-a6ba-3caf3cc20343 | -6.05085 | -43.03412 | 2025-11-05 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 504359f4-a48c-35ea-98ff-af82c771cfdc | -2.84729 | -49.41458 | 2025-11-05 03:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75205cc0-89c7-34fd-b18a-bc71c12cbbc6 | -4.41627 | -48.95101 | 2025-11-05 03:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4df7ec8f-3e62-3b14-8847-11fd575f74cb | -4.10663 | -38.31976 | 2025-11-05 03:51:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3d937121-171a-33cb-a5a3-3b1c017423ce | -7.52612 | -47.14507 | 2025-11-05 03:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 891167a0-acb3-3a85-96ea-332022130144 | -6.58932 | -35.25547 | 2025-11-05 03:51:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ef217f93-f14c-3989-874d-e41128bc32f5 | -2.6566 | -48.51082 | 2025-11-05 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 87194e0e-282b-318b-99fb-2ed902059015 | -6.70542 | -40.82723 | 2025-11-05 03:51:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0203e8da-0eaf-343f-ba83-8c3e093ad477 | -3.58909 | -50.17069 | 2025-11-05 03:51:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cbcf6838-850f-3395-9dc9-39d8bc40ed23 | -6.52375 | -39.69013 | 2025-11-05 03:51:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7b7b1dcd-e698-35ef-83a8-b58a6bc3fb6b | -5.52197 | -41.11904 | 2025-11-05 03:51:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a105b206-42ed-3ae8-bb49-036d10dd07df | -4.11222 | -43.87693 | 2025-11-05 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 225cab46-0b2a-3d80-9956-a04fe8335e47 | -6.37241 | -42.40723 | 2025-11-05 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ca5db20c-7710-3821-a156-6bc2f8d2d634 | -4.29833 | -43.78464 | 2025-11-05 03:51:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a06e27b6-c726-3eee-a785-78e2dbfd8ab9 | -8.69116 | -40.545 | 2025-11-05 03:51:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 34e34251-b805-3bb1-9239-4ea9017c58e5 | -4.54428 | -40.64033 | 2025-11-05 03:51:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 078bc72f-31af-3dd3-a149-6d1a6501f875 | -4.45387 | -43.2215 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 1e201857-2391-39ba-b670-75f4cfebea12 | -7.48562 | -41.20647 | 2025-11-05 03:51:00 | NPP-375D | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 06adc4c6-7520-3a82-8eaf-b5c02b527b04 | -3.33215 | -44.35505 | 2025-11-05 03:51:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4291e386-f963-3da7-8b0d-8e8282b8adba | -7.83965 | -38.24216 | 2025-11-05 03:51:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bab50f68-7cda-3213-bdf5-42698eb192ca | -3.96593 | -43.78091 | 2025-11-05 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2319c803-5072-3450-91ea-4470e776142b | -4.5093 | -45.43435 | 2025-11-05 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5abd4ed4-cc94-3819-9345-e57d7af67666 | -5.03504 | -44.79246 | 2025-11-05 03:51:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c707959-61e6-3ae3-b8d2-2225689466cd | -4.50661 | -45.4352 | 2025-11-05 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c21287a1-0e3d-303c-9b2a-8f3dda943f9c | -8.23299 | -49.9838 | 2025-11-05 03:51:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bce57b5d-8f0c-32ff-abf2-a822ae7cd49c | -4.05058 | -43.47754 | 2025-11-05 03:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 567b93d4-2dbf-3785-994e-b207f2108cdb | -3.97073 | -43.78167 | 2025-11-05 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 117c094f-9f8d-324d-9f4f-a377b5df0cf2 | -8.0921 | -42.94484 | 2025-11-05 03:51:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 6b53d5a2-9508-3288-ae44-741426f71d83 | -7.54678 | -45.84438 | 2025-11-05 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4122bdae-6dae-34d1-8336-b79f3708ea27 | -4.30441 | -45.37672 | 2025-11-05 03:51:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a91aaa89-f088-3abd-8237-039ceee5e5c3 | -6.84726 | -46.2955 | 2025-11-05 03:51:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e41cf435-d925-32ea-9181-4dd257f7c3fe | -5.2367 | -48.50072 | 2025-11-05 03:51:00 | NPP-375D | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 765f9824-0582-336c-a589-9655bd101fac | -7.42196 | -46.65069 | 2025-11-05 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 86e31e53-0fbf-328f-a9c6-182addc5bfb2 | -5.92579 | -41.29327 | 2025-11-05 03:51:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bdd22ad0-bf2e-332c-93d9-61d74a2058ea | -4.29661 | -43.79488 | 2025-11-05 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c4af8078-5c03-3137-8eb7-14963ac09171 | -7.28688 | -45.45561 | 2025-11-05 03:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b29dc65f-518e-3243-8fb6-e3a5529cea2f | -7.71551 | -47.18757 | 2025-11-05 03:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 520c3886-e9a4-30f4-b0f9-237188c3a664 | -4.6603 | -44.52508 | 2025-11-05 03:51:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a32f687b-c1a0-3a43-89b4-9bbb20263350 | -5.27072 | -44.14354 | 2025-11-05 03:51:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74ffc703-a8c7-3a66-a189-eea24dcc5539 | -4.71127 | -46.43577 | 2025-11-05 03:51:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 264b2e0d-b578-31ed-8366-f788dbb1ea94 | -8.21238 | -43.8121 | 2025-11-05 03:51:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 660bd504-bfc4-3871-a0bc-6c5d97d3dc31 | -5.78643 | -40.82454 | 2025-11-05 03:51:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b02bde48-2711-36f4-93a8-f9ac60b46fc7 | -6.54999 | -44.47366 | 2025-11-05 03:51:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b5fa1bb7-98ab-3f15-b857-7a15d99a5128 | -3.2343 | -43.44214 | 2025-11-05 03:51:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5109414e-009b-32e7-ba38-6becff2ae5b6 | -4.86694 | -44.63008 | 2025-11-05 03:51:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d0bc579-33e5-3df1-a132-d117b21daea9 | -3.96505 | -43.78611 | 2025-11-05 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 25c373f1-93cd-36bc-a4c1-f39a3b87b2c2 | -7.23414 | -45.69751 | 2025-11-05 03:51:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| edcc2777-2511-38bb-b2e0-c1dba04bba97 | -8.75411 | -44.23484 | 2025-11-05 03:51:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 89bdaf86-6dc1-397f-8081-6e789d4ea749 | -6.06257 | -38.15095 | 2025-11-05 03:51:00 | NPP-375D | FRANCISCO DANTAS | RIO GRANDE DO NORTE | Brasil | 2403905 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 45a379b6-8e47-3557-8c25-91a32b391beb | -3.71105 | -45.89032 | 2025-11-05 03:51:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ebaec5d5-6692-3db8-97a8-4f8ee574f4f9 | -5.53812 | -40.75595 | 2025-11-05 03:51:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c9fc3a62-c0d4-3844-b9a4-3be2d0b1a91c | -3.86569 | -41.01104 | 2025-11-05 03:51:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5f45dedf-a3b7-3e16-a4c8-3c2432477c50 | -5.92995 | -41.36678 | 2025-11-05 03:51:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 56087779-de57-38b1-8d85-d64086018a8c | -5.32302 | -41.23769 | 2025-11-05 03:51:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 834e1722-9fba-3309-96db-793a3a0da091 | -6.55088 | -44.4685 | 2025-11-05 03:51:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 93411951-b0a3-36f3-8bc9-007d256f307d | -3.97565 | -42.13935 | 2025-11-05 03:51:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2ff50d07-9771-3ca7-a134-03500438bc04 | -4.47107 | -43.22624 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| d45da217-7512-3c03-a97f-6ac44ecc1a75 | -5.52075 | -44.0522 | 2025-11-05 03:51:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22a262e4-efbe-3929-b06e-ccad2952fcf3 | -9.78197 | -43.61572 | 2025-11-05 03:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| c17a2f8d-4d63-3859-93b9-2b6462a13542 | -4.11432 | -43.88382 | 2025-11-05 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85f9a04a-3232-3e16-a1de-234d2e7ccf36 | -4.92033 | -47.3258 | 2025-11-05 03:51:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 42329055-b56e-367c-a071-f0dfeb430d0a | -5.82579 | -39.20641 | 2025-11-05 03:51:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0b69612b-7324-3ba1-a356-7656b26cf026 | -3.65579 | -44.79654 | 2025-11-05 03:51:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36411c94-4f97-3fb6-a38e-776e733aa08f | -4.71628 | -46.4406 | 2025-11-05 03:51:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29b9a14e-f735-3eab-b98f-ffdff8535393 | -8.79821 | -40.4379 | 2025-11-05 03:51:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e061a519-d3e2-356b-81e1-a4dfd43bcf97 | -5.02936 | -43.62255 | 2025-11-05 03:51:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9a43156c-d0b5-3ece-9577-219e854507aa | -6.73967 | -44.16742 | 2025-11-05 03:51:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf001d83-e23d-3542-9e03-e09425635691 | -3.86655 | -44.43312 | 2025-11-05 03:51:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README12.md)
