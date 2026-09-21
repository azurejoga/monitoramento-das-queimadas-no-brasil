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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af49eb4e-18ed-3de2-b16f-18a301046c61 | -10.3728 | -48.8936 | 2026-09-21 14:00:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 15858dc4-55c1-361c-ad57-089e9174e52a | -6.4486 | -59.9717 | 2026-09-21 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 1312b79a-e2b7-3189-a59a-ba8466b9946b | -10.9544 | -50.6165 | 2026-09-21 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| aa2d682c-632f-3c08-9cd0-70d2696df459 | -8.0279 | -61.3626 | 2026-09-21 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 57e5cdff-1f8a-3764-96b2-8d70723d71ed | -7.3289 | -55.2155 | 2026-09-21 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 9a8b4521-d7b1-3288-b1a1-db0b35300981 | -6.5453 | -44.8415 | 2026-09-21 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 546ac4af-d430-3c1b-885b-03456aa3bc9d | -9.5594 | -66.0359 | 2026-09-21 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 03d42636-7666-3d43-8d6e-a4345128b7c5 | -8.7914 | -48.7285 | 2026-09-21 14:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 102.1 |
| e41b8301-70e6-3da2-ad4f-d45ccc245fba | -6.7463 | -59.4416 | 2026-09-21 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| d6c3adef-fa9e-3975-acbb-a159a4e88bb1 | -2.8608 | -57.8188 | 2026-09-21 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| e2ef9617-e241-35a0-9b49-22bfe7b50264 | -9.457 | -45.395 | 2026-09-21 14:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| c76f972a-3a09-3bc4-a93f-8a86d688aa25 | -3.6947 | -60.5645 | 2026-09-21 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| e2b4f238-55bc-3050-8d58-ac91a2f6ea55 | -13.2602 | -51.7548 | 2026-09-21 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 642f756a-e338-371a-890b-493f7dc6d675 | -13.2794 | -51.7524 | 2026-09-21 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 8214f7b4-bd7d-331c-915f-61e474b7cd22 | -4.9535 | -45.1374 | 2026-09-21 14:00:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 8cb09a95-e0f9-39f2-a9e0-ea1d1b8b10bc | -11.8014 | -49.8129 | 2026-09-21 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.1 |
| d7860929-0e94-3f92-9c80-c8683b16dd46 | -12.8899 | -50.9695 | 2026-09-21 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 129.6 |
| bc2d5e33-bcd5-3724-b8b3-809d2380608c | -8.7706 | -45.8567 | 2026-09-21 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| a6fdfd85-a22e-38c6-80a0-a79c598d710e | -3.6946 | -60.5835 | 2026-09-21 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 671c3e4f-1a70-3b69-8f73-951c179ad187 | -12.8246 | -54.0442 | 2026-09-21 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 183.5 |
| eadea9a2-e62d-3b3a-a935-186d88ae55f4 | -16.9964 | -56.4525 | 2026-09-21 14:00:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 90.2 |
| bd82a7ab-f309-3492-b088-20e4eb644246 | -5.841 | -53.5205 | 2026-09-21 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| c9b9e075-691e-319c-988e-c578bfd78ed4 | -5.8225 | -53.5214 | 2026-09-21 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| c8c1ab63-ab1e-3a36-9c4a-48b98a165415 | -11.0991 | -54.0285 | 2026-09-21 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 9fa6ba10-f187-3e72-88d5-52bdceacccc1 | -7.5703 | -57.6962 | 2026-09-21 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 0300f765-40f0-3e8d-baa1-399f4896b653 | -5.757 | -47.2915 | 2026-09-21 14:00:00 | GOES-19 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 23cc050b-2237-34d6-a8ef-adcd0f190213 | -6.6761 | -50.9381 | 2026-09-21 14:00:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| d6b6ca11-223a-3bb9-9f7c-f52f2d41fc39 | -6.8033 | -59.15 | 2026-09-21 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 3f625ea1-6ad2-3c6f-a7a9-22fa5ebb06b9 | -8.727 | -44.8607 | 2026-09-21 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 06b49b04-a9c1-3333-bd2c-7c3774927587 | -8.0094 | -61.3633 | 2026-09-21 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 772cd0b0-d445-3d8c-bac5-69e7edf81bd2 | -6.3382 | -59.9566 | 2026-09-21 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 3747a770-76b9-3fb2-be33-4792aac86c1c | -4.2239 | -48.6127 | 2026-09-21 14:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| c1b5783c-3585-3b69-9c56-80d1f914fe8d | -10.3549 | -50.2099 | 2026-09-21 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| cc360b33-c04c-30c0-a351-128046552c27 | -5.7615 | -57.5807 | 2026-09-21 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| c440ef53-b3c6-3249-9b7d-9a652a869e9d | -6.392 | -45.1948 | 2026-09-21 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| d9e3a302-5475-3d8b-905e-10c6d9fa9645 | -10.3725 | -48.9153 | 2026-09-21 14:00:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 33c1e972-33b8-30de-b967-b34237077478 | -9.5593 | -66.0545 | 2026-09-21 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 4fa8da10-e969-364c-8637-1e1906125798 | -6.728 | -59.423 | 2026-09-21 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| b4af9772-f35b-3b6b-bb0d-144ee21f37f8 | -10.7999 | -50.8455 | 2026-09-21 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 6e1c0d71-a21b-3682-830a-f39352f67f70 | -6.7184 | -55.0884 | 2026-09-21 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| a75fc163-2ea1-383f-8c0c-1adaf3cb2f6f | -10.3914 | -48.9133 | 2026-09-21 14:00:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 379588cc-14be-3ac8-9f12-4f5c11fb7264 | -9.831 | -48.4292 | 2026-09-21 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 16b3116e-07d8-328a-9f87-7cc39c85765b | -6.5444 | -44.9327 | 2026-09-21 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 7669be40-318d-3a66-849e-3ee0440352c5 | -8.1686 | -54.7634 | 2026-09-21 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 758eba74-e57b-39c1-9aa3-f32ed4eabe3a | -5.1984 | -56.1103 | 2026-09-21 14:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| f04f6396-93f5-3283-84c5-8d8b5363e240 | -6.8034 | -59.1307 | 2026-09-21 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 848ffbcf-fcf3-39ef-983c-9ab8e2c19c5b | -10.8011 | -50.7604 | 2026-09-21 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 5ef85266-a4aa-3a2a-b875-76e67cc89317 | -5.6223 | -43.3701 | 2026-09-21 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 280.6 |
| 18dd4901-b5fa-3880-b37b-ca94a105e4e8 | -6.5571 | -45.5434 | 2026-09-21 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| d850c9e0-6d2f-3a9b-b1c1-25588fd5160e | -13.4331 | -51.7334 | 2026-09-21 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| c5930af5-6713-3c04-b6d7-2bb18a41a9b4 | -14.5406 | -53.3896 | 2026-09-21 14:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| cc497e92-1d45-397d-9a22-541fdc6758e6 | -11.1183 | -54.0062 | 2026-09-21 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 300d15e5-e392-3524-9dc4-85692edc4463 | -7.5247 | -46.2252 | 2026-09-21 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| b360a010-e243-39ff-b16c-aba23566bc06 | -14.0989 | -52.1376 | 2026-09-21 14:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 9ae9c12a-cc64-3a8c-89b5-c82c2b381dba | -3.4454 | -58.2327 | 2026-09-21 14:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 94.2 |
| ff7e7588-2a3e-3900-973e-46275d33b06d | -6.8571 | -45.5189 | 2026-09-21 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| b4d6ef30-ecfa-38b1-89e5-245092d0b468 | -6.7369 | -55.0874 | 2026-09-21 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 618145e5-7ede-3d2c-b3aa-81d73385fc92 | -5.9985 | -45.2476 | 2026-09-21 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 2a9769e6-472d-379b-943c-eca6af882245 | -12.3028 | -50.6559 | 2026-09-21 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| ec99250a-3584-3c60-883e-ed5ba0c677bb | -10.7521 | -46.3252 | 2026-09-21 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 00d345a7-6ef1-37c3-9696-093f9136b30a | -10.3917 | -48.8915 | 2026-09-21 14:00:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 20c012ec-42dd-39fd-9bfc-3c36bdd21e3e | -11.8682 | -46.8529 | 2026-09-21 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 624654d0-6858-3be0-8c3e-15d354f3f594 | -7.5059 | -46.2269 | 2026-09-21 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| dbe74f13-3058-36e0-b9ea-06bbbc15a5ee | -5.6411 | -43.3687 | 2026-09-21 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 12e8e2d6-a7e2-373b-955c-be10db62bdf1 | -9.4567 | -45.4178 | 2026-09-21 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 744471d3-7b33-3b8e-9a54-5f23ead615d1 | -10.3924 | -50.2275 | 2026-09-21 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| f9d423b9-dc34-33e4-9fd9-1c4967d39596 | -12.4204 | -47.0228 | 2026-09-21 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 258.8 |
| 1630a1ff-8e92-32c0-988a-0aa8c3162efd | -10.4919 | -51.279 | 2026-09-21 14:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 3e0ef8fc-897f-3350-818a-65eaaad82d17 | -9.2383 | -46.1668 | 2026-09-21 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 7a89d8f6-da39-3a8c-a406-244d2f9c2406 | -8.1872 | -54.7622 | 2026-09-21 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 33aebd07-e3e4-3c1a-96ad-74e5205bffba | -10.7655 | -50.5939 | 2026-09-21 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 3c041641-2822-31a6-9c53-d71e4044a898 | -10.336 | -50.2119 | 2026-09-21 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 4096a7fa-29f2-3360-8bea-78446c3bbcc2 | -3.6946 | -60.6025 | 2026-09-21 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 15ebd4bf-93a3-380c-8725-0197376071bf | -3.753 | -59.419 | 2026-09-21 14:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| fdbbd5ee-6ff9-329f-ad72-1acd0b862596 | -5.7504 | -43.7091 | 2026-09-21 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 8b618dfb-f7b5-3d93-ba75-1ed02d0a2135 | -6.7464 | -59.4223 | 2026-09-21 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 180.4 |
| dff5f1a1-5bb4-3d24-9daf-c570b21fd87d | -12.2914 | -50.1633 | 2026-09-21 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 143.9 |
| f0689259-88d6-353c-9586-b99841e61070 | -10.8556 | -50.9246 | 2026-09-21 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| ebd2396a-45fb-3466-b63c-99b3ddf448de | -6.6763 | -50.9172 | 2026-09-21 14:00:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 9e1701ba-23ea-3e56-9bc3-4639be2608a1 | -13.2596 | -51.7973 | 2026-09-21 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 180.8 |
| 1fa831bf-80c1-3bfe-991e-a64afa43d497 | -10.8735 | -53.9668 | 2026-09-21 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| bd8b3136-40fe-30ae-a81c-a4629eda90de | -11.6431 | -50.2191 | 2026-09-21 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| f512d0f9-e701-3ece-944a-f2d6b486ddbb | -11.041 | -54.1567 | 2026-09-21 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 847139f1-7216-3657-bbeb-39d156427327 | -11.8491 | -46.8556 | 2026-09-21 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| a38fcf49-8950-3846-8717-e02dd48de31d | -6.8264 | -55.5222 | 2026-09-21 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 8a1b6b9b-0f8e-3847-a13f-7e0d603e52e2 | -12.5415 | -50.046 | 2026-09-21 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 78cfb997-279a-37af-a178-d95423861184 | -2.8791 | -57.799 | 2026-09-21 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 3ed883e2-79d3-3fbc-baaa-8f0dc7d18f34 | -9.8066 | -46.1023 | 2026-09-21 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 5d4966eb-d3a5-35af-9fc7-e9b2cd2b9c96 | -9.3986 | -48.3213 | 2026-09-21 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 31a3f3c3-2e38-33d7-ac5a-df34d21dea21 | -5.8408 | -53.5408 | 2026-09-21 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| fe2b6e41-ec33-35d7-be75-4b76d3244743 | -11.6802 | -43.4209 | 2026-09-21 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 171.2 |
| a473bc7b-02c5-3265-81ed-e1b95898dfcb | -13.3251 | -51.2997 | 2026-09-21 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| dda810fe-f5ed-343d-9201-e2655bdd66e5 | -3.1698 | -58.5859 | 2026-09-21 14:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 8cb68b80-5e45-36c1-805b-4186535d4250 | -15.4471 | -48.4566 | 2026-09-21 14:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| ac022748-fd6a-32b8-b1aa-a67586394c26 | -10.955 | -50.5738 | 2026-09-21 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| f30bbdcb-99ce-3b87-ab8d-c3a33e685d6f | -6.8263 | -55.5421 | 2026-09-21 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 393f5a9c-41d8-37f0-914f-f6fb6d0d0be0 | -6.7484 | -59.075 | 2026-09-21 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 300dc479-e04f-34df-88a7-d4604b96fdca | -6.5759 | -45.5419 | 2026-09-21 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 193.4 |
| eb896385-e688-3dfe-9341-5c61d4e4a25b | -14.0993 | -52.1163 | 2026-09-21 14:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 78aa74f4-dc96-33d0-bb16-4eb93518c793 | -10.8002 | -50.8243 | 2026-09-21 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.9 |


[Clique aqui para ver as próximas entradas](README124.md)
