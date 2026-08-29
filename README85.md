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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 561410ef-d26e-3292-9779-1b978ac884d6 | -5.871 | -57.7715 | 2026-08-29 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 1c605e83-c8b4-3bd6-b8f6-0ab90ec5a517 | -8.6506 | -49.5386 | 2026-08-29 15:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| b7b2ad3c-9fd8-350d-98a2-0ceac5e0e033 | -11.2506 | -53.9941 | 2026-08-29 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| b82fb2ea-3d71-359b-a27d-19bcd033c382 | -11.269 | -54.0334 | 2026-08-29 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 17080577-ca1f-3f0a-9f3c-965a30688e04 | -9.0058 | -65.4373 | 2026-08-29 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 9ae181b1-b41f-35a0-8ead-df25e4cbb790 | -6.6317 | -43.73 | 2026-08-29 15:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 124.8 |
| ef8cb893-87e3-3ac4-bd67-0f708d60cde9 | -11.2317 | -53.9958 | 2026-08-29 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 135.8 |
| 36abff96-44e7-3f9f-b502-7d8fd785c8aa | -11.0256 | -57.2038 | 2026-08-29 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 18b63e3e-3cbf-338a-bbca-bd45b948cc20 | -11.3622 | -45.1494 | 2026-08-29 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 92c47d27-c47a-3aa1-8bf2-f76867303441 | -10.5404 | -50.4683 | 2026-08-29 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| f5ad78b2-b4f0-391e-bb5c-a02346092c7a | -8.9428 | -63.2797 | 2026-08-29 15:20:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 134.8 |
| ead1b7f4-e65e-3684-936a-73ce00e5bdba | -8.8184 | -49.6308 | 2026-08-29 15:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| ea85dd68-394c-3a92-ab04-820dc29d6da5 | -11.6975 | -54.5467 | 2026-08-29 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 1066f601-e95f-344a-a578-4ecb54b93aff | -11.1726 | -51.2728 | 2026-08-29 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 75575f0e-3b96-3071-b3f4-b7f6c9ad29d5 | -9.6022 | -55.128 | 2026-08-29 15:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 178.1 |
| c30350ce-758b-3b3c-8700-3f170de2e5c4 | -15.3654 | -53.7887 | 2026-08-29 15:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 4befbc3e-a124-30c9-aa78-fd4059fc7dc3 | -13.8563 | -54.0967 | 2026-08-29 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 192.2 |
| 4062a58b-7388-33c0-9073-410549e02c94 | -13.8756 | -54.0945 | 2026-08-29 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 260.8 |
| 02c49379-1dd4-39ed-ba4e-bdd8bb3a0d76 | -8.9613 | -63.279 | 2026-08-29 15:20:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 230.3 |
| 8b31e958-9128-3ec4-b4dd-eb5fcf23f44f | -11.2489 | -45.0732 | 2026-08-29 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 0fb81f3d-1d8d-3d1a-8ac5-fd8b8a85b2fc | -6.6315 | -43.7533 | 2026-08-29 15:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 48c732a6-03fb-379d-8c19-16b1f9a8c9c6 | -8.6495 | -66.5468 | 2026-08-29 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 2d39fc66-abfc-3678-80fa-fcb5a1906ce2 | -7.5847 | -61.3042 | 2026-08-29 15:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| caec9a1d-0064-3515-a84a-5e8300dd4abc | -9.2094 | -51.5444 | 2026-08-29 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 01b19aa7-47fa-3ab6-87a2-79de740b6220 | -14.2989 | -51.7072 | 2026-08-29 15:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 41974819-50a8-3ccc-824b-0bb9535875d7 | -11.7028 | -47.6129 | 2026-08-29 15:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| af85c7d2-aaa3-324e-b8bd-c29cec47a231 | -10.8463 | -50.2224 | 2026-08-29 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| ae942154-23b7-3430-b34d-7d6ca1a6955b | -8.8184 | -49.6308 | 2026-08-29 15:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 323edcac-b82e-3191-989d-40867f10891b | -9.6685 | -50.8299 | 2026-08-29 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 5514af21-4ec9-3094-b5c4-299446e99cef | -6.9872 | -59.2582 | 2026-08-29 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| b0b8f0b4-0e22-3ed7-ae0c-c202e34da805 | -10.5782 | -50.4643 | 2026-08-29 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 45e11518-b1af-379e-b8e2-8fe2c972f1d7 | 0.1367 | -60.393 | 2026-08-29 15:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 155.2 |
| 8d960156-0dd8-3d24-9c0d-fccb29183cec | -10.8653 | -50.2203 | 2026-08-29 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 41e9b96a-869a-3b73-b09b-7c0320f19a7a | -6.6129 | -43.7317 | 2026-08-29 15:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 06b512f2-7b14-30dd-acfd-cfeb2abef0f6 | -6.7833 | -59.4208 | 2026-08-29 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| b3513967-4278-3886-a6a8-0ab250c6619a | -7.0242 | -59.2374 | 2026-08-29 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 45285398-ec2f-321b-8d02-1de54bd160a9 | 2.2375 | -50.7515 | 2026-08-29 15:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 96.4 |
| fac9bd98-ae5f-3cd5-9be0-869e5dc375d0 | -6.1743 | -53.4834 | 2026-08-29 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 4522637f-6d29-315e-9bc9-d65634b94e67 | -15.3654 | -53.7887 | 2026-08-29 15:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 81277842-14aa-3550-a449-8d357437ab27 | -20.941 | -57.5694 | 2026-08-29 15:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 63.2 |
| 51b3c540-715f-366d-9e82-5e30157c464a | -9.9708 | -53.9419 | 2026-08-29 15:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 126.7 |
| a22e839c-355b-392b-a2e7-f1092d49a42c | -10.9859 | -51.0807 | 2026-08-29 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 4bd377ea-27b0-3af5-b789-f677c9a6840a | -12.3811 | -48.1877 | 2026-08-29 15:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| b8778ffb-c95e-3d24-92ca-a3d9f907e6ca | -1.2541 | -55.7101 | 2026-08-29 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 63490a17-3234-3728-a54c-546e02fe8626 | -7.9169 | -61.3671 | 2026-08-29 15:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 162.9 |
| 54f9b93b-e17a-39bc-a1f4-e237fde32684 | -6.6317 | -43.73 | 2026-08-29 15:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 148.9 |
| cb253df5-e5cc-3025-a393-7bbf648c011d | -20.8776 | -57.7043 | 2026-08-29 15:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 63.4 |
| f03efa02-5af5-3875-9b70-807e2803a458 | -14.444 | -53.4016 | 2026-08-29 15:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 538aa235-22ca-3aab-b480-fbae99b39c50 | -3.6216 | -60.547 | 2026-08-29 15:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 6b96e748-4359-38a5-a2cf-ac23596ecbb3 | -10.967 | -51.0826 | 2026-08-29 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 856f4689-4ce8-37a5-8ecf-3d39b282026a | -9.6497 | -50.8317 | 2026-08-29 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 124.5 |
| b0685351-c691-3a0c-a6f2-20a33ffdba4b | -11.3622 | -45.1494 | 2026-08-29 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 332ec69f-dbc8-3b13-bcae-473cc28a6420 | -10.8025 | -50.6539 | 2026-08-29 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 0ee637f8-3eab-341a-ac34-b6bc8bf59ef0 | -8.6495 | -66.5468 | 2026-08-29 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 124.6 |
| db79c58d-38de-3ddf-bb87-c8cdd3a8b769 | -11.6975 | -54.5467 | 2026-08-29 15:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 979f8b80-bc7a-3fec-b787-e1dc1ac0829f | -10.5404 | -50.4683 | 2026-08-29 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 8ca4d2ef-669b-3f5d-af22-530a43a9610d | -11.1723 | -51.294 | 2026-08-29 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 867eec3b-cab9-3ce1-96b3-e45f12b0754f | -10.8215 | -50.6519 | 2026-08-29 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 303.0 |
| 218d4d38-8ed5-3ce4-9220-5015d9524b76 | -9.6022 | -55.128 | 2026-08-29 15:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| a17f0d0f-6a02-3593-9ea9-7737519d448a | -10.9673 | -51.0614 | 2026-08-29 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.7 |
| ceca672f-0e9d-30e8-986d-e2c18878f55a | -11.006 | -49.6461 | 2026-08-29 15:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 2c90682d-0ead-35ad-96f0-d4ce19f924d0 | -12.1902 | -50.5409 | 2026-08-29 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| a5edc871-992f-328b-9f66-cf577cfac070 | -11.2446 | -45.3267 | 2026-08-29 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 219.7 |
| 02a372de-91ce-3dab-8134-211b14d144ad | -10.7975 | -54.0146 | 2026-08-29 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 5167a1c8-7376-364c-9038-e563f59d0442 | -7.0058 | -59.2382 | 2026-08-29 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 9f91459a-91ed-3d91-84ba-d3cf8305f76f | -6.7884 | -55.6635 | 2026-08-29 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 133.0 |
| a9081a05-d579-36ef-914e-7db2fccedff5 | -8.9873 | -65.4379 | 2026-08-29 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| cd2c4002-542b-328b-b0b3-200572861a09 | -8.9428 | -63.2797 | 2026-08-29 15:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 144.5 |
| 9801c15b-84df-36fe-ac4d-7a7da5389eb3 | -10.5593 | -50.4663 | 2026-08-29 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 7bb81479-f426-3226-b2c3-8f5138524d1d | -10.5596 | -50.4449 | 2026-08-29 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 2cfa5f99-7a5d-33f4-a440-88c9fa1f51bd | -8.631 | -66.5473 | 2026-08-29 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 257ba4b3-3309-3d3d-aa21-4d7432da9472 | -7.1001 | -42.2044 | 2026-08-29 15:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 98.0 |
| c8b94eb7-0e08-3ef4-b8f2-737767b1e65d | -10.7596 | -54.0384 | 2026-08-29 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 9878d39b-4d11-3d82-8ba5-cd5a71697f17 | -9.0058 | -65.4373 | 2026-08-29 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 79d2dc47-251c-3f4b-b6c1-8bd22c86bb61 | -3.9363 | -59.3381 | 2026-08-29 15:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 96e77591-b3d9-3d6a-8a8e-3b46b7bf3e38 | -10.7598 | -54.0179 | 2026-08-29 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 37695da0-1564-375d-9162-6ae29be82914 | -14.2985 | -51.7286 | 2026-08-29 15:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 124.2 |
| bf3dd003-bf33-3361-88e8-036c6324217c | -8.7584 | -49.9566 | 2026-08-29 15:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 68743907-22bb-3d6d-9f79-6f5da02256d2 | -11.0244 | -49.6872 | 2026-08-29 15:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 5292ed9f-30d0-39b5-b34d-e330384dbd8f | -5.871 | -57.7715 | 2026-08-29 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 7e2ebcad-f2bb-37d4-8924-d12f6c552b12 | -11.0057 | -49.6677 | 2026-08-29 15:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| c66f8ffa-7689-33c7-b5c9-5868723af1fd | -11.2314 | -54.0164 | 2026-08-29 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 8b3b314b-c565-3c68-9027-2dc1d431762d | -17.2938 | -46.0291 | 2026-08-29 15:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 70.5 |
| b9b1bc64-15c5-3ece-a85c-1363406e812a | -10.8028 | -50.6326 | 2026-08-29 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 035310a7-875a-3497-9216-e678ed85c5f4 | -8.6694 | -49.5369 | 2026-08-29 15:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 0dfa6454-dadf-3104-aa82-6aa7b2b55350 | -6.1795 | -45.9097 | 2026-08-29 15:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| ac3f7ba8-1aeb-32f4-ba52-dcf352a9288b | -11.7165 | -54.5449 | 2026-08-29 15:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 237.1 |
| f5992d8e-1031-36f2-9917-e205d0640a99 | -5.8894 | -57.7708 | 2026-08-29 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| a2b13057-0c85-3dae-a5cd-aa9332f29850 | -11.2125 | -54.0181 | 2026-08-29 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 082485b9-db49-3044-920e-63972439a2ba | -8.5971 | -54.7553 | 2026-08-29 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| ba5bd79f-c9ea-3b37-9d3d-27d126e130b4 | -11.7167 | -54.5244 | 2026-08-29 15:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 320.2 |
| fd8f98ac-3ebe-31b7-8a96-52c71c0468da | -11.0054 | -49.6893 | 2026-08-29 15:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| cf1133e7-9e9e-3dd4-9933-7ec55043047c | -11.1726 | -51.2728 | 2026-08-29 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 2c062621-5f28-3599-95ad-db205db4d4d9 | -10.4609 | -64.4831 | 2026-08-29 15:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 51.6 |
| d0316f5a-a6ef-34ca-9a17-e40903130a2a | -10.9405 | -50.255 | 2026-08-29 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 85220e96-1dac-3ff7-985a-6265ecea6e30 | -6.6315 | -43.7533 | 2026-08-29 15:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 25c7bc15-8a7f-3459-82ea-6e31db26ee2e | -11.0247 | -49.6656 | 2026-08-29 15:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 51a3e0d7-234d-39dd-8f95-db152b814030 | -10.5596 | -50.4449 | 2026-08-29 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| fbe8881f-a2d2-34a2-a5f8-1867e9116dfa | -9.0059 | -65.4186 | 2026-08-29 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 33d1b837-b311-393a-a6b9-8d1ad9fa0a35 | -6.9121 | -59.4734 | 2026-08-29 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |


[Clique aqui para ver as próximas entradas](README86.md)
