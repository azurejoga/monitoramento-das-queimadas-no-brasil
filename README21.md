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
| e9f28169-70a2-328e-922b-742b43bc67ea | -6.84017 | -44.87706 | 2025-09-08 03:38:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5e465c40-01d4-3243-8873-9ce62f1a6e98 | -7.31495 | -39.15417 | 2025-09-08 03:38:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| df721a95-256f-34c2-8eac-78b9083c5ce0 | -6.38995 | -43.80711 | 2025-09-08 03:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02df4b4d-1f15-3219-81b0-f5647f9ef248 | -7.57413 | -44.00724 | 2025-09-08 03:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a8b0b9b-5056-3dc3-98d6-d1bc560cf81f | -8.15592 | -44.84973 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64f72c2c-bb2c-32c1-92d0-b2ce570a3d5f | -5.87243 | -43.97216 | 2025-09-08 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 59bd8d9e-b851-329b-9ce9-e16f28963b2d | -5.82709 | -44.12187 | 2025-09-08 03:38:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00da7f4d-969f-3a62-bbd3-f057e90963df | -3.85916 | -39.33386 | 2025-09-08 03:38:00 | NPP-375D | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 99aa9177-45fb-307b-b28e-de6969a861e4 | -6.78007 | -43.42143 | 2025-09-08 03:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0b99fdbe-b431-3f8a-86d5-5464adc66063 | -4.54618 | -40.70644 | 2025-09-08 03:38:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 46672c0b-0580-3edf-8156-c588b2b85513 | -6.5409 | -44.79567 | 2025-09-08 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0856cf99-0393-3b52-a992-dd8225282e6f | -7.09961 | -42.93401 | 2025-09-08 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f83c4f99-04af-3855-9da1-19a396ec7158 | -5.87044 | -44.18674 | 2025-09-08 03:38:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7140b5e7-28bb-3ba7-8457-3cea0e0937f3 | -6.26876 | -43.68833 | 2025-09-08 03:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9738f93b-78b3-37cd-96cd-d0c5c8a2f290 | -7.5753 | -44.00568 | 2025-09-08 03:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbef4598-4e6b-38c6-ab70-c58cbc06a5d8 | -6.2977 | -43.82479 | 2025-09-08 03:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d8103e2-af1f-3c78-a046-169cc5e6df0f | -6.21702 | -43.37678 | 2025-09-08 03:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef8387d1-59e1-3891-9083-930eabd39e57 | -5.87323 | -43.96773 | 2025-09-08 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f453109e-45eb-3712-9225-c02c78db7d80 | -6.24071 | -43.5054 | 2025-09-08 03:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bb9b725-f4a5-33ab-90dd-fd81b5386263 | -5.872 | -44.17801 | 2025-09-08 03:38:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 366cac44-be00-374c-8daf-efd7e77ef415 | -8.0419 | -44.05846 | 2025-09-08 03:38:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0048f178-0833-3396-abb2-f160a26b7ed5 | -5.64987 | -45.11526 | 2025-09-08 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 00930962-534b-3c4c-a550-4c46667210fd | -6.60955 | -44.01006 | 2025-09-08 03:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| abc688d1-cbee-3fbc-9e43-4cea215f92bb | -5.44104 | -42.58575 | 2025-09-08 03:38:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a5ee590c-ff7c-3a66-b27e-693d815caa00 | -6.30351 | -43.82556 | 2025-09-08 03:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8db59a4-44b2-340b-adb7-e0a203344483 | -7.10914 | -44.14108 | 2025-09-08 03:38:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9da3c15d-5971-3fc0-b309-588418a8a49c | -6.39926 | -42.98841 | 2025-09-08 03:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9dc0c79-4780-3601-a752-552544e0bbe1 | -6.20382 | -41.00259 | 2025-09-08 03:38:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| dbe4705b-4bee-33cd-972b-0982ef166f29 | -5.64899 | -45.12025 | 2025-09-08 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d3140cd4-1a04-3aed-b8b4-a22824398ac6 | -9.39625 | -40.30474 | 2025-09-08 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 6993487f-c4c2-3765-be93-d9b3bd03bda3 | -7.73766 | -44.72963 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 20eb8271-d629-3a38-9142-082c72400254 | -5.82447 | -44.12025 | 2025-09-08 03:38:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bb3a250-90f5-3e36-8041-cae815f280b9 | -6.08406 | -43.36074 | 2025-09-08 03:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a4d5ba5a-e65e-3ecc-849c-dd17ef428736 | -7.98805 | -45.47002 | 2025-09-08 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a15dd1b5-6692-3894-b4a6-a71d7d8bd603 | -6.30796 | -42.19785 | 2025-09-08 03:38:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9346c2e9-411c-3bc0-87e1-bfa9c5cdf48e | -6.19879 | -40.97489 | 2025-09-08 03:38:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8fe31a61-413f-3d87-ad5c-7739ad66420f | -6.1956 | -42.64612 | 2025-09-08 03:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a118fd96-4b82-3339-8521-b4f4ace1a68f | -3.85586 | -39.33571 | 2025-09-08 03:38:00 | NPP-375D | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9994d188-b485-398f-9159-9c888c087958 | -6.64012 | -42.96682 | 2025-09-08 03:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6f64545-367e-3810-83d7-5e8d9c66d36b | -6.77943 | -43.42506 | 2025-09-08 03:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7fbd0c80-a37f-393d-9489-4953ce4ff960 | -7.87253 | -46.25532 | 2025-09-08 03:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d25f5f8f-5a46-315d-9fd9-0fc93723915d | -8.21857 | -44.77837 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6554b02-8e61-359e-b8d2-58e3f4ab1b2c | -5.44896 | -42.80381 | 2025-09-08 03:38:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 43206967-aa25-3dde-8b3e-de899251b542 | -6.19112 | -43.58764 | 2025-09-08 03:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f101be7-d62b-36de-9743-443fa30b63d5 | -4.80443 | -43.55166 | 2025-09-08 03:38:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21b296b9-d269-3424-84b6-d9cd2cdf2106 | -5.82373 | -44.12448 | 2025-09-08 03:38:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d5c5de0-9eb0-3305-b50c-0284a4cc1b2d | -3.46061 | -43.18525 | 2025-09-08 03:38:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cb0c62e-9a63-34bd-9948-8b340a8d8d3c | -8.22535 | -44.77492 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0ca0f23-6431-3627-81a6-500c03107761 | -6.04142 | -43.69593 | 2025-09-08 03:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 742b2fb2-1fa4-3b8a-9382-d611697fbd1a | -6.871 | -47.91245 | 2025-09-08 03:38:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5572abff-565a-3a35-8825-8f1be098e08b | -7.13986 | -44.57246 | 2025-09-08 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 30a51afe-0245-37f3-90f3-93d3e991732c | -6.17944 | -44.74115 | 2025-09-08 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89cd989a-627d-32ec-93b5-2c7d82cfa99a | -7.7324 | -35.13984 | 2025-09-08 03:38:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 667c7ba2-0597-3338-a9d7-bfd1a7b84f99 | -7.65859 | -44.80894 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ac5fce0-9767-3e9c-988a-341e006bbe10 | -6.12298 | -44.26101 | 2025-09-08 03:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a8658ea-6777-35ba-917f-9ae17f565a3b | -7.84402 | -44.85589 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46c3da05-289e-3b04-9b52-c0fc69dfef27 | -6.09394 | -43.11946 | 2025-09-08 03:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 621c87a6-683e-3bbf-aeb0-4c83ac31caba | -6.86909 | -47.92242 | 2025-09-08 03:38:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1dca7217-f7e5-39e6-ba07-9fffbcd1badf | -4.9394 | -37.96255 | 2025-09-08 03:38:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b1fd3f3a-6cd2-3b1b-a777-1b47ebd8058e | -6.24653 | -44.82571 | 2025-09-08 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7367ac7-dc3f-3ade-9827-05844ccbd4fe | -6.13696 | -44.23416 | 2025-09-08 03:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74c29a84-2cb1-3767-abe2-7c1d24a2a1a5 | -6.25588 | -43.6944 | 2025-09-08 03:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 508c3007-90e9-3985-9784-936f02f5a8f6 | -5.86575 | -43.84921 | 2025-09-08 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a46e869f-a323-3dc0-b27b-e6059a2ba253 | -5.80642 | -45.65323 | 2025-09-08 03:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 364fa99e-2a8f-3522-ae47-3a8b1bdcb3f5 | -7.03588 | -43.25248 | 2025-09-08 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ad2f0c7b-bf4b-3245-844b-5d90dac6ce93 | -2.82654 | -41.87107 | 2025-09-08 03:38:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c7d77f0-7aee-3397-b1c7-04208ae06d64 | -5.32751 | -42.68529 | 2025-09-08 03:38:00 | NPP-375D | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 08f9c26e-ffd3-31f7-91b2-c5018e79a11b | -4.89514 | -42.22165 | 2025-09-08 03:38:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0dbf6037-40e3-37bd-a137-682bf8e30fab | -6.06566 | -43.11835 | 2025-09-08 03:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 36a40cd0-09d9-3016-a7bb-cb3c2373811c | -7.9751 | -44.83585 | 2025-09-08 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b62e4837-beb0-33eb-95b4-c7dfb397e8db | -6.12383 | -44.25634 | 2025-09-08 03:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2bdad1a-1f51-3976-9085-9c018de46374 | -6.87409 | -45.53877 | 2025-09-08 03:38:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59441621-c451-3ab7-aafa-71acc728ff8c | -6.18027 | -44.7366 | 2025-09-08 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7266fe80-5733-3cbc-9bf6-b0c6960abb49 | -7.99602 | -45.46182 | 2025-09-08 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2f85a0fb-b42f-36ba-936b-7cdc8f4896ef | -6.14033 | -44.23307 | 2025-09-08 03:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c24930df-c3ff-3f99-bb74-865750d0a647 | -6.30968 | -43.82493 | 2025-09-08 03:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa48bf73-9b66-309c-abc1-98e673ea3e80 | -5.86442 | -43.85033 | 2025-09-08 03:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fef0f2de-15a8-3d71-9c8f-24469777e7b4 | -6.63953 | -42.97018 | 2025-09-08 03:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84261162-f971-3d54-a317-d80e09f897b4 | -6.25662 | -43.69026 | 2025-09-08 03:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6fb049f-c677-37d3-8761-3d95103b377f | -5.35348 | -42.64122 | 2025-09-08 03:38:00 | NPP-375D | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3f3ebe1c-1d3e-3493-97ea-001c25d26303 | -7.56206 | -37.18716 | 2025-09-08 03:38:00 | NPP-375D | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 377a6f6a-e70b-39e6-bce6-4518389e61e1 | -6.21633 | -43.31604 | 2025-09-08 03:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af566172-5701-3a95-a57e-fe4f3b81a705 | -8.2497 | -41.40765 | 2025-09-08 03:38:00 | NPP-375D | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 296b865e-de8d-38a5-99fe-d9b8760f131a | -6.20156 | -42.64361 | 2025-09-08 03:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dbaba724-0d2b-3c06-aece-05358689203b | -6.21207 | -43.37215 | 2025-09-08 03:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08bbb179-bd99-3349-9d58-2c893cee85e7 | -6.61035 | -44.00751 | 2025-09-08 03:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f223372f-d766-30eb-aeeb-1d518e0ce78a | -6.40671 | -43.88109 | 2025-09-08 03:38:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00bb720f-5751-3ab1-ba1a-2b9ee5184ee2 | -4.63014 | -38.56852 | 2025-09-08 03:38:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ddd89861-87c7-343d-b4be-65dbfd27b81e | -6.97454 | -45.57437 | 2025-09-08 03:38:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02267ca7-9f6a-3667-b287-7336c8d3070b | -7.08258 | -45.20208 | 2025-09-08 03:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1b5d2b39-6ae6-3ca1-bd41-afd71d37c6f5 | -9.39696 | -40.30061 | 2025-09-08 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 68d013c6-895b-3724-bd63-d7733ff6cf58 | -4.57322 | -40.34398 | 2025-09-08 03:38:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 37c198f3-f080-33f2-8ad5-115c17bd90c6 | -6.23392 | -43.51086 | 2025-09-08 03:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc3a859c-7da9-3fa0-a4ea-a09096d0b323 | -7.10989 | -44.13704 | 2025-09-08 03:38:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eefdfff0-a999-3cd9-b841-31d3c3f443b6 | -7.76922 | -34.91069 | 2025-09-08 03:38:00 | NPP-375D | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| f8388293-7a3c-3935-87ca-ceff91ed89ed | -7.82797 | -45.42352 | 2025-09-08 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9dac95fd-6517-3754-982d-54581a2dac9c | -6.06629 | -43.11482 | 2025-09-08 03:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddf6c1bc-7dc5-3d9e-9bec-e9f8e6e50545 | -6.46662 | -43.94584 | 2025-09-08 03:38:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c462f97a-4b13-31cb-a9ca-94fcfa4219d0 | -5.08035 | -42.41801 | 2025-09-08 03:38:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 047cd557-42e2-326f-97e5-8f48d937dd4b | -5.49637 | -42.66099 | 2025-09-08 03:38:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README22.md)
