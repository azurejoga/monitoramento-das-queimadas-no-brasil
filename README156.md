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

## Dados Diários - Página 156

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 116b839b-cf7b-33bb-955d-0d15f433c580 | -2.22732 | -50.71151 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 5450d91f-395d-35fc-8968-a15dd608084f | -2.22453 | -50.71548 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 79687856-b080-3acb-b965-9aa00a59193c | -2.22302 | -50.46229 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c51c117d-cf0d-3436-b718-c332961fffe2 | -2.20889 | -50.83484 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e34a42c0-551b-3357-9924-2a1f3d001561 | -2.20715 | -50.75716 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4d19a13-71f9-3919-ae08-9e8466953210 | -2.20565 | -50.63657 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e34c4d0d-ccfc-3e67-8860-a323bc1222e9 | -2.18482 | -50.50053 | 2024-10-25 16:52:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| c6bd93fd-5ef0-363c-9f6d-85a580cde588 | -2.18202 | -50.50454 | 2024-10-25 16:52:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| c0244626-93de-355a-ac56-aa50670ea004 | -2.18149 | -50.50104 | 2024-10-25 16:52:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| bd391b60-b0c2-3b6f-83c0-ba5700f7eaa1 | -2.17816 | -50.50155 | 2024-10-25 16:52:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e443483a-0934-3055-a83c-b99be8fa3de6 | -2.17525 | -50.52703 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88b86603-6ab4-3b31-a906-74714a75ec3a | -2.17192 | -50.52754 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e4e0b281-15e7-3f5b-8d13-ea29ca234f18 | -2.16859 | -50.52805 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 00cbc454-10fc-33d4-ab69-dcd1225983e2 | -2.15774 | -50.47961 | 2024-10-25 16:52:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c7909bdb-9332-3745-81bf-0efa3c04ce5c | -3.63575 | -51.24704 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6f2eac64-f8fe-3b74-8cb9-6705071c4ff3 | -3.59521 | -51.38425 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d0798d77-9ee0-3009-9e66-fbbb44ea4ee9 | -3.5158 | -51.02008 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4518e1cf-9c2b-321f-9c86-25dc047b6879 | -3.5125 | -51.02058 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f8f1e4e9-e5fa-3cb3-bdf2-eb0586ed5901 | -3.3346 | -50.81622 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4973f7e2-db64-34d3-8d6c-b3dbfaec83df | -3.29703 | -50.74785 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6995aa1d-8d4a-36b0-baa7-6cab065f38f6 | -3.29373 | -50.74836 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bf281da7-e32f-3b85-bb8f-80cf11112064 | -3.2932 | -50.74491 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 420e3cd8-ea58-38d1-9f6c-faeff389857b | -3.26713 | -50.7736 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3b2ddba2-b7bc-33c3-b316-0d366018e07c | -3.26435 | -50.77755 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c708ac41-f775-3b4d-a5fa-fbdd2574ebeb | -3.26382 | -50.7741 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 722d46ec-ea1d-33a4-9d42-751219e604f4 | -3.24188 | -50.85151 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 858360a1-35f3-3807-852d-82d9e30e8571 | -3.24135 | -50.84807 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 421eda67-4d26-376b-9731-8254c7d47edc | -3.13388 | -50.61441 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 71db8db5-19a9-3032-b1c7-c93bbf467cea | -3.1295 | -50.60799 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2e79771a-12fe-384f-854c-4c37eae2bc1c | -3.12897 | -50.60454 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3c12df1c-d6f7-3195-a354-e348334b6205 | -3.12618 | -50.60849 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 666c0e52-31c9-381f-b1a9-41e7a11b6c3b | -3.12512 | -50.60158 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 714961f6-09c5-3528-b37f-ad7ef2a0751d | -3.12458 | -50.59812 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 9a14bcbd-61af-393d-ab1c-65c86c768e86 | -3.1218 | -50.60208 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 40323cce-6327-36b8-b9b7-b4a490c724bb | -3.11849 | -50.60257 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| a6fde16f-25d2-36f8-8953-a5f50a789185 | -3.11517 | -50.60308 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 8d45c116-c575-3805-bf9d-5ef2b429f37a | -2.57873 | -51.851 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 91076de2-55a6-30e2-872e-0ea921282f8b | -2.57542 | -51.85151 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| b041eced-e9b2-393c-b47e-b15ebe7297c0 | -2.32715 | -51.65067 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f0e21d25-1da7-30df-9b04-9ae8f09cc818 | -2.52872 | -50.50373 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 9448aa85-d16b-3796-9b62-380b3e39be18 | -2.41407 | -50.44334 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4a057bbd-1e39-3a6a-8fc2-eba7daa4841c | -2.40139 | -50.42736 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ad4e924b-0cfb-3c59-8441-3f1980056bd2 | -2.31971 | -50.4506 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9885a911-4c09-323e-8887-b1be570ea582 | -2.31243 | -50.46962 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0b4ae5a6-ea2e-3f34-b180-63ce78b2d8ed | -2.309 | -50.46706 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 445d025f-05bd-38bf-b8f7-e5fbf991de48 | -2.30608 | -50.49255 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 05608425-6626-340f-ad91-1c7861228258 | -2.29523 | -50.84265 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 617e0a1c-a3c9-3b95-8f72-8ee9c51343d2 | -2.28978 | -50.43057 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9f5db185-5622-30ed-9f57-c164520c30a9 | -2.23382 | -50.73181 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| bc9cc76c-abaf-3442-ba53-e79e38270abf | -2.2317 | -50.71794 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 504e56fb-9cd4-3221-b771-fe2af8106da8 | -3.2757 | -51.07163 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| de59a027-3945-362c-9183-e0b1600d36dd | -3.21516 | -51.01133 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dd2160f1-9251-3b71-9c57-32d922ab28f0 | -3.19903 | -51.0384 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7a01591b-cada-30f3-b1dd-bc6c4ce364fb | -3.19735 | -51.36292 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 14e91860-84f9-3d32-945e-cf7eca61c39f | -3.19616 | -51.21812 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cb1856f6-1c27-33c5-adfb-5d2911655ba9 | -3.16904 | -51.24421 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e18bd491-0733-3e03-adc5-932f61cd7f68 | -3.09576 | -51.34327 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 483451d8-dfe2-36c9-93d3-53b02de790e6 | -3.09246 | -51.34377 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| f2e7f261-d1e4-34fd-a8fc-793ecedd3d3c | -3.08701 | -51.26019 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f6f868ff-37f5-3eb4-ae77-6fe385c7a7cc | -3.08367 | -51.2643 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4c67623-94a6-35c0-9371-9363ca1f26b8 | -3.08314 | -51.26086 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 71b785ff-2383-3384-83a3-8ef8b7908840 | -3.07984 | -51.26136 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3d8ebe97-e569-3edb-adb5-450fc6ce8be4 | -3.05214 | -51.21286 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| a91c8061-05a1-39e0-b0eb-5ef1db80e1e1 | -3.04884 | -51.21337 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 08b0d323-c357-3ec7-9d82-d2eb56c2e0b1 | -3.0306 | -51.22667 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| e90ab438-ddfa-3572-ae6a-c8d0f9d48ef3 | -3.02678 | -51.22374 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 857d499a-6709-386b-90c2-a4c1dab19765 | -2.91776 | -51.00213 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 73da57b7-cc79-3d71-bd85-42699bb41ddf | -2.8598 | -51.59872 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 83375223-9904-377b-855b-ffa048b5de29 | -2.85265 | -51.28703 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 866ddcbe-e0ad-3774-8ff7-590c44acea3c | -2.83753 | -51.81081 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0ecc5023-648d-3014-8d69-115d20455e33 | -2.83422 | -51.81131 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 066a2cc6-5428-3701-8148-410484bc54e7 | -2.83369 | -51.80786 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 49df04e3-c957-324b-8e66-6eb10b4281b2 | -2.83091 | -51.81181 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 647c2d28-07de-3948-ae48-cf72ddf07c41 | -2.81761 | -51.34503 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 112c3219-61dd-39d4-a21d-b6169a991607 | -2.81484 | -51.34896 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 05cbf630-df4b-3fbc-9a5e-6ccca313982d | -2.81379 | -51.3421 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b5f4a3b0-fd30-3455-8771-4fcf0d551743 | -2.81206 | -51.3529 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7e0e89f3-c149-3222-80b9-45a88c1a44d9 | -2.80981 | -51.36027 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 18d3acf2-b817-300a-9102-2d9b8075107c | -2.80928 | -51.35683 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1fe92866-b68a-35d4-91cb-877cceff4bd1 | -2.80703 | -51.3642 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 114d1841-5692-3ac9-9426-71debeabe4ab | -2.80651 | -51.36077 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 742ed149-a2c4-30d7-b373-038fd347afa8 | -2.8032 | -51.36127 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 49f57f32-1399-300e-8ef4-c1062e21e0b0 | -2.80152 | -51.59782 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 574e1433-cce1-3475-b713-44c191d1d719 | -2.7933 | -51.36277 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bc568ed4-dce9-3c1b-b050-8202ff6243fb | -2.76868 | -51.95911 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 034107f7-16fb-359c-8f9e-3f21304b5524 | -2.75025 | -51.97271 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 18fa7137-a55c-36cc-a894-2dda19039231 | -2.74746 | -51.97667 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c0854da8-d266-3b9b-82a5-3e4d5d692ae6 | -2.71558 | -51.79064 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a50a92c5-1c5b-32ed-b629-57b9b55c67b4 | -2.71325 | -51.97474 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 9a58f0e2-ac27-37af-8379-928258edba8f | -2.90013 | -50.70757 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ba11b311-02fb-35fe-a63c-1e9c5c1a0d24 | -2.58267 | -50.63425 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04624bde-129b-3545-9096-b1853c959254 | -2.59591 | -51.36218 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 513bbffd-289d-3106-97d5-af31483b553b | -2.55559 | -51.23132 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0987eab0-fc11-367b-ae40-ed78ace41f7c | -2.46489 | -51.3057 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d3f8c29b-2fba-309e-9f26-3e57d00974f5 | -2.39747 | -51.28849 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2889379f-1510-3b62-8ffe-6d67b521ca45 | -2.38651 | -51.28313 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 975f0c56-cd4f-3186-ad44-71782b5ad5b9 | -2.34146 | -50.94513 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3d88863a-e74d-3969-83cf-f625febbef0f | -2.33815 | -50.94563 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 8c9ab3e6-50b0-357a-b4b7-69e594552f3f | -2.32836 | -50.92594 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 345749a7-db3a-384a-860a-42aa2430a3bc | -2.32505 | -50.92645 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README157.md)
