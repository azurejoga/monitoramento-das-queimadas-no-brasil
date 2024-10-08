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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbd8d5a6-a67b-3b60-ae39-80004f372a02 | -10.62446 | -55.91418 | 2024-10-08 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| dc731319-e5c7-3989-9809-b071a780e2f2 | -10.62394 | -55.91803 | 2024-10-08 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 903146fd-d569-3d5d-b617-e0e16a011e38 | -15.87521 | -57.48166 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5dc834da-14d9-3f8b-8c9d-99ca8d6e2840 | -10.62303 | -55.91032 | 2024-10-08 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 57a999e2-1353-318f-acad-30be7778dd1d | -10.62248 | -55.91416 | 2024-10-08 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fd57b46e-3457-323a-99ab-391906e84dc8 | -10.62193 | -55.91801 | 2024-10-08 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79fac116-8be9-3678-b710-fa0c155410c1 | -12.09539 | -56.88419 | 2024-10-08 05:23:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a891a09f-3db9-36e2-a9c3-b49e7fea86a9 | -11.47278 | -56.76373 | 2024-10-08 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a05ffd8-7733-3d8e-86f8-d6e2aac7a65a | -11.47488 | -56.76481 | 2024-10-08 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e3482a1-98e5-3dc9-885a-05e7e597e1f3 | -11.47202 | -56.76902 | 2024-10-08 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4acfdab6-22a1-3779-a4e8-3fed5692a45a | -15.9672 | -57.22121 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58b09482-32b4-39f2-9a96-578c76f2ceb6 | -15.96668 | -57.2252 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 215bffa1-de84-3912-ac13-05f9a4931321 | -15.95899 | -57.47494 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15db656c-3e35-3d76-9296-79d6297e304b | -15.95894 | -57.22031 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88bcf185-9cbc-3cbc-ad2c-9cd42c7e111d | -15.95531 | -57.21596 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8832cd1d-87ba-3e3f-86ae-85f48d481498 | -15.95481 | -57.21988 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1bece534-a75b-34cd-ba18-421257bdc40c | -15.90376 | -57.48358 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa496d6d-9818-375a-a11a-336e6a7c2e9e | -15.90328 | -57.48706 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9abf5083-d5df-34c5-8293-bc4e0dc76c23 | -15.89974 | -57.48289 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d16258a-7c19-3fba-8d6e-2742f83b64d0 | -15.89929 | -57.48622 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f8360d5-77e3-386f-ba8d-f1d7990d0211 | -15.89571 | -57.48222 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bbafa01e-5bed-398a-8817-57c1b21b35bf | -15.89267 | -57.47422 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f7ff4200-84d7-353b-b3f0-fbd050cf3fe9 | -15.88914 | -57.46989 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 16d311f5-d2f7-359f-8e9c-479f4b1eaf1d | -15.88862 | -57.47373 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59184146-ce37-37a6-b910-a58d52f27ac7 | -15.88164 | -57.46443 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d9a7679c-f145-33c0-82cf-cfc73d793a4a | -15.87923 | -57.48237 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 540cc3df-0484-3b43-8e53-86206c300429 | -15.87759 | -57.46391 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d0940a23-f98d-340c-9a6e-03960c607316 | -15.87705 | -57.46794 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 876d5123-a143-3659-9c5b-1d4d30a9b991 | -15.87611 | -57.47497 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c0e5561a-2fa9-34be-a97a-6d318cb00793 | -15.87567 | -57.47823 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eabe2c19-e683-33e7-8026-47b65a51eb4b | -15.87407 | -57.4594 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76f0e2f1-3530-3a5a-b111-b06cc5830faa | -15.87254 | -57.47082 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a185801-2ff2-3aa3-b59b-9482869cd994 | -15.87209 | -57.47418 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5693597-a9ae-34e9-942d-8c94cb6e4464 | -15.87165 | -57.47749 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 817b7c3e-b52b-350c-9a6a-ccbb79865de5 | -15.68813 | -57.39293 | 2024-10-08 05:23:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0831aad3-975b-361b-9927-16e990f5cd04 | -15.68352 | -57.39648 | 2024-10-08 05:23:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1a4372e-86a6-3b72-bfd4-f51c8290e842 | -15.67886 | -57.40041 | 2024-10-08 05:23:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57d72077-8a56-3764-bb07-799b4c7b329e | -15.64031 | -57.38007 | 2024-10-08 05:23:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42e2e694-c1ab-3745-88d8-3836ce2f45dd | -15.60888 | -57.36787 | 2024-10-08 05:23:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a3cab260-e7b0-3e6b-964b-329f5b3cd902 | -15.60842 | -57.37144 | 2024-10-08 05:23:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ac79a56a-0b17-34cb-9ff6-f87e9d73459b | -15.60799 | -57.37474 | 2024-10-08 05:23:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1228da08-1fff-3c15-9331-7895e790e300 | -15.60396 | -57.37393 | 2024-10-08 05:23:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68d2886f-9a80-3772-ab79-dc113c23a2f9 | -16.55908 | -57.47621 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| a03f843b-9602-3e3f-974a-4f6ea3e8ba2e | -16.55686 | -57.71706 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 51371612-95ce-3239-b378-f11079055e21 | -16.55284 | -57.71652 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 631b74ad-ee91-352b-aae1-676c9e9a5521 | -16.54648 | -57.73394 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d8f079c0-9c2a-358d-b7f3-1c814add3a55 | -16.54601 | -57.73752 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d9d6391f-a5c7-3dab-88ac-d55633365a21 | -16.53662 | -57.7469 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7f8346bf-1086-3011-8c78-a9bd7b984dff | -16.53262 | -57.74628 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 2fdbe875-c4f0-3314-9561-87423a5f0527 | -18.71521 | -57.28349 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ea30abdd-6b24-37fc-b3d9-b32bde3c08f3 | -16.52508 | -57.74144 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 55b3f3c8-ec35-33a5-80b0-20e86b410a02 | -16.52397 | -57.7091 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 45674e7f-75ed-3530-a8df-220328bc2078 | -16.51948 | -57.71199 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 3f400d06-3718-3383-b9d7-630a609d372b | -16.51901 | -57.71551 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d6b55e5a-505e-3983-9d91-edb1ec2bd627 | -16.51498 | -57.71504 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 25719797-8304-39c1-851b-3e9ba78bf578 | -16.50743 | -57.71038 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| dabf0195-c7d4-3fa7-a58d-d969f86757ac | -16.50695 | -57.71392 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| b792db4d-5dd9-3401-a974-fc11f756277d | -16.50647 | -57.71748 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| b3ee31ce-7a43-3c1f-84d8-9d0da2d2942c | -16.50294 | -57.71331 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 3a5314ac-723f-32fe-abff-65a322396cb2 | -16.49894 | -57.71265 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 0ce20bc1-8966-3c8b-be45-e79f95c76be9 | -16.49846 | -57.71618 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| c5cf65fb-ec98-35dd-872c-87e4bb5841d4 | -16.49684 | -57.69778 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| d6232eae-774a-3fbb-941b-84a755628459 | -16.49608 | -57.73401 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3208974e-2d81-3599-b699-985e460ef5f3 | -16.4951 | -57.74127 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a4d1ee06-6280-3729-bb75-d7775c5688f8 | -16.49398 | -57.71914 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4f31d2b5-daac-3732-9c9f-96664b554f75 | -16.49303 | -57.72625 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6d96ec17-7187-3546-b35e-40775b5cf98f | -16.49256 | -57.7298 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9193ae8e-cf9a-3274-ac21-62e3e713c341 | -16.49234 | -57.70079 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| f827c86f-35e0-30d7-829b-dc6bb458f168 | -16.49207 | -57.73341 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8a5b424a-adbe-3685-b54a-54bdeac3651e | -16.49187 | -57.70436 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| b8971d3c-9edc-3d0d-920c-263930c84e34 | -16.49139 | -57.70794 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 46f70731-c74e-3e9d-9929-1b112cd120e4 | -16.49111 | -57.74063 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 87ec81a3-f5c4-34b4-ad46-c88b531698a0 | -16.49091 | -57.71151 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b04187a3-bdb8-3041-b78e-4f50179c59c8 | -16.49062 | -57.74424 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4fbbe51e-492c-30ed-b6e3-0068def3bc68 | -16.49043 | -57.7151 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 035c27c5-77c5-347b-84c8-f02816c7bc77 | -16.48901 | -57.72575 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3f2c2c0e-bbd8-3a48-9f67-1828c443fc9e | -16.16479 | -57.4215 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 091ef979-e9ce-355e-8f97-39375fdb0d1a | -16.14635 | -57.59409 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3f765568-8000-3c7c-af8b-20aa1c2322a5 | -16.14588 | -57.59768 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| cb4f8698-31aa-33fa-9a0c-778cb51f6745 | -16.14282 | -57.58972 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 135af32a-609d-3ea4-adb8-3c04e0f39250 | -16.14233 | -57.59349 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| dd92377e-b3fb-3f94-8c05-871d4707dde4 | -16.13878 | -57.58926 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 21b8be14-3467-3277-a2d7-9d5f0e4af23c | -16.13831 | -57.59288 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 225d7223-f911-390d-aff1-67221b1a829e | -16.13625 | -57.41784 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3982342e-7bd6-3ff2-b6b4-e9eccfeceb39 | -16.13474 | -57.58879 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 491f977d-e175-3c5f-bbf3-fa62ee58a1bb | -16.13383 | -57.59577 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d73448fb-f68d-3a4f-91b9-aa93719038bf | -16.13218 | -57.41733 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89d52f25-628d-3ced-a375-c485d918f5b6 | -16.12224 | -57.55872 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e2bccaaf-8f2a-3d77-8e3b-3ff7e8df5066 | -16.11866 | -57.55465 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9c7a2b39-53f8-3b63-87f2-b10989b39f0a | -16.11784 | -57.55498 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d3ba9fd2-4b2d-3f09-8f51-8682485f53f1 | -16.11737 | -57.55846 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7a439358-1559-3c64-9210-abfacf2ff398 | -16.11464 | -57.58572 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d162a296-0c72-368e-9276-6ffb6b4da1d0 | -16.11417 | -57.55761 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2f51ef33-d36f-344d-8475-8611190a9fbc | -16.11364 | -57.58592 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c0281242-d3e9-3cdf-97ad-06fdd87b2a35 | -16.11334 | -57.55786 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4bcce649-f602-3894-b63b-a003426c5b9d | -16.11291 | -57.56103 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4a2fe619-7f41-362b-ba41-7a8a1304cc1b | -16.1089 | -57.56032 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ff74196f-fd2e-32b8-8737-fe2e1c83270f | -16.10847 | -57.56353 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 00b5edef-88ef-35d0-bc99-d6ca9ddf2645 | -16.10447 | -57.56275 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 06358425-3b86-32bc-81fc-ed977aa3dcca | -16.09902 | -57.57273 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README116.md)
