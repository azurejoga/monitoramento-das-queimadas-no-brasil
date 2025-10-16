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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74fdc420-b099-3696-afe4-6939fd0a312e | -6.5687 | -42.97302 | 2025-10-16 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7efc920-0417-3ec9-8286-312f2a7c7842 | -10.12971 | -44.55325 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5de2161a-05ee-3fa9-8d3e-24c1b8079669 | -5.40378 | -41.1492 | 2025-10-16 03:47:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3b700b37-0a9e-3f26-9bbd-06bd1c1c97e2 | -11.5947 | -48.55461 | 2025-10-16 03:47:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a43babbf-95ab-3543-958c-19f7052546fa | -6.37828 | -41.48286 | 2025-10-16 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| a48e842f-8da2-3b20-8e52-872804608792 | -5.87506 | -43.89076 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7be8a9a7-15be-3ccc-8242-5efc1b2ec550 | -5.64622 | -45.9701 | 2025-10-16 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa8e9027-746f-3d16-8c7b-aec9ebd634e9 | -11.47875 | -44.08269 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9d9bc45-db21-37a2-9929-abe6d04dee8a | -10.05696 | -43.8596 | 2025-10-16 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ab3e474-b405-3551-83dc-d5517fbd9813 | -5.72589 | -35.82625 | 2025-10-16 03:47:00 | NOAA-20 | RIACHUELO | RIO GRANDE DO NORTE | Brasil | 2410900 | 24 | 33 | nan | nan | nan | Caatinga | 0.3 |
| dc62a1de-e75c-3cb3-b6ef-d613cc0a85d2 | -4.1017 | -48.03904 | 2025-10-16 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 3303ba87-33e0-362d-8efb-3fc8c09d7970 | -4.39143 | -43.39754 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| bd1f0618-5a95-3e87-87d1-714f94bd59d0 | -3.6811 | -47.6419 | 2025-10-16 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b8ac6417-320b-3509-b243-924c1e24fbe6 | -5.79565 | -35.59777 | 2025-10-16 03:47:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c958a7b7-be86-31da-be19-cc2b12621dc3 | -9.26312 | -44.36154 | 2025-10-16 03:47:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6cd5f488-e287-3160-ba63-8b196e0c128b | -4.3823 | -43.38384 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 1ece1ca0-00b9-3cd3-9755-e2698b35c4c6 | -5.67054 | -45.11048 | 2025-10-16 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73777db4-9a75-38dd-a77f-98f7a7b67d20 | -4.41504 | -40.17775 | 2025-10-16 03:47:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2e417731-f412-35e5-9d40-9fed23dd70f3 | -4.3884 | -43.40557 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 971a4494-f4a5-3c30-bd79-b8efcc239320 | -9.68599 | -44.50267 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13795a1a-dcfd-37bc-9911-fc3fc9d31eb7 | -5.09576 | -44.94607 | 2025-10-16 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2310caa-a1ff-3225-9f86-934c30d18b05 | -4.50598 | -38.26102 | 2025-10-16 03:47:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2cca02be-471e-3f69-b9d6-3eb6f92823be | -11.50438 | -44.06532 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0fb66338-7bee-3987-bc30-226c03dcd879 | -3.67771 | -47.64269 | 2025-10-16 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4cbd597c-e4e7-3669-bb45-93accf58770c | -5.30308 | -49.57335 | 2025-10-16 03:47:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2f13823a-3259-38f6-8cdd-00dd34323f7a | -5.2489 | -43.22958 | 2025-10-16 03:47:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d62dac60-0a3b-3747-8dec-60e845dc858a | -10.13216 | -44.58651 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| dbac5a1d-80f6-3e0a-8f40-51dfd5595f13 | -3.68401 | -47.64373 | 2025-10-16 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 309240a3-4df3-3b73-9fdb-fdfc516d2e26 | -5.8958 | -42.8393 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 96b3c304-6550-3d09-a1af-906b61ce4ff7 | -10.12349 | -44.58842 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6698ccfe-52b3-3258-9ccf-dbfa87129124 | -4.0974 | -48.02582 | 2025-10-16 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 97e2f78d-c162-3b2e-9f6c-f5f7e6ace75b | -6.04856 | -41.90013 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8a0f6d1d-5873-3dcb-bdce-439c8c7c4fb1 | -5.8928 | -39.25103 | 2025-10-16 03:47:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ae33a1ae-981f-3ded-8bb8-eedc58965262 | -4.38452 | -43.39974 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| bd512984-1535-31bf-a57c-7ca23a43c559 | -11.47149 | -44.14826 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8f0265c-7b54-3053-9997-bdd7354cc725 | -6.03774 | -41.92554 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 80e639dc-53e8-3713-adf7-c9b039a13a3c | -6.15589 | -40.91116 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 55aada8e-0a88-3e89-b8f1-7c41cccadc58 | -5.5732 | -41.32537 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 11119d20-a954-3400-afb4-d1d18e8c80b6 | -6.4612 | -35.2522 | 2025-10-16 03:47:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d85715e4-d542-30c0-866e-05095ca9caef | -5.44378 | -41.00876 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 98636fc5-338f-3b03-8840-9ff6164c2aa4 | -10.12948 | -44.57516 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fa60a82c-c135-34e6-a4da-ba2a4fef0e80 | -4.92205 | -45.89916 | 2025-10-16 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8c9ce32-dedd-34f4-bd02-6342b7fb1e27 | -10.05721 | -43.86099 | 2025-10-16 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbab9d49-8d6f-394e-b750-3ca58abf02fd | -6.06204 | -38.76721 | 2025-10-16 03:47:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5c103acf-40b7-3c17-ab74-3e64d2cdc5b8 | -6.13605 | -41.75739 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 055c0324-e63b-371b-85b5-c64dbf08d3cb | -4.66832 | -44.08509 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c74f026c-8f8a-3f7d-b1a7-a4abcca56421 | -5.72067 | -44.52261 | 2025-10-16 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7bbf28c-3bc5-315f-a323-ebe4dd2a20ad | -6.2182 | -44.15737 | 2025-10-16 03:47:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d42ed29-12ff-3483-931e-1b9bc3a55dfb | -10.13581 | -44.56671 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df7ad082-c838-3722-9e8d-158f6ee3cd76 | -5.2078 | -43.79732 | 2025-10-16 03:47:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1a13c58-7497-3d1d-8ae6-cef181db6601 | -6.44356 | -43.37731 | 2025-10-16 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 88900076-65a1-3120-9dcb-3c01277ee71a | -6.13772 | -41.77256 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 81d1e23b-b9de-35da-91b1-57a29899acd4 | -6.13137 | -41.76023 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 93872c23-3898-3c01-9c1a-98b85dbd824f | -6.38668 | -39.73676 | 2025-10-16 03:47:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0bc9fca7-8848-3097-88bb-98a4b853c0f9 | -9.36871 | -46.94887 | 2025-10-16 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 489212e8-0352-3385-a4ab-e1ba4f0424b6 | -10.64629 | -45.24724 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f791c626-67e2-3d44-92ae-3c0be8783732 | -11.57287 | -44.06388 | 2025-10-16 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fc497d29-a422-3cba-bc1f-b7bf4be2683d | -4.94214 | -41.71085 | 2025-10-16 03:47:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 563dfd26-d6a8-38b7-bd45-5bbc27d1f656 | -10.53807 | -47.97532 | 2025-10-16 03:47:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 612ad970-c2fa-367a-ac6f-e73c53563256 | -9.15556 | -46.87263 | 2025-10-16 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| eb057442-ef69-33cb-a8c3-7a8c57051c1e | -2.44192 | -49.3729 | 2025-10-16 03:47:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1b85d1d5-9bae-3ad4-a9bb-3d01a0ee11b9 | -6.41588 | -39.60196 | 2025-10-16 03:47:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9758ea1a-b41b-3839-9b40-751b35a2a66d | -3.6849 | -47.63863 | 2025-10-16 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d53f2337-baca-3b77-bd35-78916b077b58 | -12.65306 | -41.24818 | 2025-10-16 03:47:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e84cdbee-e534-395c-90af-02be441df858 | -5.13488 | -43.34933 | 2025-10-16 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62e9061a-1b93-3c7e-a9ce-13e092c44af4 | -12.67408 | -43.43035 | 2025-10-16 03:47:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| eadd3483-2166-3542-a2e3-bb69cb0a1ac5 | -4.3704 | -43.39749 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 7a684016-daeb-322c-a802-6e44fef85aaf | -6.52488 | -42.207 | 2025-10-16 03:47:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 22bb3433-52da-3830-aa12-929e988f7ff3 | -5.99937 | -44.22373 | 2025-10-16 03:47:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 89dd74b8-5cab-359d-8a33-359d70b04fe5 | -12.83937 | -43.81775 | 2025-10-16 03:47:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8395c36-b8ac-33de-8b41-a5c5d9247b3d | -11.35204 | -45.2702 | 2025-10-16 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07a07ee5-44ed-30d1-a0fa-f38d2d30455f | -3.00615 | -45.38091 | 2025-10-16 03:47:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 696606c4-c7c2-3461-90aa-026d2a4e6ca7 | -6.22486 | -42.49614 | 2025-10-16 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3d40014d-f172-3125-acbd-854248e2dc59 | -5.83444 | -42.34347 | 2025-10-16 03:47:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 7e25d5e9-6b6d-3409-8705-f3df80008fa3 | -10.52896 | -44.50809 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 52b61784-e9ee-32af-9a4d-741725a864f4 | -5.92219 | -42.81768 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 053ac695-f9af-3f47-82f6-27837f1f50c5 | -6.39621 | -42.55657 | 2025-10-16 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7a1225c7-ec6f-33df-9ce4-dde3828b795f | -5.40289 | -41.15442 | 2025-10-16 03:47:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 97ac5eef-76da-3d3c-a958-1630b0cfd1d9 | -9.08223 | -47.94989 | 2025-10-16 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8cb56d09-693c-3e49-b9bb-4dcb5674d329 | -5.00249 | -37.96565 | 2025-10-16 03:47:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 20da9ad7-5827-3d0b-8a0c-084aea28ae51 | -10.51252 | -43.38309 | 2025-10-16 03:47:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48fe08d3-d121-39cf-8ab8-cafc3c26ede5 | -5.74745 | -44.98529 | 2025-10-16 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a7b80b1-38a8-3ca0-aaad-6db73577c219 | -5.88701 | -43.87793 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2af8dcc-f90e-35df-a707-eba72ad7d537 | -11.43048 | -44.14952 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37f0c6ea-0754-3017-b741-d6b98ef36df2 | -6.46499 | -41.88782 | 2025-10-16 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4fce5206-8db1-3084-926e-863bea715aea | -10.12246 | -44.56727 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1eabe1a4-0663-38fb-a1a0-099a30cc9fcf | -5.39122 | -40.89093 | 2025-10-16 03:47:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.2 |
| b0ab797a-052f-3430-b439-bddfddc0b346 | -10.7136 | -44.53112 | 2025-10-16 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a7bd29e-ee68-34a3-bfc8-6e039c01e72a | -11.56946 | -48.56569 | 2025-10-16 03:47:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f02da459-1f00-3a65-ab33-608ce5d89622 | -11.4751 | -44.15343 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae930780-d799-3136-8e03-d9841d303990 | -4.15986 | -46.79642 | 2025-10-16 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 40137148-a08f-3a5e-b3dd-caea3e5530db | -4.92639 | -41.5511 | 2025-10-16 03:47:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0905c5a5-6e33-3aab-b6b5-0a9d3e90c6ce | -6.06859 | -41.90729 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 76aa3dda-c652-3b84-bf59-564a3d74e60e | -3.01835 | -45.37563 | 2025-10-16 03:47:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4eaaf2bb-f0a2-3293-ac8e-c859c18d2ae0 | -4.37732 | -43.39524 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 4332b874-9b7a-34c9-a0de-91e7d39d5b11 | -6.03927 | -41.92952 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 32fead06-fe9a-3a1f-9651-16159e4a4c6d | -11.44644 | -44.16153 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc6b1e93-368e-3baa-8c94-2ff8c0685bf7 | -11.70688 | -44.2751 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78aff94e-6f91-3ebf-b4dc-b47464dac67d | -6.0469 | -41.93465 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 7b372abe-5908-32f5-a4f8-9ab3dea83df0 | -11.9655 | -44.24629 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README21.md)
