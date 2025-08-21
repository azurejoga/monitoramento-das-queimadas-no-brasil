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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c89da7ed-e01d-31c3-8c39-0cca2df06ea2 | -2.38465 | -47.6594 | 2025-08-21 04:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3d48204d-5d1c-3944-9ac6-6f2a39cb595a | -3.04357 | -49.42561 | 2025-08-21 04:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3ffc7fa-23f7-38ef-a6d3-bae73787ab10 | -3.81823 | -41.55807 | 2025-08-21 04:14:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fe059d08-80cf-3350-8bbe-715f788c3d1f | -2.43951 | -48.61447 | 2025-08-21 04:14:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e47e1ba-2dda-399b-a3c6-c19d64e5db98 | -4.64418 | -41.40465 | 2025-08-21 04:14:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 537cc298-c20e-30f1-b223-f1357ee78adb | -4.81751 | -47.31606 | 2025-08-21 04:14:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89e313a8-30ba-3253-89df-104dd7b22c5b | -17.50301 | -48.0041 | 2025-08-21 04:17:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1147087a-163c-343f-9dc5-e8bdb4c73a2b | -17.06104 | -43.06483 | 2025-08-21 04:17:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| e757dc12-0eed-3b77-9333-afddbfe2710c | -17.58479 | -42.27435 | 2025-08-21 04:17:00 | NPP-375D | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 92c28531-5269-3e01-8b74-08b8b412f1ae | -17.3923 | -44.24746 | 2025-08-21 04:17:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e682dfce-954f-3438-bbfb-1d47e74e5521 | -15.00214 | -54.84309 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8ff0f32-dcc5-3ec0-ae26-6384677b674f | -18.29195 | -45.51518 | 2025-08-21 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf02846e-7382-35ee-bff8-0994d0f3cbe1 | -18.30137 | -45.52051 | 2025-08-21 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46474409-e52e-3537-94ce-38a9b8af8f21 | -18.29357 | -45.52665 | 2025-08-21 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bde18e8a-8c5b-3316-bb2b-0552eecec707 | -16.1139 | -46.82609 | 2025-08-21 04:17:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d03badcc-a04c-321f-9026-97a60343385c | -16.0067 | -43.70774 | 2025-08-21 04:17:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b86a9c26-da15-3d9a-a1d0-d25fa747f1e2 | -14.36697 | -51.97355 | 2025-08-21 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 85ca0117-ff72-31cb-aa0b-626efea809ec | -15.01936 | -54.83936 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d340ffe-f521-31c2-b738-29abfeb6db00 | -13.86935 | -54.06206 | 2025-08-21 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 113906a1-378e-3f0f-af81-17b99c098469 | -15.76873 | -43.22546 | 2025-08-21 04:17:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eb08caeb-087d-3998-9fed-560cc488b8ad | -19.8112 | -41.90105 | 2025-08-21 04:17:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| af8f1c58-ea3a-34d6-b23b-a731869a784b | -17.39568 | -44.24801 | 2025-08-21 04:17:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 980d37e4-bc02-385c-b09b-ee0f966cdc8d | -14.99958 | -54.82741 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c99707e-3a9c-3d7c-9891-fed0847c5d99 | -14.39003 | -52.00365 | 2025-08-21 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99b2f2cf-14e6-390d-81dc-0d94b32ee5df | -15.91902 | -47.34553 | 2025-08-21 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70a5308c-bc6d-3c25-8223-f2c086494f06 | -17.38893 | -44.24691 | 2025-08-21 04:17:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e579160-4ade-37a7-ba12-374852906f86 | -15.00572 | -54.85009 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 939c9c62-9159-3c1f-90e5-2748a8efe3ea | -16.50663 | -46.73521 | 2025-08-21 04:17:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fbcf6d8-2736-32e2-a0f7-078e582fef9e | -14.36607 | -51.97837 | 2025-08-21 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cd0aecb1-0c2d-3d7b-ac2f-62f2ffe0a89c | -16.50628 | -46.73606 | 2025-08-21 04:17:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1689903b-4f56-3a64-82a2-c8990c5cfd89 | -18.2853 | -45.51404 | 2025-08-21 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6d268fb-4c3d-3225-963f-9b2333cf701e | -18.29024 | -45.52608 | 2025-08-21 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3919fb4b-2156-3669-a200-05b619ad92fe | -15.0014 | -54.84681 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a35d9349-4ceb-378e-8ee3-aa9c201d4794 | -15.00655 | -54.84609 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14d96a32-9257-3297-aa54-a2ea6f9dc15f | -18.29633 | -45.53085 | 2025-08-21 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a6130c8-94ec-39a2-b54a-3ff31185a6ca | -15.01547 | -54.83342 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41510a6a-4b10-306e-bf6f-7cf7f913d37e | -14.75385 | -56.01861 | 2025-08-21 04:17:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97d0b7e6-cc44-3047-818d-1a12b7dc0412 | -15.51718 | -48.05604 | 2025-08-21 04:17:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e928dfa-5ea7-3677-9361-6587f2d07361 | -15.01368 | -54.8392 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b4b25a0-ff4b-3323-ae8f-6fdb7e783759 | -17.39286 | -44.24376 | 2025-08-21 04:17:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 707df7a9-83c2-3eb4-86b7-48e11f9f2bd0 | -15.56518 | -50.32141 | 2025-08-21 04:17:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53248866-ef37-3ab1-a35c-ce0cbdb09b7a | -15.01686 | -54.85143 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f15cdca-a118-31bb-b095-49ce26fe460e | -15.1921 | -48.70022 | 2025-08-21 04:17:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6aa68a1b-923d-3811-8f45-ff0b0f798d97 | -18.28473 | -45.51767 | 2025-08-21 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fcac12f8-1cb7-3bd4-b12f-5f5bcea6a38b | -18.28967 | -45.52972 | 2025-08-21 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89fe650b-8c99-328a-90bf-7161bc4d9780 | -18.28863 | -45.51461 | 2025-08-21 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b7b7284-c2df-36c8-88c9-04f8ddaca88c | -14.99883 | -54.83114 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a921f548-e6d4-3939-84f7-3f9b726f2d00 | -15.02008 | -54.83586 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35551de4-b660-3c0e-ad55-786f020b5288 | -18.29471 | -45.51938 | 2025-08-21 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 13537b0b-248b-3ce9-b4ab-70f4d22c097f | -15.01894 | -54.84462 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0909f2f5-3035-3a45-96dc-f8a557084ec1 | -18.30023 | -45.52779 | 2025-08-21 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 90700d07-35ea-3e6d-8902-4fee9a28ecab | -19.0933 | -46.68906 | 2025-08-21 04:17:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6620c177-c501-3ae9-b004-e80cf01f56e5 | -15.19476 | -48.69829 | 2025-08-21 04:17:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ecc936e-a79b-3197-a43b-4bf2eceafdbb | -18.66265 | -46.97622 | 2025-08-21 04:17:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd585691-512f-3c42-9475-f2fb8c853b5c | -18.12646 | -43.9537 | 2025-08-21 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c61b087-e37c-342b-912c-f3c8f670ceea | -15.00989 | -54.83286 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a814dd5-7369-3fef-9370-bbcf5c51ce85 | -18.66664 | -46.97305 | 2025-08-21 04:17:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1189558-e2cd-34df-bd47-23d6a16d82b3 | -14.75196 | -56.02747 | 2025-08-21 04:17:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd175217-eb58-31b0-be1d-d29f4e9d66da | -15.5136 | -48.05539 | 2025-08-21 04:17:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb602400-2c15-30fd-8e2c-9a39c05d52ab | -15.01515 | -54.83209 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18e6f4c3-31c2-307a-b598-9071fedf0f8e | -18.29138 | -45.51881 | 2025-08-21 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebed5055-a64b-369f-bd43-40846b30d791 | -17.05752 | -43.06448 | 2025-08-21 04:17:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 24d4ef7d-9b8c-33d0-9172-41fad98586ca | -14.37443 | -51.97843 | 2025-08-21 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 85954d70-79f0-320b-b2ec-706e44a46d33 | -18.29804 | -45.51995 | 2025-08-21 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 423ef31c-90b6-339c-a1ad-0041d1925075 | -16.21834 | -47.39276 | 2025-08-21 04:17:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c46e8032-5d89-3fb5-ae29-cc740c01892f | -15.02244 | -54.85208 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6d6bf2b-804a-34d8-b599-4d89b56dd14b | -15.00613 | -54.85166 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1137dda8-aa1e-30e0-8a50-638bbce426a7 | -15.50145 | -48.04013 | 2025-08-21 04:17:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 23.6 |
| dd7f9c59-0b78-3f5d-978e-73cdaf9cb346 | -15.001 | -54.84528 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 083f3c1d-d62c-3693-affa-a1fb30f9f3ff | -18.2969 | -45.52722 | 2025-08-21 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d118fdcf-aa73-326b-8e96-2369372881a9 | -15.00694 | -54.84761 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9e0b4df2-6a4e-3383-bf0f-4b210d1156a4 | -16.10591 | -48.01002 | 2025-08-21 04:17:00 | NPP-375D | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e8a17e18-e248-3bd4-b8ce-9f761b7f6b6c | -16.51464 | -46.72895 | 2025-08-21 04:17:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56a0d666-cc91-30b5-9bdb-5fa965617d8e | -14.74988 | -56.02562 | 2025-08-21 04:17:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33f733b3-546b-3a37-add3-5fc550f9e1b6 | -17.82376 | -44.41196 | 2025-08-21 04:17:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0b9e3594-91e9-3bfa-ab6e-356b6ccf249f | -16.26498 | -47.8644 | 2025-08-21 04:17:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 097b12e1-32af-39ee-b1ed-c92638a44669 | -18.48887 | -47.45512 | 2025-08-21 04:17:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fc4fb698-8ba5-31fe-8cfa-baa802e71455 | -15.50574 | -48.03653 | 2025-08-21 04:17:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee72b80f-2b3c-3e1e-a319-0679e79c7e3a | -15.56583 | -50.31792 | 2025-08-21 04:17:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 598ff999-84ae-35bc-b7af-b30e3840f20b | -14.61991 | -54.87592 | 2025-08-21 04:17:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32bb40fd-44b7-38b0-8231-b619e04c5798 | -14.61916 | -54.8796 | 2025-08-21 04:17:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4acc8eab-ade8-3d2b-bc86-88c989e89158 | -15.73733 | -46.11401 | 2025-08-21 04:17:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 50507038-649a-3d70-98e7-4c347f63d312 | -15.50716 | -48.04987 | 2025-08-21 04:17:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bb096903-3a1d-3840-9560-dc8cdaf4eabd | -13.86865 | -54.06554 | 2025-08-21 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 875154d1-7c7e-306a-9cc0-c9c357948d62 | -15.86379 | -48.77855 | 2025-08-21 04:17:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3ebe6e3-41be-30f3-bacc-b6b3794af39a | -18.3008 | -45.52415 | 2025-08-21 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2922602b-5dcc-3524-ab5d-653df655b633 | -15.93549 | -46.93146 | 2025-08-21 04:17:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e115855b-5796-3efa-985c-e78caa423c22 | -18.293 | -45.53028 | 2025-08-21 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1fc99f8-10c4-3752-b1cf-9b2f88d77f84 | -18.29965 | -45.53143 | 2025-08-21 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 14aa745e-3ef5-38e1-b0fb-8ead1b454f8d | -19.09664 | -46.68962 | 2025-08-21 04:17:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90694b8c-7daf-393b-bf01-13c960626cd1 | -14.62469 | -54.88073 | 2025-08-21 04:17:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57eea5bc-6187-31e5-b087-ba6327dce823 | -18.66327 | -46.97247 | 2025-08-21 04:17:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57582f98-7dde-3622-9028-3b5e3c1198f5 | -14.63946 | -54.86469 | 2025-08-21 04:17:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01f991cb-a8d1-33c5-90fc-acc82cc20a64 | -18.12988 | -43.9542 | 2025-08-21 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3e13a76-c73e-3881-bcd4-3ded86e72ceb | -15.57864 | -50.3166 | 2025-08-21 04:17:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d519db18-a76d-3aa6-8e5c-97ec69f1d823 | -15.01857 | -54.84315 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| faa0c40d-8296-3a9c-91a1-61b1ba89cb40 | -15.58332 | -50.31396 | 2025-08-21 04:17:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25be11a4-80b2-3cd8-9e61-18662865c576 | -14.62778 | -54.86554 | 2025-08-21 04:17:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d6b0057-9b47-39ed-8679-5d2fd86bd9b8 | -18.29747 | -45.52358 | 2025-08-21 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 17ef462a-7081-3a9b-bdc6-66fa38cb64b0 | -15.51002 | -48.05476 | 2025-08-21 04:17:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README23.md)
