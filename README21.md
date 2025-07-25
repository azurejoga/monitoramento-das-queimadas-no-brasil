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
| 57ac62ef-e307-367b-aa59-7736c78051d5 | -2.91778 | -48.24219 | 2025-07-25 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8d663bf-f289-3aec-9da3-ee8dd5e3d0ee | -8.28863 | -44.98073 | 2025-07-25 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4bb5b8fd-a7ed-3ed8-9b9d-c207d68b3b9c | -4.83305 | -45.30428 | 2025-07-25 04:44:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a7a57e6e-8485-3a60-87af-c6f08de0bc9e | -7.91687 | -44.08793 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8fa3bd59-3027-33d7-b16b-268de2ad36af | -5.99305 | -45.72654 | 2025-07-25 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45ef06b7-63e1-3765-ba3e-2e4c11c70921 | -4.10538 | -47.93542 | 2025-07-25 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 247873d7-fe48-3902-963b-b9fab37b7f33 | -5.42677 | -47.14969 | 2025-07-25 04:44:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa975a84-2b01-358f-aa53-ba72ea5574ae | -4.53941 | -48.00607 | 2025-07-25 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3aca94d7-f8b1-3413-ab78-5813a1adc1fc | -4.35309 | -47.69301 | 2025-07-25 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f110b125-1e0b-3bf8-a3b4-bca4c54fded9 | -6.673 | -43.96723 | 2025-07-25 04:44:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4de12e2-d102-3340-b25a-88ba5640eaaf | -5.77838 | -51.87306 | 2025-07-25 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 192f690b-edff-3326-9ae3-e52e3cab1783 | -3.30681 | -51.66317 | 2025-07-25 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a395092a-25b7-31a5-9356-7f33f85772db | -6.40934 | -53.33067 | 2025-07-25 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e9d2c89-a185-33e4-a7bf-7a70578bb307 | -7.10357 | -43.54988 | 2025-07-25 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c8e9b4d-1d99-38ed-b57e-cceb9c2c82ca | -3.17736 | -49.45043 | 2025-07-25 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66833f1a-7f08-3cda-9731-79e86aa8e58f | -6.94837 | -44.56369 | 2025-07-25 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 3ac26ee5-2773-316a-bcee-86b0552624f9 | -7.91682 | -44.08084 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 194abb56-d96d-3a5e-a788-63b3d54ca3a0 | -8.29887 | -44.97296 | 2025-07-25 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4fec7236-c158-3a1c-8a16-e2a3c2f95a0c | -8.32986 | -44.94843 | 2025-07-25 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3e5accea-f627-3365-97b5-e8a3edaace46 | -3.17791 | -49.44693 | 2025-07-25 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03675c89-4f66-3051-98b2-4c28d8151245 | -7.26397 | -43.06736 | 2025-07-25 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 3c5f1166-a0ba-3667-b760-663afca30573 | -7.85738 | -48.21478 | 2025-07-25 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c461909-cb69-35aa-a2d6-6007c365bedd | -7.60475 | -49.94854 | 2025-07-25 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 06e96f2b-b826-329a-9a0b-01bf55807064 | -5.23155 | -46.08978 | 2025-07-25 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8dcccc27-0c94-3228-8bf7-91442356f515 | -4.34951 | -47.69247 | 2025-07-25 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| dc53bfaf-d1fe-3dbd-b164-62502c9ccf3c | -4.77547 | -45.33543 | 2025-07-25 04:44:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a5eb896-e0c2-3402-a815-1ddd6bd921c5 | -3.12385 | -47.00956 | 2025-07-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed18d1e4-4685-3873-9971-08dd094aa373 | -7.24887 | -43.06523 | 2025-07-25 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 669b0c22-e87e-3f0d-ad78-bdb3a18a96ff | -6.91703 | -44.29403 | 2025-07-25 04:44:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4aac916f-b5b3-3af2-a809-2b8fc18d5248 | -6.14387 | -44.32818 | 2025-07-25 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1765db0f-c158-3c62-8ef1-3dd21962b50f | -7.91757 | -44.08278 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b5e8f752-33f1-3bf6-b02c-942d923f1136 | -3.18614 | -50.39001 | 2025-07-25 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf87db7f-59f8-3ec1-9aaf-3f4832969871 | -7.94127 | -44.08611 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18f7bed2-4346-30e5-91c3-1ffd16285036 | -8.32856 | -46.29293 | 2025-07-25 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8e47c3b-12d7-33f9-b9f1-549fac6953b9 | -3.27794 | -49.95676 | 2025-07-25 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b378185-2fdd-3106-998e-c1cfb8a599e4 | -6.40608 | -53.33429 | 2025-07-25 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16228ce0-8700-3381-b4a6-85ef3a8c6e4e | -6.94904 | -44.55906 | 2025-07-25 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 81c9d46b-53eb-3d28-ac1a-2b2e297944be | -7.11329 | -47.84177 | 2025-07-25 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fee6a323-0f7a-3da7-be97-e56883f141ab | -7.91828 | -44.07754 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e17324f4-0964-3262-86a5-80eb704f3179 | -7.14432 | -46.0949 | 2025-07-25 04:44:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 058cac98-d6b4-392f-a4a8-80e11f0c0038 | -7.3645 | -48.13509 | 2025-07-25 04:44:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a85f7516-d65f-3343-b6b0-5bc0da96aedf | -3.04701 | -47.38615 | 2025-07-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d43e7d83-d17e-3027-9f88-27b1f49a2032 | -7.92008 | -44.09179 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fccd3dff-84af-3e3d-8d92-a90217945f28 | -8.08948 | -43.15095 | 2025-07-25 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 84fb1fae-b429-393f-a4ab-e491ead6aeb3 | -4.31173 | -47.98154 | 2025-07-25 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e61f06c7-1ad4-325c-a38e-7955ec2dbe98 | -4.01734 | -49.50808 | 2025-07-25 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40183cea-7ed3-3412-99f6-d47066242ef9 | -6.87916 | -43.11784 | 2025-07-25 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3504ba2-62ae-396c-8d48-8ff20e537aa5 | -7.91387 | -44.10137 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b07a56ab-5ae5-37da-83eb-662d4970bad4 | -6.95423 | -44.55511 | 2025-07-25 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| a4689cbd-3b2b-3c71-aa31-f805f1d75717 | -7.91548 | -44.09819 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f56f70aa-a9f2-3c28-a840-43b556672329 | -7.9066 | -44.08475 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cb3122db-827e-3e6d-85c8-127526e93fdf | -2.91375 | -48.24542 | 2025-07-25 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 1069e3de-4ca8-3213-baf5-e24697b7fd96 | -4.99473 | -56.2951 | 2025-07-25 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0c70358-3575-3c8e-80cc-6f8fbe81bd4c | -7.09123 | -44.8785 | 2025-07-25 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ce1bc70-3dd0-3294-b1e3-731c424ae367 | -6.88385 | -45.25002 | 2025-07-25 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ee94287-7060-3856-a941-9ad6a4484a01 | -7.46404 | -49.40038 | 2025-07-25 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e02293e0-870a-3bea-a5b7-c392b8ea5050 | -3.17293 | -49.45691 | 2025-07-25 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3362d57-52bd-3568-8fce-a627e8966362 | -7.92082 | -44.08666 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b3ca546a-d02b-33be-a356-563d5373e088 | -2.39412 | -47.6284 | 2025-07-25 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07f3c0dc-df55-3457-b722-3e80b421731e | -7.84563 | -44.20953 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 49bd77d1-c875-3ab5-8d79-62a7d6cae8fb | -7.89102 | -43.54491 | 2025-07-25 04:44:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2ba5ac4-cb60-3b36-b4ea-318d4f283010 | -7.25935 | -43.06368 | 2025-07-25 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a0104e67-a4b6-39a6-9666-600eb3202f7f | -6.9322 | -42.80683 | 2025-07-25 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6b69e299-904a-33a0-bedd-0b4dfcaab668 | -7.90987 | -44.0956 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d7be940d-44cf-3089-afb5-dbb83394e0ff | -3.04764 | -47.38213 | 2025-07-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 139693b6-ef07-385f-ba6f-696f5ecd92d8 | -4.28797 | -48.0638 | 2025-07-25 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca115370-b27b-3203-a168-82def9a9e535 | -7.92558 | -44.0872 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9fdc7f0d-aafe-3b92-905b-9e76adc8012c | -8.07855 | -43.15535 | 2025-07-25 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 802ce04d-6330-39b2-b820-397a25882ab0 | -6.88444 | -45.24609 | 2025-07-25 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 780235f9-95c4-333d-b1da-511a5b461f53 | -3.762 | -47.5078 | 2025-07-25 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7655165-b1a4-3ac1-8d79-339f35cefe1a | -7.88436 | -45.54721 | 2025-07-25 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6da2a1a5-d93d-34ac-9274-9173afab842c | -7.72917 | -50.77115 | 2025-07-25 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c18aee35-1c00-3b78-b6ca-0d85e02ba60f | -8.51106 | -43.31563 | 2025-07-25 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| c1fff15b-c87c-3552-b40e-c32eae3c141e | -8.08361 | -43.15611 | 2025-07-25 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b5de0e87-4b98-350f-8aed-87d8e9c2d313 | -2.90686 | -48.24435 | 2025-07-25 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5430705a-72d1-383f-a63d-c79d98270d4b | -3.07739 | -52.43659 | 2025-07-25 04:44:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5baadc48-bce8-3351-b1ca-eb6887b89b21 | -3.32703 | -48.71716 | 2025-07-25 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f58a463-1f53-3773-9487-91191ba6002e | -6.6481 | -43.05001 | 2025-07-25 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74384ed3-1554-33bc-a018-9c365c9b3374 | -5.42743 | -47.14521 | 2025-07-25 04:44:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cff98424-d692-3612-bc25-920fd8d2b0d0 | -7.91074 | -44.09753 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 37ac8028-54cd-34f3-b35a-de3772d67061 | -7.88863 | -45.54789 | 2025-07-25 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31c750e2-5a2c-3437-88d9-0a4c0a5c0ac8 | -7.35675 | -43.43494 | 2025-07-25 04:44:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e19e0ed-f846-3dd4-811e-6f11ae8a11f6 | -3.75675 | -52.66365 | 2025-07-25 04:44:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83111b25-0c0d-3f6d-8cda-62e224b09f1d | -6.70952 | -50.47202 | 2025-07-25 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5e6cd0f3-63f3-3e05-97a7-0f1f885e4e7d | -7.91135 | -44.08533 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2f0bdf5d-3729-3cb0-b3cd-5a498366f079 | -7.85552 | -48.22745 | 2025-07-25 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 126b9cfb-f9d9-3039-86aa-10ea810bfa6b | -6.76998 | -51.19188 | 2025-07-25 04:44:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8764dc98-19b3-3d8d-9656-f805596a4714 | -6.91641 | -44.29676 | 2025-07-25 04:44:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a9da8ef2-22e3-30b0-88f5-379fc96381c9 | -4.31526 | -47.98206 | 2025-07-25 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 851f025e-ff73-3385-82e7-2ec552bc40b3 | -7.10964 | -47.84113 | 2025-07-25 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0c0d4492-35fc-347b-8086-5b98f34043af | -6.87956 | -43.11493 | 2025-07-25 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0146732-78bc-38c2-944a-52dd4efff716 | -7.53487 | -42.42895 | 2025-07-25 04:44:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5e0afd44-3c1c-351a-ac0a-42c43553503e | -7.14486 | -46.09119 | 2025-07-25 04:44:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0db552b-efc1-35b8-8b9b-491456ef7728 | -7.25348 | -43.06895 | 2025-07-25 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0ea1533d-9bf6-35fe-b2ea-adca6c1c247c | -8.28989 | -44.97182 | 2025-07-25 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 33be57b3-fabc-3d0c-a9a7-01a3e5e02042 | -3.17014 | -49.4529 | 2025-07-25 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e3c3c6b-7bf3-3f49-8719-6c308de5ec3d | -3.58274 | -47.52478 | 2025-07-25 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5ba3a221-d1c8-3466-989c-39185b6b3429 | -6.56794 | -49.50863 | 2025-07-25 04:44:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f4153e0-35d0-3374-9ae8-2bb0f93c23a9 | -3.07396 | -52.43605 | 2025-07-25 04:44:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5509ede-57a1-3bcd-9c62-be22c365fc5c | -8.07895 | -43.1524 | 2025-07-25 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |


[Clique aqui para ver as próximas entradas](README22.md)
