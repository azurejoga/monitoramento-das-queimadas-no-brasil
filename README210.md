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

## Dados Diários - Página 210

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c10bfa1-b8dd-38a0-9dee-0088914120bb | -6.20335 | -52.7907 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b3dd1da8-cb89-38d4-af32-d5b3a6766fd5 | -7.47173 | -42.82288 | 2026-10-07 16:37:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 36.5 |
| d1b08968-48a3-389b-b006-69abe545be33 | -17.02113 | -45.90321 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 18.0 |
| f845f59d-5a48-31d7-84fd-779ef46a63f5 | -5.85394 | -42.65453 | 2026-10-07 16:37:00 | NPP-375 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 5b15c7a9-eadf-390b-affc-9ee7cfc17238 | -11.3499 | -51.87527 | 2026-10-07 16:37:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 74c13477-1719-3469-86d7-535889789319 | -6.93209 | -38.28697 | 2026-10-07 16:37:00 | NPP-375 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 538eb438-8566-3379-a3f6-62b8fcdab2e0 | -9.53353 | -46.85009 | 2026-10-07 16:37:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 68d87ff7-cde8-3cc6-8228-d1562b76b15a | -9.96794 | -43.48815 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 40f9ebb5-2f4a-38bf-84b7-2d127f1fd7cf | -14.81071 | -41.89221 | 2026-10-07 16:37:00 | NPP-375 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| dc7430f1-1fca-3c5e-84c4-94113bdd65c0 | -7.71133 | -45.44469 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5bd7ab3d-be61-3707-aa46-2a70c56f710f | -3.80636 | -44.60384 | 2026-10-07 16:37:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f6acb690-b250-3dac-a45f-8a7bbcd6ca88 | -9.96356 | -45.95948 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| fd7a2ae1-a12e-32df-86cc-999f56a1cb96 | -3.74675 | -44.69796 | 2026-10-07 16:37:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b6a1206c-fa63-3692-a5e1-062edd03c6e7 | -7.77375 | -44.9096 | 2026-10-07 16:37:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ee3df44e-98a2-3880-b26c-ab5db423954c | -11.10194 | -45.67794 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 58530f17-14f5-3fba-8687-ffd780bfcc51 | -10.00074 | -39.17505 | 2026-10-07 16:37:00 | NPP-375 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 41.1 |
| 0d1cba36-dc66-3782-aaad-7baa2196bdbe | -15.34787 | -40.83388 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 44.9 |
| a8d59154-d59d-3434-bb27-a64285e3f1c1 | -5.86782 | -45.19847 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 64fbb31a-c5db-3b58-a90b-668257daf68c | -6.05505 | -47.31944 | 2026-10-07 16:37:00 | NPP-375 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 9d232638-72b3-3d81-ae96-9ee5e5c4931d | -16.04883 | -40.64843 | 2026-10-07 16:37:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| ae3fa2ee-f674-3c4c-8d57-334e1c5ad5cb | -8.21645 | -46.35983 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| cce69091-0411-326e-a21f-82019053a74a | -11.0988 | -47.58237 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1b8598fc-2c35-3770-b08e-3c2eb986aca3 | -6.48446 | -52.81879 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0ebc0b5d-9da1-3e52-ab8c-950e9e0974cf | -6.6801 | -44.96289 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e9137988-2daa-3b02-9bc9-c33a27941ea5 | -6.6868 | -44.96189 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9efcc44e-fb11-3b6f-99f5-70f25859bd31 | -6.79523 | -41.24426 | 2026-10-07 16:37:00 | NPP-375 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 31bf7160-9e4a-360e-9ad9-5f59a6727140 | -10.10425 | -40.16825 | 2026-10-07 16:37:00 | NPP-375 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 3cf3e78b-d3dd-3697-acc6-96b6e095d52f | -10.38092 | -46.25477 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cb8ecdde-ed21-3bc0-b866-347f1e172c07 | -9.15946 | -45.82199 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 021ba012-ef03-33bf-be45-42451705cc5a | -5.39471 | -42.79762 | 2026-10-07 16:37:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 24.2 |
| 3907ddbc-a2a9-3a0a-b613-8b43fdbc722b | -4.20293 | -49.70521 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 9676ab51-0a60-30db-87b6-bb933dc5427c | -5.85451 | -42.65818 | 2026-10-07 16:37:00 | NPP-375 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 32.5 |
| e752d356-c852-3700-9fcc-884ad6ac8f11 | -9.94765 | -43.55581 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 232.2 |
| 1602666e-46f8-39da-be75-96a739540177 | -4.52387 | -43.72924 | 2026-10-07 16:37:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9d16b56d-f1f9-3bec-8f71-ccb94919939e | -9.95151 | -43.5588 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 89f17046-6afc-3ddc-850b-d9c19cc982c8 | -10.07484 | -45.9846 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 27585b6e-b974-3fde-9808-02525ca2bc90 | -6.26895 | -52.84216 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 23491419-498a-393b-9872-ffb3ba1553ed | -8.01456 | -39.62233 | 2026-10-07 16:37:00 | NPP-375 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 35817ba5-e9e8-3f4f-8a24-61d20cec680e | -6.49329 | -35.5894 | 2026-10-07 16:37:00 | NPP-375 | TACIMA | PARAÍBA | Brasil | 2516409 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5610913b-b709-3812-9f37-ba32041a7416 | -6.19409 | -53.18349 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7112e72e-9c99-3098-8115-2b93652a4941 | -11.15085 | -46.12374 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2bac82c3-8c0f-387c-97da-32566b2c204c | -7.17581 | -43.7104 | 2026-10-07 16:37:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 57f6a6c8-8fba-3da3-ba9b-dd29839ebfb5 | -7.27362 | -45.57122 | 2026-10-07 16:37:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| eabb3159-20bd-32ff-9e81-e7b46661a25d | -4.75308 | -42.59851 | 2026-10-07 16:37:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 6db408bf-b9e2-356c-a49d-49b179e10f6f | -6.0697 | -51.65823 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6a4aa857-c0ef-32cd-9f3f-6a28fd217327 | -3.23809 | -44.04786 | 2026-10-07 16:37:00 | NPP-375 | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e396a97c-151d-3a9d-9607-cec29d7e1ac5 | -9.37604 | -45.92629 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| ff5af435-1004-3e6c-bb61-df1916c913e6 | -2.99828 | -41.42855 | 2026-10-07 16:37:00 | NPP-375 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 78d0e52f-3a0f-3708-a7db-f0ce1478ab26 | -6.96149 | -56.4191 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| bc25c5d3-87e3-36dd-9bf9-e65dc2ce9fab | -3.81303 | -45.40011 | 2026-10-07 16:37:00 | NPP-375 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 49a9b159-cb50-385a-a71c-83416236714b | -9.88524 | -44.83151 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 8ac1a695-9cdb-3297-a103-bcae3d918bcc | -9.03558 | -46.89785 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 503c4a0d-debf-37c7-99de-882d2e27ab93 | -9.81912 | -47.47387 | 2026-10-07 16:37:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9480239b-4185-3f69-8b11-46d8ea59c099 | -17.01491 | -42.32294 | 2026-10-07 16:37:00 | NPP-375 | FRANCISCO BADARÓ | MINAS GERAIS | Brasil | 3126505 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b4cb6b72-625b-30fa-9111-b5a6c1afde42 | -3.66456 | -41.44449 | 2026-10-07 16:37:00 | NPP-375 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 64026f00-8e59-31e0-8b27-445f1bd57165 | -6.68192 | -52.97228 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c24f9877-dc63-388c-ade5-decf44ad45a8 | -10.94527 | -54.99946 | 2026-10-07 16:37:00 | NPP-375 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1750bb74-7563-3f47-806c-2ad9f8183bfd | -3.7543 | -41.7111 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 83e85b9a-b25f-3ffa-adc4-4fda0015930e | -15.53466 | -41.24335 | 2026-10-07 16:37:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 57.5 |
| 11706e67-513a-3123-9af9-9f64261a9a92 | -8.76459 | -44.15361 | 2026-10-07 16:37:00 | NPP-375 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| c889c679-eb47-3a5c-a647-ed82d0becc24 | -6.9382 | -45.28737 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2264e39d-9672-3848-a9b8-92a71ffe1070 | -5.34526 | -45.69052 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| acb20125-6afb-3cf9-b861-0b36a23ceb33 | -4.13425 | -45.11143 | 2026-10-07 16:37:00 | NPP-375 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d99e225c-49dc-3028-ae6d-0fba0609f3ca | -5.10588 | -42.91771 | 2026-10-07 16:37:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 3a898fca-d2e2-3b2b-b767-6589b6c4d4c0 | -14.61632 | -40.04166 | 2026-10-07 16:37:00 | NPP-375 | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8a788d9a-987a-3656-a809-e7e4bfa6b179 | -17.03071 | -45.91687 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c7b9a39d-79f7-3206-ba6f-adc028786f1c | -8.95141 | -45.11263 | 2026-10-07 16:37:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7d01208a-f246-3b10-8d03-ee7baee60393 | -5.01985 | -42.45419 | 2026-10-07 16:37:00 | NPP-375 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| cb942c57-942b-38c2-a9a1-47edb5131f8d | -6.37577 | -55.15485 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1f4c0adb-baea-36f1-9687-497bf0bc319b | -8.29627 | -45.46552 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 7dfd9920-5ede-3bdb-937b-2b77e56b050a | -8.20992 | -46.36465 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 31ae9179-b1a0-3e44-abd0-9514c0e0139b | -8.21348 | -46.36423 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| ebbeac51-38d5-3b2f-b2a5-48a29b24871c | -17.02176 | -45.90813 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| f93c7976-ae39-3ad1-a476-35d59e9b9d2f | -6.99685 | -43.97695 | 2026-10-07 16:37:00 | NPP-375 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e3af4f00-b434-308a-aca8-792454d45111 | -5.72004 | -41.7435 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| da081640-d2d6-3ad2-84bc-363752b6b09e | -8.21348 | -46.33971 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 16ae4ece-fe02-3718-9723-38527f052940 | -5.50184 | -42.83658 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| e2c7405e-6cb8-38c5-bfb7-3f44bead14ff | -6.21895 | -52.78865 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 05663577-dc98-3be4-a22e-c6a7c0a2d002 | -6.34671 | -38.86758 | 2026-10-07 16:37:00 | NPP-375 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c26bbaba-2c55-312e-9770-f0bdcedcd6d7 | -5.39587 | -41.14484 | 2026-10-07 16:37:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| f3df75b2-7b1a-33bc-8f61-7cc4b0e84a19 | -6.98187 | -45.12012 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a9f54e30-01e9-34dd-a8bd-3b9c61d33e9c | -4.77194 | -49.38105 | 2026-10-07 16:37:00 | NPP-375 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 028cd657-6d23-361f-94e2-f4cb74d8b9f3 | -5.97219 | -40.92104 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 55.2 |
| e12e14c9-c339-32c8-9792-65d8af71a2b1 | -11.14615 | -47.29682 | 2026-10-07 16:37:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 55ec9af9-9d52-324e-8a1b-9f8ad3a7fa14 | -8.54067 | -54.58328 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 153b84ed-a473-3a1d-833f-431c1e00da8c | -6.5873 | -53.0225 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ae890554-b1ba-3de5-b6bb-552114edf5e9 | -7.83234 | -44.18219 | 2026-10-07 16:37:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 44efba25-30b3-3e0e-82b6-941385bf421f | -15.63792 | -48.25419 | 2026-10-07 16:37:00 | NPP-375 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| dfa63f88-6cb7-3bc2-a58a-53f797604da7 | -5.48787 | -39.72217 | 2026-10-07 16:37:00 | NPP-375 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 00bbc662-3380-3962-a7a2-2b44749d137d | -3.8642 | -44.14141 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| c1871e83-9784-3606-b797-fd143c5cade6 | -3.51729 | -43.84246 | 2026-10-07 16:37:00 | NPP-375 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9ea9f971-0d4b-32af-90df-bcae3aaf039f | -6.68063 | -44.96643 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3c571daa-a93f-3116-86dc-c71ab91cd783 | -9.14952 | -45.82724 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bb1e9a33-c37a-3a8d-bc69-b8c207109ef7 | -4.37948 | -41.84043 | 2026-10-07 16:37:00 | NPP-375 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| dc2e05e4-ce78-3e2b-a019-c1974e2ea3bc | -5.96759 | -43.52522 | 2026-10-07 16:37:00 | NPP-375 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 82991a57-ac84-31bf-b90f-7178817371e4 | -6.12794 | -47.92331 | 2026-10-07 16:37:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0f8c0320-7a24-3c9f-8996-b2e3c493b9ee | -5.76883 | -38.56502 | 2026-10-07 16:37:00 | NPP-375 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 19.1 |
| d98a215c-7f9b-3d0d-9a5a-9618d346f65e | -6.21915 | -53.02158 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1ee6656f-28a8-330a-a590-dc6c43b72b6c | -5.73426 | -45.16467 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 169.4 |
| 0781d2da-4e7f-316b-8213-736eaed5b418 | -9.44997 | -45.81923 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |


[Clique aqui para ver as próximas entradas](README211.md)
