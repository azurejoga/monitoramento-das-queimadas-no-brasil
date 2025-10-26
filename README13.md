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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c4c845c-965b-32df-8253-6107b91768b4 | -21.92384 | -46.51519 | 2025-10-26 03:45:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9f05b17c-f554-3c56-b87f-5874ae5b6345 | -19.6835 | -41.99129 | 2025-10-26 03:45:00 | NPP-375D | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8daf2fb4-6fd7-3f39-b6aa-a5bcbef57013 | -19.10693 | -41.96857 | 2025-10-26 03:45:00 | NPP-375D | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5a691fb6-4c23-3081-a6b8-397562941455 | -22.5993 | -43.64758 | 2025-10-26 03:45:00 | NPP-375D | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3b147ad3-b653-38ef-862f-e3d2e9b0cd0f | -21.43556 | -49.59436 | 2025-10-26 03:45:00 | NPP-375D | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 38eac050-e902-3240-a519-e9813d32d353 | -21.76498 | -50.0482 | 2025-10-26 03:45:00 | NPP-375D | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| c6b586c9-9b29-32f2-a0d1-cc3e476f2d3c | -20.9815 | -44.32021 | 2025-10-26 03:45:00 | NPP-375D | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e048ff0e-ae6f-36a4-82a2-f4478c93d12a | -21.92656 | -46.5128 | 2025-10-26 03:45:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a59c8154-66ab-35a4-ac55-6bbaf1d80d66 | -19.68347 | -41.9911 | 2025-10-26 03:45:00 | NPP-375D | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 98143ae6-bad3-3879-b520-de83ae54ffbb | -19.40352 | -45.87679 | 2025-10-26 03:45:00 | NPP-375D | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b06c591a-d301-3b0a-9eec-cb78037342a6 | -21.92587 | -46.51594 | 2025-10-26 03:45:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a4e86530-0f96-3978-9e27-15334f86662a | -20.24826 | -44.10763 | 2025-10-26 03:45:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| e7ffd4e0-d94f-381a-b783-1eb408f43f89 | -21.42833 | -49.5974 | 2025-10-26 03:45:00 | NPP-375D | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 08b2c506-d70a-3f77-884e-3349ec358289 | -22.77501 | -43.39148 | 2025-10-26 03:45:00 | NPP-375D | SÃO JOÃO DE MERITI | RIO DE JANEIRO | Brasil | 3305109 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 72ddaa85-f7ab-39f2-bb2b-7a8c4cf76ebf | -20.83668 | -45.60796 | 2025-10-26 03:45:00 | NPP-375D | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eec46217-586c-3f8b-9b7b-cfb1e30816a3 | -19.65614 | -44.63063 | 2025-10-26 03:45:00 | NPP-375D | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 40706b16-d19b-39cc-888b-d98292fcc9f7 | -22.91848 | -43.68327 | 2025-10-26 03:45:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3404ac78-7970-3508-a200-37bf39f40659 | -19.28645 | -45.81675 | 2025-10-26 03:45:00 | NPP-375D | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d2595f1-9a2a-34bd-a2f4-22f2e893ff52 | -19.34781 | -45.60101 | 2025-10-26 03:45:00 | NPP-375D | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0eeb749e-1f09-3962-9efe-5ec206390fa3 | -21.43392 | -49.59309 | 2025-10-26 03:45:00 | NPP-375D | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| b8e9e8db-a13f-328b-b9d1-309b8416dac5 | -22.59855 | -43.65144 | 2025-10-26 03:45:00 | NPP-375D | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4addd64a-f029-32a3-a0b7-16d9ec51d0d2 | -21.43439 | -49.59935 | 2025-10-26 03:45:00 | NPP-375D | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 4a12f9ff-083f-35f4-8db1-0ac7f1b06229 | -21.76007 | -50.04107 | 2025-10-26 03:45:00 | NPP-375D | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| b2e5d3ff-3702-3059-9033-8b90bfda8702 | -20.45112 | -44.18201 | 2025-10-26 03:45:00 | NPP-375D | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 811ade0e-18cc-3c2c-9b85-1d92d022a1cc | -19.85983 | -42.1882 | 2025-10-26 03:45:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ed730c16-9b41-3965-aed7-7fa5271b08a3 | -20.57851 | -43.32232 | 2025-10-26 03:45:00 | NPP-375D | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 2e872604-3e2f-35a4-b962-3c40b5e04f89 | -4.8933 | -43.2349 | 2025-10-26 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 46.3 |
| c81c7dea-24cf-3bb4-8851-447efdd1866b | -17.3165 | -43.643 | 2025-10-26 03:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 57.4 |
| e7fdbcad-5c23-3bfb-b52f-401da56de834 | -10.4065 | -45.3244 | 2025-10-26 03:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| a7488c7c-1873-369a-b3a5-6949014debdc | -5.118 | -43.2198 | 2025-10-26 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 2277857b-cdf5-3672-90cf-440cfec9e6d1 | -5.1181 | -43.1964 | 2025-10-26 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 169.3 |
| b3fe633a-7e41-38c3-b95c-fe75e8dc42c4 | -5.0994 | -43.1977 | 2025-10-26 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 140.0 |
| bd76b9a5-0601-3485-83be-6394b56a70c6 | -13.5405 | -43.0077 | 2025-10-26 03:50:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 92.3 |
| f814fcf1-44e9-3c7e-8c2c-43b1b97df76c | -5.0992 | -43.2211 | 2025-10-26 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 51c7f71c-319f-3330-9e0d-e47bbf8c912a | -3.22359 | -42.22937 | 2025-10-26 03:57:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2405f306-a2b7-31fe-a249-133adbff077e | -3.84424 | -38.46118 | 2025-10-26 03:57:00 | NOAA-20 | EUSÉBIO | CEARÁ | Brasil | 2304285 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d5a7a46b-1caf-3a04-a205-c8708ab5c7c1 | -2.22529 | -48.37617 | 2025-10-26 03:57:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dae54ea1-c97f-3433-a211-55c40d721f29 | 0.43607 | -51.01133 | 2025-10-26 03:57:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 443e3d14-0080-38ea-95df-afdb178a97e2 | -2.76431 | -45.09576 | 2025-10-26 03:57:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| da8dc3ca-a76b-3112-a109-60d0672d72af | -2.766 | -45.0952 | 2025-10-26 03:57:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5daa33cd-035f-3879-bda7-486e1852604d | -2.22586 | -48.3726 | 2025-10-26 03:57:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a9de40c-3814-3a54-8f65-3e11190563ee | -2.76235 | -45.09035 | 2025-10-26 03:57:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2405b7d3-91b9-3f42-9f07-ea021f593e4a | -2.22653 | -48.37342 | 2025-10-26 03:57:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdb715df-e5a7-3731-8096-d80bebee872c | -2.7693 | -45.09232 | 2025-10-26 03:57:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 71aa9a0a-b375-3751-b353-22d4835c7557 | -2.77101 | -45.09176 | 2025-10-26 03:57:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 338ff6cd-a1a3-3949-9ff7-ee6ae7d44faa | -3.10927 | -41.88804 | 2025-10-26 03:57:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8d8f0bca-d6e9-39df-b725-380e8968d447 | -2.76166 | -45.09449 | 2025-10-26 03:57:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ddfbde33-7404-36f1-8be2-d74ea8218964 | -3.22557 | -42.23065 | 2025-10-26 03:57:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c413c02c-006b-3302-9d89-1a1cb887f697 | -2.76668 | -45.09105 | 2025-10-26 03:57:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 784128f5-50f5-3c66-bdda-e57d4b4a668e | 0.43911 | -51.01366 | 2025-10-26 03:57:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65b19217-9b6d-32dc-b1ee-25e02e67e407 | -2.77033 | -45.09591 | 2025-10-26 03:57:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 385facf4-ff3a-377e-833b-30dfa5522b5a | -3.45106 | -39.36002 | 2025-10-26 03:57:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 29cd7b46-87ad-3d39-8d52-117da575e6b5 | -3.10862 | -41.89205 | 2025-10-26 03:57:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ff25d0b2-0f0a-3874-8e3c-406204b0313e | -2.76864 | -45.09649 | 2025-10-26 03:57:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1b62bc7a-95ff-3fae-b81d-e89d8bc5a817 | 0.4324 | -51.0148 | 2025-10-26 03:57:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b18820fb-a9d4-38a2-b80f-a8e3a0bbf304 | 0.437 | -51.01713 | 2025-10-26 03:57:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0ee829c-7a4f-3b26-b62a-bcd9aae760a9 | -2.76996 | -45.08815 | 2025-10-26 03:57:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6ffc69d5-0ad6-316d-aaf8-f3687cd732a9 | -2.76497 | -45.09161 | 2025-10-26 03:57:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2ae9304e-2a19-344e-acae-bfa570d38468 | -17.3365 | -43.6383 | 2025-10-26 04:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 63.6 |
| dcccfaee-a6cd-3ceb-bc19-255d3f07f0b7 | -2.3178 | -48.5932 | 2025-10-26 04:00:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 0ec824c7-c073-382a-bbde-168e63075e92 | -6.3864 | -45.7819 | 2025-10-26 04:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| b7d183b2-601a-31b8-9239-8104a9afe84f | -17.3165 | -43.643 | 2025-10-26 04:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 90c61259-c87b-3009-9e4e-172466621e0a | -13.5405 | -43.0077 | 2025-10-26 04:00:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 92.3 |
| 2154b002-f3fd-3f06-9e6d-eb12ffe18d7d | -3.10068 | -49.4442 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 659df7ee-6f7d-37bc-a5b6-5c123e1b199b | -7.64578 | -42.3145 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8cfb4df9-ccbf-3524-a1a2-6315d99c4411 | -8.31892 | -46.81144 | 2025-10-26 04:00:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8b4b148-1039-3689-a4a8-912bee6da5c5 | -3.10648 | -49.44513 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d94f580-94bc-3760-85e2-e2593cbe259e | -6.44387 | -45.73765 | 2025-10-26 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f63e99fe-eb58-3e0e-a03f-26acfde21f29 | -7.19423 | -39.40987 | 2025-10-26 04:00:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0e5494f4-71fe-3018-8959-a24ce66fb5b4 | -8.21676 | -46.82944 | 2025-10-26 04:00:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 419e468b-0874-38d5-a43c-49cfba0a3ede | -5.75021 | -42.80144 | 2025-10-26 04:00:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cd2d4c8e-f465-3f6f-996f-19ac4f79ca97 | -4.90918 | -48.62336 | 2025-10-26 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75b18210-a813-31c0-984d-7f57ae04485d | -4.02179 | -46.00183 | 2025-10-26 04:00:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 537f0eaf-c049-3c08-b72a-a326c203c902 | -6.11437 | -41.73943 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 40026baf-ead3-39a2-b990-50be6dbd9ef3 | -6.79453 | -45.41109 | 2025-10-26 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4546e22f-3db1-3b38-a59c-9e8ab65a3774 | -7.55584 | -40.94796 | 2025-10-26 04:00:00 | NOAA-20 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f640b4f5-d762-306b-a662-af87d92d3cd5 | -4.29551 | -49.29266 | 2025-10-26 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54e3693d-c950-372d-94dc-2abc7272545d | -7.85264 | -46.42004 | 2025-10-26 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34142447-2a30-3ab2-96f6-e6147d013f26 | -6.54737 | -41.59873 | 2025-10-26 04:00:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 380f1b2f-55c4-3591-a655-1ede688ff509 | -5.22748 | -48.52909 | 2025-10-26 04:00:00 | NOAA-20 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7d27d95-37b2-32ad-a9a5-89b6d8825c5a | -7.40727 | -43.90123 | 2025-10-26 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4dd46d6-22b2-38f7-8ec2-a4c1fab5d965 | -8.54792 | -41.11807 | 2025-10-26 04:00:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 79bf39d7-ccdd-3e01-8d06-f1978ad7543a | -7.08737 | -39.57063 | 2025-10-26 04:00:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 482b6565-a94a-3dfd-885a-9629122fe185 | -8.04537 | -41.11699 | 2025-10-26 04:00:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 890c088f-9fc1-344c-aeed-b7c70a744baa | -4.93131 | -48.55864 | 2025-10-26 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3000ce7e-e173-3b80-9fb0-95a717e35164 | -6.5731 | -41.46027 | 2025-10-26 04:00:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b3d300a5-0dda-352e-88ee-62ee50395a57 | -3.10613 | -49.44887 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f32c754-082f-3e93-8463-a1766e6b0c59 | -5.70731 | -49.2805 | 2025-10-26 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 702e73e0-fbef-3fab-969e-3f40f7e282fe | -5.105 | -43.19419 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| d0cf9cdf-6f71-36fd-b5ba-d5679af7f5c5 | -4.80906 | -43.3008 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e1b34bf9-c922-36ff-bb82-9d2f2c1df9a6 | -8.10676 | -44.49546 | 2025-10-26 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d48d85c9-5df1-35ca-8e99-5c05e8978000 | -5.76482 | -42.54064 | 2025-10-26 04:00:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5d2eb7c1-4621-3bdb-a5ff-647c292889c5 | -3.60625 | -49.34882 | 2025-10-26 04:00:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85cbb239-82a9-3574-94a5-7f7c40092d9b | -7.39984 | -45.13679 | 2025-10-26 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb641ae6-3afb-3666-a885-c7e06669ccc8 | -6.72939 | -39.27595 | 2025-10-26 04:00:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 10.4 |
| da6f1d1f-2c3f-36bc-908d-7b75d4fbc8c5 | -5.2206 | -40.92788 | 2025-10-26 04:00:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c8027401-7e10-3263-a6d6-a5228ad47a6f | -2.3161 | -48.58049 | 2025-10-26 04:00:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c295d62-a31d-3439-867f-ee029e3cec35 | -6.43174 | -42.33716 | 2025-10-26 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6f410db0-1a92-3d6a-8cca-404f3d280dd3 | -8.21471 | -46.83024 | 2025-10-26 04:00:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 071b6b23-d2e6-37a1-841e-3a9969dfa44b | -4.70796 | -46.42641 | 2025-10-26 04:00:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README14.md)
