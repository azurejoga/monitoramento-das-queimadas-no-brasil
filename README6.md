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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bfede54-abe3-33c8-be81-d905119ac2c1 | -3.49371 | -48.03877 | 2026-05-28 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c8a661ba-e511-3fe3-9c36-cc1bb33d91dc | -4.66224 | -42.42953 | 2026-05-28 04:38:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f1e6cbef-c38a-304b-8f04-2e36c9d6f397 | -3.49425 | -48.03532 | 2026-05-28 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0327c820-e7be-36af-ac29-b5e8ca1fb655 | -5.30471 | -43.05558 | 2026-05-28 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85507220-1a1e-33ea-954f-7e7706cd8b05 | -4.65779 | -42.42884 | 2026-05-28 04:38:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 72839823-6823-31c6-bc23-95f50ce5cb07 | -5.30901 | -43.05621 | 2026-05-28 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a8df57c-4a68-3dbb-a3d6-e5fc1ff0f66d | -5.33565 | -42.6849 | 2026-05-28 04:38:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0e331ce8-9984-3133-b8b7-b84a8cf784c0 | -13.2189 | -54.4975 | 2026-05-28 04:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 3737cec7-9f64-384f-b0fc-3b961a39185a | -11.591 | -47.4496 | 2026-05-28 04:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| b5668d0a-a98f-348c-b85f-9293aa8b2e6c | -10.44547 | -59.42902 | 2026-05-28 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddaf69b0-f959-354b-8fcb-bfd13d9d9e61 | -10.79827 | -46.87513 | 2026-05-28 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8ac306d-0648-3e38-badd-851ee84c59d5 | -5.80167 | -45.13166 | 2026-05-28 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b0843065-beae-39cb-8f77-937edaeeb68f | -5.91645 | -45.53389 | 2026-05-28 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b692c9a-5907-3a71-a120-267e9c081065 | -10.63825 | -46.89481 | 2026-05-28 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e993c3f2-de9a-3886-9384-190b2b2ba335 | -7.6271 | -47.31045 | 2026-05-28 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 246a5854-75fd-36c2-aae6-45ea99925394 | -11.30175 | -54.02745 | 2026-05-28 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9275b238-754c-33d6-82b6-3554e712417f | -5.95955 | -43.48864 | 2026-05-28 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 35986756-7e5e-307f-81cf-fde99acf172a | -9.39707 | -47.36557 | 2026-05-28 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84f1b4d7-306c-3456-a4b8-0f637f8bfa26 | -9.34015 | -45.4711 | 2026-05-28 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5190c589-c208-3495-a707-90d0425931d9 | -9.35255 | -45.46782 | 2026-05-28 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 73e5ba71-9b8b-3938-8d3d-442ea66ea87a | -11.96982 | -47.38132 | 2026-05-28 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b9516efe-5988-3123-a8cd-247fa2466fc7 | -7.40727 | -45.50843 | 2026-05-28 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9143726-c1e6-33b9-bf55-567f582067c3 | -11.584 | -47.44382 | 2026-05-28 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 826529b4-788b-3125-98cb-af113f58d4a3 | -10.56461 | -48.03015 | 2026-05-28 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6d39649f-18d4-329c-8a84-9af092e7c2eb | -5.92211 | -43.47929 | 2026-05-28 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02459bb2-bb97-3a5a-831e-9490b0be91e7 | -8.6824 | -48.30531 | 2026-05-28 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| baa1c148-47c0-3ca5-be60-9fda70fb928e | -6.99538 | -42.87542 | 2026-05-28 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 72b9f306-b183-372b-be0c-f263ae7cbea5 | -11.47102 | -52.91549 | 2026-05-28 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4590982a-2bd7-3139-bb45-a6c081ffbf73 | -9.3893 | -48.43502 | 2026-05-28 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 975f6c87-8d26-3f11-871c-904d66fcb0ab | -11.27829 | -53.96667 | 2026-05-28 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0cd1ead-5498-3b0e-9667-4eee520b59d6 | -11.59772 | -47.45015 | 2026-05-28 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 50886379-22f6-3f46-9682-96a5647822d2 | -5.80304 | -45.12253 | 2026-05-28 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 232b82da-4fe9-3ac4-8729-ab3076938372 | -11.46078 | -52.92259 | 2026-05-28 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9d3c0c38-f321-3aad-9e58-57bb7ba9fb4b | -11.47384 | -52.91996 | 2026-05-28 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a4eccf29-5334-304a-9319-dd2547a195d9 | -11.47732 | -52.92054 | 2026-05-28 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 3a8caf5f-73ce-3537-8db0-31fb246a243a | -9.73582 | -49.21808 | 2026-05-28 04:40:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74018c44-be5b-329f-9039-7f2093b89c53 | -10.70851 | -56.05003 | 2026-05-28 04:40:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 217066ec-23a6-3a46-9aa2-cd927f8c450d | -11.46488 | -52.91927 | 2026-05-28 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fad69db0-044d-39a1-8955-12fe2fd0d7f6 | -6.53851 | -44.68826 | 2026-05-28 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 452fdfd9-c71a-35c9-9e1b-0b7215fd3a9c | -10.13674 | -52.39869 | 2026-05-28 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0a1ff458-529e-39a6-a1f6-491e960a6302 | -11.97404 | -47.37764 | 2026-05-28 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 07c683bf-bc76-3a77-8c26-21c61f22718a | -9.39833 | -48.44389 | 2026-05-28 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f900939-b12d-3a5b-8118-feca3de79287 | -7.01312 | -45.00596 | 2026-05-28 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45deea93-1ba4-3bb3-92e6-c26daa38b209 | -6.54255 | -44.68636 | 2026-05-28 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f0d47548-1baa-3ce2-a0ca-2deaed30c4c6 | -12.69979 | -44.79093 | 2026-05-28 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 872357f5-73f5-33d0-b7e5-aaed349b85be | -10.56806 | -48.03072 | 2026-05-28 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f51a128f-60bd-3f94-a6a0-8ce716821b83 | -9.36185 | -45.46551 | 2026-05-28 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ceee83fa-a481-3da6-abfd-db85a2dbd37f | -11.59595 | -47.43707 | 2026-05-28 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ac7aa9b7-8edf-361c-be88-bc04f413931f | -9.44601 | -48.8902 | 2026-05-28 04:40:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7619413-ac4a-3385-958f-fed28a5f5fa0 | -7.4608 | -49.7426 | 2026-05-28 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9dadc2f9-b7db-362b-b7f8-c8d421de40ac | -9.39971 | -47.36716 | 2026-05-28 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fc9ebf0-6f23-3f66-9645-597d8eb471fb | -12.45898 | -46.53133 | 2026-05-28 04:40:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca64e15f-9c91-36d9-a33c-4b52f4ee6716 | -9.34557 | -45.46824 | 2026-05-28 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2b2ff427-2621-31bc-abfd-49351d5c6f7d | -11.99116 | -47.15675 | 2026-05-28 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee42d9a8-5f6f-3067-b530-6caf41d3b84d | -9.60468 | -58.34335 | 2026-05-28 04:40:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51e7fb31-fe88-39e0-a321-417e609fad6f | -8.84629 | -49.86786 | 2026-05-28 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfd98a54-8a36-3448-80e6-6d357baa55ab | -5.1055 | -46.94443 | 2026-05-28 04:40:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddc89bdd-2a78-35ec-9712-244e7608c4ef | -9.28463 | -48.58968 | 2026-05-28 04:40:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03e1c36f-2fa2-321b-b6b7-3d0b7e09aaf8 | -9.74023 | -49.21154 | 2026-05-28 04:40:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d921d6f6-0e73-3fd1-b64d-64ba3949a650 | -9.28502 | -57.84793 | 2026-05-28 04:40:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 244e72bc-d78d-3519-a24c-aa9323e3d647 | -8.91335 | -51.85641 | 2026-05-28 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e85f9ca0-9dcb-35d5-a16c-e6e63d744c9e | -11.30024 | -54.03629 | 2026-05-28 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5607262f-41ff-3fac-b680-11946dd5cc1b | -5.95897 | -43.49254 | 2026-05-28 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 295eab72-deef-30b1-a019-eba1644b57c0 | -11.5846 | -47.43963 | 2026-05-28 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 52174096-5078-335b-b4a0-b378312cc9b1 | -6.99856 | -42.885 | 2026-05-28 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fc853b54-6bba-325b-8392-87c0a1c4a52f | -7.93054 | -47.97137 | 2026-05-28 04:40:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2e3224cf-edb0-3020-a127-fd77158ebc19 | -9.73968 | -49.21508 | 2026-05-28 04:40:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1ed6b4f-967f-3d74-bcf4-ef5bf7cd0f50 | -9.34793 | -45.47224 | 2026-05-28 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| beb10b13-132d-300e-bca1-27dc694b7730 | -11.61524 | -47.90444 | 2026-05-28 04:40:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c3e1817c-a3a3-32e9-9e79-60a0e306eba5 | -9.34099 | -45.47265 | 2026-05-28 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f00c11da-b2af-3619-be31-20462e5342ee | -11.59056 | -47.4491 | 2026-05-28 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 21f4fb3b-4393-3a36-b1a3-e5da86367ed8 | -9.05319 | -46.3026 | 2026-05-28 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 477a7024-101c-387b-b148-bc3afb468c84 | -8.7241 | -48.33784 | 2026-05-28 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2ac4970-0239-3dec-b242-7de5c94e4ee2 | -11.29366 | -54.03061 | 2026-05-28 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fbf6dff1-ac62-31bc-a0a1-b1cb7746a3c1 | -10.48235 | -48.90977 | 2026-05-28 04:40:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0cc06749-ae2f-33eb-a7f6-e6a2afc1ff89 | -11.59534 | -47.44127 | 2026-05-28 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d179f966-2ad1-3c64-bc82-00697965877d | -10.65697 | -49.72697 | 2026-05-28 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a72d5a0-7a9e-3aee-a517-913d062ca2e1 | -5.92634 | -43.47988 | 2026-05-28 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 096d10ec-3929-3393-af23-f5ecbaa61dd8 | -6.54648 | -44.68693 | 2026-05-28 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a4275e0c-2e0a-3272-879c-00b7f495e8f3 | -8.71696 | -47.80005 | 2026-05-28 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb832e74-56c4-3e86-a50e-068633f0ffc8 | -10.65974 | -49.731 | 2026-05-28 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a3d99f45-0e5b-3d3f-9fc3-431aa28b66d0 | -8.70954 | -47.80276 | 2026-05-28 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1682ec2-c9cd-3130-9fe1-f6f85e99ee34 | -6.99921 | -42.88051 | 2026-05-28 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| db53dffb-5748-38f5-ade1-d2c444fd4a99 | -11.03699 | -56.92312 | 2026-05-28 04:40:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4483e3da-12bc-34af-9292-3ba26bf07269 | -12.32867 | -47.89577 | 2026-05-28 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 531dd5f1-1d32-3426-8084-23250cc6a435 | -5.95474 | -43.49199 | 2026-05-28 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d061e15b-bbdd-3322-9c24-c77db23d1355 | -9.2919 | -48.58709 | 2026-05-28 04:40:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e5bbe794-178a-399e-a394-09d354fac768 | -9.14567 | -51.28958 | 2026-05-28 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 700c7651-52d3-3524-be4e-c980b96890e9 | -9.28799 | -48.5902 | 2026-05-28 04:40:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11298a77-20dc-3e19-b94b-c1e5f299ed28 | -11.47183 | -52.92044 | 2026-05-28 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| aa36baa2-0534-3d7a-aae4-514aa613ef39 | -11.44908 | -52.92866 | 2026-05-28 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 387f52b9-9d71-3829-a50a-8b4ce1ea16e9 | -9.39888 | -48.44024 | 2026-05-28 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 50e7e361-90fe-346c-b1b5-250cb8f5c5ea | -11.58758 | -47.44438 | 2026-05-28 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c967408b-82d0-3d43-8944-dbebad2c0cd8 | -9.34404 | -45.47167 | 2026-05-28 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b37d1ef9-7fd4-3a80-8931-a494e681b219 | -7.00995 | -45.00055 | 2026-05-28 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5ed77731-3ab4-3924-a8cd-058c228c994d | -9.74355 | -49.21206 | 2026-05-28 04:40:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43665914-7579-3491-b4cc-ae8891c977c1 | -10.65643 | -49.73047 | 2026-05-28 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c54d40c-63b4-33f0-84b8-ebbedc8c8209 | -6.40461 | -48.01792 | 2026-05-28 04:40:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cd6f8c5a-1676-3b27-92bb-16a0e993879e | -11.21995 | -53.82312 | 2026-05-28 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7deb8b58-4087-33f1-92f5-7ef38123dffd | -5.79271 | -45.13974 | 2026-05-28 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README7.md)
