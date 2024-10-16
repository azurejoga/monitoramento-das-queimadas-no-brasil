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
| 1a8f7bb3-4f58-300b-84d9-d9cb44323445 | -12.0619 | -46.7134 | 2024-10-16 01:26:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 08b32868-e7b9-3951-a991-3003f0d14b25 | -12.0623 | -46.6908 | 2024-10-16 01:26:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 49eff7a8-3c46-3f62-914a-a159e49985db | -12.4925 | -47.2818 | 2024-10-16 01:26:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 984a4adb-150e-312a-9df1-9199cdb2ecdc | -12.3795 | -63.7103 | 2024-10-16 01:26:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 68.2 |
| ab80c24b-35ab-31dc-bf4e-26018c534fae | -12.3983 | -63.7093 | 2024-10-16 01:26:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 4e99ddde-281a-363e-8855-e7400de1be79 | -12.4979 | -63.034 | 2024-10-16 01:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 54a8c826-ba88-39bf-ba52-ca32af0edd43 | -12.4981 | -63.0148 | 2024-10-16 01:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| cf6f0360-e76f-356e-bdbd-7fbcbce6c19a | -12.5168 | -63.0329 | 2024-10-16 01:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| e2aec3a4-e86a-3f78-9715-5855ae58817b | -12.517 | -63.0137 | 2024-10-16 01:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.6 |
| bb7040b9-5948-36a3-8083-735c9a183e4d | -12.7821 | -62.9601 | 2024-10-16 01:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 8fdd0b43-62b9-38dd-8330-0836a87144df | -12.7822 | -62.9409 | 2024-10-16 01:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 235.7 |
| 5960f707-3651-313f-8151-d31f63f2c233 | -12.7824 | -62.9217 | 2024-10-16 01:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 83.1 |
| aef7399a-5885-3321-9e81-469f43e11625 | -12.8012 | -62.9398 | 2024-10-16 01:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 4e9f2d1b-0dc5-388a-8120-49d5be473310 | -17.2639 | -42.6527 | 2024-10-16 01:26:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 4e016591-f36a-375b-8d46-f06c8a192bf8 | -17.3041 | -42.643 | 2024-10-16 01:26:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 7cb5ef24-bfe9-3793-bab0-8c2af87dfa36 | -17.0066 | -58.2934 | 2024-10-16 01:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 504c8e05-5b4f-39fa-b62e-7c729ad70d85 | -17.553 | -42.3096 | 2024-10-16 01:26:43 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 67.2 |
| aa4fa2b5-80e2-3424-abd6-78799a380092 | -17.2081 | -56.6946 | 2024-10-16 01:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.2 |
| 63f45020-1d49-3171-839e-cb913ecfcd78 | -17.2177 | -57.3102 | 2024-10-16 01:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.6 |
| 12a7cea3-7a70-31b4-a061-b2b5bf919107 | -17.2373 | -57.3079 | 2024-10-16 01:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.2 |
| cd851662-c1b2-3770-9e3d-87f8e0f0e8db | -18.2544 | -56.5821 | 2024-10-16 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 244.0 |
| c52df598-b409-3b99-af38-556e9d42756f | -18.2548 | -56.5613 | 2024-10-16 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.1 |
| 94381680-3163-30db-b562-ae82164ad8cf | -18.2739 | -56.6003 | 2024-10-16 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.8 |
| 0805cb80-3c69-3ed7-aa78-f20a3010e404 | -18.2742 | -56.5795 | 2024-10-16 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 421.3 |
| 2e63ba50-d859-3ddf-88af-3b3432dc7066 | -18.2746 | -56.5587 | 2024-10-16 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 154.6 |
| 73b1cd09-5379-354b-a8e3-22127bf5789c | -19.6987 | -46.7849 | 2024-10-16 01:26:55 | GOES-16 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 180b5706-16a8-38ea-accf-9bef810a2ae5 | -19.719 | -46.7802 | 2024-10-16 01:26:55 | GOES-16 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 0b906dce-ab96-3f72-89d1-489b0e5ac37f | -19.5615 | -56.968 | 2024-10-16 01:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 143.3 |
| 3d9b8b7f-b863-30d0-9114-cdf559394434 | -19.5619 | -56.9471 | 2024-10-16 01:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.0 |
| f724e5df-8177-3960-9421-14fc72aa6ce9 | -19.5812 | -56.9862 | 2024-10-16 01:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 215.3 |
| 7737e631-da31-3702-aa61-9228d147078d | -19.5816 | -56.9653 | 2024-10-16 01:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 211.5 |
| f4450d5b-dde0-3212-871e-8da7e4efa575 | -19.6013 | -56.9834 | 2024-10-16 01:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 199.1 |
| b5063906-01d4-3d24-9b5a-44a947879427 | -19.6016 | -56.9625 | 2024-10-16 01:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.7 |
| bedba1c9-82b0-3726-9480-38fdb7cf9f69 | -23.0965 | -51.6189 | 2024-10-16 01:32:01 | METOP-C | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e10b6723-4e8d-3c56-9a5a-c678645aa111 | -23.084101 | -51.610901 | 2024-10-16 01:32:01 | METOP-C | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 63cd3b95-efb7-3226-8d6a-bb061303a855 | -23.086901 | -51.621799 | 2024-10-16 01:32:01 | METOP-C | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 59030a0a-8755-3776-a051-e84232ed36c5 | -23.0896 | -51.632599 | 2024-10-16 01:32:01 | METOP-C | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a2b42a79-07f6-3787-b081-24e773d1975a | -23.6642 | -55.231201 | 2024-10-16 01:32:06 | METOP-C | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 61ac50a0-bed6-3d6a-aca3-f134e5bd701b | -23.665899 | -55.238998 | 2024-10-16 01:32:06 | METOP-C | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 72398a66-f23b-30ce-8d06-869857e60bfb | -20.8552 | -49.851501 | 2024-10-16 01:32:30 | METOP-C | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 090c3fd4-cc32-3682-81bc-5c616e6db0f5 | -20.8591 | -49.866402 | 2024-10-16 01:32:30 | METOP-C | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f93e6453-d221-3f89-8a51-15b32ce239eb | -20.8631 | -49.881199 | 2024-10-16 01:32:30 | METOP-C | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2c65e0fe-217d-3fed-967b-f3f8d279a09e | -20.8494 | -49.869301 | 2024-10-16 01:32:30 | METOP-C | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2db5ae46-2a47-3fc2-a578-57f09def83ba | -21.0009 | -55.248199 | 2024-10-16 01:32:49 | METOP-C | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e5a53770-071c-3332-aa43-a63d7a351c97 | -20.9893 | -55.242901 | 2024-10-16 01:32:49 | METOP-C | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4bbfaa64-e577-32de-8065-923d1ddebd30 | -20.9972 | -55.232399 | 2024-10-16 01:32:49 | METOP-C | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2193a4f9-b846-3f81-bca6-432bc2615031 | -20.9991 | -55.240299 | 2024-10-16 01:32:49 | METOP-C | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 03049080-82c2-36d5-a768-31e0c6ef4baf | -19.5909 | -56.528099 | 2024-10-16 01:33:09 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5c08ac78-090c-3ea0-8324-dbf3297b43ca | -19.5849 | -56.957001 | 2024-10-16 01:33:10 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a959a5e2-d454-3cf9-9a1f-f2236f71d205 | -19.586599 | -56.964298 | 2024-10-16 01:33:10 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| da544fcf-4f6d-324d-b043-53cb0be4a193 | -19.5882 | -56.9716 | 2024-10-16 01:33:10 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1fb75307-f09d-3ba4-8def-9097941bc7ee | -19.589899 | -56.978901 | 2024-10-16 01:33:10 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a3930700-5fbd-3819-a032-5a367c5a0543 | -19.591499 | -56.986198 | 2024-10-16 01:33:10 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7cbbc6e0-1701-3077-bf0a-071fad4c71e4 | -19.593201 | -56.993599 | 2024-10-16 01:33:10 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6c5be999-f6fc-3bdb-b9d9-a536089db85f | -19.581699 | -56.988602 | 2024-10-16 01:33:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8c50c6be-f321-3988-9fe3-e057609c82df | -19.5637 | -56.954498 | 2024-10-16 01:33:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4928f827-10f0-3074-9dcb-d943abd55925 | -19.5653 | -56.9618 | 2024-10-16 01:33:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1ca17784-38b5-3999-b631-d1ac2b153439 | -19.566999 | -56.9692 | 2024-10-16 01:33:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 52211c09-c8b3-3ffe-ab7a-f5d221c32d60 | -19.554001 | -56.957001 | 2024-10-16 01:33:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2c58756c-2052-334a-8c3c-47d7b19e53a3 | -19.555599 | -56.964298 | 2024-10-16 01:33:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ac97f343-8dc7-32e3-bb4c-b037f1c064cd | -19.544201 | -56.9594 | 2024-10-16 01:33:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 32b31385-8427-372e-b180-6751cc47b1d8 | -19.545799 | -56.966702 | 2024-10-16 01:33:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b1102e2b-90b5-3fa8-a350-d5fbee2dca02 | -19.5735 | -56.952099 | 2024-10-16 01:33:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4fa3524e-95f7-352f-8880-8942a601c825 | -19.5751 | -56.9594 | 2024-10-16 01:33:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8a7b692e-5857-30d5-ac74-5cf3b124c095 | -19.576799 | -56.966702 | 2024-10-16 01:33:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c3981c71-aac7-3265-97f7-05162770a8d4 | -19.5784 | -56.973999 | 2024-10-16 01:33:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7b5249d6-1c79-3bb1-890c-1f6192df8c15 | -19.580099 | -56.9813 | 2024-10-16 01:33:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| faf87e9b-cc88-3775-8cda-93d6bc34bde0 | -18.635401 | -57.137501 | 2024-10-16 01:33:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 18c5c22e-5ee0-3fe7-a389-0b1d7fe27ef9 | -18.636999 | -57.144699 | 2024-10-16 01:33:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d1757c79-cf33-3481-adae-939d7e554edb | -18.6273 | -57.147099 | 2024-10-16 01:33:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bdd34584-a969-3580-8317-ffc3c8d3ba80 | -18.246201 | -56.383801 | 2024-10-16 01:33:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6e87ff5f-067d-3b4e-b7c4-d5d7f1fbdc92 | -18.2479 | -56.3913 | 2024-10-16 01:33:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d9d05e94-c17e-310a-8a6c-46cb9f4942f5 | -18.2514 | -56.4063 | 2024-10-16 01:33:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d48cff12-5944-30b2-a5d5-9816e6ae5e79 | -18.253099 | -56.413799 | 2024-10-16 01:33:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 047767d8-906c-3a8f-a017-fedd453301cf | -18.2549 | -56.421398 | 2024-10-16 01:33:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f482f0c9-99eb-3fbe-a4fa-727482a41ec6 | -18.232901 | -56.371201 | 2024-10-16 01:33:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e4dafbb0-3a41-3e4b-98e8-0b649653baa7 | -18.2346 | -56.378799 | 2024-10-16 01:33:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bcbe13c5-8109-3c63-985e-b061722b7ca3 | -18.236401 | -56.386299 | 2024-10-16 01:33:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f1e209bc-4fbe-309a-ab98-5cf5e807f956 | -18.266399 | -56.560799 | 2024-10-16 01:33:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b4155590-0e2e-3c0f-8b4f-a04daf5a9f86 | -18.268101 | -56.568298 | 2024-10-16 01:33:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 82a26f50-722e-3547-a9e0-047eb78e569d | -18.2698 | -56.575699 | 2024-10-16 01:33:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4750dddb-a800-3d0a-bfad-62a0f1dd4086 | -18.2715 | -56.583199 | 2024-10-16 01:33:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e2c5c62c-fc70-3573-a4e8-53a717e72de8 | -18.273199 | -56.590599 | 2024-10-16 01:33:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 675741e3-ee96-3e73-a1ef-fdbc1bbbce9e | -18.215099 | -56.383701 | 2024-10-16 01:33:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1101fb40-d315-31d2-9695-6db5b3997985 | -18.256599 | -56.563301 | 2024-10-16 01:33:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6c0c31e7-7175-37bb-a412-bf821bb74c25 | -18.258301 | -56.570702 | 2024-10-16 01:33:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ab69fcab-bff6-3c7a-8d48-ac2ccc47a58b | -18.26 | -56.578201 | 2024-10-16 01:33:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f56d0f6f-f9ff-3b32-890c-189650570d4f | -18.2617 | -56.585602 | 2024-10-16 01:33:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e5d9419d-73b6-30f1-9e4a-a78ad50eaa15 | -18.263399 | -56.592999 | 2024-10-16 01:33:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a6417b14-fe3e-39a2-93f3-032b7dddc0b9 | -18.252001 | -56.588001 | 2024-10-16 01:33:31 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f64824a1-56ee-38d3-9097-96d4cb427bc7 | -18.2537 | -56.595402 | 2024-10-16 01:33:31 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 609e2787-09ef-31b0-acca-5fbad7db415e | -18.0599 | -56.382702 | 2024-10-16 01:33:33 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7f0a9193-cd89-3a7d-9084-bcf705eedde1 | -18.061701 | -56.390202 | 2024-10-16 01:33:33 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ad10c662-4d71-34b3-867f-7f99dad60dda | -18.0634 | -56.397701 | 2024-10-16 01:33:33 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 11532bbd-dfa4-3e21-8e9c-83bc0a32cb8f | -18.159401 | -56.8144 | 2024-10-16 01:33:33 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9e6bf430-ac41-39b9-b255-3192f85aea04 | -18.1513 | -56.8242 | 2024-10-16 01:33:33 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bcaa6235-bbc9-3b80-b86a-15ff1d3b7e3b | -17.9659 | -57.278599 | 2024-10-16 01:33:38 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 431240ac-717b-3021-805c-08e9cfd2031c | -17.9676 | -57.2859 | 2024-10-16 01:33:38 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0cf6d537-5e1d-3596-b781-b2705819da16 | -17.966101 | -57.416 | 2024-10-16 01:33:38 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8172d2ea-63a5-3e1a-b169-191c05dfba1f | -17.9678 | -57.423302 | 2024-10-16 01:33:38 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README17.md)
