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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddac720b-dc0f-3f26-876c-d76043190acf | -8.8514 | -66.79623 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49785c48-5fd7-3de2-9972-04e0bd2bd982 | -9.11712 | -68.3217 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf422f0d-47d1-3e48-9d49-060cdb3f7dc5 | -12.61056 | -60.90374 | 2026-10-06 06:01:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 740992a3-26e9-31b2-99bc-f2d764d77dea | -9.16862 | -61.40485 | 2026-10-06 06:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5f5aa9b5-9f87-3a3c-a687-a3ade21ced9a | -8.87663 | -67.00529 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1454717b-288d-3863-8be7-d1078738f953 | -8.36951 | -70.57565 | 2026-10-06 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e48473bc-cd9c-39f2-a222-264c3aadafbb | -9.1495 | -68.23946 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b30962b-b0a0-3e0a-9d63-88f153ec5284 | -8.62814 | -69.49965 | 2026-10-06 06:01:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bb35e67-1684-3c9c-8bbb-aeb01852b974 | -9.7584 | -65.08335 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5eb3f3b0-4ed6-3df3-a552-db0f85b3ebd0 | -9.49383 | -63.95196 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 493e1317-0cf5-3463-8277-0b91f1b28dce | -8.82121 | -64.22961 | 2026-10-06 06:01:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72751c78-e0a3-348d-a6c1-d4c9ebf0fb0f | -9.5428 | -65.68785 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 123c3187-b4c8-3d50-9349-8aec447e2e46 | -9.15341 | -68.23646 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c066eab7-63e2-337b-bfa9-0ed4daf93bde | -9.48641 | -63.95084 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da797302-d4d1-3fac-8d12-911988cab226 | -9.16231 | -68.24517 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30bf6fb2-480f-36f6-b3cb-5f2a59dfb614 | -9.35544 | -68.92461 | 2026-10-06 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 256d1ad5-53ce-336f-88ba-f53ff93d4c1f | -13.5188 | -61.11215 | 2026-10-06 06:01:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2aaf10a-b0ac-37d1-a845-52b9e9cda5b3 | -8.60335 | -66.81083 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39019704-a557-3f95-8902-44d60cc69a75 | -7.36394 | -72.45963 | 2026-10-06 06:01:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a67ca211-a2d6-3e4b-8773-b2014702032a | -9.49012 | -63.95141 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf474bfd-19f1-3b21-aa78-05361aaf7603 | -8.75066 | -69.29402 | 2026-10-06 06:01:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95bd6945-36fb-36dd-adb9-b3cfaf2ad34d | -9.41357 | -68.8894 | 2026-10-06 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad7e664a-87f3-39ca-8930-84a30264b56d | -8.62612 | -64.1165 | 2026-10-06 06:01:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fd10a5b-547c-3176-95a7-03d1dc8e38e4 | -9.67687 | -66.82146 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bd8c48b-ffd2-3774-9ddd-03adc8878701 | -9.48269 | -67.61867 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdd5c481-604f-3e13-96f7-7f15b79ceafe | -8.8733 | -67.00477 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28402788-8dec-3d1d-95b3-0b77324f5021 | -9.12528 | -68.20658 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07eb90e6-4ad2-3d42-8440-bb50478040c4 | -8.75694 | -68.9743 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86ce83bb-9c8a-3068-b9f4-966500b63309 | -7.52254 | -70.39279 | 2026-10-06 06:01:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24bb74ae-67f0-3b6f-831e-2c77e80ed266 | -9.26215 | -68.38129 | 2026-10-06 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe46ccf7-2b3d-3fcd-a2a3-9972b3de51ac | -9.0757 | -65.38647 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0cf8cc66-7ec6-3687-8ccd-cae0892144c2 | -8.6183 | -66.9459 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee372317-4cff-311a-aabf-339db631d5e5 | -9.39243 | -68.26765 | 2026-10-06 06:01:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b335ffc5-a03c-3be2-a520-e9879b89af97 | -8.86197 | -66.79431 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e5484dc-aa18-3ccb-8cf5-a88952c0f8bf | -7.89325 | -72.29959 | 2026-10-06 06:01:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea645f6d-2c8f-34f2-abb6-97517b5ab533 | -9.12863 | -68.20713 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68a55ee1-89aa-3ce4-83a6-34efab7fa074 | -9.10596 | -67.6945 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8e472af-b45e-35fb-82bb-707f04cdc03f | -8.34835 | -62.83019 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0561c469-6c53-3173-b076-b21a37f15822 | -9.11098 | -68.31706 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5643adb-f712-3c85-b0ac-6beabb987518 | -8.9193 | -66.84306 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e92d3b4b-9434-3fd4-baee-bea903ea0c6a | -9.10857 | -65.35658 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42cdfba9-b184-33bd-a5e5-1d9a740c0596 | -9.00543 | -62.10192 | 2026-10-06 06:01:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36d5493d-6ab8-3d4b-8b0a-2e94c6621217 | -10.81859 | -69.40018 | 2026-10-06 06:01:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0dc5807c-877e-3aed-b657-ff323cc2df83 | -9.001 | -65.71957 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21f1ed8b-f8ea-3676-9187-dd122a19214d | -9.10915 | -65.35278 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f452cade-11aa-3f19-8ed8-b32b73e95a87 | -8.39806 | -70.10687 | 2026-10-06 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85ba0d40-7499-3ff7-9b99-8143b9f35f91 | -9.595 | -66.14036 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b4d0ea9-922a-36ad-85c0-c6083a330a24 | -7.3612 | -72.60772 | 2026-10-06 06:01:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e3c3185-57ae-36b1-be08-7e7269a954c4 | -8.93433 | -67.34792 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 423995bf-c983-3b9c-ba6b-a68dbc97cd4e | -10.8413 | -68.7263 | 2026-10-06 06:01:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4286f7e-c65f-3718-be16-41656f996c73 | -10.27637 | -60.5467 | 2026-10-06 06:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ecdaa41-c323-35cb-9e6b-086db7653ae9 | -9.15954 | -68.24109 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c58461a5-9de4-36dc-a27e-5ea12c4974e5 | -9.07916 | -65.38701 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48fcd2d1-bb4c-3ad8-821e-33c5e5a03114 | -9.1115 | -67.70258 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42c4cb9b-9362-31d1-8c5e-c89c4abaa390 | -9.82481 | -65.04908 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 13d5ade7-f692-3724-89d7-15c06eb53fa4 | -7.82003 | -72.83109 | 2026-10-06 06:01:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d453b19-8a46-3b84-a04a-a13d023c2cea | -8.77759 | -71.11349 | 2026-10-06 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19b33fb5-fa6e-3039-93fb-b7387d990217 | -8.92542 | -66.84763 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f5883f0e-a679-3afa-8725-3e423833ac92 | -7.85294 | -72.46188 | 2026-10-06 06:01:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1e08763-fdd1-36a0-96b5-937960ade152 | -9.62173 | -65.74157 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1faebc5-6d53-367e-b082-96dbd8400e20 | -8.84837 | -68.80118 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5afcd5c-cc4a-38e5-8c70-e27d88fc2da0 | -8.75353 | -68.97374 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e7caf69-101d-3fc9-9c84-c6794e87855a | -9.82129 | -65.04855 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 927078c6-50ad-39f6-a928-c1765c5ed600 | -8.77708 | -69.53565 | 2026-10-06 06:01:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff923344-55f8-36c1-a7ec-87e142273456 | -9.44521 | -67.42963 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3635828-b291-383f-a8a7-50180aac9cc3 | -9.72502 | -65.0915 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ba8544c6-5de0-3bfe-aa21-0aed7aa4cc38 | -9.19313 | -65.32603 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8aaa3eba-1ff1-3ef1-aef8-568f5cf7a57d | -8.93821 | -67.34496 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d410c221-21ce-35d5-af13-b2366e1fabc5 | -9.09154 | -67.67781 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3692f6cb-1bd0-3bae-bd16-cd79099858b1 | -9.7168 | -65.09824 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2500d8c-a31f-318d-a4a3-e05e7002b9d6 | -9.73265 | -65.08866 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 966166cf-5e3d-3038-8686-45c6ecc13e1f | -9.10511 | -65.35605 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1fbc9ad-0b55-3bc5-ab6d-d532769fca86 | -10.14319 | -68.39716 | 2026-10-06 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c5a38c1-f910-39ee-bb93-1258f980b595 | -9.73205 | -65.09257 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dcde8ba1-30b2-3e35-8cd7-d5be0768a85d | -6.71224 | -66.49399 | 2026-10-06 06:01:00 | NPP-375D | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a99655ed-2ce2-3097-893c-303db9b24d4a | -8.41465 | -70.10841 | 2026-10-06 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e549ac8-f8d7-3133-87ba-5abef046141d | -9.0039 | -65.72007 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1da4edb-7045-3fad-8add-76de293fa99a | -8.9778 | -65.43713 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 656bc744-276c-3f40-be93-d5c32f740339 | -8.68346 | -66.59608 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa26ac8a-0f51-3486-ac47-634c2e98a9a3 | -12.13297 | -63.16154 | 2026-10-06 06:01:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8ac565fe-8671-354c-becd-ca182e02647b | -10.28624 | -67.24033 | 2026-10-06 06:01:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f250a9b-88d8-33ae-bf81-14b4a5cdf695 | -9.71039 | -67.56946 | 2026-10-06 06:01:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a871aff2-3bb4-3866-a2f2-3b2c6d0e3a1a | -8.35186 | -62.8322 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a2e6523-36ff-3c8d-a7db-aeb058bdcccf | -10.81716 | -68.64178 | 2026-10-06 06:01:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a78c328f-0e59-365f-9df3-0a7bcaab8d15 | -10.44341 | -67.89599 | 2026-10-06 06:01:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95a70799-6464-3e1c-b7a1-da29c3f56cce | -8.60221 | -72.72805 | 2026-10-06 06:01:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41cd4a1b-e583-33c9-a041-3dac36a53fff | -9.72974 | -65.0842 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 256259bb-86c5-3e0c-aba6-05e9686cbc72 | -9.23292 | -67.89134 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14a7bdd7-1145-3c4c-9107-6d5366845bfb | -12.6112 | -60.89872 | 2026-10-06 06:01:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0594a1a1-53ab-39ab-9b7c-6fc642af2353 | -8.8503 | -66.80327 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e26d8528-9344-3be9-a11a-19d2a1f30382 | -9.67297 | -66.82448 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d1cd96d-945f-3b81-8e60-f4bd2bd98ada | -9.11094 | -67.70609 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da601d87-f8c5-3bd6-a325-5ffd11c77fb5 | -11.99203 | -60.47223 | 2026-10-06 06:01:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b0d5008-22a6-3032-9a23-27a153b1aefc | -9.72091 | -65.09487 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b3eb68b-fe5c-3576-9a8a-491882b25cec | -9.1561 | -68.26234 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c8699b3-5988-34b3-906c-ee453916a1af | -9.46441 | -64.33083 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b83b8fa-35d4-3551-a867-70f9abf1ca44 | -8.77248 | -62.87614 | 2026-10-06 06:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4daddfc5-fcbd-3ce1-94d9-5ad50bc5d076 | -8.97415 | -71.41112 | 2026-10-06 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b20a9b5-6335-331b-ae70-520d615df172 | -9.19255 | -65.32986 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7f69699-bdfe-3c02-a078-47af96f39992 | -9.71329 | -65.09769 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README75.md)
