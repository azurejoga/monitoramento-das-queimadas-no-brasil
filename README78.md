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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9de02853-0099-32c2-92cc-735a28169be3 | -12.13289 | -63.16 | 2026-10-06 06:22:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 926ecf9d-bd4d-3c57-a079-3df68b518403 | -7.82953 | -72.8606 | 2026-10-06 06:22:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb1b9d19-347b-36ab-8321-06f73228c42b | -8.42988 | -70.11874 | 2026-10-06 06:22:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c83adb9-4994-383e-8f35-fb38c0de3ab9 | -8.93242 | -67.34991 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8a3952c-da84-3d5e-a8d6-2a66c27202b6 | -9.50149 | -67.68279 | 2026-10-06 06:22:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0c80334-ce80-3e2c-ad09-a5d39213b699 | -9.11612 | -67.71235 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 852515c7-c7b1-310c-9152-cc1401e71526 | -9.22939 | -67.89548 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f733b19-bd91-353a-a67e-8607acf4e717 | -9.71584 | -65.10045 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f6195be-957c-3770-b2d1-5853c18dd5e2 | -9.95914 | -68.7782 | 2026-10-06 06:22:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4d335b0-b203-3534-bab9-9c8793d81144 | -8.87051 | -68.53468 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c984b3bc-80ee-3f04-871f-5dc0938edd13 | -8.28416 | -71.07352 | 2026-10-06 06:22:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59eb6009-6728-3198-b9de-fea86d4ef576 | -9.10547 | -68.31587 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88d814a3-b6ec-3600-b05e-ba22edc0211d | -8.60379 | -72.72749 | 2026-10-06 06:22:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36e7f30a-d3bc-383b-89aa-25b19d865403 | -8.36842 | -70.57513 | 2026-10-06 06:22:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 546ec209-8e1b-3b2b-bfc6-0fd3c917904f | -9.1138 | -65.35778 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 383ffbec-ac5b-3b94-a9af-59a28e54bcb7 | -12.1323 | -63.16489 | 2026-10-06 06:22:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9c65c20-774b-37e6-a632-b8035cd7bf2d | -9.107 | -67.81082 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c39d26b8-77a3-3370-a784-01a84c5e3b53 | -9.11233 | -67.70741 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a19db32c-9cd5-3efa-b1ef-ea1cb06892ec | -8.96859 | -65.44277 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1991ce0-8407-316d-abde-ab001dedcb15 | -8.87164 | -67.00395 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 356a5d34-1224-30ac-b20d-2c171113a69b | -7.90641 | -70.91653 | 2026-10-06 06:22:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f6263ea-34ed-356d-8157-00f39cf532b7 | -8.9733 | -65.44651 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f055edf0-0b1a-3015-92b3-104a41356e53 | -9.49058 | -63.95222 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0fde060-4027-3c87-a534-1f0c63de2cff | -7.90702 | -70.91248 | 2026-10-06 06:22:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed570303-d3c5-3665-831f-f16ddaf72876 | -9.40179 | -68.87706 | 2026-10-06 06:22:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ad0e5d6-0374-31c3-8b42-422e4cdd8b26 | -9.29163 | -65.64576 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22c31f4c-fc14-33ce-9942-3154aa1ed22a | -9.10474 | -67.69552 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03f530aa-8e73-3ae3-815a-0dad9f5b97df | -9.11228 | -67.70534 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2fa934d9-f11d-3bba-adc4-f3c952cc6881 | -8.61049 | -72.72852 | 2026-10-06 06:22:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b03f068-c779-3c81-be67-33c552907b4f | -8.58694 | -70.9339 | 2026-10-06 06:22:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d4c9447-3066-3de5-bfbc-3e4379f81aa1 | -9.12591 | -68.29401 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 590c7d59-d866-3081-b2c2-548cc37d9c5f | -8.85379 | -66.7981 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3adc1a90-7d5e-399d-8e92-14b19d898a71 | -8.63198 | -69.50501 | 2026-10-06 06:22:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8f9d818-7af9-3f28-8230-05d0018e219e | -9.02278 | -65.7163 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b8261ce-c910-37be-9ceb-cf201e56ba66 | -9.54483 | -64.81699 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e14e637-5d08-3dc5-b058-865b1e4659b1 | -9.26982 | -68.37475 | 2026-10-06 06:22:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3352e8e6-8eff-3fe9-9c1f-7ef01878ce82 | -9.48501 | -67.67162 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bd99aa7-8e20-31fb-a755-abce7426491c | -9.33949 | -64.7127 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f32bc9b4-7eaa-3c64-aaab-769f2bbf3149 | -7.82004 | -72.83387 | 2026-10-06 06:22:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b0f6ff1-2ebe-3086-8267-a7a6d34ebd6b | -9.11025 | -65.35793 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad421921-a84a-34d7-8072-492afbaf470f | -9.36741 | -65.8065 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7112866-1ab4-3531-98d1-64c586f99cf8 | -9.72285 | -65.08817 | 2026-10-06 06:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c149496-b503-3c2a-bcc9-da1cc8482d9e | -9.14448 | -65.41637 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00d8a202-ca13-309b-996b-2da81541e9e0 | -9.10491 | -68.31976 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37c245bd-df3c-34f0-83d8-56e7aef13807 | -8.59502 | -66.8148 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1452d4e-3798-3ce8-ba5a-9d9f67978289 | -9.13692 | -67.81941 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 24e324b0-a2d3-351a-aa65-4e17c537c04b | -9.16096 | -68.25902 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d2c7b21-243e-3a91-ac9d-2b9294a72b76 | -9.1663 | -68.25175 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b34597c-3fbf-36c0-9927-ee5489f2ac94 | -9.36779 | -65.8036 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0d2dc72-280f-3e75-adf4-6cec97d917dd | -7.91601 | -71.77908 | 2026-10-06 06:22:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f828dff2-6607-3164-a997-b903fb0373c2 | -9.89219 | -67.33138 | 2026-10-06 06:22:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 679748a3-ab02-38fd-81f0-3033824670dc | -7.43497 | -72.58215 | 2026-10-06 06:22:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfcdfb3c-786a-3f01-9378-d70920b955d8 | -9.11752 | -68.32172 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbe13738-def5-3c0b-bd90-8848a3a2bd26 | -8.94213 | -72.84557 | 2026-10-06 06:22:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e92b459f-ea12-39a1-b29e-ce8332efccf9 | -7.81616 | -72.83686 | 2026-10-06 06:22:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f55a183e-d66c-3fe4-9a54-8b2f58ad2712 | -7.64723 | -72.43665 | 2026-10-06 06:22:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d06cc85e-0e54-3996-860c-348853e5e1dd | -8.39264 | -70.11311 | 2026-10-06 06:22:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d7c5504-32ac-376a-8dbc-1b06fa20b940 | -8.59038 | -66.81419 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc655535-78ca-38a2-84c0-3faf170aecbc | -9.36761 | -65.80642 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78e0adcc-a42a-31b8-97ff-eac9afbd691f | -9.16318 | -68.2432 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 054949d9-0261-3a8f-b195-594b71cfd068 | -10.14867 | -69.02354 | 2026-10-06 06:22:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ffa7d5b-fa61-3c10-9934-6a38e593871b | -10.27033 | -68.83655 | 2026-10-06 06:22:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39a3f583-022c-30ef-95bf-ea073e996047 | -9.09711 | -67.75318 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1f480ff-00f2-32fd-806b-a7e4abd28d51 | -9.1051 | -65.35719 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9edc4c77-95e2-3b60-b531-b6f49e2bb143 | -7.43162 | -72.58164 | 2026-10-06 06:22:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af05ec02-57a4-3cc5-bc39-f921508b6da8 | -9.955 | -68.77765 | 2026-10-06 06:22:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d4a63da-84b3-3558-b4ba-767c6e8bad7a | -9.15471 | -68.24195 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5da2c180-9953-34fe-90fd-8131e616513b | -9.11166 | -67.70963 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 435e9d5e-1a2f-3d95-8423-c19edb516ef5 | -8.97354 | -71.41209 | 2026-10-06 06:22:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1516c147-52c2-3efb-8b24-4d77575cbb57 | -8.92151 | -66.84454 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 474fea8e-a6ac-3bd1-94ed-1df2ed0feb49 | -9.07818 | -65.3876 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f9de594-da70-367e-87b8-e383130f6965 | -8.62881 | -69.49953 | 2026-10-06 06:22:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7db31be-be97-3036-9df4-a593ddf153b4 | -9.10472 | -67.69755 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd5a2c90-c14f-387c-994e-73e608e457f7 | -8.61337 | -66.94701 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3ca48b6-b252-36e4-8958-ef4f7f219c68 | -9.38382 | -68.33012 | 2026-10-06 06:22:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a353ce8-dce9-3f7d-84d1-847500ac3024 | -8.59893 | -66.81317 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 099eff49-4327-38c9-9f95-ca03399ada80 | -9.10911 | -68.32042 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e763dcbc-c279-33ce-bb7a-976caaa89235 | -8.9308 | -66.84585 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4f2b23f1-4646-3396-bdf7-e180b5ffd352 | -9.13318 | -68.24377 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c500f0d2-120b-3854-a894-47d5d791fd15 | -9.26031 | -68.38136 | 2026-10-06 06:22:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87429b3a-a9cf-356a-a182-90d073a4534d | -7.99875 | -70.99993 | 2026-10-06 06:22:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09add54f-5317-3635-9d4d-880069c1600d | -8.87021 | -68.50784 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 501247d0-211c-34a7-a685-8bb2c858d7c9 | -7.71273 | -73.04417 | 2026-10-06 06:22:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e204d2ed-0443-3937-a8aa-55d0c43e121d | -8.92616 | -66.84519 | 2026-10-06 06:22:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1ac2fe8f-6f48-3d67-ab01-f3d6b5c3d456 | -9.39645 | -68.27127 | 2026-10-06 06:22:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0df9e3f7-45cf-361d-b95f-45b42fb12334 | -8.77934 | -69.5338 | 2026-10-06 06:22:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a91ceb30-165f-3d33-ab08-7f382f8454a7 | -10.14172 | -68.39869 | 2026-10-06 06:22:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 732a1730-d440-35f4-a8ba-b87cf793c413 | -8.75671 | -68.97358 | 2026-10-06 06:22:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36e17663-a32d-3e9e-a924-ddf4e52f042a | 2.45968 | -50.83099 | 2026-10-06 06:40:00 | AQUA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 131.5 |
| 6511e350-b103-36a9-a960-c4ccfbd63d96 | 2.46551 | -50.8226 | 2026-10-06 06:40:00 | AQUA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 36.7 |
| acd4c886-379c-37ac-ad15-05acb6582127 | 2.4631 | -50.85391 | 2026-10-06 06:40:00 | AQUA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 2b3c35d7-2ca4-3163-a4cd-f11e6df7fa53 | 2.45511 | -50.84755 | 2026-10-06 06:40:00 | AQUA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 71.8 |
| fe33dc6a-ccf7-3f12-947b-2c78c0505c29 | 2.46877 | -50.84555 | 2026-10-06 06:40:00 | AQUA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 34e95093-b6cc-3320-971a-a57220456210 | 2.45187 | -50.82456 | 2026-10-06 06:40:00 | AQUA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 1be352a2-a20f-3c11-879f-979742f8e6eb | -5.82892 | -45.00263 | 2026-10-06 06:42:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 560c0274-7239-394f-b492-4277f8d0dcfb | -4.45448 | -47.92646 | 2026-10-06 06:42:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| f5bd3290-bcb7-39ed-a35f-e608a159922e | -3.08475 | -54.2372 | 2026-10-06 06:42:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 88600a26-9e91-3b22-8013-e252e1d1d44b | -6.67066 | -43.82188 | 2026-10-06 06:42:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bdd12d17-9f5b-35d1-9aef-a078c33799c7 | -5.83769 | -45.00393 | 2026-10-06 06:42:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8fd22e20-6145-3b9f-a2ae-949e302f2cd8 | -5.74853 | -46.68377 | 2026-10-06 06:42:00 | AQUA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README79.md)
