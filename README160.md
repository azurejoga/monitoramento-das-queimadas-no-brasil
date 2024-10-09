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

## Dados Diários - Página 160

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6eea0fa1-d4bc-3b24-a53b-3e8363ddc477 | -6.94671 | -45.2299 | 2024-10-09 05:01:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fa7e6d9-297b-316f-8ab7-a45ea73a5bda | -7.73933 | -46.58316 | 2024-10-09 05:01:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3fc99c7-d547-3345-b961-9838ce82b0e8 | -7.48452 | -46.67032 | 2024-10-09 05:01:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 929ffae8-dec6-35e1-867b-aabafc3712aa | -7.48405 | -46.67372 | 2024-10-09 05:01:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 826976b4-90a9-3366-b3ff-e9afcb94cecb | -7.48357 | -46.67712 | 2024-10-09 05:01:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b632198-bd05-3374-b487-6faa1ae6790b | -7.26007 | -46.34233 | 2024-10-09 05:01:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e956f726-cbbc-352d-be5e-c5d7b84f2a71 | -6.66429 | -46.33762 | 2024-10-09 05:01:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9310cb1e-37a5-3b96-8456-bb54ba4d10b0 | -6.66381 | -46.34101 | 2024-10-09 05:01:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c25c062-4a84-33ec-9728-c2cf43a0c924 | -9.26736 | -45.79216 | 2024-10-09 05:01:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c86adda6-d586-3785-86ef-c15610595cd7 | -9.26145 | -45.79177 | 2024-10-09 05:01:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 079f984d-b400-31e2-8cee-6bf4110f92e3 | -9.26659 | -46.75484 | 2024-10-09 05:01:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ea7253c4-eacd-3268-92dd-fdc13bbe9cb9 | -9.26155 | -46.75057 | 2024-10-09 05:01:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ff698713-f04a-3981-a84d-dd1d86ffccca | -9.26109 | -46.75414 | 2024-10-09 05:01:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bed31985-ed8d-3ffe-9085-114fa11bc578 | -9.25986 | -46.72055 | 2024-10-09 05:01:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3524d544-046a-3e53-a85b-22f29d0e34aa | -9.25939 | -46.72418 | 2024-10-09 05:01:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f076d58-bf90-3f00-ae27-a5e5cdb3f965 | -8.26871 | -46.86849 | 2024-10-09 05:01:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ede23ebd-f690-39bb-a178-ff73ff556da7 | -8.26327 | -46.8682 | 2024-10-09 05:01:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8920a20c-00ab-3270-8481-88e89ca2328b | -8.24456 | -46.28716 | 2024-10-09 05:01:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 48ac268b-ca05-3627-85f3-96c2170d8693 | -8.24406 | -46.29089 | 2024-10-09 05:01:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3d3a8012-056d-355e-8fcc-809347190594 | -8.24357 | -46.2946 | 2024-10-09 05:01:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b049bd94-3c1d-37c9-bce0-70c51894c2da | -8.23898 | -46.28624 | 2024-10-09 05:01:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 44ec0463-dec3-3f3f-88da-5342ca8574a2 | -8.23848 | -46.29 | 2024-10-09 05:01:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3f3bd829-de90-3db5-83fa-89d47ac8ce18 | -2.18987 | -46.07854 | 2024-10-09 05:01:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| adf057f2-f836-35ce-b4f1-b5afa91b8685 | -2.18939 | -46.08168 | 2024-10-09 05:01:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c121f815-8246-3b0d-a647-79855f102c02 | -3.31151 | -46.99081 | 2024-10-09 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0f99e28-615f-310d-bf42-5c382bd95228 | -3.31148 | -47.02534 | 2024-10-09 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26d73b42-d8ea-3a72-b1f3-e364f6b2dc4e | -3.0728 | -50.48457 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa8eff4d-5eff-3d09-bf18-a85f9b82a0be | -2.60364 | -47.34527 | 2024-10-09 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4ccadde-8013-327b-96e5-75cb11b39569 | -2.53825 | -47.22625 | 2024-10-09 05:01:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a716bd7c-d4b4-33fc-b3fe-584af4e4c163 | -2.53746 | -47.23153 | 2024-10-09 05:01:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aaa773c9-f357-368d-aea1-f2db194bb678 | -2.52781 | -47.23009 | 2024-10-09 05:01:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 652b00a3-ac21-3bed-be2d-a61e1a137a05 | -2.36269 | -46.49157 | 2024-10-09 05:01:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05f28328-327c-3cf7-a7b1-b9e5e8762035 | -2.36224 | -46.49451 | 2024-10-09 05:01:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1eefe7b-12fb-39a9-bec3-5bf1b0d123da | -2.32153 | -46.72643 | 2024-10-09 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f8948e9-d6ca-3469-9ac1-4b3d81bbbaf9 | -2.30044 | -47.24488 | 2024-10-09 05:01:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbd60739-247e-3757-977f-5c635f6d76a3 | -4.7344 | -46.65536 | 2024-10-09 05:01:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b9a70ae-073b-3755-a5c6-3d311d85837d | -4.73348 | -46.66188 | 2024-10-09 05:01:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a836880-a400-3a87-a71c-92eae64a9c55 | -4.73303 | -46.66504 | 2024-10-09 05:01:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c12b6a68-a5ec-3f6f-afe5-cee9d931135e | -4.73288 | -46.65786 | 2024-10-09 05:01:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb6b5663-ed86-33e8-b311-b9df2cc96bef | -4.73192 | -46.66429 | 2024-10-09 05:01:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24247e22-5178-3a5e-ac25-50be40fa1843 | -4.52607 | -46.6129 | 2024-10-09 05:01:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ff2d1bc-d22c-3792-a27b-023bf91bb870 | -4.52133 | -46.60897 | 2024-10-09 05:01:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03a725f7-75be-3ebe-a6bb-32653ebbdc8a | -4.47327 | -47.73458 | 2024-10-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aee4908d-e5cd-3f19-91db-7293b8e99d6f | -4.47295 | -47.7373 | 2024-10-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6b91122-16df-3534-af9b-3467d36cea16 | -4.31658 | -47.70354 | 2024-10-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b1c3d41-c849-3532-aa50-0c6fc5fc7e9d | -4.3158 | -47.70884 | 2024-10-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85464410-b6f6-3874-8f46-6085085f75f3 | -4.21216 | -46.8497 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| abfa5c51-18c7-387e-b499-f6c710f6d3b9 | -4.21173 | -46.85265 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 75e02a0e-cbef-32a0-b10e-df90f984f4ad | -4.01088 | -46.54165 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d149a190-f55b-3df9-96eb-7b21dd130206 | -3.93817 | -46.44846 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89980fe3-a81e-3fcf-825e-13896b0b9f26 | -3.93772 | -46.45158 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a3bc5fac-b304-39b5-bb45-f4e86055aa59 | -3.93728 | -46.45461 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| daca3f6b-b0f0-3801-8380-266cd804318f | -3.93687 | -46.45741 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b514eb15-20e4-36a2-8caa-ea869aee9295 | -3.93389 | -46.44138 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6ec0afd-953b-3e29-9e02-3234ab0fe1c3 | -3.93343 | -46.44456 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b1a00ad-b87f-3703-a4d9-9cad4b60d679 | -3.93297 | -46.44772 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38ec1669-c5de-3edb-a9b9-dbf84f05617e | -3.93251 | -46.45086 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0dc64201-488a-3902-94c6-61a817bfbb62 | -3.93206 | -46.45398 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 927627cd-53d3-3253-8af2-9ec2e717c15f | -3.93163 | -46.45689 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 90c63103-f5ad-358f-8470-81a2d864b4bf | -3.92869 | -46.44057 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a7369c3c-aca2-3684-a6c2-5906a4dab952 | -3.92823 | -46.44377 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 83b483c1-c7be-376c-9aab-cc6f5dbb2350 | -3.92777 | -46.44695 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 85e933b1-6d84-3eb6-94c4-3d248c252f72 | -3.92731 | -46.45011 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f7cb2a43-1e4f-38c4-85a6-32a178bff2ea | -3.92685 | -46.45326 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d59df227-7803-3b24-b18d-ea33cb09ef9f | -3.92641 | -46.45631 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 261d2ea7-1507-3cd6-9755-2274d296e9a9 | -3.91036 | -46.45717 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| dc137070-ac4c-3488-ad2c-1ca74613fe9f | -3.90519 | -46.45629 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b6068f3e-5274-35b7-ac61-331acc67fcc7 | -3.90472 | -46.45951 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| fb50db77-549e-3db2-81f1-2e10959d1250 | -3.90426 | -46.46273 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c199a53f-70d3-3c6b-923b-2007f0f43540 | -3.90382 | -46.45873 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 32b533ad-7b75-35ad-bc20-a8b8ac5ad79a | -3.90381 | -46.46589 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1b625896-fc7f-39f6-952b-db9c3d9fa0dc | -3.90333 | -46.46195 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 6dc9fc81-ee6f-3842-b2f3-4969f2d79044 | -3.90285 | -46.46511 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 623b0888-0db3-324f-86aa-c2aa867c57cf | -3.90044 | -46.45235 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b439754f-d28e-394d-b9b8-793a7374a3d8 | -3.89998 | -46.4556 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a35cb1e9-760e-3176-a5a7-17002ccdd26e | -3.89952 | -46.45881 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 12aae043-e181-3a7a-80fc-1d15b2e0d198 | -3.89909 | -46.45486 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 9ce16ed0-2724-36f5-8d75-a007567d7012 | -3.89906 | -46.462 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1d4c7b8e-f509-3e16-a2ee-80aec8f5c9e5 | -3.89861 | -46.46512 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 28f8e67f-05c4-30ed-9f28-3e3932b29b54 | -3.89861 | -46.45806 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 2de64d58-1546-34eb-9bdf-fbe94eba7870 | -3.89813 | -46.46124 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f088caf0-bb58-3c96-910c-92e735c6c8c8 | -3.89523 | -46.45168 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8f7824a5-c501-3aa6-b525-b9b1d4fb0ac2 | -3.89477 | -46.45496 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 203dc254-5770-3085-8ee5-206e2b653c07 | -3.89431 | -46.45812 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8b474e32-0666-39b0-a286-659f39161442 | -3.89388 | -46.45422 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98e2ab93-b730-3730-9b19-c71e1762548a | -3.8934 | -46.45739 | 2024-10-09 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7f2f9214-bfb6-3ab3-9404-027ba4e07cd6 | -3.80996 | -47.49079 | 2024-10-09 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60409b1a-9547-389d-861d-301c2cd6ddb1 | -3.7014 | -47.59625 | 2024-10-09 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5b1b70df-00f4-3fe0-b956-2b51d2bef269 | -3.70062 | -47.60143 | 2024-10-09 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a112e01e-c56d-3f94-95bb-5f46e77eb59a | -3.69984 | -47.60663 | 2024-10-09 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 76973b32-63fe-3a59-a7f5-ae85bd1b19d9 | -7.67919 | -47.31399 | 2024-10-09 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6bc4781c-bbf0-32de-b87c-24ac6827795f | -7.67877 | -47.31708 | 2024-10-09 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06889d19-4991-3c79-8e04-c3f7b5b7cd07 | -7.67835 | -47.32018 | 2024-10-09 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05015570-6bad-3947-9271-f153a60ac6d4 | -7.67402 | -47.3132 | 2024-10-09 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6524aae9-eff7-304d-8be3-1ffd91f1d9f3 | -7.67359 | -47.31632 | 2024-10-09 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec92a995-639e-352f-9d98-4ca1c0817d6b | -7.48438 | -47.58703 | 2024-10-09 05:01:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3731f57e-17cf-3c55-9ed4-361aed480576 | -7.48397 | -47.58997 | 2024-10-09 05:01:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42e9aba3-b127-3ab4-abd7-b8c118011b7b | -7.48315 | -47.58696 | 2024-10-09 05:01:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37bb1bc7-fe04-3ca4-95c6-3e91c1be125f | -7.48275 | -47.5899 | 2024-10-09 05:01:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72dec868-4793-3b84-9e54-cb316d8e4b0f | -7.41394 | -47.86888 | 2024-10-09 05:01:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README161.md)
