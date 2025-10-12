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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b372a8ac-661d-3d68-a8a5-5b0e233e6560 | -7.49631 | -42.76763 | 2025-10-12 04:42:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 114ca137-0dc0-3d67-bbab-84811cf60816 | -6.75651 | -44.65495 | 2025-10-12 04:42:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fc3f192-df72-33cb-9303-e1897c1c3036 | -3.73904 | -44.38986 | 2025-10-12 04:42:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e548bbf-8d67-31c7-a104-86fe6b1faaf1 | -5.8595 | -42.84463 | 2025-10-12 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1e299f75-f92d-36d6-b80c-becf2a68e923 | -6.80559 | -47.0556 | 2025-10-12 04:42:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 547e62bc-618b-3922-a88f-743628b3db10 | -7.20712 | -45.48901 | 2025-10-12 04:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 31d719b6-96e6-3e02-95a7-4d2c02f917a0 | -2.99771 | -48.73489 | 2025-10-12 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f663ac2-d7df-33da-9cfc-811bb5d6c9ca | -7.01109 | -42.74117 | 2025-10-12 04:42:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 75416671-9a4f-387c-b9c1-1fb37dbe298e | -7.40204 | -46.94989 | 2025-10-12 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 381de9e2-0224-323b-a801-38e0ad217c76 | -6.46453 | -44.64175 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8bf5122-ea0e-3850-b1d1-736193fcbc50 | -4.27575 | -46.93729 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| af9cd1d2-5f05-3808-a8b9-b76961cd19bb | -6.2203 | -41.57594 | 2025-10-12 04:42:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 40c8fa4c-2f93-3d91-a3cd-d5079b227d49 | -2.43942 | -49.37543 | 2025-10-12 04:42:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c7cb7926-dafc-3007-a244-9b456c95485a | -5.4646 | -43.4003 | 2025-10-12 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50ff4fd2-fb91-30f3-bbd2-2af2c8cfc872 | -7.54053 | -43.83848 | 2025-10-12 04:42:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60ffacc1-5e16-3713-b27d-83de0edf92de | -3.51215 | -45.84777 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 66b8f149-abc6-3a84-9690-0ac5895697a5 | -7.67335 | -42.39907 | 2025-10-12 04:42:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6861e086-90a2-3383-8968-7013020908fa | -7.87893 | -44.45643 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d307396b-536b-3072-9a95-5c1bc54ee1f5 | -5.91719 | -45.42379 | 2025-10-12 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c4d1e645-9ae5-3bc9-86cd-576396642619 | -5.73881 | -40.76587 | 2025-10-12 04:42:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7e6433e8-7b11-30d0-a91b-3a8a598cba68 | -7.40596 | -42.97762 | 2025-10-12 04:42:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 080aaef6-3ed4-3c5d-9575-5937e7cd2d67 | -7.86981 | -44.48941 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 375890d8-9ebb-3120-ba74-7f1eae729cf4 | -5.4652 | -43.39631 | 2025-10-12 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ccc0311-d1a8-3c5f-998a-d1d393989650 | -8.47479 | -46.23538 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99dffc8e-bf2c-3578-a3a7-edce88b80e6e | -4.28248 | -46.93005 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a0d7898-608e-3d1c-808a-68925e78feb2 | -7.19787 | -45.9179 | 2025-10-12 04:42:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f9e11ad-fcc2-3f7e-afd6-ffd6a19cb243 | -3.60613 | -51.33868 | 2025-10-12 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 637c7f9b-b2ea-3c02-86b1-734caa7f0025 | -4.27556 | -46.92899 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b4e6582-1195-31d5-9cf8-ac4746532955 | -7.54913 | -43.8397 | 2025-10-12 04:42:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c21c39e-ab7a-37dc-88f0-52b566913eb8 | -7.80458 | -42.43547 | 2025-10-12 04:42:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 44032443-a25d-3fbe-b752-f9aed0bb5b26 | -2.99329 | -48.74127 | 2025-10-12 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ff2ab72-0f39-3abf-a42a-015727aec1ad | -5.86202 | -42.84743 | 2025-10-12 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ac8cb66d-8c9e-3bce-9956-b29e97474700 | -6.56514 | -39.56633 | 2025-10-12 04:42:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 34da2cd6-d615-3e73-a17f-d2ab4be477f5 | -8.4764 | -46.1993 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6f5603f7-2efa-3e6a-b47c-f7b9e430dd23 | -5.47213 | -43.39589 | 2025-10-12 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16f53fe0-7f47-3379-b7e5-11a70b090b68 | -5.9152 | -45.43034 | 2025-10-12 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a302b8ad-f2e5-31a9-b24f-07b85885867f | -5.94153 | -44.20732 | 2025-10-12 04:42:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c44a84f4-a195-3e1b-b003-967dd9f6fa22 | -3.82514 | -51.32378 | 2025-10-12 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04c910cc-fe35-38d2-be1e-308a2ff12b06 | -7.01174 | -42.09353 | 2025-10-12 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 66dfabc5-5fa9-3f6a-b462-02bb6f0c3b8f | -4.28191 | -46.93381 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d53670de-46fb-3dca-b08d-e924b25f3850 | -5.28521 | -43.3834 | 2025-10-12 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c25ba68-50ed-3e13-ac36-3bb527e147ac | -2.99384 | -48.73782 | 2025-10-12 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebf4a528-1ee8-3a97-8547-370b5f78112b | -2.71521 | -48.3578 | 2025-10-12 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53e2d096-c834-3446-b798-28c872a860b2 | -9.56104 | -43.01833 | 2025-10-12 04:42:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| ef900c66-c73c-334c-a1b6-78b79b4ac231 | -4.26656 | -46.92812 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 56be3737-7a96-3725-8ecd-ca02ddd4075e | -5.26285 | -43.10559 | 2025-10-12 04:42:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c04574c2-6e46-32a3-954a-0e2b0393d655 | -5.80293 | -51.49653 | 2025-10-12 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad72b269-3f85-3b8e-931a-1d33a70edb9e | -6.59633 | -44.56686 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77baa6f3-7023-3966-b8c9-a8799b81f803 | -3.50729 | -45.8554 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42677936-db4a-3dc6-a6d0-69ecf0460495 | -7.33807 | -43.86224 | 2025-10-12 04:42:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 250f037f-e5c0-3a2c-903d-0fe711833221 | -4.28133 | -46.93758 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c7ff39d-e5a7-3389-8e8b-36094b929550 | -4.61417 | -45.77592 | 2025-10-12 04:42:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1d25c7cd-24d9-3139-bc1b-b63cac10cd17 | -3.51991 | -49.70227 | 2025-10-12 04:42:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a96a694b-61df-3435-88b2-aca80d8e5745 | -4.94417 | -44.7627 | 2025-10-12 04:42:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6714423-857d-35c0-aca0-46c08f21e744 | -3.76837 | -43.8975 | 2025-10-12 04:42:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f8d9c12-c3b5-3f82-808e-d3b5e78811b3 | -5.83448 | -49.02063 | 2025-10-12 04:42:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b00c8b34-0d64-3b3c-9935-9fc18c09bd9c | -4.37517 | -46.53575 | 2025-10-12 04:42:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23bc76fa-2719-3892-ada6-1a82b459bb5d | -8.19178 | -43.31925 | 2025-10-12 04:42:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 41b3fd8c-4eb9-3438-9107-441f40e4a73a | -3.50432 | -45.85077 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| acec2147-45a8-328e-930c-bd61bff65d2a | -8.48145 | -46.19118 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 654ff2b7-41aa-3ffb-99c6-97b56130cf20 | -6.75361 | -44.64685 | 2025-10-12 04:42:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 998378b5-3ec2-3143-bc47-274437ae545d | -7.26572 | -46.13457 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0efd9d8a-0243-3aea-b498-8b2ffd1380eb | -2.44443 | -49.36548 | 2025-10-12 04:42:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 140d5e79-1fcd-3594-840f-205caffd8f20 | -4.67669 | -43.25462 | 2025-10-12 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e35bc5a-ea72-339b-9273-0718e7f96fd0 | -6.83266 | -42.78458 | 2025-10-12 04:42:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ef64ab40-7306-32d6-83ca-6f08cfc1f5dc | -2.44164 | -49.36146 | 2025-10-12 04:42:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| faf697d4-f7f0-31bd-8bb2-48e7c83189a6 | -6.81318 | -43.05489 | 2025-10-12 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb93701d-68f5-3624-89e0-d3ebf1b88ce9 | -7.86587 | -44.88259 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 045c9e8b-8579-3937-bd59-c96796da7a14 | -2.86019 | -48.70295 | 2025-10-12 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3102daa-28ae-3872-aa3c-0bfdd44f21f0 | -5.75665 | -46.49348 | 2025-10-12 04:42:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17f772b2-5def-3509-841f-4b1aef28fb79 | -6.28056 | -44.40316 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3296b09d-9313-3b9a-8656-a7f8fe01f7d8 | -8.47817 | -46.21301 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4df187c-8e27-3664-99e1-62f38f5c7c71 | -6.52468 | -43.9332 | 2025-10-12 04:42:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8caa6923-aab7-3f1e-8fe7-6a2a7007a860 | -8.03022 | -44.45773 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1af83117-8c66-34d4-b770-9ab7e96bc7fe | -7.50942 | -42.14581 | 2025-10-12 04:42:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fb028c24-72f0-3b0b-abde-2e1eb59b13c0 | -7.00484 | -49.3439 | 2025-10-12 04:42:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5057f45-51ee-35f7-aba3-d6f5b7c835b0 | -6.04287 | -42.4747 | 2025-10-12 04:42:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d415dd30-33b1-340d-9a8b-f4e951d275fe | -6.16772 | -44.66645 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a33045da-9beb-3a9f-86ab-9e2560c8ff28 | -7.05086 | -45.2201 | 2025-10-12 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36b616cc-8453-3ae0-b4a1-2da7b55784c2 | -8.70475 | -47.05713 | 2025-10-12 04:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1693a090-4085-3224-af41-7cc87cfdeff6 | -5.96983 | -44.37996 | 2025-10-12 04:42:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6c84b03-9195-3004-8b87-5b3c2f6a6cf1 | -6.57078 | -39.56742 | 2025-10-12 04:42:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1f050fdf-ae23-3537-83d6-78d0575c3208 | -6.94286 | -46.12787 | 2025-10-12 04:42:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0da5593-bde1-3825-a07a-0b35034b4eea | -5.0563 | -40.45946 | 2025-10-12 04:42:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f48af732-e668-3552-be0d-31e3453fb8ce | -6.17096 | -44.67214 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42e9767a-febd-3c95-b5ed-ede93bb23133 | -7.85312 | -44.51679 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f81ddd1-c40e-312d-a2a2-0fcc4611ed8e | -7.9017 | -46.62715 | 2025-10-12 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54f342c5-761e-36e8-97fb-0dd52245c3f3 | -3.25826 | -50.04917 | 2025-10-12 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2c7510f-64cb-31be-9e9a-d5add137f0e9 | -4.42082 | -43.46966 | 2025-10-12 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e2f46cc-d5cc-38c2-9fce-1785559f5d99 | -7.98969 | -44.47472 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57c8ade2-c5e8-3f35-ac98-14b62c99a247 | -7.88568 | -44.5127 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 587c8b84-9442-3648-b453-94e702869356 | -4.04339 | -42.52005 | 2025-10-12 04:42:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c5eee27f-f91d-3499-b53e-ef4903ffa528 | -7.32531 | -47.82412 | 2025-10-12 04:42:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2aca19c0-239d-3abf-b1a6-a0ce46759452 | -6.28109 | -44.40388 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0b0e24a-ea5e-356a-85fc-6cbcccf8a18e | -6.09173 | -43.4623 | 2025-10-12 04:42:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 215a1907-9c4d-3be5-a46e-d88145e7ba61 | -6.42154 | -43.78369 | 2025-10-12 04:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| beb5ce5a-3e88-3809-b9fe-f815cd9f4381 | -8.83854 | -46.03794 | 2025-10-12 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 678cdbce-1aa4-3f02-9b0b-03e4c645b766 | -3.51278 | -45.84368 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 321a3e75-c2bf-3614-8740-ceaf231fa088 | -4.27902 | -46.92951 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05fc7556-d5db-3356-a606-6291c3a302cc | -4.81787 | -43.14591 | 2025-10-12 04:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README32.md)
