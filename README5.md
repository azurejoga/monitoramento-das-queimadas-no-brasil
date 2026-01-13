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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69cda3c4-b65e-303b-b7d6-d17cad7f283f | -3.54491 | -43.65784 | 2026-01-13 03:59:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acb6b2ef-1c73-39ef-ad0b-a03e34a83d3a | -5.72095 | -41.2744 | 2026-01-13 03:59:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ab330dc2-9d49-333a-be2b-766af78de754 | -3.92366 | -42.41704 | 2026-01-13 03:59:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3414ee95-749c-38d5-a31a-33a283652177 | -8.51317 | -37.08414 | 2026-01-13 03:59:00 | NPP-375D | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 462d8f00-662b-3cd8-ae40-1a19a71bca90 | -4.91713 | -43.42561 | 2026-01-13 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b6b6434-cec4-3c6c-9184-7628b9a19fb8 | -5.10458 | -43.22303 | 2026-01-13 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1e06617b-5422-3b40-811b-af943aded465 | -5.09188 | -43.22434 | 2026-01-13 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| dee51b1c-4b59-3957-bfdb-175aaee97908 | -5.28385 | -43.56508 | 2026-01-13 03:59:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 53930859-ea92-3193-bf46-4443fe5fd596 | -4.4223 | -43.10352 | 2026-01-13 03:59:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 91d678bb-a32f-3adc-af05-6a5f1c8aaca4 | -3.60401 | -41.86587 | 2026-01-13 03:59:00 | NPP-375D | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 28d0d00f-999c-3664-9bc3-9aea06ee3fc9 | -3.13709 | -42.2094 | 2026-01-13 03:59:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9929b854-f787-3eb2-b7fc-e0a241a9c293 | -5.24926 | -37.50069 | 2026-01-13 03:59:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8f20ce7e-053c-31a9-98de-a9eaede64a92 | -1.90295 | -46.269 | 2026-01-13 03:59:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42f9fea9-e3a6-3051-bfe6-e82ec10f416a | -5.5312 | -39.19993 | 2026-01-13 03:59:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 81ba2477-af80-3e28-a004-cdb1a677b316 | -8.57734 | -39.57525 | 2026-01-13 03:59:00 | NPP-375D | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b6a76aaf-014d-3d4e-877c-4f748abaadf7 | -4.41765 | -43.1064 | 2026-01-13 03:59:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 55e90b34-7ef6-3335-adf4-92e076bfb054 | -3.29322 | -42.54641 | 2026-01-13 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9f622001-a676-3733-9a9d-190a4adfeda4 | -3.30687 | -42.53811 | 2026-01-13 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb579556-87ee-3b72-9aa6-0bfc06c764aa | -6.48385 | -42.94091 | 2026-01-13 03:59:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c704223f-ff65-35dd-996c-5ad29cede561 | -6.30482 | -39.84486 | 2026-01-13 03:59:00 | NPP-375D | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 00f5effb-2862-3708-a89c-ac51655fb4d4 | -3.73585 | -39.92095 | 2026-01-13 03:59:00 | NPP-375D | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 084db51c-aa5e-350d-a04a-0d60d32edd23 | -4.75153 | -43.24924 | 2026-01-13 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da5794d5-85ac-306f-94fc-bed60bb1aaae | -3.54001 | -43.66108 | 2026-01-13 03:59:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 929a1ac8-f79d-3f66-a482-37bc1d525a37 | -3.28838 | -42.55088 | 2026-01-13 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e7326c7c-f870-3a43-82a9-e84e0d3e34a3 | -3.54926 | -43.6495 | 2026-01-13 03:59:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 859d016a-c540-3807-abc7-ba21e62fe3fa | -3.29571 | -42.54493 | 2026-01-13 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 27861a07-70b6-3223-b015-11fcf45de477 | -2.92697 | -40.59616 | 2026-01-13 03:59:00 | NPP-375D | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d1223da2-8e04-3af0-be50-be5cd32648e4 | -3.60781 | -41.86652 | 2026-01-13 03:59:00 | NPP-375D | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7382f6b6-61ef-361e-a22b-f65ec1899cc9 | -7.39797 | -35.20862 | 2026-01-13 03:59:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cb313c5b-df80-3491-ad4a-ef57d76b6bd5 | -2.41682 | -44.96368 | 2026-01-13 03:59:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8928d7d4-b84f-3a8f-bb47-2f3c53e4d027 | -5.10284 | -43.2336 | 2026-01-13 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 879399a9-1429-3865-b389-46bbc76999b2 | -5.10973 | -39.46119 | 2026-01-13 03:59:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 83d2ffbb-63f9-34d1-b148-2c461c8a978d | -5.10804 | -43.22726 | 2026-01-13 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3d297920-c03a-3e07-9fc0-cb3ce54462a6 | -5.10054 | -43.22229 | 2026-01-13 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b0345d17-a9f2-3561-bb90-551a5527e9ae | -2.87657 | -45.2284 | 2026-01-13 03:59:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 813fde39-83e8-339c-81dc-9ae53958c785 | -6.80596 | -38.13851 | 2026-01-13 03:59:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3853ad9b-46e7-3659-b127-c5aa4f2af10f | -5.54461 | -39.77281 | 2026-01-13 03:59:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 197cd324-b730-33ab-af49-be99db4884b3 | -5.39606 | -40.34421 | 2026-01-13 03:59:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| baeeba24-7613-396a-af17-19c68b143a68 | -3.55108 | -43.64672 | 2026-01-13 03:59:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1273589d-0150-3043-ba6a-76dc6e4fec1a | -3.5486 | -43.65343 | 2026-01-13 03:59:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbcb85e4-b77e-3da0-b632-59a5e82b6a68 | -3.38495 | -42.11422 | 2026-01-13 03:59:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| da6eaf74-b947-305d-993b-783ea1ce68c8 | -5.0992 | -43.2211 | 2026-01-13 04:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 217.7 |
| 08dc8ba6-7be0-35e4-a4fd-8ffd6facfc12 | -5.099 | -43.2444 | 2026-01-13 04:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 68a2122a-e9e1-3e49-bbb1-87204a1323d7 | -9.78521 | -42.03515 | 2026-01-13 04:01:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 05fad80b-d164-3564-9c4d-5691f0bac73c | -11.20659 | -40.73194 | 2026-01-13 04:01:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 771246c3-4789-3f13-828a-8d1431f99a6d | -10.25912 | -37.86176 | 2026-01-13 04:01:00 | NPP-375D | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a98131fe-add3-398c-a66c-b418d49525d1 | -11.3321 | -37.86534 | 2026-01-13 04:01:00 | NPP-375D | TOMAR DO GERU | SERGIPE | Brasil | 2807501 | 28 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9af5041c-e85c-3925-ba01-16d37bf65318 | -16.4291 | -42.63585 | 2026-01-13 04:01:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5f52619d-68ba-3ffe-a21e-fbecac3fd7a7 | -16.24801 | -42.23238 | 2026-01-13 04:01:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b04066f6-9563-37d7-91e4-38c118201c06 | -22.52419 | -44.86707 | 2026-01-13 04:04:00 | NPP-375D | LAVRINHAS | SÃO PAULO | Brasil | 3526605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 18de94a3-a436-347f-80ce-f30be8637045 | -21.30042 | -43.80432 | 2026-01-13 04:04:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 21901d52-96c0-3581-bb02-8576cc4da1d3 | -22.6823 | -43.72187 | 2026-01-13 04:04:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2a9a90bf-d8e2-3e29-b796-c3d04d9d3a6a | -16.56197 | -43.79087 | 2026-01-13 04:04:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e712ead-e0a1-3ea1-a40a-38000e99f5a2 | -17.88776 | -39.76706 | 2026-01-13 04:04:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d1133a93-581d-3e45-8a12-dbe79d413979 | -21.56627 | -43.66065 | 2026-01-13 04:04:00 | NPP-375D | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2de28dde-b7c3-30bc-895b-78804fcd6384 | -22.59511 | -44.64637 | 2026-01-13 04:04:00 | NPP-375D | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 565c4e95-e5b6-3b52-9462-d56ec3323497 | -18.40594 | -43.27788 | 2026-01-13 04:04:00 | NPP-375D | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f8e490e8-ae6c-3046-87fe-9b717105150b | -22.85533 | -43.54652 | 2026-01-13 04:04:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ce6f4ea5-a416-3b5c-ba66-90b550549dbe | -22.68086 | -43.70954 | 2026-01-13 04:04:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 19a5a775-c4f4-3d08-8f6a-54b58657ffc6 | -20.84154 | -51.74032 | 2026-01-13 04:04:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 5bfb5e61-17df-3935-a9ba-e3c21e9de88a | -17.51906 | -43.83673 | 2026-01-13 04:04:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 26a6c8ad-b32c-3092-816f-e35e1e35b876 | -22.67891 | -43.72128 | 2026-01-13 04:04:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 295bc212-2bd6-34e7-bc39-ea5abedc0853 | -21.85816 | -43.08366 | 2026-01-13 04:04:00 | NPP-375D | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| c53cc938-a9bb-31d5-ba57-8771b4cc1754 | -17.57272 | -42.52761 | 2026-01-13 04:04:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f05b9b97-3720-3ba9-a762-ca23e06ab9c1 | -22.67407 | -43.47782 | 2026-01-13 04:04:00 | NPP-375D | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f9e85b6d-54ff-32ef-af97-5be143cef1e2 | -21.6595 | -42.45298 | 2026-01-13 04:04:00 | NPP-375D | ESTRELA DALVA | MINAS GERAIS | Brasil | 3124609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9a74efcc-0bb1-3157-aaf5-724deca3ed63 | -17.89058 | -39.77138 | 2026-01-13 04:04:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 851edeb9-5697-3b5d-ab66-2ad09599372a | -20.84426 | -51.74066 | 2026-01-13 04:04:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| d044b4e0-d9f8-3b88-82f3-6280f766301a | -17.89115 | -39.76762 | 2026-01-13 04:04:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9885b1c0-cdb9-3bc7-8e66-d599534b7445 | -23.10248 | -45.48765 | 2026-01-13 04:04:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 914a85d0-cbbe-33bd-8174-07e306e2253a | -5.099 | -43.2444 | 2026-01-13 04:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 3d0c490b-98aa-3d16-a11e-4c92ef3656ab | -5.0992 | -43.2211 | 2026-01-13 04:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 204.2 |
| b691c9e2-c013-390b-8388-4aef883d8fbf | -5.099 | -43.2444 | 2026-01-13 04:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 67dad588-2cc9-3ac4-b965-b233bd53642e | -5.0992 | -43.2211 | 2026-01-13 04:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 732bcb68-de27-3f6f-b209-a3f0413ee245 | -5.26373 | -43.57611 | 2026-01-13 04:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1f51e1a7-ed82-3148-b8ed-f970b31080c8 | -4.73317 | -45.79401 | 2026-01-13 04:21:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f879df56-eea4-3aef-939f-0a01444ddb8e | -0.04631 | -51.65912 | 2026-01-13 04:21:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66fadab4-b801-39fb-ba72-2cee336bbc76 | -3.29819 | -42.53667 | 2026-01-13 04:21:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6da4d911-d893-3b39-896f-5d660c59b428 | -6.08376 | -37.31691 | 2026-01-13 04:21:00 | NOAA-20 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2351a0d0-dc48-3bf2-aaf0-130e561ae88d | -4.76738 | -45.79576 | 2026-01-13 04:21:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f980908-cbbe-3f8e-a372-f22739777f9f | -0.04577 | -51.65702 | 2026-01-13 04:21:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c5829b3-5064-3118-ad9a-7d24fdd069ee | -1.28703 | -53.69074 | 2026-01-13 04:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 081cb9bf-3b36-3b2e-ad11-7a4b34e69a22 | -6.483 | -42.93888 | 2026-01-13 04:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| adbbd210-5903-3ac8-a33f-d341fe8c0ed5 | -5.92739 | -43.33321 | 2026-01-13 04:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4f7fdac-155e-34f8-accd-2986ed159d88 | -4.25005 | -48.26449 | 2026-01-13 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f1d20638-7392-3439-b0fe-8696e2019b8d | -3.69995 | -45.89861 | 2026-01-13 04:21:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 248e66a4-e515-3c3f-ba1a-28b9d73a9e68 | -5.09387 | -43.22732 | 2026-01-13 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1409458d-bc1b-3048-bccc-80c1003f2480 | -4.70409 | -44.48041 | 2026-01-13 04:21:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ef72fd2d-a9f9-3e0a-9308-0fe3e45d51ce | -5.09779 | -43.22425 | 2026-01-13 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 0b7e2898-a0ef-3754-93bf-d148e5cfe549 | -2.01819 | -46.64634 | 2026-01-13 04:21:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b59498da-3d73-3ad5-b61a-b2abf2ad131a | -3.54628 | -43.65871 | 2026-01-13 04:21:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99284092-6af1-35f2-a065-669ae7b330a6 | -4.30563 | -39.37365 | 2026-01-13 04:21:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1b550659-f175-3537-829b-982bed6d9ab8 | -3.55178 | -43.64539 | 2026-01-13 04:21:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d23a767f-8cca-3163-8bd0-95251312b43a | -2.86838 | -45.21648 | 2026-01-13 04:21:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c32ad96b-3af1-3abd-8d64-40ba07e9aac5 | -5.10677 | -43.23291 | 2026-01-13 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4d5b5a09-44c3-3495-abe6-a73320504e37 | -4.9047 | -38.72002 | 2026-01-13 04:21:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| db3b12bb-62f1-3ef2-8b40-03bc5b87f5fd | -5.1006 | -43.22834 | 2026-01-13 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| e639f91c-e083-3057-ae81-969c684ec0c6 | -3.70977 | -41.68983 | 2026-01-13 04:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| af6de7db-1a16-329f-9588-c3fc189d199f | -4.41806 | -43.10514 | 2026-01-13 04:21:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5019af94-9763-3cd5-bad7-0cc964112332 | -3.60289 | -41.86361 | 2026-01-13 04:21:00 | NOAA-20 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README6.md)
