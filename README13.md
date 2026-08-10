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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| daff6f17-4fb4-300d-83e8-563bfd8a7ac4 | -8.95901 | -60.57759 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 21dd7f51-5b57-34af-b548-3c381468022f | -15.05598 | -46.5604 | 2026-08-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 69dee378-88fe-3d2e-bb5b-812cd223a99c | -11.22021 | -54.02946 | 2026-08-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93829db8-53c8-3124-88e2-6dfbb9bca0bb | -8.95987 | -60.57259 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4c12c15b-82a6-38dd-ad2f-fdfb1f4963af | -15.37962 | -53.76921 | 2026-08-10 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2163d754-ad1b-30b8-8c94-14e381ee06c8 | -11.21581 | -54.03593 | 2026-08-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bfab782-b839-3c2b-b393-c98cbab55c71 | -13.62931 | -46.21641 | 2026-08-10 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d10892b3-f4f8-3db7-b4ab-ab2df08ceec9 | -11.24601 | -54.8754 | 2026-08-10 04:53:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f730e29a-0e08-319a-9331-034df07af9fb | -11.1758 | -54.80475 | 2026-08-10 04:53:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d9b82cb-d615-3364-82af-0512936b0fae | -12.1978 | -52.86837 | 2026-08-10 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 762af80c-ad4b-3b14-95b5-ff2b52749ac9 | -12.08724 | -47.20251 | 2026-08-10 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8bc22da2-93ee-3a14-b795-ebb015fca08d | -11.46905 | -50.55938 | 2026-08-10 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80783316-11e0-30e4-9d42-e9a0fb45f550 | -8.96118 | -60.5371 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f4fd99df-72d0-3610-8348-591ff5c660b8 | -8.94943 | -60.53865 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 9616f0f3-76d7-3e6f-b321-ced409ac50f6 | -8.89097 | -60.58101 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c7d0be53-9902-3497-97e2-ea7eddc3c5a2 | -11.22297 | -54.0335 | 2026-08-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3ac5ba7-3551-3f30-acf5-4a066cf2469e | -11.17857 | -54.80888 | 2026-08-10 04:53:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e06880ea-ca17-35f1-b7ac-1499f09cd655 | -13.63784 | -46.22823 | 2026-08-10 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0459be60-31e4-3cbe-ad5c-ecad992a909b | -8.95942 | -60.60324 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fad9ccb0-75b1-3f42-a776-98114282a16a | -14.31379 | -54.92392 | 2026-08-10 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d127b82e-f0e2-30af-9534-66274f8b8213 | -11.22352 | -54.02999 | 2026-08-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88716a4c-faed-39aa-a013-aac0bb94e168 | -13.86707 | -53.66417 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8740b4f-5c67-39e1-9d60-432782e0d437 | -8.95521 | -60.55984 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b11d2268-72e0-3886-a6f3-53a3bff6a6eb | -14.411 | -45.64982 | 2026-08-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27c3f84b-44ba-3d5e-8776-4466f6e47d77 | -14.30604 | -54.92993 | 2026-08-10 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 495951bf-c74e-35a1-95e9-feeb76fd663c | -13.84254 | -53.89033 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f32751d7-cb00-3432-8f2c-16c57c419266 | -14.1399 | -54.01136 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a734fa2c-39d2-3c89-a70f-b3448d551994 | -11.21029 | -54.02786 | 2026-08-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f314c8dd-22f9-3a72-b570-054845cfef09 | -16.33536 | -46.89009 | 2026-08-10 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a025303-9c43-33d9-891a-f92cbd33948d | -13.84531 | -53.89442 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bad20d48-fb42-3f8a-a9be-e23a45d77ee1 | -16.06411 | -50.80216 | 2026-08-10 04:53:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08d3243e-6776-3f3e-b6e3-f2667a1aa9e6 | -13.85945 | -53.73613 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11d37ab5-43e7-393c-9ce8-b1404b906491 | -12.10198 | -47.19529 | 2026-08-10 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 427271b4-4e2c-3992-9851-4eda682e8b41 | -8.95609 | -60.55498 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 55398a08-7c15-310d-961b-5936a4cce32a | -15.38351 | -53.76612 | 2026-08-10 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0cd58752-bc51-3c99-9260-b7201b6765e2 | -15.08076 | -52.69933 | 2026-08-10 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c00f1aa-b3fb-3983-b089-b38e7cb7cf98 | -15.08132 | -52.69552 | 2026-08-10 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 510fb8ab-3b00-3d8f-8202-75091b870b33 | -8.89446 | -60.56132 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 88a52e62-d23d-3898-9564-b7db92efdb73 | -15.15195 | -52.71443 | 2026-08-10 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4d84b74f-7dd8-331f-9a52-85e787c99a4e | -13.86429 | -53.66006 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d27743f5-c095-3112-b476-5d56c5ef92d2 | -8.95862 | -60.55194 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 4cc22595-8931-3ab5-aa9c-d87451f2ec04 | -14.77239 | -56.3737 | 2026-08-10 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fca22a1-7f66-3cbb-a1f3-8020452b4d88 | -8.68247 | -62.87505 | 2026-08-10 04:53:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a70dabd-aa36-3bfd-a827-238b19114152 | -8.95807 | -60.57068 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd99c420-b3bd-3cd1-8a4d-6012d682884c | -15.03644 | -46.55694 | 2026-08-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 10b86acc-7058-346e-a9e2-9fa30fb1d6f4 | -14.13935 | -54.01491 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d829dba4-456b-3ebb-9c54-195e296ac9cc | -15.15251 | -52.71063 | 2026-08-10 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a74e3c77-6843-394c-91e7-fce1a5086cb8 | -15.3863 | -53.77029 | 2026-08-10 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4fe8716b-be9b-369a-86c6-276b5d5ab38d | -8.67832 | -62.86692 | 2026-08-10 04:53:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| baa5e615-e8eb-3143-93ae-b1583efc6a46 | -15.13726 | -52.69653 | 2026-08-10 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6ae6740-5916-3504-a91c-52a8e212aae3 | -15.13668 | -52.70041 | 2026-08-10 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d81a43dd-805e-3dd1-941c-888c02062068 | -14.14376 | -54.00834 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3961fb28-8679-3c80-ad1a-140b48ab5ee5 | -14.14321 | -54.01189 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f6ce6c2-f2e8-3fca-b75e-ea6f032efb87 | -11.18191 | -54.80943 | 2026-08-10 04:53:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c45eb82-9c7d-3540-b5f2-1f57f27558e4 | -13.64269 | -46.22946 | 2026-08-10 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de76ec4a-44b7-3607-9fe4-da6c6155260d | -10.90755 | -56.36887 | 2026-08-10 04:53:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 71eb24bc-aed9-3f50-b944-a72a4cd3c144 | -13.84885 | -53.69421 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f5cdd7bc-6f17-3d68-bb35-b4d9d05aa3a5 | -15.1514 | -52.71819 | 2026-08-10 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| a9bf8e7b-9ce2-3f2b-8996-b0bdb9506cf6 | -11.71847 | -49.09195 | 2026-08-10 04:53:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 001c7c1c-22cf-343d-a26d-8bcf44221c94 | -10.93721 | -57.11333 | 2026-08-10 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e1eb905d-ffd8-3c6b-90ec-a067a5557bfa | -14.74115 | -56.32977 | 2026-08-10 04:53:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ea20601-c82c-35ff-aa9b-77ab28d011ad | -8.96584 | -60.53793 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f3c8a4b-d961-37c8-a4c6-85bd379b3d8d | -14.14044 | -54.0078 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cefdf37e-9450-3655-83a1-904ed2267548 | -13.87094 | -53.66114 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6f359030-cc19-3339-9292-b45b5445a19f | -8.68313 | -62.87145 | 2026-08-10 04:53:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 34bee88a-d3e8-3783-bc7d-3892aed6486b | -15.15538 | -52.71495 | 2026-08-10 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7a99d11a-46a7-37fd-8a09-ec4a195f9794 | -15.65255 | -56.0417 | 2026-08-10 04:53:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8f6a0bcb-5f04-302f-baaa-e3e09489fa50 | -11.24956 | -54.83188 | 2026-08-10 04:53:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ebe9a4f-fb0e-3106-8714-c6cdf5e7accd | -11.21305 | -54.03189 | 2026-08-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab66ae3f-1a79-3151-a91b-abd7f69f1eb1 | -8.90119 | -60.57774 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ef38681-ea71-3ae1-aeb4-0c3a175f3f48 | -12.36165 | -53.15427 | 2026-08-10 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52f0522b-d048-358f-b0f5-3131f97ad81d | -8.98295 | -60.53925 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf39554d-1c6f-3df2-8cd9-3f544d34883d | -15.07966 | -50.37816 | 2026-08-10 04:53:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d38eaf17-9df0-3e9e-b4c3-5e8049cc871e | -13.86762 | -53.66059 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3671f9b3-1c47-34a0-ae7b-e6b85262c496 | -8.95473 | -60.60245 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71fb7bbc-2603-37a3-863b-62f0f5f9d995 | -8.94169 | -60.5388 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 317e331c-48d6-35b9-8ad1-23bf5172c95b | -11.21636 | -54.03243 | 2026-08-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1891bc7d-c49e-310b-be34-68fde3e02fe7 | -8.91017 | -63.96958 | 2026-08-10 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 17699dd2-7993-32b2-ba66-7ad64b7280d0 | -8.96075 | -60.55577 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 58aa9ccc-fe6d-30e0-8bd6-c6aefc003dc7 | -20.51944 | -42.30821 | 2026-08-10 04:55:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ca6e334a-a29e-3ca7-b83f-3c5a53add3b2 | -20.04401 | -43.76193 | 2026-08-10 04:55:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 91d953f8-a2a6-3090-89c8-1c61d6b13789 | -20.39077 | -49.3079 | 2026-08-10 04:55:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| c8965487-8df1-3b1b-b5cb-aa213be00fb3 | -20.52619 | -42.30985 | 2026-08-10 04:55:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c9308311-7b8f-3a6e-a7cb-9eb724c073d5 | -20.49716 | -43.63584 | 2026-08-10 04:55:00 | NOAA-21 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9d602bd4-afc2-3d79-8f89-d0681db61bb0 | -21.41357 | -43.88195 | 2026-08-10 04:55:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2b414a78-b9a5-3d09-8788-b3d6ac4a9585 | -20.78287 | -57.67445 | 2026-08-10 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ee661d86-c9e6-3a6e-9822-4a6b02d62ea7 | -16.5008 | -54.65609 | 2026-08-10 04:55:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe426ba3-14fe-3a73-b6d0-436183e98013 | -15.70197 | -56.1526 | 2026-08-10 04:55:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 902b7b93-f84b-3f70-8979-7acad4aa0925 | -18.12141 | -43.97293 | 2026-08-10 04:55:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f1595728-c99c-34a9-ba85-04bb27ce7767 | -22.20085 | -42.34548 | 2026-08-10 04:55:00 | NOAA-21 | BOM JARDIM | RIO DE JANEIRO | Brasil | 3300506 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 28cc6223-e0f3-3287-9923-1b6ceda47848 | -17.01231 | -51.29573 | 2026-08-10 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 716cbcc4-978d-3924-b695-c9b066455223 | -20.49775 | -42.38716 | 2026-08-10 04:55:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 599d3c20-91b0-3b8f-8ab8-de003164e4c3 | -20.04557 | -43.7668 | 2026-08-10 04:55:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a0b3d51e-e9be-3e96-a8ec-72143062b9e4 | -16.49473 | -54.65139 | 2026-08-10 04:55:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fdf1d144-5361-32b0-959c-54b43bd7697a | -17.13155 | -51.67683 | 2026-08-10 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf86e19a-8750-3831-b021-6ea78ea91f8d | -16.49141 | -54.65084 | 2026-08-10 04:55:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0826966-4b90-3726-97ec-14db64381e9f | -17.84391 | -45.27007 | 2026-08-10 04:55:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf38c5ea-29b5-398d-82c1-92a86fc92025 | -18.37535 | -43.66035 | 2026-08-10 04:55:00 | NOAA-21 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d7a70f9-291c-3792-b459-824b1bb3e324 | -17.13507 | -51.67953 | 2026-08-10 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90f062e9-ab5d-333e-ae62-fce20129d3cf | -21.6787 | -49.71845 | 2026-08-10 04:55:00 | NOAA-21 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README14.md)
