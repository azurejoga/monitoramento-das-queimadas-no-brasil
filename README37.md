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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16bec1b5-9dd7-37d0-9c57-275b4fa2a331 | -15.65 | -47.2027 | 2024-10-03 01:46:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 36456be1-7f14-3f7a-a873-91df40450381 | -15.6697 | -47.1992 | 2024-10-03 01:46:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 466b8e7f-6545-3156-9dfb-6c85349e4a54 | -15.6702 | -47.1763 | 2024-10-03 01:46:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 6aefb408-f7b8-36f3-967d-c51ab0a825a5 | -23.5292 | -53.298901 | 2024-10-03 01:46:37 | METOP-B | MARIA HELENA | PARANÁ | Brasil | 4114708 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 625ea315-47e8-37f1-80a9-1d3b241b623d | -23.535601 | -53.321301 | 2024-10-03 01:46:37 | METOP-B | MARIA HELENA | PARANÁ | Brasil | 4114708 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7a23f3bf-0810-33e8-bc25-fe894795a5db | -16.7452 | -57.4878 | 2024-10-03 01:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.8 |
| 283e9014-8c84-35dd-a76a-365bb8500234 | -16.7455 | -57.4674 | 2024-10-03 01:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.9 |
| f3e49716-4291-3cf2-93fb-a40a745b4a9a | -16.7594 | -57.8328 | 2024-10-03 01:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.7 |
| 40662154-2234-38c5-bba6-37b4340386e2 | -16.7647 | -57.4856 | 2024-10-03 01:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.6 |
| caeb0572-2c50-3b57-abfa-eca41fbe4ae1 | -16.779 | -57.8306 | 2024-10-03 01:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.3 |
| 1c87e4bd-b840-3a13-b6b8-1f48a3e5b4d1 | -16.7793 | -57.8102 | 2024-10-03 01:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 1f4c6a6a-851c-3911-a9bf-e19c31ccc2ca | -16.8983 | -57.6949 | 2024-10-03 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.5 |
| ee680de8-edd1-3c79-a192-1fe74cae2b79 | -16.9179 | -57.6926 | 2024-10-03 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.4 |
| 00dd2d02-9961-3b2f-a623-91bda54149e9 | -16.9176 | -57.7131 | 2024-10-03 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.1 |
| 730b7181-0dde-3e77-808a-ebd8be383527 | -16.898 | -57.7153 | 2024-10-03 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.6 |
| 615840f8-b445-36bb-b358-d68b89f1fadd | -16.7985 | -57.8284 | 2024-10-03 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 2790dea8-0f81-3fc8-8187-6937188bdcf6 | -17.1967 | -57.3946 | 2024-10-03 01:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.9 |
| ee762b4d-1e5a-3bcf-b398-edd13c78c064 | -17.197 | -57.3741 | 2024-10-03 01:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.6 |
| a8ca29b7-8485-3229-8163-b568da8fd3a2 | -19.0344 | -43.1944 | 2024-10-03 01:46:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.6 |
| 0679a412-d6b8-3da4-8f7c-84553df5c39b | -19.0548 | -43.1891 | 2024-10-03 01:46:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.1 |
| b07b2190-0f01-3490-a4a8-30be9fdc087c | -19.3159 | -42.5976 | 2024-10-03 01:46:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.8 |
| 01e04eb2-b141-3d67-a348-7408c75c1d5e | -19.8803 | -42.1132 | 2024-10-03 01:46:55 | GOES-16 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 113.7 |
| d6dade46-646a-3070-a231-a07b9c3aa43f | -19.8812 | -42.0877 | 2024-10-03 01:46:55 | GOES-16 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.4 |
| 170a9eaa-3800-3e34-9725-fa37becca21b | -19.9009 | -42.1074 | 2024-10-03 01:46:55 | GOES-16 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 89.8 |
| 52a1ce30-fcfb-3906-8bb1-7f17d78cf849 | -19.9018 | -42.0818 | 2024-10-03 01:46:55 | GOES-16 | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.6 |
| cb9d8dba-53b0-354d-9357-7845ee15a201 | -21.3456 | -55.6841 | 2024-10-03 01:47:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 94b7b34a-c27a-356b-8124-7029ccf28249 | -21.346 | -55.6626 | 2024-10-03 01:47:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 81bb855c-8788-3aea-997c-fdc4f6bf049a | -22.0871 | -42.0819 | 2024-10-03 01:47:06 | GOES-16 | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 108.3 |
| fd4bd2cd-89cd-3d0c-8138-8685060df2c8 | -22.4452 | -46.8817 | 2024-10-03 01:47:09 | GOES-16 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 792a4ef5-be4d-3f9d-b28f-2cfd209c1f13 | -22.446 | -46.8576 | 2024-10-03 01:47:09 | GOES-16 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 109.1 |
| e7a05e48-727e-31b8-b6bf-63a068e8f7b8 | -21.3524 | -55.669498 | 2024-10-03 01:47:22 | METOP-B | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9ab3e500-352d-390d-9588-85568cb4b493 | -21.357201 | -55.687 | 2024-10-03 01:47:22 | METOP-B | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f0dba481-1c3a-30b1-9adb-b1f7e580efdd | -21.3619 | -55.7043 | 2024-10-03 01:47:22 | METOP-B | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 72688652-1dc8-34a6-b1bb-7e9414d0af81 | -21.3333 | -55.637501 | 2024-10-03 01:47:22 | METOP-B | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8c82cd11-b257-3cf6-b537-132734e7bcaa | -21.3381 | -55.654999 | 2024-10-03 01:47:22 | METOP-B | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7441332a-c29b-3c0d-9dac-03fd5566d38d | -21.3428 | -55.672501 | 2024-10-03 01:47:22 | METOP-B | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1b8ed8f1-45ef-3243-b5d3-8f5cff94546d | -21.347601 | -55.689899 | 2024-10-03 01:47:22 | METOP-B | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 906afb71-5141-36f5-8330-af5d20ebc4cb | -21.3284 | -55.658001 | 2024-10-03 01:47:22 | METOP-B | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 73e86f4f-08e3-3c38-bb55-2fe2cd473584 | -21.3332 | -55.675499 | 2024-10-03 01:47:22 | METOP-B | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 91848c47-9272-35b5-8b17-da330e9fc9dd | -21.3188 | -55.660999 | 2024-10-03 01:47:23 | METOP-B | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a5f97fdd-6fc0-3628-84d2-59a3b324ee63 | -20.0364 | -55.9235 | 2024-10-03 01:47:44 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f8245c47-4bb5-3e25-804c-703b87e39743 | -20.041201 | -55.9412 | 2024-10-03 01:47:44 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d0428020-69a0-357d-bc64-e41e95e4dabf | -17.1733 | -57.383301 | 2024-10-03 01:48:36 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 10ae443a-0439-37de-8048-9defc7c8a800 | -16.9118 | -57.6926 | 2024-10-03 01:48:42 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 95e70f0c-5a93-3a6a-bea9-51589aa0cc54 | -16.8981 | -57.68 | 2024-10-03 01:48:42 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 123d1c9a-0f89-31f1-bb76-2ddc10f48ba7 | -16.9021 | -57.695301 | 2024-10-03 01:48:42 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3ffc8f9b-0c7f-3297-97f5-028124c0c63f | -16.888399 | -57.682701 | 2024-10-03 01:48:42 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 81772878-e327-3051-9433-08948bc7efbd | -16.892401 | -57.698002 | 2024-10-03 01:48:42 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f173ec95-b961-3361-8277-1819803117fd | -16.878799 | -57.685398 | 2024-10-03 01:48:42 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fed8c9c6-aed8-3775-bb2e-46e61de207ba | -16.751101 | -57.434799 | 2024-10-03 01:48:43 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4bb0caef-068e-34f6-8704-d3b7ef500ef4 | -16.755301 | -57.450802 | 2024-10-03 01:48:43 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 206623ed-eeaa-3041-9c58-a2db079e8db3 | -16.759501 | -57.466801 | 2024-10-03 01:48:43 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 51b070bd-9e31-3b4d-8f77-0999f3cba5e8 | -16.7498 | -57.469601 | 2024-10-03 01:48:44 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2040046f-35e6-3d08-81d0-a779714696fc | -16.722099 | -57.4431 | 2024-10-03 01:48:44 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0d1b03ce-96f5-3bda-ba3d-1bd1c2d1a077 | -16.7125 | -57.445801 | 2024-10-03 01:48:44 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e4ae7f07-4ac6-3193-8fdb-188fc239bb93 | -16.7572 | -57.736198 | 2024-10-03 01:48:45 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1eb1681c-a004-38cb-9f2c-274c08258fe0 | -16.777 | -57.812401 | 2024-10-03 01:48:45 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b5671877-7dd3-316a-923a-90acc287dbfa | -16.780899 | -57.827499 | 2024-10-03 01:48:45 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9424d051-0e00-3965-93e3-c963869d7583 | -16.7673 | -57.815102 | 2024-10-03 01:48:45 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 40e92add-bf5c-32a7-bf7b-01f8aa1625fc | -16.7712 | -57.8302 | 2024-10-03 01:48:45 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d109abf0-63b3-3a14-9aef-eefaa76b2fbb | -16.7537 | -57.802601 | 2024-10-03 01:48:45 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8bd51a1f-469c-34cd-919f-213bdaa5b892 | -16.757601 | -57.817799 | 2024-10-03 01:48:45 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4be4e421-cb91-3943-a76a-3861bcd08a66 | -16.590099 | -58.2127 | 2024-10-03 01:48:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2e43d1da-c9c7-3b1c-bda1-482c26a718cd | -16.5805 | -58.215401 | 2024-10-03 01:48:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 55249442-4369-3bcb-829e-d7f616744f00 | -16.5842 | -58.229698 | 2024-10-03 01:48:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3c2ba877-4be8-3b7d-b443-ab01cf6d958b | -16.567101 | -58.203701 | 2024-10-03 01:48:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dbef6d18-8b35-3421-85d2-223945d40c2e | -16.570801 | -58.217999 | 2024-10-03 01:48:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5449bac4-8188-373f-8545-91d9073aba00 | -16.574499 | -58.232399 | 2024-10-03 01:48:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bc4bb065-07c9-3bd5-bb54-7f046b721430 | -16.553699 | -58.191898 | 2024-10-03 01:48:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 40553f57-3957-3bf6-bbb5-8d21f79d4a5c | -16.5574 | -58.206402 | 2024-10-03 01:48:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dd51d947-149d-3d1e-9177-37b2accbfdcd | -16.5611 | -58.220699 | 2024-10-03 01:48:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 19b2943a-8351-364c-858a-a4d2d4744cc1 | -16.544001 | -58.194599 | 2024-10-03 01:48:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dc161fd5-7df1-337b-9715-fb544fcb5d26 | -16.547701 | -58.209099 | 2024-10-03 01:48:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| be7f9065-ac13-337b-b6ca-835523a64fd4 | -16.551399 | -58.2234 | 2024-10-03 01:48:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5a99413d-ab7a-311e-b244-9c8c8d4fecdd | -16.555099 | -58.237801 | 2024-10-03 01:48:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e9120cc0-1c69-3ca0-b9b7-b544ff8ae2ba | -16.538 | -58.2117 | 2024-10-03 01:48:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7e35db15-7156-30b3-ad64-1fd4540affa5 | -16.5417 | -58.226101 | 2024-10-03 01:48:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9556a8d5-7ab3-3c12-b2fd-de35b72f4fb8 | -16.545401 | -58.240501 | 2024-10-03 01:48:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0e9b64ba-f768-3c9e-b635-9b8834130ef0 | -14.3912 | -59.5466 | 2024-10-03 01:49:30 | METOP-B | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0e0e3b5d-b7cd-33e8-84b7-2a418a4eb05c | -13.7181 | -60.671001 | 2024-10-03 01:49:45 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c0e4af3d-f5db-37bc-b968-334fb4c7b45b | -13.7111 | -60.684601 | 2024-10-03 01:49:46 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b476991-179f-3977-bcf6-77b3d465ebe7 | -13.7138 | -60.695702 | 2024-10-03 01:49:46 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 138d473a-e2dc-38f2-a4c5-7a4d4013fb25 | -13.4112 | -61.921398 | 2024-10-03 01:49:55 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a409a709-227f-374a-ae59-81a0c843e3b4 | -12.943 | -60.085999 | 2024-10-03 01:49:56 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e5475972-77b3-34a0-b38c-6e763e90d689 | -12.9461 | -60.0984 | 2024-10-03 01:49:56 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e47eaa46-4e75-34d0-83b2-c90ff767948d | -12.9333 | -60.088501 | 2024-10-03 01:49:56 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bca5011a-28c0-37b4-99ce-4175173146ca | -12.9364 | -60.100899 | 2024-10-03 01:49:56 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fac25711-3802-3956-9065-8e817a12e8f2 | -11.9795 | -57.1875 | 2024-10-03 01:49:59 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b032391-2456-3bc0-806a-1ae66f89bf7a | -11.9698 | -57.190102 | 2024-10-03 01:49:59 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4e76c78f-420b-32c5-9fec-efc3fb26bd69 | -12.9802 | -62.627399 | 2024-10-03 01:50:05 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f1e957a6-9cbf-34b8-b935-83ac9779b9ae | -12.9822 | -62.6362 | 2024-10-03 01:50:05 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 12ceb183-7c3d-3561-95ea-43ee4965c307 | -12.9843 | -62.645 | 2024-10-03 01:50:05 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 108f277e-edbb-38e2-85cb-5bdcbda09550 | -12.9704 | -62.629799 | 2024-10-03 01:50:05 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e7939ca4-1263-3976-95a1-c11f9fed37ed | -12.9725 | -62.638599 | 2024-10-03 01:50:05 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2db4a6b0-433f-3ba1-b0cd-8458f23e9bb5 | -12.9752 | -62.6936 | 2024-10-03 01:50:05 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 161cc868-a265-345f-bb6a-ba640eb787b5 | -12.9773 | -62.702301 | 2024-10-03 01:50:05 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ba3dd947-565c-3ce3-8503-894a054413a4 | -12.955 | -62.652199 | 2024-10-03 01:50:05 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2be4e6c8-0d55-38a7-9547-76a9cb7297ec | -12.9571 | -62.660999 | 2024-10-03 01:50:05 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 80a78932-4d54-3cc0-a92f-60f6c5d9e15b | -12.8968 | -62.450199 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6f910c50-cd5c-3e79-b48e-e2a447303282 | -12.8989 | -62.459202 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README38.md)
