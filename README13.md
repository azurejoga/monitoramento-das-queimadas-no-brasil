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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4a7d66f-fb40-3bd3-b831-4f5c95b94bcd | -21.81139 | -52.71931 | 2026-07-01 04:06:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ae256523-5559-3839-9f80-af3375f797dc | -22.69852 | -53.96609 | 2026-07-01 04:06:00 | NOAA-21 | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d5da910e-349b-39a9-ab5a-ab9061e3d7bb | -22.436 | -51.87145 | 2026-07-01 04:06:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 7b38dafc-db55-3221-944e-ebbd8b7274da | -19.84459 | -49.07178 | 2026-07-01 04:06:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57874e66-45e6-3510-bd24-72138a6c385e | -19.84537 | -49.06771 | 2026-07-01 04:06:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55b33569-acaf-332d-9ae9-719078329cfa | -22.67557 | -43.47838 | 2026-07-01 04:06:00 | NOAA-21 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e7f0c772-0e9b-39a1-aa9d-977997b96231 | -23.81874 | -48.71303 | 2026-07-01 04:06:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00d59ae1-83c5-3f4f-8420-58a7d9991318 | -20.54858 | -48.53296 | 2026-07-01 04:06:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7f472ac-f666-3e98-87ac-0c4d5b09854a | -22.79922 | -49.34924 | 2026-07-01 04:06:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b2a607e-bd9a-3ec9-8a48-f806e8c99679 | -22.87473 | -43.66319 | 2026-07-01 04:06:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 39473137-66eb-3b79-b519-88650a3bbf30 | -22.804 | -49.34626 | 2026-07-01 04:06:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fba3a3d3-4371-3574-93bc-2b95f0c7fc69 | -19.51558 | -52.74409 | 2026-07-01 04:06:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 487e0bd6-163e-3350-b15a-11c0e9526a8f | -12.7751 | -44.4927 | 2026-07-01 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 449.6 |
| 26c4d164-833d-3d97-ace4-2184a2a7a4da | -10.6787 | -54.5153 | 2026-07-01 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 3acbfffb-a8f2-3ceb-925c-a53f71a9054c | -11.4147 | -56.0726 | 2026-07-01 04:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 37.4 |
| c2edfdab-8d81-37b5-96de-430544234ede | -10.9209 | -43.0384 | 2026-07-01 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 6281069b-8a6f-31eb-bdd2-1f9844e3846b | -10.6596 | -54.5372 | 2026-07-01 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 48d919ea-e6ba-34fb-89b4-e5a555335c8b | -10.9401 | -43.0355 | 2026-07-01 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 8fb57be4-cf33-35a5-9deb-949a2eaace74 | -12.7562 | -44.4724 | 2026-07-01 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 331.8 |
| 5001c842-2087-33f4-b621-a998835c6745 | -12.8354 | -44.3657 | 2026-07-01 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 231.8 |
| 0b7e6e6d-e2ac-37f1-bd83-2f5d4e76dc00 | -12.8552 | -44.3389 | 2026-07-01 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 230.9 |
| 10c8b90b-ae39-3932-853b-a3f264f6d64e | -11.4149 | -56.0525 | 2026-07-01 04:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 126343a0-d3cd-3aac-8486-b4bc4f7d1b87 | -12.8165 | -44.3454 | 2026-07-01 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| fe538a53-7aec-3259-8ccd-3f35d4934868 | -10.9397 | -43.0593 | 2026-07-01 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 89c8f576-ef5a-3fcb-8956-d0710413336b | -10.9205 | -43.0622 | 2026-07-01 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.4 |
| dcb31a80-e517-3365-8abb-764be1bf5b64 | -12.7557 | -44.4959 | 2026-07-01 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 365.8 |
| 6b891236-0a99-3c30-8b34-b88d3b8351ed | -11.4336 | -56.0711 | 2026-07-01 04:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 31c463b5-aa6f-39dd-a698-cd13d9c0673e | -11.4338 | -56.0509 | 2026-07-01 04:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 10a4305b-6da3-3032-b00f-05d5e77a55d9 | -10.6598 | -54.5169 | 2026-07-01 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 47859f71-0e5d-3975-92cd-bf92852ca929 | -12.8359 | -44.3422 | 2026-07-01 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 402.3 |
| 05812d44-7768-3320-ae78-0985cef5cc90 | -10.6784 | -54.5356 | 2026-07-01 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| f82503e4-6ecd-330b-90b5-2ada16b22035 | -11.6286 | -59.0169 | 2026-07-01 04:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 7050c5cd-87e7-3194-af05-989c7ac60db4 | -12.8548 | -44.3625 | 2026-07-01 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 258ca7be-acf1-3b24-9e12-f996801d7f3f | -12.8363 | -44.3186 | 2026-07-01 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 7f2aa35c-d304-3e23-a888-a0cb90477d3d | -12.7755 | -44.4693 | 2026-07-01 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 412.4 |
| 35d2fd28-e7a6-3703-9f22-79f8ec50f656 | -10.9397 | -43.0593 | 2026-07-01 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 153a3be2-52e4-3d2b-b8b0-6cb5f225c2c0 | -11.4338 | -56.0509 | 2026-07-01 04:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 112.0 |
| b42a349f-439b-3b9d-90c4-ad400e419372 | -11.4147 | -56.0726 | 2026-07-01 04:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 37c9ee51-4fec-30a7-bc36-aef9ca38afe5 | -12.7751 | -44.4927 | 2026-07-01 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 457.0 |
| 7095498b-e147-34ef-b137-e3c809973139 | -10.9209 | -43.0384 | 2026-07-01 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.7 |
| c5192fcd-164a-3b6a-bf7d-eb03f0bb52cd | -12.7746 | -44.5162 | 2026-07-01 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 90d179c0-df6f-30d2-b8ac-b56a91adf670 | -10.9401 | -43.0355 | 2026-07-01 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 362a55c7-d478-3cec-9dbb-22b7af2dd6b7 | -12.7562 | -44.4724 | 2026-07-01 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 239.6 |
| 5e6ba193-8498-3c76-bdac-fa7e41cb2b1d | -10.6598 | -54.5169 | 2026-07-01 04:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 5f64a27a-f484-390f-9017-99848cc81109 | -12.8548 | -44.3625 | 2026-07-01 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 36974b2a-9817-30c1-9b99-c01e8f9a765c | -12.8354 | -44.3657 | 2026-07-01 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 196.6 |
| a4eb3bc7-d781-3db3-b633-3164ec402c30 | -10.9205 | -43.0622 | 2026-07-01 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| fed59bed-98da-3029-ba7e-680b3a606457 | -12.8359 | -44.3422 | 2026-07-01 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 446.3 |
| 0fd30ded-85eb-3a94-b007-ab28b3ab42b3 | -12.7557 | -44.4959 | 2026-07-01 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 326.4 |
| 812da61c-225a-3f87-809c-d9fb1b300080 | -11.4336 | -56.0711 | 2026-07-01 04:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 560bece3-2c5b-32c8-9955-ed234dafab19 | -10.6784 | -54.5356 | 2026-07-01 04:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| b330126e-93c3-3bb1-936a-bb772c4d1733 | -12.7755 | -44.4693 | 2026-07-01 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 329.1 |
| bc21dc72-9430-3f31-ae5f-a570fe438c2d | -12.8552 | -44.3389 | 2026-07-01 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 250.6 |
| 7eed10a5-46b2-3ade-8751-b03abc93d1bf | -11.4149 | -56.0525 | 2026-07-01 04:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 97f915e9-e348-3ee6-9286-27f360125433 | -10.6787 | -54.5153 | 2026-07-01 04:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| e53ff50d-5e66-3041-a603-3e99a89f9d21 | -10.6596 | -54.5372 | 2026-07-01 04:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 42.5 |
| f2176b31-4b00-3f1c-9530-27f78b92da3b | -12.8165 | -44.3454 | 2026-07-01 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| e86332bc-2959-3234-9516-1c82bc74292c | -10.9205 | -43.0622 | 2026-07-01 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 24cf5d91-3aa8-3ed9-8f69-041b351c0e86 | -12.8359 | -44.3422 | 2026-07-01 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 479.9 |
| 32dd152b-09f4-32d4-9c0b-f3397b995ded | -12.8548 | -44.3625 | 2026-07-01 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 4561767e-b6d1-33e5-bdc7-cce8ab418903 | -12.8165 | -44.3454 | 2026-07-01 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.4 |
| b6d18f15-7213-3a93-b639-8c0813bf0455 | -12.8354 | -44.3657 | 2026-07-01 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 190.3 |
| c0017006-8f11-34c7-97f5-0acc4f74b50f | -10.9401 | -43.0355 | 2026-07-01 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| a4e61acd-550f-390b-bd61-5439d5dda92f | -11.4338 | -56.0509 | 2026-07-01 04:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 25e52a4a-5d35-3873-aa28-fadb48f4605b | -10.6787 | -54.5153 | 2026-07-01 04:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 51cdc1f3-1590-38c9-ac62-b10fd088556e | -12.7755 | -44.4693 | 2026-07-01 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 339.3 |
| a92e71da-fdc4-3d03-a411-9cd478a9b5a6 | -12.8552 | -44.3389 | 2026-07-01 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 218.5 |
| b6bfdb2f-4784-335c-a95e-c23a8bcb7c49 | -11.4149 | -56.0525 | 2026-07-01 04:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| faa10e11-c807-3d58-a631-337f20c7ffdf | -12.7751 | -44.4927 | 2026-07-01 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 525.0 |
| 20d40b43-07ab-36b6-b829-1e0872e2e37b | -11.4336 | -56.0711 | 2026-07-01 04:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 135.9 |
| 618be32e-2636-3aff-ae98-7c0597df418f | -12.7557 | -44.4959 | 2026-07-01 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 257.8 |
| 21603774-e256-3b22-9472-ec55ae25b8b5 | -10.9209 | -43.0384 | 2026-07-01 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.4 |
| f717c8c6-c26d-3b9c-9461-afd379679a4c | -12.7562 | -44.4724 | 2026-07-01 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 170.6 |
| 7082db4d-6669-34c9-b1ef-a41538970206 | -10.6784 | -54.5356 | 2026-07-01 04:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 3e2fa165-6c31-31da-9d9c-b80085b65806 | -10.9397 | -43.0593 | 2026-07-01 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 076635ea-add1-3e66-b3d1-0a8df31f1e57 | -11.4147 | -56.0726 | 2026-07-01 04:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 4f223c63-a19e-321e-a47d-5b8e02f8b803 | -5.09804 | -37.78777 | 2026-07-01 04:36:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 906910f5-f57d-3cec-80a0-7a2e20804271 | -5.97753 | -47.07019 | 2026-07-01 04:36:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f9633f0-7542-3671-8653-ee5c62e52988 | -5.79706 | -45.06926 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d4ec75c-f9f6-3571-91ec-9d0d733a2e3f | -3.91826 | -47.82252 | 2026-07-01 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d59d928-3c9e-3c9f-9fd6-deed2b1acadb | -4.58295 | -48.02842 | 2026-07-01 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bac5b10e-8aff-3e28-b271-89163bf110f1 | -6.96018 | -44.55078 | 2026-07-01 04:36:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50c9f13b-9cc9-3009-9f1c-e98a4e8ee899 | -5.49781 | -43.22407 | 2026-07-01 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a912cf6-87a4-3e9e-a44c-41555ba7ca08 | -5.54925 | -43.96722 | 2026-07-01 04:36:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4a09bbaa-090a-35eb-be43-fc302c3b03cf | -6.16065 | -44.64506 | 2026-07-01 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e5137e0-7721-359e-970c-8ff2e950661c | -5.55624 | -43.9683 | 2026-07-01 04:36:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4e688ce1-8f15-3cd3-90bd-799458947a74 | -5.21264 | -37.4761 | 2026-07-01 04:36:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1720fe82-53ca-364f-9d94-bddb7a7e8b5f | -3.50879 | -48.03949 | 2026-07-01 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a4d332f3-9b88-36c8-bd5a-28dd60c69c9e | -6.95612 | -44.55409 | 2026-07-01 04:36:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 32d4cea4-3d28-39de-9b27-a75d3e8274c2 | -5.79819 | -45.06208 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 111bc1f9-0a4a-3f6a-9015-8e144918aa1c | -5.81255 | -43.79945 | 2026-07-01 04:36:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3738e831-e1fc-3ff8-b11a-52351c128f60 | -5.13697 | -37.84229 | 2026-07-01 04:36:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| d67701e4-8ea9-3616-ac8f-f231f7a0a650 | -3.50531 | -48.03894 | 2026-07-01 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d3c6e733-4d1f-3cfe-b9ad-57da1dd9d896 | -7.00325 | -42.7791 | 2026-07-01 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 20376a4f-1cdf-341a-ad5a-ecd8be889b83 | -5.80342 | -45.05907 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd5db958-bb09-3188-939f-2f4dd8d0ec57 | -5.8006 | -45.05495 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f36118d0-2d33-3eb3-aeae-8b4d715ebdfc | -5.79258 | -45.03182 | 2026-07-01 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec852bd9-9776-3835-b5a4-6e3639f6c070 | -5.55682 | -43.96447 | 2026-07-01 04:36:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dcb86ae2-e8d7-3c9b-93e0-1adad2e678c0 | -6.91655 | -42.84468 | 2026-07-01 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 26e6b221-a62e-330c-b251-e7a7d483a3ee | -6.95899 | -44.54992 | 2026-07-01 04:36:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README14.md)
