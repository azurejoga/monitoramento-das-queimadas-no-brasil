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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9244cd3-3854-3d07-9b60-407efa4e0a6e | -20.99675 | -41.78891 | 2025-06-20 04:04:00 | NOAA-20 | BOM JESUS DO ITABAPOANA | RIO DE JANEIRO | Brasil | 3300605 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7cf64978-a821-3ead-8226-17d2923cc194 | -21.19576 | -44.93588 | 2025-06-20 04:04:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c8bd4c72-9093-3df5-93d8-ca409a4ac6f7 | -24.24125 | -50.73982 | 2025-06-20 04:04:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7f015034-cea8-3d7e-b270-982314093c63 | -23.35463 | -46.19155 | 2025-06-20 04:04:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b4827a03-7782-3902-8ba0-8d00d2f00a28 | -19.54619 | -49.66361 | 2025-06-20 04:04:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 531933b3-680b-3020-8648-6b4fc2b73658 | -18.9921 | -52.08217 | 2025-06-20 04:04:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef33d9a9-affb-3615-97f1-e1c62076b125 | -19.54134 | -49.66405 | 2025-06-20 04:04:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 737aeb3b-776e-300d-9947-de8b1a85ec6d | -19.46019 | -44.15947 | 2025-06-20 04:04:00 | NOAA-20 | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33640a7f-45ce-3e8f-b04b-0cb72d26efcb | -22.53908 | -48.81149 | 2025-06-20 04:04:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a87b2abd-a132-3ae2-9576-40f040df1d1e | -21.20909 | -48.63316 | 2025-06-20 04:04:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 540c9e67-a420-3e21-b7f4-44692489d081 | -22.53775 | -48.81327 | 2025-06-20 04:04:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 14b303b1-bb33-3f78-9f24-519ae05fe4f5 | -21.20374 | -48.63953 | 2025-06-20 04:04:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2aab0cac-d8d9-33b1-8fb0-9ecf023d8e40 | -19.54569 | -49.66502 | 2025-06-20 04:04:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9b57318e-f8af-38e9-b5e1-19f968a1a611 | -17.60681 | -50.15689 | 2025-06-20 04:04:00 | NOAA-20 | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f84e7487-c4c3-3bea-8f5c-491787d0af37 | -22.19968 | -41.64549 | 2025-06-20 04:04:00 | NOAA-20 | CARAPEBUS | RIO DE JANEIRO | Brasil | 3300936 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 3e231563-57c6-3d83-aec4-a16412858d61 | -18.99139 | -52.08555 | 2025-06-20 04:04:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 623beb48-c4e0-3488-89db-0a0b34444fbd | -19.35285 | -45.15702 | 2025-06-20 04:04:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d680ad1d-7abb-3256-a53d-8cbab556f4e9 | -19.45426 | -45.30604 | 2025-06-20 04:04:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1824da05-cade-3f74-bdbb-e26f91808680 | -20.16142 | -45.72194 | 2025-06-20 04:04:00 | NOAA-20 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a4d71a4-ed46-3edc-8328-b1e7652aedbc | -22.90081 | -43.75203 | 2025-06-20 04:04:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7ca9bb93-190e-363c-aa34-5d802e0a85bc | -21.20841 | -48.63676 | 2025-06-20 04:04:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| efce2a50-7bf7-3b04-b43f-10bef6281a3f | -20.37713 | -45.60252 | 2025-06-20 04:04:00 | NOAA-20 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8ec18f7-ed7c-32cd-ba29-6e25fd95e21c | -19.77091 | -48.28785 | 2025-06-20 04:04:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f3a56c8-d2d9-3536-aca5-fc5f5874c785 | -21.13787 | -48.62975 | 2025-06-20 04:04:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b2400f8d-e8c1-3bc7-a171-fe3d23f1662c | -21.17951 | -43.98025 | 2025-06-20 04:04:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e7589930-d3c8-3b4d-aaa6-57a8c42b9e8c | -21.20444 | -48.63587 | 2025-06-20 04:04:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a9232920-d88c-39be-bae6-2f17bb3ec2a8 | -19.76625 | -48.29067 | 2025-06-20 04:04:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e624765e-dad3-3420-9cb0-7dc31470627c | -19.7162 | -40.35372 | 2025-06-20 04:04:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fcf49fe3-6799-377c-ab4d-659f9cf9a824 | -19.54094 | -49.66717 | 2025-06-20 04:04:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 97efc31f-af9c-34c8-b723-d09644584aff | -19.77022 | -48.29157 | 2025-06-20 04:04:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1e7d732-d017-309c-b826-f7f53f890a52 | -23.69816 | -46.67984 | 2025-06-20 04:04:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 031f8070-3fc1-3fa9-be0a-6ba4820b9404 | -19.76694 | -48.28698 | 2025-06-20 04:04:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 437cb065-027a-33a9-97e5-4d9eb15dc305 | -23.69791 | -46.67699 | 2025-06-20 04:04:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2625d031-3dc9-3fe0-8037-aa047d991229 | -19.54184 | -49.66264 | 2025-06-20 04:04:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 16d154d8-4e29-31b3-bb27-93fa0b7722ec | -22.6769 | -42.85382 | 2025-06-20 04:04:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 14017abc-6a0b-322e-8202-3f3282280602 | -23.33947 | -46.77382 | 2025-06-20 04:04:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 983ab8bb-9e71-35d3-a3d0-48e45e72f88e | -23.98412 | -48.91506 | 2025-06-20 04:04:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39db6d24-8d28-37a2-ba11-abbd8671dfd1 | -21.62475 | -43.46564 | 2025-06-20 04:04:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d7d25d71-b4f4-33ed-81d8-67a97ab4b738 | -20.31206 | -45.58598 | 2025-06-20 04:04:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af1d6337-7d15-3513-88e3-bed5639e5219 | -20.41553 | -43.55198 | 2025-06-20 04:04:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| db15404e-5bbe-39d7-a79e-0189ccd2a8b4 | -23.40403 | -46.55359 | 2025-06-20 04:04:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4188baa5-5270-32a7-9cc7-670de3b44304 | -16.3047 | -58.2676 | 2025-06-20 04:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.2 |
| 4541a92d-ea73-3359-80af-9ec313c01824 | -10.4754 | -47.0325 | 2025-06-20 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 9c60a317-6895-3115-9161-179f5f28d3bd | -10.475 | -47.0548 | 2025-06-20 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| e1c701be-fc53-3703-865d-bffa859ec994 | -9.4807 | -56.0801 | 2025-06-20 04:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 4821c7c2-098f-32be-a316-3dd15a4a5936 | -10.456 | -47.0571 | 2025-06-20 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 60f92a01-290c-3b3e-a7ac-4ab834c23f8c | -10.4944 | -47.0302 | 2025-06-20 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| f777b888-2ec0-38b7-a463-ada008f23f4d | -7.2219 | -43.0682 | 2025-06-20 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.1 |
| 2035f539-a596-3305-b9ae-fecf49107d77 | -10.4754 | -47.0325 | 2025-06-20 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 69ddac0b-7e57-3e1e-91e9-6f9018d4d1ce | -16.3047 | -58.2676 | 2025-06-20 04:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.9 |
| 92cfeb3e-60ae-301a-b364-6bd451f8d5f6 | -11.952 | -58.7376 | 2025-06-20 04:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| e558247e-f90d-3eaa-a9c5-504a404bb591 | -10.475 | -47.0548 | 2025-06-20 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 24d21ce8-858e-31da-9164-bc1b198e3540 | -10.456 | -47.0571 | 2025-06-20 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| d385143b-6411-39bb-897a-75ac14754288 | -14.0404 | -53.3669 | 2025-06-20 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 15edeec7-4107-3dea-9751-917b2764edbb | -10.4564 | -47.0347 | 2025-06-20 04:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 1d477e5c-b7b0-346f-9a64-60cd6bfd99fd | -11.952 | -58.7376 | 2025-06-20 04:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 9b1f92ce-cf64-383b-bd37-ab47b2e7811b | -10.475 | -47.0548 | 2025-06-20 04:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 141.5 |
| a69d17ac-3113-36f7-a194-bac386b226f0 | -10.4754 | -47.0325 | 2025-06-20 04:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 2dae22f7-6c3f-3e21-8b41-a3ba5f473ef7 | -10.4944 | -47.0302 | 2025-06-20 04:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 6441b836-00a7-3639-8fce-71a7acb8bdd4 | -16.3047 | -58.2676 | 2025-06-20 04:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.5 |
| cc0d1b1c-752c-3628-8763-f9a99b972d5b | -10.456 | -47.0571 | 2025-06-20 04:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 161.0 |
| ce7820ac-c52a-3b86-befc-f600d92b4348 | -11.952 | -58.7376 | 2025-06-20 04:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 49.0 |
| b21ec20e-af2f-30a1-bc09-e975fcf0caee | -16.3047 | -58.2676 | 2025-06-20 04:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.4 |
| 3c2f7f32-999f-350f-9640-ab0910395646 | -10.4564 | -47.0347 | 2025-06-20 04:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| aa8f2b54-6464-313f-bbb5-8f4a6bf0dda8 | -10.456 | -47.0571 | 2025-06-20 04:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 135.1 |
| c4dc2a8a-7f32-378c-822c-2876115c47d9 | -10.475 | -47.0548 | 2025-06-20 04:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 7adfd500-4361-39df-96a5-19dd9a89b112 | -10.4944 | -47.0302 | 2025-06-20 04:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 86b20d85-f350-394a-881e-05e25acf4467 | -10.4754 | -47.0325 | 2025-06-20 04:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 225.5 |
| a350fed3-f821-3f26-8e12-db781726c15e | -4.85101 | -43.19232 | 2025-06-20 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c579bca1-caf7-3a7b-bace-8d57fd36f565 | -3.03736 | -49.43394 | 2025-06-20 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1fc9e3b3-8731-3cd4-8267-de2c592b4da7 | -3.39339 | -43.13982 | 2025-06-20 04:49:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| beeb1f98-3c05-3d29-a251-98d4b73d2a71 | -3.04145 | -49.4306 | 2025-06-20 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bc41a4a8-0976-3b6d-ae9a-cd3399871e15 | -4.83936 | -43.19747 | 2025-06-20 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf880961-a2e3-3eb2-a036-c15ff3e02780 | -2.4475 | -47.47245 | 2025-06-20 04:49:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6e072898-db7a-34e2-8c14-460ff0d0028b | -3.61163 | -47.53868 | 2025-06-20 04:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddcbdcf2-6d94-300e-92a5-fc2b63a0f479 | -3.04495 | -49.43113 | 2025-06-20 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0b4c474f-6450-3d57-8b11-0d2c53839201 | -2.4278 | -47.23964 | 2025-06-20 04:49:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 158cf1be-8176-30d3-b12b-336b89ac4bce | -3.82354 | -48.98584 | 2025-06-20 04:49:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e08c9bf6-9577-327b-8e73-657700d4b05d | -4.85636 | -43.19313 | 2025-06-20 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b8c9666-fd46-33d1-bb8e-509d56ed55a2 | -3.75857 | -49.40667 | 2025-06-20 04:49:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fcd96064-e4fc-3ecc-97d3-09f076c178c0 | -3.03387 | -49.43341 | 2025-06-20 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 13ef5062-835d-38d9-b8e6-cc0353a56607 | -3.80936 | -48.95818 | 2025-06-20 04:49:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b387677-f7c8-39bc-9136-f3652340d8f3 | -3.60772 | -47.53809 | 2025-06-20 04:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5f347a6-c9a7-3729-a77c-20a8a97932ba | -2.91994 | -48.23257 | 2025-06-20 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4ab3347-0232-31d6-83c2-c6cd004f60da | -2.55023 | -47.70607 | 2025-06-20 04:49:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1834d838-d8db-3512-a951-4c7af468bc96 | -3.39388 | -43.13654 | 2025-06-20 04:49:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d63bcc15-6340-34ea-8c86-78b5a33f6fd2 | -3.03156 | -49.42509 | 2025-06-20 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb45132b-d045-3eed-94de-79b4ab9d1503 | -4.84518 | -43.19493 | 2025-06-20 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d527e1e-5df2-3ebb-9479-b2241a4d542b | -2.91185 | -48.23583 | 2025-06-20 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 82fa945c-68c9-3790-b3af-327ab948505f | -3.42101 | -47.60754 | 2025-06-20 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b77185d5-a7a1-396e-96cc-82ccc8a032d6 | -2.9754 | -49.10244 | 2025-06-20 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16e554ed-acad-3c34-8ae0-5c1632bbd5d9 | -2.91927 | -48.237 | 2025-06-20 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| deb0d48b-f13b-37f1-83fe-8fe98c75517e | -3.03505 | -49.42562 | 2025-06-20 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5e0ace8-47b3-38ec-8896-6b9325fdcb84 | -3.0115 | -51.49804 | 2025-06-20 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b949366-a042-3351-b95b-3a6eb7b185e1 | -3.04205 | -49.4267 | 2025-06-20 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 963809d4-bf9d-37f3-b70e-59ea21f3ca99 | -3.10959 | -47.48867 | 2025-06-20 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96695458-522c-3402-83ac-b7c36234f430 | -3.61554 | -47.53921 | 2025-06-20 04:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ae8c667-718c-3600-910e-5c701381e1a5 | -2.91556 | -48.23642 | 2025-06-20 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bfb8ba5d-9eca-3e35-affe-335529be766f | -4.85053 | -43.19574 | 2025-06-20 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b29e8fd4-765f-32ea-abf6-941b4806d5f4 | -2.29052 | -48.57955 | 2025-06-20 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README16.md)
