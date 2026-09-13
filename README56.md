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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5bae804b-49ea-38fd-937f-ce21c21877ea | -6.0897 | -57.9056 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a0d5bee-41ce-34ac-83a2-f71d70067396 | -9.46252 | -59.19302 | 2026-09-13 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22c0a4f8-6971-3fde-bc87-be63f6ffeda3 | -6.95748 | -59.74856 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf01b537-db49-3942-b685-3cb2e650034e | -6.96324 | -59.74592 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 971dcc17-eec9-3c6f-b8ad-edc869a03f7d | -6.30603 | -59.95475 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca71ebd9-0623-316e-86fd-243ed69dc680 | -6.61192 | -58.86524 | 2026-09-13 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce39548c-359b-36ec-bef8-6bf6e2f3dfa4 | -6.31285 | -59.95821 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1433de6-ff72-3e48-a02f-1c8709b515a0 | -10.58617 | -69.60741 | 2026-09-13 05:55:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8ae3cc5-bb18-3522-8a6d-502daa1ef16b | -7.68704 | -72.41787 | 2026-09-13 05:55:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6358b5e-fac8-3bb4-bcca-786f80863d92 | -6.3664 | -57.86582 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd634b23-73e0-3800-8eb9-d7db8c2217a2 | -8.8682 | -62.52036 | 2026-09-13 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e9b7d353-610e-35ab-9251-de7e378de74a | -1.22323 | -54.12076 | 2026-09-13 05:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1fee623-ae56-3d9b-8e5a-ed77e26f07d6 | -6.7951 | -58.79445 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ca35415b-484f-32b1-8458-1ad7c8589f6c | -8.52378 | -70.59595 | 2026-09-13 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38e98279-b132-30ed-9d0c-59b8f9089d6a | -8.97687 | -70.59512 | 2026-09-13 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cc0bb1d1-ba91-3f2e-85e2-03d912f0103a | -6.31588 | -59.97464 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2444817-9e1c-3bf0-95b2-69e0f00112cc | -5.97154 | -57.76771 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f0551b68-a41b-30ea-bf6b-58aa9a27baa8 | -6.28843 | -59.9302 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff4952a4-74a5-3f18-9406-4b6876d6d489 | -10.58563 | -69.6109 | 2026-09-13 05:55:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01ddeb50-2a58-348d-b306-44ee55528820 | -6.673 | -58.71171 | 2026-09-13 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a8f0f949-a383-3a17-8c4e-f8a20e10d783 | -6.59668 | -58.85168 | 2026-09-13 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c9dd3b8-92f0-364c-a8e6-f21c72715fcf | -6.07076 | -57.86729 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f4fe2ea5-e8fd-39b4-83e3-f8fb045d47a4 | -8.00133 | -70.60957 | 2026-09-13 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00d6b2a2-afd5-38da-ba9d-baea3da944bb | -6.20133 | -57.77866 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cbc26ed1-ed42-3c3d-b6f5-c05682830e98 | -6.60027 | -58.8673 | 2026-09-13 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73901c4c-34c6-3129-8e5c-17b0b904c20a | -6.30295 | -59.95356 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d2a671d-a23f-36cb-acf2-7928033ff567 | -8.55038 | -70.86221 | 2026-09-13 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 358f45af-8a57-34ef-804d-38c134c68f78 | -5.96441 | -57.77578 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 05e20c2c-3a87-39d6-a11a-aa442588aa62 | -8.63478 | -66.5056 | 2026-09-13 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dcb52bb7-e750-33c6-9b5e-a1a6d00cab4f | -6.67277 | -58.878 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9457bf49-e998-3c85-8b68-934b44553d3e | -6.66564 | -58.88047 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12609048-d374-3203-be77-22110ceb6b7a | -5.9674 | -57.77111 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e8ab715d-1bb4-3ad1-811a-3e9aa36e5704 | -6.30985 | -59.96485 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ab45eed-52c3-34ce-9dd5-c3b29462302c | -8.76955 | -61.39619 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e88e9570-7176-39c0-91cf-9bad2b62c8c1 | -6.27856 | -59.92533 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3a25173-e8d9-3d23-9cfe-b677f283cc1d | -6.13593 | -57.69845 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90655a0a-6523-38a2-8e0d-1d5139cd2d37 | -6.59419 | -58.87019 | 2026-09-13 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 99a5afe3-8e83-359d-91ee-46a8c497c6d3 | -6.67638 | -58.71167 | 2026-09-13 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3dcd4afa-8f23-30aa-889f-c365a7d880d9 | -6.66667 | -58.88089 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8607f146-ed04-3fa2-be46-f57a854b5f8d | -6.59768 | -58.84425 | 2026-09-13 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa5f2e58-6695-375d-a53c-5db35e5df9e8 | -6.08369 | -57.86075 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 47c41673-9d0f-3118-91b5-f7c7f3d4bc2b | -6.30129 | -59.95103 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0e8ce81-e27f-3ee7-a4a6-ba7941fd4d90 | -6.646 | -58.82443 | 2026-09-13 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19c6daee-2ee8-3813-91b7-fa8057ad54ec | -8.54581 | -70.86903 | 2026-09-13 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 646f31dc-aa3c-3786-ba45-879fd9114a3b | -6.12823 | -57.57403 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 79516dcb-67c4-346b-a672-215da9526fce | -6.61851 | -58.85866 | 2026-09-13 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0106d057-d22b-3e37-aa88-743c87e10b02 | -8.15271 | -70.17253 | 2026-09-13 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5df8e8ba-eaf3-3c7c-97f8-e452e3b72052 | -6.12884 | -57.56951 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d0dcc9d7-c137-3577-8cfa-cb733a7a060b | -9.16498 | -71.84543 | 2026-09-13 05:55:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44720c8a-9b71-35a6-8e87-d9c461f2b60f | -6.66006 | -58.87967 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b7efb17-cd1a-37d5-b8c5-613da75e7f52 | -6.3103 | -59.96175 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e04d55a7-5426-3aaf-ad1f-61c33032456b | -6.36581 | -57.87033 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6adf9909-374f-3568-a664-c3098638b8a8 | -8.7584 | -71.03223 | 2026-09-13 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c599a2d-9658-39f6-8aef-36678aba7ce9 | -8.95165 | -67.3888 | 2026-09-13 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c8af748-ef0e-37a3-ac58-b7aea82dca95 | -6.10268 | -55.67965 | 2026-09-13 05:55:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 79507893-9d77-3865-bf29-8ca06313567f | -6.10343 | -55.67401 | 2026-09-13 05:55:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5e90028a-a365-3b1a-b798-51fc744b77e9 | -8.88961 | -62.56491 | 2026-09-13 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 72eb8c65-8e63-3002-a516-0224d046250a | -6.30042 | -59.95715 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 715befc9-6e2b-39f1-8c02-2b9b7b9cf95f | -5.97093 | -57.7723 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0c785037-b78b-3f14-ac6a-108a1b47714b | -8.81592 | -61.40873 | 2026-09-13 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 328216e2-7aac-3c16-9c48-eda5f7b9559c | -5.96501 | -57.77125 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 412f0979-90b7-3835-9c79-046a53e791da | -6.27767 | -59.93165 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b008db5-df45-36db-9eef-ea7c578375cd | -6.66059 | -58.88368 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6ff08c55-dd91-3235-86d0-e57c96214b99 | -8.59244 | -70.88815 | 2026-09-13 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e564ac2d-fcd8-3219-b11d-62b9dda0ff70 | -6.60276 | -58.84883 | 2026-09-13 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c12dbf3-ad15-3ae3-8a11-df8801509933 | -5.9656 | -57.76687 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bcdc2133-ea08-38a8-893f-af1deea2e3f0 | -6.61801 | -58.86234 | 2026-09-13 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f1acd9a-6520-3d9b-ba97-5682ec3dee4d | -7.64298 | -73.09978 | 2026-09-13 05:55:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e43a7af8-bbdb-3662-9884-edc957a3c4c2 | -6.30515 | -59.96093 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8793997d-1c35-3a79-9d65-ae8f0fd1e352 | -6.30253 | -59.95667 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04bdc07e-0b7e-3c51-9035-16f0536f8ef9 | -7.696 | -72.47723 | 2026-09-13 05:55:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08c32cb6-fb37-30f6-894f-76d85fbe8818 | -8.53751 | -70.74731 | 2026-09-13 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 684abc45-0b95-387c-9527-09449e285c64 | -1.19195 | -55.72309 | 2026-09-13 05:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 11664a1f-aff1-3ea5-a07d-cf246f95c844 | -9.21389 | -71.81631 | 2026-09-13 05:55:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd80821b-3f97-3219-a5da-995fb2b6dd58 | -6.60226 | -58.85254 | 2026-09-13 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7563b793-ab88-3df3-beaf-f85b49e82305 | -6.30727 | -59.96052 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf6cd365-ccd7-3cb5-856a-144c81cd48df | -8.84909 | -71.08078 | 2026-09-13 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe9d3a2e-5a3e-3bc5-a4d3-78270172806f | -6.31674 | -59.96835 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2c961e8-a951-3db1-a281-933e8fe11ff8 | -6.30086 | -59.95407 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ef2fb24-8f40-3a5a-9260-1d389ceeea78 | -6.312 | -59.96446 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f4e48b25-40e3-3e33-a86f-c79822c3c5bb | -6.67779 | -58.87464 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 15fa8d46-7577-385f-a4f6-4395d3921039 | -6.06696 | -57.86535 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a44a5eaf-ab51-3c56-90be-69c89f5f80be | -6.28327 | -59.92934 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b0843bf-6d36-3461-935a-35a10cd66118 | -6.68338 | -58.87538 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6259092d-97b3-30bf-8f8d-f9e48630f4d3 | -8.03967 | -70.09583 | 2026-09-13 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73fed8be-4033-3858-bde0-b4cbe903d592 | -7.69232 | -72.47663 | 2026-09-13 05:55:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 803ce0e7-4546-3b6f-96a7-34eed806256b | -6.5916 | -58.84716 | 2026-09-13 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 50c3a054-7555-3ec1-ac1e-e6e6b3c33a5d | -8.5464 | -70.86533 | 2026-09-13 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28b9e273-c7cf-3cbd-9019-78c34eeea7cd | -6.07286 | -57.86626 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b45034f-6195-3f80-8084-4d9b620ce74b | -6.67587 | -58.71555 | 2026-09-13 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf808547-f8f6-3bbf-ba17-130f4f949349 | -6.1156 | -57.66824 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b822ee5d-c455-3e57-874e-99c548dba171 | -6.67171 | -58.87757 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f3565425-4b9e-3436-927a-19ef39b50772 | -6.18858 | -57.71468 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3f1c53bc-4265-3fce-94b1-e5f14583a612 | -8.889 | -62.56941 | 2026-09-13 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ae56930-7062-38a0-82a1-2fda7eddbb6b | -5.96676 | -57.77564 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9facd981-e060-3b66-b7aa-f1cb563bff81 | -8.54005 | -70.60226 | 2026-09-13 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c704577-710e-3922-a9b3-b61350f26767 | -6.31158 | -59.96756 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| badd2e3f-dbf9-3970-b4cc-a5c01eeac849 | -8.52715 | -70.59648 | 2026-09-13 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7eb70f72-51a0-30ef-a15e-8d37d574ced6 | -6.19174 | -57.71352 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 740fc859-ee49-319a-baed-4571b4ec6b86 | -6.76551 | -59.43 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README57.md)
