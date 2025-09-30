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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44c687f7-294a-3c8f-913d-0c832914c313 | -14.72156 | -45.2077 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 569ac25b-9600-3e22-a249-d527028fef43 | -11.26149 | -47.23073 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b68a5e48-cbe3-3c37-9b16-f9753a2e72d4 | -14.79471 | -48.30591 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7cb6f13f-6fd7-3404-bfcc-ae28d93a8594 | -16.73248 | -43.11396 | 2025-09-30 03:49:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31f81aab-b330-392e-b1f4-18cb7dd3f498 | -12.75082 | -46.84931 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b243fe7-bb17-355d-9e7e-eac9d61829c0 | -12.82428 | -47.00159 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6bd65744-8b24-3703-88e6-f51670a99b7e | -15.53192 | -44.34332 | 2025-09-30 03:49:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7ac160d3-ae21-3a38-8443-768b4f5bb4d6 | -16.42507 | -47.03742 | 2025-09-30 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2bd0a071-c799-31dc-88ad-56b540b5c235 | -13.59937 | -48.03805 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52429a02-695b-3540-aebc-b785df6a2811 | -14.70359 | -45.25439 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fa809851-9fb1-3a74-9043-1a52baa6af2b | -16.16235 | -40.68156 | 2025-09-30 03:49:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0c9a3e95-b14a-35c9-98e0-29f2970adcd3 | -13.86298 | -44.41722 | 2025-09-30 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e90140a6-ee67-3d02-9176-5eafd04270bb | -18.86109 | -41.13016 | 2025-09-30 03:49:00 | NOAA-20 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a0688e6c-5f74-3f36-9017-ea2f647d1b54 | -5.51568 | -43.88074 | 2025-09-30 03:49:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8e402f43-eb63-310b-9110-3f711cb08395 | -13.60446 | -48.03428 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22fd9bac-e78f-3b8d-902a-a1f122ae07a0 | -11.70633 | -44.4368 | 2025-09-30 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bdc755e0-7e95-3ecb-b037-ad6b29e4ebf9 | -13.65908 | -43.35779 | 2025-09-30 03:49:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 476c58ef-f3ea-3ae1-adb8-f14ec632e1ea | -11.88634 | -48.051 | 2025-09-30 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 939f1a12-31a1-3928-b5b3-94ce61b618a1 | -15.20954 | -50.12181 | 2025-09-30 03:49:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 40cb2e8d-c215-3056-8824-ae1a5472a921 | -11.80424 | -44.90548 | 2025-09-30 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 139c79da-b65b-3eb0-ab57-1cee919ff88c | -13.81516 | -47.47617 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f10c23a0-c99c-3e29-bcfc-eb74e301cde2 | -7.29387 | -42.87051 | 2025-09-30 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1e88f798-ff8d-39f1-a6f8-3b82423ab70d | -12.00036 | -46.59684 | 2025-09-30 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9eb7d1f2-d815-35a6-9f0a-8f076f66fb37 | -14.70299 | -48.16684 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 80261076-e691-3248-a0d6-f639936410ee | -5.62778 | -42.83395 | 2025-09-30 03:49:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 7df37384-bc20-3269-8117-09a797a9864c | -11.88161 | -48.0269 | 2025-09-30 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2e28919-fe90-3375-b126-dd8f0a0adf46 | -15.92521 | -46.21154 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5a63c6ba-cd75-34bd-8701-187ee6e52c32 | -14.72406 | -45.66856 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a80de1eb-cf44-3a70-a9f5-30cd508632d8 | -5.90922 | -43.70428 | 2025-09-30 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 24dfba74-aff1-3860-aa4e-b06875d0687c | -14.72949 | -45.66483 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| eda55f41-0faf-3744-ac38-927ad888dc67 | -6.45648 | -44.00687 | 2025-09-30 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 404d5a4c-b938-3d37-be4b-2b3a3a00bf83 | -14.74398 | -45.66294 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35fa4aef-3727-3510-95cf-67ed7fe794ad | -14.38564 | -47.13917 | 2025-09-30 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35a81add-171b-316d-8c9d-b62e51eee43b | -11.71516 | -44.43847 | 2025-09-30 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9f4b660-a5cb-3d91-be42-7e28a5329409 | -15.27836 | -48.0325 | 2025-09-30 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd3bf7c9-1f99-3314-873b-7fd2ef84b8d6 | -11.69461 | -44.47577 | 2025-09-30 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a1c24df-be9e-369b-bf38-e3b4087cab03 | -13.23532 | -47.30982 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a45bc22d-9437-3ef1-b1a3-68e400d3edac | -5.72756 | -43.96344 | 2025-09-30 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 92b955b1-4718-326a-aa61-4b7b59c9b2e9 | -15.27446 | -48.02474 | 2025-09-30 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44921801-515a-325c-bfa1-8fac0b5b7139 | -15.27117 | -47.85325 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfcdbf23-6af9-331a-8f58-b7d958fdc127 | -15.90337 | -46.22519 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a335e049-90be-34f7-a266-11c2cedf23ac | -15.55047 | -44.33507 | 2025-09-30 03:49:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a53c3cbc-1a12-327f-ba0d-c84f4d6e35db | -15.32985 | -47.38764 | 2025-09-30 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49043e68-1048-3c6e-9f82-cb446096e2fb | -15.53292 | -42.65849 | 2025-09-30 03:49:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0054106c-0858-3cfe-b3e0-4c91e612badb | -5.21675 | -45.22797 | 2025-09-30 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5ec13a5c-48be-37e0-90ce-78ee290a6a43 | -11.75788 | -44.74841 | 2025-09-30 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 63c06c8f-b959-3c1a-a675-57c577559f7c | -14.57687 | -48.28271 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0beabd5-b480-3690-aade-860f050c3307 | -6.3817 | -42.91309 | 2025-09-30 03:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ee61348e-2615-3bae-ba3f-16bff6fb7618 | -15.38684 | -47.06947 | 2025-09-30 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 590daf6a-1123-3424-9b86-c4b286612e83 | -15.49036 | -48.56475 | 2025-09-30 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed05aa9a-fcc4-38b2-8d04-15a3a801d9c8 | -16.5789 | -45.1054 | 2025-09-30 03:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bc62c80-2f08-36ec-ae5c-6db04be2678f | -7.03994 | -46.41649 | 2025-09-30 03:49:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80bc02a2-71fc-33a7-84ae-42afddc06b7e | -6.15139 | -43.90398 | 2025-09-30 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0cfb04a6-1956-3108-aa83-c778d00d7aa1 | -4.95564 | -47.60759 | 2025-09-30 03:49:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b1a5453f-1c9e-389f-aa18-46c3987bb9a1 | -12.83808 | -47.01276 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2436526-1416-376f-9c08-8b8b24e21c14 | -19.12577 | -44.76077 | 2025-09-30 03:49:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa9ec481-e073-398c-a637-a9c64b4eb9b1 | -15.54416 | -47.87117 | 2025-09-30 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01c04a05-c12a-3f5c-b10b-922c5be9dd44 | -7.01105 | -44.4763 | 2025-09-30 03:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9edf2fa1-227a-3469-be18-5307a0aea059 | -11.88301 | -48.0385 | 2025-09-30 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1e0b8532-cec4-35b1-ac11-56d116493b53 | -6.38677 | -42.90966 | 2025-09-30 03:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 92ae51e3-cc5d-35d8-b589-e408cfae93a7 | -15.68822 | -46.26031 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e441bc0-059e-33e0-8ebe-4ca0ab34e539 | -16.05836 | -51.03394 | 2025-09-30 03:49:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5c2a154-a2ab-31ce-92bd-c4ca16fa9c59 | -5.75026 | -42.66919 | 2025-09-30 03:49:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f7711372-f77e-3eff-95bf-48f513827520 | -14.51285 | -48.42834 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 65028a7b-b8e4-3369-b6b0-a7470e49a03f | -13.57489 | -48.09919 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6b16b92-9e62-3694-aa7d-bb812c6c90e4 | -14.53407 | -48.23486 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a923894-fb5c-313c-85d1-34eb32499c71 | -14.51517 | -48.39181 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cc3c12e6-827e-3279-917a-69db397a4246 | -13.81166 | -47.49604 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1c1d371-3535-3990-b8f0-19aa5a5f63eb | -15.48495 | -48.56367 | 2025-09-30 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d19ec80-fcc9-3322-a3c0-57a910be8dc3 | -12.75447 | -46.87183 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c21ad99b-fd00-365a-af2d-7b44eccd2280 | -5.76982 | -43.83042 | 2025-09-30 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ccac5b2-f366-315e-8d89-17974fe62224 | -14.70665 | -48.23181 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8315ac92-28ab-3301-a3d9-f8225c367cc4 | -13.64253 | -48.04745 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 953f9b49-ba6d-3132-ac1c-9e6c7cf8cc06 | -7.0212 | -45.22226 | 2025-09-30 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ece518e5-5d51-3f19-93cf-15ecd738d996 | -6.36798 | -45.61702 | 2025-09-30 03:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 567e9c74-2629-36a1-b56e-768e5cea06ff | -6.64575 | -37.37423 | 2025-09-30 03:49:00 | NOAA-20 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 68d2c843-0d3a-3d19-94b4-8f1782f7f04c | -13.66071 | -44.31044 | 2025-09-30 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83c2f955-e0d1-3948-87fd-c12a6c7b4cc7 | -13.2172 | -47.31951 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d46ee107-2385-3665-b795-c23b84ea9384 | -13.60554 | -48.03539 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 055c951d-797c-3805-be7e-89bd4db079c9 | -13.78328 | -47.85758 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ffffcdd-e33e-315a-b65b-a7304d2736e1 | -15.3954 | -44.9796 | 2025-09-30 03:49:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09df2ad2-53e2-370f-b39c-930d87ce1ef8 | -13.01094 | -49.44458 | 2025-09-30 03:49:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a89d3f0-269b-33a1-a713-7fd14f1bc128 | -15.27296 | -49.49832 | 2025-09-30 03:49:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fbdf6920-02eb-3373-9c77-13e1d9bc97aa | -5.71286 | -42.83741 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 44fc8ca7-1804-3bde-b490-ff31d5c4cf95 | -11.80806 | -44.91038 | 2025-09-30 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c71bfaaa-292b-31f5-aa80-75ce9ea89d93 | -13.38121 | -48.06926 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0cb519d1-ebf0-3baa-b57b-b5c47b279d28 | -14.53546 | -48.22784 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ccaa2ce-491b-389a-984e-dab587eef579 | -7.11614 | -45.53511 | 2025-09-30 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f890e70-560c-38d5-aeb6-7822ee08f08f | -15.05033 | -46.96685 | 2025-09-30 03:49:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0f22b7d-42b4-3ca8-885c-ccd11b5eb870 | -13.82128 | -47.47499 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f2a5d0e-002f-37a3-a744-7f839b9ffa89 | -11.93934 | -43.92349 | 2025-09-30 03:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91112cfe-e348-3c2b-857c-a35b20c5aa11 | -15.20023 | -49.55948 | 2025-09-30 03:49:00 | NOAA-20 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f70184a2-62a6-3257-81aa-c3c8a20adec7 | -6.03839 | -43.82126 | 2025-09-30 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41bd3f31-dc65-3b57-b562-3d9b6b699f1d | -12.95971 | -46.40685 | 2025-09-30 03:49:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3126fac-4dee-38bf-9f88-d8868df23689 | -15.54976 | -44.33892 | 2025-09-30 03:49:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6b4c44ea-a722-333e-b708-83c8877ce933 | -15.6789 | -46.25865 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 087f1c9b-9510-3a46-96d9-24629d52287e | -6.30164 | -43.44279 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09c7a81b-f2eb-3a27-805f-e7ab504f3e52 | -14.51571 | -48.44477 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 403993c7-63aa-33e5-9076-0fc86d0bf63c | -14.56685 | -48.22122 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c01e841-2bcf-3c02-a02a-05023d07f00c | -17.40007 | -47.13837 | 2025-09-30 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README37.md)
