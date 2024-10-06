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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a34b6c3-7b44-3f44-bf2a-ad5261c875d5 | -9.33938 | -46.55687 | 2024-10-06 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 571ec6b4-c7d6-3103-8b9b-8ceffe113612 | -9.33742 | -46.54016 | 2024-10-06 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5365749b-30d7-3d33-a71e-5b4d75179e09 | -9.33649 | -46.54536 | 2024-10-06 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1808e8c7-d8d2-3fcd-a551-a51e40464349 | -9.33554 | -46.55063 | 2024-10-06 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0d162b0f-026b-37da-ae45-d18b87bc8bec | -9.33459 | -46.5559 | 2024-10-06 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5c363d20-1398-3519-ae1e-868029730b2b | -9.3317 | -46.54443 | 2024-10-06 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c5cd81c3-8c89-3cd3-bb1f-dbfaea96db33 | -9.0371 | -46.57658 | 2024-10-06 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0ebf9c6b-fb5b-3ba9-b0b7-ec3e5ae16c0b | -9.03227 | -46.57571 | 2024-10-06 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29b2a284-b5d7-3ae5-ac82-4d43530c8252 | -9.0313 | -46.58112 | 2024-10-06 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 014aecd6-d8ad-3352-b691-9e2b205d168b | -9.02743 | -46.57484 | 2024-10-06 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b3e029b-1e49-31b9-80ce-6a6f4039d93f | -9.02646 | -46.58028 | 2024-10-06 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7b9e3644-8a98-3118-87d0-14503b25dae1 | -8.6148 | -46.49927 | 2024-10-06 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b96ea37d-e116-32b8-9031-8be00fd1508f | -8.60998 | -46.49828 | 2024-10-06 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53154099-36b1-31c1-aba5-de90994d332e | -8.59733 | -46.48513 | 2024-10-06 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28401f8f-5c76-343b-b832-08024bc72979 | -8.59154 | -46.48954 | 2024-10-06 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1f51192-0242-3e7b-b548-877b142cd3cf | -8.57233 | -46.51305 | 2024-10-06 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6526ac14-3a07-3296-af51-d7832c4ead5a | -8.39399 | -46.30353 | 2024-10-06 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0bc82617-9f1c-3252-8179-d5cb53dcf96a | -8.39009 | -46.29764 | 2024-10-06 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 4c5df6db-978e-36ca-b994-b7b5e7c144d3 | -8.38916 | -46.30284 | 2024-10-06 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0a52456f-3813-3819-8f47-2dd8e2ce473a | -4.82593 | -46.79688 | 2024-10-06 03:53:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42be120e-57f5-3cf3-8939-9d052e60d0b2 | -4.82539 | -46.80011 | 2024-10-06 03:53:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5975e7ab-594a-35bf-ad14-5cd54593eae5 | -4.82485 | -46.80334 | 2024-10-06 03:53:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f9bbebf-6e2f-3dea-aaab-4098812554a1 | -4.82433 | -46.79813 | 2024-10-06 03:53:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 94e63552-49ba-3944-bd62-61073f37e514 | -4.82377 | -46.80135 | 2024-10-06 03:53:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 499a2252-55d6-32d5-b23b-6d9275e43556 | -4.8232 | -46.80457 | 2024-10-06 03:53:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7a4686e-2b5d-33e0-9e03-9b767c88c2a0 | -4.76606 | -46.67264 | 2024-10-06 03:53:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebc04063-fcc7-3378-82e2-d9478710d9d2 | -4.45929 | -47.46675 | 2024-10-06 03:53:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3303f3c5-d02e-3cc5-8e58-763621ee16a3 | -4.45377 | -47.46563 | 2024-10-06 03:53:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea626f4a-301f-3460-86d4-ceeacb92ce74 | -4.45317 | -47.46919 | 2024-10-06 03:53:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8adc1a6-4b94-397d-938c-42de8b6d535b | -4.42491 | -46.43706 | 2024-10-06 03:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 972db7c3-3648-358b-b993-6215b0fc3bb9 | -4.31681 | -47.70643 | 2024-10-06 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59c8ef0b-5ea5-378f-a182-4aa2cd386252 | -4.31618 | -47.71014 | 2024-10-06 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc96fdb6-c131-35e8-a44b-e0515a463016 | -4.31122 | -47.70512 | 2024-10-06 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9e5b71a-84eb-3bbe-a5a0-94ce6d3edd16 | -4.31058 | -47.70889 | 2024-10-06 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1717aebf-f5a3-36f0-ae92-692473fa107b | -4.2996 | -46.76962 | 2024-10-06 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e886c37-2174-3494-b67c-0a2f529d80ba | -4.29907 | -46.77278 | 2024-10-06 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d8ae62b-2acb-32bd-98de-d0fa96bfcd38 | -4.29788 | -46.76959 | 2024-10-06 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51d2df73-4af0-308e-a601-d33a28df9883 | -4.29733 | -46.77274 | 2024-10-06 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 152f832c-0045-3146-ba34-bb4db4a0ad35 | -4.18414 | -46.85468 | 2024-10-06 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| acd2bdec-3779-39f9-93fe-36941cf1ff26 | -4.18179 | -46.85036 | 2024-10-06 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33c7685f-faaa-3cc5-9a4e-a8d87964a3db | -4.18122 | -46.85367 | 2024-10-06 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acc8996a-9974-328c-bd2d-3b0a3432f9ee | -4.17882 | -46.85361 | 2024-10-06 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c1a57a1-2649-3c2b-9e1b-ae9ab2e886dc | -3.85158 | -46.46297 | 2024-10-06 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bb31e9fe-b7b8-32da-aeee-6dd1305511ce | -3.85104 | -46.46616 | 2024-10-06 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e8f57523-8d82-3fdf-a0dd-8cde5877c2ef | -3.84638 | -46.46191 | 2024-10-06 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 0d76bb45-53a2-39f9-8caf-a0cdcf068125 | -3.84585 | -46.46504 | 2024-10-06 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 9a2bdd48-9c4a-3a89-85f1-bb1f10110b0a | -3.84529 | -46.46829 | 2024-10-06 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 42ce2dad-481e-3363-8c3a-a1e35ee14c97 | -3.84062 | -46.46408 | 2024-10-06 03:53:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 29a92851-b734-36e1-968e-8cd461cf5f09 | -3.61781 | -47.51637 | 2024-10-06 03:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1772427b-ebc0-37fb-b898-a1be8889f4ce | -3.61217 | -47.51542 | 2024-10-06 03:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b659d44f-7e89-3fab-9236-be2ce216fac7 | -3.61154 | -47.5192 | 2024-10-06 03:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bf7099d-cd5e-37ec-a99b-6accb76f2afc | -3.60589 | -47.51827 | 2024-10-06 03:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2372f1e9-b920-3abc-b685-9178da48f277 | -5.71496 | -47.14942 | 2024-10-06 03:53:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16f48a6e-9c8d-3dab-82d3-07a03a6ccef7 | -5.71438 | -47.15281 | 2024-10-06 03:53:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c30c4488-d4ae-3cf1-a170-ad50a503fd13 | -5.71381 | -47.15615 | 2024-10-06 03:53:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40e5d71f-6650-3bfd-b4eb-b7c26d6e17b4 | -5.71324 | -47.15945 | 2024-10-06 03:53:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 985c9f22-2472-30a9-b280-3265befedb25 | -5.70965 | -47.14843 | 2024-10-06 03:53:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89ee112f-51b0-3863-860e-125c1db022d3 | -5.70907 | -47.15181 | 2024-10-06 03:53:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f627732-6ca7-30a2-8342-ffb2e65ff854 | -9.45634 | -47.57763 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30dd80db-156d-3a3c-869e-4ddf86ba741f | -9.45578 | -47.58065 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 421e030c-6c81-3f1f-88e5-fd61c480a82f | -9.45121 | -47.57663 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33cf5f17-8a05-39e2-aa4c-a0e976324dfb | -9.45066 | -47.57964 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e638d8e3-e064-388a-88f0-e3ed6f610e7e | -9.43804 | -47.56187 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13b52dca-b37a-3d0c-9857-c1c35b025856 | -9.43674 | -47.56124 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44fbab86-3209-3f34-a67b-0df2fa824247 | -9.4362 | -47.56429 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f2c4eb4-6d6d-3037-8488-74526b8ec5d2 | -9.43235 | -47.56393 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00ad89ac-9dfe-3098-bddf-9b1d571de489 | -9.43107 | -47.56329 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17d53f4a-d746-3a79-b892-5904332f6597 | -8.87557 | -48.23717 | 2024-10-06 03:53:00 | NPP-375D | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 053c1ed1-5ebb-3378-97ba-deb91a7a71af | -8.87492 | -48.24063 | 2024-10-06 03:53:00 | NPP-375D | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6d40c70-6921-3107-94a2-74df2608f13a | -8.87433 | -48.23954 | 2024-10-06 03:53:00 | NPP-375D | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe865e42-15d6-3751-a258-cdcc4306aee5 | -8.86952 | -48.23957 | 2024-10-06 03:53:00 | NPP-375D | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0bb138a-ab32-3cb3-ac87-dadbcbc75088 | -8.60774 | -47.14718 | 2024-10-06 03:53:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8a6542c9-d5b8-3d5e-b185-0d09eb7f89c2 | -8.6072 | -47.1502 | 2024-10-06 03:53:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9bfcc37b-2534-3676-8128-5b6e1b3f7434 | -8.60666 | -47.15322 | 2024-10-06 03:53:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf7f7211-cc33-3d31-b5bd-ee84f2a28918 | -8.60612 | -47.15627 | 2024-10-06 03:53:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0fc52b41-7118-358c-81f3-0e4ed73baf38 | -8.60212 | -47.14938 | 2024-10-06 03:53:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8ab53ff-3fa5-3a19-8c31-5676f005c07a | -8.60158 | -47.15242 | 2024-10-06 03:53:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b31a8e1-845f-3e05-933b-8e232d737b05 | -8.48713 | -47.307 | 2024-10-06 03:53:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8c6ba94d-8895-3f24-ab18-52714b6c8b0c | -8.48204 | -47.30587 | 2024-10-06 03:53:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d83eb045-e7e0-3dc0-93c4-5e6dd419bee8 | -8.39925 | -48.48455 | 2024-10-06 03:53:00 | NPP-375D | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38fa19be-2830-31f0-beff-b7e343fd758b | -8.39856 | -48.48824 | 2024-10-06 03:53:00 | NPP-375D | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d21f52e1-8a36-3e6d-9951-b8fa01db20f0 | -9.69957 | -47.83562 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a8a1e0e-9337-38e6-a269-b0dbd83f8dd3 | -9.69785 | -47.81539 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| afb0fd79-c2d7-32be-b116-278adf173fea | -9.69729 | -47.81849 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 08bcf0b2-934c-377c-a6b4-e7c6def4cd9f | -9.69673 | -47.8216 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| ad51d030-ad51-3732-8911-3a0e4fed07fb | -9.69615 | -47.82478 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 9359d4e6-8f48-36d8-ad62-5719b53199d0 | -9.69558 | -47.82796 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1d004dfc-905b-3e7b-8fca-a861e22013c9 | -9.695 | -47.83117 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 71d10548-348f-3fb6-ae3d-7bae85c8236d | -9.69441 | -47.83442 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e2a2644-f43b-3086-a150-b4070f9411e0 | -9.69383 | -47.83763 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 775ea690-1e8d-394c-9c0b-4b2fcb4425d0 | -9.69266 | -47.81441 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 33617353-6633-36a6-bf72-ea9ea29f1a9e | -9.6921 | -47.8175 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b08b7282-eabb-3945-98ca-414a4a35c607 | -9.69154 | -47.8206 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6335f2b9-d877-39bd-97f4-709fe43145e1 | -9.69098 | -47.8237 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eeb9c9af-5554-35d7-a376-edabd10cb7aa | -9.68925 | -47.83321 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04e733a4-3627-3230-b857-154ed6df609f | -9.68866 | -47.8365 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 678d209a-cce7-328f-8125-d8487729cbf5 | -9.68691 | -47.81652 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| de26881e-9549-307e-882d-dc5e2c97d62b | -9.68634 | -47.81963 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9b7a88fe-00b6-37e5-99d4-e850d299ae9b | -9.68579 | -47.8227 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 93259f11-97a3-3eeb-a172-8395e765657b | -9.68291 | -47.83857 | 2024-10-06 03:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README51.md)
