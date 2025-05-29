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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c77e32a-c35c-3a85-9af8-2e16b4699eb1 | -8.01892 | -49.68466 | 2025-05-29 03:49:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 212d2bc2-2f78-32e5-97b8-51e4e71e2d7e | -5.64329 | -43.59054 | 2025-05-29 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a80ee47b-50c2-3bee-951f-834e638414f1 | -4.8152 | -47.32351 | 2025-05-29 03:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bcd2a67-013f-3aef-ac39-fd9d05efe494 | -7.6719 | -46.09787 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 80e45215-f9f9-392a-81cf-6273d8dc3531 | -7.62095 | -45.751 | 2025-05-29 03:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0012653a-7328-3218-8469-1b29201c80b6 | -7.46794 | -47.05631 | 2025-05-29 03:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa5312ef-5a7b-3709-8175-f21658169184 | -7.67624 | -46.09524 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1ea8f963-d00a-3d37-be60-9317434629f6 | -8.07344 | -34.97585 | 2025-05-29 03:49:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fb7be353-07f7-37ba-a5bb-ba98f5d050ce | -7.07189 | -44.92396 | 2025-05-29 03:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e96d3a1f-c907-374a-9991-16b37a7e14d4 | -7.67038 | -46.09752 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e831dfa-c981-37aa-a630-163df4f543a4 | -5.6441 | -43.58585 | 2025-05-29 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 907c2f11-8689-38ff-b2a2-414ebc55aa65 | -7.23093 | -43.09389 | 2025-05-29 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b46e0d93-5fc0-331c-854e-2894d9142e94 | -7.6364 | -45.93184 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da2172cd-2862-3a36-882d-5e3e650f0a31 | -3.2891 | -43.46637 | 2025-05-29 03:49:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0204e25d-4d55-32a2-a1f9-1bbb8bf7edbd | -5.2073 | -43.31713 | 2025-05-29 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a35a986b-c091-30dd-9933-309e0caa665a | -7.68031 | -46.10275 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3c1364e-b6d4-3453-a9fc-ee3fefe53998 | -6.82665 | -44.6523 | 2025-05-29 03:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0b93d0e5-e813-335f-b338-b27669472618 | -8.75023 | -49.76646 | 2025-05-29 03:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d3c3f40-d795-39f6-b0da-58847c52815c | -7.67302 | -46.09144 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e54bccc-772f-3a33-893b-bc7b60d9cd23 | -6.55954 | -44.49195 | 2025-05-29 03:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ed07cc3-b4f4-3ca3-939c-24e4780fd9f9 | -6.33812 | -43.3705 | 2025-05-29 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a89f2751-e4c5-348b-8951-1865c649bd8e | -7.68091 | -46.09946 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d35cc713-9ce0-3062-9b84-e4a2f9282d12 | -8.01044 | -46.15331 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1327f999-bc96-392a-9be8-fb3d13f6404f | -8.89542 | -44.78144 | 2025-05-29 03:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8a5c314c-ea64-3b43-87a1-02a19a26be7c | -7.54929 | -43.33781 | 2025-05-29 03:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 225f7038-0750-3771-ac7f-12f46238d5a4 | -7.58217 | -45.87233 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e58a897e-773a-332b-b718-af945a1dfbf4 | -5.76368 | -38.90509 | 2025-05-29 03:49:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c1bb33d9-d4a9-3c4c-9ef7-06b19557a04f | -5.20961 | -43.30331 | 2025-05-29 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed52e1dd-ca31-3024-a3ba-69857985ab70 | -7.67659 | -46.10213 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 00661b83-ab90-3f29-b7ed-581ae8abd83a | -7.55734 | -43.34351 | 2025-05-29 03:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2848f829-b71c-3820-825d-7197f4e23388 | -7.07488 | -44.93592 | 2025-05-29 03:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f03aaa0f-9013-3a45-8321-bae5a230e2e5 | -7.94996 | -44.86034 | 2025-05-29 03:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95a877a0-78e7-3bf5-84fd-4e6333fa2c2d | -7.57809 | -45.86502 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b67d5872-c388-3ae0-9fe5-3e95b0e5e96b | -7.57865 | -45.86182 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3cba1a3-5425-3392-875f-2c483ef57197 | -9.19976 | -49.47815 | 2025-05-29 03:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 92b22ea1-b66c-39f2-a298-9f2b510ca48b | -7.54639 | -43.35455 | 2025-05-29 03:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c4d3fee-196a-335f-94d5-a25ad50d2555 | -7.24375 | -43.1034 | 2025-05-29 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| dd0c1503-a4a9-30f4-9a7c-900147d275f4 | -7.6202 | -45.74691 | 2025-05-29 03:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3f6c56e-752f-3bac-94fb-9945cf9fa829 | -7.07586 | -44.93031 | 2025-05-29 03:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f74be7bb-278d-3b6e-a1af-1c41a90f4c4d | -7.66598 | -45.24846 | 2025-05-29 03:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e40d0e86-91db-3048-9e6a-234c9a3060fa | -7.19272 | -43.10867 | 2025-05-29 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 371da73d-56be-3781-9e6f-75a1ffc75e33 | -5.21417 | -43.30399 | 2025-05-29 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 974ee2a4-4160-347b-b9cc-95c5df18a7ff | -7.27813 | -44.22254 | 2025-05-29 03:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba772007-942c-3faf-b5cb-859da6eb92d8 | -6.82174 | -44.65177 | 2025-05-29 03:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f060d029-713a-3324-b667-6fd837d7e17d | -8.74263 | -49.77077 | 2025-05-29 03:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4f8f8d2-1007-3513-b904-9dca8118c102 | -7.18335 | -43.11122 | 2025-05-29 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7b79dfe1-d928-32ae-b6dc-4365ce62ea37 | -7.67565 | -46.09848 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 02fb0b25-acfe-30aa-9595-b940afe325e8 | -5.21873 | -43.30468 | 2025-05-29 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f8c4677a-91cb-36fa-b64b-3445136316ff | -7.67505 | -46.10175 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 660d4a53-3219-3262-9421-f34266c08303 | -7.57861 | -45.95375 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7cd38789-36e5-3ed2-a118-07661045ffe6 | -8.01785 | -49.69029 | 2025-05-29 03:49:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 606d4879-d522-3fe2-ade6-c2f4fe6ac54a | -8.79533 | -47.94102 | 2025-05-29 03:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3e1093a-bcbe-36c7-a7ab-facfadc3b879 | -6.23953 | -43.36877 | 2025-05-29 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46940891-1fe6-3e23-a8d1-efdca8befbcc | -7.57917 | -45.95058 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 605c8636-8df0-336e-a32b-01cd01a08353 | -8.78953 | -47.93979 | 2025-05-29 03:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3971e45d-430a-3439-b7be-bc95320b7c28 | -7.5566 | -43.32164 | 2025-05-29 03:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adaa1ba1-c46c-3604-97c2-357b266229d5 | -7.5877 | -45.96248 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e4eab48d-d3c1-3661-88f7-652fb763df2a | -7.67133 | -46.10112 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 92ccae83-2523-3715-be9d-a7198124eb68 | -7.62155 | -43.41443 | 2025-05-29 03:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec2b540d-3205-3c1a-9da7-42f3b9b01699 | -8.09834 | -46.28959 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6be6f4f2-9363-35cd-9e09-1caa5cd2a726 | -7.53687 | -43.33133 | 2025-05-29 03:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8964a4c2-89c6-3e53-af14-b36e39a79fb8 | -4.96016 | -37.93552 | 2025-05-29 03:49:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 15a2de96-5679-37cc-a68c-e2bc578ffc49 | -9.20702 | -49.47946 | 2025-05-29 03:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8f9b9bef-e64f-38f2-9026-4ff538b73c01 | -2.65731 | -48.79733 | 2025-05-29 03:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45f0ed6d-35ea-3bcb-90b4-fce8fe0bfada | -6.34181 | -43.37584 | 2025-05-29 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c8bb68bf-8c50-3736-ae38-98b1b2797ac4 | -5.28205 | -35.47955 | 2025-05-29 03:49:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e57951e2-86be-3d11-ae91-163dc5291766 | -9.39245 | -48.41806 | 2025-05-29 03:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c80aefe-45e2-3614-aada-3f06610af9f9 | -6.8525 | -44.83136 | 2025-05-29 03:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28aa0e73-0dad-303d-949d-626cbc5157fd | -8.66841 | -48.2894 | 2025-05-29 03:49:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 998a4f95-1137-3802-95a9-fa4d21bfbb1b | -8.6657 | -48.29095 | 2025-05-29 03:49:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18b39595-f64b-3cd3-9016-d1952dfc72c9 | -7.58829 | -45.95926 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aeb78f53-d105-3bd9-a1b3-5a0fb90b2a56 | -8.40261 | -47.09804 | 2025-05-29 03:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c458a5e-4f58-320f-aef5-de219cb2babe | -5.21796 | -43.30929 | 2025-05-29 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 489ad4fb-20e3-34dd-bc95-e9785f725340 | -7.9999 | -46.15152 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 347a0007-7168-32a9-a176-c9d9da464694 | -9.33107 | -36.76456 | 2025-05-29 03:49:00 | NPP-375D | ESTRELA DE ALAGOAS | ALAGOAS | Brasil | 2702553 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d84280a5-a5a7-3c5c-967c-ade7c913db0b | -7.0778 | -44.91921 | 2025-05-29 03:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| aa9c19e5-7524-34dc-b391-0f7ebfcdf2f1 | -6.33733 | -43.37505 | 2025-05-29 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f1f2186-6925-3624-ba9f-818fae01095d | -6.32093 | -43.37908 | 2025-05-29 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebd095b1-d440-3421-a34b-54155872632a | -6.34259 | -43.37133 | 2025-05-29 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 99c61eb4-1887-370a-bf25-3ca099e8ff0f | -7.54199 | -43.35386 | 2025-05-29 03:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c752b133-e01f-3263-bde2-9058b6fb5cf7 | -5.20884 | -43.30793 | 2025-05-29 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cc5888b-c4b5-31af-9cd0-839dcd77fa64 | -7.58305 | -45.95835 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0330c838-a216-39f2-a1a2-fb0bba680225 | -4.82251 | -44.35725 | 2025-05-29 03:49:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a1bcf51-05cb-3244-a726-cc56809b9758 | -4.816 | -47.31895 | 2025-05-29 03:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b80a07b9-d2a9-3749-8f95-f0194ad5993c | -7.67246 | -46.09464 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 34d906c5-b23f-3233-ba15-f97b9adeecd2 | -9.20804 | -49.47428 | 2025-05-29 03:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7ad88fea-0927-3623-a03b-2903c6be0af5 | -7.58328 | -45.95787 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c47f3fb4-64f5-36a9-a492-45af17608e3f | -4.81759 | -44.35645 | 2025-05-29 03:49:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fa353aa-af04-3b0a-a10e-16e36c5882bd | -6.91326 | -47.8591 | 2025-05-29 03:49:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d6087af-f66d-38eb-8c8f-fef35c9983a2 | -7.54052 | -43.36236 | 2025-05-29 03:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13e20f62-087d-37bb-bd92-ae7da79c585d | -5.30583 | -43.07185 | 2025-05-29 03:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6a18657-5714-39da-9493-42171d0bc97d | -6.24325 | -43.37402 | 2025-05-29 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9b402e8-6b08-39fa-9687-8884da597158 | -8.66925 | -48.28502 | 2025-05-29 03:49:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb48affc-85e0-3bea-a34a-65ca34f43126 | -7.63004 | -45.93728 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 33b8a402-2c7c-3f36-9f68-397be0d09bb8 | -7.67097 | -46.09431 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f11f0016-9413-3e3c-83dd-9474cc5ebab2 | -8.01546 | -46.21558 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c98e0c65-75c7-379f-9727-0ec4cf1bd916 | -6.22616 | -43.33921 | 2025-05-29 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4e219796-7588-35f7-a1ff-a386ae280dd2 | -5.05096 | -43.24614 | 2025-05-29 03:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 451d2d6d-fb37-328b-a182-faab7150dc18 | -8.4522 | -48.33025 | 2025-05-29 03:49:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f97cfe49-43ec-3a9e-b20f-bf1bd4430fd8 | -7.63583 | -45.93503 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README5.md)
