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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f68ae1b1-eaa4-347f-b69c-e23f3010b851 | -3.52826 | -54.68163 | 2024-11-20 04:50:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18617fa8-b0ce-3eb6-b401-c59c05127351 | -3.14056 | -49.12702 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 22f3a324-6827-3a89-ab63-04379cbb98ba | -1.14333 | -51.69303 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75b1fa84-f977-3edb-be1f-84a14fb45445 | -2.45051 | -53.6851 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3921ec36-c536-3828-9d75-22aff7bdd47c | -2.92621 | -48.32907 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ef9df598-9f5f-3114-8b39-26025cd792c9 | -0.95594 | -51.72362 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ed74de4-2c4a-3e39-bb56-21af33d6c39a | -4.36725 | -50.72726 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 993ed993-6879-361c-843e-929e15e13a6a | -2.60387 | -51.791 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69c5fc58-3c3c-3fdd-bf52-6dad071e0964 | -2.69462 | -51.87919 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7bd9e933-86e4-3af5-8942-77d41d3ecfaf | -2.13234 | -48.30455 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c40f52bc-a50c-3c95-934b-dc19909c9534 | -5.96574 | -48.06554 | 2024-11-20 04:50:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ef5d9ff5-0eb0-3a87-b779-969420e91416 | -3.80206 | -52.21912 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7eb953f3-2557-3472-ba7c-4225d79d7b71 | -3.51711 | -50.22262 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 657c9bfa-fcc1-39d4-9983-b694307fe858 | -1.29729 | -52.24026 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fe5b707-2a26-328d-b507-1327f5a58ee5 | -2.1531 | -50.7004 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc6be42d-5715-3553-a525-f254e7c2640d | -4.06765 | -46.84463 | 2024-11-20 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44d3dc47-d1e1-3b5d-bdef-047082ab8f61 | -2.11254 | -51.10321 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bab666f0-ebf7-3b39-b1bd-7914ab21730a | -3.51175 | -53.80099 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d6493363-2c0d-3f6c-9f48-f85304593665 | -3.02828 | -51.52214 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 11661e02-7414-3b8a-bda3-72d82dcd6ff0 | -2.61938 | -51.80048 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f64153b0-e1c3-3e42-861e-a170f66ba962 | -3.87045 | -47.07849 | 2024-11-20 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b50c0146-a177-300e-831b-d2641e56df57 | -1.50234 | -52.18297 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 700157a3-cfcf-37d7-ab27-a134ae6d5c80 | -1.12477 | -54.19338 | 2024-11-20 04:50:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ce8541c-b093-37b4-ad77-de9a67c79497 | -2.91331 | -53.06154 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9a3466ca-3e83-312d-8817-842385ba90f0 | -3.71569 | -51.84133 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dca015de-750d-34e4-9d84-b11bfcbd1ead | -1.14204 | -53.6701 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 860dc856-8339-33af-97e5-c8ced84e8a12 | -1.33239 | -52.23495 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dacb688-de24-3e66-a468-58f1e0cdfc20 | -2.29154 | -46.37396 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e305c532-6130-3037-8860-78dbec3d65bf | -1.6365 | -52.62952 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 716c72a5-6cfd-357d-8c45-776f4979ec8a | -3.97548 | -49.94935 | 2024-11-20 04:50:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f039ef56-76d7-3178-969f-f556322d481c | -5.41904 | -44.70522 | 2024-11-20 04:50:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22436cb4-82db-3d8a-88ba-d43f72840006 | -2.35272 | -48.60958 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f008dce6-42b4-34ab-abc1-6af8aebd3715 | -2.13798 | -50.64439 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7857fe04-4024-3214-a151-20301dc31f00 | -3.51598 | -50.22985 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed07ab80-5a0d-3983-8cdd-473e3da902b4 | -1.62188 | -52.59084 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c0619e8d-98af-3f54-8694-0acfdb29a7b4 | -2.79066 | -54.0337 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 80f35f88-e6d1-3500-8326-3f86f96c2dbb | -2.14411 | -50.64892 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5cd7bf3-5a0c-31ab-a3d1-2cfedd92be02 | -3.23275 | -48.87914 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73d64e26-e23a-3894-8016-9885c8ccb692 | -2.26609 | -50.58204 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 744c3ea6-b978-3925-b032-1f8d36b2dbf7 | -2.90768 | -53.05335 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 52c4ae07-baec-310d-84c2-e904c042a078 | -2.26528 | -48.40874 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 928dde94-dc3b-3b20-8292-1161655b8e95 | -1.3429 | -51.39576 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7439955-e546-3226-acaa-d277ee947afd | -3.06672 | -53.28436 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e42a52cb-f790-34a2-ae80-d00dcc4f2e63 | -2.63142 | -49.17999 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd7a674a-3d7c-3bff-8d43-669459b8c4de | -2.68849 | -48.51487 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3afb59c-ec49-3f34-9650-2f5e0c3a09a6 | -3.18594 | -48.57537 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05e3ac1e-d409-3b2a-b61a-45433001c2d9 | -1.64428 | -52.67414 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae58b890-e3eb-30b1-be82-f452c8765128 | -0.91618 | -51.78126 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e2ab0172-bd3b-3b77-b9e0-8551a2d2c6ad | -2.06722 | -51.45638 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0315e25-babe-3bf5-9e26-c5c2d08ab422 | -5.44337 | -45.58549 | 2024-11-20 04:50:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58197e5d-7227-35d1-943d-8976ee3f030b | -3.78025 | -53.96203 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8a0c501-d53e-362b-90f8-9dad1da2e850 | -2.25344 | -53.67498 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2d27d6d-243f-3e1b-a565-b9943bcb1608 | -1.69049 | -50.20052 | 2024-11-20 04:50:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 236b2472-249d-3395-9fd5-8e1d9de7a768 | -3.84804 | -50.69909 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 074f88d5-064a-3960-ad84-06e9bc5a98a8 | -3.79274 | -51.37201 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dabc6cc1-6c17-30fe-ae98-4bf8de5ee384 | -5.06673 | -44.22784 | 2024-11-20 04:50:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bb8fffa-52b0-38f6-a696-2f77361108cd | -2.56897 | -53.99985 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9028d45f-9127-378c-bc4c-c58ccf0edb23 | -1.14909 | -53.51105 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f271d76-05d4-327c-932d-f1ec53392c67 | -3.00305 | -45.44184 | 2024-11-20 04:50:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e3afde9c-78b8-329a-b927-67f9c8277a82 | -4.33818 | -50.42118 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3a8f75a-f6c6-39b0-bcd5-d0403a6dee1f | -2.28351 | -48.48598 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f826ed31-cb3c-3a1e-938d-81aae4fcf0d9 | -3.14447 | -48.62849 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b05889c3-948a-39a4-acbd-36426b7b9272 | -3.19588 | -53.13454 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be533165-616a-3866-9c64-c441bb024af9 | -2.95295 | -53.71602 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e3b707f-f885-3a5a-8e08-2e8eea5cd30d | -2.03472 | -48.73277 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a06960ba-6798-3ee2-aaae-e1ea8d0f55ed | -3.76994 | -53.84924 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f303b36c-c02e-30b2-b988-54c9e0bdba95 | -0.91826 | -52.54021 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d437553e-34f0-32a3-8188-029a158a402d | -2.85261 | -51.58605 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ede231a6-1ef0-3247-8f76-398245d95123 | -1.45933 | -52.6933 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fcf333e-d409-3250-a7a5-e9774f10619d | -1.49178 | -51.13663 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c3efb62-06d8-3666-a71a-47ac638619d4 | -2.73997 | -51.82625 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 5b107152-e33d-3d51-88fb-617db3c66715 | -2.68866 | -46.07199 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30b83aae-9505-32e9-883f-5cfea5d51c14 | -4.06359 | -46.84401 | 2024-11-20 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e27fef7-7a30-342c-adef-5166c435faca | -2.96426 | -51.41261 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 29d3a899-3229-3828-97e2-7e52e9d455be | -1.68416 | -52.08638 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a72abda1-d731-3f13-8f41-4180f2059edc | -3.77142 | -52.00555 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14f36629-cec0-3413-990e-c69efeba30e6 | -2.70556 | -49.09592 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d37f9683-f1c9-32ce-9264-e9b8e99c84d9 | -1.23056 | -51.7845 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17e40df2-8956-32ff-8719-770acd9f4aab | -2.91836 | -53.07333 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 614f3496-4778-3dc1-aa48-cb3b89cd65a5 | -2.45908 | -53.69798 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6c90fdd9-4953-3c65-a569-d242722df515 | -0.80844 | -51.60875 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f16325bf-58f8-38b0-92c4-175ed4e87274 | -5.59575 | -46.17092 | 2024-11-20 04:50:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86413a2f-cb18-3d9b-a096-5ae3de7dc058 | -1.3445 | -52.54003 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 024f784c-da16-37eb-8d45-dc9eafe26a1c | -1.55479 | -51.23117 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 273b13ed-f421-3e1e-bf74-7b9f2112a449 | -3.48397 | -51.4443 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25862569-a6e6-3cab-b4a7-6c4cc33cbf0c | -2.74952 | -54.0668 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 504481c2-9668-38b0-9d5e-9dfa1006cbb5 | -2.0906 | -48.37999 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fbda70b-75c4-3054-b739-5e2439f34e08 | -1.65304 | -54.08733 | 2024-11-20 04:50:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a6b3cb1-5b1c-3db2-9761-bb0c902ec6c4 | -1.4376 | -53.38145 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d57ba17-ea8c-3fb5-9ef6-e6f82d29bf3a | -1.3341 | -51.40849 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75d604b3-7acf-308c-ae57-385cbad1e7ca | -4.0897 | -51.07581 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 324356d2-751b-3d95-8684-0ff8c120fae1 | -2.88948 | -48.27535 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c7f95ef6-1a42-34a4-a4eb-6adca55837e3 | -2.89315 | -48.27591 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| fd3dd830-fb21-3ff5-8e4a-8d6233808ea2 | -3.94443 | -47.00605 | 2024-11-20 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2077598a-a533-3335-ad0c-b0ec359f6115 | -2.74208 | -54.11335 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c246eeb-5c36-3f4f-aaac-e8c404db0bc3 | -3.55431 | -51.53353 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 418c84ef-881e-3806-8241-6d7f81d02212 | -1.51523 | -55.48613 | 2024-11-20 04:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7335ade1-d9d8-3297-91ce-68fe271f0971 | -2.14351 | -49.53819 | 2024-11-20 04:50:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0680be81-8b3b-3656-bc04-2ffaf0454947 | -1.21437 | -51.76072 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de5459f8-7e3c-3d3e-9cd6-3013304b2d8b | -3.88591 | -52.24327 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README56.md)
