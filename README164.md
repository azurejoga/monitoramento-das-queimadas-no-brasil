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

## Dados Diários - Página 164

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ee9219d-c015-3927-95ba-ffc1832d0b60 | -11.8635 | -44.938 | 2025-10-05 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 96a4ba4c-2f5f-3f21-a09d-5da96a18cf15 | -12.4673 | -45.4925 | 2025-10-05 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 71a9d6fe-a57b-3233-afd6-aee403d8917e | -9.9204 | -50.2536 | 2025-10-05 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 68b372b2-3acf-37af-bf31-72ed91d52073 | -7.0369 | -42.78 | 2025-10-05 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 189.9 |
| 9a2343c8-0f47-30ba-82e0-f9dabb20c8e3 | -8.5953 | -46.3022 | 2025-10-05 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 6cd6cfea-38ba-3526-a286-aee9577cbb05 | -8.1891 | -44.1357 | 2025-10-05 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 6de8fc77-28ff-3e0a-88c0-ceb436048814 | -13.7473 | -51.3097 | 2025-10-05 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 275.1 |
| d50d2752-a63a-3d14-9b74-60d2b070757a | -6.1536 | -44.6675 | 2025-10-05 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 187.9 |
| 61171e93-3ceb-316e-946b-39f15443ae74 | -14.1611 | -53.0377 | 2025-10-05 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 449cee29-d260-320e-9190-c0f9611435ad | -11.0914 | -47.7351 | 2025-10-05 14:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| b4e5d7c7-e838-37ec-847b-f6e60c53946c | -11.4535 | -51.5177 | 2025-10-05 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 4a7878fc-5f89-3960-b52a-9cfb41311292 | -18.1769 | -53.3669 | 2025-10-05 14:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 66.9 |
| bce87e40-349e-3c12-8a4a-cff2d96c90ca | -6.6416 | -42.7934 | 2025-10-05 14:10:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 84.9 |
| 71f6b1da-32a0-3f78-896d-bc352d3e99ae | -11.823 | -45.0596 | 2025-10-05 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 248.2 |
| 8cbb794d-7414-3569-a4fd-baae365bfe63 | -7.4672 | -43.0438 | 2025-10-05 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 121.6 |
| b5a66af7-13fe-3e02-85ae-d9efe08d993f | -8.5581 | -46.2611 | 2025-10-05 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 17a85d5e-e1fb-355c-b4f0-9b4ad7067882 | -6.1538 | -44.6446 | 2025-10-05 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 171.2 |
| a1e30f25-ffb3-3b95-81d6-f3f9a99503d4 | -8.6138 | -54.976 | 2025-10-05 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 833a9c0a-4bb8-3b2d-877d-929b0965ed5a | -16.0016 | -50.9456 | 2025-10-05 14:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 698c0a93-4d9a-3e3a-a5bb-17d68c0eaa99 | -10.0504 | -50.4113 | 2025-10-05 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 113.3 |
| ad937e35-3046-36f0-959e-ff6ebf56b22b | -10.0692 | -50.4094 | 2025-10-05 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 5080f2de-4a7a-3c40-80f1-0a4823262988 | -9.0966 | -49.9263 | 2025-10-05 14:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| a2f1492a-d9d4-3fb8-890b-20c88ed4abe1 | -7.7938 | -42.5607 | 2025-10-05 14:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 152.4 |
| 20fc021f-c958-3ed1-bf46-9ded2ad0db28 | -7.6463 | -45.4262 | 2025-10-05 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 938d1f91-ed9b-3ad3-92b0-a80d8c48cfe8 | -7.0372 | -42.7563 | 2025-10-05 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| cc6f8d50-7eeb-3e9c-926a-97d9acf8aa78 | -5.9226 | -43.3236 | 2025-10-05 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 5b8f0042-b566-3cc9-9b68-55d37c93047a | -13.7284 | -51.2908 | 2025-10-05 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 153.9 |
| e3b80462-077e-31a1-8f36-b83c2d4dcb70 | -6.4076 | -43.6099 | 2025-10-05 14:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 267.9 |
| 41529828-14f8-3652-a25e-7023ecf4eedb | -9.9313 | -50.8898 | 2025-10-05 14:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 5b556714-36cc-3570-a478-777b1ff04e81 | -16.0966 | -51.0829 | 2025-10-05 14:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 198.4 |
| 8c8bb3c0-a344-318a-b3ed-cf20ba08ab6a | -13.3237 | -48.0547 | 2025-10-05 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 0bfff165-a1af-3c1d-aa00-976ef00e78da | -13.7476 | -51.2883 | 2025-10-05 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 164.9 |
| cfda9c2b-cd8b-3103-b94c-1958f7656015 | -15.3993 | -47.9487 | 2025-10-05 14:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 40907e08-6cc5-315c-b620-2a934248ce8a | -9.9556 | -43.7632 | 2025-10-05 14:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 134.2 |
| ba641df8-95d9-3f99-a8c1-c4ee429fecdb | -6.4134 | -43.0489 | 2025-10-05 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| a045b31a-a886-380f-bf38-e3f66e4d1546 | -9.283 | -45.6649 | 2025-10-05 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 28bbe37a-75f9-3405-bc50-e830eab51c96 | -8.1699 | -44.1608 | 2025-10-05 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 125.3 |
| f51f1ace-c97a-32aa-ba24-76ee90fa8645 | -8.8803 | -47.6061 | 2025-10-05 14:10:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 0a784a25-a2bb-348e-bf4a-f13941f6a596 | -8.539 | -46.2855 | 2025-10-05 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 157.9 |
| bc845bc8-e393-336f-87d5-e598aa386cfa | -7.2389 | -44.8955 | 2025-10-05 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 7f750c51-d1c6-39c1-94d5-4b9d2be925b2 | -9.2973 | -46.0026 | 2025-10-05 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 0be7b3bd-59b4-359a-bdd3-e1108819af9e | -17.9609 | -57.5698 | 2025-10-05 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.4 |
| 739449e0-798e-344b-a9b6-75ddfc7e9112 | -11.7033 | -45.3305 | 2025-10-05 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 211.6 |
| 25b84eb3-457f-343c-9b86-db81cc45972b | -6.154 | -44.6217 | 2025-10-05 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 4129f663-fa69-3b42-b562-e79acba0086a | -10.6378 | -46.3396 | 2025-10-05 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 12776de2-8354-376d-95b7-72058b0eed0f | -10.069 | -50.4307 | 2025-10-05 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 97.5 |
| e77a18fa-15c5-3f01-bbb3-bbf3aa4f1a08 | -12.573 | -48.1615 | 2025-10-05 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 5d58e39e-6aeb-3b21-9e8c-aaf04daeda35 | -12.3914 | -51.094 | 2025-10-05 14:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 136.4 |
| d5a33954-52b0-3d91-8683-96ba5e9c6e64 | -10.4557 | -48.3827 | 2025-10-05 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| a69e53bd-7441-32a6-8dab-8487e129d2b2 | -17.9404 | -57.6134 | 2025-10-05 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.2 |
| 61b8b42e-8dd7-3ab6-bad8-73ae6db09607 | -7.4279 | -46.5016 | 2025-10-05 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 6ff0ab8b-43a7-364d-bd22-1063ca14fbd4 | -12.3154 | -55.1416 | 2025-10-05 14:10:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 4051336e-9acc-3e15-adae-012b066b1d6e | -10.8093 | -48.8229 | 2025-10-05 14:10:00 | GOES-19 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 2b934ac0-4eaf-3036-836d-e70ba2eaaf89 | -9.921 | -50.2109 | 2025-10-05 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 3116a748-9fa0-325a-a170-e4b1f5ebc21f | -8.5576 | -46.306 | 2025-10-05 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| aa11bd3c-aaf6-3300-b427-d99ca88839cc | -10.4054 | -45.3931 | 2025-10-05 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 89ad8aea-dbd9-38f9-86c1-fafe95cbeae8 | -12.5733 | -48.1393 | 2025-10-05 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 159b6af5-62a3-3f91-9c05-45f649498904 | -7.7118 | -46.2754 | 2025-10-05 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 183359ca-1390-3f23-ae2b-e2a82671d005 | -11.0313 | -46.7171 | 2025-10-05 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 1e43f6e4-8d4b-3038-bdb6-85fd2154eae1 | -11.8225 | -45.0827 | 2025-10-05 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 220.6 |
| cfd11199-2ef6-39bc-b2c1-35ae34e6a88a | -15.3158 | -56.9329 | 2025-10-05 14:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| bf744aaf-3388-3410-988a-0cf6d0747286 | -5.9584 | -43.5072 | 2025-10-05 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| c2f8a709-86bc-3cf5-bcf2-349d1f816f33 | -17.9408 | -57.5928 | 2025-10-05 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 6c9ae4f4-3b02-345f-a599-7292456477a3 | -6.4161 | -44.6466 | 2025-10-05 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| a0cc0c85-ac43-3a33-969d-183148c02e6d | -6.7048 | -42.1712 | 2025-10-05 14:10:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| 470edc47-336b-379f-8b62-c3ff1c9b1acf | -11.8033 | -45.0856 | 2025-10-05 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 17cd2990-2910-3023-8dfd-de518d7b613f | -21.7095 | -50.0513 | 2025-10-05 14:10:00 | GOES-19 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 111.9 |
| 2a836a27-ff6c-3bf5-a9ef-a3ee5b1b4602 | -7.6648 | -45.4471 | 2025-10-05 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| b3bb0e6a-8a35-313c-a181-b7adfdb2d253 | -11.2429 | -47.7827 | 2025-10-05 14:10:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 4d29a7ac-d793-3b01-b415-d666f842318c | -9.9021 | -50.2128 | 2025-10-05 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 51f52300-db06-3480-979d-49645ba4c4f8 | -9.9207 | -50.2323 | 2025-10-05 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 132.1 |
| d4b0eaed-3300-3074-b3e8-4171a8ef0cbb | -5.9582 | -43.5305 | 2025-10-05 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 173.0 |
| ad20a583-af30-3924-9622-2cb6d92254f5 | -11.6841 | -45.3333 | 2025-10-05 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 0b7c9657-5aec-3c9b-973a-2296489d65a7 | -17.8417 | -57.6254 | 2025-10-05 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.2 |
| 5ca5125a-1e8b-3287-aa6b-7800e381b6b2 | -9.5794 | -46.106 | 2025-10-05 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 273f8eb8-a3f8-3656-aaeb-5e6036064a2f | -3.1764 | -42.9547 | 2025-10-05 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 4fc2a371-8090-396b-987a-fa7880ed8de0 | -13.7476 | -51.2883 | 2025-10-05 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 199.7 |
| 3b4d1fee-5855-3fdf-9615-571496050050 | -8.1134 | -47.2827 | 2025-10-05 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| b671dcaa-7080-34c4-85e6-d4dfdfbe10a5 | -11.1168 | -49.8492 | 2025-10-05 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 30d84919-43e7-36df-98aa-3287c70ed327 | -6.4976 | -45.8855 | 2025-10-05 14:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 58d7e802-970f-3511-bd29-529179f26385 | -11.2429 | -47.7827 | 2025-10-05 14:20:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 06927418-7d16-3e32-894a-b9e3d6efcc78 | -10.3721 | -50.3363 | 2025-10-05 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 5e03ec22-cf9d-387f-b443-547b758d6e35 | -10.5036 | -51.8457 | 2025-10-05 14:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 4d30a08a-18b4-3728-9248-c0df7f36a452 | -7.712 | -46.2531 | 2025-10-05 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 241.1 |
| 0c8efb12-df07-3cd0-a74b-0b8394346c69 | -13.0968 | -47.8429 | 2025-10-05 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 560939e0-6914-3200-bd6c-07888c99f053 | -7.7938 | -42.5607 | 2025-10-05 14:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 141.4 |
| 35f62bfc-96af-3103-b3a9-d519937bf000 | -6.154 | -44.6217 | 2025-10-05 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 636dd4aa-f17a-3d23-8ef5-d00b8b14bf93 | -11.7033 | -45.3305 | 2025-10-05 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 58a41713-c2f9-3ca1-a662-3a22ca1adb39 | -8.1322 | -47.281 | 2025-10-05 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| b4e3756e-408b-3253-9569-9436223d63c3 | -11.8038 | -45.0624 | 2025-10-05 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 4e8f08a2-a142-360f-bf58-bf9fe9449806 | -9.921 | -50.2109 | 2025-10-05 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 128.3 |
| e165a30a-87aa-3926-97af-e57afb6667ce | -9.6287 | -46.6394 | 2025-10-05 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 2d227c95-9b33-3c1e-b4e0-6dc6bb532dea | -7.0369 | -42.78 | 2025-10-05 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 222.0 |
| 5b7de146-9dc4-3967-95d8-abdcbe154f30 | -17.9602 | -57.611 | 2025-10-05 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.9 |
| fa89bba8-b594-3c1a-a984-3dcd78581a7d | -6.3529 | -41.6292 | 2025-10-05 14:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 89.5 |
| 03619489-c9a3-3686-8c54-3b2e3bbfc571 | -11.7912 | -48.0448 | 2025-10-05 14:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 130.4 |
| c63c6d48-f04c-3e39-b3c2-3a3328e0153a | -11.6845 | -45.3103 | 2025-10-05 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 109.9 |
| e328ad1f-9b92-32e5-a2c6-8f7d5652c4b6 | -9.9396 | -50.2304 | 2025-10-05 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 1f484aba-664c-32cb-bb16-1384e56bf437 | -7.4669 | -43.0674 | 2025-10-05 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 139.8 |
| 53fe9e2c-f8e4-3a2c-a3b9-24dc1ffcbf23 | -5.8574 | -44.3008 | 2025-10-05 14:20:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |


[Clique aqui para ver as próximas entradas](README165.md)
