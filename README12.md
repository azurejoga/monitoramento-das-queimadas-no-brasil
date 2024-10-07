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
| 28d47a36-daca-3226-b3da-4c0e2ef95b80 | -16.9711 | -56.8058 | 2024-10-07 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.4 |
| 311943a6-2c4c-3e2f-9c21-9bef8ab0e550 | -16.992 | -56.721 | 2024-10-07 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 139.7 |
| 99035568-f0ec-3135-8ddc-f5856083249f | -16.9924 | -56.7003 | 2024-10-07 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.2 |
| 1e9a5b84-a2cc-3e5e-8af2-1efefa804739 | -17.0116 | -56.7186 | 2024-10-07 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.4 |
| 326f6ec6-b329-32ed-8ca4-8faf5e9e5bbd | -17.012 | -56.698 | 2024-10-07 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.8 |
| 5eeb0809-1513-3d96-8c6c-e9390b454d7f | -17.0123 | -56.6773 | 2024-10-07 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.0 |
| 4b95861d-ba22-3126-b210-301f81b57ca3 | -17.1581 | -57.3582 | 2024-10-07 00:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.1 |
| f4d98533-d70c-377c-9896-4ad89d1ebc3e | -17.6481 | -53.0849 | 2024-10-07 00:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 42df6dd7-3a4a-3eda-be2f-9d1c3b07913a | -17.6485 | -53.0634 | 2024-10-07 00:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 045d2d63-19c2-3587-8070-68f8ad0d8d51 | -17.6679 | -53.0819 | 2024-10-07 00:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 730f9ae2-1961-3df4-a7ca-47e8091d2ec6 | -18.4523 | -53.495 | 2024-10-07 00:36:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 38550191-8d76-3f13-9c39-df674605048c | -18.6391 | -57.2578 | 2024-10-07 00:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.1 |
| dc83d941-8db1-3c8d-83b5-49bedcce0ac3 | -18.659 | -57.2552 | 2024-10-07 00:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.7 |
| d15d2031-6b05-3ea7-bae9-d10bd52e5cb7 | -18.718 | -57.289 | 2024-10-07 00:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.4 |
| c75de8ad-4de2-31db-a855-458476135de6 | -19.8112 | -42.36 | 2024-10-07 00:36:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 82.9 |
| d5c8fe98-dbee-3617-88c4-62da075fd446 | -19.8318 | -42.3542 | 2024-10-07 00:36:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 114.4 |
| 0e0097d1-ed13-39d5-beb8-9fd4bb33e047 | -20.1026 | -49.0562 | 2024-10-07 00:36:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 189.7 |
| 390aa42a-e46c-3fc0-baa8-21ded5f8b6e9 | -20.1223 | -49.0748 | 2024-10-07 00:36:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 47451ca1-e53c-3a58-b199-58542c9ab43b | -20.1229 | -49.0518 | 2024-10-07 00:36:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 412.4 |
| 7b25cc90-bff4-3128-ad91-669dd2dc63e5 | -20.1236 | -49.0288 | 2024-10-07 00:36:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 68f8dfda-c65f-3583-bed4-d179874a7592 | -20.1433 | -49.0474 | 2024-10-07 00:36:58 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 81b7a44b-df68-3bbe-b382-a5b991ffbb4a | -20.4661 | -47.6592 | 2024-10-07 00:36:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 74.9 |
| e1115b36-27fb-3eab-9d8c-03ea0bf11248 | -20.4866 | -47.6544 | 2024-10-07 00:36:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 569a8d35-3f65-3af0-a20a-248e8f6ac924 | -21.3582 | -50.1287 | 2024-10-07 00:37:04 | GOES-16 | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.5 |
| 21ccd467-cd8a-3d42-88e4-000eb4176e3e | -21.5843 | -47.9536 | 2024-10-07 00:37:05 | GOES-16 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 118.9 |
| f6b767be-bffc-3543-b2ba-38beddad417d | -21.585 | -47.93 | 2024-10-07 00:37:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 68.1 |
| cc73ce3f-7af6-3267-bb79-c9dae90f31af | -21.605 | -47.9485 | 2024-10-07 00:37:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 4da087c2-ba29-3247-9030-7121a7501adc | -22.1974 | -48.1778 | 2024-10-07 00:37:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 126.1 |
| ad9ae4e0-51f8-3db1-b43f-a2237ed77674 | -22.1981 | -48.1541 | 2024-10-07 00:37:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 9c7cee65-2d48-3a9b-ae63-210dad3c6969 | -22.2183 | -48.1726 | 2024-10-07 00:37:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 39f9c7f6-2e75-3009-a6fa-62514ef025d7 | -22.219 | -48.1489 | 2024-10-07 00:37:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 59.5 |
| a8863dd2-4500-36a5-896b-7c4e07dbee7e | -22.3922 | -48.598 | 2024-10-07 00:37:09 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.8 |
| b4e8a0a7-ec44-3a41-b03c-1bc7c41a0fd9 | -22.7198 | -53.2341 | 2024-10-07 00:37:11 | GOES-16 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 78.5 |
| 5c0ad2dd-ca51-3d11-ac7f-c03506e277ee | -1.0182 | -53.739 | 2024-10-07 00:45:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 97f5746c-5ec8-3da6-9ad4-571a65da7550 | -1.0365 | -53.7389 | 2024-10-07 00:45:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 9ebe54ab-ca14-3f64-bb41-9b264d502cb7 | -1.0365 | -53.7187 | 2024-10-07 00:45:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 56e6115f-b929-3c57-aba6-002fae5b9e4b | -2.2113 | -53.7029 | 2024-10-07 00:45:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| cfbfa5a9-a6ad-398c-b237-11768ce4ce69 | -2.2114 | -53.6828 | 2024-10-07 00:45:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| a1c14656-c250-3ddb-8f38-da99f32f71f5 | -2.2297 | -53.7026 | 2024-10-07 00:45:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 6d3eab41-4ca9-3aa9-9099-f4d579e76eb1 | -2.2297 | -53.6824 | 2024-10-07 00:45:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| ed7c60c4-b60a-376a-b282-efb7174f6551 | -2.8569 | -52.9197 | 2024-10-07 00:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 36986dc9-d6c1-3af2-9ce3-aade098f841c | -2.857 | -52.8993 | 2024-10-07 00:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 153.0 |
| 5f107093-d7a8-3b14-9352-3f03b73a01e9 | -2.8753 | -52.9192 | 2024-10-07 00:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 243.8 |
| 00cd7245-54b6-321e-a7b1-f7ea807272db | -2.8754 | -52.8989 | 2024-10-07 00:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 318.0 |
| 32538886-7049-3ea9-9242-889d5dde5004 | -2.8937 | -52.9188 | 2024-10-07 00:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 8e155022-84ea-3d14-bfd1-3bcdc2ee0f7d | -2.8937 | -52.8984 | 2024-10-07 00:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| e9e8b951-c60a-3b53-93a7-7a63719a1558 | -4.2728 | -43.7601 | 2024-10-07 00:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| fae38339-7744-3f86-93b6-6a4575c350f9 | -4.2729 | -43.737 | 2024-10-07 00:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 211.0 |
| 846a8db7-a176-30e3-ab80-be4758c5be94 | -4.2916 | -43.736 | 2024-10-07 00:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 8efd9a9b-ed3e-3ebd-a7e7-0a4cd37a4f5e | -10.3316 | -64.262 | 2024-10-07 00:46:05 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 51ce919e-3ae7-3794-9760-575cfe1ea51b | -10.3503 | -64.2612 | 2024-10-07 00:46:05 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 7be9c80f-d5c9-3936-a9ee-2356889eff78 | -11.2467 | -51.3918 | 2024-10-07 00:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 6dd0f2fa-f2d7-3ab9-9849-1f8ea3fa9fe9 | -11.247 | -51.3706 | 2024-10-07 00:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 573a319d-bdad-368f-9239-77ee5d01ba5c | -11.2657 | -51.3898 | 2024-10-07 00:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 967b677f-ca81-380b-89f0-62f72a75b03d | -11.266 | -51.3686 | 2024-10-07 00:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 7a1bc5ba-4e0a-38e5-8d64-67e2b74fdbfb | -11.2847 | -51.3878 | 2024-10-07 00:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| e49d245c-112c-3cfc-8d80-e3a782654f51 | -11.7373 | -44.4926 | 2024-10-07 00:46:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| fd28f15f-585e-3152-b9e9-15e026372048 | -11.7566 | -44.4897 | 2024-10-07 00:46:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| f6164a07-9390-3f8f-936c-5f5d7b2813be | -12.0585 | -63.7841 | 2024-10-07 00:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 24d25270-d6aa-3862-95a7-e238b6a695ca | -12.0587 | -63.765 | 2024-10-07 00:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| fc49209c-f026-3126-abc9-76b8b718a7ce | -12.7284 | -40.2117 | 2024-10-07 00:46:17 | GOES-16 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 71.8 |
| 82b83f85-7c27-38a4-91e6-f5a1a539b0d2 | -13.5719 | -50.3223 | 2024-10-07 00:46:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 00c9d514-1386-3002-b2ae-ffed52fb4954 | -13.5723 | -50.3006 | 2024-10-07 00:46:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 176.4 |
| fa6ca5d5-540f-3b35-9832-8810718c910a | -13.5911 | -50.3197 | 2024-10-07 00:46:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 122.4 |
| fb51ab74-5a2b-3be5-9b7e-b3e27e5d9d67 | -13.5915 | -50.298 | 2024-10-07 00:46:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 1208650a-f38b-3dbb-8789-a96ae821354f | -13.8354 | -44.6398 | 2024-10-07 00:46:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 6457e73f-d566-3333-8b54-aa3cd78622e8 | -13.8359 | -44.6162 | 2024-10-07 00:46:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 1c9e33a1-ef09-3007-a3c6-b2d94131821a | -13.7342 | -60.6471 | 2024-10-07 00:46:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| ab2e9d0e-97e7-34e0-a993-d19a394323a1 | -16.075 | -50.2134 | 2024-10-07 00:46:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 25c65b47-b90a-3d31-83ff-396ab24d19ba | -16.5072 | -57.7387 | 2024-10-07 00:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| 9b3565d4-a8e7-332c-82d5-4b7ef196916a | -16.5075 | -57.7183 | 2024-10-07 00:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.2 |
| 8372a4e1-7337-395d-a63b-8f19e8db9723 | -16.5267 | -57.7365 | 2024-10-07 00:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.1 |
| 463f2454-a211-355e-a19c-f2faf47c7cbf | -16.6195 | -55.5892 | 2024-10-07 00:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 94.7 |
| fd74ac4a-0908-3ae7-b94c-03b440ba825f | -16.6199 | -55.5684 | 2024-10-07 00:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 108.7 |
| 4644b641-3377-3726-a81d-2bb76538565b | -16.9711 | -56.8058 | 2024-10-07 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.8 |
| 92e3046b-d697-33fe-9974-c24260d52742 | -16.992 | -56.721 | 2024-10-07 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 131.6 |
| c2d3bae7-076b-3ab4-aaaf-5a4370bb37ee | -16.9924 | -56.7003 | 2024-10-07 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.3 |
| fa63b337-b531-3af0-8d40-0a08a99d5c35 | -17.0116 | -56.7186 | 2024-10-07 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.3 |
| 73a3eeec-672d-30ee-8a2b-11e508bac4d9 | -17.012 | -56.698 | 2024-10-07 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.3 |
| 52cd0090-ff6a-3f2b-9d35-9deca82d8565 | -17.0123 | -56.6773 | 2024-10-07 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.0 |
| fe181a81-715b-31db-a268-e0a6dbfd5349 | -17.1786 | -53.9213 | 2024-10-07 00:46:42 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 72d45424-e25b-3778-a776-f47206688880 | -17.1581 | -57.3582 | 2024-10-07 00:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.7 |
| 98bc4a86-faef-3c88-a8e9-804c055224dc | -17.1584 | -57.3377 | 2024-10-07 00:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| 1214f1c4-2be1-3763-a623-94ae01e55843 | -17.6283 | -53.088 | 2024-10-07 00:46:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 74.3 |
| ff665b99-9d8f-35cf-bbb4-074a8f7fab63 | -17.6481 | -53.0849 | 2024-10-07 00:46:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 112.3 |
| f7340bd4-ddf3-33a7-918d-815f06f92ecd | -17.6679 | -53.0819 | 2024-10-07 00:46:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 191.8 |
| b52d34fb-feda-3e6d-8ae1-4174ab6e1417 | -18.4518 | -53.5165 | 2024-10-07 00:46:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 45fb2443-f05d-310b-a90a-d297e3bb6658 | -18.4523 | -53.495 | 2024-10-07 00:46:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 32.7 |
| d82a8155-d3ba-3aee-b1cf-bd512fb3c1ec | -18.6391 | -57.2578 | 2024-10-07 00:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.2 |
| 72541d4e-d4ec-3f70-acaf-8d0897059949 | -18.659 | -57.2552 | 2024-10-07 00:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.0 |
| ac2cd869-2dc5-31f2-ae14-ea77ada8cd08 | -18.718 | -57.289 | 2024-10-07 00:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.8 |
| 8beee28f-2695-36ea-a64d-9d003f74de31 | -19.8112 | -42.36 | 2024-10-07 00:46:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 165.5 |
| f4509369-4e61-3c89-adb8-27166585f957 | -19.831 | -42.3796 | 2024-10-07 00:46:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.8 |
| d9d7f333-ac83-3db3-aea9-536cd8e1534b | -19.8318 | -42.3542 | 2024-10-07 00:46:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 340.4 |
| 44c729b3-7c32-3f54-a023-5907952670d6 | -19.8326 | -42.3288 | 2024-10-07 00:46:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.8 |
| 6a7aba48-b945-348c-9b37-3821f74286ba | -19.883 | -42.6663 | 2024-10-07 00:46:55 | GOES-16 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 107.9 |
| 0f305208-6061-31e9-9c7c-f1c2d4b6692d | -19.8838 | -42.641 | 2024-10-07 00:46:55 | GOES-16 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 211.0 |
| 10c085ed-f5ea-3a1c-8e7e-953efe49e889 | -19.9044 | -42.6353 | 2024-10-07 00:46:55 | GOES-16 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.5 |
| 10477e43-7378-3cca-bc6c-450e98a5caf0 | -20.1026 | -49.0562 | 2024-10-07 00:46:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 185.2 |
| d781092a-e22f-3071-8276-e80bf598a8b7 | -20.1032 | -49.0332 | 2024-10-07 00:46:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 82.6 |


[Clique aqui para ver as próximas entradas](README13.md)
