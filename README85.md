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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f3ac491-834f-3421-a490-ae7a9ea97d13 | -3.22714 | -50.45382 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3c913c5f-0963-3241-a1e3-85343dfbf677 | -3.08842 | -49.40532 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a978c4f5-d51e-339c-94dd-54959c6de069 | -3.6014 | -47.34627 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 5e1f4503-e43d-3d5c-9b44-17ef7ce8543b | -6.24967 | -43.55745 | 2024-11-10 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3276bce4-048d-3e2b-b393-67e203281c51 | -4.18954 | -49.98552 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c869289f-fb0d-38be-98b0-cc3aba569449 | -3.58678 | -47.35135 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 27ffef24-09d2-309b-ab43-e42937e2ea6b | -2.60365 | -49.18994 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88e354dc-5391-387c-968c-c742cd8bf527 | -7.14343 | -41.10855 | 2024-11-10 04:38:00 | NPP-375D | CAMPO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2202133 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 76d29ca3-17f6-3730-94a6-1956144c8d68 | -4.09763 | -45.6198 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe8a4252-6fec-3dfb-bf94-b20a331666ca | -2.66502 | -48.65329 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0843526f-ac25-3874-82d7-a793bb02f221 | -3.14094 | -50.44398 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a6d5eab2-e945-31e3-8763-6374a31c7023 | -3.07766 | -49.29993 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62ff3838-0768-3f38-b8b5-f8128656452f | -2.79732 | -49.292 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87252ff6-d91c-3900-8e6e-bc1333a8d7aa | -2.09455 | -50.9109 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 18d4a70a-65c5-3349-b312-8ca716125c23 | -4.13545 | -53.50634 | 2024-11-10 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87b6d37b-af87-3c1c-891a-ea7563c66e4a | -2.13002 | -50.82469 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2edbf93c-36f4-3d70-94eb-f3970cb0eca3 | -3.26483 | -53.70388 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7be4eacc-8b25-3032-8408-249f7a62c566 | -3.35549 | -50.12971 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed9de778-5a79-330b-a0fc-4a188e00e03b | -8.39941 | -44.1242 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87b02264-8a1d-3a65-9078-2bc8b975505b | -1.66605 | -53.80426 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 666d99d0-b676-3679-8e36-07881fad6266 | -2.6817 | -48.50412 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6c2960c-959b-3b40-9d87-5d5e0440f473 | -2.71487 | -49.29996 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57a15c85-ea2d-3698-91a3-155e93ab05b2 | -3.02034 | -47.96292 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9b0d921-cd7a-3ee3-9de0-4c499105937e | -3.60612 | -48.94928 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53a09545-502d-35f6-a1de-9540e85d00a4 | -3.41434 | -51.20971 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2693cd44-86bc-3585-9daf-885626f4da86 | -3.17565 | -49.10492 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ed8a274-f627-3c83-b178-5c1e55951ec4 | -3.09884 | -49.41732 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b34f82ff-fd42-33b4-ad7c-180de04ec2a1 | -2.19395 | -50.33703 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbf29016-ad3b-3775-a6bd-58a47238ce83 | -2.84562 | -52.54568 | 2024-11-10 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11cd263e-83ca-3008-a866-64eb30bd1e40 | -3.98595 | -49.98966 | 2024-11-10 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51950922-b873-32e4-8a3e-a90b6117f46e | -2.41892 | -49.86643 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd8d7195-c78c-3ee0-912d-582c603f06e7 | -3.33288 | -49.92401 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 733d08b8-bf64-3347-b646-c7ed69477e42 | -5.36387 | -50.6102 | 2024-11-10 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db396bec-267a-3f3c-b596-f1e3e3cfec17 | -5.30085 | -46.22572 | 2024-11-10 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b45731c-50dd-3e3a-a26f-4d0466b84e7f | -2.64438 | -49.89759 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20783b1f-efb7-3a68-b864-3e755ddaa06b | -2.37334 | -49.82619 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b32fed4-6919-31a1-81d1-6c032a394214 | -2.99002 | -50.29623 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9eb5b5ae-d152-36ac-9115-11c5e47fedb4 | -3.22111 | -50.38113 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39e8db56-e8c3-39bb-b81e-be8d502dd14b | -3.03369 | -50.35199 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95dd3ffb-2bf8-3d09-adfa-dab54d288926 | -3.13534 | -50.43992 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| d6d4e735-717f-3b43-8a64-42fb4ab6e5fc | -2.54854 | -50.30365 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 541d140c-6a33-3ebb-b6b0-8e697b0ea2f3 | -2.80065 | -49.29252 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b7df413-f139-324a-8b73-2afa7eab689d | -3.15783 | -51.12217 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2823df19-c37a-3006-bd54-6bfdaa143106 | -8.39183 | -44.14689 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d57212a-d8df-374d-8c5d-f49ce5b0973b | -8.84264 | -47.70059 | 2024-11-10 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f4a6297-d28a-3a7b-9730-74f301016417 | -2.74969 | -49.16619 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12aa3664-3453-323c-b6a9-5d635ce99afb | -2.72155 | -49.30101 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd369d49-dde1-335a-a034-dec6714ffb02 | -3.33698 | -51.64908 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d7191d87-f7f9-33ef-9a40-7eae631f1682 | -4.10434 | -49.11965 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 746238d6-86db-3bcc-99f8-4f34f58970a8 | -2.57997 | -51.88221 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7723b856-68df-3c4e-b326-516037c6d041 | -2.65907 | -49.84847 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 92379581-7710-327d-884e-4cbfdb431770 | -3.4084 | -50.30104 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9b0c5241-0af4-34e4-a9e6-bd81ff8b3f6f | -3.10552 | -49.41837 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 38cd8b78-2a00-36f8-8fcb-35af4ac0d6d9 | -2.76447 | -49.35427 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 7075032d-6fe0-3c33-baaf-6c0f4fdf8022 | -3.23758 | -50.18933 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1bd69bc-588a-3b2e-afe0-13e27aad26a1 | -4.07403 | -48.32222 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41e6e11c-5be1-3039-b16f-79ac8215a50e | -2.65961 | -49.88895 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 461a00e1-e6b2-3c92-9afd-986dd25ae8c6 | -4.61209 | -45.98642 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1218322c-a580-3373-80ac-3fa10bf51765 | -2.89495 | -46.81648 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 941637ca-b4f7-3aa9-a742-ce18e96ff5ec | -3.39002 | -50.35047 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7172bce-aa1e-3fc2-b899-3714edf9dbd0 | -2.81196 | -51.80626 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 96e14b95-c906-3ddd-9b12-83842e3a1032 | -2.79309 | -49.21575 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4613d571-53cf-371c-a89c-8016066e6c41 | -1.9396 | -52.10432 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f00bfd20-c08f-3270-85cf-f4235a68d049 | -3.04684 | -49.53884 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0e3f0ed-c939-3d46-8044-e9f3563cf4e7 | -4.16267 | -48.25051 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9a239b5-5faf-32ae-9ec9-55daa63146b4 | -2.81027 | -49.86859 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4645501e-1d8e-36e6-b08f-d4668ff287ec | -3.07208 | -49.58558 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 869e0d6a-48c3-3a50-a115-0b3a0d325da3 | -3.20302 | -49.4664 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f3523a37-6b3d-3619-a9bd-987a34f0d3ba | -3.43999 | -53.05282 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9dbfa1b7-e908-3d62-8501-19f882f65f36 | -2.84206 | -46.6206 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 400adfb9-c201-3224-a838-cb98933b5b29 | -2.11514 | -50.8502 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ebe5ac3e-6cb3-3004-a40a-a70663cf69a9 | -3.24859 | -49.77269 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| adbaee69-c0c7-3c6f-8595-6fb7a6bc5079 | -8.39351 | -44.13523 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7c7587d-b712-3b8a-ad4d-b29676356ef3 | -3.98348 | -50.89896 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e13f75ee-02c3-3759-a0f6-be8790b3fa24 | -4.2089 | -49.76445 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bf8b153-a0d7-32ad-9610-f4cb3617346f | -8.3781 | -44.15277 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cff08c05-c1b2-370b-84bd-18bdd0cb9ca1 | -3.31173 | -44.39396 | 2024-11-10 04:38:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 50d42f6d-3dfd-3b9e-bde6-df44fb73c995 | -3.43679 | -50.29804 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0176b40a-f8e0-3e29-a1bd-cf46cb28ac00 | -2.43094 | -50.40734 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b3df120-d598-3eff-9642-48e0d30d8c45 | -3.95393 | -50.51698 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7e2f03b-6cfb-3049-bba7-db84aec4480e | -3.1629 | -49.09938 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86ab7eb5-cfc2-364c-8fa5-412e4cc34e27 | -2.92701 | -49.54538 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2c8bfe1-611f-3d16-aa9c-5abda13b247a | -3.5372 | -51.25223 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6dcd57d7-8cc5-3587-8347-246de21c486e | -3.18599 | -50.58035 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d4984af-763b-39b2-955e-eb2c75df3a07 | -3.98647 | -48.16629 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58be65a5-a348-35cc-bb90-4f2e913d4e17 | -6.32627 | -46.72108 | 2024-11-10 04:38:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ff90967-6c1b-3201-84ad-549e34aa75ae | -3.21943 | -50.36961 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bdf1a26c-ae02-30b4-82e9-074a88cae94f | -3.95256 | -48.14323 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36db9185-c4f5-38c5-a9a2-0393456f3edd | -4.23585 | -48.02266 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ace22a2-4bc0-3fdb-8fdf-ee635ea4b938 | -3.99153 | -46.41605 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 40ea6ee8-9cfc-3757-8f36-59506645ed21 | -3.97247 | -48.12495 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a621f3c3-cbb5-3bba-99b7-a4b6c2bbeddd | -4.10895 | -46.88981 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f8928f9-0717-3a6c-8fad-78f5cae955da | -3.61679 | -47.51981 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d23beae7-434a-38ee-8221-5afcebe22711 | -4.32242 | -48.65551 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fec98d0b-a9ae-363c-9ba3-d8a38daa5607 | -2.83593 | -48.46817 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d4f2a5a-5f7d-36c7-aef3-a14ba9fd914b | -2.9234 | -51.48331 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| d4d114f1-2fd2-35ad-9d13-924d2de2038d | -4.11812 | -48.23664 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e4424d8-03c0-325a-b10c-d057e481fb98 | -3.11293 | -50.14046 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22778623-ef32-3279-a247-29c4ba916c0c | -3.58734 | -47.34777 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| dabb5bc6-eff8-3cb8-acf8-710bf67b3c0b | -4.49087 | -48.49049 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README86.md)
