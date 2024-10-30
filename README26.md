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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7937bf6c-5174-3820-952c-b6c44e296333 | -6.3905 | -35.0179 | 2024-10-30 03:05:41 | GOES-16 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 60.9 |
| 0df0b13f-65f9-3459-bffd-7e4360dcba61 | -6.8408 | -59.0519 | 2024-10-30 03:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| aac69dfe-e7f1-3c28-96ac-677b24a9ced9 | -6.8592 | -59.0511 | 2024-10-30 03:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 91cae2c5-50ab-3ea5-bc08-530c4e5b5580 | -10.3245 | -49.6556 | 2024-10-30 03:06:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| c7be0726-fe3a-3c64-9124-103811623aca | -10.3434 | -49.6536 | 2024-10-30 03:06:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 152.4 |
| eaea1f97-e522-311e-8d6e-e5d61c734515 | -10.3437 | -49.6321 | 2024-10-30 03:06:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| d3fbb91d-58db-34f2-b550-bb0699130d3f | -10.7175 | -44.916 | 2024-10-30 03:06:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 3e980fd5-bebe-3e8a-8335-d0e6017b25bd | -19.6063 | -56.7108 | 2024-10-30 03:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 144.5 |
| c0870be8-4793-30ca-9e31-5c10cd546405 | -19.5862 | -56.7136 | 2024-10-30 03:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 150.0 |
| 8255d6e9-c515-3aa5-84f7-b0c3b3a7fe83 | -19.6264 | -56.7079 | 2024-10-30 03:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 94.7 |
| e51cca35-ac2b-3408-8e9b-22cc9b01aceb | -23.9923 | -54.1106 | 2024-10-30 03:07:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 77.2 |
| c25670d3-7aae-3987-b2e3-b96c82faefc4 | -1.458 | -54.0763 | 2024-10-30 03:15:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| e17ec950-1889-36d1-a1cd-aa556499728d | -2.833 | -49.2413 | 2024-10-30 03:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 3903c717-4a27-3c6c-a16f-4e4064ecd564 | -2.8331 | -49.22 | 2024-10-30 03:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 8b1ca8b9-d802-339a-a0bb-1bad3732ecd9 | -3.1281 | -54.266 | 2024-10-30 03:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 93271f84-13bf-3034-a08f-608e787812df | -3.16 | -50.6231 | 2024-10-30 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| a10e20e4-2729-3eeb-9e0b-534ab0c914b6 | -3.1601 | -50.6021 | 2024-10-30 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 701d1d65-87cf-3789-9796-ff7a5d1f1eb4 | -3.1602 | -50.5812 | 2024-10-30 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 7d20c1d9-cd2c-3fb0-814f-4476f47d2224 | -3.1786 | -50.6016 | 2024-10-30 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 474f213b-e2e8-398f-a3c5-6f8ac89bb2d3 | -3.1787 | -50.5807 | 2024-10-30 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 425bae44-e4af-3ded-9877-23847fbdf949 | -3.2378 | -45.5839 | 2024-10-30 03:15:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 4789e7ac-a8c9-3bb1-837a-aa39f76b8a84 | -3.2379 | -45.5615 | 2024-10-30 03:15:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 58.9 |
| dfff8fd1-3f8e-31b4-b4bc-e4256637521e | -3.2564 | -45.5831 | 2024-10-30 03:15:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 1578c4e7-1ec9-3fcd-b707-ceea7be1ff0c | -3.2565 | -45.5607 | 2024-10-30 03:15:24 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 4267b9be-a554-35d5-a8d4-a057a83dc6e0 | -3.2534 | -50.3689 | 2024-10-30 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 9ecbe995-8d75-3943-b208-3abca4593120 | -3.2535 | -50.3479 | 2024-10-30 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 140.8 |
| f0fd55ea-2b0e-30c2-96f5-0e1bd8b6ffbb | -3.2719 | -50.3473 | 2024-10-30 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| f29a84cd-c4bf-3d59-8bbb-fa9d0434a577 | -3.5631 | -47.3847 | 2024-10-30 03:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 121.3 |
| dbcabb8a-1f25-3240-90ac-1942d0ece6cb | -3.5632 | -47.3629 | 2024-10-30 03:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 53903015-0fc7-3c72-9fb3-3638a689db90 | -3.5817 | -47.384 | 2024-10-30 03:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 132.0 |
| 07b618a5-9f0f-352b-b35f-a1ea98c4b146 | -3.5818 | -47.3621 | 2024-10-30 03:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 243c80fe-d39c-3e9a-9a11-ac0860790156 | -3.9485 | -48.1508 | 2024-10-30 03:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 0ebcf217-65a4-3ef3-ba7c-64c322fe74ab | -3.9486 | -48.1291 | 2024-10-30 03:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 199.8 |
| baee702f-f3e5-376a-972c-cdfa48fae8bf | -3.9487 | -48.1075 | 2024-10-30 03:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| c042eddf-c016-3673-8d65-226075a6ce6a | -3.9671 | -48.1283 | 2024-10-30 03:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 4f99e20f-c943-3ed8-bf50-54dd759f145d | -4.0681 | -50.024 | 2024-10-30 03:15:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 049cc953-0307-3fcd-80a3-563ec97e3816 | -4.0682 | -50.0029 | 2024-10-30 03:15:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| bc10e586-caea-3dda-9a9f-ff873af984ec | -4.0866 | -50.0232 | 2024-10-30 03:15:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 3842179d-0e57-3ed3-93f4-bc8799736a32 | -4.0867 | -50.0021 | 2024-10-30 03:15:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 669fd730-f5ba-3a48-9dfa-aa1a03a4d34d | -4.2748 | -43.4589 | 2024-10-30 03:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 7f119beb-6316-36ed-9fad-46a1708f3c96 | -4.2749 | -43.4357 | 2024-10-30 03:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 652ca0d8-da02-3221-90cf-e8b0aa53b628 | -4.2496 | -50.6677 | 2024-10-30 03:15:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| bc809017-33de-3298-b08c-86750695b526 | -4.2679 | -50.6879 | 2024-10-30 03:15:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 3c367fe9-02f0-30f5-91ed-c60c021599c2 | -4.2681 | -50.6669 | 2024-10-30 03:15:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| f6248bb3-e158-39fe-b556-ab8f6bb56565 | -4.4269 | -45.8199 | 2024-10-30 03:15:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 912ebbaf-0b61-3a26-817f-d1ce60ad685d | -4.6049 | -44.3161 | 2024-10-30 03:15:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 2aae8d66-de7b-3a9b-a92f-66893a58a86c | -4.6051 | -44.2932 | 2024-10-30 03:15:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 42da9efa-2a77-3bb6-a274-a55a58ecb490 | -5.2306 | -47.9566 | 2024-10-30 03:15:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 46.4 |
| d6f73107-0ab0-33a9-9309-699abcda4199 | -6.4232 | -42.1017 | 2024-10-30 03:15:42 | GOES-16 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 65.9 |
| f5f41196-9c67-3986-b64d-5fddbd0a6be8 | -6.8408 | -59.0519 | 2024-10-30 03:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 4ce329ef-f383-3d26-b97b-ca72ec18c98c | -6.8592 | -59.0511 | 2024-10-30 03:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 98ccad20-a499-363c-9372-d64964402d13 | -10.3245 | -49.6556 | 2024-10-30 03:16:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 3e99d1bb-dc31-377d-be59-42864a64fc2c | -10.3434 | -49.6536 | 2024-10-30 03:16:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 134.7 |
| b1be8700-e038-3a48-91cf-78608d912768 | -10.3437 | -49.6321 | 2024-10-30 03:16:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 596d8175-7c32-3460-8389-ee4d72ab5882 | -10.7175 | -44.916 | 2024-10-30 03:16:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| f991b17c-6e3b-33c6-8042-9822237da3a0 | -13.6887 | -46.1247 | 2024-10-30 03:16:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 617101b6-4413-3aae-b194-53afb26c2950 | -13.6891 | -46.1017 | 2024-10-30 03:16:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 3702a1ee-be46-3d2b-a5fa-8824738a964a | -13.7086 | -46.0985 | 2024-10-30 03:16:23 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 6c536498-8a8d-366b-84c6-fa5a503b0c83 | -19.5862 | -56.7136 | 2024-10-30 03:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 136.8 |
| 8994d740-c9c1-374d-80bd-2e69709d3fcf | -19.6063 | -56.7108 | 2024-10-30 03:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 149.6 |
| 5043d96f-205d-32d0-9ffd-926fde30df2b | -19.6264 | -56.7079 | 2024-10-30 03:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 93.8 |
| 824b260a-d3b7-33f1-a54c-6f0fbfc46a2c | -23.9923 | -54.1106 | 2024-10-30 03:17:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 96.7 |
| 6eebacad-623c-34f3-9354-74c996582552 | -3.04099 | -40.07012 | 2024-10-30 03:25:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 81fcd4da-2118-3a30-bd22-5c1575d630da | -3.04046 | -40.07329 | 2024-10-30 03:25:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ee1ec003-7903-371b-83e7-98670b440482 | -3.03525 | -40.07243 | 2024-10-30 03:25:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 01a4e70f-deae-311e-be14-424cb9453006 | -2.833 | -49.2413 | 2024-10-30 03:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 121a41cc-b694-39f3-ba77-55dce58ebbf6 | -2.8331 | -49.22 | 2024-10-30 03:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| d55fa237-6576-38f0-acc8-92bf393c48bd | -3.0913 | -54.287 | 2024-10-30 03:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 7c1bb075-f7d6-3add-8eae-3f304bc45691 | -3.1097 | -54.2865 | 2024-10-30 03:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 21ac169c-f0d1-37e1-99ab-6d206164cf85 | -3.1098 | -54.2665 | 2024-10-30 03:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 5e420289-6e5c-3988-a29a-1083eea4a90d | -3.1281 | -54.266 | 2024-10-30 03:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 91d76f46-e63d-35d0-86f6-7001dc6ef54f | -3.1601 | -50.6021 | 2024-10-30 03:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| ba2378cc-1ea1-3ec5-83b9-9a355caef151 | -3.1602 | -50.5812 | 2024-10-30 03:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 61835721-5ca9-35d1-a4a6-dd80021debda | -3.1786 | -50.6016 | 2024-10-30 03:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| e066a057-808e-3c58-86a0-76616f4cfc04 | -3.1787 | -50.5807 | 2024-10-30 03:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| eaf057d6-cc78-30bd-90e7-53b1f11d7921 | -3.2378 | -45.5839 | 2024-10-30 03:25:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 842c1000-4b19-344b-b739-aae79f5794eb | -3.2379 | -45.5615 | 2024-10-30 03:25:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 9ba3b7b3-3193-3112-a51c-be34fe0cb942 | -3.2534 | -50.3689 | 2024-10-30 03:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 03b7abb2-7e29-3a43-8500-58e4f1d1fa00 | -3.2535 | -50.3479 | 2024-10-30 03:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| cba8b374-116c-3a25-833b-01e7fe8c115f | -3.2535 | -50.3269 | 2024-10-30 03:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 2425e717-304f-3bb9-9d0a-90e1ad2f6549 | -3.2718 | -50.3683 | 2024-10-30 03:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 38a0cee9-e06e-3033-82f4-034a2fa02cee | -3.2719 | -50.3473 | 2024-10-30 03:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 011cf0f1-daf1-3cff-a0f5-f71ce5d3f8ea | -3.5631 | -47.3847 | 2024-10-30 03:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 124.0 |
| d3dfde84-a5d2-3942-959e-4cb0d06893f5 | -3.5632 | -47.3629 | 2024-10-30 03:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 13199494-5ad5-34f3-8c8f-1b48d0144605 | -3.5817 | -47.384 | 2024-10-30 03:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 6ba57019-265c-36a9-b8cd-cd868271876c | -3.5818 | -47.3621 | 2024-10-30 03:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 541f750e-e7b0-3aeb-be5f-71cde6cc4569 | -3.9485 | -48.1508 | 2024-10-30 03:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 136a652f-e12a-3c7a-acd6-2cb3f5e820e9 | -3.9486 | -48.1291 | 2024-10-30 03:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| b7c97b98-bb56-3e72-9910-dce3e1a69da5 | -3.9671 | -48.1283 | 2024-10-30 03:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 33c87196-d0ce-3d3c-a4b8-c2a772414744 | -4.0681 | -50.024 | 2024-10-30 03:25:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 66bcafd8-966a-3609-a29e-476bcff2d324 | -4.0682 | -50.0029 | 2024-10-30 03:25:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 03626064-eb7c-3f77-b8d2-d52f2ba6ef63 | -4.0866 | -50.0232 | 2024-10-30 03:25:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| b368ae1f-f424-3d6c-8ca6-050e2e0ab4ee | -4.2561 | -43.46 | 2024-10-30 03:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| e3719921-ef38-385f-9016-52ece6034948 | -4.2563 | -43.4368 | 2024-10-30 03:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| c2e56c59-3a56-3d86-8baa-01c811c56eea | -4.2748 | -43.4589 | 2024-10-30 03:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 1ea6e22e-2ce9-36b5-a084-f595fdc34e3b | -4.2749 | -43.4357 | 2024-10-30 03:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| a8dde775-86bf-3bfb-a2ad-edfd0277f0c7 | -4.2496 | -50.6677 | 2024-10-30 03:25:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 6cf12de3-5334-3202-8187-09a7a618b7b5 | -4.2681 | -50.6669 | 2024-10-30 03:25:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 6a1f639f-22c5-30f4-9e6a-12a2ab96401a | -4.6051 | -44.2932 | 2024-10-30 03:25:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 1e1ab935-25dd-3d07-b3d7-ad83e71fd0ee | -5.2306 | -47.9566 | 2024-10-30 03:25:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 33.6 |


[Clique aqui para ver as próximas entradas](README27.md)
