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
| b6bef9e6-0714-3887-ba97-0f3177d3938f | -3.96085 | -45.99282 | 2024-11-24 05:14:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed7d76c4-57d0-3ecd-9272-20c6c5d2f600 | -1.92706 | -54.4316 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc766fa6-c890-3c95-8dac-a585c963ac19 | -2.18043 | -54.47458 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a583150-1371-30f7-b2bf-3f942bd94885 | -1.53594 | -52.4544 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4cef8bc-bcd6-3499-9d63-efe911f7f600 | -1.42924 | -53.37666 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 52c3feb8-f8da-3a5e-9bd9-4bcd77aa35cb | -1.14312 | -51.67852 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a32ba3d5-a657-3681-afbd-17ee1baefa78 | -2.43972 | -49.08898 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 498c41e2-0d76-3a8e-b756-26eee4cbf691 | -1.73199 | -52.71632 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66e190e3-84ac-35cd-ba37-a4bc899f6ca2 | -3.29357 | -53.85842 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a564f617-3e12-396c-9492-c0c77882d7f6 | -1.38562 | -52.3334 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abb74705-d6ec-33e2-aaf5-618a52a2def1 | -1.42462 | -46.0627 | 2024-11-24 05:14:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f521cd40-c8e3-3de5-b32d-83ea1bb1384b | -3.26062 | -53.71014 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d541e9af-eca6-34cb-aadb-8b19baa2fcba | -1.30516 | -51.7379 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 389dadbf-086b-384d-a040-38093dfa70e2 | -2.85171 | -53.99837 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 536abcac-bf46-3255-9c4a-7ab1d9fdebae | -3.08337 | -54.54175 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f82dbd6-6fc9-330a-838d-4c76cbec3d8d | -2.58869 | -54.05142 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 314bfafe-41b1-3588-b714-48eec7060c40 | -2.7796 | -54.06282 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7653e892-a67a-35dc-9625-51c9ea0294b8 | -1.24781 | -51.78438 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a06bf01-f407-3942-92b9-c8427b58e662 | -2.61113 | -54.25359 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 401dced6-5818-3f6c-a622-8050bf3e5b0e | -2.73648 | -54.39578 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93b27768-5ddf-3621-a2ed-11571b330f30 | -1.94935 | -49.52283 | 2024-11-24 05:14:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02c00af5-adbb-322b-8432-69778e24f166 | 0.00995 | -51.19264 | 2024-11-24 05:14:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e208cb2-dc81-3a88-8573-7e297d3ab841 | -3.02426 | -54.05265 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62956205-f748-3c07-af79-17b2a5dee681 | -3.23155 | -54.23479 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 016d5932-e377-30c6-a634-d10d0afedebe | -2.30965 | -53.60448 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c22a516-cbee-3869-86bb-b07bb7607a85 | -3.10607 | -53.99186 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ef5f3e7-1d64-3f45-9b4a-25ec799ddc03 | -2.7987 | -53.00507 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f9c813e-a365-3836-b3e8-bc2cd197cd61 | -3.26649 | -52.63282 | 2024-11-24 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fcb3885-2089-3b92-a60a-2008cb19cf4b | -3.07698 | -54.55851 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9967cb96-8daf-3cec-9876-1a3e01a5656f | -3.03808 | -49.45307 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 25f3a516-2f93-3f9b-99a9-e97639663b4d | -2.32717 | -46.34374 | 2024-11-24 05:14:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a797524-6438-3c26-a21e-679e49dddea5 | -2.82469 | -51.79703 | 2024-11-24 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d961fd98-d2d0-3d14-b287-709be0bd5687 | -1.61329 | -52.59594 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a08da84-81b8-33ab-ba4f-609e95ad6cf7 | -2.75842 | -54.07603 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 797e8ded-29b3-339e-8427-de0969901b2c | -1.08566 | -53.64311 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 980eafc0-1434-34f1-a360-bda3b88dbe76 | -3.54622 | -50.19223 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce2e66dd-947b-30d9-9b1a-b7d29fc82a9d | 0.4043 | -50.85386 | 2024-11-24 05:14:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5f1a1569-acce-3663-b564-0d1a24f63915 | -1.53238 | -52.45012 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b39ec53-87dd-3943-9861-3e6c94705528 | -3.08048 | -49.20071 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b3df143-d42b-3425-9632-6bfceaf4cf4a | -3.0752 | -49.19991 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d4c59c3-544a-34ef-8538-76cd8b466b2c | -3.35453 | -50.13802 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23ebea63-0c0f-38bb-aa66-8b88e5bf341d | 0.4152 | -50.85439 | 2024-11-24 05:14:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5aa15ca7-5e07-36eb-9b07-f21442cb791c | -0.92378 | -53.10427 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1df2f7f5-42fe-30b8-bf61-64aac7f97b62 | -3.254 | -52.85133 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3a1aaac-1881-3210-acc4-45667156a128 | -1.5162 | -54.40825 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e3728c0-d275-3664-8c43-ca654dcf2a19 | -0.03721 | -51.6087 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0628d5e-62fe-3a2f-a9c3-91a36b0c3d71 | -1.15557 | -53.66843 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1528eaf-295c-3b8d-9f99-517c2a9a088e | -3.24886 | -50.66562 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 08c3170f-4e7c-31f5-be27-703716e89cc1 | -3.03685 | -54.0214 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 99a590aa-bbcf-3379-8252-f31f6f770171 | -3.05392 | -51.33161 | 2024-11-24 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6f10d87-78f5-3e44-9c26-1a4dba269a5d | -3.60663 | -47.50755 | 2024-11-24 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ef67ea4-6bf9-3db3-ac90-1040195d3370 | -2.27428 | -53.57263 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59269c82-08ea-344e-b332-6b77b09f4b12 | -1.10204 | -53.61224 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43695f98-55e7-3e88-9c7c-2498fe474e5e | -2.58468 | -54.22681 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9659869a-236f-3a07-918c-d76e2f081615 | -3.28181 | -53.83204 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3554aab9-e2c9-37f9-b067-fb9c5fde468d | -3.04419 | -49.44755 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8f9f3e0f-7218-358e-a399-3ff47800dccd | -3.07063 | -49.19921 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e83713b-8aca-34be-a42c-234eae4b64ed | -3.49003 | -49.90929 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3641367-70e7-3b5f-adf1-a0db48e3dbf3 | -2.20912 | -48.91993 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c68bc07f-1cfd-3589-958b-a9489a4561c2 | -3.70537 | -47.59628 | 2024-11-24 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39781428-b9fc-35e4-87cc-878998973db4 | -2.74477 | -49.11816 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c95c79d-07c3-380d-841e-0d41a5ec629f | -2.28209 | -53.62967 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58cc1b77-82c3-3272-af2a-727f7cef07b4 | -2.28148 | -53.62762 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c91f0cf-e11c-3d0b-a168-0184dd264aa3 | -1.22642 | -53.68118 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4fcce017-59b6-3fb1-9a50-3a00f16ffbbb | -2.74106 | -54.11297 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4fe3dd91-20f2-336e-9d04-dc93247692c6 | -2.62165 | -54.25972 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0b7f73ab-6927-3e64-89c0-5c10633c6fbf | -1.11461 | -53.39022 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6137eeac-7311-3bf0-a3ad-deac4e556ac2 | -1.77262 | -52.71831 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d066761b-ec6c-3999-9e00-24bdcea3a2be | -3.22742 | -53.93026 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 16d6c9a2-3048-3727-8dd9-ba6c42a519eb | -1.4277 | -53.38644 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cc386dbe-a2fc-33c7-84b8-b1dc8ecb4f42 | -3.75686 | -49.937 | 2024-11-24 05:14:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 150d5d8b-7519-3f68-8089-ab752095cb2b | -3.15893 | -50.58633 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8f19657d-bc0b-3f37-b993-5d445696cdc4 | 0.41587 | -50.85878 | 2024-11-24 05:14:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df4cb777-3be4-3478-a073-5975fb5954f8 | -3.00233 | -51.5473 | 2024-11-24 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83029305-3295-3eb9-8d57-efa8997c7a04 | -0.23112 | -51.48234 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd8c3749-3a81-3d01-9af9-de58e3c137bc | 0.4056 | -50.8514 | 2024-11-24 05:14:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 681d12a8-105b-30dc-94ec-acb5696fba2d | -3.02497 | -54.04803 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 57730874-1633-38dd-8bd8-aa30d0b8e9c0 | -2.21336 | -46.39042 | 2024-11-24 05:14:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ca7f01d-b9b7-38e3-9787-0b260086f4e9 | -1.58001 | -53.81704 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e74d9a1-b927-3e74-ac53-afa57a164231 | -0.95237 | -51.7173 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c44b1c0c-6b82-327a-bd66-fd9d5ab47169 | -3.28732 | -53.84765 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12666b51-7be9-3559-bb63-9742b9a730ca | -1.96504 | -48.38499 | 2024-11-24 05:14:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc8bf4a1-a5db-3626-9158-f8657368c1f7 | -1.0135 | -53.09453 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad5b624a-2d19-3f25-84d6-2c6006f35de4 | -3.49153 | -49.91228 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df301a2e-8d19-30d0-8afd-b98df4da98ec | -1.86886 | -48.16465 | 2024-11-24 05:14:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47a9e4fd-3721-3965-b62a-50f64a967048 | -2.61217 | -54.7433 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a92e4c1b-17c8-3158-8ea3-df1a173c6ad5 | -1.44562 | -54.91623 | 2024-11-24 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f970e74-b4b3-3b7c-a78e-65d37d9bf9a0 | -3.10748 | -53.98252 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f415681-97f7-3bb2-a7b9-8a7c3a839475 | -0.77166 | -52.48714 | 2024-11-24 05:14:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10eb6675-d32f-3101-8eee-97bebc441175 | -2.87487 | -45.83315 | 2024-11-24 05:14:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06533ec0-b6b4-347e-b675-bfd49649777c | -1.21814 | -53.68453 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 9a26fbe7-5995-35ef-bc74-f83836c4d134 | -3.2815 | -53.78227 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 003e8e15-dafd-34d2-88af-6eddd09bacc7 | -3.60004 | -47.51094 | 2024-11-24 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e91d413-4a67-3a19-a519-f7c804df473a | -2.95106 | -51.42936 | 2024-11-24 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6005fd2-7c59-3ccb-88dd-38b63febfb89 | -1.739 | -52.72469 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6bc2cc2-f3f1-334b-a2cf-126ccca87ce6 | -3.25084 | -53.27429 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c92f0fd1-bb4d-31a8-8910-18b0b037400c | -1.51367 | -54.40545 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3bd9fdf2-bc74-3162-b784-d2668129dd53 | -3.19069 | -54.32528 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f6c2850-2c69-3883-a579-89f41d52c08d | -3.76237 | -49.93487 | 2024-11-24 05:14:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c98a2b80-06d5-3993-af0e-be770f0f0f30 | -1.41983 | -53.38606 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README69.md)
