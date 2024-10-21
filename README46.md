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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f98183c4-f1b2-31bd-be01-d15588f64a03 | -3.03098 | -53.86915 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16986bc8-d7ef-364b-bfb3-7e8489d3a039 | -3.02691 | -53.86849 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1932526-86cf-3a64-86ac-de69ef50356d | -3.02467 | -54.34704 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb3a4e68-2c8f-3147-9dbf-3549ba9bdb06 | -3.02404 | -54.35097 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b772c978-187a-3a6a-9f7c-dfc2e9544673 | -3.02124 | -54.50336 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09267487-6776-33f6-8e6e-ace6d1d1ea68 | -3.64879 | -54.09832 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc68e225-364a-332c-9477-1973fed249bf | -3.64821 | -54.10201 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ea249e5-cba2-3321-986f-86b056a58f6e | -3.6474 | -54.10146 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f926e60b-8895-3e7c-bde6-5e568a56e872 | -2.86862 | -53.97055 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d92e53b-74a7-30ba-88df-e3143b774662 | -2.86842 | -54.10395 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edc955db-5d64-3999-8770-87957dcf49a3 | -2.84597 | -54.08493 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82cb23b4-652a-3281-b03f-65173c0f4286 | -2.84098 | -53.985 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 113f4355-060d-30f1-a4ea-c8f7279bfad4 | -2.83747 | -53.98064 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06a13c9a-2012-3d4b-ada6-7a27cecfb220 | -2.83687 | -53.98433 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e68261d4-5d2a-3a6a-80ab-65789ceb39b3 | -2.80394 | -53.93492 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8fdd6dbf-b49b-33dd-ae92-b5c630e259de | -2.80337 | -53.93855 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 675c5b52-4060-3214-bf82-06c0f67504b2 | -2.75403 | -54.03619 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48ae6d2c-05c4-311e-a8b2-24b1e4160864 | -2.75344 | -54.0399 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19fdfe05-1c39-3a0a-8399-af73718e4a99 | -2.56285 | -54.00955 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8e42e906-6f60-379c-997e-2ce83df4c794 | -2.56166 | -54.01706 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 438fef42-b6ee-3aa1-9cd4-87c90072e2d1 | -2.27417 | -53.7535 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5a2eb5c-bb5d-3a87-8ff9-3846b8c93b64 | -2.27359 | -53.75714 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c541be2-e421-356c-9a5d-bd886c45c4c2 | -2.27009 | -53.75283 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b8b5423-b23c-3946-a531-da4b9eb27bbb | -2.26951 | -53.75647 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d55ecb3c-7bbb-3d15-bf20-b95f570f188d | -2.26653 | -53.72252 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54d8855e-ea99-322b-8211-df72fae443e4 | -2.26595 | -53.72614 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a71407d-7595-312b-87a6-a142026ebf7f | -2.26542 | -53.7558 | 2024-10-21 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a92276f7-df1c-373b-bd1b-bcd5584bb9dd | -3.62259 | -53.97498 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8678189a-f95c-399b-8c72-01c8d3970d46 | -3.4392 | -54.12455 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a32af49-4f91-3b76-92fe-9a0ac76d493c | -3.4351 | -54.12382 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7db1d9fe-f0f1-3358-a397-92b668442444 | -3.41454 | -54.27338 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54801ed0-22d1-3170-8e6d-84c5a7b8d09f | -3.41392 | -54.27708 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30a7d7ec-51ee-3166-afa2-d8199b0a845a | -3.41331 | -54.28077 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3fcc0d2-d9fa-3fc8-a1c3-b895ee3e3e32 | -3.27628 | -54.1571 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8880dc98-068f-3486-af2b-6f8ce18241d1 | -3.27446 | -54.16837 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2b7a0e9-b28a-3253-b4fd-93a013b1ba67 | -3.27387 | -54.17204 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60a2dc03-6217-3c3d-b46d-1735482c6fda | -3.26975 | -54.17128 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72662ef0-49b2-3e91-851b-e32bd7543adc | -3.26542 | -53.78328 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37e8cf9d-1ac8-33bd-89e9-4fb9a063cd45 | -3.26083 | -53.78613 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| faf0f7e2-5151-3927-a11d-0226ab6fbeed | -3.23501 | -54.15009 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0df4ae97-8329-3380-90a3-6436da1cd848 | -3.21751 | -54.8611 | 2024-10-21 04:36:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 30159539-95cb-36a7-9321-8344130a7f31 | -3.21319 | -54.86032 | 2024-10-21 04:36:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94e63b54-efdc-3cfb-91ed-90a4a45b939b | -3.11142 | -53.73183 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb90456e-345f-3c4b-909b-47c0c0884621 | -3.10109 | -54.16338 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea8f7740-79ee-3337-a503-17be79316953 | -3.09752 | -54.15906 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a27a3710-ebf4-31e6-b324-07c9e03c3cf5 | -3.09694 | -54.1627 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 390b356b-3e86-35e8-a44f-0fcea9d7e651 | -3.0955 | -54.1586 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3660d460-1183-360a-b825-eaf96b01ec79 | -3.0949 | -54.16224 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 75aa1c75-56f8-38b3-b78c-9246bfe2d84b | -3.08509 | -54.15702 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11c912da-a4bd-36ad-add7-904cb9719be5 | -3.08035 | -54.16005 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fbca3eed-fa30-399c-bb92-f9a5c8132aca | -3.07976 | -54.16379 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 99f84519-ba6c-34c1-b5bf-87b836fe3850 | -3.14968 | -54.35095 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb2f72db-100c-3b9e-8bff-132a6f1c0ca6 | -3.13947 | -54.36088 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 604040f7-fa07-3876-88cf-c03e4ef07ca5 | -3.1387 | -54.28574 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 385acab9-092a-3178-b164-bdb917b71a33 | -3.1359 | -54.35632 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b32a8379-6722-3ab1-b97a-74816b2a7365 | -3.13453 | -54.28501 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34d498ad-596d-36c0-89c1-9b9bf6bfbf7d | -3.13171 | -54.35558 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 841f685a-15b4-347b-8a05-bd9ea9c7e77e | -3.13109 | -54.35943 | 2024-10-21 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f5712e6-73cf-3e36-90d2-896c4b1fb31a | -3.10612 | -54.17157 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 51df5c72-d29a-3678-bc5a-f9cad4f4a37a | -3.1055 | -54.17532 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1d455b9f-96ac-3e5e-8149-1ef6729c7235 | -3.10488 | -54.17908 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 96aa03fc-8a36-3dc7-bfc0-a2523f85096d | -3.10197 | -54.17089 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 5581bfa4-e1b8-36d8-b9f1-86f85588459a | -3.10074 | -54.17836 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 33219bb0-e147-38ae-b23b-de179332e0f3 | -3.10011 | -54.18215 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 1b435ab0-9486-3ecf-a0e0-92bdfffa575f | -3.09993 | -54.17072 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e354c3f4-890c-393c-9e83-6d5fcc67edce | -3.09934 | -54.17445 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 9c768813-7e5d-3096-944e-b703947db7e5 | -3.09885 | -54.18974 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f085e0c6-5b05-35b8-b436-a8c413838c16 | -3.09874 | -54.17819 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 1d3e9fa6-7533-3c58-a6ba-eae431b460dd | -3.09844 | -54.16656 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ae6d8d82-95d3-324b-b546-5bd15e59ab57 | -3.09815 | -54.18198 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| d8a6d866-b805-3ae4-be47-790cd39e54a5 | -3.09695 | -54.18956 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| edd0f28c-e9f0-37b3-a853-02c57d387dfd | -3.09578 | -54.17004 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0c2e2ec7-17ae-38c4-96c8-c7de8edb3057 | -3.09534 | -54.1852 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| aa9312fa-8f37-3092-8083-c15795a91b63 | -3.09519 | -54.17376 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1be736f7-0e79-3f6c-aaf3-c51c87b4d916 | -3.09472 | -54.18898 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0f39161e-b0e2-300d-bf9b-40ce265d2f06 | -3.09429 | -54.1659 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ec63c90a-151c-3e9f-ace8-32d4b1ef92df | -3.09368 | -54.16958 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| bfeb6358-5c54-385e-bc9c-0a547380d9c1 | -3.0934 | -54.18504 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9c09ac02-f3af-3226-9f5c-acf9a0798fd5 | -3.0928 | -54.18883 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b408cb47-ab83-3344-baed-8c76e32b6db4 | -3.09244 | -54.177 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| c7b34bf5-5357-3df8-b554-1889b8bb5c0a | -3.09163 | -54.16941 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 71efe63b-e214-3b86-af89-8a0a134ae346 | -3.0912 | -54.18451 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ff8e961b-4df8-3aa3-9037-9ebe8567a748 | -3.09104 | -54.17312 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| ea966931-aab0-304a-bafc-5bd4cffa8799 | -3.09045 | -54.17684 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| e25714fa-2707-3164-bd9e-72ad76576e24 | -3.08866 | -54.18813 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 81c278da-1cf8-3d72-9fe0-90cf9e3c776a | -3.08629 | -54.17619 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| f9577460-ad50-3802-86a8-9435440dedba | -3.0857 | -54.17991 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| cd4823f7-ad56-3111-90fc-a1cce3d9be2a | -3.08391 | -54.16446 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d5d13d73-62e9-30a2-b171-822c1ce83570 | -3.08273 | -54.17182 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 867a5a18-6f05-317d-8d6d-c84ba473cbcd | -3.08214 | -54.17553 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 115785e4-6134-367c-a7df-e7e058dd93ef | -3.08155 | -54.17924 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| eaf53a20-77a8-37a6-8dd7-ba52e16f3294 | -3.08095 | -54.183 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f584c6f9-badb-37fd-a219-cca31f62fa24 | -3.07917 | -54.16748 | 2024-10-21 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 6087bc00-187a-3da6-a84b-06d8f4936b43 | -4.04954 | -54.65435 | 2024-10-21 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89fc3aa9-fe8e-3b54-a0ad-1e0b758c5a44 | -3.82668 | -54.61221 | 2024-10-21 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c03f3695-c60b-3071-a8b1-00a6a212bbbc | -3.68383 | -54.2129 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbb60241-75a9-3b1c-8600-ebdc2e62d489 | -3.62608 | -54.67348 | 2024-10-21 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c6a33be-b2a4-3505-839a-3734aaae80da | -3.62182 | -54.67283 | 2024-10-21 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f552e78d-4c0e-3f04-935f-fb1945b0ac5d | -3.62117 | -54.67683 | 2024-10-21 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca14015f-76a2-3ebf-8ab7-50f12813a8a2 | -3.54888 | -55.44548 | 2024-10-21 04:36:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README47.md)
