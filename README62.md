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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd3a880f-b969-3ae1-9cb7-4fb91474140f | -7.75579 | -46.99793 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a50d4d31-26dc-301f-9982-3c49386c0bab | -4.31254 | -48.08941 | 2025-09-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ba3dbcb1-8b1c-341b-9e68-18e60c386d25 | -7.82337 | -44.80329 | 2025-09-29 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b75e46d-e4ef-35e8-abd8-7fc1ce2ac927 | -6.25781 | -43.63426 | 2025-09-29 04:57:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af47f1f2-a16a-3b83-b531-257007c266b2 | -6.5278 | -45.17899 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56c78e0f-4cdf-36b6-887b-aee81d2a2ddf | -9.40247 | -54.70434 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48b37d2d-5cac-3320-ad2d-3810a43c3d75 | -5.86761 | -45.76711 | 2025-09-29 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 874acfc9-c5df-36c9-8d6c-0f18f360f3d0 | -8.87139 | -46.61426 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 806092ca-74ae-32ce-b1a9-425aeac926d1 | -4.24961 | -46.94574 | 2025-09-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a01d0fd9-4d33-3089-a2f7-0c0fc99d1c51 | -9.46734 | -52.00468 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0b3d09f-33d1-37a5-bb90-3b674745afef | -5.24682 | -45.35662 | 2025-09-29 04:57:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 29231f02-8660-3ecb-b21e-2282288eb64f | -10.76776 | -45.3752 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16763b00-cb2a-32f0-a43b-e36b38a3a909 | -9.79942 | -46.93859 | 2025-09-29 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 00acba45-df06-3bd6-bedd-e9180a302717 | -5.96763 | -43.27352 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 8.4 |
| e32a4754-7085-382b-b6db-d83cb992fec5 | -6.62577 | -44.96409 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e01cd319-de50-3304-a031-7c08b4f61954 | -7.81463 | -46.99613 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7dfc7607-c967-36ec-9e5c-3605de11d376 | -3.80162 | -52.04144 | 2025-09-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7ee8481-7f38-3585-9a55-930d4b64894d | -4.31313 | -48.0855 | 2025-09-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e52d9dcd-7b16-3be2-8bb0-a34255486d6c | -7.28919 | -42.83713 | 2025-09-29 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2f7c92ef-85d4-3418-a44e-18eba8144262 | -7.46839 | -46.28852 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a278ded8-92d3-376a-924c-312a7a37195a | -7.44364 | -46.99136 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ece49f3a-773f-3544-9a51-ea11a7846a09 | -10.40318 | -48.14413 | 2025-09-29 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7c1219c-f896-3b4b-8324-13b58d7b6ec3 | -9.44772 | -50.90165 | 2025-09-29 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 293d993d-cdc9-3f82-ae82-1afda45b036c | -6.06167 | -42.48033 | 2025-09-29 04:57:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 5a39908a-f464-39bf-bd54-5d971cf281fa | -10.81409 | -46.66975 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d33690a9-5365-32a6-839c-91ce16a6ebfa | -6.50139 | -44.12296 | 2025-09-29 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89a3297a-363d-3b19-985c-2aeea4150399 | -8.87102 | -46.61704 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2cd4486b-e323-3277-9e32-f6ba25ff2637 | -8.88164 | -50.90625 | 2025-09-29 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aa4cd05b-8d4c-3c8c-baac-8bb50a38846f | -5.72137 | -42.85934 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2c77336a-c043-32d5-bb7a-641d091cd180 | -6.19212 | -44.29869 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 20d3dd18-88aa-36c0-b87d-2235c07c8e57 | -5.73916 | -42.8661 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c69fe937-76de-32ee-aec1-f3cc3dceb267 | -5.73425 | -42.67758 | 2025-09-29 04:57:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| af910400-73b3-3979-8b0f-bc3d05bf727f | -4.7143 | -41.99331 | 2025-09-29 04:57:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 7e93b8dc-2456-3d36-9f45-c10dfea3a9f0 | -7.23053 | -44.77877 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 6176f8fb-efa6-31a6-9eb4-f49b16ccfc7a | -3.25546 | -50.111 | 2025-09-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e21e398d-019b-382d-a283-9f081abcc44f | -4.70298 | -41.98108 | 2025-09-29 04:57:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 3ebf5d89-94ec-31ee-9188-ecf3bfd8d577 | -11.40451 | -44.90527 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f3d3f595-a863-39b6-8da7-189c9710871b | -5.7877 | -42.64992 | 2025-09-29 04:57:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 27d9408c-d4a4-3289-a3a1-c732535eed26 | -10.28565 | -45.19139 | 2025-09-29 04:57:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d1d6181d-c05e-3175-9c53-19e57d8415c9 | -4.28946 | -48.2704 | 2025-09-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| db4fb11e-55f5-3af0-81ed-05de411d874c | -8.72282 | -50.04392 | 2025-09-29 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdae7329-a903-3003-be76-a5c4f7b43c10 | -4.26326 | -48.55283 | 2025-09-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 67746e24-d323-360f-9808-fef36b411a23 | -6.28302 | -42.48634 | 2025-09-29 04:57:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2474ad74-30c5-3fd2-aa5c-d4a78a165dce | -10.79684 | -46.68274 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 66294642-731c-3a72-ab0a-b762c634523c | -7.30727 | -43.81432 | 2025-09-29 04:57:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16f687b8-11dd-3a38-a284-c3e5b33d989b | -9.40355 | -54.69739 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 834637e2-564d-3f7f-bee1-0110538645f0 | -7.58746 | -44.80127 | 2025-09-29 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8df7de7-e9ed-3053-a55d-c34468d62eb3 | -7.80947 | -46.89262 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ef588253-db51-32d9-87f7-2f9516e86a1c | -4.22806 | -50.39154 | 2025-09-29 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a53f5f6-c12e-3333-9fa6-eeb5e36299f0 | -7.38283 | -47.03893 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 22f2940d-1178-3abf-ac15-2b6395cef0f1 | -9.86468 | -47.73508 | 2025-09-29 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a484e85-ece6-3c4b-8936-1bd90027a4a3 | -10.44632 | -49.17776 | 2025-09-29 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebb12448-28dd-37cf-a73d-fc675d6a9074 | -9.05236 | -46.70788 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| acf890e3-578f-358f-a627-8aa108a93bc2 | -7.76346 | -45.74372 | 2025-09-29 04:57:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9095d963-a1c9-3af0-a058-c5f302e4bd96 | -10.81526 | -46.66059 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78375f02-1501-3bea-97d0-92c6042e6b93 | -7.49712 | -44.29919 | 2025-09-29 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55a42221-a126-378a-b0e5-74b54f14a627 | -8.86641 | -46.61343 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1c774a20-0618-3694-8f3b-29ff613911fa | -8.15928 | -46.39629 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 19241646-69fd-36f1-8408-215106a4fc44 | -10.8317 | -45.39904 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0e30bd2a-46f9-3f45-bb5b-ef5c1f2004f4 | -9.75724 | -47.79022 | 2025-09-29 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2943cda5-5fe8-3469-ae18-0ea0495e2908 | -5.08928 | -45.48546 | 2025-09-29 04:57:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0afbd51-e314-31dc-8ad1-364ef2922225 | -6.82895 | -44.83009 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0fdb7b4b-4ee1-394e-9b65-3493b316683e | -9.082 | -50.80815 | 2025-09-29 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb4a8cd4-5f3c-3dfe-b845-2e9d2b678d14 | -8.30025 | -45.49609 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 9e7a25eb-467e-38e9-9cee-122961d46c1b | -9.41074 | -54.71631 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e8a3044-03c0-3868-b0f1-a96a8885df47 | -9.77191 | -46.18798 | 2025-09-29 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 68d321a5-5232-3733-ad10-d4ce0585a31a | -9.77399 | -46.94034 | 2025-09-29 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 722023d6-98e3-3784-8750-38c9bb50beb3 | -11.43381 | -44.96091 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac37b193-73b3-33cb-9799-ef715e14c5aa | -10.83221 | -45.39477 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 44f27343-1072-3b0d-bbc0-57054a67cb2a | -7.13217 | -45.50035 | 2025-09-29 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 468a3b22-ed91-3c79-9faf-a2cb5867d478 | -6.46838 | -44.0091 | 2025-09-29 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f6fe874-c985-369b-9820-842757db1db8 | -6.69708 | -44.55915 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea4f6d94-25db-3a39-add7-184e6fe08048 | -9.05388 | -46.70396 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0a0e7d93-c440-3102-adc3-7ed6474ffa04 | -7.73668 | -46.99491 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1f0ac33c-eb27-3570-9c48-c741ee75be84 | -5.19659 | -43.76444 | 2025-09-29 04:57:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| eb29532f-a710-3f44-8813-1543b75e5e1c | -8.15713 | -46.33549 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc0ded40-470e-36d7-868e-a5eda36ab7a9 | -10.02226 | -52.09498 | 2025-09-29 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3235aa62-79e3-34c7-919b-42556b42c50d | -8.86726 | -45.03371 | 2025-09-29 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4975f324-06c3-3372-81f8-f954bce8186a | -3.8315 | -53.48743 | 2025-09-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcb59d55-efe0-39b7-b653-0a7494aa4358 | -9.30741 | -45.72714 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| beb2e7b5-e713-3c7a-912b-e29ad0b0493a | -5.82044 | -42.82272 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c46d20f1-4fd3-3465-94e7-45283a843283 | -9.7768 | -46.20071 | 2025-09-29 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9984fa8-ba50-3c99-b40e-2d250dff2794 | -6.48907 | -44.25998 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc94ace4-5826-3604-824c-55867f7cd070 | -9.47063 | -45.50183 | 2025-09-29 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 726c2a0a-1479-33d3-9524-e02851e245c6 | -8.30243 | -45.43832 | 2025-09-29 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a58bd30a-ec19-37d1-80f8-1ea875b1e400 | -6.49282 | -44.12886 | 2025-09-29 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3f594ac-a915-36b3-9e0f-0214b27178de | -11.50597 | -44.85045 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 356b9704-4f33-3891-8be6-5fde9c6f75c6 | -8.30166 | -45.48549 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 98e16202-3a33-391b-9710-c2e79a996b89 | -9.3506 | -47.62881 | 2025-09-29 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83b66709-4e70-3ee6-891c-6c30648a50ad | -10.42446 | -46.15435 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cd07a3d-4eeb-31eb-8b04-f3898afe3301 | -7.73765 | -44.94122 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a95feb5-a7a3-3c8f-8152-d30d6c4a8828 | -4.37183 | -43.83339 | 2025-09-29 04:57:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 981fde8d-8973-3650-a998-b09f92505c76 | -8.14812 | -46.40327 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ae30f137-2023-31f5-b346-6ee8776771ba | -8.6642 | -49.42864 | 2025-09-29 04:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2738c02c-6946-3a68-855e-b144892d5319 | -6.50548 | -44.12157 | 2025-09-29 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f7016b5-d09b-3ce0-8c68-0b73ac97316f | -5.90773 | -45.84882 | 2025-09-29 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce20a4ba-a812-35b4-9576-7239e9145edd | -7.28985 | -42.83218 | 2025-09-29 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 24d1f7e1-ce3d-3824-85e5-55c02b8b51c4 | -9.04858 | -46.70574 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 2cd1b9ac-fcb4-3ac6-be78-480e01138c17 | -6.83052 | -44.82502 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3e98aa92-c12c-3681-8ff4-967ab59077a4 | -6.25724 | -43.6386 | 2025-09-29 04:57:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README63.md)
