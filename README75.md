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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f30f1a3-c761-336c-b500-74c03660ebc1 | -3.1251 | -48.59492 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d923ffa8-19a3-3055-9fd8-12eb7c37b49e | -3.12428 | -48.60001 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 68761b70-3df3-3c73-8dd4-d6d31e5d06b3 | -3.12346 | -48.6051 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c1c80fbc-7882-37d0-88b1-ea9c560dad83 | -3.12332 | -48.63114 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5921de5e-d61a-3a5a-9784-ce18331a1c6b | -3.12264 | -48.61018 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| dc963c5c-2e4d-3ce7-95f3-bd06fccdd156 | -3.12182 | -48.61528 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 81a5259f-43a7-3b00-bee8-778bcc871585 | -3.12115 | -48.59428 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9b56197-daed-3932-ac5d-274394305be6 | -3.12033 | -48.59937 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1b7344e3-f378-32b2-bd11-12b553c2fddc | -3.12018 | -48.62545 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a7f15efd-bc65-36d9-9651-0b7b8f77a92c | -3.11951 | -48.60446 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1c6bb6e0-f152-375f-8a54-e5b06af644df | -3.11936 | -48.63052 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97ed89f2-92e3-32b4-aaef-b77d5458d103 | -3.11869 | -48.60954 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 9cbfe2a5-e6b0-3aa4-acf2-8fe36256e000 | -3.11787 | -48.61463 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2e887910-9e43-36a8-aae0-268e8c5abfd0 | -3.11622 | -48.6248 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4419da7-f574-3080-9d45-2b6178aaf098 | -3.11555 | -48.60382 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c39057fc-ee16-352a-8281-ebd90490d316 | -3.11473 | -48.6089 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| cff936ca-54f5-3d25-bc6a-fe426800aa2c | -3.11391 | -48.61398 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| e4adcd3e-33b2-3c6d-bd2e-6e90807897d5 | -2.83361 | -48.43385 | 2024-10-06 04:19:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8e98f10-9f25-3e62-8a11-6c94a0955b1d | -2.82123 | -48.69004 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b077e9d-ac0b-38a8-9245-1953b5e67832 | -2.82068 | -48.6935 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 579d665c-6cd9-3710-bd8f-afa015fa14af | -2.8188 | -48.60255 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8a631222-5556-30ed-88ac-ec4586cfeee7 | -2.81798 | -48.60766 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8f5aec9c-db29-33f2-9441-a3dfac8dae17 | -2.81778 | -48.68594 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d245513-f16e-347f-a9f3-4e28a7a13356 | -2.81724 | -48.6894 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 473b1284-ed9c-310a-9fb0-f08c4040b4e3 | -2.81669 | -48.69286 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fac3ed98-0a6e-3cbd-b224-3d81b620b9e2 | -2.81614 | -48.69632 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea16e116-a09a-36c1-b9ad-9447a1530003 | -2.81483 | -48.6019 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8ce3904d-0481-3ecd-8fe1-b7e705723945 | -2.81434 | -48.68185 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62ad6d76-f9ae-3c01-92f8-bb5c9bf3918d | -2.81401 | -48.60701 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9e321424-874a-3f16-9422-21556e575eb9 | -2.81379 | -48.68531 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| fb048a76-74fb-3ba1-9dc4-2ca845850f24 | -2.81324 | -48.68876 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 4f93dfce-4d76-3b09-8595-4f8902389dc6 | -2.8132 | -48.61213 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c283c290-ded0-3521-80b1-2975f097f7e2 | -2.81269 | -48.69222 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| c378bb54-cc1b-363c-b50e-46b520fcae50 | -2.81214 | -48.69567 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 1baba29d-3fe2-398e-975a-f3966cc11b06 | -2.8116 | -48.69912 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 610b6b47-144e-3bb8-8f10-55252238e398 | -2.81035 | -48.68121 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb73e481-b144-3bf9-bc3d-cbf9e2a9a5d7 | -2.8098 | -48.68466 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 66feaf40-dd89-3f13-a531-aa501c7a0e64 | -2.80925 | -48.68811 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 0e60a2b7-ae1f-32c1-a0e2-ae48c5838dc0 | -2.8087 | -48.69157 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 182d4c01-4d2c-3bb5-8781-06fd999953ad | -2.80815 | -48.69502 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| b8eb290e-61e1-3415-abd4-7b981e25625b | -2.8076 | -48.69848 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 47730977-3dae-3c38-9c21-c31f56621f52 | -2.80581 | -48.68402 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 460ec8ae-0e41-33fc-88f7-9d2d0abc5968 | -2.80526 | -48.68748 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d64c566c-ef00-3dfb-8363-9d6fe125c6c0 | -2.80471 | -48.69092 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62eb3dee-cae7-3bd8-bffc-5c7d3fd83084 | -2.80416 | -48.69437 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55c6d3e9-d9d6-3720-8018-5bdd589f6cfc | -2.80361 | -48.69783 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b93912ef-43fa-3c4e-be8c-43504b8ee322 | -2.80306 | -48.70129 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fdfcf2a-abee-323d-9570-d18f2370f600 | -2.80127 | -48.68684 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f250be12-786f-3180-b770-1daf70dae953 | -2.80071 | -48.69028 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21c3eb16-a268-3d25-a95c-009616dd0628 | -2.80016 | -48.69374 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a714d54-1c8d-3113-ad77-76ebd87f8334 | -2.79961 | -48.6972 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 965b5e50-4dd9-3ea2-9e9f-1f0f4e9eabf9 | -2.79727 | -48.6862 | 2024-10-06 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b0bbaf2-ba0a-329c-b073-bdcf07ad2024 | -2.44651 | -48.76929 | 2024-10-06 04:19:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be152a0c-af40-3e24-ae59-a60b24ce3c58 | -2.44595 | -48.77281 | 2024-10-06 04:19:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13d608d0-bb9e-3931-b224-632be9b44a18 | -2.40732 | -48.8578 | 2024-10-06 04:19:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb0933bb-06a0-31a1-ad41-75c63c1196d1 | -2.58578 | -47.48296 | 2024-10-06 04:19:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee55da01-eab8-3f47-bf83-e70c01b7abbb | -3.69768 | -47.61759 | 2024-10-06 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b176eacb-72f3-3aa3-ac41-af2951404def | -3.69698 | -47.62194 | 2024-10-06 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 51fcb44a-2aec-3186-afe7-4dab60770749 | -3.46571 | -47.66146 | 2024-10-06 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fd30d4a0-81e0-3c04-a427-5a16ce54d471 | -3.465 | -47.66586 | 2024-10-06 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 21fba249-72aa-34a0-aa78-3d3823868552 | -3.462 | -47.66088 | 2024-10-06 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cf27b0ff-0177-3648-b241-6d5c936142d8 | -3.46129 | -47.66527 | 2024-10-06 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ec969f22-59de-3401-99fb-58e831216b2d | -3.90854 | -48.34843 | 2024-10-06 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49d12584-de09-361e-9dd8-5514bbb00ad5 | -3.90471 | -48.34774 | 2024-10-06 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2c6dcbcf-9c17-3d7f-acca-38fb58d95030 | -3.90392 | -48.3526 | 2024-10-06 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 86d69a0a-c712-3d77-940f-90a7736c9938 | -3.90313 | -48.35743 | 2024-10-06 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 32195cc4-84fd-3f17-991b-10a835ab1f1c | -3.90087 | -48.3471 | 2024-10-06 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cd9d5ff6-2521-3ee9-92c4-9d9ff14e329d | -3.90007 | -48.35196 | 2024-10-06 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6a42af06-4e13-399e-8b64-9a6f1cfb4ce9 | -3.89928 | -48.3568 | 2024-10-06 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 15a06065-9272-32d0-91d6-e7a6de702748 | -3.89702 | -48.34648 | 2024-10-06 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b5a9227-ac5e-38bb-b795-f959443ffc0f | -4.74072 | -48.84047 | 2024-10-06 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 01c4bb18-c6a9-3f04-a8c7-ea4b3e325d4f | -4.73369 | -48.83423 | 2024-10-06 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 75745a87-89d8-3301-9597-8b1390938041 | -4.39588 | -48.71289 | 2024-10-06 04:19:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a96fd56d-704d-3ff2-af0e-7be24a4c713e | -4.39506 | -48.71788 | 2024-10-06 04:19:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f5dfb4d3-e105-3d55-abcd-d7408915950b | -4.39197 | -48.71223 | 2024-10-06 04:19:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fce3c950-5bba-38e8-8b92-0abed4d6179e | -4.38807 | -48.71158 | 2024-10-06 04:19:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7b2e642d-2e5e-3bd5-b33e-85fa4db4622f | -4.38501 | -48.70583 | 2024-10-06 04:19:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d872c84d-cac2-3d6b-b82c-8e22d66b6bed | -4.27821 | -48.64581 | 2024-10-06 04:19:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aaec75ee-0c1f-35ad-b3a5-16fc366120aa | -4.18954 | -48.87077 | 2024-10-06 04:19:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7131a59-f321-3ba7-a72d-7873efef228b | -4.11596 | -49.09688 | 2024-10-06 04:19:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 31b651d5-cf49-312e-a3f2-a74f52809afb | -4.10395 | -49.06962 | 2024-10-06 04:19:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d30dbdfa-10cb-3194-9994-0ac76da483ee | -4.09993 | -49.06901 | 2024-10-06 04:19:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39e80fe7-57f0-3e64-92e8-540187f79c42 | -3.95805 | -49.03832 | 2024-10-06 04:19:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ae696e4-216a-3625-9ff4-ef0b9f0cd802 | -3.95404 | -49.03762 | 2024-10-06 04:19:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2ffb356-cfd1-34cf-a99d-520989f8f08a | -4.27964 | -48.07045 | 2024-10-06 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5e91e063-850b-3f4d-8fb4-c0d01a8fc98d | -4.20238 | -48.13968 | 2024-10-06 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7d1181a-813b-3d29-91bb-1f280b70681f | -4.09911 | -48.27877 | 2024-10-06 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5dc87ced-f08f-3c28-8a3f-c549716f6a68 | -4.09454 | -48.28285 | 2024-10-06 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e5736f8f-03ba-38af-b362-55eb48f66807 | -4.0783 | -47.9493 | 2024-10-06 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41915ed0-aea1-3137-8ae6-6c067720c205 | -4.07455 | -47.9487 | 2024-10-06 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad9fc467-3718-3745-ac87-fc70ef111640 | -4.07154 | -47.94362 | 2024-10-06 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9156a87-c3d3-3322-a2a1-612a83879074 | -4.0708 | -47.94811 | 2024-10-06 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d717df04-4696-3e54-8813-7ccdcff3e553 | -4.06779 | -47.94304 | 2024-10-06 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36770d89-a69f-3fa3-8c41-ce67e168f24f | -9.23986 | -50.01014 | 2024-10-06 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2674562-33e1-3902-ba92-3a20dbd64c06 | -9.23862 | -50.01175 | 2024-10-06 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a4234102-de3e-335a-bcc9-b6514f804428 | -8.98254 | -49.81644 | 2024-10-06 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73b9d592-d357-3a37-a2f5-330d3cef7e51 | -8.98169 | -49.82145 | 2024-10-06 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8fc4f2ec-9927-3feb-81dd-8e1666603b8f | -8.87479 | -49.69307 | 2024-10-06 04:19:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f949873-9bcc-35cd-bdb2-80c4159a067d | -8.79674 | -49.94111 | 2024-10-06 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 761ec246-6b22-3f38-9bf4-67322b33ee40 | -8.77923 | -49.94856 | 2024-10-06 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README76.md)
