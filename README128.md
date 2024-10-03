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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21460e4e-a8a2-3bfe-953e-c5a4fdd59959 | -9.29775 | -51.07374 | 2024-10-03 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16a176af-9ff3-3b4c-9b91-2e9cc31ebee2 | -9.296 | -51.06176 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3c721eab-0741-3bc2-9cca-d44410ccd37e | -9.29254 | -51.06121 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dbe1a693-f520-354b-bd90-160d3cacb6e5 | -9.2914 | -51.06886 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e9d8cca-2a40-31c8-8247-e8ae262533c2 | -9.11609 | -51.51813 | 2024-10-03 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23d1a7a9-9286-385b-8f7e-8cbc89c6597a | -9.11553 | -51.52185 | 2024-10-03 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8283bf7-6f23-3ac2-8034-8861bf032897 | -9.11212 | -51.52134 | 2024-10-03 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6ee7717-d354-3129-82f4-ae11aa6509f2 | -9.11156 | -51.52504 | 2024-10-03 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e6ee7b4-bc13-39f9-9c12-f4872cacc812 | -9.10872 | -51.52078 | 2024-10-03 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc9a48ae-3d9b-3bed-9547-207b698c8f9b | -9.10816 | -51.52449 | 2024-10-03 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44b50685-2f3f-3c71-9852-b567e139ebd2 | -9.10799 | -51.52444 | 2024-10-03 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5041cad1-01b0-31ec-acc1-f1ba9e45aade | -9.1069 | -51.48631 | 2024-10-03 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15705bd9-b4f9-3c78-a097-7d51e730a61c | -9.10291 | -51.48951 | 2024-10-03 04:51:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f26a116-1838-3d88-a92b-f0368a717087 | -8.18287 | -50.49014 | 2024-10-03 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5dec676f-7d44-3283-8915-c0247333b1d2 | -8.17996 | -50.48568 | 2024-10-03 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f582aff3-f7c6-35b5-9974-654e156410a4 | -8.17936 | -50.4896 | 2024-10-03 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9fad0ee3-dfb1-3084-9888-d928547f42e7 | -10.63437 | -51.11056 | 2024-10-03 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c19d6d18-7916-3db7-89b3-e769f879e38c | -10.63379 | -51.11448 | 2024-10-03 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 26e0271e-3112-3c29-96fc-850329836dd5 | -10.63088 | -51.11002 | 2024-10-03 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6372fb3-109e-3c9e-b5e5-43e8fff382d1 | -10.52076 | -51.07792 | 2024-10-03 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 568fa2e8-f0a4-3efe-a74a-551480edd647 | -10.51726 | -51.07737 | 2024-10-03 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b782d07f-3f0c-3ef8-a8b1-9d19621b10d1 | -10.5056 | -51.1076 | 2024-10-03 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2dae89c5-fabb-3b08-8198-9c6efd2da024 | -10.50501 | -51.11154 | 2024-10-03 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0f70706-b175-3812-b973-440b1e5c4eaf | -10.50093 | -51.11492 | 2024-10-03 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e03284d-78d0-32bc-aab0-a744be6da8c9 | -10.50033 | -51.11892 | 2024-10-03 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 31b2d747-e4ee-31e1-9553-7dc54f09de09 | -10.49686 | -51.11822 | 2024-10-03 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa6cd101-c602-30f0-99fe-9f01ef852062 | -10.4928 | -51.12151 | 2024-10-03 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fed250ee-2c46-3988-86e9-a325ec8f65a3 | -10.48931 | -51.12094 | 2024-10-03 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8cb7ab6-3de9-3f4e-aa90-f5089fe82569 | -10.44783 | -50.76781 | 2024-10-03 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 36ba8920-acea-31c4-86ed-9fe33fdac78f | -10.43777 | -50.81134 | 2024-10-03 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c91ace54-68e8-3697-b0ba-ddf332eaff7a | -10.43717 | -50.81535 | 2024-10-03 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2282e051-2c4c-3180-9fa6-4313e315703b | -10.43423 | -50.81081 | 2024-10-03 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aaaea36d-5397-3fb8-8261-7a8f3354a7b2 | -10.43307 | -50.79417 | 2024-10-03 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3a6fc2d-2ba2-3085-82b8-9141039f47cc | -10.43247 | -50.79823 | 2024-10-03 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a2a1ccf-7974-3d1d-84d7-ea102b60cfaa | -10.43186 | -50.80232 | 2024-10-03 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 00c7a10b-205a-3cd1-ac39-440a1a15d937 | -10.43127 | -50.80634 | 2024-10-03 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f532e0d0-2195-3ac9-b508-9a0d682a98e7 | -10.43069 | -50.81029 | 2024-10-03 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5474f9d3-2177-3556-bfef-bcac07205c11 | -10.42773 | -50.80584 | 2024-10-03 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e8cb62f1-51c2-3adb-a947-60adf07b3508 | -9.74545 | -50.65708 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1480ea1b-e95b-3329-9818-63a70c194c6a | -9.73305 | -50.66743 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f41c551c-239a-3cd3-84b6-5ff67cedae9e | -9.73245 | -50.67139 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f66c36b4-08d0-3b5c-b163-69106c13fe5c | -9.72951 | -50.6669 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bd5b473-5c52-3b16-9b8c-1fe6881c5c8f | -9.72892 | -50.67086 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d87c12a-3850-349d-a2d9-5ec4db64c0e1 | -11.96909 | -51.8996 | 2024-10-03 04:51:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03752a79-f575-324c-9df0-972f6ede1c22 | -11.96788 | -51.8993 | 2024-10-03 04:51:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f62b85c-3ea4-342d-a6c9-6e801da91c88 | -11.96565 | -51.89908 | 2024-10-03 04:51:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e7fd29e-72f1-344d-968f-aa712a91a099 | -11.95707 | -51.88611 | 2024-10-03 04:51:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 769bb16c-8294-3fdf-8479-021f1862b16e | -11.2292 | -51.1512 | 2024-10-03 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01a9990c-e4d4-3b67-a7e7-c8061748c5f3 | -11.22627 | -51.14669 | 2024-10-03 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 172d27d6-e324-39df-b1f1-bf81f25910b0 | -11.07997 | -51.45617 | 2024-10-03 04:51:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77111067-1bc8-3783-8f62-ff66c053f8e9 | -13.15191 | -51.21418 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8571bda-e22e-3c3a-b0ac-eafaa46b1c79 | -13.14666 | -51.21183 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f24b127f-31c1-3566-aaee-a307f7003926 | -13.14538 | -51.20897 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a401207a-d20f-38da-8fb2-0b32733a7925 | -13.13589 | -51.19909 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 250a5a58-b43e-33b2-98fe-715f10854ada | -13.13088 | -51.42221 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9188a1a4-320c-3e73-aa2d-1f3181a54638 | -12.91056 | -51.28835 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c7a1a29-f6d4-33c8-be8e-93198bcd8105 | -12.90099 | -51.32837 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2e129129-255e-3a68-9953-9b0b96cbad51 | -12.8951 | -51.3192 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6976068d-2be1-38af-99fa-07de8e3a12b2 | -12.73247 | -51.93473 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d29825d-2c6a-384b-8b75-6545ac9fab9c | -12.73081 | -51.96976 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28fdd7df-da07-3e1c-af9e-99980b18d048 | -12.73025 | -51.97358 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e9f77e6-cbfd-3214-87cb-458a03cf18ae | -12.72958 | -51.93034 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d77fd7c-0f06-3379-84b2-3117ce449abe | -12.7267 | -51.92595 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8390dbc3-a5f7-3e19-82ca-9bbd4cea9d34 | -12.72571 | -52.00415 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 27b8be5f-b06d-399b-9bfe-89f28d4e02b9 | -12.7251 | -51.98452 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 184ddd7c-44a5-3aee-8ae4-f60002c24984 | -12.72453 | -51.98836 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0af314c-4415-3d21-bdcd-78292ffb79b2 | -12.72396 | -51.99218 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aea29a01-b6bd-31ca-a6ce-a3b91aba6af6 | -12.7234 | -51.99599 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c388c000-3694-3d88-a100-6f96cb32b53a | -12.72165 | -51.98397 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b34d1038-a2cf-3e88-b4f2-6fe7908afd2d | -13.25973 | -51.22753 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c4f8dc28-b8bd-3b76-8f59-54db98fdf846 | -13.25855 | -51.23579 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b152493c-eb65-3005-ab51-b87e1c2fc97b | -13.25801 | -51.22454 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 13b367c4-aca0-3fc6-894f-3ac05c1f1363 | -13.25679 | -51.23278 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 597788c7-8f00-3ebf-8f0a-97e334356759 | -13.25618 | -51.23691 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5d8cdfe5-4885-3ba8-995c-b55270d265ef | -13.25616 | -51.22698 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 04fb25d7-accb-3862-911f-5a2090d53677 | -13.25498 | -51.23524 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f071a10b-cbc5-3372-93d6-aff0a815e36b | -13.19072 | -51.2101 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac2ed7a8-3aef-3221-bf45-9720ae22e03e | -13.18833 | -51.2266 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6e4e5a4-5717-376e-bbe6-b1e6b5366814 | -13.80776 | -52.43819 | 2024-10-03 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7a81729d-edef-34ec-9cf4-e426b3b0824c | -7.90749 | -52.37082 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35d203f0-9922-3bad-bd8f-2b581554c6c6 | -7.9047 | -52.36683 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11f95ba3-088c-30ed-9227-c8e018e19b32 | -9.37012 | -52.51367 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc1dead1-4ab0-375a-b49c-b3d9523d7245 | -9.06697 | -53.25919 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee837637-f724-3dd1-9853-eaba8a7392dd | -9.06309 | -53.26215 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3678cac-38fe-3763-a19c-4fae89c95a90 | -8.97069 | -52.81788 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 762b7a96-73ee-3dbd-9f00-5d04ad467606 | -8.96846 | -52.81037 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c89c773f-04f4-3bbe-a01d-b00cf1593898 | -8.96791 | -52.81387 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2547e7cd-f761-3921-9152-a249fa56edac | -8.96736 | -52.81736 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88ee8a8e-5ae3-3a19-bbf8-ca9bf100d453 | -8.96682 | -52.82085 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b861516-8002-3744-b068-7e3c52b51bed | -8.96513 | -52.80984 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13dfca63-1b69-34a0-8157-2e2a0586528f | -8.96294 | -52.82382 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| befbf969-4670-38d6-8dca-01664b7a49c1 | -8.9629 | -52.80233 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c3caa03-c172-3afd-b5f4-eb0395251baf | -8.96235 | -52.80583 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1ee0013-9749-33a7-9f5b-6bee16a9c5f6 | -8.9618 | -52.80933 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b56aa80-8e91-35d2-8218-3afb48c873ca | -8.96012 | -52.79832 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d9794b8-5d53-366a-983d-68a9c7a15870 | -8.95962 | -52.82329 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7a45b35-1977-35d6-afff-987c844b6888 | -8.95957 | -52.80181 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fb437c7-8b12-3aee-8a49-56ed8c61e896 | -8.95902 | -52.8053 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f99adc4-a8d8-3d0e-837b-2e6f650fca78 | -8.95848 | -52.8088 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3290be69-d4f0-37a1-acde-3fe125498f72 | -8.95679 | -52.79779 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README129.md)
