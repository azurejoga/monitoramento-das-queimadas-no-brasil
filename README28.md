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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39b088b3-ff2d-306b-ade3-058ea4372a39 | -7.35258 | -43.85239 | 2025-10-12 04:42:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 894042df-9314-3544-a011-f4f96955c11c | -2.79175 | -49.62453 | 2025-10-12 04:42:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 291fb86e-7f4d-3c59-9f24-b494ac416f27 | -5.90891 | -45.42719 | 2025-10-12 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea5b5eb6-d1eb-3304-a214-0b47cab73eb6 | -3.52989 | -48.92089 | 2025-10-12 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c91e63a6-47cf-3711-81f8-09472282502f | -4.27787 | -46.93704 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 28753bb1-45ca-353d-8e75-43a9c6e07ade | -3.88015 | -42.50936 | 2025-10-12 04:42:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| efda00b3-1a4d-35ad-9c08-12ad1506b2ce | -2.43664 | -49.37141 | 2025-10-12 04:42:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dddc51d1-62aa-3954-8513-df8c920fa469 | -2.79231 | -49.62101 | 2025-10-12 04:42:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bf1ffd00-d1c8-3dee-aa9a-507abd5bab42 | -3.53876 | -48.92587 | 2025-10-12 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 256db6ab-0b66-3a61-b9ea-d97091e64422 | -8.83564 | -46.04023 | 2025-10-12 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fac391eb-56b5-3eef-881c-48f485086d24 | -7.48774 | -42.76138 | 2025-10-12 04:42:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 54e23f18-aab2-3c6f-8a60-db8a4c66e47b | -7.88306 | -44.45709 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2042d4e8-a42c-3d4a-af3d-fcc785a99998 | -3.43788 | -49.84101 | 2025-10-12 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb4ae7ab-684d-3ad6-b004-8cd344eca29a | -5.58102 | -42.98636 | 2025-10-12 04:42:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ee6fa6f3-3c6e-3215-8194-4aedf2f404da | -6.51088 | -44.44189 | 2025-10-12 04:42:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a006bffc-5845-3165-9f54-ecf1a116e497 | -3.41361 | -52.18107 | 2025-10-12 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 593392a2-fd0d-3d61-83f2-fa9e7adbdb06 | -7.49217 | -42.77033 | 2025-10-12 04:42:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8037412d-a197-3f3e-a4fe-512f366e4fbc | -7.43067 | -42.9674 | 2025-10-12 04:42:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f71ffab8-3795-3b46-9e88-92febaa5a1e4 | -7.33376 | -44.0444 | 2025-10-12 04:42:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22db817e-5138-3733-8fb9-46044ae4cbc4 | -3.53212 | -48.92483 | 2025-10-12 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4fe2d5a2-1ec6-3388-bdda-a2c6f44de533 | -8.19116 | -43.3237 | 2025-10-12 04:42:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fe0e9072-6d72-32b3-a1db-367aa4ab25da | -8.70177 | -47.05244 | 2025-10-12 04:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9b36b49-bcd1-3a3f-b559-8ddb1bd36d43 | -6.77004 | -42.83014 | 2025-10-12 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 718b5986-4583-3391-a370-110aafa0ac9c | -7.74295 | -44.21631 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc88496a-24ad-3e63-b97d-97e7f540dc1b | -7.05435 | -45.25051 | 2025-10-12 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25f9f30f-bd9d-3262-aed1-9492d467c0cd | -7.21404 | -39.90243 | 2025-10-12 04:42:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 12ed82a0-bdcf-3072-a3ef-130a4d8535ed | -4.42139 | -43.46581 | 2025-10-12 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b351741-4c0e-34f0-b18a-e5ac9786f998 | -5.09447 | -45.0977 | 2025-10-12 04:42:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c21abb5f-b767-300b-b59e-e146ac1dd109 | -2.81772 | -48.61102 | 2025-10-12 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d1ff6c7-a8a8-3cce-9dee-99f70bce44a7 | -6.27926 | -43.90605 | 2025-10-12 04:42:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b0216959-8d5a-38b9-b91b-37a55507add8 | -6.76612 | -42.82506 | 2025-10-12 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2e5acc72-acfc-31f1-9bad-9574dbc4007f | -5.46784 | -43.39526 | 2025-10-12 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c436d6c7-c363-32ee-ad43-a4c6a705a9c9 | -3.82438 | -42.45626 | 2025-10-12 04:42:00 | NPP-375D | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9b943f2-939b-3f81-8300-98e60cd188c1 | -7.13707 | -42.5125 | 2025-10-12 04:42:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 37bc427a-8b20-3cf7-87c6-abe573473f03 | -7.85032 | -44.47838 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0b6e499-2ab7-38ba-9343-41f4c65987b0 | -3.51449 | -45.85649 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c361c145-97e4-3fdc-bfcc-9f9903c277ad | -2.43998 | -49.37194 | 2025-10-12 04:42:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e0b07a40-645b-3d9d-b6d7-aa735012b409 | -6.58864 | -44.61976 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 816b73e1-a93a-3f0a-ae46-99be159fbeb8 | -8.47614 | -46.22643 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bd2672d-bf71-39b7-a886-8c0649dccdcb | -6.50504 | -42.43783 | 2025-10-12 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c8b6f0f8-9357-3aed-b267-0b8c5eff3742 | -7.65428 | -42.57032 | 2025-10-12 04:42:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b2ebaa16-621c-3571-a0d9-e62bb5aecc4e | -7.85981 | -44.5285 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f77038cd-ccae-364a-9d79-9ed90e70844f | -4.98524 | -45.01445 | 2025-10-12 04:42:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22fd1b02-ffeb-3b7e-b97e-ef6e0295fe6b | -5.30621 | -42.87684 | 2025-10-12 04:42:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ffc0dd5f-6e59-343e-8153-fea1df48f85a | -8.09864 | -47.24109 | 2025-10-12 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e310279-000f-35a4-87f1-f15746eb9833 | -7.32246 | -47.81981 | 2025-10-12 04:42:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ee2540e-70d4-33c9-aea7-0fbf27632232 | -2.71854 | -48.35832 | 2025-10-12 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9173dc22-907d-3a09-af7c-573cfc70ca9c | -5.33485 | -43.43177 | 2025-10-12 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e89e3e2c-4bf2-34a3-9722-496ac6f1a288 | -4.27288 | -46.93301 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f075bb40-b2ee-3a93-946d-54dc4edf197b | -6.76673 | -42.82077 | 2025-10-12 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 055ea6a7-b02d-364a-a62a-3b21c210d562 | -8.83186 | -46.03959 | 2025-10-12 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0087f86d-3702-3ad0-8e10-a417e37a9ddc | -3.40522 | -46.90257 | 2025-10-12 04:42:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1124e463-15d6-305f-b9f6-e64d16bd07be | -8.48483 | -46.16871 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 012d9529-2955-3381-8c18-6fab5970f4a1 | -8.33284 | -46.23467 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da6fca2b-34b3-3dc3-9a81-02b8303f721e | -5.93876 | -43.93974 | 2025-10-12 04:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f03309d-1e01-37de-88da-659d26592207 | -4.27693 | -46.92977 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1b71a459-2b0e-3350-a47c-49aa01751d6f | -2.71799 | -48.36178 | 2025-10-12 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bce895b0-e9b3-30f7-8794-45a22809ebb8 | -6.42115 | -42.53629 | 2025-10-12 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 50b85df4-bd3d-3f62-80a2-f9e7b1257492 | -7.86638 | -44.87907 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42eca881-a895-3844-8321-8d85cac5b6a5 | -6.72717 | -42.0749 | 2025-10-12 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 56586eb7-cdbf-3b82-80dc-06252c40b3c4 | -7.85673 | -44.52086 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 57d61f78-b2f9-36f2-8770-a372f6df5d84 | -6.57095 | -44.7131 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fe84830-2c60-38ef-8afa-1cdcc5768945 | -7.48707 | -42.76621 | 2025-10-12 04:42:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6698a846-99fb-376a-8307-110f6b255a0b | -6.31421 | -44.25715 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 24acfbb0-1d66-3da9-b276-a405b74ed294 | -4.4256 | -43.46643 | 2025-10-12 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d03a933-9cb2-3c99-907b-2be852ac9548 | -7.50924 | -44.63422 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d680b1e4-e32d-339a-95d8-110c2019d63c | -6.88718 | -44.69949 | 2025-10-12 04:42:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2be751b8-38af-3d83-b95e-988fe64c1440 | -5.62882 | -42.69317 | 2025-10-12 04:42:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ab2c15a7-739f-36b9-9d34-b5f129e0ed59 | -3.19772 | -49.47947 | 2025-10-12 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d5311ec-8db3-37b6-a7ac-6a6c6b25d311 | -7.75246 | -44.2098 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ea40205-a5e0-36b7-8879-a03fa2bc4011 | -7.3429 | -43.85897 | 2025-10-12 04:42:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1ef1edc-8e8f-3deb-835d-2bc69cc5e99d | -7.05622 | -45.21078 | 2025-10-12 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0136ccbc-a5b8-3e8a-8a39-fb1cd330d82c | -3.19223 | -52.23658 | 2025-10-12 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a990fad9-1541-3c61-9a34-25be967f0234 | -3.19717 | -49.48296 | 2025-10-12 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8eaf945f-c1ea-34c4-b35b-3d6dcf679ee2 | -2.88809 | -50.72857 | 2025-10-12 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 985292cf-ee72-3cb0-8a49-38c476c986b1 | -7.4222 | -42.9616 | 2025-10-12 04:42:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1b406719-8195-3b07-9966-20d5f68c3889 | -8.0183 | -44.4522 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b241d2a1-2bcf-3951-bcf6-3c037bc985fe | -7.01636 | -42.73718 | 2025-10-12 04:42:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e266875b-c9f5-3ac2-a0c5-fbdfac97f755 | -5.47271 | -43.39191 | 2025-10-12 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d84a5cf-3b67-3d03-ab86-c92fb6f0df5e | -7.68018 | -42.38488 | 2025-10-12 04:42:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| aa41722d-c64f-3904-ae12-05faa139906b | -8.01881 | -44.44859 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b22aa465-4142-3069-8e87-be95c167c490 | -5.80579 | -51.50086 | 2025-10-12 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fd671ba-2de5-3dcb-b696-203f7f07155c | -5.46726 | -43.39926 | 2025-10-12 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b003fcd-f2fd-3181-a4a7-d9e57831442f | -6.96295 | -42.43262 | 2025-10-12 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 9335aec5-232a-3e6d-b3c0-5fd507a8cad5 | -7.5046 | -42.1451 | 2025-10-12 04:42:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 22ed847f-798f-3993-bf44-9888e515a2c9 | -7.46316 | -43.88884 | 2025-10-12 04:42:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a3385d3-294f-30ce-bf0c-19ec3bcc7b7d | -3.53489 | -48.9288 | 2025-10-12 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f95bb873-9d17-345f-b0a7-5b60453f9058 | -7.88463 | -44.52007 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c8a288a-f15e-3c65-b998-9ec07a15b905 | -8.83409 | -46.04189 | 2025-10-12 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 423dcbb4-5487-3107-90fe-8c4c53838cc8 | -6.98547 | -42.03635 | 2025-10-12 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2c1a2ead-3dd1-3508-99a1-c9945e1ec4d2 | -8.84614 | -46.03913 | 2025-10-12 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 285b1d5c-54fb-32c5-8be6-8a9868aab283 | -3.51872 | -45.85295 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f162869-5ddc-3d83-9f98-68b999e9c6e2 | -7.45825 | -43.8926 | 2025-10-12 04:42:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8cf2bf9a-e485-31b5-8303-2012246b0e9b | -8.82599 | -46.05283 | 2025-10-12 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3a09bc9-77f4-31e7-957c-f7d4a728943b | -3.50792 | -45.85131 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd611c71-8f25-3cb5-8898-580ee0b43d81 | -3.73512 | -44.38925 | 2025-10-12 04:42:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6625a2b0-d57c-3e38-97be-fcc313d24dcd | -8.83116 | -46.0442 | 2025-10-12 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 474881c9-af06-3faf-8bc9-6fbf9425f2c3 | -3.87947 | -42.51372 | 2025-10-12 04:42:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d88b211e-7b20-39e5-8a87-712666d46ef3 | -4.27406 | -46.92548 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 515affe0-438e-3f08-b6de-a258cde1418a | -4.19924 | -46.43872 | 2025-10-12 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README29.md)
