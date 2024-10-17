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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc501e56-ac74-3d31-8e92-dbd7f85fc7c4 | -3.05457 | -53.24298 | 2024-10-17 01:41:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 83eff7f7-ce60-3d05-ba91-eec9aaae2c48 | -2.9507 | -54.14855 | 2024-10-17 01:41:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| ea5d319c-b569-3375-ad26-933a91363570 | -2.8865 | -51.7044 | 2024-10-17 01:41:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 44362b2c-6c5d-398d-be8c-f8fcad5e8ce2 | -2.88505 | -51.67988 | 2024-10-17 01:41:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 80c752ad-e305-3153-9062-70d5e47fe45b | -2.88202 | -51.67494 | 2024-10-17 01:41:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| cffda02c-2f70-37e2-91bc-c8060ae9b9ca | -2.78016 | -52.11091 | 2024-10-17 01:41:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| ee323c3f-3721-304d-8359-365508cadfc9 | -1.71016 | -52.69602 | 2024-10-17 01:41:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| e6f6ba3d-1a1d-3599-8c20-74db1680beee | -1.70792 | -52.70207 | 2024-10-17 01:41:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 7d7564dc-fb6f-3cab-8c33-94436a5dd6d7 | -2.5962 | -48.2634 | 2024-10-17 01:45:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 91dbe913-fb03-377c-8b8e-eb608f4591e0 | -2.6147 | -48.2629 | 2024-10-17 01:45:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 3081fcef-9d8c-38e6-b026-a30c0880c32f | -2.8333 | -49.1562 | 2024-10-17 01:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 31a808a5-3b30-33a9-9208-3e1766a108e2 | -2.9673 | -48.0147 | 2024-10-17 01:45:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 04ae6d6f-ac57-324e-92b1-7b807407ef45 | -2.9674 | -47.9931 | 2024-10-17 01:45:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 182.3 |
| f559816d-1e1f-34de-996e-f748b84ec0d5 | -3.2225 | -48.9306 | 2024-10-17 01:45:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| a927d2ea-485f-317e-9e35-806413547821 | -3.2503 | -46.8709 | 2024-10-17 01:45:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| eb33b926-d76e-3058-9780-484b2914474c | -3.5086 | -51.1122 | 2024-10-17 01:45:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| c2af6c68-d7ce-335a-b4c4-bc5be0515598 | -3.5087 | -51.0914 | 2024-10-17 01:45:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| e98c4103-b9a5-3cab-bcf5-166a4e3ba362 | -3.7007 | -45.9223 | 2024-10-17 01:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 55bb197e-ecf1-3dc8-a545-05478a8acb43 | -3.7009 | -45.9 | 2024-10-17 01:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 987e732b-065d-373a-81ea-cbb5b85fe76a | -4.5515 | -46.6801 | 2024-10-17 01:45:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 0644e4df-dd09-3915-ac9f-aca5d96597d4 | -5.5716 | -44.8927 | 2024-10-17 01:45:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 9cc105ef-5e44-3986-a2df-8fdb4cb07c6e | -5.5718 | -44.87 | 2024-10-17 01:45:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| f8a44b5e-89ef-3679-ac6d-599602e0774d | -5.9788 | -45.3621 | 2024-10-17 01:45:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 2d0b3677-3a0a-3907-9d38-7b8686505719 | -6.7274 | -43.5589 | 2024-10-17 01:45:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 230b7783-f814-37a2-bd18-161c4ca4dc18 | -7.8727 | -45.3593 | 2024-10-17 01:45:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| b0d0e201-2e10-362b-ba05-81358e083708 | -10.129 | -56.7722 | 2024-10-17 01:46:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 064fece2-7680-3555-b917-8973312364a8 | -11.7104 | -65.2235 | 2024-10-17 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 330782b1-a83e-3e4e-8a4e-bc11c54d7315 | -11.7308 | -64.9769 | 2024-10-17 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| bd83ac3c-2e02-3779-98b3-406058fb435d | -11.7309 | -64.9579 | 2024-10-17 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| d3083f75-991f-3dee-b9ce-6cbf8cf745cf | -12.3613 | -53.1396 | 2024-10-17 01:46:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 475e93c4-6cf2-307e-b499-a1454a5f3827 | -12.3804 | -53.1376 | 2024-10-17 01:46:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 572f5f83-0ba1-35d6-9dd7-3e5d2f23fdc8 | -17.1667 | -56.8232 | 2024-10-17 01:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| 46a74d44-f664-3f41-95b2-97e3c210ef3d | -17.2177 | -57.3102 | 2024-10-17 01:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.4 |
| 3b1db8e8-39a6-3263-b831-c0cc02687325 | -17.9036 | -57.4534 | 2024-10-17 01:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.5 |
| 1c629cec-3ee2-37b6-b21a-8ecf4714ae8c | -17.8049 | -57.4655 | 2024-10-17 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.4 |
| 9b12a231-efdc-3603-a74e-b281831271a3 | -17.8052 | -57.4449 | 2024-10-17 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.2 |
| e00b8935-dd6f-3533-ba49-6ed443e83ac2 | -17.8246 | -57.4631 | 2024-10-17 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.3 |
| 419dfbc3-283b-34b6-9ad1-863deb2e3812 | -17.8249 | -57.4425 | 2024-10-17 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.9 |
| ee03dadf-e0e1-3505-ae1a-9f18488055d4 | -17.8444 | -57.4607 | 2024-10-17 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.7 |
| 25ee7ac4-53ef-324d-b822-941a5e31dc79 | -17.8641 | -57.4583 | 2024-10-17 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.8 |
| fa14e0e2-cf85-324a-923b-cc67e5edd38d | -17.9234 | -57.451 | 2024-10-17 01:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.5 |
| 90915393-8322-3f82-bd2f-a318c13631f5 | -2.6148 | -48.2413 | 2024-10-17 01:55:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| f0faa0b9-3dde-33d5-b600-27d9a41849b7 | -2.6147 | -48.2629 | 2024-10-17 01:55:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| ff2818b0-cc24-304f-a327-90c0746b86ce | -2.8979 | -51.6896 | 2024-10-17 01:55:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| d363dfdd-d350-3422-9eed-0d38f87c58ac | -2.9674 | -47.9931 | 2024-10-17 01:55:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| eabed35c-6c38-319b-92ae-f9135f3a2e22 | -3.2503 | -46.8709 | 2024-10-17 01:55:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| aa148228-c5f0-3f34-a4bc-c068fc42f16a | -3.5086 | -51.1122 | 2024-10-17 01:55:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 3516b2c8-1af9-3cce-913a-a9b61d6b4ee6 | -3.7009 | -45.9 | 2024-10-17 01:55:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| b68c52f0-deb2-3fb8-bde6-78c282b52db2 | -3.7007 | -45.9223 | 2024-10-17 01:55:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 57.6 |
| dc714744-16ed-33b9-81e6-bf3ddecc585a | -5.5718 | -44.87 | 2024-10-17 01:55:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| bdf410b9-7ba5-3547-8bbc-85b3ea899a78 | -5.5716 | -44.8927 | 2024-10-17 01:55:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 90242364-e5ce-3f48-b37f-8a970e318dce | -5.6714 | -48.6872 | 2024-10-17 01:55:38 | GOES-16 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 2ac05624-5eef-3356-83fc-b2727d3e0039 | -5.9788 | -45.3621 | 2024-10-17 01:55:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| dc648653-a2d2-3ef9-a30f-17c1e2f1b1c2 | -6.7274 | -43.5589 | 2024-10-17 01:55:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| b4803196-e53c-3ec0-ba2f-feb777b7e458 | -7.8727 | -45.3593 | 2024-10-17 01:55:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| ccbb69c0-9056-3ec5-b9e4-133982eaf112 | -10.1477 | -56.7709 | 2024-10-17 01:56:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| e169b671-82e3-3341-bd6c-010d9cefb5ec | -10.129 | -56.7722 | 2024-10-17 01:56:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 4faa612a-564d-3d31-9d86-abb135f62bb5 | -11.7104 | -65.2235 | 2024-10-17 01:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 5661f497-52e8-3f1a-a763-1491cba04e26 | -12.3804 | -53.1376 | 2024-10-17 01:56:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 66b7486f-0a39-3660-9c84-8af7df6332e4 | -17.1667 | -56.8232 | 2024-10-17 01:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.4 |
| 3a08c9dc-ff7b-3dd2-8374-9fd6723760e8 | -17.2177 | -57.3102 | 2024-10-17 01:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.8 |
| 4f823951-ab19-3ef3-b7be-44b859d2eae4 | -17.8444 | -57.4607 | 2024-10-17 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.8 |
| c2b3dae5-8173-3484-998a-55913c5b8a60 | -17.8246 | -57.4631 | 2024-10-17 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.2 |
| 0dbe0865-932d-3da3-be4f-9ced1301a04e | -17.8052 | -57.4449 | 2024-10-17 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.0 |
| 539de40e-2a01-3a46-8999-feb4b9d892b2 | -17.8049 | -57.4655 | 2024-10-17 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.7 |
| f472e22f-3df2-3d36-9f75-63a13ed90ff3 | -17.9036 | -57.4534 | 2024-10-17 01:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.4 |
| 88072637-fc71-3d68-89a2-b06d22765e47 | -17.9237 | -57.4304 | 2024-10-17 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.3 |
| c5990c8d-9a38-3db9-a455-44d7458023b3 | -17.9234 | -57.451 | 2024-10-17 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.6 |
| 138f37a6-dca4-30a6-b6df-3fa626625ee2 | -17.1637 | -56.816299 | 2024-10-17 01:58:15 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cb5365a8-828a-3c5d-9ecc-bd26b417af7a | -11.7365 | -64.957001 | 2024-10-17 02:00:16 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4abece8f-7fa5-32ca-ad20-9a1db97748a9 | -11.7388 | -64.9664 | 2024-10-17 02:00:16 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b6838ec2-9f4e-3bce-a128-5692fa6aa7ff | -11.6636 | -64.824501 | 2024-10-17 02:00:17 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b1d06405-5d67-3e57-bbfa-8429ec573e32 | -11.7134 | -65.207199 | 2024-10-17 02:00:17 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 92e7da73-b767-36db-96f3-1a46a722d976 | -11.7156 | -65.216301 | 2024-10-17 02:00:17 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 99a675bf-3f4a-38e0-bfa2-c6eddf123e48 | -11.6982 | -65.230202 | 2024-10-17 02:00:18 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ff181979-08c9-3c52-a851-4e44044c22a8 | -11.7003 | -65.239304 | 2024-10-17 02:00:18 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 73bd8797-aff8-3dd3-bb81-d0a92a00a0e9 | -10.8521 | -68.257103 | 2024-10-17 02:00:43 | METOP-B | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 64651648-3a24-3818-8170-a2ed7678aaf3 | -10.8537 | -68.264198 | 2024-10-17 02:00:43 | METOP-B | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 75440635-b708-32a5-8a96-c4a3cac3e75a | -10.6247 | -67.711304 | 2024-10-17 02:00:44 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 16f87eb2-ef47-378a-a4be-091a7df872bd | -10.6263 | -67.718597 | 2024-10-17 02:00:44 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| fa800002-3561-3936-be08-704ff8c308cb | -10.6284 | -67.817902 | 2024-10-17 02:00:45 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 5ccc4b9b-6ee9-3df5-96ed-0f90cdf2099d | -10.6301 | -67.825203 | 2024-10-17 02:00:45 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 4d16f0f0-f180-3249-bc61-1a9c577ce5a8 | -10.6317 | -67.832497 | 2024-10-17 02:00:45 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 1d23976a-7aee-374e-8988-9e5c20721351 | -10.6186 | -67.820198 | 2024-10-17 02:00:45 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 55350a2a-30f2-3e80-b234-0058d4b85a96 | -10.6203 | -67.827499 | 2024-10-17 02:00:45 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| d86fd86c-27ef-36ec-b4c3-3ac8983250e0 | -10.5754 | -67.676498 | 2024-10-17 02:00:45 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 2c06fd11-91e4-356d-8500-5bdaf496a7ab | -10.5771 | -67.6838 | 2024-10-17 02:00:45 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e8df97a5-39d3-3aef-a060-e0a2dbb7e01e | -10.584 | -67.759201 | 2024-10-17 02:00:45 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 015b64be-be43-307a-8786-4b67f09c8181 | -10.5857 | -67.766502 | 2024-10-17 02:00:45 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 3702385f-643c-3262-8e4c-e2b8773a73f7 | -10.8899 | -69.387398 | 2024-10-17 02:00:46 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| ded1dbbd-3a4f-3dbd-a9d5-8f8149395abd | -10.8605 | -69.394096 | 2024-10-17 02:00:47 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 9640e00d-7f71-3e12-9200-39dd4d0b5c21 | -10.3868 | -67.889397 | 2024-10-17 02:00:49 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 22dbcb40-ab75-3e4b-93d9-5096b5b6a81c | -10.3885 | -67.896599 | 2024-10-17 02:00:49 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 83a29938-2f12-3b52-9c8b-05c6f158649a | -10.5408 | -68.566498 | 2024-10-17 02:00:49 | METOP-B | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| b05480f1-f7f1-3ffd-9e51-77aede3fb740 | -10.3675 | -67.939697 | 2024-10-17 02:00:49 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 505c8519-defc-32a4-8ba3-f99aef22d22f | -10.3691 | -67.946899 | 2024-10-17 02:00:49 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| a65225a9-dd83-3fe8-91e4-7ae36e904c0c | -10.6866 | -69.353401 | 2024-10-17 02:00:49 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| df40982d-e965-3989-8132-00600bd3b28c | -10.6881 | -69.360298 | 2024-10-17 02:00:49 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 413e918d-be7a-34e7-95b6-d4a9783d6c98 | -10.356 | -67.9347 | 2024-10-17 02:00:49 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 706f6e26-bd8e-3d6e-b7d4-6053077cfffc | -10.3577 | -67.942001 | 2024-10-17 02:00:49 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
