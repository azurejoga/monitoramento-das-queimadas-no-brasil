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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6051e611-d965-3e8a-ac76-36f61d50f723 | -6.1299 | -47.2884 | 2024-10-02 02:35:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 44b50410-0f7e-3c81-b47a-6381a72a7fed | -6.1301 | -47.2664 | 2024-10-02 02:35:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 258fd75f-90e1-311d-b101-b85829fed3d2 | -8.4642 | -62.7313 | 2024-10-02 02:35:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 3c7007be-c8a6-3600-94c3-fed441200f68 | -8.4643 | -62.7124 | 2024-10-02 02:35:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 86eae932-d7d4-314f-aa33-08e06d5b74ff | -9.9367 | -64.9179 | 2024-10-02 02:36:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 90.9 |
| df83b9eb-2e0a-393a-ac12-2c1a3d55cf32 | -9.9368 | -64.8991 | 2024-10-02 02:36:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 719df750-f759-3ccc-811b-c07fcdf5e1f9 | -9.9553 | -64.9172 | 2024-10-02 02:36:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 33c3b4d5-afae-36cb-af94-224769102947 | -9.9554 | -64.8984 | 2024-10-02 02:36:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| d6058f7c-9609-3ac2-ba96-50b787ec6a0c | -11.6554 | -65.018 | 2024-10-02 02:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 41fc6537-038c-367e-b1c6-c68cdca5a356 | -11.6555 | -64.9991 | 2024-10-02 02:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 6bc90f60-4d81-3fe7-b34c-f94cbbfff988 | -11.6742 | -65.0172 | 2024-10-02 02:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 8ce6acf3-6e1b-350e-9e7f-6dbfd94cc2ed | -11.6743 | -64.9983 | 2024-10-02 02:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 8ae3c75e-db68-335f-9454-6ee6fcff86c4 | -12.2946 | -47.6446 | 2024-10-02 02:36:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 34436bb1-4678-3423-a582-39607188c6e2 | -12.6484 | -63.1214 | 2024-10-02 02:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 99.1 |
| c29c1cc6-a651-3cff-90c5-802695ec610d | -12.6486 | -63.1022 | 2024-10-02 02:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.1 |
| a58fdbb0-81ea-34e6-af6a-8df02acb956e | -12.7054 | -63.0798 | 2024-10-02 02:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| f72b3551-b61b-33c8-9458-8e159073508c | -12.8423 | -62.5526 | 2024-10-02 02:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 7b05f976-684f-3104-b154-f9237c398853 | -12.8424 | -62.5333 | 2024-10-02 02:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 139.5 |
| c0d0aa53-3166-3cdf-92b3-762ea4072b5d | -12.8426 | -62.514 | 2024-10-02 02:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 615a1f13-5b68-3a02-b41a-da271bf3e4e1 | -12.8612 | -62.5514 | 2024-10-02 02:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 2bb0c97d-7dca-3e14-84d2-9009f3849bce | -12.8614 | -62.5321 | 2024-10-02 02:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 1a76d5e2-6753-3b2a-8e54-82a71f5abc4b | -12.8615 | -62.5129 | 2024-10-02 02:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 9322948b-7bcb-33f8-b6be-4e749b3470d4 | -13.0015 | -51.1694 | 2024-10-02 02:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 06d5ffe3-c990-3b0f-a8bc-ad3362a8e23e | -13.0019 | -51.148 | 2024-10-02 02:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 96297962-d749-337d-a739-0d95822709a5 | -13.198 | -48.6267 | 2024-10-02 02:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 156612a4-daa9-3d47-bde9-3b36642f1d60 | -12.9546 | -62.6999 | 2024-10-02 02:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| fca57ca3-c694-334a-aa0e-8eb5f8b82d8d | -12.9548 | -62.6806 | 2024-10-02 02:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| a7bd3be1-5635-3e63-88a5-5d278c819391 | -14.5699 | -44.8351 | 2024-10-02 02:36:27 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 4a8d07c5-1c7f-3dd5-aa09-fc56b1287305 | -15.8933 | -57.1754 | 2024-10-02 02:36:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 9ca6da80-5617-3437-a13c-3f5cb3fe6744 | -16.6124 | -57.2375 | 2024-10-02 02:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.8 |
| 1fd39cb7-138b-3c13-8d8f-5f021547eb50 | -16.6127 | -57.217 | 2024-10-02 02:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 180.5 |
| a3164f3d-e585-3fb0-80a4-0c6d812f15f4 | -16.6319 | -57.2352 | 2024-10-02 02:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 129.0 |
| 28ed7839-18d5-311e-b760-08a524086c27 | -16.6322 | -57.2147 | 2024-10-02 02:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 222.0 |
| c72ab677-dc57-323d-bf1b-f53cf4157baa | -16.6518 | -57.2125 | 2024-10-02 02:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.1 |
| 50fb84e4-62de-31c0-be3e-8452b7acf8b1 | -16.6717 | -57.1897 | 2024-10-02 02:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.7 |
| f4629d85-ac68-3e31-887b-c868903f8903 | -16.6868 | -57.4741 | 2024-10-02 02:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.5 |
| 06066657-8841-31a6-a023-c98a592a862a | -16.6884 | -57.3718 | 2024-10-02 02:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.0 |
| 25985724-6037-3eb0-b2b4-8098a40f82ef | -16.6887 | -57.3513 | 2024-10-02 02:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.2 |
| 8063b5db-4601-3a4e-98d8-d8f0ef6eef9c | -16.6909 | -57.208 | 2024-10-02 02:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.2 |
| 0c1dcef8-6ae4-3841-975a-0eda37de2fb7 | -16.6912 | -57.1875 | 2024-10-02 02:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 159.8 |
| 0de2f32e-1d24-3663-8ed2-94ea3e15e98a | -16.6916 | -57.167 | 2024-10-02 02:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.5 |
| a0611b65-36d8-326e-89c1-20ca6e58d8dc | -16.7063 | -57.4718 | 2024-10-02 02:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.6 |
| bc65f350-aba5-3105-8e52-ca8d2ef949f7 | -16.7108 | -57.1852 | 2024-10-02 02:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.3 |
| bb37bf2b-bd78-3153-b150-297cff504862 | -16.7265 | -57.4287 | 2024-10-02 02:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.9 |
| 7d6521c0-6ef1-3023-9525-f1ce0e021b84 | -16.7452 | -57.4878 | 2024-10-02 02:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.3 |
| c7f16db8-ad23-313f-ba77-1836d1245157 | -16.7461 | -57.4265 | 2024-10-02 02:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.2 |
| f4fbe2ba-8c17-3c1a-a831-d1a0b06c7abe | -16.8096 | -55.9177 | 2024-10-02 02:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 486978ec-01c1-3922-aa86-c1036b2deadb | -16.8292 | -55.9152 | 2024-10-02 02:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 119.9 |
| f9200e3f-63d8-3ce5-8a0f-9f59aeea685a | -16.8295 | -55.8945 | 2024-10-02 02:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 118.0 |
| af18b402-2028-3c2f-8947-3bd1d422f1c7 | -16.8491 | -55.892 | 2024-10-02 02:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 83.9 |
| 9caab19f-3b65-34db-a5f2-7bce755d3ce0 | -16.8695 | -55.848 | 2024-10-02 02:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 90.5 |
| 68e4d4d8-b47d-37b5-80db-f875721c81a0 | -16.8698 | -55.8272 | 2024-10-02 02:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 66.5 |
| ceef2694-74d8-3181-902c-bcdbc681b899 | -16.8891 | -55.8455 | 2024-10-02 02:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| ac5f7f3b-ec99-3023-a26e-d0b6b781e497 | -17.0895 | -56.7503 | 2024-10-02 02:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.9 |
| 8ebd4eb3-9119-35c8-9d35-7426bd4dacca | -17.1577 | -56.1844 | 2024-10-02 02:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| 594d4962-d8b1-3fbe-beef-a67b23b99f2c | -17.1581 | -56.1637 | 2024-10-02 02:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.1 |
| ad65f15d-b15a-36b9-8c95-8f75e9067f7d | -21.3456 | -55.6841 | 2024-10-02 02:37:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 104.8 |
| fc48cdf1-938a-390a-a36a-246cbf6d2d09 | -21.3656 | -55.7022 | 2024-10-02 02:37:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 280ca09a-76d7-380f-a6bc-23dd6cdaca56 | -21.3661 | -55.6807 | 2024-10-02 02:37:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 463af3a3-feda-3429-8750-fac2f5ca5f91 | -22.677 | -43.7014 | 2024-10-02 02:37:09 | GOES-16 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 86.1 |
| f21bf31d-eed4-3bd7-b616-f7545a549e64 | -22.9006 | -45.1029 | 2024-10-02 02:37:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.6 |
| d1d005a9-e256-33fb-a3b1-0bd80b6d654e | -22.9014 | -45.0779 | 2024-10-02 02:37:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.7 |
| 7dc52e0a-6fd2-38ec-82b1-e33daa82007b | -23.175 | -49.5943 | 2024-10-02 02:37:13 | GOES-16 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 96.8 |
| 4e15c92f-f9fe-3597-822f-ef8c12ec6b97 | -3.128 | -49.4235 | 2024-10-02 02:45:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| ef0285aa-f0a7-36e4-a25d-19f6322c4d2f | -3.1465 | -49.4229 | 2024-10-02 02:45:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 96eecb0e-0928-3a04-b7fb-27c8052e6530 | -3.2136 | -46.7843 | 2024-10-02 02:45:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| f30fe3d3-6215-3673-865f-56a1229bf674 | -5.9786 | -45.3847 | 2024-10-02 02:45:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 1ac33e8f-c569-3a29-96b5-89adafcdebf1 | -6.1114 | -47.2677 | 2024-10-02 02:45:40 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 5d4da57d-faf9-3df6-8656-60e66fa09168 | -6.1301 | -47.2664 | 2024-10-02 02:45:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 3095405a-3092-3e42-b042-95e490403c64 | -8.4642 | -62.7313 | 2024-10-02 02:45:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| a68d6244-5a56-3b0c-9d58-0e18905b71d9 | -8.4643 | -62.7124 | 2024-10-02 02:45:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.4 |
| dc9b6baf-3157-3c0d-8323-ee868f299715 | -9.9367 | -64.9179 | 2024-10-02 02:46:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 09462e6d-a8a9-3d2b-b3eb-ee7c2e821287 | -9.9553 | -64.9172 | 2024-10-02 02:46:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 5b489d0a-0f04-3a18-90e9-f5ba315fdd31 | -11.6554 | -65.018 | 2024-10-02 02:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 91a9fdae-953e-3fb3-92f8-694c44781a3c | -11.6742 | -65.0172 | 2024-10-02 02:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 514c1a43-96a1-3a1d-981b-b1f68b882e4f | -11.6743 | -64.9983 | 2024-10-02 02:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 79.6 |
| f954390e-700c-30eb-a140-57d27b83bdbb | -12.1406 | -50.0524 | 2024-10-02 02:46:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| bb8a7bf7-d673-3903-8ccd-3ca86b1c59c4 | -12.2946 | -47.6446 | 2024-10-02 02:46:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| ff223567-655a-3844-95ff-5b4b49a874da | -12.6484 | -63.1214 | 2024-10-02 02:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 84.3 |
| bf0d7b90-464e-394b-9345-1888357cf5df | -12.7054 | -63.0798 | 2024-10-02 02:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 958fd09f-7c3f-3fa5-9445-074c48729f49 | -12.8423 | -62.5526 | 2024-10-02 02:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 81.6 |
| ff2cb5ec-8bc5-3908-91c2-ff45f123c017 | -12.8424 | -62.5333 | 2024-10-02 02:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 23d85e9c-16b0-33a5-beee-5570c5f23d1b | -12.8612 | -62.5514 | 2024-10-02 02:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 92.0 |
| c4f54fc0-30fa-31e4-adc7-6a4e825d2f57 | -12.8614 | -62.5321 | 2024-10-02 02:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 144.4 |
| c4a67550-5e4a-3b1f-b211-8225f76d12df | -12.8803 | -62.531 | 2024-10-02 02:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| cf0f56fd-c18b-368b-83e8-5fc540108713 | -13.2173 | -48.624 | 2024-10-02 02:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 424039bb-9285-389a-90e1-346e0d77145d | -13.055 | -51.4186 | 2024-10-02 02:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 5126a08a-98a7-3577-bc22-2aa4690b59e0 | -13.0553 | -51.3973 | 2024-10-02 02:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| c7a817ed-1802-33c2-a812-c379fce5dfda | -13.0557 | -51.3759 | 2024-10-02 02:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| c309aa20-52df-303e-8c34-94fda5776701 | -13.0742 | -51.4163 | 2024-10-02 02:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| adacb2e0-8b1c-3375-ad45-ffd6e8ff7867 | -13.0745 | -51.3949 | 2024-10-02 02:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| b923f74c-5e7e-36de-bdbe-c508cf920395 | -13.0748 | -51.3736 | 2024-10-02 02:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 380284b5-d338-39f1-b028-81e6a7e3813f | -13.1118 | -51.4542 | 2024-10-02 02:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| b811c88d-1059-3c06-97fc-9db4bf6b2bd4 | -13.1122 | -51.4329 | 2024-10-02 02:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 552de5c3-fb54-3525-8f92-a146aa1dd258 | -13.5965 | -51.1367 | 2024-10-02 02:46:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| c87c8bd9-613d-3b55-b99c-8a01cd94c7eb | -15.8933 | -57.1754 | 2024-10-02 02:46:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 26.6 |
| b5f0cda4-c222-3bc4-8616-88dec0dbd5ed | -16.4337 | -57.4414 | 2024-10-02 02:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.7 |
| c4ee018d-791e-33ed-bae6-e3502a5de29a | -16.4533 | -57.4392 | 2024-10-02 02:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 32.2 |
| b7a9fca8-4bbe-30cc-a2df-6d17070e2a67 | -16.6124 | -57.2375 | 2024-10-02 02:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.1 |
| a0f67418-65cf-376c-a775-a4d4e7766ce4 | -16.6127 | -57.217 | 2024-10-02 02:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 138.3 |


[Clique aqui para ver as próximas entradas](README46.md)
