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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 338ce4a0-61dd-30f3-b685-3ab7a1a3d122 | -7.05059 | -59.82376 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e85477e3-93a0-3ebe-b215-69e45d76754c | -5.88255 | -57.75919 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 99fc8842-aa16-33ae-98d2-3f1b38a897d2 | -9.15311 | -59.5081 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 45d3fbd8-1e37-35f7-adcc-5aa25fde4a45 | -7.62642 | -63.48935 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 440af276-bdbb-396b-8e5b-0e080b38a5be | -6.56758 | -60.05709 | 2025-08-23 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01508e7c-c116-3aa8-8c61-e3e51a829a22 | -7.29243 | -59.64522 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c088f35c-0704-3e20-8dd1-05d54f3e3acc | -8.62443 | -63.67159 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32d456a5-503b-3c79-945a-7c0933695f64 | -7.81239 | -63.55983 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1775c04f-0c8b-3b24-b003-0b86340436fd | -9.50692 | -60.50991 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6137e8b6-faa7-3a33-b4cf-ac989287d4ea | -7.72871 | -67.07162 | 2025-08-23 05:42:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fee822f7-e8f1-346d-af7f-960fd472e56d | -9.17296 | -59.62207 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23c5fd50-d5f8-3b4d-8466-63b96db693f6 | -5.75558 | -57.58903 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 2e6f177d-6079-3ae2-8104-94a21d2b23f6 | -5.87232 | -57.76273 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53d4625f-5f9e-3620-b6d1-d4477e2f61d7 | -5.74114 | -57.58679 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 29b570b4-b10e-3b17-9f39-a6ec5793a5f2 | -7.78504 | -61.57381 | 2025-08-23 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5532bbf9-d629-3253-a35f-0c2465cf570d | -9.95109 | -60.19437 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| f501d504-f761-32ad-8f77-c784e80cbe82 | -7.2936 | -59.6372 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90adb156-b6d9-33c6-beae-fba6730eee8d | -9.16694 | -59.59729 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5278ebcc-9e37-3377-96ba-5af3c34fc76c | -5.79649 | -59.21599 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddc93a3d-d8a5-3d15-96c8-92b7628f9a4f | -6.58139 | -59.87534 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 53a8caf9-43ff-3add-852c-0364ac7566d5 | -7.5743 | -63.44341 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6701a83b-183d-3832-8c8d-7f0c63d6716f | -8.89086 | -62.41419 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b124ec79-0615-39b6-bbcf-615422ba0772 | -9.19626 | -59.46014 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7aaa684c-730f-3d02-9864-7a624f6d90c9 | -9.16911 | -59.58622 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55b8c009-57dd-38aa-ae7f-604b3e0f4168 | -9.95968 | -60.19554 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 36.8 |
| b749122d-6ab0-3655-98d1-eb11b703f5ae | -9.51836 | -60.51935 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca66a3f1-f4b5-3df8-9000-1218866aaab8 | -7.9529 | -63.04506 | 2025-08-23 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c7f8b4e-d85a-3a5d-8459-fd6b7faf8fc4 | -8.88768 | -62.43601 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b2ba270-6343-381f-b22a-5dfccf9b74ea | -9.19498 | -59.46903 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52705e43-3bca-32ad-9aa2-b30278b54016 | -11.30718 | -55.14587 | 2025-08-23 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 645b4e83-50ae-31c1-afe0-1fe830eedefc | -8.59443 | -62.62486 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51725fac-13ae-31d1-b999-d463b86ba6bf | -9.19815 | -59.46742 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6b5552d-a47d-3af4-83c9-86b286b6e57a | -7.80549 | -63.55878 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cae114ea-d884-39b4-9dbd-f827741dacd6 | -8.6889 | -62.86411 | 2025-08-23 05:42:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77ec17d0-c0bb-3f13-b8d3-e97ded14f9cb | -9.52601 | -60.55547 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b89165e-c6c1-3e82-b5db-b2f7b6b36151 | -9.2392 | -60.47705 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 330f375e-62bd-3842-8b21-7aa00e43542c | -6.55881 | -60.0595 | 2025-08-23 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fe4016b-b910-31e5-b07e-0211bba9b947 | -8.61554 | -62.63235 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5e78f0e-0888-33ff-9606-0f67b33db81b | -9.16016 | -59.68023 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cf590fc-006f-3313-9eb0-27e78538c246 | -5.79962 | -59.22477 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1fd210e-cd8e-3175-b4cb-ce77c89f6ce3 | -5.7959 | -59.22005 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe40b53f-c90a-33fc-bb1c-7a5b2df7c052 | -8.86611 | -62.4082 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c870dbf-9da4-31d4-9642-f359421d7c12 | -7.31855 | -59.61621 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab513d58-8111-3574-8f81-71f76bc5d9fe | -9.20045 | -59.61559 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df02f79e-9bf4-3d5c-b3f2-65128d57e9de | -9.95265 | -60.1959 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 217feb26-669b-3971-a4db-9fc79b374f23 | -8.67271 | -63.86042 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1dbac7c8-582f-387b-9db8-e8a9a90be04d | -9.42677 | -62.25578 | 2025-08-23 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b375eba2-26a9-3b7b-9b77-50bdd3cba84d | -6.93934 | -59.63914 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f7e0b34-9ae1-3e3a-b151-d5ea3059c9c8 | -11.19561 | -55.03875 | 2025-08-23 05:42:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7083dfc2-3e96-3ffb-8da2-9cac4c4ef112 | -8.68827 | -62.86823 | 2025-08-23 05:42:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 097883c9-cfb4-3d97-970c-62fd5a4e9212 | -9.44051 | -67.65282 | 2025-08-23 05:42:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 257e46fe-7194-3f1d-8a52-a65fc4f15552 | -8.88477 | -62.40437 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fbb12c1-6e51-3ecc-bca0-5e847d74c0e1 | -9.52709 | -60.54786 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3042a6fa-7e22-3aa1-80a0-f86b83e1c51e | -9.20201 | -59.47247 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6816fa3e-f78c-3a90-8974-933e2cfa8e31 | -6.56944 | -59.86963 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 821e5443-7da2-3cc0-802f-7eaea0746d4b | -9.52346 | -60.54343 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 163ee35f-132d-37ba-8b4b-140e70e4a88e | -8.59869 | -62.62118 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8eda72cf-d69f-3833-bd8f-7cdd06c82001 | -9.52546 | -60.55931 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97708bf3-a9b9-339f-b4e5-d001071b3de8 | -9.51407 | -60.54982 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19bdb858-e684-3a7d-a511-fe772fa80d64 | -11.32245 | -55.22462 | 2025-08-23 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9be0a09d-d705-3d22-a6d4-b42493e3a10b | -6.94227 | -59.55796 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28fffaee-0b78-372f-9bfb-479da3a414a0 | -9.93278 | -65.00826 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41d12eeb-e385-34b1-99f8-706ea3cc92ae | -7.72593 | -67.06747 | 2025-08-23 05:42:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20a58a76-8e4d-322f-a481-b02d9d297012 | -8.67565 | -62.87895 | 2025-08-23 05:42:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67c8d615-e08f-3aaf-b6c8-433ce6d96baa | -11.30774 | -55.14122 | 2025-08-23 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f643fa8-5f35-3919-8550-ec7338cf6af3 | -7.31426 | -59.61561 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 108d1c40-d010-30e3-b749-6cda84d33f8f | -9.21845 | -60.7933 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6df9f506-1e29-3334-b6ea-8d36b4179696 | -9.25447 | -59.77868 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5d47022-56de-30ff-adb9-8f34603a0601 | -8.9253 | -60.72251 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d5af5ba-cb0b-30c8-b3df-678454c384c6 | -9.51353 | -60.55362 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8f856d64-b1fa-3e86-80e7-7fc37923e5d9 | -9.13885 | -65.13951 | 2025-08-23 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| da756189-6663-325d-a71d-67850e61a5b1 | -11.18274 | -55.04181 | 2025-08-23 05:42:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59ae4f6d-aa06-388e-a44d-2a22aba74323 | -9.96192 | -60.1791 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 22355294-6573-3a6d-838f-224cf0d44881 | -8.60104 | -62.63018 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fccc8cd-4d7c-321f-856a-46928951b667 | -9.51944 | -60.51169 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b27c4492-1626-3b8a-84a7-4d1c0006084e | -9.51527 | -60.5111 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f4a02dd3-6271-3528-b5b5-d5382447f2da | -9.51729 | -60.52697 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 076e365e-4f2f-354e-be8e-b538468d1ee0 | -9.20922 | -60.79951 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 509d2903-667d-364e-a40c-35b15ec7e61e | -9.15755 | -59.50874 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b769e0b7-b35a-36df-8dc3-45434da959cb | -9.21504 | -60.785 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0b5ed6d-e6b2-33fa-bb6d-07a9bdda30a5 | -11.18888 | -55.04275 | 2025-08-23 05:42:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb3415b3-8c5e-32c2-b308-092ba05d08df | -9.18578 | -59.59126 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36547594-b9bc-3f70-b361-ff0542e37bd1 | -6.13459 | -62.61626 | 2025-08-23 05:42:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4222c8b1-da1c-3c21-bcc4-60a0e8e946c4 | -9.19561 | -59.6506 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e879d2f6-632c-3dda-bee1-7696a7b2e90b | -7.05426 | -59.82814 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0816ff3-2462-3661-96ac-499af6ab6668 | -5.61116 | -60.22713 | 2025-08-23 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcd4c2d0-d10f-31e3-82bd-a8ca37e49aca | -7.73325 | -67.06496 | 2025-08-23 05:42:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 104fbdb1-b891-3a97-878a-840652277077 | -9.17282 | -59.62025 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f60fbc5-2950-36f9-b947-bc159bf9b744 | -9.94272 | -60.17355 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4addca37-fda9-3873-9b92-338c34ec3615 | -9.21792 | -60.79696 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2b6cf64-c679-35f7-a025-67053a34d8c9 | -9.15401 | -59.59725 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dce3334b-a68c-36e5-91e8-49361dd14535 | -7.78814 | -61.57905 | 2025-08-23 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9b61165-f6c3-3867-9459-cd1949b12481 | -11.19116 | -55.02359 | 2025-08-23 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7039483f-8d85-3a91-a8a3-1b5cab53c335 | -6.62778 | -58.54422 | 2025-08-23 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 40562466-c06b-33e0-8d2c-4871ee3c9fcd | -11.19058 | -55.02847 | 2025-08-23 05:42:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 47e4d07e-a775-325a-8f31-edcc4a86f9b1 | -9.09997 | -61.43417 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ff925b6-7b92-33da-8f98-c9b7320f104c | -7.55 | -63.85357 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ded62837-aeba-38b1-93d6-ccc529ff044a | -8.67814 | -62.86246 | 2025-08-23 05:42:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1939caf-cf78-3520-ab01-80e1b37a5093 | -9.52763 | -60.54405 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8ffdebd-5da2-3ad5-a856-151959c8723c | -9.52454 | -60.53581 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README75.md)
