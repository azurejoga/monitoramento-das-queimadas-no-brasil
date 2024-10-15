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
| 8acf931e-f3cd-3a92-a038-6c73f73cface | -3.7402 | -49.0186 | 2024-10-15 01:45:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| b8335a8f-cdb7-37a8-9b5d-6d4c6855cfe8 | -3.7403 | -48.9972 | 2024-10-15 01:45:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 239.5 |
| c7f88d56-0f0d-3aa6-9308-726dc6be726c | -3.7404 | -48.9758 | 2024-10-15 01:45:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 295f92d7-bdde-3469-b430-624b6bcf2137 | -5.5732 | -49.3995 | 2024-10-15 01:45:37 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| ad058e4e-524e-3a7f-8a6b-f1f38e05e65f | -10.3711 | -61.1935 | 2024-10-15 01:46:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 167.8 |
| 63f9a51f-2ef5-354c-8489-cc5b11cd0b75 | -10.3713 | -61.1743 | 2024-10-15 01:46:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| c5d986c3-96c6-33d5-ad36-09aacd2cfe8a | -10.822 | -49.256 | 2024-10-15 01:46:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| d047e799-8e45-38be-925d-f2fa5d7e10f0 | -11.6915 | -65.2432 | 2024-10-15 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 4a4684df-aa9d-3737-8261-3294be4c7c25 | -11.6917 | -65.2243 | 2024-10-15 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 71.8 |
| c97d95a0-6022-374c-bfd7-7c49bc39f02b | -12.3983 | -63.7093 | 2024-10-15 01:46:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 24337598-1e44-3a19-bb00-24d3ddede2c9 | -12.4603 | -63.0169 | 2024-10-15 01:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 634fe304-55da-3f22-8fc8-0ee484826e56 | -12.4961 | -63.2641 | 2024-10-15 01:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 429864f8-eb36-3e62-a212-12b09308a9e2 | -12.515 | -63.263 | 2024-10-15 01:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 96.2 |
| c09469e0-a829-3bd4-a151-ff48dccc5230 | -12.9538 | -62.7962 | 2024-10-15 01:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| f1844580-790c-381b-b68b-6675ef2e837a | -12.9728 | -62.7951 | 2024-10-15 01:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 4c9662f9-9469-3edd-b946-76f3fab5eda3 | -13.1285 | -62.3227 | 2024-10-15 01:46:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 1cc734db-b6ff-3bbb-ac97-36d2e2181c31 | -13.1287 | -62.3034 | 2024-10-15 01:46:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 51236711-8fbf-3bf1-a427-2e247a9588cb | -13.1473 | -62.3408 | 2024-10-15 01:46:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 2744b975-d3ab-30a3-860a-efc6b80414b5 | -13.1475 | -62.3215 | 2024-10-15 01:46:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 154.0 |
| e12e482f-26a3-3f86-88dd-dcc0be38ee41 | -13.3786 | -61.9582 | 2024-10-15 01:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 8012ceab-6081-332a-bf39-1eee0fbd08ea | -13.9075 | -45.8355 | 2024-10-15 01:46:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| f26e2afc-d301-3900-81c6-70f32b638fc0 | -17.84824 | -57.43209 | 2024-10-15 01:54:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.0 |
| 7ab37a2e-c000-3133-9348-7ff5b3b96cd8 | -17.8536 | -57.404999 | 2024-10-15 01:54:31 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1da1f625-24dd-3b0b-9a29-492fc54d2cfd | -17.856701 | -57.417 | 2024-10-15 01:54:31 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 64dc2e13-f35b-3d80-ba25-adfeb442b568 | -17.843901 | -57.4077 | 2024-10-15 01:54:31 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ba247fd2-8369-337d-a0d8-8b8f09057f94 | -17.847 | -57.419601 | 2024-10-15 01:54:31 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d4380d64-53da-3b92-8a2b-17b683d8458e | -17.85 | -57.431499 | 2024-10-15 01:54:31 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3f996160-e07a-34f7-845d-3a452a4d3412 | -17.8342 | -57.4104 | 2024-10-15 01:54:31 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1bfbb9fd-bc8f-3a8d-8312-1f813cfa8c3c | -17.837299 | -57.422298 | 2024-10-15 01:54:31 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 020eb04e-86bc-3a81-a27e-934c933735f2 | -17.8403 | -57.4342 | 2024-10-15 01:54:31 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2ffd6211-5599-33fa-9c34-64892d97a22f | -17.8246 | -57.413101 | 2024-10-15 01:54:31 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a0f3d5a7-249c-3f04-ac46-5cb91066665f | -17.8276 | -57.424999 | 2024-10-15 01:54:31 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4752991c-0e02-32a0-93bb-bc6597be9058 | 1.0016 | -52.2164 | 2024-10-15 01:55:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 51aa2a4d-3367-3efd-9302-d9ab7171e159 | -3.1099 | -54.2263 | 2024-10-15 01:55:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 8eb08960-12e3-3e0e-81dc-2fe1909398ef | -3.1282 | -54.2459 | 2024-10-15 01:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| e8389181-4bd4-3df4-9820-af5e2e8d6365 | -3.1283 | -54.2259 | 2024-10-15 01:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 6cea8591-cfce-35f7-8ed3-524b6f8ff328 | -13.5122 | -61.744598 | 2024-10-15 01:55:58 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fbdb2154-d235-38bc-a77e-882e1417de61 | -13.5141 | -61.752499 | 2024-10-15 01:55:58 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1399a1db-5d5e-3676-94fe-8a7f88334347 | -13.3635 | -61.335602 | 2024-10-15 01:55:58 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 362c5eaa-bc85-3699-a312-e2df15f48439 | -13.3654 | -61.3438 | 2024-10-15 01:55:58 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 78d7e2d8-b46b-33bd-9431-49ca9cfad971 | -13.3537 | -61.338001 | 2024-10-15 01:55:59 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 47a52111-ea16-3583-9b84-0f86026d5af7 | -13.3556 | -61.346199 | 2024-10-15 01:55:59 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 00fb51b1-0620-3be1-bafe-ebdcd3c011c2 | -15.18045 | -59.70732 | 2024-10-15 01:56:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ffd33e1b-6a6f-3aa3-b9f6-c6bfac438441 | -13.14649 | -62.32442 | 2024-10-15 01:56:00 | TERRA_M-M | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 34.7 |
| ed83728c-8534-3a89-aba5-43327f5d1caf | -13.13892 | -62.33479 | 2024-10-15 01:56:00 | TERRA_M-M | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 22.9 |
| de2d0b22-ac6e-3081-a661-9221e96c6f63 | -13.13764 | -62.32574 | 2024-10-15 01:56:00 | TERRA_M-M | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 70edec1b-294c-3431-80e3-f62b0ad48205 | -12.98308 | -62.74474 | 2024-10-15 01:56:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| acf2769c-7572-32d2-8f4e-55f7a42d07e1 | -12.97292 | -62.80149 | 2024-10-15 01:56:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a436f7af-7f81-3685-bff8-bf857505bdb1 | -12.97167 | -62.79247 | 2024-10-15 01:56:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cdc03321-0cce-3433-ab9e-1a61774ffc5f | -12.97042 | -62.78344 | 2024-10-15 01:56:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e7d6336c-df40-348f-bf11-53a1360dbdca | -12.96283 | -62.79377 | 2024-10-15 01:56:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| f0e8c12b-9d76-3a4a-b12e-f6d95934493e | -12.96157 | -62.78475 | 2024-10-15 01:56:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 415e82b4-c013-386a-8674-b77a3a2c2e97 | -12.86216 | -62.60328 | 2024-10-15 01:56:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| da3b2bb8-2c4c-3d3b-80cc-310ee3d82c7e | -12.82541 | -63.00129 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c37fe4f4-e6b3-3f67-9046-208e3f14e6f7 | -12.82416 | -62.99225 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 033db712-9326-340a-b7f8-e16c3ece64d7 | -12.823 | -62.91869 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e5070244-1d28-3832-aadc-9d4f7c0b59b2 | -12.77483 | -62.3029 | 2024-10-15 01:56:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9d999f5a-c020-3b65-b523-28d3faecf687 | -12.77356 | -62.29385 | 2024-10-15 01:56:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 4c7932da-3d23-36c9-9997-260801b0e1d7 | -12.77228 | -62.2848 | 2024-10-15 01:56:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 12faade1-e434-3a41-8a56-76b8a3257029 | -12.76514 | -62.6972 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5751032d-7652-3467-8536-12f582ab05c2 | -12.7647 | -62.29518 | 2024-10-15 01:56:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 38.8 |
| da572fbb-cb6a-3bf6-af32-1b0b6463c38a | -12.76342 | -62.28613 | 2024-10-15 01:56:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 02d100d5-7b08-3f8b-b5ac-6e6db2c286a7 | -12.75492 | -62.81829 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a7d6f4bd-136c-3adf-8b34-e489da63a9d0 | -12.73236 | -62.86473 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 04ad0235-b48e-32ad-9f12-c82abbb4fedc | -12.72834 | -63.03112 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d640dbce-f36b-3f8e-9ca2-b7a953590bb3 | -12.71069 | -62.24454 | 2024-10-15 01:56:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d970e4d1-7dab-3256-b3c8-6185d232705f | -12.70941 | -62.23548 | 2024-10-15 01:56:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 11.1 |
| d0426ebf-3932-3de2-8099-c4cd589b6707 | -12.70053 | -63.02598 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6794d10d-ef58-35b7-91e2-49cd568c723e | -12.67683 | -63.06294 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6b16361d-2002-3818-8cef-dc024f10e818 | -12.66922 | -63.07327 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0912a062-697a-3713-a12c-3362e095d70e | -12.66037 | -63.07457 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c845f9ed-b77b-3685-9587-bbffc7979287 | -12.5217 | -63.27327 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 88693dba-1757-3c54-93ee-aea3c720c9a6 | -12.52045 | -63.26421 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 13.0 |
| b28901f3-6989-3e15-b270-0ae84e8534ee | -12.51283 | -63.27457 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 38789121-a57c-31a3-9fe1-c7e1aab3ab1d | -12.51158 | -63.2655 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 546f7d56-e3d1-3fc7-800e-1313292471e5 | -12.51033 | -63.25643 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 15af365f-1a29-3ca0-855d-d8ec3a4c70ba | -12.50655 | -63.02057 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 7a06603d-15dd-38f6-bd12-d3c98ccb7678 | -12.5053 | -63.01155 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1fea8647-03fc-3d76-bdd8-1f9a077989a3 | -12.50395 | -63.27586 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8d189e13-d2ff-396f-86e0-73c12830da38 | -12.5027 | -63.26679 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 4419ec30-57f3-3354-b4c0-92b1ac1065a7 | -12.50146 | -63.25772 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 55369e40-3b46-3e7a-adf7-146ee23db022 | -12.4977 | -63.02187 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 036324be-6d5c-329a-ac06-b30ea86335e3 | -12.48701 | -63.95988 | 2024-10-15 01:56:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 372d6c5f-ca1a-3f58-b2c4-5f70e6314301 | -12.48291 | -62.9931 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 40e00280-191c-33ca-8a90-dd583dc1846f | -12.46397 | -62.98668 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 35741039-f9f5-387e-9056-6fab6fb474cb | -12.46272 | -62.97767 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.8 |
| de3214c0-ea03-3462-b7aa-2ab6bc5cfcf5 | -12.46137 | -63.03306 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 49f24ba0-2cb5-3782-ad0f-785e40ab0aac | -12.46012 | -63.02404 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.8 |
| c1c56e66-0ce6-30c7-99d6-766d54002324 | -12.45512 | -62.98798 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d897bd6e-88a1-3cfe-b294-0398564830cb | -12.45252 | -63.03436 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 20.1 |
| dab764ee-496e-332b-905a-f2c98f7d7312 | -12.45127 | -63.02534 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 045a1162-d484-3024-93fd-c2e2af65c4de | -12.45002 | -63.01633 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 89f87d4b-f331-34ba-a796-f34cb6605bca | -12.39806 | -63.71339 | 2024-10-15 01:56:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 311273b1-0324-30e4-b0fc-1f15dd54132b | -12.39037 | -63.72389 | 2024-10-15 01:56:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| b8e35579-1acc-3d98-8dae-f8ea023b7387 | -12.38911 | -63.71467 | 2024-10-15 01:56:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 4f0d183f-87cd-3d5f-b106-d5f54433511a | -12.38143 | -63.72517 | 2024-10-15 01:56:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 6fb93898-abf1-3062-932b-2cdf2223ecfd | -12.37833 | -62.96883 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0d37c76e-72c1-3997-af1d-6fd644484e1f | -12.37708 | -62.95983 | 2024-10-15 01:56:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 3528f720-03b9-3863-a364-acfc4e976e57 | -11.94657 | -65.01803 | 2024-10-15 01:56:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a59c82cd-5312-3375-b0a1-06e2587a2ce7 | -11.69933 | -65.23727 | 2024-10-15 01:56:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README18.md)
