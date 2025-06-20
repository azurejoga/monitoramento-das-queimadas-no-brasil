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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6603fc1-08dd-3028-a391-bc97f11c84d0 | -8.5724 | -51.5552 | 2025-06-20 12:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 57d4e5bc-bbf2-39b4-b55d-9b576277e993 | -4.8562 | -43.1907 | 2025-06-20 12:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 1ca882c8-2efb-3555-a118-c02a21829f0b | -14.0404 | -53.3669 | 2025-06-20 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| a08d9388-2532-31dd-ad5b-f0d6457dd92e | -10.5241 | -47.5822 | 2025-06-20 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 743b7f40-1ab7-32aa-81ed-51a5e8886846 | -11.5177 | -56.9862 | 2025-06-20 12:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 03e70987-b0ae-31c4-84db-952cb3067911 | -11.5366 | -56.9847 | 2025-06-20 12:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 9e9dc00d-f803-3209-9f6a-bdd72d475a36 | -8.5911 | -51.5537 | 2025-06-20 12:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| aedb026b-a38f-378f-929c-28337c33e6e4 | -11.6584 | -44.6207 | 2025-06-20 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 156.4 |
| ce1ff4d3-e8e8-3e48-b326-e8b8e74e82fb | -8.5911 | -51.5537 | 2025-06-20 13:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 3b741c9b-f191-3594-b5e1-d0648a372f30 | -11.9246 | -51.7621 | 2025-06-20 13:00:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| e9e3c0eb-6f9f-3027-8cae-7ff4570acd6a | -11.6584 | -44.6207 | 2025-06-20 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 52c9dd58-893d-3700-b8c7-34de9b291956 | -11.5177 | -56.9862 | 2025-06-20 13:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| c8958d00-7f5b-3f90-adf3-6bbac5f88758 | -11.1465 | -46.6573 | 2025-06-20 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 8eed69bc-637e-3a1b-bf16-6c53a13ea83d | -4.8375 | -43.1919 | 2025-06-20 13:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 0e2059d4-56bf-3277-b98d-e4b9b1a4235b | -11.5842 | -47.8723 | 2025-06-20 13:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| a897d5a4-33e5-39aa-874f-b28cda6ce922 | -4.8562 | -43.1907 | 2025-06-20 13:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 3b90270e-6e9b-3cf7-886c-8a4414cdedaa | -8.5724 | -51.5552 | 2025-06-20 13:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 92654baa-c4ca-3433-bb0b-7d4f0bc110f6 | -11.5366 | -56.9847 | 2025-06-20 13:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 627e2062-c57a-3a75-bd64-0532318ddfca | -14.2242 | -45.5269 | 2025-06-20 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 8c403f0f-e096-3fea-9ff0-565c2f3366c0 | -14.2247 | -45.5036 | 2025-06-20 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 13c4384b-1110-30c6-9657-e1cf15d665cd | -10.5241 | -47.5822 | 2025-06-20 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 5e2b6876-c134-3634-8aa7-909e3cbad8c9 | -11.127 | -46.6823 | 2025-06-20 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 67b7dc28-78e1-3d46-b854-e8f15a4ea68e | -11.5366 | -56.9847 | 2025-06-20 13:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| db4281b1-4a8f-3741-b785-c7f2d036779c | -14.2242 | -45.5269 | 2025-06-20 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 36023f2b-6b48-3001-a17a-c806367e3c47 | -4.8562 | -43.1907 | 2025-06-20 13:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 118.9 |
| afa3dc9e-8e59-3095-9803-4d803e02a2bc | -11.5842 | -47.8723 | 2025-06-20 13:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 3efb3933-2600-3ddd-aa93-f5c6f018d1f9 | -11.9246 | -51.7621 | 2025-06-20 13:10:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 276.6 |
| 4fad5768-029e-3181-8f0e-b7b567810578 | -8.5724 | -51.5552 | 2025-06-20 13:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| dad40975-66b7-3bc0-ac23-e69cc5c1e095 | -11.3232 | -45.2009 | 2025-06-20 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 969ab434-c090-37ac-978d-3faf37eb7eee | -4.8375 | -43.1919 | 2025-06-20 13:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 79b700aa-eb33-346d-b4c0-7193e6dc2ee2 | -11.9249 | -51.741 | 2025-06-20 13:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 157.3 |
| 87ab8f5b-5b81-3fd2-9879-d6ceccf2811b | -11.6584 | -44.6207 | 2025-06-20 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 24c20401-f4ba-3fe7-a6bb-fe50ef2e9d2c | -14.2247 | -45.5036 | 2025-06-20 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 216.8 |
| c5659e32-f5ab-3bdb-b002-59fcd0ac5c32 | -8.5911 | -51.5537 | 2025-06-20 13:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 8b28b82c-31b3-3fa3-9e35-3ca890d53e03 | -11.5177 | -56.9862 | 2025-06-20 13:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 2068a1aa-5f82-32ff-9ada-b1230f494d3a | -10.5241 | -47.5822 | 2025-06-20 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| f6adc6e8-5448-3330-8f0f-b7ec4f8b7907 | -11.5366 | -56.9847 | 2025-06-20 13:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 9ee72ad7-8fef-348b-a159-02b2963f6bf3 | -11.3232 | -45.2009 | 2025-06-20 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| dc011ed5-dc58-3daa-9194-70b38e1e5a5f | -14.2242 | -45.5269 | 2025-06-20 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 6665ebb3-ab72-3090-aa61-1db6bbdf6cb4 | -11.9246 | -51.7621 | 2025-06-20 13:20:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 185.8 |
| 02265e9f-6a8a-3cf0-b6a3-0d6c923f886d | -8.5911 | -51.5537 | 2025-06-20 13:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| ea437854-f6a7-3770-b1a5-3ad7d3dd0b93 | -8.5724 | -51.5552 | 2025-06-20 13:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 851a7950-de49-37c1-aaea-11c00a57cd6b | -11.6584 | -44.6207 | 2025-06-20 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 97dc6609-fd5b-3d7c-95ef-58b28d29a713 | -4.8375 | -43.1919 | 2025-06-20 13:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 133.4 |
| b3e51a4c-f0fd-3530-84a9-baf5fea8cd16 | -11.5842 | -47.8723 | 2025-06-20 13:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 0b7b6a87-fb81-3517-a04d-6d820dc650cc | -4.8562 | -43.1907 | 2025-06-20 13:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 139.4 |
| a019f97b-a408-34dd-ab3d-76bc102cc6e5 | -11.5177 | -56.9862 | 2025-06-20 13:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 24b4060e-19fe-3eb1-853d-9ae4f7194946 | -10.5521 | -46.9785 | 2025-06-20 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| d6d6984a-c8c2-3294-8360-bd58cfad3261 | -14.2247 | -45.5036 | 2025-06-20 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 249.9 |
| 5cb28940-9a20-3b02-97a8-7dfff63f6699 | -11.9246 | -51.7621 | 2025-06-20 13:30:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 04073534-6411-3ca8-ad22-147e12f6c4cc | -11.5177 | -56.9862 | 2025-06-20 13:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 143.9 |
| 01fd54f7-cfce-3d6b-8c6e-c96d9996853a | -8.5724 | -51.5552 | 2025-06-20 13:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| bfe05765-6f37-378d-81bc-203dff128771 | -14.0404 | -53.3669 | 2025-06-20 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| a686a6b1-b546-3a39-b93e-b1b6da8e56f5 | -11.127 | -46.6823 | 2025-06-20 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 46c64ccc-945d-3bb9-98d1-82203dcd9583 | -11.3232 | -45.2009 | 2025-06-20 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 76056b3d-7ae7-356b-916f-53f67b2d166f | -10.5241 | -47.5822 | 2025-06-20 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| b48a98ce-12f4-3780-964b-4a8ce5004c60 | -11.6584 | -44.6207 | 2025-06-20 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 2f8adc83-fa88-30cc-aa3c-df96062733a1 | -14.2247 | -45.5036 | 2025-06-20 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 260.3 |
| 843cddb8-c4c1-3301-8cc3-d78896fcaf69 | -4.8375 | -43.1919 | 2025-06-20 13:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 8e4fd20a-ac98-3884-b972-83368b6890cc | -11.5366 | -56.9847 | 2025-06-20 13:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 1592b728-8e35-3155-a9a6-d0a4191078c5 | -4.8562 | -43.1907 | 2025-06-20 13:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 7df1c971-e747-32be-a2c1-75977200e506 | -14.2242 | -45.5269 | 2025-06-20 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 71af3fd6-c725-3e32-8971-557cd4d7352e | -11.5842 | -47.8723 | 2025-06-20 13:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 553cf050-475f-344b-b119-6e6901182e1f | -14.0404 | -53.3669 | 2025-06-20 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| d804dc65-0e24-368c-93b1-9f0f453cec6e | -4.8375 | -43.1919 | 2025-06-20 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 629860f2-f8b2-3347-a8d4-cc1ed322cd9d | -11.3232 | -45.2009 | 2025-06-20 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| c1e64c81-2497-3d87-88db-0d4243770168 | -11.5366 | -56.9847 | 2025-06-20 13:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 65e485fb-0160-355a-ab99-f7f30e415ea1 | -4.8562 | -43.1907 | 2025-06-20 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 3c622f29-226c-359f-843d-1b064c50a9b3 | -10.5241 | -47.5822 | 2025-06-20 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| c22ffca6-effa-3485-b040-4c72b0c8981b | -11.5177 | -56.9862 | 2025-06-20 13:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| f77132ce-e236-3afe-acb0-5fdd24998d8e | -11.5842 | -47.8723 | 2025-06-20 13:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| f3ca492f-994d-31df-9f47-363f0404b8df | -8.5724 | -51.5552 | 2025-06-20 13:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 8f2355a5-74de-3c37-8c53-0f4ec511ee6a | -11.6584 | -44.6207 | 2025-06-20 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 74b77746-b0c9-3835-94f6-c6877066d915 | -11.9246 | -51.7621 | 2025-06-20 13:40:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| bd770a40-124a-3dbe-92bb-5b1845a8d3ad | -14.2247 | -45.5036 | 2025-06-20 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 299.0 |
| a3f77931-b312-3d49-a190-8feb311dda97 | -14.2242 | -45.5269 | 2025-06-20 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 175.0 |
| 9302816e-bca9-3356-9d54-6b257f2d53e1 | -11.9246 | -51.7621 | 2025-06-20 13:50:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 57ca390d-8b6a-3268-9079-d6865256b277 | -8.5724 | -51.5552 | 2025-06-20 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 16e80eee-4b03-3073-a3c2-36ee6920c936 | -14.2247 | -45.5036 | 2025-06-20 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 296.5 |
| 9b0cd131-9440-3d3c-b724-7e5d7c89e050 | -4.8375 | -43.1919 | 2025-06-20 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 2886ca60-6492-36f2-98a7-18aa2535cdb3 | -11.6584 | -44.6207 | 2025-06-20 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 2fad2239-3812-32ca-9a89-20fe52d3d336 | -11.3232 | -45.2009 | 2025-06-20 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| ad778ec8-8926-3a2b-99ff-08bc072dda97 | -11.5842 | -47.8723 | 2025-06-20 13:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| e833f665-b47e-3391-9646-a417ae0f0bc8 | -14.0404 | -53.3669 | 2025-06-20 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 2c5812f7-7551-311c-82bf-1e7190f4e90f | -11.5177 | -56.9862 | 2025-06-20 13:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 45cde914-c01a-3ae7-9996-a8cbf99a1c9e | -11.7756 | -54.3551 | 2025-06-20 13:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| dd1f1d7a-fb43-3f4f-95e9-2cc85441ff49 | -14.2242 | -45.5269 | 2025-06-20 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 690e31b5-7fc7-3f25-9d55-e2cb1e1d073e | -11.7754 | -54.3756 | 2025-06-20 13:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 1d4c5fca-c17a-3e88-86d0-c67a4cb8e5b0 | -10.5241 | -47.5822 | 2025-06-20 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 12e61ae8-889e-3dce-964a-808bb4ef7304 | -11.5366 | -56.9847 | 2025-06-20 13:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 135.0 |
| f2cba4a0-8957-3ffa-91b1-36456a1fc7cc | -10.876 | -53.7614 | 2025-06-20 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 574a2ba5-ae0a-38b1-a630-66008e57342c | -14.2242 | -45.5269 | 2025-06-20 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 4f21647f-39cf-3252-a7e7-5ed87c998954 | -11.5177 | -56.9862 | 2025-06-20 14:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 149.1 |
| 64278a0e-1471-3bc8-86ac-40db9bfb1918 | -11.6584 | -44.6207 | 2025-06-20 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 726e502d-4db6-3ddc-9313-36ae94db2d69 | -4.8375 | -43.1919 | 2025-06-20 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 5ac5e968-831a-361c-87a4-52806a28659a | -11.3232 | -45.2009 | 2025-06-20 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 1f663b45-b5f7-349a-b644-73cf6216c9b5 | -10.8571 | -53.7631 | 2025-06-20 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 5ee2666d-9e03-3c0c-ab91-aa718b95844b | -11.5366 | -56.9847 | 2025-06-20 14:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 9a3eff16-aafd-347e-92bd-39911f2caba4 | -14.0404 | -53.3669 | 2025-06-20 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| bb623c0d-e1a1-308c-8b15-9df2f87f49f1 | -11.9246 | -51.7621 | 2025-06-20 14:00:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 217.9 |


[Clique aqui para ver as próximas entradas](README33.md)
