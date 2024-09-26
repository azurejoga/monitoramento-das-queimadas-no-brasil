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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cf164cb-a1a1-313e-b352-42b3a94114af | -21.30667 | -43.80111 | 2024-09-26 04:10:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 53cebd40-18e6-3446-bad5-27cccd233d6a | -21.30389 | -43.79678 | 2024-09-26 04:10:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 20976b4e-c1fa-3a96-9d7f-37518a782f06 | -21.18 | -44.27341 | 2024-09-26 04:10:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 62d25717-5ffb-3aa2-8bae-de85b4d86716 | -21.17798 | -43.9794 | 2024-09-26 04:10:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 20340488-0afe-3ca5-8c4f-e9a3244c9c40 | -21.10563 | -44.02819 | 2024-09-26 04:10:00 | NOAA-20 | DORES DE CAMPOS | MINAS GERAIS | Brasil | 3123007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bca76dc3-73b8-36c9-bc72-d42a43ada975 | -21.91859 | -45.00247 | 2024-09-26 04:10:00 | NOAA-20 | CAXAMBU | MINAS GERAIS | Brasil | 3115508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3206c1d3-a444-3232-b28f-79cf68f579c4 | -21.86474 | -45.0009 | 2024-09-26 04:10:00 | NOAA-20 | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 23d86847-87c8-343e-8084-0fb163451be5 | -21.61887 | -45.35344 | 2024-09-26 04:10:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ba6d4eb0-199f-30d1-9384-f0fbdd8235cf | -21.20385 | -44.88475 | 2024-09-26 04:10:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a5315bc6-d563-3845-9a93-311ba036f5d6 | -21.19572 | -44.93638 | 2024-09-26 04:10:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 65c5bb37-f2e2-37db-bf90-202b7954fab9 | -22.78676 | -44.1402 | 2024-09-26 04:10:00 | NOAA-20 | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c8a76117-7f48-30e6-ab66-a78edff99e42 | -22.78244 | -44.13198 | 2024-09-26 04:10:00 | NOAA-20 | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 527e27f6-8cc4-3c85-890e-955836b7acd1 | -23.20498 | -45.56859 | 2024-09-26 04:10:00 | NOAA-20 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6b5a21a0-68ef-3ac3-bad4-fca7bc9a6faa | -22.92011 | -45.41353 | 2024-09-26 04:10:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e4c2a19a-dd86-313c-9fbd-8f28a83b2952 | -22.73985 | -44.78695 | 2024-09-26 04:10:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 73a396d1-6193-3856-9f58-be56e58d7275 | -22.73927 | -44.79066 | 2024-09-26 04:10:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 454b00b4-5419-30f5-a88d-6174f86bf9b6 | -22.73654 | -44.78633 | 2024-09-26 04:10:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 408a1cba-307a-3dcf-b8cb-e3c7c76b9c56 | -22.73597 | -44.79004 | 2024-09-26 04:10:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| eaeec28e-c559-36a1-a4cd-b875fccb779a | -20.79159 | -46.32354 | 2024-09-26 04:10:00 | NOAA-20 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b9a75b0-1cb1-364b-a63b-c5a111b81e33 | -20.79095 | -46.32737 | 2024-09-26 04:10:00 | NOAA-20 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7aed2540-20cb-35f5-abf4-6b8cab39d929 | -20.78758 | -46.32673 | 2024-09-26 04:10:00 | NOAA-20 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d3a5fe1-da00-35aa-8cdb-f5d2ae98a3c2 | -20.5413 | -46.37269 | 2024-09-26 04:10:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6170e82a-0c8c-3be0-8f80-823138f26b59 | -20.53792 | -46.37202 | 2024-09-26 04:10:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7663a339-ffaa-3076-99f2-f2910cf1f39c | -20.42576 | -46.24491 | 2024-09-26 04:10:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7034898f-02e0-35ac-8b0d-ed90e73fbf97 | -20.42512 | -46.24875 | 2024-09-26 04:10:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aefd08bd-1607-37da-8619-baf296287407 | -20.42131 | -45.90726 | 2024-09-26 04:10:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8547f43d-84e9-3c74-bbae-1d2064b832a8 | -20.41795 | -45.90669 | 2024-09-26 04:10:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a483e05-478c-3adf-9820-092d186e83e6 | -20.34045 | -46.16658 | 2024-09-26 04:10:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6ba08461-e121-34b6-8610-1341839fe955 | -20.33918 | -46.17425 | 2024-09-26 04:10:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f2bbc18-12bc-3d97-ade9-9ffb708266b9 | -20.33581 | -46.1736 | 2024-09-26 04:10:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c825bce-4b05-3963-830f-f3fbddd4a14f | -20.15521 | -46.58007 | 2024-09-26 04:10:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6e13b83d-546e-39d7-b2f4-2154378917a6 | -20.15456 | -46.58395 | 2024-09-26 04:10:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 113064b0-d6cb-3f2c-bb16-a226665acb42 | -20.1539 | -46.58784 | 2024-09-26 04:10:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9db5761f-d28e-31ca-9e82-958d1d60c317 | -20.15324 | -46.59176 | 2024-09-26 04:10:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 874fdbb4-2061-395f-990f-91a58a75badb | -20.0394 | -45.66542 | 2024-09-26 04:10:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a82c6f38-79f8-3163-8213-3e9562106251 | -20.0312 | -45.65232 | 2024-09-26 04:10:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5eb347f0-5366-3c40-a0b3-74b7fe50c07d | -20.41362 | -45.15509 | 2024-09-26 04:10:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3a34f388-99ef-3ab5-99b7-2a7806e4138a | -22.30688 | -46.8417 | 2024-09-26 04:10:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8cb86e80-b305-3118-bff7-259a252ba360 | -21.21093 | -45.75537 | 2024-09-26 04:10:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e173243f-3f2a-3274-bf65-8ade781747f2 | -21.2076 | -45.75467 | 2024-09-26 04:10:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cfda9fce-5dd0-3254-bd9c-c81b35d2a677 | -21.20366 | -45.7578 | 2024-09-26 04:10:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d68bb6b-5492-3016-911b-390cb2b22c99 | -21.20033 | -45.75718 | 2024-09-26 04:10:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e3918da-dcaa-32ae-bb46-df82a09cab32 | -21.19762 | -45.75279 | 2024-09-26 04:10:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ede313f-f6ff-3250-ab25-2499139f749e | -21.197 | -45.75657 | 2024-09-26 04:10:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d998239-0fde-346e-a98b-fee6945f2b7f | -21.1876 | -45.75116 | 2024-09-26 04:10:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59dc1057-7ece-3567-ad2a-6f24725f0f00 | -21.18699 | -45.75492 | 2024-09-26 04:10:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e8130fa-7ae2-3bfb-a762-f67f69eb1273 | -22.19386 | -45.70935 | 2024-09-26 04:10:00 | NOAA-20 | SANTA RITA DO SAPUCAÍ | MINAS GERAIS | Brasil | 3159605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c6b8a678-ac8d-373a-a3a0-258e1332e32f | -22.19325 | -45.71305 | 2024-09-26 04:10:00 | NOAA-20 | SANTA RITA DO SAPUCAÍ | MINAS GERAIS | Brasil | 3159605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cb02b22b-c81f-3c09-b461-3f5973b863e5 | -22.19054 | -45.70869 | 2024-09-26 04:10:00 | NOAA-20 | SANTA RITA DO SAPUCAÍ | MINAS GERAIS | Brasil | 3159605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 78ebf943-bcde-3795-b489-cc7028b957bc | -22.18994 | -45.71241 | 2024-09-26 04:10:00 | NOAA-20 | SANTA RITA DO SAPUCAÍ | MINAS GERAIS | Brasil | 3159605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bdfa25d6-edf4-307e-a4ab-058fc935fff8 | -21.87104 | -46.63478 | 2024-09-26 04:10:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f7aecc53-5fe9-3554-baa1-f91a7bb93f32 | -21.65375 | -45.95515 | 2024-09-26 04:10:00 | NOAA-20 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 7cb92271-cdce-35d1-b1d1-bff0730639ba | -21.50425 | -46.64104 | 2024-09-26 04:10:00 | NOAA-20 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 24267f3b-7646-3187-8aa4-d30caf4b851a | -21.24735 | -45.7157 | 2024-09-26 04:10:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| afe9dcc3-f747-39df-9dd1-04e6522305d1 | -21.24674 | -45.71945 | 2024-09-26 04:10:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ecf5b932-762b-30a6-814c-e567f94e8d98 | -21.20971 | -45.76292 | 2024-09-26 04:10:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| eef2ced0-3888-3dfd-92c0-bf881495a420 | -21.20638 | -45.76228 | 2024-09-26 04:10:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 9e9a39e5-3ce4-32f8-8f59-09861aed07d7 | -21.20305 | -45.76162 | 2024-09-26 04:10:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| a686e099-9413-36d5-9bf4-2b8bd8f73ba3 | -23.71536 | -46.3691 | 2024-09-26 04:10:00 | NOAA-20 | RIO GRANDE DA SERRA | SÃO PAULO | Brasil | 3544103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5ca566ed-d088-3f39-89ba-ba1748c40454 | -23.68635 | -47.30917 | 2024-09-26 04:10:00 | NOAA-20 | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 32555bf7-62f6-3d9a-87d8-028e038c4dce | -23.59276 | -46.05307 | 2024-09-26 04:10:00 | NOAA-20 | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 58ad0327-a04c-3f04-a56c-8f0d9aa5aad0 | -23.59215 | -46.05685 | 2024-09-26 04:10:00 | NOAA-20 | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d8739a8a-ff81-3857-b557-47d514b8e6ce | -23.56675 | -46.04849 | 2024-09-26 04:10:00 | NOAA-20 | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5a8520ff-67a6-3865-b9fb-f26be3182218 | -23.56343 | -46.04787 | 2024-09-26 04:10:00 | NOAA-20 | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6655cfb4-9cf8-3560-97f2-37f03fb98bc2 | -23.53094 | -45.90952 | 2024-09-26 04:10:00 | NOAA-20 | SALESÓPOLIS | SÃO PAULO | Brasil | 3545001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 33a3b5c5-46c5-3e96-a451-c4bc99dd1c6b | -23.53034 | -45.91328 | 2024-09-26 04:10:00 | NOAA-20 | SALESÓPOLIS | SÃO PAULO | Brasil | 3545001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| feb83484-b42b-3a6e-8fab-585d70bcc8f6 | -23.52913 | -45.92082 | 2024-09-26 04:10:00 | NOAA-20 | SALESÓPOLIS | SÃO PAULO | Brasil | 3545001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3c88c16a-7fd5-30c9-a7eb-b29fc1a919a3 | -23.43253 | -47.0032 | 2024-09-26 04:10:00 | NOAA-20 | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| aecc766e-c3c7-3ecc-ac2a-83b4fe3930fe | -23.4053 | -46.55487 | 2024-09-26 04:10:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9758350a-0ef8-34bc-98a5-491ab81ddfea | -23.36106 | -46.28783 | 2024-09-26 04:10:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 5717b9c6-32f9-3e8c-855a-7c45afb1e571 | -23.36044 | -46.29166 | 2024-09-26 04:10:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ad7a1bd0-11b4-3247-b567-d15589a1eb14 | -23.35055 | -47.00831 | 2024-09-26 04:10:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 384d6e47-fe19-3969-9c9b-20dbc535cc1b | -23.34917 | -46.99578 | 2024-09-26 04:10:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5047d4b8-caa2-3156-be41-6ef7643bdc64 | -23.34851 | -46.99973 | 2024-09-26 04:10:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6bcc68e1-60fe-3fd8-a5a6-e7c7e28fb5a2 | -23.3458 | -46.99508 | 2024-09-26 04:10:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 88684740-cccc-3ca6-81a7-33d24bb25219 | -23.34513 | -46.99905 | 2024-09-26 04:10:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4a9ad269-c96f-3b2f-8293-e7dab15c3e1b | -23.34174 | -46.9985 | 2024-09-26 04:10:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a5ef7b87-bba9-380b-b846-a641ffd9e389 | -23.33983 | -46.77439 | 2024-09-26 04:10:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 091f5e01-1bd3-3f25-9ec7-5e1b57407641 | -23.33647 | -46.77376 | 2024-09-26 04:10:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e4003889-aa7a-334c-bf29-615ada3add56 | -23.25328 | -46.77334 | 2024-09-26 04:10:00 | NOAA-20 | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e7442062-1c3a-35ed-b872-9ca5fc30872c | -23.21084 | -46.45579 | 2024-09-26 04:10:00 | NOAA-20 | BOM JESUS DOS PERDÕES | SÃO PAULO | Brasil | 3507100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 70ff9d24-d168-3ce3-a9b4-5a32f4ec81d5 | -23.20687 | -46.45898 | 2024-09-26 04:10:00 | NOAA-20 | BOM JESUS DOS PERDÕES | SÃO PAULO | Brasil | 3507100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 50de8ddd-4655-34b3-9d29-ec44344ec144 | -23.20018 | -46.45774 | 2024-09-26 04:10:00 | NOAA-20 | BOM JESUS DOS PERDÕES | SÃO PAULO | Brasil | 3507100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e4cfcdda-5d9b-31f9-a809-f7741f56db0a | -23.17683 | -46.3359 | 2024-09-26 04:10:00 | NOAA-20 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ef97ca04-ba7a-3c1a-9d1e-f63023578d50 | -23.16808 | -46.32632 | 2024-09-26 04:10:00 | NOAA-20 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 50b40e94-250d-399d-976a-82ad780a028c | -22.90453 | -46.43826 | 2024-09-26 04:10:00 | NOAA-20 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7e208bbf-c132-311a-9c4a-7700790525f5 | -22.90181 | -46.43382 | 2024-09-26 04:10:00 | NOAA-20 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5f18d32e-6fc0-343d-8396-7528971dd955 | -22.85786 | -46.44915 | 2024-09-26 04:10:00 | NOAA-20 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 19aa70a6-da20-3fe2-9593-7949489130a2 | -22.85644 | -46.44601 | 2024-09-26 04:10:00 | NOAA-20 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3270a9e4-bbd6-34fc-b0ad-7b8a28204f76 | -22.81174 | -46.25616 | 2024-09-26 04:10:00 | NOAA-20 | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 40e45907-b549-3b1d-8e3a-b28cea942c8b | -22.80839 | -46.25563 | 2024-09-26 04:10:00 | NOAA-20 | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 558926da-c85d-3442-af8c-52d80ba53023 | -22.72694 | -45.73256 | 2024-09-26 04:10:00 | NOAA-20 | SAPUCAÍ-MIRIM | MINAS GERAIS | Brasil | 3165404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 3b21509b-aaaf-3255-acc3-d6e2fbab07d7 | -22.62625 | -46.24886 | 2024-09-26 04:10:00 | NOAA-20 | MUNHOZ | MINAS GERAIS | Brasil | 3143807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 696cbb76-6b6d-350d-bbcb-e89a83f34629 | -22.6229 | -46.24825 | 2024-09-26 04:10:00 | NOAA-20 | MUNHOZ | MINAS GERAIS | Brasil | 3143807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 994f0582-a7c1-3534-b091-c4e1d40c54ec | -22.55534 | -45.84772 | 2024-09-26 04:10:00 | NOAA-20 | PARAISÓPOLIS | MINAS GERAIS | Brasil | 3147303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0648b4d6-7cdb-307b-97e2-5ee70762c217 | -22.55202 | -45.84711 | 2024-09-26 04:10:00 | NOAA-20 | PARAISÓPOLIS | MINAS GERAIS | Brasil | 3147303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b253dac0-5c86-3562-a464-38aa7985b590 | -20.88981 | -47.01704 | 2024-09-26 04:10:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 438ae15d-5c48-390c-a082-00f9befd769e | -20.82696 | -47.21842 | 2024-09-26 04:10:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67ff97d5-23c1-3549-894b-12115374c72a | -20.82625 | -47.22255 | 2024-09-26 04:10:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3478a332-bb7d-3100-a2ac-4de6b1af3c41 | -20.82349 | -47.21775 | 2024-09-26 04:10:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README84.md)
