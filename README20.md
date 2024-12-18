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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9cfbb60c-c81f-359a-b224-426c88e7e4ee | -19.01365 | -56.37884 | 2024-12-18 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 39cdc365-5e6a-3b32-91a2-12a433d5928e | -15.08128 | -59.64666 | 2024-12-18 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b361bf05-f211-3063-bc92-eee1881c2dad | -15.09058 | -59.641 | 2024-12-18 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c9ab5d0-966d-31f1-b201-05bea490713f | -15.45336 | -51.80906 | 2024-12-18 04:53:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 146036fb-d409-3ecb-ab59-a839ca35c6bf | -23.37574 | -53.61877 | 2024-12-18 04:53:00 | NOAA-20 | ICARAÍMA | PARANÁ | Brasil | 4109906 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2b7483d0-3bc6-39a7-bcd5-949243b6310d | -12.01706 | -62.79615 | 2024-12-18 04:53:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f648f9e5-0512-3364-9895-f2f59abc107a | -20.16078 | -47.39567 | 2024-12-18 04:53:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da0e32a9-5912-360a-b90c-a08baa5d134b | -12.01672 | -62.79488 | 2024-12-18 04:53:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a5dc6e9-68cb-3565-9395-471fc8ffe1b7 | -19.02252 | -57.62068 | 2024-12-18 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a764cc52-e326-31fe-99db-f1f36c55741c | -15.2394 | -59.93183 | 2024-12-18 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d009250-f21e-3581-9e00-e49ff374438f | -19.06805 | -52.85975 | 2024-12-18 04:53:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 212c206e-d92f-36f6-a9bc-aa4e258f4ed2 | -23.57666 | -54.74674 | 2024-12-18 04:53:00 | NOAA-20 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 39427c87-56e0-382a-be85-e083fbbec50b | -15.08993 | -59.64462 | 2024-12-18 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89be1184-f11f-3559-a9e5-a1aeba60d2a1 | -19.06396 | -52.86331 | 2024-12-18 04:53:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 831b4ab7-41c6-34de-bf46-2e7d915cf7a5 | -16.47936 | -57.23076 | 2024-12-18 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ad35e373-d3b1-3d3a-a097-9ab1ac558d42 | -20.77643 | -49.84846 | 2024-12-18 04:53:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 23d9e906-7d1d-36f8-8c36-081489ce60c3 | -19.06746 | -52.86386 | 2024-12-18 04:53:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32455101-28b1-38b4-aea3-118bd734debe | -18.952 | -54.74982 | 2024-12-18 04:53:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc6965c1-6489-3b9a-82c8-45566e6cc02a | -15.09587 | -59.63457 | 2024-12-18 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50682c7e-8a0c-3b03-8458-85595f1019ce | -22.15192 | -55.28399 | 2024-12-18 04:55:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38c2d0bc-4ec8-344f-ac17-ac1587a244c2 | -21.59352 | -49.24259 | 2024-12-18 04:55:00 | NOAA-20 | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f052cbcf-5534-3223-a30d-a75971d502a3 | -20.51336 | -55.53277 | 2024-12-18 04:55:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fbfd863-c3e6-3f88-9564-7056a004ab61 | -21.1469 | -53.6298 | 2024-12-18 04:55:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 016ee0cf-8fc7-30f6-bc2b-c0bd186c79be | -20.87616 | -56.37634 | 2024-12-18 04:55:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 64f7121f-1703-32a8-a336-afaa7a6a0c50 | -20.72743 | -54.41986 | 2024-12-18 04:55:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3427e7e2-c279-3902-9fa9-3ce949faa764 | -22.06839 | -56.20221 | 2024-12-18 04:55:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8eb7678b-ff08-336b-8e06-cc7b842cd670 | -22.00401 | -57.30068 | 2024-12-18 04:55:00 | NOAA-20 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5714cbd0-0a5e-3fa8-9f67-201fab2cff06 | -22.29333 | -49.70923 | 2024-12-18 04:55:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d0a515d5-b69c-37c9-a313-1d25e10bc113 | -20.72686 | -54.42368 | 2024-12-18 04:55:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64359d49-2e94-3015-b11a-0d56f3e347f1 | -20.91636 | -56.54699 | 2024-12-18 04:55:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf1f7baf-a1b9-3e9e-bc57-e7dc5a87e440 | -22.14921 | -55.28807 | 2024-12-18 04:55:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80528b77-a010-37ef-957a-c83b5f20c833 | -22.20433 | -53.16066 | 2024-12-18 04:55:00 | NOAA-20 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6149c625-8bae-321a-b5c4-7d09cf09dc28 | -20.73024 | -54.42425 | 2024-12-18 04:55:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| dab3b79b-cd07-3f7f-90e0-d187b2523bf6 | -22.53855 | -48.81527 | 2024-12-18 04:55:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae768d95-fe09-3e92-b208-371a705617a2 | -21.78844 | -55.99702 | 2024-12-18 04:55:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| abefe6f1-57e6-309c-b6fb-d4d68c84250c | -22.20077 | -53.16006 | 2024-12-18 04:55:00 | NOAA-20 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5341e60f-c750-3213-b5cb-9776ab229fa7 | -22.00339 | -57.30448 | 2024-12-18 04:55:00 | NOAA-20 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e7d53b1-9649-323a-9bec-8241f54e3498 | -21.82706 | -53.28075 | 2024-12-18 04:55:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be8f1183-c32f-3dda-9c32-4222d6e06f19 | -22.15136 | -55.28777 | 2024-12-18 04:55:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 440e8ca0-3423-33b5-9ca6-3c40d0b5e176 | -20.70549 | -55.32322 | 2024-12-18 04:55:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab38975a-5f54-3f1f-8e8d-d459b04c8516 | -20.70606 | -55.31953 | 2024-12-18 04:55:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82af1376-84f0-3b5b-94de-e7f96b6f21e9 | -21.5896 | -49.23741 | 2024-12-18 04:55:00 | NOAA-20 | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 180a979d-14dd-3dbf-8958-ddd7c1b9833b | -20.73081 | -54.42042 | 2024-12-18 04:55:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 27593159-9318-318f-949a-8be1901418ce | -21.35226 | -48.62176 | 2024-12-18 04:55:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a3d44b93-c57a-3f7a-9bb8-ce4a640f92e7 | -20.47687 | -53.67504 | 2024-12-18 04:55:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8600aedd-7065-3d4b-a720-9eb555ad9287 | -20.29432 | -54.79312 | 2024-12-18 04:55:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab00a041-27c2-3539-85ab-f6eb0be10584 | -4.9643 | -43.7182 | 2024-12-18 05:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 8a107f3f-a14e-3428-9c8c-746b67e2b414 | -11.8648 | -43.8172 | 2024-12-18 05:00:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 61050eac-4707-3949-9188-50e6960a4927 | -4.9832 | -43.6938 | 2024-12-18 05:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| d30acf35-ce2a-336b-a20c-b5b0a0a913df | -4.983 | -43.7169 | 2024-12-18 05:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 18d1f5fa-5c89-3bed-b51f-a91168b28537 | -4.9832 | -43.6938 | 2024-12-18 05:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 1682826e-9bca-3c2d-bfaa-e8e2c24e9bab | -4.9643 | -43.7182 | 2024-12-18 05:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 148c3cc1-e867-371a-ab9c-7a9af0c951eb | -4.983 | -43.7169 | 2024-12-18 05:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 03862181-2c45-3052-a484-aac341f5ba63 | -1.69582 | -45.77267 | 2024-12-18 05:10:00 | AQUA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| af68a5af-be58-3aaf-aeb8-522bfe4fa0e4 | -1.62367 | -45.85178 | 2024-12-18 05:10:00 | AQUA_M-M | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2f437b3b-77d6-33fd-916d-6dae1c560584 | -4.54018 | -43.29355 | 2024-12-18 05:12:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 2b66b789-d5db-3517-9a9e-28b0b2e6aa6d | -4.95696 | -43.71404 | 2024-12-18 05:12:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 271ee6a9-4d0f-3f5e-bba9-4b4e93a897ce | -5.1098 | -43.31359 | 2024-12-18 05:12:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fc5337a5-bf21-353f-834b-318ebc708641 | -6.05184 | -44.04704 | 2024-12-18 05:12:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1f806421-2c51-398c-9a40-cfb0de08ad6a | -6.18911 | -44.42015 | 2024-12-18 05:12:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7ec15d4e-f070-36f8-8efb-14b7748820c3 | -3.86357 | -47.02658 | 2024-12-18 05:12:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 597b6bbf-5740-3431-bc7c-356ba8c5139f | -3.24149 | -46.87341 | 2024-12-18 05:12:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 25cb142d-905b-3057-8b4e-23bbbf06da4c | -4.57011 | -45.87992 | 2024-12-18 05:12:00 | AQUA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2f4ad03b-d687-3e64-857b-dc3d079f892b | -4.97505 | -43.71674 | 2024-12-18 05:12:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 12d6f94d-962f-3c32-95b1-ae6dbcdd5519 | -7.24568 | -40.16058 | 2024-12-18 05:12:00 | AQUA_M-M | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| d452baf0-0cb4-3693-a915-c1be9a3a04fb | -4.97645 | -43.70749 | 2024-12-18 05:12:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 08230783-9373-39ce-9ac9-ed7a386310fb | -5.99929 | -41.574 | 2024-12-18 05:12:00 | AQUA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 10a17510-5691-37da-afd7-1dc7ee58521a | -4.54156 | -43.2845 | 2024-12-18 05:12:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6b2c8907-1ec7-3a4e-8a1c-243d659c8a73 | -4.96601 | -43.71537 | 2024-12-18 05:12:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 130.3 |
| a0afbf79-b507-33d6-8ad3-3d8b6a632faf | -4.96742 | -43.70613 | 2024-12-18 05:12:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 3e13d117-34de-32f6-b7b6-85484195c1bd | -4.9646 | -43.72461 | 2024-12-18 05:12:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 49875e48-7c3d-3df6-9d8a-47bc43404dfe | -5.98959 | -41.56683 | 2024-12-18 05:12:00 | AQUA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b7cc5701-1efc-3ad6-9c9c-6593709ee39d | -3.24105 | -42.41014 | 2024-12-18 05:12:00 | AQUA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9bae9e0e-32e4-37ea-abfc-4246340a1b70 | -3.01884 | -45.2308 | 2024-12-18 05:12:00 | AQUA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 4c66e5d5-729c-3a5a-a1d2-7063aab1cfcf | -6.62679 | -47.3414 | 2024-12-18 05:12:00 | AQUA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| c111ef31-12df-3642-9dac-5815e8984cf6 | -4.92953 | -45.0891 | 2024-12-18 05:12:00 | AQUA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fc061d3d-fe19-3125-9e23-bfdcde64e7ac | -3.86438 | -47.02098 | 2024-12-18 05:12:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| f7fa0356-fcfb-3253-9b58-b7014aed8fbb | -11.85866 | -43.82628 | 2024-12-18 05:14:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| a7f9ee51-c242-35bc-aa20-c66fcda4dab2 | -12.33476 | -43.67223 | 2024-12-18 05:14:00 | AQUA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f74f704a-f1d7-39c3-b953-dcc421f90d55 | -4.9643 | -43.7182 | 2024-12-18 05:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 75d97c98-7ea2-3e5f-8499-bec1e1b45022 | -4.9828 | -43.7401 | 2024-12-18 05:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 4994ec7f-07af-399f-86b0-60f89ebb6600 | -4.983 | -43.7169 | 2024-12-18 05:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| cb264c10-f68e-3518-a290-21a8ea8a036b | -9.8166 | -36.1992 | 2024-12-18 05:30:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 61.9 |
| f13e275a-5bf7-30c6-90b8-0c39ab13b31c | -9.8171 | -36.1721 | 2024-12-18 05:30:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 69.9 |
| 77167f7d-6ca4-31c5-95f3-47ec1f993556 | -4.983 | -43.7169 | 2024-12-18 05:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 4430da58-206b-360a-a6e4-c51cb84d1505 | -4.9643 | -43.7182 | 2024-12-18 05:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 9780a53d-4792-3843-a5e9-6f18cf67b48f | -4.9643 | -43.7182 | 2024-12-18 05:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 9e942c4d-331b-3e39-ae9d-0f6b4e3ede23 | -4.983 | -43.7169 | 2024-12-18 05:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 68c6c4f3-d894-370c-8123-d786e774f381 | -11.8648 | -43.8172 | 2024-12-18 05:40:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 89589d75-2ab2-3399-9fd0-8d6613c52507 | -1.42739 | -55.45101 | 2024-12-18 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33e343d6-53a5-36b3-bbf1-9bd1fb609094 | -3.58285 | -54.55238 | 2024-12-18 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0934550f-9ff2-3fa5-9d6c-4265a6b7665a | -3.58229 | -54.5564 | 2024-12-18 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9ed5e44-593a-35d3-9731-32610e6cd89e | -1.4269 | -55.45427 | 2024-12-18 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5249ecb-f87b-3832-8f56-0604cb449a5c | -2.24029 | -53.74157 | 2024-12-18 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c5d5eafa-a6bd-32c0-9232-609141a8fa57 | -2.23965 | -53.74589 | 2024-12-18 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1620e61c-9374-3eaf-b2fd-e4ce1f0948da | -9.83311 | -62.67308 | 2024-12-18 05:44:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cac4bf7-b2e4-3fb0-8c71-4a52fba73f41 | -10.48773 | -67.8177 | 2024-12-18 05:44:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9d8af13-a336-300f-9f31-1cba15cdf6e3 | -9.82942 | -62.67255 | 2024-12-18 05:44:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20c826cd-5936-3305-b927-25a38d0770b0 | -15.09396 | -59.6362 | 2024-12-18 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dcfe4f28-d440-3557-8e50-c81d106a0b2f | -15.2433 | -59.92815 | 2024-12-18 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README21.md)
