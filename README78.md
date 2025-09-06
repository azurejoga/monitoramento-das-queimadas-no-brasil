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
| 5ff227a4-8128-3ad0-97c5-884d24191a97 | -2.78507 | -49.62426 | 2025-09-06 05:27:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 26a4d4d0-563d-3fec-9184-29ab9b030ada | -2.85728 | -49.5016 | 2025-09-06 05:27:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 88793e93-6004-33c8-815d-676db050fdb5 | -3.69351 | -49.54902 | 2025-09-06 05:27:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca7ae480-25e5-3820-9a82-12bde5b6f432 | -3.32628 | -54.90907 | 2025-09-06 05:27:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f207bba6-d9cd-30e4-a4e2-9bf07e483595 | -4.2708 | -48.18454 | 2025-09-06 05:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| c98bb1b5-ac72-3826-b129-db762eb48ce5 | -3.32823 | -54.9125 | 2025-09-06 05:27:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6f347ca-1493-3680-9c89-fb6985d753a5 | -3.165 | -49.48173 | 2025-09-06 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e625db2b-dc01-32da-84db-8a41ac8496bc | -3.16582 | -49.47619 | 2025-09-06 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28e31039-5cb2-3d0e-b27e-57115327b9b8 | -4.27275 | -48.18793 | 2025-09-06 05:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| df78d535-d239-33bb-8545-ad5359a80ea2 | -3.16281 | -48.60791 | 2025-09-06 05:27:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cbb99f79-4b15-3520-b214-19bb5ccbac9b | -2.85651 | -49.50692 | 2025-09-06 05:27:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 771f05c5-2720-31f5-bdca-12a2aa39188e | -1.34905 | -55.47576 | 2025-09-06 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efaaf5ad-9ae8-3f86-80e2-cedfe247fa1f | -2.78583 | -49.61913 | 2025-09-06 05:27:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4761bc96-75fa-3618-a935-ab306c5eb243 | -3.33078 | -54.90979 | 2025-09-06 05:27:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 439add8b-59cc-39db-81b0-5d44208e9420 | -4.86118 | -50.8276 | 2025-09-06 05:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 974bc3ba-7d67-3464-a2d6-a33173af3d36 | -3.6982 | -49.56798 | 2025-09-06 05:27:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8a95582-4aba-339a-9d82-a78c9043b317 | -9.21299 | -57.09256 | 2025-09-06 05:29:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88bcbafc-b61e-37f5-87c3-7222a8d36cde | -6.27279 | -53.44583 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e69c1517-e6c0-3da8-b9ed-5a2ce1815b9f | -6.74574 | -62.99828 | 2025-09-06 05:29:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea899e09-d1fc-3894-8f83-76837292f0a0 | -5.97762 | -53.59405 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be4ab581-78c0-38a3-a3d3-4bdeb750767e | -5.01234 | -56.03828 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5562df15-3768-3515-a813-0ef65ad6b465 | -4.99835 | -56.25508 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c2d4f32-96c4-303f-9e76-bbe8ea71d359 | -5.76898 | -56.51397 | 2025-09-06 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6036fe6a-47a9-31a2-8c49-5ac0bdc3054c | -7.7645 | -50.73927 | 2025-09-06 05:29:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ba2bce5d-7097-3f30-8f42-cb2984597f3a | -5.14539 | -60.31696 | 2025-09-06 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cf1b910-d4b3-311e-84a8-58cfce13af18 | -5.14878 | -60.31747 | 2025-09-06 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a28015bc-f6d8-3ad3-ae30-fc1867d6d279 | -7.7209 | -61.52169 | 2025-09-06 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d503087e-c1cd-3825-9da0-18ef1248415b | -9.24968 | -57.07771 | 2025-09-06 05:29:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2817782d-bb11-3910-a2b1-d68b91449486 | -5.97633 | -53.6031 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ace37a8a-59a1-3660-89d9-7da115b3b3cc | -5.01292 | -56.03418 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c1c60b2-7cc6-314b-9640-acc5febfd035 | -6.28411 | -53.44091 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb0afe92-66e1-3ecd-bf2b-20c2a99d51ba | -8.77358 | -49.63874 | 2025-09-06 05:29:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e5bf34cf-7ead-30d9-bab2-f86b70ea4b9e | -4.99073 | -56.21844 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e7df997-4975-34d3-9539-8da7bdceb22c | -8.658 | -54.84495 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc3dcac2-3a0a-3e39-bb10-dd0d282b57c5 | -10.46745 | -53.61879 | 2025-09-06 05:29:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9541d80-9fbc-3c22-9df2-78cfe21698c7 | -9.40088 | -54.7555 | 2025-09-06 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea8fa5fd-5b54-31f5-913d-4cc9a278ecc2 | -5.95363 | -53.798 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aca7a262-e83e-35c5-be84-62e3b270dc8e | -8.54575 | -55.24186 | 2025-09-06 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f8559fb-5a15-397b-aaac-12ec206fa218 | -9.68083 | -51.10645 | 2025-09-06 05:29:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c6da6f4-1436-379a-bb67-1d123795cfc7 | -6.44627 | -58.15013 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2492654a-7515-3462-bb19-f2195e017651 | -5.9532 | -53.80097 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6510942-6bb6-36d3-9c60-b0f806779fdc | -7.68353 | -50.29767 | 2025-09-06 05:29:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 0eb03f85-3c51-3161-8146-ca992bb0f317 | -6.16364 | -53.68598 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60192d75-bec5-3ad0-bd81-1f13ff96c58d | -9.25392 | -57.07837 | 2025-09-06 05:29:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc6de4ca-6296-3177-a24c-174ca792f532 | -6.87371 | -58.9329 | 2025-09-06 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2138ab98-a938-3d02-8101-1a7d41e0d2bb | -8.41807 | -62.29135 | 2025-09-06 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93e6ae6b-57c3-3024-b149-3c1f19dff078 | -5.06442 | -56.07043 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0b64381-e266-3596-9a72-6bae84b5b4a8 | -10.4765 | -53.64418 | 2025-09-06 05:29:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a63f180c-3b47-33fd-8684-a55415076379 | -6.32628 | -58.17724 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffbc1b24-c5e9-3a41-b832-b26e68f5fad1 | -5.96647 | -53.59874 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc815860-a0a5-364a-aaa0-247cc1683b8d | -9.68148 | -51.1011 | 2025-09-06 05:29:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 869c41a5-04c0-3ce7-98ac-ef852f504db5 | -5.78645 | -57.55775 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7737e5e0-6a07-3fef-8307-7e19f07ac6a6 | -9.70503 | -49.492 | 2025-09-06 05:29:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| f579ff76-72e4-3343-89b9-4c8fe47e9cc5 | -5.79429 | -57.55885 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d97ff8cd-ce92-3f3d-bb19-68d67fe09173 | -9.2093 | -57.08802 | 2025-09-06 05:29:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93bb4de6-35f7-38d1-a75b-85dea6d861be | -5.06927 | -56.06712 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| added85c-ed7b-3c48-ab04-62f7502ccd2c | -9.22203 | -57.0897 | 2025-09-06 05:29:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b88ff221-9c7e-332d-a5f9-4ddfb27fcdd1 | -6.49797 | -58.27234 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be3e88e7-f183-367b-a310-5816a61e6814 | -5.48636 | -60.12753 | 2025-09-06 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb3a4e07-6509-3660-9405-6fa78c077887 | -4.89494 | -55.99072 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50cd5615-2dc7-3f54-8d64-6eeaeb8c99b1 | -7.79173 | -52.13412 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20a0984b-9298-3d41-b288-7d22cc0d3186 | -9.33233 | -55.20435 | 2025-09-06 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c81ec3c9-41e2-3a23-9c18-e2f53b0f7b1d | -6.54642 | -49.51042 | 2025-09-06 05:29:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 306398a3-015d-3599-829a-f016d3134de8 | -6.34777 | -53.44909 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 207fd8b3-d2df-34e0-8c04-e861578eee90 | -8.47537 | -62.64516 | 2025-09-06 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2248c665-302b-38e5-aab0-6e9a8bd292a8 | -8.36877 | -52.56116 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 42e810c4-94c8-3d64-80d8-8516443b205a | -8.35306 | -52.54839 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c01d853-fe3d-367e-873b-616bd072f18f | -6.53844 | -49.4976 | 2025-09-06 05:29:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9d82cac-4416-3092-8c2f-6f209bc925bf | -9.68214 | -51.09569 | 2025-09-06 05:29:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ff3f6d05-538b-36c5-8939-214061e765e7 | -6.32315 | -58.17205 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4a59f2e-440d-3e7e-90e3-6c0cb5070502 | -4.89433 | -55.99478 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56227f38-5ff9-31d2-abaa-8efd4650515b | -6.18633 | -53.25724 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 608fceab-4f9e-349e-a099-fdb0958df078 | -5.8623 | -57.55893 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e25d2c5c-c254-39ed-8d29-27f13bda0100 | -9.39666 | -54.74894 | 2025-09-06 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c271ba4a-a833-3ea9-b019-7c728e5bc57e | -6.81539 | -52.81532 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3d5b278f-9549-39fa-b6fc-c57fe32f92d4 | -6.56282 | -49.85423 | 2025-09-06 05:29:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15f29cb0-2baf-303f-bd04-a551eff05d17 | -5.78254 | -57.55716 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79ae899f-7697-3366-84dc-628a88a6efc3 | -9.71202 | -49.49301 | 2025-09-06 05:29:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| d8048759-7476-3a29-9fe6-50058596d136 | -5.50402 | -60.12643 | 2025-09-06 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1312f7a-25a3-3156-88d8-60cc43e3cc40 | -5.48866 | -60.13547 | 2025-09-06 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c2f6a61-c8de-3483-9494-8b35ad46aa36 | -6.6939 | -63.13299 | 2025-09-06 05:29:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae978a5c-73ad-30a6-a0bb-cdcca6493952 | -5.50917 | -60.13862 | 2025-09-06 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47187c46-611a-3d85-913b-484d4b641366 | -9.55585 | -53.58917 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 205a337e-9dc4-3fbb-ad96-9ca3b8c82504 | -8.37054 | -52.56617 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae18a43c-73c6-3a93-978d-d616598976d2 | -6.83885 | -52.80745 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53b05a1a-c92a-3f03-83d4-faa6cc99ed99 | -8.35211 | -52.55558 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 341110c1-d450-3d74-ba16-453c6d32c49e | -9.7037 | -49.48994 | 2025-09-06 05:29:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 3a62e734-dbcc-3b6d-a87e-4365d4467132 | -6.69058 | -63.13246 | 2025-09-06 05:29:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e07e038-dcf2-34ec-8b79-a4a56a13bca1 | -9.24544 | -57.07703 | 2025-09-06 05:29:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e0a9547-873c-352c-a9bd-b18e627311f2 | -6.31936 | -58.17148 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5fdf8e7-690f-39b7-8736-d5b61d198b27 | -5.97161 | -53.59944 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5afd7fc5-1941-35ea-ab3f-71c39e4e619f | -6.73527 | -51.96665 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3bb67c5b-8c55-3a2e-90bf-c319636575f8 | -7.90597 | -61.51064 | 2025-09-06 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17379006-c89e-31e4-b100-c9ceef8f198d | -9.68654 | -51.11262 | 2025-09-06 05:29:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 394563a2-e245-3d27-86c9-f34edc3b8ff0 | -5.90517 | -57.72933 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c4fcb61-713e-390e-8343-6e38e93778ab | -7.73435 | -50.31284 | 2025-09-06 05:29:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ed6c8155-6b3d-34fc-be7b-c63968d0149f | -6.27801 | -53.44655 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 198b6398-0816-3b11-92b6-b0418823dd01 | -3.96773 | -43.2365 | 2025-09-06 05:29:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| aedf886f-4eca-3f7a-9d33-bfa3a898e00d | -8.7861 | -63.82489 | 2025-09-06 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d1eb22f-e90f-3b27-ae0a-a6bbdbaea7c8 | -6.80991 | -52.81457 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README79.md)
