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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfbc36d5-c779-37a6-8b56-a9412e9413b1 | -1.41962 | -48.01178 | 2024-11-02 05:04:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a7f74af-2784-39d1-9b17-ffc3e4725fdf | -1.41696 | -48.01338 | 2024-11-02 05:04:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83b683c6-4f73-36bf-a172-b23e91e45294 | -1.41511 | -48.01113 | 2024-11-02 05:04:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 616be626-6ede-37a6-9cf3-dbaa6e277690 | -1.84532 | -47.45405 | 2024-11-02 05:04:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 676ae3cd-a615-3556-b92f-f7d8aa91d4f2 | -1.84136 | -47.44831 | 2024-11-02 05:04:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0fbbf919-cf46-3cd8-a490-fc852c537a66 | -1.84062 | -47.4533 | 2024-11-02 05:04:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c4b42386-d2d8-366b-b06e-8232774c05e7 | -1.61008 | -47.22151 | 2024-11-02 05:04:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d4be82a6-33dd-3665-af46-5a7718ecf38e | -1.60533 | -47.2207 | 2024-11-02 05:04:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2f72bdfc-9517-3401-8aa9-730041cd1ca6 | -1.04077 | -47.56371 | 2024-11-02 05:04:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77bfade9-e348-324f-a172-34f114aaea33 | -1.04022 | -47.56474 | 2024-11-02 05:04:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66d84ad7-d9c6-33cf-a000-04cd99911391 | -1.03616 | -47.56298 | 2024-11-02 05:04:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 78dba898-f049-33c2-a45b-4b5a56343103 | -2.43201 | -48.88793 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57e3aa60-578e-36b8-b6d4-a1ecf2e66cb1 | -2.43117 | -48.53741 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 137db101-a2d4-3ec0-ab7a-f3bacac32f94 | -2.41893 | -48.52828 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67910415-6c06-3813-9b64-5f1daec3a857 | -2.41859 | -48.53104 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 809651d1-8aa5-3669-84fe-71cd5ae2e7db | -2.41856 | -48.59231 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5eb2748-c90e-391e-9b5a-c6a03e8a916c | -2.41482 | -48.52606 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5af9ed96-a6df-34ad-9016-d3bd24ab0ba2 | -2.41453 | -48.5276 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 227c639f-a550-343b-9890-dd7cd9be08b6 | -2.41175 | -48.87651 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 912f5f71-18f2-33f7-8eca-2dcc46ec8a84 | -2.40604 | -48.58598 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2aeda11-305a-3f1d-b73b-f9df25ab2ef4 | -2.4053 | -48.58734 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7bfb159-a84d-33fb-9726-e58453a94093 | -2.40289 | -48.57681 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad024b3c-a5bd-35f6-bab7-3b24a6a1952e | -2.40227 | -48.58106 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0bd33e6-5f71-37f2-8a4f-7c0ea86bc2aa | -2.40222 | -48.57821 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60d3535d-ea43-3f40-b168-a838e9856849 | -2.40157 | -48.58244 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc6544cf-cd55-3399-be82-5f12121db595 | -2.40103 | -48.58953 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1a8b9c5-2067-3839-9d44-bf4726e8d3a1 | -2.40027 | -48.59089 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9323e468-244a-3891-8d0b-96c1e3834fb4 | -2.36029 | -48.55859 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6290206-fb4c-3491-8c37-d19a61db82a7 | -2.35831 | -48.42141 | 2024-11-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5257c323-f5c8-3823-aa69-130c15ff1880 | -2.35794 | -48.69207 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c78a8bae-81c0-357a-afb5-126fe632527a | -2.35387 | -48.42075 | 2024-11-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c780eddb-3fe0-34a4-9135-54367ab3cf3b | -2.35323 | -48.42508 | 2024-11-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5efa4d6-33cc-3de9-9293-520c8c6704cc | -2.34113 | -48.44556 | 2024-11-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd73b827-25a1-3877-81aa-01b42039cd2a | -2.33257 | -48.62374 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a791d16c-037f-30e6-9072-585f3800e465 | -2.33199 | -48.59768 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3f09151-cfd4-3c59-848b-565ab9906c07 | -2.33137 | -48.60181 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46952e74-cf87-3bb0-8fb6-58fcc65d8576 | -2.32012 | -48.58714 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 482d9c0e-e16f-32fd-b316-1343d30018ce | -2.31636 | -48.58228 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1e32480-cf29-3a8a-b018-497e584f5b49 | -2.29944 | -48.54482 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5045818-13a4-387e-aa93-2adb717602be | -2.2885 | -48.79995 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d51301a9-c3bb-3c5e-aa6e-5de53ccd25dd | -2.28358 | -48.8034 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0097c1e5-504a-3b24-bc13-5e9407d1b165 | -2.92248 | -48.95921 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed8b5b16-577b-3011-a3bf-dfb269a4e69f | -2.91467 | -48.76474 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 217419ca-6048-3900-8dd9-6ad820153bab | -2.77681 | -48.72429 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 84584103-b1f3-3d22-9cd6-3de026479f89 | -2.77371 | -48.71518 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cac34a6-396a-385e-b11e-ff3b6318195d | -2.77308 | -48.71941 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 135f0c5b-2216-3373-8b2c-4e7408adac87 | -2.77244 | -48.72361 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 81fc9750-9df1-3687-92b1-2ca526452f78 | -2.73811 | -48.74419 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71e384d4-6f50-37d1-8c98-d87cb2ffcbbb | -2.73749 | -48.74836 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8a30c15-a3a8-3e4d-be79-da0c4a7478c5 | -2.73438 | -48.73928 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf5d19ea-d905-3b01-ba6a-0e38f6434718 | -2.73375 | -48.74351 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cee583c7-4322-31e5-a1e3-0cf6dbe4a710 | -2.73313 | -48.74772 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 661c3b78-3b0f-3206-b04f-f7ca90f9465a | -2.73252 | -48.75185 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1a47929-6b18-3ce1-a882-702ca23cac82 | -2.73188 | -48.72599 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ece46ac0-673c-3b59-a55e-58276e33ad0f | -2.73002 | -48.73858 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 496b1d0b-090a-33c2-b95b-dc3485c89981 | -2.72877 | -48.74704 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb138473-935b-3345-96fa-61316b3663ed | -2.72816 | -48.75118 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c021f175-9251-3e73-b1ea-da04f641e043 | -2.72751 | -48.72531 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d8d3e27-eca7-37d3-b3ec-0d878a163ee1 | -2.72067 | -48.74145 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5dec5ab-050b-350a-9d43-aaf16db6c33a | -2.71944 | -48.74982 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36e986c9-3583-38f4-a532-f6212cc08cab | -2.71631 | -48.74078 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5a63946-177b-3fd9-af7a-3f93406cce8d | -2.7157 | -48.74497 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12a36113-a809-3020-8183-7327c32926cf | -2.71525 | -48.74154 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c26d267-5448-3c13-a086-1947a1c7a215 | -3.46038 | -47.66822 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0798da3b-5552-3b4c-8a9c-d174c2569109 | -3.45566 | -47.66727 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1ec40564-0526-3427-98c3-f452af6c648d | -3.08652 | -47.78103 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff02f6e5-7358-312f-9e86-4a4d40a0c8ec | -2.24097 | -48.42343 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ec3f610-37a1-3199-98fb-a0c9d4721be7 | -2.23978 | -48.84427 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 78f7e611-145a-3530-b64d-ccec149f95aa | -2.23277 | -48.41774 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b541aacb-f078-3eb6-83ee-f29575704bd0 | -2.22448 | -48.23889 | 2024-11-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7987dbb-f4f2-3079-92fe-8b7c71f44372 | -2.20104 | -48.36197 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86e7944d-40d0-3839-90af-909f2f5cdb8b | -2.19661 | -48.36129 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0beee49e-24bf-3f40-a0d7-c6d0c0e20c0a | -2.17821 | -48.72578 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b24aae6-1ee2-37c7-b364-8b1415e95227 | -2.17759 | -48.72995 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f7dbfc5-6301-31f9-9874-791b1b6ab723 | -2.176 | -48.7275 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f05ef91-1ae8-33fe-b2ba-4966c4c01da3 | -2.17535 | -48.73164 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54cdaffb-9e74-3e28-aadb-43d3b8b6054c | -2.17326 | -48.72928 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc0afc68-b211-32c2-b1b7-373c2fe56da5 | -2.17266 | -48.73339 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| debf8581-83b3-3955-a47d-873c9d892d2f | -2.17162 | -48.82969 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c53b4b0-28e8-3d39-9f91-704a23666243 | -2.17103 | -48.73098 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 529b627f-53df-35ff-b6da-68bdbfe5b162 | -2.16976 | -48.73917 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df087d4d-80bc-3e03-ab5a-6bac1249cd35 | -2.16799 | -48.72201 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| be1fac98-7ca2-301e-9e2d-aa09af63fec6 | -2.16772 | -48.73683 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9845173f-2f8c-340f-8989-8c7833260069 | -2.16712 | -48.74096 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6d533b38-e7f4-3beb-add6-fada0395db71 | -2.16543 | -48.73851 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 64b63e0b-86c6-31e9-b606-e2a5040bf06f | -2.16522 | -48.72375 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| fff51f3b-9a1e-3017-a053-7b7734c66d88 | -2.1634 | -48.73614 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 952e0828-6fdf-3947-a4b2-6bee4e923a74 | -2.53787 | -47.37762 | 2024-11-02 05:04:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e551a6d-350d-34f3-a0ee-0cd034332863 | -2.53695 | -47.51307 | 2024-11-02 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 990734f4-dc1e-33f2-b3f4-039aca0a6f46 | -2.52084 | -47.45884 | 2024-11-02 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 779cebd8-7e9c-3d29-a0a9-116446c2a844 | -2.51609 | -47.45816 | 2024-11-02 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 760c8355-8266-317d-b74c-5c68b4a9572e | -2.36376 | -47.62806 | 2024-11-02 05:04:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 1afeb9f0-04c8-3c53-a5be-45efb7785bb3 | -2.36302 | -47.63305 | 2024-11-02 05:04:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 80bc2daa-b2a6-372b-8e2d-6530fe44d327 | -2.67278 | -48.13519 | 2024-11-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf870228-8036-313d-8bf2-8b3efe06d31b | -2.67131 | -48.64831 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3439dbe1-5235-3206-93bf-7b636faaa315 | -2.67067 | -48.65255 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7323ccde-e911-325c-b39e-22c6d86b02b5 | -2.66824 | -48.13446 | 2024-11-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecdc41be-15dc-33e5-ae8a-2af14eae823f | -2.66462 | -48.5728 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5f9376f-c511-395b-9d01-e37aa67b8649 | -2.64826 | -48.56145 | 2024-11-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60021d0f-1442-35c3-b159-a142912d565a | -2.62803 | -47.96584 | 2024-11-02 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README60.md)
