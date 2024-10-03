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

## Dados Diários - Página 198

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42d118c6-b37c-3a36-8fc5-39197722ef95 | -9.99227 | -68.78329 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95712437-09b1-3cf3-8188-0bd17b00de65 | -10.92632 | -69.77995 | 2024-10-03 06:10:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b264b67-c29e-3953-b304-a3bbe71f051b | -10.82588 | -69.60239 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1b085cba-91cb-3cf0-a406-6806dbb046cd | -10.84569 | -69.56728 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6327c813-ac35-348f-909a-3ec0c2fe0e5a | -10.84631 | -69.56313 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b1adc46-93ee-330b-8e26-a1231f97c7c1 | -10.86064 | -69.65684 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f0e7318-77db-3c92-bb57-46dac4e875a6 | -10.91716 | -69.36563 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd9df1c9-de24-37c8-827f-5c476f56757d | -10.92078 | -69.36616 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1b64bab-d89a-3847-aa79-d7051499624d | -10.1662 | -69.36192 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2be3c40f-500a-30e6-800b-42c7379bb77a | -10.16979 | -69.36243 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| daee8d9a-72f2-3807-b5f1-2922ffee0bcc | -10.17269 | -69.1317 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6de8081e-c360-3705-9003-0d447ab5f022 | -10.19556 | -69.36206 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 166b7fa9-8f26-3a74-87a5-24dfe39581c9 | -10.2765 | -69.44944 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc6e2149-df97-3353-b53b-bd779802669c | -10.42937 | -69.19543 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b1ad719-d1bd-33ef-9267-7774933574f0 | -10.47801 | -69.26818 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f58b58f8-ef3c-3212-a7c1-7ca57b886ab1 | -10.49631 | -69.45502 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ed181ad-994d-3783-9ec1-d8a8426db65e | -10.50481 | -69.1629 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9f0a2ed2-e20c-333d-bca1-1c979485e8a7 | -10.50539 | -69.16174 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3674086f-03d6-3976-8980-76eafcf1f684 | -10.51735 | -69.2337 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4080f6ae-c959-30e9-aafb-e318b6cdd1b2 | -10.52098 | -69.23425 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 003e1255-d419-303a-862a-e409dca003bb | -10.53695 | -69.32803 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 773deb6f-3cb3-3995-82a3-603950399a83 | -10.53717 | -69.27589 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f22a3c91-8bb8-356d-89b6-a6f925a25c19 | -10.53944 | -69.31101 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a75fee6-d98f-3776-ab9e-0abff46a0eff | -10.53994 | -69.33277 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3700a56-0e3f-352b-a8d2-fd0114adfba8 | -10.54057 | -69.32854 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 544425fb-5b8c-3d67-a4b7-c995bcb3a003 | -10.54181 | -69.32002 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 14876839-f8bb-3b76-af19-d9ec0c254539 | -10.54703 | -69.23374 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eaa27f95-cfbd-37be-a8be-05dd131be8ed | -10.55128 | -69.23005 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff2699a2-1c82-317e-adce-f3541543dc0c | -10.5603 | -69.2445 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e487d0e2-8d1b-301b-ac79-50a33bfc781f | -10.56547 | -69.18387 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d20eee13-0586-38e8-bbf3-7a7d71962335 | -10.5661 | -69.17957 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c2c84aa-f2d9-3e67-90f9-8a53fe1affbf | -10.5663 | -69.44231 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83a82dbd-21ed-3f50-a863-d252cd66e628 | -10.56825 | -69.44021 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60af5acc-d727-3024-9a7d-1b202aa0d0cc | -10.57409 | -69.43922 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2952371c-0151-3a52-9ec6-04fc943297e6 | -10.57469 | -69.43505 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e737267-92df-3613-b288-005cc572de88 | -10.57828 | -69.43562 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e38cddb3-ccf0-362c-b9a5-48e633deda74 | -10.62786 | -69.6464 | 2024-10-03 06:10:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97d29134-2d97-3e9f-a9b3-a6bd8e25ef18 | -10.65281 | -69.64445 | 2024-10-03 06:10:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66404a1e-2fef-3e75-b4ba-e80d04f6d000 | -10.65578 | -69.64911 | 2024-10-03 06:10:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 940fba2d-9db9-346c-a33e-aa27320ec70b | -10.66778 | -69.30236 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d44f588-c2cd-3377-832e-9eca3d139105 | -10.6714 | -69.30289 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 139900fc-be64-3364-b4ad-8c9506781468 | -10.67204 | -69.29857 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91089707-242a-3d04-b8f2-f9a9443300b8 | -10.70966 | -69.47943 | 2024-10-03 06:10:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7203c969-b726-3f29-ba25-b0faffcc950e | -10.71215 | -69.43699 | 2024-10-03 06:10:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ef6a4ce-c811-3c85-8e13-3f25f3caf99e | -10.71575 | -69.43755 | 2024-10-03 06:10:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54b2ace7-bab6-383d-adbe-7696ea07cc82 | -10.71587 | -69.61205 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ef79f2e-a26c-36c9-a460-4fd4d92c51c3 | -10.71941 | -69.41234 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd97b93f-dde0-347d-8649-53abab4dccc6 | -10.72003 | -69.40809 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 747f9253-b128-3acb-8ddc-da9195302e18 | -10.7202 | -69.55772 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf732bb1-33fd-3923-94f6-2263e6351b19 | -10.7227 | -69.31313 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eee6c894-171b-38bc-8e90-5fe7972cc1ac | -10.72632 | -69.31371 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f8d0898-de2d-346d-87e2-983ad8f29455 | -10.12233 | -69.14585 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52a5a8f5-bf65-36ed-9c62-e59e32afcdc7 | -10.15783 | -69.34358 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc8196ad-d98d-3b16-86eb-6c72ecb209ba | -10.15844 | -69.33937 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd5d9528-5895-3c15-ac48-4f3085dd5a0e | -10.16867 | -69.31947 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f38a124d-fa24-336c-a450-5bdfc012aa9a | -10.1704 | -69.35825 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1d799eb-b732-3e4a-8d9b-d2ab0bc6d931 | -10.1825 | -69.11573 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1300dd4-20bb-3e89-9be2-ce4524b58299 | -10.18651 | -69.11864 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad8675a6-8f7f-3fb8-ba53-af47992a1080 | -10.19015 | -69.11918 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d87a6ba8-0a19-3d8d-8d48-4d929bb412f6 | -10.19318 | -69.35317 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b42a6ef9-7072-3db0-8138-2e134d4cd6a1 | -10.42007 | -69.70365 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48ef3395-823f-3cc0-b9b5-4d198c0ddc10 | -10.42016 | -69.70439 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 694f046c-f9ab-35c8-944b-09b3681058d0 | -10.45003 | -69.18108 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f9b91c9-1fbd-36de-ab46-b61ab0091901 | -10.45304 | -69.18594 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 912bf5de-2df5-3b74-a27b-63135873fd50 | -10.45367 | -69.18165 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c3adbd9-da93-3dbe-bd51-8b6dac925fd5 | -10.4667 | -69.73148 | 2024-10-03 06:10:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15e7c498-27d9-35ba-9f88-34c4e36b19b0 | -10.47864 | -69.26391 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| caa72a0f-1807-3314-bc6c-f5e3a23fcac7 | -10.48014 | -69.46532 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b07d0b72-f6dc-3113-9c60-a589db3c10e9 | -10.4999 | -69.45556 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 40f8f719-dfcb-3e35-b3c8-aef8f264c87a | -10.50175 | -69.1612 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0701541-0659-3d48-a93f-a2b488afcbfe | -10.50449 | -69.29711 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e9b2a23-bc5d-3c79-8960-c651648d6c6a | -10.51674 | -69.23796 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bca7c533-12fb-31a7-8b8b-60280bba8047 | -10.54119 | -69.32428 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f148c8ec-b0d9-3a45-9498-7fd4b58c5ee5 | -10.54306 | -69.31153 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81cc14f3-cfc0-3573-941f-38d15c63b914 | -10.54356 | -69.33327 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03dceb5d-b79c-3bfd-ad36-bab012df6303 | -10.54418 | -69.32904 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4897ae7c-46a6-3f4e-926f-f7144b7046d2 | -10.54765 | -69.22948 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9a38586-a309-3f91-a610-6156503b1fc4 | -10.55066 | -69.23431 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb728923-7aea-3f4e-b646-b207f89c9a4a | -10.56092 | -69.24026 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89650d6f-bed1-3459-980c-c1e9c2c141b4 | -10.56393 | -69.24506 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 522732ee-b69c-3c66-8b0c-f1296fe0ef1f | -10.56762 | -69.44439 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e3b49b7-0967-3d7f-89a4-eff51245a306 | -10.56989 | -69.44284 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49e3da40-a6e0-3fcc-9737-e7f78affae8c | -10.57152 | -69.39359 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1b5cdc1-970b-3725-8b7a-7b8a4a02c49c | -10.57768 | -69.4398 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 24f14bb0-3077-3876-9292-7364673c8047 | -10.6106 | -69.66463 | 2024-10-03 06:10:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e373357-738f-3a3c-a962-57eb3e324c84 | -10.61595 | -69.25089 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80702318-9a3b-3409-8e88-d76831aa587a | -10.65638 | -69.645 | 2024-10-03 06:10:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87cd6e02-db04-38d9-bddd-a8acaf2278c6 | -10.70799 | -69.41488 | 2024-10-03 06:10:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2ca4c4ac-925f-3d76-bc81-6b475e9d0688 | -12.4227 | -62.9999 | 2024-10-03 06:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 156.5 |
| d40ddefe-e2b0-3be6-a409-84b350a7537a | -12.4038 | -63.0009 | 2024-10-03 06:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 250.3 |
| cc2f56d2-c707-3aaf-b520-4c502b8dd569 | -12.4228 | -62.9807 | 2024-10-03 06:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 974977d3-010e-3784-9ff6-52197b06a2cd | -12.404 | -62.9817 | 2024-10-03 06:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 111.9 |
| fc4fefe3-e32e-364b-afda-93ca467cbb97 | -12.7449 | -62.8854 | 2024-10-03 06:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| f70d5926-cd08-3a7c-bf3a-e709b81ae138 | -12.8999 | -62.4527 | 2024-10-03 06:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| a79b2579-b8df-3dfe-90a0-dc1cee5e3776 | -12.8998 | -62.472 | 2024-10-03 06:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 94.4 |
| eb14269f-b3b6-31dd-8abe-ff1320b4cb45 | -12.881 | -62.4538 | 2024-10-03 06:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 69.5 |
| ac79430f-7859-3a42-abee-460d5ac729c5 | -12.8996 | -62.4913 | 2024-10-03 06:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 83.6 |
| a2732c5d-7ad0-3871-aa13-15650b7c6627 | -9.0515 | -67.871 | 2024-10-03 06:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 7d86b62d-a6f7-3bfd-a44f-7a7af35026f9 | -11.6931 | -64.9974 | 2024-10-03 06:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 14a9b6dd-51b1-383e-ac38-61450bf4a026 | -12.4228 | -62.9807 | 2024-10-03 06:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 156.4 |


[Clique aqui para ver as próximas entradas](README199.md)
