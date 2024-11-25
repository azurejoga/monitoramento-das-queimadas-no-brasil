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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c716e8f0-80c0-3f94-9d73-8288db81530a | -2.57187 | -53.97137 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e2059c4-a6a8-3fff-a53d-c709f9ac6d8e | -1.6425 | -52.41681 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9cac38ae-fce2-3264-9c3e-179e7698f747 | -1.60315 | -52.58093 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4e64ab95-1ee6-32b1-978d-5dd22a361ec2 | -3.09134 | -51.32383 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a12b587b-3de1-36c9-8ced-0b7205ca7454 | -2.47717 | -54.05689 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37f45196-b8d5-3c1b-9ec7-2ae2a0ac264d | -3.49448 | -51.46797 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43277e34-481e-39f1-ab8e-1a6a2d319893 | -2.04263 | -51.17028 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c793087f-b7c0-3247-b92e-9716849a3f16 | -2.80783 | -46.81236 | 2024-11-25 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69e47211-40a0-3a4b-97ac-afab777246b5 | 1.855 | -55.90186 | 2024-11-25 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 809498e9-bb29-3a87-9946-2beb049ed1c8 | -3.93496 | -48.15073 | 2024-11-25 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7da810ba-2517-3642-b2b1-e94c40283415 | -2.96841 | -53.88391 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64d7a11e-3aad-39a1-9d6b-ed5f404e92b6 | 1.85366 | -55.89302 | 2024-11-25 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af5eaf77-0a40-3b97-a42f-53d5b91d0b4f | -0.99255 | -51.72896 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ca1c365-437d-3129-9676-ee77865750a4 | -2.16359 | -53.7756 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 827618ed-6c08-34da-9931-c823c229967c | -2.62659 | -51.77085 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35a98b05-5096-3f30-b30f-427598245495 | -0.80015 | -51.59742 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c361e37-04f2-3da9-a244-33c631308e1e | 0.33187 | -49.71857 | 2024-11-25 04:55:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1a191f3-087b-3b6f-a077-80c387529e15 | -2.83216 | -54.01896 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b627fbc3-15d7-3813-a5a2-411dfebc0abc | -3.25456 | -53.27043 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e893566-cc0d-34d0-b893-f7cc4b975ca4 | -3.81278 | -51.99959 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 322707f9-be41-371c-bbf1-bd33a21315c1 | -3.105 | -53.98713 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72c9c6e8-206b-399a-a216-3db8c8857f2f | -3.0825 | -53.28966 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03227d78-59a7-3c12-92fd-69481220c239 | 0.94744 | -50.73711 | 2024-11-25 04:55:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ec65db3-bf57-3f97-bc4f-99c16605eae4 | -4.25848 | -48.66961 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7875e2e5-f9f3-34e9-bfc4-a64669872e1a | -1.77001 | -53.6286 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a0c776ae-3dc9-3330-add8-f168bfe6c006 | -2.83938 | -54.01652 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c0c4bbe-3497-3dba-9911-61d6fcf7b81f | -2.21922 | -53.61381 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 383961e8-c5c5-35f4-a6a2-cc8e981656b0 | -3.4224 | -53.28242 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 59611904-d0d9-3597-af2a-fe407a11fb65 | -2.56436 | -53.9595 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae2b417a-91e9-308c-bdd6-6b14e05e1257 | -4.14039 | -48.7644 | 2024-11-25 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 999f9aeb-3ede-3481-81dc-c0357e928647 | -1.36172 | -51.37483 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 20a7ba04-5526-3801-a358-25293b9278b0 | -3.50345 | -53.81872 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59250ca8-e2cf-38a0-a630-be7dd355ef6e | -2.74975 | -54.07045 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d40fef8-cafb-30fa-8586-0830abe2242d | -1.64781 | -53.86614 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a837cd8a-1b87-337b-9c8c-679c204fc2e0 | -3.52219 | -53.78623 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dad95de6-b9f8-3162-be2b-be56b03ec739 | -1.92585 | -53.34816 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22be82ab-a681-386b-9221-7d5391b886c8 | -1.13202 | -53.6179 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac4ee5e4-f391-3778-b16a-d5224b3c0a51 | -0.28093 | -51.6081 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c8c7de6e-2946-32f0-b80a-3bf3a165b4a6 | -0.32687 | -52.00613 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f1c1ac5-75e0-398e-9562-79cc95622d1c | -3.5329 | -54.07893 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca9060ea-fc95-323f-b988-b6338587f2a2 | -3.10779 | -53.75311 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 186a2fc6-9f99-3509-bd14-7ec75b91d17c | -4.05814 | -50.97598 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b90e114d-7189-3cc9-97aa-73ac2bb74279 | -4.66329 | -49.38923 | 2024-11-25 04:55:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e204f598-6121-345b-aae8-20ef1c15a0f4 | -1.19167 | -51.77382 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d40470d7-07f6-3ae1-9799-db09c3ead305 | -2.82882 | -54.01844 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fae14ac9-2b87-32fb-8537-70f072a1b24e | -2.35836 | -53.80582 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38a4798b-07e3-32b3-959d-cb29048bb71f | -1.63745 | -55.13989 | 2024-11-25 04:55:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c0e0e7b-e0a4-3360-87ac-460310491f76 | -2.70356 | -51.995 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e202d479-08ea-3304-a59a-b3ac55ea6013 | 0.97007 | -50.13081 | 2024-11-25 04:55:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 949c491c-de63-3d18-8791-12f7c4698d5a | -1.96949 | -53.13612 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd5f34b3-7d65-3930-8062-b43fb9463eb7 | -1.23808 | -51.74115 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 289f2702-2d3f-3fef-b812-ac2701bd957a | -1.73617 | -52.7931 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abea45ad-47b4-349c-95c8-2262789944dc | -3.28671 | -53.84114 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fca49279-001e-366d-83f3-bbaac2f06858 | -0.39339 | -51.45115 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd3beb9f-98c4-3355-8077-7fd9990df924 | -3.50673 | -53.79796 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00511e17-f001-33ca-9cff-e43bfa529fa2 | -3.1602 | -45.47718 | 2024-11-25 04:55:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6517b1dd-edc7-3f4e-81c2-e99f9ddba92f | 0.6315 | -50.57051 | 2024-11-25 04:55:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c08de03e-24a2-318e-9eeb-cd8b518f8879 | -0.9738 | -52.79716 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d012e953-35c3-3b72-8a70-6a5201815ce1 | -2.96891 | -53.85913 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 547f31f6-74d6-3baf-9eb2-e906eff5fb4d | -2.73804 | -54.37453 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1bc344e-4c1e-31dc-8a11-56cd3a4e0868 | -2.89851 | -51.57103 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c3fdab15-af7d-3704-ab8d-509fbd1a4ae9 | -1.99206 | -53.2949 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f7870a93-e301-358a-9ab4-808ee325e555 | -1.25489 | -51.74376 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08a3f2b9-f942-392e-86b8-7eb5cdff78ae | -4.23756 | -48.69859 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91872c68-b981-36f8-a8a7-bd79864245c6 | -1.44782 | -52.45073 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b31fbcf7-a25a-3ceb-9fab-1d1b02e89771 | -3.28743 | -53.66418 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01d91e31-4cb5-3dd9-8c70-40d8f28e7f68 | -3.29171 | -53.85257 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a374c836-f619-325b-a058-87259e215e45 | -3.35473 | -50.51185 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e11f42d0-5833-3a2e-9d46-cf04cdfcde65 | -3.25565 | -54.21047 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27780001-722b-3bcc-9557-6815f66eeceb | -3.71021 | -53.75186 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bafbe989-3cb4-392a-87ce-904a6fc91d86 | -1.73983 | -52.72657 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 282149db-3bb0-3763-8177-efc910433aa9 | -4.37564 | -48.50328 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8ac6a4f-56a2-37e6-b757-3216b779185f | -0.99713 | -51.78754 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47a65f57-8d7c-3903-abdc-62967b0aaafe | -4.30703 | -48.07706 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fab3b3d-17ad-3415-bf0c-3a94f76b5fe0 | -2.76644 | -54.07306 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f40f57e-26f1-3321-994a-e1fa46b28b86 | -0.9309 | -51.71594 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c832ac7-71ea-30e6-8cae-ab70fc88f70a | -2.79876 | -53.00845 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63c6b44b-f37a-3bb9-962e-1d4351b44ad9 | -1.60369 | -52.57747 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 82cd1884-b023-365d-9fd6-ffbc4379aae2 | -3.93332 | -49.89897 | 2024-11-25 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8ee79f66-bec6-3293-adb0-c8b8606789a9 | -2.74634 | -54.02702 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7befe451-cc53-3e7e-a32f-2215b294363a | -4.28803 | -59.71573 | 2024-11-25 04:55:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26e372f3-0fe6-3e13-b3e4-c4ff0b5d896f | -1.22584 | -51.79723 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1edd9932-0fc4-3960-af5a-8424f10466b7 | -1.75347 | -52.6615 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04e23661-d2b6-32ed-9c84-e624d3e187e3 | -2.83779 | -54.06985 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eac5e674-7b93-3144-b1f1-af5e830ca1cc | -3.62395 | -55.30301 | 2024-11-25 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f894486-4244-31c1-94f1-49a1e9cc2efe | -2.35736 | -54.47908 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2536bf8-2d96-31fc-8e8e-ef438206ae09 | -3.52779 | -53.81547 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d9ab96c-8d6e-32d4-9bcc-4555a7448915 | -3.22344 | -53.8349 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7c7bbeb-3d7a-3bc8-b662-361f5d21bb0a | 1.38176 | -55.89385 | 2024-11-25 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26ab6340-d534-3a93-8031-d45b5f145c20 | -4.23242 | -50.66539 | 2024-11-25 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1a89d49-1ad8-3153-baae-57c85272870a | -4.23407 | -48.64067 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16d6d0bf-de6a-328f-819e-000a6708bde8 | -0.16139 | -51.57177 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fb773f0-3f5c-3b60-bbfb-2a874c204a6e | -3.53586 | -54.49212 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62594a5e-9ef8-3fa7-ba1b-a96a73ed1f8c | -1.2292 | -51.79774 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc01a6b6-cebd-33b7-ba00-fb0f281df7de | -3.82509 | -52.41443 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f85a9ff-afd4-34f3-b6cc-c4605c3056f0 | -2.04206 | -51.17399 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2dbc83b7-7e74-3f8a-a01a-94cf6b2eca79 | -4.13719 | -48.75866 | 2024-11-25 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0fc2895-04f6-3103-ac06-8016e6446696 | -3.29108 | -45.73822 | 2024-11-25 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fc417f66-9bd4-3107-8ed0-81da2ec27cc2 | -2.75635 | -54.02859 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5966729-d078-374a-b3df-317e2007f9a0 | -3.81221 | -52.0032 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README41.md)
