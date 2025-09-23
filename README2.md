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
| 0795e448-8f25-3204-90e1-3da14a208d0d | -6.2598 | -45.3184 | 2025-09-23 00:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| a3215793-a895-3541-be70-40cfa84e8f0b | -11.6247 | -52.8624 | 2025-09-23 00:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 56d8c1c1-0eae-3454-9d8a-fcd8beb698a5 | -11.6436 | -52.8605 | 2025-09-23 00:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| cec70296-12fd-3a70-a488-58cd92f01e49 | -7.8887 | -44.0281 | 2025-09-23 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 106.6 |
| e81d0eed-b4cd-3238-9fe2-5ba80acd6579 | -12.88275 | -46.75953 | 2025-09-23 00:50:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e969636c-6941-3e96-becb-0dcefd9249f6 | -12.8855 | -46.77664 | 2025-09-23 00:50:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8325130c-2ee6-38cd-a415-c499ce6bdded | -15.94504 | -59.48452 | 2025-09-23 00:50:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 1c3443f5-f601-32fe-832c-4b68021355fc | -15.95895 | -59.48216 | 2025-09-23 00:50:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 0029b99c-e8c2-3289-9a24-02ad16bcd48e | -13.63997 | -47.3158 | 2025-09-23 00:50:00 | TERRA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4c95cd50-f376-3f24-9ddf-48ad6b957d14 | -12.88914 | -45.66817 | 2025-09-23 00:50:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 7b7e0a59-27b3-3713-b298-300b197f75a0 | -13.63717 | -47.29884 | 2025-09-23 00:50:00 | TERRA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fb570cab-1c81-3a32-9f1d-dea9a1cbba84 | -13.01774 | -48.73257 | 2025-09-23 00:50:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 06b4abc6-e084-3203-893f-d1a2e84708cd | -13.01585 | -48.72015 | 2025-09-23 00:50:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 0265dabe-faf1-367d-8821-3e88750b0e0c | -15.73897 | -59.44767 | 2025-09-23 00:50:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 6041a20d-b3d4-3fac-beb2-d7a2dded63e9 | -13.6385 | -47.3047 | 2025-09-23 00:50:00 | TERRA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f76d42f5-c030-36c3-9e5f-565b22706e3e | -10.96289 | -45.7088 | 2025-09-23 00:52:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 207a7bba-abd0-30c4-b9be-e252dbf2db2e | -10.33775 | -48.6911 | 2025-09-23 00:52:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f554a78a-b30e-3def-9e35-a7eda222c965 | -8.53238 | -44.9761 | 2025-09-23 00:52:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 46.1 |
| c90f65ce-09f0-3ca8-af3e-e34974af7a3b | -11.62537 | -49.90623 | 2025-09-23 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 29b7446d-c9e4-39fa-8d8f-977f36288c27 | -11.65247 | -52.87099 | 2025-09-23 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 7ea38c7f-a5ea-3092-b453-f06fc280c58d | -8.60254 | -50.4525 | 2025-09-23 00:52:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 04961714-9286-3191-9712-2eb87bc7f047 | -8.51758 | -44.97936 | 2025-09-23 00:52:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| e58807d6-be85-3854-bf4b-3ee34752a029 | -10.96419 | -49.66261 | 2025-09-23 00:52:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0fd63235-671c-3d1f-8e73-dd3d6b2abf6e | -5.69755 | -51.05558 | 2025-09-23 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bcdb0155-128f-3440-ba7f-59e25843579d | -11.86879 | -56.87093 | 2025-09-23 00:52:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 6107342f-47d5-3297-8f49-93a49804302b | -5.92238 | -50.05878 | 2025-09-23 00:52:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8d2a0586-98b2-3c40-8fe1-048545a39c21 | -4.9648 | -48.01044 | 2025-09-23 00:52:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 84d24582-e60c-3022-bc6d-c5e84c51b6c6 | -7.90086 | -44.01702 | 2025-09-23 00:52:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 6e0953f7-0380-39c9-b6dd-dcc1d306e5cd | -6.25118 | -45.33032 | 2025-09-23 00:52:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 324.2 |
| 46b435f9-9520-3dde-ab4b-72912d96716c | -11.87043 | -56.88437 | 2025-09-23 00:52:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 98f7d3ef-c3f0-3705-873a-f7fec4a5e4bf | -8.01499 | -45.47135 | 2025-09-23 00:52:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 31.4 |
| b45f4b4b-6e16-3d62-9b11-f59f0478ce2f | -10.85279 | -45.42439 | 2025-09-23 00:52:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 297dd820-712b-3e43-ba32-8290eb587c50 | -11.62233 | -52.84801 | 2025-09-23 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 915601af-4d2c-3e68-bd80-62890bd5e781 | -11.40972 | -48.95675 | 2025-09-23 00:52:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| de295991-6d05-3366-8f31-75d99d1d0a00 | -6.58865 | -44.54532 | 2025-09-23 00:52:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 56e501da-90fd-3508-af56-e3137ac841e7 | -11.62109 | -52.83907 | 2025-09-23 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f9b78711-42c2-3732-bf51-b4f9c9ace2c8 | -8.01635 | -45.46575 | 2025-09-23 00:52:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 44.7 |
| ae3cf0e9-c707-39d9-af28-1ca33ab6d7a9 | -6.24373 | -55.36283 | 2025-09-23 00:52:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1c580923-8961-38f0-b194-f7ca2322dfca | -12.40423 | -46.9986 | 2025-09-23 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| e5a6bdd8-9388-31ed-8d05-9a6a8f2421a7 | -9.97019 | -51.46875 | 2025-09-23 00:52:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f83a4df8-bc77-3fd9-8f51-178fdc1abff8 | -7.59476 | -44.4452 | 2025-09-23 00:52:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 9d10b1bb-308c-3ba7-9ef6-8c5d1759eeef | -12.07281 | -44.80976 | 2025-09-23 00:52:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 4b31fc5e-0ea7-391a-8bc3-d72985a29e59 | -4.96159 | -47.81486 | 2025-09-23 00:52:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 17238271-c551-3525-a5c7-0473f0d57099 | -4.9646 | -47.82798 | 2025-09-23 00:52:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 6c70debd-fa78-3e10-a28d-988389538851 | -4.78742 | -47.25627 | 2025-09-23 00:52:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 69da4215-35e1-33c8-b00f-d2a79d93de53 | -8.07949 | -55.04408 | 2025-09-23 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4acd3fc1-0921-3d8f-a457-36e6fbe9eaef | -11.63361 | -52.86461 | 2025-09-23 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a74bfd97-68ef-3645-9979-382d7e10c057 | -11.65123 | -52.86205 | 2025-09-23 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 38d8e1cd-ea2f-3052-9d91-83a3fca45f32 | -11.63238 | -52.85567 | 2025-09-23 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| fdaef120-c672-397f-a110-471e87484e16 | -11.86781 | -52.90048 | 2025-09-23 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 21c6b35b-4f5a-3a84-8c12-71a6caefd21c | -5.64406 | -51.46332 | 2025-09-23 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7aa9db8d-0cc7-3227-b5ab-8ed53ca0533a | -10.87383 | -49.40018 | 2025-09-23 00:52:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7fe32e28-cbec-3f55-b0ef-48410b5af35b | -11.86456 | -56.87708 | 2025-09-23 00:52:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 6d0f42f1-cd1d-30a6-ab43-6338f3a10726 | -5.6551 | -51.47237 | 2025-09-23 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a5dfb792-22b5-3382-b385-a7209cd6ec33 | -10.85843 | -45.41681 | 2025-09-23 00:52:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 1f530cb5-8834-33a4-9b80-a18368bb1a40 | -8.01099 | -45.44588 | 2025-09-23 00:52:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 38.0 |
| f322cf2c-1a7c-334c-81fe-265fe05e55dc | -12.06843 | -44.78406 | 2025-09-23 00:52:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 84829056-4ad5-3001-b583-c148b30072f0 | -6.4232 | -53.31203 | 2025-09-23 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6da0771d-4388-35a5-8e35-16a07ebb3e33 | -6.59679 | -44.5377 | 2025-09-23 00:52:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 2d150f42-6d68-35f4-b5e9-7035f9126511 | -7.89397 | -44.02579 | 2025-09-23 00:52:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 128.3 |
| b6eb5269-f45e-3e51-92a8-80be02a5857e | -10.86235 | -45.44003 | 2025-09-23 00:52:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 067975c0-cfd7-3a36-ae37-13d459ba7eeb | -7.8778 | -44.02892 | 2025-09-23 00:52:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 87dd6023-97b5-30bc-8851-07a5d24aed23 | -11.6248 | -52.86589 | 2025-09-23 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 27.5 |
| c6fc5cc4-9c64-329d-ac42-78319b532ad1 | -7.88478 | -44.02065 | 2025-09-23 00:52:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 67580abd-bf2b-3cb7-a0fa-c2fc094a0a5a | -6.7203 | -47.20703 | 2025-09-23 00:52:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a5eebd02-9d66-3766-a9fe-38f99d5f6984 | -9.55036 | -51.36618 | 2025-09-23 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e22503d5-fc74-36c1-9acd-2623786098a8 | -6.26636 | -45.3281 | 2025-09-23 00:52:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 9faadd2f-473d-3a88-9194-60eadd5cb658 | -11.64366 | -52.87227 | 2025-09-23 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dcd1433a-1711-35a9-8079-da745fa7e810 | -12.39851 | -46.99303 | 2025-09-23 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| c4358f94-296f-33f9-88d1-2afe56423197 | -7.89061 | -44.05555 | 2025-09-23 00:52:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 92f4d8ae-7125-308d-89ec-5cde1cad09c9 | -7.1601 | -48.30104 | 2025-09-23 00:52:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 30.5 |
| a9b6fdcd-3793-3c38-bb57-0a0c6b763ca3 | -6.5179 | -54.87531 | 2025-09-23 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7f67bac2-5709-3a7a-841a-fb2611cc53ec | -7.17184 | -48.29919 | 2025-09-23 00:52:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 12.1 |
| b0db9b63-34fe-35d0-96a6-c1ddf5ecf61c | -12.4013 | -47.00997 | 2025-09-23 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5bd7f5cf-fc87-3063-931a-6a57bc6a420c | -9.59541 | -46.43923 | 2025-09-23 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 00395d78-5450-3d2a-aa67-5c3dd7223fd7 | -11.62356 | -52.85695 | 2025-09-23 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 3de6f863-5fd6-35d1-b0d5-85dc6d325ce3 | -6.2538 | -45.33682 | 2025-09-23 00:52:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 416.4 |
| 7c8397ce-7890-3640-be6a-66a30791240a | -11.85899 | -52.90176 | 2025-09-23 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 09aa6d4d-aa29-39d5-bd7b-e7a9fc9fd47e | -6.25599 | -45.36015 | 2025-09-23 00:52:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 6b9ce70b-40b4-3d28-8c1f-b6a24a184eee | -7.15768 | -48.28472 | 2025-09-23 00:52:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2a728dce-c0c7-30ff-8098-a1ccdab4f779 | -11.22044 | -46.16155 | 2025-09-23 00:52:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 35ef48b1-38b8-3eaf-9d6f-c5cf4289525a | -11.6299 | -52.83778 | 2025-09-23 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 2f43a935-73c5-3456-a3b4-9bd3114af213 | -10.96578 | -49.66765 | 2025-09-23 00:52:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 62a655c8-0d29-3af5-b780-29fcb27f37e7 | -5.68777 | -51.05699 | 2025-09-23 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 183cb909-11c3-3af3-86ac-814199fccf90 | -11.63114 | -52.84673 | 2025-09-23 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 85576672-0a53-3689-be7f-1de03970206a | -4.78276 | -47.25147 | 2025-09-23 00:52:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 49.6 |
| be8e77d3-48ca-39d4-ab7c-8fa6e075883c | -7.16696 | -48.29451 | 2025-09-23 00:52:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 6e8c9b47-0e22-397d-906d-5a019089f87c | -2.25857 | -47.89468 | 2025-09-23 00:54:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| cbe9d1e8-97c9-3513-9a9c-7c713de13add | -2.79563 | -49.60031 | 2025-09-23 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 9fbcf31b-f97f-3036-b11d-ffb263c22d13 | -3.52067 | -49.44514 | 2025-09-23 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| e3c94bef-8d33-3e34-9125-4e82d6e005fe | -3.85748 | -52.24526 | 2025-09-23 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5562a1b7-a10a-3bd4-99ce-c87de7eaf5b0 | -3.38392 | -50.25844 | 2025-09-23 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| e1312943-6e20-3c4b-a09a-8a81779b9669 | -2.25541 | -47.8732 | 2025-09-23 00:54:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 7079c818-fd2a-3af1-a886-ecd8e5b1b3e4 | -4.07794 | -48.04199 | 2025-09-23 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 5d3c8666-4db3-38b4-a884-bc782acf4ea4 | -4.49499 | -48.11227 | 2025-09-23 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 9abaa655-15e8-398c-9559-d4fe6a93f6a9 | -3.35667 | -59.43527 | 2025-09-23 00:54:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 25.0 |
| d7c993a9-7a43-3a88-92b7-473b6020d0e5 | -1.61676 | -54.29532 | 2025-09-23 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| dd442620-23d1-3543-8930-395f0ced22de | -3.24351 | -58.84962 | 2025-09-23 00:54:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 71a3a84b-509a-3c7f-be4d-ed7970ee799f | -4.13053 | -48.83121 | 2025-09-23 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| facc671c-88f2-314e-9559-f24db108becd | -2.52744 | -57.85772 | 2025-09-23 00:54:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |


[Clique aqui para ver as próximas entradas](README3.md)
