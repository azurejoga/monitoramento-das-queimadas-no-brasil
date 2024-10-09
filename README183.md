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

## Dados Diários - Página 183

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2c95809-f425-3c89-9962-2cd9206671f3 | -10.65264 | -61.74856 | 2024-10-09 05:04:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c7bed07-cd2b-3657-817b-84507b98c89c | -10.64803 | -61.7513 | 2024-10-09 05:04:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c30a8081-08ae-35ae-93c3-b3d65b32fd80 | -9.75583 | -62.3735 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c02823ee-734b-37f7-88c6-ebf984bb75a2 | -9.75259 | -62.36938 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03b1dc5c-f2a6-3e0f-8d45-5983f9cc973c | -9.75192 | -62.37336 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bb6ca232-1f51-3d4a-9b1a-dbf64d5bbed3 | -9.7516 | -62.37273 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52e4f1d3-4bbf-3866-9ad5-40b4cbb071c2 | -9.74889 | -62.34008 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ac9a3b2-5dec-34a2-a7d9-de0781d784d9 | -9.74467 | -62.33928 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7b468bd-89b4-37c6-9c92-20b505ba8573 | -9.68551 | -62.3041 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| afb5d32d-688a-3839-8a7d-a118b19b1a08 | -9.65311 | -62.43809 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4be459a0-5f4a-3e76-9dbc-6b71176b46ca | -9.6524 | -62.4421 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43603621-7832-37a4-8db7-ffcf766b0944 | -9.61738 | -62.47483 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de20c29f-8635-3511-92f6-c6409d51b1a7 | -9.47318 | -62.3756 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b6cda6f-9e40-3c3c-bd58-fe42468a2492 | -9.40099 | -62.34328 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 561c02fd-e9a2-3c93-a010-d0338e417781 | -9.39676 | -62.34244 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 656149e7-de0f-3bcc-82b3-9a39d486b11d | -10.86375 | -62.02364 | 2024-10-09 05:04:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2029ad88-2cb9-3611-a25b-481145c9231c | -10.85969 | -62.02288 | 2024-10-09 05:04:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 584c50c8-24f9-35cf-a7d5-559c3e9f3219 | -10.85905 | -62.02657 | 2024-10-09 05:04:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d6aebf2-435c-3e79-b864-2f78d4d9c963 | -10.14142 | -62.11097 | 2024-10-09 05:04:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18c2edcb-5897-3082-a979-24cb869fe86b | -10.14076 | -62.11467 | 2024-10-09 05:04:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe9875be-7e61-30c1-b50c-223fae185751 | -10.13729 | -62.11018 | 2024-10-09 05:04:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfa81c85-9517-38b2-bed9-22d0e2d3d332 | -10.13664 | -62.11389 | 2024-10-09 05:04:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4266f566-8211-3861-a794-6fdcaca7f70e | -10.13598 | -62.11762 | 2024-10-09 05:04:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75fcc6d5-c9b7-3db4-b382-a6dfebe2ecfc | -11.97574 | -63.16771 | 2024-10-09 05:04:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9feee224-e4a5-3971-a875-f9e53da8620b | -11.95464 | -63.2113 | 2024-10-09 05:04:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49920b48-7c93-3521-a047-122d8ddcd88e | -11.89269 | -63.28227 | 2024-10-09 05:04:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f795f9fd-84db-3e73-905d-b8a4a8bfdcc4 | -11.88912 | -63.27723 | 2024-10-09 05:04:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3975cb71-54f9-39e3-9d47-e3a5dbd75606 | -11.88836 | -63.28143 | 2024-10-09 05:04:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b0c1f9a5-47f6-32ce-82b7-f2a5239d229b | -11.88403 | -63.28061 | 2024-10-09 05:04:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e8f728b-60f4-3f25-92ef-2d83a0469069 | -11.87969 | -63.2798 | 2024-10-09 05:04:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2db45954-01a9-3079-baaa-ac8c54667595 | -11.62882 | -62.16835 | 2024-10-09 05:04:00 | NOAA-20 | NOVO HORIZONTE DO OESTE | RONDÔNIA | Brasil | 1100502 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48f0c490-62cb-380d-a70b-f98d018ce5d1 | -11.48249 | -61.97794 | 2024-10-09 05:04:00 | NOAA-20 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 0412a5f6-ac39-324b-a2d4-d6c36a5b4b56 | -11.30954 | -62.03196 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c047f92-c712-36bb-9cdd-1de462f5123b | -11.89634 | -62.78216 | 2024-10-09 05:04:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2aaf6c3c-d65a-321d-bb5b-0ca9a0bc9529 | -11.82365 | -62.62775 | 2024-10-09 05:04:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b675559f-7e36-3ae1-810c-bcb9169d2459 | -11.78233 | -62.8845 | 2024-10-09 05:04:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ffb55b49-314d-3860-be23-4e041c2be589 | -11.77811 | -62.88366 | 2024-10-09 05:04:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd763bbf-4b3a-3dbd-98ca-5bb21f99ad06 | -11.77388 | -62.88286 | 2024-10-09 05:04:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11e0319f-5076-3886-8c70-acdb58c92a16 | -11.76965 | -62.88207 | 2024-10-09 05:04:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ff43bf3-9964-34c0-a4cc-4b7fb725e66f | -11.76542 | -62.88131 | 2024-10-09 05:04:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4449fb47-8d04-3999-b6f3-e935122e1230 | -11.76469 | -62.88537 | 2024-10-09 05:04:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93505550-ec70-3b1e-ba70-bcb2da6ba732 | -11.76118 | -62.88054 | 2024-10-09 05:04:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e71a3b94-9d8f-3b5a-ac55-bf2d9f7b8ab3 | -11.0665 | -62.55781 | 2024-10-09 05:04:00 | NOAA-20 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afa3f456-8865-3caa-84e3-0dd60df1dbc4 | -12.89681 | -62.18818 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78038198-4b8d-39a5-96ff-1f8e968bad6a | -12.76528 | -62.27032 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ec3cc90-a9cf-341a-ab74-01346cdaef5b | -12.76191 | -62.26602 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0f3a796-90e4-3721-a1ac-835f504332d9 | -12.76128 | -62.26958 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bf249717-aecb-3ff5-a53a-8a1c26373906 | -12.76065 | -62.27314 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 498d51d3-987a-347b-bf1b-eb881bfdbd2e | -12.7598 | -62.25458 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07ca1428-9563-32d7-bdbf-46f95af29f0f | -12.75916 | -62.25815 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b69332dc-a85f-34b3-9bcf-9cbd05e6ca27 | -12.75854 | -62.26171 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd50fa79-89a2-3132-9b2d-ff5641571f77 | -12.75791 | -62.26527 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08324246-d281-3e57-80a8-c4c1b54819d4 | -12.75728 | -62.26884 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a5f59192-1c76-3235-a74e-ceccda734718 | -12.75665 | -62.2724 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4c099d02-e6a4-351f-8e76-6337215e7427 | -12.75602 | -62.27594 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7685b339-c4b0-39ff-b5e1-033bf24df795 | -12.75579 | -62.25385 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2b0cdda7-98ba-3281-a1b0-2f4469f66438 | -12.75516 | -62.25741 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7818828f-2b9a-3067-8f7f-1ed57c09fba3 | -12.7539 | -62.26453 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad9c00d1-fb8e-3f3e-93fd-40b3bbf571c5 | -12.75327 | -62.2681 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e476985-b3b8-376d-901a-d34eedbbef8e | -12.75265 | -62.27165 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d24f10b6-c8ad-3337-9e3c-2e3702d675c5 | -12.75202 | -62.27518 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5df397ee-41df-3d8f-b07e-7427c5104f5d | -12.75054 | -62.26023 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e1f4119-c2ed-337f-b31d-cf0626fcf663 | -12.74802 | -62.2744 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b8306d9c-9c4f-38f1-ab10-79190ce1bae7 | -12.74654 | -62.25949 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efa26c07-f2e8-3e2c-aae9-73d8f5d44a6d | -12.74465 | -62.27012 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d240c7cc-4617-3021-909a-6b2d2f9e38fd | -12.74254 | -62.25873 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2aa04343-41f7-3313-8393-b6378faa7047 | -12.74191 | -62.26228 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90a411ca-833a-3484-9c34-406fff4a333e | -13.06707 | -62.52792 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8714bb5-8bcd-388d-9acb-532c8436c6b5 | -12.99895 | -62.7457 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b6fccf05-b4eb-3531-b12a-01025d16c6a7 | -12.99417 | -62.74868 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43492a49-d9b8-3fdb-9bf1-fd1a48769445 | -12.99412 | -62.72525 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7fdc5f91-da6b-3ef4-9f73-3c859514e7d5 | -12.98555 | -62.46743 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| da471c6c-3da5-3293-928b-ad59c5c01599 | -12.98491 | -62.47105 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6ccc4401-93e1-30df-b81b-343201b78dce | -12.98214 | -62.46303 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cefee606-10b6-3fa8-a3de-626291a626b0 | -12.98024 | -62.47392 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e20c209-3e6a-36fa-9a0f-37f17465d8bb | -12.97811 | -62.46227 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd4226dc-b6ca-3a0a-bf57-babd95806773 | -12.9762 | -62.47319 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1c97a4f1-4110-3ac6-a7d9-cd2ab1eed6dc | -12.97471 | -62.45789 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cef631ec-48f3-3365-b633-38bfa955d876 | -12.97216 | -62.47243 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c791e333-f9a0-39a1-b964-24400727e802 | -12.97067 | -62.45713 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 28b6a12e-7b0c-3b63-88c0-94d6fefe7612 | -12.97017 | -62.69354 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ec71ed1-26a9-3078-9b56-eed7dd78e4ec | -12.96812 | -62.47167 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 78c5add7-9ac2-34fa-8999-762ef2024da0 | -12.96663 | -62.45638 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0eea6a3-b983-32a6-b7f4-22340bbd618d | -12.966 | -62.46 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77d5eb63-7ce4-3977-9c23-21e9cb9b649e | -12.96556 | -62.48623 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb93f89f-fd57-3171-96c6-8860977d7329 | -12.96492 | -62.48989 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5bee862-a61a-3cab-a11d-53d631db9d05 | -12.96152 | -62.48547 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c58ce14-6142-357d-a1e8-50f8bafa6d3c | -12.96087 | -62.48912 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c000f388-4784-3fc0-a1f6-1d62e5ff703e | -12.95747 | -62.48471 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2cfdcb8-e74e-33dc-b6cc-45d6c99bbc90 | -12.95683 | -62.48836 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bb811d1c-b1a3-3177-9fe2-7148f852a306 | -12.95618 | -62.49202 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04bab27a-d9b3-38fa-ad99-ebc692523172 | -12.95554 | -62.49569 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb03043d-62da-3e37-ad0b-f5bb00239d1a | -12.95278 | -62.48761 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3546479e-2d43-365b-aeb9-ba0b774116cd | -12.95214 | -62.49126 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b880a5d-e887-3ecf-aba0-ae600692da3a | -12.95149 | -62.49493 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05eb6285-05eb-307c-92c7-584f8ba89b94 | -12.95084 | -62.49859 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7485704e-edf1-3c7f-ad06-3b44ad1554e8 | -12.94985 | -62.45699 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d59c1f4-741a-3f6d-972e-0bb9f547ec30 | -12.9492 | -62.46062 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 975d5d6d-dc1b-3fca-98a8-2a7598909e5f | -12.94581 | -62.45624 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f1bd802-b0f2-320d-9fb3-15d7a8069a01 | -12.94178 | -62.45549 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README184.md)
