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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd5b5b98-ccee-3f90-aac5-8206caad7c05 | -17.108 | -56.20186 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 12d3b90d-0d92-3985-8a76-829801d75e45 | -17.10735 | -56.20504 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1cd6267e-fdc2-38fc-a82c-e36a1e196d75 | -17.10669 | -56.20823 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 7b2ee7d8-b7fe-3ee7-b509-d61c8493930e | -17.10603 | -56.21141 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 8bff3350-3767-30b2-8228-6fe97513ab7b | -17.10289 | -56.20075 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c388b7a3-dcf5-3085-80ff-d46498753988 | -17.10224 | -56.20393 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3adc5e74-b139-3d73-9a5a-ebc2c40f05dd | -17.10158 | -56.20712 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 48405eba-ad3d-3b1e-9e61-219145c37d1a | -17.10092 | -56.21031 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 588721b5-2b39-30a4-a074-615da2da8b94 | -17.09853 | -56.37833 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9fb0c6b8-2255-3a69-86fd-23d59cea7ca8 | -17.09777 | -56.19967 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c987c3fe-1f2f-3ab1-aa65-24059382f42f | -17.09712 | -56.20285 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1f16cb95-93fd-318a-9576-c81d7f5eb0f5 | -17.09646 | -56.20603 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 01e55f64-dc93-3c5d-8bfc-5cd3993239b0 | -17.0958 | -56.2092 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| f50e3337-606c-3404-a55f-e274068cc81d | -17.09446 | -56.20491 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 4e3cdec3-616b-38cd-b003-8292f2492b92 | -17.09382 | -56.20808 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| c12847b5-65e8-3343-8a35-d0b3d6aad667 | -17.09336 | -56.37719 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6e403383-4c7c-3d4f-a5e2-d3275b10a34d | -17.09269 | -56.38045 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8fcb8a9d-3956-3223-ae38-3b835cba2aa5 | -17.09201 | -56.20173 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6d53cc85-fd65-39e9-84b5-f54755afdb3e | -17.09135 | -56.20491 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 0832d730-bc93-3326-b8e3-1ccde0136319 | -17.09069 | -56.20807 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 2a6e2088-c847-3706-8d16-50d2cedec0f7 | -17.08935 | -56.20377 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 43fc6883-91e2-3d94-ad29-84b76ddfa167 | -17.08871 | -56.20694 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 2497ddfc-0fab-3fa1-9168-1188023b3129 | -17.08752 | -56.37934 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4e97273d-dedc-3ed1-a327-b2360a7f3d73 | -17.08684 | -56.3826 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 789a2925-e61d-33a6-874e-4f58aa99b333 | -17.08302 | -56.37495 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ac641c06-b1e4-3bfb-9a83-9aee0c95fb92 | -17.08229 | -56.13271 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 626c93b8-2820-38a1-b55a-2793b4af2895 | -17.0772 | -56.1316 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| b2ab2946-07b7-3f8c-830c-b77d20235cc7 | -17.06574 | -56.13569 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 65307726-4460-3d95-b1f1-40d81ed13d52 | -17.06511 | -56.13885 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 7ff65d9b-b0f6-3209-9a4f-21dbed5b2a18 | -17.06192 | -56.1283 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7c7971f3-01a8-3671-b35d-66f9fea33c3e | -17.06129 | -56.13144 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ea2e5516-c98c-3913-9b96-ba59cef14c86 | -17.06065 | -56.13459 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 652129c5-1be2-3941-bb87-3e93939721d1 | -17.06001 | -56.13775 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| f6ad0b33-9ed0-35d9-b6f9-0fb79db21340 | -17.05555 | -56.13349 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4c65cb5a-2026-308c-8062-6700625928bf | -17.05491 | -56.13665 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5e412321-440b-3669-80c3-a093c0ac35cb | -17.05238 | -56.12292 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d2339c65-6e5d-33a4-9303-300ad25845ca | -17.0511 | -56.12923 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4b969900-749b-33d6-b80b-10956b39da99 | -17.05046 | -56.13239 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d288926b-6f40-3f9f-a2fe-4e94e343a064 | -17.04665 | -56.12497 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9e5c06d9-825b-3847-b065-e3daefcb7de9 | -17.04156 | -56.12386 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4f5ad906-d55c-3a63-94f7-2e1b9b3f0bca | -17.03775 | -56.11645 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 46b968bc-2790-3ab9-ac7b-6651ebb51608 | -17.03331 | -56.11219 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| bc1ccb87-6ee3-308c-a539-8bbeaef7f64e | -17.02887 | -56.10793 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8a2a49f2-82c8-386e-b27b-dd27f304631c | -17.02822 | -56.11108 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 6392ea7d-089f-3e15-a6bc-bed20a1d086a | -17.02378 | -56.10683 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 5e043faa-7b44-3fce-b8ca-c58342f227ea | -17.01869 | -56.10574 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 473e3fb0-1e2c-329b-b10e-0cf10aaac171 | -17.01425 | -56.10149 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 26f4c4f6-c813-3b20-bb93-b9a88fbb3db7 | -17.0136 | -56.10464 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 70c147b9-f355-38f3-a83d-c580360428ff | -17.00981 | -56.09726 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 194e8b8e-9f1b-310c-9595-9440f03dbc97 | -17.00916 | -56.1004 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d4bec2d1-99d6-35dd-b691-d45f6c27cb13 | -17.00905 | -56.12673 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| efb1cf87-f420-3a57-b008-bdce77f50ae3 | -16.74835 | -55.82872 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| ad23ccd8-192d-3834-a24c-a2e5c7873d40 | -16.74773 | -55.83178 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| fd9fcb7d-e8a8-373c-abb0-d36e7c6bb6d4 | -16.74396 | -55.82456 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 60c7c937-1d8f-3ceb-a0ce-ab0ae394be76 | -16.74333 | -55.82763 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| c0cdbaf6-8c9b-3932-bbf1-4d8e075e7a69 | -16.7427 | -55.83069 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| afa7d222-1da1-3f91-bf6f-503a2a428b7c | -16.74208 | -55.83376 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 93124409-2cf5-304c-89c3-434ac121e766 | -16.73893 | -55.82347 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f87c5d27-d91a-37d3-8789-19a4f723c643 | -16.7383 | -55.82655 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9cec3881-0782-32f0-affa-e1fadf410d33 | -16.73109 | -55.55407 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c6ea5ec6-3a8e-3e11-86c5-23b90e515aee | -16.72614 | -55.55304 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 9e91fa72-8de6-341d-929c-4d494c9508e2 | -16.72198 | -55.82941 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5c827726-7276-3942-b204-875109c99da4 | -16.72141 | -55.83794 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5655f345-fb7a-3dee-ab6c-e143bbdbab80 | -16.72072 | -55.83552 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 784b0dea-f8a9-347a-97ce-77c700e7136f | -16.72009 | -55.83858 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f269957e-c95c-314e-a1ea-668bdc7df7b0 | -16.71699 | -55.83379 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 22cee251-5a57-3d56-b212-ce150407b5b7 | -16.71638 | -55.83685 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 62f93b10-fc83-3160-9048-944a7c69d2bb | -17.11835 | -56.17753 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1f523acf-8727-3b6a-beb5-fb0faabeac83 | -17.1177 | -56.18069 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fb917662-eda6-3a72-bf3d-89e96419131c | -17.11705 | -56.18386 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 14a4d062-7672-370d-97ac-fcf664ca720f | -17.11639 | -56.18705 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 7e8e3f1a-afa5-3914-97ea-d064677bbcdf | -17.11574 | -56.19024 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 8abed7b3-5df0-362f-9581-d4264ae3a8f4 | -17.11508 | -56.19343 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| ca20347a-b50b-3d98-84e7-a49eccabfcf2 | -17.11389 | -56.1733 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 23c9db06-c3b2-3295-b557-94a6e863e4b0 | -17.11324 | -56.17645 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f2db46a9-e961-3d8e-8c29-26a2b04f9238 | -17.11194 | -56.18278 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 647a67d5-18d7-341e-9d52-5c48753c639c | -17.11128 | -56.18596 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| c41110b4-d218-3441-962f-729467756172 | -17.11063 | -56.18914 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d848e1c8-2ab0-322d-9643-57240c036405 | -17.10814 | -56.17535 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9f6c3914-9137-3f74-8eda-2329aba71237 | -17.10749 | -56.17851 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6ae8c50e-64e8-3a8e-82ee-a926db6e6b20 | -17.10683 | -56.18168 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 8c8ffc0b-9fc3-3049-a892-9e9bea3902a4 | -17.10617 | -56.18486 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0e0f0de8-7546-3231-972c-12c987457771 | -17.10304 | -56.17424 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 012abf9a-ebd3-3582-a35e-0d91f3b29371 | -17.08485 | -56.14646 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 498e9a1d-721d-3129-9233-39d9b3cccadb | -17.06956 | -56.14312 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3972ef19-5535-3d9a-bb00-9ccea11a1aa6 | -17.03252 | -56.16815 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d01a6f4d-6570-35ef-b2c1-ab6e5f39d3fd | -17.03187 | -56.17134 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4f2d84c5-04bb-3ccd-9f41-61bdd162699f | -17.02741 | -56.16703 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 76c56f97-c340-3ed2-9626-7a6448cee900 | -17.0249 | -56.15326 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 935c0485-137a-3023-bab0-16c2a09e5138 | -17.02231 | -56.16592 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 71e21af4-4d44-3c87-bb22-b60995a1a187 | -17.02165 | -56.16911 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| e1ab3c27-eba8-3b82-8ad7-630c6ee92f62 | -17.01915 | -56.15532 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6239f0a6-23e3-359b-99ed-bd0411003e40 | -17.0185 | -56.15847 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| cd708f8d-1879-33b4-9955-9c048ec27188 | -17.0172 | -56.1648 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 04d1c5ba-e115-34bb-86dd-38a336678060 | -17.01655 | -56.16798 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| b1e44b3b-cb1e-3a90-8241-abbc2af2d49e | -17.0159 | -56.17115 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 76563b67-f3bb-3f54-9b81-bc5a4893f3ea | -17.01534 | -56.1479 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 21e0f73e-c81e-39b3-a2f0-dcb3ca6c7489 | -17.01469 | -56.15105 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ff887217-77b0-3e95-9fc7-08781011cb5f | -17.01404 | -56.15422 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 83e56010-956e-3f09-9154-2a3bb74b582c | -17.01339 | -56.15739 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |


[Clique aqui para ver as próximas entradas](README67.md)
