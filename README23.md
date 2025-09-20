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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6802bc4d-6888-37e4-a6d0-c418ba6fbde8 | -9.65621 | -62.2728 | 2025-09-20 04:55:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f45da87-2ce9-3e84-89b2-c23141bb1eea | -13.07114 | -42.14459 | 2025-09-20 04:55:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f6278c62-a236-31b6-9452-5f83bda8a2dc | -10.87872 | -53.74369 | 2025-09-20 04:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4f6718b-174d-31dd-ba9c-a476b56ada2a | -10.2331 | -54.19265 | 2025-09-20 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c6e4980-9f06-3a74-a002-f30d3ec8d6d4 | -12.91402 | -46.78307 | 2025-09-20 04:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06c8b9cd-665c-33c2-b5a9-c97ad148e913 | -10.0198 | -46.2442 | 2025-09-20 04:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7969f6ed-4b1e-372c-8353-1f79224f5e42 | -10.879 | -47.79454 | 2025-09-20 04:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e79dcb9-9ca5-3067-ac5c-b9db441a5208 | -12.90991 | -46.77781 | 2025-09-20 04:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b9bbd89-ba47-3e90-b61b-61798f8052ba | -9.35662 | -54.52259 | 2025-09-20 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5abedf0a-09aa-36df-8ac0-9c65f9e55b87 | -15.29433 | -56.81435 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8778a3cb-6530-3161-aaf1-b8236be85287 | -11.99294 | -63.52505 | 2025-09-20 04:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3fc2474e-e0df-34cd-a250-b0b97ad1b534 | -12.09152 | -44.81244 | 2025-09-20 04:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06378a9a-5a75-3f4f-b90b-b91958957f59 | -9.3951 | -54.69221 | 2025-09-20 04:55:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8bc1d065-13df-360e-90ae-de772b7365b0 | -10.32319 | -45.23905 | 2025-09-20 04:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 0376a9bf-2f2c-3652-a812-7bec6afe2273 | -10.88649 | -53.73774 | 2025-09-20 04:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 945af167-e9ff-3687-9c96-a2ca051953f0 | -12.07845 | -44.83048 | 2025-09-20 04:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51e42ab9-ce42-38b0-b115-1c412f064442 | -12.15025 | -44.93706 | 2025-09-20 04:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa7c55b4-d4da-3e97-9d18-548f057c3814 | -9.48199 | -54.4396 | 2025-09-20 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c81486ab-eeab-3fb5-9069-7cad12d17f22 | -9.40901 | -57.04412 | 2025-09-20 04:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6bae1bc6-2224-360b-acf2-8621d157f94a | -9.35603 | -54.52621 | 2025-09-20 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 053937c2-ef47-36bd-be2e-fc7148a2cafe | -9.36058 | -54.5195 | 2025-09-20 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64204537-b68b-39b7-b2ff-2785de121912 | -14.4376 | -46.5085 | 2025-09-20 04:55:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2954b51a-4951-38cf-98bc-3eeaa72c53ae | -10.23644 | -54.19319 | 2025-09-20 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b17bfc1-b691-3c0f-a835-0e56c49daeda | -10.33839 | -45.24053 | 2025-09-20 04:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7b29e91d-3f51-3d94-a9dd-286982461d9a | -15.28648 | -56.86118 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 726cbbef-d98d-3dd5-b20f-9dcdc1f989f2 | -9.40977 | -57.03959 | 2025-09-20 04:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 920ff2b0-6e91-3d54-bb20-aad44497bc2f | -9.4741 | -54.44566 | 2025-09-20 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4a735cd-ca0e-3b54-b8fa-b71c90f274d8 | -10.02801 | -59.35657 | 2025-09-20 04:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 160c4b43-32f1-3dbe-888a-b7ad84d65e82 | -12.07805 | -44.83366 | 2025-09-20 04:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d5bb721-aa80-3d9b-81e3-8379d1b83892 | -10.34275 | -45.24629 | 2025-09-20 04:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7dbe4cac-c07e-3244-99f9-f03d38e486d4 | -10.3391 | -45.23514 | 2025-09-20 04:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 86b0f5a3-80c6-3c8d-ae77-0509fb091d81 | -12.15504 | -44.9417 | 2025-09-20 04:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50ec7ab9-a387-3b89-9421-11fffa9a3803 | -15.31099 | -56.82121 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74cb0fb2-2543-3837-86bd-04f80a5dde18 | -8.96797 | -47.68412 | 2025-09-20 04:55:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5f15b3c-e00e-330d-8bb0-07f746f1201f | -10.34346 | -45.241 | 2025-09-20 04:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a9d72683-1225-315c-8384-cc3b4b8dcc11 | -10.32598 | -45.25671 | 2025-09-20 04:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c952dcc9-0ab0-3c38-9311-274891937e3a | -15.28582 | -56.86513 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7068bc9-5b2f-35be-ab84-ffec6ebf04f8 | -11.16559 | -49.93678 | 2025-09-20 04:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70c848b9-c433-36e4-811a-ac575163e82e | -9.36 | -54.52312 | 2025-09-20 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b60bb71-62c6-39e2-976c-e94097b5a243 | -9.41426 | -57.03571 | 2025-09-20 04:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a9ebe9d-d139-3ab1-9fea-2b33d4471608 | -9.84749 | -59.88361 | 2025-09-20 04:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bfcfd9d6-61bd-37a4-b843-04708d5a8e4c | -9.87541 | -54.05434 | 2025-09-20 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c87402d-cb92-3cda-ae4b-ebf1113cf554 | -12.90929 | -46.7826 | 2025-09-20 04:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee2b68a7-0f49-3c69-8aa2-37d5d0944a9c | -12.85298 | -53.00577 | 2025-09-20 04:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 287d7694-f3a4-328b-aee1-628886b58e0b | -9.93769 | -55.73403 | 2025-09-20 04:55:00 | NPP-375D | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 88558752-4afd-3d52-9d5c-8cbb969a9874 | -11.27783 | -47.41184 | 2025-09-20 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec1632e6-8c19-3a11-aa0c-37c9002f583a | -15.28265 | -56.82027 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e70f7e1-828c-3929-b589-d8c213a35b6f | -12.12522 | -55.45774 | 2025-09-20 04:55:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2d6a3a7c-b4d5-36f4-85ad-3b825306c7bf | -10.87816 | -53.74721 | 2025-09-20 04:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52d39e84-42d6-3ea3-9031-afd8c902409f | -15.28235 | -56.86454 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 311c39ef-8186-3459-b423-426fa17fedfd | -9.01266 | -48.02187 | 2025-09-20 04:55:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70fc08eb-35ee-384f-a50d-d8de79288ae8 | -9.40304 | -54.68607 | 2025-09-20 04:55:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a5c15e1-5f81-3b6f-b1cf-fe50ff0e365c | -12.90456 | -46.78214 | 2025-09-20 04:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97056a5e-a468-3d43-98af-9e292ca9127f | -9.42768 | -57.04728 | 2025-09-20 04:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebfd62c5-d7f8-3cda-8a23-a8fd511177fd | -13.2309 | -57.13253 | 2025-09-20 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34c88ac3-7120-3154-a084-a786e7b9f18a | -12.07884 | -44.82733 | 2025-09-20 04:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f8b1939-4e9e-3e08-8052-2b91a17b8053 | -12.07723 | -44.84016 | 2025-09-20 04:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0abc1aca-018a-38c4-bfa7-f5d288d9935b | -11.6327 | -52.86273 | 2025-09-20 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1cf9ca0-728e-370f-b3c9-abdd245d6475 | -10.73434 | -55.52098 | 2025-09-20 04:55:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c63e2f80-68ff-3b6c-8b3c-8c428d3cb170 | -12.0817 | -44.8475 | 2025-09-20 04:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08138331-d86e-3b44-a5a0-5208f571e375 | -12.89984 | -46.78159 | 2025-09-20 04:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e5be3ed4-9d48-3460-821f-690d1d436194 | -15.282 | -56.82416 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79b5486e-9f3e-30e7-8539-e69186effbc5 | -13.96825 | -45.04877 | 2025-09-20 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7770e3b1-156e-3eda-8e70-0abed8b46120 | -8.17395 | -55.17562 | 2025-09-20 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 659b363b-2687-3018-a12d-7b73e248ffe6 | -9.65682 | -62.26954 | 2025-09-20 04:55:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9df2012e-600b-33c2-895a-2883f5b14c10 | -10.23854 | -48.05506 | 2025-09-20 04:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ef26510-42f9-3af8-9dfb-296099d96972 | -9.46152 | -54.67295 | 2025-09-20 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29d22adb-dc29-3338-80d8-c294b25e3bb4 | -9.71864 | -55.61884 | 2025-09-20 04:55:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb55261b-6eec-3971-99e6-cff57ecf3108 | -15.27954 | -56.86001 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d19b4d1-e271-3cd2-bc7d-535d182c6554 | -9.30939 | -48.90532 | 2025-09-20 04:55:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cff9e91b-92dc-34a3-a60c-db272f2c3d65 | -11.15824 | -45.33205 | 2025-09-20 04:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| deedc179-a8ab-3248-a493-a51e5f04da1e | -11.09906 | -44.88677 | 2025-09-20 04:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b62d266-7356-3961-b06b-f585997104ae | -8.94402 | -54.45958 | 2025-09-20 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24c40357-4152-3dd4-945a-4005f942d18d | -12.85634 | -53.00631 | 2025-09-20 04:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3cb25983-1929-3c31-aef7-2358e7565efb | -9.39114 | -54.69527 | 2025-09-20 04:55:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7d449d0-597e-3d90-a560-d34d726ee7ae | -10.24608 | -58.48318 | 2025-09-20 04:55:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 067c09fb-9cec-3e63-850c-ce4ac7fb49d2 | -15.27392 | -56.85102 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 44ca2e38-75af-38ca-8a3e-2d5878986e8e | -9.40759 | -54.67935 | 2025-09-20 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7df28cdb-d2f7-31ef-9624-d777dc3f8ef7 | -15.27458 | -56.84708 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 937908cb-1c08-3915-b274-edfe27e8444b | -11.64332 | -52.86073 | 2025-09-20 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34bae5b5-0291-3ba4-aa50-cb4d8bb3b500 | -12.8569 | -53.00268 | 2025-09-20 04:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 71f29bab-cfc5-3398-a4ba-05b4744b24e6 | -10.84615 | -53.78185 | 2025-09-20 04:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a755e82-596d-33af-a9ec-a77af271e955 | -15.31509 | -56.81802 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb85e981-48ac-3d35-be6f-6e909197139c | -10.85227 | -53.76488 | 2025-09-20 04:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8ebf990-2818-3d79-b0ad-e7525bc604a1 | -12.0764 | -44.84681 | 2025-09-20 04:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c94c98f-1c01-356e-b51f-c43aa90af6c9 | -11.29045 | -47.41811 | 2025-09-20 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f8bd92f-296e-3110-8ad1-441b02976ea6 | -15.27607 | -56.85946 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49e577e0-ffdf-301f-87e6-1ea645f7075d | -12.84846 | -52.99021 | 2025-09-20 04:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0759c62-795f-352e-91d6-b38a5faf91fd | -15.2978 | -56.81495 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a69e03b-f5bc-3d43-b749-23866e30ad50 | -11.15785 | -45.33509 | 2025-09-20 04:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 060c56c3-00bf-3588-ab58-8d6da32f988f | -9.36337 | -54.52366 | 2025-09-20 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2cf5b988-0fb5-3367-8c54-2da33da415a1 | -14.43266 | -46.50822 | 2025-09-20 04:55:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c419eda0-670d-3b97-a4fc-9fca522d2ed8 | -9.71233 | -55.61383 | 2025-09-20 04:55:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4faa5b9-79be-38d9-81ef-b7ca153bd30a | -9.18883 | -62.62076 | 2025-09-20 04:55:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e69df9b-6bfb-3b29-87b1-6158aa011e99 | -14.44252 | -46.50901 | 2025-09-20 04:55:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7e892693-7c40-39a1-924c-6b739d97f6ab | -10.32905 | -45.23354 | 2025-09-20 04:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ac6ad327-a725-3633-b9de-9af380616d28 | -9.39277 | -54.70673 | 2025-09-20 04:55:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fd0ed77-3537-3dc0-98e6-2a5fccfe54cb | -14.72683 | -42.3699 | 2025-09-20 04:55:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3335f217-9c43-38a6-a456-e856be892807 | -15.30882 | -56.81289 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 601ceae6-1602-3ccc-9cea-ef19bfe76499 | -14.44744 | -46.50949 | 2025-09-20 04:55:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |


[Clique aqui para ver as próximas entradas](README24.md)
