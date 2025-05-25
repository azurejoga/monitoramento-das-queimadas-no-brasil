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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 305540d2-e366-3de8-973d-823e286c0892 | -7.49188 | -43.37561 | 2025-05-25 04:38:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 843d17ff-f547-3dab-a99b-3bfb51440edc | -7.6574 | -46.1013 | 2025-05-25 04:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| edea321f-a3cb-3fbc-b250-cf6b6f9cab7d | -12.27485 | -44.59961 | 2025-05-25 04:40:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 65c16659-7d72-34d8-9a7d-852f40005658 | -7.65904 | -46.10593 | 2025-05-25 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 99963879-9176-3540-a802-b3143f122cd4 | -11.75504 | -47.25334 | 2025-05-25 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d51efcc6-0bdf-385f-a317-f081e4e2e8cc | -10.74456 | -49.28604 | 2025-05-25 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8971fd4c-3c7f-300c-8375-ed81a283ddc3 | -12.25847 | -56.58553 | 2025-05-25 04:40:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8534d95a-a630-31b7-aacd-4de2fc63730c | -12.50308 | -55.18985 | 2025-05-25 04:40:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aaa74b2e-d189-3010-b952-c73ccf55fb86 | -8.06453 | -43.13024 | 2025-05-25 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cf47f997-d274-30ac-a4ca-c0b0bdee09d8 | -8.07027 | -43.1218 | 2025-05-25 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 276ce70f-2353-35a7-a361-eb1c933880c8 | -8.88158 | -49.04056 | 2025-05-25 04:40:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33b8ab86-115f-3bb6-b0a0-5439a9bfacf5 | -7.86719 | -48.05306 | 2025-05-25 04:40:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7c38a6f-db42-322a-be3d-dba99a7e720a | -7.86379 | -48.05254 | 2025-05-25 04:40:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 279ae57d-976f-3e64-b0ce-a0bb54440cf9 | -7.63886 | -46.1221 | 2025-05-25 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de170c65-d142-3654-b12b-1d206d58131a | -11.42636 | -54.3322 | 2025-05-25 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef1a5dbe-304c-3cc5-8bd8-6a1eef5b493b | -11.56892 | -47.61303 | 2025-05-25 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cffc96cd-e4da-3e5e-8cf5-757821b6e6a5 | -11.13889 | -53.91862 | 2025-05-25 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57964dd1-2d96-365d-8097-507d7b8dfe4e | -8.87879 | -49.03651 | 2025-05-25 04:40:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2ef8c4f-51d0-32e0-8d94-806eb55d1d8f | -12.37751 | -49.98762 | 2025-05-25 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc25b9a6-17e8-3fe1-aa7f-1fd352d18f47 | -10.37827 | -47.98164 | 2025-05-25 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ff4ee23-bc57-3217-95ab-0084413b1544 | -11.33228 | -54.24395 | 2025-05-25 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4f64a61-b176-3844-a648-937a1d05ba3c | -7.63517 | -46.12154 | 2025-05-25 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47dd9af5-f6db-357a-85c9-77eb5ec84ec6 | -8.05819 | -43.14312 | 2025-05-25 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| fe30df1a-6f7e-3608-bb35-c3a50204420c | -13.36612 | -54.26541 | 2025-05-25 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0be7ba2-af09-363a-b9ed-8bd830caa3ca | -11.88882 | -56.41463 | 2025-05-25 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8781d01e-0e60-33ee-bb5a-d0fd61ec8bba | -10.36265 | -47.96735 | 2025-05-25 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e4b77bd-a7f2-3d25-970c-4fc146f82208 | -10.72733 | -52.47736 | 2025-05-25 04:40:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 044197dc-62d5-3cb2-9987-90ee1921468f | -7.66098 | -46.09264 | 2025-05-25 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 04a64cab-08ce-3e4b-befa-eea1fc989266 | -8.06235 | -43.13158 | 2025-05-25 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 116fca75-756e-379c-8263-ae55b305a0e3 | -8.05719 | -43.13545 | 2025-05-25 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5ef4eb72-2f3a-3d07-915b-561cfeb14986 | -8.72944 | -47.98861 | 2025-05-25 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4b633148-20d3-3b39-a0de-e0fd79925cca | -11.40111 | -52.9559 | 2025-05-25 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3a76b90-34a2-3265-bb46-9b10ba02be16 | -8.0588 | -43.13863 | 2025-05-25 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 2129cdfc-4c5c-3886-994c-d5d44d542afb | -11.61819 | -47.99714 | 2025-05-25 04:40:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5c2428af-03a7-38b4-8915-4cf703495f31 | -11.57382 | -47.4509 | 2025-05-25 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea0f48c6-40a2-35a6-bdf8-eb4baae0a9aa | -7.65968 | -46.10154 | 2025-05-25 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e4c23710-f2ba-3b84-884a-63a5ac279e78 | -11.57249 | -47.61357 | 2025-05-25 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61016b9f-a130-37e5-9cce-04f34c29ffe8 | -14.69914 | -45.39326 | 2025-05-25 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a04b4447-2774-341d-9817-662acf65f12e | -11.29765 | -53.9824 | 2025-05-25 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69afa941-9afd-306d-a505-7b7187a69d1b | -13.00624 | -55.97215 | 2025-05-25 04:40:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 450893fe-b54e-31b9-9b59-f3d7c9cf6799 | -10.37133 | -47.98058 | 2025-05-25 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a54e0886-cddb-3648-99cd-797cb9a23f2e | -15.37339 | -45.67986 | 2025-05-25 04:40:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2772f657-c476-39f4-8e84-dff5118ab952 | -11.14035 | -53.9321 | 2025-05-25 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c66fa2a5-37d9-34b2-827e-c256982507c5 | -13.45135 | -47.6736 | 2025-05-25 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5094bfe-0997-3170-ab20-4fa19e6eac40 | -11.75442 | -47.25767 | 2025-05-25 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8cb477ed-c994-331d-a00c-c32bf7f9221f | -8.05941 | -43.13411 | 2025-05-25 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6d7c04fd-1d4e-3307-82c3-cea86ff33f79 | -10.73839 | -53.88582 | 2025-05-25 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95ee5380-b778-336d-9240-20421b3ecfa5 | -7.95266 | -44.87178 | 2025-05-25 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1a73398-533a-3a00-9343-b86aebaa5cd3 | -13.36159 | -56.70949 | 2025-05-25 04:40:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdf2b6ee-6980-34b0-9f87-56bdfccc3191 | -7.6486 | -46.09981 | 2025-05-25 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d7a7c301-b7ad-31e8-a2d1-a08fc6215429 | -11.97079 | -44.15805 | 2025-05-25 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b741c5e-fc4f-3d43-a1e2-84b17f701371 | -10.47123 | -47.94319 | 2025-05-25 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 158931cc-52df-3848-b3d5-9a4a6cab6078 | -8.72888 | -47.99235 | 2025-05-25 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5a18c59-5f6f-300b-b3ac-bbd02a1f4359 | -7.94468 | -44.87049 | 2025-05-25 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d3960a1-0e34-377a-8478-c378919bf8ea | -11.57547 | -47.61826 | 2025-05-25 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64bea37c-2165-3e98-9b76-f70d9bfbbb55 | -13.7032 | -47.6904 | 2025-05-25 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33c0899f-915e-3cdf-9a50-ee6f27241df0 | -14.69809 | -45.40142 | 2025-05-25 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3527033e-f379-3260-a559-c2493ea5b835 | -12.17498 | -54.26091 | 2025-05-25 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b9198d67-41ea-3894-8982-b1b74f5db939 | -11.75807 | -47.25819 | 2025-05-25 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 233b8182-974c-3e34-a29b-5b04d60a63e9 | -7.66468 | -46.0932 | 2025-05-25 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3324cdaf-1a25-3aa9-8e44-922a9c1aadc5 | -11.86754 | -52.25275 | 2025-05-25 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c18b08f-a82f-3107-b77d-4be766a34648 | -12.26265 | -56.5863 | 2025-05-25 04:40:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6294012f-ad87-3798-b871-f925b0085946 | -13.14342 | -56.80581 | 2025-05-25 04:40:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35a36fe7-6f10-39ed-8309-8463c6b62b18 | -9.03298 | -48.94058 | 2025-05-25 04:40:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 912b1057-1285-3f90-a4df-e8f01272a954 | -11.97138 | -44.15361 | 2025-05-25 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31f82c7b-1308-383a-b3d3-05e691a9e91f | -11.30848 | -54.0285 | 2025-05-25 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 485d3088-6e4e-32ba-a13d-886c34395f81 | -11.74057 | -62.72781 | 2025-05-25 04:40:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d783f5a6-6525-3607-b2a6-31a5063c5881 | -7.65728 | -46.09208 | 2025-05-25 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d69fc1c6-ddd2-3223-8852-e86e2536953c | -15.37304 | -45.67781 | 2025-05-25 04:40:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0863baff-ff4d-32ed-87e4-f0863c01e72b | -8.05591 | -43.14444 | 2025-05-25 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| d88303db-0c70-38c3-876d-04e762aae895 | -10.72795 | -52.47359 | 2025-05-25 04:40:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19946156-79c8-3112-bebd-65d3af0d01df | -7.64924 | -46.09538 | 2025-05-25 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17467bb0-3ae6-3884-b9e1-0ad6e3d07bd1 | -13.09138 | -54.86486 | 2025-05-25 04:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c0e1f7fa-3ab8-3ef8-bb97-e89e94d86362 | -10.47414 | -47.94758 | 2025-05-25 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 374428d7-2579-39c1-afbe-5fe373d157bd | -8.71965 | -50.25684 | 2025-05-25 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86df66b8-bb21-3f7b-a4d3-829f36c6a66d | -7.65599 | -46.10098 | 2025-05-25 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e497a421-2f81-315e-90d3-1295e5d80f2e | -12.82721 | -47.38678 | 2025-05-25 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c2047535-9ab8-3a3e-8784-6809ff4318cc | -8.73001 | -47.98487 | 2025-05-25 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 01820046-a35b-3ab5-ba60-77d699a3e931 | -8.06904 | -43.13089 | 2025-05-25 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| dc6d1210-5615-3077-8ac9-1bbdfe4c7c92 | -13.09809 | -52.28884 | 2025-05-25 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af108eab-b73c-39e0-ae47-ad2b670cd443 | -10.37075 | -47.98441 | 2025-05-25 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d081b3f-ab04-3f51-b407-bffeb0e5c56b | -7.65535 | -46.10536 | 2025-05-25 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c7bfb2a6-00cd-3d8e-8de2-2c250dfa1a87 | -7.65229 | -46.1004 | 2025-05-25 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cfd29d26-2c27-3255-bbb3-ea52ce08140f | -11.75539 | -54.23012 | 2025-05-25 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e951da5-fd62-3884-bc9a-904239e8d4fe | -9.76316 | -41.88238 | 2025-05-25 04:40:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f5718daa-76db-3e15-aa7f-22b0543f825a | -8.37764 | -49.65871 | 2025-05-25 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6797fdd2-6ac3-3d88-9726-125f03d90df7 | -8.72295 | -50.25736 | 2025-05-25 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eab79f4f-f234-38cd-86ae-0791812dac5a | -10.36612 | -47.96789 | 2025-05-25 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb7cd484-b660-385b-a572-fce378f9cc86 | -8.89679 | -44.78257 | 2025-05-25 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81526424-c27b-3efb-84db-7aff911619dc | -11.14197 | -48.11453 | 2025-05-25 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cff81d16-506d-3a89-a503-72179ec6892b | -14.57052 | -48.33516 | 2025-05-25 04:40:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d22b20d-ca0c-338b-9bb9-20672c80b725 | -12.25792 | -46.68304 | 2025-05-25 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f98e8c96-7e50-33b5-8391-20bce09007ec | -12.35703 | -55.437 | 2025-05-25 04:40:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d97130b1-85d7-305f-8967-fc3f1a65ed62 | -11.57487 | -47.62241 | 2025-05-25 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26af2e6a-41fb-3795-9533-f5b7f0922246 | -13.08767 | -54.86421 | 2025-05-25 04:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1603dadd-15c3-35f5-a29d-8741c2782841 | -10.37538 | -47.97725 | 2025-05-25 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03c2a53e-e544-3021-96a7-0224982240cd | -7.63804 | -46.1206 | 2025-05-25 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cdc60bf3-1271-3629-ae43-4d386ccdc881 | -7.94867 | -44.87115 | 2025-05-25 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c59427bd-b74a-3590-a906-faa7f1960dc7 | -13.90612 | -48.72992 | 2025-05-25 04:40:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56f9812a-69e2-3d4b-a8a8-cd733e154530 | -7.66644 | -46.10701 | 2025-05-25 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README7.md)
