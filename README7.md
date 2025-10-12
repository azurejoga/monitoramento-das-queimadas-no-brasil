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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d9940a3-b5f7-3aaf-839a-311af28cdeca | -14.0161 | -43.4703 | 2025-10-12 00:50:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 2d7da2d0-2efc-388e-940f-a388643c5215 | -2.5424 | -47.7893 | 2025-10-12 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 08531ccf-c140-3a9c-b5e3-06fc2805a5f8 | -13.6778 | -43.8424 | 2025-10-12 00:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 7dd4e33f-4c96-3611-954e-2d87e0aeaa51 | -7.0474 | -45.2538 | 2025-10-12 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 7a3b0c7c-9f3f-3181-892f-b2e88bdcaf77 | -7.0478 | -45.2083 | 2025-10-12 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 2d2a2c4a-f7cf-3b1d-a600-369fac64252c | -14.0155 | -43.4943 | 2025-10-12 00:50:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 121.2 |
| eae7117d-8021-3fb6-bcf1-6746e273e0f9 | -9.0161 | -67.4275 | 2025-10-12 00:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 37bda814-be90-3fde-bcdb-d3f846efee98 | -7.0661 | -45.2521 | 2025-10-12 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 3bbf3555-345f-3468-bc5e-be885e8e1177 | -4.271 | -46.9369 | 2025-10-12 00:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 101.0 |
| b79ff5ba-da4c-36fa-bf19-55da8d18a4ca | -11.752 | -54.7255 | 2025-10-12 00:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 9262b0de-a4fa-3bee-b814-5fa5fb7816e5 | -7.0666 | -45.2067 | 2025-10-12 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 2bc5b175-350a-3146-94eb-2b33e6e50542 | -7.5212 | -46.538 | 2025-10-12 00:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 3271ca9e-2e56-3965-8ab4-b7d985ad5ef4 | -13.6578 | -43.8697 | 2025-10-12 00:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 12ac1279-747d-35b0-b0d0-98db8d927498 | -13.6583 | -43.8459 | 2025-10-12 00:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |
| a3e1d507-e970-3023-82c2-ac61022fe307 | -9.016 | -67.446 | 2025-10-12 00:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 6fb9691e-e3ec-3622-a315-fc09443d26e3 | -12.5089 | -47.4362 | 2025-10-12 00:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| c9ab3eee-d035-39cb-88b3-d50fff582279 | -3.5371 | -48.9195 | 2025-10-12 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 92db6f14-69bd-3601-94de-d0904283620c | -13.6778 | -43.8424 | 2025-10-12 01:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| ab16b373-8453-35a9-b651-44171cafd19d | -14.0161 | -43.4703 | 2025-10-12 01:00:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| ccb5749c-1bf0-3aa3-9c04-e88f86d4325c | -7.0476 | -45.2311 | 2025-10-12 01:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 28034b16-97cb-3e05-93a7-c2ef1f67008f | -4.271 | -46.9369 | 2025-10-12 01:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 103.4 |
| a44c539b-885d-398d-8355-6d50c376f581 | -2.5238 | -47.8115 | 2025-10-12 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 8bf4bb4c-f0b7-3221-8be5-6708b1fa0da6 | -13.6583 | -43.8459 | 2025-10-12 01:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 116.2 |
| deb2ccaa-c9b7-3f39-9d37-fefc087f31cf | -9.016 | -67.446 | 2025-10-12 01:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| f81aad76-1332-35c3-a9ae-b066f8255eb8 | -19.0319 | -57.5382 | 2025-10-12 01:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 86.2 |
| d9c48248-dc22-3c30-925e-a975b73a4c69 | -17.5897 | -42.4246 | 2025-10-12 01:00:00 | GOES-19 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 47a2387e-8381-3004-8814-84260c9d2d65 | -2.5423 | -47.811 | 2025-10-12 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 145.9 |
| 44c79a5e-9e56-3145-8a98-37c66ffc127e | -9.0161 | -67.4275 | 2025-10-12 01:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| cd329b9a-25fb-3c94-aa46-013f1ffbb6af | -7.0666 | -45.2067 | 2025-10-12 01:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 206.4 |
| 3e416ac3-6815-317b-b730-3a14818b4b60 | -13.6578 | -43.8697 | 2025-10-12 01:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 6b0046b2-a813-34de-b61f-55d08f48c590 | -13.6773 | -43.8662 | 2025-10-12 01:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 35e76340-cf41-324b-9728-75de40e90fd6 | -14.0155 | -43.4943 | 2025-10-12 01:00:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| d3ac7a83-7e76-322f-a012-436092b47b70 | -7.0664 | -45.2294 | 2025-10-12 01:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 3a3cba19-1e9c-34a3-9c66-473128eb98a6 | -2.5424 | -47.7893 | 2025-10-12 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 3800f348-964c-3fc8-9a03-b9542ab15784 | -7.5212 | -46.538 | 2025-10-12 01:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| b560c64b-e8b1-32f4-9c76-cc7b506443b3 | -6.5851 | -44.6098 | 2025-10-12 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 4b92e003-6683-3559-bc33-aa38f5abc7db | -7.0478 | -45.2083 | 2025-10-12 01:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 596010b9-e32f-3528-8bc2-65fb197cfbb5 | -9.0161 | -67.4275 | 2025-10-12 01:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| a0386f16-ff48-377d-8385-28689952e945 | -19.0316 | -57.5589 | 2025-10-12 01:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 75.6 |
| d1ed0397-f797-376d-bade-9a7875e7c253 | -13.6778 | -43.8424 | 2025-10-12 01:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| f7913faa-a294-3438-a297-700652c41b2c | -2.5423 | -47.811 | 2025-10-12 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 134.3 |
| 964c8a6e-7728-349c-95ef-2f4677f8b457 | -7.0664 | -45.2294 | 2025-10-12 01:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| e71c2da0-0fe3-3dec-8458-2fac077fe2af | -19.0515 | -57.5564 | 2025-10-12 01:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 91.6 |
| f0413f0d-f2a0-3461-900f-f28817cb735f | -5.9355 | -43.9494 | 2025-10-12 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 03114a5c-8fdc-3da4-9b8f-b797bd333b5c | -7.0476 | -45.2311 | 2025-10-12 01:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| f1387ec7-c1f5-39ba-a120-ad418b7ddaa7 | -13.6578 | -43.8697 | 2025-10-12 01:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| d6c56077-139f-3df0-9fd8-957bed26d802 | -2.5424 | -47.7893 | 2025-10-12 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 6c7e3e57-7966-3096-b917-42c45b84c487 | -14.0155 | -43.4943 | 2025-10-12 01:10:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 898a766b-a1be-3ceb-ad2a-74b33d4782b4 | -19.0319 | -57.5382 | 2025-10-12 01:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 159.7 |
| a565f944-dbeb-3319-b16d-b8df44934b95 | -4.271 | -46.9369 | 2025-10-12 01:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 24846837-8622-3169-a02f-3f14ba0baa70 | -7.0666 | -45.2067 | 2025-10-12 01:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 8d6a3551-af20-315c-80f5-89d1718cd164 | -9.016 | -67.446 | 2025-10-12 01:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 3acc7865-58bc-3706-a916-7951e56a6162 | -9.0345 | -67.4455 | 2025-10-12 01:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 33bcfd12-f3a2-3eaa-a39c-05d778ec8d14 | -19.0519 | -57.5356 | 2025-10-12 01:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 123.7 |
| 88e1626e-c4c4-35df-a125-0f1cf650f9af | -6.5851 | -44.6098 | 2025-10-12 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 709bea62-8c58-34fd-84e6-a64ff810bfc1 | -5.9358 | -43.9263 | 2025-10-12 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 52831bc5-4f46-38f7-a70e-365e6b9183d1 | -7.0478 | -45.2083 | 2025-10-12 01:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 14058cd9-d0aa-3e70-86b4-e307650ec4a5 | -13.6773 | -43.8662 | 2025-10-12 01:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| f2d42f65-454a-32d1-aa31-6e9746a08c02 | -22.2152 | -49.6841 | 2025-10-12 01:10:00 | GOES-19 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 101.3 |
| 09e28fbd-4254-332a-aa36-cec22fc93627 | -17.5897 | -42.4246 | 2025-10-12 01:10:00 | GOES-19 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 525c12db-f01f-379b-9c46-7e266cf07b21 | -13.6773 | -43.8662 | 2025-10-12 01:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| a8a6a2ac-b800-3579-9c4b-1ea2bd97bbb2 | -17.5897 | -42.4246 | 2025-10-12 01:20:00 | GOES-19 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 5c42aa6a-9f58-3d28-9def-2a2985bcd34a | -9.0161 | -67.4275 | 2025-10-12 01:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 47c27a3e-2a7c-3146-9484-d7bd86db14f8 | -7.0666 | -45.2067 | 2025-10-12 01:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| bf973312-8faa-395e-9c75-453988c254cb | -2.5423 | -47.811 | 2025-10-12 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 144.0 |
| dc127f16-4313-3d38-81bc-895921a21d7a | -14.0155 | -43.4943 | 2025-10-12 01:20:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 439200eb-2e49-321b-83d6-de6c458583cc | -4.271 | -46.9369 | 2025-10-12 01:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 0e84667f-cd04-309f-9fba-66b0094ff42e | -19.0316 | -57.5589 | 2025-10-12 01:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 64.8 |
| 6576d78f-aa29-3662-a969-ec6c92fb510e | -19.0519 | -57.5356 | 2025-10-12 01:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 5e1a7f21-d3cd-36d6-9002-fb272734f3ed | -9.016 | -67.446 | 2025-10-12 01:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| a8e3e9c9-2c87-38ce-a2d2-23e9f38c96c7 | -2.5424 | -47.7893 | 2025-10-12 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 1291aa5c-fea6-3061-9904-e621962397cb | -15.6825 | -46.625 | 2025-10-12 01:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 9dd3a9fb-3e81-3b26-bdf6-f2fa690b668d | -19.0515 | -57.5564 | 2025-10-12 01:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 60.5 |
| 33f977c0-bd30-3f57-a15d-992a4dc46524 | -19.0319 | -57.5382 | 2025-10-12 01:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 104.1 |
| b6767c28-68cf-346d-a3fe-e83c73a3a331 | -4.271 | -46.9369 | 2025-10-12 01:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 32746426-03b8-3aef-be62-ec53eb24bcc5 | -19.0515 | -57.5564 | 2025-10-12 01:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 61.8 |
| fc664c75-eb8a-3362-a0c6-8acc270f6f33 | -19.0316 | -57.5589 | 2025-10-12 01:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 63.0 |
| 468efb10-6dbb-3868-bb09-f6a43bdb40c2 | -2.5238 | -47.8115 | 2025-10-12 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| b6928af3-71fa-3a00-85d0-df95f99296b3 | -2.5424 | -47.7893 | 2025-10-12 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 9e393e9e-4dd5-30ca-a297-77fc806222a1 | -9.0161 | -67.4275 | 2025-10-12 01:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 27579df0-bff6-38fc-a1f4-00c77e347c2f | -19.0519 | -57.5356 | 2025-10-12 01:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 61.3 |
| cbadadf1-674e-3d5d-a924-670a3014750e | -19.0319 | -57.5382 | 2025-10-12 01:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 102.3 |
| 9211e24f-dd2d-3ebc-8e6d-3e37a1791356 | -2.5423 | -47.811 | 2025-10-12 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 133.3 |
| f09d712a-6f5e-3039-9198-dc84cc858f71 | -17.5897 | -42.4246 | 2025-10-12 01:30:00 | GOES-19 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 89.0 |
| eabc5014-673f-3629-96d7-4dd36b83d7ed | -15.6825 | -46.625 | 2025-10-12 01:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 492bec77-0fe9-3800-a1ba-c82f9c6d1c1a | -14.0351 | -43.4906 | 2025-10-12 01:30:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 58d6e1c3-2aea-3a01-8787-24ab5e19d282 | -9.016 | -67.446 | 2025-10-12 01:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| b3711533-424c-3959-8b67-52f14a1807f0 | -12.7685 | -45.8363 | 2025-10-12 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 2c731c66-bb11-3004-a333-e2e0826dd05f | -19.0319 | -57.5382 | 2025-10-12 01:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 85.4 |
| b08c3fad-1331-343e-95c0-c674e92d098a | -2.5424 | -47.7893 | 2025-10-12 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| f376b467-1f9f-3a5f-9d9d-6f9cd3d2913f | -9.0345 | -67.4455 | 2025-10-12 01:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| e8a5a42d-1b22-375a-9782-b20c3c245276 | -4.271 | -46.9369 | 2025-10-12 01:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 8dcb4d20-b8e7-3240-b8be-8c17996abecf | -2.5238 | -47.8115 | 2025-10-12 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 7a820ec8-f9e2-3089-9b7f-9cabcada46c1 | -9.0161 | -67.4275 | 2025-10-12 01:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 9127d05e-71b0-3b6b-92a7-6d85ac2f74a2 | -14.0351 | -43.4906 | 2025-10-12 01:40:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 44a01af9-34e1-3626-be4f-fcf9c3e5d0b2 | -17.5897 | -42.4246 | 2025-10-12 01:40:00 | GOES-19 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 84.5 |
| a738379b-8ff7-3430-afc7-0165c52ca07a | -9.016 | -67.446 | 2025-10-12 01:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| ec69a103-80e0-326c-8c42-839893db403b | -15.6825 | -46.625 | 2025-10-12 01:40:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 99.5 |
| d171da51-1578-3dc2-bce1-83c6c85b6998 | -13.322 | -47.1144 | 2025-10-12 01:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.3 |
| b629e426-b39f-3e5f-bc09-3c07cfb04fe8 | -12.7685 | -45.8363 | 2025-10-12 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |


[Clique aqui para ver as próximas entradas](README8.md)
