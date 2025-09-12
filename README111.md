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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f0673f4-e1c4-3378-97f3-3bed0717e913 | -15.15678 | -52.40075 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11e2ec15-8405-38b5-9874-1c14ad157aff | -13.89856 | -48.2566 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d78bb06b-6804-3dfd-b8df-4aca914748a8 | -15.11339 | -48.60602 | 2025-09-12 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f0e2bd2-935e-3460-893f-983a9abfcfbc | -12.97585 | -54.75433 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 427711a2-8b75-323a-94dd-18066dfb401f | -17.38161 | -52.96301 | 2025-09-12 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 624451cf-8424-3541-8216-814fd75e6304 | -13.90423 | -48.26072 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 652fde49-4f81-3112-a337-d3f35cb8a0ee | -13.90108 | -48.22655 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b54cff2c-0a7e-3ac5-9d0c-71c97dc4fed3 | -17.83732 | -52.05616 | 2025-09-12 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df6a8f5d-2f09-3880-bf19-8fcabaa4c01e | -15.60683 | -52.73402 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e9533fc9-c737-366c-bde3-f63f0f66bae3 | -12.92992 | -54.80865 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad8b098a-da48-312b-90b7-dc68933de9bf | -15.81258 | -52.21974 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88086a4d-8e98-3428-8cda-04b6a1fd5ce6 | -13.90132 | -48.23133 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4ab4d15c-c5f2-3694-982a-5eb09e834939 | -15.53358 | -48.54808 | 2025-09-12 05:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b209930e-6c8f-3574-a665-258d1461be4e | -15.08666 | -52.43978 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3b5dc02-1a85-3d53-84bb-6c6dda75d71d | -19.3456 | -56.70198 | 2025-09-12 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0dd3415a-2a8e-3b9d-830a-4186d11004cb | -13.27099 | -51.71636 | 2025-09-12 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f30495a-2ef4-3251-ac3e-e7e3ced03dd6 | -15.10643 | -48.01308 | 2025-09-12 05:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 012898ba-4c35-3ad4-920c-4303c9104dda | -17.20977 | -50.14908 | 2025-09-12 05:21:00 | NOAA-21 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 19a8ac83-676c-3e91-b770-5d56b303181c | -12.93358 | -54.74855 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4abdc3f4-dfae-38b7-b848-58ad003d91e2 | -16.28731 | -50.04245 | 2025-09-12 05:21:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9e33f7fc-1574-3e9d-9b91-5d942f0e0ff2 | -12.96424 | -54.74463 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b9ed5a0-59c5-3a32-8391-ee02daa2e46c | -15.92023 | -51.79017 | 2025-09-12 05:21:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 7a9a498e-f56b-3b73-9f2d-7c8363ef40a0 | -18.45059 | -49.56598 | 2025-09-12 05:21:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 28b466df-99de-319b-8c74-a965695079ef | -15.91983 | -51.79372 | 2025-09-12 05:21:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 071cc684-fc32-3a4b-8c8b-45af32f89d00 | -13.22935 | -51.75405 | 2025-09-12 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8d03590-f5c2-3b48-9d65-fe56e1def608 | -13.89859 | -48.25092 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 40de2bdf-3956-337c-a401-bd69e8024e12 | -15.68274 | -52.22842 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5751cc8-becf-3aa4-8a86-8ce06146e5f8 | -15.11349 | -48.60773 | 2025-09-12 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de60621c-31ea-37e4-a6c5-bfc25d1ef332 | -14.87568 | -55.83635 | 2025-09-12 05:21:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63d848b2-dd7d-33c5-87f4-2ee9119b1eb9 | -13.90197 | -48.22532 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 155967f9-4408-3575-829a-3c6a9b3ab64d | -14.40298 | -52.93061 | 2025-09-12 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d832911f-c79f-340c-9c6e-2d1f10b0dcc6 | -13.89459 | -48.22503 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ac2759b9-049f-34bc-b67e-10c7fd56e854 | -17.13748 | -48.49647 | 2025-09-12 05:21:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6777058e-9697-392c-afea-c32168feb78a | -19.19157 | -48.01538 | 2025-09-12 05:21:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1c3dd0db-bb2e-37ab-9edb-9c2bff6a0f3b | -13.90955 | -48.27333 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4d7b041a-6da2-3ec5-acee-e181b206929b | -15.16145 | -52.4052 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02683cac-c29d-3319-b03b-f1f200059d92 | -15.58304 | -54.76056 | 2025-09-12 05:21:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8de3680-b77e-3240-80f9-4eadb20146d0 | -15.91406 | -51.79655 | 2025-09-12 05:21:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 1c07283e-8a43-347a-b2ec-50a1d705f3d4 | -14.41339 | -52.92639 | 2025-09-12 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d84e6291-9b79-3726-afb5-d69014aea623 | -13.89775 | -48.26408 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a92c93ed-05f3-321f-9c14-700cc70f7bba | -12.92307 | -54.79557 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93fdc41f-a862-3812-a405-59abd93bc70d | -15.08776 | -52.43058 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55958386-1517-385f-8db8-3f864921dbd9 | -15.08084 | -52.44532 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2c71847-1089-36bd-80ec-7c3a35c137e2 | -15.68236 | -52.23166 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 736b9978-0e10-3cab-9b4c-512b7fcbe1d0 | -14.74383 | -55.61111 | 2025-09-12 05:21:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93af3d40-e84c-3089-9723-f2be55325304 | -11.97448 | -63.92157 | 2025-09-12 05:21:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50650bcc-d4a8-3eca-9d8d-d61eeae038b4 | -15.15212 | -52.39614 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6ea5ee3-42ec-3d52-af08-7d73d41163ef | -17.38196 | -52.95998 | 2025-09-12 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6428e4c2-8f1b-32ef-91b8-931a3cb14e9b | -14.43454 | -48.41868 | 2025-09-12 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b114495b-0750-36e3-9a3b-2058b513f15f | -16.60942 | -49.80725 | 2025-09-12 05:21:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56bc1e3c-73e3-3838-963c-66884ddacc4b | -13.38738 | -51.82299 | 2025-09-12 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 654ae7f8-6e41-3657-918a-3957b6f6328a | -11.79455 | -62.73688 | 2025-09-12 05:21:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 4f20bca6-0dfc-3686-afbb-c46b9ff38120 | -20.00935 | -47.65835 | 2025-09-12 05:21:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cc1a4c52-96ae-3474-9c0a-f2c80694d2b2 | -18.77383 | -48.53732 | 2025-09-12 05:21:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e0f79d89-6b44-3a1a-b659-c14343410692 | -16.20729 | -47.98346 | 2025-09-12 05:21:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a71f2a60-86db-3345-b815-df209a09670c | -15.52702 | -48.54743 | 2025-09-12 05:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e18f7d3d-1842-3056-bd5d-2616baba55d2 | -14.1988 | -58.6017 | 2025-09-12 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5af18d45-8b9a-37ee-ba4a-6143ab99eb7b | -15.11858 | -48.62281 | 2025-09-12 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 51a39609-453c-3339-9b4e-1b05aebb983e | -19.99551 | -47.64874 | 2025-09-12 05:21:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 963f95a3-8106-35fa-bbb1-d110e7f5f3d3 | -15.12584 | -48.61277 | 2025-09-12 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf6b6599-84ca-320f-9179-b64b6231b853 | -19.98923 | -47.63472 | 2025-09-12 05:21:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 30331958-44ec-3cf7-94d2-ff68b5f59280 | -15.52754 | -48.54887 | 2025-09-12 05:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 62f2aed2-c2ed-385d-ab6c-05e79568efd2 | -14.51046 | -53.90302 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cb35bef6-f0ef-3d2b-b283-4a423b560d3f | -14.41524 | -52.92672 | 2025-09-12 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a40f067a-dfab-3e69-adc5-cc34cbb8ba5f | -15.11019 | -52.45902 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c5a9c96-14b5-3211-b897-3821a31c5000 | -14.74903 | -59.68774 | 2025-09-12 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 284fa476-b6d1-3fbc-9774-d144a0a17a7b | -20.35103 | -49.95897 | 2025-09-12 05:21:00 | NOAA-21 | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15450395-20d2-39d9-ac77-b27594ea2cff | -17.83544 | -52.05361 | 2025-09-12 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a29f2b4d-3fd9-3e2d-b706-ecefd50e56bd | -17.3769 | -52.95933 | 2025-09-12 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f7647dbe-4b38-37cd-bade-7a9cd64ae2b3 | -12.97162 | -54.7538 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6fcd0108-5e64-3911-a5de-ee4b482f4884 | -16.24062 | -48.44902 | 2025-09-12 05:21:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 34bffaed-2125-3a16-95ba-3dc872b011d5 | -15.23758 | -53.84019 | 2025-09-12 05:21:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a3acf41-dd03-32e1-bb54-ae56c2a8275f | -15.52702 | -48.55389 | 2025-09-12 05:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 054f775f-2d24-37b6-9fbe-6f0486d388b3 | -14.2103 | -58.59553 | 2025-09-12 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d49e2543-3d74-3e22-a68d-345b5242dd4c | -15.58221 | -54.763 | 2025-09-12 05:21:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7ee837e-0c86-3733-9c58-a539132979e6 | -15.53407 | -48.54297 | 2025-09-12 05:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a34c045e-db65-3897-b455-6b6a14dd1a4b | -17.8323 | -52.05165 | 2025-09-12 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84f747a4-4b5f-39ac-ad1b-ebb7010ae488 | -15.90829 | -51.79936 | 2025-09-12 05:21:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 089b3d6f-101e-3953-b9d9-19d91298e77f | -14.77526 | -48.24095 | 2025-09-12 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dcd227c4-7ff2-3298-8352-6ad1cb830351 | -15.11926 | -48.61283 | 2025-09-12 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 994235f7-66d8-3219-89ba-c9fef1e396ae | -14.50282 | -53.92617 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ffc71feb-ca81-3485-9099-9bc08597252f | -17.83584 | -52.04992 | 2025-09-12 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c1ac1f15-e45d-32db-8496-2e07e7b1b6db | -14.56536 | -48.75525 | 2025-09-12 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecbf0070-e2c7-3690-9cb5-489b70ae216f | -16.60985 | -49.80285 | 2025-09-12 05:21:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66a72cdd-e69d-30e0-a0bb-263a4df870ee | -15.16188 | -52.40146 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d803689f-5aff-394f-806a-11530227a72d | -14.50922 | -53.91259 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 06af8622-f38c-3e15-baed-47320bfc15e0 | -17.38507 | -52.93268 | 2025-09-12 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a794b12c-8145-32af-bd2d-a5678d1a825d | -13.91016 | -48.26738 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 63bc1183-0894-364a-a393-768c25433051 | -16.62264 | -49.79937 | 2025-09-12 05:21:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7c81c830-28df-3c3d-9fcd-8de6eca061d6 | -13.27768 | -51.71338 | 2025-09-12 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7327bbc0-0e67-36bc-9ad6-1e2f755e326b | -17.3709 | -52.9214 | 2025-09-12 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 19584e95-38b7-340e-abbc-6ebf9f28a648 | -19.99992 | -47.65044 | 2025-09-12 05:21:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4fd576f2-1e7f-317e-a944-47e57632f2b6 | -17.14078 | -48.49905 | 2025-09-12 05:21:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 976640f4-aabf-31fe-9668-ebda77ce6a54 | -15.13566 | -50.14258 | 2025-09-12 05:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f3bb2633-a416-37ef-b99b-31744873115c | -12.91986 | -54.75475 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 353f56b1-09f0-3ccf-9c29-85d1095703bb | -19.99597 | -47.64223 | 2025-09-12 05:21:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7150d679-5c20-3d07-b53c-76832b064eeb | -13.44895 | -56.66574 | 2025-09-12 05:21:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc754ad6-8780-339d-b33a-6acace81d860 | -12.9278 | -54.79229 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07701745-04c0-3e95-a2df-d29b748acf49 | -12.92883 | -54.75201 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 54608c21-65f7-3c63-8c19-c97eb32f19b5 | -21.22961 | -57.37061 | 2025-09-12 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README112.md)
