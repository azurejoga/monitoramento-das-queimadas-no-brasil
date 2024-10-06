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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 194fb3db-ad41-3b16-b5e0-7c22bbd2f3e2 | -17.070999 | -56.810101 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2778ddfc-2ddc-3c53-877b-32ed0436f472 | -17.0284 | -56.675598 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 27bda99b-8898-35b4-8d94-89c60f577c21 | -17.0305 | -56.6842 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 178fc622-c2d2-386c-9654-9ed18d693f70 | -17.032499 | -56.692799 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bc2b4ef6-fe0b-3ce8-b446-4e823475bff6 | -17.036699 | -56.710098 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1381183d-ecf7-35bf-b23a-192fbb75604b | -17.057199 | -56.795601 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7d37a5e9-f444-36c6-a824-dec16af9955f | -17.059299 | -56.8041 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b079083c-e21f-3e6c-8254-53090c32e315 | -17.0613 | -56.812599 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 79fe0854-56ea-3be2-b5d0-2192bc4a65ad | -17.187599 | -57.342098 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 24a8aba8-b2b6-3485-a6c5-75eb6c6d14a2 | -17.189501 | -57.350201 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9af4969c-c919-345f-974c-d5acc8938ecd | -17.0165 | -56.669498 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5bbf5788-d82e-39ff-bfb5-18e1980d7834 | -17.0186 | -56.678101 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8b49e219-1634-38ba-a5be-7d656ccb54a0 | -17.0207 | -56.686699 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b2aa0cc3-bfee-31a7-a113-6dcec0d72512 | -17.0228 | -56.695301 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c48c3b6c-abb9-3ca4-ab54-c184304e4da2 | -17.024799 | -56.703999 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 899ef1eb-6930-39b1-9ef6-936b921e741a | -17.026899 | -56.712601 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8dcdb745-176d-3744-9ca4-e0b09f40da66 | -17.028999 | -56.7211 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a63237c1-9d13-3dd6-b298-99653534dc2c | -17.031 | -56.729698 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f007e803-7579-3770-98be-a69d588d0938 | -17.045401 | -56.7896 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 37fb8e7c-121b-3a15-a99b-86d22fedaeed | -17.0474 | -56.7981 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ad156541-efb6-37ed-8d6f-cc655605c8f1 | -17.0495 | -56.806599 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ccab4fa7-24a8-3a21-94cf-4024ed03c109 | -17.1779 | -57.344601 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 06f9384d-3d3d-33a2-97a8-ce83f82cbe4b | -16.8158 | -55.886002 | 2024-10-06 01:40:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| adf1d106-483b-3bb0-94b5-80221b1ea64e | -16.8181 | -55.895401 | 2024-10-06 01:40:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e50f8c97-72d9-360f-a86f-5b917d236eb0 | -17.0068 | -56.672001 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 59e8bb50-6c00-39c2-a1f4-7d370cc23552 | -17.0089 | -56.680599 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2deeeab7-c80c-368d-9c97-6943f9a315db | -17.011 | -56.689201 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dda944e0-0846-3962-92ec-61d8fc69621a | -17.013 | -56.6978 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 844079bb-cc0f-3a33-a290-e1fa50baf3cb | -17.0151 | -56.706501 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5947771e-be38-30f9-8e02-8c33b8d3e641 | -17.0172 | -56.715099 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6618936a-3157-3739-afba-827e1af52fac | -17.019199 | -56.723598 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 99291c95-4600-3d7f-9a8f-9766c5d1d3a0 | -17.021299 | -56.732201 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| abd5d9fe-967f-329c-8fb1-35cb4a1078b7 | -17.033701 | -56.7836 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 73be10b4-ff44-391b-8657-51bcfad9c7e3 | -17.0357 | -56.792099 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| be6a628a-ae14-3c81-8329-bad2cbba9abf | -17.037701 | -56.800598 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 40c976ee-cc7f-3d9a-8702-774404819705 | -17.039801 | -56.809101 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a9ad589c-4977-38bd-bcfd-efb9483f062d | -17.0418 | -56.8176 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c281fc0e-ed91-3395-bcc6-1b545954e0c2 | -17.1681 | -57.347 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4941509d-1338-334c-b2f3-239da2106042 | -17.17 | -57.355099 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6b4e2991-3fba-346e-b724-3d96fc7b94b4 | -17.1719 | -57.363098 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e47d3482-ddb6-396d-82c6-640342873574 | -17.0012 | -56.691799 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 36939c70-4f58-3ed7-b01f-471b405d845d | -17.0033 | -56.700401 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3f41761a-3182-3e3e-af7a-3d11babe7788 | -17.005301 | -56.709 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b6530673-d0e8-3b1a-bb3b-d61cefc14bbe | -17.007401 | -56.717602 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 384ccd03-2af5-3f9e-abf7-10e4e192c42a | -17.009501 | -56.7262 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 61e816c1-b389-30ff-9359-5f91473ccd10 | -17.011499 | -56.734699 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cdf51ac3-42d1-33f7-af78-9bb7762ed1a8 | -17.0259 | -56.794601 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 76d07554-a11f-3fc3-bb9f-ad943973d8a1 | -17.027901 | -56.803101 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c3df4b7d-3031-3955-8020-42eb5ee6fde2 | -17.030001 | -56.8116 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 09cfd1e4-e9eb-3476-9275-4f128c1a0862 | -17.032 | -56.820099 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 264143f0-a8c9-3f1d-8216-060e3664d114 | -17.1583 | -57.349499 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3cd8601e-08fa-3bba-a47e-707cb7b33487 | -17.1602 | -57.357601 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 16aae291-baa6-301d-b94e-3f273d27b68e | -16.989401 | -56.6856 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| db5799df-2603-330c-8131-9284a7f79192 | -16.991501 | -56.694302 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 31976e86-69fa-3d1b-bb8c-8ff0df4f5710 | -16.9935 | -56.7029 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eb57034a-dd72-359d-9716-a150af31c963 | -16.9956 | -56.711498 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dc947ecb-0f6e-35df-a693-0747631f6212 | -16.9977 | -56.7201 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ead27e89-25bc-32d2-99f1-7bdafd68493d | -16.999701 | -56.728699 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f7fb07de-4c5d-392c-98d5-0809b8b7b662 | -17.001801 | -56.737202 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c7e5bdc1-93fe-30b2-80b3-c4485625f03e | -17.0182 | -56.805599 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 966f1f82-0b51-3ef3-a003-ccfad01faba5 | -17.0203 | -56.814098 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e8e424a8-0c36-315b-9b1e-ef26f7020ad9 | -17.022301 | -56.822601 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0558143b-fae3-3c57-9e8f-73f2d1abddf7 | -17.1486 | -57.352001 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9e7f6c8c-8fa6-3bb6-a010-27c65ef871bc | -17.150499 | -57.3601 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a5c8f4e7-78ec-3026-b608-e108b4c09593 | -17.16 | -57.400299 | 2024-10-06 01:40:54 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2c2c98e7-416c-3123-853a-d2a6338c0354 | -17.1619 | -57.408298 | 2024-10-06 01:40:54 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 57cf4a78-8f23-38ea-9c4d-7394c8a3c927 | -16.617599 | -55.2094 | 2024-10-06 01:40:54 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 51a73bb8-376a-3c8d-af04-60b173f9c599 | -16.958799 | -56.601501 | 2024-10-06 01:40:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5e7b7d41-194b-33d0-b1b8-31e0d4d3d376 | -16.960899 | -56.610199 | 2024-10-06 01:40:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ce680485-b0f6-3c6e-967b-2be1a4785c4b | -16.988001 | -56.722599 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 37d78f06-a85a-3b5b-94bd-a7cd83af4b50 | -16.99 | -56.731201 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 245b3691-3e1b-344a-b00f-35fee5b69691 | -16.9921 | -56.7397 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d3895496-4ae0-376d-854c-a7d7b2c42337 | -17.004499 | -56.7911 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2ab5e8bc-587c-37c2-89ed-25cecf5302e0 | -17.0065 | -56.799599 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fe197fec-b2e8-33fa-896a-41b3b5a65207 | -17.008499 | -56.808102 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e6aec0ee-eb28-355b-99b9-00a18598f407 | -17.010599 | -56.816601 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 24203ab4-cf90-3296-bcb6-fa5a0d82b46b | -17.0126 | -56.8251 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cb60c6f8-dd1e-3530-a97c-1a527a3ad5af | -17.1388 | -57.354401 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6a63a757-dc68-3500-b11d-15869f4a96d3 | -17.140699 | -57.362499 | 2024-10-06 01:40:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4fe5f2b9-9a12-3d74-a55d-e4ea0e6669af | -17.148399 | -57.394699 | 2024-10-06 01:40:54 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 923d4d0f-57fa-386f-a602-21d1fa8237ef | -17.150299 | -57.402699 | 2024-10-06 01:40:54 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 020ce3f7-67a3-3725-9a31-ab3b9f0e80b6 | -17.152201 | -57.410702 | 2024-10-06 01:40:54 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a546c949-6d8e-3a31-a409-5dcd1a754589 | -16.948999 | -56.604 | 2024-10-06 01:40:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6b91928a-0985-3077-83d3-03234930e556 | -16.951099 | -56.612701 | 2024-10-06 01:40:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1d929be6-8d46-366a-8c39-5f4f3679b92b | -16.980301 | -56.7337 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f838f2d4-3871-3c40-b26e-677811f6419c | -16.9823 | -56.742298 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 62028623-b236-3b86-9d68-ca274b0e3eef | -16.9844 | -56.7509 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0ed550cb-d9f9-390d-8af6-5a6ab03618bf | -16.986401 | -56.759499 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 14d05eaa-68b2-3ca6-843e-33e977b000b3 | -16.992599 | -56.785099 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c5c528cb-edbd-37db-ad18-57155c306f7c | -16.994699 | -56.793701 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ee5ec7f4-75ed-3d44-9205-4d45d91e87b0 | -16.9967 | -56.8022 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 06159589-2852-3a2b-bc43-4384d874ce6a | -16.998699 | -56.810699 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1aee670d-6ba5-3b23-ba3f-22654d7e6e38 | -17.000799 | -56.819199 | 2024-10-06 01:40:55 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| acefc8b4-c04f-32a7-b12d-30e5326954f2 | -17.131001 | -57.365002 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e6d78cc4-e804-3152-a5fc-dca2c2e0426d | -17.138599 | -57.397202 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c85f6637-6459-385f-be89-c03be69acb03 | -17.140499 | -57.405201 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2ef9225d-3b7f-34cd-b5f5-9793b141f4f6 | -17.142401 | -57.4132 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 78eb8bf6-e477-36f0-a1b9-a9f967f622a0 | -17.1443 | -57.4212 | 2024-10-06 01:40:55 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 16ccfd36-c3ea-3993-9bd7-43bf43e33660 | -16.937201 | -56.5979 | 2024-10-06 01:40:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c8c57fe7-ace6-36b3-b14c-30cd9707f2b3 | -16.939301 | -56.606602 | 2024-10-06 01:40:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README28.md)
