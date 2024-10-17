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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca3c2728-07e5-35e2-93ed-7aaba0f588e7 | -7.8727 | -45.3593 | 2024-10-17 02:55:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 3e599f82-8172-33e3-a292-91355794b7a6 | -10.8452 | -69.461197 | 2024-10-17 02:55:50 | METOP-C | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 0127e63a-7c50-39ad-ba93-83cfba30b649 | -10.8515 | -69.484901 | 2024-10-17 02:55:50 | METOP-C | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c9c5f4e5-b2cb-3c47-84ab-10030036e138 | -9.1552 | -61.9047 | 2024-10-17 02:55:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 75.6 |
| b5aa57f9-ac7f-38f1-a630-f479204995ad | -9.1737 | -61.9039 | 2024-10-17 02:55:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| dcf1d4c4-0221-33a6-aa3a-af2f8b0d5578 | -10.129 | -56.7722 | 2024-10-17 02:56:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 113.1 |
| c1593719-d275-31d2-84d1-0087eff55a74 | -10.1477 | -56.7709 | 2024-10-17 02:56:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 35118698-bce7-3e03-9239-6a1658b93bb6 | -10.1292 | -56.7523 | 2024-10-17 02:56:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 41316ba4-6ec5-3aaf-99c2-82ffd61ad0a1 | -13.4294 | -43.6733 | 2024-10-17 02:56:21 | GOES-16 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| b22f6a1c-f75c-3a47-a5ab-1d56d4782f88 | -17.1667 | -56.8232 | 2024-10-17 02:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.4 |
| a6a41e66-744a-327e-8094-0b8a9173c329 | -17.2177 | -57.3102 | 2024-10-17 02:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.3 |
| 84a2a3f1-8ed6-38ce-8af0-ea1f9e69162a | -17.8641 | -57.4583 | 2024-10-17 02:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.2 |
| 235eeab6-f75a-313d-b989-18b5e0d00616 | -17.8444 | -57.4607 | 2024-10-17 02:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.7 |
| e9ea61bd-64a6-3b86-942b-f199aeb1c34f | -17.8246 | -57.4631 | 2024-10-17 02:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.1 |
| 9625c14a-2394-39dc-bd92-c52b22f25640 | -17.8052 | -57.4449 | 2024-10-17 02:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.5 |
| 4d78a654-8521-3ad2-98a3-570fcc2460cf | -17.8049 | -57.4655 | 2024-10-17 02:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.0 |
| 4563cdd5-3122-395f-9211-12279f9a46c1 | -17.9036 | -57.4534 | 2024-10-17 02:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.9 |
| adaae5a7-903c-3c15-b744-e466ec3c707d | -17.9234 | -57.451 | 2024-10-17 02:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.1 |
| 4a2b0a56-236e-3262-9541-84b0a83ac646 | -2.5962 | -48.2634 | 2024-10-17 03:05:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 6a6fd740-a7d5-3c80-b521-6c774476c7eb | -2.9673 | -48.0147 | 2024-10-17 03:05:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 731f4efb-4fa0-3362-8df9-3fbfd50d09b7 | -2.9674 | -47.9931 | 2024-10-17 03:05:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| d05bb89d-8d15-354b-b1ae-78e54d6fd502 | -3.3526 | -53.2112 | 2024-10-17 03:05:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 95d5e36b-1350-3296-a4b8-f53691898758 | -3.7007 | -45.9223 | 2024-10-17 03:05:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 18313942-c85d-32ff-b345-c0ab4ef23430 | -3.7009 | -45.9 | 2024-10-17 03:05:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 22460be4-4244-3f06-8053-c4a100462eba | -3.9267 | -42.401 | 2024-10-17 03:05:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 99.7 |
| 13d4a716-393f-3432-ae44-7096303dc8f6 | -3.9078 | -42.4256 | 2024-10-17 03:05:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 82.1 |
| 13b235e6-53d9-371d-8686-43818c7f62c2 | -3.908 | -42.402 | 2024-10-17 03:05:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| 9b2b3049-16f4-3dc0-b758-7a82773375ae | -3.9265 | -42.4246 | 2024-10-17 03:05:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 0e790b90-ce0b-33ac-bcfd-3791356de6be | -5.5716 | -44.8927 | 2024-10-17 03:05:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| b086467a-46e8-367d-bb12-34a5b88b5f24 | -5.5718 | -44.87 | 2024-10-17 03:05:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 4942a241-0983-35e7-961e-91d336c54a1d | -7.8727 | -45.3593 | 2024-10-17 03:05:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 5bcbd2cb-aa23-39cd-b66b-7e5ec59c86fb | -9.1552 | -61.9047 | 2024-10-17 03:05:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 9fd62f0a-126f-30ca-b3b4-7f587dd7bae2 | -13.4294 | -43.6733 | 2024-10-17 03:06:21 | GOES-16 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| f2ae9686-ffa9-3950-a650-15bdc2344931 | -17.1667 | -56.8232 | 2024-10-17 03:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 80b5cd0b-9513-3161-a765-c184349bced8 | -17.1671 | -56.8026 | 2024-10-17 03:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.7 |
| ed50e694-be58-352b-a482-62d4697ce458 | -17.2177 | -57.3102 | 2024-10-17 03:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.1 |
| 41c278c0-0472-3059-8738-579b4661f0c4 | -17.8049 | -57.4655 | 2024-10-17 03:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.0 |
| e8be221a-4ae9-3c87-9945-012276ceb8d3 | -17.8052 | -57.4449 | 2024-10-17 03:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.7 |
| 7c90b533-2aeb-32ae-9b7c-b1c5b097c8a4 | -17.8246 | -57.4631 | 2024-10-17 03:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.5 |
| 2ab47226-3a15-3ace-9f4c-720fc249b4f0 | -2.6147 | -48.2629 | 2024-10-17 03:15:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| d1e090b2-4f72-3db7-bb93-04d75e7afa6d | -2.9674 | -47.9931 | 2024-10-17 03:15:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| c7381e39-1737-35ec-99fc-265b57b30254 | -2.9673 | -48.0147 | 2024-10-17 03:15:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 1629d178-7cc4-33b1-84ad-1f3c39b9ca91 | -3.3526 | -53.2112 | 2024-10-17 03:15:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 3535ea05-263e-3041-99b2-323e62c54176 | -3.7009 | -45.9 | 2024-10-17 03:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 7903220a-39ad-3186-8865-deabaf4135f1 | -3.7007 | -45.9223 | 2024-10-17 03:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 97.0 |
| e7b941b6-d66b-3e63-8171-8c76bab45a28 | -3.9078 | -42.4256 | 2024-10-17 03:15:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| 195bc4df-0b1c-350f-92c8-3fde5ce4ec32 | -3.9267 | -42.401 | 2024-10-17 03:15:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 211.1 |
| 7b6a7777-47d2-3222-89d9-3fbb8c98def9 | -3.908 | -42.402 | 2024-10-17 03:15:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 92.2 |
| 310d7fe6-b43f-3e7b-836f-9dc096c5cf64 | -3.9265 | -42.4246 | 2024-10-17 03:15:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 135.3 |
| c2dcc011-6310-38ed-8944-d122329ff708 | -5.5718 | -44.87 | 2024-10-17 03:15:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| f66f3ad4-c2c3-3f19-8163-1ff0fb1834b4 | -5.5716 | -44.8927 | 2024-10-17 03:15:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| a1fdda80-af53-3f2e-9858-8d7ed4281cba | -5.9788 | -45.3621 | 2024-10-17 03:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 21f4adb6-124f-364c-93e1-7cb3c7095397 | -9.1552 | -61.9047 | 2024-10-17 03:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 47ec9e4c-f4cc-33b0-8eb8-059c16e74d58 | -17.1667 | -56.8232 | 2024-10-17 03:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.4 |
| 60a0184d-324b-334d-8c04-20ccb8dd5325 | -17.2177 | -57.3102 | 2024-10-17 03:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.3 |
| 3ac18e06-c7d1-3f44-8bd1-ad80d6de505f | -17.8246 | -57.4631 | 2024-10-17 03:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 9feb5d36-b480-372d-b2f0-8d5a85827df9 | -17.8052 | -57.4449 | 2024-10-17 03:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.1 |
| af88bc2b-3be2-3ca6-8a10-89e924088a03 | -17.8049 | -57.4655 | 2024-10-17 03:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.2 |
| 1f8a2dbe-5c55-35e3-a006-061ffd117f00 | -17.983 | -57.4231 | 2024-10-17 03:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.9 |
| 5e80313a-0bb4-3f06-84ad-739229ff9d16 | -5.65282 | -43.01177 | 2024-10-17 03:23:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 029f88ba-92bd-3691-aeee-c4a7e927665e | -4.47883 | -42.86791 | 2024-10-17 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d8c74f6-b604-352f-9994-ed7fbd2f640c | -4.47105 | -42.87277 | 2024-10-17 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2052fdff-d462-3cab-b67e-f7d54d716993 | -9.35349 | -35.98584 | 2024-10-17 03:23:00 | NOAA-21 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 3cd0ed92-6195-3ae4-830e-b82e1f08663f | -9.35292 | -35.98925 | 2024-10-17 03:23:00 | NOAA-21 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 4673e7ce-c6b8-3e4a-a613-7713a5acf81e | -9.35979 | -35.98804 | 2024-10-17 03:23:00 | NOAA-21 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0e77f3c6-7b0c-333b-879b-4e7f87312e8b | -9.35919 | -35.99148 | 2024-10-17 03:23:00 | NOAA-21 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 92c34995-7fd6-3921-8ed6-7c33aa17f7ab | -9.35859 | -35.99493 | 2024-10-17 03:23:00 | NOAA-21 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c6232a07-cf60-3538-8537-01fd058d1ebd | -9.35581 | -35.98739 | 2024-10-17 03:23:00 | NOAA-21 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5d7c71f8-0bfb-3067-a9bc-22f3573077cb | -9.35521 | -35.99082 | 2024-10-17 03:23:00 | NOAA-21 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c5dd2d79-ecab-3a21-9c1d-af7928f94574 | -9.35462 | -35.99425 | 2024-10-17 03:23:00 | NOAA-21 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6699f96a-a14d-324a-9334-b443698f1660 | -9.74329 | -37.84337 | 2024-10-17 03:23:00 | NOAA-21 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 7.1 |
| f2bc2045-3105-3d13-a841-8cb9a9c3ed1d | -5.2283 | -37.71381 | 2024-10-17 03:23:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 58c8a10a-c8c4-3c71-b20a-d06a80956968 | -5.95226 | -39.67861 | 2024-10-17 03:23:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8a78d21c-059a-3764-8773-e9e42bfd2c30 | -8.506 | -39.9371 | 2024-10-17 03:23:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e1f3a811-d0da-300d-b581-1cf8229633ce | -8.50541 | -39.94034 | 2024-10-17 03:23:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e2b00982-d5dd-37b0-8312-4a1921a43a5b | -9.49858 | -40.36921 | 2024-10-17 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 857fb13f-a894-3798-84e9-f38a120e3686 | -3.74504 | -40.50315 | 2024-10-17 03:23:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dcde8a86-b66d-362e-9c06-081b649b33a3 | -3.74436 | -40.50711 | 2024-10-17 03:23:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4ed70585-23a1-3460-830b-a6f36178b185 | -5.50134 | -40.77895 | 2024-10-17 03:23:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d9107df5-5f8c-30d9-8eb0-138ca9dcd4d6 | -5.50061 | -40.78304 | 2024-10-17 03:23:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 611be3b3-16e8-3895-9ff8-5705db1edb90 | -8.81998 | -41.26929 | 2024-10-17 03:23:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 030ac2c4-56a5-3eb8-a21e-9c2dec3e2cd9 | -8.08794 | -41.07986 | 2024-10-17 03:23:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4bdf89e8-de6a-3450-a58c-6afc44942b18 | -8.08225 | -41.07883 | 2024-10-17 03:23:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c1d27898-1a64-33fe-b4cd-0eb06d5b2754 | -8.81926 | -41.2732 | 2024-10-17 03:23:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6b013c91-58b6-3e35-88e6-5e3b4703015d | -8.70875 | -41.16078 | 2024-10-17 03:23:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 121c437f-b044-3e73-95c1-c7901cfd1417 | -8.70805 | -41.16454 | 2024-10-17 03:23:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 10ea7a12-7a82-3660-8ace-995b3250f6df | -8.70736 | -41.16825 | 2024-10-17 03:23:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a3eb788b-c14f-3ded-927b-40db401cb27c | -8.4862 | -41.22877 | 2024-10-17 03:23:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4fc237f6-e45a-308c-b308-903331cd8d97 | -3.92878 | -42.41155 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 3426a399-7d53-3f53-87da-c7286de239e4 | -3.92839 | -42.42474 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| f42a0828-6a8c-3be9-b5af-5dbdb3b3aee3 | -3.92777 | -42.41726 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| ea1b6ecb-f23c-3c52-bbc6-0d6025538f18 | -3.92742 | -42.43048 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 39b25ca2-13df-3e78-98fa-d76786631962 | -3.92675 | -42.42298 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 569fb06a-33dc-3903-8e0f-45c652cd65a2 | -3.92644 | -42.4362 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3411ef60-f038-39f9-afe2-bf59d44dc465 | -3.92574 | -42.4287 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 59833949-7281-3375-ac96-24081fc71e94 | -3.92568 | -42.4007 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fd65b97d-157c-3207-b013-a2524692cf26 | -3.92473 | -42.4344 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 67d219f8-820f-3410-9060-6132599b0dbe | -3.92471 | -42.40641 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 2b801b5b-dd19-30ca-89dd-a28d2b8ded60 | -3.9242 | -42.39902 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1c613942-26b8-3b98-ba6c-21b09e59a3d2 | -3.92373 | -42.41215 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |


[Clique aqui para ver as próximas entradas](README17.md)
