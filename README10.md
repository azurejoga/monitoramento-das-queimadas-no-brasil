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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 408ac936-32aa-351c-930e-95cc2e347b0c | -3.3968 | -42.270699 | 2024-10-03 00:12:15 | METOP-B | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 176a4048-4e74-3dc9-b365-750d7165cf3a | -3.3984 | -42.277599 | 2024-10-03 00:12:15 | METOP-B | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0c2c8fd4-51da-3b5f-b25f-8ed9b247e266 | -3.3999 | -42.2845 | 2024-10-03 00:12:15 | METOP-B | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 50883e7e-5bfc-3e7d-8fe3-cc14004a2202 | -3.3854 | -42.265999 | 2024-10-03 00:12:16 | METOP-B | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 88fcf588-2a15-3789-8e1f-7aec03e9fa49 | -3.387 | -42.2729 | 2024-10-03 00:12:16 | METOP-B | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d09ad600-5dd2-388a-a48f-d2bbe243a630 | -3.3886 | -42.2798 | 2024-10-03 00:12:16 | METOP-B | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53638354-25d7-3f58-b237-c3c676d82eef | -4.568 | -47.991501 | 2024-10-03 00:12:17 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dac42e07-af5e-37f9-9636-e76e1e93ad86 | -4.5704 | -48.0023 | 2024-10-03 00:12:17 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31520a09-cf06-38f8-9b94-56c8a0a411b4 | -4.5728 | -48.013199 | 2024-10-03 00:12:17 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 277b37a8-0456-340e-b3b7-3d3eff7ca3de | -3.5962 | -43.794399 | 2024-10-03 00:12:18 | METOP-B | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 193cb382-b017-3aae-802d-efa6ed44cb68 | -3.5977 | -43.8013 | 2024-10-03 00:12:18 | METOP-B | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d1d3c94-f173-3c34-9459-f95bb4c92b72 | -4.097 | -46.131001 | 2024-10-03 00:12:18 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 06c57a73-83ff-327a-b729-02e210549dc7 | -4.0988 | -46.1394 | 2024-10-03 00:12:18 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d85a61d4-952b-378e-94d3-f9fcef21dceb | -4.3813 | -47.4669 | 2024-10-03 00:12:18 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 890bbc22-dd91-335f-b987-78fbdf8bc674 | -4.2834 | -47.487999 | 2024-10-03 00:12:20 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa428dae-9d3c-3757-adcc-ac37aca88430 | -4.1562 | -47.188999 | 2024-10-03 00:12:21 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b8916750-2020-34ec-98fa-e999450de65c | -3.6007 | -44.7794 | 2024-10-03 00:12:21 | METOP-B | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 440c3b14-53a4-3ae4-b60f-e96c6f911d61 | -3.6024 | -44.786701 | 2024-10-03 00:12:21 | METOP-B | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e627b465-fe03-32c0-b1b3-35c1023c13e2 | -4.1395 | -48.372501 | 2024-10-03 00:12:25 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b2cc156-afde-3847-897f-1ab55ea422c8 | -4.1419 | -48.383801 | 2024-10-03 00:12:25 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e758b94-e927-3900-8e86-4292adfbffd3 | -4.108 | -48.462399 | 2024-10-03 00:12:26 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b2f7909-d3cc-3dbd-b862-9af94aeacf68 | -4.0957 | -48.453098 | 2024-10-03 00:12:26 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b40fa54-4db3-325b-8eba-6b40ed488526 | -4.0982 | -48.4645 | 2024-10-03 00:12:26 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9313b3a0-b4e2-380a-9778-fbc04065b498 | -4.1007 | -48.475899 | 2024-10-03 00:12:26 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4aa5aff4-3853-36be-96e8-8fdfc685f288 | -4.0834 | -48.443802 | 2024-10-03 00:12:27 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa223226-2b50-3886-8980-d542b9cc5ada | -4.0859 | -48.4552 | 2024-10-03 00:12:27 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88871048-4113-3cb6-a2f8-6d8f61bd90ce | -4.0884 | -48.466599 | 2024-10-03 00:12:27 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0b2855d-87ee-349d-a852-dd336bf62bc8 | -4.0909 | -48.478001 | 2024-10-03 00:12:27 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d4afb88-4620-3f82-9657-d80c86d459d2 | -3.8048 | -47.7817 | 2024-10-03 00:12:29 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c008e6ee-8f7d-3534-a345-2a75f7599b64 | -3.807 | -47.791901 | 2024-10-03 00:12:29 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18e6776a-718d-3e65-a7a9-3a3ef2900276 | -3.795 | -47.783798 | 2024-10-03 00:12:29 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58cdc01c-cf3a-3f6b-ae73-3735ce44f89f | -3.7972 | -47.793999 | 2024-10-03 00:12:29 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0180df00-8130-38be-a0cd-a67d11632c04 | -3.6994 | -47.583099 | 2024-10-03 00:12:30 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3da8dd88-f3fb-37b5-a0a7-09fcb282cc6b | -3.7016 | -47.592999 | 2024-10-03 00:12:30 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b0f5439-4314-36e3-bfc1-07758ae43619 | -3.7038 | -47.602901 | 2024-10-03 00:12:30 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 589045c0-a5e4-3d7b-8f7c-129faa56610e | -3.4068 | -47.0485 | 2024-10-03 00:12:33 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48a7d4ca-951a-3e57-bd05-002df4e4e583 | -3.4088 | -47.057701 | 2024-10-03 00:12:33 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19418671-9a6e-3cf0-877b-45a77e75ecba | -3.9306 | -49.661098 | 2024-10-03 00:12:33 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34054214-c56c-3477-bfad-3d254ef34ae3 | -3.9208 | -49.6632 | 2024-10-03 00:12:34 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e182874-d6af-3eda-8f06-22d91b0e6330 | -3.4667 | -47.643902 | 2024-10-03 00:12:34 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb4db9a5-831a-304d-b683-62b2b51a0a76 | -4.0874 | -51.084099 | 2024-10-03 00:12:36 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01773990-9895-340e-91fd-d7d55fc2dc4d | -3.9508 | -50.9706 | 2024-10-03 00:12:38 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5916a56b-a579-3007-ae4b-4fb8cbf8a3cb | -3.9411 | -50.972698 | 2024-10-03 00:12:38 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 074fd187-ac6b-3304-b5d5-7212ef84e1bd | -3.9447 | -50.989498 | 2024-10-03 00:12:38 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd6c493a-c158-3259-8350-063eba6c329d | -3.2207 | -48.8969 | 2024-10-03 00:12:42 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3512d1a-b26a-3177-bbf7-d71121a551f1 | -3.2234 | -48.908699 | 2024-10-03 00:12:42 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 286a4978-2459-3a20-9c15-cf147d366abe | -3.226 | -48.920502 | 2024-10-03 00:12:42 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbb1a667-5204-354b-bcfd-84d5952c5b6e | -3.8724 | -52.061298 | 2024-10-03 00:12:43 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b026f411-e0b1-33bf-8f93-83e38e03cf79 | -3.1283 | -48.9417 | 2024-10-03 00:12:44 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 933a257d-8d30-3abe-8a6d-2f8478557eea | -2.3556 | -45.6534 | 2024-10-03 00:12:45 | METOP-B | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 35e06580-cbac-396f-bd5d-e0b19c042c1e | -2.3573 | -45.660999 | 2024-10-03 00:12:45 | METOP-B | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2774aeca-293d-35d9-96b5-d9dce824d83e | -2.359 | -45.668598 | 2024-10-03 00:12:45 | METOP-B | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3da4a9db-699b-3ded-9828-3277f68bc88e | -3.1352 | -49.390499 | 2024-10-03 00:12:45 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d442e20-4f10-3366-8af7-93e28bc0c2a7 | -3.138 | -49.403301 | 2024-10-03 00:12:45 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22ac653a-3cea-3ed8-a649-5e4f0aa53d84 | -3.2535 | -50.113499 | 2024-10-03 00:12:46 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8103756-1e60-3bee-9c73-66b84455f93c | -3.2438 | -50.115601 | 2024-10-03 00:12:46 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ffa7ebf-6fac-3758-892f-02ee3d42a757 | -2.5289 | -47.211201 | 2024-10-03 00:12:47 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c9e5bdf-e9f1-3331-9e30-bda331fdd0f6 | -2.5309 | -47.220299 | 2024-10-03 00:12:47 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e3425d1-38de-39f6-9bed-9b9f256424ae | -2.9497 | -49.3381 | 2024-10-03 00:12:48 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 654b94c6-8f38-3fe3-a64b-28f4ea7c2beb | -2.9595 | -49.335899 | 2024-10-03 00:12:48 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3b4c064-01eb-3d9c-848d-727c7f531017 | -2.9525 | -49.350601 | 2024-10-03 00:12:48 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf55ebe5-3b4a-3145-a345-18370b6154ff | -2.3548 | -45.558102 | 2024-10-03 00:12:52 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 171da2cd-267d-3bf0-a77b-bec66434e9b1 | -2.3565 | -45.565601 | 2024-10-03 00:12:52 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 882b5dfe-3faa-3be4-80f8-0249715f6a84 | -3.6634 | -54.320499 | 2024-10-03 00:12:54 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1057c1f-c539-3a7f-ae64-79dbc0c329f6 | -3.6538 | -54.322498 | 2024-10-03 00:12:55 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12825f8d-1dfe-326c-ac32-729273391239 | -2.5386 | -47.209 | 2024-10-03 00:12:55 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adb3d072-5a6e-3057-879c-d964fe3d8a6a | -2.5407 | -47.218102 | 2024-10-03 00:12:55 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 796e4b4c-36fa-3fab-8601-7c48588402a3 | -3.3653 | -54.063202 | 2024-10-03 00:12:58 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c625fe5-6983-36cc-bf0a-099313e64e6c | -1.9037 | -47.860699 | 2024-10-03 00:13:00 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64148700-a274-35e9-8214-fe041ef2b46f | -1.9059 | -47.870399 | 2024-10-03 00:13:00 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e2bfc6d-0da9-39ee-9bd8-7948f7d4908d | -1.9081 | -47.880199 | 2024-10-03 00:13:00 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 968d037a-1c02-32d9-a274-b3abab3b1c44 | -0.9862 | -46.7948 | 2024-10-03 00:13:19 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bf306d5-6a6f-33c5-ba09-70502ba82a6a | -1.747 | -54.382401 | 2024-10-03 00:13:34 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84711191-7fd2-313a-aeaf-9d08af5f0951 | -1.753 | -54.409302 | 2024-10-03 00:13:34 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1399feef-291d-3dd1-b2b9-336c1000a6a3 | -1.7373 | -54.384499 | 2024-10-03 00:13:34 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23e76264-2a9c-3c9e-b13b-21cb0a460ef0 | -1.7433 | -54.4114 | 2024-10-03 00:13:34 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c10bb2fd-2e5b-3115-abb9-11d049d8002d | -1.1351 | -53.598701 | 2024-10-03 00:13:41 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2be88516-cdc9-3902-99c5-936c3af37f7b | -1.1254 | -53.6008 | 2024-10-03 00:13:41 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1061b98-a0ef-34f8-8fcb-2a4c099ef4b0 | -1.0362 | -53.475899 | 2024-10-03 00:13:42 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f531336-6b7c-38bd-a7f0-b2b359c6017d | -1.0414 | -53.498699 | 2024-10-03 00:13:42 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 560e8d73-ee19-347d-bd8c-d8d7c9b31240 | -1.7509 | -54.4531 | 2024-10-03 00:15:16 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| a7a720bf-ff06-3017-912a-2cfa9bb2b173 | -2.9489 | -52.9174 | 2024-10-03 00:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| bd96ee6f-3d41-31c8-a8cd-69a111201e6c | -3.4042 | -42.2621 | 2024-10-03 00:15:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 233.3 |
| 6e715c73-bc3b-342d-bd95-2fe02b3bbe52 | -3.3854 | -42.2866 | 2024-10-03 00:15:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 148.0 |
| f03c2b4c-aea9-3fee-9fba-b82fcae2c215 | -3.3855 | -42.263 | 2024-10-03 00:15:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| a61362a0-8912-33d3-953a-b3a8b44242aa | -3.404 | -42.2858 | 2024-10-03 00:15:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 434.1 |
| 66466833-b0ec-3f5c-ac7f-cdb2677d5c4b | -3.802 | -47.8104 | 2024-10-03 00:15:27 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 37d8b946-1155-36c0-b024-317440c6dccc | -4.0949 | -48.4894 | 2024-10-03 00:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 90672d19-404a-346c-b018-6e20c6a69e55 | -4.095 | -48.4679 | 2024-10-03 00:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 54c82b7f-679d-3825-969f-45e5def67c01 | -4.1134 | -48.4886 | 2024-10-03 00:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 153f76e9-be1c-3433-ae82-bbf8321a4e92 | -4.4658 | -42.8643 | 2024-10-03 00:15:31 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 1dbc41f8-34f9-308a-b314-628b8f874f6d | -4.4657 | -42.8877 | 2024-10-03 00:15:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 173.3 |
| 4c2a059f-aefb-32f4-869f-dd20586ba1b5 | -4.4844 | -42.8866 | 2024-10-03 00:15:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| e88d02e8-be07-3de9-8c47-aa5e6188eefe | -4.5375 | -43.304 | 2024-10-03 00:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 6225e1b7-4808-3bb9-97b1-6f427ab5fbbe | -4.5562 | -43.3028 | 2024-10-03 00:15:32 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 378057ea-c59f-3dd1-9f5a-a16fed33c6a9 | -4.58 | -48.0132 | 2024-10-03 00:15:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| f7e42990-a966-32a3-b042-4335c61dd942 | -4.8398 | -42.8875 | 2024-10-03 00:15:33 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| dd3af8ca-a643-34ae-84ad-f093d4333e70 | -4.84 | -42.864 | 2024-10-03 00:15:33 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| cdcb6a30-0e18-3976-92ca-84de1df8f228 | -4.9264 | -43.79 | 2024-10-03 00:15:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 3b8724c5-b271-3d9b-a0ef-7fa31019c8de | -4.9265 | -43.7669 | 2024-10-03 00:15:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 120.3 |


[Clique aqui para ver as próximas entradas](README11.md)
