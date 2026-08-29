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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b3d958b-4978-39fe-ab42-ac00d00c9e58 | -8.9614 | -63.2601 | 2026-08-29 15:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 98d324aa-9486-3b69-8280-7e8c6a285ba6 | -11.2506 | -53.9941 | 2026-08-29 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 54e6ea38-0eeb-3540-a482-bb9f0dbf930f | -7.0817 | -42.1585 | 2026-08-29 15:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| 99e8bbe5-7f42-3411-bfe6-7335804c5a82 | 2.2375 | -50.7515 | 2026-08-29 15:00:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 35b144d6-baa8-375d-adba-40e1bacd4238 | -10.8425 | -50.5005 | 2026-08-29 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| d8d1bf21-33ff-35f9-89f2-4d6d653e95fa | -11.0254 | -57.2237 | 2026-08-29 15:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 71df1179-1277-3b12-88c9-8e7127914a9d | -6.7832 | -59.4401 | 2026-08-29 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 29108f2a-43e1-3a92-aebd-2f42482aa949 | -11.1995 | -55.1008 | 2026-08-29 15:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| b03deacf-4b1d-36b2-91aa-4ccede8670b6 | 2.256 | -50.7511 | 2026-08-29 15:00:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 95030a8f-744f-34dc-90b5-8286afce954d | -13.8567 | -54.0759 | 2026-08-29 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| a53a3366-559c-3f08-a1a9-dda9a24920e6 | -6.5508 | -55.2368 | 2026-08-29 15:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 4877de58-6ae6-3042-b2c6-0bfaad38c8e0 | -8.948 | -62.3894 | 2026-08-29 15:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 89.2 |
| fc3553ee-fa4d-3ced-aef5-7a44da8ddd3a | -1.2541 | -55.7101 | 2026-08-29 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| c9078817-e6e6-3d28-8a15-71d982a11eb7 | -10.7598 | -54.0179 | 2026-08-29 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| cd3c418b-2f4f-3329-9c12-4177174e66b4 | -11.2302 | -45.0528 | 2026-08-29 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 61e2e9ef-e1a1-3497-9955-9fb7510cd4da | -8.9428 | -63.2797 | 2026-08-29 15:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 142.0 |
| 91b8d093-4ed7-3e6f-804c-1cdb88206a2f | -20.8979 | -57.7014 | 2026-08-29 15:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 68.0 |
| e8dede53-a753-3c7c-bae5-ec2eef23ff63 | -10.5404 | -50.4683 | 2026-08-29 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 6349e7d5-e170-38e9-b3cf-967984eb7f3b | -11.2125 | -54.0181 | 2026-08-29 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 2f06e4b6-92af-36d9-991f-e75714fb250d | -10.7596 | -54.0384 | 2026-08-29 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.3 |
| ba4961c3-2694-368f-bf13-b3c2922e5e80 | -8.631 | -66.5473 | 2026-08-29 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| a7319583-e258-3409-b356-de4f30f84a50 | -8.7767 | -49.9977 | 2026-08-29 15:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| b4f73421-f11c-3ffe-ab6f-605e4035c7da | -13.856 | -54.1175 | 2026-08-29 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 0650e3c3-c715-3813-b39b-3cd65d52d111 | -8.8184 | -49.6308 | 2026-08-29 15:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 7156227b-d837-35ac-82e1-21463ac2e1d2 | -11.7167 | -54.5244 | 2026-08-29 15:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 137.7 |
| ce711d0b-5a21-3aa5-863c-8e99e099f387 | -8.9478 | -62.4084 | 2026-08-29 15:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 6922acaa-3f22-312f-bd04-3d76b6f5d8e9 | -7.5139 | -55.2851 | 2026-08-29 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| baa2e45d-879b-37ce-86c8-a9259394773f | -6.6129 | -43.7317 | 2026-08-29 15:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 9eadde89-f365-37a1-b8bc-10e844ec2b60 | -7.1003 | -42.1805 | 2026-08-29 15:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 103.6 |
| 9d9acd21-ffd0-387c-bafb-f7ed52143f07 | -14.3863 | -50.0565 | 2026-08-29 15:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 14d3319b-dbf7-311b-957a-6082d9633a52 | -10.8804 | -50.4965 | 2026-08-29 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 8fa7f3ba-23e4-396d-ac69-b1222cd0fefb | -9.1739 | -56.9754 | 2026-08-29 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| fb3cce65-9f3d-3156-ba7a-accbb0160813 | -8.5968 | -54.7957 | 2026-08-29 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| c1b87421-4944-38ab-937b-a8f58078aad5 | -11.7028 | -47.6129 | 2026-08-29 15:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| a6ae2f02-ddf1-3eeb-a656-8c369818e773 | -11.2489 | -45.0732 | 2026-08-29 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 2f1074dc-31d8-3d75-ab5d-4b6f1f5c3131 | -7.0057 | -59.2575 | 2026-08-29 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| c76ea2d7-703e-3b0e-90db-b696dd049261 | -11.0244 | -49.6872 | 2026-08-29 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 49ba9c30-da22-3e7e-8aa1-e96f6cf4a691 | -8.9929 | -50.785 | 2026-08-29 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 860fe57b-fd52-3434-a417-6824ca2b9332 | -10.3391 | -49.9762 | 2026-08-29 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| b14f45c0-e6e6-3447-9224-08c4872dbce0 | -11.1919 | -51.2496 | 2026-08-29 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 40ff80b0-3a59-361b-9cae-0abe6c2bb717 | -11.2128 | -53.9976 | 2026-08-29 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| eb132183-612e-3e46-914b-baa298b459ea | -3.9363 | -59.3381 | 2026-08-29 15:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 0f58dee2-f009-3319-942c-449afbc5f35a | -10.8235 | -50.5026 | 2026-08-29 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| a424ddbe-5f9e-36ce-b476-cabbe4ffa7df | -6.6315 | -43.7533 | 2026-08-29 15:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 174bd3b9-ec0b-3bb2-87c3-544d94d00639 | -20.9414 | -57.5484 | 2026-08-29 15:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 58.1 |
| 94672467-7a0f-3986-9588-19242d9330f7 | -11.3622 | -45.1494 | 2026-08-29 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 191410c3-cd5e-3fbb-96d2-623cdfef9d5e | -8.9613 | -63.279 | 2026-08-29 15:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 152.8 |
| 9162d630-7ddb-3ac2-b1a7-75b3b48bbe0d | -10.8463 | -50.2224 | 2026-08-29 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| ec19db61-4264-35ff-9010-7a45c650e00a | -9.2094 | -51.5444 | 2026-08-29 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 96b109c3-d5db-39db-969e-fb5a5e741ca3 | -11.1726 | -51.2728 | 2026-08-29 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 280.4 |
| 8ed30689-3529-39b6-8798-1062735b6627 | -6.5507 | -55.2568 | 2026-08-29 15:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 3e729080-f20d-3b3d-a360-db2e33403b12 | -15.3849 | -52.6677 | 2026-08-29 15:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| a03ee77a-d805-306e-86f8-77459280bced | -13.9919 | -54.0189 | 2026-08-29 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| f21599d7-1f05-3e8e-9d9a-9833651b6c73 | -6.7515 | -55.6455 | 2026-08-29 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| d96e29cd-3ecc-35f8-857a-5357ad8bfd27 | -7.1309 | -48.0672 | 2026-08-29 15:00:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 4a4c6a00-f4f2-353f-83d0-4ee1d61a9b29 | -11.2503 | -54.0146 | 2026-08-29 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 02961238-a000-34d4-b2af-4f0b4cf042c1 | -10.4609 | -64.4831 | 2026-08-29 15:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| e9bd72ab-f689-34cb-9b47-f04c601e515a | -11.1916 | -51.2708 | 2026-08-29 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 183.5 |
| 44008897-46ae-36ea-a7f0-95ef68f41d90 | -11.1729 | -51.2516 | 2026-08-29 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| cd96d78b-2205-3647-8924-d71012a70d82 | -9.971 | -53.9214 | 2026-08-29 15:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 3e9438b3-da3f-3a8c-aee7-9d3ae1859357 | -14.4193 | -52.5625 | 2026-08-29 15:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 9ad08daa-6ea8-38ac-9a25-d10c1372e48d | -6.9303 | -45.6931 | 2026-08-29 15:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| fcb2703b-5121-3556-9203-193fe4c45c2b | -6.1656 | -57.7988 | 2026-08-29 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 83890f1f-bf2c-30ac-b11b-6e5c2a998703 | -9.9896 | -53.9404 | 2026-08-29 15:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| cc567878-e7c1-3b7b-9546-93f05d3ec3af | -8.7769 | -49.9763 | 2026-08-29 15:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| e731638e-d87e-3c56-a4c0-e3134ebdf6b2 | -11.1913 | -51.292 | 2026-08-29 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 9f277d73-1437-3020-9936-1014e9fca319 | -10.8232 | -50.5239 | 2026-08-29 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 21324599-c90b-34d9-b4a2-d3b0c3d51647 | -15.3846 | -52.689 | 2026-08-29 15:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 515db80f-a1b6-342d-a399-9c0073df296f | -8.9741 | -50.7866 | 2026-08-29 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| abc27d1d-7bf8-36f2-ad50-dafa4481ef6b | -9.971 | -53.9214 | 2026-08-29 15:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 82523cf9-e331-34b0-b1b8-f348d2d541b6 | -7.4952 | -55.3062 | 2026-08-29 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 2cb5c29b-6171-3f98-8b68-84bea3a972f3 | -7.3089 | -45.3666 | 2026-08-29 15:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 626908df-6cc9-3b40-8f3f-9ba4b5dd6e68 | -6.6317 | -43.73 | 2026-08-29 15:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 157.0 |
| aa3479cf-7108-3a64-b080-2392d0e127df | -9.2094 | -51.5444 | 2026-08-29 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 6a162b40-e082-3fbd-a24c-2d5eb5f1e45b | -10.8463 | -50.2224 | 2026-08-29 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 9e76a4b3-c54d-3795-8969-055d6fcedacb | -7.9838 | -45.5072 | 2026-08-29 15:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 32291920-9880-3cf3-a91c-823c9eb702cd | -7.5662 | -61.3049 | 2026-08-29 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 187.5 |
| bbc1f923-32f4-30d7-9004-7003041b392b | -8.9613 | -63.279 | 2026-08-29 15:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 947240f8-8e67-3383-8c30-88689af24bf4 | -11.006 | -49.6461 | 2026-08-29 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 7560deb3-5aad-302d-9dc2-c7fa9f6a794d | -11.5279 | -45.5162 | 2026-08-29 15:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 154.8 |
| bbc3ae34-efc3-39df-b6c4-cb708dae4729 | -11.1639 | -45.5897 | 2026-08-29 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 912f6288-615c-35f6-98eb-a5ba05275a8f | -6.5508 | -55.2368 | 2026-08-29 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| d224c9c5-a2e4-307f-8f19-dc26c6a3da2a | -11.0054 | -49.6893 | 2026-08-29 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| b5a626da-5b3e-3fa9-aacc-735f7400e9cf | -8.6694 | -49.5369 | 2026-08-29 15:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 5fc3dd6c-6e1d-31a2-ab8a-4a26feca7d0d | -12.1902 | -50.5409 | 2026-08-29 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 136672fe-f784-3262-ad43-1b043a50421f | -8.9428 | -63.2797 | 2026-08-29 15:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 141.2 |
| 447ba762-3999-3d6b-8c6d-abaece4053d6 | -11.2298 | -45.0759 | 2026-08-29 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 71ef0445-3ca2-3172-84d1-4b8f334d6327 | 0.1367 | -60.393 | 2026-08-29 15:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 1c68487a-74c0-3c9b-8785-93a922e53afd | -14.419 | -52.5837 | 2026-08-29 15:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| c3f3de03-8438-3479-8374-b42777b55f0d | -11.245 | -45.3037 | 2026-08-29 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 5a0d3730-3c56-3f3a-8671-db3264ce8d5a | -11.2489 | -45.0732 | 2026-08-29 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| b5f061fc-fd7b-3ab6-8287-6948bc095c18 | -7.1003 | -42.1805 | 2026-08-29 15:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 100.1 |
| 40f5802b-0c32-34fd-ae7b-5e46a5b4a489 | -8.9614 | -63.2601 | 2026-08-29 15:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 2c2b5636-4bff-396c-a01b-e8369e99fb0c | -10.7598 | -54.0179 | 2026-08-29 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| bf34f413-f668-382d-bf7e-b1dc289e3c4c | -11.6975 | -54.5467 | 2026-08-29 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 58472e03-e92d-3d59-ae47-2a6abda2db60 | 2.2375 | -50.7515 | 2026-08-29 15:10:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 11be070a-6726-3857-8bec-5f5c52dbd1e5 | -10.5785 | -50.443 | 2026-08-29 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 2639b369-5220-371f-b7a9-f8bd62b564a6 | -8.167 | -47.5201 | 2026-08-29 15:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 8e5c7aed-5881-388d-b8f0-7a0094751858 | -11.1723 | -51.294 | 2026-08-29 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 2416cbf5-e967-3635-826b-19c7aa67b04b | -6.7691 | -58.6873 | 2026-08-29 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |


[Clique aqui para ver as próximas entradas](README84.md)
