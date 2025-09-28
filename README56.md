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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6d59fc7-ce16-3155-9b7f-6d01cc4be86d | -12.01624 | -47.92332 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3cb107be-52b2-3b90-b9ad-f72e4aa597c6 | -12.88848 | -47.10687 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdda5e4a-cff4-3e9e-8fa9-4e50ffe981b8 | -7.99416 | -47.93733 | 2025-09-28 04:25:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34039307-2270-33bc-b78b-11b3cdb44b5f | -8.16668 | -46.40677 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 418e8be6-9a21-3904-8acf-d2b47378bba2 | -7.78678 | -47.02639 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5e868184-5a86-394f-8575-c3803cec36e8 | -8.82942 | -45.9895 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a5da857-4a47-354b-b140-332ad2c26c08 | -8.17111 | -46.4217 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d4ac7517-12fa-3dbd-81d1-c17c8ce5ff1a | -9.26671 | -46.582 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22756440-9938-385c-840f-2a14cbc7d21d | -12.93009 | -45.16715 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00d39325-5e73-3b31-9cdc-290e81560712 | -11.625 | -44.42405 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a9ac183-226c-3b80-85ce-a28d62f3b90a | -12.92015 | -45.18587 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1a60b0f-8b54-3d70-ba79-63a1aaa855f7 | -7.80946 | -47.01212 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 0dd5515e-6dbb-31b9-bef2-72f4a055b0a1 | -7.03739 | -44.7714 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6110d475-839c-3de0-88e5-cd2c6a444e39 | -8.49413 | -44.72717 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d62eb41e-66f9-3579-b3a4-5bf34c0a78de | -11.36822 | -45.01231 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 365b2dff-d01f-3ce7-849f-5880c6d34ed7 | -8.90215 | -46.0909 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f66a11db-dc90-37be-9bac-9a11c5f36053 | -6.70712 | -44.59842 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04ddc9df-ff82-330a-902f-f813a92fb521 | -12.00214 | -47.04429 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 510baf8b-fbbd-30db-a3b8-8ba5d0be8a12 | -7.81391 | -46.89868 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 95ed40e8-3065-325b-96ce-1fec0d39ee42 | -12.97858 | -46.85498 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce894b17-e273-373f-acb9-75aea6b3709f | -11.94677 | -47.93381 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 146d432d-5b62-3cc1-ae1f-ad477c854630 | -5.88084 | -43.19913 | 2025-09-28 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 76f66ca0-128c-3265-b84b-f9d9b5bbf5f0 | -12.21161 | -43.75122 | 2025-09-28 04:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cd53241-961e-3e44-913e-0167a9d84a85 | -11.43997 | -45.00743 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c9da2ed-e5bb-3762-b52d-13590a607682 | -7.38365 | -47.04065 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 016ab19a-83c8-38f9-80b5-5d23f2aa181b | -6.12696 | -41.7957 | 2025-09-28 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 455408f3-2fe0-3f86-bd71-8fac15496ee6 | -11.36703 | -44.94819 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26351fb8-428a-379e-bc24-0e2a9554f24b | -5.90032 | -43.68089 | 2025-09-28 04:25:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| acb8ad2d-4d3d-37a8-97a6-9e59000f7acd | -10.53641 | -43.62893 | 2025-09-28 04:25:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37bb9eb5-fb22-3326-98b6-c4d99710884d | -9.9092 | -58.56262 | 2025-09-28 04:25:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56d3a2e1-b7ed-3361-a56d-7f3ef0ab9d8d | -5.94794 | -45.48438 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4368778d-2214-3de3-8cd4-0e24a823b73b | -7.87305 | -44.55378 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddd5aa88-b8fa-3162-8137-c3148b295e33 | -6.09023 | -49.3976 | 2025-09-28 04:25:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b84f77a-fbfc-34a3-a60b-300de4b9a14d | -8.02517 | -49.12374 | 2025-09-28 04:25:00 | NOAA-20 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81730006-4b7a-3f4d-ac0c-9baac32dcacd | -11.98778 | -47.88983 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9a73a48c-23d7-371c-9b86-d088dd2b295f | -7.43914 | -43.18868 | 2025-09-28 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 07de47a6-2425-3bbb-879f-712d1c7f0e77 | -11.44462 | -45.00016 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| c04bddf1-d76d-3adb-839b-1248d26a7cf5 | -9.11378 | -45.86449 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b2911f9-6f17-3d22-8ff2-c7e043b2dd0b | -5.91356 | -42.94055 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f9c593cd-4904-3652-8ef8-2952334d7c83 | -10.91479 | -45.74218 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 55b86921-3da3-39bf-9a9c-f0f4da56db03 | -7.3946 | -48.17352 | 2025-09-28 04:25:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2fe0b4f4-2edd-392c-9b0a-200dd7cbe62a | -11.97564 | -47.08338 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 964d9f2d-7597-3bd2-ac9c-c5c683402ebb | -10.91788 | -45.73145 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ecc4b0a-ca8d-3a93-a101-370f3452a2fa | -6.47728 | -44.25082 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e573d32-b2c9-3aae-b145-c00f443484c4 | -8.48519 | -47.80285 | 2025-09-28 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84bead79-6416-33a5-9590-98b554e0dd8b | -10.78481 | -49.15571 | 2025-09-28 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f81bf435-9c69-39a1-b071-5066a8512736 | -6.27726 | -43.63325 | 2025-09-28 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e27b4cee-48ec-3a63-a8db-26703eee8305 | -6.02692 | -43.92224 | 2025-09-28 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61123dc2-dfd6-3e9b-9e40-81b68f5b6579 | -7.7984 | -47.01751 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c231c7fd-3772-3591-b676-455ad283b306 | -7.16275 | -45.50914 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0af4f8f-b27c-34ce-bf1e-68bcea1e375e | -5.99837 | -45.81223 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1336068-210f-35c7-acd3-78772df98388 | -12.92482 | -45.1785 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67ab0746-1476-3cc0-9ed1-38fa58e109e1 | -8.49812 | -44.72397 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1d17370c-10a7-34c9-b839-cf86d3ccab5a | -7.80116 | -47.02153 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 60a89394-c0ea-336b-b4d6-05fa679f3c3c | -6.42492 | -43.51659 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 71d81b46-d6a2-3330-be45-cf72c2c231f3 | -8.83221 | -45.99353 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5fe011ee-0e01-3bcc-ab5f-880bf89e1b52 | -6.39601 | -43.96095 | 2025-09-28 04:25:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cea40464-64ae-3bdb-b419-016d9ce65773 | -9.10772 | -45.88157 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| caf061d7-32dc-374d-9bd6-b6da35a627be | -12.00567 | -47.94691 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f8a38b4-484e-3ec1-912f-5a23f1899bef | -7.44467 | -43.1765 | 2025-09-28 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3af714c4-a8cb-3192-b289-76161859948d | -10.11516 | -45.66447 | 2025-09-28 04:25:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 035db240-b970-3e2a-9dac-b67c64779cee | -6.56763 | -45.09979 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9bb2cebe-2a0c-36ab-9a36-9134045a99e3 | -11.79487 | -44.9062 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f1f2911-1999-331b-8c64-30aea8e3c555 | -9.92654 | -55.22754 | 2025-09-28 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 523c43f1-fdca-3112-a821-c4aa9c485659 | -11.38725 | -46.98182 | 2025-09-28 04:25:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3077c0f-9592-35da-ae66-aca88decc7f7 | -5.86528 | -45.57816 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 38ee6420-3c8c-3e87-9343-fdcc6d4fca6e | -5.82503 | -44.43847 | 2025-09-28 04:25:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 612baaa9-0e9b-34ea-a42d-48d0f1eeb823 | -5.83513 | -45.87826 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 397d085c-b813-3577-ac79-ff74cd9cee02 | -11.99424 | -47.89073 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a522a0c9-a07b-3985-843a-8bc42db2d49a | -5.82786 | -45.60071 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d1026696-1597-358b-8b20-1de191aabf42 | -11.99867 | -47.88423 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9672f005-340a-3789-b6b3-9e05eacfdc4f | -11.44521 | -44.99625 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 037482ae-43e8-3abd-9ee6-90208403c007 | -11.64786 | -52.8681 | 2025-09-28 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5c04ae6-62fc-3136-9808-d9d2efd9d8f0 | -11.4384 | -44.9707 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9dab8b1c-8490-3d61-82a8-b7fa1c88c31f | -11.35959 | -44.96367 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 48365831-3ce4-3a4c-bcc4-1412e0607592 | -11.99536 | -47.88368 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de38089b-259a-3fd8-91b1-52d2bdd60f76 | -7.74828 | -46.99166 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4feefee3-fc49-31b9-912d-d1f037d906ad | -5.83183 | -45.87774 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f962856c-98a2-3984-8168-54bb87b91996 | -7.54277 | -46.09842 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6c2efdaa-be8c-3dc8-9400-4b4f44833827 | -8.16777 | -46.39983 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5099086d-3990-307f-8e93-3eb419d4f5f0 | -9.06531 | -45.54346 | 2025-09-28 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4fd84a7-53f7-3745-965b-c00c4bb62d5d | -6.15855 | -42.80995 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ca55b581-1917-38a4-9bd4-52115f961495 | -12.01118 | -47.95506 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 791f670c-4aef-380d-8711-a49b2fdf5c4c | -12.08223 | -47.27043 | 2025-09-28 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 254b02b9-1d89-3b8c-98d9-5c69e3aa7f6e | -6.11262 | -41.81266 | 2025-09-28 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 8aad09d5-a019-33dd-a0b0-a5da4342b270 | -6.748 | -44.72326 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2af22c14-ea50-3a6d-a640-b4bd38bda994 | -10.19799 | -58.22021 | 2025-09-28 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87d5283b-21e3-3760-b46b-aa0ffbf1d404 | -7.79729 | -47.02448 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 215b445a-c750-34b2-88d8-9f9af26f532b | -10.66066 | -46.74287 | 2025-09-28 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 971259d4-5981-328f-ac0e-d40dadf7fe0d | -6.71841 | -47.20731 | 2025-09-28 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 334f60a0-561e-3243-87d5-db15394cefcc | -6.3148 | -43.457 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c32cf9ba-5f52-3dbd-a256-5a0834dc2c29 | -7.25667 | -45.53848 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0b544f1-a616-31b5-abc1-a1ad6ba2a779 | -8.52957 | -44.63254 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c81a2b5d-9c03-3220-badb-f34842db0aa8 | -6.15837 | -44.16111 | 2025-09-28 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18ba48e1-fe5a-3606-b6b4-37b4274c328a | -11.96707 | -47.99872 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef5184d4-dcc7-3b57-832c-da758d0f91b4 | -8.27666 | -45.4612 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc14488e-de3a-34d4-848d-684308a2e05c | -5.64269 | -44.93808 | 2025-09-28 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 971f7757-ae93-34a1-bac9-6815bf65f89b | -7.62876 | -43.80228 | 2025-09-28 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dba5089d-a10a-3338-8805-2d8e44363a7c | -12.00306 | -47.89939 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c49cbb4-0c3b-34db-8739-c3bb76e64cc4 | -7.54399 | -47.1449 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README57.md)
