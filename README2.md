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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 306c1a0e-75f0-3655-af13-dd40a755a07c | -27.055099 | -52.655102 | 2025-08-02 00:39:00 | METOP-B | CHAPECÓ | SANTA CATARINA | Brasil | 4204202 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a29fe302-b085-3dfd-8537-783bcadd80c3 | -3.5067 | -52.874699 | 2025-08-02 00:39:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 795218fd-995d-31ea-a24c-bb0ccb358a4a | -12.6206 | -44.514599 | 2025-08-02 00:39:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e693c4f8-e6d6-358d-8a8b-fa29b19c59b6 | -11.3564 | -54.333599 | 2025-08-02 00:39:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4bac578-5041-37f3-a54a-ea4ef568e476 | -22.3395 | -54.9716 | 2025-08-02 00:39:00 | METOP-B | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 598871f9-e255-356e-b285-7b4f4a0d91c0 | -12.62 | -44.473099 | 2025-08-02 00:39:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c8178d28-e86a-3624-8d50-21f739cc56b4 | -11.4006 | -56.862701 | 2025-08-02 00:39:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 254f0d85-7d1b-35df-a13a-238abbefaa22 | -12.6835 | -47.791 | 2025-08-02 00:39:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a23aa94f-00cc-33b5-9e2e-dfe5754fd686 | -13.0327 | -47.4464 | 2025-08-02 00:39:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e60eabca-aeb6-3a3a-8352-90d793402329 | -8.5511 | -51.5504 | 2025-08-02 00:39:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40eb0773-c808-3bea-b243-b18a2a354f88 | -12.6445 | -44.487301 | 2025-08-02 00:39:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 72404d74-8c85-3fd2-8c67-430612a83a87 | -13.9769 | -53.947701 | 2025-08-02 00:39:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 20fca776-4f54-3fe7-8fe3-6d9f8420dd59 | -11.2058 | -48.894199 | 2025-08-02 00:39:00 | METOP-B | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a418d9e4-1d66-3b39-8029-82655e1090bf | -12.6541 | -44.484699 | 2025-08-02 00:39:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 93824629-56ab-3dcd-b423-0914c84b3e69 | -22.6136 | -50.660301 | 2025-08-02 00:39:00 | METOP-B | MARACAÍ | SÃO PAULO | Brasil | 3528809 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 90e0e706-38d6-37ee-95aa-ea243421904e | -22.309601 | -48.711601 | 2025-08-02 00:39:00 | METOP-B | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c7598993-e4be-387b-92ab-4b5c8cbcfbe5 | -11.1648 | -51.522999 | 2025-08-02 00:39:00 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e5e3aa33-2297-32c6-8b9f-395152b4d971 | -10.5607 | -45.286201 | 2025-08-02 00:39:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4f29874a-6299-3936-855d-22d68a6bdb11 | -12.6495 | -44.506802 | 2025-08-02 00:39:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4d859ba6-995d-3ac1-9307-113563457f6b | -12.6155 | -44.495201 | 2025-08-02 00:39:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a1e3c82c-4106-3d92-b894-9f270304979e | -12.6399 | -44.509399 | 2025-08-02 00:39:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f12625bb-1547-301d-b71f-98b12a5c1ce7 | -8.8859 | -47.327599 | 2025-08-02 00:39:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 90001e05-3241-3b96-a843-72853255be8b | -12.6591 | -44.5117 | 2025-08-02 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 251.1 |
| c6774e00-724b-3f4b-a34a-833304715a7c | -10.0166 | -44.7311 | 2025-08-02 00:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 63.8 |
| f2e7d4ae-0083-3ccd-9fa8-5a6d41bb6fff | -12.6789 | -44.4851 | 2025-08-02 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 238.2 |
| 31d377b2-4a3a-3d51-b34a-417875a7e357 | -10.055 | -44.7032 | 2025-08-02 00:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 47b4416e-6341-3354-bf9f-f2244c0ad47a | -12.6793 | -44.4616 | 2025-08-02 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 25ff6c2c-0ee4-3082-93ca-608b32be204b | -10.017 | -44.708 | 2025-08-02 00:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 122.6 |
| db432a2e-e4a9-3cb9-ac48-fb1f4ad58caf | -12.678 | -44.532 | 2025-08-02 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 1d093e25-0890-3cd5-b81c-2940e5075a2a | -12.6595 | -44.4882 | 2025-08-02 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 362.1 |
| 6a356af7-981f-3945-866c-40ca108eac66 | -12.6784 | -44.5085 | 2025-08-02 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 33d66895-2b0f-39df-b00c-a8970902d810 | -10.0357 | -44.7287 | 2025-08-02 00:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 04e0ab37-e24a-37bb-9db0-325218d96fc6 | -10.036 | -44.7056 | 2025-08-02 00:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 268.7 |
| e2849fe2-7463-3c82-b5a2-31767f08f34b | -12.6784 | -44.5085 | 2025-08-02 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 153.7 |
| afea28d8-5c9d-3340-8b3b-f4208fc79060 | -6.8891 | -40.875 | 2025-08-02 00:50:00 | GOES-19 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 87cd3447-2628-34c3-9a13-17477e6d724e | -22.6436 | -50.6632 | 2025-08-02 00:50:00 | GOES-19 | MARACAÍ | SÃO PAULO | Brasil | 3528809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 133.3 |
| b37274ec-d791-3eb5-81b4-d5c4d835e94c | -12.6789 | -44.4851 | 2025-08-02 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 220.4 |
| 5fca492c-d50a-39de-a0c3-12f405ec3257 | -12.6595 | -44.4882 | 2025-08-02 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 302.3 |
| e6a6eb33-8914-3108-972a-5fe716cc8359 | -12.678 | -44.532 | 2025-08-02 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 47fd4146-e311-3128-9084-d6cf21f1eba9 | -12.6591 | -44.5117 | 2025-08-02 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 230.9 |
| 46e42d0c-995c-3b5d-8180-ff262b9e07f0 | -12.6402 | -44.4913 | 2025-08-02 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| f8730cee-0e70-3ab4-af8f-58d94a93e201 | -12.6789 | -44.4851 | 2025-08-02 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 238.3 |
| 379d9e03-2cb5-3c2a-b37a-97bdbb0c9fd4 | -12.6595 | -44.4882 | 2025-08-02 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 281.3 |
| 012d6589-763b-3c8f-a2b3-dd701e2d149a | -12.6591 | -44.5117 | 2025-08-02 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 201.7 |
| 98f3d70f-9192-3d99-9917-a1a1bb4476e3 | -10.036 | -44.7056 | 2025-08-02 01:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 119.7 |
| dc8e2bdb-cdfb-30f6-8628-8d09b3e7065d | -12.6784 | -44.5085 | 2025-08-02 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 156.3 |
| d1f42d42-b084-3884-ab15-46089fed00e7 | -12.6402 | -44.4913 | 2025-08-02 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| d53c8393-bfd1-3060-95f5-0f2ce5b9f762 | -10.0357 | -44.7287 | 2025-08-02 01:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| cfec05fe-7033-3361-88fc-db78d56eb8c1 | -29.62479 | -50.80255 | 2025-08-02 01:02:00 | TERRA_M-M | TAQUARA | RIO GRANDE DO SUL | Brasil | 4321204 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 573f646f-0cbb-376b-b822-56108050d578 | -25.50984 | -52.84348 | 2025-08-02 01:02:00 | TERRA_M-M | QUEDAS DO IGUAÇU | PARANÁ | Brasil | 4120903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 64573e7c-b313-3e0f-b8c6-634fca0e3c4b | -14.03166 | -53.51379 | 2025-08-02 01:05:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4ba3c451-52e2-33f2-b1c8-fd9a83c6e7b5 | -12.6566 | -44.49562 | 2025-08-02 01:05:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 455.4 |
| 937c52c7-9bcb-36c1-9b40-fedf5140a11b | -22.66869 | -53.37972 | 2025-08-02 01:05:00 | TERRA_M-M | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| d12a9197-4021-3dd3-a692-8dc7611d60e5 | -22.63775 | -50.6735 | 2025-08-02 01:05:00 | TERRA_M-M | MARACAÍ | SÃO PAULO | Brasil | 3528809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| b06e74b6-4720-3f8c-9529-1509e63b94bb | -13.69324 | -51.95293 | 2025-08-02 01:05:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 08f36b8f-fd5f-355c-b3ee-d904700e502f | -15.11907 | -55.22203 | 2025-08-02 01:05:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3b5a7b33-3cbe-3a17-a5b4-446a45d934ff | -12.70612 | -47.78683 | 2025-08-02 01:05:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 6453cdd9-d011-37f6-b885-5381ef6f231f | -12.67361 | -44.49707 | 2025-08-02 01:05:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 209.8 |
| dafb82b1-9645-3d5e-8d90-72d0ccaf1d8e | -12.66364 | -44.54192 | 2025-08-02 01:05:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 1584e478-fe53-371c-a434-eaa82ce882ef | -14.03027 | -53.50425 | 2025-08-02 01:05:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 20d2c346-5835-3fd6-8320-827e06edac60 | -15.11781 | -55.21274 | 2025-08-02 01:05:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| e4f345b6-82df-346f-8766-55aea8d75f82 | -12.68096 | -44.53856 | 2025-08-02 01:05:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 7fbd88f7-e142-383b-87af-d026c3633819 | -12.68159 | -44.53358 | 2025-08-02 01:05:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 315e8519-94d5-3524-bbfb-0bd39fb215cd | -13.99211 | -53.94516 | 2025-08-02 01:05:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f75ac626-64de-38fa-b66e-1bc1f5f4eb6f | -22.63613 | -50.66273 | 2025-08-02 01:05:00 | TERRA_M-M | MARACAÍ | SÃO PAULO | Brasil | 3528809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| b167eacb-62f6-379a-8071-33926ccea017 | -20.87709 | -56.37481 | 2025-08-02 01:05:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 16.3 |
| cfe01dda-54ba-3412-992e-63346660b6b5 | -21.5485 | -48.72172 | 2025-08-02 01:05:00 | TERRA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 21.5 |
| ebbbee08-3855-3738-8e18-968421d37152 | -12.67396 | -44.49217 | 2025-08-02 01:05:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 259.6 |
| aff70e8a-7f82-3d51-a47b-2c4266a5394e | -20.86408 | -54.95184 | 2025-08-02 01:05:00 | TERRA_M-M | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f651eb20-044b-319e-9039-454eacbf6317 | -12.66426 | -44.5369 | 2025-08-02 01:05:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 192.3 |
| 10abccb0-4883-3f7b-abef-cac3d921a7f7 | -15.10892 | -55.21409 | 2025-08-02 01:05:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 982f0c0b-af28-3751-a41e-e45be335a229 | -16.69722 | -49.39724 | 2025-08-02 01:05:00 | TERRA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| e3be85e7-8e60-3367-9ac8-4bb88b0d19f1 | -22.35557 | -54.98764 | 2025-08-02 01:05:00 | TERRA_M-M | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| ffa11277-5460-37f0-90b0-e09b398a2714 | -12.65626 | -44.50058 | 2025-08-02 01:05:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 462.7 |
| cf69b8ee-6968-343f-8db6-9fb44f6a0438 | -10.68083 | -56.55196 | 2025-08-02 01:07:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 11898f97-b085-33b8-aad1-2b54be1c007b | -10.58551 | -45.28696 | 2025-08-02 01:07:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 50.0 |
| c059ee1c-18bf-3fa8-bac2-a2764998aa0c | -11.39182 | -55.36278 | 2025-08-02 01:07:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3351b441-cfd7-3a0d-811a-dec29e29e861 | -11.41368 | -56.87125 | 2025-08-02 01:07:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| acb90b98-23ca-3547-9b06-3ae1be5ab6e8 | -10.45728 | -46.98815 | 2025-08-02 01:07:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 47c968ad-8c0c-3990-9586-b81f5a8dbe75 | -11.37662 | -54.3393 | 2025-08-02 01:07:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bf3cbaf1-a04e-3e12-a831-fed3eb14ebe2 | -8.91183 | -47.33597 | 2025-08-02 01:07:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| d6796ddd-adcc-3a00-bd7f-7519c78936c7 | -8.56898 | -51.54187 | 2025-08-02 01:07:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| f97dac70-0a10-3e25-863f-a00d2c34b64d | -11.1899 | -51.51859 | 2025-08-02 01:07:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f932c0ee-008f-320b-8bd6-c8c45b6ff2b5 | -10.58328 | -45.29219 | 2025-08-02 01:07:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 654ca1b5-1723-341f-9e66-99a4a5853f8c | -8.90911 | -47.33117 | 2025-08-02 01:07:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| f47dc4c5-34ba-3187-acf9-9bbf43611c6b | -12.46506 | -57.87404 | 2025-08-02 01:07:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bb38d48a-1001-3787-941d-893a39522038 | -10.3629 | -55.31499 | 2025-08-02 01:07:00 | TERRA_M-M | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7230da3f-b49e-3196-bfe1-72f7d2da9c8f | -11.41241 | -56.86177 | 2025-08-02 01:07:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 2ec684d4-3755-3d9b-b198-0891cc50e487 | -10.36164 | -55.30602 | 2025-08-02 01:07:00 | TERRA_M-M | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7d2a005d-4bca-30ba-a708-dd1e08e3f2b0 | -3.51127 | -47.21841 | 2025-08-02 01:09:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 233890d1-531c-3a0b-a8ae-43c06f89d5f4 | -3.50728 | -47.22573 | 2025-08-02 01:09:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 48c11d45-149b-3829-af4a-dc5afaa35b50 | -3.53089 | -52.86599 | 2025-08-02 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 11725dd3-4a39-3a8f-b0a3-aecca1bb3ed1 | -3.52787 | -52.87206 | 2025-08-02 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| d1d3b14a-bab3-3eb3-9699-53233bab4976 | -4.6606 | -55.973 | 2025-08-02 01:09:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 115bf0ab-00b0-30d5-94d2-ea4c982805e3 | -8.0318 | -43.1493 | 2025-08-02 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 250.1 |
| 6b5ec4fb-c519-3668-9c70-fac64032c707 | -10.036 | -44.7056 | 2025-08-02 01:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 338bdbba-ff76-350c-bfc8-099c02e8ee49 | -10.0357 | -44.7287 | 2025-08-02 01:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 4d159e8e-0d47-3566-b479-035ac2635f99 | -8.0129 | -43.1513 | 2025-08-02 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 112.6 |
| 1d3aacbd-6086-32aa-953c-019c1b30900e | -8.0132 | -43.1278 | 2025-08-02 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.8 |
| b716e102-54f7-3fd6-86b8-1f36c346f59f | -12.6789 | -44.4851 | 2025-08-02 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 210.4 |


[Clique aqui para ver as próximas entradas](README3.md)
