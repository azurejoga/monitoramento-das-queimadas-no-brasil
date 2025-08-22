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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7bcee2a-1662-3c01-80fe-1d33fdf3b451 | -14.5956 | -54.7782 | 2025-08-22 14:20:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 53574c79-85ad-375e-8308-159f4431eead | -14.6713 | -54.8728 | 2025-08-22 14:20:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 9580e3eb-e02c-31aa-8ff8-4eb866a2a238 | -7.6181 | -46.2616 | 2025-08-22 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 175.7 |
| e4ef7620-934a-3b5f-b89f-2c2c3853cdef | -8.4776 | -48.2578 | 2025-08-22 14:20:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 7ca90935-ae9f-3540-a6f0-54bdc8738e0c | -10.8757 | -50.8376 | 2025-08-22 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 5f0bfb1d-be1f-35cb-afa6-ed66a58bd2a6 | -7.9436 | -42.6631 | 2025-08-22 14:20:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 83.6 |
| 8222d6bc-9912-3a57-9482-f88357f6dbd5 | -6.539 | -45.4772 | 2025-08-22 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 0cfe3999-ca88-3b65-8d66-fae98de16ce1 | -10.8568 | -50.8396 | 2025-08-22 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 143.9 |
| fb8335d2-d503-31b9-bb9d-1e5e2b214407 | -12.3129 | -50.0097 | 2025-08-22 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 201c22ef-51aa-375a-a8a4-78a41f0b2adb | -6.9649 | -44.1864 | 2025-08-22 14:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 69ea9abd-03aa-3301-ac2b-f8ac4eb5604a | -6.4449 | -45.5298 | 2025-08-22 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 9b96d4aa-a7fb-3257-bb80-fa40425b2082 | -7.0354 | -44.6167 | 2025-08-22 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| a9a89e65-5055-3f4f-a687-9361d88087d8 | -5.7782 | -44.787 | 2025-08-22 14:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 248.7 |
| ea5b475f-127a-3c52-8ff1-a78dd8897793 | -11.3275 | -44.9468 | 2025-08-22 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 4abb9eac-215d-33e0-8b5f-61839d5a04ee | -12.656 | -47.7947 | 2025-08-22 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 49bda49d-e690-3d8c-9af4-63bbb5fb7def | -7.6559 | -46.2358 | 2025-08-22 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| c7a9a1cf-6ed5-3f00-9927-9dd6efb161db | -8.613 | -62.6118 | 2025-08-22 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 8d14d9d1-82fe-3dd9-b8cd-861258da7e37 | -12.2938 | -50.0121 | 2025-08-22 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 8a0d510a-58ad-34a9-97a9-7aa72905fe44 | -7.6296 | -45.2464 | 2025-08-22 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 39626485-7854-33fe-9b06-5d7bcc3ffc37 | -9.7446 | -62.7725 | 2025-08-22 14:20:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 19f4d25d-92a9-3a79-9c64-1ab1c8392f1f | -11.3271 | -44.97 | 2025-08-22 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 2e49971a-2800-39f1-a83c-cb40fcc3c637 | -7.6107 | -45.2481 | 2025-08-22 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 51846a0c-dfa2-39fa-8df3-695ee59e95a6 | -8.7759 | -45.4486 | 2025-08-22 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.5 |
| cae8f06a-6b26-3ee9-9239-119855092fb9 | -12.9963 | -56.9 | 2025-08-22 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| e5f39cc5-d800-3cdb-93d6-540bb3bd9f8f | -7.6366 | -46.2823 | 2025-08-22 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 235.6 |
| f7719dad-7d1d-3b3c-be30-c892759910e4 | -8.8736 | -62.4115 | 2025-08-22 14:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 80.1 |
| ac218a14-1922-3a51-85d8-39a4d4e66f55 | -7.6484 | -45.2446 | 2025-08-22 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 132.5 |
| c4f7be75-d7d0-38c5-970e-6c1ddc3867b4 | -7.2989 | -59.6307 | 2025-08-22 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 1cef1499-988f-3fef-9958-cc8481f287b8 | -8.4588 | -48.2595 | 2025-08-22 14:20:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 961f5a66-f140-31c3-a9fa-c7db450c522d | -14.596 | -54.7575 | 2025-08-22 14:20:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| a60337bf-e7e6-3b2c-99d5-3941297af180 | -8.7948 | -45.4465 | 2025-08-22 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 56f94156-637d-30a2-aeb4-ac1f24513b2e | -7.5922 | -63.4414 | 2025-08-22 14:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 03220e25-92bc-3fe5-ade3-6a223e665b2f | -7.1662 | -44.6736 | 2025-08-22 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 11356a0e-1dc0-3c8e-a2aa-5636d95ec469 | -12.9925 | -45.202 | 2025-08-22 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| b0da292e-1525-3db5-8900-334617e285be | -5.7784 | -44.7642 | 2025-08-22 14:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 140.2 |
| d52782d8-0ea1-355d-ac73-6db31bf28a98 | -11.3084 | -44.9495 | 2025-08-22 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 880aaac5-ab64-3bbf-8a66-f548c965460b | -6.5781 | -59.871 | 2025-08-22 14:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| f259fed2-e4d3-3d07-96d4-88f9191052f0 | -8.5943 | -62.6315 | 2025-08-22 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 9073e5fb-dca5-3934-8feb-4cc524b2ceb6 | -8.6129 | -62.6308 | 2025-08-22 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 461234ef-d5a6-3ac8-bd14-d470ef9ff300 | -10.876 | -50.8163 | 2025-08-22 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 4476f99b-2037-354f-886f-1a9745cdda63 | -7.6484 | -45.2446 | 2025-08-22 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 975f2d70-1154-3f3c-98d8-e65d89257d24 | -10.456 | -48.3607 | 2025-08-22 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| b09b966d-b13f-3525-9793-9da26a3243b2 | -14.596 | -54.7575 | 2025-08-22 14:30:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 134.7 |
| dba974d8-f89d-369e-9d10-2efe72ad6da8 | -12.9963 | -56.9 | 2025-08-22 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 90.5 |
| d0e8b366-9502-373c-ac84-ad7ade8f3b04 | -12.9925 | -45.202 | 2025-08-22 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 26310425-cbb3-3f91-9d4d-cb7d0f86d314 | -9.7446 | -62.7725 | 2025-08-22 14:30:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 9318d387-2ec4-33e0-be76-a5b8f745abfc | -7.6107 | -45.2481 | 2025-08-22 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| b1fd63d1-a3af-3d70-bd25-5c1b24c93807 | -20.2492 | -46.7017 | 2025-08-22 14:30:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 128.4 |
| a649cfe6-ea1f-350a-8a2e-7e2d939eabb9 | -11.3084 | -44.9495 | 2025-08-22 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| c406f5af-852a-3db4-9e65-1b2e34147493 | -6.4266 | -45.4861 | 2025-08-22 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| ef94ffd2-00ba-3c13-906c-209ef3910dea | -9.2095 | -59.4609 | 2025-08-22 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 219a3642-a9c3-3ada-b5c5-4903b3e3dd9a | -7.6559 | -46.2358 | 2025-08-22 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| fff28f1b-1a3b-32ae-9d65-9ded0afd2e94 | -6.2716 | -52.8255 | 2025-08-22 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| be3bf215-a529-3b28-b8b2-5242f5513993 | -14.7504 | -56.0151 | 2025-08-22 14:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 6299976a-6d4a-33c2-a5f1-9a53c5858b31 | -8.4588 | -48.2595 | 2025-08-22 14:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 188.9 |
| 7b30b17d-9e31-385d-8096-a0542e997dfb | -5.7784 | -44.7642 | 2025-08-22 14:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 00453ab0-5ebf-3623-87f1-a841ba0367d2 | -12.3129 | -50.0097 | 2025-08-22 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 4980dfbb-86df-3c5b-b846-c2378937253b | -7.0354 | -44.6167 | 2025-08-22 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 18236f0a-5640-3d51-948d-772bb7dc4fcc | -14.7712 | -45.4289 | 2025-08-22 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 671.6 |
| 6026fd64-f970-3c48-aeeb-7f5f60102138 | -6.436 | -44.5306 | 2025-08-22 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 2006e979-436e-3b73-8c5b-78a031a84897 | -14.7717 | -45.4055 | 2025-08-22 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 966.8 |
| 2dc7a6eb-58dc-3cb2-9cd4-71ce2c24eacb | -10.8754 | -50.8589 | 2025-08-22 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 113.6 |
| d9c5616f-dea1-3ad7-aed7-6a43fcacf87d | -14.6519 | -54.875 | 2025-08-22 14:30:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 71aeda54-8e92-30b7-891d-e3699b2fd848 | -14.7308 | -56.0377 | 2025-08-22 14:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 7463f608-0567-331c-b904-f9f8cba662aa | -14.6716 | -54.8521 | 2025-08-22 14:30:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |
| c1c8372f-cc3e-3f78-815a-c3ee6fc79305 | -6.5388 | -45.4998 | 2025-08-22 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| ab18550a-bcde-3ad8-9081-19c0ee99a62f | -8.6129 | -62.6308 | 2025-08-22 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 6221f57f-6c99-3a0d-b025-5da911d7afe3 | -6.5393 | -45.4546 | 2025-08-22 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 5874579a-9457-347a-94e7-0004f37edc12 | -7.6366 | -46.2823 | 2025-08-22 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| d2dbd3d7-0e88-37bf-a8c4-a94b2f47b989 | -12.5042 | -53.8091 | 2025-08-22 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 4fe8f422-15f1-3142-8a6d-63a9b857c7e4 | -5.7782 | -44.787 | 2025-08-22 14:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 120.5 |
| d91e5763-49cd-3d1b-8faa-d9fb7354d75c | -10.876 | -50.8163 | 2025-08-22 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 185.3 |
| e808576d-8db8-350e-8f30-bb611ffe2248 | -14.7691 | -56.054 | 2025-08-22 14:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 2af40c61-d8f9-3ef0-9e2b-8b03c38d3002 | -6.4449 | -45.5298 | 2025-08-22 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| eb0371db-a2e4-3465-a880-1e5b889ce5ab | -14.5956 | -54.7782 | 2025-08-22 14:30:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 24faeb6f-7e68-32df-8014-56c68054f1c0 | -14.3523 | -53.1191 | 2025-08-22 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 085eaade-3439-3355-93b8-afddde569aa4 | -8.7951 | -45.4238 | 2025-08-22 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| ca046693-4f36-3506-82f2-f059bec56c2b | -14.7501 | -56.0356 | 2025-08-22 14:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 190.8 |
| 7ca539cc-b4e6-38e6-b52e-fdc0ca709317 | -14.7722 | -45.3822 | 2025-08-22 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 178.9 |
| c31e91bb-0f63-3da0-8a85-1163e0dde537 | -7.6181 | -46.2616 | 2025-08-22 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 620946ee-297c-3cda-9885-5b1c500d4f0b | -9.8287 | -64.2635 | 2025-08-22 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 4d3c2ee0-05f6-313d-86fc-1778a7aa7253 | -10.8568 | -50.8396 | 2025-08-22 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 2284560b-d9f6-3cb0-9770-e7bb23b2c03b | -6.5196 | -45.5464 | 2025-08-22 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 127.8 |
| e6ecb350-451e-3d93-a764-283ab4411cf7 | -9.7632 | -62.7717 | 2025-08-22 14:30:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 69a88201-ebb6-3a48-8e9e-60b888505a98 | -10.437 | -48.3629 | 2025-08-22 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 321b7ae2-6f11-34f4-9526-e86c190b9da4 | -8.613 | -62.6118 | 2025-08-22 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 1017f6ea-815d-3cfa-a16e-3508a765cf85 | -8.8735 | -62.4305 | 2025-08-22 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 752bafe6-096f-3685-9d4f-a6a935a7eaff | -12.9524 | -46.2876 | 2025-08-22 14:30:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 065d6e75-53d8-31ae-af40-47830df12b9d | -8.8921 | -62.4297 | 2025-08-22 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 7b50df4a-b0a7-38dd-ab97-7c76be7918fc | -13.3966 | -46.2406 | 2025-08-22 14:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 148.4 |
| ab16f143-eaef-3a31-9ed7-d7a2b044a54e | -14.6713 | -54.8728 | 2025-08-22 14:30:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 26a57cba-42a9-3b31-9691-8cc5ffcbf6b6 | -8.4779 | -48.236 | 2025-08-22 14:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 54d30ee3-d031-3301-ab80-1177a1bcfaa8 | -7.6486 | -45.2218 | 2025-08-22 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 39ebc945-2b40-3eaa-8195-4443dd6fd1dd | -6.5781 | -59.871 | 2025-08-22 14:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 82be49aa-983d-32ee-aaf9-3c5538f63212 | -10.8757 | -50.8376 | 2025-08-22 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 394.1 |
| 5314e818-4318-356c-a287-a21703b5e928 | -9.6865 | -47.9409 | 2025-08-22 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| af9f9c94-24e3-3592-9c7e-1e76f7403944 | -7.0542 | -44.615 | 2025-08-22 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 5f0a9aa9-4d17-3418-8136-dfbfc2a77a1c | -7.1662 | -44.6736 | 2025-08-22 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 2e6212d0-1b70-3a4e-86dc-fe5f4623faee | -8.7759 | -45.4486 | 2025-08-22 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| c016a1bb-8449-372d-b182-79ff0edcb7b3 | -8.8736 | -62.4115 | 2025-08-22 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 84.6 |


[Clique aqui para ver as próximas entradas](README71.md)
