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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cdc9d4e-a1ca-3deb-ab99-0829f284c8d6 | -20.32205 | -57.87649 | 2026-01-22 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 81d9a1ee-479a-3719-9c8a-7553480bbd66 | -19.13491 | -54.54298 | 2026-01-22 04:36:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4795d454-3a98-382a-bbef-f27cc7e995c0 | -19.63231 | -56.97747 | 2026-01-22 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4f07672e-0d96-3881-8587-9b737d3dea30 | -23.29836 | -48.8562 | 2026-01-22 04:36:00 | NPP-375D | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 47f0668f-24e4-341f-a95a-b9b29c7019ca | -19.67372 | -56.98688 | 2026-01-22 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6fe93344-0a60-375a-b21b-adcdf6b75070 | -19.67832 | -56.98792 | 2026-01-22 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 213b69c0-2927-3287-bd7c-13de765accb8 | -19.35583 | -54.67847 | 2026-01-22 04:36:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4fcad5e2-a4f6-3475-858f-708541733cc9 | -18.18971 | -54.48085 | 2026-01-22 04:36:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0cb9c8b1-aec5-33fe-af65-75a34db88e07 | -19.56186 | -54.44006 | 2026-01-22 04:36:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8848d68-1adf-3953-b5ba-def445f67083 | -19.32725 | -54.02863 | 2026-01-22 04:36:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85ffacdc-b826-312b-a064-ad052494f712 | -19.67171 | -56.9969 | 2026-01-22 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d2f95b7a-1792-31ef-8e56-cba42fa84545 | -19.66521 | -56.88596 | 2026-01-22 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b3e48f71-f804-33fd-b16a-8727fc9b7145 | -23.14242 | -49.0625 | 2026-01-22 04:36:00 | NPP-375D | ARANDU | SÃO PAULO | Brasil | 3503109 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd72b32d-e302-38f4-a0e5-7ed8f9ca5947 | -20.31725 | -57.87535 | 2026-01-22 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e8b3062a-1e50-37cd-856b-748c8d824b2b | -22.01914 | -56.33698 | 2026-01-22 04:36:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04b2e49f-b040-3d7f-9fbe-e80763315c0a | -20.30899 | -57.87831 | 2026-01-22 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5b5abd27-4737-30b3-9c2d-f521fdf78b3f | -19.67991 | -56.88412 | 2026-01-22 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d02bbd3f-3cbb-3158-96ae-ab9530b1106c | -20.34241 | -57.87545 | 2026-01-22 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f4474507-14ee-31e5-9ecb-6bf1f384d192 | -23.60533 | -48.2603 | 2026-01-22 04:36:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ba84fc59-2c92-3f42-84c0-66acf92716e3 | -21.20072 | -56.93496 | 2026-01-22 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f93543f6-5d26-3b1b-ac20-a0051b5b04e3 | -20.31012 | -57.87273 | 2026-01-22 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d258c970-6c35-3902-b425-94669ffc13a9 | -20.84233 | -51.74049 | 2026-01-22 04:36:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a1d139fb-7292-35bb-8816-e7913d487031 | -19.32337 | -54.02792 | 2026-01-22 04:36:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c90ed87-a191-377c-8155-b624bbc7cf6d | -19.63333 | -56.97246 | 2026-01-22 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d7eb3c6d-bce0-370b-b622-c947ae5d6378 | -19.35513 | -54.68218 | 2026-01-22 04:36:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d988e10-c495-3427-aaf3-7f65355e65c9 | -27.44861 | -48.44697 | 2026-01-22 04:38:00 | NPP-375D | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dc119c33-3674-3052-9749-89124a635176 | -30.90223 | -52.96292 | 2026-01-22 04:38:00 | NPP-375D | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| dc9943fe-5617-393b-beb2-81cd5dca105c | -24.02399 | -51.10558 | 2026-01-22 04:38:00 | NPP-375D | FAXINAL | PARANÁ | Brasil | 4107603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| bc101b72-0ac6-3286-8966-7d511da6aef4 | -25.58215 | -54.57496 | 2026-01-22 04:38:00 | NPP-375D | FOZ DO IGUAÇU | PARANÁ | Brasil | 4108304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fc6ffd3c-e29f-3bc2-ba3e-5b38aaac5b46 | -30.90557 | -52.96364 | 2026-01-22 04:38:00 | NPP-375D | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 98e9526b-7fe6-3066-a110-56ee7caab8f1 | -30.17106 | -55.29974 | 2026-01-22 04:38:00 | NPP-375D | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 43757dfc-d25f-3098-8d62-e4a5eca34dcd | -26.97604 | -52.52893 | 2026-01-22 04:38:00 | NPP-375D | XAXIM | SANTA CATARINA | Brasil | 4219705 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 138ff399-3018-3047-8da4-24b0ffffe81e | -2.52796 | -47.79953 | 2026-01-22 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f7b89dc-7c23-316f-bd3f-bb61cf685841 | -2.14334 | -47.88364 | 2026-01-22 04:53:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 368d918b-7eee-3629-a425-3f1f9bf6540b | -2.14403 | -47.87909 | 2026-01-22 04:53:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6673f003-640e-3f84-9429-eb4b43fe70fe | -1.67368 | -46.70376 | 2026-01-22 04:53:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c84bf1b0-1a84-34df-8d49-a6b5dec24628 | -2.53176 | -47.80011 | 2026-01-22 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccccb41a-c5c6-33f9-9ba4-df6bd3394074 | -2.9666 | -54.33451 | 2026-01-22 04:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4ff6f5d-161e-3052-90bc-def4f226afbe | -2.51368 | -47.81636 | 2026-01-22 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc6e06b9-f6ca-3022-af0a-a1017a06e736 | -20.35329 | -57.87751 | 2026-01-22 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0787480e-4eb4-335b-8af4-b8d0471904f5 | -19.47375 | -55.46991 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| f928c877-ea48-3d49-b606-04936a939b7c | -19.68534 | -56.8881 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 243cd871-62c3-379a-952a-3fbd968131e9 | -19.45098 | -53.9858 | 2026-01-22 04:55:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3e5fefff-3795-30ba-99b5-461726a303f4 | -19.13738 | -54.54284 | 2026-01-22 04:55:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd9df94f-8216-35eb-b5e0-6af606743c1e | -19.6826 | -56.88376 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4980ce88-b323-3621-810f-04ff2e48618f | -16.12662 | -56.84295 | 2026-01-22 04:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d48dd6f-9f8b-3234-8626-af50a60474cc | -20.32513 | -55.9283 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ddb7332d-9385-36e1-9ba1-dbec70c0a222 | -20.84142 | -55.68813 | 2026-01-22 04:55:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b1a5e23-670a-3122-9fa9-b69c00b97109 | -20.90808 | -56.38577 | 2026-01-22 04:55:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 638a317d-82a4-3baa-9f21-bb72fb3b6546 | -19.67258 | -56.88192 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 405fcef8-ac70-30ca-9420-b8f04783aad5 | -19.67768 | -56.95586 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5d013349-3c45-3910-84ae-c6871eade7cb | -18.42013 | -54.55971 | 2026-01-22 04:55:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7b18e32-60b0-3192-bcb7-5d314e76fd42 | -19.67217 | -56.98951 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9058fb38-493e-348b-a6cc-d58654b459da | -19.64396 | -56.93046 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6015d9e1-30d1-397c-a874-a57c8084e6f6 | -20.33902 | -57.87882 | 2026-01-22 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a7c755ad-3ab0-31a8-9229-c4c88d12c09a | -20.34242 | -57.87947 | 2026-01-22 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| dfc0eab9-85fb-3dde-b485-814ecb4e213c | -15.03206 | -57.64038 | 2026-01-22 04:55:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16388cde-3206-383b-8af6-64345fb49d9d | -19.65338 | -56.93602 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 39c33f3e-f7fb-3e4f-8187-3f9e2cb2f2da | -19.2164 | -53.43937 | 2026-01-22 04:55:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5234eeb-868c-30ab-b039-8f34fe21d784 | -20.32845 | -55.92888 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b669092e-5858-368f-b66c-1252b3754b0a | -19.35508 | -54.67455 | 2026-01-22 04:55:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 717126e1-9431-38dd-b705-7c7886ef0746 | -20.61581 | -49.67316 | 2026-01-22 04:55:00 | NOAA-20 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75beccb1-705f-3bbe-8a86-ef4a206b8b2f | -19.13403 | -54.54227 | 2026-01-22 04:55:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a138e47a-01b6-3e28-946d-829ccf0b78b3 | -19.67926 | -56.88315 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 460a55cf-5c30-38f3-bdc3-ca6a4ecf96b8 | -19.34271 | -54.17365 | 2026-01-22 04:55:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8df402a5-42fa-3b94-95b1-d34d9265a150 | -20.62913 | -55.96208 | 2026-01-22 04:55:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 081d7bb7-46c8-36f3-b651-a6174b21b4f2 | -20.34308 | -57.87557 | 2026-01-22 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ab6f4fef-c65d-370b-b483-29688b5ea00f | -20.31174 | -57.87459 | 2026-01-22 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7932c9af-57c6-3efa-a138-6a7e2c5edd20 | -20.33561 | -57.87817 | 2026-01-22 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 07b84dfc-497f-3d60-aec9-e2a472cf13a4 | -20.34649 | -57.87622 | 2026-01-22 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ced07789-918b-3bc7-a9f2-989ce7d7a9b2 | -19.35451 | -54.67829 | 2026-01-22 04:55:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b7a0409-d0d6-3b79-9230-1a0cb2888cfa | -19.66194 | -56.88382 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8255ff8b-1385-35b0-9f36-9adf62e9f3c4 | -19.63843 | -56.96407 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 99906ac5-d851-3570-8324-e821bcdf1314 | -19.21236 | -53.4428 | 2026-01-22 04:55:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fcb273bb-a37a-3dfd-8b8d-55d860c24a6a | -19.13794 | -54.53912 | 2026-01-22 04:55:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 458b5711-9080-3200-9c76-e9d7a9b367ec | -18.29576 | -54.5731 | 2026-01-22 04:55:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc0a1db5-e45f-3229-bf3e-51cca82e8d7e | -20.34989 | -57.87687 | 2026-01-22 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 51a80271-5aa6-3acc-968d-e6e801b54001 | -18.41956 | -54.5634 | 2026-01-22 04:55:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 970a430d-1970-3eb8-ae2d-3b03148f5072 | -20.84328 | -51.73849 | 2026-01-22 04:55:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a9aed7a3-f6a3-30a7-9a07-f4362e22cf26 | -19.64061 | -56.92985 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7b971b1d-fc18-3ce9-aaaa-228f49b6043d | -19.67556 | -56.94778 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5dfc7741-8403-381c-bc2e-699540787097 | -15.46343 | -59.11493 | 2026-01-22 04:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c0dedf6e-34f3-3b88-85cc-828fd7ae82ba | -19.32641 | -54.02548 | 2026-01-22 04:55:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6a77494a-68b4-3ba2-b41d-53b9c49a6cd6 | -15.8551 | -55.84259 | 2026-01-22 04:55:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb391be9-d15f-3816-9cf5-671513487ef9 | -16.88849 | -54.54898 | 2026-01-22 04:55:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3bbafe5-f45e-3b07-a743-485a3604fbd4 | -15.97163 | -56.2728 | 2026-01-22 04:55:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 21de5cf8-a69b-3032-9663-2f0fefa3d482 | -19.67552 | -56.99012 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 765b3200-8907-3656-87a3-12cbbe2a9313 | -16.44816 | -58.16636 | 2026-01-22 04:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1ad9e064-608e-3b7c-ac84-e2f42070d6be | -19.62531 | -56.98092 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7d603736-47cf-3082-82ef-87b57efc1073 | -19.63446 | -56.96719 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fca57f8a-51ba-3934-a2a4-ab0796625b1a | -19.21293 | -53.43884 | 2026-01-22 04:55:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 491c8991-d035-347c-bf8a-7cbb708ef924 | -20.35944 | -57.88271 | 2026-01-22 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3c0f6a69-6fcf-311c-9a8b-456984c2cc07 | -19.67592 | -56.88254 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| e9173374-c101-3270-921f-d9bc9c4fa13d | -19.63781 | -56.9678 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 660e80c7-e511-32d2-b9aa-60ed7e44b5eb | -19.67156 | -56.99325 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ab8a017e-1bf8-36d0-a78c-fa9e6100268c | -19.64177 | -56.96468 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f241c0cd-acb8-348d-a7a6-6c84f7ea9cda | -20.3192 | -57.87199 | 2026-01-22 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 93828825-9ba8-31d4-907e-84796a3641e7 | -20.30834 | -57.87394 | 2026-01-22 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4ed397a8-679d-391a-acb4-f697d7cb2482 | -15.97499 | -56.27338 | 2026-01-22 04:55:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 51882b3c-9ead-3fbf-96b1-857ec8a2ab33 | -19.63385 | -56.97092 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |


[Clique aqui para ver as próximas entradas](README4.md)
