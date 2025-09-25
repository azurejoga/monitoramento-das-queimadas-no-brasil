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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eef9490b-b306-3670-9999-ca519e1bbb22 | -6.4317 | -43.0942 | 2025-09-25 02:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 171.2 |
| bbee39ba-4bd3-309c-8b10-2506ccff89c3 | -6.4129 | -43.0958 | 2025-09-25 02:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 04f4b8ba-6072-39c3-b87e-2135328c0231 | -2.9291 | -48.3181 | 2025-09-25 02:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 9e4479d6-6014-3675-9376-148003520980 | -17.9506 | -55.8731 | 2025-09-25 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.1 |
| 2ea14840-6897-3b97-aaf0-20684dcbb158 | -17.951 | -55.8522 | 2025-09-25 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.6 |
| 4c46b3ae-2791-3e17-b19a-1851b0ee6446 | -17.9312 | -55.8548 | 2025-09-25 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 237.3 |
| cb6e75ba-2b79-3946-905f-03e3a68c3e9c | -6.4131 | -43.0724 | 2025-09-25 02:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 45e9d031-c0c2-3b09-be9a-40c3e799ce33 | -17.9308 | -55.8758 | 2025-09-25 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 206.5 |
| 944b664b-a598-3741-b87a-fe09bbceffeb | -6.4319 | -43.0707 | 2025-09-25 02:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 145.1 |
| ac82d147-030a-37aa-9d03-65b6a0aeaa6a | -9.5598 | -47.536 | 2025-09-25 02:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| e39ddddd-a1d5-3067-adba-3a4f3d4b3460 | -6.4129 | -43.0958 | 2025-09-25 02:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| d495772e-939f-3aa2-b3f5-ef7d5857b6e1 | -6.4131 | -43.0724 | 2025-09-25 02:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| cee0a037-af9f-32cd-8744-7e5dec59edbe | -17.9308 | -55.8758 | 2025-09-25 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 190.5 |
| 60be73e7-353b-359a-bbac-3bc1ebbdd405 | -17.9312 | -55.8548 | 2025-09-25 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 238.7 |
| 69a9c0a9-28bf-33a0-afe3-cd7d769d2214 | -6.4317 | -43.0942 | 2025-09-25 02:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 5208b148-7bd4-3c59-88ca-6e8415040744 | -17.951 | -55.8522 | 2025-09-25 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 218.0 |
| 54b29fb7-edd1-3d4c-bcc4-64092ea714e5 | -15.7835 | -59.4853 | 2025-09-25 02:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 7ce92938-8f29-3cb0-9f7c-382ed8dc29ad | -21.9721 | -49.5102 | 2025-09-25 02:40:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.4 |
| 63c579d0-ecb0-3eec-b0eb-a703674d3bae | -15.7642 | -59.4872 | 2025-09-25 02:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 109.2 |
| b8d3d339-11ae-376f-8086-ed06aff37488 | -14.2554 | -42.3614 | 2025-09-25 02:40:00 | GOES-19 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 68ab41a9-768a-33c8-aaf6-a02999172d0e | -9.5409 | -47.538 | 2025-09-25 02:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 5b99672c-43c5-3b20-ae74-3ee849c4a899 | -17.9506 | -55.8731 | 2025-09-25 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 169.7 |
| c75d731d-95b4-39a6-8382-ae876c2e5362 | -15.7639 | -59.5072 | 2025-09-25 02:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 119.3 |
| d4bb851a-e0e7-3df4-9692-31456a7ae364 | -2.9291 | -48.3181 | 2025-09-25 02:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 65b48bb5-9091-30ca-9ccf-5f2264041867 | -17.9506 | -55.8731 | 2025-09-25 02:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.7 |
| 335670c2-9a1d-3cf3-b08e-db64616f2d83 | -17.9312 | -55.8548 | 2025-09-25 02:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 174.7 |
| f60beee7-dfb4-36db-999e-aefc72ed3c95 | -6.4317 | -43.0942 | 2025-09-25 02:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 166.1 |
| c86b2c2d-f501-3172-8f72-84191ce15c76 | -6.4129 | -43.0958 | 2025-09-25 02:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| cb5dea3f-62e3-3fee-8eb9-db1a077798f0 | -17.9308 | -55.8758 | 2025-09-25 02:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 167.1 |
| 8dca612b-9854-3b70-ad7b-2012661b5860 | -6.4319 | -43.0707 | 2025-09-25 02:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 40141836-6375-3195-9d26-37f3073b1c03 | -17.951 | -55.8522 | 2025-09-25 02:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.5 |
| 03e2098f-8b24-3cb4-963c-d5ba6e172f0c | -21.0131 | -50.0217 | 2025-09-25 02:50:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.8 |
| 95079d41-e00a-3c7a-b2a3-376f93adc8f9 | -20.9925 | -50.0261 | 2025-09-25 02:50:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 245.5 |
| a505285e-4c65-376d-aaa0-9ada62b7666a | -21.9929 | -49.5054 | 2025-09-25 02:50:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.3 |
| ef558acd-d84c-3681-87ad-ed0278914fb4 | -20.972 | -50.0305 | 2025-09-25 02:50:00 | GOES-19 | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 136.4 |
| 759ee210-910a-3981-95c4-56c653c8ab1d | -21.9721 | -49.5102 | 2025-09-25 02:50:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 136.6 |
| 45aefc55-77cd-3f00-9fc1-c43e9a6c4fde | -20.9726 | -50.0077 | 2025-09-25 02:50:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.4 |
| a03eb86f-027b-3b67-8522-76aa45235d1b | -15.7639 | -59.5072 | 2025-09-25 02:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| e242cf88-8a5b-36e0-8402-a821df8d301c | -22.0388 | -48.6376 | 2025-09-25 02:50:00 | GOES-19 | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Cerrado | 77.0 |
| e9f4fc4c-0815-3459-a253-5cc761c5ddab | -20.9931 | -50.0032 | 2025-09-25 02:50:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 142.0 |
| 66afc54d-019f-3e0f-858e-f9246be4d01c | -6.4131 | -43.0724 | 2025-09-25 02:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 11943a3d-2d04-3e3e-9df2-50d6f0c73702 | -2.9291 | -48.3181 | 2025-09-25 02:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| ffc75ff9-1e5a-3a99-8eaa-bed9c937306b | -22.0395 | -48.6141 | 2025-09-25 02:50:00 | GOES-19 | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Cerrado | 224.1 |
| f8b58e1f-2f58-3f52-a3a1-f09bb5ba6cd7 | -22.0603 | -48.609 | 2025-09-25 02:50:00 | GOES-19 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 159.3 |
| c5b0a6b5-2f9c-3a84-a8b5-b74ad1c851bd | -15.7642 | -59.4872 | 2025-09-25 02:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 97683843-69df-3abf-9db9-34f02526c7b4 | -20.9726 | -50.0077 | 2025-09-25 03:00:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.0 |
| e9463c3d-8ac3-398a-9447-c30a6cade21f | -15.7639 | -59.5072 | 2025-09-25 03:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 110.7 |
| ed5457f8-507f-39bd-8696-fbb49e7fa5f8 | -15.7642 | -59.4872 | 2025-09-25 03:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 011312fb-926d-3a2c-8521-8f7a9aa9391c | -2.9291 | -48.3181 | 2025-09-25 03:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 9be2e2cc-4150-3ad9-8a9d-ed43d5755a69 | -17.9308 | -55.8758 | 2025-09-25 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.3 |
| 55f07cab-0676-344d-97af-2be403d876b1 | -15.7833 | -59.5053 | 2025-09-25 03:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 56a31c6a-229c-3dc1-8a54-5f2ca397743c | -6.4129 | -43.0958 | 2025-09-25 03:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 08948920-5be1-3f50-a434-ccb7ba789b2f | -20.9925 | -50.0261 | 2025-09-25 03:00:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 271.4 |
| a789a491-05fa-33ac-a100-5270e9291e04 | -6.4131 | -43.0724 | 2025-09-25 03:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 9e11ba22-c153-38fb-8b81-55aedaa05a6b | -21.9721 | -49.5102 | 2025-09-25 03:00:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 121.1 |
| b33c7e41-933e-3243-b93c-156d3fe37a01 | -6.4319 | -43.0707 | 2025-09-25 03:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 8fec5c9c-c56a-3c83-8ac4-796189d69e6d | -21.9929 | -49.5054 | 2025-09-25 03:00:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.4 |
| 79f16e47-1320-3e79-beb1-a9b719578f6c | -17.9506 | -55.8731 | 2025-09-25 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.7 |
| 622ba948-6671-371b-9acb-f559b4d500eb | -15.7835 | -59.4853 | 2025-09-25 03:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| aa63be82-9a8e-35dd-b37f-2d481a39cb86 | -21.0131 | -50.0217 | 2025-09-25 03:00:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.9 |
| 2ac75591-dd9b-30b2-917a-f4ee3701241a | -20.9931 | -50.0032 | 2025-09-25 03:00:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 172.6 |
| d3ddef09-1ede-3e91-a961-fb023628572f | -17.951 | -55.8522 | 2025-09-25 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 125.2 |
| 231458b5-1e7e-37d1-b2f3-534fa4b6fe76 | -20.972 | -50.0305 | 2025-09-25 03:00:00 | GOES-19 | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 183.0 |
| 447eb1d1-ac14-3825-b377-888934b526cd | -6.4317 | -43.0942 | 2025-09-25 03:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 6ad1af85-dac6-31b1-ac76-ead2527cde44 | -17.9312 | -55.8548 | 2025-09-25 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 180.3 |
| 8c75c38f-f53b-3a48-8b25-bcbaa410b42f | -21.0131 | -50.0217 | 2025-09-25 03:10:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.2 |
| ac92cfae-34c8-34ec-9f27-4453cabddf8e | -22.0395 | -48.6141 | 2025-09-25 03:10:00 | GOES-19 | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 0e5b897e-b46b-39ba-a5fd-1c215668cfee | -6.4317 | -43.0942 | 2025-09-25 03:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 9db36bd7-fdea-35b6-b5b7-6fb950ca5a16 | -20.9925 | -50.0261 | 2025-09-25 03:10:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 202.1 |
| f7505872-bb78-3f99-bbb8-29cd07f6778c | -22.0603 | -48.609 | 2025-09-25 03:10:00 | GOES-19 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 8d44e4cd-da61-3b44-99be-624709bc1adc | -21.9721 | -49.5102 | 2025-09-25 03:10:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.9 |
| 9ad3d130-3286-34e9-9ded-01ab9b7873a5 | -22.0596 | -48.6325 | 2025-09-25 03:10:00 | GOES-19 | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Cerrado | 63.5 |
| daac6fc4-c2b2-342b-874b-366a0533f2ca | -20.972 | -50.0305 | 2025-09-25 03:10:00 | GOES-19 | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 126.7 |
| 7284c168-fefc-3215-a48a-6e2f28fa3d84 | -6.4129 | -43.0958 | 2025-09-25 03:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 252da011-ddac-3e09-8068-c7fb8ac2fb1d | -20.9931 | -50.0032 | 2025-09-25 03:10:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 139.9 |
| 5c7180b5-06e6-3a15-9e74-e4d1f4df7536 | -6.4131 | -43.0724 | 2025-09-25 03:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 3dc91403-f502-3960-bf2f-73708e0bc81b | -17.9312 | -55.8548 | 2025-09-25 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 168.5 |
| 221f65ea-75e2-3a61-8754-0ddc8c9f2225 | -17.951 | -55.8522 | 2025-09-25 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.6 |
| 835bf29c-9137-3422-85c3-0305dd5a2450 | -2.9291 | -48.3181 | 2025-09-25 03:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| c94f7891-c89d-39d4-b380-bacca2f15217 | -6.4319 | -43.0707 | 2025-09-25 03:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 128.2 |
| bfa4da89-714f-346f-ac2d-5f6ac1dec4cf | -17.9308 | -55.8758 | 2025-09-25 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.3 |
| af7ae974-203d-3a7c-9956-5465ba7d7b94 | -20.9726 | -50.0077 | 2025-09-25 03:10:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.6 |
| ac1f3e42-0447-3148-be1e-e95cd4c6b3a7 | -5.16105 | -42.06068 | 2025-09-25 03:19:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 56417aeb-026a-31cf-ad65-44e3a1bc00b7 | -6.42488 | -43.09313 | 2025-09-25 03:19:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 4715ac06-c32b-3083-86ac-714ecc8741ab | -2.91047 | -40.39064 | 2025-09-25 03:19:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 20a2dbfa-8307-32ca-bf37-92602d8b6180 | -3.79105 | -41.73712 | 2025-09-25 03:19:00 | NPP-375D | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f311849e-9741-30b9-9cf0-592752bf9e50 | -5.95182 | -42.91166 | 2025-09-25 03:19:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| e07c0f2a-66fc-3022-a6ca-e79f8c8ee730 | -2.91918 | -40.39207 | 2025-09-25 03:19:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 190393df-a0b9-3015-b7a1-18309536804d | -2.91703 | -40.3918 | 2025-09-25 03:19:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 9b0d1d8f-b559-34bb-b1d6-9a303a5683b5 | -3.80622 | -41.56959 | 2025-09-25 03:19:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8d1a563d-d6d4-3cef-ae8a-0b5d232285fe | -6.56699 | -42.0661 | 2025-09-25 03:19:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| e19d0917-6b14-3921-988d-001131526146 | -9.05374 | -40.52417 | 2025-09-25 03:19:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ed086355-60ff-305d-8745-dde418293409 | -3.61002 | -38.76419 | 2025-09-25 03:19:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a0d9c06f-6e20-33e8-8a10-427aaf52ab83 | -9.65926 | -40.58422 | 2025-09-25 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 2c0fc842-1b72-393f-b01c-ebbba881176a | -3.79223 | -41.73045 | 2025-09-25 03:19:00 | NPP-375D | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ee332bce-7486-3434-969b-0775c0c005d4 | -5.08624 | -37.60601 | 2025-09-25 03:19:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8902359d-cb18-3d8b-983d-4db058dbaacf | -6.5673 | -41.36688 | 2025-09-25 03:19:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9f191e14-2926-32e4-a200-f2ea73af965f | -6.42699 | -43.08265 | 2025-09-25 03:19:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| e152ca4b-ed26-3ad5-bb55-309dc0fe1168 | -3.78289 | -41.74242 | 2025-09-25 03:19:00 | NPP-375D | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 612542eb-fd4f-3ccc-a59d-2abf252d918f | -8.85141 | -42.47813 | 2025-09-25 03:19:00 | NPP-375D | CORONEL JOSÉ DIAS | PIAUÍ | Brasil | 2202851 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |


[Clique aqui para ver as próximas entradas](README7.md)
