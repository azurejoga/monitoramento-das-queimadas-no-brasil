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

## Dados Diários - Página 216

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| adcdb68c-b958-308a-8162-bd1f0bf33cab | -18.60178 | -57.23907 | 2024-10-09 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| d25be90e-e844-3a8c-9d8c-16cc1f6c8d21 | -16.7816 | -57.46199 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 2b96e8c6-8cfe-3e43-9c44-7d7f36baca14 | -16.78101 | -57.4684 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| d390ebc0-022c-34cc-a719-7dfcadb67564 | -16.78042 | -57.4748 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 14d2957b-2ee9-34d1-8d8f-e2b267bb22e9 | -17.12921 | -56.8487 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 818be253-c8e6-373f-93a6-bfe606ee7ca0 | -17.1286 | -56.85579 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| a9bae853-6ec7-34ae-8108-750b013ada9b | -17.10736 | -56.85342 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| af9d180a-61c8-356c-806b-0159e6cdbcef | -17.10253 | -56.85627 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2aad75f5-bf78-38f3-89cd-d9918c5701f9 | -17.10188 | -56.86335 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 507309ae-febc-3c4f-b719-0dcd3e4f3871 | -17.10027 | -56.85264 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a4c60feb-0f4a-31e8-ac30-f4fbcf8995ed | -17.09967 | -56.85974 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| feebd849-8e3c-303d-bffe-676f511a967d | -17.09907 | -56.86684 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4bdcb769-a0f3-37d4-aaf7-a13d41d15e9c | -17.09544 | -56.85551 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1c0df12d-9489-37db-b840-f2da9af24b5f | -17.0948 | -56.86261 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e040ac56-edf1-3e6c-91b3-31b655dc1ace | -17.09319 | -56.85186 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2c8fa810-8386-3683-9638-d0a86ecd823a | -17.09259 | -56.85898 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 83abc339-de86-340d-8055-354c715eeda5 | -17.089 | -56.84768 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 704bdfa1-7df8-3eb3-89fc-aea69bdfe5e5 | -17.08836 | -56.8548 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2c0e67a7-7e36-3c7f-a38e-2265ab2b4128 | -17.08772 | -56.8619 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6c081b42-900a-32ff-8e8f-5c464e8f1b84 | -17.08709 | -56.86892 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 466a3252-5969-3fd4-9ac1-5faa59bcd20f | -17.0867 | -56.84396 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 586d0f48-796a-35e3-8159-266f94849a06 | -17.0861 | -56.8511 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f3085493-9ecc-37c4-aaa2-cf01eefb80ea | -17.08551 | -56.8582 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| faa72325-1f07-3133-abac-74415960d0b0 | -17.08492 | -56.86528 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b8aa0818-f408-32e4-a900-85644d582b07 | -18.59995 | -57.23604 | 2024-10-09 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 5d26e410-c118-3f44-8214-1fe215faa0a7 | -17.08192 | -56.84689 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9dc6c6b7-57de-376d-b590-61b541e7132b | -17.08129 | -56.85396 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 21ec7deb-41c3-3bac-ad10-bba55ab21590 | -17.08065 | -56.86105 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a735b7f9-2c6f-3f08-b6ae-dc6ff822662c | -17.07903 | -56.85022 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d371bfa0-9b1e-3d12-852f-124f71afa4b3 | -17.12933 | -57.32767 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 4a5a21de-e05d-3944-b450-42f6991b3a31 | -17.12822 | -57.34089 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 1484475f-f0c2-3e25-b979-11c792ced323 | -17.12815 | -57.33954 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 6d66c043-b331-30cc-9413-0bbea2605ec4 | -17.11888 | -57.36515 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 3dbdac0c-aa20-30ef-91da-b7b0ef77c50e | -17.11199 | -57.36438 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| ebc2c320-8416-3079-b424-afcca2b72278 | -17.10117 | -57.32992 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 916a16ec-d4e1-397c-a325-a17eaf7a2033 | -17.0937 | -57.33571 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| b351c090-5854-3428-8762-c3bac3696d0c | -17.08622 | -57.34154 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 4e68a4e4-2805-3582-9617-7a34c5e99fc2 | -17.08564 | -57.34813 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 64ebb692-6f6d-309f-a1c8-7df680a16d5b | -17.07759 | -57.36052 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.8 |
| b6dd5878-6e5f-3e26-ac6d-10c11d0a60ef | -17.07729 | -57.35642 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.0 |
| 497c5897-652c-3a41-a83c-8fcb804986b2 | -17.07701 | -57.3671 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.5 |
| bed740e5-d05f-3cb2-9bb5-9103638578b7 | -17.07667 | -57.36296 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.5 |
| ac1d302e-1287-36c5-b6e1-238f3f38c647 | -17.07643 | -57.37367 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.5 |
| 4d9fda0d-6c15-3ec6-b867-606195e20311 | -17.07605 | -57.36953 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.5 |
| ada1e595-b49a-3ff6-9c1b-558de696f6de | -17.07543 | -57.37609 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| d2009d92-a57f-326d-bc04-0f64f28e5b4f | -17.07071 | -57.35974 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 10fd409f-d792-301b-85d4-7ae50d507181 | -17.07013 | -57.36631 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| dc2009d6-6c47-3d11-a92f-d063eab16cfd | -17.06956 | -57.37289 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| f22393d8-8577-3fbb-88e7-bdb6a8072990 | -16.92044 | -57.48316 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 3017027b-b08b-3482-a1ce-8fb2c8519762 | -16.91903 | -57.48476 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 72e44e30-a095-3807-ac6b-0d10e924cba4 | -16.91843 | -57.49117 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 4db29683-685f-39db-a49e-9fa3d388c2f2 | -16.88174 | -57.80886 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 112906a9-1e43-32fe-9680-a9deaaa2393c | -16.87847 | -57.80715 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.5 |
| 0c6c15fc-8e1b-374d-a558-9a911dc40fe4 | -16.87794 | -57.81323 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 1c9bad1e-2af2-3a85-a961-992abe912c7d | -16.87504 | -57.80812 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 633094ac-7bee-3121-845b-6168015fadd4 | -16.87447 | -57.81421 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 3ac6dec1-3805-3f79-b8f1-bd69b3b7de2e | -16.86166 | -57.80662 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 34529c75-639d-3949-945b-efd132770009 | -16.85995 | -57.82487 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 88691160-1d2d-3e87-9b8d-87ed2e6f4407 | -16.85497 | -57.80586 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| f7945ea3-c85d-3f20-bb17-1f626a32a72f | -16.8544 | -57.81195 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 9f0fbfda-1899-3715-a9e4-1d43d9f04dd9 | -16.85384 | -57.81803 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 6a8eabb4-fa73-3d1c-8a7e-a82e407e25f5 | -16.84771 | -57.81118 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 9f496e13-94dd-3995-b1f0-6570a91f8903 | -16.58325 | -57.73991 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 55af02a4-56d2-3ea4-abea-45f17b8bfc0b | -16.58007 | -57.73575 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 28fc763e-5af7-3a3d-81a5-f304b8d6df0b | -16.57654 | -57.73929 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 4034dba3-5a1b-3788-9387-2bc1a1a9eda7 | -16.57335 | -57.73526 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 44813750-307f-3757-acd5-3a2553a4642e | -16.57279 | -57.7411 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 4d4e0c5d-5642-399d-b7bc-d105ee36d618 | -16.56982 | -57.73873 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 82298bb5-2318-347a-870a-f52ba69e2280 | -16.9756 | -57.48293 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 8e1e40a5-07a6-3118-a625-b96cbf5065ef | -16.95456 | -57.48703 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 62c455f7-ade1-3f17-ae4c-b7ffe0544d9c | -16.95398 | -57.49346 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 2c110680-71dc-3fa4-9a3d-16994e7974c8 | -16.95341 | -57.49987 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 63e1396a-cbed-3560-a60f-6bd9d9e79640 | -16.95252 | -57.49492 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.6 |
| 6699a555-d159-33de-bae9-cf6d8122ac19 | -16.95191 | -57.50131 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.1 |
| 9ca1c36d-34d5-3dfa-a39b-56d5bf36a0af | -16.94773 | -57.48625 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| debd5d19-9526-3508-a9b3-52d26f5252ef | -16.94659 | -57.49909 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 8230bb94-c23d-3d06-9904-d1edd943581b | -16.94632 | -57.48774 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 9bd8ae91-529b-3504-b270-4ecd86651c40 | -16.94571 | -57.49415 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 4929bca7-9afd-3ab1-bf29-d1d8657af704 | -16.94147 | -57.47907 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 3e394265-b02c-3a3e-bb5a-2f822ca5e109 | -16.94034 | -57.49188 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 3ae147db-4b13-3517-9dc7-83806943de34 | -16.9401 | -57.48058 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| ee0ac93f-ca66-37ee-9236-f7695a656712 | -16.93978 | -57.49831 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 73c65f6d-e7e4-3b7b-b53e-f1aca8e57c4c | -16.93921 | -57.50471 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 3155d4ec-a0ab-3e43-b2ba-cd0c6ef1139b | -16.93828 | -57.4998 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 2953246e-816d-353e-aec0-ab35abdc327f | -16.93319 | -57.69655 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4f398069-d81c-3ec6-8f89-49bdcf071315 | -18.59944 | -57.26706 | 2024-10-09 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 82ba62f1-96d2-3a4f-8db1-08e2901d1d56 | -16.93296 | -57.49753 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| d47782ed-f88a-329c-9f0c-27b74e496d84 | -16.9324 | -57.50393 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| e0a9caaa-ea48-365e-89ce-9a8254753afd | -16.93087 | -57.50543 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 0d73bfa2-c540-3ea8-97e2-1869a02435ec | -16.92764 | -57.68335 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 599cb829-f35d-34d4-8e59-ac6205f142e9 | -16.92704 | -57.68958 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 94002e7e-1a6b-390b-a5a2-b105ee3126d3 | -16.9267 | -57.49035 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 42b748cb-3522-35e1-9a3a-46c573c38f4c | -16.92614 | -57.49675 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 9e71784a-768d-35d5-ae28-8ead6b6c4af7 | -16.92558 | -57.50315 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| d833ba5c-5a8f-35f2-8e28-29d0ade73df3 | -16.92525 | -57.4919 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 3a5e63db-8af6-3000-a75d-f2573f7b8fa6 | -16.92465 | -57.49829 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| dd948284-b1c0-3969-94aa-3641dcb5984e | -17.15234 | -56.82957 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| c8846155-86eb-32da-b4a1-36c7dae1b74d | -17.15171 | -56.83678 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 78a9180b-aa43-3cc8-a3cc-4ec7d77ac073 | -17.15109 | -56.84391 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 7e73d170-f0e9-3c53-a4ae-57bfe8a1882a | -17.14338 | -56.85026 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |


[Clique aqui para ver as próximas entradas](README217.md)
