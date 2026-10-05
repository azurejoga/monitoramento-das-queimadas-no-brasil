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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82c4d217-463e-37de-a232-db26d4814ddd | -7.43275 | -63.56743 | 2026-10-05 06:20:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 558e2edd-8c36-3b0f-b6cc-96e8bd2a7dba | -9.15331 | -68.23404 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07526ad6-2e50-3183-95a5-3f3f32c0a79c | -9.06296 | -67.73336 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28fd34bf-b4f1-3038-920b-c474ed3bc930 | -9.13278 | -65.91128 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1135f5b5-838c-3521-986e-909de9979c2e | -8.74411 | -72.82721 | 2026-10-05 06:20:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8705eec8-7a0f-382d-82ef-0967eaefcc92 | -9.16438 | -68.26406 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6b1cf40-f762-3c4d-b54f-fb536203e1cc | -8.04923 | -72.43418 | 2026-10-05 06:20:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c69e26d5-7123-3205-963d-110c9de11d3d | -7.6592 | -67.16258 | 2026-10-05 06:20:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96689bdf-7a18-3e54-97f0-3b3e7508c56f | -8.64589 | -62.52999 | 2026-10-05 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a29b5d3a-45f2-3456-8c1c-ef35c9db1d9b | -7.68328 | -69.93346 | 2026-10-05 06:20:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0a41f4d-ffd0-3916-867d-8a601e7957a5 | -9.16371 | -68.26865 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f4bec93e-74e4-3776-86ed-70e2d4d30abb | -9.15749 | -68.25829 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49d0a2d1-45b9-3715-91e2-9034762e7f84 | -9.15236 | -68.26691 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59923edf-ef30-39f0-bf68-9d627af3f7cf | -8.60392 | -70.20142 | 2026-10-05 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01257c5c-afb3-3f08-b188-12c91a05fd40 | -7.3612 | -72.60805 | 2026-10-05 06:20:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6a554cfa-5c48-3c8f-a0ea-95c343c5cf8c | -8.65591 | -66.93453 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25445421-fcc4-31a1-96b3-93569b927454 | -9.39786 | -65.8994 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5935f734-f41f-38b7-8ec8-62d294e854ff | -9.4035 | -65.89137 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8728dab7-f38b-37a6-bed5-78ea20d61b14 | -7.36398 | -72.61211 | 2026-10-05 06:20:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 381035f6-0d2d-3aba-bc34-58cd3c2923c0 | -9.4498 | -68.57396 | 2026-10-05 06:20:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9824c1f-422e-3f77-9519-88d1ec56a003 | -10.05743 | -67.56109 | 2026-10-05 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41468348-ec83-39e5-b401-fb02278bbca8 | -9.12202 | -68.21706 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b269450-4130-3eae-a490-efb12c8e2c99 | -8.59918 | -66.80694 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91981ae2-aeba-32b2-872f-d81a8c336237 | -7.43672 | -63.56387 | 2026-10-05 06:20:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72d2c5a6-0c6a-3e1a-aba2-68c852562154 | -8.43741 | -70.1079 | 2026-10-05 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8644e48d-7dbd-3ef4-b3f4-5a9703937798 | -9.22133 | -68.16827 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2dab9238-8529-3107-b968-5272d0ee830f | -9.44049 | -68.06525 | 2026-10-05 06:20:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80a1cd02-0129-3765-ad1e-a45d88a9ede9 | -8.44143 | -62.72031 | 2026-10-05 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7c0c8192-e49f-3b3f-b81f-b506e9f10829 | -8.66995 | -70.04591 | 2026-10-05 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f089074-f256-3201-a0ae-05bc2720ec8e | -8.56188 | -67.06687 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c713ca58-42c9-33d8-8557-151670ac2c72 | -7.70558 | -73.10895 | 2026-10-05 06:20:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c850b3de-ea12-3d97-9eb7-cf58951f3e6b | -8.34261 | -62.82903 | 2026-10-05 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 68edcd6f-51ee-3ed1-976b-98cbcba0e85b | -9.14078 | -67.93569 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7783015-a300-3ee8-8f6c-59a9c3782b5a | -8.38407 | -71.06518 | 2026-10-05 06:20:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4b2d3a61-a7fa-30a1-87f9-7ed9d0fab303 | -10.24335 | -68.30447 | 2026-10-05 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42b10abb-0349-30fb-abdd-902d670a8fff | -9.11471 | -67.70769 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ea79c248-deb9-3f72-9069-c6914cee4000 | -9.21752 | -68.16771 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a2c005b-53e4-3b7f-9d55-015c7767bd79 | -9.40289 | -65.89574 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1c139b1-848e-30ea-b961-6b2893431db3 | -8.59454 | -66.81001 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee0123a7-a5c7-3d8b-90d9-216f82cb7dfa | -10.27011 | -68.83157 | 2026-10-05 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9effba93-7187-35aa-9566-4bdcab927c82 | -9.10854 | -68.30245 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b67367b-33c4-31ed-b4d5-0c7af5274fe2 | -8.74745 | -72.82774 | 2026-10-05 06:20:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 407cb37e-ac3c-39c5-bb81-1462e34b02c3 | -7.45266 | -63.56023 | 2026-10-05 06:20:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 38fae7c0-f1c6-3c2e-8d48-160a94460f78 | -8.34706 | -62.83651 | 2026-10-05 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b54550b7-1950-3ee7-84d7-30c630b5bf74 | -8.7868 | -69.46777 | 2026-10-05 06:20:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 858862cf-f3cc-354f-b305-265bf2352cdd | -8.3466 | -62.83989 | 2026-10-05 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 073a39c1-62a2-3ebb-91dc-7f93b2860d46 | -9.50377 | -68.49452 | 2026-10-05 06:20:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62fedd48-86d0-3a61-87b8-bafe49665b4d | -7.44761 | -63.55951 | 2026-10-05 06:20:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 050ce4f0-d3af-3beb-b2b9-ab9ad468c890 | -7.41528 | -64.66476 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a49212e-30a1-30a4-a910-2233a47f4bc0 | -8.58938 | -66.81676 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78cde967-6dc2-3887-bdc6-0235b9ebaf39 | -9.22984 | -67.8727 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edc80ae9-74bb-35e9-a4f5-f08d7a6eada9 | -7.66 | -69.93053 | 2026-10-05 06:20:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fba7908-672a-3ab2-b9c3-30677260e48f | -10.1417 | -68.39776 | 2026-10-05 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5f4d9e5-bb5e-3cfb-a5d3-faf8d8fdeb65 | -7.43752 | -63.55804 | 2026-10-05 06:20:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b5a80279-e5ae-3136-8f30-da8ff3497c91 | -7.52539 | -70.39234 | 2026-10-05 06:20:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5fd4fb0-8a22-37e9-897a-3425133a4ffb | -9.23087 | -67.89261 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab5101d5-b6cd-340d-83e5-4e6bef6959ce | -9.67037 | -66.82679 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82a0bbae-e4a1-3fd8-aab6-877584283b08 | -9.67454 | -66.82737 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b05183b9-15d2-3ee3-b551-abeffa7e8084 | -9.12397 | -65.91002 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f1e835a-4c69-37fb-8be3-9c3d4c2fc285 | -7.43167 | -63.56314 | 2026-10-05 06:20:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7575823-d09c-3771-8176-5031a78eef5a | -7.43592 | -63.5697 | 2026-10-05 06:20:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0a3f1f8-7856-3be6-9f91-9b93fbfee29a | -10.2664 | -68.831 | 2026-10-05 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a20768a4-a68e-3206-b6b1-50460d937476 | -10.47963 | -68.6096 | 2026-10-05 06:20:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5410ab23-a28a-38df-bc19-3ea03d81e433 | -9.12837 | -65.9107 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a161a5a7-43f5-314b-8b88-8f396b5ecf7e | -9.47421 | -67.10702 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e95ec02-04b8-34fa-949e-08883d40f41f | -8.77649 | -69.53535 | 2026-10-05 06:20:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0cb92c2a-e511-36bc-867e-7c4213ecefc0 | -8.34799 | -62.82977 | 2026-10-05 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a63826b-312c-31ca-8f02-e0c7ba449d2f | -7.43864 | -63.56233 | 2026-10-05 06:20:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 158b3bf0-bbbf-378e-9c9b-c51f93e7c437 | -7.43948 | -63.55654 | 2026-10-05 06:20:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 40ba9ccc-5fa5-36c0-811c-f98985e24587 | -7.45185 | -63.56606 | 2026-10-05 06:20:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 88317fa6-c758-3946-8eb4-fba655aa4d02 | -9.11594 | -64.36287 | 2026-10-05 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5255e735-6810-3db2-991d-55a9ae953e14 | -9.12335 | -65.9123 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20c69aca-7e62-3870-a36a-0ea9814a09bd | -9.13546 | -68.2502 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8fe23069-7b40-3923-8bc1-9d3c7b4979d0 | -7.44681 | -63.56533 | 2026-10-05 06:20:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e80a0794-7fa1-3dfc-bbb9-4c0d1692a6cb | -9.13167 | -68.24963 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aebcae2b-6acf-3c94-8663-1f7c9e6b6195 | -7.36455 | -72.60859 | 2026-10-05 06:20:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c59c5cee-9264-3ab4-bc38-c51e6d226b34 | -9.03287 | -67.55587 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 860556a9-036d-314d-91fe-19839b430f30 | -8.61991 | -69.50041 | 2026-10-05 06:20:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e9223a6-ba0e-3352-baf3-c53538cec637 | -8.5899 | -66.8131 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9e05c0b-8603-3330-8c1e-f4f9a328bff9 | -8.87108 | -66.64648 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ec9ccdd-8f7e-3a20-b529-70aed66598ee | -9.11893 | -68.21185 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6aa05063-2614-357b-a67d-26a9e8fff367 | -7.36063 | -72.61157 | 2026-10-05 06:20:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 924828a0-6870-34f3-b714-481a77594bca | -8.62344 | -69.50095 | 2026-10-05 06:20:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38c6581a-dd41-3cdd-bfbb-93d2cef92fbc | -9.12834 | -65.90868 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e24509c3-d3ef-3541-a662-8262f8048734 | -9.15303 | -68.26231 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5a1b7dd8-39d0-3542-b687-960a0762d90d | -10.61802 | -67.92229 | 2026-10-05 06:20:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 606a7ddf-bc02-3467-9800-3894dfc6e30b | -9.47766 | -68.59184 | 2026-10-05 06:20:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b009b00a-d812-3afd-8e7b-094b57d17a39 | -7.43087 | -63.56895 | 2026-10-05 06:20:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c38ccfa-b6f9-3856-b78d-90f83125a4d3 | -7.44256 | -63.55878 | 2026-10-05 06:20:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 293aebb3-3911-3c72-8c25-788c40f3c490 | -9.89294 | -67.32838 | 2026-10-05 06:20:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bc7fc55-373f-332b-803f-d493be2e645b | -8.65139 | -62.53084 | 2026-10-05 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35ac9f57-1c6e-35f4-9b62-0d0de3d41e92 | -9.16817 | -68.26465 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd9a4ff2-749a-3ea8-a2b5-34e7913af053 | -9.12272 | -68.21244 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdabb808-3cbb-306f-8383-94c565e07e41 | -8.35243 | -62.83728 | 2026-10-05 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 482e3b5e-5d1b-30e0-bcce-9ce1c8c72b8a | -9.10882 | -68.30437 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32c8f89f-8e2f-3abd-b442-6ef34e32b168 | -8.35569 | -62.81362 | 2026-10-05 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb8283a5-61fe-3624-975d-3fd163558eae | -7.66459 | -72.42995 | 2026-10-05 06:20:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a61296a7-05fe-3ef1-b8d8-490f0b9a4fad | -9.25847 | -67.64987 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9fa13e70-207b-3ed4-988c-7aecf11ea035 | -8.3529 | -62.8339 | 2026-10-05 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb466f40-4200-3eb9-b8b6-6479d3bcdc08 | -9.43736 | -68.05989 | 2026-10-05 06:20:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README60.md)
