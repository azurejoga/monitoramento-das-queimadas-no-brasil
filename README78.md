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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1743459a-300a-31cd-8b79-769b286b5a3b | -19.58486 | -56.70346 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 613e6bfc-f938-34cd-a858-42e28522e13e | -19.58415 | -56.7076 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 615fe7d7-6e96-373f-8f4c-b917d46ba6c4 | -19.58344 | -56.71175 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 5688b620-2c75-3f19-a53e-4675f27a310e | -19.58272 | -56.7159 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 807babf2-c8bb-36b4-a826-4c7d5e1ce473 | -19.58201 | -56.72005 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 417869a4-92e0-38a8-943c-1e2158dcff77 | -19.58134 | -56.70277 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 204be706-2e5e-3da8-952b-70a62e76c8e4 | -19.58129 | -56.72421 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| c70fa77e-5cb7-3006-826c-8c04caa2be92 | -19.58063 | -56.70692 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 67893372-bb0f-3607-86e7-9410132344aa | -19.57992 | -56.71107 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 7ce9f5e3-8576-3740-aade-9495eb54632a | -19.5792 | -56.71522 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 1fd5d746-094f-3b8c-88f4-9100ca70a8c4 | -19.57849 | -56.71937 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 54da985b-775c-32bf-b27c-25dd78c9bc3f | -19.57777 | -56.72353 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 21ce486b-a0df-3c4d-b318-d8f17f205adf | -19.57711 | -56.70624 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| c2b36f47-eec4-36df-8c7a-f8e3a398d146 | -19.5764 | -56.71039 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 6a4ed5cd-bcc3-3c2e-b837-a1ad06142c7c | -19.57568 | -56.71454 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.9 |
| c644ab0a-2ddf-3624-a17c-71ef007de6a7 | -19.57496 | -56.71869 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.9 |
| cabc2eb7-8cbd-3767-b332-7a1ca0b954a5 | -19.57425 | -56.72285 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 38093938-3a99-3e2d-9cfc-26a8eeb8ec5e | -19.5736 | -56.70557 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 6fc9c443-a155-39db-9194-d48fc4e1cbba | -19.57288 | -56.70972 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| a69f5ea8-8f42-3cb8-a6a0-a7a390196ee1 | -19.57216 | -56.71386 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 012bf35d-a542-35fd-a526-c99039d91461 | -19.57144 | -56.71801 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.9 |
| f51d9d93-d855-30ef-9ae6-3a384d119957 | -19.57073 | -56.72217 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 8ea4a990-7d00-39d2-b352-5d1d802447c3 | -19.56799 | -56.69592 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| fa906107-2590-3ca6-abdb-52f52b08b263 | -19.56447 | -56.69524 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f80da117-cda4-33e5-8d59-fe5604c9fde7 | -19.49689 | -56.62759 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7af9820d-0ee1-3009-af1e-c6027fecd207 | -19.49623 | -56.58918 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 19fd2114-1235-3ca8-9be1-ae59fc0a89c5 | -19.49537 | -56.69996 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 48c4a3ba-8a30-3296-abbd-25fe406fb88c | -19.49408 | -56.62278 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d4b37426-d313-3594-8bf3-b19baa1703bc | -19.49399 | -56.68683 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e2735dca-a252-3168-b9a8-85ebc300f7e8 | -19.49338 | -56.62691 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d23c0993-87b1-3e3c-853c-d6435f57bb21 | -19.49327 | -56.69098 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3c89ff9a-0d93-3878-80a8-a8f51fe183a7 | -19.49185 | -56.69928 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e0df529b-5be6-324d-a96a-24c783a13a8c | -19.48987 | -56.62624 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ec7d8c71-c701-325a-8ef2-b979738ec5d1 | -19.48904 | -56.69446 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 443c4234-792d-3500-86b6-929a63557a4f | -19.48833 | -56.69861 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| fd39efad-1e8d-3d98-8711-2d12322bfead | -19.4877 | -56.65996 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e4961f08-667e-3d37-8af2-7db4e25ea5c8 | -19.48565 | -56.62969 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| aa6fead1-8b0e-3b0a-bc7a-46e2369e02ac | -19.48552 | -56.69378 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0d705813-8b50-334b-bf5a-2cb6283d4298 | -19.48494 | -56.63381 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| ccfe4d6f-ea94-312d-af4e-97a7400e475b | -19.4849 | -56.65514 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 5b99e3f5-4eeb-3f66-96f8-410de8f9a4ca | -19.48423 | -56.63794 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 890f7eb6-85f1-3691-8d80-c3754f1d16d0 | -19.48352 | -56.64207 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8783abc1-815b-3eb2-9940-e1a8f8adb32d | -19.4828 | -56.64621 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 599e7725-49be-35b4-9d1e-8864e2a5a8d1 | -19.4821 | -56.65033 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 86468200-78d6-3fe0-a436-1b57e551c27e | -19.48134 | -56.67584 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1f81cffc-9d28-3250-8b36-244b51dd0733 | -19.48067 | -56.6586 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 7338a599-88d4-382e-b5d7-3d27f1fb557f | -19.47996 | -56.66273 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 41b4fd5a-0326-3b17-ad2c-75e4dc3dd691 | -19.47782 | -56.67516 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8fd19332-0e15-32d9-815f-c93050ce5726 | -19.47634 | -56.70488 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| a7d8529d-db39-3095-951d-721455be204a | -19.544 | -56.70844 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 05822b76-a84b-339c-9e19-235b7d910659 | -19.54328 | -56.71259 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 64e35cf8-5542-38e8-914d-763ad9a808de | -19.54049 | -56.70776 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| a70a37c5-3b90-3e48-bcc7-6b24408a000e | -19.53976 | -56.71191 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 9aabdd4c-e218-3e5c-bce0-74de8222ad23 | -19.53904 | -56.71607 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 3c625fe9-9591-318d-a496-e805093cabf6 | -19.53697 | -56.70709 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| b5831674-2e91-3c55-8ed5-6d01a54ed5d3 | -19.53624 | -56.71124 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 778bd6a0-1529-3d74-9704-7aedbfb0dd8f | -19.53552 | -56.71539 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a85d2107-217c-320b-9adf-7df7b3fac3e2 | -19.53345 | -56.70642 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| eb8e169f-8918-3650-a7b3-3ebc53f4e860 | -19.53272 | -56.71056 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 04e6e09b-8dfa-3fc8-a5c6-383a2a0655b2 | -19.52992 | -56.70574 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 20f2c959-71fb-3c1f-8e3e-cdf07e722ccd | -19.5292 | -56.70988 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 5a482455-64b9-3232-b61d-1ade1de84bd9 | -19.52847 | -56.71404 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a509a910-55c4-3053-b7a5-b71a1b620ddc | -19.52706 | -56.70607 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| c087f94f-d22e-37fe-8f1c-d4389589f274 | -19.52641 | -56.70506 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| e77712f6-eee6-3d2b-99d5-a4a88a9b5736 | -19.52635 | -56.71023 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| bae9e3ad-1896-310d-80b5-bf5b4e7b3f85 | -19.52568 | -56.70921 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| daf125bb-8068-306c-9d40-4bb52d2e69b1 | -19.52565 | -56.69294 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2e0d4046-841d-37a2-a28e-5b3665788b5a | -19.52496 | -56.71336 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| eca9dcbc-a914-362d-a43e-b1b41e1f6a0e | -19.52495 | -56.69709 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a2d8d916-f936-3810-a49f-6fad38ff1447 | -19.52434 | -56.69609 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2838e8f8-7649-318f-a91c-e86fa4e38dd7 | -19.52424 | -56.70124 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 888ed32b-a98d-3590-abf2-90d78998c457 | -19.52361 | -56.70024 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ee6d5e5c-794c-3317-9027-31e930c28cd7 | -19.52353 | -56.70539 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 676158a6-7421-3d79-833b-35158c3b3622 | -19.52289 | -56.70438 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 72e307fb-4ab0-38c9-b44a-bcbbb1484337 | -19.52283 | -56.70955 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| ceea569f-85e4-34e1-a488-aa4cf99789f7 | -19.51095 | -56.58775 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| b90d3c7c-6a49-3ffc-91c9-741268ce774f | -19.51025 | -56.59187 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 08489409-d85e-3e33-a9f3-4e24b391cc69 | -19.50955 | -56.59598 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| ddb4ce9f-1eed-301f-8cef-abc203986836 | -19.50948 | -56.68126 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 86d1c090-4a1f-3d8a-91d1-c9a939f4a166 | -19.50877 | -56.6854 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| be75c8de-93ed-33a3-8329-a9ade46d81c8 | -19.50806 | -56.68955 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 0ef1f615-1683-360d-9281-9cee58c7e07a | -19.50745 | -56.58708 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 5ad78c8a-fbc1-3b2b-a359-8115f4d320e0 | -19.50674 | -56.5912 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 8eed0642-b7a7-3e0a-a50f-f894caa0b8a8 | -19.50604 | -56.59531 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| db3e2278-f7b9-32ef-aca5-9d71947f8b38 | -19.50525 | -56.68472 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 06963f02-1346-36ea-971a-d4b755d724f8 | -19.50454 | -56.68887 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a73c9169-00b8-3c9a-bb4e-92210958d296 | -19.50394 | -56.58641 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9feff297-6ea6-3b58-9cb6-4a253523e1ad | -19.50383 | -56.69302 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 51b2ad3e-d5cc-330f-8fa6-d1fb04cc3326 | -19.50324 | -56.59053 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c4154ec9-ff16-3ff2-a1d2-4a968c5dd10b | -19.50253 | -56.59464 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 71ea8f56-f870-386f-8638-4a6d2f0aaba1 | -19.50173 | -56.68405 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9f8f8958-6b6a-3eac-9975-b5b5a78ad866 | -19.50114 | -56.58163 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e8bad437-2e1f-3d9b-beb3-3f70783e6ef4 | -19.50102 | -56.68819 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0cc66f59-7a62-3067-8db0-27d7d5d93145 | -19.50044 | -56.58574 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 862de2fc-3e4b-32a5-8afa-9ec186c66cb8 | -19.50031 | -56.69234 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 243a923c-b415-3a20-bdd9-2063da549d3e | -19.49973 | -56.58985 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ea1eedd0-a03b-314f-b83d-1986feec9cfb | -19.49961 | -56.69649 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 10fed095-673c-3e50-b7ee-41cab140396a | -19.49903 | -56.59396 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5d36b74a-8c18-393c-b36a-2a090d1cd982 | -20.88508 | -57.25976 | 2024-10-30 04:49:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82580773-17c2-3966-8c55-d7c2efa3ca25 | -17.80437 | -57.38029 | 2024-10-30 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |


[Clique aqui para ver as próximas entradas](README79.md)
