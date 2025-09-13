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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9d90142-5034-394a-aebe-9aeeb4e14d02 | -14.27825 | -46.0581 | 2025-09-13 04:08:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7be96ad7-8a90-30f9-9c48-4128aae7e4dd | -14.42837 | -47.32277 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 34f8e6fd-ead9-34a5-a27c-3500588b77b9 | -14.21808 | -46.263 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 898cfae7-f270-3c79-9a3f-c6bde7f0bbb1 | -11.81195 | -50.55201 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 21a558a7-f766-34e4-8b06-10800867a250 | -11.18634 | -51.43237 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 3d49b9f4-aa99-34f9-b378-c5e6a19ebeba | -14.20186 | -46.27213 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9d0b72bf-497d-318a-8e52-0710c87dad78 | -11.46967 | -43.59533 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe3541d2-1374-3178-870a-91f637825900 | -14.20042 | -46.25914 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a2412882-4519-3583-b151-e9db5dc003f9 | -10.6488 | -48.97354 | 2025-09-13 04:08:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 845583c1-87b3-33c6-bb26-6107f3006c66 | -10.75246 | -50.49936 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| c7de504f-98e1-3292-9c2f-3f2172972c21 | -14.21523 | -46.25822 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0add78bb-693c-3cff-b47f-388336cc7a15 | -10.35982 | -45.40004 | 2025-09-13 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ab44cdc-5f20-368e-817b-adc54fe1ec11 | -11.49059 | -43.63549 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 365c183a-3565-3bd7-a655-2cdd2d237575 | -14.21733 | -46.24588 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c5f38a9d-9a25-38db-b4e8-6851cb8fc6c7 | -13.58427 | -44.89029 | 2025-09-13 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 68cc8be3-85b2-3fcb-a295-00d4d88129da | -11.41719 | -50.75057 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cb1d5bd3-0e4b-32cf-934f-65ba0de9d6a5 | -9.65389 | -45.81374 | 2025-09-13 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b84fa99-c6dc-39d4-b09d-8006ccceb9b9 | -9.96105 | -50.39312 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28b45179-0273-3259-a83f-19c7db03de8d | -8.09374 | -50.18039 | 2025-09-13 04:08:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 0deb1c12-7915-3b2c-a49d-8fd8d4341994 | -15.05884 | -47.99442 | 2025-09-13 04:08:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c3ec0aea-42f7-37a3-8ac4-26a334589f96 | -14.17837 | -46.2808 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 47.1 |
| a07bf7a6-b44d-3b35-9ffc-915ba441849a | -12.11211 | -44.88227 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b56d651-e3f9-3e1a-8a2f-3f4e405cd470 | -10.09986 | -45.50019 | 2025-09-13 04:08:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9f976b2-d353-3d9b-b172-dae3199999ea | -11.74611 | -46.62975 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 24f7776c-bf84-3917-b2cf-f915f7bccc84 | -12.11718 | -44.84721 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 26108762-3257-31d0-af4e-6c2067ce4e33 | -7.79746 | -47.1039 | 2025-09-13 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d468ccc5-8c65-3887-87c8-91c6e3177f97 | -10.76286 | -50.55287 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8df6bd6c-d7a2-386a-8779-fc15e6a7487c | -9.25841 | -51.24091 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd97cf89-4769-3520-ad7f-101636079b3d | -14.46283 | -47.34649 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2c0a009f-4788-39a6-9897-e25fce9fca15 | -14.69943 | -45.15122 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a6be4d52-a7a7-3ffd-a345-ce69f023abc2 | -14.17479 | -46.28028 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 47.1 |
| d463f341-e48e-3b8f-ac3f-11923e320fe9 | -11.73355 | -44.21423 | 2025-09-13 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13735365-8dcb-3111-a010-0412da5d2fa0 | -10.50867 | -51.55017 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 29ca8e71-e044-3022-9cd4-cdf32a87c8e6 | -10.59596 | -43.02786 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8aeb888c-75f6-36ea-911b-3f0a3b8cd185 | -9.247 | -59.4201 | 2025-09-13 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| ffc3445d-6fa0-3a9c-91b8-3d7df11fd847 | -9.2844 | -59.3986 | 2025-09-13 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 792e1d97-824d-39a0-b180-92a73174b6c8 | -9.2658 | -59.3997 | 2025-09-13 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 173.5 |
| 1b6bb830-2809-3577-a47f-4e34bf732cdc | -23.6978 | -51.7916 | 2025-09-13 04:10:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 81.3 |
| d5e5f090-b31d-3f6b-870a-9a2a3c05b0ed | -9.2843 | -59.418 | 2025-09-13 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 6e043e68-6cc0-386e-ae85-087d8fe51f11 | -9.2472 | -59.4007 | 2025-09-13 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| a58a0d25-98a4-3694-b402-b90ad95a8a1c | -10.1611 | -64.7401 | 2025-09-13 04:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 3f6307ec-986a-3aa9-a772-d9b45a393c87 | -9.2656 | -59.4191 | 2025-09-13 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 204.4 |
| da4549f2-aaf1-30b7-bf53-28c9a0e4b67d | -18.33666 | -52.05581 | 2025-09-13 04:10:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93ac338e-bc17-3968-baff-2163c8d4301f | -18.33504 | -49.43679 | 2025-09-13 04:10:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff3950c1-b72f-317c-895a-b62872966ded | -16.52991 | -51.75328 | 2025-09-13 04:10:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b5df829-adb3-3746-b948-6320aafb942e | -15.81209 | -52.20243 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 70567821-570c-3628-81f2-298c84523fe9 | -20.59885 | -50.407 | 2025-09-13 04:10:00 | NOAA-20 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 478f5ab0-46aa-31db-9743-c42f9dbf02a2 | -16.55108 | -49.22458 | 2025-09-13 04:10:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1463901-5ece-39ac-ba74-b7eaf8ce94eb | -16.06276 | -50.00718 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2f4a327e-c975-3bf5-a2d3-f80cd3c9bf42 | -15.0662 | -52.47327 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dcb3abe-3fc5-35e7-83a2-11a7bfee5676 | -16.28242 | -45.68048 | 2025-09-13 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d882a17-2034-32f5-9043-39874fc00127 | -22.69043 | -47.58449 | 2025-09-13 04:10:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f504c8b8-fadb-35cf-89c8-12c3f70aee22 | -18.90671 | -46.6735 | 2025-09-13 04:10:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7517ac6-f3a5-39e1-937c-e2308c660ad9 | -17.45583 | -45.09845 | 2025-09-13 04:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eeb60e30-c0a2-369a-b5af-19e871d8e7d0 | -15.11741 | -52.46599 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47fb1158-35ae-3576-a44e-87f2d457d0c2 | -16.4332 | -49.04492 | 2025-09-13 04:10:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e96517f-3af9-3c3f-91ee-d2c91cdcd93c | -16.52586 | -51.75076 | 2025-09-13 04:10:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| feefef30-378f-33c3-b4ae-942b92306ed1 | -16.85342 | -41.5384 | 2025-09-13 04:10:00 | NOAA-20 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4b59168a-4af3-3b10-9265-b1b1d6172994 | -21.61763 | -46.80613 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7eda38d4-9065-36fe-998d-d71e1c2182d9 | -17.42253 | -49.24609 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1ed6bd5-eb27-3df4-98ef-c859a70da6ef | -16.07812 | -49.99637 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c6c94d3-ec3f-3a20-8efc-fb900acadec5 | -20.07975 | -46.94542 | 2025-09-13 04:10:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b91ee7e5-19c9-33eb-ab34-93c782687d2d | -15.1403 | -52.485 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11649d15-f3c7-30df-9aa8-bbba7084b86e | -16.5289 | -43.73661 | 2025-09-13 04:10:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f0cb59d4-57ca-3fff-b3a0-ad0d8cb07d32 | -20.42581 | -46.4556 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a81823fc-7cce-3760-b39b-3d493081648a | -17.41921 | -49.2416 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 254c4a3a-7649-39ce-b01a-e86dd43329d8 | -17.8296 | -50.41019 | 2025-09-13 04:10:00 | NOAA-20 | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14b0bcc2-c605-379a-a364-a003c6ba3be0 | -16.35522 | -51.51311 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90e02497-454b-3fae-9771-82081f8657e9 | -16.55177 | -49.22079 | 2025-09-13 04:10:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 21848552-b3aa-3357-bc0c-111a552b068d | -20.26037 | -44.1848 | 2025-09-13 04:10:00 | NOAA-20 | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1eecb389-db77-3bad-8f5b-093429e4ec91 | -18.04872 | -45.42218 | 2025-09-13 04:10:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68f04710-feb9-3179-8349-fe5e50e9f609 | -17.43509 | -49.22255 | 2025-09-13 04:10:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5f21c9fb-4218-3137-8824-5b52385ab0d3 | -16.35353 | -51.5461 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd1a41b4-7f1b-34d1-b5c4-66fc33d8388d | -15.38124 | -52.10361 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dabf0b50-a2a3-3642-9ad9-82580260e5a2 | -20.02187 | -47.63995 | 2025-09-13 04:10:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 365b2483-cac5-3e74-981f-43d88d7f153a | -15.10979 | -52.50397 | 2025-09-13 04:10:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8d4bea72-569c-3d8f-8ce9-1a9a838322c9 | -20.02318 | -47.65365 | 2025-09-13 04:10:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ff92d80-8d17-3701-bf9f-c6caf173b0df | -15.05563 | -50.15647 | 2025-09-13 04:10:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e5caaf3-6f6a-3532-ae83-7dec5f82fd78 | -20.62018 | -50.2261 | 2025-09-13 04:10:00 | NOAA-20 | MAGDA | SÃO PAULO | Brasil | 3528304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e3cff437-7173-3ed4-91e1-50f6f60ae712 | -16.33893 | -51.54158 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 685081b8-0eec-3623-a8c1-46025fdd7e6e | -18.59218 | -47.19071 | 2025-09-13 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d981f80-9a28-38b7-b16f-b742963d3ec3 | -16.53747 | -51.74196 | 2025-09-13 04:10:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 200a2950-b407-34f6-8228-7d4fa56ae487 | -21.61357 | -46.80949 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 632f5352-c4b9-3b6a-a23c-0c021ae7dc0c | -16.84375 | -40.8629 | 2025-09-13 04:10:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 03c12e9e-4f80-351b-aa28-24180c048a25 | -20.98438 | -46.54162 | 2025-09-13 04:10:00 | NOAA-20 | BOM JESUS DA PENHA | MINAS GERAIS | Brasil | 3107604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4280f0e7-1577-374b-b397-7ba177f6b494 | -18.79264 | -44.62406 | 2025-09-13 04:10:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d5de954-a734-38ab-8b1d-98fe120d0de1 | -19.65245 | -45.86703 | 2025-09-13 04:10:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e6dfb9a-5e92-3b25-baff-82c3dc00bc04 | -15.13226 | -52.49852 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26e9ea56-8837-3df4-8a39-0f786c022336 | -15.69514 | -50.58195 | 2025-09-13 04:10:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32da8cc1-c6f9-3206-a74d-1031f3cb842b | -15.70941 | -50.58041 | 2025-09-13 04:10:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 56cd41d1-c894-3b2c-8e1a-b8e9cdb461ef | -15.0491 | -48.15886 | 2025-09-13 04:10:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 12c96e76-99da-30e7-b038-e73063a52b17 | -16.35311 | -51.54436 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd1376cd-f335-3eca-af11-b9a9c36c16b9 | -22.18018 | -49.61035 | 2025-09-13 04:10:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3fc4c532-caeb-3b00-bf7f-5ed0193a1ebc | -15.15331 | -50.11789 | 2025-09-13 04:10:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a13f5ea-4951-3e31-b372-7a2d384713cd | -16.97994 | -45.81284 | 2025-09-13 04:10:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef05d37b-7c26-3972-b54c-c43f773c31dd | -14.61977 | -52.08739 | 2025-09-13 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b87fe93a-3307-3c85-87b5-458cc35a495d | -16.32841 | -51.54527 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dc2b8177-6888-3aaa-a287-43517d772261 | -15.1489 | -50.1171 | 2025-09-13 04:10:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2c70564-984b-35e6-b4a2-54993fa54a05 | -15.85594 | -47.23677 | 2025-09-13 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2d18bfd-7d24-3233-90b5-e2d4f8f9452c | -15.1151 | -52.47752 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README62.md)
