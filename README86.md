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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b81afc17-10e3-3719-91ae-be55fa66351d | -13.3604 | -51.4872 | 2026-08-29 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 46.4 |
| b33cc7d7-f11c-3aad-83fb-d34d5125d4eb | -10.5404 | -50.4683 | 2026-08-29 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 1705e98a-3dd8-32e1-a458-1910b1372d74 | -7.0242 | -59.2374 | 2026-08-29 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| d0845adb-6a2b-309e-a0f0-06b38b488456 | -3.9364 | -59.319 | 2026-08-29 15:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 0daf87d8-b009-3f06-81d5-184c8e21f218 | -7.1001 | -42.2044 | 2026-08-29 15:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 129.5 |
| 30ed8b65-2467-3e9d-a46e-86f4d5f6ceec | -10.7598 | -54.0179 | 2026-08-29 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 39c306a1-b508-3ba1-b3b4-88c77c1a2972 | -4.1516 | -60.6878 | 2026-08-29 15:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 62a15a91-d725-3832-a33e-7fce45168a9e | -9.2094 | -51.5444 | 2026-08-29 15:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 3daa240a-f95a-3c84-8877-34c2952ecc33 | -3.6216 | -60.547 | 2026-08-29 15:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 98.9 |
| f86d0bb2-2f77-39cb-b3e3-f8652c6b78a8 | -11.1995 | -55.1008 | 2026-08-29 15:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 659afe9c-98d0-3335-82fa-03b5da0f541a | -14.4649 | -52.1538 | 2026-08-29 15:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 3ef12fa9-6e10-3148-837d-f63884c56883 | -3.9363 | -59.3381 | 2026-08-29 15:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| aa8ee86e-dad4-3f87-9817-b7c71f614692 | -11.9081 | -55.8891 | 2026-08-29 15:40:00 | GOES-19 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 12884517-c766-39a7-914e-d2645dc53b19 | -10.8425 | -50.5005 | 2026-08-29 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 609ba362-6c1a-30f2-ae66-0cf8dddde567 | -6.6315 | -43.7533 | 2026-08-29 15:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 3e525f2c-855d-35db-b683-670da4217a0e | -9.0057 | -65.456 | 2026-08-29 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 38339d68-33ee-3368-8d0a-e654527cd235 | -9.006 | -65.4 | 2026-08-29 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| eca4e9bd-449e-3d32-96f9-33cd8d9230ef | -10.8235 | -50.5026 | 2026-08-29 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 222.4 |
| 8824ac0c-d056-303f-832c-ae2ad2f714fe | -9.971 | -53.9214 | 2026-08-29 15:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 178.9 |
| 56cce10c-1598-3276-a598-aac36b604918 | -11.2302 | -45.0528 | 2026-08-29 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| ed7ba343-2061-3588-be38-630bdca73261 | -7.6041 | -45.8366 | 2026-08-29 15:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| c3a71233-b032-31d5-9307-ce0c98329531 | -14.4842 | -52.1512 | 2026-08-29 15:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 116.1 |
| def0b62e-85e7-327f-959b-17ce5e8802a4 | -10.8804 | -50.4965 | 2026-08-29 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 5a98760f-55ac-347a-bfae-aecf0d059450 | -10.7407 | -54.0401 | 2026-08-29 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 68b4da22-d13a-3133-89e4-c6a19413316c | -11.2106 | -51.2688 | 2026-08-29 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 6de21bb0-426b-3dcc-91f7-47e3b2b233d4 | -10.9029 | -50.2377 | 2026-08-29 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| e97d16de-9649-3738-9fda-ce8355687d51 | -12.2284 | -50.5363 | 2026-08-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 10cf89a2-6557-3c1d-83ce-6b3263340fb3 | -10.8232 | -50.5239 | 2026-08-29 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 6b4f1c73-c25d-3384-96a1-3fd420738404 | -8.8184 | -49.6308 | 2026-08-29 15:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 7178aaa6-9c29-33e2-8f16-c1920f57e6a9 | -8.9428 | -63.2797 | 2026-08-29 15:40:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 000aae5c-353c-3f21-8881-f41c32f24e6e | -11.0256 | -57.2038 | 2026-08-29 15:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| eb5faf76-0a8e-3718-85ad-65f7cbf129e5 | -6.9872 | -59.2582 | 2026-08-29 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| f8a29b6b-f089-3e85-8fe7-e3dafa8c1b92 | -8.6495 | -66.5468 | 2026-08-29 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| c3ef1e18-a57f-37da-b5c9-4f542343bde6 | -20.9406 | -57.5905 | 2026-08-29 15:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 57afbde6-b0cd-30c6-960b-7ede1988b705 | -11.1998 | -55.0805 | 2026-08-29 15:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 4e5ccf57-7277-3658-a8fd-9e473bb2b101 | -11.2877 | -54.0522 | 2026-08-29 15:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 3a87ace6-d974-3a68-a315-97d6b5a01edb | -14.2989 | -51.7072 | 2026-08-29 15:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| a51af894-695c-321c-b59f-86740644378e | -13.3607 | -51.4659 | 2026-08-29 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 0c11e791-d36a-300e-b3a7-43d5d2d286bc | -9.6024 | -55.1078 | 2026-08-29 15:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| c42fdb19-5282-3c2d-b299-96cd459e8778 | -17.2938 | -46.0291 | 2026-08-29 15:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 74.6 |
| a7724634-e03b-3c0c-a733-cb754cd89821 | -14.2985 | -51.7286 | 2026-08-29 15:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 118.3 |
| fce522b2-b9b4-39ed-8638-6e7ebe3b965e | -9.6685 | -50.8299 | 2026-08-29 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| d5f0b9f7-788f-3070-95d1-2cfd4d3951fc | -14.5032 | -52.17 | 2026-08-29 15:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 715695ff-a970-3672-bdf8-575bd750854c | -7.1003 | -42.1805 | 2026-08-29 15:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 100.6 |
| eeb2c060-f68e-3154-85fc-70bbab29adfd | -10.8801 | -50.5179 | 2026-08-29 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| bb92b11a-6316-380f-bc1b-baeaae858beb | -11.1639 | -45.5897 | 2026-08-29 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| e6ce1d18-acd2-3052-891d-156f5543a5f0 | -11.0057 | -49.6677 | 2026-08-29 15:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 2e435616-9fb9-35de-aa3c-48ad305b2595 | -6.7652 | -63.054 | 2026-08-29 15:40:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 6239d082-4a56-3434-a0fa-37b52de187b5 | -12.2475 | -50.534 | 2026-08-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| a1f49dae-bcb0-381e-9c8d-398369a880c4 | -11.2506 | -53.9941 | 2026-08-29 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 2e48b595-c2f2-31d2-816d-266c946f811b | -7.0057 | -59.2575 | 2026-08-29 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 23a61931-d8c4-304e-8d4e-80f064aeff33 | -7.9169 | -61.3671 | 2026-08-29 15:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 112.1 |
| abb2d699-8b0f-3a37-b618-7005f7f4f7c8 | -10.8215 | -50.6519 | 2026-08-29 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.1 |
| c80e8d39-57c0-3b1d-b410-5b02a0b688c2 | -9.9288 | -60.4277 | 2026-08-29 15:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 505e8b3e-4d11-3ebb-8ce2-dbd264b7fb09 | -14.4444 | -53.3806 | 2026-08-29 15:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 31303a85-8cad-35b6-8a2f-f6f20c06a47c | 0.1367 | -60.393 | 2026-08-29 15:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 61553026-c803-3199-bb60-d05b301d3a6e | -8.6694 | -49.5369 | 2026-08-29 15:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| e348f14f-8ba9-3066-a842-cf5a322e5786 | -9.9708 | -53.9419 | 2026-08-29 15:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 154.0 |
| 41ee27f1-eff4-3ffa-98b8-830890b54049 | -7.0842 | -43.5961 | 2026-08-29 15:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 88b7251f-2c0c-35b3-8bc8-763e9f0e08bb | -1.2541 | -55.7101 | 2026-08-29 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 92f70d4d-0152-3d92-9c62-5fb56c43ff28 | -11.1726 | -51.2728 | 2026-08-29 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 7293bcc6-b481-35b2-a307-a8e5363602e9 | -13.8378 | -54.0573 | 2026-08-29 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| b11bfc3b-5978-3f5a-ba36-b6956bf2096f | -6.4908 | -53.2629 | 2026-08-29 15:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| bcb9f7ad-c886-3c9d-9e73-6a5684024408 | -8.574 | -66.9569 | 2026-08-29 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| f2f31a72-b210-3d55-b36b-02d81b1eeb84 | -7.6214 | -61.3408 | 2026-08-29 15:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 6c10ca7c-bcae-3af0-bf3b-626080b120e6 | -11.1723 | -51.294 | 2026-08-29 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| a98df0f8-54fa-38d1-ab9c-5b0440b9f1a5 | -11.2317 | -53.9958 | 2026-08-29 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 183.0 |
| 35016ddb-d761-336e-93a3-342fcc0703d2 | -11.245 | -45.3037 | 2026-08-29 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 182.0 |
| aa09f488-d3a6-3e17-8617-e63eea74beec | -11.7165 | -54.5449 | 2026-08-29 15:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 1fa2b7e2-2c10-3121-9caf-db9a780086b0 | -8.9873 | -65.4379 | 2026-08-29 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| d0394149-c16f-318b-9de3-92855a96d809 | -11.269 | -54.0334 | 2026-08-29 15:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 1fbe859f-9905-3234-a8a5-f78dd5527881 | -8.116 | -45.4715 | 2026-08-29 15:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 480dd21f-aa72-3f86-ab2d-23d6cf1f2a83 | -10.8993 | -50.4945 | 2026-08-29 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 5a2616ef-bc01-3db5-bf0a-c005c0d24b91 | -6.6317 | -43.73 | 2026-08-29 15:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 119.4 |
| b275af6e-6507-343c-892a-e2bdd7553b68 | 1.7849 | -55.8423 | 2026-08-29 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 9d1c51d1-66b3-3803-a2f2-f76db160d03a | -9.0058 | -65.4373 | 2026-08-29 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| f8e03790-4bdc-342d-b9cb-a95d70cd549d | -10.7975 | -54.0146 | 2026-08-29 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| bc24b378-ffd7-3708-9248-a464f5e3df48 | -11.1723 | -51.294 | 2026-08-29 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 089cf7eb-5a4e-394e-92ee-dd337cc09332 | -11.1995 | -55.1008 | 2026-08-29 15:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 91d4fe0f-cb33-3c53-9005-14386d84b8ba | -6.8017 | -59.4394 | 2026-08-29 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 120805f8-262b-3528-8c73-3dd0ee9aa9c6 | -19.0744 | -57.3876 | 2026-08-29 15:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.9 |
| 6a7e630f-c2de-32af-b4ad-f37f15055776 | -17.2938 | -46.0291 | 2026-08-29 15:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 79.1 |
| a22db9af-8db0-355b-8619-46811d8d86e1 | -9.6024 | -55.1078 | 2026-08-29 15:50:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| c95e2e73-d004-3f2e-8158-c8f214a43992 | -8.8184 | -49.6308 | 2026-08-29 15:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| c8f67e92-22ed-3218-aff1-7fae7dda9cae | -11.269 | -54.0334 | 2026-08-29 15:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 247aa63e-c4e2-3385-b144-9bbb404865a7 | -13.323 | -51.428 | 2026-08-29 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 746f6eb6-d454-3d57-ac61-615ca3a82ea8 | -11.1726 | -51.2728 | 2026-08-29 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 5d3c0bdf-1ed8-3ac1-a641-ff9697f4af42 | -14.2985 | -51.7286 | 2026-08-29 15:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 24cdb840-06e1-3f18-b3ff-8d2a0e3520f9 | -10.7603 | -53.9769 | 2026-08-29 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| a9534241-d63a-31f8-b197-8523cdaa9157 | 0.1367 | -60.393 | 2026-08-29 15:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 147.0 |
| c5debfdb-935b-3fc8-a32c-a9e6da0e4716 | -14.4842 | -52.1512 | 2026-08-29 15:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 143.4 |
| ccf52ab6-6561-3731-970d-149c2d7ce679 | -10.7789 | -53.9958 | 2026-08-29 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| f9f68f07-83bf-3156-a88c-2fcde0e5c306 | -10.8425 | -50.5005 | 2026-08-29 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| cb50c14f-a897-3a6a-8007-cc85b83367e3 | -12.2284 | -50.5363 | 2026-08-29 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 19d7be55-3940-3a1d-9951-7a4282eba64f | -8.3717 | -62.716 | 2026-08-29 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 318bd721-7802-3d8c-bca2-2422f1256057 | -11.2319 | -53.9753 | 2026-08-29 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 6e3af070-8c43-386f-8c3b-420a384a4e66 | -13.471 | -57.0373 | 2026-08-29 15:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 3dee3a10-2d69-3a22-ac3c-9f53258e91fe | -10.9405 | -50.255 | 2026-08-29 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 8dd4e462-c077-3f00-8beb-dc9c69230d11 | -8.6495 | -66.5468 | 2026-08-29 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 4a83bbcc-2c7a-369f-bf96-09abd3328196 | -10.8235 | -50.5026 | 2026-08-29 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 124.1 |


[Clique aqui para ver as próximas entradas](README87.md)
