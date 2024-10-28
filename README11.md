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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 386aa2ef-df9d-3943-a65c-7f76bdb80f17 | -4.72276 | -45.80408 | 2024-10-28 00:50:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8908fada-7957-31f0-8251-ca4a8df5a9f0 | -4.71238 | -45.79277 | 2024-10-28 00:50:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c4172a35-81c1-36d3-ad06-4454c317c504 | -4.69824 | -45.88986 | 2024-10-28 00:50:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 343fa830-b30b-3951-824c-ed9d32ebf98a | -4.69694 | -45.88062 | 2024-10-28 00:50:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a8e3b905-7a4f-3d61-aa28-c95245a1a88b | -4.6892 | -45.89127 | 2024-10-28 00:50:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8171c82d-4b8a-318d-a9b0-8277a2ad8724 | -4.67786 | -46.65814 | 2024-10-28 00:50:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 49e48ade-d09c-31ab-a7e3-bbeed887f51f | -4.6503 | -44.66749 | 2024-10-28 00:50:00 | TERRA_M-M | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c83f488f-4179-3b35-99ed-0815bfe4ffea | -4.56703 | -45.80978 | 2024-10-28 00:50:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 76cc5ceb-cba8-3f56-8753-448bdb314be2 | -4.5657 | -45.80043 | 2024-10-28 00:50:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 79310026-a61f-3832-b769-e7a0d947b0f4 | -4.55662 | -45.80182 | 2024-10-28 00:50:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 38.3 |
| ab49311f-fab5-3931-a05f-ed3cb1bf5629 | -4.55527 | -45.79239 | 2024-10-28 00:50:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 76a38b01-7034-3eda-88d5-5c633933aff3 | -4.54979 | -46.60684 | 2024-10-28 00:50:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ef253c40-cd3c-32b0-b292-7523021b0b9d | -4.54905 | -45.94245 | 2024-10-28 00:50:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 98c49cd2-2eb1-350b-adde-b4516e8c2b3f | -4.54775 | -45.93311 | 2024-10-28 00:50:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 0040235b-30e1-38f5-a18a-e0f2b6033d38 | -4.54753 | -45.8032 | 2024-10-28 00:50:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9f5b29c2-b51a-3eb6-8033-c7ac42fedb10 | -4.54215 | -46.617 | 2024-10-28 00:50:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dc0605f7-9482-365a-8f72-4e8e3c9fb513 | -4.5409 | -46.60808 | 2024-10-28 00:50:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 35.7 |
| ec5d63db-4149-3936-b319-9327b62adbd7 | -4.52086 | -46.46464 | 2024-10-28 00:50:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 4a109743-e670-33ec-9d8c-768eea127bbc | -4.5196 | -46.45566 | 2024-10-28 00:50:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d51d533a-26a3-3c9b-86d9-a4d6cbba4528 | -4.48461 | -48.12334 | 2024-10-28 00:50:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 1764d569-31c7-3367-806a-9f24c5e4ad16 | -4.48336 | -48.11438 | 2024-10-28 00:50:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 374f1652-c743-365e-a531-12e4b128a53a | -4.47438 | -45.67566 | 2024-10-28 00:50:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| f5aae4bd-3347-3afa-adfc-75c598900a5d | -4.47362 | -50.99367 | 2024-10-28 00:50:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 83ae2528-e80e-3a75-a084-5df18960a4a9 | -4.4655 | -45.74453 | 2024-10-28 00:50:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 854811d2-c08d-327c-a89d-1a893156ff45 | -4.42453 | -45.65374 | 2024-10-28 00:50:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 49.2 |
| c8d0ddd2-c812-3985-8c7c-561e19ab1eef | -4.42318 | -45.64433 | 2024-10-28 00:50:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 97118523-a4ec-3ff8-a9d6-66223993fafb | -4.41626 | -45.65114 | 2024-10-28 00:50:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 355.2 |
| e987a50d-4353-36bf-a07b-bd72400b4d09 | -4.41493 | -45.64161 | 2024-10-28 00:50:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 2d6e187e-fd7b-36dc-af75-8ed36a98c25b | -4.4144 | -45.96793 | 2024-10-28 00:50:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 69027774-ec1c-3ca6-bbe7-341b33d4f0ec | -4.41293 | -45.8921 | 2024-10-28 00:50:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d12b5725-fce5-3a8e-a523-3c10e5472ab0 | -4.40886 | -48.24063 | 2024-10-28 00:50:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 49c8fb5a-cb7b-359a-92b3-d0d126e72eca | -4.35058 | -48.14803 | 2024-10-28 00:50:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b0df7923-4147-3eb0-8bbf-9ef0abda3dd9 | -4.34413 | -48.63619 | 2024-10-28 00:50:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 39fd4189-f20a-3ebf-97ef-97ce17dd8e33 | -4.33512 | -48.63749 | 2024-10-28 00:50:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d4d35572-8c77-385a-b98b-5ce59ff70355 | -4.33458 | -50.57292 | 2024-10-28 00:50:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| eb8a60b5-d9d1-390e-9276-a623dd2c29b6 | -4.32439 | -45.78643 | 2024-10-28 00:50:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 767e453f-8aa9-3a82-ba8b-8fcc140a086d | -4.32306 | -45.77702 | 2024-10-28 00:50:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 469b6052-5552-3958-b1f0-9cdc71797c25 | -4.31813 | -45.87386 | 2024-10-28 00:50:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 58e3bb94-3f67-3cbc-bb26-31bd3b427284 | -4.31679 | -45.86442 | 2024-10-28 00:50:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9f999382-ec9c-3eac-878d-c661ef6f2098 | -4.30031 | -48.65182 | 2024-10-28 00:50:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8564c3d2-5e6d-3bf7-bf3a-4c9eb42be5c9 | -4.29527 | -48.61498 | 2024-10-28 00:50:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| eff440af-cfab-32e1-9bae-47be3a4509c3 | -4.29128 | -48.65309 | 2024-10-28 00:50:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7494f306-45e0-3180-a5f0-06ae09d4de85 | -4.29003 | -48.64387 | 2024-10-28 00:50:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e9c56e6c-a045-3847-86b9-7873f82cd323 | -4.28025 | -45.53969 | 2024-10-28 00:50:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 27094c17-3e6e-31e0-aff7-a56d96562879 | -4.27889 | -45.53 | 2024-10-28 00:50:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 164.6 |
| 5ed5b9e8-dfe1-32aa-afa9-9e6e548685c5 | -4.26966 | -45.53133 | 2024-10-28 00:50:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 0872d10a-4eea-3183-99a2-3ce8db34176a | -4.24066 | -48.55374 | 2024-10-28 00:50:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6de15b0e-d74d-3e82-81c2-e02d809c9d86 | -4.23888 | -46.87832 | 2024-10-28 00:50:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| b61d71c0-5d15-39da-801e-c5ada7b918f3 | -4.23764 | -46.86949 | 2024-10-28 00:50:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 319367eb-d895-39e2-882c-65c36fb4ef60 | -4.23612 | -45.74718 | 2024-10-28 00:50:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 31626fc6-4d51-3805-83a4-5c026f7ab33a | -4.23479 | -45.7377 | 2024-10-28 00:50:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 0530ce5e-aaa2-33d6-8934-373a5d72d0ad | -4.22394 | -48.56542 | 2024-10-28 00:50:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 699777a0-f893-31eb-b2fc-dcf15180f213 | -4.20571 | -53.46688 | 2024-10-28 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| b654864f-6eaa-3699-867a-d875ef411316 | -4.20399 | -53.47264 | 2024-10-28 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| feb6c6d7-960b-3cc4-832f-9c849e28d70b | -4.18738 | -46.38363 | 2024-10-28 00:50:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 231dd1e6-78e9-372e-9ad3-e6d99bcc0f66 | -4.17971 | -46.39397 | 2024-10-28 00:50:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b90e521d-f8bb-3e4b-8aac-1453c13f0213 | -4.17843 | -46.38494 | 2024-10-28 00:50:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 14e7ab95-7c08-3b81-8df5-36dcfc37c072 | -4.16981 | -44.11462 | 2024-10-28 00:50:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| f67a1440-ef04-3eab-98f2-3646b18a13a1 | -4.16816 | -44.10311 | 2024-10-28 00:50:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 4e344857-3de7-3709-9775-30d1001f179d | -4.13495 | -46.40617 | 2024-10-28 00:50:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a0e6d1ee-81c8-3d98-b300-e86be7a3707e | -4.12945 | -46.89716 | 2024-10-28 00:50:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d1f0977b-50fb-3ae8-a4c6-9bdbde4b0c35 | -4.12669 | -47.32943 | 2024-10-28 00:50:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 4f8f23a0-8fe0-3986-a03a-e0fa692a591f | -4.12546 | -47.32063 | 2024-10-28 00:50:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 38bdb5ae-cb3e-3d80-b9af-20a82d79f0f4 | -4.12184 | -50.51037 | 2024-10-28 00:50:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fa0bcea6-5f23-30cd-92e3-79db4a3482d3 | -4.11671 | -49.26234 | 2024-10-28 00:50:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 40dd3ad4-ecb4-33b5-8919-b8570790e287 | -4.10637 | -48.51382 | 2024-10-28 00:50:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c9afadc1-2046-3948-94e3-33b7c8e2604f | -4.10511 | -48.50467 | 2024-10-28 00:50:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c3298c80-4055-3bf7-b62d-0cfe5f65c5a5 | -4.10075 | -46.75616 | 2024-10-28 00:50:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bc9f2b22-dfbc-34cc-8421-5f5722f0d4bf | -4.0995 | -46.74728 | 2024-10-28 00:50:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8369ee34-e607-3251-b7f4-d14dbc38e00b | -4.09739 | -48.51505 | 2024-10-28 00:50:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 55b854f7-6669-3ce1-a29b-15abe6618a9d | -4.09614 | -48.50594 | 2024-10-28 00:50:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7c3e2af2-3299-3bb2-94bd-bd07b1ba9dc9 | -4.07747 | -44.61915 | 2024-10-28 00:50:00 | TERRA_M-M | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0f405f0a-75ec-3257-a592-435034a1a2ca | -4.06757 | -48.29791 | 2024-10-28 00:50:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 55f1ea97-a719-30e4-b563-4ec5a7af1646 | -4.0663 | -50.0305 | 2024-10-28 00:50:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| bd06551a-a4b6-3bef-9f5e-c1f12675f0f9 | -4.06486 | -50.01999 | 2024-10-28 00:50:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 99135bcf-f7c9-3576-af7f-c1e5d315b82f | -4.05936 | -46.25928 | 2024-10-28 00:50:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 096ea9cb-4ec7-3657-99da-c605c687f3fb | -4.04254 | -53.42514 | 2024-10-28 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 08115be0-2f5e-3477-98f5-e4b223c5fdda | -4.00558 | -46.9929 | 2024-10-28 00:50:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9e24caf2-0ece-39f6-aadd-e723ebde6960 | -4.00434 | -46.98404 | 2024-10-28 00:50:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| ef1a50d7-8559-33b6-9e4f-a9b36b81692d | -3.99047 | -46.4885 | 2024-10-28 00:50:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 77505f73-3725-3d9c-92d8-59ceb18994aa | -3.98919 | -46.47947 | 2024-10-28 00:50:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 086e7187-6aec-39e1-a169-7b60505fcbbe | -3.96974 | -46.21305 | 2024-10-28 00:50:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 121905bd-7ef4-3932-9e9a-db4eaa78ab55 | -3.961 | -52.20912 | 2024-10-28 00:50:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 6f883664-fba8-3b1b-9a6d-f17b79966776 | -3.96073 | -46.21432 | 2024-10-28 00:50:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3ca0b0f3-efca-3d76-a7ec-52c0f06f8310 | -3.95983 | -46.40665 | 2024-10-28 00:50:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ac9437c2-9d12-34a6-b9d5-39929e38bb9f | -3.95216 | -46.41708 | 2024-10-28 00:50:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 565d0bda-13d7-35df-a353-f7e1d2e02834 | -3.95088 | -46.40794 | 2024-10-28 00:50:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 56ac25cb-036c-3556-93cf-7b29ea5c74e9 | -3.93804 | -48.36499 | 2024-10-28 00:50:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 90c8f9d0-e332-30fc-9fd6-f08af1f08cb0 | -3.93622 | -49.89533 | 2024-10-28 00:50:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| cd8012db-483c-3fa5-b8ac-7e13bf6ddc61 | -3.93553 | -48.34693 | 2024-10-28 00:50:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| fbc0f6ea-77a9-3116-b398-23da7644763c | -3.93482 | -49.88507 | 2024-10-28 00:50:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4a0608fc-4a80-3474-967e-294c49895110 | -3.92731 | -45.84879 | 2024-10-28 00:50:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b7fc9cb2-3b02-3d3d-89cb-3225d5d0d8d3 | -3.92713 | -52.12511 | 2024-10-28 00:50:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 15da9903-0a6f-34d7-9e8b-89186c1f41f1 | -3.92708 | -52.13142 | 2024-10-28 00:50:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 7874c66c-53c4-3d3f-b573-f916e2142a31 | -3.92661 | -48.34818 | 2024-10-28 00:50:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e06da867-a542-36fd-a42c-88d57108a0f3 | -3.92597 | -45.83934 | 2024-10-28 00:50:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 4629935d-c7a4-3678-87de-bc8c0dd53ed2 | -3.92508 | -52.117 | 2024-10-28 00:50:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| a27697e3-fd8a-32da-9a75-8a5d94049143 | -3.91125 | -48.36874 | 2024-10-28 00:50:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f4de029f-8a4d-33f4-803a-cea3dac230a1 | -3.91124 | -46.45066 | 2024-10-28 00:50:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 1cce35e4-47ed-3966-a89c-3ecb6ca833a7 | -3.90996 | -46.44162 | 2024-10-28 00:50:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README12.md)
