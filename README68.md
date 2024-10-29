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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdd53e49-045a-3df7-a215-d0aee99e3c04 | -11.76176 | -55.45756 | 2024-10-29 04:42:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ba5cd05-ef2b-3c78-a77e-78d384eb4186 | -11.76116 | -55.46592 | 2024-10-29 04:42:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84a124dc-e113-3d76-afbe-94e7cab69799 | -11.76084 | -55.4627 | 2024-10-29 04:42:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 518c09e9-8a63-3ef0-bfb2-005e9d21a751 | -11.5601 | -54.4747 | 2024-10-29 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dfff5d35-8764-3461-87c0-2401df73a019 | -11.55637 | -54.47402 | 2024-10-29 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d8b72cb-f3a9-3c57-ad2e-be80817192eb | -11.39526 | -55.08699 | 2024-10-29 04:42:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea9e1a10-a334-3577-96bd-99e04faa76df | -11.39393 | -55.08867 | 2024-10-29 04:42:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c7a494a-c20c-3ea7-8dd5-c355f73b4d14 | -11.3521 | -54.48439 | 2024-10-29 04:42:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd48c301-ee12-3110-8994-8404021158a3 | -11.34758 | -54.4883 | 2024-10-29 04:42:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35986f6a-782a-3c07-80da-ae1c7fbe2bd6 | -11.32803 | -55.21601 | 2024-10-29 04:42:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 033d47dc-98bd-371c-92e4-e5e0747e8b53 | -11.32499 | -55.21029 | 2024-10-29 04:42:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47ebc354-9d11-3381-9c39-b7b0fd61fcb4 | -11.32413 | -55.2153 | 2024-10-29 04:42:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 261a0f4d-3c5c-3396-9038-54261d01aa4b | -11.32109 | -55.20958 | 2024-10-29 04:42:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59a4fc73-a4d3-395d-b7e1-2ea586a7edee | -11.31413 | -55.20324 | 2024-10-29 04:42:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf9d142c-56e6-3916-9629-2e06a83ddfd4 | -11.14647 | -53.94424 | 2024-10-29 04:42:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5cb40e08-9f7c-31c9-814f-231493f97714 | -12.09821 | -56.82909 | 2024-10-29 04:42:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3ebf112-d58c-32c7-9b6a-42c4eee0ea1f | -12.09392 | -56.82835 | 2024-10-29 04:42:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea376e10-78f8-3722-93fd-5a1d42e130e2 | -11.17532 | -56.29074 | 2024-10-29 04:42:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0192048-fd69-3f1f-844f-dbec2b1a17dc | -11.17111 | -56.29001 | 2024-10-29 04:42:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5dd09183-1086-38d3-9637-608c4ec1aafb | -11.16691 | -56.28931 | 2024-10-29 04:42:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 48fc4e01-3d48-3e05-9351-0ef49a3e3e18 | -11.16622 | -56.29327 | 2024-10-29 04:42:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| becee602-6ed9-3139-8ad4-cb0e7ad880d1 | -11.12704 | -56.29434 | 2024-10-29 04:42:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5036e2e-111c-3c00-b8f3-053328d17da3 | -11.14028 | -55.52851 | 2024-10-29 04:42:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1b94a9e-9c37-30fe-b40d-f40841f83d2f | -11.13965 | -55.53208 | 2024-10-29 04:42:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 037e17e4-023e-3285-9456-617226d402c9 | -11.13903 | -55.53564 | 2024-10-29 04:42:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e69926f6-0441-3116-b1df-bb31e6adc287 | -11.1384 | -55.53922 | 2024-10-29 04:42:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| a4cac2ed-0838-3416-8dc5-fbb3b5283edc | -11.13777 | -55.5428 | 2024-10-29 04:42:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4b545866-cb12-3805-80d8-a8735ecca74b | -11.13715 | -55.54639 | 2024-10-29 04:42:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ece7d89-eb8a-3f63-b380-61472e15f1be | -11.13628 | -55.52783 | 2024-10-29 04:42:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5918cb78-5c37-3beb-895b-97d84dd22f16 | -11.13565 | -55.53139 | 2024-10-29 04:42:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| edd5ee6d-ccbb-3138-9635-80ac734fceb3 | -12.79221 | -57.02078 | 2024-10-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6cea387-5125-3564-8b6c-d4f8a3c1ebe6 | -12.79056 | -57.01957 | 2024-10-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abad6f03-b6e0-383e-a612-cbf6821c6c17 | -10.84891 | -56.91486 | 2024-10-29 04:42:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 332a26e8-6f3d-39d3-9eb9-57519fd9a357 | -10.84814 | -56.91922 | 2024-10-29 04:42:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 27f1d795-a5cb-3e00-bbf9-df1ceafa5e2d | -10.84814 | -56.91778 | 2024-10-29 04:42:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7ec00de4-4b7f-34e3-9d68-7ceed734abfd | -10.84734 | -56.92214 | 2024-10-29 04:42:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 990d87c2-c6c3-3ec1-9f5c-278f4bbf2fe5 | -10.59639 | -57.79625 | 2024-10-29 04:42:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49f7a432-08b0-3dc2-9a9d-7e33e6d91aaa | -10.59546 | -57.8013 | 2024-10-29 04:42:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f85b385-89b2-3b3f-ac6d-bd7a4bdf224a | -10.59398 | -57.79757 | 2024-10-29 04:42:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7cdf16f8-6ebf-388b-a2fd-564b01bfa6a1 | -12.20754 | -57.22449 | 2024-10-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 782ddd6b-87a1-3297-856b-99a3784136ff | -12.20717 | -57.22728 | 2024-10-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55444b27-dd51-3811-9b4d-e44829f97a47 | -12.20314 | -57.22373 | 2024-10-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12b176b6-26b9-3ef3-a43f-fe08876d8b12 | -12.20237 | -57.22807 | 2024-10-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d87e3bdc-d29a-3e8a-b29e-c1826feb9485 | -10.98497 | -56.914 | 2024-10-29 04:42:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21af190c-bd69-38ca-865e-474193137a61 | -12.3041 | -58.15398 | 2024-10-29 04:42:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c99b20aa-6515-31b8-b646-ff9eaae80c97 | -11.48566 | -59.09749 | 2024-10-29 04:42:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22da55fd-a753-3c3f-b5ee-f59b62550b0f | -11.48062 | -59.09659 | 2024-10-29 04:42:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a1cb539-8321-3aeb-92d7-f4cf709400ba | -22.55766 | -47.70429 | 2024-10-29 04:44:00 | NOAA-21 | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 103967f0-0e34-303b-b4a4-a1b8ea6c6a97 | -19.48169 | -56.64435 | 2024-10-29 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6aee86b5-baa6-337b-b0f6-28af7be0fe42 | -25.18956 | -52.78891 | 2024-10-29 04:44:00 | NOAA-21 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f16cfb3e-7ea4-32ac-8f8f-95a6292d369b | -24.87087 | -53.47952 | 2024-10-29 04:44:00 | NOAA-21 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 6d72211b-5bab-378d-bef7-3101f4155be5 | -21.80728 | -53.49295 | 2024-10-29 04:44:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4088b8a5-4794-3682-bc11-9712a0a83e77 | -21.80396 | -53.49234 | 2024-10-29 04:44:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd804cda-016f-31f1-aab0-b8cac9a466ce | -21.80337 | -53.49606 | 2024-10-29 04:44:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 73f4c0d3-9872-3e27-9dcc-cd90ea14d025 | -22.96008 | -54.904 | 2024-10-29 04:44:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 85b02194-3c64-3e5c-bf57-207b3b346a04 | -22.68765 | -54.65728 | 2024-10-29 04:44:00 | NOAA-21 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b2555b73-fa2c-3eb0-bf68-b8587955b8ed | -24.00997 | -54.12713 | 2024-10-29 04:44:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6c250e49-0980-3c0c-9d6f-89f7b549d066 | -24.00727 | -54.12272 | 2024-10-29 04:44:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| a7ebb6ba-fd22-3a1f-b912-79101a06c96b | -24.00666 | -54.1265 | 2024-10-29 04:44:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 217bb3bb-e81a-3639-aa37-4b77ca27d3ac | -24.00456 | -54.11831 | 2024-10-29 04:44:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a6636644-bfb4-306a-a8d9-2a2acb426d87 | -24.00395 | -54.12209 | 2024-10-29 04:44:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 1ac5c009-c163-34d7-8bec-0d9da2e42ab4 | -24.00334 | -54.12587 | 2024-10-29 04:44:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 7d70c7f4-84fb-3372-8b3d-249e70b76ddc | -24.00064 | -54.12146 | 2024-10-29 04:44:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 8d1dcf98-e1f5-308e-b814-4a32e8762ce8 | -24.00003 | -54.12524 | 2024-10-29 04:44:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 9c40e23b-9791-30f7-9c6e-39c9ebe2d403 | -23.99793 | -54.11705 | 2024-10-29 04:44:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| d721fb3a-9385-371d-9880-fe14ce4fed20 | -23.99732 | -54.12083 | 2024-10-29 04:44:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 6faa5793-c947-3693-926a-a1573b116f45 | -19.50988 | -56.59534 | 2024-10-29 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 1839b425-0919-3b09-86a6-3b36475dd051 | -19.47505 | -56.63805 | 2024-10-29 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 4efd8c92-c79c-31cc-b70e-f3cab685ddb4 | -19.61712 | -56.69371 | 2024-10-29 04:44:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a61bf064-cd4f-3a94-a41f-0ed256009ffc | -19.61679 | -56.69624 | 2024-10-29 04:44:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 14cece41-998f-32f6-862d-11864b182501 | -19.61627 | -56.69853 | 2024-10-29 04:44:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8e672c2c-4e3f-349d-80a9-f7f4349c6e92 | -19.61502 | -56.70587 | 2024-10-29 04:44:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 407ef20e-4f53-30c9-a764-54ed2e6b5fa4 | -19.61165 | -56.70261 | 2024-10-29 04:44:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| dbd70f46-c90f-366e-a5a7-2d2c489fbbd6 | -19.60037 | -56.70035 | 2024-10-29 04:44:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e2af5252-48e7-3002-a6b8-e090599f684e | -19.5995 | -56.70518 | 2024-10-29 04:44:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d934ebdd-cb86-3615-9063-8a90dc910470 | -19.59661 | -56.6996 | 2024-10-29 04:44:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9f66d726-49ea-3546-9b9a-afc00d5ec6ba | -19.58735 | -56.70775 | 2024-10-29 04:44:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4a7e2a6f-a010-3cc5-b9c0-e52af98c2ae7 | -19.51073 | -56.59055 | 2024-10-29 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| afbbba92-c1d6-352b-b9ac-0496de2a7d05 | -19.50613 | -56.59459 | 2024-10-29 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 2d8e2045-9910-3aa4-90b6-32a4c830f4ce | -2.6666 | -49.2673 | 2024-10-29 04:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| dbf4b086-f4bd-3c6f-9138-e4dff19b00fb | -2.6667 | -49.246 | 2024-10-29 04:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 178f9cd9-d1e3-336e-9be8-ee6c9d295c70 | -2.8145 | -49.2418 | 2024-10-29 04:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ec6b8f67-6ff5-36f4-91a1-fa6dfaa6624a | -2.8146 | -49.2206 | 2024-10-29 04:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 959d56bc-5c77-3b33-b6c1-1cbf696c304c | -2.833 | -49.2413 | 2024-10-29 04:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 8cd5aa9b-9941-3de3-b43c-a0871fb8733f | -3.1794 | -50.3922 | 2024-10-29 04:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 2f460772-55f7-3b0c-88c0-ea74115caf99 | -3.1097 | -54.2865 | 2024-10-29 04:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 2013feb9-dd1b-3af0-ac7b-63e7053c005a | -3.2503 | -46.8709 | 2024-10-29 04:45:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 0fc8299d-8159-32f4-a137-9a4cfb83d4ac | -6.137 | -42.507 | 2024-10-29 04:45:40 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 48.3 |
| 1f572d33-06c4-31a7-b81e-1024b9333eb9 | -3.96132 | -46.39965 | 2024-10-29 04:46:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 27.5 |
| d35ed327-c4b2-3047-86aa-3e2689dbc0ed | -5.28245 | -43.41401 | 2024-10-29 04:46:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a6792245-e453-345b-8d3e-97ad3b4f6f8e | -3.25702 | -46.85412 | 2024-10-29 04:46:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 50fda608-5ad8-35eb-8969-434cceb8d8ed | -3.25396 | -46.84615 | 2024-10-29 04:46:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| d4fce428-5e07-3657-bb9f-096d59f6a362 | -3.25111 | -46.8905 | 2024-10-29 04:46:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 12b0e7c1-77d8-318e-aae1-4dee03d1fe99 | -4.34954 | -46.77671 | 2024-10-29 04:46:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 30.6 |
| ed0ba977-2342-351a-8ca7-1c796f82462e | -3.24831 | -46.88247 | 2024-10-29 04:46:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| e58cd1c9-8961-3008-b36a-aeb162d2da06 | -4.43016 | -47.59862 | 2024-10-29 04:46:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| e1b6c1ac-0a12-33a6-8bdc-bf8ad59f1fdc | -2.52175 | -47.44868 | 2024-10-29 04:46:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| b1649ba9-7b9b-3298-803e-4e08aaec3ec8 | -3.95531 | -46.40342 | 2024-10-29 04:46:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 48714c1b-86ad-34fc-8dc6-c0a42e9e2ea9 | -29.12374 | -51.74413 | 2024-10-29 04:46:00 | NOAA-21 | MUÇUM | RIO GRANDE DO SUL | Brasil | 4312609 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1149efc5-5ba0-3f78-818f-5664443e7287 | -29.81463 | -51.17621 | 2024-10-29 04:46:00 | NOAA-21 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |


[Clique aqui para ver as próximas entradas](README69.md)
