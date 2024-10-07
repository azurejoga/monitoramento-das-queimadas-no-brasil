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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 441a0c9a-af18-3f62-ad70-db6964478c03 | -16.8196 | -57.43525 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| 701a6180-4442-3397-92ea-1834c4d943a3 | -16.81893 | -57.43922 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| b7fd2b19-f5a3-3e20-a2de-247100188d76 | -16.81817 | -57.42271 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 88144caf-ca1f-3d7c-a364-9229066a9025 | -16.81749 | -57.42668 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 145.4 |
| 427079c5-c937-3f17-b643-b395ba96723e | -16.81682 | -57.43066 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 145.4 |
| c02ffe32-2ce5-3da3-b85f-e0239520b245 | -16.81614 | -57.43462 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| ee15332d-9ada-30a5-9390-4dc5aa543eaf | -16.81546 | -57.43859 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| b794ef77-9d65-36d3-bf8d-5c1a5bfbaa01 | -16.81403 | -57.42605 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.0 |
| d12d3cb2-f2f3-372c-b094-4a1cd38e4191 | -16.81335 | -57.43003 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.0 |
| be32512b-b311-3004-8496-6fae6979cb7d | -16.81268 | -57.43399 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.3 |
| 14bb72ab-0162-3877-9051-09a8fa399e87 | -16.812 | -57.43797 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.3 |
| 2948be78-c26e-344b-bf92-23c957735b4e | -16.81184 | -57.39705 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 3545c702-02eb-3b08-9af6-1698b33f967f | -16.81116 | -57.40101 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 52b1dc77-7aa2-3cd8-be89-3235fe5fa8be | -16.80989 | -57.4294 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.0 |
| 07543d19-a22f-3e99-b2ff-6e3ace6f1377 | -16.80921 | -57.43337 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.3 |
| 698d6ed7-a1f6-3271-a510-d9bc9ead539b | -16.80853 | -57.43734 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.3 |
| ebc1920e-f580-3fee-8b7b-aca3dab2771c | -16.8071 | -57.4248 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9a5c3c30-126d-30eb-a8db-33258be13d21 | -16.80643 | -57.42878 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e1cb116c-90bb-3670-a53d-1f962467dd35 | -16.80263 | -57.39631 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 12ab73f3-e745-3592-bc68-92d97171abed | -16.80131 | -57.40425 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 574f2bb5-f135-32b2-8689-79cbf0a9cb74 | -16.80079 | -57.39914 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 7e1350af-495b-3b3a-ae4e-a10795ec998c | -16.80011 | -57.4031 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| bf4de33a-a4e9-3218-9b65-012b3fe94176 | -16.79255 | -57.4354 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| fd4a7d36-ae6c-3d74-ad4f-675cd540867a | -16.79159 | -57.3984 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 755fd2a0-b6e3-3b9f-8a7d-7838ccf4f14c | -16.79093 | -57.40238 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 6b20e6b7-63fa-3b8b-8e3b-be334eb69077 | -16.7896 | -57.41032 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 5397601a-b3ec-35f2-a8ac-2263eb72cdcf | -16.78629 | -57.43018 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 4ee78ff6-0097-3765-95d9-1aa163682c12 | -16.78282 | -57.42955 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 0b9b2118-c381-3b80-b119-899267522329 | -16.78216 | -57.43353 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 5a068e4e-8c12-3c2f-b52c-41573f406eda | -16.77936 | -57.42892 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| ec03f229-8e9d-3b1c-811b-58cc34bf889e | -16.77869 | -57.4329 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 2b5e09b0-a665-3e19-9fd1-441cc52a6509 | -16.83837 | -57.45094 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| a80b1795-5461-3119-b091-8b737e565d5c | -16.83769 | -57.45492 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f8168f5a-d4f7-3c11-84ec-baab7ad1ba32 | -16.8349 | -57.45031 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 71ad0acb-a8bc-3588-9e76-630841543d79 | -16.83423 | -57.45429 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e646ddb3-db52-36fb-aabb-ea3ea4c3e4c9 | -16.83211 | -57.4457 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 8b9efd6b-d8e3-3a5c-a287-4baf46cfb4e1 | -16.83144 | -57.44968 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f0ad9990-8555-35c8-878e-49372b98aa78 | -16.82865 | -57.44507 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| e02c755a-0e16-31f1-b06a-bec43d0cd6a6 | -16.82797 | -57.44905 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 88830d0e-f449-313d-9897-4e21d668c2f5 | -16.8273 | -57.45303 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6a1463b3-7172-3122-b66e-173d0aa18804 | -16.82662 | -57.45701 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c3ab3358-b0ce-3fb8-8e91-f447a9e23338 | -16.82518 | -57.44445 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| a9e4fa5d-9226-35e0-96ba-6ade6d35ff60 | -16.82451 | -57.44843 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 88276bb9-5678-3b48-bdb4-87c738ce903c | -16.82383 | -57.45241 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8eb972b6-9e7f-3377-bb17-630664903399 | -16.82315 | -57.45638 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e6a66301-761b-3f9e-a186-40cff6e8289d | -16.82104 | -57.4478 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 9295c95b-f350-3efe-aee7-d22de59e0411 | -16.82052 | -57.49289 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7b37bc99-5dfe-3310-9b35-c0ff7894048f | -16.81985 | -57.49689 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0fddabf9-3fb4-3c25-b783-cddc47f101e9 | -16.81825 | -57.4432 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| fb8a9cf7-d04a-3eb2-9414-d1720717834c | -16.81758 | -57.44718 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| bb8a2b8c-80a9-3ccb-bf4e-bfa16662cf95 | -16.81705 | -57.49226 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 928039d1-b322-32f4-b9e2-38fece975ca3 | -16.81659 | -57.55822 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 441d649a-37b5-352d-90ec-a7280962f091 | -16.81479 | -57.44257 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 9a2de45b-f541-3fdc-a92a-d0a3d8bdc33a | -16.81132 | -57.44194 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 03157e0e-9285-3751-a482-59df173eae3f | -16.79263 | -57.44677 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 8e0a510d-a695-308a-810b-08ec0ae1828c | -16.79123 | -57.44336 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 75d77d3b-452e-3c13-ad1c-4ef811366dd3 | -16.79056 | -57.44735 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 9bf79e20-9409-38d2-9d91-42bf85aa667b | -16.78871 | -57.47989 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 862cdc56-54b0-371a-9360-5a4b284e2ad2 | -16.78776 | -57.44274 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 8f875e84-cb8f-3124-a18f-e605a7161136 | -16.78717 | -57.47865 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 797a760c-33fe-3172-b3a9-1ae0eb26921e | -16.78709 | -57.44672 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 68f2f36b-089e-3e76-bc0c-070f2553ae5e | -16.78523 | -57.47927 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 9fe60190-6d7b-3f8f-a413-11422ef40564 | -16.78363 | -57.4461 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| abb7a6e2-b931-37c6-ab5e-951d929aee09 | -16.78016 | -57.44547 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 15d81e73-57fa-3e4c-a050-13a5679228b3 | -16.77883 | -57.45343 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 6eb8a17f-b924-39bb-b9bb-85f467830970 | -16.77816 | -57.45742 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 797133b3-0b5c-31fa-aff3-62d5518770df | -16.77775 | -57.50261 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 3da663b0-6408-39bc-9262-83e7357d81c7 | -16.77749 | -57.4614 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1cf568d2-9323-3d20-9b54-97f63d0247b8 | -16.77482 | -57.47738 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| e2d8b8b7-d2dd-3fde-9e14-3cfc4667a62e | -16.77428 | -57.50199 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| c13125d1-b134-3f77-802c-fbb82d4bb95a | -16.77415 | -57.48136 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 1e3288cd-0cad-3de7-96c7-e240dbacec85 | -16.77402 | -57.46078 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c1f28131-b281-32b5-a593-b18ee994caa3 | -16.77269 | -57.46876 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 8e9b2e99-8e07-3f9a-9224-bbf08272a816 | -16.77147 | -57.49736 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 575a3916-2211-353e-8204-56000ddf49df | -16.77135 | -57.47675 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 534bbaaa-cc67-329e-9ac5-8d72bdaafc42 | -16.7708 | -57.50135 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 1239b96d-cb1c-3b37-a9bb-151d6e05a134 | -16.77068 | -57.48074 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 4a09634a-1c1f-3b3e-8a01-c6f2964270a4 | -16.77001 | -57.48472 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| ce93b17c-2e0b-36a0-8758-b33b849a1257 | -16.76922 | -57.46813 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| cd9b109e-b6d7-3dde-8fc7-a289faf7b986 | -16.76867 | -57.49273 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 383179d2-95dd-327d-bff4-4c65e7124d8e | -16.768 | -57.49672 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 8c9558eb-644a-38ed-84ef-2aa68013bd33 | -16.76733 | -57.50072 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| f92e3858-fbc8-34e0-b1e5-11ff9395e9ed | -16.76721 | -57.48011 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 647f00ff-cc08-386e-8aee-7c91ac733d69 | -16.76452 | -57.49609 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| a8a08723-a09d-3f8e-a112-012ff830fc52 | -16.76385 | -57.5001 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 91008ce4-181f-3bf2-9815-be6f72903546 | -16.76228 | -57.46688 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e3c50e79-91b1-341c-bc7d-79153fd9d6b7 | -17.11389 | -56.83236 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| af9f18e3-4278-3743-86af-13bbb1f24032 | -17.1136 | -56.84011 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.0 |
| becbbd7f-d8df-3d69-b4f4-7acff1b8d406 | -17.11264 | -56.83995 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 53377854-013b-30fd-9ebb-bba82cf67e3a | -17.1105 | -56.83175 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e2154c4f-bdae-3b27-b20c-5602b62b861f | -17.10988 | -56.83555 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c2a56beb-45bd-3029-9924-46e5eeaf495d | -17.10925 | -56.83934 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 9162cc13-35dc-3eca-86a3-2245a106804b | -17.10863 | -56.84314 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| d41ecf85-5884-3f35-851a-9ad360d083ba | -17.10711 | -56.83115 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| d0c567f8-1346-36a4-bedd-02d3dad5302d | -17.10649 | -56.83494 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 985a69d7-991f-36c6-bcbe-f742209df399 | -17.10587 | -56.83873 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| a1b243f3-83cb-348e-891c-3d338a64cb0c | -17.10524 | -56.84253 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| f5d5ac88-3e4d-31eb-bad4-211af76b38f0 | -17.10373 | -56.83054 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| c7afbb48-bd98-3d59-ab96-43fb1bb95c95 | -17.1031 | -56.83434 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 5d3fab28-7e68-3ed3-b24c-b1728b8c3d19 | -17.10248 | -56.83813 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |


[Clique aqui para ver as próximas entradas](README105.md)
