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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63bb812e-6666-3ba2-813d-8bac642b89f8 | -21.03472 | -42.52839 | 2025-08-24 03:21:00 | NPP-375D | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| da7deef4-be0a-30f2-b4a3-73390a05c2a0 | -20.8021 | -40.90752 | 2025-08-24 03:21:00 | NPP-375D | ICONHA | ESPÍRITO SANTO | Brasil | 3202603 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| df4048c4-6ad8-3df3-83f4-4a41f9ef9cbf | -20.77814 | -43.44399 | 2025-08-24 03:21:00 | NPP-375D | LAMIM | MINAS GERAIS | Brasil | 3137908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ab23268a-7f0e-34bb-a5c9-cae07f38568e | -20.36977 | -46.74947 | 2025-08-24 03:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7978dc5f-d9b3-394e-b2eb-19b55afc3eab | -20.35464 | -46.7501 | 2025-08-24 03:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79ca31b1-f29b-3688-96e1-ce7fee94b042 | -21.03925 | -42.53394 | 2025-08-24 03:21:00 | NPP-375D | ROSÁRIO DA LIMEIRA | MINAS GERAIS | Brasil | 3156452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 73d4ef34-5b73-30d3-97de-81c630e54a06 | -20.35907 | -46.74754 | 2025-08-24 03:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f9b19759-1388-3bf2-8002-c267a8109fd2 | -21.27359 | -43.75765 | 2025-08-24 03:21:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 2a9cc377-f9cf-38bc-aeda-f34aae2c7ea2 | -17.60398 | -44.30548 | 2025-08-24 03:21:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 53791241-fe5a-3490-bcba-68e4254a2efc | -21.78958 | -42.08501 | 2025-08-24 03:21:00 | NPP-375D | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c8c9b85d-7ebc-3897-a25f-02699bdc360e | -17.61191 | -44.30084 | 2025-08-24 03:21:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d2c327cb-7520-302b-898f-a333b96dd603 | -21.03492 | -42.53395 | 2025-08-24 03:21:00 | NPP-375D | ROSÁRIO DA LIMEIRA | MINAS GERAIS | Brasil | 3156452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| d29fa3d2-b320-32c1-b2f5-0c839fff91b6 | -17.39973 | -42.6191 | 2025-08-24 03:21:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 501a6aec-9b6e-3bb3-ac43-eef315fafba4 | -17.39184 | -42.62682 | 2025-08-24 03:21:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2028902c-296a-3f8a-82e3-5a3519689681 | -19.63653 | -43.18769 | 2025-08-24 03:21:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 723fe7db-d44b-32cc-a2ec-a1e04757b531 | -19.92416 | -44.21479 | 2025-08-24 03:21:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 9dd2e59c-9a9e-37b7-9cca-73727c92e021 | -20.36144 | -46.75282 | 2025-08-24 03:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e936cdf-caf6-3644-8ad3-d6c5e35de596 | -19.63078 | -43.18575 | 2025-08-24 03:21:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 4b26dc47-fb6f-3fa1-8bc4-f3a29c13bb6b | -19.92295 | -44.21999 | 2025-08-24 03:21:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7bd0c834-f546-3666-a19d-5bd7ee63bc55 | -20.90546 | -42.64588 | 2025-08-24 03:21:00 | NPP-375D | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 886fec1a-402c-3f0b-b7da-225617351c99 | -20.36354 | -46.74452 | 2025-08-24 03:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca779417-1926-341d-97ec-9775763c1c31 | -21.27458 | -43.75333 | 2025-08-24 03:21:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 30db512c-693e-3b11-8a7b-d3f5a55532e1 | -20.77917 | -43.4395 | 2025-08-24 03:21:00 | NPP-375D | LAMIM | MINAS GERAIS | Brasil | 3137908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e7dffb37-3540-32bd-84e4-39b8fb4e787a | -20.37178 | -46.74149 | 2025-08-24 03:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d67e50a2-ec0a-3b7e-9c50-ead38a7232a1 | -20.47011 | -42.62212 | 2025-08-24 03:21:00 | NPP-375D | JEQUERI | MINAS GERAIS | Brasil | 3135506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 97c7dd90-0327-3805-a128-b62cf8782634 | -20.90759 | -42.6454 | 2025-08-24 03:21:00 | NPP-375D | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 268f01f8-2012-3796-9ee6-008024ec4b27 | -17.82581 | -44.54819 | 2025-08-24 03:21:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4370a979-80cf-3cdc-9391-3650c8c77dc1 | -20.9744 | -42.86336 | 2025-08-24 03:21:00 | NPP-375D | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 511bef12-49bd-3dd6-87b6-7dd9a555a377 | -17.60674 | -44.29356 | 2025-08-24 03:21:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 33.2 |
| c518ba5a-25f5-3269-985e-8641fdcc707f | -20.36928 | -46.73647 | 2025-08-24 03:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1cdf9ccb-f8e4-3bd4-86af-87155c103ad7 | -20.40405 | -41.40314 | 2025-08-24 03:21:00 | NPP-375D | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 008219c3-359c-32b3-b778-38ed99f3d08a | -20.36559 | -46.75143 | 2025-08-24 03:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 84450389-dc6a-3fc5-9baf-bd901db82ad3 | -17.39283 | -42.62228 | 2025-08-24 03:21:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| be347706-33b2-32c9-b82c-98b77cb49c13 | -20.08106 | -46.11604 | 2025-08-24 03:21:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61fa5d76-99e7-3de2-82ed-c8ea8ab4d752 | -20.354 | -46.73783 | 2025-08-24 03:21:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5e72b3a-e6b0-3e9c-b565-c6971fc7fe34 | -18.70805 | -40.01009 | 2025-08-24 03:21:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6a3956e3-46c3-32fe-94f2-dedc76d7f6f1 | -17.59463 | -46.09735 | 2025-08-24 03:21:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38df48a9-ab2a-3436-b22d-23982cd408a6 | -18.7557 | -45.09868 | 2025-08-24 03:21:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1396e7fc-9c91-30b2-83b6-ead0b31d8727 | -20.96149 | -42.86836 | 2025-08-24 03:21:00 | NPP-375D | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1787dfe5-8a9f-3502-af61-c1671a1037aa | -19.87149 | -45.29168 | 2025-08-24 03:21:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d45316a1-9ede-34d0-99d1-6b1b188b2ab1 | -17.60537 | -44.2995 | 2025-08-24 03:21:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 87f54924-6c99-3808-b692-3f7fe5a69d41 | -17.39876 | -42.6236 | 2025-08-24 03:21:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f318c6af-0c7d-3266-a76f-fac13b3d068e | -20.96375 | -42.86695 | 2025-08-24 03:21:00 | NPP-375D | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 683fd9eb-6eeb-3b2e-a125-db983dba61d3 | -23.25581 | -46.63348 | 2025-08-24 03:23:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 44eada13-6e85-302f-9b65-8660cb1d35a1 | -23.37126 | -46.86637 | 2025-08-24 03:23:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 2b9839a8-e7f9-3c56-84d3-633fb60f46c4 | -22.3669 | -42.27623 | 2025-08-24 03:23:00 | NPP-375D | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c00172ea-1d9c-3996-b919-b867c5acec2a | -22.3678 | -43.378 | 2025-08-24 03:23:00 | NPP-375D | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8747e6e5-5e56-351e-b964-42668faa21a9 | -22.14168 | -43.65489 | 2025-08-24 03:23:00 | NPP-375D | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 9d834397-a0c4-39d9-a7d8-2c75f5617f47 | -23.25074 | -46.62568 | 2025-08-24 03:23:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5ee76f07-a8ee-3f18-a471-9585697e37b9 | -23.35453 | -45.80645 | 2025-08-24 03:23:00 | NPP-375D | SANTA BRANCA | SÃO PAULO | Brasil | 3546009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 99fbb550-2188-37df-965c-128c1e9bc4d5 | -22.22136 | -45.69113 | 2025-08-24 03:23:00 | NPP-375D | SANTA RITA DO SAPUCAÍ | MINAS GERAIS | Brasil | 3159605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 187378ed-7cc7-3e8d-9710-b7e09c24cb8f | -20.94043 | -46.83705 | 2025-08-24 03:23:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d2e8ebc-e626-342f-8dc7-9d4faf8ab643 | -23.30684 | -45.53371 | 2025-08-24 03:23:00 | NPP-375D | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 6b470bf8-5b7b-393b-895c-067e14b919b9 | -22.1407 | -43.65912 | 2025-08-24 03:23:00 | NPP-375D | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 6ba5dc79-319d-3888-9696-80a97fac680f | -23.32855 | -47.84366 | 2025-08-24 03:23:00 | NPP-375D | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| a150cb6b-4130-368c-833e-e4f1b01ae460 | -23.26372 | -46.6301 | 2025-08-24 03:23:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 34f7f60b-2da8-3137-825b-eb1138c8b237 | -23.62637 | -46.02791 | 2025-08-24 03:23:00 | NPP-375D | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| b864596e-6049-3d67-b819-4cba956d729b | -21.54212 | -44.17084 | 2025-08-24 03:23:00 | NPP-375D | PIEDADE DO RIO GRANDE | MINAS GERAIS | Brasil | 3150307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e63f5dfd-c33b-300f-a796-13c16fd8b133 | -21.54809 | -44.17234 | 2025-08-24 03:23:00 | NPP-375D | PIEDADE DO RIO GRANDE | MINAS GERAIS | Brasil | 3150307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dc8f66bb-f8e5-3cb6-9a29-51afe443ea0c | -21.54864 | -44.17359 | 2025-08-24 03:23:00 | NPP-375D | PIEDADE DO RIO GRANDE | MINAS GERAIS | Brasil | 3150307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 488aac29-a98f-3a61-b35a-4516811c5a44 | -21.54266 | -44.17212 | 2025-08-24 03:23:00 | NPP-375D | PIEDADE DO RIO GRANDE | MINAS GERAIS | Brasil | 3150307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 87d3794c-28fa-330f-a4d8-40fc6e5c8d95 | -23.32306 | -47.85026 | 2025-08-24 03:23:00 | NPP-375D | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 08f2a570-0854-391d-bdc2-4d95b144e3d1 | -22.45192 | -42.30737 | 2025-08-24 03:23:00 | NPP-375D | SILVA JARDIM | RIO DE JANEIRO | Brasil | 3305604 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 9277b641-e94e-30cd-b2a0-02aa6bc20cfe | -23.32666 | -47.85093 | 2025-08-24 03:23:00 | NPP-375D | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 4eadac7a-9807-3093-964d-a39a77919126 | -23.13126 | -47.03561 | 2025-08-24 03:23:00 | NPP-375D | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 1fda1f7c-4a94-3c3c-ac76-decedec722f8 | -22.72805 | -46.97068 | 2025-08-24 03:23:00 | NPP-375D | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5c378124-5c57-348f-b454-9800a1ec9240 | -23.62137 | -46.02084 | 2025-08-24 03:23:00 | NPP-375D | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| e2b58ca7-b099-3da9-a1c8-2e95b5e15789 | -23.31327 | -45.53448 | 2025-08-24 03:23:00 | NPP-375D | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| c4dcaa32-6b4b-38ce-affa-07f96dcd9770 | -22.14266 | -43.65062 | 2025-08-24 03:23:00 | NPP-375D | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 773caaf1-a00a-3ef0-87f4-5ab2031132b9 | -23.30533 | -45.53983 | 2025-08-24 03:23:00 | NPP-375D | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 17493d15-5dd2-383f-bde7-3bea513e6dec | -20.94278 | -46.82768 | 2025-08-24 03:23:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99ff0da8-5601-308e-8daf-f50cf180bd3b | -23.32501 | -47.84298 | 2025-08-24 03:23:00 | NPP-375D | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 07fda3a5-8228-35b7-b41c-101a0eb97d64 | -23.6201 | -46.02589 | 2025-08-24 03:23:00 | NPP-375D | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| c903d6a0-ffaf-38a8-8661-0150d58bb6d9 | -23.36939 | -46.86494 | 2025-08-24 03:23:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 087c9600-3c3b-3e17-9c00-07032da668b1 | -23.36468 | -46.86426 | 2025-08-24 03:23:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 6b2329de-34f6-35c0-b474-485b0be0e08b | -23.24918 | -46.6318 | 2025-08-24 03:23:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8e9f4198-3e1b-327b-9ba2-aac30eb39141 | -23.27965 | -46.56729 | 2025-08-24 03:23:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8b4ba325-648d-3bd9-84e3-23ed5c713f31 | -22.3675 | -42.27351 | 2025-08-24 03:23:00 | NPP-375D | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2ed99c05-e2a4-32f4-83f5-c55f51bbf15e | -23.49738 | -47.07607 | 2025-08-24 03:23:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f1ee81b2-0b38-3424-88d1-8bd20267e43e | -23.27831 | -46.57258 | 2025-08-24 03:23:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 19b0fc1d-6647-33e5-a285-6f5efa8518a6 | -23.62762 | -46.02289 | 2025-08-24 03:23:00 | NPP-375D | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 21ded2d1-29db-3234-a19f-777eb9421dcb | -23.25731 | -46.62755 | 2025-08-24 03:23:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9d4a92eb-0fe5-361b-bcbb-0c5b863d13df | -23.12084 | -46.84729 | 2025-08-24 03:23:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1fe915fe-099e-33d8-881f-a22a142567c5 | -22.21993 | -45.69699 | 2025-08-24 03:23:00 | NPP-375D | SANTA RITA DO SAPUCAÍ | MINAS GERAIS | Brasil | 3159605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 14d771e5-068e-36ad-9bf7-eb6b8e8b07f6 | -22.12611 | -43.24987 | 2025-08-24 03:23:00 | NPP-375D | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fa618e5d-d553-3795-8aff-10bf9c4de660 | -23.47056 | -46.81182 | 2025-08-24 03:23:00 | NPP-375D | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| fb8170f7-513b-358c-8bbd-62c156158a4a | -9.0046 | -65.6988 | 2025-08-24 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| d2c7a953-f6f2-3025-b7d1-1fb4fd41d05f | -9.1722 | -59.4629 | 2025-08-24 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| eb9df8cc-01d1-3fe4-8bb2-fe3e2f0b984f | -9.1536 | -59.464 | 2025-08-24 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 129.5 |
| f87b7a19-a1ac-35e9-afba-0f2e1bacc8f3 | -14.8157 | -47.9118 | 2025-08-24 03:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 9536476b-81fd-3d75-96ed-41f09ec7d705 | -14.8153 | -47.9343 | 2025-08-24 03:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 46.0 |
| fc85c27c-dd5a-352e-84d9-45a58fcb9220 | -5.4364 | -60.1779 | 2025-08-24 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| ffa5e96d-9916-334c-a8ed-81e0ea0bbea9 | -9.1535 | -59.4834 | 2025-08-24 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 106.2 |
| a68bbd30-fdaa-3932-8fbe-1e16f048b751 | -20.339 | -51.7062 | 2025-08-24 03:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 68.2 |
| c3bb61d4-9df5-3a52-ad98-ae59040a97ff | -20.3396 | -51.6839 | 2025-08-24 03:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 83.9 |
| e3a5ad8c-5bf0-3882-a9bd-9863c51a242e | -4.9605 | -55.8226 | 2025-08-24 03:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 072dd5b8-09ac-382b-b43c-5b0e996f8f7e | -16.7965 | -51.3637 | 2025-08-24 03:30:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 511b64c0-b2eb-3610-a127-903d42e9d47f | -9.0231 | -65.7169 | 2025-08-24 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| c986454c-b772-3f5c-bde4-d669c196e8d2 | -16.797 | -51.3419 | 2025-08-24 03:30:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| ca3c220d-6dfd-32f0-b175-a1c4d9b75644 | -9.1998 | -60.793 | 2025-08-24 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |


[Clique aqui para ver as próximas entradas](README22.md)
