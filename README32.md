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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91c2b3be-b3e1-326a-87c3-503cf3bf70b1 | -2.63813 | -49.24976 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fb7943e7-831e-3588-be9e-d24dac9371f5 | -2.62429 | -49.24757 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 203b0464-a29b-3f57-b760-8ab605a6c94e | -2.58818 | -49.2369 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 22f56ba2-1e1d-3815-acb7-ca6001a3c0ff | -2.58741 | -49.24165 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e16797a1-5783-31a4-a6b6-b5729afce96b | -2.57051 | -49.22924 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f3291e0f-0693-3985-bb6e-d9b42e14eaf6 | -2.56973 | -49.23398 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c06353eb-7118-39b5-8b7e-961d429f3547 | -2.47711 | -49.10925 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84c35950-e609-34f3-9996-9c1aac1aedc9 | -2.47331 | -49.10381 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9b7a9c36-4507-3577-8671-8c90eb256307 | -2.46873 | -49.1031 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4e89aa41-6a85-3f8d-b529-ee68dc238940 | -2.38858 | -49.38542 | 2024-10-25 04:14:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f783799f-96d3-3561-9263-2e599220f1f5 | -3.5475 | -50.30576 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e742f3dd-ef35-3805-805f-2ac299267339 | -3.54515 | -50.30336 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 542096f2-5e81-32c8-a067-812b4aaa65c8 | -3.51141 | -50.47976 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f69a3a4e-88c4-3dec-bac7-778223fea0fb | -3.50964 | -50.27535 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 582f1eb6-5a2e-3c51-8bdd-0570a0b45173 | -3.50874 | -50.28075 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ebda1859-baa1-3eba-b277-e07ccd2335ec | -3.46254 | -50.08486 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d9ea95e8-8e6c-33bf-a904-214da427a68f | -3.43528 | -50.35908 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1c14f8ea-6acc-3950-965c-e3f388e2ffc3 | -3.41149 | -49.52874 | 2024-10-25 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ad3f85ef-401a-3565-8c3d-95e2c6076f58 | -3.40685 | -49.52799 | 2024-10-25 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 95f69eb3-370b-30f4-831e-a9dde2c9373d | -3.31239 | -49.53064 | 2024-10-25 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57dba07c-40f9-39fe-8cf3-2a0e495b3879 | -3.30175 | -50.16471 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0a86e2ad-5d76-34de-aab9-a1194deae808 | -3.30087 | -50.17008 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a5f39ba3-7d8f-315f-9217-3cf5e4fd69b5 | -3.29779 | -50.15852 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 09468d4b-c73c-3592-91dd-6d6475efe01f | -3.29601 | -50.16927 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 77a04f77-2f29-3284-b293-ffb5da868dbf | -3.25562 | -50.2016 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f7fa0b64-fcdd-336c-b6b5-4f3c1818aa9f | -3.25468 | -50.20718 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 75b9d828-b39d-3404-babf-8671df68eb5e | -3.25287 | -50.19953 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9ab368ba-e135-34d2-88f0-406392c5b8c6 | -3.25075 | -50.20081 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4e3eb15-b1b1-39ac-aab9-b809a8c95587 | -3.21362 | -50.3013 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7c52c964-c5fb-337b-b299-4d0bd1a970a2 | -3.15933 | -50.46441 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a58958b0-5722-32e6-827c-4647c1be0d1d | -3.1548 | -49.77298 | 2024-10-25 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ab56001b-5332-3083-b6db-3357353e7c5c | -3.15437 | -50.46359 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b3120071-78e7-355c-8fb6-107d5761eee9 | -2.98564 | -50.29786 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ddad2097-104f-3c89-9bbf-321161660d11 | -2.9816 | -50.29163 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfe87b4e-4f99-3920-868a-9c54a74fa01a | -2.97032 | -50.42347 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 337d1829-55c9-3237-b668-f498736ca508 | -2.96985 | -50.42632 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 78e30bf2-65c0-3fd9-acd8-e3a369626f11 | -2.96939 | -50.42915 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 90776327-c8b9-3c04-a990-6dba7b494348 | -2.96671 | -50.41423 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cd81512d-ec59-3b1e-971b-01fc4df6b66a | -2.96626 | -50.41705 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| de31d7c3-6197-3926-b036-d433e4d06ff3 | -2.9658 | -50.41986 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 28226236-9463-3924-a119-53518624d81a | -2.96534 | -50.42269 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8f06be76-a160-3480-83ae-357946b450d8 | -2.96488 | -50.42551 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fbcf0cac-528d-3d48-a805-dce8bdb4668a | -2.96442 | -50.42834 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7d796aba-1847-3327-8742-cad9b1b21c3e | -2.96129 | -50.41624 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e7d8222-b444-3b84-9b0c-7a5aa89df381 | -2.96036 | -50.4219 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 589751b5-a241-322e-8309-bdf7de4d3db3 | -2.9599 | -50.42472 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d4a687d0-1adf-3da1-b2ab-6f719487f112 | -2.95954 | -50.5215 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ecf16766-118a-3078-a273-881b507ba805 | -2.95944 | -50.42755 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e54104c2-237b-3cc9-9777-40608374519d | -2.95907 | -50.52439 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e900d02d-2116-303e-972e-d1637d0439ab | -2.95898 | -50.43039 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b9432cb3-d5a1-3060-95e3-cc6cc15bf336 | -2.9586 | -50.52728 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ca9b055-4b25-3a3f-9819-ff7c61cf1165 | -2.95813 | -50.53016 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7e014a0-f60c-36cb-bb16-d15bd95f6abd | -2.95539 | -50.42112 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 99b3745d-d305-35fc-a3d9-4b40db361a09 | -2.95499 | -50.51787 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7c88867-7dd3-3b08-9575-933a91601497 | -2.95492 | -50.42395 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ec6d0191-bb67-3e50-a19b-40ac92c48a2b | -2.95453 | -50.52071 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0de4d7b1-a8f4-337f-9d63-d355bfb5c3e7 | -2.95406 | -50.52359 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1fa69f9-add5-390b-a2fe-24cc5987ec41 | -2.95359 | -50.52646 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ff8a3f8-3002-37f6-aa44-1b78c33da1c6 | -2.95312 | -50.52934 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d8dc386-6fcf-3e62-96c5-ed3bd87efa93 | -2.90208 | -50.40392 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd84c271-30e8-3a7d-92b2-e1ab6007adf6 | -2.8971 | -50.40318 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bcdeff4f-e8a0-3c99-8c0b-336fd523725e | -2.89663 | -50.406 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32a40e1e-f54b-3ef5-9118-65603fd41793 | -2.87269 | -49.45424 | 2024-10-25 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e5698afa-4dcb-3efb-ae19-629a8bb291db | -2.86804 | -49.45345 | 2024-10-25 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f64b5c48-e2fd-3055-b685-51412235eb01 | -2.86723 | -49.45835 | 2024-10-25 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 49f3fde4-ebb1-338e-ac05-20465573478d | -2.80655 | -49.62132 | 2024-10-25 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 54e1d6b3-6916-32af-b183-eb0c7c0dcf6b | -2.73723 | -49.80028 | 2024-10-25 04:14:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 728d6663-4dc1-3669-8ec6-964558b45dbe | -2.68818 | -49.82977 | 2024-10-25 04:14:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0629772c-a4d8-31bb-867f-acca6bb06add | -2.65672 | -49.50967 | 2024-10-25 04:14:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f966586c-2b02-37e6-81a4-dc220dc89d00 | -2.6533 | -49.83281 | 2024-10-25 04:14:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 282ee3bd-4960-33fc-aabf-5a969356514a | -2.65287 | -49.83485 | 2024-10-25 04:14:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| def69d09-38be-3814-88ac-80a739e312c7 | -2.44855 | -50.37516 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb53ac92-bc71-3cee-bcf2-a830498d5688 | -2.44101 | -50.2949 | 2024-10-25 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c17328f9-35d3-384b-8e24-da4430d35bc8 | -2.12104 | -50.14446 | 2024-10-25 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 38f6204d-fad6-3316-a970-2b1b3862dea2 | -3.54841 | -50.30041 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7693155e-4e54-3614-9c61-70f09a7194b1 | -3.54427 | -50.30872 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 703c1546-f27c-3090-bcb0-f306333769ab | -3.50577 | -49.61282 | 2024-10-25 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 692bfc82-6a5d-3688-9ae8-62eb40887c05 | -3.46738 | -50.08555 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 10f628a3-95e4-396a-ae4b-50375549e553 | -3.46737 | -50.08211 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ce238b37-4386-3d34-b052-40ffeb828928 | -3.46649 | -50.08731 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f21c30c1-9925-3049-b8f9-b81aaba4eb57 | -3.46165 | -50.08662 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 56c104cb-a32c-3cda-a4d2-1eb36531d76f | -3.43826 | -50.35793 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d56800f4-5e96-3e4b-a317-53181ad60dca | -3.43623 | -50.35347 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b844e8a7-7238-32ea-8f3b-e72e49fbe972 | -3.43336 | -50.3571 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f49c87a4-caee-339d-b207-26bdd0198abb | -3.43072 | -50.24961 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 93163eea-e5ac-3ad4-a23b-46996793c33e | -3.41905 | -50.38303 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d1d36816-c839-3f74-b952-6c14aab1de56 | -3.41612 | -49.52954 | 2024-10-25 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7446e112-4333-3f45-aa2f-523b7f57923c | -3.4017 | -50.33487 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 39d28c58-f75e-37b0-bec1-fe483003cfa1 | -3.37692 | -50.39324 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3907a3ca-6024-31a3-8eaf-15d2af464687 | -3.35169 | -50.15438 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b64cfa0c-740d-3597-aa20-30a5138724ef | -3.34859 | -50.32088 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd7d9e2f-bfeb-3d95-8214-15ce467735c2 | -3.34803 | -50.15602 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 175f2d7d-8961-34d6-b008-769176a0facd | -3.30773 | -49.52995 | 2024-10-25 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ec8620b-7d41-31db-822a-67ea925fc657 | -3.2969 | -50.16389 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a6288c15-d3ea-3867-9d55-7a7d6aa13ad9 | -3.25199 | -50.20503 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f3f410fc-0eca-3904-b585-930190968694 | -3.24981 | -50.20639 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f839605-6af4-39da-af79-449bebbb7132 | -3.1598 | -50.46157 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 89835ec6-5c7d-34f5-b46c-7908b749c2c4 | -3.15483 | -50.46077 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1e836f30-0588-3564-9cae-72b14d9a6344 | -3.1539 | -50.46643 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cee77fd3-368d-34f6-9fea-9f9b9240c045 | -3.15149 | -50.45009 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |


[Clique aqui para ver as próximas entradas](README33.md)
