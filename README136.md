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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 083cda2c-5f5f-3438-be56-c51014a76d2a | -6.1732 | -42.6458 | 2025-09-12 14:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 3e4e0122-e32b-38e4-b790-05297c5fb7be | -9.0793 | -49.7997 | 2025-09-12 14:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 2ef07234-ee5a-3556-a47b-7b41d8c78d7a | -7.853 | -43.8693 | 2025-09-12 14:20:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 3fda7676-44d2-3abf-a105-116c6d779601 | -15.0788 | -52.4331 | 2025-09-12 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 101.4 |
| ec4052fa-1fee-3d64-b32e-32f7d47a53ce | -8.2085 | -45.5981 | 2025-09-12 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 111.3 |
| a709a801-f450-38d0-b29f-05302aaa27de | -11.6813 | -46.6084 | 2025-09-12 14:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 3babf476-cdf9-3fa1-b122-2fe8e21ff415 | -15.5822 | -54.7429 | 2025-09-12 14:20:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 39b22208-af45-36d7-b602-bd6f6fe5d012 | -8.0526 | -44.4961 | 2025-09-12 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| d48049a9-bb3b-3cb4-81b5-6096ac981c23 | -10.8972 | -45.58 | 2025-09-12 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| beb6d0a0-e204-3a63-b241-2d1969c6cb4f | -9.4807 | -46.4096 | 2025-09-12 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| e2527124-2393-3fb7-90db-c76b2536a0c2 | -10.0754 | -47.1686 | 2025-09-12 14:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| b9a0992f-5c54-3810-a7c8-127c8e5d1351 | -12.8649 | -62.1268 | 2025-09-12 14:20:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 5eeb0030-d14b-37f8-b8fc-e02a053b90ef | -6.1698 | -41.1387 | 2025-09-12 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 177.3 |
| 5b9a915a-3682-396c-bc3f-f02627a54219 | -14.4588 | -47.3174 | 2025-09-12 14:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 132.8 |
| affc0681-db70-32a6-a836-d1bc987f886d | -10.679 | -48.6633 | 2025-09-12 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 2f622a57-688d-3db4-8059-f2be12c158b0 | -10.8968 | -45.6029 | 2025-09-12 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 9c94ad9c-235f-316e-a5c7-7791520003ee | -6.6837 | -44.142 | 2025-09-12 14:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| ba8b0cf6-f446-3cfc-8947-cd6a93f7ed8f | -14.444 | -53.4016 | 2025-09-12 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 6716ca1b-0680-35d2-aa0d-abaf79299b9a | -9.7197 | -46.8972 | 2025-09-12 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 280367c5-103a-33f7-a06e-b8478ffa498a | -11.5425 | -50.5947 | 2025-09-12 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 213.1 |
| 9e80eb0e-0e57-38c2-bd9f-35fdae931312 | -8.4893 | -47.2694 | 2025-09-12 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 6316900b-4d2c-36cd-811f-ca4004e99a98 | -16.9621 | -45.8176 | 2025-09-12 14:20:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 198.6 |
| 5741b6f2-a07e-315c-bc74-2f6fb162affd | -8.9749 | -46.1054 | 2025-09-12 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.9 |
| cbbdfb4d-b936-3957-8991-5dc0d46434fe | -8.8768 | -51.111 | 2025-09-12 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 2d1293a1-5630-3b81-88b0-61a4c9d1613a | -10.4441 | -50.6059 | 2025-09-12 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 6e3d93a5-af37-3172-a99f-735a8f424b4d | -8.9938 | -46.1034 | 2025-09-12 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 126.2 |
| b94b7e06-f771-390f-990a-97b095c9cb33 | -7.321 | -49.6468 | 2025-09-12 14:20:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 7fa39294-35a5-3f78-b42e-d027c8ba1994 | -10.0947 | -47.1441 | 2025-09-12 14:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 5e100318-f343-3233-a410-195dcc00d040 | -8.956 | -46.1074 | 2025-09-12 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 1024e3ae-4a3e-300b-8070-017fd36d04ec | -10.7172 | -48.6371 | 2025-09-12 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| f076237b-c61f-32a1-8403-795633df0d17 | -9.4804 | -46.4321 | 2025-09-12 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 145.8 |
| fb6471bf-eec1-300e-a500-4fe1704b8cbd | -15.5819 | -54.7637 | 2025-09-12 14:20:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 96744386-70c7-3fa7-8fd2-b660da1affcf | -8.4143 | -47.2545 | 2025-09-12 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| fef1685a-68db-3227-9ec3-853959a850d5 | -10.6983 | -48.6393 | 2025-09-12 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 8211a2b3-5aac-3abe-b89d-3a2c90532d3d | -8.9368 | -46.132 | 2025-09-12 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 136.2 |
| f0eed88e-7875-3275-8b4c-08e93ee0a0b3 | -9.1331 | -46.9831 | 2025-09-12 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 610b6e92-71ed-3c56-9225-c35052e0e1ad | -10.0943 | -47.1664 | 2025-09-12 14:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 498.7 |
| 68ea2ba8-da15-3922-b0f9-9432f4d7b3cc | -4.553 | -43.7439 | 2025-09-12 14:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 9e8cbacc-c005-342a-b739-c40be642f13e | -6.3092 | -42.2072 | 2025-09-12 14:20:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 5a71cc95-7b37-3fc8-9de3-ddeac42ededd | -9.0759 | -47.0335 | 2025-09-12 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| e5822e7e-9c99-3768-8ba3-761d88b43bb3 | -6.1891 | -41.0884 | 2025-09-12 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 485.5 |
| 53211348-b388-33a7-bba0-a8b67a1e74fd | -9.751 | -46.0185 | 2025-09-12 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 640e5af1-eaa8-3980-af7a-5f087220bb24 | -12.7696 | -44.7737 | 2025-09-12 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| cb3297bc-3934-3a0f-ae15-ffd7b4a0c4b9 | -6.8182 | -45.6574 | 2025-09-12 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| c0be7a2d-9874-30ee-8111-13a5e2a4bfb4 | -11.9717 | -51.1427 | 2025-09-12 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| a042d4d1-7a44-3f41-8dd1-75f6f9efd519 | -8.9371 | -46.1094 | 2025-09-12 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 0fbb263d-c186-3387-a81e-11fb0a7f4c5c | -10.4252 | -50.6078 | 2025-09-12 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 08b3b2d0-3dfc-3d33-b605-b3e6a8170a68 | -10.1405 | -47.9133 | 2025-09-12 14:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| f714aab0-28ad-3fbc-acf2-4209d582b860 | -13.2414 | -51.7359 | 2025-09-12 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| eed71b6a-ca04-3ddb-a38e-7e4adee7ce53 | -7.2374 | -55.0604 | 2025-09-12 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 7319fb5d-67c9-3c39-8d2f-6e64fcdd0ac4 | -11.7192 | -46.6257 | 2025-09-12 14:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 174.5 |
| ee049d6a-fc8d-3e00-b274-dc1b7d9dd214 | -7.4508 | -44.4407 | 2025-09-12 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 5e10dd3b-e6df-3e59-ae7c-5c84cecd774a | -9.77 | -46.0163 | 2025-09-12 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 1c8e18cb-8662-3fb3-bc3e-8de46916fa7a | -9.5324 | -54.6277 | 2025-09-12 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 131.2 |
| 2d83803a-2037-3480-b702-a1b051d63cab | -6.2588 | -43.4828 | 2025-09-12 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 601daa9f-a1cd-31a8-8821-ef1155797c10 | -8.4331 | -47.2527 | 2025-09-12 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| a873bd50-4959-36c5-89a8-c63cc788ca86 | -9.3433 | -45.4082 | 2025-09-12 14:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| b94e3462-ef7a-3096-a578-e223e007634e | -7.5641 | -44.4068 | 2025-09-12 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 126.7 |
| bebd7ff9-8052-3f40-9e28-173281769d9f | -16.3623 | -51.4969 | 2025-09-12 14:20:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 91.8 |
| f91b482c-0f77-361c-9626-f2cc3d95b39d | -8.8899 | -49.945 | 2025-09-12 14:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| ba4119f8-355b-358e-8b95-28e46f584067 | -9.0382 | -47.0375 | 2025-09-12 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 5b760b47-5a31-3955-b96f-6f193044780b | -12.9289 | -54.7744 | 2025-09-12 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 4b201473-5c84-366c-90c1-e37a74e93b88 | -11.5422 | -50.6161 | 2025-09-12 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 332.8 |
| c1a965d4-0367-352b-892e-ddc8de370625 | -9.3436 | -45.3853 | 2025-09-12 14:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 832cfc13-24ca-347c-861a-906fb912d971 | -9.0376 | -47.0819 | 2025-09-12 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 06c747f8-9bd7-3fbd-a893-42401208fa50 | -9.6473 | -48.0548 | 2025-09-12 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 9a440d93-c7a1-3788-94c9-3c7c536f4595 | -9.4993 | -46.4299 | 2025-09-12 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 2c296f81-6feb-3680-8ced-be6389769f63 | -8.414 | -47.2766 | 2025-09-12 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 5b7bdcdd-b248-38ad-a26f-64af30197c25 | -8.096 | -45.5641 | 2025-09-12 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 8ae4747a-b2a4-3afb-ba5c-1e251337c5a8 | -16.9615 | -45.8411 | 2025-09-12 14:20:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 125.5 |
| e9ea10c7-3bc9-3211-a044-81919b12dd2a | -10.4249 | -50.6291 | 2025-09-12 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 72e584fb-34e1-3139-9a97-cb4ac46e2f89 | -12.9292 | -54.7538 | 2025-09-12 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 246.5 |
| ae434b65-54c9-3821-979a-5730c4f52c6a | -11.1949 | -48.4277 | 2025-09-12 14:20:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 71518735-0bd1-30bc-a3d7-b3ad4e091fd7 | -10.0717 | -46.116 | 2025-09-12 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 4527f352-b1eb-39e6-a9f6-cbb180936341 | -6.1735 | -42.6221 | 2025-09-12 14:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 125.6 |
| 9b1f3eaa-bc7e-3802-bf06-53cfa094737a | -11.6622 | -46.611 | 2025-09-12 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 4f4740c6-acde-3218-bd85-e2af579de0e8 | -7.5455 | -44.3856 | 2025-09-12 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 3ee42a3f-445b-3bf5-bf60-180dcc012873 | -9.057 | -47.0355 | 2025-09-12 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 2360d3c5-b9bb-3f8f-9e8e-39bc883a75d8 | -11.4473 | -43.5751 | 2025-09-12 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.4 |
| ed589e42-5bfb-3639-8218-6a4b826bc6fb | -9.0379 | -47.0597 | 2025-09-12 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 3ce826e6-6cdb-3a55-9e87-dcd75d9d9952 | -8.4705 | -47.2712 | 2025-09-12 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 271dfb9f-691c-3be0-8e0d-68675921c272 | -11.4477 | -43.5514 | 2025-09-12 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 187.0 |
| f696cd28-20aa-38dc-b548-1e2a7b187871 | -11.9523 | -51.1661 | 2025-09-12 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 0444806d-3eec-3b00-a563-b0f13012e0ea | -15.1363 | -52.4679 | 2025-09-12 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| d8923a31-6647-391f-9415-b1e7885f781c | -9.1162 | -49.8604 | 2025-09-12 14:20:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 3989e978-f39c-3671-be23-70056715f232 | -9.9571 | -50.3353 | 2025-09-12 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 102.2 |
| b6d031a5-5789-3516-8be2-2f02fdd3d009 | -9.6827 | -46.8345 | 2025-09-12 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 966f4556-4b9b-3fe2-9d68-97b5d1d3a13c | -7.5452 | -44.4086 | 2025-09-12 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 9f746226-c0c9-37b0-9a2b-153b328ba31a | -11.9332 | -51.1683 | 2025-09-12 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 14692462-0f3f-37a9-b0bb-611e37109855 | -11.5232 | -50.6182 | 2025-09-12 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| ca238c34-9233-3ac3-bb25-ee9786512751 | -12.0852 | -47.5842 | 2025-09-12 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 99dfc65e-f9d7-3ac3-9159-4db4e39b72f7 | -11.6817 | -46.5858 | 2025-09-12 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| cfd0de1d-5781-3e64-8a77-d901b33673d8 | -4.553 | -43.7439 | 2025-09-12 14:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 4491ad09-929d-3b07-b465-c48977a0c62e | -12.009 | -47.5722 | 2025-09-12 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 636a7568-4470-35c9-a0fa-d5fed42528f4 | -9.0376 | -47.0819 | 2025-09-12 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 6df30046-369a-31a9-9c1a-6284eb541242 | -8.4331 | -47.2527 | 2025-09-12 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 90d8aa34-cafe-3b17-a24d-8a6252ceac61 | -7.5455 | -44.3856 | 2025-09-12 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 129.3 |
| a569bc60-3c8e-3b4b-b8cb-f7dfea076a0b | -9.1162 | -49.8604 | 2025-09-12 14:30:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 57775f70-ae84-3df8-af2f-84bd73ebbcf8 | -9.5688 | -48.2819 | 2025-09-12 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 30f3ed55-93b5-361a-94ca-486c5004302c | -8.0817 | -50.1836 | 2025-09-12 14:30:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |


[Clique aqui para ver as próximas entradas](README137.md)
