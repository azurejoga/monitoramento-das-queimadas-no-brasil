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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e364383-7516-3dee-ae24-fa3386c1d9d1 | -12.5508 | -53.46557 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0a3cb63-c78c-3a0f-ad36-604caece8256 | -12.55013 | -53.4696 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c2198f5-034c-3cff-b5c6-b803a15abeff | -12.54729 | -53.46497 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e503712-cdf3-34f5-9f16-f9d913b6eb28 | -12.54661 | -53.46899 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0075664-6be1-30d2-9945-40a1984888a6 | -12.54309 | -53.46839 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bb04376-54d9-39be-aba2-e961729633a5 | -12.54103 | -53.28738 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c003d0d0-8f47-31da-8f0b-a0aa050b80e4 | -12.53472 | -53.28222 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 245a98f8-d218-34b1-b5f8-88432c67cc1c | -12.53452 | -53.18997 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a84ed65-f9bc-32c9-a357-de322288dcdc | -12.51847 | -53.46411 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a1a5749-1784-3c5d-8f63-b7c40461115c | -12.51563 | -53.45947 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77dfccb2-59ca-3ace-852b-622ed776f7b9 | -12.51211 | -53.45886 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21c7120d-30af-3f51-ad59-d07209d6af96 | -12.50975 | -53.21003 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb33f11a-2f4b-3bb2-835b-422b3b4df49e | -12.50757 | -53.20155 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75ce30bf-2e9e-3d55-8db8-0145b230b902 | -12.50627 | -53.20943 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f2a6a23-e222-3d7f-850f-50c06b5426d2 | -12.50473 | -53.52399 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ef245db-02ed-33e9-a7db-e481d20c2b0f | -12.50278 | -53.20883 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76d591ea-2839-38d2-b33c-5bdb1417a77b | -12.50213 | -53.21276 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b04b7d0-85c4-3f73-a771-2abb095409cb | -12.50189 | -53.51933 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e70b92c5-c563-361d-9a05-a2c3e3e67336 | -12.50052 | -53.52742 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c885017-546b-3894-8623-872f06d0d7ad | -12.4993 | -53.20823 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 328c3885-dbd7-35b6-92ae-d19107e8f7d9 | -12.49865 | -53.21216 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53835175-74b0-3fee-922c-50abd9b975fe | -12.4963 | -53.53086 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbb09215-c549-3862-889e-4bd21407e784 | -12.48301 | -53.17702 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aaa4cb77-8214-37ac-9370-a4d01995a685 | -12.48149 | -53.16463 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27d2af70-d8f7-3565-80b5-9e6c82b1a2b4 | -12.47953 | -53.17642 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b008d979-126a-36f4-a48c-9638b02eca64 | -12.47736 | -53.16795 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 011d648f-e789-3c93-84ad-f864aa4a9a4c | -12.47671 | -53.17189 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46289465-a244-3126-865d-8d095e308999 | -12.47389 | -53.16735 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f2d0ec6-45cc-3a4a-97e2-cea8b03ec883 | -12.47323 | -53.17128 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1780f6f0-bf40-3643-a8e6-94f9f97f337c | -12.46975 | -53.17068 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3da24fa1-2b42-33b7-92c9-36be6382e089 | -12.45195 | -53.53688 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1dd24ca-2493-3d24-9202-ab04855cf91f | -12.40023 | -53.49871 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de4ffa0d-21d4-34bd-86c6-f79ac94a5abe | -12.30812 | -54.08359 | 2024-10-05 04:38:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3023095-1f52-31be-b5d0-82d1b3928f68 | -12.29347 | -53.46428 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02ea306b-5e13-3906-82be-e3b17318b052 | -12.63497 | -53.10992 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b11bb118-5fbf-300d-a618-6cb695081a50 | -12.63433 | -53.11382 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eea2bff9-9a87-3c8f-a278-906cdcf54941 | -12.63368 | -53.11771 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83bd788e-7d37-3491-a045-82a8c68e24d5 | -12.6315 | -53.10932 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 860763e3-9060-37f8-b921-dc0d37159938 | -12.63086 | -53.11322 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| bb26db7c-5133-3278-bbe4-f23479cb80a4 | -12.63022 | -53.11712 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 36.0 |
| a0e7ecf5-2b93-31ae-9928-ed7fef8681cf | -12.62957 | -53.12101 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 36.0 |
| d93a73b2-1910-3163-8072-216c0092331b | -12.62804 | -53.10872 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| eea4e97d-c69b-370f-ad8b-da10ec56008c | -12.62675 | -53.11652 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 9f23d33f-4516-39b3-8501-8f4b9198f8c1 | -12.62611 | -53.12041 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 36.0 |
| d1c0e665-f528-31a4-836d-0c6c3c8ce920 | -12.62458 | -53.10811 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 2c3488d8-3c69-3522-b564-d4a129156424 | -12.62393 | -53.11203 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| defb384d-a3e1-3a93-b1a8-1fda8016d752 | -12.62329 | -53.11592 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 4200ea24-fcbd-3331-aa33-5a10f2b030c9 | -12.62264 | -53.11982 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| cacb4cc6-1eca-34d4-af5e-91edd3c00532 | -12.62112 | -53.10751 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| c4955231-c32e-3868-bfaf-cdbba5b831cd | -12.62047 | -53.11142 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| f6a07f07-c582-3627-88c3-56e916bae6a2 | -12.61982 | -53.11532 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 6e95fae1-6731-3899-84f2-cb6a39196c32 | -12.61918 | -53.11922 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 83468bd2-bcdc-34c2-aed4-346a75d175dd | -12.617 | -53.11082 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ecb80540-cbf8-3b00-9356-041e2ce3dff4 | -12.61636 | -53.11472 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 804b71d5-011f-3a64-8f58-ced8c9da654c | -12.61571 | -53.11862 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 6ef388e6-af19-36fb-9b0f-bea200797664 | -12.61354 | -53.11021 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d86f17d7-a1b5-3c66-bc72-72bc233df2c7 | -12.61289 | -53.11412 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| df266712-738c-3d1f-a19a-1a4e1ca445ef | -12.61225 | -53.11802 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 209812d1-f17d-3893-9fee-d0456d62ec64 | -12.60943 | -53.11352 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 408f0cf1-b484-3538-b139-40bfa3d928ea | -12.60878 | -53.11742 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0a864efb-0d4c-34ec-9cc2-5c146a1cff01 | -12.60814 | -53.12132 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| d67492b1-635f-3be3-8299-8de057c43fb3 | -12.60532 | -53.11682 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c8e178a0-4c89-322b-aad7-3b607a97ea7c | -12.60467 | -53.12072 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 2088dd8d-0d31-39f8-bd1c-2636f35f9987 | -12.6012 | -53.12013 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 1b6a7fdf-f679-3e20-995e-ae8879084fb6 | -12.59774 | -53.11954 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 3a381f65-3122-3355-9f42-8c8f6e838d6d | -12.59427 | -53.11894 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8641a4b-81bc-33e4-a19f-0faf27ff1955 | -12.57694 | -53.11596 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b47872a-8bde-3cec-a54f-dfde91b3ad8c | -12.57628 | -53.11987 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5016c42-762d-33ab-8cca-e576f21c16cf | -12.57347 | -53.11536 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cedda55c-0e43-3339-96a3-3b56ce1d6ec7 | -12.57282 | -53.11927 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42e648cc-1393-321b-9a66-1e296cbeb74b | -12.57001 | -53.11477 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 482f2a02-e8bd-3a51-a255-681a325d5d1e | -12.5672 | -53.11025 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb6c3dd4-fe5b-32a5-a28d-6bc2514d0765 | -12.56307 | -53.11357 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d69ba89f-fdd8-3b44-bc08-4b8f5727b0d9 | -12.52809 | -53.12047 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5ef8851-ed03-3214-bf02-64f606ad678a | -12.62547 | -53.1243 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b72f12a-ea25-3531-b25c-f738fa536ec9 | -12.622 | -53.12371 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 4e68aa10-c98e-3891-8861-4b5559ff175b | -12.61853 | -53.12312 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| aaacf597-3723-3a3d-91a9-eef0c11abd46 | -12.61507 | -53.12251 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 136896b1-e46c-3326-ac8c-b00e36a104c7 | -12.61442 | -53.12642 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| cb56ff28-6cf9-310a-813d-05bc2ede3cf6 | -12.61403 | -53.15035 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ce211678-7b64-32bf-b998-8a44823d91f6 | -12.6116 | -53.12192 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 87bfce8d-c253-326d-90f4-94dbf05c95f0 | -12.61096 | -53.12582 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e9056c84-f145-34c6-87df-5314cdb976a8 | -12.61055 | -53.14976 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 94c3b4e6-a705-3329-b709-bff65c937490 | -12.61031 | -53.12971 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| c2252256-02cb-3507-a704-3cf4965756ab | -12.60749 | -53.12522 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f34395a5-cb68-3dec-ae34-2d836d640e24 | -12.60708 | -53.14917 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| be86103d-ec17-3db2-adc7-cc7376839c53 | -12.60684 | -53.12912 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 6c27db98-1d4c-3b8f-965f-f534757f06ad | -12.6062 | -53.133 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 0352f626-b7fe-3acc-b1f1-45b076360164 | -12.60402 | -53.12462 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| cc4c5154-c261-30be-aa3f-4fdc037a41e6 | -12.60338 | -53.12852 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 68b3b7ce-4e28-3f21-8645-34ffbb05509b | -12.60273 | -53.13241 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 7e807b40-520a-39c0-8f3e-8bc0aaba69c7 | -12.60056 | -53.12403 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7f0c281c-989a-3679-b890-a07b1d931f96 | -12.59991 | -53.12793 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 0f8465f5-944d-3d56-84fa-a4102e4484b1 | -12.59926 | -53.13182 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| cdc2aea2-dd39-35e3-91e7-1b91882841c1 | -12.59709 | -53.12344 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 20217711-89b2-340b-9e53-b31ada69dade | -12.59644 | -53.12734 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| db8a2704-b7e1-353f-866b-34a623db794d | -12.59579 | -53.13123 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 3381a268-d5d8-3887-ab70-6435dd0972a0 | -12.5945 | -53.13901 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 242fe132-10f7-3c3d-ba1d-610aa34d56f4 | -12.59385 | -53.14289 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6d9013e-2069-3725-81d9-71a793ce47a9 | -12.59362 | -53.12284 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README110.md)
