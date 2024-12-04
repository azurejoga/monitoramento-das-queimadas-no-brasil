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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aad39fe0-7755-3848-a365-a63955866372 | -3.26728 | -45.37555 | 2024-12-04 05:03:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cf054702-4708-3a27-85c9-bbc29dbb9677 | -3.02871 | -53.87597 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b256070-0151-3e02-bdc4-6184b35e3af3 | -2.75061 | -54.39557 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 374aef0a-ec34-394b-9f7d-a05d7fdd5416 | -3.21769 | -53.63565 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5207a6a-b5d6-3b46-a4d8-c4d3c34590cc | -2.3633 | -53.86847 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b690d2d0-b231-34c8-ac7e-e2676a8a09eb | -3.20036 | -53.42689 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb4645aa-3faf-33ed-93e4-3623ad947dce | -3.24892 | -46.28292 | 2024-12-04 05:03:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62eba4b8-b9e4-38f3-b32e-eba615c40846 | -2.95499 | -51.69251 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61fbf721-c18f-3cb1-ba51-b38560491222 | -3.08487 | -53.37956 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7013a98-f64b-3448-b3e2-138d839f4e5a | -3.2708 | -53.65133 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4ad0f1a5-e7c2-355a-b632-070db443d607 | -2.64476 | -54.28963 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03b0036d-2f08-38cd-a2f3-d19c3d3f5888 | -1.94962 | -51.20807 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 744e7c63-d398-3703-8193-3e8bb094f7f2 | -3.37421 | -51.06671 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9e21f479-5121-37a0-8fe2-fb3ac1cfa790 | -2.45507 | -53.66772 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 57fc4cda-c768-3e9b-b7ba-70d5cc354211 | -1.48983 | -54.43314 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df2d80c6-9fd5-3804-995d-a76f3d7e3f47 | -3.02392 | -54.039 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 078df64a-bbd0-311d-acf8-7586490b9229 | -2.47368 | -53.7036 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be4ed75d-647c-3ba9-9f6d-823c23dce2ed | -3.85379 | -52.15864 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9b5746bc-ad23-310c-b0a7-9585555ed6c7 | -3.76423 | -52.08178 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a68bd8e-f2e0-3ca5-aad5-1dbdbe9526ae | -2.52242 | -51.80236 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4701f108-4310-34d2-b666-50239afd23a2 | -2.88957 | -54.15919 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9497c28c-3e3a-32b8-bdf0-db0788a17292 | -3.036 | -53.42477 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ee8ac5d-b5d4-3988-9ad9-0274173f7e85 | -3.08544 | -53.37588 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b661ebd6-52aa-3aca-ba05-c133d427b147 | -2.86748 | -54.01505 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d5caf771-74d1-359e-8c09-260be4ebd508 | -3.19414 | -50.29565 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a170cb5c-3484-344e-ab2a-4bc24a9b45e4 | -2.76005 | -54.00587 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84971b97-1b5b-3b3c-b29e-dd4d67bc878e | -3.53817 | -50.38718 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d38cec6-722e-3962-8a99-3f72136dc13a | -2.79046 | -55.36126 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5415d3ec-a0b0-3755-ba47-31151a4f20b6 | -2.42371 | -54.02618 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1f671c0-3739-3e79-bfbf-5cbd80135897 | -2.52711 | -54.03844 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 911d98cb-7cef-383c-8eb8-9df234bf5abc | -2.69569 | -51.86623 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9710c7b9-f78b-3f00-b26b-b24dad42f261 | -2.81389 | -53.04543 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4c27badd-70e4-3ecb-93d8-9b5e6d4ca145 | -3.27023 | -53.65498 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9d21ab03-1a56-3a28-9380-f2b61fb937eb | -2.80757 | -53.04059 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8b88bb88-d5d5-357a-8ff8-4c2eaa1b0858 | -3.01833 | -54.0309 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bc54d4a-f590-3425-a603-81d88762e056 | -2.90395 | -51.58181 | 2024-12-04 05:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf3ccde3-adc9-3766-b61c-e0b2d0827eb8 | -2.60346 | -48.25903 | 2024-12-04 05:03:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0f261ec-e10d-3f55-83b9-2a6e5c4b795b | -2.23264 | -53.6993 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 63b7a8e0-7cf1-3838-818d-fbd2c474dcf3 | -3.12145 | -53.27911 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3921c4cb-f767-390f-bde4-fa8249ba67ee | -1.45781 | -60.16477 | 2024-12-04 05:03:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69a6d1df-971e-3215-8eb2-3fb8812aefed | -3.02109 | -54.01318 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cfe0907-993e-3581-8b46-053beb7501dc | -2.99568 | -53.88918 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b42a129-25f8-3611-9e3a-887cc720d1ad | -3.2943 | -53.71012 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee31b71e-0303-3e9c-b627-1a981767740f | -2.35995 | -53.86796 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acaf2f10-47d2-3fc8-944c-e167b82b9d96 | -2.87956 | -53.93703 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3de3c10-1177-3f52-94c8-a85f33506106 | -1.47864 | -53.80495 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1733e9c-1cf6-3de2-aa00-64a0c51fe35e | -1.81248 | -52.73376 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6202ae5-18bc-39fa-a0a5-1ba6ab73f92d | -3.11982 | -54.62334 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| a1fcc3be-faf1-3b26-940d-f4fc31053e60 | -1.90381 | -52.85228 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b62ea22-7a0b-33f8-8e7d-ac8f2d83e5dc | -2.56519 | -54.34158 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91ed256e-0379-3715-a73b-d62b109561bd | -3.11509 | -53.97643 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 679df346-0e6f-33d7-ac11-45da9b51f469 | -3.05476 | -53.43897 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76db09d6-3e12-3686-adbe-c69697ab16e6 | -3.2623 | -53.61652 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 602f6cad-b977-385b-a044-6a567869a76d | -3.49129 | -53.97949 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74269c04-af90-38e0-8db9-5873edfbb8d3 | -4.08083 | -46.69073 | 2024-12-04 05:03:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28b93b23-bce8-3ba4-9eeb-4a1b4055f9d5 | -3.04773 | -54.05686 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9a7d479-46ab-382b-a347-ea57c2be0651 | -3.02278 | -54.02433 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e559863c-fd9d-39fa-af22-7a400734865e | -2.68812 | -54.27179 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30daece5-66d5-32a3-baf3-5c29cdc6f231 | -2.37801 | -53.66287 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1031b1fb-802c-337b-a4a5-c0aa8a985cd7 | -2.81299 | -54.05731 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 434990ed-6324-38ae-b1cb-1f54716dc68f | -1.81351 | -52.73469 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f8ae7d0-4239-3af4-b42e-9c93f9c478bd | -3.92267 | -52.387 | 2024-12-04 05:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 083d1218-0e96-3718-ace4-5688973382ed | -1.66329 | -52.28526 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d43be73b-df34-360b-8851-4a1a75e5e138 | -3.25461 | -50.61587 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfa61fba-29a9-3680-afa1-ebbbe4c9d388 | -3.31415 | -50.43584 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2d2234b-1cd8-314f-81d1-47ee9a73703d | -3.28272 | -54.14371 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c214c0c-a4ad-34bd-b63d-a6069cb30e2a | -0.34882 | -48.43833 | 2024-12-04 05:03:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 014b0003-5572-3189-af02-59873cf10f2e | -1.17345 | -53.42438 | 2024-12-04 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 983bf466-d3fd-312e-a710-88c2c059eb35 | -2.83989 | -54.10477 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78fe8cc6-cb40-3f78-b474-2b27dd53931e | -3.17822 | -53.63682 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26fd7f69-a8e2-39ea-b4a1-cdc64d3a4bcd | -2.41413 | -54.15398 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa3938e7-7ee9-3ab9-904d-9ce99383a9f8 | -3.25838 | -53.66431 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d258ac7-3a1a-39f3-9e36-c1e961db0772 | -2.81102 | -53.04113 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 282f8d14-84cf-3a64-87c4-6a4d6d4a7277 | -3.03596 | -54.04417 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0d73387d-da7b-3dfa-9be7-a7374e991c38 | -2.79209 | -53.00341 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e836d2f7-fd58-3b5d-bf50-84c29a29dec9 | -1.70735 | -52.78032 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89a986fd-6b6d-3fec-98a9-e540dc45e5b6 | -3.28464 | -50.63084 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89107c6f-6fb6-3402-8da1-ed7c0314fa7e | -1.65967 | -52.75065 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 336b27f1-9330-38cb-aaba-f78cc0d45c3a | -3.51885 | -51.30891 | 2024-12-04 05:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a1f4666-21b0-33de-a0cc-d0e7a779c207 | -3.05359 | -54.48116 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 862284e5-3ddb-3d17-b909-e7bea1a507fd | -2.78992 | -55.3647 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 018833ef-97c5-3d45-a5a3-2834d9b81f3f | -3.24288 | -53.8759 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0becba6-8bfe-39e1-9c99-c7d3cbc6298f | -2.98053 | -53.87587 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fa0318d-6f78-3db7-8460-70cb46fcdcfd | -2.2633 | -53.61238 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2742b8a9-c9e1-3105-99bb-5dcf614ab4ca | -2.94386 | -51.01691 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2403a4e3-f64d-33ab-b791-84986b088e14 | -2.69789 | -52.90826 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1295cb9-6575-30e7-a9e0-2e04042ab5fa | -3.88108 | -51.97727 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ccab4cac-29f4-31d9-8439-7afa356c576f | -1.33575 | -54.96124 | 2024-12-04 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2e59857-6656-3812-8931-ff526efda5c2 | -3.24343 | -53.87231 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd6e393d-a5fe-3715-b87c-422a49baf764 | -3.7205 | -51.79848 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97a71857-5d88-3e1a-b9b1-56d22c4cf4c1 | -2.88087 | -54.01712 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1aeff5a6-6c54-398a-b713-0470b3673337 | -4.26474 | -50.68067 | 2024-12-04 05:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2f93577-c0e7-3a03-8398-93ce1cdf6575 | -1.65274 | -52.04748 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 680e2b0f-7ee8-3250-8e79-94ecd78114c0 | -2.26385 | -53.60878 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04dbdef6-d9d3-3106-8076-d7aa7738fa60 | -1.97958 | -51.16204 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 034c96da-410d-391a-8624-4adff766cdd0 | -3.08319 | -53.06969 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0114561c-91f8-39f5-a33b-9a18a38ec9c7 | -2.80683 | -53.9697 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c8418f1-d959-347c-9a94-b099d7634471 | -3.02814 | -54.18385 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dea533d7-a948-36fb-9e9a-2f79e706c7cb | -2.80385 | -54.13882 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7784c008-2b57-3d25-89ec-3e2700350b19 | -3.20214 | -50.64644 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README37.md)
