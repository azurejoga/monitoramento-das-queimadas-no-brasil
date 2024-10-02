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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6216b3b-93e4-304e-b491-8217fa2e3200 | -13.2231 | -48.593399 | 2024-10-02 00:30:43 | METOP-B | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 079da1b0-8150-37c1-b4ec-812e47ae8729 | -13.2247 | -48.601299 | 2024-10-02 00:30:43 | METOP-B | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| be56ad44-97a9-3e8e-85e0-95fbdacc76fd | -13.2149 | -48.603401 | 2024-10-02 00:30:43 | METOP-B | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1ceb97af-bec0-3839-af3a-cd69b2b12019 | -13.2376 | -48.565399 | 2024-10-02 00:30:43 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b96d1d1-d75a-3358-ae0a-07935b93c36a | -13.2393 | -48.573299 | 2024-10-02 00:30:43 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e396164-d9e3-3786-a7d9-9554c3e90d2a | -13.241 | -48.5812 | 2024-10-02 00:30:43 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a4db645-b2c6-3a64-82ce-f73ff9a474b1 | -13.2262 | -48.5597 | 2024-10-02 00:30:43 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 131520ce-d264-32f2-8496-3295cfc268fb | -13.2278 | -48.5676 | 2024-10-02 00:30:43 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9123335-63cf-3c15-a936-0f116bdb89d6 | -13.2491 | -48.571201 | 2024-10-02 00:30:43 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a980b3ef-aeb0-3e4b-9265-89ba815c1bd1 | -13.2508 | -48.579102 | 2024-10-02 00:30:43 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 03abbe2e-e67a-3eaf-a6dc-d64e4473a8e3 | -13.2035 | -48.597698 | 2024-10-02 00:30:44 | METOP-B | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9387047b-092d-3e56-a880-a96d8f05ad1d | -13.2068 | -48.613499 | 2024-10-02 00:30:44 | METOP-B | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 69902db0-9ff9-3d63-8070-b7231aa9edda | -13.2085 | -48.621399 | 2024-10-02 00:30:44 | METOP-B | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 21c79240-b781-3513-b048-e31b1e2ab525 | -13.2051 | -48.605598 | 2024-10-02 00:30:44 | METOP-B | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d26fa16a-8992-3272-b597-3e5e6cde0541 | -13.5899 | -51.107498 | 2024-10-02 00:30:46 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| af48ac06-7e62-3009-984b-83533b2ebffa | -13.592 | -51.118301 | 2024-10-02 00:30:46 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 555113d7-f5b4-38c3-b815-5cdf96e35f48 | -13.5942 | -51.129101 | 2024-10-02 00:30:46 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0cfcf561-020f-3b97-bebb-536dc6a47851 | -11.8781 | -43.7976 | 2024-10-02 00:30:48 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 277906fd-4eea-379f-85e3-b452127a3081 | -11.88 | -43.8055 | 2024-10-02 00:30:48 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2528c17d-e9a5-3575-9605-72830e136c6c | -11.8818 | -43.8134 | 2024-10-02 00:30:48 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3bdf0c91-838e-38ca-8da1-a91663179fb8 | -11.8684 | -43.799999 | 2024-10-02 00:30:48 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2a23fe87-a29b-3496-8aa5-db0dea08effe | -11.8702 | -43.807899 | 2024-10-02 00:30:48 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eb017bb4-5c66-3843-8d8d-b2e6772c5acb | -11.8721 | -43.815701 | 2024-10-02 00:30:48 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d1bb509-df1b-3c4e-b9dd-d40fd7f43051 | -12.4716 | -47.485802 | 2024-10-02 00:30:52 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ecba789-81c4-33b9-8f44-58c7590575b7 | -12.4731 | -47.493 | 2024-10-02 00:30:52 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6496b0d4-acf1-3f32-aafe-ee10b18517d3 | -12.4747 | -47.500198 | 2024-10-02 00:30:52 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6ded8490-480e-3b40-9e34-3a3f0308aac6 | -13.2324 | -51.2043 | 2024-10-02 00:30:52 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2af615ac-050e-38ca-98b1-61610b918f24 | -13.2183 | -51.184799 | 2024-10-02 00:30:52 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 88f63a32-ac32-3abf-bcb6-e287af798c96 | -13.2085 | -51.186901 | 2024-10-02 00:30:52 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 32ff7a33-0a40-3614-80da-516ad379eea9 | -13.2107 | -51.197701 | 2024-10-02 00:30:52 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f74d5a64-b7d6-3239-8167-362155d1caee | -11.7317 | -44.953701 | 2024-10-02 00:30:54 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8be11ad9-8d54-3cf0-9959-5c892ab5ccf9 | -11.7333 | -44.960999 | 2024-10-02 00:30:54 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 788dbb8c-6805-3788-82f5-acb4d0401b51 | -13.1273 | -51.3396 | 2024-10-02 00:30:54 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 16005750-f55e-363d-b25a-842a4aa507c1 | -13.1295 | -51.350601 | 2024-10-02 00:30:54 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6c9f25a9-fccc-39c6-aadf-83f8d52d9e58 | -13.1175 | -51.341599 | 2024-10-02 00:30:54 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0e4cf06a-fea2-3092-a5a0-8c2320593019 | -13.1197 | -51.3526 | 2024-10-02 00:30:54 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 38692fce-7b17-3c3d-9317-5fa417770f16 | -13.1099 | -51.354698 | 2024-10-02 00:30:54 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8d14eafa-fdbd-32d7-9815-1072c1a609ae | -13.1121 | -51.3657 | 2024-10-02 00:30:54 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 438743d5-2043-3bc6-9b4a-a6a181a2ae44 | -13.1002 | -51.356701 | 2024-10-02 00:30:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 104266b9-eb6c-3e72-816b-6ae3e7867626 | -13.1024 | -51.367699 | 2024-10-02 00:30:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 558d78b0-aad7-3949-aac1-66dcaa4edf38 | -13.1046 | -51.3787 | 2024-10-02 00:30:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4685d353-58fa-334f-bac7-173d65e28ea9 | -13.0993 | -51.402802 | 2024-10-02 00:30:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0b501521-eae5-3999-be0b-0b7b04e1d66b | -13.1015 | -51.413898 | 2024-10-02 00:30:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4c09c908-893f-3e4b-aecb-2c7232d2e34e | -12.2991 | -47.637901 | 2024-10-02 00:30:55 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 632fc6e5-7af8-38c1-9a3f-e707e2d149aa | -13.085 | -51.382702 | 2024-10-02 00:30:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9ec8a42d-3147-305c-bccf-3ef26837f63b | -13.0873 | -51.393799 | 2024-10-02 00:30:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bfe22010-2c84-3fa1-9bd7-89d736e0ac49 | -13.0557 | -51.388901 | 2024-10-02 00:30:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e6be280b-355b-3e2f-9fb5-515800e46021 | -13.0895 | -51.4048 | 2024-10-02 00:30:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 48d826ff-7b7f-3712-9173-fe56474d3a5d | -13.0917 | -51.415901 | 2024-10-02 00:30:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 305753bb-4b9b-3eff-ab11-d47f9712872b | -12.2878 | -47.632801 | 2024-10-02 00:30:55 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4cd901ea-6f2f-3a04-9e37-531ba6a814eb | -12.2893 | -47.640099 | 2024-10-02 00:30:55 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 19db21a9-4cc4-3767-a8ec-a4dbd475cbcc | -12.2909 | -47.647301 | 2024-10-02 00:30:55 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ddc2089-1874-3991-9e4e-6e4b8485e413 | -13.0641 | -51.329899 | 2024-10-02 00:30:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2a764c31-3541-345b-9f29-80696b3e7d52 | -13.0664 | -51.340801 | 2024-10-02 00:30:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 20bb6b7a-e048-3f8d-b376-663b60af81be | -13.0686 | -51.351799 | 2024-10-02 00:30:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c4650002-a317-37ae-aba4-2bbd51e4021f | -13.0708 | -51.362801 | 2024-10-02 00:30:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 26385eac-39d5-36a3-968d-d608aeb615b9 | -13.073 | -51.373798 | 2024-10-02 00:30:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1f0de363-4620-3337-966a-75d86df79a9b | -13.0775 | -51.395802 | 2024-10-02 00:30:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 134c2045-5865-30d1-bfdc-4f10e59dbb64 | -13.0797 | -51.406898 | 2024-10-02 00:30:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 447cb461-6d53-370c-aa4a-5750f911727f | -12.278 | -47.634998 | 2024-10-02 00:30:55 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c51ccf9d-26db-340a-ac5e-20909fa9e206 | -12.2795 | -47.6423 | 2024-10-02 00:30:55 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e486e028-c88d-30d9-a31b-60935520a0a0 | -12.2811 | -47.649502 | 2024-10-02 00:30:55 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 73a05585-8b91-35f1-97aa-af7b2770684a | -13.0521 | -51.320999 | 2024-10-02 00:30:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8f1c257a-38a5-3c3d-81b9-e1ddfbf00433 | -13.0543 | -51.331902 | 2024-10-02 00:30:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cda24e84-6e83-38b9-83ac-5ce7ed31ab5e | -13.0677 | -51.3978 | 2024-10-02 00:30:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3e0c557c-ceb4-300b-bbd7-4ae6a88651df | -13.0424 | -51.323101 | 2024-10-02 00:30:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aae81fa2-caa7-3a51-9723-a8be34c33335 | -13.0446 | -51.334 | 2024-10-02 00:30:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4aee9861-a2e2-3ba9-a26a-7835de062d68 | -13.0469 | -51.344898 | 2024-10-02 00:30:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 82dcdc00-2428-3a63-ae29-b50bee0e3516 | -13.0535 | -51.377899 | 2024-10-02 00:30:55 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 69bfce93-08b8-3ae8-b739-8f02771f99f2 | -11.2625 | -43.3717 | 2024-10-02 00:30:56 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 58ecbdc4-aa6b-3267-a12d-e4e21ce5c2e3 | -11.2645 | -43.380001 | 2024-10-02 00:30:56 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3499d8c4-09c0-376c-a61d-cebbefb0b5da | -11.2527 | -43.374001 | 2024-10-02 00:30:56 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5a45b3ea-3368-3e0a-a1fd-9594ebed2b74 | -11.2547 | -43.382301 | 2024-10-02 00:30:56 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0e61813a-0484-365b-8519-0bfaab944898 | -11.2567 | -43.390598 | 2024-10-02 00:30:56 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 19300cb2-b5fc-3f71-aaa1-ebd0391c6091 | -11.2586 | -43.398899 | 2024-10-02 00:30:56 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d9fb728-6817-368c-90f5-08900f7dd74f | -11.2469 | -43.393002 | 2024-10-02 00:30:56 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fe6b38f2-f80f-3c17-aa69-122affa1556b | -11.2488 | -43.401299 | 2024-10-02 00:30:56 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b2a2d8ff-ba24-3be4-b885-6101b3803148 | -12.9934 | -51.131401 | 2024-10-02 00:30:56 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4ce59265-e679-31c7-845e-828bc11b596b | -12.9955 | -51.141998 | 2024-10-02 00:30:56 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cd2539b6-55da-3fe8-b3fd-6e92f8baf60b | -12.9977 | -51.152699 | 2024-10-02 00:30:56 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bc47f32f-ac83-3f76-a54a-8b44ae08041e | -13.0459 | -51.3909 | 2024-10-02 00:30:56 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1097ee6e-88ac-37fd-8600-97d43f211dfb | -13.0482 | -51.401901 | 2024-10-02 00:30:56 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 93681687-cade-331e-8184-219eef624f1b | -13.015 | -51.489799 | 2024-10-02 00:30:56 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 54fdc08d-5d35-34ff-8efc-97ffb9e435b6 | -12.4945 | -49.1217 | 2024-10-02 00:30:57 | METOP-B | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa6a7d15-98d6-3036-8aef-280b1078762b | -12.4962 | -49.129799 | 2024-10-02 00:30:57 | METOP-B | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| daa80716-4f55-3722-a295-fe99808c9b6d | -13.0052 | -51.491798 | 2024-10-02 00:30:57 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 49542dd6-fb9d-3530-a395-a0852864298f | -12.9804 | -51.520199 | 2024-10-02 00:30:57 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b6768b58-870b-3d81-b987-40c2854b4021 | -12.9661 | -51.499901 | 2024-10-02 00:30:57 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3c562c62-dab3-379f-8fdb-68db8bc2bc71 | -12.9683 | -51.511002 | 2024-10-02 00:30:57 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 81a50387-fc82-31b8-b38e-9239a7147087 | -12.942 | -51.481602 | 2024-10-02 00:30:58 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f8e8a04f-fd16-3f5c-8db1-31409ede48ce | -12.9277 | -51.461498 | 2024-10-02 00:30:58 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 39290837-fe35-30a8-8dcb-ebd3707296b8 | -11.7565 | -47.600498 | 2024-10-02 00:31:04 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e54ac668-7f1d-392d-a0da-42fc95e6f338 | -11.7581 | -47.607601 | 2024-10-02 00:31:04 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0002b5fe-62e3-3c33-aeb9-e8301ed43cb5 | -11.3361 | -46.258999 | 2024-10-02 00:31:06 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 86ee5b8d-098f-39df-ba61-6c185b00ff06 | -12.1557 | -50.041698 | 2024-10-02 00:31:06 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b5eb9e0-626d-3b65-b342-181e83375156 | -12.1575 | -50.050598 | 2024-10-02 00:31:06 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c6cff16-37b7-3130-92ae-b72af4f04e17 | -12.1594 | -50.059601 | 2024-10-02 00:31:06 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f3866ead-80d2-363f-8ad6-d857c63c2bab | -12.1422 | -50.025902 | 2024-10-02 00:31:06 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f1b7c2c-f619-3561-8efd-eebe33c24c46 | -12.1441 | -50.034801 | 2024-10-02 00:31:06 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf6bf109-92a8-3a49-bbc5-b9f37a638d27 | -12.1459 | -50.0438 | 2024-10-02 00:31:06 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README11.md)
