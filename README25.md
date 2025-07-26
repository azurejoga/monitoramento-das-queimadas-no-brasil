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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03a0a8c3-5115-3b8b-8b9f-a560f4b0ce03 | -6.68827 | -58.84849 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1659d14f-69ea-3de3-929d-3dc1c2fb3580 | -6.62674 | -58.84905 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| d86bda99-aeca-3cef-aab7-75e6a25e7f8d | -6.67558 | -58.84298 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 24.5 |
| be8aa17d-e6b9-3219-8e94-fc7b005b231d | -6.61566 | -58.83315 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 771b64c9-aefa-3fdf-ae30-c76487bf854e | -6.67612 | -58.83951 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 42b991cb-5762-348b-a148-007fe7e3750b | -10.29541 | -57.05283 | 2025-07-26 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6557e061-8a82-36e5-9c21-1353d7d4e7ba | -6.68112 | -58.85093 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f905e012-efc7-3058-9b92-d873e778e50c | -8.60949 | -64.07301 | 2025-07-26 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6535c7a3-b6f8-3524-a524-129140fa4567 | -6.64436 | -58.8447 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 919a9fe6-a5bb-3827-b69d-300aa64cb833 | -6.66735 | -58.85233 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 526.2 |
| f8d3c8b6-ac33-31f8-8eb2-94a1af64d2d4 | -6.65421 | -58.82495 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.0 |
| c0da005d-efb7-36f6-88b1-2b9f81a90142 | -6.67827 | -58.82566 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fd449624-5aac-355a-9639-a0008b51e5b6 | -6.66396 | -58.83053 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 79f0b2b4-dcaf-3d62-90ec-56493d001878 | -6.65813 | -58.8433 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3a6d3f0c-c54e-35ef-b9f8-81ac57a1a799 | -6.66181 | -58.84438 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 4a28f338-63bf-3c34-9556-4b7f5fc443a4 | -6.56227 | -56.24769 | 2025-07-26 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2988b181-1076-30c1-9553-690dc455b2a1 | -10.22846 | -59.41099 | 2025-07-26 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac4c63d6-9582-3e5e-b82e-f93fd6cf6b73 | -7.25641 | -60.1256 | 2025-07-26 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 612e679e-12e4-3ee2-8a91-948686e3b771 | -6.6322 | -58.83573 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 25284929-d20c-317f-b747-1311724fc0b0 | -6.55932 | -56.24307 | 2025-07-26 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1381ded-8a43-331e-b99d-b9e3e8750350 | -7.56007 | -61.4098 | 2025-07-26 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e62b3722-6829-39df-a0d4-25925446ecc4 | -6.75467 | -58.99004 | 2025-07-26 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 15b73d04-1e16-3fa1-93e2-278ee3999525 | -6.56289 | -56.24362 | 2025-07-26 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fdc9598-227e-31fa-9005-97b83a485160 | -6.68166 | -58.84746 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c81bc08e-382d-354c-a123-3f54020c47c3 | -7.4946 | -63.82275 | 2025-07-26 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9332b2bd-cccc-3bb6-ad4b-158c1c27380b | -6.6372 | -58.84714 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 2e71bebd-9e4c-3c48-8de8-80ec30540a74 | -6.64321 | -58.83034 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| a184c874-fd5c-3afc-be0e-33da2ffd83f4 | -6.66627 | -58.85925 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0afdb482-f1f6-3562-b269-b171c56e41c6 | -6.62613 | -58.83123 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 18f5c1bf-c57c-3632-9273-8bf276b4ade7 | -13.12905 | -47.33009 | 2025-07-26 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1953b31a-ee01-371b-97a0-daf5ba2e612a | -7.29576 | -60.17849 | 2025-07-26 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e84cff09-1859-3011-82ee-c9c5bf7de155 | -9.13165 | -63.92332 | 2025-07-26 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38fa1e7c-c725-3109-8194-df44e31be52d | -7.97412 | -49.69333 | 2025-07-26 05:18:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9d09235-8b3f-3b6c-9736-2645ea2b9a2f | -6.67996 | -58.83657 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 44bb54d1-c394-33e1-ba08-6cb8d92a2058 | -6.53908 | -56.25664 | 2025-07-26 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 858b2cef-ca34-36f9-ba6c-3d2b1bb7476a | -9.64003 | -63.1554 | 2025-07-26 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2669779b-1980-308c-8788-fd2c72b1c9b6 | -6.67173 | -58.84592 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 35.1 |
| b476afce-a58c-392a-84ab-3683a6f302f4 | -6.64382 | -58.84816 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| dc417c9e-a7fc-3a8a-a267-11544b31e6b1 | -7.4961 | -63.82134 | 2025-07-26 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aac5c888-e17f-3702-a48f-4c658ab4134c | -6.63004 | -58.84957 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 3d0bcfc1-d425-3e00-912f-77dc8c1f0875 | -6.68443 | -58.85144 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b9be3224-65ed-3563-8994-d8a398e2562e | -10.68408 | -51.88776 | 2025-07-26 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 143b3a60-4c19-3dc1-b2d4-a4bfd28e786c | -11.3216 | -55.21638 | 2025-07-26 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e963a9c-3496-3c48-8f3a-955b698feccd | -10.22568 | -59.40697 | 2025-07-26 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bd49429-4d67-3224-b16f-412929de49dd | -6.65698 | -58.82894 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 157f013b-f736-3be1-b508-f6f555d9a5dc | -6.65644 | -58.8324 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 566c1c72-eaf8-3438-b0fb-07b5c342c0e8 | -6.62066 | -58.84456 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 71afa418-6260-399d-ab5c-8fbd068de761 | -10.3591 | -46.63996 | 2025-07-26 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7366a193-e545-32c8-b1c5-2bbcd594591a | -6.65313 | -58.83188 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 54e7635e-d025-33f9-b733-4388736e16ae | -6.63997 | -58.85111 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bad0212d-e3c0-3662-81d7-c8bf2d03b5ef | -6.63828 | -58.84021 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cb115096-b74a-3ceb-8b9d-2fcac1bb8f91 | -6.55159 | -56.24606 | 2025-07-26 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2aacad3-1ee6-33ea-812e-7d09529137ec | -6.65374 | -58.84971 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 04e30b55-e850-3cf7-af26-abed1bf0897f | -6.65536 | -58.83932 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 714ad3cc-c516-3580-8726-3d43fcdbfad5 | -9.62907 | -61.45656 | 2025-07-26 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 504408a8-c019-33a6-9b6a-3b021967831c | -6.68542 | -58.82322 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ce88af60-e4e2-3814-9557-e1cf293b2bd9 | -11.79346 | -57.24236 | 2025-07-26 05:18:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f136baf-e6cd-3927-a8b9-d5fbe4863e5d | -6.63112 | -58.84265 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 3037fe36-1503-3d2e-b085-30e70957340f | -6.68658 | -58.8376 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 66347674-d673-3344-a326-61682e95337e | -10.29812 | -57.05172 | 2025-07-26 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1919555e-0b2c-3c3b-82c3-c571610653c8 | -6.66565 | -58.84143 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 2ef757d0-1643-3e69-8bbc-56abd7534abb | -9.81154 | -46.71118 | 2025-07-26 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b1f07534-ce84-3392-b95a-0dd0862c4bb8 | -6.6482 | -58.84175 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2b82b8d3-b863-32ba-a5d9-753e2340d31d | -6.63774 | -58.84368 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| fcc49076-e7ab-329c-ba12-f1bc01b09c42 | -11.31923 | -55.21525 | 2025-07-26 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b93696d7-5b67-3df4-9857-7865396ac715 | -6.62174 | -58.83765 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 2124b864-516e-3a9c-9960-3c4b34a11a4b | -6.6449 | -58.84124 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 652e40c7-9ffe-372b-b177-596a49d82809 | -6.63497 | -58.8397 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 244e7f29-f4ad-346b-8513-942e15ab7b87 | -8.30815 | -55.11059 | 2025-07-26 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac9b6bb1-46b1-3d64-860f-bf2029a07624 | -7.28911 | -60.17746 | 2025-07-26 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f9b3166-4d2d-3ba5-a5f9-a3d195c62c28 | -7.50255 | -63.51003 | 2025-07-26 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba0cf57a-7c45-33cc-981c-24c712456bf7 | -13.10725 | -47.33133 | 2025-07-26 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 994ff375-67b5-38f7-b58b-3f77022876e3 | -6.68935 | -58.84158 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a46cc7a-e7e5-37c2-863c-caa9191f1388 | -6.67165 | -58.82463 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e7feaa3-70a5-30b8-914f-133f65567e2b | -6.55219 | -56.24198 | 2025-07-26 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34d4a58e-aac8-3b3e-a7c0-8b855d07dddf | -9.254 | -50.22705 | 2025-07-26 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22f71eeb-b6d5-36ab-93a3-995a213e7b10 | -5.91604 | -61.30617 | 2025-07-26 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9196c16f-716a-345e-baaf-807b5d2c650a | -6.64105 | -58.84419 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 4f50d4fe-13a9-3870-b72d-d793376897ef | -6.68774 | -58.85196 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65472dce-a663-3b23-b9e8-4797e556dc78 | -6.61897 | -58.83366 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| d8180fb0-ff70-3764-b7fc-cf0e8b7d84cc | -6.66029 | -58.82945 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 6631af77-502f-3bb9-819b-036e88768c02 | -6.69212 | -58.84555 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 48c4b0f5-df5d-394d-b148-8f2815388f02 | -6.6532 | -58.85316 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b3c09f8-20b3-3f86-82e0-fdf3aaff7dca | -6.54029 | -56.24848 | 2025-07-26 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 736cee36-e8ec-31fb-8ab0-0a5a0e0296c8 | -6.62943 | -58.83175 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 83fb1004-cf5b-3dce-bb8a-3b6ec7da93bc | -6.68435 | -58.83016 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cd1500e1-f176-39ab-bf56-26bb28033d7b | -9.3314 | -58.83669 | 2025-07-26 05:18:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3c76c476-5299-3336-b7da-43d7f65cbc51 | -6.64989 | -58.85265 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| d734d9bf-a042-3159-8152-7faf074339d5 | -9.19962 | -59.68723 | 2025-07-26 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7191fc36-0edf-3c08-a47a-32079db1c538 | -6.63882 | -58.83675 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0bc8c239-9c1e-3c43-a6d4-d1f377ed355e | -7.56023 | -61.40966 | 2025-07-26 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d1d47a42-1052-3963-8aa1-8c7d822e1a6b | -6.65151 | -58.84227 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d33c9584-72d2-3aea-af79-516dc25bd2cb | -6.6262 | -58.85251 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| a0ba5320-eeb4-3e31-a8e7-59b090a99807 | -6.67388 | -58.83208 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 70e8fd12-a23d-3858-8d67-0ae1bd1835e2 | -6.67281 | -58.839 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 39e248b9-6659-35eb-b5c2-19d91736a875 | -6.66073 | -58.8513 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 315dd22e-dcaa-303f-9d40-3d2f535979b3 | -11.31875 | -55.21883 | 2025-07-26 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7193d92-c521-31bc-807b-6e68338d3a14 | -7.6682 | -47.47379 | 2025-07-26 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 57d7bb37-d76c-385e-9f5c-d479ce6d851e | -7.29299 | -60.17447 | 2025-07-26 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee0165c6-6b06-30d3-af40-f3ae1a117b4c | -8.07394 | -48.01536 | 2025-07-26 05:18:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README26.md)
