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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3067cc6-67fb-34f4-bf85-83705fb6398c | -16.6912 | -57.1875 | 2024-10-02 02:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 193.7 |
| e8414ef7-7ebc-31b4-86d3-660f04e78780 | -16.6319 | -57.2352 | 2024-10-02 02:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 210.5 |
| 7b1f6a06-5496-339c-b711-4607e9f7019c | -16.6322 | -57.2147 | 2024-10-02 02:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 303.0 |
| 08ad88da-6650-35bb-9e8b-8bdc90e6b0d5 | -16.6326 | -57.1943 | 2024-10-02 02:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.4 |
| ed6afbf1-7244-38d9-a3f4-81d9e0acaae8 | -16.6518 | -57.2125 | 2024-10-02 02:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.1 |
| 1ac9de2e-8096-30fa-b96b-42d789b295ec | -16.6717 | -57.1897 | 2024-10-02 02:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.3 |
| dd6d8890-4e41-3a4d-baa7-babfa51966fe | -16.6868 | -57.4741 | 2024-10-02 02:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.9 |
| 9b5ea640-8b7b-3755-bb45-44da8627399c | -16.6884 | -57.3718 | 2024-10-02 02:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.4 |
| 46f8d4c7-b4e6-36a4-8e9a-ddd3f590f80d | -16.6887 | -57.3513 | 2024-10-02 02:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.9 |
| 41141c42-304a-3da3-86a6-7eb56249f919 | -16.6909 | -57.208 | 2024-10-02 02:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.6 |
| fea4aff2-2452-3a2e-9ccf-f56d4689ce8a | -16.6916 | -57.167 | 2024-10-02 02:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.7 |
| f4664c15-703b-324f-9656-0ec35c0aa0eb | -16.7063 | -57.4718 | 2024-10-02 02:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.3 |
| 9969b0cf-df3d-3326-97b8-f72d83a91719 | -16.7108 | -57.1852 | 2024-10-02 02:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.3 |
| a26e4741-2478-3bca-a56d-6ef442d0ce0d | -16.7265 | -57.4287 | 2024-10-02 02:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.9 |
| 83147818-26e5-36d9-b7cc-f97b2cdc88fa | -16.7269 | -57.4083 | 2024-10-02 02:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.9 |
| 48c610e0-d131-3b46-9b6f-987da2a1abd3 | -16.7452 | -57.4878 | 2024-10-02 02:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.4 |
| 0e2d7b2d-a459-3cdd-be1a-c1bc38cf6d96 | -16.7461 | -57.4265 | 2024-10-02 02:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.1 |
| 9aefcd24-1c61-34b6-9f27-f2965fed9c65 | -16.7647 | -57.4856 | 2024-10-02 02:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.6 |
| f1a4e40f-a018-35a6-9a40-9c19f98f31e7 | -16.8096 | -55.9177 | 2024-10-02 02:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| c01dd39c-52e4-3fa8-93d5-aa4a45954a54 | -16.8695 | -55.848 | 2024-10-02 02:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 89.9 |
| 567a5149-1917-37d2-b865-8f8bc1edfaec | -16.8891 | -55.8455 | 2024-10-02 02:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.1 |
| 0e8805a4-6533-3e7a-a19d-e33bd88f0de8 | -16.8292 | -55.9152 | 2024-10-02 02:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 111.6 |
| 324ca045-b948-3277-bc8d-f5570660c747 | -16.8295 | -55.8945 | 2024-10-02 02:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 116.9 |
| a046f11a-6c78-3122-b478-bc3745834cd1 | -16.8491 | -55.892 | 2024-10-02 02:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 84.7 |
| 45086580-1014-38b3-bc0b-eaa7645dc3d1 | -20.0424 | -55.9738 | 2024-10-02 02:46:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 85.1 |
| 5c7ea46d-d3ca-39c3-ae1f-b1f50cddda3a | -21.3456 | -55.6841 | 2024-10-02 02:47:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 41d684da-e146-3528-88ab-b9468819b7c6 | -21.3656 | -55.7022 | 2024-10-02 02:47:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 7ae2a235-1b8a-3622-b065-f297cd164bf9 | -21.3661 | -55.6807 | 2024-10-02 02:47:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 120.3 |
| f1af811f-d691-3b9a-a464-91e3beb3f46f | -21.6069 | -50.8004 | 2024-10-02 02:47:05 | GOES-16 | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.2 |
| 1c363934-f363-308b-8e11-874fc89d9a9e | -21.6269 | -50.8187 | 2024-10-02 02:47:05 | GOES-16 | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 120.1 |
| 741b3c03-a295-313c-a870-91fcca92565f | -21.6275 | -50.796 | 2024-10-02 02:47:05 | GOES-16 | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 279.3 |
| 55e85ab0-f25d-35e8-8085-a0e0bc8729a3 | -22.3505 | -49.306 | 2024-10-02 02:47:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.8 |
| c3160d99-d830-31e7-b2fb-85f9d4f1428a | -22.3511 | -49.2827 | 2024-10-02 02:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.1 |
| e9a21b03-3061-3d44-9a5e-5a09be05b51b | -22.3713 | -49.3011 | 2024-10-02 02:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 231.6 |
| c1904469-b2cd-3d87-ae06-60321cba9b63 | -22.372 | -49.2777 | 2024-10-02 02:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 211.8 |
| b3d0ce84-0408-3d2b-a6f6-b4613cbfc6f6 | -22.3922 | -49.2961 | 2024-10-02 02:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 205.8 |
| 939ffe10-0d0d-3832-8cbb-7560d93a80ad | -22.3929 | -49.2727 | 2024-10-02 02:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 143.4 |
| b26eaba5-36a3-3666-ba92-0b745c8830ed | -22.9014 | -45.0779 | 2024-10-02 02:47:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.7 |
| f873c1b8-6a3c-30d7-b142-8c68b9dddb83 | -22.9006 | -45.1029 | 2024-10-02 02:47:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.2 |
| d2d7af18-1f22-3d4d-86a5-0dded3c254d0 | -23.175 | -49.5943 | 2024-10-02 02:47:13 | GOES-16 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 163.6 |
| ce89edbe-4e0f-39e8-84b4-ce73a5e8d73c | -23.196 | -49.5892 | 2024-10-02 02:47:13 | GOES-16 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.6 |
| 62b54fb3-0a53-3dbd-bde5-7a3f084f2ae5 | -3.1465 | -49.4229 | 2024-10-02 02:55:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 5a1be474-93b5-36bb-9a4e-8b90f3bfb10f | -3.2136 | -46.7843 | 2024-10-02 02:55:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 4c839f1a-7ebc-36f3-8138-60abdb8dced6 | -5.9788 | -45.3621 | 2024-10-02 02:55:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 9b2bf11b-bf79-3df6-bc5f-77d50eec0743 | -8.4643 | -62.7124 | 2024-10-02 02:55:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 2bbd586c-c02e-358b-bb32-ee2877f14add | -9.9554 | -64.8984 | 2024-10-02 02:56:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| a01d999a-1ffe-324a-8a29-8cde4dc6c9fe | -9.9553 | -64.9172 | 2024-10-02 02:56:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 8602e56a-342a-399a-9832-eb067e04b2aa | -9.9368 | -64.8991 | 2024-10-02 02:56:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.1 |
| d65f3190-ffc1-3ae9-8ebf-b7180367bdbb | -9.9367 | -64.9179 | 2024-10-02 02:56:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 110.4 |
| d33c5c31-377e-3918-9d8b-07504eff72e0 | -11.6743 | -64.9983 | 2024-10-02 02:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 9a2e40d0-8095-32e9-9b03-a607dd2939d6 | -11.6742 | -65.0172 | 2024-10-02 02:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| e5b41192-96bc-3fa4-8250-fda3536fb2b7 | -11.6556 | -64.9802 | 2024-10-02 02:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 43d68d51-6844-32cf-b475-f34c05b93929 | -12.2946 | -47.6446 | 2024-10-02 02:56:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| bd8256bf-ddc0-3c4c-b005-92869f072673 | -12.7054 | -63.0798 | 2024-10-02 02:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 3ee3a4fe-225f-3969-a11a-feb1da5e8438 | -12.6484 | -63.1214 | 2024-10-02 02:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 542d03d0-6c1a-304a-926b-15cf041f970a | -12.8803 | -62.531 | 2024-10-02 02:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| a426fa64-029a-3592-9dbd-4645eb164472 | -12.8614 | -62.5321 | 2024-10-02 02:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 131.0 |
| ae30a8d6-0a47-39db-ad8f-6ab4ba85a05f | -12.8612 | -62.5514 | 2024-10-02 02:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 88.2 |
| cff99db9-4964-3abb-8398-a8e98e250cf0 | -12.8593 | -62.7826 | 2024-10-02 02:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 6716ad0c-a2cb-3096-8a69-eafa0f3b9603 | -12.8424 | -62.5333 | 2024-10-02 02:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 120.5 |
| dd40a42c-faed-3b99-ad06-a49e6d401b3a | -12.8423 | -62.5526 | 2024-10-02 02:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 330b7a30-1806-3a35-aee1-b50c72caf914 | -13.198 | -48.6267 | 2024-10-02 02:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 2347ee81-238e-3539-a05a-3afed3e90dfb | -13.1984 | -48.6046 | 2024-10-02 02:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 85.6 |
| f3aa989a-6f3e-3eae-95a0-1d11e8126def | -13.2173 | -48.624 | 2024-10-02 02:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 165.9 |
| 25a3c2bd-f7c3-30e2-b081-30dd778a5845 | -13.2177 | -48.6019 | 2024-10-02 02:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 9df6a0cf-b6c8-3fd1-9e24-14b1b99e7a30 | -13.1122 | -51.4329 | 2024-10-02 02:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 59926c2e-e278-3d61-86b1-88c8562a70d6 | -13.0742 | -51.4163 | 2024-10-02 02:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| fa0eb724-c25f-367d-956a-cabc9282925b | -13.5965 | -51.1367 | 2024-10-02 02:56:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 538230df-3d28-3d92-9bb6-751800cae01f | -15.8933 | -57.1754 | 2024-10-02 02:56:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 4eed954e-7d37-3a03-8f59-7a1ae12d4d1b | -16.6127 | -57.217 | 2024-10-02 02:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.7 |
| 9a5df62e-55ec-3f29-9627-c5a64f4e5106 | -16.6124 | -57.2375 | 2024-10-02 02:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 4cba1384-8b5b-3ddb-ac9c-c5ea4b328215 | -16.6887 | -57.3513 | 2024-10-02 02:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.4 |
| d21ddbcb-3d47-36d4-bc0e-4cf5f939cba3 | -16.6884 | -57.3718 | 2024-10-02 02:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.6 |
| 19bd4f5d-b287-3fab-a4c4-8efece3930a1 | -16.6868 | -57.4741 | 2024-10-02 02:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.3 |
| dd2cbef0-4527-31aa-8bcd-9caee2b9a1df | -16.6717 | -57.1897 | 2024-10-02 02:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.1 |
| 4dca5a97-388c-35a0-ba31-bec3fded2969 | -16.6518 | -57.2125 | 2024-10-02 02:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.1 |
| 686420a0-a327-3b9c-840c-58fdd691eeaf | -16.6322 | -57.2147 | 2024-10-02 02:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.8 |
| 47a3ce51-f5a3-3c02-ab94-ae6557662aed | -16.6319 | -57.2352 | 2024-10-02 02:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.7 |
| f6c8c293-4a22-3c91-bbd4-2ca1c9fe3c3c | -16.8096 | -55.9177 | 2024-10-02 02:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.1 |
| d5d67097-d0d1-3e69-98e3-e12b7b0970c5 | -16.7461 | -57.4265 | 2024-10-02 02:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.7 |
| 57e089be-17e6-3aa9-9a1c-a6604492be54 | -16.7452 | -57.4878 | 2024-10-02 02:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.3 |
| ebfa729f-57cb-34da-a0ff-01dc343f06f1 | -16.7269 | -57.4083 | 2024-10-02 02:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.2 |
| fa3779a7-fa31-3287-9b05-d2f2ac125a24 | -16.7265 | -57.4287 | 2024-10-02 02:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.7 |
| bc999e7f-8708-326d-9e52-2ff60d40aa89 | -16.7111 | -57.1647 | 2024-10-02 02:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.4 |
| 1c29b3ff-361a-3b15-8dd2-0d14463bd3e5 | -16.7108 | -57.1852 | 2024-10-02 02:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.3 |
| 8fed96d4-ab0e-399f-ae30-c3c6dd60c7d5 | -16.7082 | -57.3491 | 2024-10-02 02:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.1 |
| 0440517f-fffb-331b-b0bf-e64ea74b57b7 | -16.7063 | -57.4718 | 2024-10-02 02:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.9 |
| 4969c987-90f6-31cd-944f-34dc9a6f3b9f | -16.6916 | -57.167 | 2024-10-02 02:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.2 |
| 1dcc1c49-dd5c-384c-a15d-a226f5e9027c | -16.6912 | -57.1875 | 2024-10-02 02:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 179.8 |
| df1680cd-cd8e-3126-8dc3-7aabb078e87e | -16.6909 | -57.208 | 2024-10-02 02:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.4 |
| e378a620-6167-39da-b69b-4392c382760f | -16.8698 | -55.8272 | 2024-10-02 02:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.2 |
| 9b4ed8a9-6932-36ec-bd17-ba4d31e70fab | -16.8695 | -55.848 | 2024-10-02 02:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 97.1 |
| 330cc166-3d2b-3243-aefe-0e584cd19193 | -16.8491 | -55.892 | 2024-10-02 02:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.3 |
| 5d520667-36a2-3bcc-93d3-cef8f4ae68fd | -16.8295 | -55.8945 | 2024-10-02 02:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 107.4 |
| 6ae83156-42db-3bb7-a77d-55b06a6c5dfe | -16.8292 | -55.9152 | 2024-10-02 02:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 118.9 |
| 9d2763e2-681c-3fae-bfcd-08c23ff21ba8 | -17.1581 | -56.1637 | 2024-10-02 02:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 79.5 |
| 4c334680-a01e-387c-9700-adafd1ad0471 | -17.1577 | -56.1844 | 2024-10-02 02:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.5 |
| 526b2767-93d2-397d-8427-3cc939a69857 | -17.0705 | -56.7114 | 2024-10-02 02:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.7 |
| c2eea697-69ee-39eb-81a4-bf25bb3da25c | -21.3451 | -55.7056 | 2024-10-02 02:57:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 69.3 |
| d57ad99f-203d-3d97-b1d9-cd49cb94aa2e | -21.3456 | -55.6841 | 2024-10-02 02:57:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 136.3 |


[Clique aqui para ver as próximas entradas](README47.md)
