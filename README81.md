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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8c36f94-7ff6-391d-a943-220685a1a4a3 | -11.6289 | -54.56841 | 2026-09-01 05:36:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb11cb21-64f0-32cd-9bf6-d1188ccaad45 | -10.5035 | -59.62438 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fefe847e-f7ef-3c10-b2b8-bea4309581db | -9.17692 | -59.63767 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2a87b1e-784b-3afe-81b1-216cd7c82961 | -6.86701 | -59.46859 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 975c84ea-25d6-3bdd-824f-d989b77cffa4 | -9.16005 | -60.29216 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31209341-3e9d-3d7d-baf6-563b161ab2a0 | -9.02509 | -65.45277 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 897bdc98-af90-3d53-a8bf-1707f79983a3 | -5.96218 | -57.6945 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9208451b-8376-30a5-9a37-339ca10ab29a | -6.9565 | -55.63683 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d9d411bd-c1f5-3d21-aa27-4f2be72bc35d | -7.34415 | -60.58488 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 05c76c28-35c7-3bf0-a8e2-e834c1ba95b1 | -9.88795 | -60.27981 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 956a437e-72fb-3d7e-8aec-744ecde768e4 | -11.17643 | -55.08912 | 2026-09-01 05:36:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba40cae3-2779-3223-b8e0-04c4280c6e87 | -6.80834 | -59.56746 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4b401c76-4b25-3370-afd8-eb3c37553dcc | -6.12177 | -57.67194 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a808a554-21cc-35bf-8b93-58a4a5599d0a | -7.56943 | -61.36889 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14aee7a7-6f56-3c47-a5ac-1568c235176b | -9.47233 | -57.02174 | 2026-09-01 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7d69cc6-365a-3b29-8b02-2c64ff03deef | -9.14565 | -61.09552 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd521954-d2f6-361e-bc39-e8539f55fd50 | -7.2004 | -60.67701 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 08de8a84-5c92-3238-9a81-588466fd3145 | -7.35408 | -55.19852 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3415d1c9-1e21-33cc-a534-2283a56f8d1b | -7.79225 | -61.57504 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29c57e72-80af-3000-9334-f38f444cb4d7 | -6.05784 | -57.6451 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a9387b3-e305-33ba-9166-6bd6b9097513 | -6.25646 | -55.42498 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d67f0a21-35f1-3a28-8059-69f920660e3c | -6.69823 | -55.41101 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7df91347-609a-3bea-ae52-c6e9bf8d2349 | -7.91053 | -61.33769 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f7e0ac1-9167-36f4-a3bf-c29c0805c352 | -11.24727 | -54.0139 | 2026-09-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b15ffa5-a388-32f4-85a5-13bfd4615279 | -8.9437 | -62.37268 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67049296-8549-3bd2-86b9-84a20c2ccb5d | -8.94038 | -62.37215 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce75b638-28af-3864-86e3-bf37b91c71e8 | -9.38826 | -60.57779 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d39fc668-6861-34be-9926-4478861e76bb | -6.80392 | -59.43476 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd4290da-61d6-3a21-a875-8ed989c7ca8f | -7.19016 | -60.6754 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06a6d8e2-2c27-3a1f-ae28-ebabbd2cf81b | -6.90805 | -59.48738 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78e141f0-20a5-36e5-9d94-412324da1a12 | -8.37242 | -70.84949 | 2026-09-01 05:36:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b25c3602-df71-3ab0-9255-1c92874ac1b6 | -8.58766 | -54.77135 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a813523d-2833-317a-b54c-0068950179a1 | -7.02398 | -59.64788 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5457d34f-44b2-33d3-a0cb-a42e70f1759d | -5.87675 | -57.78115 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25140769-9155-3851-84f5-3111048ebf3d | -9.91338 | -60.15815 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76520324-bb13-330e-a872-90d3f9313f16 | -9.02637 | -65.44491 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6260f79-4907-3ebe-8a5e-03ab666fbeca | -7.34815 | -60.58168 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f472392f-e2f0-31b4-b5d9-078b8842bdd7 | -8.79316 | -62.48842 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8364529-e9a3-31e4-ab67-b892362f5fd7 | -9.48524 | -57.02353 | 2026-09-01 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fd6c6ee-bbad-3d30-9765-95873f426bc7 | -7.28355 | -60.65944 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f12202be-7320-3389-b4a2-9c53cb1d8bb0 | -9.45238 | -67.45896 | 2026-09-01 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c0a8ca04-cc7e-3e93-8956-adadb9795c2b | -8.12464 | -54.96243 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 751baf6f-531f-368a-9146-e99c7c2e6f52 | -5.56794 | -60.18133 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29300f05-1961-382e-af4b-fe883e390db3 | -6.94881 | -58.95117 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c4dbb4b-1b80-3a69-a173-163986201680 | -8.72064 | -67.11475 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7fb752a-7563-3432-abf5-47c7b7ed4d0c | -9.39631 | -68.93729 | 2026-09-01 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 187c08d8-fcdb-3cbe-bb99-7862aaf13db6 | -8.87796 | -66.89326 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c819a48a-9843-3e86-8e04-ef2ddda47349 | -8.88791 | -66.83347 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0c3fc05-34f8-3a6d-88bf-8d4bda44b800 | -5.85889 | -57.55566 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bf0615fd-804d-32e1-99f4-5162214139e4 | -7.29163 | -56.68647 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8252914d-77ad-324b-b66c-eafd2acc00ed | -6.12152 | -57.67505 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d77c49b-5859-35fa-905e-1e6650ea6e8b | -10.49494 | -59.60499 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e3f7e83-5bcc-326a-adcf-c0f815aba961 | -8.87496 | -66.88795 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 96245ffa-bed9-3e68-a648-94eed4390914 | -9.0628 | -65.49046 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0041cda5-a2f1-35a7-99ca-96dcc4802dab | -7.05572 | -52.72009 | 2026-09-01 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67732143-2edb-3d16-8abc-3d26f99f956a | -8.51124 | -67.13855 | 2026-09-01 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 54a2cf95-d2f2-3630-80c6-ff55e3452a30 | -8.12391 | -54.9675 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a0c525cf-649a-3254-8c2b-9cf275c0c80d | -8.60504 | -70.20661 | 2026-09-01 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7f36c07-e45b-3531-a596-0859a92e84a3 | -6.43136 | -62.85829 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47baa8b2-a2f6-39de-94c6-c282054f1fe2 | -5.95268 | -57.67788 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8bad1623-cf63-3d65-946b-644497fbb520 | -6.1203 | -57.682 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| db543e6f-7412-34a0-b186-6d46a2fbeab5 | -9.27603 | -68.34842 | 2026-09-01 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 748af820-a619-3e06-98bf-3e896190a283 | -6.95853 | -55.64838 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 78315dea-ad9e-3345-a39f-eed904238289 | -11.68512 | -54.54603 | 2026-09-01 05:36:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d737a7f0-49c0-3cec-a029-c99609d86b62 | -7.52571 | -61.31816 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1676ae9-8c83-3cf7-b722-1f35d6ee37cd | -8.70625 | -52.36531 | 2026-09-01 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b96064c2-912f-306b-acb1-8aaaca2ee33c | -6.84875 | -59.41967 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cb2bcf9-3067-3cc7-acae-377e3f741ab0 | -7.56554 | -60.46417 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c945b86-070c-3e57-99e6-eb6002279429 | -5.88899 | -57.7532 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fbbd0fa-2885-335a-8b40-bba2a74ffacc | -10.06678 | -59.40405 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8639f088-50c8-3309-859b-9a95f154d33a | -8.86707 | -66.77359 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 644d0464-0077-3611-af05-631d1af7e8e9 | -11.62849 | -54.57167 | 2026-09-01 05:36:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b0f87e1-c9b8-31d3-af5c-5c02b2b14054 | -6.01809 | -57.66992 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 58c761ce-c2e8-36f3-a8bc-c26c4255afaa | -8.13199 | -54.97081 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6b3b0e9-cee9-3b3a-afa8-0d4724c10432 | -6.96378 | -55.64434 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 6fd793e0-a241-35c4-ad06-b41e1c49e73a | -7.26956 | -61.11377 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a39aaaec-f5f9-3ac5-9160-984f4093a79e | -6.86377 | -56.57176 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0cc6b91a-7208-3ff3-9c85-b0fd0d5c5f0a | -9.20405 | -59.55402 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d39808c2-921f-35c1-9f55-fa0578f5558c | -11.30464 | -50.57839 | 2026-09-01 05:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f91ea379-7bc2-3f13-b60d-0ab27674f380 | -8.54473 | -67.16137 | 2026-09-01 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ecaf291-9cf5-3afc-a70e-d0d1de9cf3a0 | -6.13085 | -56.38826 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b21569f-7d94-30be-a0e3-e85f15375c7f | -8.87005 | -66.77876 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de8453be-f71b-376f-a427-1d06f6084e8d | -7.28192 | -61.12308 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67592632-e82a-3a45-be4d-d5c18eec93cc | -8.78653 | -62.48737 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d95d950b-8a16-3715-b8bf-758f9dc8c383 | -8.59859 | -70.21572 | 2026-09-01 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca331b61-fcc8-3ca7-9180-b82462d371fd | -9.20597 | -59.41802 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 146619da-7aa9-39ab-9c75-d6ec4866ee15 | -8.92875 | -62.35955 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfa740c1-28cb-3fee-9caa-b2a7ede041a2 | -6.94674 | -55.64019 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32bec5f2-7fe4-3d1c-b9bd-1fdbe28c8114 | -6.8113 | -59.572 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 81ce4735-c92f-3ff7-b74f-9061ec92dff9 | -7.34129 | -60.58063 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 54104246-217e-3f62-9049-061b87e83d51 | -7.56841 | -60.46852 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58d52708-fa83-3c34-9f4f-381340be607e | -7.26 | -61.1086 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2f6d035-884d-3c99-8efb-6fb712ddb820 | -6.80888 | -59.56833 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e77483e-bfea-38ea-b22a-00af593b002e | -10.35513 | -50.00637 | 2026-09-01 05:36:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4408be5e-7de8-39da-992d-4f18eae2bdf5 | -6.79525 | -59.39559 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3148f0a8-45d4-3f69-80d2-9f90b0010ab8 | -7.30704 | -60.59819 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad0db9c3-2e6a-39d7-b6d5-940d4e86fc96 | -9.03182 | -65.34544 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47c8406c-4c15-3268-aedc-2e94c6df1425 | -6.11998 | -57.68508 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8fa86659-64b9-35f6-8e1d-41dda9f7c108 | -7.05119 | -52.72018 | 2026-09-01 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e1f7a05-8792-3921-8b97-55d827b45752 | -9.17332 | -59.63402 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README82.md)
