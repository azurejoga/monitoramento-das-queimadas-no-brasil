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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca0ce4c2-4893-3526-b284-f7e4c7531d6e | -10.06148 | -47.9002 | 2025-11-19 00:32:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 64852444-8447-3e5f-a831-07c70429a151 | -11.79252 | -44.64452 | 2025-11-19 00:32:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 8b7ebc74-7436-3ab5-b804-10d76e955893 | -14.39097 | -48.28264 | 2025-11-19 00:32:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 029d1151-b76f-37bc-a4c1-98392be3bb93 | -9.40327 | -48.4504 | 2025-11-19 00:32:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8a868e34-4ce8-3774-975b-17ecd5f06136 | -9.3916 | -48.43317 | 2025-11-19 00:32:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2027112e-41cf-36f1-8120-87ebb254a199 | -11.67644 | -47.97757 | 2025-11-19 00:32:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3b79d2aa-5c11-38ff-a793-d84fde98c2c1 | -15.48744 | -43.17331 | 2025-11-19 00:32:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 36.4 |
| 1e0357e8-b195-378d-a605-d547098edeb3 | -12.13968 | -45.1626 | 2025-11-19 00:32:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| e162f211-d281-3c7c-8bb4-fc3735d5dc45 | -13.49227 | -44.54995 | 2025-11-19 00:32:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 82abd20e-7478-3138-8c38-69f2edff238d | -8.88135 | -47.32807 | 2025-11-19 00:32:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 6403dc6a-9ebe-3e38-a7a8-fc88b1357e72 | -11.51672 | -44.88532 | 2025-11-19 00:32:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 004a948b-fa46-3c4f-b8cf-f65a108bf698 | -16.75511 | -50.69678 | 2025-11-19 00:32:00 | TERRA_M-M | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e52930fc-6473-3c97-9b45-c6e5566fc72b | -10.69861 | -44.79507 | 2025-11-19 00:32:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| d4829362-e3f5-3ccf-86a2-3157839e2896 | -12.63426 | -47.32843 | 2025-11-19 00:32:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c0feddbe-276f-3827-9de7-2dc8b0ad8fa4 | -10.88877 | -54.14405 | 2025-11-19 00:32:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 50686786-e4be-33b6-9bdf-82851c5573c2 | -13.50294 | -44.5483 | 2025-11-19 00:32:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 32924945-4c3a-305b-ad37-8177109490ea | -11.79029 | -44.63042 | 2025-11-19 00:32:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| a36c911e-11b8-326b-8ac2-7a7624e27511 | -7.83239 | -42.1568 | 2025-11-19 00:32:00 | TERRA_M-M | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| a98cb4fe-8474-3ba9-91b3-f798b9f0f7ea | -4.68024 | -43.24057 | 2025-11-19 00:34:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 01d9b852-dfd0-3dab-b7dc-afd061ed50e1 | -5.047 | -45.1378 | 2025-11-19 00:34:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 50b5b25c-e8c0-3074-ba65-7a79077d9855 | -2.70536 | -49.30605 | 2025-11-19 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| db470d94-5fbf-3f82-ba6d-1fabf1791ee0 | -5.2342 | -43.99364 | 2025-11-19 00:34:00 | TERRA_M-M | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 9f0dcc59-9318-3cc0-9cb1-45d9503aae0f | -4.68564 | -43.23317 | 2025-11-19 00:34:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 8876c35c-8a29-30c6-a542-041fdd915017 | -2.52415 | -51.17571 | 2025-11-19 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| b639710b-38d5-388a-af3f-1742c924d592 | -6.30606 | -43.79704 | 2025-11-19 00:34:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| ec38744f-4c70-3bbb-b313-a2175421897c | -3.92046 | -50.28881 | 2025-11-19 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fe128e09-b8e8-30b2-9e47-0da19ba5cac2 | -2.82067 | -49.13593 | 2025-11-19 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 4c9df5a5-02b5-3643-9172-29f2ddb39e4b | -3.55124 | -52.0798 | 2025-11-19 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b02188f2-c6de-3b40-9fb1-1696c7aa1694 | -3.3519 | -43.50437 | 2025-11-19 00:34:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 54d5e3d9-a164-381f-81ac-a769097c3185 | -2.47832 | -50.24779 | 2025-11-19 00:34:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b3bcda05-b386-35cd-91d3-e80e9dd1c4c9 | -3.49844 | -51.08879 | 2025-11-19 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 5f561e5a-c606-31cd-aeb2-a792cfa3eee0 | -2.22435 | -44.82178 | 2025-11-19 00:34:00 | TERRA_M-M | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 70.0 |
| dd18f8a4-ef5e-3a62-a654-deb3aaa37f7d | -2.94751 | -51.8472 | 2025-11-19 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0c84f804-69a6-30ad-8e64-ad998ae8a3d6 | -3.2515 | -43.03466 | 2025-11-19 00:34:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| d806662a-cadc-355a-af10-790f713be323 | -2.22155 | -44.80201 | 2025-11-19 00:34:00 | TERRA_M-M | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| c3a48e12-0319-3050-9ec5-f207246004eb | -5.00236 | -50.91497 | 2025-11-19 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2e355223-8791-3e67-875c-94519f0845b4 | -4.67175 | -43.23545 | 2025-11-19 00:34:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 10432528-22cb-3c99-af2e-06b27a78e139 | -4.96125 | -45.98098 | 2025-11-19 00:34:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 23.4 |
| a6421595-91fa-3bcc-8fa7-2173c0bc8dca | -6.25048 | -43.68734 | 2025-11-19 00:34:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 8de0ab27-16a6-3205-b243-df8632c31d74 | -3.15684 | -51.69003 | 2025-11-19 00:34:00 | TERRA_M-M | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1669f28b-f9f4-3b4e-8d0e-1b8f2cb5b709 | -4.91611 | -48.17929 | 2025-11-19 00:34:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 38ec15e5-8124-325b-9295-e6c5b0dd5195 | -2.89331 | -51.45605 | 2025-11-19 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6a9bf7cf-49ec-3db1-b2a0-bc73afbc0bb1 | -4.99569 | -44.75286 | 2025-11-19 00:34:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 7dfeb431-070e-3a8d-851e-c3f9bf46a633 | -2.85261 | -45.45617 | 2025-11-19 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 24.1 |
| abdaa65e-014b-3b0f-890c-ca7ab0de2ac2 | -4.8737 | -49.58674 | 2025-11-19 00:34:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7ca894e5-c94f-38dc-9bbb-06825e76c5f0 | -3.79593 | -51.64944 | 2025-11-19 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 59a0955e-339b-3d7f-96be-ae85eda45196 | -4.91466 | -48.16899 | 2025-11-19 00:34:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 8f562a84-06d0-3f03-af2b-4c78d8d59194 | -3.84383 | -51.32769 | 2025-11-19 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b1743f53-21e6-3348-a821-c0b84171b427 | -4.66283 | -43.21896 | 2025-11-19 00:34:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 1e20ce6e-4caf-33b5-80df-ee9c8772a30c | -3.14121 | -51.51094 | 2025-11-19 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ef91fce6-b9ed-3a39-a3ef-7258071fa021 | -5.06415 | -49.63057 | 2025-11-19 00:34:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 33c75081-1214-341f-9738-63d4ae6849ba | -4.66806 | -43.21154 | 2025-11-19 00:34:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 408.0 |
| 39898575-3279-306c-bd8a-29aaecc906c1 | -4.11466 | -49.10081 | 2025-11-19 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 97833df7-858d-3fe6-8b92-4bd4432d649b | -4.87499 | -49.59589 | 2025-11-19 00:34:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 788a971c-e926-3b0f-8db6-3013584e0e03 | -2.22382 | -44.81631 | 2025-11-19 00:34:00 | TERRA_M-M | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 7b48ec29-de8c-3439-a369-9aea5023b010 | -2.47706 | -50.23882 | 2025-11-19 00:34:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5056d588-92d0-3cf4-86ce-ce25b8f5ffd3 | -4.76275 | -50.98467 | 2025-11-19 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 878407c7-498e-3d66-8c8e-bd3edf579479 | -4.61055 | -48.44936 | 2025-11-19 00:34:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 7fc93fba-8409-35c6-9588-0d49746ec65f | -3.92933 | -50.28756 | 2025-11-19 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 2938e6a4-fdb3-36ed-807b-6786035c0e8d | -3.48622 | -51.5378 | 2025-11-19 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 264271b2-3951-3fce-907c-e4c120c624e3 | -5.04504 | -43.60411 | 2025-11-19 00:34:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 974c5b1d-f045-3a37-a954-4ba7bdc522c4 | -3.42424 | -52.36383 | 2025-11-19 00:34:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| da62a393-c372-3bdb-aa03-78bc5cd6eefa | -5.03162 | -43.60617 | 2025-11-19 00:34:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| bef814bc-b6ab-3d6b-b24c-8bb33e3f547f | -3.33893 | -52.6762 | 2025-11-19 00:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 50f4804e-9b35-3d8b-8f87-71fd092c8701 | -4.33561 | -48.97331 | 2025-11-19 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cac500f5-1de2-3a45-947a-20e14f1ede44 | -6.24718 | -43.6657 | 2025-11-19 00:34:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9aaa7665-84de-37c1-9fa7-11a52a9a0322 | -4.68199 | -43.2094 | 2025-11-19 00:34:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 42dcb17e-e8da-3770-9102-92a173e56bb3 | -5.23164 | -49.57587 | 2025-11-19 00:34:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 06a33a2d-27f4-36e8-a685-bfa50b26e2aa | -4.99249 | -44.75897 | 2025-11-19 00:34:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| ff75281c-550c-3e6e-8c8b-bf6a6ac50982 | -4.61201 | -48.45951 | 2025-11-19 00:34:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5d64e202-ae36-3e75-80d1-8cca51d01622 | -4.7514 | -50.69265 | 2025-11-19 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| da9941f3-330b-3124-8577-aae349c2ff2c | -2.52537 | -51.1845 | 2025-11-19 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8751af49-cd01-3605-8c82-6458f7f59345 | -3.41276 | -54.68352 | 2025-11-19 00:34:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 77cbe6b3-7094-372a-bae9-3917df4e7fac | -3.7845 | -42.8416 | 2025-11-19 00:34:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| f34ef342-9e2c-3e20-9dd1-a0a4ccf8a9a6 | -3.14243 | -51.51976 | 2025-11-19 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 06b12aa7-21a6-3a2d-8b9e-fe7600c919d5 | -3.17975 | -48.6184 | 2025-11-19 00:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dbe6918f-21fc-3783-9a08-a3cf7aeddf0d | -4.24186 | -46.96156 | 2025-11-19 00:34:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 60767646-5670-3b8c-9dc5-bac578ed96ea | -2.81931 | -49.12617 | 2025-11-19 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 2c98b69e-42fb-33a3-bc0c-32c0a7a7fa79 | -3.23854 | -48.51991 | 2025-11-19 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fa46fda9-2de0-32de-b847-430307d0bfb8 | -6.11062 | -42.96036 | 2025-11-19 00:34:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| 0984cd55-679e-3541-8913-b523077a9987 | -4.67676 | -43.21675 | 2025-11-19 00:34:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 392.8 |
| d11c18cd-0147-3e06-975a-47632ada0e95 | -3.75549 | -51.82607 | 2025-11-19 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ccb18b68-9b16-352b-b104-3519d9338db2 | -3.24996 | -43.04049 | 2025-11-19 00:34:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 5b7aea95-d247-3c08-8bf4-ca9bcf0dd18f | -3.84794 | -51.69709 | 2025-11-19 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5d50c532-7d4a-312e-aa65-1e257b14943f | -3.08939 | -51.26612 | 2025-11-19 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 54513879-d165-3c79-afd7-f4ae9782a6ef | -2.89482 | -53.95819 | 2025-11-19 00:34:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d373afa9-359f-33bf-9f01-1d073ad3eef3 | -2.78131 | -54.55789 | 2025-11-19 00:34:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ad082a11-34ec-331b-8279-1bd1405331dd | -6.30292 | -43.77707 | 2025-11-19 00:34:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| dc2429e3-aa01-37c5-b985-874acaf0fc4b | -5.05295 | -45.13109 | 2025-11-19 00:34:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 6a7536c4-c23e-3efa-94be-bd52378d3657 | -3.73239 | -45.60197 | 2025-11-19 00:34:00 | TERRA_M-M | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 7f184689-5874-3cd9-b89d-c724246ec794 | -3.7947 | -51.64051 | 2025-11-19 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d6fcc53b-0abb-31f5-96e1-86cbb0d7ba4b | -3.9281 | -50.27868 | 2025-11-19 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0258802c-e2aa-3733-bdc1-0ed9b3ff2fa9 | -4.14618 | -46.78669 | 2025-11-19 00:34:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3e967a91-9c76-3405-8a87-2e8929d48fc1 | -6.71156 | -42.12072 | 2025-11-19 00:34:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 91d1967f-a878-3c74-a9d0-eac04e3eafbf | -4.67542 | -43.25922 | 2025-11-19 00:34:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 88797661-3351-36ea-84d9-b36bc7e75b98 | -3.73934 | -51.70903 | 2025-11-19 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 78e08546-a3d4-3ca2-9d84-8b388ecce895 | -5.01121 | -50.91375 | 2025-11-19 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 78f9f889-01bd-35ff-813e-4295dedefd7a | -2.87884 | -52.61931 | 2025-11-19 00:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 49d116ae-93dc-3de7-952b-4b819321da38 | -3.49722 | -51.07998 | 2025-11-19 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 637c87c4-08b7-3026-beca-43b987c26d64 | -4.33696 | -48.98286 | 2025-11-19 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |


[Clique aqui para ver as próximas entradas](README3.md)
