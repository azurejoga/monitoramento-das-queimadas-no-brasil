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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2214965c-3e3c-3f66-bf84-6fb41437b394 | -8.43076 | -47.1175 | 2024-10-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 42c40a26-9cb9-3c7a-8073-b56435d64fb3 | -8.36237 | -47.53943 | 2024-10-04 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a4ad2d20-b321-34bb-8130-6e49ab82352a | -8.35822 | -47.53866 | 2024-10-04 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 43411ace-c1f6-37bf-9c2f-4657fe98621a | -8.35474 | -47.53405 | 2024-10-04 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ad31179f-99c9-3ae0-b225-b18084fbd2c6 | -9.80967 | -47.47298 | 2024-10-04 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b43bc0d3-b7f6-3a9c-a3b4-b2ecb4e2040d | -3.69723 | -47.61801 | 2024-10-04 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 41f98bf1-9478-39e3-8c7a-b93d5398e9f1 | -3.4644 | -47.65923 | 2024-10-04 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| deb237b8-2f92-38f0-9950-80ee4013b622 | -3.46367 | -47.66367 | 2024-10-04 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b9c380c5-d37f-3de5-b939-7b23df81d097 | -3.40977 | -47.58622 | 2024-10-04 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdb65621-d288-3348-82a6-f0820d1f1f57 | -3.40903 | -47.5908 | 2024-10-04 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb1e23c4-459d-33dd-9067-ac2d99daa6ec | -3.31731 | -49.04255 | 2024-10-04 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 905371a9-3d9a-3d5d-acf3-5195eb9c4b00 | -4.27836 | -48.06413 | 2024-10-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ade8fdb6-be70-3e23-8410-bb8a83f3259a | -4.19719 | -48.23515 | 2024-10-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3410fd6-1c20-357b-8941-221de9f98e71 | -4.19553 | -48.22754 | 2024-10-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 530f8daf-cedf-3cd3-8af9-69a5e20417c9 | -4.19419 | -48.22461 | 2024-10-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcb766c6-e18a-3c66-b053-367b99bb40f5 | -4.19335 | -48.22959 | 2024-10-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da2dde8f-cec2-3d59-840e-2dec4ba46ec7 | -4.1805 | -47.88755 | 2024-10-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e559cad0-cabc-3150-a0ea-8e2be487fc35 | -4.17971 | -47.89225 | 2024-10-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ecc8282d-c66b-33de-8269-5c9ba7094fb6 | -4.17594 | -47.8868 | 2024-10-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d9cfc567-3bf1-3b44-af5e-016868478eec | -4.14823 | -48.39931 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 815b795f-1a40-3d31-b595-54d6ca99b7b6 | -4.10463 | -48.48652 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa71f19d-2cca-37fc-85e7-3a043eb17e12 | -4.09986 | -48.48579 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d6ab396b-235d-33ad-a6d9-1c39e5997308 | -4.09597 | -48.47979 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b7510824-5010-3140-89c0-feccee02428c | -4.09509 | -48.48508 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b3f9e468-425f-3de3-a07c-36ffa22b0e01 | -4.09422 | -48.49033 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8341161f-0a37-33bf-9fa0-7d0f9c238b2d | -4.09292 | -48.46881 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72836704-e662-3d58-be97-3129b1e9851b | -4.09206 | -48.47398 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ae433c60-d134-34bf-b625-e84c99242205 | -4.09119 | -48.47916 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d1d3e1b6-aa63-31d2-ab30-e0b7ccafef62 | -4.09032 | -48.48437 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 213de363-4674-3b59-af02-b8195a5a6024 | -4.08945 | -48.4896 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 2c400dc6-2383-3c62-91e9-49ef2631aa5c | -4.08856 | -48.49489 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0a2bdaef-f6cf-33ab-8f49-ef8520eaaccf | -4.08815 | -48.46814 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70267b24-4515-3c02-8936-87c3a5887476 | -4.08728 | -48.47334 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0699b1ab-9bbc-3a2f-a575-d2825402339e | -4.08641 | -48.47853 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ce8ed101-4ea6-393b-9815-f7b7f0e48d7b | -4.08555 | -48.4837 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| b3f5dcd7-cba0-3bf4-a76a-5cfb68f4555a | -4.08468 | -48.4889 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| c22ddb88-5b30-346b-902f-a6c714dd0b03 | -4.0838 | -48.49415 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ed6b64a1-d145-3bd1-bf49-0f2e270ac90d | -4.08164 | -48.47784 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd1558da-007a-36b1-93fe-dbe14df53bea | -4.08077 | -48.48303 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 68781fdd-df98-31d6-9316-ea92329a79c5 | -4.0799 | -48.48822 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 8ef6c245-4b2f-3f42-a3cb-3a918a37c0f8 | -4.07903 | -48.49341 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dddeb040-9057-354d-9357-115d88f5b0eb | -4.02701 | -48.92279 | 2024-10-04 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2d408a62-24e8-31dc-9b9f-1dfcf907b3ee | -4.88202 | -48.98519 | 2024-10-04 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43025701-2f1e-3805-8afa-e6bbfaacb245 | -4.828 | -48.54831 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| becc3b33-e340-3fde-90cd-d687ec58698f | -4.80176 | -49.07309 | 2024-10-04 04:08:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71e2a18a-7db7-3b40-9812-97968c10ffef | -4.72413 | -48.84324 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ffd19bfb-c4ea-334b-9af6-ce6226330ea4 | -4.61263 | -48.0652 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46ee0353-9352-3c15-ac8b-d0d1ec89a56b | -4.57416 | -48.01427 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3c3f03b5-5627-30a9-a955-aa1c752805b4 | -4.57337 | -48.01897 | 2024-10-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0fcb09f5-5930-3024-a318-1b2436db781e | -5.50827 | -48.80711 | 2024-10-04 04:08:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3a426496-1e21-3721-b91e-f27e8f835ca4 | -5.50786 | -48.80479 | 2024-10-04 04:08:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1566889-ff57-3243-93cf-9222ef0fc71e | -5.50702 | -48.8099 | 2024-10-04 04:08:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dd177386-87c0-36e5-81e3-5c4d4364d35f | -5.50351 | -48.80635 | 2024-10-04 04:08:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99d466df-722d-30e7-a071-d58e1b3f1970 | -5.50262 | -48.81144 | 2024-10-04 04:08:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0879652e-9073-3b98-9b5f-467c32e7689f | -5.50226 | -48.80912 | 2024-10-04 04:08:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95fd793b-6782-3eae-b6e4-b7c0e0bd9701 | -5.45574 | -48.99961 | 2024-10-04 04:08:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1db3311b-0e5b-36d3-9d40-2b5c36838ed5 | -5.43809 | -48.89925 | 2024-10-04 04:08:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6c10ca08-0c11-39e0-9de5-8dfefafb26d5 | -5.4333 | -48.8985 | 2024-10-04 04:08:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cdf2ad6b-262f-3211-8b68-93a604d757a5 | -5.3026 | -48.11391 | 2024-10-04 04:08:00 | NOAA-21 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0147b5e1-c7a3-3226-bdeb-73b7f902e34f | -5.30198 | -48.1113 | 2024-10-04 04:08:00 | NOAA-21 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86a97c2c-e25b-32f8-9fa2-71b798140a33 | -5.79338 | -49.32589 | 2024-10-04 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eab00f3e-6033-3f45-b370-4115b515aae2 | -7.81933 | -49.45881 | 2024-10-04 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a7a3dca-9909-3f48-a8ad-af35084e8254 | -7.57089 | -49.41333 | 2024-10-04 04:08:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ddf75ac6-aaae-34d2-b190-b9f0d092aadc | -7.38201 | -49.62057 | 2024-10-04 04:08:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f79cdb35-1f72-3931-9ca7-be9375180b36 | -9.02913 | -49.81046 | 2024-10-04 04:08:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4ed028af-648e-355c-97d7-77979cfe0ff6 | -9.02433 | -49.80964 | 2024-10-04 04:08:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe73ff37-505d-318c-b13a-22079bee78f1 | -9.02337 | -49.81495 | 2024-10-04 04:08:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f4458da-8b65-33e5-ac1d-797b96a2a785 | -9.01858 | -49.81409 | 2024-10-04 04:08:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ae42e9b-7d44-31d6-80f2-a9ad78bfb51b | -9.01838 | -49.8175 | 2024-10-04 04:08:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0f4bf53e-126f-35d9-b80d-a178fd07c1b6 | -9.01762 | -49.81934 | 2024-10-04 04:08:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ad820228-aaf1-3cb9-a0d9-c07a99417c9d | -9.01359 | -49.81659 | 2024-10-04 04:08:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bf92b824-91b5-3ada-ba6e-343909f58872 | -9.01283 | -49.81845 | 2024-10-04 04:08:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 797c1fe7-82b7-3325-af0d-5cc3dba44a98 | -9.01267 | -49.82187 | 2024-10-04 04:08:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 18a3efe8-47c6-3a4b-a282-d3fe3258bb48 | -9.00973 | -49.81042 | 2024-10-04 04:08:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 860a3f05-5fa7-3ef0-b82b-5e9a9aa209c6 | -9.00901 | -49.81232 | 2024-10-04 04:08:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| db38d0c5-94b0-33cf-906a-6d4f208d48de | -8.91389 | -49.68541 | 2024-10-04 04:08:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 162f6568-6336-3187-a960-30b5a6dd3f8e | -8.91073 | -49.67221 | 2024-10-04 04:08:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 55a5eda2-f43d-3d90-bbf1-b4bce1b1f4cb | -8.89062 | -49.6473 | 2024-10-04 04:08:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5e455e9a-e11b-3f19-ae7f-a7eba371892b | -8.88618 | -49.70005 | 2024-10-04 04:08:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3ce69e8f-915a-36a7-aff7-abd2c584b9d1 | -8.88526 | -49.70528 | 2024-10-04 04:08:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8b284720-3a9f-3feb-8512-27b43c32a90b | -8.78017 | -49.94062 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1508dc82-34e4-38ae-a9a7-08c81c747779 | -8.76894 | -49.61136 | 2024-10-04 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| df795b0d-6317-32f8-8896-18a424b37f73 | -8.65736 | -50.03725 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 426bdab2-bcbd-3902-bac7-0b5fca7930d0 | -8.65532 | -50.04844 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 16fccf1e-7afc-35f0-9803-1636e6df0886 | -8.65431 | -50.05399 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5a39ad2-ee8b-3148-ad1d-88c19e0ca9d2 | -8.65425 | -50.04082 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6fa2ebd6-16a9-33ad-8464-faff2fd56f33 | -8.65328 | -50.04643 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| acca9ab4-7247-3b19-a65d-cacc78e3bfd4 | -8.65231 | -50.05199 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e66f9619-4cb7-381e-b891-f307d104d197 | -8.65144 | -50.04198 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 21d9a3ef-babb-3b0d-82f4-4e78e9cab252 | -8.65042 | -50.04757 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a339a43-1a6e-37a9-84a9-3dbcaa3b0ceb | -8.64941 | -50.0531 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 758e4794-bcc4-3e96-a7fa-18e3954cf434 | -8.6484 | -50.05865 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e398735f-9a7e-3463-b8d7-509788fa1437 | -8.64741 | -50.05109 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c2a5fcb5-27e6-32cf-94ef-26f75184cc05 | -8.64655 | -50.04111 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9e8955a8-eb24-3126-944f-a1b69662e82f | -8.64644 | -50.05664 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6a6e61a1-366e-3d89-a085-69aeaed5d52a | -8.64552 | -50.0467 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9dba4ef9-7457-3c39-be02-ba19d959ec7d | -8.64452 | -50.05221 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9ca51a2a-b7fb-3893-8531-e86a8d6b36ff | -8.64446 | -50.03906 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 915a7cf7-71f8-3646-a36b-1ee4e298cf6a | -8.64267 | -50.03466 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 10eee8cf-ac5e-334f-9e1b-b6e3935fb969 | -8.64252 | -50.05019 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README64.md)
