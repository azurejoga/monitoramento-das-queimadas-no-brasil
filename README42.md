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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1ae7df9-af59-3fb6-97f1-6280ae5c944b | -7.43361 | -60.6235 | 2025-08-24 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c35f997d-1160-3ad6-8c82-72dc44e52eb3 | -6.91406 | -52.85427 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a79ee0e3-14e6-3ded-8124-5d8614850f15 | -6.87462 | -59.82333 | 2025-08-24 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 55abce17-2c73-3f16-9ba2-f9d4a5ae350a | -10.52967 | -47.1596 | 2025-08-24 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6325e6c6-f200-3f3a-986e-d5550afcff25 | -11.53747 | -51.86499 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c19c4a7-8757-31ff-b19e-12a0c86b61bc | -5.74208 | -57.58963 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b469be14-c335-3f4e-81f2-3cf08c6457d7 | -7.06624 | -44.06731 | 2025-08-24 04:34:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ad976516-709a-389b-b4bf-280a63e982bd | -6.61166 | -48.04632 | 2025-08-24 04:34:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12be72cf-d440-3fc1-819d-30c57b6a4f6d | -9.15078 | -59.48617 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 26253095-e557-321a-b844-087dc89a7b07 | -11.11963 | -44.78715 | 2025-08-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99b8a022-0aae-32a6-970c-566f9a0a0b68 | -12.73785 | -48.13001 | 2025-08-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 60c0b08f-4342-3b72-bbb7-86619ed4a997 | -10.26869 | -46.74783 | 2025-08-24 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4f12506-c9c6-3627-90ef-8df7b94e66e2 | -8.06128 | -49.6573 | 2025-08-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3223e44e-fa83-3869-80bc-9c10c9c17e9e | -9.02316 | -47.64761 | 2025-08-24 04:34:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d7a59818-2454-3a00-9eeb-439dfaf57f81 | -13.41394 | -51.80825 | 2025-08-24 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83a58b68-812b-3fdd-80ac-23cb2cc693f0 | -13.47157 | -47.02976 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 27310c5d-8230-349a-970a-24efe591cf5f | -9.16417 | -59.47959 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 75cbf7fb-c211-3bb2-be03-b9b8ec7f2f1f | -7.9311 | -45.91434 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c8dc1bd8-ae4c-3c01-8e5f-561e6d054ad2 | -5.75376 | -57.58773 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 841b6431-1e9b-3e5f-acca-371be3245c47 | -11.70284 | -60.18728 | 2025-08-24 04:34:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59f0a971-3afb-39ca-ac43-1ef34cf820ac | -11.18187 | -55.02762 | 2025-08-24 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37be6f34-dc18-3c15-af74-5ba19899578f | -9.15649 | -59.51175 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 27a5669d-3a96-35ae-98c1-aa8fa03e2aef | -11.14004 | -46.33005 | 2025-08-24 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fbed47b4-3343-3387-955d-e1106d950b17 | -12.96296 | -46.32045 | 2025-08-24 04:34:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57698d6d-23e7-3225-8137-53013d555c0a | -10.29964 | -46.75321 | 2025-08-24 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8ed6266-e351-3212-b323-76f11182e07b | -8.84081 | -49.89296 | 2025-08-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46e1e2a3-7a4e-3f03-adf2-b28bef5449c9 | -9.14919 | -59.4947 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9bbe5265-44cd-3852-83ec-4cd9a1f5a192 | -7.57464 | -43.84476 | 2025-08-24 04:34:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba2aa787-0a85-32b7-9321-01cf5cedfec7 | -13.05233 | -46.32348 | 2025-08-24 04:34:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bc89ddf2-c8e6-3807-af4c-d790c8d161aa | -8.76075 | -46.73474 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09d0b70d-1418-30e7-bc65-ac0a8b4dd7a3 | -11.53313 | -51.84777 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 1ee1598b-60c2-3d81-bf67-9250d9a223d2 | -8.76347 | -49.97675 | 2025-08-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85b577b7-6200-3386-9c09-f29be3adf14d | -11.32132 | -47.85839 | 2025-08-24 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4952b267-9469-3041-84e8-b480a6897857 | -8.53178 | -48.86044 | 2025-08-24 04:34:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e942dec-4296-364b-be8d-30270753e4e7 | -6.68757 | -58.85451 | 2025-08-24 04:34:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f753dc29-a036-3de9-a00b-52e442976b41 | -7.61177 | -45.24411 | 2025-08-24 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa854bd2-3ffc-3891-986d-d9241475530b | -8.20553 | -44.42706 | 2025-08-24 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3db1f151-a296-3565-8a40-4af7d22858fa | -10.74834 | -49.58029 | 2025-08-24 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78718f98-c15f-3da1-8ef8-ab10f78d0bb8 | -9.96947 | -46.38968 | 2025-08-24 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49abcbfd-8032-3ac1-87dd-175e396d37a0 | -8.61675 | -62.60481 | 2025-08-24 04:34:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c9e7a7d5-b52f-35a1-a126-a9447f511dba | -8.54009 | -37.72365 | 2025-08-24 04:34:00 | NOAA-21 | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3a9570c7-902d-3608-a958-600bb10175ce | -12.73171 | -48.12508 | 2025-08-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 608a3079-20ed-3f4d-9c42-d03189bba15c | -7.92645 | -45.92157 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 70cbb21d-87a3-3706-a884-9db43efd340d | -10.604 | -44.3232 | 2025-08-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 758e99cc-b524-33ea-807f-cfa9d204da0c | -9.16656 | -59.46675 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ab8aaf2f-765a-348a-9193-dbabb9263356 | -7.60299 | -44.3681 | 2025-08-24 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b78d6fe-415e-31c9-9cde-34fa6e0f28e8 | -5.61692 | -60.23454 | 2025-08-24 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e6f7731-53e7-3982-a54d-a8c1bdc9b8ba | -11.52829 | -51.85515 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 1312d8a3-d1f6-3325-80cc-d56e9a4b7b69 | -5.74518 | -57.6034 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4c590bc4-9963-3a0e-b0a3-7d8ff2c6e410 | -7.06627 | -44.07014 | 2025-08-24 04:34:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c9cc53d-dca7-3095-85d2-a9e1b68b6c77 | -6.46137 | -53.40396 | 2025-08-24 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43418346-ddce-3a34-831e-68ef5ce83f27 | -10.41451 | -47.18053 | 2025-08-24 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8ec2c52f-447e-3106-b97e-30c6152533a4 | -5.87587 | -57.76512 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04171cb8-c46e-3737-bc99-e019430108b5 | -8.23561 | -47.46361 | 2025-08-24 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a01481f6-e144-3525-a376-987d926bc743 | -13.17319 | -46.9171 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efd4fd54-27a6-3018-9588-8b7291b99eb3 | -11.60286 | -46.23261 | 2025-08-24 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 303ac93c-8579-3ee3-aeed-529e66c18f0f | -6.89249 | -45.6933 | 2025-08-24 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 55e41355-ebf6-3422-a240-fe069369a1a0 | -9.52167 | -60.51021 | 2025-08-24 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d86365ea-3274-38f2-861d-f92dc0111139 | -7.17885 | -44.66219 | 2025-08-24 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a53400b7-a260-355c-84b7-7c3e90b3f0a4 | -6.89307 | -45.68947 | 2025-08-24 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b54a198-4a5c-3041-9ac6-01f86ba66028 | -13.04938 | -46.77274 | 2025-08-24 04:34:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94c6cf56-7713-35a0-bb70-b24230285a6d | -6.88496 | -45.67238 | 2025-08-24 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba7d7df1-aedb-3990-bf87-8b1c8a344d3e | -7.4832 | -44.93058 | 2025-08-24 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5b56424e-e764-32b8-999a-d57a17cd278d | -10.80528 | -46.41725 | 2025-08-24 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0a157b6a-d020-3c21-aa31-f26582843705 | -8.87895 | -62.43554 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bc3df2c6-07c2-3c46-baa9-58ab0be44876 | -9.15666 | -59.48726 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4fafcc00-7791-3983-b4d2-82d775cca322 | -10.20218 | -48.46338 | 2025-08-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6c8f6be-5afa-35f1-ac82-55fb37183eab | -11.53947 | -51.85301 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ffaf8d67-e611-3915-81a0-bd567bf35c3d | -11.5109 | -51.86969 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ca5e056-cb91-3517-9632-b4d639ae3d32 | -6.89253 | -45.66953 | 2025-08-24 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18323559-9372-35f8-891f-00d4af45de5d | -9.71436 | -48.53978 | 2025-08-24 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e52b2f57-5d97-3242-80df-f4fbea59817d | -11.15441 | -44.70797 | 2025-08-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1d78de40-c45d-3d34-9bb0-dce1b7f38f56 | -11.52605 | -50.48204 | 2025-08-24 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e71b692-a0f3-35b8-8d4d-172ad1f82adc | -13.48047 | -47.04246 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e543ded-9448-3d4d-84a2-e4f1bc438843 | -5.74084 | -57.59687 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe3da521-29a5-364c-ba32-99259c5182d8 | -9.51654 | -60.55834 | 2025-08-24 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 04286cda-86f8-3ca7-9b8d-1091a4d0a5c6 | -13.03882 | -45.23629 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2d7a8592-ee94-3486-9803-26760b55570b | -9.19905 | -59.45517 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 64342c3c-7e6a-34d9-bcc6-e99e98d63060 | -8.73266 | -45.46248 | 2025-08-24 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 451fd6a2-bcb3-357d-b1a0-b37afa25d387 | -13.0549 | -40.94202 | 2025-08-24 04:34:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2d89cac2-d21d-346d-ad8d-b125683de7a3 | -11.31797 | -47.85783 | 2025-08-24 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3a5e6771-441f-3ca1-aae4-3ed1eb036f8d | -7.60554 | -46.26133 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 17fa50e0-5fdd-3760-a5ec-f23b573760a8 | -8.90471 | -62.44033 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b633f54f-1705-3a0b-a9d6-1299c93ce8ec | -13.47677 | -47.01856 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f2aede2-c210-3bc7-8237-18631749e36d | -9.17116 | -60.80711 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 33fb45f7-a450-3f8e-86ee-a7eb937330dc | -9.1476 | -59.50317 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c9243587-a102-3ba0-9b52-8bbc8259cac4 | -9.5145 | -60.514 | 2025-08-24 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1ee8629f-c791-31e0-94fd-bc825593ecef | -13.47443 | -46.88229 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f8f3b0d-7cfc-327e-ab74-867ec5230619 | -9.16366 | -59.51508 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9156d6c1-e7f4-3f4c-9ca1-8463645ac2ee | -11.13591 | -46.33355 | 2025-08-24 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a29223de-d148-350c-99b2-b59de19dc0ca | -9.1624 | -59.51274 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7454d495-ce5d-3fb4-a669-ec490b581f6b | -8.89835 | -47.32941 | 2025-08-24 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8cb44c31-1bab-3229-a7f4-a00eb354d1c5 | -11.42891 | -55.01036 | 2025-08-24 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ce7df9d-3409-3332-a31a-7090d42bcaea | -12.72498 | -48.10139 | 2025-08-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdfbf702-60f1-3cd3-8875-cf943f28b449 | -13.10075 | -44.10088 | 2025-08-24 04:34:00 | NOAA-21 | CANÁPOLIS | BAHIA | Brasil | 2906105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac49cb30-71e4-3ded-86e3-d46e179119ff | -7.17821 | -44.66644 | 2025-08-24 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 43f44d4f-11e9-33dd-b907-2e2fc5b0269b | -9.1599 | -59.46988 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 2a62f172-80ed-3a5d-9de1-dee32abf4be7 | -8.77212 | -46.75175 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 296d0953-eb5d-3146-839e-2178d2b43c14 | -8.90889 | -62.41976 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fe1a7eb6-c2c8-3d4e-b38a-8050dacdf149 | -8.76289 | -49.98037 | 2025-08-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README43.md)
