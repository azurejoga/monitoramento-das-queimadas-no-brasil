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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e03edba7-70e9-3030-a3dd-e13edee39c0b | -5.7127 | -43.83825 | 2024-10-27 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 806fe185-19d4-31c3-9b40-9e40c4e3d262 | -5.71212 | -43.84207 | 2024-10-27 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68c9c1b9-19c3-33dd-85ea-0234b991be77 | -5.70508 | -43.91113 | 2024-10-27 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8f89ef4-8703-3939-a1dc-b9857209ab4e | -5.69759 | -43.91387 | 2024-10-27 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 531914ce-f689-3f72-8e20-318b98048d09 | -5.44803 | -43.57946 | 2024-10-27 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 268b8fad-d02a-3509-9df0-d46cc7fac89d | -5.42112 | -43.37891 | 2024-10-27 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c4b5d4d-2186-3960-aff6-9064436d244f | -5.42052 | -43.3829 | 2024-10-27 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6a6a2d3-f00e-3b67-ac11-e531de60b819 | -5.41819 | -43.3744 | 2024-10-27 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b6ac5753-6294-3844-a1af-609cf0bb5766 | -5.41759 | -43.37838 | 2024-10-27 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ac23afe-7fd4-36ea-9a2f-1c96476e6b26 | -5.417 | -43.38235 | 2024-10-27 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ecdbf9d8-c367-3e2b-b9fd-5c8b5818b995 | -5.41467 | -43.37387 | 2024-10-27 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a94bab0f-fc5e-3031-956c-c63b70c59fd0 | -5.41407 | -43.37785 | 2024-10-27 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92ea5225-f6ba-31ec-b8d8-605ba3696105 | -5.19754 | -43.30284 | 2024-10-27 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fce57aa-d89e-3a38-b033-5c8208734e69 | -5.19716 | -43.30585 | 2024-10-27 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33f4b230-29ea-3639-9029-fa5b45fc34f3 | -5.62738 | -44.82965 | 2024-10-27 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f9259f4d-8b28-3caa-8a57-6f241392878b | -5.62683 | -44.83321 | 2024-10-27 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3246d161-6b17-39d0-a31b-5402c8766dbd | -5.62458 | -44.82557 | 2024-10-27 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a0f04c9-0056-3d9a-a350-a62921644ad0 | -5.62403 | -44.82912 | 2024-10-27 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 179c477f-afd6-3544-82dd-f12de8a179eb | -5.62348 | -44.83269 | 2024-10-27 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 00283d4b-18bf-3fda-a58f-89839d70dc2b | -5.62293 | -44.83625 | 2024-10-27 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f20acc16-075a-3707-81d2-33f396afef29 | -5.62122 | -44.82504 | 2024-10-27 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68da725f-c5d4-3954-9e9e-7c0b2a0bf1ef | -5.62068 | -44.82859 | 2024-10-27 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| adc58b40-f2dd-36d7-a9c8-ea40acdd5a68 | -5.62013 | -44.83215 | 2024-10-27 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f69c67d9-fa3b-3ca7-9188-4d1d3152129d | -5.61958 | -44.83572 | 2024-10-27 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b22f0ba4-e2ee-3e45-bd56-6cd678734950 | -5.61787 | -44.82452 | 2024-10-27 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15772cc7-d992-3422-a7d9-3edeeb2bac56 | -5.61732 | -44.82808 | 2024-10-27 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fc8b8994-781a-31a7-83c1-1912f0dac3a4 | -5.61678 | -44.83164 | 2024-10-27 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e3738ced-3583-3309-9872-98913af28490 | -7.42253 | -44.72416 | 2024-10-27 04:23:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b846430a-55ee-3b28-9318-f20e671df08e | -7.41912 | -44.72363 | 2024-10-27 04:23:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ea50692-35de-300a-8b33-4ee30d6b3c90 | -7.41572 | -44.72312 | 2024-10-27 04:23:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c2acead7-6025-3852-b67d-f53838eef336 | -6.67988 | -43.90003 | 2024-10-27 04:23:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 09cea3b9-a6f3-399f-864c-c25d27e650b0 | -7.19166 | -44.72295 | 2024-10-27 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f7ed612b-604b-36b2-a886-12cdf1be6987 | -6.90429 | -44.56393 | 2024-10-27 04:23:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86b045be-c3f6-32f6-a49d-b77940eb9f6c | -6.88123 | -44.75943 | 2024-10-27 04:23:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2a1fdf7c-d589-367e-bc28-17f74d91b737 | -6.88067 | -44.76308 | 2024-10-27 04:23:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfe0d9d5-19cb-331b-9a12-64cc4d5d2f9f | -6.8784 | -44.75529 | 2024-10-27 04:23:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 896983f9-da25-31d1-b50c-a083b2e83f5c | -6.87784 | -44.75893 | 2024-10-27 04:23:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d88e8b55-b66b-3d88-8b2c-140da4626d51 | -6.82023 | -44.47176 | 2024-10-27 04:23:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60f929e8-b3ab-3b73-b850-ad520648415b | -6.81681 | -44.47124 | 2024-10-27 04:23:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3da1eb6c-c702-3d33-aeb2-eb02ff974152 | -6.81339 | -44.47073 | 2024-10-27 04:23:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cd3dcb02-5c48-3541-b404-cc68e8c81177 | -6.81283 | -44.47443 | 2024-10-27 04:23:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1096c71d-d491-31d0-ae6d-b7eab971aaee | -6.80941 | -44.47391 | 2024-10-27 04:23:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 08dc943d-c9e2-34bc-af4c-2c324e293eaf | -6.72476 | -44.68651 | 2024-10-27 04:23:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f7f80e7-8657-36d9-a287-94512c6ad4cb | -6.7242 | -44.69016 | 2024-10-27 04:23:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b721dafa-0a8b-30cf-a3b3-5131461ef61d | -6.72379 | -44.68677 | 2024-10-27 04:23:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68cd5590-348a-3000-826b-6024782efdfb | -6.72323 | -44.69041 | 2024-10-27 04:23:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 581851fb-01ce-3d30-af4d-7f270c0c98f7 | -6.7204 | -44.68625 | 2024-10-27 04:23:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ee41267-1c65-391e-a5d7-d66d3bbb004f | -6.61677 | -44.79689 | 2024-10-27 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28f912c4-8509-3b32-b25c-e56c735b1f55 | -6.59275 | -44.69652 | 2024-10-27 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6f0baa3-9f47-37b8-8683-b4f814ccbb02 | -6.58937 | -44.696 | 2024-10-27 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8988b6a2-e424-3881-89e3-3932678375e4 | -6.97677 | -45.21507 | 2024-10-27 04:23:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a62875c-511b-329b-8861-0ef86cedab30 | -6.91832 | -44.90939 | 2024-10-27 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78a3cec8-595a-3387-bfc7-80c39fc6ca5a | -6.87521 | -44.88823 | 2024-10-27 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 128bfdd4-2dfd-3ce6-9853-c5027a91d1b9 | -3.0804 | -45.65372 | 2024-10-27 04:23:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36390439-fb98-3f96-bb22-4c9759092fdd | -3.13327 | -45.3173 | 2024-10-27 04:23:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ff4f85a-fc3c-3844-a5b0-1c69e8198d9e | -3.1305 | -45.31334 | 2024-10-27 04:23:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f533879-cc0b-31b7-84a9-68fa6cbae119 | -3.12996 | -45.31678 | 2024-10-27 04:23:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22ee6068-5503-3ecc-b008-efe9d01d1f2e | -3.12942 | -45.32022 | 2024-10-27 04:23:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1fb33f8-307e-39cd-8d0d-17b21ff491ce | -3.1272 | -45.31283 | 2024-10-27 04:23:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 658f9e67-f27c-3bc2-81a1-9df8833313a1 | -3.12666 | -45.31627 | 2024-10-27 04:23:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e3b3d95-2c73-329b-8ab6-268035b2608b | -3.12612 | -45.31971 | 2024-10-27 04:23:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4934e6f-d00b-3653-a5a8-8e7d45043877 | -3.1239 | -45.31232 | 2024-10-27 04:23:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f35ba68-bd93-39e1-bf67-91ddb04b176e | -3.12336 | -45.31575 | 2024-10-27 04:23:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 712f5772-fde6-3883-b16d-4f2468f7c001 | -3.00729 | -45.12473 | 2024-10-27 04:23:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b50bd211-3305-3606-8e9e-a4bc0fdd7ccc | -3.00399 | -45.12422 | 2024-10-27 04:23:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0082ca08-6647-3b37-85f0-0d5b91c8cbaa | -2.86753 | -44.9967 | 2024-10-27 04:23:00 | NOAA-20 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b75010d-398f-3f13-8491-6cfec4acfa2a | -2.86699 | -45.00014 | 2024-10-27 04:23:00 | NOAA-20 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98098ad4-a2a3-3d6a-8129-4b9eafc59443 | -2.86645 | -45.00359 | 2024-10-27 04:23:00 | NOAA-20 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45d9ebc5-bd7a-376f-842b-236ec7124764 | -2.86422 | -44.99618 | 2024-10-27 04:23:00 | NOAA-20 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1dc1a227-78c0-3cfb-888d-a246ed153fa5 | -2.86368 | -44.99963 | 2024-10-27 04:23:00 | NOAA-20 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31a15a42-8138-354f-b3d2-cad40814a300 | -2.86314 | -45.00308 | 2024-10-27 04:23:00 | NOAA-20 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fc2c62e-8666-3511-bb6b-69eccef1121c | -2.86037 | -44.99912 | 2024-10-27 04:23:00 | NOAA-20 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3fc6ff70-0fbe-3655-b7f3-64b4c8da5e0d | -2.85983 | -45.00257 | 2024-10-27 04:23:00 | NOAA-20 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 227955ff-b468-310d-bb5f-1d75bd6e75a9 | -2.85706 | -44.9986 | 2024-10-27 04:23:00 | NOAA-20 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbd5afc4-9c3e-397f-9edb-60fd8a021fbf | -2.85652 | -45.00205 | 2024-10-27 04:23:00 | NOAA-20 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c7cf758f-2327-3dbe-942f-457286155d12 | -2.85375 | -44.99809 | 2024-10-27 04:23:00 | NOAA-20 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e4c8e01-0e5a-3706-9c66-c111da56651a | -2.72066 | -45.15368 | 2024-10-27 04:23:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 483bbb12-2d27-3f7e-b592-36e2d60a6fec | -2.46207 | -44.94102 | 2024-10-27 04:23:00 | NOAA-20 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5d622dd-06ad-33e7-8f2e-5666e6145f0b | -2.45653 | -44.93311 | 2024-10-27 04:23:00 | NOAA-20 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a02255f-c7a7-3061-8387-25832bdcb360 | -2.45599 | -44.93655 | 2024-10-27 04:23:00 | NOAA-20 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3ac3b07-50f9-302b-9c19-ce1a0c2eb309 | -3.60018 | -44.78796 | 2024-10-27 04:23:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 983f65c2-c9ed-3989-bd9b-0ab5abd4c5b4 | -3.59964 | -44.79145 | 2024-10-27 04:23:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4141081-25e9-3094-b741-33ae78b0519a | -3.45396 | -45.41638 | 2024-10-27 04:23:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9a28365-15fc-35b5-8c71-0cce94287b37 | -3.45342 | -45.41981 | 2024-10-27 04:23:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8729acbb-3540-3175-856a-161161e73aee | -3.42473 | -44.84605 | 2024-10-27 04:23:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03e14321-913f-31b1-b149-5595ea79863b | -3.40274 | -44.48446 | 2024-10-27 04:23:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41a4980f-860d-38bb-a5c6-edf175f02632 | -3.40242 | -44.98821 | 2024-10-27 04:23:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ef0a756-b781-3190-8246-d2e07a04b562 | -3.3991 | -44.9877 | 2024-10-27 04:23:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1712f131-90fa-3267-89c0-7deab0829106 | -4.95127 | -45.92291 | 2024-10-27 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca4baf23-0ebd-38fb-9ec0-adccdf0cb171 | -4.95073 | -45.92635 | 2024-10-27 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9822d031-89ca-304a-9696-b40eb9487673 | -4.91422 | -45.8572 | 2024-10-27 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60032e80-2e6a-3583-90fc-2079d8d6a3d7 | -4.91368 | -45.86064 | 2024-10-27 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1628eb0a-5213-3d4f-91ad-93ac6abb1228 | -4.90947 | -45.71151 | 2024-10-27 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e4104d7-a687-33a1-8f92-33f1080ee92a | -4.90671 | -45.70755 | 2024-10-27 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b8c14e0a-c3ce-30cb-9c70-1f1c42b0220c | -4.85599 | -45.85828 | 2024-10-27 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9e62916b-0bf2-385f-be39-b3a2757365ba | -4.77056 | -45.9259 | 2024-10-27 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3edb0ab0-5bf7-3f50-bbea-29ecaeafae7a | -4.18956 | -44.97227 | 2024-10-27 04:23:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e3dca3cf-bc6d-32fe-a793-00552fd3fe23 | -3.90193 | -45.03032 | 2024-10-27 04:23:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0802ea39-222c-34aa-aaef-365e8543fe57 | -3.90139 | -45.03378 | 2024-10-27 04:23:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2bb4ded2-a752-373d-9747-946fa30faa73 | -3.89862 | -45.0298 | 2024-10-27 04:23:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README42.md)
