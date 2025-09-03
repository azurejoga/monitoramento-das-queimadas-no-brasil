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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 635b6aad-13b9-3be2-b265-8b296712d071 | -11.1224 | -44.6521 | 2025-09-03 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 280.9 |
| 05809a25-e039-335d-8352-1b5b8e3ef236 | -8.8842 | -45.822 | 2025-09-03 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 432721e8-e821-37fd-8967-77906ae7f4b2 | -12.9189 | -57.0074 | 2025-09-03 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 4e1d07f7-70eb-3723-ad59-5fb1ccdc469e | -12.9387 | -56.9454 | 2025-09-03 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 6aa04884-4cbc-33c7-8aff-05cef4d1339c | -12.9385 | -56.9655 | 2025-09-03 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 41df8a29-e497-3e72-8ff5-87af86c69fde | -12.6341 | -56.9926 | 2025-09-03 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 34.1 |
| b24b834c-6b1a-327f-9bfb-f91e70ea2eb6 | -3.2306 | -47.1131 | 2025-09-03 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 572ad33d-f8bd-324f-8d97-e0aba95503e3 | -12.9573 | -56.9839 | 2025-09-03 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 0e179686-e379-39eb-a6b4-a0e010ff81d6 | -15.0254 | -50.071 | 2025-09-03 02:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 8f93c375-8353-3f8e-ab3a-6c9f9029294b | -4.8935 | -43.2115 | 2025-09-03 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| a7d9fad2-b553-3289-9c18-d510b9cc08b1 | -11.1224 | -44.6521 | 2025-09-03 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 53a9594d-b9f7-3b5d-8460-fe26562273d5 | -9.3394 | -55.2277 | 2025-09-03 02:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| cd195b35-94ff-3211-b75a-b9c364a958b7 | -12.9189 | -57.0074 | 2025-09-03 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| b18e9a80-a642-3e60-9e30-133098b9fd95 | -12.9385 | -56.9655 | 2025-09-03 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 67ddb0e5-517e-3156-8020-068b8e0cddc0 | -3.212 | -47.1357 | 2025-09-03 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 9a70c70c-a5c9-32db-b675-1ccdf3dc2fc8 | -3.2305 | -47.135 | 2025-09-03 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 151.6 |
| 71ac8871-1397-3491-ba89-07eacad8d9f4 | -10.45 | -54.7785 | 2025-09-03 02:50:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 29317fff-9629-32de-929f-e648a2167ff5 | -3.2121 | -47.1138 | 2025-09-03 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| cabbd84b-466a-349c-986d-d82d7ae2640c | -11.1228 | -44.6288 | 2025-09-03 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| db329bbe-bcbd-3fe0-926c-6ad1b6ad9daa | -12.9573 | -56.9839 | 2025-09-03 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 64043582-7948-35b9-9965-b79ceb761e21 | -4.8935 | -43.2115 | 2025-09-03 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 6e2d48f2-f13f-3f44-801c-4d91adc687da | -10.5409 | -50.4256 | 2025-09-03 02:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 8db492e5-9a60-3280-8e6c-a3a3c2394764 | -12.9382 | -56.9856 | 2025-09-03 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 177cb9bf-aafb-38d4-9a56-08d1b8943e94 | -8.8842 | -45.822 | 2025-09-03 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.7 |
| c0c7b036-ee59-34f9-82a1-f187cf7fa3bf | -22.1784 | -48.8134 | 2025-09-03 02:50:00 | GOES-19 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.4 |
| 7f744414-1dff-3abd-8ddc-dfbfee097acf | -15.0254 | -50.071 | 2025-09-03 02:50:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 47eef2f9-a68f-356c-8e9a-666ac77e55b8 | -22.1777 | -48.8368 | 2025-09-03 02:50:00 | GOES-19 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.0 |
| 12511172-b242-32d1-a5e8-6e040b897e99 | -3.2306 | -47.1131 | 2025-09-03 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 4021cbe7-5814-35f3-b8d9-8896f8fd1669 | -7.6851 | -48.7386 | 2025-09-03 03:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 7dd6822f-248a-3035-a285-d932b86dd325 | -7.7039 | -48.7371 | 2025-09-03 03:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 5f502c59-7a01-3f87-a50e-8bd4482d957a | -12.9382 | -56.9856 | 2025-09-03 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| a9477ba4-c5d2-3ca5-8ca3-a76a4214c3b1 | -12.9385 | -56.9655 | 2025-09-03 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 7e496298-55ce-35d1-93d3-952ffadb0202 | -3.2305 | -47.135 | 2025-09-03 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 8a74f178-ed1b-320f-a415-cbc4d6e7b254 | -7.7041 | -48.7155 | 2025-09-03 03:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 0301a331-bb0b-3009-8a17-972c5b9eaccd | -7.7226 | -48.7355 | 2025-09-03 03:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 49.6 |
| c2270f5f-6393-3d04-affd-cf21928eff0b | -3.2121 | -47.1138 | 2025-09-03 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 7b027e6f-e9c2-3b51-aac7-ff37aae38bff | -14.5801 | -48.0398 | 2025-09-03 03:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 59.0 |
| dbee777b-5f91-3a89-940a-65993ca12ba4 | -9.3394 | -55.2277 | 2025-09-03 03:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 2b7847e6-6ba7-35d4-8974-a75a95ad0c3b | -8.8842 | -45.822 | 2025-09-03 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 069b52db-bb15-33d2-9f8e-193e143468d0 | -3.2306 | -47.1131 | 2025-09-03 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 84e15eb2-b00a-3c56-8b2a-d355c8a4c02f | -4.8935 | -43.2115 | 2025-09-03 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 31a3f7b5-1103-3b19-8951-444678ad3200 | -10.5409 | -50.4256 | 2025-09-03 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 555c914a-94e9-3f68-9659-a82e3cc486b8 | -11.1224 | -44.6521 | 2025-09-03 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 5ac1833c-ccc2-33a5-bbff-2031a3aeb262 | -12.9573 | -56.9839 | 2025-09-03 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| f6af5f59-f862-3258-a821-2098513512f6 | -3.212 | -47.1357 | 2025-09-03 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| b1792d55-8e71-3826-9074-25d0e1838f6e | -7.7036 | -48.7587 | 2025-09-03 03:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 5d96b462-8200-342c-8743-0a3dcbc670a8 | -5.53513 | -36.8526 | 2025-09-03 03:04:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 28a56254-e78e-3559-bdf9-1feaabdddc33 | -5.53674 | -36.84844 | 2025-09-03 03:04:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2768cedc-8194-3b4c-b8ab-7d59118acf0f | -5.53589 | -36.85307 | 2025-09-03 03:04:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 10.7 |
| e7a70333-bdb8-3271-8b8f-0c154b0462c9 | -5.53431 | -36.85724 | 2025-09-03 03:04:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 9.6 |
| aa0d87b5-8f23-3d3b-abaf-c82e9ecd3c8b | -5.53594 | -36.84797 | 2025-09-03 03:04:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 8.9 |
| a9fe3497-6748-3d41-8c37-1541af648a8d | -5.52904 | -36.85157 | 2025-09-03 03:04:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 1ef7fdcb-2f1f-3502-94ad-4e85a53e6010 | -5.52986 | -36.84693 | 2025-09-03 03:04:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 8.9 |
| ebee91f8-46ed-31e5-ac68-eba187f49aa4 | -9.61493 | -40.62267 | 2025-09-03 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e13cb594-4cd6-389d-8edc-029f2d74a2fb | -9.61637 | -40.61555 | 2025-09-03 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| dda03d80-ee23-38aa-9103-28c70ab7e9d5 | -19.74513 | -43.29686 | 2025-09-03 03:08:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f108d642-ca60-36e2-844b-174b191fbdd8 | -19.74597 | -43.29634 | 2025-09-03 03:08:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 5d1d3849-b077-3c2e-847b-a7c64b8dbb11 | -12.9382 | -56.9856 | 2025-09-03 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 98d851d8-d7ed-3dfb-b580-c05f87c06eb2 | -3.2306 | -47.1131 | 2025-09-03 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| d64b6b39-2615-385a-aaac-ae9724af9069 | -10.4497 | -54.7988 | 2025-09-03 03:10:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 3a43a6a1-736f-334a-a9f6-9018096bb717 | -4.8935 | -43.2115 | 2025-09-03 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 987d53f1-feb9-3d69-89a8-0852d904e39b | -3.212 | -47.1357 | 2025-09-03 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 24928894-c78a-3826-a358-08f1de51eb22 | -7.7036 | -48.7587 | 2025-09-03 03:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 97684737-88f4-3a1f-8ff4-13c054ec76c2 | -6.4648 | -45.4154 | 2025-09-03 03:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 8fe1ee30-598e-3063-8b33-24c924cc1783 | -7.7039 | -48.7371 | 2025-09-03 03:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 114.7 |
| ba3895c3-02bb-3158-955d-311054b8dadb | -10.45 | -54.7785 | 2025-09-03 03:10:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 8b8604be-e55c-3b14-9a12-f84833bc44fc | -10.5409 | -50.4256 | 2025-09-03 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 45.0 |
| a49ea7e9-0fcb-3045-bbde-2faea59438d8 | -12.9573 | -56.9839 | 2025-09-03 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 9a0607d3-f4c7-3084-b2be-2a9a95127bc5 | -12.9385 | -56.9655 | 2025-09-03 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 27cc34eb-f6ce-38f5-84b3-4f50659f3979 | -3.2121 | -47.1138 | 2025-09-03 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 347ee2d0-70b7-399b-9e56-c944fec1f2ab | -3.2305 | -47.135 | 2025-09-03 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 131.1 |
| 75cb6530-5723-3e0c-892a-9f3ae2fd3671 | -22.4908 | -43.72554 | 2025-09-03 03:10:00 | NOAA-21 | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e574665e-09b2-3f75-83ce-a2de18de7896 | -22.49309 | -43.72688 | 2025-09-03 03:10:00 | NOAA-21 | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1b1567bf-d78a-34ae-8a1a-6daabda2efb6 | -22.48631 | -43.72559 | 2025-09-03 03:10:00 | NOAA-21 | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 13b18b08-4088-3dad-87f7-189e1f154264 | -22.48903 | -43.73274 | 2025-09-03 03:10:00 | NOAA-21 | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 2a776656-13fd-319f-a15b-00788497eab5 | -10.4497 | -54.7988 | 2025-09-03 03:20:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 9af9bf22-c76b-30af-bffe-9b04b58d7575 | -3.2306 | -47.1131 | 2025-09-03 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| e71e2fd0-f89b-3c70-9668-64994c0f60d2 | -3.212 | -47.1357 | 2025-09-03 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 35a3dc0b-7c06-310e-8d44-47e7e1f69491 | -4.8935 | -43.2115 | 2025-09-03 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 4d07da8d-b905-3f55-b057-cac555fc916b | -4.1604 | -46.7881 | 2025-09-03 03:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 1767f9a1-b5ed-38ef-ae75-988fbe16c426 | -10.45 | -54.7785 | 2025-09-03 03:20:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 4386ed5b-fadc-353b-93f8-3fb2731c6044 | -12.9382 | -56.9856 | 2025-09-03 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| ed22f447-d4d6-3d0a-9710-433df6e64f20 | -3.2305 | -47.135 | 2025-09-03 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 151.4 |
| 11d87180-28d9-370e-a646-02f62386b149 | -12.9385 | -56.9655 | 2025-09-03 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| b5e83527-c462-37f6-8102-af1f503a8ed6 | -10.5409 | -50.4256 | 2025-09-03 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| ec981e29-7a2c-30d7-895b-7bb3951be2ab | -12.9573 | -56.9839 | 2025-09-03 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| eff533fd-50a3-31a7-9bda-952396b9f6a7 | -3.2305 | -47.135 | 2025-09-03 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 157.8 |
| 46f6430a-19f6-35cc-846e-522b937195f1 | -10.45 | -54.7785 | 2025-09-03 03:30:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 7aea4f1f-ed1d-388b-bd48-ca08e142b71d | -3.212 | -47.1357 | 2025-09-03 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 9b62a711-c482-3154-83ac-7c3d4d613625 | -12.9382 | -56.9856 | 2025-09-03 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 61e7f8aa-0fdd-3bae-95e0-0e361ba91b97 | -3.2306 | -47.1131 | 2025-09-03 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 749e4301-eaf6-3a1a-ae29-964575b047d2 | -22.1784 | -48.8134 | 2025-09-03 03:30:00 | GOES-19 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.5 |
| d2b83763-c3f6-37a9-acf4-c36259788f97 | -12.9387 | -56.9454 | 2025-09-03 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 27c7e21c-2999-3e94-85c9-a99caf03f5b9 | -22.1777 | -48.8368 | 2025-09-03 03:30:00 | GOES-19 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.3 |
| c54b2749-643c-3cac-9053-34cad0eb6afd | -4.1604 | -46.7881 | 2025-09-03 03:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 9c257ab9-cdf4-32c5-89e7-7dcd015d0c9f | -12.9385 | -56.9655 | 2025-09-03 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| a6a83c16-b237-3535-995b-6c2764557c1e | -3.19773 | -40.74286 | 2025-09-03 03:30:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b2f628a1-1560-3970-a540-a12d3dd54218 | -2.78782 | -41.87481 | 2025-09-03 03:30:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 633cf1d8-10ed-3dc0-9e28-cb32c8d688ec | -3.19834 | -40.73923 | 2025-09-03 03:30:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0068d30f-f299-32b7-8af3-2502cff35543 | -2.78709 | -41.87915 | 2025-09-03 03:30:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README21.md)
