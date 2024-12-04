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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab034618-ff46-3401-bce9-3806b49cf73f | -0.85233 | -52.70859 | 2024-12-04 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e84d1175-bd7d-3435-a297-6171209fac4a | -1.89796 | -52.84916 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68575dc1-c333-3214-bc81-e322e6af0c85 | -2.79978 | -53.05618 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2147df70-4019-36c7-8a7f-67eb08641ee1 | -3.26944 | -53.65398 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7623e77f-0683-3b08-86eb-4801a07524e4 | -2.98585 | -53.88086 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf4dad2f-75e5-3987-a31f-36e560ba0248 | -2.20172 | -47.25132 | 2024-12-04 05:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 044beae4-d38c-3559-9bf5-aa93e5b6f56e | -3.12135 | -54.61939 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 20071f15-775a-3292-85a1-9c8c47259eee | -2.69319 | -51.86406 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54ad9080-29da-3d7a-9526-3d98d2a3686a | 0.70339 | -59.87603 | 2024-12-04 05:29:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47f82c29-72b4-3735-83dc-7cfa0401b03e | -2.80704 | -53.0424 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1037c164-49c2-32fd-8bba-74e9fd2fcca7 | -3.25804 | -53.66331 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5190b00c-3ad8-3bfc-8777-65986cd1e2f8 | -1.73946 | -52.60943 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| cb908e4b-edf5-3a5b-894b-fd6477df3689 | -1.38663 | -53.55878 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4c433d5-ee5a-3f2a-ad07-46e131c1623d | -2.81254 | -53.04027 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 835e86ef-0281-3cf7-b7df-49cd7c8a1836 | -3.19585 | -51.17513 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0640869a-4819-36a3-b775-42868b3aeef2 | -1.7085 | -52.78077 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0e291f5-48f0-350b-8682-1d426c0e328f | -1.4631 | -54.96191 | 2024-12-04 05:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03bbd1c9-b63d-3c1b-8ad6-a6de4c10146d | -2.63344 | -48.05857 | 2024-12-04 05:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49b8f67f-f9b2-3e02-8cb6-3b53fd864b10 | -1.49077 | -54.43709 | 2024-12-04 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2fd5e68-898c-35f4-9af0-496c29d41308 | -2.00283 | -54.11824 | 2024-12-04 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1ba44b2-3173-3663-b7c1-7a3371f1a1a5 | -1.07345 | -62.64547 | 2024-12-04 05:29:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c6f046e-fd84-3fd5-8bf7-6bdb3eb9f353 | -2.55332 | -53.40805 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc1f6926-f56e-3ed0-8c55-a4b00299720d | 1.09006 | -59.6454 | 2024-12-04 05:29:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86736f1e-80e4-3d5a-96b4-84d0957cbb27 | -3.28931 | -53.70729 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eb61851b-d9a1-337b-b6d1-1b0a5d25ce92 | 1.05083 | -59.52637 | 2024-12-04 05:29:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4586877-88f9-39e9-bb00-0d48b7ce2eef | -3.26124 | -53.83644 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d25927a7-022a-39b8-ab2e-74c0a63bd264 | -2.88205 | -54.12222 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 612b0725-f238-31aa-b0da-bbf7a044167e | -1.65059 | -52.37902 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 888b5951-9336-3091-a8fe-b309c6089e48 | -3.05575 | -54.49631 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f63f75f-e91c-3033-88d2-4d844fe1375d | -2.81491 | -53.05853 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1168757-e57f-3f2a-bf1d-ee533876c5c0 | -3.37841 | -51.09972 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c87f510-a16e-38bf-9fd9-d03b9c5da3ed | -2.88335 | -51.79688 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6ea9a3e-ad70-3eb9-973c-4cb90be579d3 | -3.37214 | -51.06122 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5a8330e-c132-3544-a126-182d1ff7ae2e | -3.44819 | -54.08414 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a186f15-9fd0-3204-bb9e-8e2bef322b19 | -3.18377 | -54.51762 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4ce8c73-2860-3c12-823b-5f97de35663d | -2.0217 | -53.30132 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3666b08d-744e-3abd-9eac-15bb53d4ee54 | -3.10486 | -54.0612 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33bf587c-a651-34e7-a015-9585036cf54b | -1.03617 | -53.55221 | 2024-12-04 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c43f3f32-886a-367e-b6d9-0c8dd01e234b | -3.85705 | -52.15937 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e676f78-396d-33a4-b072-d7ff3ad630a4 | -1.65529 | -52.38293 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a4aee49e-b102-339e-b490-d6cf61c8ba96 | -1.87345 | -60.31958 | 2024-12-04 05:29:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47fb30be-10d0-38d4-ac92-c38a22d8f41b | -2.80087 | -54.14325 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52372772-3baf-38a6-9b27-096e671c376a | -2.80987 | -53.05775 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99d68970-c5ab-3b89-902d-85358b4749a5 | -2.99457 | -54.12072 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d81c8b66-f90e-3ad0-94cc-7907f1edd379 | -5.37434 | -60.09759 | 2024-12-04 05:29:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3fc4131-6469-37ab-ac0b-bac707377619 | -1.45877 | -54.96127 | 2024-12-04 05:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11d6debe-9acd-3e6d-946a-7ad29a415d4d | -2.99239 | -54.12373 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 715313b9-c848-33f8-a7d6-e636ac2c9d96 | -3.60805 | -50.7984 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c034058-1ecb-34f6-92ef-6a88d6d9faae | -3.37737 | -51.06618 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6709d7c-7593-3fe3-8e2b-01f77a85c139 | -2.78156 | -52.866 | 2024-12-04 05:29:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 77dd181e-4d9d-3f7d-a2fd-53018e9d5907 | -2.80749 | -53.03947 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1ea17e5-0be4-39a3-aa4d-8f20c46837cf | -2.02121 | -59.77903 | 2024-12-04 05:29:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ecf04a6-5543-3af7-a07c-2b6ca95a6590 | -4.18961 | -50.67976 | 2024-12-04 05:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c82d1f14-3917-376a-8ddc-c29b25ed13c4 | -3.11611 | -54.62317 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 12f2aeb1-235b-3df6-b8bb-be9573b389df | -3.12827 | -54.60836 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3bd48b1a-1605-3cf4-9610-e30162c00524 | -2.97729 | -53.9052 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 660b8508-0874-3725-8997-d94dda5f2cb5 | -2.55699 | -53.40777 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a7e8e3b-5df2-37c1-aa27-d08176e00082 | -3.31998 | -50.34582 | 2024-12-04 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6116d6bc-44e4-350c-a6a0-f6cb5d89d903 | -2.62651 | -48.05751 | 2024-12-04 05:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79de6922-6f99-396e-a93a-7ce5e74de35e | -2.89453 | -54.15753 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91166c78-377a-346d-80ed-f4f2bcb707c3 | -3.33933 | -51.20545 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bc77976-724a-3c89-97bc-0eecb3822e1d | -3.10569 | -54.05901 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 934c0e4c-7732-3558-98b6-3e2f411e1cf2 | -3.1071 | -53.7573 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9eb30fda-348d-3180-aac4-f1a52c5657d3 | -1.65481 | -52.38603 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7079608e-7a28-32c2-bece-5e2767e4c437 | -3.07177 | -54.05605 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6337a6fc-b140-3e9c-a459-b1f6a148d6be | -2.80482 | -53.05697 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da32e69a-8207-39c0-a57e-224cfee844ee | -1.49344 | -52.5274 | 2024-12-04 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6c97184-3a27-3fc5-8292-b7b84f810b35 | -5.37092 | -60.09706 | 2024-12-04 05:29:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60caa4b9-f926-372a-b211-62a696e4ad54 | -1.65741 | -52.75122 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0aaf0a58-fe73-33d6-a157-a6881dc0dd35 | -3.29895 | -53.67558 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d7ccb9ec-6a67-354f-9fa5-00688aeeabe0 | -2.8167 | -53.04687 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 193777e5-fceb-35e1-a5e4-26ecad63a423 | -3.83678 | -52.33645 | 2024-12-04 05:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b022b3a5-6a0d-360a-9b4e-62c4e2bfd8e3 | -2.82501 | -53.06007 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ea694160-9b24-3a41-8c39-4e9e829a1bb4 | -1.76279 | -52.62839 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f170caaf-e4ea-311e-bc36-cbe4abf6582d | -1.66709 | -52.75571 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 68bd4773-b1a4-3d03-ae17-decaa8cc795a | -1.0354 | -53.55732 | 2024-12-04 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ceb20ed7-29d5-3c27-8f90-a8f24d1ad73a | -2.44541 | -54.03511 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcc984bd-9cb2-3912-8513-c65add301983 | -3.20229 | -50.64324 | 2024-12-04 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8dc8e971-2a11-3016-bc5c-13671107822b | -1.44741 | -60.07809 | 2024-12-04 05:29:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cff042b-a814-33b7-ab9a-8de2782daff0 | -1.73901 | -52.61245 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2898f071-4d69-3c50-93d2-94801ea4bcc3 | -3.26461 | -53.62014 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6d984f09-673d-3845-bebf-6d7a1238dd87 | -1.65383 | -52.39223 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eaf55f24-e326-3f84-a07d-45c3a9cb22ca | -3.19507 | -50.65097 | 2024-12-04 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 793cbac6-9928-3419-8dd0-1eef4269c717 | -1.75722 | -52.63062 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 58a5857d-1b21-38b8-b6cd-333a0f086de1 | -1.33281 | -55.01902 | 2024-12-04 05:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72a5102b-0891-3093-a29b-e5fc4a27cea2 | -2.52274 | -51.80676 | 2024-12-04 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa1379f7-f6bc-3914-8740-9b17df69e607 | -3.20546 | -50.64881 | 2024-12-04 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 830f20af-fb10-3c5b-9146-76c2da6dbe15 | -2.64429 | -54.29239 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50fa909c-b856-3d6b-b64c-0ad37cc3d5bf | -2.55123 | -53.41251 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d20b1e4f-18b0-3169-92c6-8f9f2ad50246 | -1.69009 | -52.33078 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cbb3a9b-ae86-33fb-809f-58161b7bade9 | -2.58326 | -53.67453 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb247610-dfa3-32ce-9d60-118bd197b243 | -2.90823 | -51.81845 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21b56d66-d6af-3c5f-8f45-f33de0d6b902 | -1.65696 | -52.75415 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a6e18e8-9d6c-3e1f-acd3-b7b8c85f1fa2 | -3.1269 | -54.6263 | 2024-12-04 05:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 268.7 |
| 01bd24c5-636c-3873-85f9-23bc144bba86 | -3.1269 | -54.6463 | 2024-12-04 05:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| dac51c52-11bf-341d-86fc-db55f5f7e49b | -3.259 | -53.659 | 2024-12-04 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 87ba573f-41a6-37ab-bd30-9cd74c5b2a47 | -1.7728 | -52.636 | 2024-12-04 05:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 74fd530c-bc9b-30bd-9cd2-12c8ae58e898 | -3.1453 | -54.6259 | 2024-12-04 05:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 7e4349de-a17c-37b6-bac8-ae1dc77b6947 | -3.1086 | -54.6268 | 2024-12-04 05:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 108.4 |
| a10ad2ea-c941-313c-87b3-cce5ec74419e | -1.7361 | -52.6162 | 2024-12-04 05:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |


[Clique aqui para ver as próximas entradas](README58.md)
