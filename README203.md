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

## Dados Diários - Página 203

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9966cb3a-4717-3fe4-98ff-20e1e2a6754a | -15.65402 | -59.41415 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 496088df-6729-3d75-93b0-7d9a9a48b558 | -15.65341 | -59.41787 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 42a64fff-0aa7-366c-a60c-922d0bff7dfa | -15.6531 | -59.44095 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8eaf8caa-88c2-3d16-bf41-fbc732b47119 | -15.6528 | -59.42158 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f597baf1-afe1-30a8-8fe3-d6179af19685 | -15.65247 | -59.44481 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e9866f2-f6a2-3828-a0bd-bc7e7d6a041b | -15.65158 | -59.42903 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7434766-bf5c-3e4a-90c0-8e4b6e2b6fdc | -15.65096 | -59.43277 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f0d99dd-f7c4-32d2-befc-710a360ec216 | -15.65035 | -59.43652 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66d7e08b-83d0-39f6-8333-5e6039443e87 | -15.64972 | -59.44035 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9c33732-fff7-3b55-8780-bd799ebd696e | -15.54932 | -59.3473 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 062141e6-1e15-3aba-9fd3-6fc79fcb75f0 | -15.9716 | -59.08919 | 2024-10-09 05:06:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6431a79b-91c5-31f4-9d82-405840459b84 | -15.97101 | -59.09284 | 2024-10-09 05:06:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 853fb1db-828b-35c9-aa8d-c500f91397d1 | -15.9693 | -59.08945 | 2024-10-09 05:06:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e7ed58b0-b425-3d4a-975e-1c3f25f28dc5 | -15.96871 | -59.0931 | 2024-10-09 05:06:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4aba0097-94ac-3153-a4ca-4798ddf12c94 | -15.96812 | -59.09676 | 2024-10-09 05:06:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf469505-2fbd-3f8a-8602-b66c2fb6f328 | -15.80683 | -59.20879 | 2024-10-09 05:06:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c7cdac7-5cc1-3e40-af97-2e6005c7448c | -15.80347 | -59.2082 | 2024-10-09 05:06:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7c5a6e9-066d-3b82-a577-3a6c92c4162e | -15.80287 | -59.21189 | 2024-10-09 05:06:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36a4e5e7-eb50-3538-90dd-d5179257e243 | -15.71974 | -59.44458 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 021ab487-2d71-3530-87ad-4073426bf744 | -15.71912 | -59.44833 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 421226bc-0840-35f0-8f84-7508f83dda9c | -15.71574 | -59.44775 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f7f9c35-6aee-35b7-81b8-35577a6309c8 | -15.71236 | -59.44717 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92316904-7880-3dd3-8100-7dad1ed79c66 | -15.71175 | -59.45091 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ef0cc97-172d-392d-b38c-adb235618d9b | -15.71146 | -59.38966 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a4d0fb5-140c-3f11-81ff-cd3a7e1cbcf0 | -15.71053 | -59.37431 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6b3b498d-d050-38bb-92b4-b1678b115856 | -15.70992 | -59.378 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1ca56a1-5a61-37d3-b9de-3061b7c6f816 | -15.70931 | -59.38168 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 443c086e-db8f-3fca-9362-8f90034610ca | -15.70837 | -59.45031 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 715da5cc-b21d-3c75-9a46-0d8e61cd6bb9 | -15.70716 | -59.37367 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3c52817a-72dd-34ac-8986-b8adea4406f9 | -15.70655 | -59.37737 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ca14dd25-ae0b-388d-870e-e4b45dd3f073 | -15.70595 | -59.38105 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d5a51914-9c04-3a25-a3ff-a74f15b41a0d | -15.70573 | -59.37356 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d888da22-5595-3e9c-9abb-2a7687c9442e | -15.70513 | -59.37725 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 234aa1c6-91ee-3424-b769-4231f136f9c4 | -15.705 | -59.44973 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42b3135c-d5c9-3c52-ad34-346a59326507 | -15.70176 | -59.37667 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9c934062-db73-3ff5-8e7f-cbb18ff1dc91 | -15.70167 | -59.40689 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 410ecb6f-f79e-3bcf-9d11-f6e5e25e4907 | -15.70116 | -59.38037 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8843a90d-9207-38b5-a7cd-0733bb752e6e | -15.70106 | -59.41062 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a81b580-ff1c-32cf-86d5-28fd86825626 | -15.69971 | -59.41056 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8211c56-fa3c-3435-b079-f523be21ab40 | -15.69778 | -59.37983 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6047f246-b70f-32ed-953c-6ff6b11dccf1 | -15.69718 | -59.3835 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c3427bcf-d7ef-3dc6-b535-70932e9ab398 | -15.69441 | -59.37927 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9eb832fe-2d3b-3d77-baaf-8230460db72c | -15.6938 | -59.38296 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7dc7a01e-bcb0-331f-ba89-67814d5d76cf | -15.69356 | -59.40572 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90b7c750-ca5f-3ac6-9bab-661170493914 | -15.6932 | -59.38664 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 581ddcfe-d565-34d0-8f7b-08dc26c7bffa | -15.69173 | -59.41694 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47d761a6-c3c8-3d78-8d2f-f3f63f4eac21 | -15.69018 | -59.40519 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f37e8a82-f066-308c-8252-b3bbfe5a4df3 | -15.68983 | -59.3861 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 40cfe4fd-f382-3f71-b46c-da49b93e5360 | -15.68957 | -59.40893 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c54f013d-45da-3964-8ec8-8cbd6c89ceed | -15.68922 | -59.38979 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 78d2cb2c-f31b-3a6e-a82e-a617d5df585f | -15.6868 | -59.40464 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cd491ac-c26d-3dc2-893e-aa2fd4a40612 | -15.68645 | -59.38556 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e2c665d4-d210-3269-b937-97c63aa6d231 | -15.68585 | -59.38925 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3dfab4dc-384f-3100-a024-effc839af9da | -15.68525 | -59.39292 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 34557671-43cf-3f25-9e7a-38cdffc19a2e | -15.68464 | -59.39661 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ee6445c-b3a6-31a0-9eb3-ad49c5663f43 | -15.68343 | -59.40404 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19941827-1613-3875-a265-0a23aec3720b | -15.68187 | -59.39239 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e06547a-d50b-3c4d-9ee9-025740e328e3 | -15.68126 | -59.39608 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f35d56a-f2ee-3b5f-9298-1d69fa4a7615 | -15.68066 | -59.39977 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0cc9ca5-b342-3e61-a567-90ca52fc720f | -15.67789 | -59.39554 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f46149a4-dfd7-3d2c-b4d4-b97713f288db | -15.67728 | -59.39921 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afb1f4c8-6fef-3d90-89c9-c7d31c6f6c78 | -15.42076 | -60.01725 | 2024-10-09 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 691efb1d-d47c-3ffa-a966-bad761da9c70 | -15.41732 | -60.01663 | 2024-10-09 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd230129-ad94-3b89-946b-3ffd5c275f5f | -15.41684 | -60.04063 | 2024-10-09 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bc8608b-cdc7-3e29-aac3-e01c698c07c5 | -15.52437 | -59.60522 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 018ce0a8-3256-3502-9980-9ca54c49d5ad | -15.42141 | -60.01336 | 2024-10-09 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2fbb62a2-5680-33a7-a001-5cc634f25cb3 | -15.41666 | -60.02053 | 2024-10-09 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc1653f1-a6ec-32f5-8ad1-c506682bd148 | -15.41535 | -60.02833 | 2024-10-09 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd1179c7-4e57-3fc2-9899-6ddead0b2c8b | -15.41387 | -60.01603 | 2024-10-09 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a36159ef-3e40-3ad5-a847-0ae67a2dc326 | -15.41339 | -60.04002 | 2024-10-09 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07010888-0f6c-3212-b9c3-095892feafd4 | -15.41256 | -60.02381 | 2024-10-09 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e9042b4-c2b9-372b-b28e-b0b7511b2c34 | -15.41191 | -60.02771 | 2024-10-09 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f14933f6-932a-39ff-8b8c-d4a54770e5be | -23.14788 | -49.79576 | 2024-10-09 05:08:00 | NOAA-20 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 54d60cb1-35dd-34d5-91eb-d80187d45231 | -23.14758 | -49.79899 | 2024-10-09 05:08:00 | NOAA-20 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 56e50750-03b4-3101-a8a5-1a07e51ea658 | -23.14728 | -49.80226 | 2024-10-09 05:08:00 | NOAA-20 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2aa5c9ca-081a-3a99-965d-f5590978ed4e | -23.1422 | -49.79831 | 2024-10-09 05:08:00 | NOAA-20 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| aad04cfe-13dc-3615-b54c-e1a3d2f3a5d8 | -23.14191 | -49.80148 | 2024-10-09 05:08:00 | NOAA-20 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3ddfb562-fcf0-31b8-aea1-4e214e94cc25 | -22.97406 | -49.79522 | 2024-10-09 05:08:00 | NOAA-20 | CANITAR | SÃO PAULO | Brasil | 3510153 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ac7f0e9a-b2d9-338d-a9e8-7c649dd2ee06 | -30.2833 | -51.53494 | 2024-10-09 05:08:00 | NOAA-20 | MARIANA PIMENTEL | RIO GRANDE DO SUL | Brasil | 4311981 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 3a836c3e-a07e-3dc7-bfb2-ebc23d4e46be | -23.20905 | -50.8959 | 2024-10-09 05:08:00 | NOAA-20 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| af06b27c-68c6-3660-a5ac-a4f2e4893b78 | -23.20847 | -50.89626 | 2024-10-09 05:08:00 | NOAA-20 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 4c31a95c-f86f-3d6b-a026-de8508ff101f | -23.20842 | -50.90197 | 2024-10-09 05:08:00 | NOAA-20 | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 90314551-6050-32a0-ae51-2dd14ccb79e0 | -23.34867 | -53.91263 | 2024-10-09 05:08:00 | NOAA-20 | ITAQUIRAÍ | MATO GROSSO DO SUL | Brasil | 5004601 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0d39e81c-2bbc-3082-8b43-529042a93852 | -23.34452 | -53.91206 | 2024-10-09 05:08:00 | NOAA-20 | ITAQUIRAÍ | MATO GROSSO DO SUL | Brasil | 5004601 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 827453cc-9a58-36c3-935e-952d560d8fea | -3.56686 | -54.34042 | 2024-10-09 05:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76b6ebbc-9d0b-3668-949a-90220b8d5d03 | -3.56592 | -54.34694 | 2024-10-09 05:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93a88487-9475-315e-b766-2bf58dae8f05 | -3.26436 | -54.1868 | 2024-10-09 05:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0fb7258c-2e1d-356b-bdde-fc96201f4695 | -3.25724 | -54.18627 | 2024-10-09 05:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 505f45c0-219f-323d-87c9-1a7a3ca6454d | -2.93769 | -54.81964 | 2024-10-09 05:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9eea3291-044d-3277-899f-049c100a1019 | -2.8749 | -53.95644 | 2024-10-09 05:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b90b2092-03b4-3434-8e08-54ca1e2af533 | -2.87386 | -53.96358 | 2024-10-09 05:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f83a23f8-a04d-3817-864b-bea8c3e2c9ee | -2.81622 | -54.3579 | 2024-10-09 05:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c1031f1c-1cb7-30f7-9f63-590d746fc579 | -2.81521 | -54.36481 | 2024-10-09 05:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4d3ce3d6-c5b3-3ba5-8912-ce6900244d22 | -3.65732 | -54.29543 | 2024-10-09 05:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d3f764ab-bcc2-30e7-aaa9-1b10602d2046 | -2.58516 | -57.40846 | 2024-10-09 05:53:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70b65f34-b034-3665-a768-7c1c72119a44 | -3.01939 | -59.09975 | 2024-10-09 05:53:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 751cfb7e-9290-3671-855e-58bf1a251ed0 | -3.01892 | -59.10282 | 2024-10-09 05:53:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fe82b28-b954-391a-b8eb-6685b2618e8c | -3.01376 | -59.10215 | 2024-10-09 05:53:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd2e2703-071f-34fe-90b1-20dfac7603ae | -3.0133 | -59.10522 | 2024-10-09 05:53:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 01159364-69c5-3dbe-8912-72f588162fbc | -3.01284 | -59.10825 | 2024-10-09 05:53:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README204.md)
