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

## Dados Diários - Página 196

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fefd4d97-24db-3bbc-a64c-c263cd026123 | -9.46467 | -68.52511 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 99c2d8e8-d08a-3c8a-a1e2-a3f6d01c8fa9 | -9.46507 | -68.52206 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 778e8d7e-40c5-316c-80e1-b3c8d211cdca | -9.46978 | -68.52586 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c25235f-dc19-3e67-a0d1-b307a2215675 | -9.47449 | -68.52963 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 278b10dd-949e-3801-86f1-e46738c82268 | -9.4792 | -68.53336 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 282b05fb-8713-34dc-aaea-fa446dd17715 | -9.4796 | -68.5303 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c086b033-3226-376c-8059-c4cf960e7729 | -9.48431 | -68.53399 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1acc4365-937b-3826-980a-2ed0a003b709 | -9.49933 | -67.11345 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 04c54347-915d-33b6-8356-605ca992e42e | -9.49983 | -67.1096 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 66f9b8e1-b295-3a7a-ac3f-1970661e69d7 | -9.50757 | -68.51538 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e3864e0-2686-3b86-af82-ec9e28753d62 | -9.53717 | -68.56626 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60885313-49e6-3631-ad10-b35d434d4ea9 | -9.53758 | -68.56326 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08fbdfb1-e512-36e8-b751-fc05d253b828 | -9.53843 | -67.71496 | 2024-10-02 06:27:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5eab50f3-d4be-3ee1-9696-41517982a865 | -9.53888 | -67.71152 | 2024-10-02 06:27:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cfddc3e-f488-3a0b-a103-666fcd6e2b21 | -9.53934 | -67.70805 | 2024-10-02 06:27:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78930a4a-24c3-3470-97e4-ef7bfabd6af1 | -9.54067 | -67.71721 | 2024-10-02 06:27:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fac214e3-66ed-3760-9d52-e2db224fa5e5 | -9.5411 | -67.71377 | 2024-10-02 06:27:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 190dd4bf-e0f4-388e-96ba-b701fd617f43 | -9.54153 | -67.7103 | 2024-10-02 06:27:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dea9b62d-dfb3-3b4c-badb-ae59d0f1a907 | -9.54336 | -67.71921 | 2024-10-02 06:27:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d75faa40-d64a-379e-bdeb-745ab72bbcfa | -9.54382 | -67.71577 | 2024-10-02 06:27:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20d22da2-b96d-3ec6-a50d-fa0f6049381a | -9.54428 | -67.71232 | 2024-10-02 06:27:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98326370-e937-3e64-ae1a-3fab6f031da9 | -9.54513 | -66.62255 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7150d38f-cd1b-3781-a5e9-0fab2775c1d7 | -9.54566 | -66.61839 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d31be24a-f09a-3ae9-b216-efbe27031f15 | -9.54606 | -67.71803 | 2024-10-02 06:27:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eab4bb34-1e62-3f0f-ae34-0d8e8c106387 | -9.54619 | -66.61421 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1a677ab0-cb5b-377c-aa78-7b123768a80d | -9.54649 | -67.71458 | 2024-10-02 06:27:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 380bd943-306e-3536-9e92-12066653cfc5 | -9.54693 | -67.7111 | 2024-10-02 06:27:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a828c16-b858-32f6-85ff-c6f2301e75ab | -9.55173 | -68.26084 | 2024-10-02 06:27:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 460d36fd-1afa-3d2a-b52f-0e70cf53ec87 | -9.55176 | -64.2569 | 2024-10-02 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2584337c-d9c2-325c-a427-b3aa19acfe78 | -9.55468 | -64.26203 | 2024-10-02 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc518388-3166-31d9-bc4c-fd87f4fab690 | -9.55776 | -64.26396 | 2024-10-02 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da45736c-2181-3c21-89b6-987371d123a4 | -9.55848 | -64.25786 | 2024-10-02 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0a2737a-576a-39a6-b304-d86c77b860b1 | -9.56139 | -64.26292 | 2024-10-02 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f61014ea-5069-352d-b066-830a2dfcb01b | -9.56215 | -64.25681 | 2024-10-02 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 06b0d0d9-d154-3aff-b639-6f3b93582d34 | -9.56447 | -64.26492 | 2024-10-02 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a868baac-e3e0-347b-a691-e4d293d8b581 | -9.56519 | -64.2588 | 2024-10-02 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5a35f65-f027-3802-986b-0d7539ef8766 | -9.58315 | -67.8564 | 2024-10-02 06:27:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74f7f9ae-8566-379d-96bd-4d0dc0ff8ca9 | -9.58336 | -66.50911 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26dab734-1686-3905-b24b-b85533709427 | -9.58866 | -66.50906 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| da2c244d-4b61-374f-938f-22b45d78cfc2 | -9.58916 | -66.50491 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| df2fb9da-825a-3b75-850d-c0f36f0168f9 | -9.58921 | -66.50986 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58b4c548-212e-32d1-a6d2-f0bd3ce33f53 | -9.58975 | -66.50572 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 735c1d6c-d138-3a38-86a5-9baf0bbbdc4e | -9.59502 | -66.5057 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 836dc585-4f0a-3fde-850c-7ca76209a6cb | -9.59552 | -66.50158 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcd86e42-5c38-3a63-80dd-aa5f7a01f81a | -9.59613 | -66.50237 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f37a1d14-62b0-38b6-86fd-b8b4e4edeb70 | -9.60545 | -68.73999 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 179b33e0-ff8e-3b85-95f2-752011bdbe7d | -9.60584 | -68.73705 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b27ef3f1-ea4e-306d-9241-26ed0c0c2e1f | -9.60958 | -67.16135 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08b893f3-3382-37fd-9460-2053ceaafa0a | -9.61087 | -68.73784 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12b10111-1bb6-3657-938b-5a685e17d181 | -9.61138 | -67.16019 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7770e8ff-c803-31c2-b2e8-f687aa653993 | -9.61778 | -67.45719 | 2024-10-02 06:27:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 313ba68b-8de8-374c-9d4b-fa536629f879 | -9.61823 | -67.45361 | 2024-10-02 06:27:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf017d25-c837-35ea-a010-8aeecb54c442 | -9.62258 | -68.612 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cdeda3d-8e9d-3eab-96eb-a93ea85f6b17 | -9.62298 | -68.60899 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dff16233-e227-3746-baaa-4a46a58ae910 | -9.62465 | -68.74701 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d71aa3f2-0818-3dad-aafb-282efe2234d1 | -9.62481 | -68.74873 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98ea2bc5-b63a-3b7f-b4e2-3ea607a87564 | -9.63285 | -67.47055 | 2024-10-02 06:27:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 727f06c8-cc87-3516-87dc-5bff8cacfd7b | -9.63332 | -67.46693 | 2024-10-02 06:27:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e5ce949a-a222-3109-869a-1606ed78a56b | -9.67198 | -68.81654 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9302da9e-6cc4-3deb-8029-910da9b5061f | -9.67237 | -68.81361 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1d3501d-0097-3834-aca8-5d6b8cc231bf | -9.67275 | -68.81068 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 47bd36d4-5a41-3fa7-9c56-9a5e5d2fbab7 | -9.69994 | -66.85162 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01df1ba2-a2f3-3022-9b64-b8558abbf200 | -9.75705 | -68.52659 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11319d15-de9f-3721-ba9c-02ba01c1b9d9 | -9.75927 | -68.52967 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96f3fe00-2512-31f7-a53a-bf8ebee43812 | -9.75966 | -68.52658 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53ae150d-ae10-3ad2-a68f-27835e6da122 | -9.89145 | -68.89501 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32c9e8cc-4cfe-3ec6-aef2-b6fcda9da488 | -9.89183 | -68.89213 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51343f4a-9354-3775-9a00-ae01dad06c18 | -9.89722 | -68.88999 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01f3119d-eb8e-32b7-a418-f0e883689ef8 | -9.91151 | -67.30659 | 2024-10-02 06:27:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c9e9eb5-e82b-35dc-be8a-219622d37469 | -9.91292 | -67.30508 | 2024-10-02 06:27:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9bfbd8e9-bae7-39e7-8973-e0de67dec88b | -9.92004 | -66.8427 | 2024-10-02 06:27:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8d3774cc-5227-31e7-8a94-bc714b5deb7d | -9.93614 | -64.92122 | 2024-10-02 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| be7bd48b-8103-3d70-beca-adab76cb4a72 | -9.93679 | -64.91574 | 2024-10-02 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 87cd70b4-e95c-35c6-9910-09ff0c4b8d75 | -9.93745 | -64.91026 | 2024-10-02 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0c8ac466-c22b-315a-8c2f-4025a830ae28 | -9.9381 | -64.90474 | 2024-10-02 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 05137e57-e729-3717-9bac-e41106b16dcb | -9.94265 | -64.92192 | 2024-10-02 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 7813b4d1-39ca-3180-b0a6-e5d9de7928f0 | -9.94329 | -64.91656 | 2024-10-02 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4e5ef971-24f7-3a4a-af51-ed56421b3846 | -9.94393 | -64.91117 | 2024-10-02 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 433948db-3be7-33aa-b903-27333d1a5f8b | -9.94459 | -64.90568 | 2024-10-02 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 6a531978-c94f-385b-8423-0d1ac17b7718 | -9.94525 | -64.90018 | 2024-10-02 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 022fe47c-5058-3931-b535-84a371b7a586 | -9.94979 | -64.91729 | 2024-10-02 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| bf3493e9-1721-3c85-a11e-3cc33a980326 | -9.95043 | -64.91195 | 2024-10-02 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 0eefd74b-f6c7-3d78-8af2-d0b0f660ae02 | -9.95108 | -64.90654 | 2024-10-02 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 198fa76a-c0f9-3509-8570-bf932d0e13a5 | -9.95174 | -64.90108 | 2024-10-02 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 891e440e-6a46-3dea-b3f7-a3ac01cbd7a7 | -9.95425 | -68.76249 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f084729-13df-385e-afb0-904168b8cf27 | -9.96635 | -64.77908 | 2024-10-02 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 130d4e24-36d4-3f32-b83a-379c10455dc8 | -9.96704 | -64.7733 | 2024-10-02 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7e4bdb9-cc01-3491-8ec2-fe2c37f34b9e | -10.87942 | -68.22005 | 2024-10-02 06:27:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59a7c672-eaae-358f-862b-7cb0a5ca8836 | -10.25853 | -68.01677 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e901fc42-9532-34cc-b6d0-b0ef52172353 | -10.11222 | -69.26231 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6608a1a-a37c-34db-8588-806a09228e09 | -10.26632 | -68.76564 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f26213f9-dac5-3c9d-a007-acc1e385b4b2 | -10.26999 | -68.76733 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a622fd7-60ac-3314-a4f2-b0d55f057e99 | -10.27038 | -68.76427 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 964f9d75-d47e-35a3-abc5-d659ad9f1737 | -10.27076 | -68.76125 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2acf7f3-fe42-30d5-b938-b704240bd64b | -10.27099 | -68.7694 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d62b5947-2a2d-341f-b138-636f245b3cc1 | -17.22698 | -56.18985 | 2024-10-02 06:29:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.9 |
| b0db607c-5f02-3c34-9723-9fa47dde837a | -17.15418 | -56.17477 | 2024-10-02 06:29:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 53.0 |
| fc1eb5b8-d163-3156-acf0-f40dfd1febae | -16.89176 | -55.8332 | 2024-10-02 06:29:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.4 |
| 6dea68c7-3761-32a9-bb8d-2d8af77a6967 | -16.88547 | -55.84017 | 2024-10-02 06:29:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 93.4 |
| 96e81400-c31c-3b0e-a3c6-35dc036bbb48 | -16.87603 | -55.83157 | 2024-10-02 06:29:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 135.7 |


[Clique aqui para ver as próximas entradas](README197.md)
