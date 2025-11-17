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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7798c31e-acdb-3f60-b083-dddeab495085 | -11.71652 | -48.8642 | 2025-11-17 05:10:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 64237f14-3f8e-3b71-9664-581cf35b84ee | -14.65081 | -46.53676 | 2025-11-17 05:10:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 44d6f1c7-8d23-3bbc-83bd-678cf473de1f | -14.53712 | -53.77303 | 2025-11-17 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abd20f3c-55d6-3105-a564-efea2b688e95 | -9.44477 | -59.20516 | 2025-11-17 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e0e6e0e-e2ee-354f-b778-bd85f132c233 | -11.81631 | -47.58541 | 2025-11-17 05:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ecc97663-c05a-3796-b039-d693da43816d | -13.72761 | -51.45426 | 2025-11-17 05:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4966c023-f1ef-369f-b89c-319c7ceba2a8 | -12.09607 | -53.27674 | 2025-11-17 05:10:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c374c8c-34c4-364b-8416-29477fb89ec1 | -14.65583 | -46.53685 | 2025-11-17 05:10:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 23628f0e-0854-3994-aa1d-0281574341f6 | -13.50479 | -61.53722 | 2025-11-17 05:10:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c036f9a-7d84-3650-99a1-402bb8e24c29 | -12.67299 | -47.16246 | 2025-11-17 05:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 997f7874-4043-3b02-9aca-3ce2aea9f317 | -11.82179 | -47.58572 | 2025-11-17 05:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 69805ded-086a-34fa-ba30-bc82b4783aec | -11.34065 | -48.90778 | 2025-11-17 05:10:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 12c9a587-7ab5-3838-819c-ada4b35532d4 | -13.73191 | -51.45485 | 2025-11-17 05:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b1daf5d-398b-3e76-be16-a618858126d6 | -12.67495 | -47.16469 | 2025-11-17 05:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aaf6e252-a4df-3214-84fc-e6726e5e7a69 | -12.9864 | -49.79835 | 2025-11-17 05:10:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6a81523-8a2a-3c5d-8741-4ef4df47bff4 | -12.40225 | -47.5901 | 2025-11-17 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 832f27ea-23e4-3f82-9514-40d17fe8b995 | -12.43826 | -44.75317 | 2025-11-17 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79a94362-3be4-345c-8ff4-3841fbc08b93 | -11.96723 | -44.30282 | 2025-11-17 05:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8454829a-0855-3678-be8d-ee5d6eb71a8e | -12.98629 | -49.79949 | 2025-11-17 05:10:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6d1ac96-19e8-3d4c-be20-a9d712df4fcd | -12.40851 | -47.53993 | 2025-11-17 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b8129d6-b210-3e86-9d98-a2b759379b19 | -12.22849 | -49.61451 | 2025-11-17 05:10:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4c831dc-cea3-3003-82c5-416953b7b841 | -11.15884 | -49.44126 | 2025-11-17 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5405df7d-6c68-3370-b52a-22762f9cbcfe | -12.40213 | -47.54635 | 2025-11-17 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4bbcfec1-6188-36fb-8028-f7b3feca93c0 | -11.7073 | -48.85731 | 2025-11-17 05:10:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2a186178-8c0b-3d55-86ba-07b72e337274 | -12.85004 | -46.47358 | 2025-11-17 05:10:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c75c761b-cbba-399a-9787-fe65aec2ca77 | -11.85359 | -56.89845 | 2025-11-17 05:10:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d83f619-bfaf-3b54-8f45-0856acb55f4e | -12.9041 | -45.1099 | 2025-11-17 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 753ad4f2-ad77-3a05-9670-43f7006ca3d7 | -11.62281 | -43.90095 | 2025-11-17 05:10:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e22dfc5-76f7-384f-b594-de0d1c68463f | -12.22374 | -49.61382 | 2025-11-17 05:10:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a1688c7-ab18-3235-b993-ab6f4f88c664 | -12.87885 | -46.46551 | 2025-11-17 05:10:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4526ae34-c130-358a-a759-065f2a636702 | -11.84417 | -49.21219 | 2025-11-17 05:10:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2cc95e6b-7e31-3656-8b12-78aa04b0a43f | -11.84348 | -49.21755 | 2025-11-17 05:10:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bb4f862a-6069-35c3-937a-7905e20e4931 | -12.67153 | -47.17431 | 2025-11-17 05:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fea5f7e1-8995-3be1-b28b-f9ea02b440ef | -12.00653 | -52.46425 | 2025-11-17 05:10:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb40aedb-364e-34cc-9454-8c6b2d301897 | -6.6875 | -42.0296 | 2025-11-17 05:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 66.1 |
| ea75262e-94ba-3641-8b05-929465d51d24 | 3.01517 | -60.89292 | 2025-11-17 05:27:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 061f22d8-7ee6-3dce-addd-8f41c9cefe86 | 4.52296 | -60.88755 | 2025-11-17 05:27:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 323d17fc-0855-3364-b3fd-dd3623bfa969 | 4.02862 | -59.66741 | 2025-11-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb3d5fc2-f92f-34cc-8596-2321a2b8e1e4 | 4.02753 | -59.66058 | 2025-11-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3fe42393-daa4-3ff2-9c4c-c6701011d4fd | 4.51826 | -60.20646 | 2025-11-17 05:27:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 482fe4d4-554a-3230-9eed-5ae1c0832ae9 | 4.51965 | -60.88823 | 2025-11-17 05:27:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2970ac4d-3310-3d44-8391-ac912e65dbc4 | 3.01462 | -60.88943 | 2025-11-17 05:27:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d59409a-b433-3c14-a33a-e3f02ed1bec0 | 4.03083 | -59.66005 | 2025-11-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 12da3eed-0af1-3af0-b860-a1a5eac96a5b | 4.03191 | -59.66689 | 2025-11-17 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eb6908e5-8e1c-3f89-b908-42aa82bff7a9 | -3.30338 | -50.0834 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19c0fd56-4323-35ec-aa43-62fa6c5ba599 | -3.30139 | -53.84695 | 2025-11-17 05:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54306d38-37b9-321e-aeb6-65993bc40742 | -2.88767 | -53.28751 | 2025-11-17 05:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ae44d971-032f-3a03-a9a7-26bf3f724836 | -2.47703 | -50.24346 | 2025-11-17 05:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f3e9353-0510-335a-9448-d1d4817faada | -10.66476 | -49.37396 | 2025-11-17 05:29:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| dfb9783c-b371-39eb-a68d-39c49e0fda8f | -3.1904 | -50.65019 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0edee849-dff3-31fb-bda6-30c842a45f34 | -2.66687 | -51.88535 | 2025-11-17 05:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f58ac35c-035d-388f-b6ab-bff7976a8317 | -1.7732 | -56.16575 | 2025-11-17 05:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de50c638-f4b3-39e4-a31e-5bba182f8c97 | -0.89896 | -57.17399 | 2025-11-17 05:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59a47832-3b05-36a6-b5b3-af2c39bb854e | -2.51848 | -47.81855 | 2025-11-17 05:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0c0dd5bf-0a41-30b6-adad-05eba43f6281 | -3.60042 | -55.53679 | 2025-11-17 05:29:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df0eacd4-45e2-373f-86cc-ebd3ca1b17d9 | -3.01262 | -51.34337 | 2025-11-17 05:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77c15aef-8a63-3492-9dc6-fb9fd4f9909b | 1.01394 | -59.51936 | 2025-11-17 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2b7e386-c5f9-3922-bb13-ff504aba29d0 | -3.23661 | -50.487 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90857b93-0367-3ae8-8a79-08140df96602 | -3.23541 | -50.50812 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ab8f889c-8ace-32a6-a954-b3b63f336702 | -1.52727 | -55.52111 | 2025-11-17 05:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28a27020-13eb-3718-84f8-33c0f7bb66e0 | -3.29929 | -50.07585 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec96ea1d-dece-3158-aa01-57dbb7353c58 | -3.18444 | -50.64932 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7056fc09-85b5-37ab-9015-09e303c93b6a | -4.09433 | -48.02367 | 2025-11-17 05:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e44c5863-12d6-3a58-a8d5-12dc7febe724 | -3.08411 | -51.25449 | 2025-11-17 05:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 111f3a08-1dd3-39f4-81c7-435bc1fc4405 | -1.77267 | -56.16922 | 2025-11-17 05:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f6e4192-3032-32da-8c89-b05c7189085c | -2.6674 | -51.88186 | 2025-11-17 05:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c226f065-4671-37a5-92ea-ac3fb5daa49e | -3.23808 | -50.48971 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69fa9c61-f3ef-3e88-9e10-1e77492cfa90 | -3.75874 | -51.11221 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20ab1e7c-da45-3546-9a9e-51060e18f3f6 | -4.54928 | -48.48294 | 2025-11-17 05:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5adf1c92-a44d-3035-a9e4-c191dfdc74cc | -2.9392 | -51.76407 | 2025-11-17 05:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4615489c-bb0a-36f4-a7c8-e3062de0d672 | -11.15459 | -49.45051 | 2025-11-17 05:29:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7e14fe81-15bc-3ed7-807c-7991ad8a85a5 | -3.22846 | -50.5001 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c80d1f5-05ac-3f38-afca-1850e50db963 | -3.58619 | -50.71575 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc831a88-d65d-3f74-993e-1a9a2aeb94f8 | -3.23873 | -50.48526 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 981cdd5f-c6a3-3be2-bfe6-1e898f8394d3 | -3.23521 | -50.49617 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7fc64147-7241-3263-99b1-8126282d332d | -3.22778 | -50.50462 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ae42600-b724-3a96-b30b-ebc02a3a07a2 | -3.23311 | -50.50993 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e4d86948-6480-3b41-9986-bccb0130aecb | -12.19582 | -54.27157 | 2025-11-17 05:29:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 789aec0f-f1b6-38d1-9bf7-2982014c72fc | -4.01607 | -48.81617 | 2025-11-17 05:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9379bdb9-7c14-3a10-9dc7-be5cd50bff0a | -9.58325 | -49.11885 | 2025-11-17 05:29:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 17250a96-875b-3557-a6ae-6e9d59111acf | -3.3302 | -50.28498 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6699d46d-a25f-357e-aa82-e1e901da5763 | -3.23138 | -50.49353 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b39c8d38-f5ba-3a93-98b1-6c48e3263667 | 0.23585 | -51.01879 | 2025-11-17 05:29:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7581f4b-f8c6-3d01-9584-756e4df2cba8 | -3.7483 | -51.81934 | 2025-11-17 05:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 719d82df-3fe8-3498-a6b7-7bfedcec1766 | -4.09876 | -48.0254 | 2025-11-17 05:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f599c977-0117-3554-855c-8c84a7bf6e92 | -1.34741 | -54.61034 | 2025-11-17 05:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e0cb918-c2e5-3465-9a57-0a78e75d22a5 | -3.39554 | -50.18305 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f88afdff-81a3-33f7-837c-9de9ce277024 | -3.58556 | -50.72001 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57e20f71-79ee-3a21-badd-dcbed0814a89 | -2.24322 | -53.62577 | 2025-11-17 05:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f77f06a7-6214-3fbd-b8ab-12278dc260b6 | -3.23675 | -50.49888 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c3c7c58e-895b-3006-9fb2-8346352883c9 | -3.23004 | -50.50278 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 06ac74cd-d83e-3b5f-a1c6-7588372c70bd | -3.75933 | -51.10824 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd602d9b-f017-3dc2-9eca-506c5641dff0 | -7.81834 | -61.6849 | 2025-11-17 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 46372cc4-593b-3980-8220-a242c5fe23ca | -3.49074 | -54.05351 | 2025-11-17 05:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e299a407-d164-3b8c-b817-fc6a8a913d00 | -3.90188 | -54.15207 | 2025-11-17 05:29:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4167eb62-588d-3cd9-a9a4-ff4a6dd2dd11 | -3.23071 | -50.49817 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 26ae72f1-4778-360c-be7b-e1ddc805ae9b | -3.1484 | -50.20296 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9699a7b1-984b-3d28-8934-62a2dc25f67c | -10.91337 | -49.41122 | 2025-11-17 05:29:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 048ad4ba-1f74-3902-9b5b-1e82c1ccd83d | -1.46713 | -53.4192 | 2025-11-17 05:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d88d2c2f-340b-3ef2-ac29-6fefaf94da7f | -1.70099 | -56.04047 | 2025-11-17 05:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README49.md)
