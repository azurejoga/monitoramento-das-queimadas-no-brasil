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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecbd95c9-e8e2-3a14-92e1-ecdaea8d03b4 | -11.45957 | -46.60022 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 851578c8-9978-37ef-b443-7e2d9a79593f | -12.74603 | -48.4325 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| deb86ee2-de4a-3361-b520-a138948d1a25 | -12.44589 | -46.65324 | 2026-08-16 03:55:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a924a2f4-bcba-3126-b965-c75bee191641 | -11.88507 | -50.62083 | 2026-08-16 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f4f16392-6efd-3aa4-b70e-224b451ebfcf | -13.5061 | -48.22173 | 2026-08-16 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 24b3b04c-1a93-3e3b-a45c-1cb7f2661d8d | -15.54071 | -47.39184 | 2026-08-16 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 733982be-6ebd-3235-9893-f1b72957ed28 | -12.69728 | -48.48175 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5199476a-b6ba-3067-a68a-20275bfddadc | -9.10264 | -46.38716 | 2026-08-16 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6308ca6e-53db-3786-bd29-fd0588d33269 | -11.47614 | -46.59503 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33798c03-379f-36ad-a396-5b45d5e3e8b1 | -11.07826 | -47.25208 | 2026-08-16 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8590907a-58db-385d-bdf4-8f9903182d2f | -9.11287 | -46.3897 | 2026-08-16 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd38fa51-2b91-3794-af11-9e38fec497be | -12.47061 | -46.65836 | 2026-08-16 03:55:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 394f35db-cfe4-3dbf-8549-857ba19b5c6b | -14.48943 | -45.68439 | 2026-08-16 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca5e3276-662c-3306-9afc-7d9354b1c223 | -12.89499 | -44.60414 | 2026-08-16 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 776b2aa1-27aa-34bb-9036-53b97bd44d7c | -11.43493 | -43.92001 | 2026-08-16 03:55:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce1af72b-81bd-397f-821f-8f2c31ec6aeb | -12.69648 | -48.48581 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddc479ad-e745-31c4-bb5b-8c5beb45bcb7 | -14.48495 | -45.68349 | 2026-08-16 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2a3c432-3b12-3d36-b8de-fa68ff720b73 | -11.87867 | -50.61943 | 2026-08-16 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0dbc0c97-0bad-3a3f-b9c3-b132b66e4c47 | -15.0641 | -47.03005 | 2026-08-16 03:55:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34a0f579-7da6-3fa3-9a33-373fc9764405 | -15.04801 | -47.01909 | 2026-08-16 03:55:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1f948a3f-5add-3174-89f4-e70d6977293c | -13.49271 | -48.23279 | 2026-08-16 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b69270cf-820c-37ae-b0d8-bdf67eda9938 | -11.45675 | -46.61548 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f25051fb-888f-3471-a4e9-4451dccb3e3c | -11.43564 | -43.91605 | 2026-08-16 03:55:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad48d1c3-9b4a-3a9f-9bb8-478bee1fa679 | -15.16483 | -50.07122 | 2026-08-16 03:55:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4f8b7cab-b4e7-32dc-9145-869056f8463b | -11.48006 | -46.59748 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 98767163-b928-36cd-b063-f64fd4d79ea0 | -11.47622 | -46.59036 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a0931457-7695-31ee-ba2e-a298054fa84a | -13.38594 | -41.33025 | 2026-08-16 03:55:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b1cce2ec-8104-39fb-ad19-b73cfdbad475 | -10.27376 | -48.29396 | 2026-08-16 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6a0ffa95-db50-3050-9e6d-040b2b2f1c03 | -13.68842 | -46.24993 | 2026-08-16 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6af3408d-f82c-3073-96f8-fbc7d0a12bad | -12.69169 | -48.48077 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a69591d-0881-3793-b763-d2c011498d3e | -10.52369 | -44.84996 | 2026-08-16 03:55:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1a38ad47-4997-31ca-80ce-084db87c8945 | -15.09702 | -48.71625 | 2026-08-16 03:55:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b93c1cd-fa2c-3264-a2a1-29bac88b56f1 | -14.4 | -51.88382 | 2026-08-16 03:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4dee4100-8d6a-36cd-8847-4cc95d7daadd | -14.29085 | -47.19077 | 2026-08-16 03:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7498132e-f871-3bcb-b7d3-257f55439142 | -11.80481 | -51.78885 | 2026-08-16 03:55:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da2af384-369d-3ff4-ba5d-696d5a03c93c | -14.93406 | -46.61325 | 2026-08-16 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| faa96904-8baa-38a2-98e1-a104429621af | -12.67335 | -48.45674 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd410a66-1d88-31e3-8012-cecbdca7a972 | -15.57161 | -42.36586 | 2026-08-16 03:55:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b37d8415-fb0b-37c2-b7a9-89f2086c5d04 | -14.90159 | -46.65004 | 2026-08-16 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4ea79ffc-375c-35d1-8d5d-4bce4dad7a12 | -14.29195 | -47.18496 | 2026-08-16 03:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b2c2a38-304a-3ddf-863c-07fed9cd18f7 | -12.72157 | -48.46804 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c1d549e9-b0bb-3d78-af71-c68db1f9bdfc | -13.43489 | -43.85429 | 2026-08-16 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5bc6a11-043b-3347-bf93-1dbfff5be0cd | -14.47872 | -45.69182 | 2026-08-16 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3755b903-0210-3bea-8e00-8824f1a4497d | -15.17169 | -50.06767 | 2026-08-16 03:55:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| be5836a3-b499-30c5-89df-2b67be6a5858 | -11.0678 | -47.27829 | 2026-08-16 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0462e710-c3b6-3557-9c94-2a60bb703fe8 | -9.6073 | -46.04623 | 2026-08-16 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5169eb3-5029-3a4b-8220-5a8f6479948d | -11.91096 | -49.3378 | 2026-08-16 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 816bfd6e-ec54-3383-af04-e6626436d06e | -12.43962 | -46.657 | 2026-08-16 03:55:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6df134e-8e96-36a1-bf52-0ca2970657be | -10.27458 | -48.28981 | 2026-08-16 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 43815b6b-4bc4-37d7-bfcc-76c3cb55c364 | -11.5767 | -46.79604 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6dda2764-ba1f-35f4-81dd-25e247fd70e7 | -14.48408 | -45.6881 | 2026-08-16 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2260a00f-5b0a-331e-91dc-e826f657abc0 | -14.37644 | -51.89687 | 2026-08-16 03:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a53994c2-20c0-35e5-bcad-6eb8290fa841 | -12.66775 | -48.45588 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a1e10dd1-ed7b-3c17-966f-fe99051664fe | -12.69807 | -48.47771 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8527c01a-4279-39dd-a81c-ba8af355bd26 | -14.39641 | -51.88668 | 2026-08-16 03:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f327313d-f4b8-36e8-a0ac-9600fb48310b | -12.74704 | -48.43327 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5482dca8-06f6-3f98-ad85-8a0e7707dba3 | -11.90021 | -45.97025 | 2026-08-16 03:55:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91fc6892-0937-3df7-b45d-45cedf3d5d5d | -13.69848 | -51.88234 | 2026-08-16 03:55:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 27336e78-47a7-34e9-acd2-cfab94fd11f3 | -11.88479 | -50.61979 | 2026-08-16 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71ef348a-34be-3b3a-8759-87d2befb2fb9 | -15.14448 | -48.6208 | 2026-08-16 03:55:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cf494a1a-5c89-30f5-bb66-24347a09d3e5 | -14.89931 | -46.63625 | 2026-08-16 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dc831f84-5c0a-3e64-9690-d5df332b0f66 | -11.46008 | -46.59746 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa321ea3-5fd3-33fd-93d8-2ba01cf3f04f | -11.3285 | -46.21832 | 2026-08-16 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8ad70ec-1f7c-3e61-9861-2dbbcafe7846 | -12.7037 | -48.47841 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9463087f-a8b3-3172-81e0-c4d7d28cfc53 | -11.47564 | -46.59341 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b8ce5fe8-1fd8-3964-a283-7b0abe02243b | -11.4767 | -46.59199 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5b4ea16-88a3-374d-a9c6-bc575125effb | -11.48449 | -46.60157 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 661a4bf8-47bd-32b8-b1bf-a3ceedf25460 | -12.01163 | -46.4345 | 2026-08-16 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| ff945e75-70af-3778-9aa9-5000af1a7cc8 | -12.72281 | -48.46914 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c10ff12f-2c08-3c18-ad46-4a6b4d7b6e8b | -15.06528 | -47.0241 | 2026-08-16 03:55:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f3c35528-4ca5-37eb-877f-30c0ebc7f21a | -10.45822 | -46.29585 | 2026-08-16 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13b16732-d48d-3bda-a2b1-7f1a32bae768 | -14.28589 | -47.18974 | 2026-08-16 03:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 514bf504-d8ab-3fe1-ac4e-7cb806c226a6 | -15.05877 | -47.01546 | 2026-08-16 03:55:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4c51b045-4a20-3ec8-830a-771ef87079c8 | -12.27798 | -45.90504 | 2026-08-16 03:55:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5525ac88-8bc9-337d-9c2d-3ba1bf8450f0 | -9.0958 | -46.39545 | 2026-08-16 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35b7f29c-1396-3115-a6cf-e609100fe9fe | -14.90859 | -46.63914 | 2026-08-16 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a11f91b2-37ed-3b5b-9aa5-01fdea6cc50c | -13.46401 | -51.80887 | 2026-08-16 03:55:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dbea5233-b77c-32af-a0e5-54a2bc00a0cc | -14.29227 | -47.18443 | 2026-08-16 03:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 059918be-1e83-3834-9103-e4f2ad920bde | -12.71798 | -48.46437 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8bb151e7-b5a6-3169-9ddb-6de536b8d1ac | -14.92928 | -46.61257 | 2026-08-16 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f5a71337-5bb0-3959-9287-43bcf2525cb8 | -12.23881 | -47.01156 | 2026-08-16 03:55:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6105f775-ae8b-3e44-81f1-e7293a853a1b | -10.53364 | -44.84691 | 2026-08-16 03:55:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5150ed40-441a-30b2-b67b-c7bad12cee5a | -12.68609 | -48.45062 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 85397905-1af4-37a5-bac5-61cdf585ce39 | -14.15776 | -42.76219 | 2026-08-16 03:55:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3f54abd5-c2a8-3c80-a81f-0a9c54b42408 | -14.93333 | -46.61228 | 2026-08-16 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea13d7b3-682e-34c0-ac01-0b67d61110c8 | -13.43556 | -43.85061 | 2026-08-16 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eaf5f699-7f2e-329a-8a90-a88da151dde6 | -10.18505 | -46.41074 | 2026-08-16 03:55:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6b23fd1-ad00-35ac-b68a-7e75a15a22c8 | -10.27352 | -48.28967 | 2026-08-16 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 020190ea-a020-383c-a53d-3d36dffccf6f | -11.99892 | -46.42066 | 2026-08-16 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94c50c36-ead9-3ec2-85f5-f88d2e4de53d | -15.06271 | -47.02109 | 2026-08-16 03:55:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a16e8e62-7058-3bea-a026-4712a035a35d | -11.48122 | -46.59143 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f6ee9790-fdc0-3564-a85b-23bba590a7b2 | -12.03186 | -46.44193 | 2026-08-16 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| a0e65c71-69b6-3aa0-8777-e074445a29e8 | -14.41099 | -51.94624 | 2026-08-16 03:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae054cf1-73a5-39eb-bb8e-a9bea46b598f | -9.09694 | -46.38916 | 2026-08-16 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 180c5bb1-b284-3acd-80b6-81bae2543b12 | -11.46177 | -46.61648 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4f70b56-a35f-3cad-8cf0-14927df2b51b | -13.50413 | -48.23173 | 2026-08-16 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9fa4ee1-6a75-390f-8754-8cfd27969a73 | -13.55629 | -49.05892 | 2026-08-16 03:55:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01528d83-2162-3c01-b028-5953e2eacc18 | -11.61925 | -51.09595 | 2026-08-16 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 51b1837e-e9f3-35f7-a003-07d407b4f6fc | -15.69698 | -47.46224 | 2026-08-16 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1746d0e5-56fc-3496-bf21-7b808bd09f6b | -12.03084 | -46.44083 | 2026-08-16 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |


[Clique aqui para ver as próximas entradas](README13.md)
