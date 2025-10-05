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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 953a40d5-9749-3a89-b9eb-4066b764c20d | -6.10716 | -43.10949 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d154837-6f89-3851-aec7-79e3f5c14e47 | -5.96537 | -43.51171 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| decd27c6-6ff0-3ea8-85bc-7fa4ecc80cd9 | -5.50936 | -44.57094 | 2025-10-05 03:53:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 25c82123-0186-309d-a417-1c7c1d10089a | -8.53936 | -46.33601 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e5b6a1c5-8125-35af-95f9-1a79bdaa0459 | -6.33232 | -41.63426 | 2025-10-05 03:53:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dbcf8a95-c8e5-318f-856e-ae7650aaa291 | -7.5852 | -43.07159 | 2025-10-05 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a029b3d7-7089-3173-abe1-7f5dba243c64 | -5.67341 | -42.74153 | 2025-10-05 03:53:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8fc3e181-f887-3bb8-992d-776b52cce169 | -5.77118 | -42.94987 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 87375c31-1d8b-3652-a1a6-cde74bafb4cd | -5.89349 | -42.91745 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 27da72c2-eaff-332f-9ae9-9ca32e3f7149 | -3.81416 | -51.07455 | 2025-10-05 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 505b9fdd-bce8-3178-bbb9-1a8e5ca58ecd | -9.63435 | -40.58282 | 2025-10-05 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3f1ff977-bb43-356a-85a9-2aa4baa85fb8 | -8.56692 | -46.26506 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a0cec4b6-3359-3456-a1c5-ca5eba9be9d3 | -10.19601 | -45.50188 | 2025-10-05 03:53:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a4988fb1-a77b-3196-ac56-efcf303baaac | -7.6571 | -45.44628 | 2025-10-05 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05bbdfce-38a9-39d9-960b-fc015a36ac36 | -5.97896 | -44.35912 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10a81582-32db-314f-b460-0131899120fe | -7.72625 | -46.31583 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 05c3854e-3f1a-3292-b7bc-25d348dabf8a | -7.24503 | -44.88029 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdc690a2-9c8f-362c-affc-6dbc78084981 | -3.60704 | -51.04352 | 2025-10-05 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c5d1b250-b4cb-3bcf-8e25-c47ff83e42f0 | -8.22304 | -49.14604 | 2025-10-05 03:53:00 | NOAA-20 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c2adf18-dddb-3158-96b5-06800a2d2e8e | -6.11547 | -42.86472 | 2025-10-05 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f2243843-1967-39d9-a7b8-a66c1884034e | -5.46486 | -42.78618 | 2025-10-05 03:53:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 12b3a4bf-c6ab-35a4-ba1f-ca14d4f521ae | -9.20492 | -46.9282 | 2025-10-05 03:53:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 842231f1-78df-3ce2-9e62-b941e88dfa2b | -3.8113 | -51.08347 | 2025-10-05 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eadf887f-857d-32bf-aff8-f584c1360e4e | -7.02659 | -42.80457 | 2025-10-05 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| d82d1d50-1820-302e-90a0-c154e474186a | -9.33053 | -45.76635 | 2025-10-05 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6437af40-7caf-34c9-8b80-7d3497f149f7 | -8.57939 | -46.33271 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| b869c5dd-a817-3e6b-a236-0ed91aaa82d4 | -5.80189 | -43.28911 | 2025-10-05 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07a82f50-23b1-3fb5-aa3c-49d460a741e8 | -7.47485 | -42.62843 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f9f7337c-ac76-34a9-9826-70d0426675ee | -9.12517 | -44.39017 | 2025-10-05 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0122f3fe-505c-3886-869a-4f05b35b8db9 | -8.14361 | -44.0823 | 2025-10-05 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe6f7204-cee1-31b9-af94-d96c88f39e85 | -6.14319 | -44.63945 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0cb397f-d1ce-358f-82fa-cfaeb7014411 | -8.86961 | -46.72242 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1482c6a3-0f32-3323-80ac-418ff3b0a8c6 | -10.64668 | -46.31702 | 2025-10-05 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c99fcc0b-b6a9-3ac3-82fb-9ab88a9356b9 | -6.14837 | -44.66248 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| d8640a22-02c6-3e4c-b99a-e900a76593cd | -8.85627 | -46.10311 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68eb6ae3-78c6-3dfe-8fe4-ceb44451c3b6 | -9.97772 | -48.01634 | 2025-10-05 03:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31ad119a-fda4-34ee-bbdc-56af557c5428 | -8.54386 | -46.28236 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1dbfdc2e-3d4d-3242-9d6f-aa181ddf0590 | -10.01639 | -48.26825 | 2025-10-05 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc2fa3a3-16f2-3748-8b77-44934e749c91 | -5.25667 | -42.97844 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d88f3aa9-a63e-367c-a3d2-14dd6757151c | -9.4707 | -45.53564 | 2025-10-05 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f7df246e-e57c-3613-80a3-6f6ab992bf5a | -8.58606 | -46.32294 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| e7a13e2b-cd72-322d-88c0-fa569934b405 | -7.79275 | -48.05035 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24ff6601-117f-376c-820c-a6570b48bad8 | -6.07904 | -43.48025 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f53a0f46-b785-3416-8a32-e696f5fc459b | -10.39542 | -45.4218 | 2025-10-05 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 449c9861-2bba-3484-96db-a3fb54197d1c | -5.90306 | -43.75877 | 2025-10-05 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9cd22171-0e76-34d1-90ba-55f74c17c6e7 | -7.02212 | -42.78363 | 2025-10-05 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 5c4198c1-59ba-391d-bba3-e94476419517 | -5.53336 | -42.66713 | 2025-10-05 03:53:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7669310f-5c1d-3bad-b71d-a77fd9251095 | -8.787 | -40.57109 | 2025-10-05 03:53:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 84b79c8f-a713-387d-8e68-a0d03e611c9e | -6.1092 | -43.42484 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7179e14b-1909-3d13-b98b-a712a2b75cb9 | -6.39638 | -43.62026 | 2025-10-05 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33a127bb-b13b-39dc-9779-6f07448c79f4 | -6.06317 | -41.24311 | 2025-10-05 03:53:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bdf7ad5a-72ac-363f-ad7f-6ae062a052c1 | -9.5768 | -46.12886 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 274d59bd-64e1-3e2a-b268-88b75cabfac0 | -6.83468 | -44.07497 | 2025-10-05 03:53:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e13a86c-9696-3c7f-8911-4f49ce38b502 | -5.97098 | -44.3533 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9f2ac71-7a6c-3ad5-9fe4-1bf6da8470d9 | -8.23614 | -46.81269 | 2025-10-05 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| be4a2d2f-a39f-31d2-8008-d1b4658f92ae | -6.2773 | -44.03535 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 213d0c93-61c6-37f4-ab6a-b55ba6181bc1 | -6.15278 | -44.66338 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| fabc8953-c2b2-3e93-a0ba-af76d4cad406 | -5.35807 | -45.95359 | 2025-10-05 03:53:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a593d7dc-708e-3693-bd02-81c9fe3f63af | -8.54959 | -47.66854 | 2025-10-05 03:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5ca7c7fa-3cca-3d41-86f0-a6cdeca24be5 | -6.70301 | -42.15977 | 2025-10-05 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1b678cf7-e285-3b13-9532-d39aa2305b21 | -7.75792 | -46.30589 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d989fb64-603d-34ae-b3a2-a9f7d7278802 | -9.64916 | -45.85679 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 81c150a4-d470-378a-aaa9-42bc07cc52aa | -6.98813 | -44.21806 | 2025-10-05 03:53:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 233695ee-82c3-33b8-a0b9-e5198e9da481 | -7.42521 | -46.50823 | 2025-10-05 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7e4efba-59ee-3db5-88ab-5fc77dceb6dc | -8.58791 | -46.31255 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 92ed2871-f062-3c9e-ac78-7164a1de8941 | -8.56984 | -46.33101 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 40292170-53e7-3463-b6e8-0cd4f742bff9 | -6.1476 | -44.66695 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 2ad9f2ed-e9ff-3cd7-b149-fb626b253147 | -9.04948 | -47.01811 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 40b06cb2-edd9-3f37-83e1-76faf620371f | -8.54801 | -46.31519 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 479ca1d2-7cfc-3929-9d03-02e22f73e03b | -6.66101 | -41.59521 | 2025-10-05 03:53:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 503987a3-1a51-3479-9475-5a8c7efcb819 | -6.01801 | -44.0272 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba0c658f-9bdd-37ec-b161-6240f4ccdaea | -6.71234 | -42.83089 | 2025-10-05 03:53:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8c2c286d-e2b2-3676-be55-687f49f0150e | -6.24829 | -45.34061 | 2025-10-05 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91f02473-a5c0-3391-8bbb-b7090eb69489 | -5.22254 | -43.70473 | 2025-10-05 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8e106714-370d-3298-9e0d-dfdb5f08fbe2 | -5.27351 | -44.73824 | 2025-10-05 03:53:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc361a49-76e1-3d22-ada2-c69489862267 | -8.53847 | -46.3134 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| fac58fef-c8d9-31f4-a222-4ba319ea7d60 | -6.2453 | -43.05407 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28dbe23e-b3d4-3847-87f1-37e4bb20c9af | -7.29479 | -39.26869 | 2025-10-05 03:53:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 680c305d-0feb-32e2-b043-a7e67201f154 | -8.5561 | -46.26831 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 92c31a7b-88e9-3977-8199-41197ff9d74e | -4.25788 | -48.55986 | 2025-10-05 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24f8aa32-a6d0-3176-94e8-28d79917f64e | -7.79829 | -46.01712 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 108274c4-0168-3887-b923-572a12f66d7f | -8.57172 | -46.32051 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 88de3433-adf9-3e33-89fb-45cb8c8b2205 | -5.66062 | -42.70001 | 2025-10-05 03:53:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0b520f7a-d10d-3dd7-a36c-6944172e0dd5 | -9.04412 | -47.01521 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e282f929-440e-323c-a9d6-052dfa8ee0b6 | -6.71417 | -42.79569 | 2025-10-05 03:53:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5c4b7444-b113-3f7d-94da-36fb8b6fab9a | -8.14709 | -44.08688 | 2025-10-05 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 536ef814-a4a0-30bb-b7eb-476fcdc03860 | -6.70374 | -42.17871 | 2025-10-05 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0e1a1be9-67e8-359b-9e58-7049206861f3 | -10.35468 | -48.17012 | 2025-10-05 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 51af2cab-6096-3949-b64d-3196f457be4a | -6.24249 | -44.21539 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2f3e7c4-a416-3f70-b61a-7700e1706fab | -10.19017 | -45.50936 | 2025-10-05 03:53:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ff1ded6-c991-34a4-aa16-c99ac26151a7 | -5.40933 | -41.32093 | 2025-10-05 03:53:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| edfc1b43-9492-35ae-bf33-d2011b309b1c | -7.04938 | -42.76328 | 2025-10-05 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 42f3f12f-9ce7-3e1d-b45e-90e64ad9469b | -4.24777 | -48.56596 | 2025-10-05 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae4a5acd-a453-3877-bdbe-740135733962 | -6.15202 | -44.66785 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| af189e29-69da-3468-b46e-3828f4589e04 | -6.71272 | -42.171 | 2025-10-05 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| decfa381-c20e-3958-8feb-cac272b7c7e8 | -10.64316 | -46.33646 | 2025-10-05 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 43.3 |
| cc3c67b0-be20-331c-a6c1-dfca8f007403 | -5.25229 | -42.6381 | 2025-10-05 03:53:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a0677cbd-bade-3023-96cf-bd701f7376ad | -5.43257 | -42.92894 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b96c7b2b-7e9d-3ff4-a8bf-b28a391807b7 | -9.91828 | -50.24213 | 2025-10-05 03:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf3eba29-e4e8-372a-944b-464dd1b026cf | -7.24222 | -42.98237 | 2025-10-05 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |


[Clique aqui para ver as próximas entradas](README45.md)
