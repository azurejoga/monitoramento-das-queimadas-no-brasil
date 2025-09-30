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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4a7486e-331f-3ba5-8c71-adca687061ef | -13.35726 | -46.38293 | 2025-09-30 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08f033a1-e9b3-3beb-be51-77b3b2818df4 | -11.20743 | -47.20854 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9857e208-7725-3d91-a7ef-15279366fffe | -13.20885 | -50.94807 | 2025-09-30 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| b0b4bdb7-db38-37cd-b433-39e6d35a479e | -6.50624 | -45.22807 | 2025-09-30 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e490c6b-891b-34bb-a39e-444698ab2fea | -12.84283 | -46.98848 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8816d364-7fe6-3607-9899-e2c7d49ceff7 | -14.69526 | -48.23286 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d02eed37-4222-3648-a57d-6782c2986a4d | -11.64975 | -45.33197 | 2025-09-30 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a105dacb-1df3-39cb-89d2-432ce4df3a21 | -14.58917 | -48.19387 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5433f695-fdb3-301e-ad8d-527b4f25b13f | -14.7179 | -45.67494 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80348c82-60dd-3301-8b10-dd6b559c1a06 | -5.69256 | -42.60645 | 2025-09-30 03:49:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 94af77a2-5c5e-3e2a-b23c-62a361db8641 | -14.51665 | -48.01444 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4258e89c-dd35-380f-badf-b7b9a8a97ae9 | -11.96591 | -46.58438 | 2025-09-30 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9b3e47c-81b1-3762-af88-ea78ad683532 | -19.21527 | -44.07036 | 2025-09-30 03:49:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1eb3727c-fd13-343b-814a-88cc08c74c05 | -16.4079 | -43.12281 | 2025-09-30 03:49:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b4661497-f454-33b4-912f-e90557f439e9 | -13.23726 | -43.37528 | 2025-09-30 03:49:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| ba820166-8cf4-3c5d-b101-39fa55371f45 | -11.80712 | -44.91665 | 2025-09-30 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10a517b0-61f3-3dda-846b-7187aac11907 | -7.11441 | -47.78558 | 2025-09-30 03:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 67a34df9-761a-367d-acc9-dc513551fc97 | -13.24466 | -48.44183 | 2025-09-30 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09946fb3-8e3a-3264-bfb3-fb6eb05b866d | -12.86756 | -46.78117 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07640b6d-5d46-3862-9678-b35b136f4224 | -11.7562 | -44.75752 | 2025-09-30 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e00b59fb-4995-317c-ae97-311f14ecd8af | -15.92313 | -46.20431 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5fbb2c86-323a-3d6d-a887-f110681d92fd | -16.08784 | -48.11053 | 2025-09-30 03:49:00 | NOAA-20 | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16fe4e9d-0442-36fb-871c-5cd3530a8e4e | -13.81069 | -47.49944 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9578aefa-a87d-3d8c-a9c0-8f77bd5b8409 | -16.22712 | -41.73208 | 2025-09-30 03:49:00 | NOAA-20 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 4ac4f690-256d-3409-9b78-df794bf40998 | -15.47771 | -45.88368 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1ebc02c-0838-3520-870b-0b45c516576c | -14.64718 | -46.96395 | 2025-09-30 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ae7e61ef-720d-3c58-a1ce-5b3cceed962f | -11.88152 | -48.04602 | 2025-09-30 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f8ccb49d-e888-322b-b76e-bed06197c413 | -15.73124 | -48.89377 | 2025-09-30 03:49:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fc7d991a-166a-3839-b227-72df14cee356 | -13.78137 | -44.24749 | 2025-09-30 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b077099-aa68-3f29-9ece-613fc8fe339c | -13.82244 | -47.46922 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 05728cf8-f1c9-3498-9d8b-df7fabf60cb1 | -15.54835 | -44.34658 | 2025-09-30 03:49:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 66009a44-70ee-3ba3-a97f-9e581f5b8bf6 | -15.52599 | -39.8808 | 2025-09-30 03:49:00 | NOAA-20 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9df3357d-6c8e-38a2-a64b-9c4d28563154 | -6.36707 | -45.10697 | 2025-09-30 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea93b864-02b9-3e77-8dcb-ab6c02d9af55 | -14.5294 | -48.48947 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| eb452b36-0bdb-3940-bef9-c8c5b80b32ef | -6.83872 | -44.83057 | 2025-09-30 03:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6de5639e-67fd-33bc-bd46-f941b7dbec27 | -16.4212 | -47.01373 | 2025-09-30 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b8f027b-b4db-305f-9b53-86309b6a1a65 | -14.53997 | -48.26191 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8a36f135-404a-3fa1-be9e-0260ed1d03b3 | -15.71513 | -47.5839 | 2025-09-30 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8293041d-223b-3fae-a7de-846eeda2640e | -16.61073 | -43.36061 | 2025-09-30 03:49:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d403709a-8110-3958-bce6-42aa7f251906 | -14.52529 | -48.48161 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 39a34c8f-f7d2-314d-8740-7845e6f46c8a | -13.21536 | -50.94448 | 2025-09-30 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| cfab52e6-e2ee-3402-b6db-4d3c9954f3d9 | -7.05657 | -45.19883 | 2025-09-30 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9a6a8a4e-649c-3624-ae0d-8223d53c6b87 | -12.82673 | -47.00652 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0a2c4e7e-5172-3d49-85af-c7e2afb8abeb | -14.75588 | -42.50181 | 2025-09-30 03:49:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e8252110-331a-3835-92ae-b30084855f2a | -15.77939 | -43.67641 | 2025-09-30 03:49:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0889710-40c2-3490-9f1a-b03147d839ef | -17.50148 | -43.47234 | 2025-09-30 03:49:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e4e3751-cbef-3826-ae19-6ae590b3cd5a | -13.80564 | -47.96963 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55005352-90e1-36e7-84e8-60b5c7e6862b | -5.93233 | -43.4576 | 2025-09-30 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1971e90-9bc9-300d-b237-0a988ce49b39 | -11.88557 | -48.05489 | 2025-09-30 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6013c162-e1e3-3fcd-a746-dc004b043d59 | -19.19109 | -40.87882 | 2025-09-30 03:49:00 | NOAA-20 | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5ae3c466-7b71-3871-8aa7-d39efa9d56b8 | -14.7062 | -48.15085 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6772ae74-6ac9-3207-8f2a-a5021b073c1f | -5.66838 | -43.04558 | 2025-09-30 03:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 96eb134b-920b-313e-bc59-90ec0c90c4d1 | -15.39969 | -44.98043 | 2025-09-30 03:49:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50f7800b-f5c2-3991-884d-362290293fe9 | -7.28037 | -42.85642 | 2025-09-30 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| da75fe09-1059-3ab3-836c-1db5ab12a582 | -15.22773 | -50.09442 | 2025-09-30 03:49:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02f3d79e-0038-3e65-be0b-1d8359d7c687 | -11.88457 | -48.03061 | 2025-09-30 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ff1b4f9c-79c1-3065-8a5f-1476301a8c1b | -13.0266 | -42.8107 | 2025-09-30 03:49:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 89666c39-4e36-350b-ae22-1e7a50d1ad1e | -16.4191 | -47.04216 | 2025-09-30 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03de5a0f-17e0-3cfe-b04c-125cbc018dfd | -15.68975 | -46.26378 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5378a67b-37df-3931-b099-377a7d996300 | -14.5239 | -48.48846 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 05e79690-473d-31a3-b79b-9631cdb0a8b6 | -14.69316 | -48.24326 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1be9c396-03ce-37f1-afa5-18165a0c4fa8 | -12.95432 | -48.41531 | 2025-09-30 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a88818bb-1eda-31a1-bae2-4611451b5f3d | -12.89083 | -46.76943 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 8fdfe1a2-c49d-3b85-8e77-f6ccb1ef697c | -13.78742 | -47.86464 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a9213203-93ae-3265-9d7a-edf1bf1763ee | -15.29687 | -46.41035 | 2025-09-30 03:49:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c5e2877-09b4-3bc8-8c8c-6f5cb0637942 | -11.74971 | -44.74218 | 2025-09-30 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3ea3f876-8c1a-3e1d-93f9-69e0a81df53f | -14.39169 | -47.13501 | 2025-09-30 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 882f31c0-ed8d-3083-bdde-43900d13f977 | -12.82146 | -47.00624 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 21d5c8ac-b6d4-35e4-8d70-fb789a760def | -14.54044 | -48.49126 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 893d57ac-4999-3f7c-b1f4-959c6012ef41 | -6.21228 | -44.20359 | 2025-09-30 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bcebc5c1-24ee-3a63-8205-5eac697cf4ad | -13.39125 | -48.07873 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e547d41a-0460-3d21-a992-915857cebb93 | -5.51655 | -43.87569 | 2025-09-30 03:49:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0347f6d9-7013-3c9d-bbf9-a62b14725852 | -14.70322 | -45.70324 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75c6684c-94bf-302e-9c01-14249dd17fc8 | -14.70698 | -48.14698 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1567eff5-f50b-317d-a4ce-3521d20f3277 | -13.25084 | -48.43998 | 2025-09-30 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f71c904-d6d1-339d-989a-d3092242f085 | -11.64799 | -47.48967 | 2025-09-30 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 39aeaf29-b49a-3b92-b85c-5f12afa27e7b | -6.50206 | -44.26286 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 609d110d-069b-37a0-82b2-c2cd3b856b6d | -13.00919 | -49.44151 | 2025-09-30 03:49:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 040da0d2-9a92-33f2-9dd2-b48d08f45246 | -15.17375 | -46.40916 | 2025-09-30 03:49:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eb97364b-0b2e-3aeb-a448-7eae0a627723 | -13.35999 | -47.91838 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2065121d-a4df-3ac0-99b9-3daf9199e771 | -12.58668 | -41.28754 | 2025-09-30 03:49:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 462400d9-1062-304b-a11c-8bd4299985b6 | -14.38669 | -47.13382 | 2025-09-30 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb3e730c-35a2-3358-845b-5cfc24b92a28 | -15.06721 | -45.05799 | 2025-09-30 03:49:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37cecef0-2cc6-3e15-b3c0-0afc0a56c41e | -12.86942 | -46.96121 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a705a2fd-8541-3f48-89c5-d60fef417b3e | -11.97668 | -46.58301 | 2025-09-30 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54d96938-a373-393e-93c3-c1a12899eef9 | -11.88076 | -48.04986 | 2025-09-30 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a595a34e-1d43-3937-a5df-d8ccf068bb98 | -6.14667 | -43.90339 | 2025-09-30 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 349cf48c-6d01-3234-979f-a56ea6b3f148 | -11.21339 | -47.20642 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 34f5de05-d2b0-3f26-86e6-411ff4989b2c | -15.92978 | -46.21268 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 32f86059-6a40-3e71-b25c-8da295cf0fcf | -7.11531 | -47.78069 | 2025-09-30 03:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 97712e66-dcf8-3c4d-aadf-f27015f24856 | -11.65447 | -45.33272 | 2025-09-30 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb268854-c634-3109-85cf-7e9083a0650d | -16.67774 | -44.55844 | 2025-09-30 03:49:00 | NOAA-20 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afd8454f-13ea-33d6-9b49-b96235fde0e3 | -13.35829 | -47.81379 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c283874-3947-3def-b5a9-63991e3e8e0f | -16.41958 | -47.01475 | 2025-09-30 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92604b4a-7635-369d-a6a9-8d15cba395a5 | -15.169 | -46.40833 | 2025-09-30 03:49:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4fac2723-411e-3c7f-93c1-1daadf8ee7bc | -15.32503 | -43.80263 | 2025-09-30 03:49:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff7ac971-faa8-330e-808d-2edc6ee5f9b3 | -15.4857 | -48.55997 | 2025-09-30 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 76a7610f-ed54-3bf5-86d8-cbd4db936aab | -16.42498 | -47.02007 | 2025-09-30 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a84fe8e2-b639-319c-8d05-2e45a24d49fa | -14.51447 | -41.84155 | 2025-09-30 03:49:00 | NOAA-20 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e722e242-9b76-35e7-8064-fefe35ff4406 | -4.87185 | -48.88738 | 2025-09-30 03:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |


[Clique aqui para ver as próximas entradas](README42.md)
