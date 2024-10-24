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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00f18335-40e4-31fd-b476-0d29fd4267ac | -13.00578 | -48.89063 | 2024-10-24 01:24:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 08d5f1c9-1a9f-3451-955d-aaf8027852d0 | -12.96208 | -48.88611 | 2024-10-24 01:24:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5533645c-8097-3e75-89b9-ff0ca303c33d | -12.95932 | -48.86872 | 2024-10-24 01:24:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 7136ce1f-45c4-35aa-bd06-69872159cfc4 | -12.95514 | -48.88161 | 2024-10-24 01:24:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 4217fe0b-71bd-30e6-a0f3-9578539a6fdc | -12.95222 | -48.86415 | 2024-10-24 01:24:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| caf9bb60-6326-315f-8314-2296d2ff7210 | -12.68741 | -43.87284 | 2024-10-24 01:24:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 85815890-a754-3885-9242-40ac6ae7068f | -12.68701 | -43.86571 | 2024-10-24 01:24:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 3d974e1a-6db4-3b43-bb21-eb8aa10151f1 | -12.67953 | -43.83006 | 2024-10-24 01:24:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| efeef7e0-f46f-365c-91ec-d8fa3127819c | -12.67885 | -43.82297 | 2024-10-24 01:24:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 4ae2c640-6a58-3744-93f0-49db5f8c86ca | -9.37554 | -51.88956 | 2024-10-24 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 13161885-3b41-3ad1-a63e-416c73fd764d | -9.37368 | -51.87738 | 2024-10-24 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5d9cb701-2bf2-3064-846c-1e77de916bf5 | -9.20764 | -47.95717 | 2024-10-24 01:24:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 62f86fef-65a6-35a1-85a9-53df48fe2e2b | -8.57365 | -49.21886 | 2024-10-24 01:24:00 | TERRA_M-M | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 8684970c-bd60-3ee5-996b-02bf38e5d898 | -8.5736 | -49.22454 | 2024-10-24 01:24:00 | TERRA_M-M | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| e7aa77e7-54c4-3f06-80ea-160adbe27d75 | -8.38678 | -49.96362 | 2024-10-24 01:24:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| c0784288-f49f-3596-a319-42c9a892a142 | -8.3078 | -55.11328 | 2024-10-24 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4cfb171d-7f1a-3810-9253-6644d43ba152 | -8.30654 | -55.10435 | 2024-10-24 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e42608cc-7efa-33fc-a855-7a923f867adc | -8.06425 | -48.90412 | 2024-10-24 01:24:00 | TERRA_M-M | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 20.1 |
| a77b1a00-36ca-3930-abbf-d6b42d19316d | -7.99299 | -50.6926 | 2024-10-24 01:24:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| f5c5ad8f-72e9-3476-9d3d-a4950ef5bda9 | -7.99104 | -50.68639 | 2024-10-24 01:24:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| cfb9574d-4929-3615-a381-63b548f1f708 | -17.79639 | -57.51954 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.6 |
| 19b5ca02-c508-3395-b188-276fdf23e068 | -17.76493 | -57.49007 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.8 |
| cfc01d3c-4557-317a-acb6-0e046408bc9b | -17.7609 | -57.54393 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| bffe629b-7760-3b56-82b3-d1b99d85e901 | -17.7529 | -57.47839 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| 39acef78-eb02-3186-bc28-31e0af1b4e1d | -17.73362 | -57.4942 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 7d08ffeb-620e-3db1-bf40-12ce685f397d | -17.7112 | -57.48391 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.0 |
| ca0bfac5-b1ef-3f1b-a137-f674b47378c2 | -17.70965 | -57.47088 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 65178d99-c662-3179-a8ea-0a7fb41d2e11 | -17.70078 | -57.48529 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| e49d50c2-8fdd-3534-a3eb-1c6e9c8dbe67 | -17.69729 | -57.36757 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 51be69e6-0743-3343-b564-ec21b2610257 | -17.68274 | -57.48022 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.1 |
| 3665e3f0-9e44-3e5c-923e-200f37a1c842 | -17.68113 | -57.46723 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.3 |
| ad366930-b8dc-3d00-aeaa-926ac3b65ad9 | -17.67841 | -57.47503 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.0 |
| 976c59a3-9090-3133-8f8f-37618868b056 | -17.67688 | -57.46202 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 999e821e-59d3-34fa-99fe-fcadd94c7967 | -17.66752 | -57.44268 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 5e2986a3-92a1-37f7-b9cc-d1c9c767edc1 | -17.30091 | -57.29049 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| a8c8da1b-03f6-3f76-9fbd-152c0eaad733 | -17.28772 | -57.26692 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 85fecb14-2378-3c1a-ac73-a85457307227 | -17.2831 | -57.29853 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 17adeef3-df74-329f-9455-3c0141074aae | -17.27999 | -57.27361 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 086c048c-7c79-38bf-b927-f5374feda506 | -17.27287 | -57.29989 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| cb2fb541-ebc0-37d1-b3d7-4d6ec540b444 | -17.27133 | -57.28742 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 030acf8a-5f58-3f0d-b512-a2c13807a8c2 | -17.26978 | -57.27497 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 54689653-daf9-3496-96e5-bfe08282dfcd | -17.26516 | -57.23776 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.9 |
| e3f11af8-d9bd-3238-919c-761de207e3e0 | -17.25651 | -57.25151 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| d1279b48-2616-3605-8119-38935f01c9ba | -17.25498 | -57.23913 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 679b9a4c-4d64-3a81-b6f3-6b7faafb717f | -17.24632 | -57.25287 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.8 |
| e06900f4-917a-352a-a192-8bdd8895cfca | -17.2448 | -57.24049 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.5 |
| 92bbeefb-2e1e-3cd3-bd04-d1cbe8ba2e08 | -17.23613 | -57.25424 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.2 |
| f7372f4b-cf78-32bd-81bf-f6c0d90dc674 | -17.23462 | -57.24186 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| b91e6c0e-b424-39e2-998e-03ccaa57f577 | -17.22927 | -57.51828 | 2024-10-24 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| 40e8b0c9-4d8c-306a-8d36-fa0d6279b9f9 | -17.22594 | -57.2556 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| a4cdbdc6-bb55-3e1e-8c0a-62d9d615d7eb | -17.22534 | -57.51238 | 2024-10-24 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 63bc8b3f-6164-31ec-8aba-6cc9a231d2a6 | -17.22382 | -57.49952 | 2024-10-24 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 6bfb9cdd-08c2-380b-be05-7de6efeb000c | -17.2173 | -57.50679 | 2024-10-24 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 4b7f454d-8c1a-3335-a749-024769a4fd83 | -17.19056 | -57.29198 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 03de127c-2822-3732-9c29-f53b3d25dc31 | -17.07973 | -57.3888 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.3 |
| 81e3f86a-efaa-30a3-9160-f386ca4a781e | -17.07819 | -57.37625 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 140d3dd3-0b32-3143-a1ca-f0aec9c181a9 | -17.06947 | -57.39017 | 2024-10-24 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| d30da601-eedd-3da7-89f9-e8393a4149a3 | -17.0596 | -57.48148 | 2024-10-24 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 9f8ab4f8-cd7a-35ae-9193-60ccadef9174 | -17.05921 | -57.39154 | 2024-10-24 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| b2e3a030-1d66-3207-9617-7dd6c18677bf | -17.0387 | -57.39428 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 5283edd4-ae8b-3c29-83a1-ca5862d86b96 | -17.03765 | -57.45206 | 2024-10-24 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.6 |
| 483b85d9-ad3e-3ec7-9cfa-619ac740a210 | -17.03594 | -57.45881 | 2024-10-24 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.6 |
| 766fd780-7fbc-3364-a9d3-5eb880a8a378 | -17.02893 | -57.46609 | 2024-10-24 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 82b0c532-7400-340a-910f-70b5deb4123b | -17.02817 | -57.37656 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 931fb4a2-9d8d-32ee-8f0b-65d5cba52699 | -17.02735 | -57.45342 | 2024-10-24 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.8 |
| ed74871a-afef-3722-a64c-ec37b68456a5 | -17.0266 | -57.36406 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 6def1c25-26f6-3752-8a49-62fc1ca0db6c | -17.02177 | -57.49287 | 2024-10-24 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.1 |
| ec9bb556-0859-39f2-8480-7d04c172813d | -17.02019 | -57.48015 | 2024-10-24 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| e1e90e25-1822-3b52-91f6-eca8963af352 | -17.01862 | -57.46746 | 2024-10-24 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 0c6a3ba9-ffdb-3d10-a27d-2dcf30a6ade9 | -17.01458 | -57.51975 | 2024-10-24 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.4 |
| f008b075-5334-3015-9ab7-53bae2bc5231 | -17.00769 | -57.37928 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.7 |
| 450ba70b-2f24-3f4f-b0d7-6412f765d7db | -17.00303 | -57.34186 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| cba79332-7db3-3c4b-83c5-a794d9f5e99a | -17.00149 | -57.32943 | 2024-10-24 01:24:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| f09d21b9-460f-37b2-8f7b-fe82fc7d970a | -16.91016 | -57.50056 | 2024-10-24 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 609fcce5-f02b-3505-9e09-967b746396c7 | -16.81862 | -57.41661 | 2024-10-24 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 8c4c9381-e718-329f-a4e5-74bec2db3533 | -14.87036 | -59.87283 | 2024-10-24 01:24:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| ec8954a5-3dbc-3b8d-9a7f-d3c290569d2e | -14.27239 | -51.13305 | 2024-10-24 01:24:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 70e1d7c6-2395-3da5-8677-0c37c3356bda | -14.26246 | -51.13454 | 2024-10-24 01:24:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 37.0 |
| a05742a1-e3b6-3871-89f3-c7cbfce492b5 | -14.26067 | -51.12297 | 2024-10-24 01:24:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| f7d535fe-c569-3fe4-aa7a-035aa5fdf893 | -13.7558 | -54.07289 | 2024-10-24 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 54f24097-cc0d-3362-9c24-38dae558295d | -13.75452 | -54.06382 | 2024-10-24 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| ff87c2aa-798e-3b8e-a006-ab4f152a64ff | -13.75324 | -54.05473 | 2024-10-24 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 8ed276d3-8eee-3233-bfa4-322da31e4ab6 | -13.74567 | -54.06515 | 2024-10-24 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| ab80b6e3-571d-3e57-8f55-08742d03318d | -13.74439 | -54.05608 | 2024-10-24 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 41.9 |
| fee08949-cfd8-305e-9066-bbfe6dd518cb | -12.89536 | -48.52502 | 2024-10-24 01:24:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| fde63504-10d8-3a70-b79c-5b67e34944af | -12.89287 | -48.53096 | 2024-10-24 01:24:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| cff6784b-9f19-39f5-8a9e-c592a8fe84f6 | -12.89233 | -48.50702 | 2024-10-24 01:24:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 9e04f7cc-12f2-3da8-99e2-d290d7aefd4c | -12.88995 | -48.51283 | 2024-10-24 01:24:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 35.5 |
| d3be1753-dbe3-34fd-8a50-38b30869adea | -12.883 | -48.52689 | 2024-10-24 01:24:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 93973539-49cc-3845-999a-911c74f2f3e3 | -12.59237 | -48.76964 | 2024-10-24 01:24:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| a2b44432-b587-3348-b6ff-d32d9058dc1c | -12.46841 | -51.33505 | 2024-10-24 01:24:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 8b07e6b3-f481-3ba4-b1bb-a35c8e5a978d | -12.20266 | -46.73035 | 2024-10-24 01:24:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| ab7b6a02-8d96-3e75-8096-869c5d08c4dd | -12.20077 | -46.73632 | 2024-10-24 01:24:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 49d472ff-133e-3f70-a842-532813617efd | -12.16491 | -49.68529 | 2024-10-24 01:24:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 50693c66-cca3-37d8-acfd-f955621e6541 | -12.07984 | -47.98532 | 2024-10-24 01:24:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 7b6c3a7c-e889-308a-9965-a34f9574c804 | -12.05888 | -48.33042 | 2024-10-24 01:24:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| ebc9c643-4135-3cfb-ba32-37e340c041b4 | -12.01067 | -48.27768 | 2024-10-24 01:24:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 488ea898-f975-32b0-bd75-4fd475d95ea0 | -12.00822 | -48.26385 | 2024-10-24 01:24:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 9d40261f-108b-38fb-b8d8-e046811de480 | -12.00722 | -48.25742 | 2024-10-24 01:24:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 795ae82c-837b-33bb-8306-f0243ac414ab | -11.82691 | -47.07306 | 2024-10-24 01:24:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 42.7 |


[Clique aqui para ver as próximas entradas](README9.md)
