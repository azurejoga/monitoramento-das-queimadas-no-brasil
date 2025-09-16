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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a293551-2c44-3e3c-8684-9ea579d8a30f | -6.62166 | -44.73683 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 923c11e4-4d7e-3c1e-86bf-10f528bb6023 | -6.93988 | -44.3448 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11bc09f3-5a30-3bc5-a283-2a94b2eab402 | -6.18712 | -43.47015 | 2025-09-16 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 38d6d00a-84ce-347f-9d2c-74c7f133ef18 | -6.29627 | -42.40304 | 2025-09-16 04:27:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9a44f49b-869e-3611-86f2-494c9efa95a5 | -5.9575 | -42.7272 | 2025-09-16 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 197c57a8-ce28-3736-8e67-c75007e372c6 | -6.34474 | -44.76603 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8814d7e5-dbe4-35b1-9dcc-e34fabc4d991 | -5.67206 | -45.0512 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfaf5288-9442-3317-8194-fdfc856b8709 | -7.67236 | -44.47623 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 863af278-f0ca-33bc-803e-ee23abf5c0b6 | -6.45111 | -43.32196 | 2025-09-16 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5d6a4e7c-8cdf-3d63-b179-8cc5b92fd1ac | -7.20648 | -44.3845 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aca2b199-94f6-3d05-91a5-2c7cc8b3d360 | -5.8973 | -45.75085 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f3c50ce-244e-3ffe-a378-66b946749ca5 | -7.49598 | -44.67207 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 95e561ca-9884-3efe-955e-16777ef40a90 | -6.26076 | -43.46479 | 2025-09-16 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef6259fd-3fe4-39ad-8f2f-5311da66753a | -6.09666 | -46.50082 | 2025-09-16 04:27:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37842061-14f8-3b6b-a9d2-fd425b6beb3b | -5.78843 | -45.90466 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3dd641ed-f551-3928-96d1-0d8843c292b4 | -2.30605 | -48.14613 | 2025-09-16 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 351e31e6-ac2c-38ce-bf1f-92442b28ae6b | -6.46112 | -43.67984 | 2025-09-16 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ceef865-05ff-3f1a-819f-d8c85d6f85e2 | -7.01552 | -44.91589 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eba1447a-a2d9-305f-a9ec-80250c32809e | -5.28306 | -43.21441 | 2025-09-16 04:27:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e4accf0d-bd07-3ecd-b9c2-4bb4e1fff26e | -5.92111 | -45.72965 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb30261d-aca0-30ea-8dd0-7b739d0d67d8 | -5.86316 | -45.85944 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f43c3d2-e4da-32b6-842c-28ac5c3681aa | -5.77911 | -45.94225 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 518b73c5-c143-3921-9e96-0ed46e30453f | -7.05632 | -44.17145 | 2025-09-16 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 581227a7-ac6d-300d-b91d-587c865f7a57 | -5.89065 | -45.74981 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30308da9-577a-3ee7-be6b-a29ef16f0e7a | -6.34414 | -43.16692 | 2025-09-16 04:27:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 101b7343-bcf0-3fcc-9187-2eecdda5c33f | -5.67596 | -51.14289 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69c237d1-d68a-3a62-9116-ade17f1026a5 | -5.47689 | -45.34554 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64741128-2b90-3317-8962-8fcefa5098bd | -7.13824 | -47.9851 | 2025-09-16 04:27:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b1e223d1-a1a2-3ded-9ea4-a04d47cd35e3 | -3.65047 | -54.06166 | 2025-09-16 04:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebcb8618-7817-390c-adf2-a204022ca27e | -5.8095 | -44.8651 | 2025-09-16 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a88251e4-88bf-3709-9375-6ffe2a1a5a23 | -7.26997 | -46.59057 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f564df32-21dd-374b-8228-48547e09b382 | -6.1767 | -41.21837 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bf698661-cab9-30d6-aaf4-ada228060a96 | -5.77445 | -43.91257 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f0656be-56c1-31a1-a95b-541de48f722f | -6.09388 | -46.49682 | 2025-09-16 04:27:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa51922c-a86a-3121-9460-e5f498c43186 | -4.91221 | -38.00503 | 2025-09-16 04:27:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e5111fd8-389c-3031-8779-30c23c3cd8d0 | -7.26887 | -46.59753 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 72cc1f2f-e90b-32ac-af7b-85c7c362989a | -3.42374 | -43.15186 | 2025-09-16 04:27:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0aca6eae-9ab2-37f9-ae3d-8becf79af9c1 | -7.51889 | -44.72899 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85660a63-ff00-3c30-9c01-7660ce2a652f | -3.89761 | -40.92129 | 2025-09-16 04:27:00 | NPP-375D | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9d8dda54-52f3-3afd-a35e-4c341e7e593f | -2.56215 | -48.96831 | 2025-09-16 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ffd587c-9204-3c76-bef8-93ce0c880ca0 | -6.16226 | -45.11289 | 2025-09-16 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 749c0fe5-101f-382a-b962-2cf6bbef563d | -7.13942 | -47.9778 | 2025-09-16 04:27:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b78b92c-6d15-3a4c-a6c7-ad234e6a03fc | -6.43016 | -43.31473 | 2025-09-16 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 543084e0-0ab8-34c5-a7e7-afa1f77896d2 | -6.67878 | -46.30837 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a5d3f2bc-ba71-30f6-8b2a-353e3e151833 | -6.17327 | -46.80951 | 2025-09-16 04:27:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b909205-7d8b-31e0-a671-f8ce65b76cd1 | -3.42665 | -43.15629 | 2025-09-16 04:27:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5fc20578-867e-3462-b20f-3020ab15b293 | -6.51354 | -46.21466 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e138e5d-fa07-375f-b48f-d5e551fb52ec | -7.0546 | -44.11223 | 2025-09-16 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4cf15088-df7f-3182-9aa4-406ebe4f806a | -3.83448 | -44.10571 | 2025-09-16 04:27:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b314421f-5848-3131-a4eb-9d866da0e9af | -6.98863 | -44.59269 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3249f736-85f5-3cd4-b45f-350e214ebd5e | -5.91304 | -42.74715 | 2025-09-16 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d2138ed4-02af-3586-bf83-552044001914 | -5.09851 | -43.82933 | 2025-09-16 04:27:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3f509119-d5b5-3df4-b8f0-c8a7d67947b1 | -7.20994 | -44.38499 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b42b621-7ad2-37a0-976c-e8196b83b1fd | -5.99511 | -45.81582 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3234cb10-4c51-3bd9-8243-c41d7fa11851 | -6.96888 | -44.56765 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c811dde0-1f39-355b-b902-bbd38481b31f | -6.89345 | -44.55603 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7f70126-9cbf-36ab-9c14-2455f239f49d | -3.73753 | -49.05371 | 2025-09-16 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 87b8d14b-1497-36e4-b08c-5c0a4e624a87 | -6.67823 | -46.31184 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dcc907aa-b591-3939-b6f6-8a5af5530290 | -6.36775 | -44.41262 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e663a08-74ea-3b2a-bfce-051bef8464a2 | -7.28052 | -46.61008 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f9617b25-6980-34df-9fb2-29eddb56ad36 | -6.43438 | -43.3111 | 2025-09-16 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e57f24ad-d230-3d09-984c-b4386b9fe87e | -6.96679 | -44.44519 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd186133-e021-3037-88e6-f8c97cf68c8b | -5.79623 | -45.91652 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e612acd-d180-365e-9458-7ed37f19626d | -6.62747 | -45.57556 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45d6ce56-d3ed-39c6-9755-40828ef3b3eb | -6.66692 | -45.54219 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4466c58a-5346-3bf5-b260-b9109af3a7fc | -5.79349 | -45.93381 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c4a8094-b0b8-35d2-b405-8fab9da91e6c | -5.90884 | -45.90904 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 196b46a8-65f7-3c6f-95c7-235cfe43f436 | -6.75709 | -46.36685 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6341b3db-ec57-37ae-aa84-3298d734739b | -3.82315 | -44.11138 | 2025-09-16 04:27:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce9f099e-c5d5-31aa-9e83-60a89f89efa2 | -6.19016 | -41.1842 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7174e5cb-978e-3242-971b-44f2f26ac230 | -3.78389 | -48.15738 | 2025-09-16 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42bdca1e-4e48-33e2-a5de-bcad607686af | -3.73891 | -49.0451 | 2025-09-16 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9a29e743-0802-3f45-b15e-fdbe04886cbc | -4.16251 | -46.79049 | 2025-09-16 04:27:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6f0cc7c-c546-371b-b18e-5b1cb785759d | -6.82516 | -44.77199 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dcddb5f4-9aa8-34e6-92d4-0157883cd488 | -6.40914 | -43.33245 | 2025-09-16 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b8f0863-b157-3891-930a-69c648795954 | -6.16334 | -41.16974 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eefc852c-42ce-398f-9b49-46f4e0287bc4 | -6.24393 | -44.38266 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4b97e3a-f44b-37ee-9a35-7c0b6b92a52c | -6.40495 | -43.33595 | 2025-09-16 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 901c4a02-889d-347e-95da-c0fd4047c6a6 | -5.90443 | -45.91546 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 653afd27-1ece-301e-8ccd-cd6833cae68e | -5.89671 | -45.73295 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2411ead0-a034-3515-96a8-ff35001c2c14 | -6.18853 | -41.19489 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b85e029c-a763-3d6f-8c10-5fbed76cd34b | -6.9622 | -44.4521 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60ecbb97-1144-3118-9c4c-ccd50347181e | -6.46547 | -46.00741 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c778ab2e-4879-3295-86f7-4e86f45e0091 | -6.34476 | -43.16282 | 2025-09-16 04:27:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fce67b2d-b2dd-30f5-858f-fb1c4731e93f | -3.82655 | -44.1119 | 2025-09-16 04:27:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d646453-af79-3010-86ba-897a91c4fb8b | -6.75776 | -48.11353 | 2025-09-16 04:27:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a330b626-887b-3eb7-beaf-9ae183a9db46 | -5.33814 | -44.82545 | 2025-09-16 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d29531bc-0428-30c0-944c-2bc2c1cbefbd | -5.9214 | -45.82917 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 789fc6c0-ec05-3e15-9b65-4151f4d78483 | -4.48647 | -48.11743 | 2025-09-16 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 33bc04cd-dc11-37d1-9ed1-db88005d417d | -7.05053 | -44.11552 | 2025-09-16 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0984cd26-0990-3d4d-85cd-9d2b791efd87 | -6.18716 | -41.17662 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6ac3d973-acf5-363a-b4de-e3ae40b04695 | -5.98677 | -45.80382 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da47c01e-7682-3748-9560-9755513e8773 | -6.47267 | -46.00497 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dacd203d-12bc-3898-a2a9-3a2e399fa158 | -6.53049 | -41.82988 | 2025-09-16 04:27:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4b352ed4-a30d-3a81-8bad-25c81e70422c | -5.7996 | -45.93832 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a76ab77d-9230-34a2-804b-06b73707521f | -6.31012 | -44.56346 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d851e5f9-e43e-3afc-ba01-b6bae8eb7dd0 | -5.77436 | -43.92908 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d00285d-a8ef-397d-a1aa-cced7a711523 | -5.9735 | -45.8231 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8dea4fab-c8ad-3b87-badd-0cd88f7e0932 | -7.27054 | -46.6085 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e19c28a1-a6a8-311e-9884-5211256edd67 | -5.80219 | -44.86761 | 2025-09-16 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README32.md)
