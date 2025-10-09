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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f3580e1-3401-3219-90ff-5d49226f38a9 | -18.02593 | -57.56608 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f00aa8d0-550b-3273-a6e2-86e0651ef907 | -17.82418 | -57.62262 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 917f6e04-02d4-39d6-9b92-951d0b36db91 | -17.90314 | -57.66128 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.3 |
| f679cb8f-2be2-3164-9121-f278022cd4d9 | -17.91071 | -57.50525 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.6 |
| f00ca04e-e250-3a1f-abde-5e1cbb17e77b | -17.89534 | -57.65902 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9dd12653-9bbd-3779-8b68-1f84a33f5f43 | -18.02672 | -57.56607 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a5df5316-14d6-369e-a487-f3f6e6a0ce4a | -18.02042 | -57.56837 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d43f86fd-23c4-3ed1-ae4d-c796893f94b1 | -15.99535 | -59.54717 | 2025-10-09 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f16d1d33-4882-3874-ab26-5fcb9c14efc0 | -18.24239 | -55.38086 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2a230424-8b46-3a4b-886d-1d0fe1e5bdd0 | -17.92406 | -57.52619 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 21665210-bb7b-3bde-bc10-96e2ebac2aa8 | -16.6053 | -58.15653 | 2025-10-09 05:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3a31d847-699a-30a6-906d-2dd3b7046b49 | -17.92061 | -57.5106 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9bd5b0d7-3917-3ceb-ba04-c0545fd678b6 | -18.02107 | -57.56277 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 350f8ca3-4d44-3d9f-94ba-3ce469b0ca57 | -17.91212 | -57.5036 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.6 |
| 57fc6335-0bf3-3994-88ad-0edec788fea2 | -15.99973 | -59.54799 | 2025-10-09 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8c214c4a-3a9a-3c77-9b10-63ceea55318a | -17.90048 | -57.65964 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 54d3e7d8-ab9e-3aee-b76e-26164ed04488 | -17.83197 | -57.64637 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 4029d74f-c1f4-38c6-89f3-ad3473aea99c | -18.02153 | -57.56551 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b8f9a02a-542f-3870-9684-727e0882393c | -18.03708 | -57.56718 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2fa4ca6f-97ef-3d65-bb39-e3f88fbf7454 | -18.0319 | -57.56664 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d7a632f6-ec21-31b4-b243-3e9ad9021c2c | -17.86061 | -57.57696 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| abd86572-1a60-34fb-a714-f1e4117b9e7b | -18.05404 | -57.55613 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6d002aaa-1d3a-39a2-ac84-4871f39de074 | -16.00026 | -59.54379 | 2025-10-09 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e2e0e1b-c2bd-3f3f-bcc6-96c8ac9e10a3 | -17.89836 | -57.65763 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 835931d0-c318-3ce7-83d0-4c0f7eebc651 | -17.82455 | -57.61935 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 49658c78-cc12-3752-94f9-9f18f1568a47 | -17.9648 | -57.50282 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 1dd3f38d-7e77-38fc-8e33-d2f45e38e393 | -17.82297 | -57.63366 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f39d2d4b-eb10-3b3d-9d36-36aab936be65 | -17.84893 | -57.58788 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c2ab9b4b-6a1e-365b-9dec-80529a2ba566 | -17.85763 | -57.64962 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6a8118a7-3c4b-3dda-bfde-f09e2db16434 | -16.60042 | -58.15588 | 2025-10-09 05:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a6c4f75d-17a5-3694-a621-7eb9981c8306 | -17.98476 | -57.51253 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5aa0aa03-41d8-3b27-8597-278d7bd2280e | -17.8285 | -57.63079 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d75cb717-2efe-3f91-b3ce-0bee96d3cc61 | -17.84239 | -57.64632 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f813e884-77d6-3427-9df3-fb9a6a87b316 | -17.92211 | -57.50848 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 97759a98-d939-343e-b8af-c5390022a65f | -17.84208 | -57.64906 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6ccc79b1-b257-33c2-9815-b4d5e59c2865 | -15.97835 | -59.54287 | 2025-10-09 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ea7e4f9-ebad-3551-9187-ef6149efa4a3 | -17.91158 | -57.49775 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 1f3967a2-36ed-34cf-b6ec-115f3755a788 | -16.01521 | -59.53199 | 2025-10-09 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d188714-84de-3cfd-97cf-c882808154d5 | -15.99484 | -59.55121 | 2025-10-09 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 102296f1-a311-31be-b720-1063ae301c32 | -17.84695 | -57.65198 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| bebb6333-c225-314d-b073-f69f8f8bc14c | -18.24192 | -55.38535 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7f538f8d-b77d-3794-9fdc-e83242bc476b | -18.00704 | -57.50174 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 94412b0c-2889-33ec-8fac-1e753b28c201 | -17.91689 | -57.50806 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 93563b22-b04c-3795-a5e2-de2b839ab1f6 | -17.82381 | -57.62597 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 39e3a32e-43ee-30d5-b0c2-0723c6f3a38e | -17.90596 | -57.6571 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 644a4029-4063-387e-ad00-65a8e4b73462 | -17.9035 | -57.65821 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 7a06e41a-ec2d-3c03-8db4-b4604df3440e | -17.9159 | -57.5059 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 0c0285a2-414d-33cf-ad16-f52a7399d8bf | -17.8249 | -57.61615 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| baec889b-ce6b-3746-b586-5904d3d478ff | -16.01964 | -59.53247 | 2025-10-09 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cee1ab71-c4d5-3a3c-b177-c095b71a6033 | -17.83688 | -57.64903 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 61f7903c-727c-30b6-a48c-bc434869663a | -17.83717 | -57.64639 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| f981588c-15da-3745-ac0c-513eeb024fd6 | -17.84278 | -57.59616 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5a9b9b37-b9d5-3350-a3e1-2c182993218d | -15.97335 | -59.54386 | 2025-10-09 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e27de75-9007-31b9-9e52-4df6975ef391 | -17.83139 | -57.6516 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 6d1f798f-46c8-3c70-833b-bd45022f29dd | -17.83167 | -57.64905 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| bddeac56-b25e-385f-ad13-b998cf8994fa | -17.84856 | -57.59119 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f5d1f184-5e94-3e3a-b49c-db4964625092 | -17.89466 | -57.66525 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 93973fe2-279b-3dd4-a0ad-965ec3b43d57 | -18.00217 | -57.49823 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cd275745-ba68-3834-b155-7d3a4698a81f | -18.01224 | -57.50232 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8052479e-2f1b-3d2d-9ac5-aac5e961c996 | -17.84784 | -57.59758 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a43230a2-7245-3bf8-b40d-d67b366f87d5 | -17.85474 | -57.58261 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 36703d2f-a87b-3d13-bf50-42bdbeb828ef | -18.06624 | -57.5408 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| b014b8f3-306c-3896-a178-b6ead1c8118e | -17.89288 | -57.66006 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8e5f9c70-03f8-36cc-b191-d2584a45a871 | -18.02843 | -57.55035 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| eb8fd483-187b-3703-990b-30fc39166b96 | -18.02184 | -57.5627 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9777dbca-22a3-39ab-9f34-27a244001fb7 | -17.97966 | -57.51111 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b9354b01-463f-3e91-95ae-85f5fec92c29 | -17.88739 | -57.66245 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| d7e1ebcc-275f-3171-bc66-cc4c5b6af86a | -18.06524 | -57.54988 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 333f11a5-2458-3599-b99d-6e892c9e215e | -18.0256 | -57.56895 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2b49c816-1fa3-3b4d-b821-37024a41301a | -18.0599 | -57.55062 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 694599d8-b6e4-3fa4-bede-9de7d99b9d37 | -18.02075 | -57.56554 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 671fb107-2c1e-3dd5-91f2-ba3d0819155c | -15.99923 | -59.55196 | 2025-10-09 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| abb7fd54-af15-30fc-acff-9592c79dd01c | -15.97383 | -59.53999 | 2025-10-09 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16e07d50-0abe-3fa3-b966-b96e9f302bff | -19.47009 | -55.48074 | 2025-10-09 05:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 0c3e4566-162d-3f1a-98d8-9d1ffad8cccd | -19.47053 | -55.47611 | 2025-10-09 05:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0fd4b62f-b356-385c-8997-6821da21c11f | -17.8311 | -57.6542 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| c7243031-8164-3d69-ac9e-f2e38e2e1e71 | -17.90014 | -57.66272 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| df4fb71c-1bc4-321d-a368-eca52df22a18 | -17.91114 | -57.50149 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| bf4f5def-021b-3897-9563-bbd547086508 | -17.895 | -57.66213 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 19fe38a2-8bf3-3f31-954f-851aead66681 | -17.88811 | -57.65623 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 6ca6ef4a-b61b-3219-bf6d-edea8890098e | -17.99773 | -57.49092 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e7d1045c-a253-30e6-a6a3-d208eecb94be | -15.97447 | -59.53827 | 2025-10-09 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea0d8d95-c19a-3ec7-aeb4-2aed1241765b | -15.97396 | -59.54214 | 2025-10-09 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a24e26ca-5a24-31a2-a799-cfda4df75e74 | -17.82586 | -57.65456 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 448a4ebc-b458-368c-9d8e-c8b05579d511 | -17.898 | -57.66072 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 371c032b-6e77-3e84-b7a4-d990ee33e203 | -8.93266 | -69.43333 | 2025-10-09 05:59:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e3e6edc5-4389-363f-944b-e5cfab6c308a | -9.45903 | -67.13208 | 2025-10-09 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee03d0b1-e91f-3de3-9af3-d3a1adb04674 | -9.80474 | -64.48751 | 2025-10-09 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76c5a0b7-2982-313c-a5e3-0b25fd78d098 | -9.80397 | -64.48463 | 2025-10-09 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d9b8e24-b2aa-3a3e-9b98-eb3494574e94 | -9.29997 | -68.24904 | 2025-10-09 05:59:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94d20f87-06c7-3667-b5e7-7846f95dd98f | -9.38021 | -67.44188 | 2025-10-09 05:59:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41507196-83e1-37ed-821e-350c3fc8aa28 | -9.86547 | -65.1715 | 2025-10-09 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd713e9e-bcbe-396f-8173-7ff1e84c1555 | -8.42731 | -70.12565 | 2025-10-09 05:59:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 989bb044-5101-3580-8fba-39317bf79119 | -9.22254 | -67.16644 | 2025-10-09 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbab3b5f-ae48-39dc-91e2-9cb36fd962e9 | -9.18899 | -67.83315 | 2025-10-09 05:59:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03dd80f0-5cbd-3893-8276-b0fac44fd0ff | -9.37075 | -66.59828 | 2025-10-09 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a45174de-762d-357b-9591-f6a6b7c110f4 | -8.72489 | -69.87325 | 2025-10-09 05:59:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14773947-01e7-3d5c-9a4d-5c5cada31f1d | -10.83194 | -68.27427 | 2025-10-09 06:01:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0a04f0ba-57eb-3560-b3b2-fb2c6ce1eadf | -10.43305 | -69.22485 | 2025-10-09 06:01:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 11540538-9c95-3e84-bd38-f73ddd5fd9cc | -11.78484 | -63.18553 | 2025-10-09 06:01:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README61.md)
