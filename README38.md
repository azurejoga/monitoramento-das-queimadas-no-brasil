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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 421ff613-f85e-355f-8cae-ff3bab0d21a3 | -2.13889 | -47.98918 | 2024-10-17 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6687d24d-3e2d-3a6e-8ee5-9b432b148844 | -1.87776 | -47.88698 | 2024-10-17 05:04:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b70ff585-953e-3a22-8f3f-437f29f74207 | -1.87081 | -47.80895 | 2024-10-17 05:04:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae2828b2-2f9b-34f1-b7a7-88d8b4e3e64e | -1.74841 | -47.37925 | 2024-10-17 05:04:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bdf09b47-6e81-320d-ad6e-ed032249e1a8 | -1.25137 | -47.83339 | 2024-10-17 05:04:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05e0f810-a9ab-319d-8ebd-93559403c2f2 | -1.23721 | -47.71255 | 2024-10-17 05:04:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d310779-fae2-3d65-a0aa-e66a487a87e6 | -3.46519 | -47.66993 | 2024-10-17 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 0600a491-f2ef-3ba3-b7b6-d4dd10ff53e0 | -2.63319 | -47.63375 | 2024-10-17 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 25c5ac84-de7d-324b-af80-440a2acb26eb | -2.63078 | -47.63604 | 2024-10-17 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83628278-2383-301c-b102-c8bf9dab55d6 | -2.40861 | -47.64458 | 2024-10-17 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03ae1c78-db92-3e80-bbe4-76c2f264bda3 | -3.69821 | -47.62113 | 2024-10-17 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6981c9d8-24a7-33d3-9611-110ecabe59c8 | -3.6982 | -47.6201 | 2024-10-17 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14cdb4a9-7672-3af8-96f7-2fcc35eeb262 | -3.69741 | -47.62537 | 2024-10-17 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73e57265-23aa-389f-9ded-32ac95f81cbf | -3.5237 | -48.05936 | 2024-10-17 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21c0d792-5293-3566-8a0c-f0036dc4c1db | -3.25798 | -47.98106 | 2024-10-17 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df97fd6e-61d6-372a-940a-34085358fd7f | -3.22196 | -48.92299 | 2024-10-17 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba9c01be-79a7-332b-9c12-8aa48ab6d990 | -3.21763 | -48.92231 | 2024-10-17 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| d16eb8a4-82d8-3d12-b9a4-1abbabe9f647 | -3.16552 | -48.37387 | 2024-10-17 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 906e26bb-5033-3a08-8885-d9b49519f9fb | -3.16332 | -48.37174 | 2024-10-17 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd045fbc-8caa-3feb-8fcb-5f4075b452b4 | -3.11395 | -48.1308 | 2024-10-17 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52f05a6b-ece5-363e-b1eb-85c2938d6e33 | -2.9731 | -48.0048 | 2024-10-17 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d0d4728-8372-3f37-ad8e-7e7a19ce9a15 | -2.97067 | -47.98977 | 2024-10-17 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 17ef6660-c131-339f-a6e0-2ad99ca9071a | -2.96995 | -47.99448 | 2024-10-17 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 4c57ae3f-02ad-3c71-8474-3f1a613d6b65 | -2.96923 | -47.99928 | 2024-10-17 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| a8a8c48b-7538-385a-898b-86625b20bcf0 | -2.9685 | -48.00409 | 2024-10-17 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 7b6313e9-81ad-30a6-88b3-6020156fe091 | -2.96535 | -47.99377 | 2024-10-17 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| a5dd19f9-acd6-3aff-a33b-cecd970ca9ac | -2.96074 | -47.99305 | 2024-10-17 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a76847b-9309-392b-b58f-beed44c7bf0a | -2.91204 | -48.76521 | 2024-10-17 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fdc9879f-89bb-37ed-84fb-a3e4b06bac02 | -2.46219 | -47.84329 | 2024-10-17 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 656834b7-6468-39ab-b253-edf8c8d848cb | -2.46203 | -47.81341 | 2024-10-17 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e2f74d3-825d-3cc7-b152-186cf090eac2 | -2.45128 | -48.50268 | 2024-10-17 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fd92f6a-b30b-3fed-88bb-a84512ac5115 | -2.42877 | -48.30017 | 2024-10-17 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3adcf9c-a73e-36ac-af85-aa31de6db24f | -2.4273 | -48.51214 | 2024-10-17 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94faac1b-e536-392a-a71f-420b14c0e440 | -2.42694 | -48.30161 | 2024-10-17 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99357588-6853-37e7-a00b-0785246830a2 | -2.42665 | -48.51644 | 2024-10-17 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e362ee43-c994-3b0b-9b6d-998b1339ebac | -2.42589 | -48.24659 | 2024-10-17 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7f5e2962-8401-3d90-9d1e-491a5cd336b7 | -2.42453 | -48.11942 | 2024-10-17 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07b23938-cd8e-3a39-b44c-d74670b667ea | -2.42366 | -48.24461 | 2024-10-17 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f5602cf5-4fcf-3b89-acab-8fe7368a4ce6 | -2.42307 | -48.62932 | 2024-10-17 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c1d8495-8699-3183-b0c2-4c4b191f3762 | -2.42289 | -48.51147 | 2024-10-17 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f6ed557a-e84d-3fa6-ab59-a7f1433dbbc6 | -2.39187 | -47.72191 | 2024-10-17 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c9a9a1a-4e54-3742-9351-e57d3add1778 | -2.3908 | -47.7183 | 2024-10-17 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c9f76e3-2829-3a3f-b417-1717fec76020 | -2.39008 | -47.72321 | 2024-10-17 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50ec2d7c-63fa-362f-9a22-bda5260c0939 | -2.3872 | -47.72127 | 2024-10-17 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8db16d5b-a81d-3297-afc5-80d85f19850a | -2.35727 | -48.28907 | 2024-10-17 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cca7d94-befb-3178-87df-c2a0a02afa5e | -2.27677 | -48.43609 | 2024-10-17 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae9777b9-c72a-388c-b3ef-0805028dc3ee | -2.21066 | -48.19303 | 2024-10-17 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c733881-e877-3cd5-89e8-521515c2542d | -2.63156 | -47.63103 | 2024-10-17 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2fca21a8-254c-34a0-95f7-764128cd764e | -2.61001 | -48.25955 | 2024-10-17 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7ae18b34-6862-35e1-909f-8ae8d4ac6cd7 | -2.6062 | -48.25432 | 2024-10-17 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| bfe3d4ac-eee5-30f6-a23b-def658ed5928 | -2.60551 | -48.25885 | 2024-10-17 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| e11eaf89-17f8-35c5-a2bd-028cbe985682 | -2.60482 | -48.26344 | 2024-10-17 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| ad944350-ad83-3f72-9a88-788cb53a799e | -4.72113 | -48.30297 | 2024-10-17 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 92e8eb1e-24f2-3c82-830f-c25e3933e182 | -4.51126 | -48.79559 | 2024-10-17 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b18d0a51-9769-3b5c-b218-95b7fe9771b1 | -4.5106 | -48.79993 | 2024-10-17 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f3cc6668-15fc-31e3-b0b7-df80e61513a2 | -4.50954 | -48.79807 | 2024-10-17 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1a0aafbc-a05c-3c19-98e1-1c48f77920ce | -4.50614 | -48.79928 | 2024-10-17 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3294eda9-61b1-3b36-b689-aab63a73e2bb | -4.50507 | -48.79741 | 2024-10-17 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7b3b029c-8d71-3199-b1eb-a9a1425b776d | -4.47186 | -48.12127 | 2024-10-17 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3525673-c48f-36f8-a893-489dc78f27f9 | -4.29625 | -48.0758 | 2024-10-17 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48b317d7-d19b-3ae4-aeb1-a0ccfe57901a | -4.29455 | -48.07289 | 2024-10-17 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33980bd4-c262-3ce4-a8fc-02666fd6a892 | -4.28935 | -48.62098 | 2024-10-17 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cff55bcd-dd2d-35a6-a2e8-572c716cc54a | -4.28868 | -48.6255 | 2024-10-17 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ed957b6f-d651-3818-b64d-e8cc42e5864a | -4.28284 | -48.22057 | 2024-10-17 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cbcc25b-2b70-309d-9f31-581e1f5a3b66 | -4.26856 | -48.00487 | 2024-10-17 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4e1a9e8-dd2f-37f3-98e2-93b6d2403298 | -4.14708 | -47.86763 | 2024-10-17 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c528d2b6-c5b3-3f8a-9709-6ef8f318c12b | -3.92682 | -48.34821 | 2024-10-17 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| d7e349f9-7be2-38af-91ee-52a850807b4e | -3.92645 | -48.34563 | 2024-10-17 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a7932ae8-b1bc-3a76-ab57-37d7fbfe0642 | -3.92575 | -48.3502 | 2024-10-17 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 75d7c0db-8128-3da4-89bc-9fcadb910f8d | -3.90434 | -48.33757 | 2024-10-17 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 09ee6797-cd0c-33ba-ad6b-ae077977b197 | -3.9002 | -48.36506 | 2024-10-17 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1366f4ed-bb7e-37c4-8419-0325255f5bff | -3.89978 | -48.33682 | 2024-10-17 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f6ddef83-b06a-3e91-88ec-a22cf442466f | -3.80002 | -47.78795 | 2024-10-17 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 986cfb25-a3f3-3c76-931c-2a6c8c5b939d | -3.7642 | -47.73613 | 2024-10-17 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a361541-1ee5-3bad-9c4d-b7e493724618 | -5.66557 | -48.67976 | 2024-10-17 05:04:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6c9263d4-3d8e-31a9-a7cf-7b812b5255f0 | -5.66489 | -48.68446 | 2024-10-17 05:04:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2c9675ef-f99a-3c0c-8584-ba3a1f764f6e | -2.58074 | -48.95913 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| da22aa61-1e30-3ccf-a36e-cd6f76f19e8e | -5.2267 | -47.95437 | 2024-10-17 05:04:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1cfc3009-45e1-38f8-8abd-bea1a92a292c | -5.22596 | -47.9595 | 2024-10-17 05:04:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 44385343-4e3c-3050-a236-111d7eb96fed | -0.75948 | -48.68913 | 2024-10-17 05:04:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c720a3c-3827-3c66-97a7-d7f05a3e59c8 | -0.75887 | -48.69308 | 2024-10-17 05:04:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5063688-cda0-301a-b6af-0ff54662f721 | -2.17095 | -48.83547 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07cf0b6e-e647-3155-8463-0bda81e08eaa | -2.14829 | -48.84015 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 019b31b8-5655-3921-b942-cd3b6e892875 | -2.09819 | -48.97273 | 2024-10-17 05:04:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7f257172-936e-35a3-af2e-686b60ee7310 | -2.09746 | -48.97577 | 2024-10-17 05:04:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9ab84adb-ae8e-30ce-8b67-42fe458372a4 | -1.13763 | -49.16186 | 2024-10-17 05:04:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e64d6f95-47e0-316d-a849-4b8cf34c9bb8 | -1.13407 | -49.15747 | 2024-10-17 05:04:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8d5d11cd-1288-3aa9-ae6b-247668437aaf | -1.1241 | -49.16735 | 2024-10-17 05:04:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca5a6962-fe02-3088-9e70-7a122d0df216 | -1.12353 | -49.17107 | 2024-10-17 05:04:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 715170f2-18ef-306f-b1cc-35e2eb054b10 | -3.29246 | -49.46304 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee48281d-5fa8-30b6-bae9-730f1838d230 | -3.28935 | -49.0784 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c7a8e306-66cd-3ee0-b24c-8c08427bbc9a | -3.28505 | -49.07778 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e9919e4c-1e57-3775-850b-b88392dbf497 | -3.27167 | -49.09015 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 080f75c6-ace6-3056-aaba-4d7da86bc027 | -3.27104 | -49.09423 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 804666ee-e1d0-3be1-8707-bc236ffbbb5f | -3.16494 | -49.53388 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d642260f-319a-3c16-9f5f-95ecf8be1864 | -3.16079 | -49.53323 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75d708de-798d-3675-b5fc-5052eae0e7ec | -3.15301 | -49.21129 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e99b959d-a252-3ef6-9ddc-bcaff1642d0d | -2.52056 | -49.82642 | 2024-10-17 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41aabe06-3f81-3a02-b964-533110fb6bf6 | -2.51393 | -49.75678 | 2024-10-17 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c44d7028-cad6-35e3-b665-9f228d8c168d | -2.50445 | -49.90685 | 2024-10-17 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README39.md)
