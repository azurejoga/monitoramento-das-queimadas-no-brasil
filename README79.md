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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18595a33-64e5-3d6b-95e1-8e0b4cfa8962 | -4.70188 | -47.96188 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e159a88e-48d9-3867-a3fb-f30ff52b41e4 | -4.70156 | -47.96282 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10ea2437-63f8-381b-990d-693f2403c51b | -4.58075 | -48.01759 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| e9fd9323-d38b-3b22-bf78-1c7644737e60 | -4.57954 | -48.0254 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 7e316b8f-41e3-3078-97f3-cd55f10ba353 | -4.57893 | -48.0293 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 54aa0a58-93f6-3bb6-b179-86211c1bdf6c | -4.57603 | -48.02487 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| e6e6bef0-5012-385c-b685-5100fcb6c58d | -4.57542 | -48.02876 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 8b6a9682-82a8-3720-bfb2-9809c03b168c | -4.57482 | -48.03263 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b5ad23a2-56a1-3c7d-9a0c-e96210827e05 | -4.57252 | -48.02433 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 5e932bb0-dde5-33eb-87ff-bb0d4117403a | -4.57191 | -48.02822 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 73381405-6373-3e32-a35e-84f53c24142b | -4.57131 | -48.03207 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 3879846e-4863-388c-96d9-1ce8d96e5732 | -4.56961 | -48.01989 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 69349f84-0299-3f8f-8d9a-9d171875704c | -4.56901 | -48.02378 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| ccf52d62-fb60-3c7f-ad0d-3090a02fe162 | -4.5684 | -48.02766 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 98f9eb39-2256-38fc-8b16-e6cadcc0b8ae | -4.56781 | -48.03153 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 513818a7-5710-312f-b074-062e8a961e9b | -4.49681 | -47.85996 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c9650ef-e482-3aa0-acad-0564fe310e13 | -4.48569 | -48.12278 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 073139e5-e14b-3bfa-909b-4f13984b00d7 | -4.46915 | -47.85164 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 213f65d8-1ac6-3cd5-9449-aaeca765b606 | -4.20868 | -48.03955 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df5eb3f8-b48c-3135-908a-0b76a5ffab66 | -4.2075 | -48.04724 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0037773-e43f-38a2-b9f3-7613360ec845 | -4.20459 | -48.0429 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91c249c3-2eb4-3cda-a634-4efa7e4d9e51 | -4.204 | -48.04674 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9abbec12-d807-3fae-828c-7f9e4a10899a | -4.20341 | -48.05053 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 815160f1-a3c4-3eda-a510-f3a386a261a3 | -4.20109 | -48.04239 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57f36aec-02d2-3747-96c6-7c0bc7db0197 | -4.19076 | -47.99295 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f0ea3f5-a737-301d-afe2-47fee212ce8e | -4.18885 | -48.05222 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90e8bbf8-c0b7-3fd0-99ad-13b3b74d5d4a | -4.18826 | -48.05606 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1530f04-7ea8-3f1d-8e11-5ab62f1c0321 | -4.0487 | -48.11833 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d19937e-716b-3266-b41c-9c512f6c1d19 | -4.04699 | -48.10615 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d94cbb54-93e5-37f9-a801-b63f8d9a6b8a | -4.87395 | -48.56221 | 2024-10-26 04:44:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e620d3a-2a70-37c8-8737-bac6383ef4bc | -4.84123 | -48.61492 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 29fba637-bb6e-344e-81bf-cf4342218493 | -4.84066 | -48.61864 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a41d68d4-2f53-3ad1-9051-ae5272b334cd | -4.83723 | -48.61811 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d0e3358-0370-34d1-a8a8-b6c827292962 | -4.51799 | -48.21466 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 69fa5a52-53c1-3e16-917c-445b5a0ed7b0 | -4.51392 | -48.21798 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86a05c6c-b4b6-3b44-a877-0c0dc7609495 | -4.51043 | -48.21746 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adc662c2-433c-3e90-9bfd-234415b46b88 | -4.50984 | -48.2213 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7422622e-e74d-3eee-b24a-bb551d80c648 | -4.50636 | -48.22078 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4f21fde3-675f-3b2e-8360-bb7edd48284b | -4.48956 | -48.21424 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46ba6c9c-4816-3811-9c57-aa936c3d13bb | -4.36082 | -48.59717 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 408e808b-e82a-3f50-898a-ebf329ee133c | -4.34423 | -48.61372 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90b7aa7a-1808-304e-a6b2-7bd460f1f8b2 | -4.34135 | -48.6323 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 811a39e5-54d8-3a5f-b180-93cbab9b7e8e | -4.33678 | -48.63917 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9414f51-c706-3467-9291-715dfee04e0e | -4.33337 | -48.63863 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c24a06d-04b9-39b3-a5ba-42700a4baf4c | -4.32995 | -48.63808 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d07e522f-c29b-3d9c-9b6a-a6eb9041b583 | -4.24825 | -48.5541 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1d81bd7-7710-3c97-882b-73a5abd1de93 | -4.24541 | -48.54984 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ab6800b-36ad-346a-8adf-016b109b3557 | -4.24198 | -48.5493 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98b53f44-731e-3339-abea-ad3a816bc939 | -4.2414 | -48.55304 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da74db27-59f1-36c3-b00d-71c2881e8892 | -4.24082 | -48.55677 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e1f86ee-0f67-3395-8860-274911a1df34 | -4.23797 | -48.55251 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7f15a49-6244-36b7-8811-8bb6e4692e07 | -4.2374 | -48.55625 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ff84701-63cc-3eeb-8c76-9a5a5ef6339d | -4.21855 | -48.56476 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ab789ef-bc85-3aa1-a5f7-112bd5c28a03 | -4.17117 | -48.59967 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e856e6b-dff0-3a89-af79-61cf53ace1d3 | -4.13562 | -48.28364 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3c67738-406f-3a75-b8b0-f9fcff3d03c9 | -4.13317 | -48.41466 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e1fe7a3-6dfa-33d4-a218-6852ef5aa60d | -4.09821 | -48.50493 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 138e6fb9-598b-36ed-8abe-6f7ebb03c6ad | -4.09817 | -48.23541 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 14c2e19e-55d4-3a75-afa1-eba82b682a5b | -4.09757 | -48.23925 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4bd7bc28-5b02-3783-8a1c-d943698437b1 | -4.09411 | -48.23869 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 97ec2d52-56a9-3585-b9e3-eb9c432d02d3 | -4.07333 | -48.23551 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46bafa99-7628-38ae-a97d-ebc669338c76 | -4.07214 | -48.24319 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1c73684-b6c8-3e87-8e69-9425d78b9f22 | -4.07084 | -48.29734 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5f5ae0c-3bc5-34a8-9daf-8a55e2d62d0b | -4.06868 | -48.24264 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a436759-0475-317b-bb53-d37893ca2f45 | -4.06798 | -48.29301 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4ba989b6-27ef-3f3b-84c3-e3746e0c20ac | -4.06739 | -48.29678 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8aee21ea-28ca-3135-8eae-1f922dd2c1b6 | -4.06633 | -48.25787 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8dce8de-87f5-3acb-a88f-10deea6a0e62 | -4.06463 | -48.24593 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c76c45f3-55d2-3258-b5bb-bb38c279efa6 | -4.06287 | -48.25734 | 2024-10-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d45967a-87b3-3256-a08b-64ba69f5830d | -5.30041 | -49.49744 | 2024-10-26 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03a8c9be-0b5c-3cfe-b101-24758ce5acdb | -6.4154 | -49.59066 | 2024-10-26 04:44:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 480892eb-9625-3845-ab2b-ffc197f206ea | -5.65928 | -49.10468 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e170f527-ef7d-3e7c-a12f-1bdaab6eb25c | -5.21619 | -48.22009 | 2024-10-26 04:44:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 547b6983-c453-3e1c-a324-bda8647a563f | -5.2156 | -48.224 | 2024-10-26 04:44:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c54c674-3eff-39c3-bbc0-b5ad5f5f2c4d | -5.21269 | -48.21956 | 2024-10-26 04:44:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc836212-965a-3c91-b725-108f39d50be7 | -5.2121 | -48.22346 | 2024-10-26 04:44:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e9a171f-1308-3e99-83a1-902337a58a1c | -5.20859 | -48.22293 | 2024-10-26 04:44:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 573005d6-69c3-39af-ac41-7432a3cf7fbe | -5.20747 | -48.22328 | 2024-10-26 04:44:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4aca1ff4-a729-3d8c-a977-d5ffe9948c43 | -5.51131 | -48.08517 | 2024-10-26 04:44:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 270a61bf-b0fd-3891-a4e9-905bac86ebeb | -5.71035 | -49.29916 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 086cfa52-e260-31c9-8fd2-0c63eeee5b93 | -5.65871 | -49.10836 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| daa204b8-31d7-316e-a763-0428eb84d69e | -5.51225 | -49.28745 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| faf40129-4d4d-35a6-bcfe-d9e42c445a09 | -5.49581 | -49.50563 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13915f64-dec4-3897-929c-05fef6d16aa5 | -5.49415 | -48.94797 | 2024-10-26 04:44:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec4a50b8-24d8-34f1-9459-fe122837c252 | -5.22379 | -47.95476 | 2024-10-26 04:44:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d9bfda5-2832-3da7-8362-fe897759e8b3 | -7.72546 | -49.54229 | 2024-10-26 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b85fb572-c6d6-3739-8bdc-bc107dffa27e | -7.80721 | -49.25684 | 2024-10-26 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fd53024-4081-382f-8702-5925baefcb60 | -7.80664 | -49.2606 | 2024-10-26 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b71893db-45d3-39f0-a790-22c066dd09c5 | -7.60352 | -49.3989 | 2024-10-26 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0cc957dc-ed8c-3728-9e76-5734adf8bb42 | -7.55807 | -49.53604 | 2024-10-26 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fbecf9b-2f9b-3ffb-a23d-ff34f8db4770 | -7.13808 | -49.51052 | 2024-10-26 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 788c8efc-0b23-3c1a-90a1-640e9489c46f | -7.13614 | -49.27233 | 2024-10-26 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68aa30a8-058d-3d64-a36b-23e5026590f3 | -7.11867 | -49.13623 | 2024-10-26 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 17cda8e8-3991-3db4-996a-66f78732b835 | -7.11523 | -49.13572 | 2024-10-26 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f331597-4bac-3dc3-b86c-98e7ec61b8c6 | -7.11289 | -49.1737 | 2024-10-26 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29b6440e-350d-312c-9bdd-f8cbb01d141f | -7.11231 | -49.17743 | 2024-10-26 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1cad490b-a3f7-3b2b-82e8-22ea4a19674d | -7.09976 | -49.14489 | 2024-10-26 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c63bd9b-a9f1-3559-8541-6715c7ed60ab | -7.09289 | -49.14384 | 2024-10-26 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09c66de6-6461-3ba0-bf7f-67fbf6676181 | -7.0906 | -49.13583 | 2024-10-26 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5135082-0816-3d43-8b7a-5e20edd29981 | -7.08888 | -49.14704 | 2024-10-26 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README80.md)
