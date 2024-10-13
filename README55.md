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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 999b19b3-54b4-3cff-8c52-0d520c67c137 | -2.5691 | -49.13291 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d3b7e9ca-cb9e-3785-9e49-0af03d83f114 | -2.53192 | -49.02484 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3039d6bc-7ed8-331f-8775-926310dd7645 | -2.46758 | -49.02173 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbed25f9-8408-32b7-b81c-19ce38d3eb22 | -2.46481 | -49.01778 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb2f0036-b91a-3ce9-bcd3-5ee1b3d7ef58 | -2.46427 | -49.02122 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9df08d00-e478-3dff-9ccf-2205995bbd11 | -2.43215 | -48.94579 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 745e97d7-493d-3632-aa02-044a5a9b146c | -2.43195 | -49.07616 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ade110a-d297-3915-86ac-54bbade34301 | -2.43161 | -48.94923 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17b215ed-367e-3d2d-88f0-f6cecf750b5c | -2.42939 | -48.94185 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 595c0e6c-9be0-39d9-aec2-55af5f239078 | -2.40841 | -49.13963 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 521446c8-0e4a-3819-9d3c-41e958dadc78 | -2.4052 | -48.94514 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4dbca0a-7559-30e8-96eb-e5394cf77bf5 | -2.40244 | -48.9412 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 893a8155-6022-3527-bdbb-42453aefd5e7 | -2.37973 | -49.12811 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4881dc23-c94b-3828-a46e-fc4feadbf9d2 | -2.37918 | -49.13156 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9526d2c9-54eb-3854-8c32-22e1cb6557e5 | -2.3221 | -49.16801 | 2024-10-13 04:38:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b3c1c0e-c7d0-3603-8df7-9f62dc26ce90 | -3.33763 | -49.16239 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b63ce84-1caf-33df-bc84-a05cad601de4 | -3.3365 | -49.14811 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5fdc4d8-ef2b-302a-88e2-bdff177caa0f | -3.33596 | -49.15156 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 053da4a1-46b3-3a18-9113-3be51682694c | -3.33587 | -49.12666 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38777602-3673-3efb-a08d-352a045c7dbc | -3.33533 | -49.1301 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a444452-aeb9-36ff-9164-d094040f31b0 | -3.33371 | -49.14042 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7cad1dc-4d42-3316-a7df-1ab08e2a61cb | -3.29457 | -49.10968 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f4e4236-ead9-3c08-85c0-d356a764aefe | -3.29235 | -49.1023 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 906bbbf4-ec4f-33fe-b3c6-b6465d55e5a6 | -3.28683 | -49.0944 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 787679be-082e-34f0-815e-ecccf65f5bcb | -3.28407 | -49.09045 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e9be2d9-c7b3-33d4-af4e-a734cbd6e9b0 | -3.28023 | -49.09338 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa7082d2-67bc-36da-b027-6607eb4950f0 | -3.19032 | -50.45964 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65898ca7-0ce1-3dbc-af89-12e8f763ed7e | -3.1875 | -50.45549 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a21dbef-44da-37b4-ba6d-becc9d5b4d4f | -3.18693 | -50.45911 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 506f45ec-ee99-3182-b908-4a72af5a4c04 | -3.18411 | -50.45495 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2d59228-e02a-3972-be0d-5857b87097b5 | -3.18353 | -50.45857 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 0daa0772-7ad9-3eff-8bfd-6b831be6ed20 | -3.17956 | -50.46167 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 63ebb196-4950-3f82-8f47-34eac05be255 | -3.17899 | -50.46531 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 24533a2d-32cd-3ce8-a903-d6082e091895 | -3.17733 | -50.45386 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20e6f207-8118-36a6-98eb-e84c9f6983b5 | -3.17394 | -50.45333 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17e64132-823c-3b74-8b5a-3a4d037355fb | -3.17336 | -50.45697 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f7a3aad6-0d04-3da3-8020-6c3b2c705c65 | -3.17278 | -50.46061 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5eabfcf5-4569-3f1c-9e2e-31030464821b | -3.17104 | -50.47153 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7eb6d550-f3b8-30b7-92cc-9217765295ab | -3.16599 | -50.45954 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1d55f62-78e3-36a9-8be3-d6517f22ee65 | -3.16541 | -50.46318 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a7d5612-2378-389d-a733-08d826975670 | -3.07317 | -49.52127 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5434c8aa-7ba8-3ec4-9c55-f4daad745eff | -2.99408 | -49.52668 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d5300985-1d81-3a12-88df-d4cc3e0182a9 | -2.99353 | -49.53016 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 10630315-30d1-3514-b6c2-c206f842ad61 | -2.99076 | -49.52617 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6e987ade-9e1e-36f4-842b-a913a4e29613 | -2.99021 | -49.52965 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eae9be1c-3a7d-3cd2-87e6-441fd9b7c69e | -2.98966 | -49.53312 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a02da04-2e31-36f9-ac73-2b6784d29189 | -2.98744 | -49.52565 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14ee30d0-b77f-3e60-a283-0793a12db824 | -2.98689 | -49.52913 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcea9d36-faca-31ce-8e9b-43f1749d40a7 | -2.966 | -49.35817 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91b8316a-5b1c-30c7-af3c-21f9148c92d5 | -2.96323 | -49.35419 | 2024-10-13 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c3fb02f-ce53-3445-baf9-c77673744824 | -3.40662 | -50.35978 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea8a0041-ee90-3ec6-9e4a-e0a928ceb527 | -3.31982 | -50.46148 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| d4744ac8-752f-3def-8fb0-06d4cc0b8743 | -3.46574 | -50.60732 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fdd68dff-f3c7-373b-9fda-e7b44ca192a8 | -3.46234 | -50.6068 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41015ed5-8760-3566-ba3b-61297fdf5108 | -3.31644 | -50.46094 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd99c097-7923-33c0-ac76-137418a3f5c9 | -3.19089 | -50.45604 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bdaf5171-729b-39c6-bf44-9a69969a88a0 | -3.18974 | -50.46326 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7fceba04-2df5-369f-9b1e-8a9a8cc77399 | -3.18807 | -50.45189 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2968d325-1c40-3150-8b7c-9f947410e04b | -3.18635 | -50.46272 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| c0378be7-679a-38f0-bb2f-7ada1d07426d | -3.18577 | -50.46636 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c6b999d-30bb-3d96-9dd1-f0735a1959bd | -3.18468 | -50.45134 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dd69492-3a78-3e7b-8874-bf87088141f9 | -3.18296 | -50.4622 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 0ea576c7-be84-30c0-8552-23f9e59231aa | -3.18238 | -50.46584 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00c4f0dd-71e5-3160-b9da-c183fecacc0f | -3.18129 | -50.4508 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34d59e19-81e6-39e3-a476-d6bcc7702a87 | -3.18072 | -50.45441 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fb46023-a51f-3496-ae4f-ed17af5ef297 | -3.18014 | -50.45803 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 707016d5-b3c6-3619-a314-a12354313af0 | -3.17675 | -50.4575 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6f768c88-cd20-3dfb-a4eb-409d9c53df36 | -3.17617 | -50.46114 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ef73af90-5217-37e4-bafe-3d8f52cdee24 | -3.17559 | -50.46478 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6eda825d-37fd-34cb-9b50-3c3807370507 | -3.17501 | -50.46842 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9633ffb1-3d09-35a1-a7f4-9feb23ff7c05 | -3.1722 | -50.46425 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2206b8a4-de04-3044-b861-1d56d8a483d5 | -3.17162 | -50.4679 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a655c1fc-0992-344f-914d-f77a07c20d01 | -3.16997 | -50.45643 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c174d859-8987-3f25-9c00-c11e69ca77b9 | -3.16939 | -50.46008 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d66ba400-acb6-3847-b46e-0426054fc608 | -3.16881 | -50.46372 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e5ef4e58-2a3d-3f25-8976-bc4aa96e5b12 | -3.16823 | -50.46736 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| fa4dcea0-5542-336a-a445-2470afaf07d3 | -3.16765 | -50.47101 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1be2436-32ef-3d86-bb89-fb0988a37ff4 | -3.16483 | -50.46684 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3253d00b-607d-367d-b565-5c3b7cd65dfb | -4.02597 | -49.56464 | 2024-10-13 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 630e1202-dfbc-3ba9-b1b9-cc754338bcb9 | -4.02266 | -49.56412 | 2024-10-13 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 97dd73c0-2413-33b6-b39e-76f5bd27b3f7 | -3.96454 | -49.89034 | 2024-10-13 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e68352d4-846e-3726-8c0a-cb115a9065ee | -3.96122 | -49.88982 | 2024-10-13 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0a3f931c-74b7-313a-a5a8-4c682cda8726 | -3.9568 | -49.91788 | 2024-10-13 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3d19be1-1dda-35df-945e-cf18d4191682 | -3.95625 | -49.92138 | 2024-10-13 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eea9cade-fc02-3b73-9cc2-73761f96551b | -3.92461 | -49.992 | 2024-10-13 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09935002-8298-38bf-ad25-66877876ac69 | -3.77535 | -50.16065 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d5d9173-044a-39e2-991f-eea9a893fe1c | -3.70085 | -50.11636 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b61e02d9-e457-3571-8356-92fe5ae34353 | -3.69694 | -50.11938 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b0d00ca-57bb-3aca-b2fa-ac1893a50ba1 | -3.69638 | -50.12292 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ec6f7f0-ea5f-3d1f-8f31-502ff820a751 | -3.69415 | -50.11532 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| caa3d86a-523c-3a30-afe6-02efd68df232 | -3.67802 | -50.04386 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f12f4eca-03df-3e9d-80db-47a41c19c091 | -3.66537 | -49.86514 | 2024-10-13 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2ef319d9-c80e-38e6-9d37-7195a062c184 | -3.77592 | -50.15709 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 188a3a09-6a60-378d-9c5d-aa0295d1d4cb | -3.73518 | -49.68277 | 2024-10-13 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb47873b-b298-3c8a-bbf0-baa0536c352e | -3.70029 | -50.1199 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 694bb58e-a18d-3306-87aa-1c26091c4c12 | -3.6975 | -50.11584 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4dd39be-0f90-3125-8d43-98ebb12795b4 | -3.69359 | -50.11885 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a7e8f69-10b1-321b-8642-0a0059b079ae | -3.69304 | -50.12239 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a559f7ec-5dd0-39f0-a1ad-93c8e0d11e40 | -3.57724 | -50.56889 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b19ea83-0916-3533-bd27-97277fc7e8fc | -3.57385 | -50.56835 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README56.md)
