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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f770e44-bf07-38ee-af3f-311d3b66376b | -10.44153 | -50.73943 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d8a26b88-d388-3430-9ff6-0ed1026ad4c3 | -10.44119 | -50.70161 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 35.3 |
| ab8ed9e9-6c0a-30f2-ba26-6ca36a6a674b | -10.44087 | -50.7096 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 221.9 |
| f571987a-0fc2-3bde-8b6f-7119190476f2 | -10.4407 | -50.73609 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48b9ac7b-963a-34fd-8aa6-61c3803a81ac | -10.44061 | -50.74419 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9094baae-aecb-3c39-a633-7997c6f4eb33 | -10.43995 | -50.71436 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 221.9 |
| d43d42e0-3638-3668-a6b9-d60e1c743026 | -10.43975 | -50.74084 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cb504f9a-9f16-3f76-8b0c-1b6758b445a7 | -10.43934 | -50.68441 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 38ee38a3-524e-3976-9568-891545bc2536 | -10.4393 | -50.71105 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 180.8 |
| 73450cef-be5f-321e-8301-7b32b4fab2b3 | -10.43903 | -50.71917 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 47.5 |
| d75671b9-5e8e-3791-bd7b-4343683f0afb | -10.43889 | -50.68116 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a1d0da5-1700-3bfb-99f6-a7d0e3c8cfc0 | -10.4388 | -50.74559 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de74edbd-326f-3cb0-a8af-eb55ac3d3222 | -10.4384 | -50.68926 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7379f2f5-50e2-33c8-8f94-e29fa4a5bab7 | -10.43835 | -50.71581 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 50.4 |
| fb5309e3-73b4-3168-a9fc-bd9658fabeca | -10.43811 | -50.72395 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 28bf9863-2474-3e6d-9bf8-16044ffe45af | -10.43791 | -50.68601 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eff6c454-4a71-3d73-aaf4-3063986f6824 | -10.43747 | -50.69409 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8fd2b44d-3b95-3115-becc-9af2a1f1f9d8 | -10.43739 | -50.72062 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 4f029b61-17c8-3900-bae9-d49c66992ad5 | -10.43718 | -50.72873 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ba8a8f49-0b5a-31ff-a1c2-6fb4c6d0c996 | -10.43695 | -50.69083 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3379ccb1-972a-3b70-a76d-af2f26a869e2 | -10.43655 | -50.69886 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 207.7 |
| bfb6f47e-4306-3258-9715-ebfa747fa715 | -10.43643 | -50.7254 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9f8fcd01-3571-34ae-b0fc-cbe62352832e | -10.43626 | -50.7335 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 57dc2136-27de-3356-b99e-07b0ba020f01 | -10.43598 | -50.69564 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 21d361e3-a956-3200-b2eb-03bc3878343c | -10.43548 | -50.73016 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 79101801-0135-3cb0-8bac-c7fe7db1add8 | -10.43534 | -50.73828 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 861b7e4a-37e0-34be-adc6-0426c0c6fef0 | -10.43472 | -50.70832 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 221.9 |
| 001d20fb-6791-3cae-ae6e-5aafc73e1c1b | -10.43452 | -50.73493 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 980b8321-fa23-355a-ac5e-4ec69467c004 | -10.43442 | -50.74306 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 825f5711-f827-3017-8f0a-360f2b9f2675 | -10.43381 | -50.71308 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 221.9 |
| 59d49ec5-0d3e-3718-a079-b3fbaa1c50d8 | -10.43357 | -50.73971 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 853ae7ee-aaaa-307a-a15a-1a0bd0bf59af | -10.43323 | -50.68297 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 593df4cf-1e88-3ac9-9f67-712644cbed36 | -10.43314 | -50.70982 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 331.9 |
| 75582cf7-0d26-302c-a9cd-2d10b356e710 | -10.43288 | -50.71788 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 314d6624-b97a-3b1c-8043-1828eba12c49 | -10.43278 | -50.67973 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d3e27572-021b-3dca-a257-f17b70d48983 | -10.43261 | -50.7445 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 115026d8-7b3e-3eff-a357-fbdefe4e1263 | -10.43229 | -50.68782 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e85b2c99-d028-330b-88c5-ef6820f1c50d | -10.43219 | -50.71457 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 107.1 |
| f4082120-2897-393a-9401-f32cd6e2777d | -10.43195 | -50.72269 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 83d5d702-10c3-3565-8126-86f5b5b8c01d | -10.43181 | -50.68456 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bdb898dc-ae93-3585-9a4e-70ef139b9df7 | -10.43134 | -50.69274 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c3123533-47fa-3e8e-816b-42dc08f580dc | -10.43123 | -50.71936 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 90e9a2f3-5b62-3c0d-a6ed-b22104d1d391 | -10.43102 | -50.72748 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0db7f6a5-7e48-3b76-abd4-556b6f2f7db2 | -10.43084 | -50.68942 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9e33f829-fba7-355f-a329-34f962dcb1cf | -10.4304 | -50.69761 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 6e6042dd-4e9b-39be-977f-a50a42ee4c1b | -10.43027 | -50.72416 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 26.0 |
| a6dd1a0f-a46b-3142-b936-d988019150f4 | -10.4301 | -50.73227 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f1f17aa2-6ee9-3665-bce0-ec12ed4c1557 | -10.42985 | -50.69435 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 355a3dcf-05c0-34b3-8e83-8c4bfccd8e0b | -10.42931 | -50.72894 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 26.0 |
| b2c9d0e8-f4a9-3c3d-8525-dcc5f398611a | -10.42917 | -50.73707 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ab736367-cc49-3e60-9587-747c1c7c5f7e | -10.42889 | -50.69915 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 121.8 |
| ef9cf0eb-eb9a-34f8-81ad-df5b6ed5602f | -10.42856 | -50.70711 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 0d22d34c-a9c4-36bf-a47d-1b737107174a | -10.42835 | -50.73373 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 52b2ac4a-1dc6-339b-97a8-047b7e2b5acf | -10.42824 | -50.7419 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 62b136a5-83bd-386c-9e63-9af581343da0 | -10.42793 | -50.70389 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 331.9 |
| efbe3412-81a8-36e3-a2f2-39eaa1c8a3a3 | -10.42764 | -50.71186 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 9a37c1a7-669f-37d5-9870-512ac5f3716d | -10.42739 | -50.73854 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d80d3fa3-4ab7-386b-bfaa-8354ccd9d862 | -10.42698 | -50.70863 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 331.9 |
| 18e5c581-401b-3666-9e4a-574bab8a6f69 | -10.42672 | -50.71666 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| ce97ab21-cb4d-3b06-96a8-f37b2c403cda | -10.42642 | -50.74337 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f2a1cc73-8259-3bc0-a799-8cca40f6c519 | -10.42619 | -50.68635 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e29073b-7156-3f87-8ceb-4352f258ef9c | -10.42603 | -50.71339 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 107.1 |
| ff2af48a-01ee-3dc5-ad24-946f8ff4d20b | -10.42578 | -50.72147 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| e55edaa7-f4de-3bef-a744-c11469089846 | -10.42523 | -50.6913 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6a71eb09-eedf-359d-8aba-66c5b671de07 | -10.42506 | -50.71819 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 107.1 |
| c20991c2-c9b9-3432-ae52-76083ac92053 | -10.42485 | -50.72629 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 02c5eab5-cd3a-31b7-b199-650d6d134054 | -10.42427 | -50.69625 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 9ac939d0-9b25-37a5-aeec-4b641fab1318 | -10.4241 | -50.72299 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 26.0 |
| ba7d4cc0-6d8e-3f55-a407-1f5ecfa27518 | -10.42392 | -50.73111 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| ab3682d5-73f7-3b8d-afbe-c28aeb847c83 | -10.42334 | -50.70109 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 75aa2045-0b00-3402-af04-27a56a10fa3a | -10.42313 | -50.7278 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 9b1d5783-f285-30ac-8f72-59fba1c0ab1f | -10.42299 | -50.73593 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| dfeb4422-a40c-3e06-b8d5-c69b09d289d4 | -10.4224 | -50.70591 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 6902685e-565d-3dc7-a0a3-ac592d140813 | -10.42216 | -50.7326 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 337bead2-363a-325a-a263-d6845fba4bc0 | -10.42205 | -50.74076 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5c1b6918-268a-333e-a30a-5357dbc7cbb3 | -10.42147 | -50.71069 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 1c0c18cc-6af1-3a74-a198-863574d80c93 | -10.4212 | -50.73742 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2e9f867b-bcd7-3a0c-9458-7266a87df500 | -10.42111 | -50.7456 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9413ce86-a65e-3342-82b5-54cd059c3f19 | -10.42054 | -50.71549 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| fcb290df-32a1-3e43-998c-b79253fbb93e | -10.42023 | -50.74225 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 90f7d554-b7c5-33c6-97d4-e55ed42d9556 | -10.41961 | -50.72031 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 5127a94c-688b-389c-b641-5b95aaa91789 | -10.41868 | -50.72512 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 9b8307c2-2219-3e2e-b309-7262dfd31434 | -10.41774 | -50.72993 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 9481303d-7100-369b-b96c-e5ee18029e1a | -10.41719 | -50.69979 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ca3d8da1-7af7-30ed-9b33-7d80711848f1 | -10.41681 | -50.73475 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d768044a-ae8c-3527-b1a9-26fad170b655 | -10.41625 | -50.70463 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 17d07fb7-14bc-3f04-ae4f-b850a9a33b7a | -10.41587 | -50.73958 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 31f60e7a-3161-3f1e-ab12-0c523d0ed32d | -10.41532 | -50.70945 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 31c689a0-e717-3c89-ab59-54b2f601df6c | -10.41493 | -50.74442 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5211c1c3-e5b7-32ca-9260-6e5122702b1a | -10.41438 | -50.71428 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2441e420-54f3-3406-9cb2-e53a81a9647a | -10.41344 | -50.71911 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0fd026ae-bd7c-3abd-9e01-84952f3ac028 | -10.41251 | -50.72391 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f3641f2-3e01-37fe-b896-482f6dad0bda | -10.41158 | -50.72869 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 29712f8e-86f2-39ff-a05e-696c28ae9558 | -10.41065 | -50.73348 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f38e6055-550b-3572-9853-2cebee665c0d | -10.40972 | -50.73826 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3a1abff3-373c-33b7-8dda-823b6c47987d | -10.90472 | -52.38187 | 2024-10-06 03:55:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1afaed4c-d866-3936-86e7-8418dac566ee | -10.89921 | -52.37448 | 2024-10-06 03:55:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88fd3d83-b764-3aad-a202-267874e3304f | -10.898 | -52.38038 | 2024-10-06 03:55:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 17dbff25-1f06-38e2-a2cc-ce05c6e102ce | -10.69985 | -53.03907 | 2024-10-06 03:55:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68861baf-30c0-3352-9e70-44f8144c023c | -10.697 | -53.03687 | 2024-10-06 03:55:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README58.md)
