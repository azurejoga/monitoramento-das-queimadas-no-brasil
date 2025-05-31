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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4b86795-2234-3062-9097-b65e2a7925d1 | -12.27654 | -44.58963 | 2025-05-31 00:37:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f6b833d5-2b3f-3657-97d3-8c7e5e0bbd18 | -10.4572 | -47.94818 | 2025-05-31 00:37:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| ff450fed-04c4-31b3-b2e5-633c190f228e | -10.45597 | -47.93913 | 2025-05-31 00:37:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 66dd7c2e-ae52-3d93-b13e-bb003ebea2d8 | -10.67386 | -46.39414 | 2025-05-31 00:37:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f7dd0730-5884-3d8d-a70e-9dcb55b6056c | -11.82518 | -51.27228 | 2025-05-31 00:37:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 2cf0ebe3-aba0-3c51-97d8-4e250a098fc0 | -12.02261 | -49.53537 | 2025-05-31 00:37:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f9a4bd49-e50d-3d67-9e40-7824a60431e4 | -8.65939 | -47.81497 | 2025-05-31 00:37:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| efb6eefc-aa2c-3266-a1df-bd500fbfd701 | -10.63999 | -49.43941 | 2025-05-31 00:37:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 108387cc-2223-3470-95c8-6793df029e1a | -10.63862 | -49.42915 | 2025-05-31 00:37:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 4ae13dfb-f986-3b01-a36d-e3a1a706a348 | -11.83431 | -51.25689 | 2025-05-31 00:37:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 99ca5bbf-6ea9-34e8-bd0f-6f5fe150e474 | -11.13764 | -53.92879 | 2025-05-31 00:37:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 19d1ef38-e8ea-31cf-bb85-f40e819afaa3 | -11.83603 | -51.27076 | 2025-05-31 00:37:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 202.0 |
| f31533fb-cd7e-39f4-9a77-339b53f0d9c1 | -10.46486 | -47.93785 | 2025-05-31 00:37:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9176940d-cce1-38ac-8160-4de93f39d661 | -11.79022 | -48.27739 | 2025-05-31 00:37:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c4c44b5d-6ef7-3b33-878f-2360c1696da0 | -13.10093 | -52.29713 | 2025-05-31 00:37:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 38.0 |
| bf8e724b-36f7-30f0-af9c-46876c513bee | -10.46609 | -47.9469 | 2025-05-31 00:37:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 40.6 |
| c170a06f-a764-3667-90e2-18d4b3d6b650 | -14.62009 | -47.97133 | 2025-05-31 00:37:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bc125c60-f453-3a56-82e2-2513ba881eb7 | -13.9571 | -54.488098 | 2025-05-31 00:38:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7e8aafae-7c7f-3f4d-8ee2-51a95beec722 | -7.2447 | -43.114601 | 2025-05-31 00:38:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6725823a-4bd5-3264-adac-d995521c8969 | -14.0199 | -55.120201 | 2025-05-31 00:38:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 10724943-ca7d-3047-bf67-d59060df2f53 | -12.019 | -49.5149 | 2025-05-31 00:38:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61b7e5be-59b3-336a-9426-41ffd676e3a9 | -10.6573 | -49.434502 | 2025-05-31 00:38:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c3b9901d-5c04-38a9-a79a-06ff17d734f5 | -7.2304 | -43.058201 | 2025-05-31 00:38:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a2ec8978-6551-35e6-b4e8-3e4ea173dd75 | -11.9207 | -54.811001 | 2025-05-31 00:38:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 544f6842-0cda-30cb-8b30-9fa774a5aaae | -8.8123 | -49.837898 | 2025-05-31 00:38:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 675ec0a1-8b92-3dc5-99ed-dd3edb80854e | -10.828 | -56.942001 | 2025-05-31 00:38:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 99698dd3-2455-3e3e-a3f2-c4047eb62669 | -10.3034 | -57.125702 | 2025-05-31 00:38:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb77bcc6-c0fb-3d5d-9de5-725c57958ac2 | -11.6853 | -48.250301 | 2025-05-31 00:38:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f0570a0-3cf0-3ad8-a4ae-63cbe36a7db2 | -12.1872 | -54.241001 | 2025-05-31 00:38:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb18d861-da91-32c8-a9ba-6d356ca8bfc4 | -10.3052 | -57.134201 | 2025-05-31 00:38:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 18d58226-ad3e-3aa2-a1f0-3f00b1fbca3a | -14.033 | -55.133499 | 2025-05-31 00:38:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c680686a-ad8b-3d01-b58c-56d984e5a8aa | -16.652201 | -49.353802 | 2025-05-31 00:38:00 | METOP-B | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8283ae07-97f6-3323-92ea-b2e22024219e | -18.8374 | -53.594299 | 2025-05-31 00:38:00 | METOP-B | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b5d25a3b-836f-3047-828b-9f7d653cedb3 | -11.8289 | -51.266102 | 2025-05-31 00:38:00 | METOP-B | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0efe05c1-5dae-3bc2-b289-9b1fd3d975d2 | -12.1046 | -54.664101 | 2025-05-31 00:38:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df24e287-f314-3df6-9b4c-fd8282579949 | -11.8404 | -51.2714 | 2025-05-31 00:38:00 | METOP-B | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 29384a0d-0191-33e7-8e43-4419015514ec | -10.6454 | -49.427399 | 2025-05-31 00:38:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49948948-b3dd-3957-a5a5-223c24d071b6 | -19.195 | -52.081402 | 2025-05-31 00:38:00 | METOP-B | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ef3fb99e-c066-38a0-8d47-996ea161c446 | -11.1447 | -53.945099 | 2025-05-31 00:38:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aad2807d-6cf9-3a33-9bf8-f0eee068fb75 | -16.6542 | -49.362099 | 2025-05-31 00:38:00 | METOP-B | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6ea01753-1d5d-360a-86f1-e14b0b5e5866 | -11.9109 | -54.813202 | 2025-05-31 00:38:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bc94e7d4-abc8-3336-8aa7-abfd7d711bb4 | -12.0309 | -49.521599 | 2025-05-31 00:38:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6b196f9-d21d-348b-9f19-c2621169dd38 | -13.9457 | -54.4828 | 2025-05-31 00:38:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ce2ab98f-d7e2-394d-9b09-fdbedecc0bae | -14.5956 | -58.749401 | 2025-05-31 00:38:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dc247b7b-3d13-3e95-98ec-eb95397e9d0d | -14.0314 | -55.125801 | 2025-05-31 00:38:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 08176e9a-0a18-3c67-9ce6-480e1fe94702 | -9.5339 | -54.7598 | 2025-05-31 00:38:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 94d0f4b9-e97c-314c-8b3c-21047d8fc53e | -11.455 | -49.098 | 2025-05-31 00:38:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 72961513-d65f-3380-8437-7dc86866056f | -12.0114 | -49.526402 | 2025-05-31 00:38:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 28e91d3d-43c7-3a6e-af50-f6645960d645 | -10.8262 | -56.933601 | 2025-05-31 00:38:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa120628-2883-38b8-abbb-7d2ce87c2a81 | -19.196501 | -52.088699 | 2025-05-31 00:38:00 | METOP-B | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| cc4908a9-75e0-384d-8194-e645d0d50453 | -8.4801 | -49.610298 | 2025-05-31 00:38:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c15fb55e-9f52-31a1-9036-e50b233307d8 | -6.1445 | -42.602001 | 2025-05-31 00:38:00 | METOP-B | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a1623288-a311-3a9a-b7db-b9f65a2a0396 | -11.8369 | -51.256199 | 2025-05-31 00:38:00 | METOP-B | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b032b816-0c87-3aaa-8971-6e7242e9bf8e | -6.9982 | -44.615601 | 2025-05-31 00:38:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 472c4e7d-11e3-3314-bb92-44a1da9ea4cd | -10.4553 | -47.947399 | 2025-05-31 00:38:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d1ce3072-7fb2-3882-9de8-df3436d33608 | -10.4524 | -47.9356 | 2025-05-31 00:38:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1966b364-2293-3f2d-ada9-09676756b7c7 | -8.4777 | -49.600498 | 2025-05-31 00:38:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37c042fc-2273-3f74-bb4a-0a40c719ef02 | -9.248 | -51.216499 | 2025-05-31 00:38:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95f15020-861e-3faa-a7d2-62449f94a9d5 | -12.0169 | -49.505798 | 2025-05-31 00:38:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5fd6e2b4-d004-34db-9a9f-10cd1c842439 | -10.8378 | -56.939899 | 2025-05-31 00:38:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b2e5aa0-603d-336d-984f-a44cfbad3698 | -12.0287 | -49.512501 | 2025-05-31 00:38:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6fb30030-3d0f-3abd-97a7-86f420a22dc9 | -11.688 | -48.261101 | 2025-05-31 00:38:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c149f2c9-1f2a-31c9-8af8-5758ed3bd70c | -11.8272 | -51.258499 | 2025-05-31 00:38:00 | METOP-B | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 73f8a0b2-922e-3c02-944d-42b0e36469c5 | -20.610901 | -48.860699 | 2025-05-31 00:38:00 | METOP-B | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 91a9e874-cec3-3ce7-8f28-97b5ecf8d692 | -10.6551 | -49.424999 | 2025-05-31 00:38:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0459ec38-edae-3a29-adcf-fbd19e56e4a3 | -11.1416 | -53.931198 | 2025-05-31 00:38:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46a0945e-2dc2-3346-b16d-e70a081d237b | -12.1888 | -54.2481 | 2025-05-31 00:38:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cfe8b5ee-06a6-33b7-85af-5828846adff3 | -12.4649 | -54.904499 | 2025-05-31 00:38:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a54eb2f1-2ec3-3b92-84b9-7676414db408 | -13.0931 | -45.2626 | 2025-05-31 00:38:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 79b40a08-ee84-3c74-b91f-b5fff797bb54 | -8.205 | -49.7999 | 2025-05-31 00:38:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c59eb911-21a2-3789-b24b-6574284d41f4 | -10.6476 | -49.436901 | 2025-05-31 00:38:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bd48366e-97d9-3060-9018-ef68ffcb33a7 | -10.7328 | -49.2743 | 2025-05-31 00:38:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a1d272c4-9d96-38dd-bab1-e41dc0f83bd7 | -11.8386 | -51.263802 | 2025-05-31 00:38:00 | METOP-B | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 19811b2c-66b9-3671-a1c3-53764f87b757 | -10.4622 | -47.933201 | 2025-05-31 00:38:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53cc9c7f-a396-3998-8384-821316a37bff | -10.4651 | -47.945 | 2025-05-31 00:38:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f7bafe2-f489-335b-8890-7acc5b1f9827 | -11.1499 | -53.922001 | 2025-05-31 00:38:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e368b936-b354-3a49-8608-799ea1ef26e1 | -11.1431 | -53.938099 | 2025-05-31 00:38:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1d3f9e8-670e-34b2-a77f-27f4b1466948 | -12.1031 | -54.656898 | 2025-05-31 00:38:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 64fd8b6f-4014-3336-ada3-67a446f30d0f | -8.2027 | -49.790199 | 2025-05-31 00:38:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a52790b-bf0b-3d16-9083-e16d09022b09 | -7.0078 | -44.613201 | 2025-05-31 00:38:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 225fae23-bb60-3a40-a1ee-0656491ff2d0 | -11.9125 | -54.820499 | 2025-05-31 00:38:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c69edab9-3896-304b-a93a-2cf4aa29b429 | -13.9555 | -54.480701 | 2025-05-31 00:38:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7d7681ef-7cb0-3cbd-ba1c-b87957e96354 | -7.2471 | -43.084099 | 2025-05-31 00:38:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c2c19c6f-a0c7-30af-9cba-0adf2739f03a | -13.0834 | -45.265202 | 2025-05-31 00:38:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2b46638a-0a29-30b1-8615-3f33fce63c2b | -11.8307 | -51.273701 | 2025-05-31 00:38:00 | METOP-B | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 05993ba5-be87-3267-93a2-ee49ca03d572 | -11.4527 | -49.088299 | 2025-05-31 00:38:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 87d09347-9963-3574-be93-2553dfca524a | -13.6251 | -47.429401 | 2025-05-31 00:38:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5aa20e29-fe54-3673-a3b5-d3e8dce58bf5 | -7.2376 | -43.086498 | 2025-05-31 00:38:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a170b798-94f0-3dc3-a66b-17e33eef8608 | -7.228 | -43.089001 | 2025-05-31 00:38:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a2e0184a-a21f-39cd-aaeb-87fa3a041caf | -7.2255 | -43.119598 | 2025-05-31 00:38:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 519f1595-bc82-34a0-adad-276567517a4d | -6.2104 | -43.3489 | 2025-05-31 00:38:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 309c48fe-bc64-39f5-81e9-6af578335ff7 | -8.1953 | -49.8022 | 2025-05-31 00:38:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a74b0d43-381d-3060-889c-ab72e0d568bf | -12.4665 | -54.9119 | 2025-05-31 00:38:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dfe5ab69-3f18-363e-907e-d2c11354476a | -12.4551 | -54.906601 | 2025-05-31 00:38:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 380a5c61-92c2-348d-ac2c-5bb361332b60 | -8.4754 | -49.590599 | 2025-05-31 00:38:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b10f69aa-0fd6-3d3f-848c-77d278df4f6d | -7.2231 | -43.150101 | 2025-05-31 00:38:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dd3ab511-9cb0-3eb5-a141-09512c03c531 | -13.0971 | -45.278702 | 2025-05-31 00:38:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 57700ebe-7f67-3688-aa2e-62e669b69009 | -10.7351 | -49.284 | 2025-05-31 00:38:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9993b1c0-3497-3d25-ad0c-7a3563457eef | -12.0092 | -49.5173 | 2025-05-31 00:38:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2dcede5b-0772-35d0-a041-c561eeb32744 | -10.6431 | -49.4179 | 2025-05-31 00:38:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
