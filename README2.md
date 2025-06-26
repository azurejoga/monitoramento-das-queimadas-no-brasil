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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d03b23ec-a1ae-320b-bf27-63f969944617 | -9.121 | -49.4528 | 2025-06-26 00:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 444c77b6-d2e0-37ad-b4a9-e3de713a0d99 | -7.2031 | -43.0701 | 2025-06-26 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 60.9 |
| e1e6d034-0be5-3eb7-aa61-e8056c09a5bd | -4.524 | -48.0593 | 2025-06-26 00:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 167.6 |
| ce9a28bf-de53-38fb-b710-70caa35ef50e | -11.0896 | -46.6422 | 2025-06-26 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 66a10a4e-702c-33b1-b47b-28c72b09c1f1 | -4.5427 | -48.0367 | 2025-06-26 00:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 245b04a5-097c-38d4-9fc3-c1241732aa81 | -11.0644 | -55.3757 | 2025-06-26 00:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 131.2 |
| d451271f-2ad0-38be-9be6-0cb3fb9ff0bb | -9.518 | -56.0975 | 2025-06-26 00:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 201b32c5-464c-36de-9006-907ec339703a | -6.1975 | -48.0916 | 2025-06-26 00:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 68d8037b-b957-3377-b3e0-f16561a74e43 | -11.0705 | -46.6447 | 2025-06-26 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 227.5 |
| e52fe1ef-ec27-3aad-8c7f-51626cd5e424 | -11.0709 | -46.6221 | 2025-06-26 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 75030664-8669-3458-bad4-b787d6b2a07d | -9.1213 | -49.4313 | 2025-06-26 00:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 60a2381e-db5f-3b18-84c7-9b91d047310b | -9.1213 | -49.4313 | 2025-06-26 01:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 98743e58-0735-345a-9c68-75554e6be240 | -7.2028 | -43.0936 | 2025-06-26 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 44.7 |
| dd97e664-ac04-3213-9d82-86d04307ac09 | -4.524 | -48.0593 | 2025-06-26 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 152.8 |
| 25625bc1-029c-3e64-a5cb-2dbbb83047c8 | -4.5426 | -48.0584 | 2025-06-26 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 19dba21e-ab68-3357-b624-3314152b19ac | -4.5242 | -48.0377 | 2025-06-26 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 173.3 |
| cd3f8dbe-be40-3d98-991b-46d4751b83b2 | -9.121 | -49.4528 | 2025-06-26 01:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 8c8fed90-2592-3e47-8fd3-e03615f59a7e | -9.518 | -56.0975 | 2025-06-26 01:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 36f7185a-eff8-3fb3-a8a1-57e9abaf8fd9 | -6.3687 | -43.7525 | 2025-06-26 01:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 14a6838a-0d89-3bdd-8fab-59b049fa149d | -11.0644 | -55.3757 | 2025-06-26 01:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 9348be54-6c94-3e06-bac1-d5b57cf057ee | -9.4993 | -56.0988 | 2025-06-26 01:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 28d8ddc0-7fd7-36e4-980d-5f975a93976a | -11.0896 | -46.6422 | 2025-06-26 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 2cf9a7e5-3d20-33cb-b467-5506b373f181 | -11.0705 | -46.6447 | 2025-06-26 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 66fccc7a-b106-3884-9728-c024be79fb5c | -4.5427 | -48.0367 | 2025-06-26 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 6bbdaf1b-6e5f-3a70-9b77-acd77b2363db | -11.0832 | -55.3741 | 2025-06-26 01:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 8be53a05-8bc3-3e58-ac1d-73aa6873248d | -13.0408 | -48.825 | 2025-06-26 01:00:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 45859410-caaa-3868-9b1a-230dc7cd824f | -9.121 | -49.4528 | 2025-06-26 01:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 1e190602-0375-3f20-8ac9-7b12a74135f7 | -11.0832 | -55.3741 | 2025-06-26 01:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 163afa00-841d-3c07-8bd6-d83bf04dcc02 | -11.0514 | -46.6471 | 2025-06-26 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 36ac2c05-1083-360c-8bb1-39ce20f57aeb | -4.5427 | -48.0367 | 2025-06-26 01:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 3da48a6b-3047-3d35-9130-eed3948fbe56 | -11.0705 | -46.6447 | 2025-06-26 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 255.4 |
| b849719c-5bb8-3a3b-89a6-33698f3593f2 | -6.1791 | -48.0712 | 2025-06-26 01:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 323.4 |
| ce6b1305-10d3-3fcc-898a-a25000affd1e | -6.1789 | -48.0929 | 2025-06-26 01:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 159.7 |
| c64efd1e-913c-3ec8-8902-41d46d76b29f | -6.3687 | -43.7525 | 2025-06-26 01:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 26592f73-4585-3d19-84d4-da137b6aeb20 | -4.524 | -48.0593 | 2025-06-26 01:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 144.7 |
| 466c9e56-73e8-3625-b8ad-694f3188fdf4 | -13.0408 | -48.825 | 2025-06-26 01:10:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 5299b0a7-73dd-3392-bab3-39af659414c9 | -6.1977 | -48.0699 | 2025-06-26 01:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| cbef821f-2be4-3a47-ab66-c0a7084daf34 | -6.1604 | -48.0724 | 2025-06-26 01:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 17ac8ede-6286-3925-9d3f-657ebc8b7f92 | -11.0701 | -46.6672 | 2025-06-26 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| fb9611ed-6d35-3bbb-b1c3-de9638266949 | -7.2031 | -43.0701 | 2025-06-26 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 38.1 |
| 0f9df41a-81c8-3bd1-a0ff-a6fbb03576a1 | -4.5426 | -48.0584 | 2025-06-26 01:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 5b043db0-97f2-3862-ab82-afa477d019b3 | -9.4993 | -56.0988 | 2025-06-26 01:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| bd1af2fd-5bcc-3685-92fc-908f18aa02cd | -6.1602 | -48.0941 | 2025-06-26 01:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 42.8 |
| e340f581-14f4-3f28-b4ae-1cfaca18d905 | -11.0709 | -46.6221 | 2025-06-26 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 245590a9-26aa-3d5c-bfa9-f8f0eb8cc061 | -11.0644 | -55.3757 | 2025-06-26 01:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| c141bcb4-fcdf-3cc3-8910-8008afa87922 | -4.5242 | -48.0377 | 2025-06-26 01:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 141.7 |
| 171da7c4-817b-3a81-8da0-20204f793ca9 | -9.518 | -56.0975 | 2025-06-26 01:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 5a24a2ff-c8b0-36ac-81f4-e7214a87cb97 | -6.1975 | -48.0916 | 2025-06-26 01:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 3f64a4ba-0f2e-33ef-83b8-01f9046e8823 | -7.2217 | -43.0917 | 2025-06-26 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 35.0 |
| 1183e282-52fd-3413-b857-e6218ec56b44 | -9.1213 | -49.4313 | 2025-06-26 01:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 5744e03a-2e0f-3a63-b41f-f4a9f448f32d | -7.2028 | -43.0936 | 2025-06-26 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 60.7 |
| e8bfe9bb-34d6-361a-bbdb-8fa6acfc7441 | -21.18606 | -48.69133 | 2025-06-26 01:17:00 | TERRA_M-M | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 50.5 |
| 55988630-97c3-3373-81e9-1f7bf854dc74 | -4.524 | -48.0593 | 2025-06-26 01:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| ee3f6444-5113-3d9e-acfd-f015a99ee62b | -4.5242 | -48.0377 | 2025-06-26 01:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 78a9b6de-6c18-33b9-ab20-3835a62f4155 | -9.121 | -49.4528 | 2025-06-26 01:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 3dfcc8be-b625-3858-9379-dd01fdb728ad | -9.518 | -56.0975 | 2025-06-26 01:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 4afe5226-b399-39b4-96cd-7961545c65d5 | -6.1604 | -48.0724 | 2025-06-26 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 64aa7e8b-7c6c-32be-ae46-f3f2f4f0acd8 | -9.1213 | -49.4313 | 2025-06-26 01:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 163f275a-b8f0-3f4f-87c0-e49ecfe5c351 | -6.1789 | -48.0929 | 2025-06-26 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 6dcc3df1-24f1-3971-8146-67b6e0608e08 | -11.0705 | -46.6447 | 2025-06-26 01:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 5cc5ca99-b8e8-3552-9328-5ee09371a117 | -13.0408 | -48.825 | 2025-06-26 01:20:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 916526b8-bbb1-35ba-b1ea-8849aae0e7df | -10.2941 | -57.138 | 2025-06-26 01:20:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 482dca65-ac3a-32cf-a754-32ce45bf9f06 | -6.1977 | -48.0699 | 2025-06-26 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| a6a7d509-15b1-37da-b3e4-95d3ca70eb8e | -9.4993 | -56.0988 | 2025-06-26 01:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| c6bb3fc8-4a28-3045-98e6-1a8e7f4634d3 | -6.1791 | -48.0712 | 2025-06-26 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 280.7 |
| ac29ed52-aa75-3e00-9a6a-c080cca0a5fc | -11.0644 | -55.3757 | 2025-06-26 01:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 436640f9-bc85-3c12-83ec-d2c39aa57ff5 | -6.3687 | -43.7525 | 2025-06-26 01:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 48aab59f-03e4-34a7-8c6a-554115fca974 | -6.1602 | -48.0941 | 2025-06-26 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 6525ed6f-6b5d-3efb-be65-8a0514127a35 | -14.91186 | -54.33115 | 2025-06-26 01:20:00 | TERRA_M-M | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| e59782f6-ad2d-38f0-b961-b73bfc536c64 | -11.43937 | -54.48203 | 2025-06-26 01:20:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 354299ed-da15-3828-b46d-a1d7d59f5e31 | -12.6179 | -57.87204 | 2025-06-26 01:20:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4d206e90-3629-3b41-bf0c-4a2909c65561 | -13.09863 | -52.30088 | 2025-06-26 01:20:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 65d15cdc-ef1a-3b62-ad1c-f4b4cbc41293 | -10.82791 | -53.73657 | 2025-06-26 01:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| a8091352-7640-3d50-9adf-44e0f71eff47 | -10.83034 | -53.74462 | 2025-06-26 01:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 33eb76f5-c60c-37da-81a6-fbba9a59b4f4 | -12.02843 | -57.08809 | 2025-06-26 01:20:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 7bd6aeb0-10c0-39fe-b0e9-8d1abf591014 | -11.07397 | -55.37842 | 2025-06-26 01:20:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| c7ee569a-c7c3-3fa1-b2a6-cbf8391a656b | -13.05652 | -48.83742 | 2025-06-26 01:20:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 6400b728-1908-3e8b-8458-874fd906764e | -11.87191 | -54.69381 | 2025-06-26 01:20:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 94c282a2-64bd-32bd-8ad6-11de14d4bc6f | -11.80699 | -57.34713 | 2025-06-26 01:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| fafe4350-7fae-367a-84d0-5d05d2d1cc12 | -12.588 | -57.38995 | 2025-06-26 01:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ee9cc48f-9f2e-310d-b85e-8346023454ac | -13.29248 | -57.09426 | 2025-06-26 01:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 2e490fcd-4378-3c67-9b14-a3579b6ca259 | -11.13343 | -53.91277 | 2025-06-26 01:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 16d8772d-dc2f-3e6a-9159-046917ffb963 | -11.13566 | -53.9269 | 2025-06-26 01:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 4b88dc3b-8f79-39ad-aed9-cce7862b8136 | -11.61038 | -55.54725 | 2025-06-26 01:20:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 7d62b05b-3a94-3507-80b5-a78a9d724d1a | -12.78962 | -48.73256 | 2025-06-26 01:20:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 32.4 |
| d8e6cf4f-5015-3309-8585-6dc9df57e641 | -11.82297 | -51.26475 | 2025-06-26 01:20:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 26.7 |
| ab99a79a-78a4-332e-80e3-e831b502bd79 | -13.03513 | -48.83607 | 2025-06-26 01:20:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 88dbd7e7-f0e3-3483-b095-75d09803d275 | -11.56539 | -52.10482 | 2025-06-26 01:20:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| da4a3123-defc-3c86-86aa-29381b7342db | -10.8168 | -53.73841 | 2025-06-26 01:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| dd110e1d-67cb-3298-9f7e-c237b0591dd5 | -13.05077 | -48.83337 | 2025-06-26 01:20:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 3451cbfb-b2f9-3c92-ac58-51321b2c46c7 | -11.07155 | -55.37365 | 2025-06-26 01:20:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 138e15cb-59cb-3e62-ab5f-eeb90d6283b1 | -12.53112 | -57.18922 | 2025-06-26 01:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a5f603d9-4686-3d85-aa3c-25fd38684cec | -12.01946 | -57.08943 | 2025-06-26 01:20:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 884e9079-28bb-3ada-9215-d725bb22e376 | -11.60876 | -55.53636 | 2025-06-26 01:20:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 30c2d9a0-56d0-3086-b54c-3645abca9520 | -11.06338 | -55.38656 | 2025-06-26 01:20:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 8524939a-f607-39ec-8300-24915a766f4d | -13.04091 | -48.84031 | 2025-06-26 01:20:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 91ea375f-50a5-3cce-b3d6-b4cded015c79 | -13.29117 | -57.08508 | 2025-06-26 01:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 348f776d-d391-382c-9f6e-426e84b0fd3f | -10.828 | -53.72989 | 2025-06-26 01:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c530257b-d2f2-311d-9be3-57c5232a8728 | -11.13184 | -53.91862 | 2025-06-26 01:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 74d4d6be-829d-3721-8c5c-76722cee30f5 | -11.06171 | -55.37524 | 2025-06-26 01:20:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |


[Clique aqui para ver as próximas entradas](README3.md)
