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
| 0ffa38b2-0ff0-3141-ba9e-6c78304f89af | -5.32002 | -55.87887 | 2025-09-02 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab3bfc0c-b6d6-31f5-be77-6d360a63b5ad | -6.84384 | -52.81001 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ac41796-350d-3656-b777-71f18f80bfb8 | -8.71174 | -50.44873 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55ac391b-d66f-3d59-90ab-58b5d2795320 | -7.41832 | -44.80601 | 2025-09-02 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb95258f-1ac0-39e8-9c8e-46465204e6dd | -6.87579 | -45.85438 | 2025-09-02 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1416e174-e8e0-371a-9f7c-42b6e0177c61 | -8.19274 | -46.78423 | 2025-09-02 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 166d3bb1-95c8-3ef0-9725-6ae1f1cafc58 | -6.83046 | -52.82508 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42ef9314-8301-3857-9949-524805bb3e44 | -6.27579 | -44.51125 | 2025-09-02 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a23291fe-7a98-3bbf-ac51-5e06966951a4 | -6.82448 | -52.81567 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4421557f-3b28-32d3-9c19-75b5c2a96548 | -7.98199 | -46.46114 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6c0b91aa-df7b-3617-9397-35d537a112ec | -6.85844 | -52.81918 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db007140-a0fb-3084-962f-dc044c69cb63 | -6.82024 | -52.81932 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ffce1ea3-90b0-3f90-b59e-ffb79b303c0c | -6.88043 | -45.86338 | 2025-09-02 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1a3eeee-d99b-3377-9878-7a77b84c6722 | -7.91652 | -46.45022 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f159d5b-649f-3398-8c7f-6172a36c8353 | -8.70753 | -50.42914 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6eba7ae-bf28-36e6-8a27-f6db194b4aee | -8.70578 | -50.44142 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 23f855ef-9bdd-3a46-aaf6-8eab318d77d9 | -6.8413 | -52.82674 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75e38bb6-0ebd-34b5-868a-dbfb78e8db7d | -8.7132 | -50.45081 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 85fac90e-5c96-356a-8fc7-314d6f81d168 | -6.82559 | -52.83289 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5344d9c3-f1d3-3c63-9240-843a7d2c0b87 | -7.12497 | -44.56936 | 2025-09-02 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50e9efa2-a0f5-3d4d-a27a-7c1d35d97bb8 | -6.39959 | -58.21038 | 2025-09-02 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c337dc8a-99dd-38c2-9c8e-d391dbe72539 | -7.48384 | -45.36675 | 2025-09-02 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e70a6645-529c-3ebc-bfcd-68ffd9b2dbfa | -6.77324 | -52.81218 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1a51e769-26d9-3018-acb5-be6512b2991e | -4.22192 | -47.21146 | 2025-09-02 05:04:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34f5b793-dbfe-3e39-ac52-4b55462c2040 | -7.71686 | -50.25422 | 2025-09-02 05:04:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 86174b6c-861d-3d03-91ae-2bc33c60ed08 | -3.78998 | -47.57022 | 2025-09-02 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3a2accce-9bed-34da-9d5c-dbd9c09452be | -6.80876 | -52.8219 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d2b81c6-d67b-34e6-85d4-c520ce7a75df | -5.85244 | -43.01174 | 2025-09-02 05:04:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| c0f31a5c-a71c-3db1-9a5a-f9e2886da38e | -5.69338 | -45.95388 | 2025-09-02 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82e6b5f4-73e6-398d-911a-0beb08c6df5c | -8.13244 | -45.03782 | 2025-09-02 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b686517-7403-3f60-b01c-2aa322f66bfe | -8.74722 | -46.12278 | 2025-09-02 05:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82a6cba1-ce43-3abd-926f-3f04e48c20a5 | -8.88607 | -47.97333 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4367bd7e-9a43-3341-9066-7e7433952fa9 | -7.70105 | -50.27326 | 2025-09-02 05:04:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e9ef5de1-506c-38d6-8a6c-34faa61c51da | -3.69449 | -52.32381 | 2025-09-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85fffa07-b701-3d3b-bde0-a04077b86934 | -6.85366 | -52.80132 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3e7078e-92b2-3e13-8a25-47a1bfaccd96 | -6.33619 | -58.16971 | 2025-09-02 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c48e4d06-9e71-3e15-80e4-20110baffa11 | -7.8501 | -46.74007 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5195f8f8-ce50-39ef-b284-707713ff22fd | -6.34189 | -58.17843 | 2025-09-02 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 89576eb7-cb04-3597-b9f7-8218778afce3 | -7.63793 | -46.55566 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7761ef5c-f3f6-3b62-8ac1-b3d892a59d8e | -7.2787 | -60.65106 | 2025-09-02 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c43221b0-6a9d-32ce-97dd-ee172cc7625d | -5.85563 | -46.61389 | 2025-09-02 05:04:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4b31397-0288-35ef-9af7-683139acb1f0 | -6.85667 | -52.80603 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b98cf32-3af4-327f-95bc-7c650c8af1fd | -3.72774 | -58.83992 | 2025-09-02 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60dc46e8-f0c9-39e0-93df-626756574c3a | -6.79793 | -52.82019 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b465933-fc1f-3950-8ff2-3c07f64a9e1f | -8.70694 | -50.43326 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 227b1d6b-83e8-3495-aebb-5065d4b016e1 | -7.71027 | -45.01679 | 2025-09-02 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 963cf8f5-b882-319e-b983-8375ae7a454f | -5.57352 | -47.42449 | 2025-09-02 05:04:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dcb0eb21-b9c7-3917-89b6-6a43d4367b00 | -6.22146 | -53.5756 | 2025-09-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a908fd5-42b0-3506-8cd3-5456c772f542 | -6.98148 | -44.34132 | 2025-09-02 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c2b2315-a3b8-3224-8f13-0023c2d44546 | -7.77681 | -45.44913 | 2025-09-02 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b06f54c-31cb-3493-81d1-748a7940bba9 | -2.44627 | -49.36351 | 2025-09-02 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cffea150-9fbc-3f0f-8cc1-b465ec426317 | -6.20135 | -45.40112 | 2025-09-02 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1cfadca3-30a7-327e-811a-de3adbdf998b | -6.98181 | -44.31438 | 2025-09-02 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6d5224a0-715f-35d5-8b3b-eb1bf1307480 | -6.8536 | -52.827 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51593633-d75a-3aef-90ee-1b7021a9935a | -7.55356 | -45.69831 | 2025-09-02 05:04:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a0dfb38-264d-3ef8-abf1-6a733d95fe4e | -6.9886 | -44.33624 | 2025-09-02 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d622f77-2124-31bb-8361-7a79c621d2da | -3.72408 | -58.83932 | 2025-09-02 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f6a3bdd-18da-3c5a-aa00-55a93ff2e743 | -6.34068 | -58.18605 | 2025-09-02 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1d57ce7-b26f-33a7-bd63-cb2e667aa839 | -8.18727 | -46.78342 | 2025-09-02 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ae9d251-84a2-397b-a349-7fc097ab213b | -5.01289 | -47.65017 | 2025-09-02 05:04:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fc3e4a3-5301-3692-bb43-e0503baac9de | -6.17607 | -47.27969 | 2025-09-02 05:04:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f9f45102-170f-398d-b3e5-6e245cefaf75 | -7.46764 | -44.81272 | 2025-09-02 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8d98768f-a643-3539-a2dd-04ccd096ab40 | -7.37952 | -48.18928 | 2025-09-02 05:04:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5493a0cf-47a8-3830-8009-14b6e9d06138 | -8.85145 | -47.54757 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10e25371-bfca-3440-8ba3-fc686ecd27e0 | -6.72549 | -42.26153 | 2025-09-02 05:04:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f8db0969-750a-3f5e-8385-61f5a54272f5 | -7.6962 | -50.27671 | 2025-09-02 05:04:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 800d16e1-f256-3d91-ae35-0628f3dfeb65 | -2.77248 | -48.60781 | 2025-09-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f318cf52-9b91-3cc2-8980-c0982bc34a06 | -8.13622 | -49.83271 | 2025-09-02 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| acb32080-fb00-30ea-aea4-8e516368418a | -7.9292 | -46.4403 | 2025-09-02 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 777f5393-8817-37dc-beba-23d333ac4683 | -6.17564 | -47.28276 | 2025-09-02 05:04:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bca20bac-682c-36b2-b19c-4028547f5297 | -5.91887 | -61.30441 | 2025-09-02 05:04:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf44ac76-b496-3088-8782-eab57a2ec1de | -7.70899 | -45.02266 | 2025-09-02 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1154146-da1c-34cc-b6dd-3681cdba422a | -6.19338 | -53.76194 | 2025-09-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7cd7382-929b-3ae6-a07e-595ecc46d464 | -4.22682 | -47.21105 | 2025-09-02 05:04:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0416082b-4817-3410-acf4-d63e9ac5197a | -7.72112 | -50.25511 | 2025-09-02 05:04:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a43c70ee-1503-3a5b-85ae-b8673c86cda6 | -7.79281 | -45.44771 | 2025-09-02 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f499417a-de27-375a-b268-66923ae2b8a9 | -6.85421 | -52.82285 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49255723-d577-3ff5-a71a-8bedbd95039d | -6.86638 | -52.79033 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f425b52-2f4d-3c20-9cb3-271de721d398 | -6.79255 | -52.80666 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3c6d5f6a-6537-3521-b44f-b20574b9a38b | -6.33988 | -53.43866 | 2025-09-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24d05a78-8ae9-345b-a4d1-645b5a7a9fdb | -8.71603 | -50.44937 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2884c880-07e0-3a67-a291-aafec88a4ba7 | -8.01547 | -44.04922 | 2025-09-02 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bcbc6f4a-442d-3f6a-b8c4-255c2dd989b6 | -7.87551 | -47.97046 | 2025-09-02 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 345b1571-7cfa-3607-ae3a-d4eb20143f97 | -6.85829 | -52.81228 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f320b55b-cf03-33cd-8b0a-5f162fd954aa | -6.42993 | -55.61252 | 2025-09-02 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66b3eea7-3108-3ace-a6bc-275a4c0f9199 | -9.12976 | -46.04998 | 2025-09-02 05:04:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 65adab41-2e85-3cf3-baff-bcf9d7fb0700 | -7.25822 | -57.54366 | 2025-09-02 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 476519e5-6127-3092-8f2e-ca87662e0150 | -7.46823 | -44.80819 | 2025-09-02 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| df51004d-aad4-3aa8-a6fe-1943b71bf28c | -6.81772 | -52.83604 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64654178-d629-3cf5-bab0-0953bab635a4 | -2.19845 | -47.99123 | 2025-09-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e60c3e95-2208-33f4-a3b9-79a1ce4962dc | -8.70949 | -50.44609 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e393c11-8d3a-316d-b60b-08df77695a1f | -4.91093 | -43.19418 | 2025-09-02 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1faebf44-2fbd-349d-b770-6a8baba3bbf4 | -6.86268 | -52.81549 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8ed96ac-13b5-3272-976f-ac5ccb232b40 | -7.73042 | -50.25126 | 2025-09-02 05:04:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| afd561f7-e8c9-36d6-bf15-ae29b6dc56d2 | -6.79069 | -52.81915 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b9deff7e-d4f6-3b12-9a58-a17160b7dd13 | -7.98247 | -46.45747 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5eb98f5e-ef3b-37d5-b654-bb705f47a4c6 | -7.98061 | -46.47178 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 367a4b10-aaba-39fa-9f72-c1d700f67a08 | -9.12337 | -46.05375 | 2025-09-02 05:04:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| af3f3fdf-391f-377a-80dd-43e3e3c1cbbb | -3.21642 | -46.83359 | 2025-09-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f67ffa9c-adaf-39bd-9701-e7bb924a092c | -6.87633 | -45.85026 | 2025-09-02 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README57.md)
