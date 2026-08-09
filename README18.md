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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45f952fa-eab3-34cb-969c-d5962ae4249e | -6.82991 | -56.42425 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b791028-0315-39e5-9ea7-9bd70ff2ba16 | -6.41839 | -55.78805 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3b652f48-cdea-3e3e-8370-dcbdbfac1e50 | -6.83209 | -56.41006 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c574d093-894f-3ca8-b6ed-dc16fa704b31 | -6.82882 | -56.43133 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 990b31b3-b3b4-3648-9e98-4b0bf269c629 | -6.65209 | -56.43285 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4ee2b7c-6b12-397c-9658-f97e64d28797 | -6.83154 | -56.41361 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2a7d929e-685c-3b7f-8d68-d9c421d0d156 | -6.82377 | -56.41966 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22b6afaa-0dec-36e7-aa52-458be9d32a4c | -7.38508 | -59.97047 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f2cec80-e0a6-338e-94cf-8cdfc8267d51 | -6.83494 | -58.93411 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e52135f-0990-3f34-ab7c-fa28c48fdc7e | -6.82656 | -56.42373 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6294ccf1-6377-39cf-af7e-007faf5e3e0d | -6.82385 | -56.44144 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 693910c1-1056-31c8-a26a-cd6e76a3b553 | -6.88736 | -59.8927 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9846d218-68ef-3923-8544-c0af384803a6 | -6.85324 | -56.40609 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aa5f81ba-3958-3d4f-8a55-a166b1527ac7 | -6.88264 | -58.93795 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 52e97174-421b-3c35-8d96-40c88fd0b4a1 | -6.60788 | -56.36455 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fd59bca-9884-396e-b9de-91a43c762e1b | -6.81934 | -56.42624 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aebac819-a5b7-31b0-8264-def0db01d4a9 | -7.55326 | -61.15955 | 2026-08-09 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5af3428-4ff8-3927-b72c-6b7088162620 | -6.83488 | -56.41414 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c1453ad6-6ed2-3a5e-b320-760eecb33252 | -6.70839 | -58.95852 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff3dea98-961b-37a0-b93a-4e4fb899b389 | -6.831 | -56.41716 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7c81b558-8454-34de-a873-ef9eec7e0c52 | -6.58188 | -56.53387 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c45fa8bc-1f83-373a-925f-781b10720c15 | -7.55325 | -61.16101 | 2026-08-09 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32cf1ca7-3602-37ba-8e36-c24ea94e5509 | -6.83552 | -58.93052 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 505437ca-a492-3ee9-8dae-01e55fda6cfd | -7.38569 | -59.96666 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a218352-4cb0-35b3-a2df-ea4b1f8c4c06 | -6.83713 | -56.42176 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 270ca9b0-e63b-38d2-9531-47f947c0bd99 | -6.85433 | -56.39897 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a4928e5b-6f65-384f-82f5-9c207933469c | -6.84375 | -56.40099 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d35ff484-736d-3613-ba58-86093a2d0c7c | -6.85154 | -56.39491 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0a329052-d82f-37df-b963-d72fe8bcb82f | -6.84819 | -56.3944 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35025f1a-a716-3f68-9b20-c211ee971335 | -6.83877 | -56.4111 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 361d3865-56f6-3e4b-89fa-6f25c0edf732 | -6.82268 | -56.42675 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ca977c5-f70a-3a56-8a1d-31dd5232cd9c | -8.15584 | -55.39913 | 2026-08-09 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6936407b-95af-3761-bee8-a7c2cf3b0119 | -6.41783 | -55.79171 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 38ecca39-b66f-3ce9-8ad4-10de9b2606f7 | -6.82431 | -56.41613 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35e72e9d-c25d-38ce-a531-fe06bde2f386 | -6.83605 | -56.42883 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 090747b3-3d9d-3b98-a982-db4b3928ce35 | -6.84661 | -58.96912 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd16539a-9e14-3347-8748-373bcfaa3f66 | -7.38855 | -59.97103 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 628bf0e6-5a7d-3619-91c0-5ea2138c4721 | -8.15178 | -55.4025 | 2026-08-09 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28c0b25b-1dc7-341a-9130-79a1b27c4e7a | -6.83597 | -56.40703 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 404c2814-9a1a-355d-9f1f-e07e423ac850 | -6.71012 | -58.94772 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 04f0be5e-0bc4-35c4-ab1f-ed6090aa681f | -6.64814 | -56.4142 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 140d7fac-356f-3bb9-9a82-f7a6ef587501 | -6.88937 | -58.93903 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6506372-6388-37e8-b7a6-aa4703d34a7d | -6.83496 | -56.43592 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2101d44e-e7fe-30ad-b5ac-b1ddd644d45a | -6.82548 | -56.43081 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 86da0c4c-7fd6-3ade-bfc7-fe645af46188 | -6.8393 | -58.97167 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c5b932d-78ab-303a-b29b-9254c26cf9e0 | -6.82051 | -56.44092 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c635aa02-8ad7-33cf-bcd2-db687029d130 | -6.84102 | -56.41873 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1f5801d6-e976-3418-8b18-ed3a121cece5 | -7.55398 | -61.1552 | 2026-08-09 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f37c0bcb-aaf2-300e-8549-346a6c20f0a5 | -6.82602 | -56.42727 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd9afbb3-72c2-350d-97bd-330304fbdcec | -6.83215 | -58.92999 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f5091ea-ac12-3416-b78b-2185f1856052 | -6.83543 | -56.41058 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 62d30ec2-4722-3c3c-a20a-5435981518a7 | -6.84764 | -56.39796 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e23b9143-8091-36ae-b596-ff1ae101aa3f | -7.69481 | -55.16214 | 2026-08-09 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ee5812e-edcd-3fd4-a03f-545701e377cb | -6.81825 | -56.43333 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 041a852f-c96e-376f-bdfb-e3e412c5c340 | -6.87312 | -58.93275 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c327d68-d91c-37a2-bec7-141b5f2f2ef1 | -6.70954 | -58.95132 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a8ea3c8-76c6-3efb-b6f9-700cb6fbce29 | -6.13889 | -57.72137 | 2026-08-09 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 898fea78-e985-392c-a2b6-bf381becf6b1 | -6.61177 | -56.36147 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2f8a305-de03-3b32-bb32-01e2f654f975 | -6.7107 | -58.94412 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1d7a5438-ae2d-3a82-b859-e3ed47e8984f | -6.84273 | -56.42987 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59836bbe-3105-3004-9141-b1be7560dcb1 | -6.82711 | -56.42019 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d499eb28-c197-3e6f-bfb5-5c934ac15970 | -6.84157 | -56.41517 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ab677648-7fe1-38f8-b190-dba9ec4d85a4 | -6.82214 | -56.43029 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| acba0b20-0aff-3cef-b56a-a469dedb2029 | -8.14886 | -55.39807 | 2026-08-09 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 319a55fa-1916-3f51-9582-7d538d668bcb | -6.72253 | -58.93493 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2e26844a-acd8-3ce6-aa54-950f3b64f903 | -7.55395 | -61.15665 | 2026-08-09 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b3b9234-1f46-309e-a0b9-8a6bbb248613 | -6.415 | -55.78753 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d82e8088-2799-3d42-919d-82058b3215a2 | -6.88207 | -58.94156 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e01ed92a-97d1-36ed-a771-96b3a5cc4f65 | -6.82828 | -56.43488 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 203da54b-b8fc-34d2-bc1d-22ef46f2e57a | -6.84041 | -56.40046 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f2e17ba-d529-334c-9921-d7f5fae34689 | -6.8282 | -56.41309 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c1f43520-4bf4-3fd9-8fd6-cd5d99b340ae | -6.87369 | -58.92916 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da639bb2-5f21-3a15-8ced-9e1a9d20be28 | -6.7084 | -58.947 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2ad7d55a-a6c7-32c7-811d-ce529c77605b | -6.89083 | -59.89324 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e32cda1-f113-3615-9189-6346443cd648 | -6.85099 | -56.39847 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be8c575e-bf0b-3523-9ae0-d6d2b85cc1a4 | -6.14626 | -57.71968 | 2026-08-09 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 22a3dfb2-e3b7-3542-a78a-9aab151b7931 | -8.15235 | -55.3986 | 2026-08-09 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 755f6257-a676-3a0e-a6c2-73f88640e37e | -9.63179 | -45.51843 | 2026-08-09 05:12:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1a77e5dd-64f7-396a-b46e-f85dcd85503d | -14.02405 | -53.82789 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e2f20c9b-7491-396c-9274-fba48f633eac | -14.17252 | -53.99207 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1348532-253d-37dd-a2f0-689433ff9ea0 | -13.81377 | -53.6924 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fdf2016-b9a0-3813-b041-dc11d7f6f6f0 | -14.73902 | -56.33672 | 2026-08-09 05:14:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 682e652d-c3d5-33e4-9303-86435eab0715 | -13.83961 | -53.75 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 146a782b-acb3-33b1-a21f-e62f576c43f3 | -14.31797 | -54.94035 | 2026-08-09 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f6acd2a-791a-38f6-b45f-3f26b9c50e70 | -14.03434 | -53.84445 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 45f5a597-b437-332e-8838-30ef415a9953 | -13.87077 | -53.67399 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0823bfb0-1596-3cf5-bbe7-a2726af171d4 | -13.87591 | -53.66704 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 86495b4d-86d5-3ec3-9ab7-a303416c8772 | -14.31731 | -54.94519 | 2026-08-09 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba9e1194-2beb-338e-8405-afe3a1ba1dde | -14.03385 | -53.84815 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 212d9039-0ef4-32e8-89f1-d4c6cb4dcda4 | -14.31664 | -54.95005 | 2026-08-09 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ded1fa1-2e81-3381-8370-a84203287423 | -15.75987 | -47.76657 | 2026-08-09 05:14:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 543da428-dd03-3eb8-a070-90fd049a3da2 | -14.02356 | -53.83159 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 63ad53a5-bfcc-37de-8400-909f5c066bdc | -15.38865 | -53.76877 | 2026-08-09 05:14:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a8ded323-cb20-367a-bb2d-6832c3c88031 | -14.03074 | -53.84022 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f55bfabc-ad1e-3157-aa71-2c1adac0f997 | -14.0763 | -53.99762 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2a4aedd-ab9c-339b-aad9-486797bf7a32 | -14.02617 | -53.84327 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f1652df4-ccc8-38d4-b95a-aa0c74aafd0a | -12.01129 | -64.83259 | 2026-08-09 05:14:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79fe0028-1af7-339c-bfdb-39f9d40be4a3 | -14.02209 | -53.84263 | 2026-08-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d41d280b-2196-360b-baf1-e97fa1f6fca2 | -13.93988 | -58.11774 | 2026-08-09 05:14:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| c574d128-4048-3382-8f96-5627d4954315 | -13.93211 | -58.12393 | 2026-08-09 05:14:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |


[Clique aqui para ver as próximas entradas](README19.md)
