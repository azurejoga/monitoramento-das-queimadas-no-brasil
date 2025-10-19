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
| 1ed93495-face-3f7f-8843-5bcad83b0eda | -10.9555 | -45.46503 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce50b218-37cd-3ea3-ac44-26c45108d130 | -13.89472 | -45.53423 | 2025-10-19 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 278b3f25-3983-36fc-8557-44451c44aa28 | -9.33079 | -46.11343 | 2025-10-19 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a10e41b0-6842-37d3-8029-fc3a8fb70b99 | -11.60987 | -44.05857 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c02f3bb-9217-3283-bb10-b5b1d8994071 | -14.27844 | -42.33088 | 2025-10-19 04:12:00 | NPP-375D | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 38490032-9bf3-35d0-bd0f-4cd924866899 | -11.14237 | -47.71695 | 2025-10-19 04:12:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 492208a1-1edd-3cac-8457-894e044e8eee | -8.5641 | -48.51171 | 2025-10-19 04:12:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8c3fb067-0379-3455-a0a0-c2b488c0b219 | -10.67805 | -47.42157 | 2025-10-19 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3c027a1-8388-3563-9603-59813fe4ec4a | -14.09391 | -43.61863 | 2025-10-19 04:12:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec25f74e-ea4f-3f6d-bce0-ba508260031f | -8.2207 | -43.96745 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c787916-8ff5-3e8c-b6fd-11f333924bdc | -11.64742 | -44.08356 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49e016a7-a685-3585-a356-b826f3b010f1 | -10.82999 | -43.93412 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0a85e537-e8cf-3291-b23d-34002761b905 | -11.14296 | -47.71355 | 2025-10-19 04:12:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32e3d5b3-6b4d-352b-9280-ea1ebc2cd6d2 | -10.64247 | -48.80609 | 2025-10-19 04:12:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8f9c31c-771d-3fc1-8718-472991a07ef2 | -8.59672 | -45.43483 | 2025-10-19 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3229c081-c128-318b-a401-019c1a8dc2c0 | -9.11299 | -46.64272 | 2025-10-19 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 51c76c3d-5917-3112-9b64-a763646b5b69 | -9.90654 | -45.9528 | 2025-10-19 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b70f79e-04a5-3773-aa0a-41ac07b1d0df | -9.21689 | -46.05368 | 2025-10-19 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df3dfd43-3526-32f5-8441-7e63fef595d1 | -13.53751 | -43.00651 | 2025-10-19 04:12:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3ccb59f7-a10e-3bb7-81f3-f99b4a5339d1 | -12.45477 | -45.44066 | 2025-10-19 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1c97b55f-abb5-350f-8610-4af3efc57c46 | -12.18432 | -45.09076 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aec997b7-338c-3c30-910c-2418dc68ba42 | -12.95216 | -47.29561 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f09e846-5bde-3908-85a3-696070f6dc46 | -8.36023 | -46.20729 | 2025-10-19 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69b4fcfa-908e-3e47-a958-9b93c013ca2e | -9.2494 | -44.34275 | 2025-10-19 04:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7790c3c8-d626-3e77-a822-d4235084ff75 | -10.86655 | -43.944 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7fec3f44-0990-3760-ac72-31faf76e1e5f | -13.01251 | -46.95364 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71fa28e5-0dba-3163-b6b2-4ec685bee8d7 | -11.20905 | -47.83771 | 2025-10-19 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e70dd10b-3cb8-3d97-891e-a2e22dfcab9c | -12.69548 | -46.95667 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbb585f5-3d30-3ed0-a589-72921c669e66 | -13.69875 | -43.16024 | 2025-10-19 04:12:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7916204f-2cf5-3f6e-ba3e-93800ca9755d | -11.60928 | -44.06221 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bdf58178-5aec-3e80-b93a-da721f5fdfb5 | -13.53695 | -43.01006 | 2025-10-19 04:12:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 4f580832-b824-30d5-9d37-57fb1e7f3592 | -10.81026 | -43.92387 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00ac7f2e-af96-3635-948b-c9d9448269ca | -10.37024 | -47.46639 | 2025-10-19 04:12:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8acf1b26-b698-34ba-ac93-8c180d00f1e0 | -7.45234 | -46.52846 | 2025-10-19 04:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 318e53ce-2ad6-3988-8994-cd0267f5e0b9 | -9.9324 | -47.66386 | 2025-10-19 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c52ef3e5-1375-35ad-b890-8079cef58f89 | -10.88982 | -46.07288 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 19e7188f-71ce-30da-8aba-5de5ad850203 | -10.87647 | -47.45466 | 2025-10-19 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9afb3a34-6608-374c-9497-581ea1b46807 | -10.15924 | -42.21146 | 2025-10-19 04:12:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 2671af3c-ea46-35cd-a35c-f1ced46c6e7a | -12.15118 | -45.09701 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd33c772-13ce-33ad-81fa-0c527f8bada3 | -10.63132 | -48.02266 | 2025-10-19 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b78a4b61-3bbb-3f4a-bcc7-5b8d984f3458 | -13.02348 | -46.95887 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdb275e2-eeb6-3125-ae59-8e31e6e0f06e | -10.13262 | -44.52308 | 2025-10-19 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 455ec2e0-c481-3766-a6db-76e1d51a6a69 | -9.10609 | -43.21074 | 2025-10-19 04:12:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e3e349e9-3ac8-30fb-bce5-11ce86e034de | -9.2667 | -44.34559 | 2025-10-19 04:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7ee685e-1b0b-3122-a187-2f3556a536bf | -13.01608 | -46.95704 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eea7f43f-dfef-3e9f-9794-52507bbe778d | -10.83337 | -43.9347 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bfd4870c-d4e7-32f2-ac0b-1f37497ad207 | -9.92831 | -47.66314 | 2025-10-19 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0521ac19-5a68-3443-baec-32d763ee3394 | -10.88029 | -47.44854 | 2025-10-19 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b21e38bf-d298-3c2e-9752-2afc505e9f0f | -8.62548 | -43.99864 | 2025-10-19 04:12:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65151769-7a16-3d02-b39c-566ecb80e7e2 | -8.24738 | -43.99891 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 266eb13f-afb2-3429-b614-a507f893532f | -8.29722 | -42.30413 | 2025-10-19 04:12:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 313b21eb-1967-357f-8af3-0e67ea278046 | -10.87556 | -47.45982 | 2025-10-19 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f34ef5e2-5f99-3b0f-8eaa-ea4f88d83fe3 | -11.41809 | -41.31447 | 2025-10-19 04:12:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1442de41-7a5e-3ab2-9843-91bff63e8f73 | -10.81767 | -43.92457 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b1dbc2b5-dbfe-361d-a653-6913443dd8ee | -9.88804 | -47.65199 | 2025-10-19 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef428378-3734-3211-9b79-270c3ba79205 | -9.61852 | -49.02694 | 2025-10-19 04:12:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f4fa4a9-eec9-3689-91d5-57c47e98ccf5 | -9.32705 | -46.11269 | 2025-10-19 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 46fef954-7325-3b82-b930-03308009f770 | -12.33392 | -41.39058 | 2025-10-19 04:12:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 84b49fe5-3e08-3e59-9ad7-9f0f889bd351 | -8.25082 | -43.99948 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a34b2c90-801e-3b27-a576-9ce9e600bdd0 | -9.90853 | -47.65551 | 2025-10-19 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91eacbf6-1a4a-38b0-abf0-a241d68fde31 | -10.22902 | -44.06154 | 2025-10-19 04:12:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce86272a-4567-3fe9-a4c5-42905ed4c190 | -12.14548 | -45.08128 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56530c3e-c3d2-3c27-b984-3aaa87260720 | -14.28124 | -42.33506 | 2025-10-19 04:12:00 | NPP-375D | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 1ec69204-394f-3486-83c9-dfb01336a388 | -13.90014 | -45.5231 | 2025-10-19 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5ab15bdd-5023-37f3-8144-733920e925fa | -8.23347 | -43.31313 | 2025-10-19 04:12:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9267d512-c9ef-3664-91bf-1c058ec34292 | -13.01685 | -46.95265 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d3bc0c4-14ba-38d7-b5c9-196d1c20d13e | -13.53418 | -43.00597 | 2025-10-19 04:12:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3d07d599-9294-30ab-809f-05ef00ee5ac8 | -9.13168 | -43.2442 | 2025-10-19 04:12:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9f4f12b3-dba5-3239-a256-8e05d1a6cafd | -8.93883 | -42.69753 | 2025-10-19 04:12:00 | NPP-375D | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ab7a87b2-c738-3222-a9ff-8352011dfa37 | -9.2349 | -46.06143 | 2025-10-19 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 400fd6bc-6b92-37b0-aaf7-b03e94ec4dd6 | -7.94293 | -46.02046 | 2025-10-19 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03cf8d13-66ad-3177-a28f-1740200b1d23 | -10.71865 | -44.53319 | 2025-10-19 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9eed4b3c-0d08-3b4f-a798-8d83384d7aff | -13.01623 | -46.95448 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30e04f49-6266-3a9b-ab79-64c782a53465 | -9.24593 | -44.34217 | 2025-10-19 04:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d8f7229-8948-3329-9363-f6c328b882f3 | -8.43959 | -44.16967 | 2025-10-19 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f17abb6b-5f12-30ec-a758-e5a266aa0976 | -12.18292 | -40.62001 | 2025-10-19 04:12:00 | NPP-375D | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 22ead016-d1a4-3f3d-8692-151d0ba9f8cf | -10.51161 | -43.46063 | 2025-10-19 04:12:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0c304547-17a7-3d17-a743-8ca7da869c9e | -11.6059 | -44.06164 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5b24ab6b-b52b-3188-b8bc-8e2f2e29a948 | -13.8964 | -42.36461 | 2025-10-19 04:12:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 3e6b0fbe-4746-301d-bf37-37f14a561472 | -13.89255 | -43.4548 | 2025-10-19 04:12:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7abf8d2-3626-377c-a504-3fddf04ef55a | -13.98713 | -44.09298 | 2025-10-19 04:12:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7ab5f2a-42c1-3440-8407-cd6ab8c159fc | -12.45289 | -44.86342 | 2025-10-19 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e0d9df5-1bad-3566-b7bc-71d837ff11e4 | -9.7527 | -43.96154 | 2025-10-19 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e027ccd-ae5e-31d0-bb64-2b29f0f17e6a | -10.42321 | -45.01627 | 2025-10-19 04:12:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d28a36a-d1ee-3f9d-952d-850631809ad7 | -9.22738 | -46.0602 | 2025-10-19 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 21aa5b50-4e20-375f-9908-54152f1c8ed2 | -8.29778 | -42.30064 | 2025-10-19 04:12:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9cffb911-543f-3bbe-96d0-5a6fb9487ae8 | -11.36429 | -48.2134 | 2025-10-19 04:12:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef04a5c8-918c-3fd0-9d94-12b1b43b782d | -9.71527 | -43.37869 | 2025-10-19 04:12:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d7a1d149-ff9b-3cb3-bb59-a9efc4e5bd2f | -10.77901 | -39.4388 | 2025-10-19 04:12:00 | NPP-375D | NORDESTINA | BAHIA | Brasil | 2922656 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9da3576f-fd9d-3a84-bd91-cc462303d30e | -11.28776 | -45.03111 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa178560-0c5e-3ae4-8324-74f4255af491 | -10.88526 | -46.08693 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3b00378c-06bb-30cf-9c61-027a9c62282f | -9.88738 | -47.65571 | 2025-10-19 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f187833e-bd13-366c-97a9-f1d413dc8d4a | -12.98018 | -47.27094 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca3f7108-0fb8-3f58-b3d6-d1595de5c1fa | -11.80675 | -44.41571 | 2025-10-19 04:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1079c671-72b0-3ba2-b5d6-4e90de2feb55 | -12.15353 | -45.06178 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9308fdb-f65d-3da7-bf04-8f3bb1f48756 | -10.72079 | -44.53274 | 2025-10-19 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbbee7b8-0b8f-3ad2-9135-5326777f5f85 | -12.95131 | -47.30038 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c1ddacd-65f4-3335-96c0-f92c289df244 | -14.38607 | -40.77682 | 2025-10-19 04:12:00 | NPP-375D | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a74eca20-6c38-365d-ac3c-e09e05bf0b70 | -10.12855 | -44.52623 | 2025-10-19 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8eb803a-821a-3adc-963c-d41ccbcb54c7 | -11.88045 | -45.46031 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README32.md)
