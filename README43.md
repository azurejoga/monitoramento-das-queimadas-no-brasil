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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72c3774b-d2a0-3519-ba9e-2556b78d0594 | -4.90482 | -43.46771 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 76f2268e-b68b-3bc2-91e6-66120bd67051 | -5.00321 | -44.49458 | 2025-10-15 04:55:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f38c1c32-c45b-3353-88f7-9864735770ae | -3.4266 | -50.24694 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31861407-0d2d-328c-9a84-468546b033ca | -2.81792 | -49.21252 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0513448-8166-32ef-8830-49af42944846 | -2.71494 | -48.33721 | 2025-10-15 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 394f8348-9d11-3d6a-bd63-3c44111a80b2 | -3.3883 | -50.2795 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e0f70e4-f5da-3235-80a5-7e09523b9d87 | -3.43681 | -50.25276 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea78b947-f6c6-39cc-a4c4-27e8bb5c8fdb | 2.04741 | -55.83502 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ca9c659d-a240-378d-8f3c-94836d90a6fa | -4.55682 | -46.43367 | 2025-10-15 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08a9ba57-7a5a-3ad3-a9be-2ca5cf9a2dbf | 1.86263 | -55.70366 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 650ba70d-0781-3e7c-87fe-100f9a11a43e | -4.13919 | -42.21337 | 2025-10-15 04:55:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 199a9749-0c7b-3e8f-bfa9-22fe214e740b | -4.89326 | -43.46583 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c5a444e0-6c17-32bb-8055-7c48a7199812 | -2.55143 | -48.40418 | 2025-10-15 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe5a39cf-1c1c-31ea-8f7f-30feb993914f | -3.59402 | -49.43565 | 2025-10-15 04:55:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 956ab5f2-94d6-3201-a6a8-3b4ab36aab76 | -3.02142 | -50.45038 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ac020d1-561d-3e95-b89d-79c7cb5da45a | -8.21806 | -44.04448 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8fcf5a32-31a4-32da-bf39-7874909fb28a | -5.47456 | -44.64058 | 2025-10-15 04:57:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cf81acc-d23a-3133-a553-160b383d6575 | -11.71032 | -44.27505 | 2025-10-15 04:57:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 762d7506-dd4e-3408-839b-dc8a5d26a3c5 | -6.05558 | -41.90065 | 2025-10-15 04:57:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| c2c73fff-ce51-329b-b88a-3bea01277e49 | -5.24387 | -44.46549 | 2025-10-15 04:57:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 023e5d3e-9590-39fd-88ea-a3505634e878 | -6.82531 | -44.64769 | 2025-10-15 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99ca5999-ea35-31d3-b581-f82b5cde462e | -10.05308 | -58.43447 | 2025-10-15 04:57:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6359f84-dbef-3206-97bf-31a8bec277b7 | -8.24432 | -43.3361 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 3b465699-20b4-3ed6-844c-07e1ea126ae7 | -5.27682 | -45.17064 | 2025-10-15 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97dada9f-a3f0-38dc-a4a6-8e4e6e6d68a6 | -5.44115 | -44.22734 | 2025-10-15 04:57:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 22ebdb75-3103-380b-8ba1-65a9266657ae | -8.19914 | -44.10037 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3626b651-6b58-3c58-b44b-909f302ab7b8 | -6.4618 | -41.83953 | 2025-10-15 04:57:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 072ebf9a-24ee-347c-8ddd-ab3c6d1b8950 | -7.57016 | -43.84004 | 2025-10-15 04:57:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d5bfb889-688d-39df-be6c-f03753b797e5 | -5.86307 | -43.87372 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c6a272f-261b-3333-810c-0d4f9a14a616 | -6.63377 | -43.92143 | 2025-10-15 04:57:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cf5542c3-0cee-37d0-8a59-b360c28e8e77 | -5.95113 | -43.75457 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2ea9cbb7-bcf7-3633-9b50-c6bad38f91c6 | -5.79663 | -43.891 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26b84816-8b7e-31d5-a112-61028806f2a3 | -8.21726 | -44.09827 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af744311-fbb2-3dc2-8bc1-b58e6b93d2f5 | -7.753 | -42.45141 | 2025-10-15 04:57:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ac5a1a28-eded-3206-ad5c-ddc1e5a29d4f | -8.21401 | -44.03394 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36f1c219-96c8-333e-999f-f02d5bfb6409 | -8.45983 | -44.18979 | 2025-10-15 04:57:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 5296a122-e6c7-3e39-8729-415c68c4566e | -7.94629 | -44.13107 | 2025-10-15 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6e5d1d5f-8d1b-3c3a-9d82-194774a8c8a4 | -6.35584 | -42.66844 | 2025-10-15 04:57:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ac1bf156-5c03-361b-b1aa-131380925d72 | -8.22071 | -43.32079 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 34dc6f56-6e02-388e-961b-3e9162a7120d | -7.1836 | -41.39625 | 2025-10-15 04:57:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 10613299-9ee5-3762-8c28-8d0d05de10a4 | -8.21063 | -44.00902 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1641902e-2496-3818-a337-e09f828aeb1a | -5.86941 | -43.87006 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9fa58cda-26c9-3d79-b219-82b25a8ce290 | -7.94521 | -44.13932 | 2025-10-15 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e5258fb7-ab09-3c08-9db1-63d0ededfac6 | -8.24867 | -43.35066 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 11f1d0bc-7e5f-35bd-8b70-8b8bfb036580 | -5.42536 | -44.22326 | 2025-10-15 04:57:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 91671328-2891-3004-afc3-955246f2f775 | -5.1684 | -46.27667 | 2025-10-15 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae9c2c57-c641-3da9-8e0a-b7b94b41e846 | -8.22017 | -44.07463 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc22e8c0-76fc-3d14-a20c-75bcdae65c36 | -5.56663 | -42.99788 | 2025-10-15 04:57:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| bbbd3de2-753c-38ed-ad20-6855341c796f | -5.19778 | -46.1407 | 2025-10-15 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ced893d-c46d-30ad-b8a1-8df4f7a75eb0 | -6.0571 | -41.88964 | 2025-10-15 04:57:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 7e67d805-35c9-3d0f-adb9-3c7d6ecf028f | -7.94051 | -44.13026 | 2025-10-15 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f49e7ab0-3ead-3d9b-9b08-f01eb70810c5 | -6.17531 | -42.61724 | 2025-10-15 04:57:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5dad91d2-7e8f-3eb7-9f11-de006c43adc4 | -8.21513 | -44.02555 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c150e6c8-f9d6-321b-82fe-5b577e1f3870 | -6.45732 | -44.58003 | 2025-10-15 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 40f64144-db95-3135-aed5-e1d8ed571ac6 | -8.82449 | -50.05903 | 2025-10-15 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df2e8c53-3f43-38ce-95a2-2492e0306be1 | -8.21814 | -44.04749 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9149661b-9aa7-3ee3-a1cf-9b4e44ef208e | -6.22172 | -47.03633 | 2025-10-15 04:57:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8dd8ad7-1ed5-3710-81a2-8e4b80e32fb8 | -7.2572 | -44.91447 | 2025-10-15 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 965ef52e-492c-34d2-b33e-7b219e399307 | -5.18755 | -46.17746 | 2025-10-15 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24d78fa1-80f5-3d29-a128-d15cf42dd891 | -6.59281 | -43.92047 | 2025-10-15 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a9185f5-5f08-3999-945a-895f03a59e27 | -6.05534 | -41.90541 | 2025-10-15 04:57:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| fb7fa469-0d8e-38c7-bdff-2d72c8297772 | -6.88967 | -43.96443 | 2025-10-15 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fb6eb4e-6eb8-3504-a5ea-34af69079939 | -5.47156 | -44.64353 | 2025-10-15 04:57:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6f2f4e4-34a7-31f5-a15a-294f7c83c6e4 | -7.16324 | -42.5071 | 2025-10-15 04:57:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 56b129aa-21f7-3790-8197-f43d2ff7fe59 | -4.91384 | -46.71175 | 2025-10-15 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c738a0ce-8118-32f6-98c9-76938825cbc0 | -5.92745 | -42.82251 | 2025-10-15 04:57:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| dde49f70-d903-3b56-87c4-afd9950ef2ad | -6.44627 | -43.8181 | 2025-10-15 04:57:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8665d877-baff-3b35-a0a4-a5831e791edb | -5.47709 | -44.66217 | 2025-10-15 04:57:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2abc069-c67b-3975-8bf1-b0e3406f06aa | -4.61669 | -49.544 | 2025-10-15 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64e8d487-fe76-3f97-86b8-205ba68494da | -8.97572 | -61.97551 | 2025-10-15 04:57:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07cc40a8-37b1-3da3-a499-81b4565a6d15 | -8.22005 | -44.07751 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f27b5100-9f26-36b8-b60d-bd74f789d220 | -5.43105 | -44.21846 | 2025-10-15 04:57:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 135a3ed4-f6d8-38f9-8734-825b4b6da25d | -7.95622 | -44.14506 | 2025-10-15 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 00af641d-f582-36bd-8dae-d5953fde9c9c | -5.89305 | -43.74931 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f18e4e20-9866-3569-a88a-d4c1a87f6343 | -5.681 | -46.42405 | 2025-10-15 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0fce289-c9d9-34e7-8842-4c49ac512993 | -8.21859 | -44.0871 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e8f33b8-197e-3ca8-add8-c667a08e2ca4 | -5.59332 | -42.84369 | 2025-10-15 04:57:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b1bf79fe-c56e-3f8f-bebb-e7803f0c916c | -8.4652 | -44.19391 | 2025-10-15 04:57:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1ab80d8c-ab8e-3b19-917c-2831f6d57924 | -6.52584 | -42.20101 | 2025-10-15 04:57:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 30fcba8f-5b74-3e5b-a3ad-0fa97d3fdad6 | -5.65105 | -45.87407 | 2025-10-15 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b801fa9a-c701-3510-a412-a6c05c068018 | -6.53238 | -42.20095 | 2025-10-15 04:57:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f4ba7e10-6935-3ebb-ba8f-721787745c94 | -5.44167 | -44.2236 | 2025-10-15 04:57:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7567dd53-f59b-3da3-9d7f-bd0120a7d360 | -8.24374 | -43.34063 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 53c78b94-0eaf-32e6-924e-6cce73df1a49 | -6.17474 | -42.61205 | 2025-10-15 04:57:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 650d4e3e-e338-31bb-8394-1b99fca6cd65 | -7.94466 | -44.14342 | 2025-10-15 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f6c2232b-4b90-3274-84b3-4980ea648eda | -6.84637 | -44.37006 | 2025-10-15 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7ed001b0-6d40-3dea-bd65-7d2d8dff8ffe | -5.24782 | -44.47672 | 2025-10-15 04:57:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 742d1d85-dcea-3451-823d-a55a80261c4b | -5.89358 | -43.7453 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ea155865-a92f-30d7-87ec-dfc8b79a5e04 | -5.89218 | -43.74963 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 86ee5233-96c9-37d2-b466-cc4f484f1e70 | -6.61046 | -43.61538 | 2025-10-15 04:57:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| efc4d9a9-a77a-3f3c-b82e-366db5278021 | -5.4361 | -44.22288 | 2025-10-15 04:57:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3cba3b7a-7475-38d8-9043-3ffd0e849535 | -5.60383 | -46.24304 | 2025-10-15 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d32ef22-b725-3a59-a89e-d032dd42db8d | -5.34684 | -43.74145 | 2025-10-15 04:57:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 01306af6-b191-3fb2-afce-afe0658c6d75 | -7.48764 | -42.14777 | 2025-10-15 04:57:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 72433bcd-fda2-300f-b895-8d23641a24d0 | -6.05483 | -41.90615 | 2025-10-15 04:57:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 882c65de-6a9f-3f99-9d5b-4552b8e24146 | -8.21859 | -44.04025 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5cbba7e7-e07f-3e7b-9ff6-093807d1a732 | -8.20788 | -43.32363 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 409ffb5d-a845-3bb7-b99f-5cdc2b02482b | -5.63367 | -42.68351 | 2025-10-15 04:57:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c830f192-d0d4-35af-87b9-95602b86412e | -8.23822 | -43.33515 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 60c046a9-b96e-3bc5-ab96-b0405cf78b80 | -8.28742 | -43.44328 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README44.md)
