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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6670f958-0d53-3085-9b18-74f446149363 | -10.0239 | -53.439201 | 2024-09-26 00:56:10 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3dbfa81c-a08a-35ed-bd5e-eade62f7b07c | -10.0254 | -53.446201 | 2024-09-26 00:56:10 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb0484de-1178-30bd-80a1-970f38a1819d | -10.027 | -53.453201 | 2024-09-26 00:56:10 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 027171f9-0701-3ea7-a79c-aa1b0ea6e7b7 | -10.0285 | -53.460098 | 2024-09-26 00:56:10 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 75819dc5-4a80-37c8-b7da-667dc03b7e78 | -10.0301 | -53.467098 | 2024-09-26 00:56:10 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98ac4989-2aec-3e1c-8137-bc682b162f43 | -10.0316 | -53.474098 | 2024-09-26 00:56:10 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 576ba2d4-f505-3a70-9b5a-a9970354675d | -10.0332 | -53.481098 | 2024-09-26 00:56:10 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a72a7608-a98c-3149-b26f-210a5a7bace2 | -10.0347 | -53.487999 | 2024-09-26 00:56:10 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 65b9b10d-2459-3d98-ae15-de43dc8ea712 | -10.8821 | -57.427101 | 2024-09-26 00:56:10 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 30eff44e-490b-3e64-b5e5-2f7c6566ec81 | -10.8843 | -57.437199 | 2024-09-26 00:56:10 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 866b78fd-9d33-38bd-b2a2-332df14bb92c | -10.8864 | -57.447399 | 2024-09-26 00:56:10 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b2ead1cb-8e17-3f64-b462-a96edf0b7b58 | -10.8885 | -57.4576 | 2024-09-26 00:56:10 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f3ce5e0f-b729-372b-bd1b-24351114439c | -11.2599 | -65.299 | 2024-09-26 00:56:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| ded87ee5-419f-3cce-a3cd-b6e39fcb8e6c | -11.26 | -65.2801 | 2024-09-26 00:56:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.3 |
| bd6e6adf-7041-38d8-ab67-8d1b8318e93d | -10.0141 | -53.441399 | 2024-09-26 00:56:11 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9a73ddcd-ce9c-345a-9a37-eb7b986c4630 | -10.0156 | -53.448399 | 2024-09-26 00:56:11 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43b9c618-9be3-3474-882b-009006f15044 | -10.0172 | -53.455399 | 2024-09-26 00:56:11 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 515bbbfa-4be8-35df-8ccf-0b554a5faaea | -10.0187 | -53.462299 | 2024-09-26 00:56:11 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0f1d768c-fcc9-3873-8488-6e9f72bcf0de | -10.0203 | -53.469299 | 2024-09-26 00:56:11 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 39b79185-2379-3625-88ab-b969c7b6bcc6 | -10.0218 | -53.476299 | 2024-09-26 00:56:11 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 428ef702-f3e2-3ac9-b6d2-3a3cbaf66166 | -10.0234 | -53.483299 | 2024-09-26 00:56:11 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a22d69ee-7cef-3cd2-b8e1-c3d434f32dc2 | -10.0249 | -53.4902 | 2024-09-26 00:56:11 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9983bdb4-49e4-38c5-bb44-0df97fa3e9e4 | -10.8745 | -57.439201 | 2024-09-26 00:56:11 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 92739f01-1aae-3bce-bb9f-03629aad4848 | -10.8766 | -57.449402 | 2024-09-26 00:56:11 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ff592d2-b160-3725-913e-cbd6bd80158b | -10.8787 | -57.459599 | 2024-09-26 00:56:11 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 33a643b1-7f24-3fc5-8a72-52decae60728 | -10.0089 | -53.4645 | 2024-09-26 00:56:11 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df54bd06-8496-33ed-b278-808422f036b9 | -10.8668 | -57.4515 | 2024-09-26 00:56:11 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 06329911-c110-3334-96bc-f53f9a02629d | -10.8689 | -57.4617 | 2024-09-26 00:56:11 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 698d94ac-a6a3-3d65-8db4-390d4d4f8e4a | -10.1995 | -54.610901 | 2024-09-26 00:56:12 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f0a39343-1e09-3c6e-b6b4-5ae3faf83569 | -10.2011 | -54.618198 | 2024-09-26 00:56:12 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 435a250d-a6a5-30ec-99a0-c06a5b5d845a | -11.8613 | -49.6327 | 2024-09-26 00:56:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 370eea26-d05b-336d-9930-b3374dd47272 | -9.3212 | -50.925301 | 2024-09-26 00:56:13 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 595ef562-d15f-37d9-ac1f-1b89f97ad038 | -9.4352 | -51.467201 | 2024-09-26 00:56:13 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4261dfa3-1977-32d2-a1fc-1149b3da61b2 | -9.4369 | -51.474499 | 2024-09-26 00:56:13 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e1293c6-34ac-3f04-b486-0cb58d4409a9 | -9.4418 | -51.496201 | 2024-09-26 00:56:13 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91fe1d53-6c36-3b56-aecc-d1eaa4670a07 | -9.4435 | -51.503502 | 2024-09-26 00:56:13 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fceec60-afd0-3baf-bd29-d898e7934d9e | -9.4271 | -51.476799 | 2024-09-26 00:56:13 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92c8d39a-0756-38b0-bc4b-6daaecef5729 | -9.432 | -51.498501 | 2024-09-26 00:56:13 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53273ad8-730b-3349-ab6d-a05542137c53 | -9.4337 | -51.505699 | 2024-09-26 00:56:13 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05394d15-d7a2-39e8-bc14-57c4228593dc | -9.4123 | -51.457199 | 2024-09-26 00:56:13 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db9a32af-4722-3d13-932f-faa932899595 | -9.4156 | -51.471699 | 2024-09-26 00:56:13 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 788c66c0-8fbc-39dc-831a-ef18764c2e29 | -9.4222 | -51.500702 | 2024-09-26 00:56:13 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fda4f5ba-1723-3e47-b7be-b82d20aab86b | -9.4008 | -51.452301 | 2024-09-26 00:56:13 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa7bfa1c-94c4-33cb-bc10-a2350f6f6ccc | -9.4025 | -51.459499 | 2024-09-26 00:56:13 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d675829c-628d-3f81-bb84-0db26797a2be | -9.4041 | -51.466801 | 2024-09-26 00:56:13 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc68444e-892e-373b-b78a-9a176b08b28b | -9.4058 | -51.473999 | 2024-09-26 00:56:13 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cbe7d29-f06b-3709-b805-489895c3c016 | -9.4141 | -51.5103 | 2024-09-26 00:56:13 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7fedef8-b417-3351-aa8e-7c6454ca07c5 | -9.4157 | -51.517502 | 2024-09-26 00:56:13 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| affae77d-eec8-375c-a28e-b8a5a46fb19c | -10.5718 | -56.775902 | 2024-09-26 00:56:13 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58673f48-204b-3efb-93da-f518656e2b13 | -10.5738 | -56.785099 | 2024-09-26 00:56:13 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 517516e4-5f51-3617-98d6-20e8d37a5b43 | -10.7263 | -57.513 | 2024-09-26 00:56:13 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a919b47-3027-36c1-85a2-992e729cb205 | -10.7285 | -57.523201 | 2024-09-26 00:56:13 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b2af6848-9e82-38d6-b8e3-827c4c8c582a | -9.4076 | -51.527 | 2024-09-26 00:56:13 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88597dfc-d34b-3aa6-bb0d-f63c21dc5109 | -11.955 | -60.363 | 2024-09-26 00:56:14 | GOES-16 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 42.5 |
| d782b611-16d1-3880-8ccd-f215c9474549 | -9.8123 | -53.552601 | 2024-09-26 00:56:14 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b9ed8f8-b07a-341a-aeb9-9941ffd4a70d | -9.8138 | -53.559502 | 2024-09-26 00:56:14 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c103cbb-53ac-38e6-a531-fa3ee3b6f9f0 | -9.8154 | -53.566502 | 2024-09-26 00:56:14 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df426b4d-fc79-3c94-9e05-cec58a936852 | -10.638 | -57.383701 | 2024-09-26 00:56:14 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 069ef23c-a87d-35dc-b64d-f8c2b4949ed1 | -10.6401 | -57.3937 | 2024-09-26 00:56:14 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ff173e5-c8fd-3bb5-a902-4a9e99c84261 | -9.7222 | -53.193699 | 2024-09-26 00:56:14 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad79e7dc-5367-335a-9621-0997ddb17b2b | -9.7237 | -53.2006 | 2024-09-26 00:56:14 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd36f38c-69ba-33f3-bd79-2871b9da37d1 | -9.7994 | -53.540798 | 2024-09-26 00:56:14 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4632bb2a-fdf0-3a24-a02b-909c92c70db2 | -9.8009 | -53.547798 | 2024-09-26 00:56:14 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c413fd9-1888-31dc-9c25-f7926cd21679 | -9.8025 | -53.554798 | 2024-09-26 00:56:14 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f1b0f03e-012a-361c-be44-9ec9001316a7 | -9.804 | -53.561699 | 2024-09-26 00:56:14 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d3e3525-e957-35c6-a00e-a2605aa12a31 | -9.8056 | -53.568699 | 2024-09-26 00:56:14 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1c3c2d38-952e-34d6-9bbb-05254d2d65b1 | -9.8071 | -53.575699 | 2024-09-26 00:56:14 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7370e3e-5719-35d4-b34f-bca469eb23fe | -9.8087 | -53.5826 | 2024-09-26 00:56:14 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eab2506f-54e0-377a-b8af-5d75847e8922 | -12.2175 | -45.5074 | 2024-09-26 00:56:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 85344152-29bf-3a44-a912-5fa05ae5037a | -12.2179 | -45.4844 | 2024-09-26 00:56:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| f994335e-20f3-3305-a367-aaa8cc67e25e | -12.2367 | -45.5045 | 2024-09-26 00:56:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 188.1 |
| 3ddc921e-9a6c-3b46-bee1-f32088894fa5 | -12.2371 | -45.4815 | 2024-09-26 00:56:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 77730c97-d6b0-3c1b-bcc4-6c4a0bebfe8a | -9.7896 | -53.542999 | 2024-09-26 00:56:15 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1a02fc0-19e3-3a2a-866f-ff9c58bed9f9 | -9.7942 | -53.5639 | 2024-09-26 00:56:15 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d945906-296e-3d4e-b4bb-1738932adfed | -9.7958 | -53.5709 | 2024-09-26 00:56:15 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d816e6e-87dc-39c6-b0fa-303b37ef5e95 | -9.7973 | -53.5779 | 2024-09-26 00:56:15 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bfe42736-c4ca-3ca8-9ffe-ea65c1b79e92 | -9.7989 | -53.584801 | 2024-09-26 00:56:15 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6243bacf-1e52-34fa-9f08-85fee38c129b | -9.7767 | -53.5313 | 2024-09-26 00:56:15 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7f206cca-e1f1-359d-96d2-7f1c1f854cf5 | -9.7783 | -53.5383 | 2024-09-26 00:56:15 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 73d8609b-cd83-3318-8430-9c395f959873 | -9.7798 | -53.5452 | 2024-09-26 00:56:15 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c3a2f21-5418-30c0-b1c4-c0345c913fa7 | -9.7891 | -53.587002 | 2024-09-26 00:56:15 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9730fb8c-d116-3968-be95-4d0d656ba4ee | -9.3751 | -51.836399 | 2024-09-26 00:56:15 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d67cde69-4bbe-3967-ad4c-42bc86c83d84 | -9.6685 | -53.184101 | 2024-09-26 00:56:15 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5571faf-226b-303a-80f0-62bff0ba1a21 | -9.6489 | -53.188499 | 2024-09-26 00:56:16 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01a3649e-1f42-31e7-989a-90090520d471 | -9.6504 | -53.1954 | 2024-09-26 00:56:16 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a94690c1-5add-3e9c-9e6f-b99fcec06587 | -9.652 | -53.202301 | 2024-09-26 00:56:16 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 081dbab8-69e7-3a3f-b5ae-07ba311dd363 | -10.4562 | -56.907299 | 2024-09-26 00:56:16 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f1700fc-ead9-37a6-af3c-39de8aadf9e8 | -10.4582 | -56.916599 | 2024-09-26 00:56:16 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b74f1995-07a9-3d98-8839-a259ee919e5d | -9.6339 | -53.2136 | 2024-09-26 00:56:16 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1db6c23-eb39-3b60-9dfb-8936dd833194 | -9.6257 | -53.222801 | 2024-09-26 00:56:16 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 673ba673-54b1-3504-a074-062931996c42 | -9.6272 | -53.229698 | 2024-09-26 00:56:16 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f58d037c-a34c-3241-ab92-b629e6e2464c | -9.6138 | -53.261799 | 2024-09-26 00:56:16 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9e91651-2669-3206-8ccb-29c9c858f9bb | -9.6694 | -53.511501 | 2024-09-26 00:56:16 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f66379ad-d3e1-390b-bb01-c34ffbb4c52c | -9.671 | -53.518501 | 2024-09-26 00:56:16 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 15047552-7ba1-39da-b54a-46e54464c52f | -12.5276 | -53.496 | 2024-09-26 00:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 6c2c891f-faff-386e-b747-0999e3d83226 | -9.5755 | -53.321301 | 2024-09-26 00:56:17 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08d12c79-6c82-3128-beb1-ef747f77915f | -10.3193 | -56.743599 | 2024-09-26 00:56:17 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 784ad32f-10c5-365d-bd18-66e304801603 | -10.3213 | -56.752701 | 2024-09-26 00:56:17 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0c10c75b-416c-3330-b817-f7dcb594c1eb | -10.3115 | -56.7547 | 2024-09-26 00:56:17 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f86b82ab-72db-364e-acb7-1aad2c89f39d | -10.3134 | -56.763901 | 2024-09-26 00:56:17 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README25.md)
