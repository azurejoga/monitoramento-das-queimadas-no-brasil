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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3d2256e-fda1-3e01-a0e5-1c79e219adf7 | -3.4899 | -43.6383 | 2025-11-05 02:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| e3757d1e-48d6-38d8-b2dd-0750a54302a5 | -5.2452 | -48.5182 | 2025-11-05 02:20:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 56c9af80-4ff7-322c-9f82-5487e486f0ea | -4.482 | -43.2141 | 2025-11-05 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| da2cb8e4-6b2d-391b-a138-bf0715933553 | -1.2638 | -49.1469 | 2025-11-05 02:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 05940c10-c288-3a7f-82ee-87ec1954cd0f | -5.0399 | -43.6205 | 2025-11-05 02:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| aad4310d-68e1-3c08-9e9d-bd45bff3ecfd | -3.4899 | -43.6383 | 2025-11-05 02:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 27a46163-ee10-30d4-8888-1dad13526161 | -1.3006 | -49.1677 | 2025-11-05 02:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 581cdf8f-f249-3630-ae98-a14d1a479ea3 | -3.2317 | -46.8716 | 2025-11-05 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 1df277a4-2110-3a12-82cd-4bcdad5e6156 | -1.2822 | -49.1467 | 2025-11-05 02:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 6aa38f82-7b27-3f81-abba-caecafe2ebdc | -4.4632 | -43.2386 | 2025-11-05 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 175.6 |
| 7b586d76-d03b-3593-b62a-fbe823097afa | -4.4073 | -48.9474 | 2025-11-05 02:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 63fb90a3-3226-3445-820c-9ca049120c06 | -4.482 | -43.2141 | 2025-11-05 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| d94a762d-27f8-3182-a042-f3deb9d19c45 | -4.4633 | -43.2152 | 2025-11-05 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 224.6 |
| db2ff52d-166d-3dd5-8f02-27f625c3ad8b | -4.4819 | -43.2374 | 2025-11-05 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 7d6af628-b144-3f5a-8d27-af77edec5765 | -3.49 | -43.6152 | 2025-11-05 02:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 00b76516-7e99-3161-bde8-0e0b4dd2f654 | -4.4259 | -48.9465 | 2025-11-05 02:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 0271a380-c077-316d-9f1c-ac9dc29d8238 | -4.4446 | -43.2164 | 2025-11-05 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 3ee9b956-948e-33bc-9e01-cb62bf0ffbe6 | -5.2453 | -48.4966 | 2025-11-05 02:30:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 41d92cee-b3f6-3d78-9b97-f8e0c676bd78 | -5.2452 | -48.5182 | 2025-11-05 02:30:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 2f1641e0-8a22-3e9d-ac22-d942ff7ea4ce | -5.4553 | -45.3988 | 2025-11-05 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 126.6 |
| cc8c99bf-cece-39c0-98bd-14f17ee0428f | -5.2268 | -48.4976 | 2025-11-05 02:30:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 0ac12772-065e-341f-9f60-b2062e7a5ffc | -3.3135 | -53.839 | 2025-11-05 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 6acb7346-2fb2-37f8-8593-735b1840932a | -5.2268 | -48.4976 | 2025-11-05 02:40:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 67.9 |
| efe19e90-8257-3552-8aa0-da11f1f65104 | -5.0399 | -43.6205 | 2025-11-05 02:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 1870fdef-8eaf-34f2-9f56-bb2899558609 | -4.4633 | -43.2152 | 2025-11-05 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 212.9 |
| 87f95698-32d3-31cc-87e3-fd1dd18c4332 | -3.3135 | -53.839 | 2025-11-05 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| ebcaace1-b0de-3e81-a661-b802766da668 | -4.482 | -43.2141 | 2025-11-05 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 581f8598-206a-3bd8-8be9-5ebc1bc5813d | -18.5117 | -53.5071 | 2025-11-05 02:40:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 57fab756-e247-3083-9f09-0b919d45a957 | -4.4819 | -43.2374 | 2025-11-05 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| f247a630-1b72-36c6-9cd3-d4f01ff04656 | -5.2452 | -48.5182 | 2025-11-05 02:40:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 93.0 |
| e2d2fc11-3f2f-3cb9-b789-688148202d7a | -5.2266 | -48.5192 | 2025-11-05 02:40:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 54.4 |
| d9d51fc2-455a-3493-bde3-724f35464ba1 | -3.4899 | -43.6383 | 2025-11-05 02:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| b78501a7-2474-356b-91d4-569b635c263d | -3.49 | -43.6152 | 2025-11-05 02:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 6145a6eb-d9f0-30ee-a396-7bc4c1e93114 | -4.4632 | -43.2386 | 2025-11-05 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 88a3f645-43f0-39d6-b359-a0f8a6c0acec | -4.4073 | -48.9474 | 2025-11-05 02:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 9d69b1eb-4c49-35c3-af14-516c43e6ac8c | -5.4553 | -45.3988 | 2025-11-05 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| a8bf49a3-3858-37ea-9183-99f0f7c8e615 | -4.4446 | -43.2164 | 2025-11-05 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 01536beb-236e-3e4f-b3d1-aebc2f3a8778 | -5.2453 | -48.4966 | 2025-11-05 02:40:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 65909cc7-21b8-3f05-a2d8-e546f447aafa | -4.4259 | -48.9465 | 2025-11-05 02:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| f70365c6-4eda-3f3b-9b38-2d799b036a71 | -2.6508 | -48.52 | 2025-11-05 02:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| a88e632a-2978-302c-8ed9-020029bfa10c | -5.2452 | -48.5182 | 2025-11-05 02:50:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 57351c32-224c-3112-a6c4-e0cce5387948 | -5.4705 | -43.5906 | 2025-11-05 02:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| a99f5067-f6cb-3d21-a349-523785dfd495 | -5.0399 | -43.6205 | 2025-11-05 02:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 1d473c1c-b6c0-3e97-93cd-503982cfed10 | -4.4073 | -48.9474 | 2025-11-05 02:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 156.4 |
| 4d7bafdc-f474-3b66-9a09-a4caeaf00ef3 | -3.4899 | -43.6383 | 2025-11-05 02:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| f1dc81c0-2c2f-3ace-82ff-04278278d8cf | -4.4819 | -43.2374 | 2025-11-05 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 9d88d5ab-29e7-34fe-a141-edc24e955449 | -5.2453 | -48.4966 | 2025-11-05 02:50:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 1b7a283d-4021-3a30-9514-6f5cb8a7ea9a | -4.4446 | -43.2164 | 2025-11-05 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 9441a847-57dd-38f8-819f-1a49e2b17d9a | -4.4259 | -48.9465 | 2025-11-05 02:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 1b4f38c2-bd69-3500-b948-92b2d318dd19 | -5.4553 | -45.3988 | 2025-11-05 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 22a1220b-42a8-34ae-8326-7988da5bca0d | -5.2266 | -48.5192 | 2025-11-05 02:50:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 2eca370b-0c57-3066-a446-f4728dbc1bc4 | -3.49 | -43.6152 | 2025-11-05 02:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 684676c8-0fb3-3e68-a048-ae8f68b7d154 | -4.4633 | -43.2152 | 2025-11-05 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 168.8 |
| dbeceedb-59b8-366a-a187-abfd297d0ee1 | -4.482 | -43.2141 | 2025-11-05 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| a646ba3d-13ba-3be4-8fcb-f7248d479f9b | -5.2268 | -48.4976 | 2025-11-05 02:50:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 1245a3b4-c452-334c-b23e-923c6407317f | -5.4707 | -43.5674 | 2025-11-05 02:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| af7cd376-72d9-3d4c-81fd-14e161f7e881 | -4.4632 | -43.2386 | 2025-11-05 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 58dcc0f7-4f1d-3282-9670-444b8e8ef013 | -4.4819 | -43.2374 | 2025-11-05 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 0ef5aac7-4bcf-39b6-a43b-c850b9b33d56 | -4.4633 | -43.2152 | 2025-11-05 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 173.4 |
| c9630bd3-76b7-3e55-86c2-6be05731c3ee | -5.2452 | -48.5182 | 2025-11-05 03:00:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 84.3 |
| c3c70960-148f-3113-9dd7-9074701fc73c | -5.2453 | -48.4966 | 2025-11-05 03:00:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 1f8d0a29-66e8-344c-b623-70effb7c2d3c | -5.2268 | -48.4976 | 2025-11-05 03:00:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 57.2 |
| a1a42f6e-7860-3848-834d-4efe2adfd99a | -4.4632 | -43.2386 | 2025-11-05 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| ac3f7ddf-1482-38d0-b98c-38c0c6280535 | -2.8124 | -45.1499 | 2025-11-05 03:00:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 46.7 |
| eee1aa7b-4150-3ffc-827f-3e7f5c2bc7d2 | -4.4075 | -48.926 | 2025-11-05 03:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 1d4c82bb-83f3-3f28-8825-e9c5e110fcb7 | -5.4705 | -43.5906 | 2025-11-05 03:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| e3f2792e-f5c0-342d-b293-ef30312e3dd9 | -3.4899 | -43.6383 | 2025-11-05 03:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 68809f3f-49c8-3681-9ea9-6abc50788c10 | -4.4259 | -48.9465 | 2025-11-05 03:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 151.8 |
| 02bf4fc5-9c21-3f12-9d31-935bab19b38d | -4.4258 | -48.9679 | 2025-11-05 03:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 5b96ca7f-72d8-356e-94fb-673f1ad12808 | -4.4446 | -43.2164 | 2025-11-05 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 42fa8318-1bab-370a-8d8e-7dfabfbc0f1a | -4.482 | -43.2141 | 2025-11-05 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 31acd3c6-1c38-31c7-a690-e79191addc80 | -5.4553 | -45.3988 | 2025-11-05 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 83955fbd-d985-3a7d-8e5f-52d1b02033bd | -4.4072 | -48.9688 | 2025-11-05 03:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| f9ccc167-0c30-3e46-bd80-3fddf8de723a | -4.426 | -48.9251 | 2025-11-05 03:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 7c1a9557-1836-389a-8e31-90a5503f2871 | -5.4707 | -43.5674 | 2025-11-05 03:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| c5002492-72de-3af8-8c43-eba7679d09c4 | -5.0399 | -43.6205 | 2025-11-05 03:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| abae0a70-3011-3053-97ae-7a7368305799 | -4.4073 | -48.9474 | 2025-11-05 03:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 142.3 |
| 5036acca-cca8-35fc-bb1d-546544f137bc | -2.6508 | -48.52 | 2025-11-05 03:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 4d22fc7e-8e34-3e6e-a851-2eeb18a89e0e | -5.4705 | -43.5906 | 2025-11-05 03:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| da057107-ced7-3708-abca-65c4a06d9c27 | -5.2268 | -48.4976 | 2025-11-05 03:10:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 15d7606d-cfe2-3034-8d1d-8c0fed05dd99 | -5.2266 | -48.5192 | 2025-11-05 03:10:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 898f57a9-8591-3639-9369-9aad6a720bb2 | -4.426 | -48.9251 | 2025-11-05 03:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 020cd59f-a9cd-3836-a6a3-01222a5ab9c6 | -2.6508 | -48.52 | 2025-11-05 03:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 18e750a5-a647-3a45-9a9f-085145c1a499 | -5.2452 | -48.5182 | 2025-11-05 03:10:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 62.1 |
| c5fa12bd-f331-31d2-887a-1c9c922fcb0d | -4.4072 | -48.9688 | 2025-11-05 03:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| c4c16132-c0c2-3e31-a4ad-afb7a57e08fa | -4.4073 | -48.9474 | 2025-11-05 03:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 246.7 |
| dc2278c2-a2aa-3f75-8224-69ae77142f1a | -4.4633 | -43.2152 | 2025-11-05 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 631a6bc2-5477-3e0b-92ab-cdd7f1d7b0f5 | -3.4899 | -43.6383 | 2025-11-05 03:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| cdfe4258-3bce-3fe0-a7f1-e66c9003adb4 | -5.0399 | -43.6205 | 2025-11-05 03:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 698c41dd-a8f6-343e-b486-ce3c9b2c0d99 | -5.2453 | -48.4966 | 2025-11-05 03:10:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 86.6 |
| b5dd8ba4-a4d2-3846-8b0c-56d2909a5b51 | -5.4553 | -45.3988 | 2025-11-05 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 387db639-bcd8-3ef5-b41f-8aa8908950e0 | -4.4075 | -48.926 | 2025-11-05 03:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| de7c9343-ff04-3870-b89f-466aa0efa24e | -4.4632 | -43.2386 | 2025-11-05 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 83343f78-4d27-3a94-b5a5-f3d4f68de36b | -4.4259 | -48.9465 | 2025-11-05 03:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 686127b5-183b-350a-9f15-8ce03a91e809 | -5.4707 | -43.5674 | 2025-11-05 03:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 21ce295e-33ea-30b1-8bc6-ded804995004 | -4.4446 | -43.2164 | 2025-11-05 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 20da0995-4f69-319c-bd6f-3b1042c6d5d7 | -4.4259 | -48.9465 | 2025-11-05 03:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 11223f7f-9dbe-3498-9cac-a48c17d74213 | -5.2268 | -48.4976 | 2025-11-05 03:20:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 80.1 |
| e3057547-8964-30e6-842d-a93925392918 | -4.4632 | -43.2386 | 2025-11-05 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |
| a2a69321-d095-34d1-ac8f-d3d85f241add | -3.4899 | -43.6383 | 2025-11-05 03:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |


[Clique aqui para ver as próximas entradas](README7.md)
