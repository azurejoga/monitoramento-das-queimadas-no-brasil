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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 623c7582-c84d-36f6-895c-ffa657e37dba | -6.92104 | -38.73177 | 2026-09-21 15:16:00 | NOAA-20 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 2286504b-c13e-33f1-82d7-c257246f0f0c | -7.17095 | -37.71716 | 2026-09-21 15:16:00 | NOAA-20 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 2748c5ed-5b42-33ca-9b39-5ad693bfb258 | -7.5234 | -34.95369 | 2026-09-21 15:16:00 | NOAA-20 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| abc9309d-1fd7-3488-b4f4-44dd6de7d772 | -7.81967 | -38.85593 | 2026-09-21 15:16:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 12.2 |
| f3b70479-7051-3627-98b0-4121973e8017 | -6.92037 | -38.73912 | 2026-09-21 15:16:00 | NOAA-20 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 23.0 |
| e757b947-f075-307f-a2ca-e41b6779484c | -8.42542 | -37.08104 | 2026-09-21 15:16:00 | NOAA-20 | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| af463555-9fd9-32a3-bbd3-8eca6cbcd102 | -7.84949 | -35.22024 | 2026-09-21 15:16:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 42.8 |
| 6ab34ffc-23dc-3773-849d-3334bb2fb378 | -6.92658 | -38.73186 | 2026-09-21 15:16:00 | NOAA-20 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 16.7 |
| a7c118b4-4afe-318d-8d6c-2378d2a62d5d | -7.16357 | -37.71211 | 2026-09-21 15:16:00 | NOAA-20 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9ef0cd6a-30c0-366e-b365-f321261db4d2 | -8.66362 | -35.29582 | 2026-09-21 15:16:00 | NOAA-20 | RIO FORMOSO | PERNAMBUCO | Brasil | 2611903 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| bb485e2f-f71e-3eed-9607-bfe9190ff6d3 | -7.98158 | -37.48503 | 2026-09-21 15:16:00 | NOAA-20 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 446b49e3-e039-313a-ae74-129ca4ff6e6c | -6.10845 | -35.28407 | 2026-09-21 15:16:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| c6f5abde-99d6-3d6f-b74b-49ecb65bb277 | -8.59443 | -36.89914 | 2026-09-21 15:16:00 | NOAA-20 | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 0e9b35cf-50f8-3739-9f44-fcba58d65cbf | -8.59697 | -35.46318 | 2026-09-21 15:16:00 | NOAA-20 | GAMELEIRA | PERNAMBUCO | Brasil | 2605905 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 710375f0-0b3a-304d-a78a-9c3ed6b172eb | -7.30864 | -35.64931 | 2026-09-21 15:16:00 | NOAA-20 | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2acddf31-db33-315b-a1c5-cfa0c72a6d1d | -5.88245 | -39.10859 | 2026-09-21 15:16:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 34c79311-3ca2-3bf1-ba5a-19da00d87e28 | -7.93753 | -35.4413 | 2026-09-21 15:16:00 | NOAA-20 | LIMOEIRO | PERNAMBUCO | Brasil | 2608909 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| e3986d56-37dc-3b88-b3d6-e5aef3f12e79 | -8.07731 | -38.23089 | 2026-09-21 15:16:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 955d7104-c364-3385-9549-221b82ebea6c | -6.85817 | -36.89979 | 2026-09-21 15:16:00 | NOAA-20 | SANTA LUZIA | PARAÍBA | Brasil | 2513406 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 279dfdab-7802-3ffc-8236-d485adf365cc | -7.16641 | -37.71764 | 2026-09-21 15:16:00 | NOAA-20 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 4.6 |
| aac3aaf3-c1f4-3ba9-b5eb-16eec139c710 | -6.10672 | -35.28643 | 2026-09-21 15:16:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b0740149-23ce-315b-9b2f-ba28bca48bb3 | -8.00364 | -35.44895 | 2026-09-21 15:16:00 | NOAA-20 | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ad375cce-e2df-384b-96cd-5380e9711d82 | -6.39406 | -35.03662 | 2026-09-21 15:16:00 | NOAA-20 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 02634615-ce44-3a29-983e-d8ecfe79e652 | -6.86212 | -36.9006 | 2026-09-21 15:16:00 | NOAA-20 | SANTA LUZIA | PARAÍBA | Brasil | 2513406 | 25 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 25944bf8-93ed-34ee-b460-3c00f91bf022 | -6.45961 | -37.11575 | 2026-09-21 15:16:00 | NOAA-20 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f79e3339-0095-379d-af97-c13147da0fb3 | -7.93899 | -38.91319 | 2026-09-21 15:16:00 | NOAA-20 | VERDEJANTE | PERNAMBUCO | Brasil | 2616100 | 26 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 63e0806c-5626-32d1-83e5-474eaa8e99b8 | -7.15369 | -35.14061 | 2026-09-21 15:16:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| daa089e5-e25e-3fe5-ae0b-a26d1e871494 | -6.93363 | -38.73117 | 2026-09-21 15:16:00 | NOAA-20 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 8f0fdc63-dd04-3ea3-a343-29fbe29db37b | -8.27962 | -35.25313 | 2026-09-21 15:16:00 | NOAA-20 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 46fbe7f9-64be-3ff9-9b1c-b739e067857b | -7.3602 | -35.28323 | 2026-09-21 15:16:00 | NOAA-20 | ITABAIANA | PARAÍBA | Brasil | 2506905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 7d1f52fa-352c-3aa2-a3f5-8c567c63c6b1 | -5.67561 | -38.88532 | 2026-09-21 15:16:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 021ba886-3769-3185-a563-de295b42ee3f | -4.98806 | -36.89114 | 2026-09-21 15:16:00 | NOAA-20 | PORTO DO MANGUE | RIO GRANDE DO NORTE | Brasil | 2410256 | 24 | 33 | nan | nan | nan | Caatinga | 29.9 |
| 79424ca4-0de2-3cc9-a5ed-566c6c98de98 | -8.78485 | -37.10521 | 2026-09-21 15:16:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 55c1469c-b983-368d-9e0c-52e328da726b | -6.91955 | -38.73272 | 2026-09-21 15:16:00 | NOAA-20 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 4a082710-a363-33d3-8896-07a3a8bf9013 | -7.84897 | -35.21627 | 2026-09-21 15:16:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 35.3 |
| 90c9bfe7-667a-3110-8f89-9a890a13c757 | -6.39384 | -35.03741 | 2026-09-21 15:16:00 | NOAA-20 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| f591184c-6c3d-32d0-962f-4b958f33cfec | -7.84324 | -35.21701 | 2026-09-21 15:16:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 35.3 |
| 76616a91-f9d6-35f1-a457-b605e165eb9d | -7.56878 | -35.29263 | 2026-09-21 15:16:00 | NOAA-20 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 74e84b5e-941b-3c11-9465-67f6d5a88403 | -8.78516 | -37.10572 | 2026-09-21 15:16:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 14979a08-16c7-3d1b-babc-c8ecc91691c9 | -7.39484 | -38.73095 | 2026-09-21 15:16:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 5e424660-dff5-3c7f-948e-c6b79231cca7 | -5.14315 | -37.34016 | 2026-09-21 15:16:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 1b1a0ce2-4beb-3f90-83e2-7b85da605416 | -7.9372 | -35.43944 | 2026-09-21 15:16:00 | NOAA-20 | LIMOEIRO | PERNAMBUCO | Brasil | 2608909 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 8f02513e-5df5-383b-88be-7c5b3f12a5db | -6.60007 | -35.74714 | 2026-09-21 15:16:00 | NOAA-20 | CACIMBA DE DENTRO | PARAÍBA | Brasil | 2503506 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5bbb7b4c-19c0-3d23-b2c6-21fbe43e3ff1 | -7.93774 | -35.44348 | 2026-09-21 15:16:00 | NOAA-20 | LIMOEIRO | PERNAMBUCO | Brasil | 2608909 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| ab35be3b-9d28-3ca5-b80b-9a0f3b9fe577 | -7.98684 | -37.4872 | 2026-09-21 15:16:00 | NOAA-20 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 8ce030a7-8256-3421-b39a-2a0c72ca01d1 | -6.45896 | -37.1107 | 2026-09-21 15:16:00 | NOAA-20 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 097cb6e7-480f-3891-82ce-7c9287829ec7 | -6.5998 | -35.74802 | 2026-09-21 15:16:00 | NOAA-20 | CACIMBA DE DENTRO | PARAÍBA | Brasil | 2503506 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8f76c456-d6e4-348e-9c81-586e735e06d4 | -6.42083 | -35.64913 | 2026-09-21 15:16:00 | NOAA-20 | PASSA E FICA | RIO GRANDE DO NORTE | Brasil | 2409100 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a8fd4dae-364e-3ea4-bc71-99b92cb04ab3 | -6.63338 | -38.63512 | 2026-09-21 15:16:00 | NOAA-20 | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 3f5d3c10-1348-3b4f-8a6c-adcbc6f6fcdf | -7.39397 | -38.7238 | 2026-09-21 15:16:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| b3965b17-937e-3fe2-ab4d-32ae35cb857c | -7.17307 | -37.71696 | 2026-09-21 15:16:00 | NOAA-20 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 11dfc224-5c02-3b3f-af3f-55ebe8e3e226 | -8.49757 | -37.02474 | 2026-09-21 15:16:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 573cb1eb-216b-3d62-a58c-298f036be0e2 | -6.10622 | -35.28269 | 2026-09-21 15:16:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 88558fda-6d0f-30d2-b959-a51f1dac8da8 | -6.46248 | -37.11116 | 2026-09-21 15:16:00 | NOAA-20 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 8de14efc-9ded-303f-93f7-9fe11d0efd7c | -7.17023 | -37.7114 | 2026-09-21 15:16:00 | NOAA-20 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 3f98881b-56c9-3482-b699-54ab35c979d7 | -8.66344 | -35.29679 | 2026-09-21 15:16:00 | NOAA-20 | RIO FORMOSO | PERNAMBUCO | Brasil | 2611903 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| dd28625d-ccab-32fd-9868-f4ad87a0654a | -7.40367 | -34.94252 | 2026-09-21 15:16:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 3c6dbae7-3b76-3913-8911-63ca0640825c | -7.15649 | -35.14185 | 2026-09-21 15:16:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0e20174b-5b51-36bb-ab38-30db001451b4 | -6.21796 | -35.38654 | 2026-09-21 15:16:00 | NOAA-20 | BREJINHO | RIO GRANDE DO NORTE | Brasil | 2401800 | 24 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 6bd0a95b-66df-3b08-87ba-f82272bfd7b1 | -7.3896 | -38.72493 | 2026-09-21 15:16:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| a9889bff-0175-34e8-bf4d-6097f812c1f0 | -5.14246 | -37.33511 | 2026-09-21 15:16:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 327dac1a-1480-3ed0-adf0-357af9f98b52 | -6.97464 | -37.16833 | 2026-09-21 15:16:00 | NOAA-20 | SÃO MAMEDE | PARAÍBA | Brasil | 2514909 | 25 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 216ea835-b41c-3e7e-b0cf-a5b4b7b5c556 | -8.59567 | -35.46111 | 2026-09-21 15:16:00 | NOAA-20 | GAMELEIRA | PERNAMBUCO | Brasil | 2605905 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 1ae187cf-1881-3869-ad9a-abf50dcf6f84 | -6.84276 | -37.82047 | 2026-09-21 15:16:00 | NOAA-20 | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 82892702-b956-3dd8-a578-d98ee8e82d1c | -7.8227 | -38.85532 | 2026-09-21 15:16:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 9.3 |
| cc903101-bccc-3916-8b49-987184ef20cc | -8.31552 | -36.16754 | 2026-09-21 15:16:00 | NOAA-20 | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 6.7 |
| aab96013-5b11-3aab-a92c-0250a95ead22 | -8.02296 | -37.0878 | 2026-09-21 15:16:00 | NOAA-20 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 54ad56ea-5ae3-386f-b563-9807e26b9d5c | -6.92191 | -38.73822 | 2026-09-21 15:16:00 | NOAA-20 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 9e3df91e-9fa5-3340-baf2-0de5644d1726 | -6.18566 | -35.23703 | 2026-09-21 15:16:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d5f06e49-b61c-3af2-9dd3-1af5078f5acb | -6.21851 | -35.39043 | 2026-09-21 15:16:00 | NOAA-20 | BREJINHO | RIO GRANDE DO NORTE | Brasil | 2401800 | 24 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 416741a4-0dff-327f-b5c8-c30b9bb6d81f | -4.13806 | -38.57579 | 2026-09-21 15:18:00 | NOAA-20 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 93d64903-fda3-3cc4-8b21-69e9d6700d40 | -3.7111 | -39.38226 | 2026-09-21 15:18:00 | NOAA-20 | UMIRIM | CEARÁ | Brasil | 2313757 | 23 | 33 | nan | nan | nan | Caatinga | 15.6 |
| c19414a0-ca81-3b90-903c-6ccb0431134b | -4.46614 | -38.28856 | 2026-09-21 15:18:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a614cbea-332a-3425-9cd5-f5931f6ec4e3 | -3.49757 | -39.60102 | 2026-09-21 15:18:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 520abca1-87e8-391c-a18f-63c4958de7ba | -3.70526 | -38.84482 | 2026-09-21 15:18:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 8ee73a0d-ad45-3cca-bca0-3163e2b5eb46 | -3.8673 | -38.54649 | 2026-09-21 15:18:00 | NOAA-20 | PACATUBA | CEARÁ | Brasil | 2309706 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 02dfbcf1-a59d-37fd-a10f-ae14b3755d88 | -3.7093 | -38.709 | 2026-09-21 15:18:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 88ad69c0-0a5c-3688-baa4-a27c1b12eee3 | -4.47277 | -38.28766 | 2026-09-21 15:18:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a755556a-a519-3349-ac14-1a0a2daea2c0 | -3.71221 | -38.70259 | 2026-09-21 15:18:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 348430b5-f30d-3c3f-a6be-eaa5efdcb2e7 | -3.71811 | -39.38132 | 2026-09-21 15:18:00 | NOAA-20 | UMIRIM | CEARÁ | Brasil | 2313757 | 23 | 33 | nan | nan | nan | Caatinga | 15.6 |
| afa7411c-6da8-32e2-a933-8d9d62f42e44 | -3.71308 | -38.70853 | 2026-09-21 15:18:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 437e6a59-334c-3312-87f2-aace22d30aba | -3.71294 | -39.38266 | 2026-09-21 15:18:00 | NOAA-20 | UMIRIM | CEARÁ | Brasil | 2313757 | 23 | 33 | nan | nan | nan | Caatinga | 38.1 |
| 74710d79-667c-3040-8d82-59b20d035fdc | -3.70848 | -38.70309 | 2026-09-21 15:18:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 9df8142d-92bf-3f15-8000-01e3d153381a | -3.86645 | -38.54055 | 2026-09-21 15:18:00 | NOAA-20 | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 2613dfa9-b765-3c24-8fed-1926829d0a1a | -4.14126 | -38.57521 | 2026-09-21 15:18:00 | NOAA-20 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| d75f170e-1e63-3882-8759-826c0e9191c2 | -9.5594 | -66.0359 | 2026-09-21 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 111.5 |
| be6b9934-765a-3cfd-a2cb-aa421cfa05a3 | -8.7267 | -44.8836 | 2026-09-21 15:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 1db7fe8e-735c-307a-8ab0-3989b87c2573 | -10.4541 | -51.2827 | 2026-09-21 15:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| aa42ecb1-b1a0-3b46-a416-6a4391fd4081 | -9.8683 | -48.4689 | 2026-09-21 15:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 123.0 |
| bb4cfacf-c944-3e27-9f49-e0aa2d5e2077 | -7.2117 | -56.0193 | 2026-09-21 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| efc83cd1-d0b7-3b45-8fa0-fed216b3f154 | -3.4369 | -50.6142 | 2026-09-21 15:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| b7f52a38-9a8b-3256-9fb0-5919d5a4ff6a | -5.5848 | -45.5478 | 2026-09-21 15:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 76fbfed2-b792-3a34-89cf-bea2e36bf592 | -14.6487 | -45.6833 | 2026-09-21 15:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 0da32f12-db2d-33f9-bdda-6c71446b6aa3 | -2.9157 | -57.7983 | 2026-09-21 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 041cc9fb-ac8f-3a29-ba6e-562c5a5dd811 | -4.4112 | -55.2466 | 2026-09-21 15:20:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| f276612a-4c5b-35f3-8a17-6b9b4dd70998 | -9.1711 | -49.9835 | 2026-09-21 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| bf2089a4-786d-3fdb-b1ed-08689068f960 | -6.2585 | -41.6617 | 2026-09-21 15:20:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 198.2 |
| 9a6b91be-3f15-3988-ae33-7db0a3fd7628 | 1.0212 | -51.1654 | 2026-09-21 15:20:00 | GOES-19 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 9f4434f2-2045-3b99-9bea-0954be0feed2 | -9.1708 | -50.0049 | 2026-09-21 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 187.3 |
| 59b30afc-e1a6-325f-9586-aa05911ac11b | -4.0925 | -62.0874 | 2026-09-21 15:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |


[Clique aqui para ver as próximas entradas](README140.md)
