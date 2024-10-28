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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f645d379-6942-3396-892d-29e220d7c325 | -3.67392 | -50.30161 | 2024-10-28 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0da0dd4c-c2e5-37db-9ac6-96eff392e514 | -3.66965 | -50.29384 | 2024-10-28 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61d9c5b3-780d-3af1-9d78-be8e1b7e7c7d | -3.66907 | -50.29729 | 2024-10-28 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 033d737d-2e72-31eb-aed0-25ebccc17953 | -3.66849 | -50.30076 | 2024-10-28 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 461751d6-f358-303e-aee2-403ddde8b305 | -3.65396 | -50.15668 | 2024-10-28 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d7078bd1-0dae-38c3-8405-fc258c9d6b4f | -3.65339 | -50.16004 | 2024-10-28 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 84f0ced7-7714-3e1e-bed9-1dc91f0fafbc | -3.64858 | -50.15589 | 2024-10-28 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2adb6311-a5bf-394b-be67-9243ed0ab8a0 | -3.64802 | -50.15919 | 2024-10-28 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 43ada5ef-393f-3ba4-941b-778c4077686c | -3.62244 | -50.17955 | 2024-10-28 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94bc1fb8-1e06-3634-9def-37de2f672fad | -3.61997 | -50.17936 | 2024-10-28 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ed9abf0-117c-328f-8f85-ca4abe921cd7 | -3.61941 | -50.18279 | 2024-10-28 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1786adf7-757d-33d1-9d9c-97c46d6ef4d1 | -3.61705 | -50.17873 | 2024-10-28 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 040f5bde-f26d-3f7c-b5aa-ef7ca6e4532f | -3.61647 | -50.18212 | 2024-10-28 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3648e8c-5ffd-3eb0-84a8-e651b4b4a764 | -3.61403 | -50.1819 | 2024-10-28 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40b961f7-9aee-36ec-9a28-42b8f7d3ac28 | -4.84789 | -49.94644 | 2024-10-28 04:06:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9a53306d-db4d-3c1c-b29b-e4f138bd920d | -4.84417 | -49.94396 | 2024-10-28 04:06:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa2c85d6-5796-3def-b40c-e323d1ea728f | -4.84363 | -49.94707 | 2024-10-28 04:06:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2793f77-5ce6-3c93-a313-9e54a93dd9b9 | -4.84271 | -49.94553 | 2024-10-28 04:06:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d8ef070-47bd-336e-8689-0a1093f9abec | -4.76984 | -49.45666 | 2024-10-28 04:06:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6a1808f-597e-3e1d-901c-7664c06082ca | -4.7341 | -49.39406 | 2024-10-28 04:06:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2589a3f5-4ecf-33c4-89b8-a519aeedeb2c | -4.7336 | -49.39696 | 2024-10-28 04:06:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8808cd4c-1fde-3535-b9a1-f843e1c871d1 | -4.72912 | -49.39309 | 2024-10-28 04:06:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9fdcbca0-4acd-33b7-9873-0b3537de6db8 | -4.72903 | -49.39419 | 2024-10-28 04:06:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bf8fd60d-2420-3bee-bbe8-7499a7cbcf24 | -4.72863 | -49.3959 | 2024-10-28 04:06:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa7a4141-ca4e-34be-8845-a7b4f6d4e718 | -4.72855 | -49.39709 | 2024-10-28 04:06:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 919e0c94-96f0-3d77-991e-10fc6e1e91cd | -4.72401 | -49.39339 | 2024-10-28 04:06:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b3f5bc3d-e9a9-3a80-a212-270b65b70b67 | -4.72361 | -49.39512 | 2024-10-28 04:06:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b114c91-c0d3-3506-87e5-85826a68d874 | -4.72354 | -49.39624 | 2024-10-28 04:06:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0d714b3a-744c-3cc8-8f8c-15b0d65c314a | -4.70225 | -49.60883 | 2024-10-28 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dcf3cb68-e44d-3318-bf1f-4551af50b3fb | -4.39116 | -49.75008 | 2024-10-28 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbce5441-14c8-3bc7-b118-d3f008be6639 | -4.39066 | -49.75307 | 2024-10-28 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e14974c-fe53-352f-8eac-31e7dcf46fbc | -4.3896 | -49.75933 | 2024-10-28 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe3e3272-c892-3322-98fb-3ec06db2cba4 | -4.38498 | -49.75526 | 2024-10-28 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edac0b32-cbb0-39b7-8942-47f9f173cff3 | -4.38444 | -49.75844 | 2024-10-28 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 570c2052-fbac-3b86-86cc-a30d29bd5df9 | -4.28125 | -49.40002 | 2024-10-28 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ec7df17-ccb7-33a3-93b7-c38a59130037 | -4.28077 | -49.4029 | 2024-10-28 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28e3d8b3-433c-39aa-99cf-e05d7866f31d | -4.11384 | -49.26217 | 2024-10-28 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68758114-c96c-3172-a522-5da5c3ec31c5 | -4.11334 | -49.26511 | 2024-10-28 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e183a33b-0264-3979-9fde-061e503c3b5b | -4.10883 | -49.26128 | 2024-10-28 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4eee80f4-86fc-34a1-8c0e-4793314090c9 | -4.10834 | -49.26418 | 2024-10-28 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c6571ba-d5fc-323b-a35c-d92fd605fc73 | -4.10784 | -49.26707 | 2024-10-28 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b54eb6e6-2bc0-3cce-9c46-e1aa700035ba | -4.0706 | -50.02343 | 2024-10-28 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38484401-09aa-3192-81f1-e3b86fc7b699 | -4.0696 | -50.02339 | 2024-10-28 04:06:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 42b373fd-70aa-3b8e-a6f5-c819a6ddcda0 | -4.06953 | -50.0299 | 2024-10-28 04:06:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e04eed1b-8dcd-3485-8779-6625ee030862 | -4.06905 | -50.02661 | 2024-10-28 04:06:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c76f8bed-7432-3aa2-8806-170cf190d40d | -4.06899 | -50.03315 | 2024-10-28 04:06:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20c0ae93-d07e-34ff-828d-4c5511a30e1d | -4.06849 | -50.02983 | 2024-10-28 04:06:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4582afb5-6402-36d8-9c51-539b7e121689 | -4.06792 | -50.03309 | 2024-10-28 04:06:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34a43358-c86e-3d41-a8b0-8191d0dc692b | -4.06535 | -50.02237 | 2024-10-28 04:06:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3cd1521f-1f6c-3cb9-a928-4114963f1fac | -4.06481 | -50.02557 | 2024-10-28 04:06:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d44caab-aaa3-3955-8d54-74fdc1a3fa94 | -4.06428 | -50.02878 | 2024-10-28 04:06:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d9179d4-e605-3cb3-b9f7-2c5e1972c5f5 | -4.06374 | -50.03204 | 2024-10-28 04:06:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9d42696d-6422-322e-9e47-e035e151f409 | -4.05955 | -50.02455 | 2024-10-28 04:06:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00975fbc-9fe7-396c-bf1c-27412c02d7da | -5.60835 | -50.13903 | 2024-10-28 04:06:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ba47015f-7b4e-3836-9f25-d8d016e59d19 | -5.60782 | -50.14212 | 2024-10-28 04:06:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a450d7f0-1ec2-3a54-963b-a551bb4c8db3 | -5.177 | -49.98353 | 2024-10-28 04:06:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1157d449-738d-32b0-98be-89508d9269f5 | -5.17129 | -49.98575 | 2024-10-28 04:06:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbdcd298-49d2-3ff3-8ec1-65727744a531 | -3.33665 | -50.75822 | 2024-10-28 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bdab0c52-23e1-3bcf-97c2-ff0a188c9206 | -3.33041 | -50.76098 | 2024-10-28 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 804a068d-f5aa-3bac-a8cb-194c737649fa | -3.92886 | -52.12342 | 2024-10-28 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9fc2d68-a1e5-3932-ad69-2c301ecc825c | -3.9228 | -52.12238 | 2024-10-28 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fefae254-7ae7-322d-b5b8-d60b09e75930 | -3.92203 | -52.12693 | 2024-10-28 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54cf6ec6-3140-3138-82e0-7c5ea7045a3d | -4.53196 | -50.98866 | 2024-10-28 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0445d6d6-1425-3593-a186-cd5d59861d92 | -4.52636 | -50.98781 | 2024-10-28 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dea5a42a-aa47-312e-bf2d-00d95adb52a4 | -4.47346 | -50.99414 | 2024-10-28 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 054d3e5e-45ce-360c-9382-08910cb2c163 | -4.47281 | -50.9979 | 2024-10-28 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 572dbb6b-2ad0-3c54-a147-82100980ce6f | -4.47216 | -51.00161 | 2024-10-28 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4739f3dd-3f28-3487-aa9c-343cfc60e670 | -4.46657 | -51.00064 | 2024-10-28 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2a7486d-710c-3615-8025-845ac2fc5157 | -3.85641 | -51.69963 | 2024-10-28 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97da397d-40fb-34f9-8190-736c0ba1447d | -3.85568 | -51.7039 | 2024-10-28 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b53be9f-85f4-3c51-b0c1-5bcb1de59482 | -3.85495 | -51.70818 | 2024-10-28 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5506873a-f8fb-3676-a0d1-10b54c4bfd08 | -3.79644 | -51.38669 | 2024-10-28 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 564737b9-d091-3918-acbc-c34d887063b0 | -3.79144 | -51.38098 | 2024-10-28 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd2b9453-04ad-3a91-9475-8e609ece52b3 | -3.6837 | -51.56034 | 2024-10-28 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a8850b60-82a1-3220-9f5f-9ac1ec116866 | -3.683 | -51.56452 | 2024-10-28 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4b96abeb-c515-3fb9-85fb-179a8ea80ef5 | -3.67711 | -51.56357 | 2024-10-28 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 72c61f82-9070-3f79-a74b-60dc31f8918b | -6.12491 | -52.16439 | 2024-10-28 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 707a52ff-7d41-3e57-8ffe-47ad47179c5d | -6.1242 | -52.16839 | 2024-10-28 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 95c53a34-b5d3-3161-95cd-0acbc89ad904 | -2.98168 | -53.27127 | 2024-10-28 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1225037e-b3b1-3a69-a468-53ecee56dbd8 | -2.98037 | -53.26736 | 2024-10-28 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2a02c50-fd54-3d69-82e5-2cc3af07f326 | -2.97935 | -53.27319 | 2024-10-28 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e109b15-5f82-3dcc-848d-721ba34bec68 | -2.97512 | -53.26987 | 2024-10-28 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5eacb400-5f96-3ec6-a38a-c29e2a8843d8 | -2.96638 | -53.04251 | 2024-10-28 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01512a28-5c08-3052-81d8-d6e3ac3addd3 | -2.9654 | -53.04821 | 2024-10-28 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3580aae2-e580-3aa0-9881-0b05894c7b9a | -2.86466 | -53.3348 | 2024-10-28 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ca7eb45b-b60c-3905-bea4-2f30656f1734 | -2.86372 | -53.34042 | 2024-10-28 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2c487a4b-ca57-3dd8-83a8-85671c8029b7 | -2.86274 | -53.34628 | 2024-10-28 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1407a37b-09d6-31fa-8c5b-5424936b5b8a | -2.8623 | -53.33192 | 2024-10-28 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5198175d-fd65-3144-b8eb-8e7836d0e976 | -2.86132 | -53.33751 | 2024-10-28 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c926c135-73d5-3014-a6f3-71f4aa8eaf93 | -2.86032 | -53.34328 | 2024-10-28 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c88450b4-7cf9-3e90-be16-d93e1e109482 | -2.85808 | -53.3333 | 2024-10-28 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 80d0ec2c-cbc7-3461-8dee-0c8e853ace25 | -2.85712 | -53.33902 | 2024-10-28 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e793bd1-25cb-3d3a-a9a0-2d5d0d6a67f9 | -2.8547 | -53.33626 | 2024-10-28 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 40dcb2d5-bd01-30cc-be31-26199d7081b6 | -2.85146 | -53.33204 | 2024-10-28 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c94ccc60-bc71-38e3-9681-26454c73b73f | -2.84907 | -53.32937 | 2024-10-28 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8296f7d3-6009-321f-8754-f2be38fa4942 | -2.84806 | -53.33515 | 2024-10-28 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 92300301-4f37-3a5f-ab7d-6c64da1d60f9 | -2.84482 | -53.3309 | 2024-10-28 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78e0a742-1890-3ecc-8902-fed0b056ad90 | -2.84384 | -53.33669 | 2024-10-28 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 745d8975-b76f-3fc5-9bb7-0c85a96d3db6 | -2.83818 | -53.32976 | 2024-10-28 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c81c4a03-b393-3477-86e7-04aa996ac597 | -4.0429 | -53.41862 | 2024-10-28 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README44.md)
