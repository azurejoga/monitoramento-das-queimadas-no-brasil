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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03e2afaa-2ad2-3957-9561-6dd2e776d061 | -7.6169 | -49.9439 | 2026-09-03 13:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| f1dcb662-faa0-399f-8881-268c0a911e39 | -5.3264 | -60.143 | 2026-09-03 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 7e096368-cc90-3d49-b5cc-39b7a68101f8 | -8.4675 | -54.6631 | 2026-09-03 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 128.3 |
| dfdd81a8-1a68-381e-801c-94482739c858 | -10.8046 | -50.5046 | 2026-09-03 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 6ceb2961-3f7a-3128-933d-025e65ccd4f1 | -10.5254 | -50.1709 | 2026-09-03 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| c8d7ea97-b34a-3a63-a05e-995151059ed8 | -10.3007 | -50.023 | 2026-09-03 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 4b2045d6-dea5-3653-a316-603241ae9a8d | -6.6883 | -59.9436 | 2026-09-03 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 61b9a4e2-d669-3b47-9fb3-af76b4ba7a93 | -11.277 | -50.5815 | 2026-09-03 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| cd87d998-e75e-3632-af5a-ad5b7095f1a2 | -10.2815 | -50.0464 | 2026-09-03 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| d7b568b9-1b03-3ec3-a09e-6e5d5f1c0cdc | -11.6577 | -50.5175 | 2026-09-03 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 2b221bd3-7fea-3640-8779-5004998ceb07 | -12.0553 | -47.0966 | 2026-09-03 13:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| b16b05e2-14eb-3d49-867a-43d0c37d45a9 | -10.2212 | -50.3303 | 2026-09-03 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| dd06b43c-e83f-3f5f-b7d4-08f2a3526db2 | -11.6767 | -50.5153 | 2026-09-03 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 7c02b10c-d08f-394e-85e6-c2fecff1723d | -11.5825 | -50.4618 | 2026-09-03 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 2a905cd2-ed43-3700-bc20-94f660e6b4f9 | -11.5634 | -50.464 | 2026-09-03 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| e9575bd6-0d68-3bf6-a417-30e327dc982a | -8.7819 | -46.4399 | 2026-09-03 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 6a106b6c-4f2b-31c1-9792-dcdbe2a5a7de | -8.7631 | -46.4418 | 2026-09-03 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| b7e1427a-edff-3d17-968a-16bcbce941f9 | -1.4752 | -54.8157 | 2026-09-03 13:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 890cb5f3-1350-373f-ae53-433a3b37df2d | -7.9611 | -44.275 | 2026-09-03 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 5f5134e9-8c1f-3fb7-b6cb-3683d871bbb6 | -13.3625 | -51.359 | 2026-09-03 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 765b234b-bfa8-3abf-be2e-39cde183a521 | -10.6964 | -46.242 | 2026-09-03 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 0b107aed-9e34-3ecc-900c-53e800d305dd | -12.3626 | -48.1459 | 2026-09-03 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 7cd6bb68-1bef-361b-91b7-93937a107eda | -7.9608 | -44.2981 | 2026-09-03 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 469a2b40-1c97-38da-bef0-65c3dec42f0a | -5.3264 | -60.143 | 2026-09-03 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 506bf1c5-7c26-3305-809a-7883ec6011a7 | -8.4675 | -54.6631 | 2026-09-03 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 135.0 |
| cc1b89b2-0969-3ce5-bd83-e96080a22d82 | -7.6169 | -49.9439 | 2026-09-03 13:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| e8649fab-c04a-3bdd-b54b-bcf0de7ea01f | -10.3959 | -49.9703 | 2026-09-03 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 7dd3d08a-5a4b-3e69-8718-2fd7a80b2b6e | -6.6541 | -59.4452 | 2026-09-03 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 99697910-694a-30e4-bdc6-821dc421235d | -10.9391 | -45.3457 | 2026-09-03 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 218.8 |
| cf10f0ee-4466-3413-b82c-86cc36852771 | -8.4481 | -54.7452 | 2026-09-03 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 184.2 |
| 01d7706e-7955-3a81-98c5-a863f90d4e12 | -12.1462 | -44.1725 | 2026-09-03 13:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| cb61a9ba-6f5e-34c2-a6b8-a1b25c11699f | -12.1457 | -44.196 | 2026-09-03 13:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| d95ff4ff-557d-38db-9837-904947cc7c6f | -3.6215 | -60.566 | 2026-09-03 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| a84ab2ef-6980-3df5-96cc-2474f5884401 | -11.5825 | -50.4618 | 2026-09-03 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 2cbdf5d8-302e-35a7-82ee-be21fe7300f1 | -7.8068 | -47.8591 | 2026-09-03 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 571d372d-b1cb-3085-9a02-1e51c0c8636e | -8.4673 | -54.6833 | 2026-09-03 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| b042cb1e-6ee7-3a33-a3c3-047054b95942 | -8.9598 | -44.4204 | 2026-09-03 13:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| cd42011e-0bda-3687-8537-006dfbcd6d9c | -12.0557 | -47.0741 | 2026-09-03 13:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 6d34065a-7f3d-311e-9325-633a3987085a | -12.1269 | -44.1755 | 2026-09-03 13:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| a3f1e8db-a7da-364d-8c8c-8ad20064292b | -8.4677 | -54.6429 | 2026-09-03 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 153.6 |
| 131491b9-aee8-3b6c-a548-a59acf58b054 | -5.5098 | -60.1947 | 2026-09-03 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| d7694a70-f00f-35be-80f6-77d97f4bcbb9 | -11.0057 | -49.6677 | 2026-09-03 13:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| f19d0f3e-2611-3f42-be1b-565a2ed47ea5 | -8.4483 | -54.725 | 2026-09-03 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 63cf9270-5217-390b-89b6-585f843e534f | -7.1187 | -42.2264 | 2026-09-03 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 72.2 |
| 9daa49c5-5dd0-327b-9885-bdaf5055912b | -11.1634 | -50.5727 | 2026-09-03 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| a0213713-7827-30dc-b77a-ce5f0cccb5c2 | -7.6149 | -44.8833 | 2026-09-03 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 7da4d7e5-98f4-3e9e-916b-98fec19011e9 | -7.998 | -44.3405 | 2026-09-03 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| b9a982a2-8f0c-377c-8008-5e4caa1ee907 | -13.3817 | -51.3566 | 2026-09-03 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 4b40d781-7f72-3f78-a0b5-9c961fa7c82d | -11.006 | -49.6461 | 2026-09-03 13:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 95d45624-b39a-3fe3-9237-92d52c6b52ef | -7.9419 | -44.3001 | 2026-09-03 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 6be06382-2432-3fb2-a31d-af2655310435 | -12.0553 | -47.0966 | 2026-09-03 13:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 06d72036-8166-36c4-aaab-8e9c9ea9722b | -10.7154 | -46.2395 | 2026-09-03 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 4b3a90a6-b7e3-3029-ac03-6bdb38e16ff0 | -1.4752 | -54.8157 | 2026-09-03 13:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 6f66e4a9-8396-310b-b94e-3562fda93ea9 | -12.1265 | -44.199 | 2026-09-03 13:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| bdcd332c-6205-3c8b-a774-b1d6d8afb531 | -12.132 | -47.086 | 2026-09-03 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| a1f9a08d-5b6e-3aca-883e-e98e80465591 | -12.0749 | -47.0715 | 2026-09-03 13:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 8a3975fe-c0e0-33b0-9304-34b196018eca | -7.9605 | -44.3212 | 2026-09-03 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 604205de-7546-3b80-8c9f-edefc71ac5a1 | -10.9009 | -45.3509 | 2026-09-03 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| b45c118b-cea6-3798-b43c-e7005a516f39 | -11.2879 | -54.0317 | 2026-09-03 13:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| f4f4299e-f4c0-3107-859b-f0b739963274 | -6.6883 | -59.9436 | 2026-09-03 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 105.1 |
| c4311f7b-0fb5-3399-afdd-02abaeba4d40 | -10.7158 | -46.2169 | 2026-09-03 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 4f79c308-02e2-32c5-9397-0994853427d4 | -10.92 | -45.3483 | 2026-09-03 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 334.8 |
| 579d2f4c-48f9-349d-a06b-aaa61cc9fd19 | -13.3813 | -51.378 | 2026-09-03 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 8709c0e5-836f-3d60-aecd-17bbc7153a77 | -11.2106 | -51.2688 | 2026-09-03 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 08a9d8fe-13d0-3911-bbe1-4900c21c01cc | -11.1824 | -50.5706 | 2026-09-03 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 60ea122c-ce75-3e20-8ec7-aa569a83440d | -10.6967 | -46.2193 | 2026-09-03 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| fbefdc44-0207-3170-910f-58f98068092b | -13.3625 | -51.359 | 2026-09-03 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 8c760a67-1a9e-30ed-9356-fd9a56711eea | -1.8019 | -47.9586 | 2026-09-03 13:40:00 | GOES-19 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 48cec3ae-db9a-3458-b923-1b83bfa4c66c | -11.5086 | -50.3204 | 2026-09-03 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 90620fae-aba6-37e4-94aa-9fb6ea53f48e | -8.7853 | -54.5808 | 2026-09-03 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 129ba16a-06bb-3b94-a9c6-14ce307bff87 | -11.5634 | -50.464 | 2026-09-03 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 80e723b1-c5c1-38b2-b213-9d2632cf2db0 | -10.8822 | -45.3305 | 2026-09-03 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| e24bf169-dc6a-302d-95ee-be4f8d965536 | -10.3205 | -49.9567 | 2026-09-03 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 4d49bca3-9ae0-3ff2-bba2-d00cf88dd4db | -11.1634 | -50.5727 | 2026-09-03 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| fe34fe46-b620-3a26-bef9-b288394be910 | -10.8631 | -45.333 | 2026-09-03 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 65ab3fde-0583-3ad6-a4e8-fe620ca351aa | -8.502 | -44.7475 | 2026-09-03 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| ea6a0406-8b85-3401-8ff1-a1334d67f168 | -10.6964 | -46.242 | 2026-09-03 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 910e438b-81fc-3d54-a907-47a32e262a91 | -7.6169 | -49.9439 | 2026-09-03 13:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 80fa9514-34f5-3edc-a99b-0517afee5b77 | -7.6144 | -44.929 | 2026-09-03 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 7d58617e-48ea-31b5-9c10-f03c8a8a89b6 | -12.0553 | -47.0966 | 2026-09-03 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| ea0b49a9-17cb-3877-8af7-b6fdcea2795f | -11.3056 | -45.1113 | 2026-09-03 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 88933c4e-e46d-31f5-90d9-fe90b4e2107b | -11.2474 | -45.1655 | 2026-09-03 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.1 |
| b70ca78b-f0c0-31ab-9533-2753b512175d | -10.7428 | -50.8727 | 2026-09-03 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 68b66ee9-0c18-3fc3-a531-ab6e872b193c | -12.1265 | -44.199 | 2026-09-03 13:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 249.4 |
| 8f2d4851-e7a4-309e-bf35-3c4b1f6f5cb4 | -10.8826 | -45.3075 | 2026-09-03 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 34ff9775-14dd-3766-a6e9-0faf84894e81 | -13.3817 | -51.3566 | 2026-09-03 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 83e46d64-811f-31b9-baf5-3002d52dfd6c | -3.2455 | -47.9187 | 2026-09-03 13:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 946e31ff-40c7-341c-96ac-277cdf879df9 | -13.3625 | -51.359 | 2026-09-03 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 68f3b032-5ccc-3896-8cb4-e5132f6f9095 | -10.3956 | -49.9918 | 2026-09-03 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| bd6e8b4a-0fe4-3dba-bc57-cb8562d3e5bf | -11.2282 | -45.1682 | 2026-09-03 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 71f87225-7d0b-3d6d-a823-7574743467d4 | -10.696 | -46.2646 | 2026-09-03 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 44d68f26-71d1-3949-a2d5-6966e595ef82 | -1.5128 | -54.2561 | 2026-09-03 13:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 23033836-546c-3360-af24-2980b8432307 | -8.4046 | -44.9869 | 2026-09-03 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 4be1c084-540f-3a6c-8a1c-97014422a1f8 | -11.0057 | -49.6677 | 2026-09-03 13:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 04e54505-7415-3de1-91d2-159dc3ee8992 | -5.5098 | -60.1947 | 2026-09-03 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| f3421e23-eee7-3dd1-83c0-9cd61632692d | -6.6698 | -59.9443 | 2026-09-03 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| bab701d1-feb1-3ab8-b229-b82f0fb96a4b | -7.2255 | -42.7616 | 2026-09-03 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 55.2 |
| 84e4011e-594a-3b72-9c83-6cbe5c247121 | -7.6171 | -49.9226 | 2026-09-03 13:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 2d8f8aad-a007-35e3-8432-c47b2e0a85a5 | -8.4481 | -54.7452 | 2026-09-03 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 187.2 |
| b0cdb458-8de6-3313-b2bc-7bd19c39177a | -11.006 | -49.6461 | 2026-09-03 13:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |


[Clique aqui para ver as próximas entradas](README58.md)
