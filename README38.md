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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcc2540f-1a26-3062-8bc8-e84af93a08e0 | -6.66434 | -44.20392 | 2025-08-27 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 001a6b7b-ac05-3eb4-ac6f-7954f4ea0a7e | -9.16423 | -59.54271 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9ffb518c-4a25-3321-9917-08cd69aea4a7 | -9.09024 | -49.5779 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 161e364b-c40a-3e26-bd07-30a2ad3faaa7 | -6.24168 | -60.01995 | 2025-08-27 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5c09e68d-b0a7-3b53-8914-b5fc4af61078 | -6.87952 | -44.40178 | 2025-08-27 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43338228-a594-343f-8309-afb18fc25281 | -9.01295 | -40.34362 | 2025-08-27 04:25:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dcaad79f-8b38-3d6e-834f-5ac57ff89da1 | -8.86275 | -47.17203 | 2025-08-27 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6485c9a9-0e11-3dda-90f5-32e731538e1c | -5.6264 | -45.72479 | 2025-08-27 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42b28208-869f-34e8-b193-25f728d02908 | -5.15377 | -47.84441 | 2025-08-27 04:25:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b41bc5a4-d8c2-31bb-b2a4-d0330e8b4ce8 | -6.12077 | -46.48973 | 2025-08-27 04:25:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 322538c1-5258-33c3-83cc-ab61af1396c8 | -7.34787 | -57.63079 | 2025-08-27 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 88247d19-a6e8-3a57-8084-dc9722881872 | -10.66786 | -47.16209 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88ae7427-4985-399a-a49a-4b3e8c415c7b | -4.96045 | -55.8264 | 2025-08-27 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c13112af-f896-39c3-8680-9fa0b7a11bad | -9.07465 | -49.56313 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb944ca7-b6ab-3b9b-b03f-570cb9fb1e7c | -5.75557 | -53.76696 | 2025-08-27 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05652cfd-d419-349d-9e15-9df810852251 | -9.26942 | -59.7835 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c4976ea3-05ea-3dcc-8a4f-70816c434cdb | -10.31747 | -46.79777 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72559a36-3526-3fe3-9604-551f155e19fe | -9.1723 | -49.62851 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9744fd19-a24f-31f8-ab69-33152fb4592f | -6.77055 | -59.67301 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a8a64809-6bd4-368d-89bd-7d5755ad261a | -9.49992 | -46.70663 | 2025-08-27 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 095a55b5-dafd-3bbe-91ec-16424ef3ac06 | -11.57617 | -44.65013 | 2025-08-27 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93155dd8-250c-31a8-9ff2-1494089574d0 | -8.27028 | -45.06178 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71a1e5b3-f7d6-3514-8120-06ebb3b82aff | -8.55959 | -51.35387 | 2025-08-27 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3dc95c41-3186-31d2-a346-f1b0d16af08e | -6.46719 | -55.89392 | 2025-08-27 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 664a88ff-dc8b-3e5b-8015-0ea1fc0c33c3 | -8.06883 | -44.9822 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec666cf8-8def-3b48-93da-079fe83d8f2f | -5.9499 | -42.49371 | 2025-08-27 04:25:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7b9a3f1f-be69-3d78-af46-109dddcab5fd | -8.88826 | -60.76627 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 89a12570-f7be-3d7c-9e12-af668b7a19bb | -6.08263 | -45.95635 | 2025-08-27 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af0d9ecc-5fd5-3ab6-8597-9f5ba2798fb8 | -9.58947 | -55.37733 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c273b0a0-e71e-345b-bddd-1ea154fcba6e | -7.70744 | -45.77202 | 2025-08-27 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a706c990-9e34-399b-8467-3babd5b994de | -8.29577 | -46.32968 | 2025-08-27 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb61b725-7e18-39b7-b908-19ae3a3613a9 | -5.47643 | -42.60508 | 2025-08-27 04:25:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| dc113bcb-76fe-315e-9878-390c33398d14 | -9.10079 | -49.57964 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8383e1ba-d25e-31d4-bde1-cb8c2058167b | -8.55593 | -51.35438 | 2025-08-27 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ed8811d-a1ee-3fbc-a88f-5565047073c4 | -11.24739 | -44.991 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3dd0eea6-b053-3dbb-bb83-ccef50a197d6 | -4.49491 | -46.37408 | 2025-08-27 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a3a258be-e2d2-352c-82be-1b16bf2434df | -6.68619 | -44.40763 | 2025-08-27 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 80590838-8730-3ea5-9a66-7b1116f2ab6a | -9.17199 | -59.46865 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 195bb067-862c-3696-8856-77cc35edd0fc | -6.35793 | -55.80117 | 2025-08-27 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8678d8c8-22d5-3a85-a6fb-aa629e180b36 | -9.58988 | -55.37643 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3f5f698c-da04-3119-bd13-ff4f340734bc | -5.11548 | -43.2097 | 2025-08-27 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b3869555-2d2a-33bb-9f09-4ce328abd691 | -8.27424 | -45.05864 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e65a6dc-108e-386d-bbe4-5b43a1f5db8a | -10.49002 | -51.60587 | 2025-08-27 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 335a37f4-6649-32a6-b163-424108b9fbce | -6.83124 | -58.96463 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c5a3a4fd-5641-3088-b892-a4ac0182b95e | -3.8481 | -55.8103 | 2025-08-27 04:25:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00752aef-4186-3eab-b1a4-6a9698872148 | -8.52202 | -47.41461 | 2025-08-27 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b9300d9-c007-3c96-9401-2d89da08369c | -6.89764 | -43.1385 | 2025-08-27 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2737e39a-7049-34b8-a2e1-08c9fd7b2bdc | -11.20748 | -41.59832 | 2025-08-27 04:25:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b68a9964-3217-3a6d-9b34-ba1edc5669bd | -9.42356 | -48.25357 | 2025-08-27 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6d085dd-b796-3f49-bfca-949e29dacd78 | -3.73166 | -48.94143 | 2025-08-27 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8a9cf915-c310-3086-ac07-665df8e6d9e7 | -3.67862 | -49.1807 | 2025-08-27 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4eb814dd-2af8-3624-ac5f-f35ebf137e26 | -6.12958 | -42.95571 | 2025-08-27 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b0ddd4b1-796a-3fd5-9d88-ced8ef0b3dce | -7.65818 | -40.15627 | 2025-08-27 04:25:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 369aefc8-9217-384a-9c0b-ea10740ee59f | -9.19311 | -60.80805 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 339139f3-2ca9-39cd-9d05-cc38a485ba67 | -9.57145 | -45.74714 | 2025-08-27 04:25:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eaa3846d-1581-392b-8a69-d614c2669ec4 | -11.61594 | -46.45821 | 2025-08-27 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6342c551-9f7e-3a90-b414-ec9ea959e6f3 | -10.78692 | -47.07353 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f3f466e-851f-341b-ab7a-e01c2c7b61a0 | -8.5557 | -51.3532 | 2025-08-27 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| edf29455-6dba-3b75-a614-136e9297e787 | -7.01461 | -43.10702 | 2025-08-27 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d0498c11-12b3-36bf-af1c-17c8c53bb542 | -7.16867 | -43.8531 | 2025-08-27 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 430e03f5-bb90-393f-a7d8-720a1e8315ad | -6.87323 | -44.3969 | 2025-08-27 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff8e6ca9-60ed-3b8d-8fbb-9fb56c35ca71 | -7.22552 | -44.40661 | 2025-08-27 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc79bee3-675e-309a-9b52-0a680b44be74 | -11.61729 | -46.20365 | 2025-08-27 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 652a5300-2bdd-37ee-9d12-1a352eb863e3 | -6.69313 | -58.5542 | 2025-08-27 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cfe258c6-5df8-3571-8882-02dba2dece53 | -9.57782 | -55.38613 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6079adba-c697-30ac-8f30-eb0e7a2896c7 | -6.96762 | -43.58412 | 2025-08-27 04:25:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03d56d70-3f7d-3081-b257-4f48aaf02dc0 | -9.94542 | -46.3746 | 2025-08-27 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 90e8bee7-8d4f-3af5-b164-59f95c625815 | -9.08871 | -49.56545 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4d3e0e44-c2b0-3808-8a61-e72e35a24d45 | -9.86526 | -44.6907 | 2025-08-27 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1a605a6-2c13-33cb-92e0-596be247f05b | -4.48387 | -47.66756 | 2025-08-27 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4651b5e7-df73-311b-8b14-ec590af62cc5 | -8.89529 | -60.76771 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81f928dc-34a0-311a-9512-5d9a31f30516 | -6.2432 | -60.02572 | 2025-08-27 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ffa723eb-44ee-3dfa-b77b-953748334f04 | -8.72612 | -49.73915 | 2025-08-27 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bb947d5a-f08b-31ff-91db-3db0c433ce42 | -9.16203 | -59.55393 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4c726e9-78f4-37a3-9555-4c2c071b91e1 | -5.6308 | -45.71838 | 2025-08-27 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b77b7c1f-bb23-37f5-8d48-3d6c53b79166 | -11.2446 | -45.47854 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a4859d35-c4f4-3134-a6f9-12c9d824b499 | -10.81485 | -46.36987 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 874174f5-446c-3377-bc62-65327e2e1383 | -9.06427 | -49.55834 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c9cdfae-b635-35ec-84b4-88ed06e5c50b | -7.04957 | -44.29981 | 2025-08-27 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a838602-8760-39f8-a3ae-9a81012193f3 | -9.2725 | -59.78139 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d731dee4-4369-3a61-96e1-376d4901b3ec | -11.15112 | -44.7874 | 2025-08-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9d8b4e5-fd58-3bc1-944d-b31bb6f1b362 | -6.45848 | -44.61247 | 2025-08-27 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1ee19a5-d375-3fe6-9cd9-1b205a9c9394 | -9.16862 | -59.5203 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89eca786-fce8-385e-bf58-2f266456721b | -9.55615 | -44.93727 | 2025-08-27 04:25:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99031fb0-9dc2-3a29-a2b6-3cc509f55623 | -9.18176 | -59.45328 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d301be7-f3f6-37ac-a6e2-1dd832f967bd | -5.25352 | -43.34866 | 2025-08-27 04:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dd196472-923f-337f-adf2-7e23d732f69e | -6.68277 | -44.40701 | 2025-08-27 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 812cc64e-84c7-3f02-a265-84f636529347 | -9.58553 | -55.37082 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f24ab17-ead9-3a23-9824-eed7708e1c46 | -7.63806 | -42.69046 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a7de3ddf-3ac2-3c1c-9483-f200fc7f1401 | -7.3852 | -47.04253 | 2025-08-27 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9512feb-6d19-3560-97f9-fc47aa0a6a21 | -10.3202 | -46.78031 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88b582d7-edad-361d-a633-e3b4408cfa13 | -6.91951 | -52.82102 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cfd9ffb-827a-3361-9ac1-97aa241cc0d0 | -5.66225 | -47.49363 | 2025-08-27 04:25:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd813a88-bc15-3003-be7a-1d54e77bdbd6 | -9.57367 | -45.73284 | 2025-08-27 04:25:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ef4388a-fe8e-336c-be89-2d21b7fb4763 | -7.14955 | -44.14591 | 2025-08-27 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77f54ea4-6a7b-31d8-84c2-59068bb918fc | -8.1351 | -49.58855 | 2025-08-27 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8260334-fd8e-3ce2-9e9f-803ea2b7eac1 | -4.79286 | -47.27568 | 2025-08-27 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d7a67c0-c0aa-34ec-8445-caa0c7acacca | -10.68549 | -47.13621 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbd35249-ccf7-3583-85e4-d99de2d43a89 | -10.50235 | -51.60319 | 2025-08-27 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 36787e9f-a276-35ed-a432-ef9ab23ae1bb | -8.88525 | -60.7672 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README39.md)
