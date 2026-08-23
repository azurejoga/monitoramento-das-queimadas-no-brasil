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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 165a4713-1769-3bd8-894f-d127facac184 | -7.78084 | -61.43175 | 2026-08-23 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c19bca4-d995-3aa2-bd4d-865c8fbae63e | -7.40047 | -60.0222 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 251052db-f834-3f9c-aaaa-4eb8880b5f57 | -6.85438 | -59.41565 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2f3ddf85-b467-3358-8a11-ac943f124f4d | -9.17479 | -58.33523 | 2026-08-23 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33304a5f-7dca-3e11-8024-dc177eaf379c | -6.54732 | -58.52189 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5982d56b-2b57-36cd-a751-4077cfe0d110 | -8.47819 | -46.99585 | 2026-08-23 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6306e427-4d9f-3d03-acb7-b9b60d182b14 | -8.70971 | -62.90045 | 2026-08-23 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 92ea40d8-0665-3b19-8b3d-d7b6c85ccf55 | -6.01322 | -57.82638 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66cde732-6fb0-3dd6-96f2-c15ac0710574 | -6.80943 | -58.98118 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b48168a0-c5df-30a7-b6c1-4015a793e4c7 | -10.91767 | -57.16982 | 2026-08-23 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbba9c89-f9fa-3204-805c-6bfd22488dad | -6.22662 | -55.42448 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 790dff2e-d96a-3463-9f68-659f35e2bf41 | -6.79236 | -59.59016 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d220b56f-3b93-35bb-ba2f-5949e294e57f | -12.24273 | -43.18829 | 2026-08-23 05:04:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0e77d211-6d47-36d2-82d2-8ac97ed46a7a | -6.6978 | -58.73553 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b1a91517-d116-37de-a572-b651e6378060 | -9.11543 | -60.34263 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53c2ed67-08bb-3b70-a5d5-00cd681c6fde | -9.44871 | -56.90741 | 2026-08-23 05:04:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4b11cd48-7280-3fd0-8000-d1786a3f1b14 | -9.41622 | -60.41409 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bb7d6a9-43dc-3f80-b84d-2ece8dd8957b | -9.18936 | -59.44931 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 45d414a2-7e96-3c75-b393-7035dcddd1b8 | -11.16317 | -54.0101 | 2026-08-23 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64c8d0ac-e47f-35ed-89c1-542eda08b008 | -7.59787 | -60.94762 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5397550a-5d9c-324b-a217-f5fda7a61a9d | -9.13102 | -60.92187 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13cc6006-1a79-37dc-b75c-d6ca435760e2 | -9.14559 | -65.95564 | 2026-08-23 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b40f33c-78b8-3c4f-a713-41a95f2275d5 | -7.81443 | -61.78198 | 2026-08-23 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 137249f7-6460-3447-9e38-4167dd9e59e9 | -6.90284 | -55.70394 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2445be4-f93e-3582-8845-ca69a6dff7d8 | -11.44174 | -44.53459 | 2026-08-23 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| af43ce18-a70f-3fc1-a44f-5b49b894f22e | -6.11971 | -59.92561 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ea8fd47-d6f4-3fb4-a8ff-befee76f21ce | -6.80144 | -58.64865 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b08ae821-0649-366c-aad9-2fc822b60688 | -8.53587 | -55.32813 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40262759-f5ce-384d-b45e-9cbd98d9f93e | -6.55751 | -55.09999 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72cbaed3-a446-3aca-ab66-b897002efef8 | -8.63571 | -54.74178 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac73416a-b920-304d-be72-2361502d607a | -9.09208 | -59.47654 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d890a537-63b3-3ea3-9259-f0c16357d3d6 | -6.22605 | -55.42804 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b7669a0-1267-3202-8329-a7d0bb5c0823 | -6.1149 | -59.92874 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a22cd0a7-f621-39a0-89d0-ac6a547595d0 | -7.59936 | -60.93913 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2b49246-9f50-3ab9-86af-a48cd33953bb | -9.07971 | -65.41303 | 2026-08-23 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21aa5dba-8f0a-34e3-bc13-7c312f4aac92 | -6.76771 | -58.66931 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7816be14-5fa3-3a6b-a766-bf9b48e87988 | -11.60879 | -50.55586 | 2026-08-23 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 71230165-8b24-3936-89e4-e4e18b9c9071 | -8.93114 | -60.72437 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbc7cb0f-05ea-3429-bc67-1d46ca7ee4bf | -6.22697 | -55.48623 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6cdcbc73-1aa7-3ba4-a3fe-26ca9eef27f8 | -4.53379 | -55.51837 | 2026-08-23 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93c8d89e-e52e-35cc-a557-c6a31e3aee3c | -7.22507 | -51.68832 | 2026-08-23 05:04:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b10e7141-6e2e-3f8a-8552-4c423b101c6a | -8.09348 | -51.65968 | 2026-08-23 05:04:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e5d578d-c6a1-3aa4-8fdb-59fdb7070b57 | -6.37255 | -62.90665 | 2026-08-23 05:04:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6532aea9-1708-3dba-93c5-43604dc20bef | -6.85039 | -59.41496 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77deff5d-467b-3cfa-a23d-829609ccdccc | -9.17307 | -59.45152 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e3acf61-00e1-3eb9-b378-aab4bd6b66f8 | -9.11591 | -61.59557 | 2026-08-23 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b2e3df2-65b8-345b-8ce3-de36778f6bfd | -6.85037 | -57.68159 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67790d67-f8b1-30d0-8731-37c59716b369 | -6.79439 | -59.43046 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d1261cd-47d7-3523-b97c-8d2169d64263 | -6.37538 | -54.96357 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f02721fc-83a3-310e-ba79-78cf71481a7a | -6.19594 | -53.51763 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 259c7121-4918-3d3b-8a63-5eb758bd3e43 | -6.38312 | -54.95767 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3b3931e-d8a7-37e8-8f18-19aeec1ea7a0 | -6.3798 | -54.95714 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aeffb502-d120-3a4a-9e67-d52cbbcc78f2 | -8.90186 | -60.5418 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9c9316ef-d721-3d7f-a4bf-bc03c858059b | -8.69412 | -62.87482 | 2026-08-23 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 556559c0-7ee7-300c-a1b1-11cc4f98aff6 | -6.11997 | -57.83847 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 6b2d9b7d-b1b7-3636-9960-5cccb56c2cdc | -6.91942 | -59.43086 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e535c86-a4f5-3fc7-b036-d07161cd094b | -6.81632 | -59.67159 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6de30c73-3903-37e6-a02e-78923594ef62 | -7.84751 | -56.56982 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4a56655-4974-39b5-abce-adf40ff0651c | -9.85936 | -60.12318 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d85e85b8-5a02-30bd-8777-1528dee7bd0e | -8.52435 | -54.84505 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ef4ea18-1ed4-32db-a5a7-03d2f564f1a4 | -9.97212 | -53.94564 | 2026-08-23 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc8846a2-1610-33e3-8d2e-9ebc1ac652d3 | -6.18568 | -55.42862 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3ad991e-3f99-366f-a906-256ea3aabeab | -6.8515 | -59.43309 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09de5dcd-49bc-310d-ac68-b79b6995161f | -11.43356 | -44.53024 | 2026-08-23 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f78c7c2-c231-31bd-ae65-a303c0793efc | -6.25505 | -55.41819 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a0f4216-1b3d-3b95-a162-dd31604d3962 | -4.53545 | -55.52969 | 2026-08-23 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bab1917-5137-3a8e-93a5-19eae7ff450e | -6.75612 | -58.68459 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7fa70738-ba51-37c4-9a1e-f8cfc5232a54 | -6.80879 | -59.39372 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 666cb77b-ebf6-341c-9393-a10fc56a576c | -6.89043 | -59.4081 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf6c9282-4792-3d20-9169-5a7dcdbfb6d7 | -6.12874 | -57.83091 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d11a2c97-ae2e-353d-bf77-af6def45bf1a | -9.43678 | -51.59863 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbbf4837-6150-3a2d-b86f-c487021a97f4 | -6.81103 | -59.67825 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75c45c8e-bcff-3206-9ea2-d5e5964e8788 | -9.17527 | -59.46194 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11ec95e1-ea3a-331f-b7f6-ece9cc180460 | -7.48523 | -46.09632 | 2026-08-23 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f3c753ec-5ff3-3805-a788-e1c7dcd57d49 | -7.02176 | -59.5659 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 343491cb-5540-38dd-9cb3-10d22746d41b | -9.21567 | -59.78961 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd942576-4fbb-33e8-b90c-5354dcb2421c | -5.77931 | -50.19116 | 2026-08-23 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a661ccd-2d08-302e-afd7-667e024cd0c4 | -10.32991 | -45.40956 | 2026-08-23 05:04:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| efb62998-9388-3421-a29a-1cc6ba7042bd | -12.25078 | -43.18693 | 2026-08-23 05:04:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1079fefb-e8a4-3206-873b-55e0459304a6 | -9.12783 | -65.95224 | 2026-08-23 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e21d3b93-5eef-37cd-9294-8d15dce616f2 | -7.84289 | -56.57668 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 062ca8cd-ab0f-3853-9cba-d584d7fac62d | -9.2447 | -60.79498 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bf89b49-425a-3aac-8956-223293642bc4 | -6.77382 | -55.70126 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8886b11f-4e96-3a87-9e3c-9ed65402a2f7 | -6.55262 | -58.51337 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4132c32-663d-311c-909f-8a3f6b766b5d | -11.46847 | -54.32205 | 2026-08-23 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36e5e2a8-78a8-3482-aa22-81d218a2e19b | -6.821 | -59.66894 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 129fb7a5-a9c3-33e3-a636-bf41203876a7 | -6.9386 | -59.31645 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79b24255-a71f-3488-8297-00bacabf8a41 | -6.88704 | -59.40396 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef99dc2c-193d-3f11-ab01-3bb7b02d7016 | -6.53666 | -56.17484 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25fdee5f-9113-3f72-baf0-e021c9ce1c2a | -9.44539 | -51.59114 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6251eaa8-bf69-3954-a394-9835336a2f2c | -6.69396 | -58.73492 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fe56cd3b-597c-3a0b-a9ba-f9a697f66bce | -6.78697 | -59.42571 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05434c66-cc49-344c-b146-63e56f4b2b38 | -6.85736 | -59.40952 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2d0a6a35-ad34-3508-be30-d16a2b640d3c | -6.81692 | -59.66799 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d7306d9b-7e0a-3b97-9323-fa6756190115 | -7.43417 | -59.79497 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1b5b27d-2b46-3863-9ebd-7ebd818b95ce | -6.81365 | -58.64592 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 87c79d76-6bf0-3774-8b6e-1e336112152d | -6.1317 | -57.83591 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0f773ed7-efd0-3ede-b1ca-a9e1c5f5edf2 | -6.97586 | -59.06976 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 85554e66-9d32-3513-86a1-ac7bfc895cce | -7.00944 | -48.01806 | 2026-08-23 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 93e95f52-1ab9-300d-af31-6918553caec0 | -6.85188 | -58.97012 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README48.md)
