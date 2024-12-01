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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 094b5572-3f4d-3978-8813-162548690fe7 | -1.71914 | -55.02684 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3f343fa4-21ca-3167-b218-fca7bd4a12cd | -3.09252 | -54.0204 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a07db6c-ace6-3cbe-8b87-e623d3cf5256 | -3.47816 | -50.44203 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef2f1388-2963-3a02-8b8c-5ae58c61bea9 | -2.36018 | -53.6535 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 887d27db-abd1-3174-b05e-6a46f461252e | -6.76247 | -46.52603 | 2024-12-01 04:44:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 061a816f-3ac0-31af-8003-ab5f7671e80c | -2.60352 | -54.252 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b091dde0-cf60-35da-8a08-c64b85890eee | -2.32547 | -50.66888 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3deea660-aa51-3811-804b-efa1b9bd2ec8 | -4.54056 | -45.70164 | 2024-12-01 04:44:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| b547d7a9-9e86-3aab-9470-9bc8798466a1 | -1.63882 | -53.86281 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf526e58-04dc-3b5d-942c-d0903e3f47c8 | -3.93431 | -48.14071 | 2024-12-01 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 56956af4-989b-34ac-a72a-97ba2c51e294 | -4.02824 | -49.12702 | 2024-12-01 04:44:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc594190-e970-3960-87c7-2ff1ffde97d0 | -2.94471 | -51.50438 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3c377ea-7566-31c5-88ba-5be4af7c43da | -5.66513 | -49.75699 | 2024-12-01 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb9e197c-8e53-38be-802e-54047d680991 | -4.1149 | -54.40976 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 453201e5-70ad-393f-964c-f68631eca551 | -3.24751 | -50.61488 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a219043e-712b-39bc-8915-032f61f7ba9b | -1.72321 | -55.0275 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 304e88c0-aee8-3169-bf07-c1486e2091fb | -3.28114 | -50.55286 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b392730-07a9-3925-b8d7-de79af69978e | -2.69293 | -51.99316 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ce2e2b6-41c4-3c9e-8e82-776e92bae6a2 | -4.01377 | -49.93822 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9317b426-d0be-37fb-b81e-389cd89d210c | -3.9967 | -44.75528 | 2024-12-01 04:44:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5dd1a8e9-aa2b-3283-a175-5814b99314f2 | -1.15691 | -51.70091 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ecc77661-0a40-3b9b-abf2-0c5ae2692464 | -1.29274 | -51.72531 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a88e3c95-f7f9-362c-b2d9-b5779d7e5621 | -4.62171 | -48.03024 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec062034-4bec-3136-832a-16977585be91 | -3.49436 | -53.83272 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b6b8bae-1d4f-3f9f-a43b-0af22f3e0237 | -2.37083 | -50.40285 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b358b2e9-682b-37c0-afa2-0436a0891b3c | -2.36709 | -53.68156 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf86c5df-9164-3dc4-bf03-b95cbda1daa5 | -3.08949 | -54.01531 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e885ba5a-569b-35b7-879a-dc156743c28d | -3.99267 | -46.65038 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8a4e106-1a5f-3851-bf4f-5646364a75d6 | -4.31301 | -48.21125 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b8ff619-7eb8-3ee4-a6a8-3b80260af62c | -3.0927 | -53.1357 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27692da1-bfd1-315f-863f-f8b5eba81d13 | -3.21328 | -50.27356 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01b0b64a-4a1c-30c1-b1f7-c8bc92e4df73 | -1.03866 | -51.73996 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9c3cf27d-4015-3fa4-b85d-99789eeb070f | -3.5047 | -53.839 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 5cdf6aec-6b43-3515-8e31-0b6e937daa56 | -3.49732 | -53.83775 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b7a32e37-3f3a-3175-9191-caa78cc37cb9 | -1.65967 | -53.7567 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1b1b9fe2-426e-3ead-9142-2c4408d0f226 | -2.00699 | -51.18338 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ed4fab6-298d-33dc-8cae-ec99acaec307 | -3.74498 | -53.39167 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd591079-96d5-3e91-b256-e12944c8c35a | -3.13564 | -45.9778 | 2024-12-01 04:44:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 382ea38a-1208-3658-a3f2-3edd0830c990 | -0.17045 | -51.35828 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 368fdeea-1d90-3187-8369-fc8ebef6400d | -1.28287 | -47.9035 | 2024-12-01 04:44:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b9aa65e6-00c3-3abf-9f81-4ca9567b52c4 | -3.29397 | -53.67306 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4351b2f-24a3-3e72-91d6-9fab9fe351c5 | -3.26072 | -53.64557 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5ef81da4-e2b6-3c8c-a962-3f98f8205fb0 | -1.16574 | -51.93594 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79fa46e0-51ed-3a5b-9c05-9597394a5f78 | -3.44698 | -49.99164 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d3073b5-86db-399d-aadb-39a388b3eaea | -2.98541 | -53.35935 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 64e75b62-b926-3f8c-9d43-3089607fc713 | -2.87488 | -46.80292 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7832fb9-485d-3da7-ab66-cab69c0ef0c4 | -6.91748 | -43.54169 | 2024-12-01 04:44:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ca644392-5bb4-3e2b-8ad8-19871036a5bf | -2.58437 | -49.22026 | 2024-12-01 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19913e35-a4f4-3998-aa18-3382ae1155d0 | -2.9851 | -45.57547 | 2024-12-01 04:44:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| fb0e3aaf-18a5-38a8-91e9-055429f3e8ca | -3.74883 | -52.26524 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4ce4f5b-44ec-308c-a280-3f34b8d343a5 | -4.9525 | -47.8024 | 2024-12-01 04:44:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0ea42d0-1623-3585-87da-75deb1871759 | -3.28446 | -50.55338 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 69b6be6b-d8b0-3fc4-9630-f32bd38f2516 | -2.53027 | -53.98779 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c58110e7-0294-3ee2-980e-06c11b550388 | -2.8348 | -54.03833 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 783e3e2a-3395-306a-a510-c341e0174ee6 | -3.25907 | -50.04745 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bcf44c20-d58a-31e0-8a83-738e4cdaecd3 | -3.29697 | -53.67788 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f39bd597-45b5-3ae7-9697-aba35039c95c | -3.09361 | -50.34692 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4442c61f-6c12-3f4b-85eb-0fc43fd11e12 | -2.98982 | -45.57106 | 2024-12-01 04:44:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb368ba8-66c6-3767-bd40-4acee9c8cf18 | -4.35906 | -48.70232 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8922ea3b-d78b-362e-aeaf-a4c1ec25d837 | -2.78567 | -51.6703 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 452dca49-4278-38b8-8dd4-8cfa05c1252d | -3.1181 | -51.30932 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fa536e3-df3f-36de-aafa-283e36570478 | -4.34067 | -50.76515 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ded43de-76a2-3769-ad6f-c5e066af7d8f | -3.30369 | -50.49623 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afb6fa4d-2bf0-350b-be12-e88f239672dc | -1.74407 | -52.65643 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 636714ba-c467-31b0-ba00-151abeecbd93 | -2.62856 | -54.21804 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5b071f6-768c-3388-a59e-5ff23c4ca12e | -1.25065 | -51.79105 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7687b03-18dc-3a18-ba7d-bf38d83e946d | -3.50745 | -62.75315 | 2024-12-01 04:44:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8367f42e-498e-3d1c-99ee-5e473e8fa9e8 | -1.01232 | -51.72822 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 5d3410b9-66e7-32bd-8754-49011db0b667 | -1.00948 | -51.72395 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2af4638b-bff3-3ef1-b0e8-e216eea01f21 | -3.2401 | -53.63356 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee8d8c24-1d79-3a43-8377-b545f23f04d7 | -2.79682 | -53.04615 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63243f3a-81ca-320d-be5c-b58d53c86d50 | -1.21464 | -51.73655 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 39cf774d-589f-36bd-bdd0-40d2a0768657 | -3.1306 | -54.53341 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 55836270-5dab-3906-8644-0bf05462d837 | -2.1976 | -50.57802 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc7d281d-2cc1-3a0c-b001-9988ca88d9a4 | -2.86502 | -53.32062 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65e42488-7dde-3c96-912f-28ce898cfac9 | -0.00369 | -51.19786 | 2024-12-01 04:44:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d478440e-6d96-3e3c-b60f-a63b5b62ee0e | -4.3171 | -48.20787 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bd31e16-17e3-3191-bb7f-352eb3838d98 | -1.18935 | -51.76307 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ed3a960-c71f-33d4-b914-55f77dfe5ff0 | -3.03793 | -54.04842 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9637eaf-ce9e-3145-9204-e6940df6286c | -2.27037 | -53.46753 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd4838c3-cc1d-30c1-83cf-867d165c49dc | -3.5239 | -51.13537 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a143a20e-3c28-32c8-97cd-d8388fb4c813 | -3.82398 | -46.59258 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77d054f5-2e59-3856-aa18-936ba9251c52 | -2.98708 | -53.27912 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ae27286-7f97-32d2-8b53-303cc474579f | -3.0972 | -53.29152 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 336fc89d-0708-314c-a1eb-6e33b6095725 | -1.72821 | -46.22533 | 2024-12-01 04:44:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7da2e2a1-5267-3d5f-ae02-f3230ea0b129 | -2.62934 | -51.77626 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff0378cd-2246-3971-ad5a-828fbb95db03 | -3.28497 | -50.20701 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53628137-4f22-3aad-beb6-abd087424e2c | -4.552 | -43.29779 | 2024-12-01 04:44:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 42dca180-3b29-30a5-a15e-07e20e4af97f | -3.35756 | -43.1698 | 2024-12-01 04:44:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d9454b9-a09a-3358-9d7e-f42976d6cdbd | -1.00242 | -51.73124 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ede426ee-b5df-3ea9-94b5-be37cf770024 | -0.83529 | -51.81231 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 27d4e83e-4b0b-3809-97c3-8ec6d62497ce | -2.27981 | -50.56936 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 519678de-973d-3ae3-8497-ff467c9f68a6 | -5.5828 | -43.61077 | 2024-12-01 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43ec6e2d-b384-31a3-a7cd-029b293b61c1 | -2.87289 | -53.99345 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 502b3c29-c663-3474-97e1-b6b97211cf08 | -3.33281 | -53.54268 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5f870ca8-9f0c-3090-a02d-f360e9eb6a86 | -2.58037 | -53.67619 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 17431454-dc03-3a77-91f3-27853f39a32d | -2.96677 | -53.89271 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee959bb4-f2f9-3656-8122-f2884558a974 | -4.13458 | -49.36187 | 2024-12-01 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 58b00350-4f2c-3960-b2d5-e13dbb312a0d | -3.69458 | -51.33785 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb467bab-2a48-3348-852d-d329d630ae31 | -3.09179 | -53.71731 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README69.md)
