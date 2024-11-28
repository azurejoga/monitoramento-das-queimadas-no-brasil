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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc4d6fe5-99b8-38c1-bcf2-68e6a02ecb40 | -1.55479 | -52.77499 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b61dfe98-2ef0-3bba-9ec9-d1efca4cebd3 | -1.6745 | -52.43721 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 988fe5d9-d874-3022-a70a-1362ed38e613 | -1.73908 | -52.74657 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f81bc2d8-8f5d-39aa-8d3c-efcbb4a8a5d9 | -1.33013 | -51.95067 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 892b5273-f3d7-3e50-9471-6180948ea2ae | -1.78489 | -52.74103 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a32f4cc-4023-3bfc-a795-18aeaab68fcc | -2.53221 | -47.33187 | 2024-11-28 05:16:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 62f1814c-e910-3d42-9d2c-0fadc87848e9 | -1.62555 | -52.69849 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46bd419a-e587-30aa-8729-d3831015251d | -1.57552 | -53.74839 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca75cb43-0008-3eff-8a78-296bee3298c5 | 4.26121 | -59.98389 | 2024-11-28 05:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c77f80aa-b1c2-39ff-9997-1d962d5228aa | -1.10717 | -53.40023 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29936b0e-9318-3c0d-b050-b94a606498d6 | -2.84242 | -46.8379 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 059b3b4d-f6a1-3354-ba77-aa1db58991f9 | -1.59278 | -52.26519 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 870286dd-97f1-3d82-9293-98e7d49446ea | -1.79203 | -52.74977 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46321844-cc85-3fbd-b9f8-756c0396451a | -1.45636 | -54.51586 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bf7a0fe9-c288-3c1d-802d-22224227d28a | 0.35412 | -50.66638 | 2024-11-28 05:16:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 740ea9ed-2fb0-36e7-8a16-864ce31c6b3c | -1.70241 | -52.62572 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71b54f7c-5651-3122-9cf8-301f168fcd79 | -1.78075 | -52.74038 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3264c18a-28f2-3e1d-8ade-823cd99a4e0a | -1.5557 | -52.27974 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e1f7793b-d033-3990-abf0-1e937f74bdcc | -2.84576 | -46.87112 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 50960e43-3c5c-3356-97ae-f5120346cdfe | -1.37049 | -55.39615 | 2024-11-28 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 208b96b9-2f26-393d-9031-546c80e5da83 | -1.36012 | -54.653 | 2024-11-28 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5acc6620-6151-3448-8d11-31eb65d9b4c5 | -1.1708 | -51.93655 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be8a11ec-9315-3c07-9f67-46ab147c1152 | -1.44535 | -52.5999 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa586211-fce9-3962-8101-1510f3c4f0d6 | -1.21273 | -54.19279 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 905dad57-e5b5-3e3a-b1fd-701ca624273f | -1.70213 | -54.71933 | 2024-11-28 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| faed0da6-e8b6-3fb7-8d72-e9e72032094b | 1.44445 | -55.92854 | 2024-11-28 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9643e075-7abd-3da7-90e2-72b3f696e5d0 | -1.42488 | -55.25414 | 2024-11-28 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bef9e01e-9cce-3844-90ff-e48adcec8dba | -1.13028 | -53.64159 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b86ad43-d637-36c0-a92e-7de9106242d2 | -0.25483 | -53.76288 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27eafadf-2cda-36b6-b413-ec152d5ac661 | -1.56119 | -53.78997 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 35f52ce9-af6c-3826-88ac-6ab7935ca37f | -1.30734 | -51.92598 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8181cbd8-edfe-3b5e-8813-3d80a02d0a9b | -2.26832 | -51.23798 | 2024-11-28 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b2bdd0e-f85d-3a90-894a-c9eef5a5d304 | 0.97241 | -50.12755 | 2024-11-28 05:16:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 804dacab-29f9-3755-808d-1dcb80569a08 | -1.57908 | -52.00995 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a6d2ccb-d508-3004-8c1f-77d41817a851 | -1.15687 | -53.5721 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 19b1224d-2dd0-3db2-b242-47cfa31d647c | -1.31702 | -51.74672 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 47062359-1547-3344-bb3d-40a5d8dbe4da | -1.64507 | -52.46042 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 52e9a7c2-9587-38aa-894a-3819884de808 | -1.66585 | -52.7276 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 016cd461-412a-3a65-8840-f39954e458f8 | 0.97075 | -50.12372 | 2024-11-28 05:16:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ca6717dc-d324-392f-b45a-c83260171d0c | -1.78545 | -52.73729 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4bcefad2-95d3-3526-9308-f49ec8ad40b2 | -1.29239 | -54.55796 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19c0168f-ee0e-3986-9c3e-ce1628485927 | -1.35474 | -52.54014 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0448f6f8-9cb7-3867-81d1-b9926dc78960 | -1.7032 | -52.76002 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 788159bb-59f8-34d6-8a67-12e717e52c3a | -2.86739 | -46.842 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ca539ee6-b625-347c-86e7-db9dd3e17790 | 0.9877 | -50.2649 | 2024-11-28 05:16:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 30bb25b0-952b-3c64-b9ea-bffeec4435c0 | -1.19468 | -53.87814 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 619a1e90-fde1-3391-99b5-97090c096f9e | -1.16152 | -53.56774 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 655751fc-ff17-3ff5-b5bf-ea59643c9cbc | -1.64101 | -52.73518 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 979c22eb-7a1d-3a69-93e0-4c0026440e41 | -0.35746 | -49.95192 | 2024-11-28 05:16:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a59cef04-83bb-3dad-92b8-23fac4262109 | -1.58566 | -53.82497 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 290c1f49-28b4-31f0-bed4-fc183249cc75 | -1.92001 | -53.00484 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82b93455-0640-351e-8868-6e0021cc83a2 | -1.35563 | -54.63386 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9214bd43-d4d8-301b-8f3a-1bcf33224ba5 | -1.46877 | -52.68291 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f4cf71f-0e45-3ed9-9d6a-b47173808aa1 | -1.23681 | -51.79735 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7cd511ef-524c-31a3-a14e-348d3606e02a | -1.6919 | -52.49139 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 30a4041e-4d47-3365-ab86-dace3687ea37 | -1.81035 | -53.58179 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e56272b-30c9-3b89-ba1e-a25f47314dab | -2.85637 | -46.8429 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9cd390c9-6913-3b54-a06c-4f321b1eb3f6 | -1.22675 | -51.80447 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 650f59de-39b1-3f45-96c5-7980c116bcc9 | -1.13665 | -53.70265 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3dc2a013-d53b-3a32-b413-14be01d8346a | -1.27464 | -53.02398 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa657a85-f1c7-3955-a547-2abf7aa9062f | -1.3677 | -52.1219 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a531b28-40e1-350a-bb56-d69e0382e610 | -1.28812 | -52.10711 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fb024436-0fe5-3585-9417-46d157592d7a | -1.12388 | -53.7343 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5fa4bde6-a109-3061-b48e-e2eeb52288ea | -1.1242 | -48.33327 | 2024-11-28 05:16:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a2078ea-70e8-3ef8-8b70-9c9b085c7bcb | 1.45061 | -55.94596 | 2024-11-28 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7f9ace4-3bcd-3748-872e-8bf4bed47815 | -0.58375 | -51.70568 | 2024-11-28 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 45b9d84a-b150-3c6a-8acb-e29d37355644 | -3.38432 | -50.12244 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e093de27-0d5d-3db0-ab8a-563bfe423785 | -3.53213 | -50.7524 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8aa2bf7e-aaf4-38ae-bc87-8c14675901fb | -3.07069 | -50.98885 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bba34307-f2ac-3806-9ce5-5bfd61c23361 | -3.11084 | -53.25702 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b410b14-54ae-32a1-a6cf-9a06857a1469 | -3.4401 | -50.02691 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2726f79c-f7c5-3f35-9207-577eb5ee3855 | -3.7787 | -52.02723 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87fd7da4-72c5-3796-9c6b-d42e309c6400 | -2.72748 | -48.89685 | 2024-11-28 05:18:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a68042ca-9049-3d40-86e7-c51fbb84af16 | -2.80033 | -54.12317 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a1e97b7-8a14-37b6-9e26-e7be0b39597b | -2.25839 | -53.46309 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d18302e7-60a2-3ffd-96d5-64351df120cb | -3.95937 | -49.34774 | 2024-11-28 05:18:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48cbcfa7-7cac-3dec-a0d5-63209be7395d | -3.96564 | -54.61379 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3cad992-d70e-3543-8169-5516514e73d4 | -3.56779 | -50.23227 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d4f37975-2601-32c1-be16-2995895ef95b | -3.38775 | -51.23856 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58d127a9-2551-3595-b580-fa4e7a697884 | -3.96401 | -50.19076 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0f692b92-0369-30bc-92c6-6c7cc7e570d5 | -3.10923 | -53.26784 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30a56d30-e11d-3f78-a283-ac35c65e55af | -3.06077 | -51.05492 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b9748e7e-c574-3ec8-9d65-7ac66b137366 | -2.58501 | -54.06079 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6128857e-9d67-3b72-9bbc-0af6059d283e | -3.50235 | -53.81023 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fd5b24cb-9423-30a6-9b11-65285408081f | -2.65257 | -49.50651 | 2024-11-28 05:18:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5658f912-e569-3e04-8463-51e5a61f954d | -3.04982 | -48.51864 | 2024-11-28 05:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26d2f3b8-aed6-3bd2-9a05-b4627a339313 | -3.0532 | -48.52072 | 2024-11-28 05:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77cd1bfa-61c2-3041-baab-904ea9e21380 | -7.79784 | -49.99585 | 2024-11-28 05:18:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83a1feb6-3717-38e0-8ecc-0850d0c51eba | -3.43834 | -54.54114 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 777fc95f-0eaf-363e-9472-ec741987e221 | -3.04534 | -48.51017 | 2024-11-28 05:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d93dedb6-6f07-368b-ab1b-7865950b62dd | -3.69788 | -50.2203 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bf548f2-4aab-3069-8c1b-6e304470fe9c | -2.75484 | -52.10016 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ce713dd-56ba-3344-a588-019723317904 | -2.8916 | -51.58608 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0c00e191-e73a-305b-b6e1-ebfc4f87ce16 | -2.87296 | -53.91366 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1979bebd-fdba-30d4-b5e6-5264b2cb647a | -3.15538 | -50.14653 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b450932-37af-36cb-87d7-468a708b616e | -3.3856 | -50.11364 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 15e4cf07-e1a5-38e2-8eda-1289e12c07f7 | -3.70908 | -51.80184 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b7f70e8-6222-3877-a90a-d25b79640980 | -3.9197 | -53.67153 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fb535117-23b3-3e89-a45e-b227b55476cf | -3.78711 | -50.13023 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b04ec421-82e6-3386-beb5-e26ac050a170 | -3.2493 | -50.61687 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README80.md)
