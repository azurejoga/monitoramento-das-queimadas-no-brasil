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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e612163-be39-388d-8520-d24ada227756 | -11.81293 | -58.19055 | 2026-09-17 01:00:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 0061059f-45a0-3a75-89ac-ca3ced38998b | -9.76398 | -60.46888 | 2026-09-17 01:00:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| d4fae681-0fd6-39d1-a723-c234cc03a456 | -9.62147 | -61.82254 | 2026-09-17 01:00:00 | TERRA_M-M | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6dfa82de-bee3-3adc-890b-acacf4233ed2 | -9.39126 | -60.30099 | 2026-09-17 01:00:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 5bda2081-9e79-320e-b494-16c811149815 | -10.57454 | -57.69279 | 2026-09-17 01:00:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| c89d02c2-b3cc-3e6e-8887-0b75b99940fa | -12.78321 | -62.07608 | 2026-09-17 01:00:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 53743208-9ebc-3d8d-a2c3-ffd77c035410 | -9.38096 | -60.30264 | 2026-09-17 01:00:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d9470fdd-54e8-38be-85de-98058f80a7c4 | -11.81034 | -58.17409 | 2026-09-17 01:00:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 9c4891f4-66f6-3400-9bef-33c9d157541f | -9.40886 | -60.34921 | 2026-09-17 01:00:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 0d337cda-3f2f-3570-8258-3ff705734ee6 | -10.57673 | -57.68546 | 2026-09-17 01:00:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f31297e7-59a9-3427-8ea7-2d963391e0ac | -9.59729 | -60.5192 | 2026-09-17 01:00:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 75504a0e-ac47-3f6d-b98b-43a12ce150ac | -10.87597 | -61.39569 | 2026-09-17 01:00:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 763f9212-087e-396a-bb25-f695336c2954 | -9.75384 | -60.47039 | 2026-09-17 01:00:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e56c9455-e4e5-3af1-935a-cbe36d6bb027 | -10.40126 | -58.31265 | 2026-09-17 01:00:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| c0dbca83-f218-34d7-aebe-8bdccca31f65 | -9.44202 | -60.37605 | 2026-09-17 01:00:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f0ce1415-c83e-34e4-9661-20573d98775b | -10.82952 | -54.10762 | 2026-09-17 01:00:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 171.9 |
| 91cf7681-8d74-32ca-9f6a-5a67e55560e9 | -10.14524 | -61.18055 | 2026-09-17 01:00:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8ea2529d-5ac2-383f-9aff-38861027ee91 | -10.82106 | -65.02198 | 2026-09-17 01:00:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 31554635-ab03-345d-857f-10e45ec8f219 | -9.77411 | -60.46734 | 2026-09-17 01:00:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5d9ff2dc-0c26-31c5-a5a6-fa31b6f1190b | -10.6003 | -64.95761 | 2026-09-17 01:00:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 17.5 |
| a272a632-7d3d-3f2e-9dd0-5910286499d4 | -10.69927 | -54.17353 | 2026-09-17 01:00:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| da0c6cf1-928e-3506-beff-c30030e4c153 | -10.73834 | -61.5849 | 2026-09-17 01:00:00 | TERRA_M-M | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a6476663-c628-32a6-9a4e-5222ec6f1009 | -10.83906 | -54.11108 | 2026-09-17 01:00:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 169.1 |
| d847712c-7feb-34b1-8b27-86c6886ed4ad | -10.3925 | -58.30251 | 2026-09-17 01:00:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 4307eaa8-a531-34ff-a2e1-596b79828cc2 | -9.44387 | -60.38832 | 2026-09-17 01:00:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 55e7737e-3d8b-3ecf-bca9-bea0e5d619f1 | -8.7532 | -66.537697 | 2026-09-17 01:00:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 27c27368-8268-3550-9417-4a32050c01f2 | -9.1046 | -60.941502 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 34393847-1358-3297-8778-6824bc8e0838 | -4.5003 | -54.938702 | 2026-09-17 01:00:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ad5eeff-4407-300b-9fca-5e0ddb088a27 | -6.9237 | -63.0121 | 2026-09-17 01:00:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb57c759-f2c4-3d90-9210-bd7cfe8bdc46 | -9.0948 | -60.943699 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd2a8edf-adfd-323d-a203-960010a162b3 | -13.3731 | -57.018101 | 2026-09-17 01:00:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 524b93e3-e9b8-3487-a96f-141a6a8a2ccf | -9.0228 | -60.989899 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5bb39098-6fa7-3d28-b1fc-7cf2c2822a9a | -6.8139 | -59.1465 | 2026-09-17 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 42d5558a-ed12-3c06-930d-5cb34837ee67 | -7.0058 | -62.964802 | 2026-09-17 01:00:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ced6107-4539-3e7b-8fa4-bd611fe65d1b | -3.4799 | -54.7005 | 2026-09-17 01:00:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb2bdff3-675c-3b9b-9161-bbb4daf7f119 | -2.6942 | -57.598801 | 2026-09-17 01:00:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 21ed9360-7057-3860-8266-2707784c6044 | -6.8159 | -59.1549 | 2026-09-17 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 90038b75-202e-3727-a711-b565307128e9 | -1.1307 | -54.140701 | 2026-09-17 01:00:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78de11cc-fbf2-340a-ad83-ce76efc1fd53 | -13.6623 | -60.539398 | 2026-09-17 01:00:00 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cfe14253-9b2c-3f09-ae66-cefd37de0e38 | -6.935 | -63.0168 | 2026-09-17 01:00:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fcb93042-b0b6-35b8-8c29-025ddd2e1d50 | -9.1124 | -65.918404 | 2026-09-17 01:00:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a060da48-4769-39f5-97fb-7cc6cd877f66 | -3.4712 | -54.664001 | 2026-09-17 01:00:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01897d88-3d17-3c74-aad1-b1b7d593461b | -6.6807 | -58.8405 | 2026-09-17 01:00:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 861b4f10-b706-33ab-a5e9-31cc5a1e7eb8 | -9.5378 | -62.361599 | 2026-09-17 01:00:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a3a59920-58b5-3ecf-877c-ff4af57c343a | -9.7897 | -59.789902 | 2026-09-17 01:00:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e2063b39-6ff7-3379-83fa-31a6e9dbd6fb | -6.6786 | -58.831699 | 2026-09-17 01:00:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c1a6c615-2cb4-387d-a8de-8e78f75316f1 | -2.8935 | -54.1278 | 2026-09-17 01:00:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 728cb14a-6637-342e-a59a-ce88d43f3418 | -9.0371 | -63.351398 | 2026-09-17 01:00:00 | METOP-B | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9b462836-941e-38b1-96df-8972979a342e | -6.7885 | -59.1703 | 2026-09-17 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 50d0a9ee-4fb4-34ae-91ca-71a62dea7fdb | -13.3904 | -57.004002 | 2026-09-17 01:00:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f0bd5b09-f931-39fb-b76b-b4c072fbaeb9 | -8.6434 | -66.550797 | 2026-09-17 01:00:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7b229102-1047-3a1b-8a9f-639d9e6147d6 | -2.8984 | -54.148201 | 2026-09-17 01:00:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 437d90e8-07eb-33d2-8e6e-70c1b759438c | -8.1506 | -64.041496 | 2026-09-17 01:00:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b2e2bcfe-83af-388c-b0f0-8540be80b94d | -3.4756 | -54.682301 | 2026-09-17 01:00:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 769789ab-428f-3d63-a205-3da290262c85 | -9.3868 | -60.280701 | 2026-09-17 01:00:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80e77c28-2124-3a86-8003-bc6c14ba7398 | -11.8025 | -58.149799 | 2026-09-17 01:00:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a3dab0fc-3108-354b-a8aa-82ee0a5e4439 | -3.8044 | -58.879902 | 2026-09-17 01:00:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1b9f1d45-5071-3784-a213-d7ecab4361e2 | -9.4037 | -62.684101 | 2026-09-17 01:00:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 75ca9ed5-c06e-3dc5-ab45-fbd38de0c72e | -6.7094 | -58.787201 | 2026-09-17 01:00:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d2153079-4d5f-37d8-9869-d7e3d2da5aff | -6.9335 | -63.009899 | 2026-09-17 01:00:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0e92f32e-908b-3e48-8fc3-2cc77090fbf7 | 2.7242 | -60.285301 | 2026-09-17 01:00:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2b790386-d488-349e-b4a4-248fed05aef2 | -10.7413 | -61.571999 | 2026-09-17 01:00:00 | METOP-B | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 23f87b83-1ffb-30a1-8ca9-299fd4c21955 | -8.475 | -57.6124 | 2026-09-17 01:00:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4038aa58-e1dc-3584-8f9e-eaae9f45a43b | -6.7865 | -59.1618 | 2026-09-17 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4843536e-f3df-333c-b493-f2bef784f0e8 | -11.8065 | -58.166599 | 2026-09-17 01:00:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 503526b1-1a38-39bf-b196-8555d3795500 | -9.1026 | -61.023399 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3b2c86a-6dfb-3255-b1c2-35e969562052 | -12.486 | -50.778702 | 2026-09-17 01:00:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e0787241-11ee-36d6-a380-98e0c594f39e | -10.1455 | -61.1675 | 2026-09-17 01:00:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 974f3a71-221d-35e2-a711-f3326066d022 | -6.8977 | -59.019199 | 2026-09-17 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ac7c277-138f-367c-8407-9209cf28c768 | -9.2848 | -60.600899 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f31a2587-4e52-3390-8b73-f63eb8879424 | -9.098 | -60.957802 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50bf1481-01fc-310c-80c3-cae61d68c406 | -9.446 | -60.358799 | 2026-09-17 01:00:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 28ca2a01-663c-381c-8cf5-ad7b5473a5ca | -4.5043 | -54.955601 | 2026-09-17 01:00:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9eb4b446-397c-302b-a5dd-084b2ea42ab2 | -9.0848 | -60.990501 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e4c86fa3-6079-3e86-ab90-a7901026423f | -9.5916 | -60.499802 | 2026-09-17 01:00:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb58ebca-66a1-300c-8829-a82dabf2e1b1 | -10.6857 | -54.149899 | 2026-09-17 01:00:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74a70883-fa22-3595-9ca8-6c07863735ba | -9.093 | -60.981201 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fe53cd5d-6bad-3d90-b9fa-685b87795878 | -8.4797 | -57.632 | 2026-09-17 01:00:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b035133-37de-33af-8d37-8c850ed86e57 | -9.1046 | -65.929604 | 2026-09-17 01:00:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 120c6751-4eb4-3bf2-a7a0-97cb37cd464d | -12.4636 | -50.733501 | 2026-09-17 01:00:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ef0efcda-7bd5-3cb6-9baa-2b707bcb7586 | -6.7409 | -58.7892 | 2026-09-17 01:00:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8ab02d3-a073-327e-8a64-fa0a93d9b88b | -9.0994 | -61.0093 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62b17b62-88ae-3790-8b5b-652532c868da | -9.103 | -60.934399 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 94ab8928-45fd-3698-9756-177415f61e1c | -9.7647 | -60.444698 | 2026-09-17 01:00:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c08e48e-ddc3-3fc1-86b6-c67a9acb0a8b | -10.3886 | -58.284199 | 2026-09-17 01:00:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45a11bf8-bc3a-3079-b5f2-fb949de3c401 | -12.1084 | -57.174702 | 2026-09-17 01:00:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 06769236-86f5-3f67-aec7-a0d13d8cb973 | -5.1466 | -55.923199 | 2026-09-17 01:00:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44e5abae-e11f-3fa3-a794-62128c447a4d | -7.9691 | -62.026001 | 2026-09-17 01:00:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0f27889f-210a-33f2-84c9-fc2803fcbfac | -9.0914 | -60.974098 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8aa8f446-ef4f-3896-9c8d-52aaa5f2d99e | -8.4848 | -57.6101 | 2026-09-17 01:00:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e273a48d-0ef0-3e83-90d8-d5257fb27f8f | -8.4918 | -57.6395 | 2026-09-17 01:00:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba2e0299-5beb-3d13-a5fb-e8d15368a076 | -9.1686 | -60.815102 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d5951acf-d054-31aa-846c-d78a22ac572d | -6.9221 | -63.005199 | 2026-09-17 01:00:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b7c62ab8-b0d2-3327-a105-d294698fd192 | -1.1404 | -54.138401 | 2026-09-17 01:00:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66b7edc0-3ea4-3334-8657-7b0e7d432df6 | -13.6607 | -60.532299 | 2026-09-17 01:00:00 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab811899-ac15-374e-a376-6fd10755ee82 | -9.4083 | -60.329399 | 2026-09-17 01:00:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a3ebb74a-6047-3e7f-a8f7-cf016a0fb650 | -9.0898 | -60.967098 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b79315d-627d-3ce9-bc23-bbe67c0a143f | -4.4842 | -55.472 | 2026-09-17 01:00:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad8d8a1b-7892-3279-9337-b7979878f611 | -3.1329 | -59.003601 | 2026-09-17 01:00:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ab9edb37-0fde-3afe-94ff-3a9ac10d9655 | -10.3906 | -58.292801 | 2026-09-17 01:00:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
