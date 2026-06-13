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
| 38e19f68-19e9-32a8-ace7-d22be8b0b7ac | -9.3048 | -48.9552 | 2026-06-13 00:42:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| addf09e8-52a9-3f3d-8d5c-d8ac95039c60 | -11.2442 | -46.6954 | 2026-06-13 00:42:00 | METOP-B | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b2377996-3811-3162-aaba-7494f96cd746 | -11.0514 | -56.922901 | 2026-06-13 00:42:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 41640932-9991-39f8-ae41-e88e702f26e3 | -11.6278 | -48.508701 | 2026-06-13 00:42:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ab5e765-f6e4-39e9-a98a-4e1423e5a0f9 | -10.0479 | -48.057201 | 2026-06-13 00:42:00 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96d91708-c217-3fc6-931a-abf40a9ac2ff | -10.0428 | -48.077702 | 2026-06-13 00:42:00 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca668380-8520-3ac9-89f2-8fac2f3ff492 | -11.1534 | -46.742599 | 2026-06-13 00:42:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7ab3f5d7-ad0b-33dd-b18c-d91e93b3f877 | -11.1589 | -46.763802 | 2026-06-13 00:42:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce32e839-ff7b-34ca-9c2a-7cd1a2471f89 | -12.4181 | -58.473801 | 2026-06-13 00:42:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 36d1e47f-11e1-3f58-b9cf-3c817f669f3f | -11.2305 | -46.721802 | 2026-06-13 00:42:00 | METOP-B | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 489d0c18-1f5c-3ce8-8a34-ec25f68b98f9 | -12.9016 | -54.2024 | 2026-06-13 00:42:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7fd7134-feee-3dd4-a39b-9aba11449d96 | -7.3451 | -49.696098 | 2026-06-13 00:42:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 344cf9d2-b74e-3a50-b284-518a16c1074a | -11.5089 | -56.110401 | 2026-06-13 00:42:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9070f2b4-f297-3ba4-b12f-1087ea20a011 | -10.8388 | -53.723202 | 2026-06-13 00:42:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f5cdf8af-1f93-3f25-bd9e-f96a47182300 | -16.17434 | -58.49027 | 2026-06-13 00:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| b65b8b16-4a9e-3cc6-8076-081f8bc55252 | -13.52847 | -54.30503 | 2026-06-13 00:45:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 941e1bf0-6aa5-30a3-a6ae-b5a9572f0ea3 | -11.16821 | -46.80172 | 2026-06-13 00:45:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 220.9 |
| ff501292-a132-38e7-af76-65d2809aa2bd | -12.42952 | -58.47432 | 2026-06-13 00:45:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e11e5432-c887-37c9-8463-9276fe934500 | -10.06777 | -48.10899 | 2026-06-13 00:45:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| d4732049-d705-314e-b0a9-f125c04f24e0 | -12.3045 | -57.41224 | 2026-06-13 00:45:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5170773b-a6f4-36ee-8046-c72b42609207 | -10.5381 | -53.71537 | 2026-06-13 00:45:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fc32cb29-66e5-3e21-a474-6b4c8869745d | -10.05515 | -48.08145 | 2026-06-13 00:45:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 5751a2ae-f985-34ce-9ede-2844c41516b2 | -12.27678 | -57.40711 | 2026-06-13 00:45:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 31.9 |
| a3b5645a-b797-3f82-b52b-e4585b30a609 | -11.57041 | -54.58189 | 2026-06-13 00:45:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| bc61890d-6525-3a7f-893b-6721bbe9e32c | -11.63152 | -48.53793 | 2026-06-13 00:45:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 245.2 |
| 0c9c42f6-bfa8-3be3-b0e4-9b0c619e06f6 | -10.82959 | -53.74133 | 2026-06-13 00:45:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b68caeee-e4d3-3b1c-a138-c31336aebeb2 | -11.62029 | -55.18766 | 2026-06-13 00:45:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e6619a0a-d4d6-3c95-abb4-767b09bde8bd | -10.71248 | -56.24297 | 2026-06-13 00:45:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cc5902f9-8692-3685-9c44-424d90d9be7f | -11.90521 | -57.79435 | 2026-06-13 00:45:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f8a2d7bb-f3c0-3281-93d8-762eee8acd10 | -11.16089 | -46.75953 | 2026-06-13 00:45:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 191.8 |
| d88d0f6a-de14-3b81-b90d-0eba6a216853 | -10.57139 | -48.03164 | 2026-06-13 00:45:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 524403b1-265d-327d-99dd-f895d4f4f111 | -10.57786 | -57.32267 | 2026-06-13 00:45:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e9c257e0-ca0c-3902-b88b-a558dffacff4 | -11.16064 | -46.75275 | 2026-06-13 00:45:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 6ac97894-dac4-373b-bfd9-f8ba7c8bda50 | -10.06127 | -48.07219 | 2026-06-13 00:45:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| e7a82aeb-8ecf-3d72-a1ce-9c41805ec726 | -11.51606 | -56.12535 | 2026-06-13 00:45:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b3667740-70fe-3585-9b27-c07a1d0eb851 | -12.27555 | -57.39812 | 2026-06-13 00:45:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 41de4c84-9d8c-3e7f-9664-c7caca0eefec | -11.23066 | -46.73423 | 2026-06-13 00:45:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 162.6 |
| a1c07e06-a344-3ba3-b3f8-4c737a4fd7bd | -13.51888 | -54.30654 | 2026-06-13 00:45:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| dec688e2-a368-3284-b0dc-d952caf5274c | -12.54569 | -57.15733 | 2026-06-13 00:45:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 93b6ba04-693b-3d8c-8b7f-bd1651c5a60b | -10.06126 | -48.11734 | 2026-06-13 00:45:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 20e021ca-b7c0-3df4-9de1-07e59275e32b | -11.6332 | -48.56218 | 2026-06-13 00:45:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 8e98a5a0-32b3-3ce1-9d6d-a27fd25dbc04 | -11.88818 | -55.12807 | 2026-06-13 00:45:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e89bc6b6-e2fd-3f97-a94c-4b018373f937 | -11.0406 | -56.93449 | 2026-06-13 00:45:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e014e3ed-7ee6-314b-8808-d842d05213e1 | -10.57855 | -48.02502 | 2026-06-13 00:45:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 35b9065a-a87d-300e-b4cd-608e6c3cd338 | -11.18562 | -46.79111 | 2026-06-13 00:45:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| e58b4012-e30b-332c-bc31-64798472e0f3 | -12.18926 | -56.45339 | 2026-06-13 00:45:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| db8f3c10-7c88-3966-800c-9561abd8ace8 | -11.71167 | -54.49139 | 2026-06-13 00:45:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 81a67d62-03b7-3797-8e29-4dc72123b9c1 | -12.26425 | -57.39692 | 2026-06-13 00:45:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bf265958-12f0-3f5b-9e92-280b6fadbf9b | -12.30327 | -57.40326 | 2026-06-13 00:45:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 68f96adf-e5c3-30f3-b445-cd505be9a975 | -10.71379 | -56.25227 | 2026-06-13 00:45:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2b6cb449-3f20-36c6-8857-15612ca7c562 | -12.42174 | -58.48494 | 2026-06-13 00:45:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| c4ddf296-37df-312f-84dd-5cb641d3c10b | -10.82764 | -53.72867 | 2026-06-13 00:45:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5ea48520-c48e-3caa-93c6-133921fb0e22 | -11.64314 | -48.52906 | 2026-06-13 00:45:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| f6d132d7-267c-33d4-8dc7-8a82926da071 | -12.1545 | -48.4675 | 2026-06-13 00:45:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| faca852c-00dd-3352-b09d-44d444dbece7 | -12.90047 | -54.22408 | 2026-06-13 00:45:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 25.0 |
| dd2118fe-dd0a-3f44-91f2-ee2ce0474294 | -11.26543 | -53.97453 | 2026-06-13 00:45:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7809ea04-f647-38d0-967f-4e1629de4e5e | -12.42051 | -58.47561 | 2026-06-13 00:45:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 330e2100-a610-31bf-bc3c-b2c770ab6764 | -11.16822 | -46.79481 | 2026-06-13 00:45:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 263.4 |
| 7c955195-c87a-3d62-b48c-1a71c9fff2f1 | -11.04945 | -56.93319 | 2026-06-13 00:45:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0e1b8077-2095-3a71-81d7-598007271478 | -10.83993 | -53.73962 | 2026-06-13 00:45:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 51e30e7a-cae7-392a-9ec5-993cda558b96 | -10.53242 | -53.72209 | 2026-06-13 00:45:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 18a87aa7-1219-33eb-b9da-779c6e5da762 | -11.62784 | -48.53181 | 2026-06-13 00:45:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 132.9 |
| b7c656b5-cec6-3501-a85d-8ca20a6564d7 | -11.64847 | -48.55946 | 2026-06-13 00:45:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| bf86dfdb-5a6b-3c1b-a840-2e9c74c35ccf | -11.63663 | -48.56821 | 2026-06-13 00:45:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 82750adf-5b3d-3162-ac2d-d336ea7b2d65 | -11.17818 | -46.74952 | 2026-06-13 00:45:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 9ca5f56c-2831-380d-9d21-c2826ec3caff | -12.26548 | -57.4059 | 2026-06-13 00:45:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 7a667abf-1574-3d56-87c1-7b4034352e5b | -10.84186 | -53.75223 | 2026-06-13 00:45:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7882ce3c-c457-3cd6-82bd-8b4c18ce1764 | -11.88967 | -55.13824 | 2026-06-13 00:45:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 40.9 |
| f4d334d0-5138-3dde-9e8e-25c921d123ba | -12.41075 | -58.47367 | 2026-06-13 00:45:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 73144569-c438-3707-81f8-9d576e7e7010 | -11.23065 | -46.73901 | 2026-06-13 00:45:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 952e77e3-fed8-3a05-a438-ccea0e74999a | -12.412 | -58.48299 | 2026-06-13 00:45:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| f8742486-9ec6-31f4-8378-49f0c90bf110 | -12.14934 | -48.43739 | 2026-06-13 00:45:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 08a22e85-aedd-3eb8-9c77-17d5da01723e | -11.54688 | -52.80117 | 2026-06-13 00:45:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c44f1746-5ac9-33d2-8fde-9326c5b5fae2 | -12.89883 | -54.21299 | 2026-06-13 00:45:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bdf677bf-b400-33f2-8bb5-94af86b30d68 | -7.34912 | -49.72708 | 2026-06-13 00:48:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 00d9e893-7cf3-33b1-9ac1-1fbc82092fae | -10.02501 | -59.34725 | 2026-06-13 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1f438660-67ad-36aa-84eb-a68ae24fe447 | -7.34703 | -49.70269 | 2026-06-13 00:48:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 5290a138-8466-3ea8-8c28-fa87d7465cef | -11.1638 | -46.7674 | 2026-06-13 00:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 012685ac-a35d-3de8-80bc-2ba92210eaa3 | -11.1634 | -46.7899 | 2026-06-13 00:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 7a2823bd-c3f4-338d-ba88-484cadb71c56 | -11.6309 | -48.5277 | 2026-06-13 00:50:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| fd13a07a-d113-3a29-8a34-d3e7588a703f | -11.6306 | -48.5497 | 2026-06-13 00:50:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 188.3 |
| e2bb7eec-0116-385b-af6d-295ce7734f81 | -10.0626 | -48.0758 | 2026-06-13 00:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 94473d44-878b-3787-a051-31de3cbbce5a | -11.6497 | -48.5473 | 2026-06-13 00:50:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 87e5d947-ddc2-3374-8315-4013df1c8a19 | -10.0623 | -48.0978 | 2026-06-13 00:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 4a3212a6-336c-3ef3-8465-21d4002ae50e | -11.1828 | -46.7649 | 2026-06-13 00:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 509bc2e3-f483-3a64-8e3c-82fac5592679 | -11.1638 | -46.7674 | 2026-06-13 01:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| e9e6b476-7286-36d1-add1-495a3f63a5d2 | -11.1828 | -46.7649 | 2026-06-13 01:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| e50fa6f7-cf9a-3530-a53a-1ac6feb9d6ff | -10.0623 | -48.0978 | 2026-06-13 01:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 7de67e4e-e744-3f90-9c09-139e6914941b | -10.0626 | -48.0758 | 2026-06-13 01:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| b1415816-b20f-301f-9e47-cff508e58342 | -11.6497 | -48.5473 | 2026-06-13 01:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 2ad98d6b-af1a-3ec8-9048-88c44f11b58e | -11.1634 | -46.7899 | 2026-06-13 01:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| a0906a3b-8e3b-3273-a03b-836acd771eea | -12.269 | -57.4039 | 2026-06-13 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| f72aa56f-ede8-3efb-80d0-47035749c9b0 | -11.6309 | -48.5277 | 2026-06-13 01:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| c1ffc765-d60e-31bd-bcf4-67c4dacfdfe2 | -11.6306 | -48.5497 | 2026-06-13 01:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 153.7 |
| f9b9522e-edc8-37cc-8536-8db230c6744f | -10.0626 | -48.0758 | 2026-06-13 01:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| fa0d931c-0d7d-37fb-bb01-b0f0fc078936 | -11.6306 | -48.5497 | 2026-06-13 01:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 165.0 |
| d9a74cb6-c6f0-3f1a-ae1f-8569bd342817 | -10.0623 | -48.0978 | 2026-06-13 01:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 2bc40d06-0308-363c-93cd-ff4ce3c65203 | -12.269 | -57.4039 | 2026-06-13 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 5590233e-cb34-370a-b728-b2100ffac634 | -11.6497 | -48.5473 | 2026-06-13 01:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| ad9883e1-fbd6-3939-851c-9a93836062ce | -11.6309 | -48.5277 | 2026-06-13 01:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |


[Clique aqui para ver as próximas entradas](README3.md)
