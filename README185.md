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

## Dados Diários - Página 185

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d484f187-1e28-3548-9298-e0e65f77ef47 | -16.87915 | -57.69615 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 6a534a73-591b-3efb-ab09-43fb18bcac27 | -16.87861 | -57.6951 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a0168d9a-00f5-3cdb-b661-f03c49f29fe6 | -16.87848 | -57.70199 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 2c5de786-1567-3993-9bbb-30a4cd57f947 | -16.87791 | -57.70093 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 10307af5-eeba-3afa-ab45-2159944c534f | -16.8755 | -57.68381 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2987e3e7-71c3-352e-bb48-2826e1dd3b72 | -16.87483 | -57.68967 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 13bfdbb2-1ca4-365a-a305-f8fc83de30b1 | -16.87435 | -57.68864 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 5eac8078-b3e9-3065-bc31-6a06ef72fbbd | -16.87294 | -57.70032 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 415cb8ab-91a8-3f3a-bc7a-1619bbf56ad7 | -16.86244 | -57.78727 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 26deb8cb-efec-3e45-9609-4580dba48bca | -16.85637 | -57.76413 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3ffe9c05-7c04-3334-aaf8-6e3f598e83e5 | -16.85533 | -57.76298 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| f0d4704b-2a26-3503-9f91-6624e6eb2185 | -16.85142 | -57.7635 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6e0f5319-af3b-34c1-a947-aec2c3c7cd5b | -16.85038 | -57.76236 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0915bae5-6151-330f-9e19-21560dcaa6ec | -16.84969 | -57.76812 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| f1808fb4-99e1-33a8-8c8e-11d3d80c8768 | -16.84216 | -57.75646 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 8585dfc4-83fa-3739-a144-30163eb1bebf | -16.84087 | -57.76801 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 35904e70-636f-3199-80d6-1d90ab2eeef1 | -16.81662 | -57.79322 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a4667f35-6d17-3b94-9ddb-49c7988427a5 | -16.81594 | -57.79895 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| d0697094-3245-3e1d-8e34-b0b2724b9be6 | -16.80404 | -57.68578 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 907c402d-24c8-3a2f-9e76-7a14d90f9676 | -16.77317 | -57.82263 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 7658957a-72d9-373b-9034-5ff1bb8e0738 | -16.7689 | -57.81628 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 22d6cf34-0e30-33e6-b544-7d4fa6953a9e | -16.76398 | -57.81565 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| a5f7d9b0-5689-3d37-8830-d1eb041eecb9 | -16.76299 | -57.78059 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 772e66fc-c649-365f-ad69-be6797f08385 | -16.7608 | -57.78431 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 1ed2f7f0-e20f-398a-8dd5-9def73dc385c | -16.75971 | -57.8093 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| cfddfc85-4a3d-3a70-aedd-8d389e0679b8 | -16.75801 | -57.80722 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| ad936a79-cce5-3a92-845e-ef8029f9d50a | -16.75739 | -57.78571 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5573061a-92e6-3d76-ba46-796a26727cbd | -16.75731 | -57.81295 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| fda4e03a-32c6-32b1-a1d3-0862f86d8ace | -16.75478 | -57.80867 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 132de51f-24d6-34c5-9a46-8a7e75f972b2 | -14.84504 | -58.61464 | 2024-10-02 05:36:00 | NOAA-20 | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea792bb5-4424-3480-82f0-38c609527fd2 | -14.84445 | -58.6194 | 2024-10-02 05:36:00 | NOAA-20 | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f7ffc09-80d9-3ab5-b8cb-29a8a922042c | -14.83477 | -58.62303 | 2024-10-02 05:36:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c034948a-1880-3742-9366-c4be27564487 | -14.83396 | -58.62194 | 2024-10-02 05:36:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b363764b-78b3-35ca-84ec-32e3218ad16e | -14.8314 | -58.61294 | 2024-10-02 05:36:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 44e39bb1-e6fa-3e09-9aff-7892ce4a736a | -14.83081 | -58.61769 | 2024-10-02 05:36:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 027da326-d7ca-3366-9fd5-e91d5193f30b | -14.83066 | -58.61188 | 2024-10-02 05:36:00 | NOAA-20 | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14e3e952-a8d8-3593-816a-5af7f026a0d5 | -14.83004 | -58.61661 | 2024-10-02 05:36:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a7a1772-55c1-3460-a1fa-58eb994f87ac | -14.82942 | -58.62135 | 2024-10-02 05:36:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d68027c-fc7a-3e66-84af-efde341c7bb4 | -14.82819 | -58.6308 | 2024-10-02 05:36:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 238bbd2e-c40d-313d-8c5d-4efaec6e0cbb | -14.82685 | -58.61236 | 2024-10-02 05:36:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 720587fd-fa4b-3364-8ba1-fa1c1befea17 | -14.82611 | -58.61132 | 2024-10-02 05:36:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c1884dac-f748-32eb-ac95-7065539bd5e3 | -14.82549 | -58.61605 | 2024-10-02 05:36:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 577e9002-9ccb-30d1-9be9-1962e55a58cb | -15.27613 | -58.18814 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc896a0a-b932-3713-98f3-6546e5c28fe8 | -15.27149 | -58.18702 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8a1848ba-f275-31fb-b6c8-aa329e5c987a | -16.60594 | -58.21446 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 66a50411-7675-374b-a385-3a2481044434 | -16.6053 | -58.21992 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 8183afd5-a88f-3271-b307-5e522eb370b9 | -16.60467 | -58.22533 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 1d9cb182-f7fd-3e12-9bd9-f4df905dfbcf | -16.60404 | -58.2307 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 10280deb-19aa-3c17-8589-0ef0457f6507 | -16.60139 | -58.21243 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.1 |
| ec3d00b2-7766-389d-80b6-41654dcd9d82 | -16.60115 | -58.21386 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 86669309-e342-3796-bee6-88a0d9db20dc | -16.60072 | -58.21786 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.1 |
| d958f832-f9b8-3f07-a22f-2baf76a2991a | -16.60052 | -58.21932 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 173.0 |
| d2cfe5dc-423b-33ff-a54b-88ccecdd4bb8 | -16.60005 | -58.22327 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 229.0 |
| 4a772dff-1069-3e1f-aa49-f855adcef367 | -16.59927 | -58.23007 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 138.3 |
| d20b42f5-aa8b-3fbb-a210-63475648d8fe | -16.59661 | -58.21184 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.1 |
| eacca0b9-9b35-3b30-8ba8-d18a7d950338 | -16.59636 | -58.21326 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 67ea1a29-3a94-3f18-9c7b-363df2b0c6b5 | -16.59593 | -58.21725 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.1 |
| 1f02cb22-e5b5-34be-ae5c-6fe2349fa696 | -16.59574 | -58.2187 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 173.0 |
| 99f64413-03c5-3db4-accb-7dcebd335d25 | -16.59527 | -58.22265 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 229.0 |
| 76b0bf8c-8783-3cdf-ab5a-b906979f5036 | -16.59511 | -58.22408 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 173.0 |
| 3758c665-fe4f-389a-b40a-374830100868 | -16.5946 | -58.22799 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 229.0 |
| 3e06ed2f-a158-3f99-a1cc-a7f349676163 | -16.59158 | -58.21262 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 1bb5160b-ae01-331b-8a44-a9ab255c0e87 | -16.59115 | -58.21662 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 2221021d-3421-3ee1-adb8-ba1f1cefb070 | -16.59095 | -58.21804 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.5 |
| dde5f7f1-d9d6-3942-a23f-7f0d8352ce5f | -16.59049 | -58.222 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.2 |
| c26c08bc-0108-389f-a04c-5830737f0cff | -16.59033 | -58.22342 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.5 |
| b2b90da5-73d6-3d6a-bf2c-e36cfa19891f | -16.58983 | -58.22734 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.2 |
| b57e4552-e966-3143-bc4b-a2af6b71ce09 | -16.58971 | -58.22876 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.7 |
| c261e2b6-90db-36d1-a06e-ff87f99937c2 | -16.58638 | -58.21595 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 86d50fc6-70ae-355d-b933-751fc7aa1861 | -16.58618 | -58.21735 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.5 |
| 7f707c95-cf44-366b-9cca-946973e44f8f | -16.58572 | -58.22131 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.2 |
| 5fe7f83b-ce43-3eab-9536-b4d9ccdd4c49 | -16.58556 | -58.22272 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.5 |
| 381768a6-9855-3e44-8280-7a436d010a54 | -16.58506 | -58.22665 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.2 |
| 82ea3015-9dc8-341d-ac8c-34d5dd6e74f9 | -16.58494 | -58.22807 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.7 |
| e68de51d-9f3b-36d0-a9b1-1852aa52a235 | -16.5803 | -58.22591 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| cc27ab3d-9635-393c-b600-0e2b335642f7 | -16.58018 | -58.22731 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| bd70073f-8aea-3cc1-86a2-3969675ee180 | -16.57965 | -58.23122 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 675b1e89-65df-3506-a0eb-dddbb58727fb | -16.57541 | -58.22664 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 6d1ec747-b6b2-3955-9ea8-af0dc1aef16d | -16.57488 | -58.23057 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 9d858906-6ca7-368d-9064-90d3cb16354c | -16.60343 | -58.23597 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| bfa4ece3-d52d-3a5c-848d-c0781f65bc4b | -16.59872 | -58.23391 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.1 |
| 0161aeb6-bc5e-3ec9-861c-45279fba13d4 | -16.59865 | -58.23536 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 138.3 |
| 608672ae-b83b-37e5-965c-df71e1628e8b | -16.59807 | -58.23916 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.1 |
| bc4c49ac-7e06-3b1d-876a-3e623912b8cc | -16.59804 | -58.24061 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| fcb909ef-88da-364e-96ba-f40c0dfde9f2 | -16.59743 | -58.24436 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0ccfadf6-b608-3965-9bfb-f002f4b59421 | -16.59395 | -58.23328 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.1 |
| 9d850c39-358b-3dee-a84a-1af06f167be2 | -16.59387 | -58.23471 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 138.3 |
| f197bfd8-fdd7-3c3c-bfa0-906249756469 | -16.5933 | -58.23852 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.1 |
| 5fc1ac3e-6583-3f03-8d93-1b5700f7d447 | -16.59326 | -58.23996 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bd6e8267-0070-320f-8077-81a447ac3f23 | -16.59266 | -58.2452 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c6138586-d01a-3d49-a346-2d324f0f34c4 | -16.59266 | -58.24373 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| caf6923c-160e-3cfd-86b9-e8c9edfcb2b4 | -16.58918 | -58.23262 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.3 |
| d91c932a-51b1-3517-b21c-91a47d787ff8 | -16.5891 | -58.23404 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.7 |
| 0ff75fe9-b300-365f-b7e6-f1d50f19fe1f | -16.58853 | -58.23785 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.3 |
| 2aab2954-4af6-32e8-8899-7cdbbb9840be | -16.5885 | -58.23928 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.6 |
| 26829d15-057a-3031-88f6-8818675a31ac | -16.58789 | -58.24308 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 3f71219f-6534-3095-8b02-d072a3f1d338 | -16.58788 | -58.24454 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.6 |
| 1070f871-50ce-3581-9e11-0ba86cd17866 | -16.58723 | -58.24837 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 89c225f9-9f13-300c-a88c-7a63c2eb297b | -16.58441 | -58.23193 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.3 |
| e3863f92-f3d2-39a3-8ebd-0688643e4e89 | -16.58433 | -58.23335 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.7 |


[Clique aqui para ver as próximas entradas](README186.md)
