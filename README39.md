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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b867590-0a71-31ca-ad0f-65cb6feae8fe | -7.46507 | -42.67653 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c16d7b3d-4dbb-3023-9f6e-873e42810226 | -13.6554 | -43.92677 | 2025-10-16 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 554c39ab-14ec-3d02-aa63-4af7460e9d06 | -7.85437 | -45.41045 | 2025-10-16 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc86b8bd-8b02-35c3-a00d-5fa669ec6996 | -7.07647 | -44.95156 | 2025-10-16 03:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7c92f7a7-df8a-3dc4-a30b-a0d1b8a5baa9 | -18.57637 | -43.85476 | 2025-10-16 03:49:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c68f952-8b8a-3464-9f55-1a49173ab7b2 | -7.54086 | -42.71338 | 2025-10-16 03:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a0ce322c-b44b-3e00-b918-9a7450cbc9a5 | -8.40968 | -46.25565 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9ff415f-f0d2-3871-b631-bdcfbc5f01c1 | -9.15798 | -41.06294 | 2025-10-16 03:49:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 1d4e5985-c8e3-334f-8fbf-7df4938d2fb3 | -8.24112 | -43.41435 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 352480e3-35f4-304e-a886-91e39a2fedcf | -7.06753 | -41.95147 | 2025-10-16 03:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ecaa6aaa-00cd-3957-94dd-4cbf3f2ea266 | -7.50513 | -46.6432 | 2025-10-16 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9986bbac-4c7c-3f1a-a532-61061ee8f15c | -8.19613 | -43.97026 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 610d01a8-15fe-39fc-8077-750466b350f8 | -15.80593 | -42.45342 | 2025-10-16 03:49:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f1c3cd3-e749-3266-a464-29e22a4183f6 | -7.47681 | -42.14862 | 2025-10-16 03:49:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3393b312-f570-3494-90db-d13ee82935af | -14.46847 | -43.83308 | 2025-10-16 03:49:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9b6ee1a3-c45a-36ee-ad2b-1b1cdfbf70a9 | -13.65124 | -43.92596 | 2025-10-16 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a9073e0-6444-3849-b302-9159fdb7fd13 | -17.21528 | -46.92949 | 2025-10-16 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 140e5d30-40f1-37fe-8361-8a24fe4967f0 | -7.35469 | -44.06887 | 2025-10-16 03:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a9d39e8-9783-3417-9932-8a5f665f38d8 | -7.07751 | -44.94568 | 2025-10-16 03:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b298ac3-ab7e-36a0-a024-e7c5b46445af | -13.81041 | -42.86438 | 2025-10-16 03:49:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 91ddff3f-433a-3ac2-8647-915ecc6ffe60 | -7.64232 | -44.09038 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| adbdb01d-1887-37c7-a21a-a2c3088a35fc | -8.40845 | -46.26252 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ec062a1-fd61-3854-b554-d1a00b06e5a0 | -8.19368 | -47.01596 | 2025-10-16 03:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 964d36b5-0a4d-30c5-bea4-5838f57970fc | -7.647 | -44.0911 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f5138372-61e9-3874-8757-7a4d302c04a9 | -7.67666 | -42.55819 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 54c775c4-ad9a-39f8-8c01-5d28ba738844 | -13.65469 | -43.93064 | 2025-10-16 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d20578da-f651-343f-bc18-591b6444d6de | -7.9427 | -44.13322 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e67dda8-1f76-3626-be69-9652712094fe | -12.98652 | -43.46135 | 2025-10-16 03:49:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 942e25a8-29c6-3755-baa9-5912a34156a5 | -7.14776 | -44.38259 | 2025-10-16 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 74fb27f2-63b2-34b3-94e7-b72647b7d68f | -7.40606 | -44.75149 | 2025-10-16 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b4cee381-dc86-38dc-b114-4ea5ef8cb9d8 | -7.08252 | -44.9465 | 2025-10-16 03:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d184bce-6d0d-3603-b68a-9d93b90b54d2 | -8.25073 | -44.06382 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa3ac814-d8ea-310b-878e-5a49dfe036e5 | -7.95282 | -44.13015 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6416810d-b086-3c9d-a696-0c95cddaa209 | -8.255 | -43.43932 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3654105-c854-3c7f-8f13-d794c677d4a5 | -8.25574 | -43.43501 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f26b4e08-72ca-3b7f-b61e-c27136b16724 | -7.48341 | -42.13455 | 2025-10-16 03:49:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d7b7c31c-df9f-3844-b196-4c38be1240d8 | -8.89996 | -40.56939 | 2025-10-16 03:49:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4311cb47-b972-3843-b5cd-de93d47649c2 | -18.44735 | -44.48694 | 2025-10-16 03:49:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| be7b4c02-f82f-3605-8d5a-3877a4a0a565 | -8.46445 | -46.24532 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41754a04-c55b-3adc-9f74-1ed4e45673e5 | -12.2333 | -49.39236 | 2025-10-16 03:49:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 505bb8c5-07ed-33f5-a917-8848dbe7e2e1 | -7.47358 | -42.67797 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6c888f0c-b670-3de5-817d-b6f7e949d45f | -8.4512 | -44.18421 | 2025-10-16 03:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 869199ea-37a2-3753-88f7-ea00fad6cab0 | -13.57523 | -44.43607 | 2025-10-16 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| aa7eeb4e-a2cd-372a-bcb8-17c8bbfdc248 | -8.06286 | -45.42474 | 2025-10-16 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58ecb39b-5ddd-3914-820d-16c5b232db26 | -7.39215 | -39.70351 | 2025-10-16 03:49:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b994bb5d-fbcd-3d0e-8ffc-b80d24bcbacd | -6.52729 | -44.73812 | 2025-10-16 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20512934-8a88-30b6-8566-60c1066d4ca8 | -7.93805 | -44.13239 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e08f89bb-34ba-3c95-a842-8a75d737574e | -7.35249 | -43.86306 | 2025-10-16 03:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| c67fffe5-c0f8-3ee8-9506-b5900a3785e8 | -7.54083 | -42.06533 | 2025-10-16 03:49:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6814848f-0cb3-3f67-be84-625d6e1f080a | -8.25411 | -44.09915 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2e341a4b-8d83-3848-8576-88d224940a5e | -8.29285 | -43.42642 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6fc31134-101f-3d43-9f8b-556e341bb4a3 | -8.2478 | -44.05336 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b16dc01-3a63-32db-806e-e764a38d2c8f | -15.80102 | -42.02478 | 2025-10-16 03:49:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2662a0a8-f342-363b-a240-e8ead85a635d | -8.5616 | -44.59579 | 2025-10-16 03:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc90eaaa-d547-3683-a093-04d781427957 | -6.40866 | -45.36436 | 2025-10-16 03:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 87663dbb-1ec5-3319-9bb7-581657a69ac5 | -14.07396 | -44.28098 | 2025-10-16 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca080592-9e8e-34e3-a55e-a37bc407f7ab | -7.0383 | -42.73671 | 2025-10-16 03:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2621e314-fcb1-35c8-8bc2-845a04c1b1c7 | -17.60965 | -46.68871 | 2025-10-16 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42148adb-90f3-32c0-872c-f456886f9b8b | -8.29588 | -43.40932 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6d70a99e-0c87-328d-9405-44f55ea19bcb | -7.4364 | -44.7513 | 2025-10-16 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 05266799-d59c-30f4-a4e8-d13eab6c6ba0 | -16.19628 | -43.01998 | 2025-10-16 03:49:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0b940b6-c32b-3311-9a2c-56f4510aa749 | -13.83629 | -43.7889 | 2025-10-16 03:49:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7837dcaf-861b-36a4-9de3-3c3388fcbcf3 | -8.20395 | -47.01009 | 2025-10-16 03:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8752525-68ae-3d09-a6ff-d298d7fa10db | -7.18866 | -42.36493 | 2025-10-16 03:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| baad24ac-43e8-3aa9-98eb-001c11fe8ad4 | -13.63772 | -44.42232 | 2025-10-16 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c7301d8-8b16-38fd-8565-33c936c8f19a | -7.18514 | -42.36038 | 2025-10-16 03:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2d8310d4-a48e-35b5-9d5e-a016589ed39b | -16.24093 | -39.13033 | 2025-10-16 03:49:00 | NOAA-20 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d19fd61b-f580-3e78-a2c5-64e9098766e8 | -7.15825 | -42.51639 | 2025-10-16 03:49:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9e8b0878-2ffd-3838-a47d-9ee966b25254 | -7.47013 | -41.52067 | 2025-10-16 03:49:00 | NOAA-20 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c9984f1b-9538-3734-98b8-ab4fc7a5790c | -5.8518 | -42.8843 | 2025-10-16 03:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 56.0 |
| 2cfd3fb5-f873-34a6-ae7e-cac2805d3fa4 | -6.1723 | -40.8954 | 2025-10-16 03:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 52.2 |
| 16dfa735-84b0-31fd-b972-b124517d1601 | -4.3687 | -43.3838 | 2025-10-16 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 461.3 |
| 69013118-aeff-30f4-8325-9b2c824524fe | -4.1161 | -48.0136 | 2025-10-16 03:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 127.6 |
| bd1a99cc-9f68-3956-8118-c8abe1b2e547 | -8.4528 | -44.1767 | 2025-10-16 03:50:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| ef6a87f5-50d3-339f-890e-ec0a91a9c4fb | -5.4762 | -42.9367 | 2025-10-16 03:50:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 57.0 |
| 8221e791-03bb-31c9-a1ab-ff89a23059a8 | -6.1532 | -40.9215 | 2025-10-16 03:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 104.6 |
| e38fa811-8a5c-38c6-8f37-26204ff4c713 | -4.3872 | -43.406 | 2025-10-16 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 419.1 |
| 0ba6d174-0e8f-3152-9022-dc89812c245b | -4.6626 | -44.0832 | 2025-10-16 03:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 4a27a507-1754-3438-ba36-a4184e02e78f | -4.3874 | -43.3827 | 2025-10-16 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 469.5 |
| dd2ca700-4e57-3d25-8730-864a4ed5c6c8 | -4.6437 | -44.1073 | 2025-10-16 03:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 0bfc1c0e-7360-3d3d-ae13-3dcc04d6b81d | -4.116 | -48.0352 | 2025-10-16 03:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 4db478ea-798f-3b41-98aa-f178c26b2e6c | -4.6811 | -44.105 | 2025-10-16 03:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 37413cc2-ea13-3b05-967c-a34b8784edcf | -4.0974 | -48.0361 | 2025-10-16 03:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 7fd81c1d-5593-339a-a6e4-e89c50d34b33 | -5.8799 | -43.8844 | 2025-10-16 03:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 133e04a2-7867-3e97-990c-8782c3255fe6 | -4.4061 | -43.3816 | 2025-10-16 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 1f716bdb-fac7-38ed-bd61-8d49b12f84f8 | -5.6819 | -45.112 | 2025-10-16 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| a3eaf5ec-3c81-3b66-86b1-aa12223b57f5 | -4.4059 | -43.4049 | 2025-10-16 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| de92039a-3c86-35af-855e-a3d0bcc07911 | -4.6813 | -44.082 | 2025-10-16 03:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| cf940975-bf71-3d17-999b-88b8043f1565 | -4.3685 | -43.4071 | 2025-10-16 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 346.0 |
| 98b01484-fbaf-3a1e-b141-0a5fee4fbad7 | -7.3955 | -39.6845 | 2025-10-16 03:50:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 57.3 |
| 8b4220f9-b7de-3e49-a6ee-2f997b1e44b9 | -3.0158 | -45.3679 | 2025-10-16 03:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 6012748d-51a7-34ac-880d-74565279a480 | -4.6624 | -44.1062 | 2025-10-16 03:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 242.5 |
| d599f3e7-d712-3ce5-87ec-536b15714ef2 | -4.0976 | -48.0144 | 2025-10-16 03:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 157.7 |
| b1d60bab-d405-397f-9e63-144f242aae49 | -8.4717 | -44.1746 | 2025-10-16 03:50:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 3e977ae1-4e54-3622-8dc5-3dc964104ec7 | -6.1534 | -40.8971 | 2025-10-16 03:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 112.0 |
| 8b05a02e-0f25-37c0-8907-cad957053840 | -5.6821 | -45.0893 | 2025-10-16 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| e6e06052-ab9f-3e5e-ba50-cbaeb4be2268 | -3.0157 | -45.3903 | 2025-10-16 03:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 8d67135e-4129-39dc-bc7c-bdf246c6a183 | -19.96138 | -49.42029 | 2025-10-16 03:51:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f4289639-43a1-33ea-80f6-24e17238e70d | -22.0962 | -46.5398 | 2025-10-16 03:51:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d1f2b908-79bd-3a01-9197-8f86ba25837c | -20.39656 | -45.96123 | 2025-10-16 03:51:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README40.md)
