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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1abc2125-871f-3259-adc8-f2a82830f10f | -19.8895 | -42.63006 | 2025-10-01 03:13:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 50541dab-58e4-3192-9cbf-6c0c5d0fdf71 | -19.86753 | -42.59771 | 2025-10-01 03:13:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c2b4070c-b0bc-3cfe-b79b-7de7fa817e5c | -19.76749 | -42.1531 | 2025-10-01 03:13:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b4c4f821-e7c0-3b3b-a296-54e278f3b03b | -19.76422 | -42.14986 | 2025-10-01 03:13:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ceed997e-f02e-32af-b163-c079ea7b25b6 | -19.92948 | -43.90271 | 2025-10-01 03:13:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 841f2610-f197-3ca5-b19b-71a1440ae3bd | -19.86095 | -42.59562 | 2025-10-01 03:13:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 06422a9a-d742-3061-8987-86b96ae6adc2 | -18.91816 | -43.12907 | 2025-10-01 03:13:00 | NPP-375D | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| aa0e6c24-8dd4-381b-b6a2-de3250ebaefe | -18.95981 | -43.71363 | 2025-10-01 03:13:00 | NPP-375D | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a9d334b7-4830-3861-aa95-f86adc7ac102 | -19.7708 | -42.15126 | 2025-10-01 03:13:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 93aab4e7-46d4-301e-9518-4934172c1455 | -18.91299 | -43.11988 | 2025-10-01 03:13:00 | NPP-375D | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 84e95cfa-57a9-37b3-83a1-9bd8f42e78f0 | -20.8348 | -43.01644 | 2025-10-01 03:13:00 | NPP-375D | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 117956f5-9b30-3e0f-abc1-44426ac36ea9 | -20.83877 | -43.02497 | 2025-10-01 03:13:00 | NPP-375D | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 715889ac-0154-3aca-a9ef-fb53ec2ba9f0 | -20.23011 | -43.8964 | 2025-10-01 03:13:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ff56e0f0-d0ed-32f0-b3e1-5463a08612f7 | -18.96053 | -43.70853 | 2025-10-01 03:13:00 | NPP-375D | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65bacdfb-4340-3c0f-95fe-27c2766df7c3 | -19.86629 | -43.82235 | 2025-10-01 03:13:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 41bf06ea-0081-3d39-a1a7-788a01807246 | -19.86168 | -43.83149 | 2025-10-01 03:13:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a7b7b727-7e7c-3443-90e3-19d5aff3efd7 | -20.796 | -43.52053 | 2025-10-01 03:13:00 | NPP-375D | LAMIM | MINAS GERAIS | Brasil | 3137908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f88f8522-1afb-3024-9f4e-1a233e967a39 | -20.34993 | -43.34546 | 2025-10-01 03:13:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e27b09e5-e956-365a-9811-baacb88521f6 | -20.79425 | -43.52758 | 2025-10-01 03:13:00 | NPP-375D | LAMIM | MINAS GERAIS | Brasil | 3137908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 27c0f19b-7d54-3261-b47a-98423550c564 | -20.49935 | -43.94529 | 2025-10-01 03:13:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 49d753fb-f79b-3a86-8aa1-9e4085dba78e | -19.86388 | -43.82261 | 2025-10-01 03:13:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1905eea0-2d47-33fc-b938-79a34fa4ca7d | -19.86396 | -43.83147 | 2025-10-01 03:13:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 96153828-ca26-3c39-b2df-4295976c2b4c | -20.83358 | -43.01702 | 2025-10-01 03:13:00 | NPP-375D | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| c8d29da9-fa81-3a0d-8a38-ff61ebe45238 | -20.47937 | -43.95329 | 2025-10-01 03:13:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 62587ea2-ac5f-37b8-bda5-f82ac012e2c9 | -20.69972 | -41.56752 | 2025-10-01 03:13:00 | NPP-375D | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4af6cda5-2fe9-3869-91ba-f759942436f7 | -20.83204 | -43.02335 | 2025-10-01 03:13:00 | NPP-375D | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 9681af29-77e0-36cc-bae2-61140fb6c97d | -20.42844 | -43.60593 | 2025-10-01 03:13:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1133d126-73c9-321f-9f6b-ca3a50dfbb58 | -20.48133 | -43.94545 | 2025-10-01 03:13:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 2cc9d463-9622-3f6d-86dc-037fd78ff527 | -19.85736 | -42.58739 | 2025-10-01 03:13:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 73f545f1-63a6-3a30-bda4-6e34c3fa591e | -20.49679 | -43.94391 | 2025-10-01 03:13:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| c72bf302-8a29-3743-b053-086a59d2482a | -20.43056 | -43.59741 | 2025-10-01 03:13:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 79c8d0f5-3873-3621-a6bf-398cc71f30f4 | -20.23194 | -43.88897 | 2025-10-01 03:13:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d67a6285-2f9b-3339-8a9b-3cfea3a08c97 | -19.85582 | -42.59367 | 2025-10-01 03:13:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fd3b8f09-6b9a-3de5-a20a-aed3824473a7 | -20.49014 | -43.94036 | 2025-10-01 03:13:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 7370570d-37b0-32ee-ad3c-8ccd0a8b2b69 | -19.76877 | -42.14778 | 2025-10-01 03:13:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8b626343-3bb8-3094-a7ed-893a868f90a8 | -19.76218 | -42.14639 | 2025-10-01 03:13:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 851d6e8b-4fe2-3914-8727-74253b2a2a1a | -19.86242 | -42.58946 | 2025-10-01 03:13:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 17410714-7723-395a-bd8c-81e4f3a86214 | -19.76547 | -42.14453 | 2025-10-01 03:13:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 8e92d03c-5d25-3b78-abe1-655eb15d63db | -20.23573 | -43.88206 | 2025-10-01 03:13:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8a096208-7168-3124-83cf-25080207c5d7 | -20.23367 | -43.89023 | 2025-10-01 03:13:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 983a5718-e0aa-3451-9e31-9ac861cd9798 | -20.35161 | -43.33855 | 2025-10-01 03:13:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0ca7d53b-35c2-317c-b8ac-9a588a220c61 | -20.50086 | -43.93938 | 2025-10-01 03:13:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 4a348188-ca28-35ee-a21c-6e235274b51c | -20.48187 | -43.95461 | 2025-10-01 03:13:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 89df4f9e-4596-3bfe-b2d3-ad17131b2684 | -20.83996 | -43.02436 | 2025-10-01 03:13:00 | NPP-375D | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 30d9b246-8ce1-3631-9d59-f4977f77f799 | -20.49274 | -43.94161 | 2025-10-01 03:13:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 1bc55ead-d4d6-3904-ac38-488b71eb228a | -20.49828 | -43.93798 | 2025-10-01 03:13:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 0022f84a-4de7-34ac-b427-8121c9967c78 | -20.43764 | -43.59872 | 2025-10-01 03:13:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 300edfa8-aabf-308a-a968-b4d35e44cb21 | -14.1926 | -46.1091 | 2025-10-01 03:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 4de2ced7-a6c8-33ef-99f2-9022a09b1cba | -11.383 | -45.0543 | 2025-10-01 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 168d5417-111e-33b9-ba5e-827795b6ccea | -13.2165 | -50.9071 | 2025-10-01 03:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 30dcc835-64ed-3584-a623-215217d5fbc6 | -11.478 | -45.0868 | 2025-10-01 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 79a0ba78-71c7-357d-aef4-c633d08261f9 | -11.8438 | -44.964 | 2025-10-01 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| ba94c666-ff3b-37bb-99ee-45f9ff0a6f20 | -11.8246 | -44.9669 | 2025-10-01 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 2452081b-b442-3150-b86d-d4d76c60b120 | -11.3826 | -45.0774 | 2025-10-01 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| bd59e51d-32b7-3363-967b-2ad8887a01c3 | -20.6309 | -46.2046 | 2025-10-01 03:20:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 47.6 |
| b1cbbc8c-2a69-3e10-a711-062879772058 | -16.2562 | -50.9275 | 2025-10-01 03:20:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| d7ca8777-663b-3a23-839a-33f4362bb779 | -3.0827 | -47.0088 | 2025-10-01 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| d9bd3ff6-26d8-3d57-9119-4a670b87d9a4 | -3.1013 | -47.0082 | 2025-10-01 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 177.4 |
| 0d21330c-b299-30b9-9a80-86ec7ecd8afa | -11.8434 | -44.9872 | 2025-10-01 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 5706125a-ad2e-3b8f-9abe-7d4f4d00b1d4 | -13.9396 | -48.1182 | 2025-10-01 03:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 15696d85-6d41-3faf-b023-f8585059cb46 | -12.2536 | -47.806 | 2025-10-01 03:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 547cc8e8-a36c-3c3c-9177-edb7ee85e49d | -9.3089 | -54.5229 | 2025-10-01 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 75734823-01f3-3708-a84e-eabf32538e54 | -14.3519 | -45.9206 | 2025-10-01 03:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 5cbbb300-583f-381e-bcc3-8b73212cdac0 | -14.8021 | -45.7946 | 2025-10-01 03:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 221a3d5e-e46f-37e1-b8c5-078c3ae938ec | -14.8026 | -45.7713 | 2025-10-01 03:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 55.0 |
| c5c5138d-aa1d-3c57-a807-94da3e4993f7 | -11.4588 | -45.0895 | 2025-10-01 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 716d1f7e-8c0f-3dc7-90f8-96120554a50e | -13.2168 | -50.8856 | 2025-10-01 03:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 212e8918-73d0-300b-8b4e-46ac659ff4bc | -14.3514 | -45.9437 | 2025-10-01 03:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 2ae9cc59-dbee-323d-82fb-af474284e71f | -9.2902 | -54.5242 | 2025-10-01 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| b017c774-d785-38ab-9afd-8f3f06006954 | -3.1012 | -47.0301 | 2025-10-01 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 4e943b31-d531-3cba-9e23-198442db94cb | -7.09544 | -45.55661 | 2025-10-01 03:28:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aaaa3ad0-10a4-3eef-bffb-58095231ab59 | -3.88464 | -42.52544 | 2025-10-01 03:28:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 02758e80-51e1-3857-9da5-3c275d40dd9f | -5.76078 | -42.87019 | 2025-10-01 03:28:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 8e8f7a23-8aae-348c-bc96-26d3d657ceb8 | -6.68078 | -42.80633 | 2025-10-01 03:28:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 3adf706f-5400-3f92-9ed1-f2593c35cb7c | -6.35865 | -43.95632 | 2025-10-01 03:28:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e5c4ed3b-ae2f-3561-940d-40869bc0978e | -6.7933 | -44.74495 | 2025-10-01 03:28:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b0e4972-8ba5-3842-b731-125a0add4973 | -5.85874 | -43.40537 | 2025-10-01 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| fe5068f3-306f-3676-af3b-fc3440f29f53 | -3.41342 | -40.21436 | 2025-10-01 03:28:00 | NOAA-20 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d5a97c7c-2737-3732-b017-db6014ebbd77 | -5.48832 | -37.38168 | 2025-10-01 03:28:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b95426da-30f6-3b40-8914-a51e757721c9 | -7.16091 | -41.70786 | 2025-10-01 03:28:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 3626789d-4e12-3504-9991-31e12be59d68 | -6.21582 | -44.22708 | 2025-10-01 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e8323752-9a13-30fd-bc82-4219a71f0aac | -7.79707 | -42.51653 | 2025-10-01 03:28:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| bc36b079-6545-37c8-890b-d0c2c5cb73ad | -5.72216 | -42.69384 | 2025-10-01 03:28:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 84937bbb-7bbe-38bb-b0a5-c4367c14d4d2 | -3.41383 | -40.21668 | 2025-10-01 03:28:00 | NOAA-20 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f72e9881-fd21-3273-9808-ef6f0adf1e15 | -3.88543 | -42.52074 | 2025-10-01 03:28:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ed5db4ea-a279-3731-9950-944be0f01984 | -3.87934 | -42.51968 | 2025-10-01 03:28:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 0c3e3362-7da6-3b65-8590-7636ff7939d9 | -3.87856 | -42.52436 | 2025-10-01 03:28:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| e5ba1ef7-7fb6-3727-bf3a-c1653bd36018 | -6.07371 | -42.66652 | 2025-10-01 03:28:00 | NOAA-20 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 23fdd149-6df9-3046-b48c-9a03305f52d5 | -6.23162 | -45.34552 | 2025-10-01 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d47f8b5c-42dc-3282-a68c-9fc2573b7028 | -5.40831 | -41.32754 | 2025-10-01 03:28:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 467efa4e-fab6-327d-b023-a844fa530900 | -6.23282 | -45.33902 | 2025-10-01 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f9861736-f288-395f-866e-abd848f91a99 | -7.6262 | -45.45742 | 2025-10-01 03:28:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4adacd8c-9d2a-3374-bd93-67f02ae6556e | -6.81081 | -44.48164 | 2025-10-01 03:28:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 93a836f0-6759-3f2e-94a8-d5c5e1473dfd | -2.98128 | -39.93351 | 2025-10-01 03:28:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b67e2fc0-7c1a-3ab4-9247-25ff04ab624e | -6.20722 | -44.23738 | 2025-10-01 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 76ad094c-0442-3921-b7c4-cfdd102f0f24 | -6.63454 | -42.04078 | 2025-10-01 03:28:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8d48b88b-826e-3411-bfa7-64c4378c92dd | -5.80192 | -43.7388 | 2025-10-01 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4a148187-3ee6-36b2-882f-0d558db80f40 | -5.63734 | -43.91499 | 2025-10-01 03:28:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| d79a8221-976a-38db-bd19-c0c0725cc4ff | -5.83831 | -35.47905 | 2025-10-01 03:28:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ad157d5c-23f9-3a34-ad31-7dd00cd977cf | -6.23038 | -45.34526 | 2025-10-01 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README13.md)
