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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2d10ec0-723b-3123-a5d4-e9c654f1f33a | -9.0615 | -61.384102 | 2024-09-26 01:50:08 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3d476220-7d66-3f3d-b04b-87a3f3c28eb0 | -9.0508 | -61.426701 | 2024-09-26 01:50:08 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4038fe06-c54d-3a8b-b8f6-5df4b7e60d66 | -9.0526 | -61.4342 | 2024-09-26 01:50:08 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ae888789-40be-396f-b8e8-b512b82578c7 | -9.0411 | -61.429001 | 2024-09-26 01:50:09 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 158b9988-cf54-3f74-b74b-b19baeb1d49d | -10.3881 | -67.855698 | 2024-09-26 01:50:10 | METOP-C | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| cede4750-ab91-32f9-8fa4-f1e68d47e66a | -10.3902 | -67.865601 | 2024-09-26 01:50:10 | METOP-C | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 38e2d78d-ecbb-36db-a37d-5ea1156a09cb | -10.3923 | -67.875603 | 2024-09-26 01:50:10 | METOP-C | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| d0905d32-9690-368d-b1c6-85e0a6b70fe4 | -9.7676 | -65.2892 | 2024-09-26 01:50:11 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1c870a43-dbdf-353d-ad3f-02e95ade8d6e | -9.7692 | -65.2966 | 2024-09-26 01:50:11 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ac894b02-e541-3893-97f9-7eaf3aace7b7 | -7.3804 | -55.484402 | 2024-09-26 01:50:12 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3bae268-18b5-3624-be7c-70b8286820c4 | -7.3849 | -55.5023 | 2024-09-26 01:50:12 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae70909d-3032-3781-8e39-d1b8b980eeee | -7.3662 | -55.468899 | 2024-09-26 01:50:12 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0625f7d-337d-3d97-89c8-a51b6c0d4bf9 | -7.3707 | -55.486801 | 2024-09-26 01:50:12 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe8403e7-67e9-3453-b93e-ae97acbfdcb9 | -7.3752 | -55.5047 | 2024-09-26 01:50:12 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0527c468-076b-303a-b1e2-eb7760014c04 | -7.3797 | -55.522598 | 2024-09-26 01:50:12 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82d3c383-aeb5-3145-b2e5-dc2d44cfddf5 | -7.361 | -55.489201 | 2024-09-26 01:50:12 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 644345bd-2363-3df4-aedb-976ad00b1349 | -7.3655 | -55.507099 | 2024-09-26 01:50:12 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb8d7824-1b5a-3660-a149-c0b92c1910c8 | -7.37 | -55.525002 | 2024-09-26 01:50:12 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56ca5d52-2b97-3bd4-9a89-9907d7766c4a | -8.9674 | -62.1311 | 2024-09-26 01:50:12 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 650ebbcd-8116-3e3a-bff0-f826368e3d9d | -8.9691 | -62.138302 | 2024-09-26 01:50:12 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 90685222-1718-36af-90be-637bf65b37cd | -8.9576 | -62.1334 | 2024-09-26 01:50:13 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 46067eff-325f-3487-8d90-35cb8de3345a | -8.9593 | -62.140598 | 2024-09-26 01:50:13 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 76cee514-1ee1-3242-9e6c-ebb3839c1f0e | -8.9783 | -62.400299 | 2024-09-26 01:50:13 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4112e832-a960-37ff-a0c9-d2136a6cae9e | -8.8622 | -62.344501 | 2024-09-26 01:50:15 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 40d73f27-8b62-3ed7-84a0-508b761420f9 | -8.8638 | -62.3517 | 2024-09-26 01:50:15 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ac3196d1-443d-3b54-8e25-39732f5315c4 | -8.864 | -62.396801 | 2024-09-26 01:50:15 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 11f9f078-cd70-3b04-a68a-fcec62ae57fe | -9.0326 | -63.308399 | 2024-09-26 01:50:16 | METOP-C | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 83e30e4e-abc4-3736-bd1f-eb6c03a31a85 | -9.0342 | -63.315399 | 2024-09-26 01:50:16 | METOP-C | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 92b2236e-9dee-3e17-9484-5073217f9fd2 | -9.36 | -65.629898 | 2024-09-26 01:50:19 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4ac91e22-adaf-38cd-a5de-58e35d9f3b6b | -8.8354 | -63.709202 | 2024-09-26 01:50:20 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b5bf5be1-7adb-3bd4-83c6-235dd19d1709 | -9.5063 | -66.761002 | 2024-09-26 01:50:21 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0745701c-63b8-3269-9d46-4bd7cba67ffe | -8.2297 | -61.490299 | 2024-09-26 01:50:22 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 106bfc78-6c4b-3b3e-9522-801524b37134 | -8.2314 | -61.497898 | 2024-09-26 01:50:22 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ed05d218-78ea-31b0-9185-f16ea704c7a6 | -8.235 | -61.513199 | 2024-09-26 01:50:22 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 50e91ec5-59b2-3695-be80-efe52c5be778 | -8.1965 | -61.392899 | 2024-09-26 01:50:22 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8e1523eb-4085-3e88-bb25-86f8da9da6b9 | -8.1983 | -61.4006 | 2024-09-26 01:50:22 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c2e66b70-07f3-3149-9e42-c8183ec6ee10 | -8.2199 | -61.492599 | 2024-09-26 01:50:22 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 16beb1ba-c684-3ab8-b78a-f8539aa77fc8 | -8.2216 | -61.500198 | 2024-09-26 01:50:22 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 59a7133f-3bed-3ffb-bae2-d4d6c6ebe14e | -8.2234 | -61.5079 | 2024-09-26 01:50:22 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 63406b67-3f9c-358d-a520-f77084ec289e | -9.1374 | -65.553497 | 2024-09-26 01:50:22 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 941061cb-306e-37f5-8685-191ef4228460 | -9.1391 | -65.560898 | 2024-09-26 01:50:22 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5e7eb8e5-5bda-32d0-aaa4-daa1e9cda087 | -9.1407 | -65.568398 | 2024-09-26 01:50:22 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0f8a2c4b-a7a5-3af1-bee1-19009c58116f | -8.1515 | -61.288898 | 2024-09-26 01:50:22 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 886267c7-3d49-3ed8-ac0a-04794610e04a | -8.1533 | -61.2967 | 2024-09-26 01:50:22 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d9691299-ddec-3551-9252-8a58764ff088 | -8.1752 | -61.389702 | 2024-09-26 01:50:22 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 96f8264f-7053-3ad6-99fe-79a5812acca8 | -8.177 | -61.3974 | 2024-09-26 01:50:22 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 885d76d4-1d69-3097-a11a-215c020ae403 | -8.138 | -61.2756 | 2024-09-26 01:50:23 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| df040acb-01c1-37ee-8978-be70a9ba95f7 | -8.1398 | -61.283401 | 2024-09-26 01:50:23 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| edb5174b-0836-3fe7-bd09-91a89c104bab | -8.1417 | -61.291199 | 2024-09-26 01:50:23 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 550a9af1-9063-3390-aefc-6a3bf450b22e | -8.1635 | -61.384201 | 2024-09-26 01:50:23 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 671d4aa1-6a4d-3cbc-9ee5-0af1cf611080 | -8.1654 | -61.391998 | 2024-09-26 01:50:23 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a08ae293-1226-3171-9c8a-3c3b70c2e560 | -8.1672 | -61.3997 | 2024-09-26 01:50:23 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 52dc63ba-b72b-3689-8bb5-be9a969d03d8 | -9.8142 | -68.809402 | 2024-09-26 01:50:23 | METOP-C | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| bba54dfe-d16f-33fa-93f2-7df8973cb253 | -9.8045 | -68.811501 | 2024-09-26 01:50:23 | METOP-C | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| bd8e2fb9-7da9-32bb-a8cc-f26393b4723a | -8.1665 | -61.529202 | 2024-09-26 01:50:23 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0b6edfa3-c4a6-39fd-95ad-76e11d80c8c9 | -8.1683 | -61.5368 | 2024-09-26 01:50:23 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 29a167c6-0533-3c91-b282-04caeea9ee74 | -8.549 | -63.178398 | 2024-09-26 01:50:23 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1a4c1108-da49-3bbd-af62-da486f16ca4c | -8.1549 | -61.523899 | 2024-09-26 01:50:23 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 76d5065e-8086-3157-913f-a5031ef166b8 | -8.1567 | -61.531502 | 2024-09-26 01:50:23 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e6288b59-688c-3f56-90ba-2973f2b40fa4 | -8.0872 | -61.279301 | 2024-09-26 01:50:23 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6a3d57a9-c716-316c-b663-449c45a3b6c1 | -8.0714 | -61.2994 | 2024-09-26 01:50:24 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a362166-96e1-3e61-8604-579f42856646 | -9.2559 | -66.554901 | 2024-09-26 01:50:24 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 22bd3e8a-a7d1-3985-bb76-546ec281d4f8 | -9.2577 | -66.563103 | 2024-09-26 01:50:24 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c111de29-502c-3e89-a56a-5bb1efbfbc1b | -7.895 | -61.471401 | 2024-09-26 01:50:27 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1821f683-bd08-3ffe-b7c8-51b571228af0 | -7.8542 | -61.3419 | 2024-09-26 01:50:27 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b349ade2-dc2f-38d7-b1c8-47c6489a3360 | -7.7343 | -61.0951 | 2024-09-26 01:50:28 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bc0cfa7c-f0d3-37fc-9d80-625c340a8ef7 | -7.7362 | -61.1031 | 2024-09-26 01:50:28 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6aae0517-5dc3-3585-b736-8a86550cfd8c | -7.7864 | -61.316601 | 2024-09-26 01:50:28 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 28e5f42b-fafd-3575-9d1a-ff0891d62d4f | -7.7264 | -61.1054 | 2024-09-26 01:50:29 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b5e6a124-31b6-354d-bd7f-32e6f53b736a | -7.4035 | -59.787899 | 2024-09-26 01:50:29 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 23b2397a-dda3-3049-8d8f-591b50a01c50 | -7.5824 | -60.583401 | 2024-09-26 01:50:29 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bf76fd8c-6000-35c9-827b-d4f6f026d2b9 | -7.5845 | -60.5919 | 2024-09-26 01:50:29 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98a02824-a815-35a6-9ba1-c72f75213bec | -7.2691 | -59.484798 | 2024-09-26 01:50:30 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 66908f54-5a08-3c82-ba4e-36a4a29121d8 | -7.2714 | -59.494598 | 2024-09-26 01:50:30 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5c7894ef-b12a-3333-9ba9-d61baa84d07e | -7.3161 | -59.8974 | 2024-09-26 01:50:31 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ab0e664e-b941-39af-ab7c-2c8e3dc78bd7 | -7.4109 | -60.2953 | 2024-09-26 01:50:31 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aa45c08a-f1e8-3a4d-ae52-bf1125e758b8 | -7.6278 | -61.212502 | 2024-09-26 01:50:31 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c51eecb3-672b-36a7-8b4a-523ce68d1366 | -7.6296 | -61.220402 | 2024-09-26 01:50:31 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8c6b3bb7-0510-33c3-9232-4206899fe216 | -7.3064 | -59.8997 | 2024-09-26 01:50:31 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 64d34f7a-93dd-30a7-946c-4439cf9b9ccb | -7.4358 | -60.617901 | 2024-09-26 01:50:31 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5879df34-1680-385e-8f34-3ac75a310e12 | -8.9314 | -67.181099 | 2024-09-26 01:50:31 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ce4bd437-0f6b-3281-9abf-e5943f083999 | -7.0944 | -59.2299 | 2024-09-26 01:50:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 193d99a1-e897-376a-8d3e-866d4474922b | -7.0968 | -59.240101 | 2024-09-26 01:50:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8de752d7-e760-3a5c-8941-ee36dbb70232 | -8.9216 | -67.183197 | 2024-09-26 01:50:32 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2902a9fd-58e1-3468-b36f-de5ebaeb1397 | -9.141 | -68.194504 | 2024-09-26 01:50:32 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 047f857a-5628-3680-8eac-4ada981bf91a | -9.1431 | -68.204399 | 2024-09-26 01:50:32 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a54acf4b-8a92-312d-9dcc-f67625c2dcf9 | -7.0846 | -59.232201 | 2024-09-26 01:50:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f4db415d-1472-3129-9ac4-5b955560f36a | -7.0871 | -59.242401 | 2024-09-26 01:50:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5e7ce513-392a-3b76-ad54-c425b941dbc5 | -7.9579 | -62.939701 | 2024-09-26 01:50:32 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 01c09030-e21d-31b3-b135-096da1251007 | -7.1257 | -59.445999 | 2024-09-26 01:50:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2fb33ff8-8dad-36d3-9044-d203cc9fb21e | -7.1159 | -59.448399 | 2024-09-26 01:50:32 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6ddce768-9fdc-387a-890a-6175676c4f6a | -7.9055 | -62.981098 | 2024-09-26 01:50:33 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d96b3b6-f97c-3fba-9414-77facc422e63 | -7.5202 | -61.501701 | 2024-09-26 01:50:33 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 69ba1400-86f3-39ef-beff-695658ac2b01 | -7.2481 | -60.653 | 2024-09-26 01:50:35 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 34161861-0d47-3bb5-8fa1-2897ec1f3c3b | -7.2501 | -60.661499 | 2024-09-26 01:50:35 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 26848476-2feb-3283-ab0a-35436d69abd2 | -6.988 | -59.603401 | 2024-09-26 01:50:35 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a08eb067-92aa-3e78-a19e-08dc80a9dd52 | -6.9903 | -59.613098 | 2024-09-26 01:50:35 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ea26dda-e569-33ff-9047-1f9f356984d9 | -8.6867 | -67.000999 | 2024-09-26 01:50:35 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b8a0c07b-0086-3857-8db0-5c79758a3cda | -8.6886 | -67.009399 | 2024-09-26 01:50:35 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dde189ae-e565-335d-9c2c-e994949cb265 | -7.2227 | -60.676899 | 2024-09-26 01:50:35 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README41.md)
