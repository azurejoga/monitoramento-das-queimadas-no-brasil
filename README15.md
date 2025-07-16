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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53e3e4ac-3931-3ebf-8861-f0834c7ee78d | -8.51237 | -43.30576 | 2025-07-16 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 65e17b7b-742e-3f4e-a288-745cc81769aa | -13.09493 | -47.27938 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7bcef3d-1d9a-3dea-9c57-2e0a64bcebc9 | -7.84199 | -44.19532 | 2025-07-16 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28d8a146-03e0-3363-8877-68830ed40bab | -6.94651 | -42.72045 | 2025-07-16 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| be7b952f-c89c-3d4b-9bf5-8cfc63c792fe | -8.94724 | -49.83468 | 2025-07-16 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca976f41-138a-3e15-af01-9a2b03d1c633 | -7.19588 | -43.12273 | 2025-07-16 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 8c8f53a7-6fe5-368f-96f1-ce8006251770 | -13.20951 | -43.12627 | 2025-07-16 04:14:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f30074c0-57c8-3548-8b02-8c55a02e2d08 | -7.10151 | -43.65712 | 2025-07-16 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c980ab5-65ba-3f1e-baf8-80831aef3dcb | -10.31849 | -49.91978 | 2025-07-16 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16e6e685-5886-3a3e-8c04-6302db8cc977 | -6.87061 | -41.72807 | 2025-07-16 04:14:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a516c24c-9a8c-3179-b95f-0f0b85472196 | -7.90277 | -55.41976 | 2025-07-16 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2723e6d-3c48-3adf-a0cc-c2f35863cd31 | -6.55123 | -44.67757 | 2025-07-16 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49784d6d-d169-3c5d-83bb-59304e38c17b | -7.31167 | -45.77095 | 2025-07-16 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| deb1cc2c-edc4-3a14-86d3-6c959f060cac | -8.23528 | -44.92055 | 2025-07-16 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2dfc361f-21af-3666-ac84-a708bf7f2596 | -8.75759 | -46.5991 | 2025-07-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 66aeacf7-9035-30c6-8302-0b8979c8c842 | -10.28349 | -47.61647 | 2025-07-16 04:14:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 737fca49-b6cb-35ec-b819-7de44d079639 | -10.27904 | -47.61881 | 2025-07-16 04:14:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| be373b75-59f5-3598-b244-640386483e03 | -12.5725 | -48.88161 | 2025-07-16 04:14:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| badd2c0d-7ae4-3274-8b12-5e97d3bb4a6a | -12.56645 | -48.8875 | 2025-07-16 04:14:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 11a5264d-7d72-31b4-bf8c-0818b284dd06 | -11.5871 | -47.31366 | 2025-07-16 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 698f204c-7292-31f4-b4e7-b79f9f3098c4 | -7.94076 | -49.65985 | 2025-07-16 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c81c27bb-28d0-3ddb-8bba-43c3c14d10d3 | -12.5641 | -48.88494 | 2025-07-16 04:14:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8bb83eaf-4364-300b-a08d-fbf1e6a61d87 | -10.9633 | -49.25293 | 2025-07-16 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bf3d3b4-069f-3c88-8acf-025263e80864 | -9.4955 | -48.13085 | 2025-07-16 04:14:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f874322-5a14-3573-8277-df7666dfc18c | -8.24476 | -44.92575 | 2025-07-16 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adb0229e-764b-3f85-8b20-ef8a6e1c7266 | -12.47364 | -46.91897 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b031c6c4-4cba-3005-bc8f-2945278b951b | -9.42883 | -40.36676 | 2025-07-16 04:14:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 20.8 |
| fa1c8d59-f0a0-3549-b696-ad9a09139d95 | -7.46084 | -43.83509 | 2025-07-16 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ffd5015-ada8-316a-a739-19b1071138d9 | -12.49439 | -46.92253 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9290965-3786-3e60-8bea-32d59081bf9e | -8.90801 | -47.33884 | 2025-07-16 04:14:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a4c6474-2635-3572-aad1-0fcd54204e4e | -8.91127 | -47.34644 | 2025-07-16 04:14:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80622b88-2501-32b4-9ebb-c25f67d434d2 | -9.30511 | -44.84561 | 2025-07-16 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1882a140-052a-3400-a3a2-587188894ad9 | -7.94148 | -49.65561 | 2025-07-16 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| afe80360-0e4e-3aab-ad3d-cef7a06bd09c | -12.99646 | -44.88062 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4feb9f30-47ed-326c-960e-e705e3730eb6 | -7.20748 | -45.32845 | 2025-07-16 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7896c65-3a06-3a22-8e87-d42428c64c01 | -12.49309 | -46.93028 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc986c80-3205-343d-8f48-5e836b22e8b7 | -9.43186 | -40.37169 | 2025-07-16 04:14:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 5e98b2dd-893f-3d2d-b3ec-66909d1900c8 | -12.4786 | -46.93179 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67967554-45e8-3670-bbf2-34dc819c7253 | -12.47018 | -46.91838 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2f7d6ba-c697-36a7-9d85-e745000b9be3 | -12.5671 | -48.89034 | 2025-07-16 04:14:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16b18372-2c4e-3f26-9703-09c1c43de2d7 | -11.47069 | -47.31593 | 2025-07-16 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd78df7d-174a-3728-806a-30dff63d9b38 | -6.91952 | -52.85421 | 2025-07-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d3ad96e-a5cd-324a-9be0-080a56981638 | -8.24868 | -44.92274 | 2025-07-16 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fbcbdbc-4784-3189-b838-6600fe5234cf | -10.27983 | -47.61585 | 2025-07-16 04:14:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 29b10149-0633-34f6-9642-62b118dbd0b5 | -7.26381 | -43.51311 | 2025-07-16 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 62d4d4e0-6b24-3017-aedd-8d918404fdf1 | -7.94506 | -49.66058 | 2025-07-16 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33166a8d-a2df-3fa0-8041-21b96dcd6a8a | -7.10205 | -43.65365 | 2025-07-16 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4b69c4b9-2a84-3c55-a322-bd9fcb8f176a | -13.02211 | -45.0619 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| e26b4974-2576-323e-970a-1fd982e40a91 | -7.05008 | -43.48951 | 2025-07-16 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| caa41f2b-dad9-3ea6-ba4a-581d988856b8 | -7.00444 | -44.47941 | 2025-07-16 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9efbfabb-846d-3018-9dce-404a1775ba15 | -10.56662 | -49.13821 | 2025-07-16 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3e2411f-af1f-354e-868e-99dda8b0473e | -10.64946 | -49.47419 | 2025-07-16 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bd78605-ffa8-3174-b1b9-7c27c31786f3 | -13.01494 | -45.06434 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 31b1bb25-d99e-38e7-9177-6604859fb002 | -11.95199 | -48.41896 | 2025-07-16 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 9c107c3f-9b8c-3137-9bfd-cb67dcac3a4e | -10.27978 | -47.61447 | 2025-07-16 04:14:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23232438-d4c9-31c8-896a-2a44b06b84fe | -13.09869 | -47.29974 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cda5ff00-2667-3661-8fe6-49e786b051b8 | -12.4799 | -46.92403 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd09ab37-82a4-30ee-9725-280ce32c4129 | -6.73345 | -44.3271 | 2025-07-16 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1de6f76d-3b8d-38d5-8e13-262c4d2108ad | -7.50885 | -46.69132 | 2025-07-16 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 028b18d6-9a11-3fed-af5a-c55016daa02d | -12.48682 | -46.92522 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08c3bd9a-314a-34e9-9c31-a69f6d902523 | -6.73176 | -44.33766 | 2025-07-16 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| b19c7544-2582-3d26-b544-7637c2c2c7e0 | -12.98985 | -44.87953 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 112f2eeb-7446-3562-8b85-a3c2a8a081d2 | -12.07788 | -43.9808 | 2025-07-16 04:14:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e6ae2ca0-1427-38a0-bba3-d4f393afffe6 | -11.87137 | -55.45377 | 2025-07-16 04:14:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e019164b-91aa-3103-b8ab-c535de1653a6 | -8.5019 | -43.30767 | 2025-07-16 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 777adeb4-5a34-3dd4-bf61-e73c50fbcef2 | -11.46919 | -47.30304 | 2025-07-16 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 144cde03-8863-38d5-aafc-fbddaaa8ecba | -8.24256 | -44.91806 | 2025-07-16 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a16e99c7-b00e-3bd2-987c-7847f5dde72f | -12.56265 | -48.8868 | 2025-07-16 04:14:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de8f2bb2-173b-3f44-abe4-24e8810fd046 | -10.65289 | -49.47851 | 2025-07-16 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e0b40751-df12-353b-9a95-a9ae90259742 | -7.21431 | -45.32959 | 2025-07-16 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c7af5cc8-349c-37f9-9745-52329189d025 | -9.60221 | -40.55752 | 2025-07-16 04:14:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9dce6126-3893-3ba1-9461-ba694711c186 | -11.95414 | -46.74995 | 2025-07-16 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 935dac51-ce6a-3c33-a7fc-622bb9249f4e | -10.57432 | -49.11783 | 2025-07-16 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb34ada2-2f12-3d0c-8c45-a53df11c0718 | -13.05283 | -47.81118 | 2025-07-16 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b00a5e8d-bdc3-38c2-8694-2e7a4438b68c | -11.45932 | -45.10152 | 2025-07-16 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fac70324-21e0-3f4e-8ec5-a71f0d62a641 | -13.01768 | -45.06842 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4718856b-c88c-3f42-bdeb-84c5cb2f2491 | -6.96771 | -42.80222 | 2025-07-16 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 271d52ff-90c8-3422-9ee9-ee1c034cb0bc | -10.64722 | -44.48306 | 2025-07-16 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e0d35f8-f89a-37e9-8248-45b0898969ca | -12.48747 | -46.92134 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d1f8c0a-e852-33ac-b172-7ecb770b60dc | -7.04954 | -43.49297 | 2025-07-16 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3dacc5b-b736-369b-be38-33589c891194 | -7.50594 | -46.68653 | 2025-07-16 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 023bcc2b-2d9a-33aa-99d4-66541a38fbeb | -6.63667 | -44.57415 | 2025-07-16 04:14:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d81ff110-746d-3ef9-aed8-a3ad538a2238 | -10.64475 | -49.47713 | 2025-07-16 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b767198-7dfa-3dc7-82ce-df351db3f489 | -9.49169 | -48.1302 | 2025-07-16 04:14:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09dac885-861d-3e8c-8324-d73c27508e5b | -11.94826 | -48.41827 | 2025-07-16 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| d1e06830-8ea0-3b35-ac51-a6402ed1c1d0 | -7.83812 | -44.19825 | 2025-07-16 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9f9ea11-7e96-303e-ad75-c69d90f9ed9d | -10.56971 | -49.12067 | 2025-07-16 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a9272bee-c40a-3b0a-be55-c80d8c20d59a | -7.34558 | -49.60513 | 2025-07-16 04:14:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88ffbc42-13ce-3ca0-baf9-47684af71503 | -11.49327 | -48.07341 | 2025-07-16 04:14:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b62da2f6-a6e9-3d29-9a93-9d1d5dcd0f5b | -12.15027 | -44.81752 | 2025-07-16 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a11a162-b15e-358d-9f20-dfc7df3a31f0 | -12.48271 | -46.9285 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50cb2013-924d-356a-bf2a-f588898fd1bb | -9.31177 | -44.84669 | 2025-07-16 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4404f32-8653-3b83-a8aa-4c3922a55b44 | -10.38615 | -49.75924 | 2025-07-16 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ac456d0-32ae-34dc-aa40-c3ec7014666a | -12.48899 | -46.93357 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 643cd715-d02a-3de7-b8b1-fe0df0afea95 | -9.85293 | -47.87774 | 2025-07-16 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a669b32-ea9a-3292-b918-22ed56361d8b | -8.86575 | -49.03303 | 2025-07-16 04:14:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dc17b66c-aeef-33f7-8c08-83233382a42d | -6.92436 | -52.85846 | 2025-07-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70febd44-44ed-360b-8d39-7a002d96c448 | -10.65353 | -49.47489 | 2025-07-16 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2b9a6673-9c0f-3bde-a8e9-49025be98fb0 | -12.47449 | -46.93508 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bd7e477-b58a-3503-90b7-62d95e0669ae | -8.5412 | -47.84917 | 2025-07-16 04:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README16.md)
