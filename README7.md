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
| b006f333-9d75-3d74-9613-300cee000d1d | -16.7435 | -42.7761 | 2025-10-19 02:50:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 390baaf2-0bf8-30c0-8583-4fced799b422 | -8.6032 | -40.1834 | 2025-10-19 02:50:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 120.2 |
| c8f77237-4571-31e2-8fd8-17c2ea58225e | -16.7834 | -42.7668 | 2025-10-19 03:00:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 197.4 |
| 38c1af25-1acc-3cca-a35b-67021b50b481 | -16.7641 | -42.7467 | 2025-10-19 03:00:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 031f78cd-6ed6-31e0-82b9-6a9ee2cd8125 | -8.6029 | -40.2083 | 2025-10-19 03:00:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 109.3 |
| 059ef727-e8f0-3c97-ba2e-39e4457c4d12 | -16.7628 | -42.7961 | 2025-10-19 03:00:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 131.9 |
| a5f8ba30-0603-36fc-b9d7-3f64279b29b4 | -10.8891 | -46.0814 | 2025-10-19 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| df75f5d2-7f22-395d-8359-d75717e7ebad | -8.6219 | -40.2058 | 2025-10-19 03:00:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 64.8 |
| 310de09e-da64-3476-b77f-de896877dc95 | -2.9128 | -52.7146 | 2025-10-19 03:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 623ccc10-a041-3afd-ba00-06d899189a4f | -16.7841 | -42.7421 | 2025-10-19 03:00:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 127.0 |
| ad43c270-8c25-35e8-9674-7ac8848b74f6 | -16.7635 | -42.7714 | 2025-10-19 03:00:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 415.2 |
| 89f1786e-cce6-3439-aabc-8203d2dca4dc | -11.6109 | -44.0678 | 2025-10-19 03:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 258c1369-1f94-3ea2-9f67-4db27271b86a | -8.6223 | -40.1809 | 2025-10-19 03:00:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 75.1 |
| f5856d11-4674-3aee-9e7b-88d9ebe36056 | -12.9917 | -47.2767 | 2025-10-19 03:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 60bd910f-d82e-330b-9eb4-4c67560ee679 | -2.9127 | -52.735 | 2025-10-19 03:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| fecf384f-069c-3d08-b2b4-2a5993d65a67 | -16.7435 | -42.7761 | 2025-10-19 03:00:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 192.4 |
| 1c68f1e9-0f55-37da-8bdd-c38bf69a8af0 | -12.9921 | -47.2541 | 2025-10-19 03:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 6b630400-8787-349f-9a26-9eb68a2e2903 | -8.6032 | -40.1834 | 2025-10-19 03:00:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 134.6 |
| 571f414e-60a7-3a27-94e9-2db04e094794 | -2.6841 | -49.5427 | 2025-10-19 03:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| eeb1d7ad-3f9f-369d-b907-531588f7b795 | -10.9347 | -60.9306 | 2025-10-19 03:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| fb5098c2-372a-3963-b00f-735c190b370e | -10.8891 | -46.0814 | 2025-10-19 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 7485f442-b6d3-35da-a8db-29ef49bbbe0c | -8.6029 | -40.2083 | 2025-10-19 03:10:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 90.1 |
| 7694ff5e-f2e7-3624-8206-ffa4a7754043 | -2.7026 | -49.5422 | 2025-10-19 03:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 2c050bf0-dd28-324b-b412-b82bf1093961 | -8.6032 | -40.1834 | 2025-10-19 03:10:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 142.7 |
| fb81fb25-ca22-329b-b3f5-ae16f4e44880 | -14.4377 | -51.4961 | 2025-10-19 03:10:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| bc048dc1-a5cf-39c4-8e2c-bd54e496a541 | -14.457 | -51.4935 | 2025-10-19 03:10:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 726e5208-2fef-3ab3-b7a5-5c08c1bb7880 | -2.9127 | -52.735 | 2025-10-19 03:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| d20ae891-432c-3da1-8ecb-7878738952b5 | -2.9128 | -52.7146 | 2025-10-19 03:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| de420361-17f6-3d21-a9ed-ddfe9fe4c58a | -8.6223 | -40.1809 | 2025-10-19 03:10:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 82.4 |
| fe7652af-ad8f-3d92-8058-a7ae6e899aaa | -11.4719 | -42.2341 | 2025-10-19 03:20:00 | GOES-19 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 72.6 |
| d6f3b527-b0c3-3dbf-b13d-f88b0219e9cd | -10.8891 | -46.0814 | 2025-10-19 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 98d1a905-d5df-3df7-9645-1bf1394d5585 | -8.6223 | -40.1809 | 2025-10-19 03:20:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 78.5 |
| 03ec0233-132c-30ee-ba51-66627f86d641 | -16.7635 | -42.7714 | 2025-10-19 03:20:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 729.4 |
| fc079239-9cac-3a0c-855e-5692c3d8d36e | -16.7435 | -42.7761 | 2025-10-19 03:20:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 225.1 |
| ff951a60-bbc8-3e07-8688-c401f69ac521 | -2.2527 | -51.9108 | 2025-10-19 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 67c54df6-c267-3bd4-9028-d5bd0e8e1afe | -10.916 | -60.9317 | 2025-10-19 03:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| fa5b8fb3-2f0e-3ebc-b433-9363c74a0ce6 | -12.9917 | -47.2767 | 2025-10-19 03:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 9e6ed11d-ef6b-35b3-a446-703eafc26cd6 | -2.6841 | -49.5427 | 2025-10-19 03:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 63739f65-6329-3ebc-a598-bf33f6881ff8 | -11.4724 | -42.2099 | 2025-10-19 03:20:00 | GOES-19 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 88.4 |
| bf779494-8bbf-3f15-a031-026c1dffcc70 | -8.6032 | -40.1834 | 2025-10-19 03:20:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 115.0 |
| edbfc620-812f-3ab9-bf12-680533bf1ee1 | -16.7441 | -42.7514 | 2025-10-19 03:20:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 33bbe425-e69d-3814-aa79-bd2475da8dfc | -16.7641 | -42.7467 | 2025-10-19 03:20:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 4ec3c314-a817-34e1-ae0e-d1cc9337b949 | -2.9128 | -52.7146 | 2025-10-19 03:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| a006e01c-4162-31fd-9486-169bf6ed375e | -16.7628 | -42.7961 | 2025-10-19 03:20:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 201.8 |
| 0b76631d-d2c1-3473-893d-f525943c84cd | -16.7834 | -42.7668 | 2025-10-19 03:20:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 128.5 |
| bf02aa2f-598d-3ed5-b3ab-8d84a808e401 | -8.6029 | -40.2083 | 2025-10-19 03:20:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 82.4 |
| 8ac92b52-05a7-306a-baf4-6ebce7de9bec | -2.7026 | -49.5422 | 2025-10-19 03:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 9823ec6c-9793-3b09-b3a1-8e2d8bd50af3 | -10.9347 | -60.9306 | 2025-10-19 03:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 291897b0-bfed-37ec-b4dd-b28453aea796 | -13.5405 | -43.0077 | 2025-10-19 03:20:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 60.5 |
| 8a6f0b83-1e95-397a-9266-c06f2203a3c7 | -12.9921 | -47.2541 | 2025-10-19 03:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| b4bb04eb-3bb4-327e-a715-e4594eadfb33 | -8.6223 | -40.1809 | 2025-10-19 03:30:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 68.5 |
| db71f5a5-f4d0-30fb-8bad-41783d70a730 | -8.6029 | -40.2083 | 2025-10-19 03:30:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 93.9 |
| bdda2c4a-d2d0-3444-983e-33628c49e369 | -13.5405 | -43.0077 | 2025-10-19 03:30:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 8dc7befc-6ca6-3b49-922f-396f4f9265b4 | -12.9921 | -47.2541 | 2025-10-19 03:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 85a8e287-eb58-3f0c-b53f-c493e81b18d1 | -14.0559 | -46.1552 | 2025-10-19 03:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 539a0ed9-6ce3-3db5-bfee-ed9b319b41f8 | -14.0555 | -46.1782 | 2025-10-19 03:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 153.2 |
| bd124139-8059-3373-83cb-117b8cd50982 | -14.0365 | -46.1585 | 2025-10-19 03:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 215.8 |
| fa016865-ab71-3438-b205-1e54cde3b09b | -7.1944 | -42.195 | 2025-10-19 03:30:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 43.2 |
| 77d7d138-4dc4-3396-9907-9fe1bcf58cf0 | -10.8891 | -46.0814 | 2025-10-19 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 591922dd-8aaf-38bf-8906-3c2836f91083 | -8.6032 | -40.1834 | 2025-10-19 03:30:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 109.6 |
| 4c44d1f9-067c-3a8b-a143-1bd23f713306 | -14.017 | -46.1618 | 2025-10-19 03:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 3b14c66c-7249-370a-a339-fee32591b54b | -14.4759 | -45.5751 | 2025-10-19 03:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 902cd59c-60ec-3acf-b403-ad1b6c7b5792 | -2.9127 | -52.735 | 2025-10-19 03:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| a17a1fcd-da04-3c48-bf6b-43f91acdbc4a | -12.9917 | -47.2767 | 2025-10-19 03:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| c5628273-8ed1-34b8-ab44-6d4e7b6f4022 | -14.036 | -46.1815 | 2025-10-19 03:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 221.1 |
| 8d4d93a3-b469-396c-be69-13c165ac10ce | -10.8891 | -46.0814 | 2025-10-19 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 2acd21a3-f28c-35cd-a25b-ea1bab63083d | -11.4724 | -42.2099 | 2025-10-19 03:40:00 | GOES-19 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 59.8 |
| 8b4ba30a-2cc7-38a6-9f27-13ca5b8c1fd5 | -7.1944 | -42.195 | 2025-10-19 03:40:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 55.0 |
| 1858393c-4929-35ee-92ff-7047f954c429 | -8.6223 | -40.1809 | 2025-10-19 03:40:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 65.3 |
| 49d53b78-49e3-3e77-aaae-5766daac75a5 | -8.6032 | -40.1834 | 2025-10-19 03:40:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 88.7 |
| 51914cb8-a913-337d-af2e-c18c10898ada | -8.6029 | -40.2083 | 2025-10-19 03:40:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 79.3 |
| a08729a8-3426-3d7f-9a23-0110ebfae8cb | -2.91054 | -40.40543 | 2025-10-19 03:40:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8102be6c-4c4e-3698-9866-ad64cdb04c6e | -0.98574 | -47.0773 | 2025-10-19 03:40:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 918b31d5-0c3e-3e75-9812-5540a2a4f281 | -4.11431 | -38.17192 | 2025-10-19 03:40:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c432ea0c-5b41-336d-bb9b-267eebc54c78 | -1.66649 | -46.76831 | 2025-10-19 03:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7007e7c4-b84c-3405-82c4-41a78a2ad5ab | -3.04469 | -40.11034 | 2025-10-19 03:40:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| cc239690-4bd6-32e2-9fa9-cc62ac8d9fb9 | -1.66421 | -46.76358 | 2025-10-19 03:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 308f0d09-d7f9-31a6-98f4-ab529d4215ad | -3.59346 | -43.04781 | 2025-10-19 03:40:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9cad2fd-4b6e-3673-baf3-c0391ba4ffdb | -3.59398 | -42.83554 | 2025-10-19 03:40:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eca834cd-859e-327e-b8e0-a9d6e36ec3c5 | -3.69552 | -38.86826 | 2025-10-19 03:40:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e98b1b48-cab1-31e5-82d4-392dfbd22423 | -1.66323 | -46.76933 | 2025-10-19 03:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc9f2709-54b2-30f9-8fda-acf3268af574 | -4.14508 | -38.23929 | 2025-10-19 03:40:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 45e03147-366d-3676-a984-7006e2c7d9f2 | -3.59398 | -43.04478 | 2025-10-19 03:40:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef1dcc67-56e1-3a3a-a99d-8ef835f1dca9 | -4.31571 | -38.36731 | 2025-10-19 03:40:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2b071c6f-a7da-351d-b14e-024534633b91 | -4.53489 | -37.88654 | 2025-10-19 03:40:00 | NOAA-21 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 49550c41-ef31-3b0e-a331-6c283857087c | -3.83707 | -41.77954 | 2025-10-19 03:40:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8a005c4a-c5f8-30b9-a5f0-5a0b71fcf463 | -4.53667 | -37.88565 | 2025-10-19 03:40:00 | NOAA-21 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 98914138-1b69-3e8a-b794-2bb27ee6d47f | -4.11361 | -38.17625 | 2025-10-19 03:40:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6aeffc3c-0966-3fdb-9837-34296348ea86 | -3.60575 | -42.85854 | 2025-10-19 03:40:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1915bb21-66a0-3611-8a62-cf56b359ea6e | -5.34233 | -46.06083 | 2025-10-19 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96167448-cd26-3aa0-8201-96768abc6152 | -10.16487 | -42.2064 | 2025-10-19 03:42:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3b0917d9-f458-330b-af6b-a9927c8f1b34 | -4.95804 | -45.0903 | 2025-10-19 03:42:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 17446b7e-cc7f-32b0-b027-f0bfa0835a7c | -7.33342 | -38.98593 | 2025-10-19 03:42:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 569d5cf1-5d6e-3919-97f8-9129714de5b9 | -5.76258 | -42.7108 | 2025-10-19 03:42:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a1720970-8989-33b4-884b-719d3d92fef2 | -4.31446 | -43.0201 | 2025-10-19 03:42:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2965c38b-02ee-399e-b221-7e0df41a8fbc | -4.96404 | -45.91087 | 2025-10-19 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5d9fbbec-36f0-313d-af87-8b3bcd72d000 | -8.62227 | -40.19402 | 2025-10-19 03:42:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 9b0ed6a4-2c53-353d-a1c6-2a61d5bc8ed0 | -8.34843 | -46.21776 | 2025-10-19 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2eca980e-1477-347e-acad-72b316aa35bf | -5.64444 | -44.81515 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96ba963f-3ad7-3e83-8f33-cf265ceba98f | -8.24718 | -43.99403 | 2025-10-19 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README8.md)
