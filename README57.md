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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b44eacae-0122-3758-b79c-f74a45bbe133 | -3.0338 | -50.40675 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1af4d421-5308-3c4b-b764-e6951774906c | -3.03345 | -50.42596 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e1a54e3-50ad-32ea-bc45-cdfac67992c3 | -3.03317 | -50.41079 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| dce0cbe0-dfe6-3e56-8a9c-bf953081a89e | -3.03294 | -50.40521 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5f1349be-85ae-3b13-97fe-ae95881e8b9d | -3.03253 | -50.41485 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0036a976-ba9b-39a1-85fc-7fb8220f2afd | -3.03232 | -50.40926 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ec30a006-d5a0-3d9d-bdf0-cc3d7fc5534e | -3.03189 | -50.41891 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e81a77e8-b2dc-3941-a62d-14dbf83b6b76 | -3.03171 | -50.41332 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 78282e23-c788-3893-984e-de36978505ba | -3.03126 | -50.42295 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6808af90-e925-304a-b7ac-ee4e50ba5005 | -3.0311 | -50.41739 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9596b45d-fded-3772-9964-6af3db321974 | -3.03064 | -50.42692 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ed7a7e52-1db8-3261-89e8-92b6d21d649e | -3.03048 | -50.42146 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 42a9e62d-2df1-3142-bc40-9f1b5c717f50 | -3.03023 | -50.4062 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9b6af8bc-1a25-3714-9155-b1cb65584d28 | -3.02988 | -50.42545 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 108ce299-2030-3c9a-927f-d5b72d532d45 | -3.0296 | -50.41025 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| cce78993-58a3-37ce-b779-d590e780a6fb | -3.02936 | -50.40466 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fae11a88-a902-363a-a5b2-c703df087e61 | -3.02896 | -50.41431 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8ef04fb1-f4ab-3ebb-8575-f05dd3074f68 | -3.02875 | -50.40871 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b13eead1-c4a3-3f26-8b65-8b61c086a9af | -3.02832 | -50.41838 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 20acbbd9-5735-31cd-9559-5762a2b2fa75 | -3.02814 | -50.41277 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1ad8e059-3ec2-3e83-8685-8285b8142446 | -3.02769 | -50.42243 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 626de120-ff04-3a52-ac99-7c74280b87df | -3.02752 | -50.41685 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ac731288-5ccf-3859-af3f-1c7b261954e9 | -3.02691 | -50.42092 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fc6ce240-9975-3cad-a20a-527b04fb315a | -3.02666 | -50.40566 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8c8c20c0-b87d-380f-84db-0bc13e88e549 | -3.02602 | -50.40971 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0ad4a604-26c5-3500-9dde-1046af3cc9d0 | -3.02539 | -50.41377 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 35df8fae-5e20-33a2-bbfa-9d961cdc4c2d | -3.02475 | -50.41784 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 169148b4-7876-3b29-b563-a0e0fe873605 | -3.02245 | -50.40918 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0e32a07a-033a-3319-8564-69e7d908010c | -3.02182 | -50.41324 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 206eae1f-b560-3c44-bbd5-ea1320a906c7 | -3.02118 | -50.41728 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 935a2dee-9d6b-3d51-bd32-1aaff4506656 | -3.01186 | -50.26479 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b556e293-aecf-3afe-8f5b-afb0972d7d3c | -3.00827 | -50.26422 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e07bf71-2681-381c-a672-3fc1054d0d47 | -2.96516 | -50.42527 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 448a74d2-619e-38d8-86b4-a9a683b31652 | -2.96453 | -50.42933 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b14a60b1-47d3-3584-ba45-e943a0a4f8a7 | -2.96159 | -50.42472 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0381fffd-eaa6-3b56-be24-21b03c77a587 | -2.96097 | -50.42878 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16c00fce-a59b-31b4-a59c-6279da6d5795 | -2.95803 | -50.42416 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 358053b8-261d-3d73-a567-97f5f73da3d7 | -2.9574 | -50.42822 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8c2bab70-9cfd-33aa-8a89-4ec5d1dbc320 | -2.95446 | -50.42361 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c75a3e36-cae9-3464-ade9-3ce4f2f8594a | -5.04589 | -49.61601 | 2024-10-28 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d64a1d7-5f1e-3ee8-b1ea-9feecde70c58 | -4.84627 | -49.94232 | 2024-10-28 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 356900e9-0762-31a3-83f1-bf024357294d | -4.84476 | -49.94444 | 2024-10-28 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa34f2e9-f841-3999-b105-5e1ebaa37f84 | -4.77211 | -49.45557 | 2024-10-28 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bfa5280-e069-3782-98db-d1922e4d3b30 | -4.76826 | -49.45498 | 2024-10-28 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37c39575-65b0-31ec-9de9-3f9b25460b04 | -4.74778 | -50.82403 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 92073a39-e4b6-3c1d-bc35-e91abc672a1c | -4.74717 | -50.82809 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 79d99fb7-7a49-3f83-84de-98c7198796af | -4.73451 | -49.39053 | 2024-10-28 04:57:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ccec2f59-066c-3294-ae55-e969750c47ea | -4.73378 | -49.39544 | 2024-10-28 04:57:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 599829a9-389a-34d3-8287-71cdb889a2cd | -4.73067 | -50.79222 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad83b9b0-f8d6-3304-9de8-282dd707871c | -4.73064 | -49.38999 | 2024-10-28 04:57:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c38f1220-92f9-3747-8417-cafbd4c137dc | -4.72991 | -49.39492 | 2024-10-28 04:57:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f5cf67eb-cd0c-3a9f-84ef-71ed334f12ba | -4.72605 | -49.39431 | 2024-10-28 04:57:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c8d6cdf7-71d2-3c81-b167-220e817a33d5 | -4.71463 | -49.8341 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 315d9970-bc11-3756-9d51-a23388dfb4ab | -4.7026 | -49.60518 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e103fbd-42f8-3c7a-a2ea-9d0cd4bd2b12 | -4.62994 | -49.60089 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc310af3-4512-372e-8978-7ffa61cb856f | -4.60731 | -50.56123 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08bc78a4-b78a-3f10-9e9b-e4cf20945179 | -4.50493 | -50.75195 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43a04120-28ff-39dc-b875-203fa08aca32 | -4.44265 | -49.76447 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c41491f-db33-392b-9014-e009c44d5d23 | -4.40744 | -50.56737 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5570b943-3d6c-35a4-afd7-d2d64f08b0a4 | -4.40681 | -50.57149 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4083974c-bfc1-34c8-8acf-ef5d1a237651 | -4.40586 | -49.72388 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b9ada83f-6b7d-3fb8-92f3-84e2665d069c | -4.40194 | -49.77479 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e254759e-9a40-32b9-9954-8fcda46a2895 | -4.39414 | -49.7502 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56de6ab2-cca5-3845-8b99-0c66eabe03fe | -4.38968 | -49.75425 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7ce528c-ab4a-3a7b-bf1d-d37d9923d3ab | -4.38899 | -49.75877 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c10ded8f-e804-3a91-bc14-4c76b632d880 | -4.38592 | -49.75368 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe6b2ab0-bb31-3370-a98c-f3a962947989 | -4.38523 | -49.75819 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c560e24d-8a65-3e9c-9556-9074a2dbf8fd | -4.37713 | -50.45191 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e243bf0-46f6-30a4-aa44-e30e06781b54 | -4.28354 | -49.40148 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 223cc4d9-50fc-35cf-8306-4d352439f8ca | -4.11541 | -49.2596 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b3e6b6d-0599-3d98-af37-fe7a8ab4e3fd | -4.11469 | -49.26442 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c6e270b1-2b24-3c23-9670-def3a211b50a | -4.11083 | -49.26384 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 724b4217-c7dd-3573-8087-2b4ec0ed23ef | -4.29633 | -50.74314 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b17161a-039d-39cf-a0df-fb4e45a56638 | -4.29573 | -50.74718 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6c69778-d7bb-3a22-83ed-3060e817c928 | -4.12598 | -50.50538 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a814e51c-e7a5-3349-b68b-5479c133f7dd | -4.12238 | -50.50483 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ee2970a-8b29-3abc-9315-d53cc339310b | -4.07217 | -50.02244 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b8329f7a-7fca-3ab4-be7a-d0c8790960d7 | -4.07167 | -50.01997 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 61c06437-dd22-3781-afb2-fae17ae2fec0 | -4.07149 | -50.02681 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 78494e2e-38dc-34cc-b603-1287a627a705 | -4.07147 | -50.60797 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00bdf26f-72f0-321d-abcb-a87aba0d6a60 | -4.07102 | -50.02435 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30bad1d2-5ba5-34e4-9e46-99a358233cff | -4.07081 | -50.03117 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5c663ba7-699d-3143-b2d7-39d46b518810 | -4.07036 | -50.02874 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71710ce1-43bc-3f2f-8c85-64b73e24d7ac | -4.06971 | -50.03312 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02607c5e-88d3-3316-85f2-a8324d8b55d7 | -4.06848 | -50.02188 | 2024-10-28 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6e2bc6b5-3879-3c47-a8d7-0c8d2887945c | -4.06798 | -50.01942 | 2024-10-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b34aade9-ca3f-3cb7-a068-df0d56f71416 | -4.0678 | -50.02627 | 2024-10-28 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9bc74e39-448a-3085-b0a2-f2dce7421f81 | -4.06732 | -50.02382 | 2024-10-28 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d79e7f4b-fc2d-38ba-89e8-02a13b088918 | -4.06712 | -50.03065 | 2024-10-28 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| acd64259-2303-3eed-96b9-6380333e4319 | -4.06667 | -50.02822 | 2024-10-28 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5ee515fe-ec38-359b-9f9f-287b9aee1f7a | -4.06478 | -50.02136 | 2024-10-28 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 784e1362-c5df-3e5d-a83c-e8b88477ec8e | -4.0641 | -50.02575 | 2024-10-28 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1c54b81-ddcb-3ab1-8ce0-ab0aa72a5674 | -4.06363 | -50.02329 | 2024-10-28 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 507c10b2-d0e7-35f8-9378-d690f379d163 | -3.99428 | -49.98822 | 2024-10-28 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ceea6d22-0e1a-39fa-b642-ab62afb27973 | -3.99058 | -49.98766 | 2024-10-28 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b2f6cda-13ae-3842-b5c7-74206337122b | -3.67775 | -50.29506 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ddee2ecd-e419-3be8-a317-53c63068fc67 | -3.6771 | -50.29927 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c7f9260-ded5-3cd2-bff0-0b61a64bf70f | -3.67478 | -50.2903 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91c42abe-448b-344d-8214-ad5349195a8d | -3.67413 | -50.2945 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c3f86fbc-1837-349d-b822-64e64a98de10 | -3.67348 | -50.29871 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README58.md)
