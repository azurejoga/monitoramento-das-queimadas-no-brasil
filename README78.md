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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d0cf56a-60e0-3958-9673-a50494925bc2 | -14.99648 | -50.06121 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 83d0780c-3150-34c2-b896-abb72822ab17 | -13.58589 | -46.91781 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5c29518-37c0-3139-85d9-75c716c43e45 | -15.99582 | -49.1519 | 2025-09-03 04:49:00 | NOAA-21 | SÃO FRANCISCO DE GOIÁS | GOIÁS | Brasil | 5219902 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6afddbcb-b51e-3f4c-83c7-598c4f054fdb | -12.98167 | -54.77181 | 2025-09-03 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1a687f8-d64c-3a7a-8854-43f775192fc0 | -14.35096 | -52.79687 | 2025-09-03 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e74b795-819f-371b-9968-47e9e7310423 | -12.60045 | -48.20414 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 51e7ec46-a29d-37ac-871c-a892f0be1594 | -12.80599 | -48.05059 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a5249ac-cb16-370c-8c2f-be360ab8ce20 | -13.72967 | -46.93722 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bae7565c-4c9e-31ae-acb1-f1f2bed18f9b | -12.85422 | -48.01859 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10b4da3f-feb3-3369-9f5a-28288d94094b | -14.78719 | -48.16192 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 338e553d-58b4-3475-bf86-1e12fc9fac17 | -11.53365 | -54.40715 | 2025-09-03 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1c1caa9-3bd7-398f-9dc3-c44c0a624990 | -14.40695 | -51.70163 | 2025-09-03 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87d67a71-c747-3173-bcf2-15ba543c3d29 | -15.55576 | -48.3883 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1130b7f6-780c-38e6-a7c8-1962464fe83a | -15.74261 | -53.66171 | 2025-09-03 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c77047fe-04cd-3599-968b-fb084ec1cecb | -11.86643 | -51.47072 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 677c6485-c396-31df-b106-a8d2164a4f8c | -12.99296 | -48.08541 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6452c028-4d7e-3a5c-9a94-d8fba57a9afe | -17.53487 | -47.58146 | 2025-09-03 04:49:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cce09db8-9849-3551-9f30-27f1a2315f39 | -15.15078 | -53.51166 | 2025-09-03 04:49:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a725cb1-b4f4-31f9-a4fa-bfe8f77b95b5 | -13.00515 | -48.11184 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe77f884-1d05-38ce-84c2-f77d681dd463 | -14.58736 | -48.04245 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d168999c-6295-3f91-8270-d5a26c981c78 | -11.41895 | -55.18532 | 2025-09-03 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4057fd81-6843-315a-9532-a2d6db3550cb | -15.16322 | -52.35765 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 926ae5ea-b065-3139-8eb8-8be3254766d3 | -15.10787 | -48.12535 | 2025-09-03 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31a5f095-e2d9-3bbd-91b9-d374d36ff1b8 | -13.0946 | -57.11761 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2628cdda-a72a-3f47-929b-cb3b9ff57b01 | -12.95453 | -48.07552 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 562391ef-6917-3750-888b-d637f3f8fc68 | -12.88979 | -48.04942 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94406a58-e201-32e5-a025-4471e2873b87 | -15.54063 | -51.71918 | 2025-09-03 04:49:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 155863c2-3312-33eb-a7a3-f5cbcd0dd6bd | -11.66177 | -57.36005 | 2025-09-03 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07ab9f21-d521-3da0-be2e-28e78a6dfb80 | -14.40193 | -51.71208 | 2025-09-03 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 363a1063-6ab6-3572-898b-de188ccf26fd | -13.49923 | -46.81904 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9dd1ab2a-36ee-38ef-8b78-de0a459f9e1c | -12.92146 | -57.00961 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 962cc526-0381-3120-b241-08a7f7ff058e | -13.33778 | -46.83779 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4f4665c-a473-3b50-bdba-d69c32e91792 | -15.24138 | -53.79786 | 2025-09-03 04:49:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d98012cd-6f23-3519-b4bd-8a967b568a6e | -15.24744 | -53.80255 | 2025-09-03 04:49:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ce0dff6-f0ff-3504-bacc-35ac99e178cc | -13.50813 | -47.01689 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8a017baa-80ff-39f2-b9fb-28db1f22c5cf | -14.5167 | -53.15083 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e6b0917-d0a5-3c0b-bdee-965224806464 | -12.9795 | -54.76364 | 2025-09-03 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c512488-bbcf-3ac2-9d04-f06197b9dc91 | -11.85456 | -51.57105 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e3c0084-b4d6-3431-a08f-851487419425 | -14.2754 | -51.64753 | 2025-09-03 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a2e14f8-3fa1-3836-a3a3-02d49a59de00 | -11.84193 | -51.45597 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2de00e38-fadf-3b0d-ae11-0e912d1f8c5c | -11.85778 | -52.43021 | 2025-09-03 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c735aea-0e2f-3630-a90f-fb78bcaa3de8 | -14.57501 | -54.5531 | 2025-09-03 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97811d78-7a26-3019-b3b8-54faf9a4e964 | -14.98929 | -50.06026 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a8767c7-d5d9-3b06-9b39-6e47a96f9c5a | -18.0207 | -51.61552 | 2025-09-03 04:49:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| feecc765-c296-3931-b6d9-ff609861aa87 | -13.49657 | -51.812 | 2025-09-03 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f92158e-895b-3a28-8e70-a1d89fef810d | -16.79298 | -49.27648 | 2025-09-03 04:49:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c98e2a1-708a-3555-afb1-05d30f57fb68 | -12.51223 | -49.56766 | 2025-09-03 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eeb3781c-02d5-3ecb-88cc-005d67c252b6 | -12.4938 | -53.8444 | 2025-09-03 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f901294b-f954-398e-b67e-4cd1e6f19338 | -15.20106 | -53.79476 | 2025-09-03 04:49:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ad61651-94c1-3feb-89a4-0978f91854c6 | -13.45871 | -46.93302 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ad15cf0b-961a-306c-9703-ec040ac83052 | -13.72921 | -46.94072 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b6df7a7-c71c-3499-8cc3-588b661b3347 | -13.70058 | -46.96206 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c5f08d80-f8a1-35d2-ba2a-ac145ad0a25a | -15.56493 | -48.41082 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 97caafc5-110c-3e9f-9651-c514df1bbe78 | -15.01201 | -50.07095 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f48bc67e-0119-3880-ad03-f53fef6980d7 | -14.78976 | -48.17294 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2dabb54-129d-3d9b-9fb2-65a9a13b0f98 | -15.58109 | -48.31823 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91d48d7d-7e07-3616-97e7-9e56cbd8371c | -12.17751 | -53.88528 | 2025-09-03 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f656be37-f103-3503-b895-0039f5b30520 | -12.84384 | -48.03592 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f2691ee9-1776-3914-adfe-6b5652b25dd4 | -12.95848 | -48.07576 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90092b79-28b3-383e-b4d3-1f522d7e6010 | -14.7662 | -48.13687 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0887d8e5-31b1-3728-81ae-57e10cadec54 | -12.9355 | -56.95229 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 77514570-62fb-3d3b-9c2c-e33771d4158d | -13.46389 | -46.92656 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b901cb46-fb9f-3ca4-a7c6-114bc692937a | -12.91659 | -57.00031 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7e625b22-e3df-3830-8f5d-119517fa99fe | -15.99753 | -54.13585 | 2025-09-03 04:49:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e001674-c2cb-314a-85eb-a27c5c9a7e2e | -18.19871 | -48.12734 | 2025-09-03 04:49:00 | NOAA-21 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e79e1078-f569-39fe-958f-aca1bddcee48 | -15.5603 | -48.41538 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3983fc26-8f56-3b96-ad12-2aa71029e18f | -15.74858 | -53.68837 | 2025-09-03 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b9dc48d8-f4ad-3336-9e58-9cca10b3cb4f | -13.306 | -46.84921 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 418cb697-423e-3382-99af-34847033b7c5 | -11.85074 | -51.42082 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc6e2eb4-e153-33fb-aa6c-818d399f233a | -15.01971 | -50.04216 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0d628c0-8d38-3bb0-904f-b796f76c3097 | -12.5152 | -49.57238 | 2025-09-03 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f1a1b26-eeb8-3247-8157-f53157c3c5cd | -11.86053 | -52.43425 | 2025-09-03 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a54a7a88-1242-38f3-bd70-8470881fe3d0 | -14.99289 | -50.06072 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 89b0a77e-54a4-3590-930b-8066ad957a9f | -7.7039 | -48.7371 | 2025-09-03 04:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 138.8 |
| acd87435-e3e7-3825-82ac-bc9372a1ba1c | -7.7036 | -48.7587 | 2025-09-03 04:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 0f30cb0e-68d1-3c1c-bdca-b02f56901c29 | -7.6851 | -48.7386 | 2025-09-03 04:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 68.4 |
| c7b4c096-09ef-3b98-a6b4-6cba91ca5b39 | -7.7041 | -48.7155 | 2025-09-03 04:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 8ff80a94-431e-3df6-8349-a8463d4d7758 | -3.2305 | -47.135 | 2025-09-03 04:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 1dbb6237-581d-3c79-86aa-ec92e65f4ac2 | -19.14436 | -47.59692 | 2025-09-03 04:51:00 | NOAA-21 | PEDRINÓPOLIS | MINAS GERAIS | Brasil | 3149200 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95b4373b-ddcd-3e1e-80f6-4e66caadbfa4 | -20.73208 | -49.33637 | 2025-09-03 04:51:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 30f6f67f-c369-37cc-aac9-3f7a9ce7e220 | -22.70565 | -47.03556 | 2025-09-03 04:51:00 | NOAA-21 | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c58458d5-22fd-3145-9542-989c5eb93b90 | -22.00548 | -45.06153 | 2025-09-03 04:51:00 | NOAA-21 | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9638ae14-aeee-33d2-8822-1cfd89330d76 | -18.66821 | -49.09646 | 2025-09-03 04:51:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1eaa4402-ef25-3a12-8c78-aac1e348fd3d | -23.3506 | -47.72202 | 2025-09-03 04:51:00 | NOAA-21 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| de050667-de3d-30e2-a7b3-f924fa2448c5 | -23.92868 | -48.8622 | 2025-09-03 04:51:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffeec867-b6c6-3dbd-b26d-b20994bf3852 | -20.89168 | -50.09618 | 2025-09-03 04:51:00 | NOAA-21 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| fb0055db-eaf6-332d-82ad-facf0f4e67d5 | -22.17762 | -48.82444 | 2025-09-03 04:51:00 | NOAA-21 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 252295db-c4dc-3fbb-902a-b35d7aff3000 | -23.53845 | -46.86763 | 2025-09-03 04:51:00 | NOAA-21 | BARUERI | SÃO PAULO | Brasil | 3505708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bdbc1830-4ac4-32ed-b61a-832ec4d3a399 | -22.17715 | -48.8286 | 2025-09-03 04:51:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| fac7c09c-85e5-3610-8111-709f38cdf7f1 | -20.94732 | -54.95676 | 2025-09-03 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8e880ad-9a18-3856-84b5-e261be8f1f4c | -21.08966 | -45.45596 | 2025-09-03 04:51:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3aceaa93-6ca5-3664-88fc-38e928cdd004 | -22.18558 | -48.82979 | 2025-09-03 04:51:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 6a0f94fe-af42-348e-96e6-c3bb79824e6c | -21.30322 | -48.55267 | 2025-09-03 04:51:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70d635bb-ae36-326a-924d-bb00bd4657da | -18.14406 | -51.75072 | 2025-09-03 04:51:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f1de668f-5e9f-3d45-80ad-30f615ded3ce | -19.38194 | -49.06678 | 2025-09-03 04:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5d04a29-d064-31b0-a64b-4e03e2662374 | -22.18136 | -48.8292 | 2025-09-03 04:51:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 18129f3f-ded7-3c48-aaa6-ad9102a62bd6 | -19.38593 | -49.06745 | 2025-09-03 04:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f0dd73d-b76b-3a17-8001-28a4c7f32516 | -20.89414 | -55.14092 | 2025-09-03 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf427674-2d2c-3272-8b2f-e51e9e269d4b | -18.14349 | -51.75465 | 2025-09-03 04:51:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19485f98-3371-36e3-9776-1ab2167564e2 | -19.38148 | -49.07047 | 2025-09-03 04:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README79.md)
