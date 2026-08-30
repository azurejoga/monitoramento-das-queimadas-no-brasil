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
| ecf1a442-0b4e-3f97-ac78-29cc1e34e245 | -7.40385 | -60.5836 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b74caa7-9ca5-368c-8a4a-14c6a71a4fd8 | -8.50593 | -55.28018 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f61fced-7477-3763-b058-2d6917a0f2cd | -7.57777 | -61.29905 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b35b1f9-44d0-3645-abf3-8eb062f9607a | -9.17285 | -59.60938 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a2e16a8-084b-350a-be41-1ca120e3089f | -9.71194 | -60.74285 | 2026-08-30 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fe8de96-d4d6-30c0-88a4-302499cf4cff | -9.60952 | -55.12554 | 2026-08-30 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3c6f51db-6d60-3591-aec6-05d61e20a2e2 | -6.81645 | -59.45519 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12a2da5d-c32f-33bc-ac8b-d1861ae031bc | -6.72561 | -58.70699 | 2026-08-30 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0d80084-6213-3693-addb-2ae74d3b7c7b | -8.59276 | -54.75514 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39c2e21d-806f-3d67-9c3d-1fa74f01833a | -7.32564 | -60.60801 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71ae92f8-1d18-3bd2-97a2-dc8e5b1ebc27 | -7.49207 | -55.31172 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1700237a-53a5-37e4-9fe2-81af992d1325 | -9.13812 | -61.01252 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0845a25a-2ffb-3e20-b3e2-aaf38aae86a4 | -8.94756 | -62.38087 | 2026-08-30 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 443a7073-c616-3407-ba44-1aa81ccc88a4 | -6.79018 | -55.6723 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf7726c6-3b69-3488-b3c4-c9fefc5ef142 | -7.49922 | -55.31543 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e87b1047-cea3-3952-91ea-6b4c4fc1e88c | -9.17231 | -59.61286 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8cf46a7a-5238-3053-b64e-083c12f91b5f | -8.49866 | -55.30355 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 206141a2-7e2b-37a8-b0b4-199f95d43f94 | -9.8568 | -60.30096 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b665d51-4b40-395d-9911-7e0eb416acc4 | -8.25554 | -62.75225 | 2026-08-30 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b22e9e5-7ca2-35d8-b033-4e0998082d32 | -7.51143 | -60.72246 | 2026-08-30 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9679b8f6-e55e-3e52-820d-ea06c7d4195b | -11.19834 | -53.99035 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e6e5038-b435-37b2-960d-3906c7783a03 | -8.93548 | -67.36145 | 2026-08-30 05:18:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| ee31cdaf-633e-3065-bd08-ecc1c60fb2cc | -6.86115 | -59.47275 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c415cac7-95a0-342f-8d1d-6638ff8ca34d | -5.88467 | -57.76928 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 192992ec-6a57-30ef-a697-908e3e29328f | -6.25529 | -55.42492 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65c529d6-37aa-3135-8fe3-e081ae50b2d0 | -7.30605 | -60.60123 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20093cac-c461-310a-9a0a-c5e403074af7 | -7.01598 | -59.65751 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0252f399-218b-3239-b8d1-fa5964b13236 | -9.15546 | -59.50331 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49b9d872-678a-3b3c-b9c0-135ff91f0460 | -6.32469 | -54.7495 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 017e49cc-e7a2-3c54-8a94-6c2e7bd0c759 | -8.24577 | -54.9677 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 034b43f9-a375-3a53-bbb2-49295296f0b3 | -7.00714 | -59.64898 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3da21a0e-4ae6-38c4-bc7c-23574278b587 | -9.20473 | -59.57876 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3be08d63-ff11-35fa-a9d7-9bc5ebb4976e | -7.56106 | -61.3155 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d8dbe931-95a5-3ade-b65f-614bca08c467 | -7.10324 | -45.76748 | 2026-08-30 05:18:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ff85dbe-ccc5-33ec-85fe-0a7ec4559f4d | -8.67454 | -54.76858 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5ae57ab-a52c-3221-a189-e5d9eca84a1c | -6.64632 | -53.18482 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea819f08-8e66-32ef-86a5-8e761e916341 | -5.96988 | -57.67673 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5999a62c-413a-3bed-b00e-177a3b81327d | -9.16815 | -59.50883 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b30a5fe-b202-37d6-859f-e19e98ecad99 | -8.74 | -69.56624 | 2026-08-30 05:18:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c4ba751-e5d6-3473-ae1e-9b246167303b | -11.16102 | -51.31361 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d6a05699-bfd1-3478-b437-bcea15586e5a | -5.97043 | -57.67312 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1f53767-601e-3428-9fb5-a5598a524b0b | -8.79614 | -62.48437 | 2026-08-30 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef720b32-fee9-3ffb-abe6-5ceb30d7583d | -11.29179 | -54.03141 | 2026-08-30 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a080764c-49cc-3a04-80d1-e3b4f8ce1b28 | -10.48266 | -59.60325 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 83238206-bbea-3f13-8f8f-ff4715d24d83 | -10.35427 | -49.97884 | 2026-08-30 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 10154b31-117c-380f-9c3a-f12dea2ea02c | -8.70855 | -62.91758 | 2026-08-30 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b335bfaf-7c22-33ce-8c5f-46905250afe5 | -11.15432 | -50.58461 | 2026-08-30 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ceef77b9-e860-33ae-ad9c-594b00d1dc2f | -6.86531 | -59.46997 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 2d0dc0c1-88ab-3577-b66a-43d71ed7ea23 | -9.85735 | -60.29746 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1c75ec5-7c48-3909-bbc7-cae011db890a | -7.45982 | -70.13614 | 2026-08-30 05:18:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0392106-0adf-38ad-b1d5-a47992b20bb4 | -8.94822 | -62.37687 | 2026-08-30 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d7a3706d-d825-3f61-b104-97cf307fbf6b | -10.75713 | -50.87656 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 326674c6-1d88-324f-a75a-859c259f7b81 | -6.11576 | -53.56215 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9af0ce61-fdd5-3d11-9e37-2a35ece91074 | -9.17838 | -59.61738 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf411e98-b17f-30bd-a56a-678d737e1ff6 | -10.55566 | -59.6147 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2976be4d-8a1b-34a6-9dc2-bbf01ee1042f | -5.88132 | -57.76875 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 290ef87a-06bd-32a5-9545-38bda2a585ff | -5.87353 | -57.77482 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b55b84df-049b-37ee-b5a5-359aff3bd20a | -6.92833 | -55.70037 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8dfc5f0f-77bc-319c-8ff2-a149daace8d0 | -7.84329 | -62.31912 | 2026-08-30 05:18:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0701dc2d-b7cf-32b5-a866-bb5b26551432 | -6.09243 | -57.72097 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e11728c2-8af1-311e-b2a7-d41d3de971fb | -9.95138 | -53.99831 | 2026-08-30 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 903f84c3-c33e-3ea0-8cdc-ce6325484f45 | -8.2323 | -61.42204 | 2026-08-30 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b77be75-32ef-343f-a529-1a0b0f3a0984 | -6.93248 | -55.72316 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e074aae-0384-320e-9e24-33d226080215 | -9.18976 | -59.36953 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b814c61a-a7fc-3eb4-ba5c-a2ad80f03d79 | -6.25758 | -53.69611 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38cc63ad-6338-3ba8-8dcc-7d03702432c2 | -10.84421 | -50.49596 | 2026-08-30 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b1822dc-f6b6-3515-8324-61fe2ff3b1a8 | -7.29655 | -60.59605 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2f427eff-b8bf-313c-92b0-fad7b27c2eb2 | -9.00905 | -60.60768 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bdf76fe-9412-3790-8e09-c73fcda07860 | -9.72109 | -54.826 | 2026-08-30 05:18:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e12fab0-8737-3405-94be-5a70cd56bbbb | -10.75677 | -54.03548 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30ba5aa9-7d63-3cc6-b1e2-305abd230ede | -6.67888 | -58.74592 | 2026-08-30 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f820cab-303e-378d-9126-7ef1b7407332 | -10.48543 | -59.60727 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 93212bc2-ec4f-35af-bafd-9430c5e5996a | -6.91275 | -59.49156 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e83da26c-5d70-3103-8f3a-779fd3dac433 | -9.88935 | -60.28821 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1af01c0e-d46f-31f3-8fa0-69488d5e73ec | -7.31835 | -60.61053 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b37c1ee6-94fd-33f9-ba92-ecafcc4a6967 | -7.52809 | -55.59122 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66620e9c-d3a0-3972-9a64-18516cc23748 | -6.18266 | -57.7747 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2be91994-650a-3695-9c42-6f3dbaa64441 | -8.23534 | -54.95718 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8c991c4-0576-36e7-ab29-f505d37e3df0 | -6.78179 | -55.68173 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 04e281d3-91a8-394f-a97a-2fbc993408c8 | -7.23764 | -60.61977 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8230f381-71b7-302c-a0d8-50bacf485dfe | -6.005 | -57.82802 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e32bc9ff-ec5c-3f76-af88-d07198428e2e | -7.09621 | -45.7667 | 2026-08-30 05:18:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42b1625f-0c6d-3b71-a776-b56833a4918b | -10.35771 | -49.97909 | 2026-08-30 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cba041aa-d642-369b-926d-0d5f2f50156c | -7.56288 | -61.30431 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aeb04919-1b1c-3cc0-97c3-73512609b5af | -9.16806 | -60.29061 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fc83f17-b7db-3cc9-9005-63efa983557d | -6.27339 | -53.13922 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5bbb3a1b-35fa-3c36-884d-606abfca3daa | -10.48435 | -59.61427 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e1d5367-80fe-35ef-92b3-33e920a64798 | -6.12045 | -53.55908 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15549790-b553-3b53-b29e-14a0876d6d75 | -8.67193 | -66.5116 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20a685e7-6590-3365-b69d-67c244c39e85 | -11.29501 | -54.04029 | 2026-08-30 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 828fa128-de05-3663-9930-ee3e88d94876 | -10.75266 | -50.86909 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 990e441b-4976-37b4-bd2c-a968ed252497 | -8.60556 | -70.21385 | 2026-08-30 05:18:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edb88dcd-f86e-3cbb-9d13-cfa27b454299 | -7.52615 | -55.31663 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 61cf862b-1d28-399c-af57-ce0073db55a0 | -6.1085 | -57.86187 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c48a68db-a0ae-39fa-a75a-ce00414ab9c0 | -9.18283 | -59.63234 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f88f2aec-c412-3521-ab84-14143b8c4c16 | -7.24043 | -60.62389 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 483ec692-ccb1-3bd9-bef6-3b3bf315dbfe | -6.08746 | -57.90944 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d0cd149-8a72-3dff-8f8c-ed2f2873efed | -11.16622 | -51.31435 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8673ba4a-946e-3f25-a22d-0b90154a1493 | -8.60131 | -70.20569 | 2026-08-30 05:18:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f62a60c5-1b12-33b1-aade-23cdee2a4e87 | -10.84545 | -50.49431 | 2026-08-30 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README57.md)
