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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de41af68-cb90-3386-9a74-d1e0432accfb | -5.96981 | -42.11929 | 2024-10-27 04:00:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bfce9a25-b6a4-387f-be18-8b62ff2fe2bb | -5.96919 | -42.12313 | 2024-10-27 04:00:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9d2f26e1-857c-32ed-9c77-915a72824af8 | -5.96858 | -42.12696 | 2024-10-27 04:00:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aefdabbc-1c69-31cf-a63e-a7724a64a508 | -5.96631 | -42.11871 | 2024-10-27 04:00:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a34a511f-5218-39f3-9f04-d8eb8bc7366c | -5.9657 | -42.12254 | 2024-10-27 04:00:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a910a759-7d40-3523-a5d3-5501d242c4f3 | -5.96508 | -42.12637 | 2024-10-27 04:00:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c8b39f3f-ce0b-3f58-9eb2-a6fa3112378c | -5.88407 | -42.56348 | 2024-10-27 04:00:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 077665c2-c26a-3b9a-9f8f-43d4af598467 | -5.88341 | -42.56756 | 2024-10-27 04:00:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e7b0af9f-4180-3298-810d-1b5bd8a23970 | -5.81916 | -42.73711 | 2024-10-27 04:00:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 97583a1c-5460-3cfe-9974-e3df30b23a6a | -5.78634 | -42.68967 | 2024-10-27 04:00:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8650d869-e621-3baa-9b54-fd3025f3a32c | -5.69077 | -42.37433 | 2024-10-27 04:00:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 36f7b54c-7813-3da6-b902-1126905f3e0b | -5.47624 | -41.93967 | 2024-10-27 04:00:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 93826c62-5024-3bf6-86b6-68595937f596 | -5.41926 | -42.83195 | 2024-10-27 04:00:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3d6af170-7dd0-36c4-aeb2-7efc84237f9e | -6.60275 | -42.06738 | 2024-10-27 04:00:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 45552b71-8f36-3d9c-9f86-32225869e766 | -6.59928 | -42.06683 | 2024-10-27 04:00:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dff38d69-0ef4-3800-b6cc-b4da4df38d1b | -6.51776 | -42.19516 | 2024-10-27 04:00:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 40197242-c404-37f9-824d-015a3cf34e4e | -6.51166 | -42.34196 | 2024-10-27 04:00:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7bf024e1-da75-38c5-aafd-5ffb87da729d | -6.5091 | -42.35763 | 2024-10-27 04:00:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a84981e6-821e-3bcf-8056-6bd2202c70c0 | -6.50752 | -42.34527 | 2024-10-27 04:00:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2502df15-d475-3209-839b-e86db4eb628f | -6.50624 | -42.3531 | 2024-10-27 04:00:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 76c229cf-434f-36bc-ab89-3fadec97b950 | -6.50559 | -42.35705 | 2024-10-27 04:00:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 78c9bd58-d4f0-363e-bd8e-485501a46a0f | -6.49922 | -42.35196 | 2024-10-27 04:00:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1e5f04d8-e69b-3128-a54c-2a36cd410a95 | -6.65238 | -42.20835 | 2024-10-27 04:00:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0a9a08e5-cdd2-3750-9c37-f6f24d5e36bc | -6.81523 | -43.28839 | 2024-10-27 04:00:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 270745e4-a6c2-3f51-9651-f5543417e868 | -6.81453 | -43.29266 | 2024-10-27 04:00:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| db8c63a0-4e14-36ea-811d-ce60e7390925 | -6.81087 | -43.29208 | 2024-10-27 04:00:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d9a277ee-9087-37b7-9103-c13a503b22f8 | -6.66812 | -43.54626 | 2024-10-27 04:00:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52f8c84f-b18c-3927-a02b-d8962b1e67b6 | -6.66515 | -43.54116 | 2024-10-27 04:00:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18465347-ed61-3262-adb8-033f17ddfacc | -6.66441 | -43.54565 | 2024-10-27 04:00:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9160591d-95f9-3715-8729-f92a09b0d628 | -8.71976 | -44.02486 | 2024-10-27 04:00:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 384b1673-dbe1-3e16-9dfc-09437b016419 | -3.18016 | -44.38095 | 2024-10-27 04:00:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4aacd44f-62c8-3e6f-9065-0e4b8aa10341 | -3.06709 | -44.33313 | 2024-10-27 04:00:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 0aaf872f-243b-3138-9b75-7c90e6e2496f | -5.70317 | -43.90906 | 2024-10-27 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 578872db-71ed-381f-a39e-62b113994635 | -3.06649 | -44.3368 | 2024-10-27 04:00:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e1c6a1af-59c6-3401-b6a3-aed01629020e | -4.70986 | -43.88158 | 2024-10-27 04:00:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd30bede-72f3-3da8-a045-1f10a035254a | -4.70907 | -43.88645 | 2024-10-27 04:00:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ae25129-e857-301b-93e6-fb79df446893 | -4.70596 | -43.88095 | 2024-10-27 04:00:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa25a2db-35b4-3651-8797-1f6949c24b61 | -4.70518 | -43.88582 | 2024-10-27 04:00:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fc07a939-759c-39c3-9243-126c9bf5fdf1 | -4.21918 | -43.62833 | 2024-10-27 04:00:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8e6958f-9822-3fd9-92c2-73921150f2a0 | -4.21857 | -43.62636 | 2024-10-27 04:00:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb9d3b73-7654-3d64-bbd1-26cce0bb6db5 | -4.21531 | -43.62777 | 2024-10-27 04:00:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c424fe8-f3a0-3393-ab1a-dc0ceab182ec | -4.2147 | -43.62577 | 2024-10-27 04:00:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce64efe0-9f77-3287-b5a8-9460a17cbf04 | -4.15891 | -43.70074 | 2024-10-27 04:00:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bfe927d-c527-3fe7-9541-14def6cca710 | -4.15503 | -43.70008 | 2024-10-27 04:00:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| eb1b9d6d-3394-31ec-9994-9a1a06480086 | -4.15424 | -43.70496 | 2024-10-27 04:00:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6fec533f-db11-37f0-bce4-3d7d02a67898 | -3.88583 | -43.14458 | 2024-10-27 04:00:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f75a827-5184-3fab-8d7d-26b168bb7372 | -4.75145 | -44.09466 | 2024-10-27 04:00:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f80e11fa-d47e-3cf6-a0c2-6d39ec253d56 | -4.75063 | -44.09973 | 2024-10-27 04:00:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e9e7d6e-3ed3-3f0c-833f-ea7ff3db6091 | -4.74751 | -44.09403 | 2024-10-27 04:00:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7bda2b7-d467-3335-874d-e1ad0283d537 | -6.10602 | -43.86567 | 2024-10-27 04:00:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2136a6ef-81f8-3429-a7d9-caf518ca60b5 | -5.73045 | -43.81633 | 2024-10-27 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 026dd072-0bbe-3894-a84b-8feb42cd7d9f | -5.72741 | -43.81104 | 2024-10-27 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e63af606-8b07-3110-973b-685ece42aef5 | -5.72663 | -43.81572 | 2024-10-27 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eebd2724-9356-3ba8-8402-994ea904e96a | -5.72358 | -43.81044 | 2024-10-27 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f56847ad-56fc-33c3-b078-f69b13b0a1a6 | -5.71807 | -43.84346 | 2024-10-27 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b6b7fa66-68e9-39cc-8ca8-638bb5589295 | -5.71503 | -43.8381 | 2024-10-27 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 19eee83a-0c6e-3047-893d-1cb4a730fc8f | -5.71424 | -43.84282 | 2024-10-27 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e7484964-ac0e-3ad7-ae56-58766bbdd5ce | -5.70702 | -43.90968 | 2024-10-27 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eeb4724f-4218-3247-ac50-304323586f8d | -5.69853 | -43.91317 | 2024-10-27 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12fc549f-6616-3217-bc85-4dc6ad46768d | -5.44887 | -43.58163 | 2024-10-27 04:00:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 219f7c96-d8b0-337f-8194-dc27b8da893a | -5.42085 | -43.37415 | 2024-10-27 04:00:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| baa81a21-6beb-3ebe-9e9a-71ef15bd8b0c | -5.42013 | -43.37859 | 2024-10-27 04:00:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6d7f25d5-941e-3cde-9787-d414c76e2a9e | -5.41941 | -43.38305 | 2024-10-27 04:00:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3f832d34-10a8-3339-a36f-c3079c2c575d | -5.41711 | -43.37352 | 2024-10-27 04:00:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f552542-3448-3097-9911-7be7c2a7d13d | -5.41639 | -43.37799 | 2024-10-27 04:00:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1e8071a2-ea9b-367c-8d10-33c1f3c76994 | -5.19669 | -43.30446 | 2024-10-27 04:00:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 220cbf20-87ff-385a-968e-4c6413927dbf | -6.45751 | -44.45198 | 2024-10-27 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e52bbe2b-d2ee-3317-916a-c18fb4eb6bcf | -6.3707 | -44.01333 | 2024-10-27 04:00:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb297684-7a16-3a67-bcf6-dad4cbeacc53 | -6.36689 | -44.01256 | 2024-10-27 04:00:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8d2c893-0be0-3cad-b7c4-3ed9633fac4b | -6.36611 | -44.01728 | 2024-10-27 04:00:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e8ec9da-51a8-3d75-aba8-2bbdf07c81c6 | -6.3623 | -44.01652 | 2024-10-27 04:00:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f4fb0d6-2b22-3856-a445-232e68aa23a0 | -6.27984 | -44.73312 | 2024-10-27 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b05de86f-19c1-3afa-b74a-d8d9cd3fdfff | -6.27927 | -44.73655 | 2024-10-27 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4bf55d5f-be8f-310f-9413-bf0d77630ebd | -6.21455 | -44.63179 | 2024-10-27 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4094b18-45c1-3129-8a8a-d29e0958b295 | -6.21369 | -44.63683 | 2024-10-27 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14d50a67-065c-3d3e-8a1b-dc76a5d94cab | -6.21271 | -44.63515 | 2024-10-27 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33302948-a275-3fd8-a9de-62fba35c3051 | -6.13897 | -44.05817 | 2024-10-27 04:00:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff627440-b4f7-3382-8115-ffcb64c38278 | -6.13822 | -44.06271 | 2024-10-27 04:00:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae57dc61-6397-309c-952d-71268e5a214a | -5.9716 | -44.00092 | 2024-10-27 04:00:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac1740cf-acdf-3e41-99da-58cb511eb2f7 | -5.92555 | -44.66636 | 2024-10-27 04:00:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f67f3ca-5e80-3c6a-962a-bfbee04d643c | -5.9236 | -44.72752 | 2024-10-27 04:00:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d26f0529-d4c6-32e0-a240-ca6669ea92dd | -5.8935 | -44.33017 | 2024-10-27 04:00:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f55fa722-d813-357b-ae30-aed8752d2e82 | -5.86137 | -44.674 | 2024-10-27 04:00:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d64dc81-d80f-3f9b-bc4e-ccbbb76133ef | -5.83134 | -44.90776 | 2024-10-27 04:00:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ba5ea9a-f462-3c57-b9f3-15477d88719d | -5.81417 | -44.13258 | 2024-10-27 04:00:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eba7eedc-c75f-3f98-8f9a-8a40bb985574 | -5.81108 | -44.12708 | 2024-10-27 04:00:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 88604291-4508-3459-acdf-0978f56a4ff4 | -5.81027 | -44.13198 | 2024-10-27 04:00:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f464bc5d-06ab-3c74-9a1e-10a9a949b712 | -5.80636 | -44.13139 | 2024-10-27 04:00:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42d78ecf-0146-3f61-ba79-034087a454ed | -5.62748 | -44.83332 | 2024-10-27 04:00:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5cf97f8-904b-3f9c-8105-9041d46612ff | -5.62689 | -44.83694 | 2024-10-27 04:00:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a9c2ebc-1aee-3054-b639-6fcaa40abb05 | -5.62398 | -44.82911 | 2024-10-27 04:00:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9ee607c8-66a5-39e7-aaef-ff03cd183d4f | -5.62339 | -44.83271 | 2024-10-27 04:00:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 520648b1-92ea-320e-9297-acb66eaa28bf | -5.6228 | -44.83631 | 2024-10-27 04:00:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 951d585b-b9df-3529-83bc-bb2b2e1c1c21 | -5.61989 | -44.82848 | 2024-10-27 04:00:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 91afb436-769d-381a-8c42-7dbf5da580b5 | -5.6193 | -44.83207 | 2024-10-27 04:00:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0e3e47a7-d9f5-3b1d-a0d6-da43586c3a19 | -5.61872 | -44.83566 | 2024-10-27 04:00:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8c4ae2bb-bdd1-3ccd-80af-50b2f376e29b | -5.61582 | -44.82777 | 2024-10-27 04:00:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e8c87f8-9e06-3647-95c8-838ebf15be73 | -5.61522 | -44.83138 | 2024-10-27 04:00:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c44c97c6-5a81-3d7d-97a8-adcc1a0f2cb3 | -5.27588 | -44.06845 | 2024-10-27 04:00:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c141ddc-dd16-330c-8249-501f4a8c1b4f | -6.59963 | -43.68148 | 2024-10-27 04:00:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README33.md)
