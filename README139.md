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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 016dce30-c0e5-3fe8-80da-2aac537fce7a | -6.78252 | -59.30921 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3cf1034-aadf-3cc3-b2aa-6580c5249a43 | -6.7825 | -59.31244 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44f17bde-47d0-33b7-aefa-bd8fd94f55ff | -6.78179 | -59.31451 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3ed1a2d-6bb7-3905-a327-849f290b778c | -6.78172 | -59.31778 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc342315-033a-3d5c-ba67-3158c309c6e3 | -6.77691 | -59.31715 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be84808a-78a7-343a-910e-2be08f3fef4f | -6.77624 | -59.31923 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63691097-236e-3063-9ab3-0d5ba6f0b4de | -6.77613 | -59.32246 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09e8c49d-8e04-39ff-9041-e6b0d045ebd8 | -6.77209 | -59.31649 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad2a47df-bae7-3548-80cc-817ed895dc75 | -6.77142 | -59.31855 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eab85500-d842-3897-887f-9e2f878fb4e9 | -6.77132 | -59.3218 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24b1f286-5033-3724-bc86-5fc2bb751186 | -6.7707 | -59.32383 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c9c212a-6c02-3c4d-a497-e8286ced8522 | -6.76652 | -59.32111 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d583426e-c492-39ff-b7f2-c2f552d1c6ee | -6.7659 | -59.32311 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc1e52b2-fc05-3d6d-9e1f-94de27ed1c9b | -6.76577 | -59.32629 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21f76988-32ce-3b20-87c2-cd816706e4a3 | -6.76519 | -59.32828 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c682ab9-409c-3dd9-b30e-cf62be0f6c3d | -6.76171 | -59.32043 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bce052b0-2f8e-3bab-bbd4-77518eb40099 | -6.76097 | -59.32558 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f95f7a5d-ff3a-3420-a319-32030df57674 | -6.75391 | -59.34055 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e3389ef-3395-3eba-8dc1-ef52a0e2f30d | -6.75135 | -59.32426 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56b86443-77c4-30e0-be7b-cbbee90cfcb6 | -6.75061 | -59.32944 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a2a50406-e180-3a5a-89d7-2d792d0221a9 | -6.74985 | -59.33469 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a8a487a4-2dcb-3492-955c-cd6cf8395572 | -6.7491 | -59.33992 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7319147e-2452-3191-86f5-ce81fc5520a4 | -6.74654 | -59.32359 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5d4243a-378a-39b1-9e01-a9f977f4bbd1 | -6.74579 | -59.32881 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8310649c-1c0a-3c1b-a7f5-884b3a0367f3 | -6.74504 | -59.33405 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d1d58390-a1a2-310b-8e5e-f2d60ef6d1a6 | -6.7443 | -59.33926 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 79a46d4b-b6a9-358f-8df3-fe1fa705b361 | -6.74101 | -59.32801 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 864ff5cf-69e8-3695-a036-1d65d5351a2c | -6.74026 | -59.33323 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 70146a62-cc56-35b7-9047-4ca9e972e5dc | -6.73952 | -59.33846 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7dd35c20-e640-3063-90d1-faabecb71cd0 | -6.73585 | -59.29532 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c159a333-6a53-3d96-830a-ad485d573fa1 | -6.73511 | -59.30052 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce6668d6-d367-3202-a508-c9332e6d3fa7 | -7.06694 | -59.40739 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6a08f80-8852-3961-acfe-eb5bdcd38313 | -7.05267 | -59.265 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 365484b1-607f-3d7f-8a2e-615f96f06214 | -7.04782 | -59.26432 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0533ed5b-205a-3102-bbe0-78b7afd80320 | -7.04708 | -59.26957 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9893b52-f794-314d-877c-03fc1f625887 | -7.02896 | -59.43373 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18af5c9b-47ff-3950-a3ff-a87021d261b8 | -7.02822 | -59.43896 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6306c11-00eb-3209-9e65-6479e3ee9831 | -6.81021 | -59.14368 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c1b9984-eec5-3032-9235-a9acac4813f1 | -6.80738 | -59.14124 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bc49986-f253-3296-b191-ac54a6c269fe | -6.80659 | -59.14669 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3069970-bad2-3034-b3ba-46ea31e729ad | -6.80534 | -59.143 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa2ebc53-da6e-3e71-8347-05a384f0fbbf | -6.80485 | -59.12436 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a8b2cb3-1876-3df9-ac30-e367020ef3f1 | -4.73349 | -60.79179 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b98c3412-debb-346b-b290-c7909fd4369d | -4.73296 | -60.79352 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4f98f3ff-1377-3bbd-bee8-e36af4be461c | -4.73292 | -60.79568 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d8b3ee8a-ca1b-33f1-8cbc-1ab32f8ad95c | -4.73237 | -60.79739 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c3cfe906-7545-385b-86b7-b999081584be | -4.73096 | -60.77948 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4613112e-5357-3031-a15e-52ccf1ccb0b8 | -4.73052 | -60.78123 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cbd20aff-7a03-34e2-87fd-b9626db46f96 | -4.7304 | -60.78337 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0880870-e6dd-3ab9-ad2d-243934cac593 | -4.72993 | -60.78512 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc187976-1b20-3064-8f96-a31a112f830b | -4.72984 | -60.78726 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 491f79cb-ab12-3bc9-85f3-97a6467e2690 | -4.72934 | -60.78901 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4bbd505b-d4fc-3cf5-a020-19e2ca99b646 | -4.72928 | -60.79116 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fa59ae7e-35c0-3f38-9a2f-5253b924c43e | -4.72875 | -60.79288 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9720a30f-9bec-3bad-aabc-87e165d90637 | -4.72872 | -60.79504 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a0551206-ed87-31ab-87ae-88aad2afc634 | -4.72816 | -60.79676 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef12cdcf-6691-324d-96c9-d7c9c277f072 | -4.72631 | -60.78061 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5aa679a3-7dd9-3072-949d-7117c4ec37ca | -4.72622 | -60.52108 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b580dba-6b49-314e-8ce1-bcc69cf170cb | -4.72572 | -60.78449 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2c8aab6-6ad3-37d9-9ab2-7e0d8bfd7c4f | -4.72513 | -60.78838 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28df728c-88d5-380f-84f3-609a949295c1 | -4.72454 | -60.79225 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccd30004-ce76-3553-b1eb-dc1e2c72a47f | -4.72209 | -60.77999 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56c0e281-f491-3feb-a638-a1b773ced404 | -4.7215 | -60.78387 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfd03f8f-99b0-39a6-8154-09d29406e78b | -4.72091 | -60.78775 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 229438d9-b19a-394e-a841-4ccea3b82dce | -4.71974 | -60.79553 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7744d424-9194-3e57-ad0d-1c3b2c288447 | -4.71915 | -60.79941 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7dad46a8-70d7-3346-978f-1ba373d5a10f | -4.71669 | -60.78718 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cf95672-8f39-302d-b421-22891364a7ac | -4.71611 | -60.79107 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6c032e8-0faf-3a5a-97cc-3d4e349b400e | -4.71552 | -60.79495 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 411b61cd-01d5-33bb-a5e5-97f16a029450 | -4.71083 | -60.82593 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9a350937-0ddf-3976-8ab3-6145987d7141 | -4.70721 | -60.82144 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa5e350a-cf8d-369e-9cb9-22831e73c0cd | -4.70663 | -60.82532 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b89c1b6f-7ad9-3972-bf15-541262f18f71 | -4.70477 | -60.8092 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4984e98-8039-35b7-902e-346c346f246e | -4.00432 | -60.38044 | 2024-10-12 05:46:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8a472019-8ac4-3084-9c01-ef16a6e6e5b5 | -4.00371 | -60.38447 | 2024-10-12 05:46:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa1f66f6-8ece-3f3f-a76c-0de8ecc043c2 | -4.0031 | -60.38851 | 2024-10-12 05:46:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e8ccabd-eff3-3626-bfea-8676a51dd790 | -4.00004 | -60.37982 | 2024-10-12 05:46:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47cbe1f9-5fb7-3838-8bba-f0ffdd7aee17 | -3.99943 | -60.38385 | 2024-10-12 05:46:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98a311b7-b299-322d-9afd-f7a519380b72 | -3.99882 | -60.38788 | 2024-10-12 05:46:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1fbcd943-53ae-3c31-883f-1c5e08b9b9ac | -3.99821 | -60.39191 | 2024-10-12 05:46:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c41b0b53-27aa-3dca-a604-e61e43cd9ea6 | -3.81447 | -60.75245 | 2024-10-12 05:46:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa4c29e1-d44c-3743-adef-72c4676aeb6b | -3.78767 | -60.11989 | 2024-10-12 05:46:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0697a532-ae09-323a-a5bb-5319753ab922 | -3.77713 | -60.13109 | 2024-10-12 05:46:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c021b873-7bb7-3f97-aa7a-8dcb0303367e | -3.77279 | -60.13043 | 2024-10-12 05:46:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d47ff4af-0622-3e66-977c-eaa75435a52c | -7.83152 | -61.36734 | 2024-10-12 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66029ffa-f860-3228-83b1-5713fdd6407c | -7.83095 | -61.37131 | 2024-10-12 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20852d92-3f5b-345a-8b51-83bd5dcd5275 | -7.8301 | -61.22411 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee4bcbfb-cdfc-3ceb-a4e5-61268a4f490e | -7.82583 | -61.22341 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6636d414-e1b8-369f-97c1-2fab321272a3 | -7.82524 | -61.16513 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 565ee24f-be83-3c22-9ea7-386dfe686ba1 | -7.82094 | -61.16451 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40222c01-dab5-3026-9ee4-f0984bcecd35 | -7.7326 | -61.45414 | 2024-10-12 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d25db8dd-6b2b-321f-bb7e-d1d70aa14ec4 | -7.73204 | -61.45801 | 2024-10-12 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c47a5caf-a6a4-3679-bdb6-35095cce5c28 | -7.65283 | -61.20021 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c2af9cd-f186-316b-90ae-d8e2a33b1929 | -7.64913 | -61.19552 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef9f673d-6480-396c-ace7-86e244eb8d7a | -7.64855 | -61.19958 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1035501a-93a1-34f4-b69a-967db54be241 | -7.59157 | -61.23242 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e18b45ea-3f1a-3b9f-bfd4-574b65eb2e8a | -7.58866 | -61.22853 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3f67b3d-400d-37e3-b633-a87939db38e5 | -7.58807 | -61.23254 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f5656afa-0ff3-3df3-9ce4-97f7091fe68f | -7.5873 | -61.23183 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0b565643-f97e-3138-b384-1314217da731 | -7.58674 | -61.23582 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README140.md)
