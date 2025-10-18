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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 229c576e-3963-3564-8504-63426d7cd616 | 1.76913 | -55.9337 | 2025-10-18 06:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 65be8a14-0a56-35ae-b6a1-d870dc7c2cf7 | 1.75452 | -55.99343 | 2025-10-18 06:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 5faa1a12-e2ca-3ef9-a443-36d708bf1d4a | 1.76462 | -55.993 | 2025-10-18 06:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1251f506-be49-34cb-b229-d01dda67beb7 | 1.7557 | -56.00043 | 2025-10-18 06:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f63e0e2b-c126-32c9-8201-c2e03b230d1b | 1.7665 | -55.93235 | 2025-10-18 06:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1be2c001-51de-3e28-b1b7-5d347c36aeff | 1.75809 | -55.97066 | 2025-10-18 06:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5db80982-256c-3684-994a-b3812942703d | 1.7664 | -55.9805 | 2025-10-18 06:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| c939e6e0-c3ef-309e-917d-44eaa77d7339 | -6.5411 | -68.4034 | 2025-10-18 06:10:00 | NPP-375D | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80834ffb-cfe8-3de7-80c7-cb53d3151aba | -7.49433 | -63.51628 | 2025-10-18 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4013c055-f0ab-3859-94b7-7c996b796e79 | -6.54126 | -68.40521 | 2025-10-18 06:10:00 | NPP-375D | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c60a3569-caf2-3377-87cf-a525d0fc57fc | -1.42177 | -60.40388 | 2025-10-18 06:10:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74a3ba0a-6777-3681-8329-8e40a2520990 | -7.49475 | -63.51328 | 2025-10-18 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 272204e8-a989-3d33-a382-bb77523ef335 | -5.74573 | -63.15238 | 2025-10-18 06:10:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e2b339a-a6e1-3ff9-8d65-d04fc95eb45c | -7.68148 | -61.04531 | 2025-10-18 06:10:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8860d7e-a22e-322e-9e10-288e604e8f05 | -5.74531 | -63.15537 | 2025-10-18 06:10:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22aae85c-b55e-3f8e-8707-778e0da9a96c | -1.42239 | -60.39992 | 2025-10-18 06:10:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0f8ad2d-b84c-3f88-a827-239d1c8b9995 | -1.42241 | -60.40154 | 2025-10-18 06:10:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a9cddff3-fe9a-37b9-92ac-a5585e56bdcd | -7.68752 | -61.04619 | 2025-10-18 06:10:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f103f5b2-5b37-3e0b-b889-9ec3bbb21a39 | -6.5376 | -68.40466 | 2025-10-18 06:10:00 | NPP-375D | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c97c95b-8294-3e1b-b3f0-ceaad66421d3 | -9.71658 | -63.23219 | 2025-10-18 06:12:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66123cd3-db32-38bd-a05a-e2009530caa5 | -9.89953 | -64.17315 | 2025-10-18 06:12:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81a4c83c-7a80-3773-84c6-7b48296be37e | -9.76558 | -65.09018 | 2025-10-18 06:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0c387cc-79a9-3046-b8f4-80369a09545d | -9.89141 | -64.98927 | 2025-10-18 06:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ad3246d-c803-3894-896e-9b35c763ddbc | -8.9478 | -65.93353 | 2025-10-18 06:12:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b02a9e1d-5846-312e-a247-1b802418f54c | -10.69374 | -63.47466 | 2025-10-18 06:12:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 262d8cb1-73d9-3297-b2fc-5c9a7130888d | -10.68838 | -63.47391 | 2025-10-18 06:12:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37fb5bd0-0625-330e-a528-c46ddf08433c | -9.89447 | -64.17245 | 2025-10-18 06:12:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50803945-d7ea-329c-bf04-2dbddd5e3114 | -12.0743 | -63.69134 | 2025-10-18 06:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc558e5d-ec7b-3117-a427-c31f9479bc04 | -9.53425 | -62.96193 | 2025-10-18 06:12:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60806bea-8477-35e3-915f-8cc07496980a | -9.62265 | -67.2143 | 2025-10-18 06:12:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b453558d-6b27-307a-a60d-0388ab06043d | -8.57957 | -63.37069 | 2025-10-18 06:12:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 340bbc78-0562-3c96-93a9-640b8f412f7b | -9.29813 | -64.22635 | 2025-10-18 06:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97bc2cc3-544c-3ca4-92f6-44a2fa68d183 | -9.53471 | -62.95842 | 2025-10-18 06:12:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85b1f12d-9c0a-35e2-944c-0ba8f084e723 | 1.7481 | -55.9807 | 2025-10-18 06:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| eb7ad619-fc45-304f-9721-24352f1ab204 | 1.76817 | -55.91754 | 2025-10-18 06:20:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 36e78a2f-dc5d-3fb5-9e8e-b6fe94853327 | 1.75431 | -55.98636 | 2025-10-18 06:20:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| c3c20641-28ed-3e06-b5e8-bebb5c9ceb21 | 1.76607 | -55.98475 | 2025-10-18 06:20:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| e371eadb-a78e-3e48-b426-c5ec1937112f | 1.77063 | -55.93422 | 2025-10-18 06:20:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 6d249830-f066-32ec-a772-eb449a3f699a | 1.76368 | -55.96839 | 2025-10-18 06:20:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 2a875d4e-0f2c-3a50-838f-885e5f9694e2 | -6.36674 | -45.7742 | 2025-10-18 06:22:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| bde1c68b-3dc2-3649-9d5f-2478d261941b | -3.13646 | -50.24128 | 2025-10-18 06:22:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b0842460-5c0b-3438-8d33-8cc18ee9ceb7 | -8.10987 | -45.4293 | 2025-10-18 06:22:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 3d18c458-be1e-3973-95e3-b0fc8a61e0e4 | -5.25591 | -47.23513 | 2025-10-18 06:22:00 | AQUA_M-M | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c2211c1c-da3c-305d-801f-874339b0ec03 | -3.75647 | -49.0387 | 2025-10-18 06:22:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 259ce5a5-5fe9-32ed-a9c8-cf19d0eeb364 | -4.43729 | -45.4354 | 2025-10-18 06:22:00 | AQUA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 153.2 |
| ad28049e-60c8-31e9-b592-050adf78d13a | -6.3695 | -45.75417 | 2025-10-18 06:22:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| abd6291e-89ae-33b6-ade1-72c04222ae9a | -5.89132 | -44.71347 | 2025-10-18 06:22:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 57f54e63-3946-33a9-9223-ad1975288631 | -3.81594 | -51.69673 | 2025-10-18 06:22:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7e65c4fb-9abb-30aa-b344-32e4680ece7a | -2.94966 | -49.33373 | 2025-10-18 06:22:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 518c3b07-5b4c-344a-8a7f-4a753fa93646 | -2.86863 | -50.73697 | 2025-10-18 06:22:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 842dadea-cda6-3ca5-9e5b-025c56dba561 | -2.85976 | -50.73567 | 2025-10-18 06:22:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7823e2b8-a52b-3cf2-b4a2-67620e06cb14 | -2.91184 | -52.72197 | 2025-10-18 06:22:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 00044321-2bd2-3591-9d83-c63f64dc237c | -5.88751 | -44.70546 | 2025-10-18 06:22:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 46b8c929-ce5e-34a2-9880-27ba4e270c27 | -4.44024 | -45.41503 | 2025-10-18 06:22:00 | AQUA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 172.5 |
| 5c9e6709-25c7-36b6-b6a2-9406e6360b28 | -3.80389 | -51.64369 | 2025-10-18 06:22:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 07f7da24-f83d-36f4-86f0-8e2afca93d08 | -7.34008 | -43.84964 | 2025-10-18 06:22:00 | AQUA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 1a40f20a-f527-3796-b622-91d55ccc7103 | -3.14411 | -50.25183 | 2025-10-18 06:22:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 75944e1a-de14-3d76-81e1-2fc3bc2d01ae | -3.14548 | -50.2426 | 2025-10-18 06:22:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| befd58e8-5292-30e2-9a22-8275c41021f1 | -2.86996 | -50.72803 | 2025-10-18 06:22:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 94ba9932-daab-3271-97a9-0dd73359d3ab | -8.10286 | -45.42317 | 2025-10-18 06:22:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| d9acff33-a47b-3d8d-81ec-d162fde6225e | -4.4393 | -45.42026 | 2025-10-18 06:22:00 | AQUA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 252.8 |
| 229d68dd-dc55-3e7c-b623-c89a989b32a8 | -5.0097 | -46.01198 | 2025-10-18 06:22:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 1689f28e-1180-3077-b32c-b33caf507308 | -5.25487 | -50.90393 | 2025-10-18 06:22:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a6493b49-b6c3-3259-ba1c-75fadb415068 | -4.43651 | -45.44067 | 2025-10-18 06:22:00 | AQUA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 60.4 |
| eda3b923-3d17-3b2a-b0aa-816509cb40c7 | -5.011 | -46.01956 | 2025-10-18 06:22:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 31.2 |
| ac7243a5-278b-3006-821b-0cf1bf030c25 | -2.8713 | -50.71911 | 2025-10-18 06:22:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b298aba0-8104-3810-beaf-0c10b05292a5 | -12.61123 | -52.80596 | 2025-10-18 06:25:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| d0cd2030-fc26-3935-8e23-17cd145ce41d | -8.82456 | -49.68481 | 2025-10-18 06:25:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5cb6b6fc-c6e6-3190-8714-4ec55a500ae8 | -10.49643 | -43.42767 | 2025-10-18 06:25:00 | AQUA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 91a4a3df-fea2-347d-b671-9a2a3c94042c | -12.72149 | -50.86148 | 2025-10-18 06:25:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| aa6228c7-0d6b-3ffb-9a67-a3655c02cba6 | -10.47973 | -43.42561 | 2025-10-18 06:25:00 | AQUA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 24efbf79-6097-3f60-9e3e-8185e54728e0 | -11.20952 | -47.82567 | 2025-10-18 06:25:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 381292e4-89d4-37e4-93c9-f917caa45173 | -10.24287 | -44.02501 | 2025-10-18 06:25:00 | AQUA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| aff69f9d-ef6b-3696-9894-7d410ac80b98 | -12.60989 | -52.81514 | 2025-10-18 06:25:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c4f889f8-aa0f-35ca-a8d2-eb777a99da8a | -12.59564 | -52.85046 | 2025-10-18 06:25:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e6656733-b2db-3425-8f64-eeaf87f9191a | -18.37724 | -55.43476 | 2025-10-18 06:27:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| c8a8ae53-61f6-38e8-b1b3-a5d8c6aa8394 | -18.38042 | -55.47324 | 2025-10-18 06:27:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 560c1b8a-718b-372a-9a0e-98696d537d3a | -18.37583 | -55.44402 | 2025-10-18 06:27:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 788c5ced-3025-32e1-9618-4d7d2497edcb | 1.7663 | -56.0001 | 2025-10-18 07:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 1ab919c0-afc5-3d35-98b7-b8e98c9d8453 | 1.7663 | -56.0001 | 2025-10-18 07:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| bf21e74d-12e4-389d-b6c0-2c90b60057aa | 1.748 | -56.0004 | 2025-10-18 07:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 806129c2-12bf-3138-a06d-6db5603032a5 | 1.7664 | -55.9805 | 2025-10-18 07:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 12c77628-2c1d-37b6-b356-aa972d13cb17 | -13.1928 | -42.9511 | 2025-10-18 10:30:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 95.0 |
| 80501523-291f-3421-87e3-b6596f28ec3f | -13.8573 | -43.6193 | 2025-10-18 11:10:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 7d2febd7-b34d-3737-9b4b-9ca0e1183273 | -12.487 | -45.4664 | 2025-10-18 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 175.9 |
| 125ef920-7541-301a-a34c-81e4d8cd60c2 | -13.8573 | -43.6193 | 2025-10-18 11:20:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| b22b6dc9-c43d-37c8-89eb-2b343e3795df | -12.4678 | -45.4694 | 2025-10-18 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 51f5c442-8f7e-3cdc-a711-1d6899bd9b16 | -13.8573 | -43.6193 | 2025-10-18 11:30:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| c945c0be-73e5-3899-8ee5-2197d3749898 | -12.487 | -45.4664 | 2025-10-18 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 9c5135ea-855a-300f-9dfb-ba7b61bd06d7 | -4.87087 | -38.61138 | 2025-10-18 11:36:00 | TERRA_M-M | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 04ab5b24-b3bf-3e64-a630-6ba0901cfe74 | -3.84901 | -41.56581 | 2025-10-18 11:36:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 31.4 |
| e9205dbe-7a2a-336a-aa46-70d0d276f1ae | -4.87223 | -38.60204 | 2025-10-18 11:36:00 | TERRA_M-M | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| de2a6174-69dc-34ee-8b95-f512cf883417 | -7.17322 | -42.6512 | 2025-10-18 11:38:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 31.8 |
| c5089a9a-de82-3a49-9c5c-553eff092df4 | -8.56153 | -44.57281 | 2025-10-18 11:38:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 6c795659-2ed7-3b0b-b23e-66177e385f14 | -8.00729 | -38.86942 | 2025-10-18 11:38:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 9.8 |
| f9027b1d-952c-3bec-b42d-e40e26005ba0 | -7.1715 | -42.65773 | 2025-10-18 11:38:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 56.2 |
| 24faaceb-f633-356d-b32e-27df03adf2ae | -8.23228 | -43.99353 | 2025-10-18 11:38:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 107e7cb2-4454-35ec-9677-34e290fd806a | -8.35342 | -43.91404 | 2025-10-18 11:38:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 7f66df6c-3115-31ea-95bf-0cd36843012d | -8.84076 | -44.39442 | 2025-10-18 11:38:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 629aa07e-e5cb-3b8a-a601-9eb038c238a6 | -7.98462 | -44.15377 | 2025-10-18 11:38:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 33.6 |


[Clique aqui para ver as próximas entradas](README89.md)
