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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53a3d1e7-2fe3-3abe-954f-42efa26da5b8 | -3.3552 | -44.4255 | 2025-11-17 13:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 98bbb458-93f7-3855-a6af-34bc35a82a02 | -8.3046 | -43.961 | 2025-11-17 13:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 159.1 |
| b0af633f-d930-340f-a0f2-ae2347d1361a | -5.3442 | -43.0402 | 2025-11-17 13:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 1b6563ae-b867-30ce-b10f-d6a000187300 | -3.6701 | -44.7303 | 2025-11-17 13:30:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 950a58f1-5a2e-3089-8791-dcb7d2e4311b | -7.7135 | -42.9478 | 2025-11-17 13:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| 97853446-15e7-36e3-b373-b50ebba04bfe | -5.3254 | -43.0415 | 2025-11-17 13:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 9b1000ac-894f-3e1f-953e-f91c00517e60 | -6.1791 | -48.0712 | 2025-11-17 13:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 19a1d174-fdb7-33bb-84b8-b34473172e17 | -9.6232 | -44.3876 | 2025-11-17 13:30:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 6cb162d5-b595-3a93-8a4b-a4f8174c9f18 | -3.8102 | -40.1418 | 2025-11-17 13:30:00 | GOES-19 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 104.5 |
| ffc102f0-575b-3fea-82d4-7c196f954127 | -8.3016 | -44.1931 | 2025-11-17 13:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 173.4 |
| a5a63d4c-cf41-3faf-b57a-bf45dc3148da | -8.3202 | -44.2142 | 2025-11-17 13:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 8b0d83fa-1a87-3f78-baf0-a447920d4de3 | -10.2813 | -39.1579 | 2025-11-17 13:30:00 | GOES-19 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 98.0 |
| 12fd2e05-5bf1-3412-9657-c74a665a3e48 | -8.3049 | -43.9377 | 2025-11-17 13:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 237.5 |
| 4b4b38c5-592f-31f4-88ed-651a615317f2 | -3.9895 | -44.2813 | 2025-11-17 13:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 337bc4fc-e942-34bb-aa0f-6933467c0cf0 | -9.6236 | -44.3644 | 2025-11-17 13:30:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 4e3dda74-5b51-3210-83ff-2e65767afeeb | -7.442 | -45.2184 | 2025-11-17 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 1285b2a7-a2a1-306e-a52e-0403e46173f1 | -3.2116 | -43.3726 | 2025-11-17 13:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| a895fd48-f31b-3667-8093-b4dfe23b8cc5 | -9.4645 | -44.868 | 2025-11-17 13:30:00 | GOES-19 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 139.7 |
| e7794b60-5691-3fa8-b361-bcb65ca534cf | -10.4327 | -42.5374 | 2025-11-17 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 73.8 |
| 8acd1d44-6d98-3075-934d-59b8631c6844 | -6.1789 | -48.0929 | 2025-11-17 13:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 754cf830-142f-3734-a0dd-4d255db5c43f | -9.0217 | -45.4217 | 2025-11-17 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 66aa28ec-80ce-3023-b039-dce1d0c44ed0 | -8.0386 | -48.9467 | 2025-11-17 13:40:00 | GOES-19 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 79.9 |
| a4add67b-6c3b-3c68-bb96-09941a2bf609 | -8.283 | -44.1719 | 2025-11-17 13:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 80f8c438-f85c-38c3-a482-b30f7d217eeb | -8.3049 | -43.9377 | 2025-11-17 13:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 153.7 |
| de611613-3739-3898-aad4-3393036f0779 | -9.6236 | -44.3644 | 2025-11-17 13:40:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| fd581894-72d1-3b4a-923d-b0f023245c0e | -9.6232 | -44.3876 | 2025-11-17 13:40:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| fc4f8e3c-d426-376b-a52a-a73d3dab556f | -2.4015 | -45.7243 | 2025-11-17 13:40:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 6f735cda-a520-3f7a-96a3-31f16056d01e | -10.0917 | -44.7907 | 2025-11-17 13:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 2cdcc373-3d22-3b68-a77a-df611ecadd1b | -6.1791 | -48.0712 | 2025-11-17 13:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 480388a1-2af8-353e-bf13-dec1a197cf2d | -10.092 | -44.7676 | 2025-11-17 13:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 128.6 |
| e7c14002-0fb0-3b8d-80a4-14756483dc4d | -3.6701 | -44.7303 | 2025-11-17 13:40:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 0168fd3a-6178-375b-ac5b-4c8b8a45500c | -3.2116 | -43.3726 | 2025-11-17 13:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 24a10da8-8cf7-3b02-ba28-f4688a5053ff | -8.3016 | -44.1931 | 2025-11-17 13:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 4c04446e-c6dc-3037-9bbe-89b877b8a6cc | -9.2088 | -45.5599 | 2025-11-17 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| ea679816-634c-3d2f-bf47-e585cc2f743e | -8.3019 | -44.1699 | 2025-11-17 13:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| a34c8d88-2cd4-33b2-bbb2-b7642d87325f | -3.2117 | -43.3494 | 2025-11-17 13:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 47381fe4-682e-3d93-9d92-d552f4743408 | -7.442 | -45.2184 | 2025-11-17 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| dbd7931d-e529-37c0-8b6e-96a3cb3823e7 | -3.5833 | -43.6108 | 2025-11-17 13:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| ebaf432f-e064-34a7-880e-927e1655f5fd | -6.3516 | -41.7494 | 2025-11-17 13:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 69.7 |
| c3d2bfb8-91b6-36d4-8e93-f168ed90fd97 | -6.7013 | -40.7962 | 2025-11-17 13:40:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 83f90d09-e112-3ecd-8c35-ddf0dc94ba3b | -5.3442 | -43.0402 | 2025-11-17 13:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 6bad08fb-9a69-3f91-8931-5f360bc6b4a8 | -8.5844 | -45.6729 | 2025-11-17 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 2345dd72-fbc9-37aa-a0c3-1d30c524566c | -6.1789 | -48.0929 | 2025-11-17 13:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 217910fb-0cbf-3b04-934f-1def3e39adc8 | -3.8102 | -40.1418 | 2025-11-17 13:40:00 | GOES-19 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 119.2 |
| 77a9e925-021c-3c79-8c02-6d2e4c53c339 | -6.1973 | -48.1134 | 2025-11-17 13:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 57.8 |
| c60a2707-a9d8-3b12-a8ae-1c86fade7e3c | -3.6019 | -43.6099 | 2025-11-17 13:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 155.7 |
| ae16beac-d9f4-3ee8-8170-a70f5134c7de | -2.4201 | -45.7015 | 2025-11-17 13:40:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 9f08882a-a2bf-3835-841f-a970d7bf76a5 | -8.3202 | -44.2142 | 2025-11-17 13:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 61d4f2e8-38bb-3141-aa99-7f66aeb41b51 | -7.9714 | -50.0013 | 2025-11-17 13:40:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| e99f4b21-b88d-3491-af34-4782231e1fe1 | -3.7293 | -44.1568 | 2025-11-17 13:40:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 5390903c-9e88-373a-98af-f28e890da980 | -6.3328 | -41.7511 | 2025-11-17 13:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 52.9 |
| babd7c90-cf7c-3039-adca-ff87c201f4ee | -7.7135 | -42.9478 | 2025-11-17 13:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 60.1 |
| 9d3a0d43-5272-34ea-9965-2afac6cd068a | -5.3254 | -43.0415 | 2025-11-17 13:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 99d82056-07c0-319b-b219-26083844c172 | -8.3046 | -43.961 | 2025-11-17 13:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 239e8a40-9352-3ac6-bf29-3af725212404 | -5.7467 | -46.2755 | 2025-11-17 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 38ca8b2c-b5d4-3ea6-b446-4ebeb7d86b75 | -7.6237 | -42.5788 | 2025-11-17 13:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 8816276f-a3cc-309d-a44e-eeeccfbaa12d | -3.9895 | -44.2813 | 2025-11-17 13:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 70cce9c4-5ccb-3005-a226-2617a677e44b | -9.9972 | -44.7566 | 2025-11-17 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 93c13b06-49fc-312d-ac50-185529775eea | -10.092 | -44.7676 | 2025-11-17 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 8d734125-2ad0-31c3-9f3b-c3b24db12947 | -9.6236 | -44.3644 | 2025-11-17 13:50:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 75fef7d9-3a46-3fd3-a6c0-78bede1cc5be | -5.7614 | -42.5142 | 2025-11-17 13:50:00 | GOES-19 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 150.9 |
| c58b5ee0-9e4d-3694-bc7d-52c8c2d476f0 | -5.0401 | -37.0597 | 2025-11-17 13:50:00 | GOES-19 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 111.2 |
| 723e17c8-5b8f-3dcc-a73a-fd0d2181cd00 | -3.7293 | -44.1568 | 2025-11-17 13:50:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 6c0dee43-3879-3e3f-9b93-7952049bc0f6 | -8.3019 | -44.1699 | 2025-11-17 13:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 111.9 |
| af403db1-3d35-311a-ae96-7fb0549f1402 | -4.4816 | -40.7365 | 2025-11-17 13:50:00 | GOES-19 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 135.4 |
| 7e5fe84d-2d93-3107-8d98-0966694d8d13 | -3.5239 | -44.2351 | 2025-11-17 13:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 55510b03-f0a7-30ad-8ce0-b4c0d13666e3 | -3.9895 | -44.2813 | 2025-11-17 13:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| e536767c-3b1a-3cd3-89b5-582fa5df86d3 | -10.1111 | -44.7652 | 2025-11-17 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 112.0 |
| ae79309f-836b-39e1-863a-10760e42c9d5 | -3.6019 | -43.6099 | 2025-11-17 13:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 159.2 |
| c80ab9e2-09a0-37bf-b966-03a73c3a793d | -5.7467 | -46.2755 | 2025-11-17 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| f3b82d79-0528-3294-b1a0-25ad7a80a0db | -9.9567 | -44.9228 | 2025-11-17 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 2e9be6fe-df80-33b1-ac32-f127be0ce44f | -10.6464 | -44.6022 | 2025-11-17 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| c8846481-067a-3343-8e80-52f9329ff884 | -5.3442 | -43.0402 | 2025-11-17 13:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 28a727d9-5b9b-36d3-936f-a984b813d6a7 | -4.3434 | -44.354 | 2025-11-17 13:50:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 0b0fe004-00b1-3ab2-b3fa-3e3519fc6d70 | -8.3049 | -43.9377 | 2025-11-17 13:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 275.4 |
| fec32747-dea3-3c36-8f07-e5da18ea8afb | -3.2117 | -43.3494 | 2025-11-17 13:50:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 652d1590-43cd-3569-a2c2-7a7b629a8c8f | -9.6232 | -44.3876 | 2025-11-17 13:50:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| dbcbebbf-5767-38a4-8a52-1ec8e73e548d | -3.3414 | -43.5061 | 2025-11-17 13:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 6a8bec41-b98d-39f6-acfb-2d8ef5bbe6f4 | -3.2116 | -43.3726 | 2025-11-17 13:50:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 726ee689-a841-398c-a3bd-615a9915fd00 | -8.3046 | -43.961 | 2025-11-17 13:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 191.5 |
| f224645d-608f-3692-98a6-d1bfa760092e | -6.3516 | -41.7494 | 2025-11-17 13:50:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| 29890939-e0fc-3c5d-a039-8fbc514c716e | -5.3254 | -43.0415 | 2025-11-17 13:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 78e60ac7-98b3-356e-b2a2-fa5e26481d37 | -6.6873 | -42.0535 | 2025-11-17 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 57.9 |
| b472f86c-b8da-34bf-88ad-e22105357a54 | -3.6701 | -44.7303 | 2025-11-17 13:50:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 7fbdad23-8fd8-3dab-96ac-d12298f40d3f | -3.3552 | -44.4255 | 2025-11-17 13:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| d0e2841b-5965-395f-b6de-74934d75100c | -3.8102 | -40.1418 | 2025-11-17 13:50:00 | GOES-19 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 112.2 |
| ea05814b-80f5-3219-b87a-1931620510ce | -9.9754 | -44.9435 | 2025-11-17 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| e21d3056-03b4-3a90-a742-b0fe41b81433 | -7.491 | -45.8693 | 2025-11-17 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| b9bf5696-05cf-3344-a421-06c74c78dadd | -3.9897 | -44.2584 | 2025-11-17 13:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| b3c17797-ae66-38d5-9a6b-8c9c86e09877 | -6.1791 | -48.0712 | 2025-11-17 13:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| a0f210ef-9fa4-3b5b-977b-967ca1590775 | -9.0211 | -45.4672 | 2025-11-17 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 153.1 |
| a6589e76-04fc-3975-b81d-575af210a229 | -11.4136 | -43.32 | 2025-11-17 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 05ee74c2-e077-3834-80d7-34d36f012456 | -7.7135 | -42.9478 | 2025-11-17 13:50:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 79.0 |
| a7fe6135-035e-306c-9393-509361dd9f5f | -7.8653 | -42.8845 | 2025-11-17 13:50:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 55.4 |
| fea9d201-b57e-3448-8080-ebc0e6606ffc | -8.0573 | -45.6583 | 2025-11-17 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 2f2bed17-3fd9-3504-8cf3-ad9dc925a100 | -7.094 | -42.7272 | 2025-11-17 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 60.9 |
| d35de8a8-2c9b-31e5-9378-3beb42470581 | -7.0429 | -42.2577 | 2025-11-17 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 60.1 |
| 6aba8816-3d0f-39b0-b3e3-755a4f4e6a3c | -8.0386 | -48.9467 | 2025-11-17 13:50:00 | GOES-19 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 105.6 |
| f6c7d039-41ef-3bce-a510-e78dc870f8cd | -7.8842 | -42.8825 | 2025-11-17 13:50:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 79.7 |
| d46c51d8-5dc3-3126-a65c-4b011336f149 | -9.9779 | -44.7821 | 2025-11-17 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 303.7 |


[Clique aqui para ver as próximas entradas](README55.md)
