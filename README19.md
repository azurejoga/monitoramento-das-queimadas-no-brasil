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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3e95fa5-f0de-3cc4-bf3a-aa12d618ad2f | -4.63134 | -38.5653 | 2025-09-08 03:38:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e039124e-a2dc-3fd7-8764-123f3a95ec8c | -7.5696 | -43.6755 | 2025-09-08 03:38:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6233b53b-40a1-38d2-a91b-f842445df5d5 | -6.1436 | -44.23114 | 2025-09-08 03:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7e80f4e2-8ddc-3a02-9b65-b93ba979a386 | -5.41692 | -42.85886 | 2025-09-08 03:38:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a9d5d3cd-054d-3188-81fb-43131a6be92d | -6.60883 | -44.01402 | 2025-09-08 03:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82dfd236-d67f-3416-b145-3e5b71bc5539 | -7.97432 | -44.83998 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 294ccf64-cbd8-376d-b6ea-911b8e886595 | -4.90217 | -42.2127 | 2025-09-08 03:38:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e590b74b-e13d-3376-b8d4-ab1c6c7ce2a0 | -7.31559 | -39.15034 | 2025-09-08 03:38:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 06db60ae-2aa6-322f-8258-4a252dfec61c | -7.8256 | -45.42518 | 2025-09-08 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3c41a51-1d08-3d87-ae8b-f7897628fd3b | -7.73578 | -35.14038 | 2025-09-08 03:38:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dd30ea11-6ccd-3419-89e8-a780c0e75dff | -6.24575 | -44.83014 | 2025-09-08 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| daf8e192-1ef2-3c65-9ab8-16597983d00c | -7.57481 | -44.00339 | 2025-09-08 03:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ca5a6dc-4d2a-37ba-b926-371557c2ebdd | -6.19877 | -42.64262 | 2025-09-08 03:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cc5516ca-d889-38a8-87d1-bdaf2899090e | -7.24471 | -44.83205 | 2025-09-08 03:38:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7e53291-2bc3-3da9-a36e-933abba192c2 | -7.09758 | -42.93399 | 2025-09-08 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6cde6c69-09ed-31d0-8422-9a534cbe2b30 | -4.56392 | -40.3419 | 2025-09-08 03:38:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fd541043-606e-336a-a7db-400909255cd9 | -6.29699 | -43.82869 | 2025-09-08 03:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0453308-ebd5-3be4-a40c-787e8287f706 | -6.46072 | -43.94543 | 2025-09-08 03:38:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3c2fbff-fcc5-3deb-96ea-cf0857de566a | -7.82175 | -45.42245 | 2025-09-08 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d61ddd86-f3df-3962-8806-730582214e8b | -5.78428 | -45.62751 | 2025-09-08 03:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d20dd3fe-793e-3520-ac3b-8885ccc7ef3e | -6.14083 | -43.30142 | 2025-09-08 03:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1ec95f92-cc9e-37c5-b8d4-2795b4e1a41a | -6.53485 | -44.79425 | 2025-09-08 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f0d5a8e-baf7-34ed-8c9a-22d509951127 | -7.83179 | -45.42643 | 2025-09-08 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc5d0649-3881-3b53-b5db-b56decae0ad6 | -6.08779 | -43.12208 | 2025-09-08 03:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b5c0be0d-c075-3ce2-9edc-45d95a8c0069 | -8.24945 | -41.40865 | 2025-09-08 03:38:00 | NPP-375D | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 34f99b27-def0-36ee-87bb-48681c6e4281 | -7.00009 | -44.92986 | 2025-09-08 03:38:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af95e195-6bb7-3d28-8436-3ee70dcffb12 | -6.40747 | -43.87696 | 2025-09-08 03:38:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b472898-3c89-3706-9861-7864aa06b402 | -7.76586 | -34.91016 | 2025-09-08 03:38:00 | NPP-375D | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 97376e71-8334-34d1-9a08-88920c27d5c8 | -7.39253 | -43.99339 | 2025-09-08 03:38:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 998f6066-8fa8-3c01-b301-db7f791cb284 | -4.89572 | -42.21836 | 2025-09-08 03:38:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 23b2133c-5569-370c-b3e7-02a842468a5e | -4.55879 | -41.78136 | 2025-09-08 03:38:00 | NPP-375D | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 935d3333-b1b8-3a8f-b243-4c65a5789fe6 | -5.44409 | -42.79948 | 2025-09-08 03:38:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| de49b4e0-de57-31d6-9a82-80c99b83c1ac | -6.4961 | -43.98202 | 2025-09-08 03:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3e008c44-b118-3c89-aa4f-faf24d0027fa | -6.88111 | -45.53637 | 2025-09-08 03:38:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 505ee4e5-5e8c-3917-ab71-28b7d895e414 | -7.39325 | -43.98943 | 2025-09-08 03:38:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d561de7-f665-3355-a85e-be5f82e83a55 | -5.78599 | -45.62468 | 2025-09-08 03:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f377daa8-e8d1-31ea-b8d9-ccbd596ffda1 | -7.43777 | -45.21431 | 2025-09-08 03:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 277c7d37-83dc-34e4-88d3-8241ab40770a | -6.17391 | -44.25045 | 2025-09-08 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 325cb50d-be05-3e31-bcc9-1451ce065ae5 | -5.44991 | -43.44107 | 2025-09-08 03:38:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c077816-26e4-3a6f-bc56-6343e9003cf0 | -6.19818 | -42.64605 | 2025-09-08 03:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aebeda76-e4b9-3ffc-a9da-362ad74ba7fd | -5.63858 | -43.91382 | 2025-09-08 03:38:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc99d1ae-bd72-3782-9eb8-0dec38b07d1e | -5.49035 | -42.66352 | 2025-09-08 03:38:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8edae438-aa1d-3ef1-9ab0-afe88b6b05e8 | -7.36396 | -44.31416 | 2025-09-08 03:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73700225-fe0b-3470-b503-ffc06383a89f | -5.44047 | -42.58912 | 2025-09-08 03:38:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 62ddf3b0-b22e-3ea2-8841-94f57fa7ae58 | -6.38604 | -42.6098 | 2025-09-08 03:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 538a0aeb-afbf-3e4f-82e9-2e80bf6f5b10 | -8.19916 | -44.78373 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 18da4b4e-29f5-30b6-9d5f-42ebdcc884e6 | -7.09899 | -42.93737 | 2025-09-08 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 00f8880b-8a21-3216-84c8-d3a2cb41ce81 | -6.19338 | -41.00606 | 2025-09-08 03:38:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| da9403b4-8a59-3866-8f6d-93445e9e6098 | -5.77853 | -45.62896 | 2025-09-08 03:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 367c1a10-43be-3e26-8380-8654a8c085b8 | -6.13628 | -44.23801 | 2025-09-08 03:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5d2da88a-01b6-385b-9aa4-d5877f2daee7 | -7.36983 | -44.31503 | 2025-09-08 03:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51871ca2-f058-309f-ac41-9218fcf5bbc3 | -7.31909 | -39.15487 | 2025-09-08 03:38:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2c76b15d-6c47-39d5-ac86-d3b20add520f | -7.2935 | -44.14607 | 2025-09-08 03:38:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 464c3d83-fad9-3208-823f-ab3f9eebb03b | -8.62212 | -40.20452 | 2025-09-08 03:38:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 6.2 |
| c2ad24bd-4c45-3f92-9315-6fab18afdce7 | -7.5696 | -44.00461 | 2025-09-08 03:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13168b90-0b68-35cc-aeda-5a30f6965bdf | -5.94124 | -42.96065 | 2025-09-08 03:38:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8c68bb87-94ba-3324-9d15-e73fcd4be634 | -6.53289 | -42.41566 | 2025-09-08 03:38:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2ab58f7a-874d-33f7-adbc-4b567fb773e1 | -5.45445 | -42.80463 | 2025-09-08 03:38:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0259386f-ba09-3bba-8c72-d15d8ae37ce1 | -6.40468 | -42.98953 | 2025-09-08 03:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22e0a071-3f74-3c58-8a9c-706d75d6b6ca | -5.85271 | -43.85523 | 2025-09-08 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b09a73d8-c3a8-3e38-8da2-0bd69a2f46cb | -7.04074 | -43.25703 | 2025-09-08 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9a10ead5-93fd-3879-8077-2efb4914e8b2 | -6.20753 | -42.64107 | 2025-09-08 03:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 392ed98e-3c39-3085-b68b-e1e339e25709 | -5.8571 | -43.85757 | 2025-09-08 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4c0e8fdf-fae8-3c3f-badc-3921643f2084 | -6.94853 | -43.35938 | 2025-09-08 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3c0a4dbb-cf4e-35fd-92a8-04920c2aea91 | -6.33415 | -38.92583 | 2025-09-08 03:38:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9d7213a1-a4ce-3979-8ad2-86f0bc4a9c7d | -8.16987 | -43.17417 | 2025-09-08 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bd02a1bc-27c0-37e7-aeed-339c58b68004 | -6.66951 | -43.84391 | 2025-09-08 03:38:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c021523-1889-38f1-b981-5d014244cff3 | -5.85926 | -43.85204 | 2025-09-08 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f3c55605-b223-3c1e-bb9f-6501456e55d0 | -7.26344 | -39.3837 | 2025-09-08 03:38:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7c9ba3fb-e50e-3ea5-952f-9df5db882bc0 | -6.22064 | -42.59845 | 2025-09-08 03:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 564b4075-b162-3b14-b34a-3a03886d3b91 | -5.88657 | -43.96072 | 2025-09-08 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 20f9c587-135f-358e-8d1f-d59dfd862c1d | -7.34928 | -43.9399 | 2025-09-08 03:38:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abee806d-04f5-3a55-b2f5-5a9b569c7efb | -5.41754 | -42.85522 | 2025-09-08 03:38:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f324d488-2415-351f-8974-85fa56958281 | -6.26314 | -42.57518 | 2025-09-08 03:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 75f9b646-c60b-3449-8b90-6e7f08c40a9b | -6.19815 | -41.00693 | 2025-09-08 03:38:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f2991b5b-0556-30aa-83a4-0471958f48f0 | -6.61607 | -44.00714 | 2025-09-08 03:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60ff5f18-4cf3-3e14-b3e5-380df52cd417 | -6.13027 | -44.23745 | 2025-09-08 03:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8931dc92-e1dc-3541-9e1b-2d93c67ee636 | -6.25779 | -42.57444 | 2025-09-08 03:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a686e777-a1aa-30e1-ae0b-6bc199d1ba2f | -4.56855 | -40.34306 | 2025-09-08 03:38:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 526f7b8d-a0a7-397b-9782-b7febc8f61ba | -5.8586 | -43.84932 | 2025-09-08 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3aa9baff-fccd-33a7-981c-4348053fbdd4 | -7.43686 | -45.21912 | 2025-09-08 03:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e70fba47-5211-3209-b3eb-36f4751d5bd6 | -6.08843 | -43.11845 | 2025-09-08 03:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e507e11a-0638-3bff-8f16-78241614e8b3 | -6.21073 | -43.3796 | 2025-09-08 03:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 008d4187-3437-3fb9-a4b2-57a29e75db0a | -5.88732 | -43.95651 | 2025-09-08 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca8f04b4-1a86-3929-b278-533acc687412 | -8.62283 | -40.20039 | 2025-09-08 03:38:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 470f2624-947d-39cb-809c-8a464a5adf16 | -6.26227 | -43.69167 | 2025-09-08 03:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f16928eb-9500-3198-92f6-666bb0b7a18f | -2.82597 | -41.87442 | 2025-09-08 03:38:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68e2ffc8-bbb4-319e-a700-04bc37108000 | -7.02298 | -36.63697 | 2025-09-08 03:38:00 | NPP-375D | JUAZEIRINHO | PARAÍBA | Brasil | 2507705 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2d918f5f-96a6-345b-909c-e18f5fde12da | -6.17797 | -42.63556 | 2025-09-08 03:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| eba47311-271d-300f-ad48-d2521420d56e | -7.73562 | -44.72628 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c02701a-df10-37b5-b247-a63035198f00 | -6.46456 | -43.95742 | 2025-09-08 03:38:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2c9b6c06-f849-33e6-ade5-b4933a3102ce | -6.22884 | -42.58322 | 2025-09-08 03:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8c199cf1-f9f5-37aa-9915-b450ff7d7449 | -6.25072 | -44.83321 | 2025-09-08 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3bad0497-654a-3e09-b6d7-0776afc4ff48 | -8.15907 | -44.85229 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a9ce7c1-bfd4-364f-95b2-d50a0d84eb3b | -6.46526 | -43.95346 | 2025-09-08 03:38:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4c4c5dbe-501a-3cc2-b6ec-166718201173 | -4.63074 | -38.56478 | 2025-09-08 03:38:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 51df30f3-0de2-335b-912a-906e85eb51a2 | -7.87903 | -46.25667 | 2025-09-08 03:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c8edcd76-ab80-3141-be6d-3255d6bc13e0 | -6.1206 | -44.25765 | 2025-09-08 03:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9177d74c-e7e2-324a-af4a-26a2b892840d | -3.89831 | -38.53648 | 2025-09-08 03:38:00 | NPP-375D | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 538546ac-d4ed-36e3-8e91-ae2a1d7c497f | -7.35421 | -43.9451 | 2025-09-08 03:38:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README20.md)
