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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ef85469-1f3e-36bc-9471-606e9ed06a6e | -22.32803 | -49.1801 | 2025-09-15 04:23:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b99a24b2-a758-3e8a-9f32-915deabaae27 | -17.16868 | -49.38391 | 2025-09-15 04:23:00 | NOAA-21 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68d962e0-7365-3836-9daa-4c2a26d8ec21 | -21.75734 | -45.49828 | 2025-09-15 04:23:00 | NOAA-21 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9f9d7592-bae9-30cf-955b-d6c598d0bdba | -22.20409 | -48.34779 | 2025-09-15 04:23:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a7081579-e464-3b2d-b61b-135be6445dc9 | -23.00924 | -47.54602 | 2025-09-15 04:23:00 | NOAA-21 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 14f30888-2aa9-3959-b7fe-2ae60645c1ef | -18.61796 | -43.90179 | 2025-09-15 04:23:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6d8d1800-04fa-388b-986d-c0e3c1dbf1cb | -20.08633 | -46.88431 | 2025-09-15 04:23:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33850239-4b9b-30a3-812f-3b37af7c0e3d | -22.18204 | -49.61712 | 2025-09-15 04:23:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 16459ce8-b912-37e3-8968-bb37f89512c8 | -20.2347 | -46.17373 | 2025-09-15 04:23:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 403466a2-9947-387d-8c55-678bd6e8474d | -17.99353 | -46.94911 | 2025-09-15 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9495a367-764f-3e74-a4d2-ad772e8a2260 | -20.8622 | -46.21555 | 2025-09-15 04:23:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 57e9c4e8-fa56-3418-9d9c-105ee02de35c | -16.67048 | -49.77765 | 2025-09-15 04:23:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7b86f7e3-a72f-3c93-bb7b-672857a50276 | -17.83355 | -50.42534 | 2025-09-15 04:23:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f8b6d17-9bd3-3c6f-bee6-297a755658af | -21.76028 | -45.50315 | 2025-09-15 04:23:00 | NOAA-21 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e46f365f-a6a4-3050-96c1-af09ac6f4545 | -21.26546 | -47.00706 | 2025-09-15 04:23:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6315aa58-2fd1-344b-9c4a-459ec626506f | -18.04047 | -46.97537 | 2025-09-15 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15de9961-3de1-3045-a7c7-89623da2b31d | -22.29592 | -47.36841 | 2025-09-15 04:23:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a347af01-6ad7-3d10-aa94-c7e5d8de6527 | -18.61979 | -47.18715 | 2025-09-15 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f41ff7ab-7436-3167-9281-ce06ed176e5f | -18.61719 | -50.39338 | 2025-09-15 04:23:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3c2d61c7-dd33-3708-9bf1-7ac0fd9a3165 | -22.29963 | -47.94832 | 2025-09-15 04:23:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65b6b40b-7d2a-32fd-a8f3-c781551a0ea9 | -21.92126 | -46.56426 | 2025-09-15 04:23:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 95843da7-79de-3bec-a092-09723bfa9372 | -18.90018 | -50.15892 | 2025-09-15 04:23:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da7090dc-836f-309f-a408-bad57aed2af4 | -21.55338 | -45.87774 | 2025-09-15 04:23:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9084f993-c916-3b3b-8355-e48eed76290c | -21.13187 | -45.94365 | 2025-09-15 04:23:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 84578896-e45f-3905-96e8-4cf67e7fcc73 | -23.01201 | -47.55043 | 2025-09-15 04:23:00 | NOAA-21 | RAFARD | SÃO PAULO | Brasil | 3542107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d6ea54b0-fbe0-36f6-acc1-3af88de4279b | -21.26248 | -45.63214 | 2025-09-15 04:23:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c136a6ce-164f-31db-ba72-4fd3f4248364 | -21.76086 | -45.52498 | 2025-09-15 04:23:00 | NOAA-21 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| eaf427b9-9324-3461-9114-c50fa5ef9df3 | -18.61735 | -43.90625 | 2025-09-15 04:23:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22731c19-49da-3bd0-bde5-1d50b7c75bf0 | -20.61761 | -50.36668 | 2025-09-15 04:23:00 | NOAA-21 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bd5413a8-9ce1-3570-b20a-76e2edbd6105 | -20.55699 | -44.91539 | 2025-09-15 04:23:00 | NOAA-21 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bcf72692-9df6-3f2e-98d3-713ff4c728c0 | -21.63295 | -46.81642 | 2025-09-15 04:23:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9c5f78a5-5cff-3451-b67b-2d56a733ab54 | -17.18282 | -48.58977 | 2025-09-15 04:23:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bc58aaf8-4acc-3371-827a-42833ea336e5 | -18.48036 | -46.94376 | 2025-09-15 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b7c1a96-2dfc-355b-8ba1-9a4f1dc62143 | -20.3221 | -58.08522 | 2025-09-15 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5ffd0b52-866c-3267-bbe5-7ebef15ba8fa | -18.67069 | -47.36366 | 2025-09-15 04:23:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6dc65880-1d7c-308b-b51d-2aef7bb4535d | -18.60047 | -47.20244 | 2025-09-15 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c101f192-1adc-3df1-b50f-fbdf61edd869 | -17.37901 | -53.25485 | 2025-09-15 04:23:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d2567dd-eac7-3d2c-b925-da304cb586ac | -21.63407 | -46.80878 | 2025-09-15 04:23:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| df25973a-3c51-335c-b7ff-d6e664c527e6 | -20.85879 | -46.21495 | 2025-09-15 04:23:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5342a60f-bca6-3436-9cb5-d7755cc642f7 | -22.20351 | -48.35151 | 2025-09-15 04:23:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5775f6f4-ceb3-38c7-8b8d-d2b928c7b5ed | -20.78948 | -46.01418 | 2025-09-15 04:23:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5684539e-5ae8-37bc-8d03-a52956960faf | -18.62891 | -47.32677 | 2025-09-15 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0e384023-ecc5-3a27-942c-c4b03000eb96 | -17.27512 | -46.10482 | 2025-09-15 04:23:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3da2fc9-fbb3-34b3-b236-beebdd129f84 | -17.73838 | -49.08649 | 2025-09-15 04:23:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7f67cc6-1bd2-3204-95f7-962c881ea822 | -22.2893 | -49.03858 | 2025-09-15 04:23:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1443a1a8-4fef-3384-b5e1-d701a918234c | -16.67818 | -49.77457 | 2025-09-15 04:23:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3c73bd73-32d0-344f-8154-a96d684d11a9 | -18.15939 | -49.19945 | 2025-09-15 04:23:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 08c3d3e4-f3b4-3451-9711-1b812d1d888c | -18.16278 | -49.20001 | 2025-09-15 04:23:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3e6cc32b-fd09-3cfb-bd39-2e942664fb3f | -18.01343 | -46.97452 | 2025-09-15 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf0be3b7-7997-368f-b8bc-7e09e8b64cb4 | -18.6143 | -47.17874 | 2025-09-15 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df77e309-b487-37e4-b85c-be1f3763407c | -20.19631 | -46.29443 | 2025-09-15 04:23:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d37571c-f740-3f58-b259-f514dee1a4bc | -22.3588 | -48.94408 | 2025-09-15 04:23:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| edb311c0-77ee-3501-955a-73915387c9df | -18.45127 | -47.2 | 2025-09-15 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dea79e72-2f0f-3282-a1a1-dce3b199f2a3 | -18.25685 | -49.4604 | 2025-09-15 04:23:00 | NOAA-21 | PANAMÁ | GOIÁS | Brasil | 5216007 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a276b650-3366-3af0-829e-219f503573c6 | -18.02722 | -46.97314 | 2025-09-15 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3656d479-ddc8-3872-b05c-2940a601886e | -17.14507 | -48.52589 | 2025-09-15 04:23:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ea5c9cc-37e4-32d4-a0d5-7e1fd6487aff | -20.04686 | -46.16432 | 2025-09-15 04:23:00 | NOAA-21 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7aee98bf-cf75-361e-a062-12d0ff2ddd49 | -21.92523 | -46.56084 | 2025-09-15 04:23:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 629bb422-41e4-3e12-a9a8-ab0f42a4f00b | -17.43458 | -49.22481 | 2025-09-15 04:23:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7d61854-7101-390a-a989-49d6af01d105 | -18.15537 | -49.20278 | 2025-09-15 04:23:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cddde074-2619-30c5-bea1-4b41904e74dc | -20.52016 | -45.35868 | 2025-09-15 04:23:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c99f7e9e-9fef-3afc-83e7-eaff4ad6c40e | -20.82289 | -45.6007 | 2025-09-15 04:23:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1d2eef4-ed95-3ddc-882a-6aef164a3d77 | -19.71743 | -45.44143 | 2025-09-15 04:23:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78f09c45-d074-31a7-bbde-d91712e1b186 | -22.26248 | -49.56585 | 2025-09-15 04:23:00 | NOAA-21 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cda0c466-ee97-3220-9cb5-63a11d274f9f | -18.62106 | -43.90665 | 2025-09-15 04:23:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e24f52d6-ae23-35dd-8d06-95377a366eaf | -20.23755 | -46.17812 | 2025-09-15 04:23:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b8d60687-4cda-35d8-a100-a1ea06ae628d | -17.31585 | -46.10765 | 2025-09-15 04:23:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93a8e385-8791-3698-b68f-f00271531229 | -20.51897 | -55.63536 | 2025-09-15 04:23:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 95271a04-8806-352f-8a4d-cf089a36e58c | -21.76244 | -48.1262 | 2025-09-15 04:23:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4873f42-1f73-39db-98df-2258157d6a1c | -21.09976 | -47.99183 | 2025-09-15 04:23:00 | NOAA-21 | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51bea4c7-bcad-3a2e-bcb9-405d670526d5 | -18.8974 | -50.15424 | 2025-09-15 04:23:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46593fc0-d28e-3f27-bf17-e48db98d5b9c | -21.92237 | -46.60469 | 2025-09-15 04:23:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7d25f7d5-c925-321d-b0ab-45cac03ed5e6 | -20.52256 | -55.64137 | 2025-09-15 04:23:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 289a8a09-49bd-3d7f-a724-629e71446fbf | -17.139 | -48.52099 | 2025-09-15 04:23:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a57982a7-6e47-3d52-ba46-4196bdce80c4 | -22.20682 | -48.3521 | 2025-09-15 04:23:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e28ca08d-3171-3d91-b86f-a2b9584b6f63 | -18.63165 | -47.33096 | 2025-09-15 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ea08b94e-f9c8-3b4f-bad9-4e3e2ee8faef | -19.74422 | -45.1258 | 2025-09-15 04:23:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3d17acf2-6f50-3d86-b6a1-31dbc9def7a3 | -21.92637 | -46.55296 | 2025-09-15 04:23:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f32665da-ceec-3211-b91a-033711f51dcd | -17.83426 | -50.42116 | 2025-09-15 04:23:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd63058a-e904-317b-ad95-8176a82ebfa5 | -20.32689 | -43.67816 | 2025-09-15 04:23:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2dd78416-9847-340d-b0da-fc9ae3137b9d | -21.63013 | -46.81206 | 2025-09-15 04:23:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 22d58d98-5962-35c2-9505-36a9f18008f2 | -17.72783 | -47.95209 | 2025-09-15 04:23:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 086e582f-55c0-3a03-a3ed-c33817863374 | -18.37288 | -49.26921 | 2025-09-15 04:23:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a39402de-843c-3908-8611-b6b603fb77c6 | -17.61715 | -44.17533 | 2025-09-15 04:23:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a008657f-0774-305f-8103-fe4d6af65cf1 | -22.20955 | -48.35641 | 2025-09-15 04:23:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64b654c0-eb91-3f01-84eb-c667e1d062fa | -20.85823 | -46.21888 | 2025-09-15 04:23:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03746ccd-763d-3093-b6ab-2142c5ecdd98 | -18.61761 | -47.17932 | 2025-09-15 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 380cafe5-408a-348e-a1ad-73a4bc5b395e | -17.40664 | -49.26357 | 2025-09-15 04:23:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b48312e-44f8-38f8-aa5a-15529d258f6e | -17.83072 | -50.42054 | 2025-09-15 04:23:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a24cceb3-43cf-37ee-8acc-c2788aeda141 | -15.79383 | -53.50691 | 2025-09-15 04:23:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 03b2965b-0ea3-39ec-b869-903bff70b76a | -16.6747 | -49.77392 | 2025-09-15 04:23:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5d2c5a4e-5c2d-3703-98d3-8e254ab3f4c2 | -18.95916 | -48.21349 | 2025-09-15 04:23:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a90aab38-6cb4-3c17-b2fa-4083a8510c1e | -17.14173 | -48.5253 | 2025-09-15 04:23:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ef65ede8-a037-37d4-b1d2-ace40f698a74 | -18.97797 | -48.58484 | 2025-09-15 04:23:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b8fe0e9a-acdf-3a53-b96d-331af6f8bf8c | -18.89326 | -50.15763 | 2025-09-15 04:23:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d022da80-d4c5-314b-a861-a63d52114e56 | -17.43523 | -49.22095 | 2025-09-15 04:23:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f299de4-55b0-3b88-9aa8-1bf4a1078f16 | -21.26289 | -47.01059 | 2025-09-15 04:23:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee15f6d4-b4cc-3f31-895d-c7e55993e1b8 | -17.16164 | -53.23143 | 2025-09-15 04:23:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb02ed8e-3d3b-304d-a899-d9b139c3da80 | -20.73856 | -56.74228 | 2025-09-15 04:23:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 02ad4778-4557-37f9-87c3-b04a7ac2dbcf | -17.82454 | -47.77224 | 2025-09-15 04:23:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README36.md)
