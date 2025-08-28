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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e379169-b052-34a9-aad9-776285644e48 | -7.3431 | -59.658199 | 2025-08-28 01:41:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 77df9359-3d4c-3f1a-a1a5-206cfb0e39bb | -9.7331 | -64.891602 | 2025-08-28 01:41:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b71f185e-170c-3a5d-9dde-573b8a2d2d18 | -9.4061 | -60.550598 | 2025-08-28 01:41:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f029c1f6-5f76-3dbf-a620-d310daa53e5c | -9.5447 | -68.569099 | 2025-08-28 01:41:00 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 746ee0c7-4cbc-3dac-8fa1-3b625039e668 | -9.0169 | -65.691101 | 2025-08-28 01:41:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c6213036-0d71-362d-9d7f-bbbf38eb62cb | -10.798 | -60.7635 | 2025-08-28 01:41:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0b2bab3c-eba0-3c50-a04a-e08f626fc221 | -9.6619 | -64.981499 | 2025-08-28 01:41:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d9475f09-9a63-38f3-8efd-83248c92f2bc | -10.1539 | -64.2435 | 2025-08-28 01:41:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c24f7d25-bb95-3fb6-85a7-241ed2f60c1a | -9.12117 | -65.81172 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 095aeb4f-4cab-3975-b912-fbe22d03346c | -7.37395 | -64.36189 | 2025-08-28 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 64956e12-9715-3a38-92a1-e878cca2b0c5 | -9.55535 | -65.68884 | 2025-08-28 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6db1a1a3-5725-3470-9fcf-1263f742c531 | -7.27605 | -60.30264 | 2025-08-28 01:49:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| d3924abe-4576-3971-aa8d-310a5f12a3f7 | -9.18434 | -60.81765 | 2025-08-28 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 541982e3-63ff-3cbd-889a-5692a6998337 | -8.9567 | -65.95174 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| b14787a8-bf8c-3215-83ea-eed5dbbf198f | -7.62718 | -60.86197 | 2025-08-28 01:49:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 5d615be8-20e6-37ef-b5c1-4545237be263 | -9.80055 | -64.27283 | 2025-08-28 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 5143ef0f-2bd8-3a56-b373-bc08bcabe71e | -10.82279 | -60.77523 | 2025-08-28 01:49:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 37.5 |
| faf7beaa-a5fe-3177-a4a5-7f7d9da8fa69 | -9.16482 | -65.79583 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c312c8bb-d5fd-39a9-aac4-7e0098bd8793 | -8.88366 | -60.75385 | 2025-08-28 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| c8aeb7f1-bdf0-308f-9d41-35dafe986d40 | -9.48874 | -62.39039 | 2025-08-28 01:49:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 0d098879-1047-34b8-af8b-ef117ac67703 | -7.62415 | -60.84185 | 2025-08-28 01:49:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 3ed1122b-a816-39f4-952f-0a7540a31f4b | -8.26176 | -61.46297 | 2025-08-28 01:49:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 54f257a5-a8f1-355c-89bb-3fdefff7c28a | -10.27937 | -64.49437 | 2025-08-28 01:49:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 18.9 |
| bac9f8e8-39e1-3e3f-9041-788d768eaaa6 | -8.94774 | -65.95305 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 54c15bfa-97b6-3092-b9b8-e462e956887a | -10.32035 | -62.62383 | 2025-08-28 01:49:00 | TERRA_M-M | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 32.4 |
| ef4b85f5-99a4-3f03-b66e-867e6193432e | -9.17637 | -60.86332 | 2025-08-28 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| c28e2cb3-3071-3d8c-8fd6-06e4801dcc24 | -9.13758 | -65.28338 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 0b005720-8669-3aa3-a31a-7cbbf5a127b5 | -9.08088 | -65.72294 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d2ac8938-a9e0-36d9-84d5-90ed767f052e | -9.54768 | -65.69945 | 2025-08-28 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 616beb77-74b4-3c25-a242-3f167af5fab1 | -9.80991 | -61.19694 | 2025-08-28 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| e8f8154f-2cdb-36d0-bf6f-1aa3fd39b095 | -7.3586 | -59.66798 | 2025-08-28 01:49:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 7c53cb6e-6e8a-351b-8f4d-b8b1163462be | -9.72936 | -64.91223 | 2025-08-28 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 45599470-525f-384c-b89c-cc1e644b4477 | -9.25451 | -65.90853 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 056803e7-3eca-38b0-9ccf-fd95e93a544e | -9.4099 | -60.59047 | 2025-08-28 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 8e663d3a-08ab-3307-8c23-46a3d3053d55 | -8.94067 | -64.15618 | 2025-08-28 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9077efb4-ff05-3030-b405-6f552332d498 | -7.54398 | -63.84475 | 2025-08-28 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| e15bd129-89e6-35ef-bfc2-3fa56d3cda8d | -6.9264 | -62.94756 | 2025-08-28 01:49:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 8d2a8474-9f2a-34ca-a321-5a09202b1bc6 | -7.35457 | -59.64284 | 2025-08-28 01:49:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| a51aaf2b-e5f8-30ce-a2cb-13bb43a4e5be | -10.4687 | -57.92802 | 2025-08-28 01:49:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 71ce4aae-08ee-384c-acfb-8cd734b8a3c3 | -10.15266 | -64.25483 | 2025-08-28 01:49:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 9af46f2d-75b2-3b87-8f1e-4bc0f15341d3 | -8.96566 | -65.95042 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7aa338ff-1f34-31a8-8e01-e49ab39ddba3 | -9.66705 | -64.98837 | 2025-08-28 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 28ed36f3-1f82-3e10-877f-bd7c7a138126 | -9.08355 | -65.7415 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| a2371d31-765b-3621-a9db-6d684e421993 | -9.15999 | -59.57764 | 2025-08-28 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 4c4b72dc-a959-3ef7-9ce0-ee83b6181b97 | -7.40171 | -62.29062 | 2025-08-28 01:49:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 0b487895-9fce-38eb-a775-45eb9655bcf8 | -10.83783 | -60.79099 | 2025-08-28 01:49:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 606406f5-3909-3c5e-a2f5-2f56034be8cc | -7.35131 | -59.64881 | 2025-08-28 01:49:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| b628e3f7-5b08-3ffd-bbca-3f92eeb26651 | -9.31164 | -57.70935 | 2025-08-28 01:49:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 5b28534f-3b36-3f33-85b3-e36876e5447c | -10.81928 | -60.78173 | 2025-08-28 01:49:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 69bf65d6-e21e-30b4-8711-bd5e0bdd9693 | -7.37556 | -64.37305 | 2025-08-28 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 35.2 |
| a5d6ffdc-f2be-36fa-940f-91626b1b4612 | -7.55415 | -63.8432 | 2025-08-28 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 6dd7ac8f-f1f9-3132-981d-c2c17fde26e0 | -9.1298 | -65.29435 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 8691bd4c-b1e5-38e8-ab0a-6678676f77f6 | -9.09122 | -65.73085 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 97476ceb-3331-30ee-8e26-283328611495 | -8.95035 | -65.97141 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 25.8 |
| d1b9f93e-4ac7-3cfa-b356-9019e15f7bae | -9.12753 | -65.79188 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 6f793a88-0f2d-398b-b9f1-d917cb7ccdaa | -8.65349 | -67.27035 | 2025-08-28 01:49:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7760e702-221e-3aa1-a82a-6df6070ec7af | -9.17794 | -60.85743 | 2025-08-28 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| c9daa86a-b0f4-3368-8ba6-228563fe7e26 | -10.15114 | -64.24428 | 2025-08-28 01:49:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| e78f298c-7d58-34b9-b624-8961d73bdb1d | -8.95931 | -65.97009 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 49cb9447-6977-3830-b747-d246fcd05e74 | -9.18955 | -67.75553 | 2025-08-28 01:49:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c9b06a18-7ed9-3a2a-ab86-a1f3dc7b9e0a | -8.94208 | -64.15012 | 2025-08-28 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 552b9fcc-4833-3369-9dbd-1d1f935c2461 | -9.41306 | -60.52261 | 2025-08-28 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| a87ac819-78d8-3ec2-a9c2-6a217c780ed6 | -9.13521 | -65.78125 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 866eca39-a1db-35b2-858b-166a88f913ae | -9.45816 | -60.30812 | 2025-08-28 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 741139cb-92de-31a3-b988-e35f8d21ffa7 | -9.11191 | -65.74681 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| bc1b6225-ca26-3a3f-a824-9da85c5ff09f | -6.91325 | -62.93509 | 2025-08-28 01:49:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 48ded0b6-e133-375f-88fd-63d475e1cedb | -9.53607 | -62.39095 | 2025-08-28 01:49:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| ee313aeb-258d-363d-a6cd-b2152a8c2d33 | -9.31911 | -57.71518 | 2025-08-28 01:49:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 7940d6c2-e1d7-3314-bae4-a993e079cd87 | -8.61256 | -64.07711 | 2025-08-28 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b1e3d61c-7847-3282-a768-6360005c17c0 | -9.47777 | -62.39213 | 2025-08-28 01:49:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 11.0 |
| ab213589-3af5-3fea-8c3f-4c6da2d9a214 | -10.81063 | -60.7773 | 2025-08-28 01:49:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 102be46a-8f7e-303e-a98a-85b3a2739aa4 | -7.34036 | -59.64516 | 2025-08-28 01:49:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 72be59c8-7da8-3ca6-aead-a155791654d2 | -6.91542 | -62.94923 | 2025-08-28 01:49:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 444c4848-ed68-3683-ab86-edd8ce4bcf2d | -7.56783 | -63.86556 | 2025-08-28 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| e66c5057-f483-35e2-bf92-af35657f82c2 | -9.08989 | -65.72157 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 06cfb546-aa1b-3cb3-8a2c-f175837ee94d | -9.54045 | -68.58147 | 2025-08-28 01:49:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 7.0 |
| af42dcce-b2bb-3867-955d-ed7d28a65ca8 | -9.11805 | -67.70766 | 2025-08-28 01:49:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a99f12d4-c5cc-3d70-84ca-998a4658248d | -9.13257 | -65.76271 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a88e6d8d-7121-3f9d-8aa9-0bcfae64a4ea | -9.1029 | -65.74812 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 55440330-f601-367d-a30d-53acc56be2cc | -9.11721 | -65.78394 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 599.4 |
| d374d551-2f33-355b-bceb-37d26fa193bc | -9.65781 | -64.98976 | 2025-08-28 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 90e753fd-3528-31f4-96d5-ac22e1777b56 | -9.40687 | -60.57095 | 2025-08-28 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 148.5 |
| 44301a2a-083f-3652-a5eb-869d97736ac4 | -10.28548 | -64.49807 | 2025-08-28 01:49:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 202bc84e-238c-31bd-a3ce-ab7f864c641c | -9.53825 | -62.40508 | 2025-08-28 01:49:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 36.2 |
| e3adbe89-37cf-3852-b456-e08af30b7f62 | -8.57096 | -63.93259 | 2025-08-28 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 87dba143-eb56-33c7-b2ea-a66dd7031288 | -10.09856 | -68.48708 | 2025-08-28 01:49:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1fdd477b-3faf-31b3-8b99-a8c1d8f42e3a | -7.34442 | -59.67028 | 2025-08-28 01:49:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| c69571f8-5681-3216-ad21-e2be1b941a26 | -9.15123 | -62.35914 | 2025-08-28 01:49:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 21a0bcb4-d663-3a0f-ac89-6acebc336342 | -9.11853 | -65.79321 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 0cce5e5f-bcd7-3e89-ae06-be974c7c2fef | -8.69785 | -69.66503 | 2025-08-28 01:49:00 | TERRA_M-M | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 5491e463-10b3-3592-9e66-b587e7023448 | -9.18016 | -60.80454 | 2025-08-28 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 969569af-8d65-3781-a207-86494d517ff9 | -7.80172 | -62.34543 | 2025-08-28 01:49:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| a0ec5353-f97f-3aa0-9d6b-795fffb3a044 | -9.72792 | -64.90236 | 2025-08-28 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 9fdccbbc-8cfa-30e7-80df-e2ae52ded83a | -9.22181 | -60.81127 | 2025-08-28 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| d462e872-e3f7-301a-9531-035138de84f3 | -7.3371 | -59.65112 | 2025-08-28 01:49:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 17616284-a49f-3dcb-a1f7-f0d0e118dfd6 | -9.24397 | -64.41154 | 2025-08-28 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 4fdd734e-9987-31c3-a40e-f36192a49e00 | -9.09256 | -65.74014 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 007afdc1-4e5b-36a6-b9f0-7151762749f0 | -8.90395 | -62.47567 | 2025-08-28 01:49:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 721ea6e0-d018-3658-9e8b-9149702bfd67 | -9.13389 | -65.772 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a6bb8f15-ef7a-3c3c-bd5d-e03db8aee9e7 | -9.12841 | -65.28472 | 2025-08-28 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |


[Clique aqui para ver as próximas entradas](README14.md)
