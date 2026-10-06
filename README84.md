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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e35f7180-04ee-3577-9437-0a57dd6005b4 | -11.8311 | -43.5628 | 2026-10-06 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 4a0e2a10-f783-34d3-ba10-68c69c4d0aff | -0.3952 | -52.0562 | 2026-10-06 14:20:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 76.6 |
| bb978156-05ba-3f01-a421-749fbb882861 | 0.4465 | -60.5442 | 2026-10-06 14:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 90.5 |
| a7975e6f-811f-344a-8c24-09994893c680 | 1.8038 | -55.5458 | 2026-10-06 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 22b5dee1-b37a-3b9f-bb01-b8d132a47c50 | -9.0244 | -65.4181 | 2026-10-06 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| d5f988e2-6b89-3fcc-af97-4757da0b7081 | 3.1097 | -60.6133 | 2026-10-06 14:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 1d316ef2-fe95-3014-9105-76249cc523a3 | 3.0733 | -60.576 | 2026-10-06 14:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 9593ad54-3726-37a2-a6ae-9e83004c39c2 | -7.2077 | -44.3255 | 2026-10-06 14:30:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 18a4ab3e-b33c-329b-982f-edc31a15631e | -9.0058 | -65.4373 | 2026-10-06 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| e03e0d1f-8aa9-3436-ba31-358f14ef6370 | -11.0485 | -45.6511 | 2026-10-06 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 245.7 |
| f77425b7-07c2-3a4f-97ab-de2e36853ce2 | 1.7855 | -55.5461 | 2026-10-06 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 0e57334e-5be1-33b6-9f21-760a6f8692ba | -3.951 | -41.5426 | 2026-10-06 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 160.9 |
| 5a96dc3d-e003-36f7-9ae6-f650b9e95284 | 1.8583 | -55.7821 | 2026-10-06 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 78b86964-e3fe-35b0-a979-0320f9054dbb | -3.3921 | -44.4923 | 2026-10-06 14:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 167.4 |
| 73186147-f0f7-3fed-b0d3-6e036b871d41 | 3.128 | -60.594 | 2026-10-06 14:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 587ae399-ff8b-37fe-854e-45c0db28ed0f | -9.0059 | -65.4186 | 2026-10-06 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 2413ff2f-aac6-3059-84af-6acc602cd667 | -9.8261 | -44.7781 | 2026-10-06 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 62c27f38-f716-3265-b018-15d0ef9d64e7 | -9.1334 | -65.9 | 2026-10-06 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 6ffe2822-6215-39e3-88e9-46e8db41b96b | -9.7312 | -65.0944 | 2026-10-06 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 5516de2f-ac0c-377d-85f4-005c266b6075 | -6.7228 | -44.0001 | 2026-10-06 14:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 194.4 |
| 30750ea4-c60c-392c-bff5-2779ddc3dbb9 | -9.158 | -45.1328 | 2026-10-06 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 184.5 |
| 594d1ba8-f063-375a-a4d2-5672eddf4d99 | -9.8257 | -44.8011 | 2026-10-06 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 32536ede-9b3a-3341-9a13-ef66df97015e | 1.9134 | -55.7221 | 2026-10-06 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 2ec18c25-ff1d-3e46-9969-2c01eb7ad73b | -3.9697 | -41.5416 | 2026-10-06 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 209.4 |
| 66668c35-02c6-3081-bc15-775283593c9f | -7.2079 | -44.3024 | 2026-10-06 14:30:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| e2925b07-29ac-32ef-bde1-6bbe3f004a1c | -9.7126 | -65.0951 | 2026-10-06 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| d9a8849e-d405-3a23-883a-f42a9b1c96e8 | 1.7304 | -55.6259 | 2026-10-06 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| a1fecfe4-0450-33ca-a494-51fceffa1d7a | 1.7854 | -55.5658 | 2026-10-06 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 01d434ca-9b87-385d-b047-74943de08db0 | -11.8311 | -43.5628 | 2026-10-06 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 267.5 |
| 44b83319-b6ba-3407-b059-442df6e5a6cf | 1.7854 | -55.5856 | 2026-10-06 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| e6dd67cb-ab7f-3a12-b33f-43381c095976 | -11.8315 | -43.5391 | 2026-10-06 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 421.9 |
| 7c1fd940-5083-3328-ba14-65d627c24872 | -3.3923 | -44.4695 | 2026-10-06 14:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 195.6 |
| 726e2969-4ab3-33d2-996e-97ea54eb296e | -10.9758 | -45.4324 | 2026-10-06 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 251.9 |
| bb0e6dfa-dd94-31ea-a818-c6160858cd07 | -10.9762 | -45.4094 | 2026-10-06 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 158.9 |
| d34e1e2a-6e06-397e-9b47-2df0b20c4667 | -5.942 | -41.3282 | 2026-10-06 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 157.4 |
| 41923c73-7bad-3620-9ec1-fbb13169d779 | -7.8496 | -44.1478 | 2026-10-06 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 91a034a5-cf82-3564-a235-cdcd2466b849 | -11.21 | -46.2655 | 2026-10-06 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 186.9 |
| cf97de24-34bf-353b-9bfd-bb12e56267c2 | -9.043 | -65.4175 | 2026-10-06 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 57c746b0-9a7c-302f-8f1d-e3d167e58e71 | -9.0046 | -65.6988 | 2026-10-06 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 9047b7e7-9c2d-30b5-bd3c-05b996144f97 | -3.8182 | -41.8132 | 2026-10-06 14:30:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 213.2 |
| a440d79c-b195-3b94-bc48-275ec4e30463 | -11.6575 | -43.6136 | 2026-10-06 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 73bd43cf-f50b-37d3-b22c-0ca8cff9bc46 | -7.2079 | -44.3024 | 2026-10-06 14:40:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 1b054efa-101b-39af-8abf-ae8abd4aa0f4 | 1.7854 | -55.5856 | 2026-10-06 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 9b1a0e60-df3b-36f4-ba3c-0ad9897f59c6 | -10.9571 | -45.412 | 2026-10-06 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| fad636de-40ea-3c81-bdbd-3a19c89bac6a | -9.0059 | -65.4186 | 2026-10-06 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 0e3ebf71-5b7c-3882-8f34-7295e100a7d7 | -6.7068 | -45.5539 | 2026-10-06 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| fee8b991-1ba5-333e-86c3-6fb98b0c680e | -9.1334 | -65.9 | 2026-10-06 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| c7c2e010-9987-37ad-85d7-e217c9a2b286 | 3.128 | -60.594 | 2026-10-06 14:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 391c6b5b-c679-3872-b086-36c13028daf1 | 1.7855 | -55.5461 | 2026-10-06 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 305215a0-8ba9-3ecf-9cec-dedeb9fe2213 | 1.8038 | -55.5458 | 2026-10-06 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 70d340a7-8bfd-3db0-aef7-6cc76f73463e | -3.8182 | -41.8132 | 2026-10-06 14:40:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 239.5 |
| bdb603a3-d933-39d9-a1cc-1cea6b25ea31 | -10.491 | -47.2533 | 2026-10-06 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| b3e10db2-ae5a-356c-8b0b-07a34b35c938 | -11.47 | -43.3824 | 2026-10-06 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 864b7c39-83d8-30f6-b74c-975604976586 | 1.8583 | -55.7821 | 2026-10-06 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| a4160542-8632-35d1-a1f4-e1f951338cc5 | -9.8261 | -44.7781 | 2026-10-06 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 5af589e3-2199-3145-b441-fd9db694031d | -11.6951 | -43.655 | 2026-10-06 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 269.5 |
| 6d3ded0d-abed-3bb3-9847-ffb6ba1ef49d | -1.1531 | -49.1483 | 2026-10-06 14:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| a3980956-2944-3ede-803a-2415f35b31a0 | -7.2077 | -44.3255 | 2026-10-06 14:40:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 192f3e02-0887-30a2-8420-1b0ba286010a | 1.4922 | -55.688 | 2026-10-06 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 1a63d9e9-0884-3caa-b30c-1c9e278e4c22 | 1.7304 | -55.6259 | 2026-10-06 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 37aeb003-49af-3dca-a54a-7148c7b5cb57 | -0.3952 | -52.0768 | 2026-10-06 14:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 95.5 |
| f2188393-ab32-3a3f-bbe3-a08bc7de9ecc | -11.6763 | -43.6343 | 2026-10-06 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 8bc15218-6e89-3d01-ba45-f2ec94b58ef6 | -3.3923 | -44.4695 | 2026-10-06 14:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 296.6 |
| 43170148-e5af-3bf9-abbe-202974fa8134 | 3.1098 | -60.5943 | 2026-10-06 14:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 22aef7b9-0f83-350e-980d-6655be928b1b | 1.6202 | -55.7852 | 2026-10-06 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 6d8ba8ee-b153-36ca-955b-b15f8d63717c | -11.6575 | -43.6136 | 2026-10-06 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 216.8 |
| bb00c781-12cc-37ea-ad4f-d38ffc32ba80 | -9.0046 | -65.6988 | 2026-10-06 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 8c9dda4c-a06a-318b-ba97-bdc50553729d | -11.6758 | -43.658 | 2026-10-06 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 178.8 |
| a4943328-0f98-3f55-8425-ac99e5aff595 | -9.1408 | -64.3836 | 2026-10-06 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 0170c2bf-97c7-3c29-a78b-31ac5c1f11d5 | 1.7854 | -55.5658 | 2026-10-06 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 841a0038-9332-3eca-beeb-cda38bf8f49d | -11.657 | -43.6373 | 2026-10-06 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 230.7 |
| b3207d3e-87bd-3a6a-98b8-7e64bd2a5f7b | -9.8257 | -44.8011 | 2026-10-06 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 99810cac-098a-3b05-878f-de13bbea3285 | -7.8496 | -44.1478 | 2026-10-06 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| aa3a52c3-61e0-3239-b504-a15a1d545c04 | -9.7312 | -65.0944 | 2026-10-06 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 820f463c-ff87-3cfc-ba47-6e0cdf5a6600 | -10.9762 | -45.4094 | 2026-10-06 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| c54db5d0-289a-3b8b-9581-30be717f1959 | -9.7126 | -65.0951 | 2026-10-06 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 482f1cd4-4fec-3cd9-8ab0-5219e3611650 | -11.7147 | -43.6283 | 2026-10-06 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 185.2 |
| ca457b06-6aa0-398d-8cfd-39b3b09c7bf9 | -6.7228 | -44.0001 | 2026-10-06 14:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 99f01f39-133d-3cbe-9bf8-4439fe7b6b34 | 3.0916 | -60.5757 | 2026-10-06 14:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 60.4 |
| dbed5979-55ba-3738-a9c1-a7642f5e61b1 | -10.9758 | -45.4324 | 2026-10-06 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 99f60850-0764-3d98-b25f-fc6a512717f5 | -11.8315 | -43.5391 | 2026-10-06 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 338.8 |
| 013417c7-a002-3f94-800e-b3c28476f9d9 | -11.8311 | -43.5628 | 2026-10-06 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 175.4 |
| f8f454c7-dcb7-34e8-a792-12dc5d8527e3 | -9.8071 | -44.7804 | 2026-10-06 14:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 4b6d3dd4-7081-3cf1-8f79-a3b6d6449b83 | -7.2077 | -44.3255 | 2026-10-06 14:50:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| aadf7507-2a4f-30a0-b736-b1e38b6d204f | -10.7493 | -45.3024 | 2026-10-06 14:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 130.8 |
| a7240324-0199-3fd3-9cd0-2f8299a0bbc6 | 1.8583 | -55.7821 | 2026-10-06 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 40958f15-8c4b-3643-8224-611ac302bf62 | 1.7854 | -55.5658 | 2026-10-06 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| deddcfb3-51aa-33d4-b936-58fe946b9609 | -9.7312 | -65.0944 | 2026-10-06 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| b9629d59-9903-3550-b0c1-6968126dd192 | -5.942 | -41.3282 | 2026-10-06 14:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 584.8 |
| 5cf65f48-81a0-39b2-af78-c9ca271c1156 | -10.9571 | -45.412 | 2026-10-06 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 0e750228-0c4f-3b79-ac61-cc26be9ef6e0 | -9.1408 | -64.3836 | 2026-10-06 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 6cd4d16d-4ee2-36a4-b3ad-a3c724d1429f | -9.1334 | -65.9 | 2026-10-06 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 63c10c7f-0102-3702-8a66-88bb0fca34f1 | -11.657 | -43.6373 | 2026-10-06 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 206.9 |
| 1eada911-c2a9-3707-9f4b-5b256b3aad90 | -1.1531 | -49.1483 | 2026-10-06 14:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 8f069e86-e263-3f12-ad01-a545bc8fac74 | -3.3923 | -44.4695 | 2026-10-06 14:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 425.7 |
| e2fa8002-8d3b-3e8e-a88e-e26716693e62 | -9.0584 | -66.1073 | 2026-10-06 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 45b81427-7bc3-300b-aed1-65d9dbd04b79 | 1.4922 | -55.688 | 2026-10-06 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| bb3d41cb-9783-3321-8842-b528c82d6f08 | 3.0733 | -60.576 | 2026-10-06 14:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 009b68e6-5697-32e9-98a2-9e15352c01ef | -9.9175 | -65.0313 | 2026-10-06 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.3 |
| f175fe7a-20a0-39fe-82bf-e0e314464980 | -10.9755 | -45.4553 | 2026-10-06 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.9 |


[Clique aqui para ver as próximas entradas](README85.md)
