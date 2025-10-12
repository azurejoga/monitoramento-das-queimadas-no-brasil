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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4c2664d-d651-3b16-a3a5-cbd482c1d4bc | -15.15014 | -56.8157 | 2025-10-12 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc34b1b8-e8c4-379a-a2a0-2bdb9079edaa | -12.20985 | -64.37409 | 2025-10-12 04:44:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bcd3ecd3-9c16-3715-aac2-43e6ecf4b327 | -15.16645 | -56.84179 | 2025-10-12 04:44:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 728c2e3a-1553-3b8f-ab7c-b5eda64c6ccf | -11.75217 | -43.31404 | 2025-10-12 04:44:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 889939ec-0e6d-36c2-9516-c40e100f978d | -10.17099 | -44.53647 | 2025-10-12 04:44:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b02b6eb2-52f1-35fc-84eb-fe54e8bf8a1b | -15.29012 | -46.13974 | 2025-10-12 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad3fa295-4d74-33d5-b190-a08d87db439f | -10.17526 | -44.53706 | 2025-10-12 04:44:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 656bb690-ae3f-3625-9cce-0d4f4a4284c6 | -13.45519 | -51.28363 | 2025-10-12 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3b54f866-0bcd-375e-abf3-fd7f640d55ab | -11.24856 | -61.17074 | 2025-10-12 04:44:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8c9f4bc1-5194-336f-98c0-380000ca86d1 | -15.78263 | -51.1293 | 2025-10-12 04:44:00 | NPP-375D | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca2e1422-4463-3997-ba7e-8f8b736f2d22 | -15.23175 | -56.87111 | 2025-10-12 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f07c6cc5-9a96-39b6-a46b-bb2d27b9ebf8 | -11.91585 | -44.1788 | 2025-10-12 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab273499-cc52-32df-a44b-d826251bdd1e | -15.64146 | -44.47207 | 2025-10-12 04:44:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 56177cd9-3a43-3dc9-891d-506520d2cc10 | -10.55864 | -57.52398 | 2025-10-12 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| baf0c193-71b2-3ae3-9b4d-6e274926eeb2 | -15.22491 | -56.86242 | 2025-10-12 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df861783-a9e4-34b2-b6ee-02dbd1371a8b | -10.56408 | -57.52026 | 2025-10-12 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef71bcf3-4cea-3236-91b2-2a3a5d836594 | -14.40557 | -47.97964 | 2025-10-12 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f215bde-f2a6-3175-8511-021a97de5733 | -11.62489 | -55.00993 | 2025-10-12 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6e74a169-588e-3436-ae43-431e8b0091e5 | -11.62594 | -55.01217 | 2025-10-12 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 80d62509-911f-3c71-ae84-1c327a9b7fc6 | -11.37003 | -44.00592 | 2025-10-12 04:44:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c0789abc-6c40-31b1-81d1-2f41697fb583 | -13.29093 | -47.98364 | 2025-10-12 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f909ac31-1ab9-3502-8397-2a1a7261678e | -11.45005 | -43.47715 | 2025-10-12 04:44:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5f661de-e9db-3161-b09f-97455c365406 | -13.45355 | -51.27242 | 2025-10-12 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c859779-0bcf-346b-bf36-2c0b7f2eab8b | -13.2823 | -47.98841 | 2025-10-12 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5915d4c0-e493-3621-a5f6-ac609e0d54c8 | -14.416 | -47.95892 | 2025-10-12 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 996efdaf-ad98-3cb7-8b19-188a9bbbf338 | -14.99952 | -53.8836 | 2025-10-12 04:44:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eb70828d-2766-36bf-a541-01c956b22f25 | -10.78319 | -43.95027 | 2025-10-12 04:44:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d00631e1-6f06-3008-af59-66ec5d20dabc | -15.18145 | -47.49392 | 2025-10-12 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1b09121-ca05-34cf-a7e3-a28afca4bf00 | -10.17043 | -44.54056 | 2025-10-12 04:44:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1433aa2-10d2-3b44-ab84-396b25248e3c | -14.9559 | -45.58147 | 2025-10-12 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31015bce-4049-303c-9148-1ed93ab05911 | -9.89934 | -48.15963 | 2025-10-12 04:44:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e494a38-845d-3223-9e95-94f67430bf85 | -15.28554 | -46.14261 | 2025-10-12 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebb72a2b-0bd6-3183-ae40-055ad238e41f | -13.45576 | -51.28008 | 2025-10-12 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 12984a50-0375-3305-ac3d-7fb1a907434b | -9.40026 | -45.75936 | 2025-10-12 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dfae5d30-730e-31e7-8258-0a957378d6d1 | -11.85468 | -56.8699 | 2025-10-12 04:44:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 872fb09d-a405-3969-a187-6e4e6826409b | -13.57414 | -46.34841 | 2025-10-12 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a3be847-0a57-3151-966d-11eec7703727 | -11.79812 | -46.35154 | 2025-10-12 04:44:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 835f9699-9648-372b-9e52-da380c587b2c | -15.20374 | -56.86288 | 2025-10-12 04:44:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76471606-480d-3a47-9542-0b1ff788c540 | -14.93671 | -46.74298 | 2025-10-12 04:44:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3136d0c5-e42d-3e7d-9383-dc8c56daf834 | -15.23331 | -47.1648 | 2025-10-12 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f59079c8-51e7-3198-ba19-b81041b51e20 | -10.18227 | -44.61077 | 2025-10-12 04:44:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ddad0c8-22f9-3629-9eb6-9fd093428616 | -15.6584 | -43.90232 | 2025-10-12 04:44:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43b99733-3b62-30f9-9bab-91fe91890c82 | -13.46631 | -51.27818 | 2025-10-12 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0f204122-84f3-3edb-bd82-2bd212b2fde7 | -10.1607 | -44.54804 | 2025-10-12 04:44:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46b7f07d-2eef-3cf5-b328-1ccc5fe44161 | -14.4038 | -47.96581 | 2025-10-12 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2c0d9f7c-8d92-318f-b210-7566b50a053a | -15.02564 | -46.27477 | 2025-10-12 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57eb0790-a7da-370e-bf4a-5f494e154e81 | -14.95164 | -45.58093 | 2025-10-12 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 67101e87-e951-39f0-8921-4025ba45c0ea | -13.29013 | -47.98539 | 2025-10-12 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 500ae43e-4fab-31a0-8940-f9cd5a83f98b | -15.29406 | -46.29948 | 2025-10-12 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09ca4321-babf-3a2a-b1d3-0b81bad5336c | -15.22697 | -56.87413 | 2025-10-12 04:44:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15992612-0dbd-37d2-b34c-1876548c5a45 | -9.3964 | -45.75859 | 2025-10-12 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 165dad6e-d212-391e-80a3-838771da4f11 | -11.3694 | -44.01043 | 2025-10-12 04:44:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b2044b8e-10dd-39a5-b9d5-eb13b7f78645 | -14.40253 | -47.97472 | 2025-10-12 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1649a9e-dcc6-3e32-aa2a-b9310c79de52 | -15.00234 | -53.8882 | 2025-10-12 04:44:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 30f71bc5-9067-3a27-a006-ccb5ccb43511 | -13.44432 | -51.25232 | 2025-10-12 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4c426e67-91b1-3c76-a8da-76c8e1229d63 | -13.44263 | -51.26297 | 2025-10-12 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2193cec-a38c-3c31-9c15-e09963d81a90 | -12.13763 | -45.59218 | 2025-10-12 04:44:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 16de9bc0-ad5e-3f9f-807c-80495acd7b87 | -14.9221 | -46.76147 | 2025-10-12 04:44:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9f1b3a25-bf0c-3bc4-80ba-a1e2fc561e03 | -11.75759 | -43.3096 | 2025-10-12 04:44:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d4e60e9-8585-336b-a552-d230f4aca1a3 | -11.50071 | -43.48932 | 2025-10-12 04:44:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0142337-3988-3225-8ae9-cf30f011918d | -11.62022 | -55.01406 | 2025-10-12 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f81cf183-eca0-37af-ac17-220e02613fe2 | -11.50471 | -43.49494 | 2025-10-12 04:44:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01e749c3-b96b-314b-9193-0b06e7c78453 | -14.9228 | -46.75636 | 2025-10-12 04:44:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b3438169-06c8-3f98-801f-0327e0acccf5 | -15.65772 | -43.90301 | 2025-10-12 04:44:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e63ff4c-025f-3778-a550-5e1fd9ccc247 | -14.40127 | -47.98364 | 2025-10-12 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 348a253c-dc37-3aa0-9f79-6f06404c219b | -15.28602 | -46.13901 | 2025-10-12 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04f0952f-c746-38b5-be62-07e05cbf954b | -14.94684 | -45.58454 | 2025-10-12 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| ee545d2a-b319-36a4-8d87-9f097659ff85 | -11.67156 | -43.77774 | 2025-10-12 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0bba5888-aaae-36a2-a404-71bf667a03d0 | -14.9207 | -46.77166 | 2025-10-12 04:44:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6b732d57-dc74-3a67-a814-732a4fed66ae | -9.89588 | -48.15906 | 2025-10-12 04:44:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bfef535c-2a4d-3931-a9aa-dda5dc146abc | -10.15161 | -44.55102 | 2025-10-12 04:44:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 773ee0b9-206b-39a0-ab8e-0a0d06359c61 | -10.5595 | -57.51926 | 2025-10-12 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cba3d082-d75d-3374-a480-0302e3f14a7a | -14.41539 | -47.96316 | 2025-10-12 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0b05161-cd82-35ef-ba52-594d5d88ced5 | -11.67678 | -43.77365 | 2025-10-12 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e660a18-13dd-3f24-ba0d-b190e954a8b7 | -14.94199 | -46.73392 | 2025-10-12 04:44:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| e6c17c56-66b7-3dee-ae40-cb297fe4bdc2 | -15.76384 | -48.97579 | 2025-10-12 04:44:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9b728fd-264a-3671-a1dc-d91aba65bfc2 | -10.17469 | -44.54111 | 2025-10-12 04:44:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c2ca788-747e-3bac-87b9-352d9c3b075e | -9.43051 | -46.95343 | 2025-10-12 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3f9f4c2-dadd-37a9-b954-5ffd6ff1006b | -15.22767 | -56.87031 | 2025-10-12 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 881afec9-3738-39ef-92dc-84493f203bc1 | -13.44319 | -51.25942 | 2025-10-12 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf55c93e-c037-39ea-a597-e4f48557c22c | -13.29438 | -47.98162 | 2025-10-12 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e0ea030-400e-342c-9218-ccf27ca63de6 | -10.21254 | -44.6109 | 2025-10-12 04:44:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80861fae-1345-3b1a-8b98-7c64b1634a83 | -11.85974 | -56.8666 | 2025-10-12 04:44:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4844ba32-3a54-34fc-a99e-fd16e9c2d202 | -9.08157 | -48.02998 | 2025-10-12 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6945f97b-6854-31b3-a282-29f4667bea92 | -14.92351 | -46.75117 | 2025-10-12 04:44:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c22551b7-a625-385c-b79c-eb1af0f6a6cd | -14.40683 | -47.97075 | 2025-10-12 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cf11994-364b-3314-a85c-16057ace1f93 | -15.20393 | -56.86766 | 2025-10-12 04:44:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6c60162-df66-3609-81a8-41059d92d411 | -12.21217 | -64.36134 | 2025-10-12 04:44:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a6dace11-bafc-3e54-a72a-c264048d3033 | -15.67693 | -46.64399 | 2025-10-12 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41295cb3-b12d-3016-b3ce-37989f951dff | -13.46241 | -51.28118 | 2025-10-12 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a3d21f49-0ef3-38f3-808e-fcfe7732e370 | -12.13355 | -45.59159 | 2025-10-12 04:44:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 92d35994-e3fa-34f7-b162-4453d7b22dde | -14.98203 | -44.93871 | 2025-10-12 04:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5ec1d53a-128e-3071-b74b-39f8603088d1 | -11.85115 | -56.86487 | 2025-10-12 04:44:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8825610d-2128-3658-a81f-b3a0fc91a952 | -15.21682 | -56.33482 | 2025-10-12 04:44:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b2501df-9236-3bc4-8a01-a350f486f14d | -13.98575 | -54.89027 | 2025-10-12 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0295b895-be87-3ef1-a1f9-92364f03b992 | -14.91318 | -48.53079 | 2025-10-12 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dfc50c4a-09d7-33fd-9d52-a35b537be5bf | -15.89518 | -48.96488 | 2025-10-12 04:44:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7d02c31-13b9-3bf5-9ab8-0494b122830a | -11.36898 | -41.88287 | 2025-10-12 04:44:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| afb768dc-242d-3ea6-8b22-80f707e0f12f | -15.2297 | -47.99017 | 2025-10-12 04:44:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5cfad77-4912-391e-973f-33b8c21538dc | -14.40189 | -47.97924 | 2025-10-12 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README35.md)
