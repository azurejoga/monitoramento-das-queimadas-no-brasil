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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fbcffdd7-f380-36c0-9600-a1ac4f68a921 | -18.09575 | -57.3602 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| f8c252a0-a167-34d1-bf77-49105541fc60 | -18.09497 | -57.36389 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| f3e830b8-0345-3ed1-9458-6e1a5028b8fe | -18.0903 | -57.35892 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 0dc769af-d1a2-3267-8b3e-0888f708624e | -18.08953 | -57.36261 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9016b810-ed82-32e1-bd76-f332171acd9f | -18.08875 | -57.36631 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2967e8fe-6dc4-34be-b70e-d68bf787ade1 | -18.08489 | -57.27653 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ad95f4e2-0b95-37d2-8c1e-3443d27979dd | -18.08412 | -57.28018 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 40985aaa-681d-30db-b299-150017c0a065 | -18.08408 | -57.36133 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 58dc52ad-6c5c-3bab-bc6d-ccbd90964c94 | -18.08334 | -57.28384 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f86822f7-cc14-30e4-a05e-ea5ac63b8753 | -18.0833 | -57.36502 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6bbb58f5-6bcc-3949-b5bf-d9a1188d3765 | -18.08254 | -57.23398 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 36fba52f-4d1e-3b06-a78c-0c2977808cb9 | -18.08253 | -57.36872 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| ba313b6c-cbe8-3fd8-a417-fe248748bbd4 | -18.07947 | -57.27525 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 70a5a325-ebe4-3da0-9edb-c895af6d9024 | -18.07942 | -57.35636 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 407f9a6a-3eb6-352a-9d7f-f44639a4abd7 | -18.07868 | -57.22545 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 8205d8d6-aa43-33d6-8198-057f96e67b86 | -18.07791 | -57.22909 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 65fd3c10-163c-3269-b83b-01ad172f8cad | -18.07786 | -57.36373 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| bfd2d8e6-d246-31f8-a859-cc46e32d864f | -18.07708 | -57.36742 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 4031e302-3b17-3faf-a26d-426683dc77b4 | -18.0763 | -57.37112 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| d4d9473d-259b-35ac-8136-aea1a1e36363 | -18.07552 | -57.37482 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 3ba75fba-8f87-3a26-8b5e-3cb478c4665a | -18.07329 | -57.22418 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 17810d1c-858e-3425-9b33-5e054933a065 | -18.07252 | -57.22781 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 597034f7-d274-3c44-afe8-3ce3de529b8b | -18.07242 | -57.36243 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 13aac89c-9581-3ac5-96b1-ed91f38cbae7 | -18.07174 | -57.23143 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4169986b-dd7e-3806-adf8-0300ae401dea | -18.07164 | -57.36613 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 895c6e37-5955-30f7-9e92-cf04044334d5 | -18.07086 | -57.36983 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 37813924-4f67-36fa-aa6d-3d7c05657bd4 | -18.07007 | -57.37354 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 722d8770-5005-3e6f-af83-2337228f65dd | -18.06929 | -57.37726 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| edfc9eac-824c-38c1-b946-9e7944c8f252 | -18.06698 | -57.36115 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e4720cfc-fa6e-3e2c-b78a-e7c13daedadb | -18.06635 | -57.23016 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f4b85cc4-95c1-378f-89a5-2300cd2cc6cf | -18.0662 | -57.36484 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 8deebf96-a90d-35b0-9c11-69171b22960d | -18.06541 | -57.36855 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| c08065b8-a642-3036-9bd0-9335d4c5f7d8 | -18.06462 | -57.37226 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 1caa6be4-e765-3363-a2f7-0e4f6b81e60a | -18.06384 | -57.37597 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 0bb62de4-fef8-338c-8345-f09aed3f6c64 | -18.06095 | -57.22891 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5c4ebb1e-814f-32f2-b24e-cb14ec95dd13 | -18.06017 | -57.23253 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4292762d-7358-3c48-9840-5f9075471f26 | -18.05996 | -57.36727 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 18b03255-dc83-3d40-80c8-8afdcca2cad2 | -18.0576 | -57.3784 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 58592594-946f-3304-99aa-8ae3c17f8905 | -18.05294 | -57.37341 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b132518e-2960-36e1-b2bc-b42e3faa9ea9 | -18.05215 | -57.37712 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 733b3b21-b7f9-31a7-9460-a846d5fce6b7 | -18.05136 | -57.38083 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ac9e29bb-47b6-372b-b109-948f28da76e8 | -17.29221 | -57.30185 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 724c0a24-59f1-305b-8e99-1a079e494a92 | -17.2867 | -57.30057 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 97acac2b-6163-3cb6-9b3f-ebb85c09289a | -17.28039 | -57.30308 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c950d63f-04ff-305a-87ae-f23bf8d1cac6 | -17.27271 | -57.26518 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 757b13af-a444-340e-b307-3c6f94e4e5c9 | -17.27115 | -57.2653 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f755e871-3c06-3f93-94a1-4759c02c45a3 | -17.26721 | -57.2639 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 118f3cc4-623d-369e-a9cb-1c05ddd5fafb | -18.0264 | -57.33634 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 122f2e2b-0fbd-3b51-847e-ca75aa895618 | -17.26643 | -57.26767 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5955869f-a103-3b46-a2c2-c71fa2caf2d6 | -17.26565 | -57.26403 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ea762fd0-4375-3275-a394-085349166b5a | -17.26484 | -57.26779 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| fe0d6643-0c1e-3df5-ba66-76fafbe0046f | -17.2625 | -57.25884 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 394304e5-4a7e-30da-8507-c0174937f986 | -17.26094 | -57.26638 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7535d677-03ea-37ca-8b91-4d4a6534c005 | -17.23666 | -57.18983 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ba3075d4-5929-3cce-ac0a-600cc587b17d | -17.23587 | -57.19356 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 576a8b38-1af9-3d05-a2d1-bf3837dfc158 | -17.23509 | -57.1973 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 77574e5c-bf11-38b8-a26c-9a2316536450 | -17.2343 | -57.20105 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| da95e6e0-8db9-3899-9856-f8d855ad7fc6 | -17.23351 | -57.20481 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| aed0f180-b94c-36b3-8fa3-41630a086adf | -17.23196 | -57.18484 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3b988851-386f-32cc-b024-a3346a25ff70 | -17.22804 | -57.20351 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 096c90ad-df5d-3839-8d32-070e993ad468 | -17.22725 | -57.20726 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 21d6e693-ebda-3b8f-8580-2a6835262d6f | -17.22567 | -57.21477 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3315ec09-d120-3c5a-9e14-03ed9cead40c | -17.22488 | -57.21852 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1a8e8275-b7e4-37c4-bbe6-f99d2571f87f | -17.21782 | -57.22475 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8701262c-c04f-3504-bb6b-4bf88311eb3b | -17.21703 | -57.22851 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 17c9923e-2df3-30db-beba-767f1715ccbc | -17.21623 | -57.23226 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7b15579e-74cc-35bd-bb88-23790f2446a2 | -17.21544 | -57.23603 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3fef2710-f4ae-3db5-b256-383c9b27eb62 | -17.21465 | -57.23979 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c63573af-354f-355c-8886-61e70ce6b160 | -17.21147 | -57.25487 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 76c00802-5fe8-3486-b010-8a9db37b4f79 | -17.21067 | -57.25863 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f8686844-6d99-3cbc-976a-0a122b4f8c6f | -17.20748 | -57.27374 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f3d12904-bbd2-3d87-b3bd-340942f91735 | -17.20517 | -57.25736 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1b2c37bf-cc06-392b-ad9e-f9c5057a879e | -17.20278 | -57.26868 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 34947c09-73d4-36d9-b4c4-2eb2383b5a00 | -17.20198 | -57.27246 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 17325497-8552-3fc9-a918-36edef5817a1 | -17.20118 | -57.27624 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 52054c35-96d4-38f7-89bc-991e87c5144e | -17.18776 | -57.28504 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| eabc7a72-cac0-3288-a810-ff4ca353685a | -17.18695 | -57.28884 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| cd648925-522e-365d-8bde-dc18afd98a6b | -17.05574 | -57.39574 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 055b4604-9730-3aa9-ae3e-efd545ebebf5 | -17.05491 | -57.39961 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b03c4277-ab0f-3bd5-8aca-70bf4f106d44 | -17.05017 | -57.39446 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 5bbf1cde-2c48-384d-b77b-2b76bb404198 | -17.04935 | -57.39833 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 2abf7dac-bfaf-3f20-b83d-83177e2a9c91 | -17.04713 | -57.39546 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 39152cb3-03a4-3610-bef2-6fdac60fbe6a | -17.04634 | -57.39933 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c07a907e-7902-3e66-b240-f1c912f7465e | -16.99475 | -57.36697 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 779ac488-b041-3467-aeec-578c3e109860 | -16.99394 | -57.37084 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| d9cd5b96-3344-37a2-97cc-d20c9681b270 | -16.98594 | -57.38118 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 82fee00d-7cf1-3044-9bc1-ecab9a996647 | -16.98512 | -57.38504 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7113dfc8-2371-3950-8bbf-24773cbae9fd | -16.74695 | -56.67247 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 2cadf1dd-2a64-3ef4-a033-bc23fb28ede1 | -16.74592 | -56.66952 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ad27d351-b4bd-3041-923e-aef72499bb12 | -18.03565 | -57.31921 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d00b9808-bd7f-302b-80a2-f4e50ba18b46 | -18.03512 | -57.3497 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| d8e71d15-08e6-3d51-911b-0322ec0a7053 | -18.03413 | -57.32657 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8161ecfe-630a-30d4-9fa7-aaab955c11c0 | -18.03363 | -57.33 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 232658a8-4abd-3243-91d4-29f87bdd3f5c | -18.03336 | -57.33026 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5481a34d-e848-36be-a52c-f420f70ae5e5 | -18.03284 | -57.33367 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b26457f2-1150-32e8-81bc-bf299769a409 | -18.0326 | -57.33394 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 29a0ce43-1e10-3ee2-a821-f8f176aa7c1c | -18.03205 | -57.33735 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4feb5194-c1f6-3e07-aedb-fb63488f6f6b | -18.03184 | -57.33763 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3aa2c580-e8ab-330e-bb11-45b291ebabec | -18.03047 | -57.34472 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 767fbf1a-4ccd-3b7f-8115-3a8106128706 | -18.03031 | -57.34502 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |


[Clique aqui para ver as próximas entradas](README60.md)
