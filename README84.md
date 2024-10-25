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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa10cf26-e477-3011-bc0d-1ce85e7a1743 | -3.44085 | -50.16 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 764792e5-b9e8-3c2b-a4ac-05ddce71019f | -3.43529 | -50.3574 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 50c58aee-29f6-38dc-8fd4-f1d7e22b80b1 | -3.43133 | -50.35678 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40adc5e3-8fc6-37bf-961d-a8fd9978080e | -3.42716 | -50.25047 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 04515aeb-747a-3445-a2e2-9bc86388ce56 | -3.42664 | -50.2539 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 81c9db47-a932-32b9-88ab-e0beb90a621b | -3.41951 | -50.38111 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5fe9c8a-ee3c-3dab-a1fe-a99f481766fa | -3.41468 | -49.53128 | 2024-10-25 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 10f38f05-c4b4-3bda-8750-94f51809aa18 | -3.41049 | -49.53067 | 2024-10-25 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d4bc7110-d929-3d85-84b5-b0b98ba6a67b | -3.4063 | -49.53004 | 2024-10-25 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8c28865f-32e5-3e6b-808c-31240b070c73 | -3.39243 | -50.34586 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cbd48492-7aa7-3b0a-ba24-62c8c447d709 | -3.34948 | -50.15644 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ab2175c-b0bd-31c3-a227-a552aa6d4c07 | -3.33441 | -49.95537 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e61ccea-b773-36ed-be94-b7601d30557c | -3.33387 | -49.95893 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db624ee3-a6e0-3fff-9f81-5f5f7700ec9b | -3.33268 | -49.72382 | 2024-10-25 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8beafc0-dc5c-3c49-93e6-a136973af7b9 | -3.3298 | -49.95839 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4391317f-72b1-372e-9bb3-2c70ac33abb5 | -3.32367 | -50.10985 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0623e32-92c8-3aad-b01a-4d54b63e8bb3 | -3.31965 | -50.10924 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 742caeee-f37b-3ff5-a6a1-48fb29caad50 | -3.3109 | -49.53196 | 2024-10-25 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 594a085e-9591-3842-bb84-4917037b8008 | -3.29924 | -50.16333 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4917ceab-2795-3088-bffe-d7f4fa736510 | -3.29872 | -50.1668 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b48c5705-5c54-3154-9cfb-e80646edade4 | -3.2982 | -50.17028 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b34949e0-e240-31fc-b409-7ab33ba77c86 | -3.29552 | -50.10553 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 780adb26-2539-347e-9210-f4bc88d4edb9 | -3.26947 | -50.08025 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b1ce24a-aaae-3818-bd76-7f512d93ce56 | -3.26598 | -50.07613 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d252b8a-a75b-3ee3-8757-08f9e738dd09 | -3.25872 | -50.15012 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a248a9a3-0546-3112-8a43-2a0ea379b6ba | -3.25818 | -50.15361 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6ab3f1a-46c1-33eb-bf2f-d850589023ee | -3.25073 | -50.20206 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cb0afc6b-0735-3bae-9fb6-10d9013b6f94 | -3.25021 | -50.20544 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6dc93b72-9957-3306-8c52-a685a5430c7e | -3.23397 | -49.11906 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b187027-1ead-3a71-bf02-91b5d47d2498 | -3.23131 | -49.11982 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 98b422f5-5ab2-337e-840c-82135755c41e | -3.23027 | -49.11439 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f5e8a69-d7d2-3e84-83aa-0328c83cee2b | -3.22751 | -50.16669 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6bbf3119-d371-38e1-8606-c2b3a833deb4 | -3.22298 | -50.16956 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39ddc2ee-cc08-3856-91e8-5677ed770922 | -3.3487 | -50.32107 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 081c6339-976d-3206-898c-48a5bab8ee90 | -3.31912 | -50.11276 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7fa0c01-da2b-325d-a9e6-f6605294311e | -3.30672 | -49.53131 | 2024-10-25 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bf8e06b-7e7f-3b19-ab8a-21b40432fb2c | -3.30274 | -49.55788 | 2024-10-25 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bc316fb-b7c7-3a2c-ac90-e0ac4310182a | -3.29954 | -50.10617 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 835cf323-c800-340a-87af-094f9bdeffaa | -3.29523 | -50.16273 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d22fde72-058b-3137-898f-be885470b3cd | -3.25472 | -50.20266 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 55df5e8f-5bb1-3b86-8c69-e3e15c2ad024 | -3.25471 | -50.14951 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95b84298-16ee-32ca-bafc-a41cc1f067f3 | -3.2542 | -50.20601 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e04b2c41-e6bd-3620-bd5d-51123df58bc6 | -3.25418 | -50.15299 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf8fce38-594c-3590-a48c-df428e8e7826 | -3.25231 | -50.13845 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d64ac7db-bac2-37dd-ae80-f94209fbd77d | -3.22968 | -49.11843 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b751ed67-ccf9-3a92-a9af-96176bd8074b | -3.22908 | -49.12247 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48ae5b10-2c64-3484-8065-82dbb2b6d322 | -3.22764 | -49.11516 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ecf9251-a144-33f7-9586-2988d7093958 | -3.22351 | -50.16608 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19af6fe8-e1e4-3a59-a767-c0cb68c349ec | -3.22335 | -49.11451 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07ddc153-929d-3ecc-b3e4-11e1ae7b3535 | -3.22245 | -50.17303 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a3a32a6c-2608-32c2-91c6-9f7238081ba7 | -3.21951 | -50.16547 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 42fde4d4-6927-3cc3-a3f4-3e4a9fc1b247 | -3.21898 | -50.16896 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ad05b62c-ab27-3dc3-95e7-7aefd86279ca | -3.21845 | -50.17244 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 52b5de40-a394-3c6a-ae4e-21c34c5c390d | -3.21843 | -49.11789 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85dd7571-b2a3-31a2-9c4d-e0cf6b4f30ad | -3.21445 | -50.17184 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 893b0b46-7c8b-3dee-b77b-a38d1a37f259 | -3.21393 | -50.17528 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3bf10da6-9c51-35b3-87ca-2c7e3919b5b1 | -3.21045 | -50.17121 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a890d6f0-770c-3fe6-8631-d00e28be28f0 | -3.20993 | -50.17466 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 853dda4b-069d-3ee0-b567-1dc20cb84747 | -3.15866 | -50.46088 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9056ed3d-de3a-3274-a48e-9b7eaf7c906c | -3.15791 | -50.46586 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 696a18aa-81c9-3c5c-a804-060c7c8f6808 | -3.15473 | -50.46029 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 862bd1da-55ec-3d87-8234-e57657251f67 | -3.15398 | -50.46527 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3a936da6-138a-37d7-85a1-04a96f3e89ff | -3.15388 | -49.77231 | 2024-10-25 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| effe9f9f-12f6-370d-8346-2af0105e1f53 | -3.15333 | -49.77598 | 2024-10-25 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf25e4fb-9f11-3200-9b5c-512fc3e09944 | -3.15156 | -50.4547 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a0c2d9cd-d657-3b87-b37a-00015ff239a5 | -3.15081 | -50.4597 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2711d059-f45f-3fa8-8314-5c13c9100652 | -3.15006 | -50.46468 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3c9a756b-82fe-3127-b8bd-ba683dc05014 | -3.14978 | -49.7717 | 2024-10-25 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3f23751-52b5-3a3d-a481-e07e21ef231f | -3.14764 | -50.45411 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 66ba20b3-8e26-3151-afc0-0803d2a68de9 | -3.14689 | -50.45911 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b4843573-49ea-310c-943e-8f1a86609835 | -3.14371 | -50.45352 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 223d7eb2-8247-3175-9ad0-70c429482af1 | -3.13756 | -49.53044 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53f3ae08-19ba-302a-9748-5d0036ae39d9 | -3.12361 | -50.42762 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5ec31e9a-36aa-358b-8279-29a75faef40f | -3.07488 | -49.57897 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ef129ba-46b1-3a94-af11-dfe47197acea | -2.88722 | -49.50212 | 2024-10-25 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a51506df-f264-3e64-b3dc-adcfe361fa67 | -2.87324 | -49.45348 | 2024-10-25 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f58e0563-35b4-391c-aa06-a4795adb40c9 | -2.86906 | -49.45286 | 2024-10-25 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2bb7b446-8f28-3866-852a-675da17b26b5 | -2.86432 | -49.45605 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4b2d1790-9719-3a15-ba4c-232bff602831 | -2.81685 | -49.25197 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b6256499-cd3e-38b7-9d0b-60bf8ddf0f1f | -2.81626 | -49.25588 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b907f9f3-69ca-32c3-8be2-03e727ffe4fb | -2.81262 | -49.25134 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 576a5f54-0a67-33f5-a2b8-5738aaa4f7ee | -2.81203 | -49.25524 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6bdd63d5-f8cc-3dc2-bb16-169897e03b93 | -2.81144 | -49.25913 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6e45fc62-4bf4-3686-b4e4-c3dcedbda842 | -2.81016 | -49.23895 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20ba8471-cddf-3fd6-8ae4-a641c20e89c2 | -2.80957 | -49.24287 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c724bfe1-bfb3-39ac-87a6-fc8f43571874 | -2.80898 | -49.24679 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b22fa614-de92-36db-982e-b4feacad41d3 | -2.80839 | -49.25069 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 34382674-20bc-383c-88ba-434db7ff0778 | -2.80781 | -49.25458 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c88cd524-6c7d-30a3-a47d-4023613c39df | -2.80743 | -49.6203 | 2024-10-25 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 130436f9-c7b4-33d1-a2d6-94e9b71fd1b3 | -2.80722 | -49.25848 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fad1564b-2527-3c57-8ea1-2dafdd7af8aa | -2.80593 | -49.2383 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf8448bd-da10-3b25-b6e6-ba82f25002b9 | -2.80534 | -49.24223 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e6956ef-1452-354c-9052-c4a84866893f | -2.80475 | -49.24615 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51b8bb22-e120-3d5c-b6b5-ac93c835dfa2 | -2.80417 | -49.25003 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93229bd2-3471-337d-b57f-860ba8aa417a | -2.80358 | -49.25393 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b62cf07b-a476-317a-b0c4-09bea888441e | -2.80111 | -49.24159 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 67dc5e8b-8470-3d07-9cbc-f04ea5cbad07 | -2.80053 | -49.24551 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4a7f850e-eebe-323d-a451-62758a3dc055 | -2.79994 | -49.24941 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 74074027-6793-3bbd-9d06-a0870da6a14e | -2.79936 | -49.25331 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6dfd0c42-6ef2-3aed-afd3-136e72742e31 | -2.79688 | -49.24095 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README85.md)
