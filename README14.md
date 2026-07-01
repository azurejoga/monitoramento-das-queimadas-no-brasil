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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b27685b1-646a-3d30-9cdc-563d11b7931c | -5.2074 | -37.47546 | 2026-07-01 04:36:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5add90cf-392e-3075-b010-72284b08e4b0 | -3.91542 | -47.81826 | 2026-07-01 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c044f752-8fd2-3e9c-8019-82fe4e866967 | -3.50941 | -48.03566 | 2026-07-01 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 21609c69-a5b1-3908-b0b6-5728fbecb97f | -5.13653 | -37.84526 | 2026-07-01 04:36:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 61602168-313f-3510-bd34-8c4f5e947721 | -5.79762 | -45.06567 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 825308b1-805a-3789-9694-2d5948db397b | -5.86336 | -46.25456 | 2026-07-01 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 28e711a8-4218-3d5e-9af2-ceb26cc14c2a | -5.81195 | -43.80337 | 2026-07-01 04:36:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d65b55cf-692f-3b9c-81e0-a8d16b895615 | -7.01813 | -45.42981 | 2026-07-01 04:36:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fed63a74-171e-3084-b2f8-57768229e891 | -7.07818 | -45.65046 | 2026-07-01 04:36:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63b5369b-f7d5-3f56-975e-e1da5e3355bd | -7.10183 | -46.50754 | 2026-07-01 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6fdf39c-4473-3789-9763-924888dff23e | -6.16407 | -44.64559 | 2026-07-01 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 2fdbb7b4-07e9-375c-9377-d34ec3bc72e9 | -6.95671 | -44.55029 | 2026-07-01 04:36:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82faab74-0e75-3644-b39b-c318aab1395e | -5.55561 | -48.70571 | 2026-07-01 04:36:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ccbace1-7047-3c4e-b330-301a4426db5b | -5.13144 | -37.8445 | 2026-07-01 04:36:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| d6418cca-5fe1-38d2-a0a7-a1cbaa2e1856 | -5.80551 | -43.79834 | 2026-07-01 04:36:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 18a17a65-6ac1-39fe-a2d1-b7f36685a980 | -5.79876 | -45.05849 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 683137d2-e3a1-380f-aea9-6302aa8a2b34 | -5.55274 | -43.96776 | 2026-07-01 04:36:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 413ef73e-7290-3428-8ac4-f0bdb9fd4593 | -6.90392 | -48.0448 | 2026-07-01 04:36:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 657fa849-ea2a-3068-bdc3-ae9de8bd99c2 | -5.78807 | -45.03847 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95737aa3-efdd-366b-a881-0a0f3f16c310 | -5.79893 | -45.06574 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7f14a3f-9f53-3fbd-89fa-9def481574c2 | -5.79843 | -43.63534 | 2026-07-01 04:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebd5201b-c240-3f89-88be-48d9687ec3cf | -5.80171 | -45.04775 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6049c9d8-b975-3520-87bf-628163463aa0 | -6.84308 | -47.94245 | 2026-07-01 04:36:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ab01282-a8e2-3b6d-af1b-28b04958bfe2 | -3.51697 | -48.03296 | 2026-07-01 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17741183-303c-3b2a-8618-0a83cbc235be | -5.80286 | -45.06267 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2453da98-bb80-397b-8417-3261c23a5437 | -3.51635 | -48.03677 | 2026-07-01 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca1d6ea9-abfb-37ea-97ae-b23c5a0ff543 | -7.01757 | -45.43338 | 2026-07-01 04:36:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b9861809-4ce0-3963-9bc4-eb8070d0fd8c | -5.80903 | -43.79889 | 2026-07-01 04:36:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 772867fc-fe85-3249-b832-9b9e0e5e41a0 | -7.09851 | -46.50702 | 2026-07-01 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e4e6f4b2-9bbd-3411-a75c-f3fffdb498ed | -4.57952 | -48.02783 | 2026-07-01 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4450a92-163b-3576-8ef3-88a4fa2f77b8 | -5.79586 | -43.88503 | 2026-07-01 04:36:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4f33da7-21ed-32c6-a630-4ff2c9a34f71 | -5.79596 | -45.03234 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca13bb9b-0e47-31db-a9bd-e0ef4894337c | -5.86004 | -46.25404 | 2026-07-01 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14a93d48-afb1-377b-8dc9-d6551b78a287 | -5.71318 | -43.22821 | 2026-07-01 04:36:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b577ca5-7e3e-385a-98fb-7658c20e4057 | -7.00394 | -42.77459 | 2026-07-01 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 489b4449-b743-384a-8ce4-5e3589aee082 | -5.55333 | -43.96393 | 2026-07-01 04:36:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8abe2258-7946-3f31-b97e-68b0a64d326e | -6.9128 | -42.84414 | 2026-07-01 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 601a4fec-83b5-36f5-9026-08fda233b541 | -7.0142 | -45.43287 | 2026-07-01 04:36:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 26d0fd3a-c58a-38cd-91f2-e27ae6c1bbc6 | -5.80004 | -45.05855 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6729fa51-6174-3745-a53f-5448eeaa2042 | -7.00631 | -42.78644 | 2026-07-01 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c1957fca-146f-3ad3-8fe1-1c4be1d4d29b | -5.79989 | -45.0513 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c442744e-3a99-3a71-82b0-72a3f7b8f40c | -5.79176 | -43.88836 | 2026-07-01 04:36:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a88064b-c37d-36c2-9d12-858e7d795401 | -5.79538 | -45.05796 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14ccbaf2-53cd-3d01-8b12-c43b4bd28626 | -7.0215 | -45.43033 | 2026-07-01 04:36:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42a16ee5-ee37-3692-bb88-a815e36abaad | -4.69932 | -45.20083 | 2026-07-01 04:36:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a563022-2e53-3519-8979-e9ab7b4106fe | -7.00697 | -42.78192 | 2026-07-01 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b8dc7425-9f95-3ffd-a8e0-88a5c14511a8 | -5.20679 | -37.47696 | 2026-07-01 04:36:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a525877d-3fac-3405-a992-891a3ffb71bd | -5.79145 | -45.03899 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b1d60849-96db-30da-af8f-9a573b5ac32a | -6.83971 | -47.9419 | 2026-07-01 04:36:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2927beb3-7bfd-39e9-b427-e306192d2378 | -3.91886 | -47.81879 | 2026-07-01 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9dc174e8-d6ab-326d-b2cc-a3c75bbbf54c | -5.03365 | -42.72857 | 2026-07-01 04:36:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d8d14b5-78da-3b46-b9d7-943260ec9c23 | -3.67587 | -48.9866 | 2026-07-01 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d3aa439-9cb2-3086-9284-5de8b65d8cb0 | -4.35007 | -47.76461 | 2026-07-01 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b75ba88f-f2b1-39ba-8f59-b79dc5fd853c | -3.80618 | -48.96356 | 2026-07-01 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0173c83-1704-3224-9a42-39a9088b25c1 | -3.50593 | -48.03513 | 2026-07-01 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a06483ba-c2a4-3c26-b590-5858605d31a9 | -5.29487 | -45.31144 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39318cb0-29b0-36f6-bf6a-781fa1f7980c | -5.79202 | -45.0354 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21c70867-479b-370a-83f7-d54b9b5ac5ce | -5.78751 | -45.04205 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb4bcab7-8e08-3e7d-b5a1-b9dd47041183 | -5.90921 | -43.84919 | 2026-07-01 04:36:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| abff8f01-1f60-3aff-be59-ae8e5fc98608 | -4.34665 | -47.76408 | 2026-07-01 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6ffd791-7080-3c35-af70-6213233a605b | -3.56283 | -43.20387 | 2026-07-01 04:36:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b287fc25-6fef-36b6-ab21-1a153e0bdb9e | -5.80046 | -45.0477 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5ad9274-1bd0-3650-9440-9fd1992982a7 | -4.94361 | -48.24605 | 2026-07-01 04:36:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 527fa7c9-2f87-39f5-a89b-6b335560c11b | -4.18304 | -47.8446 | 2026-07-01 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f21f4cdd-7f84-3eaa-8fc9-c27bc968a36f | -7.00086 | -42.7695 | 2026-07-01 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7fbeb3b5-efe7-340b-974c-111d480b52e1 | -5.79595 | -45.05437 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24cb6a35-2f54-3cc9-b251-20d518ecccf7 | -7.00632 | -42.78419 | 2026-07-01 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 84554451-a85c-321b-adcd-76dcecd3bdfe | -5.79932 | -45.0549 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3af5b8e-7de1-36d1-9dde-d78efd6211c4 | -6.19161 | -44.87069 | 2026-07-01 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b080607-6d2e-3b3e-8558-cab1d979ee72 | -6.95841 | -44.55371 | 2026-07-01 04:36:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3f13a820-333e-37bc-9c21-ab0fb3ab77c7 | -5.79837 | -45.06934 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d61c9d5-228c-3f99-b689-fa8217aa30d7 | -7.1992 | -45.50126 | 2026-07-01 04:36:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7abdf66f-a03d-345a-ac60-6fb213cc4264 | -7.09519 | -46.50649 | 2026-07-01 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a8dbf66-ca7d-32a0-b512-ac931336f0e0 | -3.71179 | -47.16733 | 2026-07-01 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 28772109-0e0e-3adb-86a5-16df24561416 | -6.18821 | -44.87015 | 2026-07-01 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3133aa8a-552d-3787-8c69-42027f80865a | -7.00701 | -42.77968 | 2026-07-01 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| af5f57d0-efb0-3913-b769-502311a2c642 | -5.79539 | -45.03593 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5d548b9-37c9-3785-8d92-048d1ac95e4b | -3.71517 | -47.16785 | 2026-07-01 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| edace505-2fda-3c77-ba45-06929992cb07 | -3.51226 | -48.04005 | 2026-07-01 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2d53a74-b14c-391d-8150-a076c5acc346 | -7.09906 | -46.50354 | 2026-07-01 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 38d60256-f197-3ac6-bfcf-80c864cbb19d | -5.29152 | -45.31093 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 19211079-0abd-36a8-b3b0-7198db9213b0 | -6.91214 | -42.84857 | 2026-07-01 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0b58cd9d-2e2c-3489-b6a6-1962985d0cc7 | -7.09574 | -46.50301 | 2026-07-01 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6eba5bd-f0de-3a6c-9f6d-6019beced117 | -6.91589 | -42.84912 | 2026-07-01 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 61dff204-14e5-395f-af9c-83e843117a8e | -5.35368 | -45.1901 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 260f9410-e5df-3f6e-8002-68421e7242c0 | -5.35032 | -45.18958 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 46354e7b-1735-3b97-9a91-7075700edee7 | -5.09847 | -37.78478 | 2026-07-01 04:36:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 93f6db49-560a-30a3-b540-2709bba3d41a | -5.79089 | -45.04257 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 926e2094-0265-34ce-b835-5dc9397448be | -5.13188 | -37.84153 | 2026-07-01 04:36:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| cd85edec-302a-32ad-ae4b-f797c68219ea | -6.16007 | -44.64875 | 2026-07-01 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 21c5af3b-bb77-36a9-917a-4dedf07259f7 | -5.8023 | -45.06626 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 77ba8dc6-4b40-3f30-84f2-38c04b3367b6 | -5.21204 | -37.4776 | 2026-07-01 04:36:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 79a20bc3-a434-39bc-a0b3-bcd6df34a25b | -5.80843 | -43.80281 | 2026-07-01 04:36:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 41ec2afe-82f6-3aa7-9773-38cfcb5240ab | -5.79948 | -45.06215 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4ed6d0c-704b-3b47-804f-48e993745395 | -5.80115 | -45.05135 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44ff2d36-a7fd-3cd4-af82-a6870ec1be76 | -12.83502 | -44.35451 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| dc72add6-0a3a-3e22-8766-ea0659bb4f31 | -13.17341 | -46.02053 | 2026-07-01 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4dc48609-1d04-35d3-909a-55d0cbf38bfe | -15.21708 | -42.59366 | 2026-07-01 04:38:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91f63f6f-9ce6-31da-b3fe-f4af7b71d440 | -10.4372 | -49.58314 | 2026-07-01 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6658eb06-b89a-3595-ab0b-5f52c1e170d9 | -9.02693 | -59.54198 | 2026-07-01 04:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README15.md)
