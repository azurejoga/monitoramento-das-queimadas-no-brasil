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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1bb3083-ea41-3c07-9353-ee11936b9c3f | -6.0263 | -45.89117 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd2d86f6-ac65-3cfb-a4bd-13ccd142124e | -5.87757 | -43.15471 | 2025-09-08 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 62cf3d0f-a708-3cdf-9f56-3ce614dc1975 | -6.8793 | -45.53707 | 2025-09-08 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62ac9c3b-f14e-3ce2-a317-07b6670f5272 | -5.49047 | -42.66185 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3f69bd4e-a232-33a1-9846-0bc72de36231 | -5.57592 | -42.75802 | 2025-09-08 04:00:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a7778bcf-c55a-3e50-87e0-4acfd5b69ca2 | -6.20156 | -41.00636 | 2025-09-08 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 565f187b-3a93-36ff-85c1-122e4949b500 | -6.2515 | -43.50106 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2896ca0a-1a07-312b-8dee-bf290cd54ede | -6.38398 | -42.60613 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c179aa4c-a4e9-3de2-9fa8-6490537dbee1 | -7.54547 | -42.52402 | 2025-09-08 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b51c25f3-6d7a-3c5f-bed4-6e72c007fcc3 | -5.88121 | -43.15528 | 2025-09-08 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bce4a38b-957c-38a9-8982-d65d53390d91 | -6.60592 | -44.00848 | 2025-09-08 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f7d74cf-7e26-3782-b620-bd8eeb141345 | -6.40231 | -43.87953 | 2025-09-08 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a661bac9-fdce-38c0-95f9-e67bd0fdf5bf | -8.15848 | -44.8495 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5a2046c-c32f-36ab-a746-60be33e96dd6 | -7.63433 | -46.55947 | 2025-09-08 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38ae5146-32b0-328c-9c51-31e344cce646 | -6.4846 | -44.01406 | 2025-09-08 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e831c62e-e060-3940-9be8-8e4f232d4187 | -5.43709 | -42.81874 | 2025-09-08 04:00:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 40475211-5d02-3b58-8947-461581c5bd5b | -6.21525 | -42.59628 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 497e7eca-242c-32dc-b875-b15080ffa1b3 | -7.99403 | -45.46494 | 2025-09-08 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c25676f-977b-3431-8ba2-a3345c0d3f0d | -5.87536 | -43.96975 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 371a72e3-4f91-35d7-b0d0-4d3e37ff0222 | -7.1082 | -44.13725 | 2025-09-08 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 259274c2-0a69-3d89-b705-dddb81a43afd | -6.20885 | -42.45768 | 2025-09-08 04:00:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6ad8b38e-b34d-3d50-bbac-f54b17d34120 | -4.55782 | -40.34254 | 2025-09-08 04:00:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e0b7f0f1-12d2-3dde-987d-16cc1fe18b0a | -6.55436 | -42.93714 | 2025-09-08 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd42a385-00f5-3467-97b0-f48520993ff6 | -6.84191 | -52.85243 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 57a677cf-a654-333a-a18a-0fc98aff6a42 | -6.24324 | -43.71349 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca187494-40b5-3d45-bd17-c1b3f408139d | -5.06647 | -48.41877 | 2025-09-08 04:00:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5d7a164-0049-3646-b7bb-1632517d1e0c | -6.23536 | -43.50693 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7bade3e3-aea7-3dfa-8680-a1427d25f330 | -7.13504 | -44.79022 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afc2f09b-a9f2-33bc-8bf1-3fbbc61220bf | -5.94468 | -45.74826 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ef623e4-ca25-34ee-969e-0f8927f85d22 | -5.74008 | -43.7294 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd7e40bb-1083-3343-abd3-da1b145e8575 | -6.21759 | -43.29734 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19f213f5-fe40-36cd-8cc6-e779d3ec506d | -7.22192 | -43.98714 | 2025-09-08 04:00:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e2cd47e1-40e3-3423-853f-f33991f3a5c5 | -5.73635 | -45.3658 | 2025-09-08 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7b36480-b3cb-3913-a916-9ea2324d8f3f | -7.24305 | -44.84139 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71ff3007-4148-31aa-9d11-904709484e87 | -5.43821 | -42.58437 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 44411960-af28-374a-8d5e-675806cea90b | -7.9809 | -44.83181 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0f934a6a-b38b-386e-ba33-b5da424f1b85 | -6.36128 | -42.59021 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0992dd83-4b64-3cec-aeed-4f31bd97ab75 | -6.28293 | -43.33327 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c4a5e37-62ca-3991-bfb4-0d2fa41e3e21 | -6.26744 | -53.42392 | 2025-09-08 04:00:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a39693f-03ac-3a3b-a702-a0223db2a530 | -6.20506 | -42.48098 | 2025-09-08 04:00:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ae64a500-90d7-3162-96cb-13287a256ed5 | -7.62218 | -44.66601 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 532aeb49-9fa3-3173-8ffb-5dffc65b2702 | -5.44764 | -43.42854 | 2025-09-08 04:00:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87cfbfd3-82fb-3c40-969a-595f7329deb0 | -6.20062 | -45.03501 | 2025-09-08 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df1c8988-e860-3538-910e-23d5b2857ab5 | -8.03639 | -44.06182 | 2025-09-08 04:00:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c7cc01b8-b9d2-3037-8b73-4df9f46edd67 | -7.81393 | -45.41875 | 2025-09-08 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c741d52e-990f-3d8e-bfba-dc5e08ecc72b | -6.36907 | -46.40362 | 2025-09-08 04:00:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d37a7b24-52bd-3a39-a365-94f9f3933563 | -7.08277 | -45.1999 | 2025-09-08 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 73dc9665-1e78-3b8f-ae56-27af267f4571 | -6.19785 | -43.60648 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0a66501d-d167-3459-8e68-cb2b21d1ed3e | -6.4038 | -43.87053 | 2025-09-08 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efedd105-32bf-363a-a094-c29198f113b6 | -7.8438 | -44.85687 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6ad60a4f-c36f-3c45-8ada-2b81bbd5f06a | -7.8802 | -46.25762 | 2025-09-08 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 66c711b0-f027-3364-a239-a400cc7f68a8 | -5.63552 | -42.61793 | 2025-09-08 04:00:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b9eeaa23-adad-3bbc-a841-c1d3f654f759 | -3.31337 | -48.71978 | 2025-09-08 04:00:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 07bd08f1-6e58-3c71-9b0f-e18b8b525f54 | -8.19472 | -44.78207 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b497052-9b44-3b0a-9feb-e8d9147913f8 | -6.53205 | -49.50388 | 2025-09-08 04:00:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5096c5f0-084b-3a7b-9c39-66fc003c725c | -6.48505 | -41.76912 | 2025-09-08 04:00:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c2386fcb-dd64-311d-b591-dc2f4e6b9fe5 | -6.61423 | -44.00517 | 2025-09-08 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8cbcfaac-a88c-3b5c-9b78-57f53813e326 | -6.83824 | -52.85241 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b1e7a25-f1e2-3589-9f4b-d7fe4e156d82 | -6.21609 | -43.37609 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa48a81e-a0b2-39e6-96ee-f7fbfe404bc5 | -6.60894 | -44.01367 | 2025-09-08 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e4710f1-138a-312e-b50a-cd0206597007 | -5.87187 | -44.18427 | 2025-09-08 04:00:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 976574ed-d5d8-3e67-9f26-f7a08c5f014e | -5.80524 | -45.65307 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c198ba92-1ac7-3641-94dd-b4c7777241dd | -5.8551 | -43.8562 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9e0e5024-c742-371b-b80a-5397c324b71d | -6.92006 | -43.80298 | 2025-09-08 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19f27818-7370-30db-8dd1-ab93bb9574d3 | -5.08109 | -42.41808 | 2025-09-08 04:00:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 4f31e9f4-6efb-3e99-9251-c8bbc5fac815 | -6.08004 | -43.36005 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9823952b-975b-330c-944d-41a08802fbbb | -5.64066 | -43.11445 | 2025-09-08 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cb999da2-fc43-343b-9951-7f4936776c56 | -4.82622 | -42.7349 | 2025-09-08 04:00:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6eedd75e-1b9f-3a21-bd1b-9a8d016e61ee | -5.94226 | -42.963 | 2025-09-08 04:00:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 16c13ff1-002e-310f-84c6-8e705dc55b5c | -6.18129 | -44.7727 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e1fbf44-ac3d-3568-b0d2-8cea53879b49 | -6.22837 | -42.58226 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d0c08a72-9bad-3501-a245-670be2c14b8c | -5.94151 | -45.74903 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2aee0cc7-5499-3781-bd53-83b4e6975c03 | -6.59463 | -44.00626 | 2025-09-08 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 991b42e4-7e58-3aea-8ca5-ec2e83e4b755 | -6.17828 | -44.7415 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 89632965-af55-31ca-b1bd-c20a8df91a60 | -6.18555 | -45.42694 | 2025-09-08 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dec6d60-7dae-30f8-912f-699cbc809668 | -5.85206 | -43.85112 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 242a6904-e477-37dd-bfb5-14ce853aa32f | -6.6238 | -53.37882 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81aa9f86-2dc3-361a-8d54-d8e65f060a17 | -6.27439 | -53.42525 | 2025-09-08 04:00:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a840aa6f-b7d3-3865-9f80-63b849915a4c | -5.87464 | -44.17748 | 2025-09-08 04:00:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ab909f8-263a-336c-ab62-151c393fd7f5 | -6.97315 | -45.57357 | 2025-09-08 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55c7795a-dbca-386a-bfc4-65b81947b7c3 | -7.13987 | -44.57094 | 2025-09-08 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b1d75cf9-ebd6-3a93-b049-c933490d36f2 | -5.42025 | -42.8545 | 2025-09-08 04:00:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 5a51f37f-8532-3057-a27e-f250057df54c | -4.66188 | -46.35588 | 2025-09-08 04:00:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0d47c22-2e63-3e99-978e-a372c9143128 | -6.19993 | -40.99519 | 2025-09-08 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e3b9196c-b367-3637-9d5a-08ea9357a706 | -5.80323 | -45.66506 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad875b2b-de23-36d6-a4d1-c0b4d931af5c | -6.07934 | -43.36433 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34057422-caeb-3f0d-9034-8688ad6d39d0 | -6.25372 | -43.69627 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 785a1901-5134-3462-b59b-9c3fe07d8e15 | -6.21539 | -43.38041 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2842997-abec-35f4-ac4f-1b2188663d20 | -6.59915 | -44.00245 | 2025-09-08 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b11a28c9-983f-3845-9006-7bad9b256eda | -6.40608 | -43.88007 | 2025-09-08 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fbb1097d-c49e-3a72-acf0-e292e36d7a2f | -5.86042 | -43.84756 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 0d279ea9-4423-36a4-8da7-9ec6a9eb0611 | -7.62689 | -46.11182 | 2025-09-08 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 932c2b22-2ce6-3e65-b5d7-4dc945693d83 | -6.46111 | -43.94577 | 2025-09-08 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7b5293a4-a214-3bfd-8e49-54213ff1a02c | -4.41032 | -47.6099 | 2025-09-08 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13b63b11-cc72-38c0-91cc-16a2aa59088f | -7.09786 | -42.93729 | 2025-09-08 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6e902aa8-89c0-3167-bb3a-7ad541c5ad29 | -7.61733 | -43.87562 | 2025-09-08 04:00:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d603365-a915-39d5-91ca-0b2e272cfa21 | -4.90388 | -42.21701 | 2025-09-08 04:00:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c235893c-1026-37bf-8a05-f5615e2ac54f | -5.63843 | -42.6225 | 2025-09-08 04:00:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8a20fdd4-7c27-3f29-a1a6-0cb2a0e608fd | -4.56448 | -40.34353 | 2025-09-08 04:00:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f4f15335-7263-3ed9-bbe2-2c013c51cd38 | -8.19861 | -44.78263 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README31.md)
