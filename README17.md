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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6fe4d674-95ce-3220-80f2-e1f1b6314218 | -5.96526 | -39.77061 | 2025-10-25 03:57:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a8dcead1-8c33-3d6b-9145-5abcb6e7f5aa | -6.13602 | -42.45804 | 2025-10-25 03:57:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ed96f1f2-b8ef-3d90-88a3-e6994c056385 | -7.14257 | -40.28969 | 2025-10-25 03:57:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0a03cb4f-075e-32bd-8f15-d94e87a0b35a | -6.9153 | -45.16335 | 2025-10-25 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a23499bc-9875-3c69-8b08-172d4b146875 | -7.54555 | -42.51741 | 2025-10-25 03:57:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fd6a0d83-a1cb-3d02-aa4a-d4f9782bb2ca | -7.77375 | -42.9145 | 2025-10-25 03:57:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b12308e4-adad-3cff-a53f-e9be964804ad | -1.49205 | -47.81319 | 2025-10-25 03:57:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d000262b-d520-3e0d-8f76-22f3ae29ca86 | -9.6259 | -40.34196 | 2025-10-25 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2ccc232b-cd9b-3c9a-8679-e2f9cfca5675 | -6.83407 | -41.54768 | 2025-10-25 03:57:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ab6e8c35-6836-3adb-9eb6-ad429335ac4d | -6.13303 | -41.72426 | 2025-10-25 03:57:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9b193013-a143-3484-a36d-96678748d825 | -7.44314 | -46.60918 | 2025-10-25 03:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 80d37f27-0ccf-3fce-bbba-d1a10b030227 | -4.60863 | -47.02101 | 2025-10-25 03:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 114513bc-256d-359e-b76f-27f1d906444a | -7.64527 | -42.17298 | 2025-10-25 03:57:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| cf55ae24-53e5-3267-b87a-92d5e26a8505 | -5.58753 | -41.31727 | 2025-10-25 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 02d2b07a-4ba0-3de1-8c6c-f77fa954dcde | -3.1651 | -48.60953 | 2025-10-25 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 71a071a9-1bea-3233-8ce0-a8c69d02442f | -6.22855 | -41.8394 | 2025-10-25 03:57:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2ffed154-8700-3b45-a7be-f28d84abfe28 | -5.45877 | -46.47446 | 2025-10-25 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d89c9f37-4563-3624-b0e6-f100283111b9 | -5.59049 | -41.32187 | 2025-10-25 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a399fb8b-eb52-3351-b4d4-6c7d627582af | -4.83874 | -50.93744 | 2025-10-25 03:57:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ce2bffc6-8d76-35e9-a690-720bdb1577e0 | -6.91369 | -42.2457 | 2025-10-25 03:57:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7c31de6f-1fff-3bc8-b26f-859220ed45d8 | -5.57119 | -46.35149 | 2025-10-25 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07cd1330-d419-38e0-9f86-cecb1ab1fe6c | -3.2396 | -48.75755 | 2025-10-25 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa02b64e-101b-3b02-a04c-1f64acca8df6 | -5.56855 | -40.90468 | 2025-10-25 03:57:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 62ee121c-bd4b-397f-b647-1fc7df66fa95 | -9.61842 | -40.33731 | 2025-10-25 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1d98809f-8306-3745-b02c-b3e353e93401 | -4.82524 | -50.93481 | 2025-10-25 03:57:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0020b1b9-84ac-31a8-9c5b-21c2f9af2943 | -4.25153 | -38.69849 | 2025-10-25 03:57:00 | NPP-375D | ACARAPE | CEARÁ | Brasil | 2300150 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e5cbffb7-4978-366b-b503-fa7cd51cc49f | -6.0673 | -42.15571 | 2025-10-25 03:57:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3ef7d1c9-c25a-3f90-b524-0c8b384d213a | -7.23304 | -44.34188 | 2025-10-25 03:57:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee11a160-ae61-3dcf-8dcb-a17cb98ae134 | -4.77718 | -46.50848 | 2025-10-25 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3e4d4b83-fc1e-320d-92a4-7f611eae7796 | -5.58687 | -41.32131 | 2025-10-25 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 97cbc2c6-c433-33ce-92f1-742c51f3b1e7 | -8.59819 | -44.82519 | 2025-10-25 03:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c25b8d8-bb2b-3dda-bd70-d2b372143d84 | -5.12866 | -41.19768 | 2025-10-25 03:57:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 377b17e0-2191-3d5b-ba36-64a87857dfff | -5.28809 | -38.29229 | 2025-10-25 03:57:00 | NPP-375D | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bb402912-10db-3b51-a2dd-c9710ea4e5e5 | -7.98415 | -47.38521 | 2025-10-25 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b886c014-a1f2-3ac7-97b7-8f032d9c5cf4 | -8.14203 | -46.86634 | 2025-10-25 03:57:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2cd6446-4fca-3a9f-8b22-cdd97ef6557c | -6.13939 | -44.73214 | 2025-10-25 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb294b8d-ae84-327e-b7da-6451cc63450c | -8.08352 | -40.88885 | 2025-10-25 03:57:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9545b679-80fd-3ea5-ae8c-5e413fb3d6a9 | -9.61975 | -40.33726 | 2025-10-25 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| fbdecdde-f857-39b8-9712-10d62b2c130c | -3.60355 | -45.97346 | 2025-10-25 03:57:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c26940e4-ca56-36f9-9e87-efd35af735d7 | -7.48702 | -47.03389 | 2025-10-25 03:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef46432e-47f8-3fbd-b8be-5f0447538886 | -8.42898 | -42.46181 | 2025-10-25 03:57:00 | NPP-375D | JOÃO COSTA | PIAUÍ | Brasil | 2205359 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 67242460-ff9c-306b-ba13-6a47f0feb8cf | -7.14834 | -44.12883 | 2025-10-25 03:57:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7346ddc8-c0c3-3b5f-ab0a-2c969c93c974 | -2.7992 | -49.13824 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b732ffb-e882-3b06-a9b8-34ec27bb528a | -3.23389 | -48.75834 | 2025-10-25 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f38d92c5-4604-336e-ac06-4b2114a34f09 | -3.10357 | -50.20713 | 2025-10-25 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 441028a0-bf6c-3c70-aa5e-03f9de2d219f | -4.97337 | -48.36032 | 2025-10-25 03:57:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4016316-b949-3aa5-a54d-8961920da785 | -6.12504 | -41.7271 | 2025-10-25 03:57:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d7315955-1489-354d-a292-417981a2d6d0 | -5.45723 | -46.41393 | 2025-10-25 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10594657-a610-3f69-b912-1ff4f09b3238 | -2.89383 | -49.16789 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a374e6c-6720-3025-a79f-b762e014986e | -6.13449 | -42.45569 | 2025-10-25 03:57:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0594c2d3-5e7c-3914-b145-2ff67521f2d3 | -7.17058 | -45.84608 | 2025-10-25 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 196d90a1-15b7-30d7-8d36-ea35241ee120 | -5.83023 | -40.82776 | 2025-10-25 03:57:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2b7f3bfb-b054-33e3-b32e-e3ae66608063 | -3.02283 | -45.39732 | 2025-10-25 03:57:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb8de0bd-d066-3a73-a5dc-c64e29b55a4c | -4.60383 | -49.58641 | 2025-10-25 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d87c6fa1-e61b-39c9-825e-8207a6161301 | -6.91976 | -45.16439 | 2025-10-25 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c190ee1b-621e-3ddf-b9dd-6f5ba3245dd1 | -5.6551 | -45.97274 | 2025-10-25 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6afe63f7-86f1-3c2a-83a3-7a26c9edb59a | -6.25659 | -42.8619 | 2025-10-25 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef318c15-5bd9-306d-8d5a-2ce4f7836767 | -6.73386 | -44.15131 | 2025-10-25 03:57:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42c7c8a0-a772-30c8-afc1-88511ce62599 | -8.09558 | -42.98807 | 2025-10-25 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 51faa13c-3426-3b6f-8bba-cabff46ddc2d | -6.33508 | -41.71965 | 2025-10-25 03:57:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8ea02f4c-8020-3f49-b1d5-7b3403297279 | -3.56293 | -39.09079 | 2025-10-25 03:57:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8f8095db-15a0-3b9e-bdd3-af90e238b477 | -5.03495 | -41.20127 | 2025-10-25 03:57:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3afdb24a-8d3c-36e8-b5db-c65f650e67c4 | -5.37639 | -40.71065 | 2025-10-25 03:57:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 182bfa7a-e7c6-3224-82a5-89ef28fb1487 | -7.7768 | -42.91993 | 2025-10-25 03:57:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2cc92376-3ecd-3492-a59c-327cf559fa79 | -7.42061 | -46.65067 | 2025-10-25 03:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9af0d381-add6-3182-96f4-355da81282a8 | -5.02233 | -47.15539 | 2025-10-25 03:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b8e5e52-a9ff-3369-ae7f-734919f53315 | -5.67124 | -46.65837 | 2025-10-25 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d92b6a38-9ac5-354a-8500-3bf9e138dbf6 | -3.70172 | -40.42339 | 2025-10-25 03:57:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 12.2 |
| ef4588bc-7cef-3ad8-bba2-0e76d3431887 | -4.87397 | -47.53541 | 2025-10-25 03:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9def104-2d78-39f3-8eac-fd08e8abdaa2 | -1.48824 | -47.81009 | 2025-10-25 03:57:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9015817-f9ba-3dbe-9bd6-a9951369042e | -7.00488 | -43.46645 | 2025-10-25 03:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 421908b4-b994-3733-8f4d-71c4c28fa050 | -6.7862 | -45.42221 | 2025-10-25 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85111b77-b925-3e97-8c6b-9ff0dc24ab9f | -6.54509 | -41.68976 | 2025-10-25 03:57:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5317d02b-6ead-3e29-b395-65c269b388a8 | -5.45238 | -45.40549 | 2025-10-25 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 078527ea-fa60-36ae-9fb0-eb317ea42d06 | -6.23211 | -41.82854 | 2025-10-25 03:57:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6551ab76-ddf0-3695-ba3f-1c18c0d87639 | -4.00214 | -43.74917 | 2025-10-25 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8793dea-5a6c-381a-8727-fc4b7418e7df | -5.02063 | -47.15357 | 2025-10-25 03:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9c5c43f-ca91-32dd-966a-c52fc2eaebc2 | -5.54261 | -41.38334 | 2025-10-25 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a6395acc-70dd-36ce-8ba9-71928e581f25 | -6.80843 | -45.43045 | 2025-10-25 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63abb116-fda7-381c-ac54-9c6aed324714 | -5.37991 | -40.71121 | 2025-10-25 03:57:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a6a14fa8-4330-3387-9ec1-0a9e14ef0d6c | -4.87456 | -47.53201 | 2025-10-25 03:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5f8458b-2b97-36d1-a8de-518cf770e365 | -3.09694 | -50.20585 | 2025-10-25 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 916938d3-d064-3a11-a391-91481c56f9ef | -7.64231 | -42.16796 | 2025-10-25 03:57:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ad086d7a-e988-3f2f-8908-05e269817ff3 | -7.15385 | -44.12156 | 2025-10-25 03:57:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4669f8d9-c6a6-3b25-af5f-4db392b6665e | -2.90011 | -49.16889 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5c9632a-e083-3fce-8759-d72b4d09ed8c | -6.82065 | -45.44213 | 2025-10-25 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5b7381b4-7897-375a-b77e-f3172f6c166a | -7.94344 | -47.199 | 2025-10-25 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1b8f454-395c-37cb-a15b-373a8265f51a | -5.40076 | -44.41837 | 2025-10-25 03:57:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f4cc46c-e169-32a7-a142-7bfd42e407f2 | -3.92271 | -47.69256 | 2025-10-25 03:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d54a4792-87ce-399a-bd75-28cb350f9cd8 | -4.60111 | -49.58546 | 2025-10-25 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 775cbb70-0233-31e4-90d6-385e45483b66 | -6.01951 | -38.43597 | 2025-10-25 03:57:00 | NPP-375D | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e1509174-1fe2-39a5-8564-7ca659c92f34 | -6.54977 | -43.23386 | 2025-10-25 03:57:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ecac1ad6-3bb0-32d4-9abb-dd7fc757a4d7 | -5.45827 | -46.47741 | 2025-10-25 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea9ddd19-777b-371a-a00f-6920e60401ec | -4.22437 | -48.61086 | 2025-10-25 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ead78242-4730-3a8d-be34-5aad966f2249 | -6.93872 | -43.63683 | 2025-10-25 03:57:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8787403-7699-384d-b107-06dcf642c3cd | -6.12434 | -41.73142 | 2025-10-25 03:57:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8c2a42fa-fbb5-39da-a4e7-343104dc8810 | -6.02679 | -39.62473 | 2025-10-25 03:57:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 18a47fd8-80cf-31e3-9775-8c474c574931 | -5.47141 | -40.88229 | 2025-10-25 03:57:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 799e5e8d-bdb8-331b-bf74-ea8d5c8a46ee | -6.28633 | -40.86544 | 2025-10-25 03:57:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 621cfe66-99bb-3390-90b8-b2e714d273c9 | -6.41899 | -46.19058 | 2025-10-25 03:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README18.md)
