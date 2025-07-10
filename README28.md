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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 147e3ef5-facc-3fd9-9dcc-8c7426bc6a5e | -10.5773 | -49.1533 | 2025-07-10 07:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 5be66098-242e-32e5-baa0-303672d11c07 | -8.5025 | -43.285 | 2025-07-10 07:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.3 |
| 4ceca87d-0ce8-372f-a554-8db1ecfed1f9 | -10.5773 | -49.1533 | 2025-07-10 07:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 80a63b93-ebb9-3a4e-a911-f1d73ad7b90e | -10.5776 | -49.1316 | 2025-07-10 07:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| a4d7a817-83d4-3074-9a69-9727a4d6d913 | -8.5211 | -43.3063 | 2025-07-10 07:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 186a6948-9ec9-3792-a4f9-a0a63b5eca21 | -8.5025 | -43.285 | 2025-07-10 07:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| b471ceff-9520-3f58-bf9b-c98888885403 | -8.5022 | -43.3085 | 2025-07-10 07:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 116.8 |
| 1a8d68e2-78de-3f9f-8dc3-4f57b32995f2 | -10.5776 | -49.1316 | 2025-07-10 07:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 09557294-19f2-393e-9be8-6cf823e4f09e | -8.5025 | -43.285 | 2025-07-10 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.1 |
| 4e64e135-e315-33f7-b184-66bc3e752e56 | -8.5022 | -43.3085 | 2025-07-10 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 119.7 |
| 7fcce8b4-fd6d-3edc-a17b-15f3cfd337f8 | -8.5211 | -43.3063 | 2025-07-10 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 320ce9d4-41ec-3c81-aa8b-e20e4c94bb5f | -10.5773 | -49.1533 | 2025-07-10 07:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| f15dcccf-ef40-3c39-9dda-6dd492918871 | -8.5025 | -43.285 | 2025-07-10 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.5 |
| f3b57c55-c52d-31d5-93b9-d01687e7decd | -8.5018 | -43.332 | 2025-07-10 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.0 |
| f95b1056-0c3b-3136-8f2b-ed828bc8f5f2 | -8.5022 | -43.3085 | 2025-07-10 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 143.3 |
| 5fa9a5ba-394c-3cc7-9b44-9114ad634b18 | -10.5773 | -49.1533 | 2025-07-10 07:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 02237a9b-3727-3897-b9bc-d56de10bf373 | -10.5776 | -49.1316 | 2025-07-10 07:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 9315d121-d4c0-3918-8275-1e90a29969a8 | -8.5025 | -43.285 | 2025-07-10 08:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 106.8 |
| eef96f8b-3de8-3fce-ad78-4882d0b00199 | -10.5776 | -49.1316 | 2025-07-10 08:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 15aea2a3-afa4-303b-a5df-457311de98f6 | -10.5773 | -49.1533 | 2025-07-10 08:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 620df76d-23d5-3242-9a0f-6b03893bceba | -8.5022 | -43.3085 | 2025-07-10 08:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 135.0 |
| bff767c2-af16-3698-9e30-5ebd58908926 | -8.5018 | -43.332 | 2025-07-10 08:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.2 |
| 7d771593-b3c0-310a-8683-719575b94c04 | -8.5022 | -43.3085 | 2025-07-10 08:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 135.4 |
| 49426704-e98a-3841-addb-26d8c9da00c0 | -8.5025 | -43.285 | 2025-07-10 08:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.5 |
| 1e53a916-6ce4-387a-8b72-93520bca4348 | -8.5018 | -43.332 | 2025-07-10 08:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.3 |
| 47d13fed-9620-32af-b90f-aec9999ad64c | -10.5776 | -49.1316 | 2025-07-10 08:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| b183c142-94d8-31c6-836a-8039a645c4e7 | -10.5773 | -49.1533 | 2025-07-10 08:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 089e87af-ab04-3c05-a327-85e87adc16fc | -8.5022 | -43.3085 | 2025-07-10 08:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 127.5 |
| 9ff307d3-01c9-393a-9234-a528be415bba | -10.5773 | -49.1533 | 2025-07-10 08:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 16079995-0d54-302c-a33d-1807f35bd52e | -10.5776 | -49.1316 | 2025-07-10 08:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| bff17e98-9d3f-3b71-8e9f-17b5015ebd5c | -8.5211 | -43.3063 | 2025-07-10 08:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 8597a58f-4550-3641-a17f-771411f929c4 | -8.5025 | -43.285 | 2025-07-10 08:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.4 |
| 9a8b2d81-78f4-3829-b7cf-30736ab7b399 | -8.5025 | -43.285 | 2025-07-10 08:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.1 |
| f7e1a074-4ada-3c64-986e-cc48e098b220 | -8.5022 | -43.3085 | 2025-07-10 08:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 133.0 |
| 0d55dcd6-55c8-3e2f-b328-e8c959441035 | -8.5018 | -43.332 | 2025-07-10 08:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.2 |
| 35309e45-d815-3590-891d-03b9387fec82 | -10.5776 | -49.1316 | 2025-07-10 08:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| b1f56a7b-cb2c-3c17-81f1-7da3fda6501a | -10.5773 | -49.1533 | 2025-07-10 08:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 73b5570a-8f47-34c8-a9c5-a68b85a6a969 | -10.5773 | -49.1533 | 2025-07-10 08:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 1a89a795-f3e8-3531-820b-ff17155215c7 | -10.5776 | -49.1316 | 2025-07-10 08:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 37ca6401-7e1b-371a-8728-426326d96593 | -10.5776 | -49.1316 | 2025-07-10 08:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 9bea1d2c-422d-3fc0-95a5-1652416f795a | -10.5773 | -49.1533 | 2025-07-10 08:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| e5d33898-6610-3f4d-8dac-abcfc54ff73a | -8.5022 | -43.3085 | 2025-07-10 09:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 111.9 |
| 25295fde-3a07-39e5-ac4b-5fe76d4f2ae4 | -8.3613 | -43.9548 | 2025-07-10 10:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| bb4317ea-c238-35c1-b48d-6d650278b6eb | -8.3613 | -43.9548 | 2025-07-10 10:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 3d483de4-2a27-313c-9203-813320cc5c7b | -8.5022 | -43.3085 | 2025-07-10 10:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 107.2 |
| b480a690-21b4-3ec0-970f-ad90d8808063 | -8.3613 | -43.9548 | 2025-07-10 10:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| a32c3300-9c49-30f0-8fdb-4bae3d0c97a5 | -8.3613 | -43.9548 | 2025-07-10 11:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 1a44d972-8ce8-3983-bb7a-fbca9e3213ce | -8.5025 | -43.285 | 2025-07-10 11:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| ae33995d-c49d-3d60-81ce-241de5c17600 | -8.5022 | -43.3085 | 2025-07-10 11:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 152.9 |
| 024c3671-e443-31e2-85c8-eb471514a51d | -7.0102 | -43.4865 | 2025-07-10 11:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 3a3104d3-619e-3978-9ab6-2e44ae3af7c8 | -8.5025 | -43.285 | 2025-07-10 11:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.6 |
| e158ba18-fcf4-3787-94ea-3fbbaabc79cf | -8.3613 | -43.9548 | 2025-07-10 11:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 897c544c-d00f-36e3-83ce-7d8e529b8145 | -8.5022 | -43.3085 | 2025-07-10 11:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 142.9 |
| 55304310-36bd-304e-81bc-0bb1116345ba | -8.3613 | -43.9548 | 2025-07-10 11:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 117.7 |
| decac622-c0f6-346a-9f31-8af105fd519f | -8.5022 | -43.3085 | 2025-07-10 11:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 148.2 |
| e6a53e64-1825-3040-8048-dc6ef6875045 | -8.5025 | -43.285 | 2025-07-10 11:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.2 |
| f98f1929-d49e-3d3c-a0e5-034ea581d81a | -8.5022 | -43.3085 | 2025-07-10 11:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 164.6 |
| 2d18fefc-6740-33eb-b6f5-2c9132b6e2e4 | -8.3613 | -43.9548 | 2025-07-10 11:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 132.3 |
| da6167e2-ff10-3b30-9ac3-6741f8b5b03e | -8.5025 | -43.285 | 2025-07-10 11:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 99.9 |
| 7a3741c4-6777-303a-847f-5d1118aeba77 | -6.8526 | -42.8015 | 2025-07-10 11:30:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.3 |
| 0a4434e5-c7a8-3ab8-90b4-12f0600da2f4 | -6.99473 | -38.16099 | 2025-07-10 11:30:00 | TERRA_M-M | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 7853c655-6d1a-317f-b70b-35bea361d6cc | -8.36476 | -43.91705 | 2025-07-10 11:30:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 3c541b70-c21a-31a0-9c73-ed1578566237 | -8.49634 | -43.32858 | 2025-07-10 11:30:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 50.2 |
| eb752f67-38c4-3529-9e0b-e922264cabae | -6.995 | -38.16707 | 2025-07-10 11:30:00 | TERRA_M-M | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 8baf18ba-5e20-3a08-8ed9-083fd7120ab8 | -8.50257 | -43.33701 | 2025-07-10 11:30:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.1 |
| 8bcdc559-5152-30bb-9dc4-c96729a08830 | -8.06418 | -43.12378 | 2025-07-10 11:30:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 33.3 |
| 7bde2189-8c64-30c1-8cd8-1ad0931c38bd | -13.62052 | -40.91121 | 2025-07-10 11:32:00 | TERRA_M-M | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 34.0 |
| 29a4a3d1-3f66-3245-8f81-174708b37b69 | -8.3613 | -43.9548 | 2025-07-10 11:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 116.6 |
| f156501b-0019-34de-890c-25df82f3b5d9 | -8.5022 | -43.3085 | 2025-07-10 11:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 139.2 |
| 4412362d-75e8-328c-ade6-ecf8c7485b6b | -8.5025 | -43.285 | 2025-07-10 11:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.7 |
| 7a25f91e-5926-3293-9ca5-2cc35fb17b33 | -10.5773 | -49.1533 | 2025-07-10 11:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 848c752e-fd33-31ea-8381-cecada75db6b | -8.5022 | -43.3085 | 2025-07-10 11:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 173.4 |
| 279c87e9-d99d-3453-815e-3ddac946ddf0 | -8.3613 | -43.9548 | 2025-07-10 11:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 3c6171df-514d-3065-a18d-32c4798ec65a | -8.5025 | -43.285 | 2025-07-10 11:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 110.4 |
| 69945532-e144-3b92-bbb5-1e20c040f737 | -8.5025 | -43.285 | 2025-07-10 12:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 107.1 |
| e81193ef-5271-3d3e-92bb-2c777657a377 | -8.5022 | -43.3085 | 2025-07-10 12:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 177.4 |
| 42fa5542-5f77-33d2-9e83-b6dc3c5efa02 | -8.3613 | -43.9548 | 2025-07-10 12:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 3e96bb50-1c39-3ecc-894c-c3ebbd84352e | -8.3613 | -43.9548 | 2025-07-10 12:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 1f962d67-4cf1-31c8-889b-711471837019 | -10.5773 | -49.1533 | 2025-07-10 12:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| a44ea505-0a2a-396e-816e-cad7fa4cf7a0 | -8.5022 | -43.3085 | 2025-07-10 12:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 154.5 |
| e0680058-edcf-3b0a-abe2-793def163c12 | -8.5025 | -43.285 | 2025-07-10 12:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.4 |
| 3e099a38-bb47-3693-b664-af0ccce9d116 | -8.5211 | -43.3063 | 2025-07-10 12:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 2ab61e7f-d374-3cbe-8681-8b677b66b2d2 | -10.5776 | -49.1316 | 2025-07-10 12:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 2a3db096-f454-3fe9-b3e8-2346e634cf63 | -8.5025 | -43.285 | 2025-07-10 12:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.6 |
| f7f755e6-5ca4-3b57-83a4-689d3779c19d | -8.5022 | -43.3085 | 2025-07-10 12:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 192.6 |
| 57f41a76-c428-3687-9979-1650074adedf | -10.5773 | -49.1533 | 2025-07-10 12:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| ea204951-ff02-3afd-a6a9-199cd3e2e7de | -6.1425 | -45.8676 | 2025-07-10 12:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 8d00b1fd-811e-3d2f-a6bc-c0f6cb1d1de0 | -8.3613 | -43.9548 | 2025-07-10 12:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 140.5 |
| ad597540-de23-3976-a2a3-1025db143b2c | -8.3802 | -43.9527 | 2025-07-10 12:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 2c2bdc00-c83a-338e-bd76-ee246a94d3d5 | -8.5022 | -43.3085 | 2025-07-10 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 179.2 |
| f0346443-8657-380b-8913-c39423b2f03c | -8.5025 | -43.285 | 2025-07-10 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.5 |
| 6686aba8-54a2-370d-a700-d573ef568b4f | -10.5776 | -49.1316 | 2025-07-10 12:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 03b70e1f-8013-3666-bac1-612b4e902384 | -8.3613 | -43.9548 | 2025-07-10 12:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 5484ab51-c613-3ac7-aaea-ce96a697cc4b | -10.5773 | -49.1533 | 2025-07-10 12:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 9128ac56-9002-357f-bb2d-f87894c225cf | -8.3613 | -43.9548 | 2025-07-10 12:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 65bc71a4-af8a-339c-8527-83760e66abde | -7.8814 | -47.8964 | 2025-07-10 12:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| f5f7bad1-1a05-3bbd-add6-2583dec80c5a | -8.5022 | -43.3085 | 2025-07-10 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 130.8 |
| 262ea6d5-c85d-30bc-bf1f-a641fa6ad1da | -8.5211 | -43.3063 | 2025-07-10 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 4ac47683-8f48-319d-86a1-92ac355a67e4 | -8.3802 | -43.9527 | 2025-07-10 12:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 4b4f719f-5be1-3f9f-9c70-7f6e1ed1d8f7 | -8.3802 | -43.9527 | 2025-07-10 12:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 100.5 |


[Clique aqui para ver as próximas entradas](README29.md)
