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

## Dados Diários - Página 162

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2daa8d37-ac6f-30bd-836d-325d7de36ada | -8.26833 | -40.75481 | 2024-10-25 16:52:00 | NOAA-21 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8e31bc4e-d1ee-3b85-9cc6-58edc3a0bf1a | -8.20803 | -40.60549 | 2024-10-25 16:52:00 | NOAA-21 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f27dacd5-404f-3840-8e22-a68487a11b5e | -8.20664 | -40.31753 | 2024-10-25 16:52:00 | NOAA-21 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| a9d2a41e-3652-33e9-b1f7-6a3926ea3300 | -8.19496 | -40.56453 | 2024-10-25 16:52:00 | NOAA-21 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 155c2867-e3aa-38b8-85c6-6046ddf1a7bf | -8.11647 | -40.7576 | 2024-10-25 16:52:00 | NOAA-21 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 0a55a5eb-f96d-3596-88f4-83807df109a8 | -8.11584 | -40.75416 | 2024-10-25 16:52:00 | NOAA-21 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 06e19cb1-7559-3d5e-a8ea-aea1abc75a9d | -8.09353 | -40.53981 | 2024-10-25 16:52:00 | NOAA-21 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 7.1 |
| c6012253-440e-388b-9924-22d6e6291abc | -8.04477 | -40.77528 | 2024-10-25 16:52:00 | NOAA-21 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4cf3d337-5663-3f80-a30a-6c027e4f906a | -8.03943 | -40.77636 | 2024-10-25 16:52:00 | NOAA-21 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e1fe54c8-122f-3ebd-bf36-854d0f91a806 | -8.0254 | -40.54297 | 2024-10-25 16:52:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 5.5 |
| dd0bed3b-0197-3e64-b393-f8a0782de826 | -8.01034 | -40.55295 | 2024-10-25 16:52:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 46.3 |
| 2af7925d-21ac-399c-a823-1c807983e50f | -7.9515 | -40.54506 | 2024-10-25 16:52:00 | NOAA-21 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6b3b8340-32d4-3134-a092-ce64debbc336 | -7.94736 | -40.54669 | 2024-10-25 16:52:00 | NOAA-21 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0856835c-103b-3156-932f-1113eacdc2bc | -7.89511 | -40.63763 | 2024-10-25 16:52:00 | NOAA-21 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 39.3 |
| d8cb0152-3a05-3212-bac2-b79105b812cf | -7.89082 | -40.7821 | 2024-10-25 16:52:00 | NOAA-21 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 49.0 |
| b9b05c09-ed08-32ae-8044-10cac5e21b04 | -7.88789 | -40.78159 | 2024-10-25 16:52:00 | NOAA-21 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 28.9 |
| 97488032-07a7-36aa-93b3-e0df9e199c4e | -7.87146 | -40.63072 | 2024-10-25 16:52:00 | NOAA-21 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 136.9 |
| 79f197d0-00e1-3702-98c8-8c14e8eb0bc8 | -7.87019 | -40.62381 | 2024-10-25 16:52:00 | NOAA-21 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 52.3 |
| 2e91df26-2c61-3d65-b8ff-d375905327ef | -7.8701 | -40.63196 | 2024-10-25 16:52:00 | NOAA-21 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 58.8 |
| 79db3664-4dd1-3329-81e1-42b0475703e1 | -7.86948 | -40.62843 | 2024-10-25 16:52:00 | NOAA-21 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 58.8 |
| 6a8bdab2-173e-3caf-8f16-92053dea29c5 | -7.86888 | -40.62497 | 2024-10-25 16:52:00 | NOAA-21 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| d6d69de3-bc67-3d1d-95f6-a156da6603c1 | -5.32664 | -40.88146 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 8b077d01-1d90-344d-9595-1d522ee00257 | -3.6785 | -40.12634 | 2024-10-25 16:52:00 | NOAA-21 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 79.3 |
| 21eb8be5-1c06-3caa-b713-4c4c1b6bcfb9 | -3.67402 | -40.12343 | 2024-10-25 16:52:00 | NOAA-21 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 83.4 |
| ffbd5d8b-fc4d-3766-b3ca-899f7b52a1ca | -3.53029 | -40.70737 | 2024-10-25 16:52:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 28.6 |
| 9bfb6266-7ce5-3f94-8972-7d260cf00cbe | -3.45725 | -41.26053 | 2024-10-25 16:52:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 5bba083b-9fe3-3cb0-a077-5f6f565224e3 | -3.45672 | -41.25743 | 2024-10-25 16:52:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| e9e94cf7-42d4-3c33-b6af-8d644cb74b1d | -3.45319 | -41.25947 | 2024-10-25 16:52:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 2d1756b3-cb4a-3f74-8de8-f3f0672ca8e7 | -3.02445 | -40.78686 | 2024-10-25 16:52:00 | NOAA-21 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1f540c0b-ab24-34a9-90bf-e070b314b55f | -5.05777 | -40.27972 | 2024-10-25 16:52:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 6e6353e3-5863-3e49-9b43-5d1dfb5cc0cb | -5.05706 | -40.2756 | 2024-10-25 16:52:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 7310e336-c570-3bfc-b8dc-8a84b33c1b6c | -5.04165 | -41.01054 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| c419c105-8bc3-3861-824a-66e82385f663 | -5.03576 | -40.97668 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 22.6 |
| 8f3abbdf-43db-30d5-aa92-99762dda8690 | -5.0351 | -40.97289 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 22.6 |
| 51d04d11-70b6-3abc-a0d2-5828dd9b42f5 | -5.00321 | -40.41108 | 2024-10-25 16:52:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 57c88068-668b-34a5-bd78-51ca2b00fd65 | -5.00262 | -40.41121 | 2024-10-25 16:52:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 98eb84f7-9f1a-3560-8711-0c1e2837470e | -4.99698 | -40.75379 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 12.6 |
| b4aa99a4-97cf-3186-af26-e655d694cf24 | -4.99686 | -40.41232 | 2024-10-25 16:52:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 25.7 |
| 2f557cbb-afb4-322c-8157-abdecc9eb73c | -4.95806 | -40.53068 | 2024-10-25 16:52:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 813a9842-3a47-3453-bb94-634f1e16dbb4 | -4.93072 | -40.79229 | 2024-10-25 16:52:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 80434bbd-135f-38fe-be06-45307edfae52 | -4.92508 | -40.79324 | 2024-10-25 16:52:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 6b1c7efe-b9c3-3548-b59f-5d3bf46fc267 | -4.89309 | -40.74276 | 2024-10-25 16:52:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 8f9a748a-7dce-3126-a591-e1baa30b5531 | -4.88743 | -40.74375 | 2024-10-25 16:52:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 22.4 |
| f8f30639-af37-3535-b7ee-3bc721363984 | -4.86854 | -40.75088 | 2024-10-25 16:52:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 32bda586-13ee-3e85-a475-617f726ead0f | -4.86616 | -40.75542 | 2024-10-25 16:52:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 54.7 |
| ee58780c-fbdb-33e2-8848-1f270febaacc | -4.86548 | -40.75158 | 2024-10-25 16:52:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 54.7 |
| 6c52cde5-56e7-30d6-ae05-37d616bef691 | -4.86354 | -40.75577 | 2024-10-25 16:52:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 44.9 |
| aac50653-8237-3d74-b988-982e2bb7dd34 | -4.86289 | -40.75193 | 2024-10-25 16:52:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 44.9 |
| b39420cd-3fed-3903-8a5b-4ded0394e332 | -4.84699 | -40.51154 | 2024-10-25 16:52:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 11b16253-034f-36cb-b74c-67bd13cb26d9 | -4.84628 | -40.50746 | 2024-10-25 16:52:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 41.3 |
| 01adc66e-4767-3bb4-9d89-284e13524a95 | -4.82718 | -40.36367 | 2024-10-25 16:52:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 10.4 |
| f3ec52cf-0ef9-34bd-92ce-e30b16b33d12 | -4.78589 | -40.47083 | 2024-10-25 16:52:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 2c7e53a3-0643-3014-b323-f8fde7bc8ada | -4.77676 | -40.14422 | 2024-10-25 16:52:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 53.1 |
| f5f5e62a-6b4f-3f7a-a370-7fcf41d2fb2a | -4.77612 | -40.14061 | 2024-10-25 16:52:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 53.1 |
| cff4d21a-ffe9-3851-814a-dd624e5e8cb0 | -4.76475 | -40.16959 | 2024-10-25 16:52:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 8bb3363a-cd2d-3581-bc4e-37ac45c1bf6a | -4.7377 | -40.22391 | 2024-10-25 16:52:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 43.4 |
| 4b28490f-a4c9-34d3-86a2-7cb173a420a6 | -4.73697 | -40.21962 | 2024-10-25 16:52:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 42.1 |
| 093919aa-aad9-3320-bff7-4cb45970e539 | -4.72701 | -40.12615 | 2024-10-25 16:52:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| b0e9054e-dfdb-3943-81d4-570d19bc922e | -4.71986 | -40.60215 | 2024-10-25 16:52:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 13.7 |
| d000ef0c-5872-3cd3-be92-8dc1222fcdef | -4.71846 | -40.60301 | 2024-10-25 16:52:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 5815d11f-81f0-3eed-b856-0482ec61383e | -4.71411 | -40.603 | 2024-10-25 16:52:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 13.7 |
| d327ab7c-ad34-3505-a0cb-2e7bcabf474f | -4.63533 | -40.74734 | 2024-10-25 16:52:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 71c7abaf-98af-38bd-b02e-3564206edd0c | -4.63466 | -40.74339 | 2024-10-25 16:52:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 25.9 |
| dc73c16c-8bc9-3f96-81aa-23e277255a96 | -4.63151 | -40.74599 | 2024-10-25 16:52:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 27.6 |
| e36f59f5-a796-3f28-a51b-80debf3232fa | -4.62963 | -40.74824 | 2024-10-25 16:52:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 29119406-3314-3b03-9364-ed3249ac03ac | -4.76915 | -40.16989 | 2024-10-25 16:52:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 14.0 |
| d6eff1df-d341-3313-8d9c-c6b9a8aeb0e3 | -4.72772 | -40.13029 | 2024-10-25 16:52:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| c31419ae-e3e8-38d9-a612-9ffe5c9bf32c | -4.72112 | -40.1272 | 2024-10-25 16:52:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 95.0 |
| eee8beb8-d8c3-3752-9be2-f185d9626ab5 | -4.72184 | -40.13145 | 2024-10-25 16:52:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 95.0 |
| 1263b3d4-41e0-33b2-a754-359856b9cb94 | -4.44349 | -40.15197 | 2024-10-25 16:52:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 32.5 |
| cadb5b63-9447-3996-bc34-cdf4bab44712 | -4.44559 | -40.15079 | 2024-10-25 16:52:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 605ca97e-4d2b-3711-b4d7-e33f5af82f79 | -4.54105 | -40.67641 | 2024-10-25 16:52:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| d9c6fa73-f7a3-31de-9a9d-e04978020d80 | -4.53942 | -40.67657 | 2024-10-25 16:52:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| e1c34fb6-d0d6-3743-86a9-ee64637c0b13 | -4.53031 | -40.6823 | 2024-10-25 16:52:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 46.8 |
| b0aa533c-5781-30d9-8ea2-e2bbb7af52ba | -4.5296 | -40.67825 | 2024-10-25 16:52:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 46.8 |
| 6861a204-283a-36ac-a760-3f0b54a3926a | -4.52932 | -40.6865 | 2024-10-25 16:52:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 34.4 |
| dffadd61-0d71-37de-83dd-7876117cd741 | -4.52864 | -40.68245 | 2024-10-25 16:52:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 46.5 |
| bfd6a803-8bab-3e94-8625-0035e7577755 | -4.52862 | -40.73973 | 2024-10-25 16:52:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 246.3 |
| 32ae9dcf-8a80-35c7-a3fb-3bb70263eb1e | -4.52797 | -40.67841 | 2024-10-25 16:52:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 46.5 |
| 12a34de9-7951-302c-8c7d-f1b1076bc72e | -4.52655 | -40.74001 | 2024-10-25 16:52:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 186.0 |
| a3ab78b6-149a-3fa3-873e-eb9cffc81b8e | -4.52586 | -40.73588 | 2024-10-25 16:52:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 186.0 |
| ff6ff508-de36-385e-b711-af13de916329 | -4.52518 | -40.73185 | 2024-10-25 16:52:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 50.5 |
| 229dad03-135a-3aad-921c-a6202bee40a4 | -4.52362 | -40.74466 | 2024-10-25 16:52:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 60.9 |
| f7307c90-5bac-306d-bc75-4508684db83d | -4.52289 | -40.74053 | 2024-10-25 16:52:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 246.3 |
| faddcd23-02e3-327b-a6bb-9998fc05cab0 | -4.52218 | -40.73645 | 2024-10-25 16:52:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 246.3 |
| 4195acc2-3552-3d13-a33e-7def53cd020f | -4.51949 | -40.73291 | 2024-10-25 16:52:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 50.5 |
| e031f6da-8e1c-3ffa-9aae-77349054783a | -4.51888 | -40.16529 | 2024-10-25 16:52:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 9bedc40f-cf12-39aa-b9c8-d02aac54bc67 | -4.51213 | -40.68921 | 2024-10-25 16:52:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 9cd5ed41-7723-3c72-9dd1-822abc9cf451 | -4.44041 | -40.1562 | 2024-10-25 16:52:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 16.1 |
| cbe79afd-0c5e-350c-b275-b32a896f4127 | -4.43967 | -40.15183 | 2024-10-25 16:52:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 38655392-93c7-32f7-a5a8-e6274c55c11f | -4.36751 | -41.51046 | 2024-10-25 16:52:00 | NOAA-21 | LAGOA DE SÃO FRANCISCO | PIAUÍ | Brasil | 2205573 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 82efb037-0d7d-3962-9a9b-af28d2cc5e1a | -4.34778 | -40.45807 | 2024-10-25 16:52:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 849c4d78-7f30-3c79-9b7e-aba829421519 | -4.34707 | -40.45389 | 2024-10-25 16:52:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 135.8 |
| 2a9f2ed6-5c95-3c9f-ab15-3a7ec08a3bac | -4.33737 | -40.64085 | 2024-10-25 16:52:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 0677f5e5-fcb6-3106-a17b-6497aa3cf565 | -4.33125 | -40.77576 | 2024-10-25 16:52:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| dca61c0f-dbd6-3df3-b05c-b5ea20f962db | -4.23429 | -40.45828 | 2024-10-25 16:52:00 | NOAA-21 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| fd2d062a-176b-3196-8ac1-a31d3a2ef457 | -4.22139 | -40.41777 | 2024-10-25 16:52:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 51.2 |
| 9fb8edca-e1bc-3ccb-ad36-a8d34da646f6 | -4.19152 | -40.66446 | 2024-10-25 16:52:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 3df46fb1-f2c8-3244-b3f3-dab60c0abc7e | -4.1908 | -40.66019 | 2024-10-25 16:52:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 0e71c8f0-c3b5-355e-b892-7470083bcb4e | -4.18667 | -40.66597 | 2024-10-25 16:52:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 51.3 |


[Clique aqui para ver as próximas entradas](README163.md)
