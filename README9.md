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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a058c1e-e053-36be-924c-9d34a292cd79 | -7.62084 | -45.18612 | 2026-07-31 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a47e4f07-d2e8-3f91-a1d0-f0794434bac5 | -12.8521 | -44.39598 | 2026-07-31 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 834287b7-8ea6-389a-aa12-39d24512f954 | -5.80691 | -43.63728 | 2026-07-31 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a041981-9176-34bb-aa29-e9e6675fd600 | -12.6097 | -44.6069 | 2026-07-31 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bdb57bfa-77e4-3efe-8e8a-1b51668ec42e | -11.29383 | -50.39666 | 2026-07-31 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dde4b3ba-2d08-31ee-99c0-9232905899a8 | -12.60971 | -44.64148 | 2026-07-31 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93144707-b3aa-3c42-9403-4ef1367edee5 | -11.83302 | -45.60514 | 2026-07-31 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a133667d-44e5-3421-875e-1017a83f4119 | -4.21684 | -56.04576 | 2026-07-31 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7b2f073-05fa-3b73-8a0c-b84865e7fd7b | -9.45704 | -50.31288 | 2026-07-31 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5fce907f-cba6-38fd-a4f7-72bee3fcc5bf | -11.16565 | -49.42048 | 2026-07-31 04:40:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95443133-56e8-376f-a3f4-09708228fdb6 | -11.7419 | -48.90664 | 2026-07-31 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38323e31-eb43-3078-96a6-72af5570e450 | -7.00897 | -45.84806 | 2026-07-31 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0d53734c-cacb-33dc-9789-8e13f0ced935 | -6.55722 | -55.15723 | 2026-07-31 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b537857-5cf5-3821-932b-fc46ff750568 | -12.61951 | -44.59957 | 2026-07-31 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 062fd6b9-e707-33b8-99e8-81112423b711 | -7.41004 | -49.52557 | 2026-07-31 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 586fbda7-3517-358c-af99-6c3d563badfd | -10.63442 | -47.48957 | 2026-07-31 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 06810150-89ee-3bb4-9c0e-65b7b9b7233a | -11.47289 | -50.16254 | 2026-07-31 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28abf5ef-cd3b-3350-af53-3b5b379005f5 | -9.17183 | -49.6757 | 2026-07-31 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 594d7007-4171-3547-b32e-b5e03ca0af09 | -5.72214 | -48.12548 | 2026-07-31 04:40:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8be5c6d4-6d53-31c8-aa98-fd4338f7eb5d | -11.29329 | -50.40016 | 2026-07-31 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 202c8400-f270-3e26-a923-dd86ed80a36b | -7.01372 | -45.42179 | 2026-07-31 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cd39dcc-965c-3a83-9b91-89fa1b09e7c5 | -12.85269 | -44.39159 | 2026-07-31 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 89a40e7e-d60f-3aab-90eb-aa2c02154d80 | -11.46779 | -50.10766 | 2026-07-31 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4b73a74-0193-35ca-9b35-db4c6f904dd1 | -6.5436 | -55.15539 | 2026-07-31 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4a7ffcd-8a82-36a3-92aa-cd72e9d22ba0 | -8.98065 | -45.1709 | 2026-07-31 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a64cea95-264f-31c3-8b6d-eeae6ed8414d | -4.21607 | -56.05051 | 2026-07-31 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 36f3315e-0988-317b-a080-61400430fc38 | -11.92864 | -47.63742 | 2026-07-31 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80e60d20-c13c-3eab-9cdc-b5122fb85224 | -7.40674 | -49.52505 | 2026-07-31 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8050aafd-dab2-3129-b3f0-38896c41b1e1 | -11.42964 | -50.09079 | 2026-07-31 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 536adf09-8aaf-3a0a-93b8-43de9956579c | -12.6108 | -44.63298 | 2026-07-31 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b97a9cb4-56f7-3091-905c-e79511a94346 | -8.47544 | -51.54496 | 2026-07-31 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbc0a480-6766-3d78-9317-989e528a2155 | -14.39662 | -48.06509 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 53cbae36-a701-31e1-850b-f844325c611e | -17.61262 | -46.65589 | 2026-07-31 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 04338e9d-20fe-31e8-ad6f-8115e275b0f8 | -14.40932 | -48.05375 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d81b0ca7-cbcd-3dfd-ae2f-e48c02eaf386 | -14.37905 | -48.05895 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 066ebe59-37e7-37e1-94da-fb3a3703c867 | -14.36155 | -48.05241 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5251e841-d7f2-3151-b1c8-cc70b8b97978 | -18.02309 | -44.37215 | 2026-07-31 04:42:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d27cbbd7-2064-320c-8396-4a02b609828a | -14.37422 | -48.06699 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a7b2e805-4193-3508-ada7-61675a0b79af | -14.83652 | -48.52002 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 722f4665-41f7-3f16-8d66-3e0ce1b5509d | -14.28308 | -47.42279 | 2026-07-31 04:42:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7fddd64-0ce2-310e-b1b2-0b092ac05594 | -17.53337 | -45.30212 | 2026-07-31 04:42:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 17f7bb01-9027-3077-ba8f-59a85484167d | -14.23624 | -47.48545 | 2026-07-31 04:42:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e65214e-92f3-3924-a094-90168e2f66cb | -14.39964 | -48.06976 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| de96e840-b88e-3c52-8744-6a932fa7dea6 | -14.05359 | -46.22124 | 2026-07-31 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c3d8aca-6777-3368-ba1c-f24d0c5745fc | -17.54168 | -45.34512 | 2026-07-31 04:42:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7886a9f0-8e83-3c3e-8b73-b70093376814 | -14.38087 | -48.072 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b5a27180-b543-3370-bfa3-1472864e67f6 | -14.37968 | -48.05454 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4389c371-3310-3823-a0e6-9672ce301790 | -16.4049 | -54.84801 | 2026-07-31 04:42:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 176a5fa5-c1df-3cc7-955d-4c498a4787ce | -14.40213 | -48.02677 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16636779-10a7-37ab-af13-6bf200bfda6e | -14.77868 | -46.80561 | 2026-07-31 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1d00a90-4e8a-356a-9405-d5d38d247072 | -13.70092 | -47.52288 | 2026-07-31 04:42:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 720dbb48-6f0b-36a1-9a55-e7f7603e1e8f | -14.23997 | -47.48587 | 2026-07-31 04:42:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f13b86d-f958-318b-8896-16fd788c036b | -14.35071 | -48.05079 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de335e94-376d-3077-9500-b4367ea82d01 | -14.40693 | -48.04475 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e64f07e-85d5-31d9-9a2d-16cbfea68a1c | -16.40245 | -53.33971 | 2026-07-31 04:42:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6f0ae68-ea5c-3fbb-8892-fc6544881726 | -14.38451 | -48.07231 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 34cb66b2-f5c3-352a-8864-3a00cbdd98d1 | -14.40516 | -48.03137 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48840c3b-044b-3921-adb7-a12c2486e90d | -14.38571 | -48.06397 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 7c7c337d-5f8d-38e1-bedd-6837cf45c361 | -18.37524 | -47.20236 | 2026-07-31 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ee93ae7-25d3-3385-acb4-c7a4e2b58148 | -16.40366 | -53.33226 | 2026-07-31 04:42:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c88a196-373e-3eb9-a88b-ca8b4e1abf4d | -14.28484 | -47.42117 | 2026-07-31 04:42:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f7db170-6419-3570-9144-7676b3b3946a | -14.83356 | -48.51538 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b7eda37-eb55-3424-a254-95e32ddea109 | -16.55957 | -49.05245 | 2026-07-31 04:42:00 | NOAA-21 | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 99e8caba-0662-388e-b19a-d9cf8bfd18f5 | -12.19984 | -52.8645 | 2026-07-31 04:42:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d09de77-bf32-3bf9-b26d-f2be4d2eaa04 | -18.12391 | -44.6423 | 2026-07-31 04:42:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2285ed61-d327-3796-bbd8-e7c7f7bf8df7 | -14.40153 | -48.03093 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe8cb8c0-5a64-34cc-9b5f-0e8fdb5d7aa3 | -14.36819 | -48.05756 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56369d93-56b7-3c46-ae87-0a7b9f43ffb1 | -14.37784 | -48.06747 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8e13a654-387b-3992-bf19-8b52167c0f70 | -14.38331 | -48.05499 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9f54f97-4c13-3459-840b-8c996a233f78 | -13.96191 | -49.14622 | 2026-07-31 04:42:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e62680b-77ab-3941-9a14-354aeda321b1 | -19.1595 | -47.3176 | 2026-07-31 04:42:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bb08f3e-cc8d-311d-987c-19d597cdb4b4 | -13.41843 | -51.51059 | 2026-07-31 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 699a7af9-cff9-316f-a35e-0494a265395f | -14.39722 | -48.06086 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| de48f598-1401-35dc-bc07-81edcb42da11 | -16.40029 | -53.33168 | 2026-07-31 04:42:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd8baaf3-16c9-38c4-9ecc-3bb629653b59 | -14.83596 | -48.52395 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a2f7eed1-e3bb-38b3-b9f2-51f52e7c2df6 | -14.36457 | -48.0571 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7b7edc8-8c6e-33cf-a0fb-e354938b0c6e | -15.62888 | -48.89105 | 2026-07-31 04:42:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d2ecb1c-11a3-3462-8e75-2e3cfcad8f8b | -14.06606 | -46.21943 | 2026-07-31 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d3837a1-863f-36d5-911e-18bb0dfee239 | -13.95792 | -49.1495 | 2026-07-31 04:42:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 313df7e7-6f0a-34c3-9c2f-76a9ff2b9115 | -14.05759 | -46.22182 | 2026-07-31 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c9c5a7e-48ae-3a1c-841d-c4bee3191894 | -14.36276 | -48.04385 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 678a64f9-6bc1-3ce9-9137-2471ae270916 | -14.39601 | -48.0693 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cea89034-4627-3aed-a475-3c57acd0313b | -14.07005 | -46.22001 | 2026-07-31 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e1f04d2-e9e3-37f1-aa66-8b639e9decc0 | -14.83242 | -48.52332 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 85873429-122b-3970-ab02-a1c53cfd0584 | -14.83185 | -48.52734 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 681421b7-b4cc-350c-963a-939d5190ebec | -14.37605 | -48.05412 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f185d2a1-32a8-3730-9068-b1185f6f1f98 | -17.53281 | -45.30671 | 2026-07-31 04:42:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 88af8d49-b1a4-3647-8b5a-20e28ac6ef6c | -18.3674 | -46.51824 | 2026-07-31 04:42:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cd9ce0b3-658f-3913-bb14-c34a114ab59a | -14.38334 | -48.08051 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d6d971eb-ac5f-3cb0-bbc6-5271f16787f7 | -14.37486 | -48.03661 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e097963b-e448-345b-9bad-b24154e3c27d | -15.54367 | -56.02829 | 2026-07-31 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04c630f3-831c-3010-8bb9-583c445deb9e | -14.38935 | -48.0643 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 183cab76-bd65-38fa-9232-81ca9044e481 | -13.95848 | -49.14568 | 2026-07-31 04:42:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9949d18f-1c97-3f7c-a870-3515a3902ccf | -14.38875 | -48.06849 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c4d9af0-49da-3950-81f7-2504e4cb3b30 | -14.35915 | -48.04332 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba9938fa-122e-3d19-8ecf-8b3216b6feb5 | -14.38511 | -48.06815 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 6494651b-9a68-3e18-8f10-03e144ebca61 | -14.38147 | -48.06786 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 85493fc6-d783-3084-ab2d-1e8fa49f98fd | -14.37481 | -48.06284 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 24aeaf9a-33e0-3512-89f3-f5979ed68c79 | -17.94129 | -44.32537 | 2026-07-31 04:42:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89526c11-615d-37d3-a50c-1ecea2f523cb | -14.35734 | -48.05604 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README10.md)
