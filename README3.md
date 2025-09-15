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
| 80e94bf4-56bd-3092-8952-592bbe46a65c | -12.12451 | -44.8225 | 2025-09-15 00:30:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| eff5a7c9-81b3-3887-ba24-6f5a00e1a68c | -14.93281 | -46.56946 | 2025-09-15 00:30:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 8ac61913-5367-335a-b3c8-ceca9e397a37 | -15.04967 | -47.97158 | 2025-09-15 00:30:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e82c3047-c192-338b-9ec9-734eca9b6d20 | -15.77262 | -53.47747 | 2025-09-15 00:30:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 32.5 |
| a749cae1-3a19-3682-a127-5e53a5145fe4 | -12.57015 | -45.65267 | 2025-09-15 00:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| ffd8856e-1ebf-3009-b67d-5b03706b74d9 | -12.64181 | -47.93164 | 2025-09-15 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 28a6f9b2-5e4f-371b-9541-5a5a0a49a2e9 | -16.38353 | -48.89662 | 2025-09-15 00:30:00 | TERRA_M-M | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 23.8 |
| e2cd0cf0-214b-356d-84f1-534f8efeeb97 | -16.48198 | -55.1293 | 2025-09-15 00:30:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 25.7 |
| 85572cc5-938d-3ffc-a250-64501579d9fb | -15.7988 | -53.47361 | 2025-09-15 00:30:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 8cdd9f08-43d5-36f5-88b1-cc8b04dfc07e | -12.09694 | -44.86524 | 2025-09-15 00:30:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d9d74a12-d326-3213-97a3-ef2e6f8679e2 | -14.93406 | -46.57846 | 2025-09-15 00:30:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 2b2b0ba7-e3de-37be-a795-7e25acb50979 | -14.50154 | -47.31874 | 2025-09-15 00:30:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9280497c-2e16-3de2-890c-ef839e5bc436 | -12.83389 | -47.18612 | 2025-09-15 00:30:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 06ec4deb-0010-345f-80b6-245f2500ed1c | -12.59932 | -45.73022 | 2025-09-15 00:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f891fd40-bf32-39f3-bdb0-e54583ae043d | -14.4014 | -48.35582 | 2025-09-15 00:30:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 789c5016-e7a9-3e6a-8f7c-c3f715180b18 | -14.50278 | -47.32781 | 2025-09-15 00:30:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ce907f8c-ea1a-3f83-a1a5-e7ddc2274439 | -12.55965 | -45.64441 | 2025-09-15 00:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 017cb105-6a45-3539-a1ea-57a29d326b86 | -12.61514 | -44.20325 | 2025-09-15 00:30:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9dce3f82-596a-36e3-ac94-4cb41961f1c3 | -15.87533 | -47.33298 | 2025-09-15 00:30:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c4f154ff-7486-3174-bd95-20bf408be8a8 | -15.87409 | -47.32371 | 2025-09-15 00:30:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 4e9d4106-799d-350a-aed3-f4bba1bb96b3 | -12.99608 | -47.97269 | 2025-09-15 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4b63cb09-aef5-32aa-951c-576a0c5297d9 | -14.49642 | -47.34727 | 2025-09-15 00:30:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 19b62caa-0fc0-319f-8780-f1ee8bbab178 | -13.18899 | -47.2837 | 2025-09-15 00:30:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 56887178-5ea1-3b1a-8bb5-1798c8aea29b | -15.04734 | -48.16169 | 2025-09-15 00:30:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 295b798e-5993-3566-b951-2652ff5fc3e6 | -12.56877 | -45.64304 | 2025-09-15 00:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 189.0 |
| 3f2beed7-c9cc-3bb5-81c3-4fb53c7e369f | -15.07647 | -48.03539 | 2025-09-15 00:30:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d5e6304c-9871-38d0-bee7-4f5a784c4473 | -12.79198 | -47.95923 | 2025-09-15 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6e1deb82-4bb1-38b1-855d-c2e788b952f7 | -15.03166 | -47.97378 | 2025-09-15 00:30:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |
| f7cf03ec-e0f0-3b09-bb12-0e6d69c559b4 | -12.95208 | -48.25159 | 2025-09-15 00:30:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 340a3991-4f38-365d-b315-d0845c3728ae | -12.76145 | -48.00087 | 2025-09-15 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| af08480c-f6d3-349a-b514-6122e1cba8c0 | -12.95332 | -48.26085 | 2025-09-15 00:30:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 24396497-9434-3911-bb17-7f27c66a949c | -14.279 | -46.12468 | 2025-09-15 00:30:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9c0586ec-aed6-3f1f-bd77-5ae89ec09629 | -15.75581 | -52.24675 | 2025-09-15 00:30:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4b69429d-8ad3-318a-bacd-ae5ccae2c73e | -14.16301 | -46.14849 | 2025-09-15 00:30:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| dbb42ca2-76ca-369e-9cfd-bf2986738464 | -12.67655 | -47.7234 | 2025-09-15 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f453b02c-7e55-39e1-8a22-f324490c1dc7 | -14.44347 | -43.22067 | 2025-09-15 00:30:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4ecc4002-5175-3b28-9f5a-50ed2fcd1b44 | -15.7875 | -52.20771 | 2025-09-15 00:30:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 88ec37f2-128e-3fd8-beb3-4db8c2721320 | -15.06619 | -48.02706 | 2025-09-15 00:30:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 20df9e74-f60f-3987-96cc-64fb7c75f27b | -13.76613 | -48.77281 | 2025-09-15 00:30:00 | TERRA_M-M | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 52ead00a-cd4a-36c6-9486-6575f1a6e270 | -14.94415 | -46.5862 | 2025-09-15 00:30:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 5f7071b3-bc48-3443-964b-7531d8fe6553 | -15.02433 | -47.99057 | 2025-09-15 00:30:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d40ee20f-cf29-3894-a93a-13b7fb107308 | -14.50401 | -47.33686 | 2025-09-15 00:30:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 3eb1e18a-692b-3ab8-a4b6-71c2951b426e | -14.33916 | -46.09038 | 2025-09-15 00:30:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c9b6c0e7-1c5d-3dbc-8ead-82ca6ae6db82 | -12.96308 | -47.99623 | 2025-09-15 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1d95fe0c-7acd-36bd-aa2c-a5ad98482ce8 | -12.68788 | -47.74019 | 2025-09-15 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5c83dfcd-fd70-3f48-9b9a-4a1ae91c9230 | -14.50524 | -47.34587 | 2025-09-15 00:30:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 501adcb0-deca-3c7a-b5fb-8af2a8675a79 | -12.56104 | -45.65407 | 2025-09-15 00:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6d97559c-34ee-3dcb-83e9-c65bddc20ef3 | -15.92564 | -49.96171 | 2025-09-15 00:30:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a36fdac0-afe8-39ec-9ffc-5a656be6ca3d | -12.79074 | -47.95016 | 2025-09-15 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bcd7dc4a-a404-30ab-97e8-d7a1d70ddb9b | -14.44151 | -43.20831 | 2025-09-15 00:30:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3dc93ce9-b77c-3058-b568-7c804f8c49b4 | -15.75335 | -45.09098 | 2025-09-15 00:30:00 | TERRA_M-M | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| be64bd68-bb9f-34a8-94bc-acfefe507c87 | -16.47907 | -55.10072 | 2025-09-15 00:30:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 25.8 |
| 5f49cb91-53ff-3400-a6f9-a62ddbc77ce6 | -12.44788 | -44.7426 | 2025-09-15 00:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| d3618a47-fa61-34d3-829a-daca664d5c5e | -15.74429 | -45.09246 | 2025-09-15 00:30:00 | TERRA_M-M | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 12834f1c-7f80-3047-8464-c01517dfc5ec | -15.04067 | -47.97268 | 2025-09-15 00:30:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 67ddc633-23eb-337b-a75f-a826b2979c3c | -13.75698 | -48.77407 | 2025-09-15 00:30:00 | TERRA_M-M | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 20978be6-890f-3db6-ac52-3cffa47ae26e | -5.76802 | -52.3652 | 2025-09-15 00:33:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 640f6f0c-4048-39be-bb12-abc80c534935 | -7.39399 | -49.98697 | 2025-09-15 00:33:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 9b1ab057-03ae-3478-85c7-a6136d582d30 | -8.07939 | -44.51094 | 2025-09-15 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 557ccf9e-f3db-3c0f-9b3d-8925cb6d4e5a | -6.69335 | -45.52179 | 2025-09-15 00:33:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| c7deca76-0e18-3fa1-a73b-c4b9ac231c4c | -11.78275 | -46.66369 | 2025-09-15 00:33:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 126b4bc7-e656-3761-80bd-8f6661c0d318 | -5.69142 | -49.19576 | 2025-09-15 00:33:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 090135ab-b5e5-30e7-ad37-5004e92ae3db | -7.89036 | -43.58478 | 2025-09-15 00:33:00 | TERRA_M-M | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 12753ad5-d2b2-3878-a573-2f09819bfb66 | -5.23314 | -48.54917 | 2025-09-15 00:33:00 | TERRA_M-M | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 80e01287-472b-38af-923c-881bc9527aa8 | -5.63801 | -45.94103 | 2025-09-15 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 70220370-8dce-3402-bcbc-6882487e6a23 | -8.60526 | -46.3631 | 2025-09-15 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3cc591b5-7bde-3dbd-a61d-89e6caa3eafc | -7.48472 | -46.1288 | 2025-09-15 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cc99e43f-acd1-394d-9ec7-b7a2df91b67f | -7.87924 | -43.58648 | 2025-09-15 00:33:00 | TERRA_M-M | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 399f394b-8434-3a5d-82a1-f4d25f82003a | -8.64635 | -44.03181 | 2025-09-15 00:33:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| a7544edf-aefd-3887-af30-580e7963d4d9 | -8.76642 | -46.0675 | 2025-09-15 00:33:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 330ba53c-1464-3c9d-aeca-5d11e74835ab | -11.72123 | -46.4861 | 2025-09-15 00:33:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 47dfcb62-91c9-3751-8d53-a840e173a5f2 | -11.36459 | -47.35363 | 2025-09-15 00:33:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 847a776d-0b15-322b-a408-2cd25390b2a3 | -10.72125 | -46.45806 | 2025-09-15 00:33:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| da139b85-d3b3-3135-8467-711837db2e95 | -5.12224 | -46.13084 | 2025-09-15 00:33:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 6917a5b6-3d77-3ff9-a62f-eab7f8c570a7 | -7.50904 | -44.36808 | 2025-09-15 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e333bc9f-9a53-3d62-8c67-647da8847e3b | -12.01242 | -47.77967 | 2025-09-15 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| dd1a3fb7-e585-363a-ab19-cee6b5a18d3b | -12.16036 | -47.58106 | 2025-09-15 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 200e680c-8805-3df3-940d-0d2b601badee | -7.48615 | -46.13893 | 2025-09-15 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4b9abce5-4591-3585-bc6b-baad83baa49f | -11.47767 | -43.60113 | 2025-09-15 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 3526cde0-b1ca-395a-a15d-e210e1838a68 | -5.15528 | -46.01564 | 2025-09-15 00:33:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f661a9a2-061f-3c51-8396-39114a84c340 | -11.81 | -44.70297 | 2025-09-15 00:33:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a95701a0-107f-3696-93ae-9ae9b21a69a7 | -10.92288 | -45.49582 | 2025-09-15 00:33:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 56d6a3b5-62da-3519-8635-7805b7c2bd2e | -12.66413 | -54.70407 | 2025-09-15 00:33:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 6fb054f5-3df9-39ad-a674-09b3e09e063c | -7.87035 | -43.60268 | 2025-09-15 00:33:00 | TERRA_M-M | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| bd8f54dc-5128-3c8f-b85f-1ae160ab25bd | -11.492 | -43.62492 | 2025-09-15 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 84a4b1cf-5b81-3187-b2a3-f7b684b78956 | -10.93514 | -45.51443 | 2025-09-15 00:33:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 5838248f-3266-3d6f-a576-b219de1ffaf5 | -8.96421 | -45.78308 | 2025-09-15 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 2d8527ef-2d87-3f01-b137-cba8ecc12b60 | -6.17008 | -41.18775 | 2025-09-15 00:33:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 80175b55-46ba-39f9-878d-46412837f92c | -10.7355 | -46.49381 | 2025-09-15 00:33:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1e79ee65-b4b6-3e8c-b3cf-115f5ddd2cdb | -9.23427 | -45.67179 | 2025-09-15 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a45fccbb-33b1-3bad-b503-99b9ace9d84d | -10.89734 | -48.18497 | 2025-09-15 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cb232ab9-378f-3edd-b2d1-0dfce65f7258 | -10.92544 | -45.5778 | 2025-09-15 00:33:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8c710380-256e-3225-a183-31dddfbc3258 | -8.93752 | -45.79756 | 2025-09-15 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| faf69f64-cc07-3fc2-9d0b-1ca8c0875174 | -10.73372 | -44.77747 | 2025-09-15 00:33:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9a8540e6-761e-37a5-91e6-17590dde6276 | -8.91743 | -45.46115 | 2025-09-15 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4c8dce11-0b64-3d96-9e27-548f7f589b87 | -9.01389 | -48.02319 | 2025-09-15 00:33:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 45.9 |
| c71537f2-4062-3c05-be44-20f33db2cde7 | -11.77387 | -46.66501 | 2025-09-15 00:33:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 71e3c6f0-c8e6-3b8a-ba03-8cedbf3d3554 | -10.74839 | -46.52013 | 2025-09-15 00:33:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f50ca86a-cbaf-36e2-9c1c-e6e8e40d51a0 | -7.98552 | -45.66288 | 2025-09-15 00:33:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 644ed4f8-93e8-3ea9-9e2a-d3c4df5bd9f4 | -7.52347 | -47.63988 | 2025-09-15 00:33:00 | TERRA_M-M | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README4.md)
