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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2dbce9bf-64c0-3bb6-b2c0-07ba78f00e4a | -6.68535 | -43.68861 | 2025-06-15 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 235396a8-d867-381f-9e8f-6b72b50a148e | -9.11094 | -49.63556 | 2025-06-15 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08c8cff3-ae43-3127-a5e2-aaf602f407ee | -7.23671 | -44.15405 | 2025-06-15 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cf9296db-9935-3e9c-b582-c2952c2875e0 | -11.00603 | -55.07851 | 2025-06-15 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2c4150e2-1990-3bc2-aea9-d4852422750a | -7.20826 | -43.11243 | 2025-06-15 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 85c91c16-a2af-3ca2-b42b-086d638b988b | -6.69087 | -43.68409 | 2025-06-15 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3d656a87-b9a8-378a-b746-125017a40e65 | -12.77049 | -44.41023 | 2025-06-15 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c8fcdcb5-e37e-3cf8-8150-232b216dc83e | -10.62226 | -54.91703 | 2025-06-15 04:46:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91efa08a-4973-31b4-b7ff-bcaf656200d2 | -9.03985 | -47.02831 | 2025-06-15 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea6b999e-eb49-37ae-93c6-9e1cfdcd294b | -7.20949 | -43.10381 | 2025-06-15 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f7df5dd9-f4eb-32d9-a161-82b85ec4172b | -8.59218 | -45.86168 | 2025-06-15 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a6e047c6-d8d3-34c2-9735-c717132e0c02 | -9.68144 | -48.60995 | 2025-06-15 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f200ca70-df19-3937-96f2-b4ea43c8744b | -7.23739 | -44.14923 | 2025-06-15 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5dd9b423-1be5-380e-a867-421a567b608a | -9.04056 | -47.02323 | 2025-06-15 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cfb6ffc8-03aa-39af-83de-1bfb39a794ff | -10.63233 | -49.42923 | 2025-06-15 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2f9d7d8d-2f7e-3dee-b391-27664c349c08 | -10.91807 | -54.75504 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f0db93b6-0704-3405-baba-e10cea91f9c2 | -9.90544 | -56.05329 | 2025-06-15 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57cae446-6314-3179-a40a-969774c285bf | -10.91894 | -54.77147 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4df151a8-4049-344c-9d1f-9154d46c937f | -10.74481 | -48.57323 | 2025-06-15 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f1ce7e9-5dc1-3e4b-ac68-540fea9bad4b | -11.78393 | -54.77148 | 2025-06-15 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e918c08f-145f-34d7-9f05-2393434b8582 | -11.75525 | -46.74892 | 2025-06-15 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 183f58cc-e95c-3368-8505-cc1e854e9357 | -10.74849 | -48.57378 | 2025-06-15 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62d6eede-1842-3ca3-b043-774a4727f181 | -7.4469 | -44.82518 | 2025-06-15 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a55a585a-ad38-31cd-a6d4-318b3f36c198 | -10.27604 | -47.61212 | 2025-06-15 04:46:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 404dbb70-9278-37f8-8e54-91090783f431 | -11.01311 | -55.07973 | 2025-06-15 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a447e59-d730-3777-82ec-7f0b08e1c274 | -11.01244 | -55.08382 | 2025-06-15 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61a1d05c-086d-3c3d-83c6-0fc365c3850a | -9.41187 | -48.43039 | 2025-06-15 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34421694-4249-3d38-bd32-6f8dedf7d90e | -12.76978 | -44.41592 | 2025-06-15 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ad0a4fe6-96d7-3dd0-a347-577abab64990 | -11.0089 | -55.0832 | 2025-06-15 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ba3db7ac-675d-3d9c-8361-52517ab6610b | -10.0945 | -52.74021 | 2025-06-15 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6c9aea6a-1757-307a-aff7-031879bd38d7 | -10.72106 | -46.55706 | 2025-06-15 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf3e6bef-ae64-356e-b2a8-4700c0882585 | -10.9161 | -54.76692 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 10e417f6-06e2-3302-a9c0-f2ec63c1aef7 | -9.41062 | -48.43897 | 2025-06-15 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53ac068f-0ff8-360f-9445-8de363e50d31 | -8.5916 | -45.8658 | 2025-06-15 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4a747f9-95b5-3a61-bb9c-abbf404bb5ac | -8.07707 | -43.11483 | 2025-06-15 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 7c9b36aa-82f8-3831-b46d-86ff5c5e0e0a | -10.91042 | -54.75783 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3994db47-f2c1-3f6f-9f3c-91cb485e716f | -6.68659 | -43.68429 | 2025-06-15 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b9a55bfb-8b0a-39bc-b941-4fa5148c820a | -8.58737 | -45.86528 | 2025-06-15 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fe0158e-e4a0-3c5b-99a8-b72b4dcce46d | -11.00957 | -55.07912 | 2025-06-15 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 62f4e0e4-7afa-3e68-920e-488cac545eae | -10.71815 | -46.56196 | 2025-06-15 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10917c7c-d9c0-3bdd-a5fc-c6c7eddf2332 | -8.37496 | -47.0553 | 2025-06-15 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc35b50f-6714-3571-ac97-984350098607 | -10.63293 | -49.42524 | 2025-06-15 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| faaf347b-5235-3380-b774-e03d07f86ecd | -9.41602 | -48.45289 | 2025-06-15 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 99f4b356-7042-306c-9c10-70b574af783b | -11.89079 | -47.46033 | 2025-06-15 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dadb6bd6-b46e-3659-b8b0-75a5a17c4234 | -10.85743 | -47.23441 | 2025-06-15 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1755bbd2-512c-3f2b-bbe8-5226da31ccc6 | -7.20785 | -43.11532 | 2025-06-15 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f4b75974-9d71-338a-9968-196a41a68571 | -10.04021 | -46.59146 | 2025-06-15 04:46:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29d29fb0-8ed3-39b1-bd97-4846a7b2c167 | -12.23457 | -44.16663 | 2025-06-15 04:46:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33d9c8ea-74bd-3e21-8967-eb689246c3ef | -7.23141 | -44.15799 | 2025-06-15 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 445021e3-cd4d-3135-a47c-19ca532d29a7 | -9.42329 | -48.45399 | 2025-06-15 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d0cea01a-0045-311c-a7b0-ba455bd3f9f0 | -11.57352 | -47.87177 | 2025-06-15 04:46:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fb534b69-0caa-37a7-8ace-3b3131d99280 | -9.41965 | -48.45345 | 2025-06-15 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a01e0550-c134-3fe6-af20-3b64a9b0f468 | -6.68609 | -43.68348 | 2025-06-15 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 17dce037-38f4-3d86-8581-a1c7c0d2465a | -12.76484 | -44.41525 | 2025-06-15 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e9681730-10c1-343c-b614-142183213211 | -12.76625 | -44.40384 | 2025-06-15 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8ef39c6f-15fd-3daf-af52-0c6d8299acad | -10.91544 | -54.77091 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b43fdae2-cf69-3006-8439-50476457aa0c | -9.27391 | -47.32444 | 2025-06-15 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d880ec28-cf10-3fed-9c85-274f8451589b | -7.23603 | -44.15888 | 2025-06-15 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c3bbd6f6-e6fc-37dc-8120-878180b2c3f0 | -10.85258 | -53.78444 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d523405-0c49-3d18-beda-166844b59729 | -10.24216 | -52.23674 | 2025-06-15 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 33b1843d-e157-34f9-84ee-48a3005f7906 | -10.52793 | -47.83086 | 2025-06-15 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75e0ed17-b414-3e61-9e98-a0d4eb67a0b6 | -10.51177 | -53.58197 | 2025-06-15 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ec361218-7f81-3811-98f4-f04530d3fe23 | -6.44507 | -45.72901 | 2025-06-15 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 447941fd-41ac-3189-9206-79976fe43662 | -12.0926 | -49.48938 | 2025-06-15 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 799f0ad3-872c-3d9c-8527-51de834ee606 | -10.91326 | -54.76237 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 64d89340-0881-3675-9513-105b067ee224 | -9.04904 | -47.91653 | 2025-06-15 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3467f02-c7ab-33a0-9cfe-a2b7dc0f0cac | -6.87193 | -47.2341 | 2025-06-15 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b334ac4e-7c0f-3185-bf8f-42aed92359e8 | -6.68589 | -43.68943 | 2025-06-15 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 72163154-a58f-3cde-9bc3-518661b11a4d | -10.8504 | -53.77651 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d679633d-9ac5-3772-a5fd-6d31620cce80 | -7.2084 | -43.11428 | 2025-06-15 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7b52780e-b869-39bd-998a-a1246d1c8d7b | -7.20867 | -43.10955 | 2025-06-15 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c0609e95-8215-3667-b461-552c5cd02120 | -10.92092 | -54.75956 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d433430f-a275-353f-9735-51b84372771f | -8.07746 | -43.11184 | 2025-06-15 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 398eac32-2506-3cef-9244-d23379aa08de | -9.41664 | -48.44863 | 2025-06-15 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c95973f3-5c5b-30cc-ab92-c85287463e1d | -10.93202 | -56.83504 | 2025-06-15 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52d23a38-3a16-3ad1-972e-d06252b1d9bb | -8.31561 | -46.20119 | 2025-06-15 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 65633c56-774a-34e4-937c-0d10f5533774 | -7.11303 | -43.43132 | 2025-06-15 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9c6fa98e-4b19-3a58-a6fe-d86bca45863e | -7.23534 | -44.16372 | 2025-06-15 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1bebc165-a850-3996-bc1f-8e96d12c428f | -10.64314 | -47.48009 | 2025-06-15 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f806a8c-86b5-3533-a5b8-6323d936436f | -10.29786 | -56.97601 | 2025-06-15 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 293ca990-fe55-34c9-b52a-59f0e9fec9db | -10.38356 | -53.5088 | 2025-06-15 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b12ea010-676b-37c1-966b-b2688237fdfc | -10.91392 | -54.7584 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 79f0f27e-fd27-3402-8136-a3d150fcf5d8 | -11.19055 | -44.49057 | 2025-06-15 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9d5ab1c3-9e19-31ed-a011-77b3a04d6f0a | -10.04379 | -46.59577 | 2025-06-15 04:46:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| baa37451-c33f-3eff-9e7a-63be9562c41b | -11.19126 | -44.48521 | 2025-06-15 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b04c1ad3-1362-3207-9b34-d4f0d10ed8b6 | -10.92026 | -54.76352 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bb6a7b27-e41e-3d0d-a390-36792f8e8cd2 | -11.18645 | -44.48454 | 2025-06-15 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1d442f0b-066d-3f1c-81c3-4928095dacc6 | -10.92247 | -56.84383 | 2025-06-15 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 692de1cc-9380-393b-a1fe-2cf505ef3a0d | -10.92812 | -56.83434 | 2025-06-15 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd502a4e-51ed-3507-9cb6-bdd45edb8f52 | -11.0067 | -55.07444 | 2025-06-15 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 33778ab4-8a48-392f-bafb-81049d916e0c | -10.71869 | -46.55817 | 2025-06-15 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a93a9b74-1150-3bc8-aac5-eac584e46389 | -7.20327 | -43.11166 | 2025-06-15 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9a99431f-8bc2-3664-8150-a077ddb72100 | -9.42392 | -48.44973 | 2025-06-15 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| aca29ef6-7441-3217-afb3-33ed7bb2514a | -11.13762 | -53.91426 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbae9fa1-c24e-304b-b884-967b870f9676 | -9.04969 | -47.91199 | 2025-06-15 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9331200a-5346-3cbd-a1d7-8aa3cb8fa99f | -10.56928 | -52.01812 | 2025-06-15 04:46:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 778422ed-9544-334d-ba6e-3e7898d7a5c7 | -10.04327 | -46.59944 | 2025-06-15 04:46:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e90c0a2-e53d-3d11-b4d2-208e6e87ac0b | -7.10816 | -43.4306 | 2025-06-15 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b8b36a30-829e-3108-a10b-8cf0c7c156b3 | -11.01379 | -55.07566 | 2025-06-15 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68d78635-aff2-371d-ab41-24e482857642 | -10.91742 | -54.75898 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README10.md)
