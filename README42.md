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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fe929c5-d43f-39d4-b745-ebd1c47549c9 | -3.23375 | -50.85054 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab1ea8fc-aaa1-3a1e-8125-2c23a0a75ad4 | -3.23307 | -50.85449 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ceb962f2-e46c-3196-b595-be54237190a0 | -3.23105 | -50.85336 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 770731b6-c5e5-3c05-98ef-3c3e6e35ce34 | -3.22741 | -50.85346 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b626d93a-5dcd-3e90-9c2b-924e98800f33 | -3.0425 | -51.13247 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c52c413c-020a-3b5a-bdf2-93e78b40eb80 | -3.04182 | -51.13655 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 85ed69b9-1d9e-345c-b08a-63c453d1e181 | -3.04067 | -51.03603 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 822c80e5-dd7e-3ac4-ab4a-cdf2dfdfafc4 | -3.03671 | -51.13145 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 295c5761-42ae-3fd8-9269-cec8fb95a20d | -3.03603 | -51.13552 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 04f0db32-dca6-3dfe-b6a7-93914722d535 | -3.0349 | -51.03508 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e8ac0e2-6463-3013-bab3-17b30af148eb | -3.03089 | -51.13057 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb86d4ba-3206-3c3e-96bf-f4a6bf05ef4b | -2.9644 | -51.03141 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41acb924-28c1-3103-bb4f-1b76335a9df7 | -2.96371 | -51.03541 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 46d774a5-2ad3-3862-bdb6-32a3903a354e | -2.9637 | -51.03276 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08bb22a2-cd9c-3f39-bc6c-363848335d83 | -2.96305 | -51.03676 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a78b5b69-70b8-3753-b228-58bef7148931 | -2.86362 | -51.02814 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ffbf5bb-2301-3c87-ba8e-7c0debd0231e | -2.86308 | -51.02816 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d37acc8-ee7a-3243-9d2c-b2e7a4d66580 | -2.80597 | -51.01458 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6cd016d-bf72-37cc-b3a4-089afb37738a | -2.80527 | -51.01876 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12d8d01f-5b29-3fab-b659-0fe461906fc5 | -2.80458 | -51.02288 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f07b763a-0582-327a-8ef3-bb21a7208bfe | -2.80018 | -51.01373 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c52894eb-5e91-3595-9816-19f293228798 | -2.79949 | -51.01785 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 53dccf75-d7b2-3f3d-9be4-0f105f219a63 | -2.7988 | -51.02195 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ccd0a3ea-14aa-3977-99ce-1aa9670f8c29 | -3.18418 | -51.2463 | 2024-10-12 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19ac1f08-43ed-3ac2-b0fc-5663f95d7ac9 | -3.17837 | -51.24522 | 2024-10-12 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f974dc7d-a513-334a-83af-58fa25d55b75 | -2.973 | -51.36956 | 2024-10-12 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc504feb-1d81-3a36-bcfa-0ba4bb11d435 | -2.96852 | -51.36014 | 2024-10-12 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39c0121d-46d6-3289-87f8-d3bb63096f43 | -2.96782 | -51.36431 | 2024-10-12 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91c01db5-3d88-3719-8fa9-00a3e162b824 | -2.96711 | -51.36851 | 2024-10-12 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ac8b6ea-51ca-38a7-b897-37b5a5edf34b | -2.95053 | -51.28775 | 2024-10-12 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5706e95a-8594-3390-b22f-0255e1996488 | -2.94983 | -51.29188 | 2024-10-12 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 028e1439-9b82-3abe-9d0c-80f31f6daaf0 | -2.94576 | -51.28889 | 2024-10-12 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9839a50-b79e-3d25-8a17-44065fcdac69 | -2.94508 | -51.29308 | 2024-10-12 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40b47081-a66a-3817-b0d7-deb3bb09a1b5 | -2.90116 | -51.76091 | 2024-10-12 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0167b9ef-2fa0-331f-8679-2931cbcb2d21 | -2.89512 | -51.75984 | 2024-10-12 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d43c6ca9-0ab3-31e0-bb3e-36e51bc94b88 | -2.87681 | -51.6744 | 2024-10-12 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92934f4f-f39f-3bb0-9604-bb2ddd0c663f | -2.87607 | -51.67891 | 2024-10-12 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a733bbb-ddb3-3f32-88cf-e47d6ef96192 | -2.87227 | -51.66434 | 2024-10-12 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8bf69c00-1834-3d9d-964d-e52717e2e372 | -2.87153 | -51.66888 | 2024-10-12 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b1a3c569-feb3-3e2e-9f5b-30a6efb2d6dc | -2.86769 | -51.66579 | 2024-10-12 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 795c7f71-bd96-3ceb-b450-e70189f3c95d | -2.86691 | -51.67034 | 2024-10-12 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b681ab51-f43f-3ede-bbf9-04063f4c46af | -2.86626 | -51.66331 | 2024-10-12 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1274da97-6070-3cca-90f3-ca1d076950ad | -2.86551 | -51.66787 | 2024-10-12 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 532e10de-8e89-3a72-9046-445c9dc6ea2e | -2.86477 | -51.67239 | 2024-10-12 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 58c49331-c69b-36f3-af66-630bccce9676 | -2.86089 | -51.66936 | 2024-10-12 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9e692ff2-32ae-3a4e-b93d-e72a85d6d7f6 | -2.86011 | -51.67388 | 2024-10-12 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f8c0b2e2-a9b9-333e-bd2d-3674e5d2ee29 | -2.85874 | -51.67142 | 2024-10-12 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1d1af9b9-3017-3748-b7e5-162dbc4279d9 | -2.82215 | -51.34145 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 047514a4-296e-37f1-b902-a28accd037db | -2.82143 | -51.34569 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f7d007e4-19a7-30bd-86b2-aa00b8c8f796 | -2.81865 | -51.33695 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 77cc49a9-39cd-3d18-bc4f-39e61366614d | -2.81795 | -51.3412 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 74d9554e-975b-397f-b99d-012b996d9fea | -2.81726 | -51.34546 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 7254000e-875b-3442-9727-14f33c74dbf8 | -2.81698 | -51.33619 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 821891fb-7497-3cfd-bdf1-4723ea3bd828 | -2.81626 | -51.34045 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 7b0e7ce1-4ded-33d6-abad-0729b0810232 | -2.81553 | -51.3447 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 71a48388-e524-3d5b-b4b1-7a39ba177d76 | -2.81206 | -51.34019 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 8216d41d-b30f-3403-aa16-5fb18a086732 | -2.81136 | -51.34446 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 56e5f69d-f62d-337f-9cf5-f52a21a2da3c | -2.81036 | -51.33946 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 5deb99bb-6edf-31d0-9b11-c2a89b98a55c | -2.80963 | -51.34373 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| f7b1df84-eaa3-369f-ab0e-78f12cdd009f | -2.80831 | -51.60346 | 2024-10-12 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4ec77ba-60aa-397f-b4a1-b16182cd6a48 | -2.78352 | -51.36615 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| c4604c19-363c-3373-b88c-1de43756eec9 | -2.78281 | -51.37047 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| c7d77cc0-b7eb-3abf-9e65-57eddd54cbee | -2.78209 | -51.37482 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4d79d1b9-1bd3-3786-88b2-78edfa4078e8 | -2.77763 | -51.36509 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2f1d58d0-a0c7-36ef-9e65-f82260e6ec3d | -2.77691 | -51.36939 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 06090905-a44e-3675-bc1c-bbceeb70499c | -2.77619 | -51.37375 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f06413b1-f1bc-3f9a-9321-6e536763243b | -2.77028 | -51.37273 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 82367890-14ad-306b-951b-b4881032b0ae | -2.76956 | -51.37712 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e16db059-4607-3455-a156-ebd0e474a8b1 | -2.64418 | -51.71296 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57fe03dd-84c0-3c40-b510-054f23fbbe50 | -2.63888 | -51.70735 | 2024-10-12 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4002e6b-ea0d-3dea-8a48-cf31f8a06329 | -1.89724 | -52.49433 | 2024-10-12 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 251a3de3-ba9a-3a2b-89f0-33efcb95aaa8 | -2.98146 | -52.90548 | 2024-10-12 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9deed33b-1314-3b58-8b0b-a457a597f770 | -2.98119 | -52.90775 | 2024-10-12 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d48bbe03-990f-3af4-b8fb-4e0ad0c8f9d1 | -2.98059 | -52.91069 | 2024-10-12 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c549ea9-ad7f-30ea-85e5-5ed71181b480 | -2.98028 | -52.91299 | 2024-10-12 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a315728e-b888-3752-bfdf-b9d929341e36 | -2.97498 | -52.90433 | 2024-10-12 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d76f203-aaa0-3b13-9c43-c41f26144133 | -2.97472 | -52.9066 | 2024-10-12 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c697413-a2bf-3e46-83f9-b8f7186cd515 | -2.97412 | -52.90954 | 2024-10-12 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c35f5c5e-755b-3a74-a204-6db9d9444e71 | -2.97381 | -52.91183 | 2024-10-12 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 801a106b-8743-3a1d-b3bd-94ed078121ec | -2.96827 | -52.90532 | 2024-10-12 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52a7c5f0-7d5f-3ad4-81a6-08d929bd5761 | -2.96767 | -52.90819 | 2024-10-12 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2bb7051-60ef-3bc1-8758-af1704c129d5 | -2.96737 | -52.91047 | 2024-10-12 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4188f40b-babb-30df-bf7d-93c77c6b3ac7 | -2.9668 | -52.91341 | 2024-10-12 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6cc45db-a202-3752-b2ff-265a37f316f7 | -2.96183 | -52.904 | 2024-10-12 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d831712f-31e0-3a8f-970e-a75d360197b5 | -2.96123 | -52.90683 | 2024-10-12 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 878968ef-c0f1-392a-80e6-0ca3dee7900d | -2.96093 | -52.90911 | 2024-10-12 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1cc6d6c2-cf1e-3665-8129-f151aac60866 | -2.96037 | -52.91198 | 2024-10-12 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7bebf78-ec58-3d67-a4df-dc8c65c8c080 | -2.77873 | -52.48728 | 2024-10-12 04:04:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a0519d3-98a1-3774-b0c6-9178cd20dbbd | -2.77239 | -52.4862 | 2024-10-12 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4de4942-35e7-32a6-b288-d891d46c4cc5 | -2.67481 | -53.34549 | 2024-10-12 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83fb630d-b573-3e90-9901-d972b5ce0494 | -2.67383 | -53.35137 | 2024-10-12 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 766409d2-cd50-3440-b318-d12f72dd44f4 | -2.67109 | -53.34745 | 2024-10-12 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6133888-9556-31ce-a9fd-648fc274e405 | -2.67007 | -53.35332 | 2024-10-12 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 236b7a15-b9e5-3872-8860-d3f9655a8b21 | -2.66715 | -53.35019 | 2024-10-12 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab8bc4f0-997d-3a78-adcd-cc7acec9bc89 | -2.66616 | -53.35609 | 2024-10-12 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b68aa75c-d96e-3970-9d41-aa428caa3db1 | -2.66339 | -53.35215 | 2024-10-12 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f75dc875-06a5-3c69-a28e-0c1475adb35e | -2.66236 | -53.35806 | 2024-10-12 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d632cf80-679b-39ed-b9a3-3948cc82d1bb | -2.66047 | -53.34901 | 2024-10-12 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e7fb2d1-780f-3ca2-82b5-aea97136287b | -2.65949 | -53.35488 | 2024-10-12 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06a243d3-0ffa-326f-b3ba-d627eb58f34f | -2.65848 | -53.36087 | 2024-10-12 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README43.md)
