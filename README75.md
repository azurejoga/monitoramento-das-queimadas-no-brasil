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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40827e31-dd62-3b18-8773-953acd76252d | -5.20394 | -48.96839 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b15cba6-e434-3a48-bb70-9df97c4edcf5 | -5.20225 | -48.95756 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f3134fe-7e5f-3f23-afc2-99e49ce1fee7 | -5.20003 | -48.95016 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2c0a57f-5c03-3417-9551-efd4118330ff | -5.19673 | -48.94965 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f9e41f1-5725-3f04-9121-9a9a0f2a61c8 | -5.19343 | -48.94914 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 990ac33c-dc70-3ddb-9556-ddf5ce641376 | -5.19013 | -48.94863 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c5dc799-256e-339f-a38d-2de709c32a9e | -5.18805 | -48.98354 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab939dd7-34f6-34c0-a4b9-aa1c80538493 | -5.18562 | -49.27898 | 2024-09-27 04:38:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc6dfabe-38f0-385e-b6ee-a7bee0d8079d | -2.80225 | -49.58598 | 2024-09-27 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5a66cbfd-bfe4-3434-8a04-57d426b72219 | 0.0943 | -49.85455 | 2024-09-27 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5427630-7715-3fd3-a037-e7def6a7f92e | -1.47434 | -49.48204 | 2024-09-27 04:38:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25d07caf-857d-3143-8126-8976631735b7 | -1.12871 | -49.23379 | 2024-09-27 04:38:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6b0ba946-6d89-3c90-b37a-2358be0a5a6d | -3.53934 | -49.18731 | 2024-09-27 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acb6edb6-b53c-3a05-9f86-f126b68139a1 | -2.95045 | -49.35952 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3c5afa4-6e3f-3b4a-85eb-97aa43d204ba | -2.9499 | -49.36299 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d5fbb3d-0f5e-3f3e-8544-3684b2454ec6 | -2.94714 | -49.359 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 818fb465-2a5d-32cf-80f7-37498ae21fc4 | -2.8423 | -49.8734 | 2024-09-27 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffc8f707-7455-365d-98dd-db3dcd80152a | -2.8047 | -50.275 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4e4c5275-57ee-3ff0-9875-3018865b9d91 | -2.80412 | -50.27863 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4fd03036-9fc7-3723-aaa0-27c58ac23b47 | -2.8028 | -49.58249 | 2024-09-27 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9bba5e09-8508-391b-aa9e-797542ddc16c | -2.80132 | -50.27448 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dec78bea-9e22-315e-95c2-1eb71136466b | -2.80004 | -50.27442 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e3b572f5-7cd5-3e1e-902c-b498d5225f3e | -2.79904 | -49.58556 | 2024-09-27 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 20a5455a-15fe-310c-ae69-c3452bcbfb53 | -3.43834 | -49.1364 | 2024-09-27 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6767376-3525-33ee-bed8-aedeb1d8dadd | -3.41268 | -49.2347 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5941d98b-caff-3262-87f1-de1645588288 | -3.39329 | -49.118 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6eb014da-af85-3a95-a276-4d46ff907736 | -3.30513 | -49.11482 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 42eeac1e-9794-3b43-aaab-5d102b1f16a3 | -3.30465 | -49.13942 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22bff6c1-ed86-3099-a01a-10ab3cf62111 | -3.291 | -49.50918 | 2024-09-27 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 23d76d08-2016-3e92-b6e7-c23255a5b7c1 | -3.29046 | -49.51262 | 2024-09-27 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5dd810c0-a1b7-38a2-80a3-397704a0de15 | -3.28768 | -49.50866 | 2024-09-27 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fec90db-9b0c-3772-ac42-0f96a6e7283c | -3.27871 | -49.11072 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b857d857-846c-3f4a-9688-38b11257e1b6 | -3.2754 | -49.1102 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 629c4319-c2cc-36f6-90ff-9fd1f2a75771 | -3.13475 | -49.20465 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccd72830-274d-3593-915b-b14cd86df9dd | -3.13144 | -49.20414 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78a4fe8b-17e5-35ee-92a2-e5d91b208983 | -3.12809 | -49.18243 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afc162a4-cd8f-3b90-9af2-bd16a5f7a8a6 | -3.11676 | -49.29733 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50537c37-e563-3b08-a83a-35ccb8b3637a | -3.08919 | -49.30014 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36e4b5c0-560d-3934-bcfc-5149ed2cb5c3 | -3.08865 | -49.30359 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74faf6af-3f92-3079-968f-474147d00871 | -2.57075 | -49.11199 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cc5f103-7306-360e-b715-b6b4a6f416a6 | -2.56908 | -49.10114 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eed38078-c383-34eb-99c0-7346d56393a9 | -2.56854 | -49.10458 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be902f74-b904-3409-bd58-a680a58ea91a | -2.56745 | -49.11148 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7dbb28d1-f705-3a26-9a07-5de2c9f527ae | -2.55698 | -49.11339 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06bb35d2-2df7-3e95-8ae2-665ca056cf25 | -2.55644 | -49.11684 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ef88a56-6393-3cfa-9041-13170c9734a5 | -2.48811 | -49.05315 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95216d0d-08c3-3050-9757-7402da40d3e6 | -2.48173 | -49.15818 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3607e31b-ed24-345c-80d8-84567b5fb6ba | -2.42671 | -48.94425 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5957eb8f-4cce-3022-9611-c00e29ee2575 | -2.42617 | -48.94769 | 2024-09-27 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 556a2cae-e7fc-3eaf-a151-993b3e6afdca | -3.4466 | -49.77351 | 2024-09-27 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f05f038-4995-344e-ad40-cad3dfceebec | -3.43615 | -50.25156 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fcccff6-86cf-39bb-9173-1703043db6b8 | -3.35072 | -49.77671 | 2024-09-27 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f554faf-100a-3f17-9814-aa88d5444897 | -3.35016 | -49.78022 | 2024-09-27 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d65657aa-b811-35dc-9cc0-92e54a529d37 | -3.34738 | -49.7762 | 2024-09-27 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42e3dc86-1de5-3bea-aedf-0841c57cfdd3 | -3.32175 | -50.3079 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d6d6eb1a-78b7-3014-82e0-c4fdcc5b033c | -3.32118 | -50.31152 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 3378b7bf-404d-391b-a492-8cca6df549f0 | -3.3178 | -50.311 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 347a10d9-3984-3cc5-8834-ab3c1cd79a5b | -3.31442 | -50.31049 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87b97c52-011a-3e2c-97af-305051b8dbe2 | -3.31385 | -50.3141 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8195f355-34f4-3848-bc35-1eab873b2b2a | -3.25012 | -50.47539 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f260f728-0991-34ed-9faf-a902e23ea1f6 | -3.24673 | -50.47486 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83d73ec4-2e18-38d8-9e52-6055671e1cc4 | -3.23559 | -50.01123 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da11603d-fe62-35f3-b0e3-8b8482177a66 | -3.23488 | -50.46184 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65b95027-b1d0-3866-8743-d22bf64bd51d | -3.23267 | -50.32361 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3ebf8cb2-f1ac-31f1-92a3-c1441c1d94d1 | -3.23148 | -50.46132 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd18011a-cbc3-34b6-98e5-b51fbe864ff0 | -3.22929 | -50.32308 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 15f57e90-9538-3312-ac75-74705b580c00 | -3.22799 | -50.32232 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eff08a5a-e49f-314c-9b3f-1dbb1bc59388 | -3.22518 | -50.31817 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52ffb9f7-57fd-3889-8418-b403a495be7c | -3.22461 | -50.32179 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ad7b5cfe-9f47-33f6-a8c4-cdee23285552 | -3.22404 | -50.32541 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e4f1ad28-4e3e-339d-93ce-e5fc7fe9d61c | -3.21228 | -50.45082 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5946af53-bc32-3f5d-8d98-f32ae8045e21 | -3.18185 | -50.28548 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d05591d-4331-393d-90fd-d2c4f8dd34f3 | -3.17452 | -50.28804 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0cce1bdb-2986-38ed-b493-0cea144ca1ba | -3.17407 | -50.24729 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9eaed35c-e687-3609-afc0-2899c5dfb3d6 | -3.17395 | -50.29166 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7cb79e1-09c8-33a6-876b-4a82fdcab4d7 | -3.17057 | -50.29113 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74741f81-6d23-3e34-baad-1c8a9f96e1ec | -3.17 | -50.29474 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5fb7f3a-b1ef-385c-96ef-cc211eb2c5b2 | -3.15087 | -50.28436 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 349d9661-cc6e-34cd-a139-b9319e41012d | -3.14806 | -50.28023 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 281718cb-4104-3ef3-9209-bfd1fe780bc1 | -3.14749 | -50.28384 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a1ccc41-44d9-3911-bccb-ca4978b34d93 | -3.14691 | -50.28745 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a67b211-2054-3298-a0bf-4a0ec0097661 | -3.14411 | -50.28331 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 57205de4-092f-31b5-8885-7866fe4f7def | -3.14353 | -50.28692 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16904f6a-3ba4-37ed-a1ee-632238fc7eac | -3.14073 | -50.28278 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca2118cf-92db-3465-bbd8-af7849d24a60 | -3.14015 | -50.2864 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b620f7b3-c0ca-32c4-9dfe-00be72964009 | -4.3338 | -50.64059 | 2024-09-27 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5110a684-3054-329c-8198-b502ecd720fd | -3.56771 | -50.57713 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2824c373-4411-33b3-a279-fc5fd276db95 | -3.56713 | -50.58078 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d690b7fc-bda1-3ce5-81ac-f4e66e133247 | -3.56432 | -50.57658 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ac62d583-3c93-32f0-b543-302956a104bd | -4.50026 | -50.10542 | 2024-09-27 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5fe0f7e-e46f-3568-9b8d-fc40258a6fce | -4.49971 | -50.10894 | 2024-09-27 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d43bd18c-9bb6-369e-b621-48e87af65ef6 | -4.27778 | -49.96257 | 2024-09-27 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4dcc20e1-96ee-368e-a991-4a4d820773aa | -4.06916 | -49.94734 | 2024-09-27 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdae93e9-2373-3a27-b76a-d86571e1afe6 | -4.06639 | -49.9433 | 2024-09-27 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 964ce29d-6591-3573-9180-e7857d0138aa | -4.06471 | -49.95385 | 2024-09-27 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1513809-5dd3-3094-b01f-1b9515ea5f8b | -3.95444 | -49.94029 | 2024-09-27 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e9e4649-49f1-365b-bfb4-ca3f4c86da91 | -5.16742 | -49.48062 | 2024-09-27 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12050efc-013c-38fd-953e-c16cc493746d | -5.16688 | -49.48406 | 2024-09-27 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30d0f12c-537e-3bed-a044-3e7fb58a8bb4 | -5.16412 | -49.48009 | 2024-09-27 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd39d4c7-c757-34a8-9895-b34ae5e35e6a | -5.16358 | -49.48354 | 2024-09-27 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README76.md)
