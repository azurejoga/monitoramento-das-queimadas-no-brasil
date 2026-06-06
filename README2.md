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
| 98ed8e8a-324e-3d10-a3c0-15819c720571 | -17.3048 | -42.6182 | 2026-06-06 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 722bb385-ab97-322e-b6fa-68991d44c414 | -19.7513 | -53.5407 | 2026-06-06 01:10:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 16f841c3-a57e-3f71-bf31-a30f25829ed5 | -17.3041 | -42.643 | 2026-06-06 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 45f6e2cf-a44e-355d-82ea-a889c6c06973 | -11.5686 | -52.8057 | 2026-06-06 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| c89a51e5-f9cb-3702-a992-7126160a3631 | -11.5496 | -52.8076 | 2026-06-06 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 0ae9f13f-954b-332e-847f-d007bb319b3f | -11.5688 | -52.7848 | 2026-06-06 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 63c20917-c9cd-378b-aacd-a9826de1050d | -11.5499 | -52.7867 | 2026-06-06 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 172.1 |
| 93c3d341-6d26-31b7-ac53-c575ee5fa942 | -11.5686 | -52.8057 | 2026-06-06 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 6c4ac22f-2179-31b7-9463-670887078bdc | -17.3041 | -42.643 | 2026-06-06 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 98.3 |
| e02c650a-049b-3548-9335-b8cca1814608 | -11.5496 | -52.8076 | 2026-06-06 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 3b67fabf-9ac3-3ccb-8c2c-8f8751e2b250 | -19.7513 | -53.5407 | 2026-06-06 01:20:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 094f3249-b2f1-3c72-a0cc-22b4ea30b68e | -11.5688 | -52.7848 | 2026-06-06 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 0009a025-ddec-3b22-9a76-4938cb4f5d0e | -11.5499 | -52.7867 | 2026-06-06 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 160.2 |
| 22b848da-447c-39ea-8ac7-9a904a7f621b | -19.7341 | -53.5453 | 2026-06-06 01:27:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2b44864c-7784-3ea7-9d77-92a77abe2533 | -19.743601 | -53.542099 | 2026-06-06 01:27:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7e33b92f-d39b-366e-97ee-f4e024397130 | -17.3041 | -42.643 | 2026-06-06 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 77.1 |
| c1ed56af-e5aa-37c8-9752-f7432399f3f1 | -19.7513 | -53.5407 | 2026-06-06 01:30:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 836dbdd2-022d-37df-83a5-db49f9e200f4 | -11.5496 | -52.8076 | 2026-06-06 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 127.4 |
| b599343c-0e2d-3f4f-a309-ec7c02285c07 | -11.5499 | -52.7867 | 2026-06-06 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 9d4fee67-1e4e-3062-86d5-51363e5a6991 | -11.5686 | -52.8057 | 2026-06-06 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| ea853333-3b56-3038-82dc-54bc5dd8b686 | -11.5688 | -52.7848 | 2026-06-06 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 8349109f-61e0-394d-85e8-df1f5d9d382f | -11.5499 | -52.7867 | 2026-06-06 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 159.0 |
| 7d702e52-7be4-3d27-bb7e-3e27e424ba95 | -11.5686 | -52.8057 | 2026-06-06 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 5ed96fb4-f18d-3c0c-ae02-7bee7cdf29e2 | -17.3041 | -42.643 | 2026-06-06 01:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 89cbc60f-3515-3226-8dfc-99b9d1a6402a | -19.7513 | -53.5407 | 2026-06-06 01:40:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 29e88c2a-9b7c-31fc-8f04-bbd7b693b495 | -11.5688 | -52.7848 | 2026-06-06 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 909dbc13-5d92-34dd-b36e-03a9a081fa3b | -11.5496 | -52.8076 | 2026-06-06 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 9aedffd7-af62-305c-93a1-4831423ee1f7 | -11.5496 | -52.8076 | 2026-06-06 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 88781112-69c7-34ca-993b-163646e19a51 | -11.5499 | -52.7867 | 2026-06-06 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 3ad49ebd-c0df-31b4-b374-2c288de4476a | -11.5688 | -52.7848 | 2026-06-06 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 57debcbb-6f98-3354-8b3a-c21ec6f4f0f3 | -11.5686 | -52.8057 | 2026-06-06 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 11a585d1-6a14-35fa-86a6-8fb4ba1267dd | -19.7513 | -53.5407 | 2026-06-06 01:50:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 58aa754c-fe47-36ea-b260-c2336690d99e | -17.3041 | -42.643 | 2026-06-06 01:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 53.3 |
| f5eb3ec6-ea02-37e5-b204-5f126c88880c | -11.5496 | -52.8076 | 2026-06-06 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| c4080cdd-83c8-3ff7-b15b-971f5d4bc20b | -11.5686 | -52.8057 | 2026-06-06 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| a5186145-bde1-350c-94f2-7077e4c50809 | -17.3041 | -42.643 | 2026-06-06 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 50.8 |
| fedc9825-9d38-3ea0-9953-6d9bbc76679f | -19.7513 | -53.5407 | 2026-06-06 02:00:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 901290ac-3f09-3259-a9cf-674b884f6e35 | -11.5499 | -52.7867 | 2026-06-06 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 79f5bb9e-1a24-3a61-b881-379b9e8ca75f | -11.5688 | -52.7848 | 2026-06-06 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 659a269e-77b9-327b-b355-2ab90364166e | -6.0502 | -47.8841 | 2026-06-06 02:10:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 39.0 |
| aeb9edbc-0944-3305-abd5-b38d9b457f8b | -11.5499 | -52.7867 | 2026-06-06 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 117.5 |
| f0fc95fd-ba3f-3946-b73d-be8dae0f3638 | -11.5496 | -52.8076 | 2026-06-06 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 3b284873-1837-39d6-a28f-24d3d63b5b12 | -17.3041 | -42.643 | 2026-06-06 02:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 4c9e3c2c-4352-3a3f-8e5d-c6f1d0b1abc7 | -11.5688 | -52.7848 | 2026-06-06 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 8551fd25-9f45-3cc4-b6a7-6d81aeffe15d | -11.5686 | -52.8057 | 2026-06-06 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| daaa044a-5629-3afc-b123-ba0ea209f2d8 | -11.5499 | -52.7867 | 2026-06-06 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 5e71b93c-93e1-3d2a-8f55-a06c5ccc7b81 | -11.5496 | -52.8076 | 2026-06-06 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| f80e44e5-1c84-308e-9ab5-88e81b36a897 | -19.7513 | -53.5407 | 2026-06-06 02:20:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 46.4 |
| ba93f544-0a9b-3b86-8080-c6c620c06c2b | -11.5688 | -52.7848 | 2026-06-06 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 6975fc0b-de83-3add-860f-c7ab98505c65 | -19.7513 | -53.5407 | 2026-06-06 02:30:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 47.0 |
| dfaf89e4-39f2-3291-a3e5-9693444719db | -11.5499 | -52.7867 | 2026-06-06 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 84152853-058d-3092-8871-c6c24ca899f4 | -11.5499 | -52.7867 | 2026-06-06 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 30.1 |
| c483cd2f-1523-3b31-a966-60d6696041e3 | -11.5499 | -52.7867 | 2026-06-06 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 7b5f4d86-348a-39af-bb8c-c1cc3888de99 | -11.5496 | -52.8076 | 2026-06-06 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 8c479265-c461-3e8d-9569-026acfaa7c1d | -11.5688 | -52.7848 | 2026-06-06 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 35fe288b-499c-32b0-8d0a-b1d46f56b658 | -6.44396 | -44.56253 | 2026-06-06 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c3b2d9c0-045d-328e-b22c-ce31e67c9ffc | -6.44193 | -44.58524 | 2026-06-06 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c2743729-6589-316a-a8cb-50893deb8fbb | -7.3358 | -37.43177 | 2026-06-06 03:30:00 | NOAA-21 | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bf49af59-5a44-33fc-9a83-57737d2a4b7a | -6.44511 | -44.56772 | 2026-06-06 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4b9de5d4-31d0-3e3e-b3a1-bee3634f3ab8 | -6.44618 | -44.56184 | 2026-06-06 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b23176ee-a156-335f-8b3d-619d0515698a | -7.15958 | -44.06671 | 2026-06-06 03:30:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4044bba-0718-3564-acf5-22e269a4757a | -7.00547 | -43.86215 | 2026-06-06 03:30:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39222491-69de-3ef2-bf2e-8fe6cbf0d12f | -6.43402 | -44.57897 | 2026-06-06 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 593e549e-1abe-3bf1-af04-3d485d6ad8d2 | -6.72104 | -44.37553 | 2026-06-06 03:30:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f139565e-b075-37d6-9768-7d1c4b9eadd5 | -7.15424 | -44.0601 | 2026-06-06 03:30:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ef65736-0d15-3a9d-aabb-cab6a97db43c | -6.99249 | -42.87699 | 2026-06-06 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| e64337bc-288c-3886-83d4-52dec68cefc9 | -5.35081 | -45.18598 | 2026-06-06 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fe3ee7a9-bfbd-3615-a3fa-8c72045448d9 | -6.98715 | -42.88457 | 2026-06-06 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 6287eaf9-88f9-38bd-ba3e-529315289d2f | -6.72767 | -44.37454 | 2026-06-06 03:30:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 25e7472b-cc9f-3715-9a27-8c215a1eede9 | -5.49387 | -37.24398 | 2026-06-06 03:30:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7daf2452-d9a3-3c23-9af5-261551c31f0e | -6.99381 | -42.88146 | 2026-06-06 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 7d1f78d6-5cb2-3d9d-9a3a-b63dc8029915 | -6.72869 | -44.3704 | 2026-06-06 03:30:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11a8f868-d8b7-3915-a5d2-a2fcff31a6f1 | -6.44953 | -44.56921 | 2026-06-06 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c43f3964-da24-3935-a808-0ccd8fdbbe61 | -6.98198 | -42.87931 | 2026-06-06 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 83ad21e5-4cf1-37e6-b927-31ebcc54db62 | -6.9858 | -42.88017 | 2026-06-06 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 9e4047dc-27bc-381b-aac6-a9cecc800c4c | -6.9917 | -42.88126 | 2026-06-06 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 03d2dd57-0108-363a-a216-80fcee63474f | -6.98658 | -42.87589 | 2026-06-06 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a7001059-fdb3-3a8e-9335-c25a1d5c19a6 | -6.44074 | -44.59181 | 2026-06-06 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 87320039-c10c-3465-9d41-69d94e3ee6da | -6.98867 | -42.87602 | 2026-06-06 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 9fbdf737-17db-3254-8bfd-492db20fe59d | -6.43637 | -44.57821 | 2026-06-06 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8463114c-c4a2-3d29-aca1-2aef0b3e29be | -5.92665 | -43.47819 | 2026-06-06 03:30:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| abca8e87-f4d1-342c-a606-7edcb9ca6cb6 | -6.45179 | -44.56855 | 2026-06-06 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 481cac41-953e-300d-a1c5-57cf71a244f0 | -6.43825 | -44.59277 | 2026-06-06 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aec0aa2a-c1d6-3e06-9dc1-3e228851489a | -6.99919 | -43.86099 | 2026-06-06 03:30:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9959b6a-9635-37e3-b5f2-e3c43a481056 | -6.985 | -42.88445 | 2026-06-06 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 31d430ae-25d2-3094-a45e-ff85b79e0628 | -6.72113 | -44.3735 | 2026-06-06 03:30:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7b3d08f2-475a-3443-9bf3-3f8ef92ce64e | -6.43956 | -44.58587 | 2026-06-06 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cdc5fb17-94ee-324f-b781-4d6b75044661 | -6.45063 | -44.5634 | 2026-06-06 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| df56e1e9-082e-3d5d-a966-a417c66210ff | -5.92573 | -43.48325 | 2026-06-06 03:30:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b73041c5-7ed5-3a6c-bda0-9844a4184e49 | -6.72757 | -44.37665 | 2026-06-06 03:30:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78327196-2af4-37f3-9885-7a23778c8ed8 | -5.34939 | -45.1863 | 2026-06-06 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 269659b5-4996-373f-868b-095510525d02 | -6.72212 | -44.36954 | 2026-06-06 03:30:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fca6cfb8-0a31-39b1-953e-6f8857ca049f | -6.98122 | -42.88358 | 2026-06-06 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 218a72d4-fe73-3239-8d51-b76993a86533 | -6.98791 | -42.88028 | 2026-06-06 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 5c708d0b-27c4-3c85-858b-51a48a649672 | -12.50341 | -46.28999 | 2026-06-06 03:32:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ccd014a0-7f28-351c-bf84-c3346cc75087 | -12.06139 | -45.98188 | 2026-06-06 03:32:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe485f4f-dcea-3300-8814-7cf225f3b083 | -14.22542 | -45.80341 | 2026-06-06 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6d7b0ff6-8c68-30d9-a254-077b75c93de5 | -12.49678 | -46.2887 | 2026-06-06 03:32:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3c66318d-d5f1-3e11-b568-03865aa9ab11 | -14.23162 | -45.80491 | 2026-06-06 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 600bdbd7-5614-38a0-b829-f33bc7744628 | -12.50646 | -46.27542 | 2026-06-06 03:32:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README3.md)
