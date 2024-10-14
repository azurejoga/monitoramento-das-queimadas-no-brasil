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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 450841b3-870c-370b-bbb7-58472b5a836f | -6.92602 | -47.47303 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5dae94c4-c76e-3ddb-8ab4-27e0a1a25e54 | -6.92298 | -47.46814 | 2024-10-14 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4560b25d-d142-33d5-91ac-00cf9e2872f2 | -6.91599 | -47.23603 | 2024-10-14 04:44:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b7529f8-d77a-372d-8946-d83c41b0a48b | -6.91048 | -47.22154 | 2024-10-14 04:44:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc98993b-a303-3fea-a490-b239f0b06373 | -6.90783 | -47.23938 | 2024-10-14 04:44:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17997ac2-2343-3001-a867-a2a6e9a6ca54 | -6.90673 | -47.22097 | 2024-10-14 04:44:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1887cbd1-2cf3-37ff-9e3d-d0dd1a4468f3 | -8.60413 | -48.62156 | 2024-10-14 04:44:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 278e5c44-62b6-3e24-bec9-7947491e2f99 | -8.5984 | -48.61776 | 2024-10-14 04:44:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 532c87ef-a804-376b-b04e-fc4970ddda95 | -8.48282 | -48.62122 | 2024-10-14 04:44:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 520db3cc-354b-3bd3-a148-b3009ebc3efe | -8.48159 | -48.62934 | 2024-10-14 04:44:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2dfdd5f7-e80a-38ae-bcba-b55457be1901 | -9.39055 | -47.89819 | 2024-10-14 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b92924d3-7e47-32a5-bf4b-a0d753f84017 | -9.19733 | -47.55885 | 2024-10-14 04:44:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cad9215-e9bd-3fb8-adfd-b688552b3924 | -9.11197 | -47.72152 | 2024-10-14 04:44:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d6ab01c-65e8-31e3-83ff-0a7fd401a5f0 | -9.10997 | -47.73513 | 2024-10-14 04:44:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef4ecabb-d567-3cdf-adb5-7dfa62e62373 | -9.09842 | -47.9425 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91520fe5-fe08-3b27-a1e9-f9a0ac33d04b | -9.09777 | -47.94689 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 622479ee-ca2b-3a5b-b04e-246df96a7d96 | -9.09732 | -47.92439 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 805df020-978d-3fe4-bae1-aa5a0cb8d28b | -9.09602 | -47.93316 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bbe515f3-6ae5-3fbe-8581-eea64d162836 | -9.09524 | -47.7835 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 566e9c91-d320-36f0-8811-6dc40ad46598 | -9.09472 | -47.94194 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d776cd4a-33b7-30cc-8253-47e109fcfa7f | -9.09361 | -47.92386 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 676659ed-433d-3307-853c-e2319f80b71b | -9.09102 | -47.9414 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 420d3938-227a-33d5-b5da-a25b3bcbb1d3 | -9.08777 | -47.78239 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7dd7693a-8b4c-364e-8887-cbae03b9c666 | -8.98498 | -47.75011 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4228735e-cc6a-38be-aa9b-1f0bdc03a24b | -8.98124 | -47.7495 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fb24ad23-9e9a-3c24-b2d7-8c2044c4ee8e | -8.97919 | -47.68465 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d38ac01e-c92d-3ec5-b280-9a8d25817923 | -8.9761 | -47.67955 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1cd24d0-fadf-3ede-8a00-42d24e94caed | -8.92082 | -47.91492 | 2024-10-14 04:44:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69ec6e5a-e942-34c4-8094-ffb3d224dd02 | -8.91779 | -47.90995 | 2024-10-14 04:44:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 15c25795-775f-3b1d-a1d7-3ddce794bc2b | -8.91039 | -47.90879 | 2024-10-14 04:44:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72086857-924e-3a22-8f51-40161c5d4aba | -8.80254 | -47.8591 | 2024-10-14 04:44:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8af93811-978a-3014-87c5-739c33fe534e | -8.43028 | -47.98187 | 2024-10-14 04:44:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe68320c-1682-3a8f-8cb1-4557ca5b9ccb | -9.30222 | -48.24846 | 2024-10-14 04:44:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ab1593c-fa64-3b89-8920-3ef24eeaa6d4 | -9.30168 | -48.25101 | 2024-10-14 04:44:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 287eaa26-3bec-311f-81b9-4c5b5c601e80 | -9.11737 | -48.68655 | 2024-10-14 04:44:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aec28af5-1f9a-3890-b471-1a43d7798da0 | -9.09898 | -47.78407 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 528c91fd-ce2b-31dc-a494-f2de37c17b9f | -9.09667 | -47.92877 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3bc4553c-c313-3d14-b834-50a48e5b4373 | -9.09537 | -47.93755 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2452b45c-eb00-352f-86aa-07f95aa37ce9 | -9.09426 | -47.91947 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbfd137f-bd63-396a-af63-6070f074721c | -9.09407 | -47.94633 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8dc0c0db-5323-3896-b2e2-a994e620e5ce | -9.09296 | -47.92825 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3d8a9150-72d4-385e-baee-b59fdeaa9afa | -9.09166 | -47.93702 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5bacb9d1-b45b-3d0d-86bf-9634fcdff76c | -9.08796 | -47.93649 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c8ef05a-2180-3770-93ba-c94fd35da186 | -9.08404 | -47.78185 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cca8a9b-554c-3e48-a23a-39722c200e00 | -9.0539 | -47.7236 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8003d93-5ed0-3cdf-b46f-e47632439c85 | -8.97985 | -47.68011 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fd02f77-6105-370a-8583-c3bf158de100 | -8.91959 | -47.91267 | 2024-10-14 04:44:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 60e8d68a-9c0d-37e1-a8d7-67becb238298 | -8.91713 | -47.91433 | 2024-10-14 04:44:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 741d5d20-e851-3dec-8845-7cad4ffdfdf9 | -8.90974 | -47.91317 | 2024-10-14 04:44:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b338975f-6dc2-39e4-87e8-ba3be06bbce0 | -8.90604 | -47.9126 | 2024-10-14 04:44:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| adca7e91-2639-37a7-afe9-342a58353176 | -8.80188 | -47.86353 | 2024-10-14 04:44:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4127893-3432-30d7-b41a-c7e8c1816724 | -8.70349 | -48.07059 | 2024-10-14 04:44:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a549ff51-f578-3205-b002-9cc01b1b66d4 | -8.60195 | -48.61831 | 2024-10-14 04:44:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 403e16bf-a109-3648-b8e2-3b935bbd3ab0 | -8.60133 | -48.62243 | 2024-10-14 04:44:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ece45fc6-039e-3a5c-a1a4-152df1706ab2 | -8.60117 | -48.61689 | 2024-10-14 04:44:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5163851b-8a2d-352a-8df4-e61860195126 | -8.60057 | -48.62099 | 2024-10-14 04:44:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 90b4de81-dd18-3f36-aada-85939d2f94d0 | -8.4822 | -48.62528 | 2024-10-14 04:44:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a4c45c58-7512-3f69-af93-606e73caecd9 | -8.47927 | -48.62066 | 2024-10-14 04:44:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7c805590-17fc-38c0-8439-44512a0070b5 | -8.47865 | -48.62473 | 2024-10-14 04:44:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4979b06d-21f8-3ec4-9e44-6c3b49b0722f | -8.44519 | -48.03241 | 2024-10-14 04:44:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eae07b51-69c1-3fbd-ba07-a87977d0d81d | -8.42662 | -47.98129 | 2024-10-14 04:44:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7762f85-abc0-32bb-8d3a-8d48d68174ed | -9.49997 | -48.67214 | 2024-10-14 04:44:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 727b9705-e645-3f4d-bdbe-c5fd120adbda | -9.56222 | -47.6949 | 2024-10-14 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4321189c-c9ce-366f-8170-1370e0349aec | -9.53928 | -47.79898 | 2024-10-14 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e49b621-46bc-3cde-9961-b12cb37c5824 | -9.52363 | -47.80111 | 2024-10-14 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50343595-39e9-33b7-95da-a2df2955343f | -9.50356 | -48.67265 | 2024-10-14 04:44:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13892e47-54f4-304a-8aaf-486fbb68e1bb | -9.566 | -47.69543 | 2024-10-14 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2b3540d-69c8-3879-8bb7-74b521a6a7a9 | -9.53512 | -47.61533 | 2024-10-14 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 441b30b7-3e64-3540-9736-1d459774574d | -9.53445 | -47.62001 | 2024-10-14 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4298cf7f-3d8e-3740-ad73-f539e24a0ef3 | -9.53176 | -47.63867 | 2024-10-14 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37b020fe-1f57-3a93-b4b9-3efe1460b178 | -9.53066 | -47.61947 | 2024-10-14 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9fdb1c1-ffff-3e74-9025-5bba4b61b38c | -9.50274 | -47.8395 | 2024-10-14 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0639ccda-0969-3766-a003-82f520e5164b | -2.11048 | -47.98458 | 2024-10-14 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3830619-a234-3074-8aa3-bc3d8b27c5c8 | -2.10808 | -47.98493 | 2024-10-14 04:44:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f76ba731-a1bd-3b24-a6a1-a8f03c5328a8 | -2.10704 | -47.98406 | 2024-10-14 04:44:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 435b2b58-da1c-38a1-8f98-0dda1ff7e372 | -3.22159 | -48.91938 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2fb330e-ee3b-3bea-a966-8fee8ac2aa49 | -3.22103 | -48.92294 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ddb04971-7559-3cde-8752-f9cbbcbc4bd5 | -3.21822 | -48.91886 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 00b3d6b7-1cac-3040-ba7c-8ea9477cb7d4 | -3.21766 | -48.92242 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c0a6672-de64-3aaa-aee9-d98aa2637f07 | -3.13067 | -48.60718 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a1b7280-c033-38ba-b4a4-d099ed6b6213 | -3.13011 | -48.61079 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3336a5b5-9add-350c-97a4-6015cc0d431a | -3.12727 | -48.60666 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36ddf0cf-3611-396d-9917-a936a9a2b30b | -3.12671 | -48.61028 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5114c31e-b20d-37ca-896f-649ba108d36c | -3.11316 | -48.63041 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edbd3c79-e1f0-3f69-9d6c-2873c5122443 | -3.11085 | -48.60042 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1362303f-2556-30f3-b0db-6f6cb15380ba | -3.0852 | -47.78151 | 2024-10-14 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44f25d83-f69a-351d-ad75-6398504afdca | -3.06237 | -47.48661 | 2024-10-14 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54a92896-bf54-3abd-bad4-055041178c46 | -3.06177 | -47.49057 | 2024-10-14 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1113f91a-c533-36c5-9d13-9503bb6acfc2 | -3.05823 | -47.49002 | 2024-10-14 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8579608-5523-35df-8354-2a1a21b3dc57 | -2.99632 | -48.07877 | 2024-10-14 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75dfb491-05d5-361d-8015-d5268376cd04 | -2.98758 | -48.72214 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10054ffc-9313-3f06-97b9-233cf9c7e419 | -2.98376 | -48.58541 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4afee8d5-89a6-3f66-b3e1-7e709e94561b | -2.95037 | -48.50974 | 2024-10-14 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7167fcf-9b6f-3e07-adc7-01c47c91dd93 | -2.9117 | -48.91174 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2448fcfb-db4f-3f59-a9fd-ca6d0138c31c | -2.90834 | -48.91121 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f82a91e9-0bb0-389d-abb9-0860f9626dc4 | -2.8854 | -48.61459 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4fe5f1b-3f48-379c-89c5-aa22df3800f3 | -2.87469 | -48.906 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 47f15a56-b196-3c35-b6a2-f0f500a99b05 | -2.87413 | -48.90955 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2be20782-b16b-3f8a-87a7-cf2264e9ad2a | -2.79497 | -48.56799 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ef989dc-b7c7-376a-a556-f736deb4dc37 | -2.79441 | -48.57161 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README79.md)
