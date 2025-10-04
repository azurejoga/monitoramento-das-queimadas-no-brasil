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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72d495e7-fdbe-31ce-bff0-07a2a84c8eda | -9.6293 | -54.3158 | 2025-10-04 14:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| ca6ddc09-5bec-35ea-b7b6-89bc0efd6d0f | -12.9471 | -50.9838 | 2025-10-04 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| de04fb9b-bf39-3ac6-b537-62b946344b80 | -5.9584 | -43.5072 | 2025-10-04 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| e8809adc-6006-3fa8-a62d-ad5260585729 | -7.7938 | -42.5607 | 2025-10-04 14:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 160.0 |
| f46fa65c-ee5f-34f4-9c25-6d242c961893 | -10.8334 | -47.2118 | 2025-10-04 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 91648e46-fd02-394a-b419-5e4d4ac0a363 | -12.0895 | -45.1583 | 2025-10-04 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| e9b80cea-87e8-3963-bcca-88f334b73319 | -15.3797 | -47.952 | 2025-10-04 14:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 131.4 |
| ac73d166-d3a3-3f65-a926-8910a6615316 | -5.8739 | -42.5289 | 2025-10-04 14:00:00 | GOES-19 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 125.3 |
| c6965b94-b50e-3c3e-8c8c-329650720adf | -16.3627 | -51.4752 | 2025-10-04 14:00:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 4bddea95-13a5-3a07-8fc3-d2aa233e148e | -11.792 | -46.8409 | 2025-10-04 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| bcebf8ab-51fe-3038-a6ab-ebece68ee7a1 | -12.0891 | -45.1814 | 2025-10-04 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 752204a2-051e-39c8-bf78-d7672a01c6f9 | -13.0959 | -47.8876 | 2025-10-04 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| e94c22a8-ce21-3409-a75d-fb5c03e5d467 | -14.3899 | -45.9601 | 2025-10-04 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 02d868f5-f2d1-31dd-bf5a-87504890918d | -13.3127 | -47.61 | 2025-10-04 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 107.9 |
| d5078f18-0496-3f27-bcce-bcfb362f6907 | -12.7194 | -48.5611 | 2025-10-04 14:00:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 1946c215-bc54-336e-97fd-f0cde8ffb82e | -9.1713 | -49.9622 | 2025-10-04 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 8fe3fbc6-dab3-370e-aba7-0edc19462a23 | -7.5504 | -42.3965 | 2025-10-04 14:00:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 114.6 |
| 717f5b47-4e5a-39aa-ad33-ee957788a5dc | -9.9628 | -45.7897 | 2025-10-04 14:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 92.2 |
| d039055a-1cf2-35ba-a1a9-cc78e31dba82 | -12.3222 | -50.6322 | 2025-10-04 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 6a541511-0401-352c-adaa-4ce12a0680b2 | -14.8461 | -54.7903 | 2025-10-04 14:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 1efd3ec1-3e5f-362f-83d7-faad5cb9a82a | -13.251 | -47.8203 | 2025-10-04 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 7f16b2a2-8099-3a62-bbc8-bf70792205f7 | -11.9138 | -49.9289 | 2025-10-04 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 875e2210-0107-381b-a96b-0b037f1673f7 | -13.3225 | -48.1216 | 2025-10-04 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 9bfdf277-f7a6-3ede-be0f-b74e5efb29db | -7.4416 | -46.9666 | 2025-10-04 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| e7dfc4f3-ffc0-3ae2-b221-6bc9237ba446 | -7.813 | -42.5349 | 2025-10-04 14:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 109.9 |
| 8cbc654d-fa7f-3633-9dc5-74f37ef27f74 | -12.8265 | -46.8509 | 2025-10-04 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 4e99daf5-3d62-314c-a21b-fc32b59eac48 | -10.5838 | -48.696 | 2025-10-04 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 1306d4ad-998f-38f0-93b4-2d03b363dcff | -8.8526 | -46.812 | 2025-10-04 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 80d68ce2-d92a-36c7-9dcc-3e5584b78c50 | -7.7684 | -46.2479 | 2025-10-04 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 3b217c02-f5b8-35de-bfdc-bb22438ae535 | -8.7777 | -49.9123 | 2025-10-04 14:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| a42ce7d5-2b0d-3754-a16d-763808bad407 | -11.449 | -43.4803 | 2025-10-04 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 092d68b8-a2e8-3b90-9102-54012049cb7e | -15.5413 | -46.8114 | 2025-10-04 14:00:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 120.0 |
| d3fb341d-a734-3449-8c87-cbc902fd1045 | -7.7941 | -42.5369 | 2025-10-04 14:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 139.9 |
| ee0b68e6-8e7e-370c-9d96-180e1c2598a0 | -11.5683 | -47.6749 | 2025-10-04 14:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 5a31d552-dd47-3493-9168-3cf3fab3980c | -12.3158 | -45.3776 | 2025-10-04 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 0d69eac5-decd-3a7c-9937-b57c5085fadd | -6.1234 | -45.9139 | 2025-10-04 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 81b67e75-a1bc-3dd4-bdcb-f36951523b45 | -6.2515 | -44.2242 | 2025-10-04 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| b56ce138-92f8-38e5-91b5-ae56782ca235 | -13.2934 | -47.6129 | 2025-10-04 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 60.7 |
| f7aad46e-dd50-3db3-b985-612f8ab05e2e | -7.7491 | -46.2944 | 2025-10-04 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| dbf9d59c-2748-35cc-a6e9-0f849c9279d1 | -12.5866 | -54.7474 | 2025-10-04 14:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 0bb63640-eb39-38ac-b9af-5683045069e0 | -6.2408 | -45.3424 | 2025-10-04 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 128.3 |
| c6981b26-9d24-388a-a6d9-aeb2ff9f93d5 | -9.648 | -54.3143 | 2025-10-04 14:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| bc7c9ad7-c7fe-3a21-af39-fef8f5dfa16b | -11.1268 | -47.9077 | 2025-10-04 14:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 265.7 |
| 1c753c9d-330e-3aed-85a4-adbb3b796639 | -7.8593 | -48.2037 | 2025-10-04 14:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 182.7 |
| e0182331-39e2-33ef-a0d7-453dd4053795 | -7.4229 | -46.9682 | 2025-10-04 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| e3a86bfb-55b1-33d6-aca1-2fde9500aef0 | -11.3265 | -53.9665 | 2025-10-04 14:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 03d1288d-3263-37d0-a13f-5c7048a1f052 | -7.7563 | -42.541 | 2025-10-04 14:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 130.6 |
| 0f8a2bba-a047-3176-87a8-cd08d5aaf853 | -15.1357 | -45.7104 | 2025-10-04 14:00:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 4509685e-ca83-33b5-b2a1-786b1a51d973 | -15.5408 | -46.8344 | 2025-10-04 14:00:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 1ce770f8-a9a2-3e39-8ddf-5a7ca4c3956c | -10.1462 | -50.2952 | 2025-10-04 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| faad2b4c-5b1f-39e9-b6bc-9a73ad06fe18 | -11.48 | -44.9711 | 2025-10-04 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 214593a6-c641-3408-95e2-03fb163fd387 | -8.8529 | -46.7897 | 2025-10-04 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 739d244b-32d8-3b5f-b153-04d29c8577de | -13.6717 | -51.234 | 2025-10-04 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| dd085634-5826-358c-b8f6-e7b56f74153e | -16.097 | -51.0611 | 2025-10-04 14:00:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 136.6 |
| cfa5f53a-c366-3b07-b13f-95fc465a0466 | -13.5119 | -47.2655 | 2025-10-04 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 2e433b9c-b38e-33c0-9ac7-4c603743d5ec | -13.7472 | -48.0806 | 2025-10-04 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 6f5dc1d7-f3b1-34aa-816b-73f58e0ed560 | -12.8978 | -47.1557 | 2025-10-04 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 8006f085-1331-3106-8543-6b6ee2298287 | -11.5069 | -46.7671 | 2025-10-04 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 196.3 |
| 8d7f9249-598e-3d55-904f-722b1047a3eb | -13.1156 | -47.8625 | 2025-10-04 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 67fe4430-dd8c-3c8c-8274-d84093e4cfcd | -15.3179 | -46.3011 | 2025-10-04 14:00:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 111.3 |
| a55cac1a-592d-3b50-966b-ebe49240fdb2 | -8.8523 | -46.8343 | 2025-10-04 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| c460911f-80d1-3cc8-a5f4-ee5f6122f9b0 | -10.5835 | -48.7178 | 2025-10-04 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| ed3ac381-b9ea-3d34-92bd-45eb8012b784 | -7.0558 | -42.7782 | 2025-10-04 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 226.6 |
| 0d1d8293-912a-3c88-8682-c90cbdae4c33 | -13.3233 | -48.077 | 2025-10-04 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 79293039-a65f-33e4-addb-1cc5d10eb8e0 | -11.4988 | -44.9915 | 2025-10-04 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 6e9caea5-93c9-3684-9914-6e7bc6157a7b | -6.154 | -44.6217 | 2025-10-04 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 2671b116-e996-3101-a4dc-b853a15f354c | -9.1716 | -49.9408 | 2025-10-04 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 0b1d383b-2633-3257-9b38-850115434605 | -11.7924 | -46.8184 | 2025-10-04 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 8a496fef-2ea0-3de0-a81d-ed2f75492012 | -13.116 | -47.8401 | 2025-10-04 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 243.2 |
| d02f5021-6c39-35a2-9190-6874a218b4f8 | -14.2949 | -45.8613 | 2025-10-04 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 74770d9d-ba80-3f1d-a5cb-50a359218273 | -6.2596 | -45.341 | 2025-10-04 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 228.6 |
| cd63b23d-b8c6-31cc-abf0-042b9c234717 | -5.9879 | -44.3598 | 2025-10-04 14:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 5e9ef27e-dab8-3efc-9f8c-f437f1e26c81 | -14.6716 | -48.3157 | 2025-10-04 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 122.7 |
| c2ac201a-9bc1-38d0-83d0-e36fb1f04c66 | -13.3032 | -48.1244 | 2025-10-04 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 4faac579-5e89-3a21-b38f-f1b13bdfd48b | -6.2325 | -44.2487 | 2025-10-04 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| c94ee6ff-65cf-3a7b-b68e-b5409ba6356f | -7.4414 | -46.9888 | 2025-10-04 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| aa44bf5c-f760-3925-b672-51f5d0954ef1 | -13.3229 | -48.0993 | 2025-10-04 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 27a2f9bd-c2a8-3ac5-b201-ec2bdcbb32c8 | -8.1615 | -43.3465 | 2025-10-04 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.4 |
| b4e61655-eaac-334f-adca-d1b4f30d118e | -13.0968 | -47.8429 | 2025-10-04 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| b7cdbc15-ffbb-3e14-8027-b50c9da20572 | -14.5941 | -52.4976 | 2025-10-04 14:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 4b5af3d3-30de-36c5-91b6-7fb109200c7a | -7.878 | -48.2021 | 2025-10-04 14:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 9e2ee75d-d388-3ebb-975e-198c6048c756 | -12.9468 | -51.0053 | 2025-10-04 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 157.4 |
| bc28ca49-1517-39fb-9e32-56eff3c2fe92 | -14.672 | -48.2933 | 2025-10-04 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 76.4 |
| b2a446d0-15fa-3808-bdb0-598a765bb5e2 | -6.1542 | -44.5989 | 2025-10-04 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 83301864-e886-30cb-b76e-92178d80d0ac | -13.4732 | -47.2714 | 2025-10-04 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 11b9f2e1-776e-3399-b7df-31cb15541c0c | -11.4486 | -43.504 | 2025-10-04 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 165.1 |
| e8ffe71b-1809-3966-86b2-b5cd033f23c0 | -8.7589 | -49.9139 | 2025-10-04 14:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 2079963f-42b6-3dfb-887e-338c440ab8c1 | -15.5402 | -46.8574 | 2025-10-04 14:00:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 119.4 |
| c1b4c591-02fb-3be4-994e-9ac45104049f | -12.3853 | -50.2595 | 2025-10-04 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 537.5 |
| cc9e6bab-fc3f-3f27-8a1b-2d0cdf8381da | -13.1164 | -47.8178 | 2025-10-04 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 0fe1fca2-9e6a-384a-b9e8-67a3dfca28b9 | -15.5211 | -46.838 | 2025-10-04 14:00:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 43533e34-b17c-3784-9349-ff7671a3223b | -8.5598 | -47.6593 | 2025-10-04 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 82d0380d-909b-3363-896e-e3c41dc08f4e | -7.7746 | -42.5865 | 2025-10-04 14:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 121.4 |
| b2312e9a-7970-3d95-b9d4-7287e803c90c | -11.8818 | -44.9815 | 2025-10-04 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| cc288ca5-2cfa-3c12-9906-11cb3490821c | -14.8271 | -54.7719 | 2025-10-04 14:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 0be4b797-8388-3dfb-9375-948aec98ce7c | -6.1728 | -44.6203 | 2025-10-04 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| fb8aeba7-150d-3155-9e20-da4421cfdf7c | -7.0369 | -42.78 | 2025-10-04 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 309.0 |
| 4cb33667-7162-3b5a-8770-5bf3dd4e0284 | -9.3196 | -45.7515 | 2025-10-04 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 163033d9-a440-38c1-b698-add75645f080 | -12.4105 | -51.0917 | 2025-10-04 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| ab662b1b-b7e9-312f-b444-e62519594077 | -11.1271 | -47.8856 | 2025-10-04 14:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |


[Clique aqui para ver as próximas entradas](README153.md)
