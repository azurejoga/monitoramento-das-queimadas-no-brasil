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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 408fbeb5-2a94-34b0-946f-de5dab44c5c0 | -11.119 | -53.9446 | 2025-06-18 05:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 97b55a82-f48e-3c91-ba80-6a548879f897 | -11.1382 | -53.9223 | 2025-06-18 05:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 96170891-dc61-3408-9b59-5b38d3930e36 | -11.1379 | -53.9429 | 2025-06-18 05:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 8f7d8e99-7301-39ab-bd73-f9c02f5aa3b4 | -11.1382 | -53.9223 | 2025-06-18 05:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 05ee473b-0aaf-3b35-ac9c-1862016fd12e | -11.1379 | -53.9429 | 2025-06-18 05:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| a83f6a1d-1dd3-3360-81da-90e1dedf3c0a | -4.38573 | -48.07038 | 2025-06-18 05:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ced60b68-e5fe-3cb8-8c07-ac323d7c1c8e | -2.95505 | -60.01513 | 2025-06-18 05:27:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30f0e835-e968-34e5-a31a-fcc76d135d4e | -3.22164 | -54.8652 | 2025-06-18 05:27:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ac6ae0a-485f-3a6e-9acf-09a643ab9125 | -4.38476 | -48.07735 | 2025-06-18 05:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d21a06a5-2622-368c-b429-1ab63192f67c | -10.27493 | -60.5477 | 2025-06-18 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39fc125f-67ca-37a4-9cd0-4f99a3889f20 | -11.13405 | -53.9476 | 2025-06-18 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2ca020a-60ef-3525-97b5-7136438d78a0 | -9.49643 | -56.08978 | 2025-06-18 05:29:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a9f7267-df6e-3c6a-8ad2-b54dc94333d5 | -10.9153 | -56.84608 | 2025-06-18 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b543720-1328-3140-8d83-5893e55ff75a | -9.26812 | -50.04251 | 2025-06-18 05:29:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 249e133e-6db8-33a3-9412-f2c0c32386a0 | -10.27611 | -60.53976 | 2025-06-18 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5b45c40-4193-3c4d-b4b8-cca65c000233 | -10.87995 | -54.31669 | 2025-06-18 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b085677-5438-3919-aaad-441b2660d36a | -9.4919 | -56.08911 | 2025-06-18 05:29:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| d6bdb0c2-55b5-379e-932f-9fa4b26de8ba | -7.72469 | -55.13806 | 2025-06-18 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 646e0537-e34a-32db-9bf6-2f946094553b | -10.27902 | -60.54427 | 2025-06-18 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf5f13d4-492b-3a8b-a54b-e3ca3c1f2cd7 | -10.2963 | -57.13972 | 2025-06-18 05:29:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af8eae1d-ae7e-326c-94fc-7547801183a1 | -10.91971 | -56.8467 | 2025-06-18 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7bd7cc97-e8ae-3c93-883d-0a823ee26076 | -10.35534 | -57.24469 | 2025-06-18 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31cb8777-274b-3bb1-b404-eaae69252ed6 | -11.12952 | -53.93993 | 2025-06-18 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 0d93e802-13ea-3407-99c1-2e47b5a0b033 | -11.08246 | -55.05764 | 2025-06-18 05:29:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e6d7653-e24c-3c81-998b-5caea75d7d1c | -11.0773 | -55.05293 | 2025-06-18 05:29:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3208debf-128d-34a5-a9fb-500af6f2a0be | -7.27852 | -50.00252 | 2025-06-18 05:29:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a4b35d4-a4de-3c3f-8165-6e9826769f44 | -10.28662 | -60.54136 | 2025-06-18 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea3b7ae7-cbb3-3a32-abed-5d10dc6dd31c | -10.2767 | -60.5358 | 2025-06-18 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d7a2c4c-371c-3dae-a0ce-ff807bcb6fa3 | -9.2614 | -50.04158 | 2025-06-18 05:29:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61e32dcb-bd0d-3f8b-8eb1-f8724a64eddd | -11.14649 | -53.93549 | 2025-06-18 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e55f2ef8-7904-3c49-b074-ce5e67d89e66 | -8.72382 | -49.02475 | 2025-06-18 05:29:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 37bca5ed-b075-352f-b81a-1f2475961af2 | -11.08745 | -55.05836 | 2025-06-18 05:29:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 243117bb-7007-3dd7-b641-99706c65d47e | -10.2411 | -52.23151 | 2025-06-18 05:29:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d06e6812-5005-3c9a-930e-e897e0622b3f | -10.24379 | -52.23085 | 2025-06-18 05:29:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1e375190-d5cc-30fa-a9a1-d5904b9110f4 | -10.29831 | -60.53502 | 2025-06-18 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb663fd2-bf52-3c0d-81f1-4facfe0c7bff | -10.72804 | -49.56186 | 2025-06-18 05:29:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2557862c-acc7-3154-83fe-8ac5c6d6cbe1 | -10.2837 | -60.53688 | 2025-06-18 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eeecbe6a-cbab-33b6-9908-fe923a6eb0b0 | -11.14153 | -53.93135 | 2025-06-18 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4f75e79f-c24e-3122-bbaf-62e9388a12a5 | -7.92709 | -61.55702 | 2025-06-18 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 956ca7af-aa7b-3963-a24c-45703655d31c | -10.27961 | -60.54031 | 2025-06-18 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3734e8f4-aeea-3396-bc11-1ecdd05132de | -11.1291 | -53.94337 | 2025-06-18 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 49cd01a1-7128-3a7a-b3ed-01b574a71269 | -11.07819 | -55.05118 | 2025-06-18 05:29:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54475e30-73f1-3685-8d86-d523fd772eaf | -10.2948 | -60.5345 | 2025-06-18 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bea4150a-05b0-32e8-aefb-7236674bdf7e | -10.66388 | -49.36329 | 2025-06-18 05:29:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4e2fea99-67fa-3f9e-9ca4-97b0cec67b8a | -10.2878 | -60.53346 | 2025-06-18 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74d49e28-413a-3fb8-ae87-24167954201e | -10.65943 | -49.36546 | 2025-06-18 05:29:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| a3832c94-5f38-30af-abb9-9dc32bcc3c98 | -10.35959 | -57.2453 | 2025-06-18 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56e8d4d7-45f5-3d1d-b552-3b2814941dd7 | -10.9241 | -56.84736 | 2025-06-18 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6323439e-659a-39bd-b2ea-00035981de7f | -7.89179 | -61.4755 | 2025-06-18 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b3697815-93a6-3517-abe4-0ef91cd78f75 | -11.1349 | -53.94074 | 2025-06-18 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 9de6e358-c4c7-3eee-aa7e-468a3246b446 | -8.72755 | -49.02925 | 2025-06-18 05:29:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ebd068ab-44b8-3c93-9951-cff4be1539d0 | -9.48736 | -56.08843 | 2025-06-18 05:29:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| b12d6c7c-8354-34e1-8dfa-f1d862da67de | -10.66313 | -49.37025 | 2025-06-18 05:29:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| aad46700-d97a-3fb1-a07e-1c587a91a58e | -10.35588 | -57.24062 | 2025-06-18 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41789663-f43b-3dae-b3f0-3dc36acf0845 | -11.13036 | -53.93309 | 2025-06-18 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 7a2df6b9-2221-333d-8e95-3d010bc36529 | -8.72129 | -49.02118 | 2025-06-18 05:29:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e69ea1e6-881d-39e5-b1cc-8aa168879659 | -11.13985 | -53.94496 | 2025-06-18 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a814ad05-e320-3527-a026-74123889d008 | -10.2802 | -60.53635 | 2025-06-18 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a1ba302-4ec2-36f0-bfa4-8cd85e6319a8 | -10.62027 | -54.91715 | 2025-06-18 05:29:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a561a8e-9cee-3693-be0a-197fcc1a3725 | -9.46276 | -57.85082 | 2025-06-18 05:29:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7e24392a-89c3-30f1-80f9-0a32664b7f25 | -11.13573 | -53.93394 | 2025-06-18 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 0196ec1f-26e4-3819-bc92-dca409046966 | -10.29575 | -57.14379 | 2025-06-18 05:29:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2f646be-e7a9-3f73-9136-9ed741048d0c | -10.62566 | -54.91489 | 2025-06-18 05:29:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89e74dc8-cdd7-3277-8e81-153a98a0833c | -10.29303 | -60.54638 | 2025-06-18 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84468835-23b1-388e-b006-1dca1ee2594e | -10.24163 | -52.22701 | 2025-06-18 05:29:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26b934d9-b4bb-3590-9f90-bdb6f127bb47 | -10.27843 | -60.54826 | 2025-06-18 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97f621c7-ef33-3ead-946b-54222e55c20b | -10.30058 | -57.14032 | 2025-06-18 05:29:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03fa6d62-36a0-397c-832d-51a55e5fc831 | -10.27434 | -60.55169 | 2025-06-18 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 061274e6-fe4b-394d-ac1d-1d40d50b0e12 | -11.14691 | -53.93211 | 2025-06-18 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ae10c28f-7d81-37a7-a09f-d7c161978afa | -10.46514 | -58.69056 | 2025-06-18 05:29:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a4300fa7-53e1-3533-bd4c-c4d9e473eb6e | -10.62529 | -54.91777 | 2025-06-18 05:29:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9be092d7-4a6f-3944-8cfc-605856b13b06 | -10.36174 | -57.22927 | 2025-06-18 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2823fbe7-f2de-31da-9097-6b7a2bab5b2c | -10.92469 | -56.84307 | 2025-06-18 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a371c13d-afcb-30be-ab8c-298874d054e0 | -10.3612 | -57.23327 | 2025-06-18 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73436eaa-371c-336b-b866-77e97e5e26ed | -10.47342 | -55.59148 | 2025-06-18 05:29:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72731bbc-42f4-3b7d-84b2-7fc8576612b6 | -9.49127 | -56.09373 | 2025-06-18 05:29:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 94143a4a-242a-3fc1-9f3b-5a21823ffad3 | -10.47305 | -55.59037 | 2025-06-18 05:29:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75b7817a-e85b-3ea5-bc0c-c28819b09310 | -9.45924 | -57.84669 | 2025-06-18 05:29:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adfd289b-c01a-38b5-916c-23de19067b25 | -11.14027 | -53.94154 | 2025-06-18 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 494b1fbc-56a6-315b-b1c3-0106a569c4e4 | -10.28252 | -60.5448 | 2025-06-18 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c1714d6-86a3-3385-8989-73dbead27924 | -10.46622 | -58.6925 | 2025-06-18 05:29:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 953a6a5e-dae1-31ae-bc5e-92bb782c4c11 | -9.5131 | -55.96782 | 2025-06-18 05:29:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4ce3b14-a032-3032-88d3-abcda06d2614 | -10.24436 | -52.22634 | 2025-06-18 05:29:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44a779a9-c87c-3bce-8ce6-ed2655b8fa64 | -8.7247 | -49.01764 | 2025-06-18 05:29:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4b93635c-200e-3157-97d5-cede3a13b07d | -11.13448 | -53.94416 | 2025-06-18 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 0f5abbdc-1f9f-3304-8681-0885a5bf5996 | -11.07783 | -55.05407 | 2025-06-18 05:29:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3d33e6c-6526-36b0-af27-ec4bcd22f656 | -5.12276 | -56.11749 | 2025-06-18 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d5397bf-1e99-3614-b72d-4b54886db08a | -9.46326 | -57.84731 | 2025-06-18 05:29:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 692eaef4-650e-3457-a0d1-eb5ce6b54d06 | -9.51376 | -55.96301 | 2025-06-18 05:29:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91154970-c26c-375f-8e89-183d4b1b84dd | -9.49253 | -56.0845 | 2025-06-18 05:29:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9e76066e-a360-3c47-92d2-5c2b1eac2714 | -10.35594 | -57.2425 | 2025-06-18 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd69d217-5f20-32f3-9dbb-e2441df2465d | -11.14111 | -53.93473 | 2025-06-18 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1876421a-8764-3fba-b179-270b8c3f487b | -10.86401 | -53.76419 | 2025-06-18 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fa2ca9cf-2752-3e5a-813d-cd4232434406 | -10.92029 | -56.84241 | 2025-06-18 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3c68b2e8-2c4a-3baf-ac11-b3b0a31c596f | -10.35905 | -57.24936 | 2025-06-18 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9f78ef13-458d-3293-ac78-590e54fe37de | -10.28311 | -60.54084 | 2025-06-18 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35c5f45b-4029-30ec-b848-a580df2a8df9 | -11.14069 | -53.93812 | 2025-06-18 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5f88d8ac-3c3a-33dd-b7ba-8fc3e71b5807 | -10.4669 | -58.68759 | 2025-06-18 05:29:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d75ea239-04f6-3aaf-a172-3d840e4dcfbb | -7.2851 | -50.00335 | 2025-06-18 05:29:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c35e07ef-4695-3aec-8c95-146b33c04b50 | -8.72839 | -49.02209 | 2025-06-18 05:29:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README23.md)
