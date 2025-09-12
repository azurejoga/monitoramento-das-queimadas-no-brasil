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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70d2d29f-9ef6-322e-b42c-15089d057e61 | -8.2085 | -45.5981 | 2025-09-12 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 95.2 |
| e70d323f-6993-3715-af14-ff7e0a1422ec | -7.4511 | -44.4177 | 2025-09-12 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 23627a7a-1874-3a51-8ebd-96079a92f317 | -9.075 | -47.1002 | 2025-09-12 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 8ff419e4-5c59-39e1-a64a-b556e8d7f94a | -9.057 | -47.0355 | 2025-09-12 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 0d6e6af9-18b9-3609-9732-fc6a32b76b94 | -6.166 | -43.374 | 2025-09-12 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 4a550ddb-4092-31b7-894e-aeb6aaa537bd | -11.5422 | -50.6161 | 2025-09-12 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 382.5 |
| 5189743c-1ee0-363d-9902-d226370afe2d | -13.1838 | -51.7429 | 2025-09-12 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| b0d22355-e042-33c2-95b4-1a13418f465a | -8.956 | -46.1074 | 2025-09-12 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 5e1384a3-9380-38c7-a2c1-b7823f083e43 | -10.4438 | -50.6272 | 2025-09-12 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| b83a077e-fdea-38ea-9af9-9afec0e52fb1 | -11.5425 | -50.5947 | 2025-09-12 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 185.2 |
| e65ef8d6-6681-3979-b0b5-ee31f6d9584f | -8.8899 | -49.945 | 2025-09-12 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 18454193-8de0-3a52-bdf3-f0a8c5f84206 | -6.3808 | -44.4205 | 2025-09-12 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 95c58147-a01b-39be-9bfa-3256e8774eab | -15.5819 | -54.7637 | 2025-09-12 14:30:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 153.2 |
| ff5b9541-faad-3237-b7db-8ff8698b25f0 | -18.9304 | -46.8429 | 2025-09-12 14:30:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 8c505aea-9995-3533-b7f3-c9c724ca17f8 | -6.1735 | -42.6221 | 2025-09-12 14:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 141.0 |
| adfae6cc-4713-30df-8f40-6a04d55a72f1 | -11.5257 | -50.4469 | 2025-09-12 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 166.8 |
| e4c770bc-c231-3cba-8ac9-77c986c1ee77 | -10.0757 | -47.1463 | 2025-09-12 14:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 58c65d98-9a65-328d-bd9c-dabc66ef8f6f | -19.3534 | -50.7405 | 2025-09-12 14:30:00 | GOES-19 | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Mata Atlântica | 165.5 |
| f15cb287-b9b2-3b0f-a520-3dac59f4111d | -12.9292 | -54.7538 | 2025-09-12 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 284.9 |
| 05b03886-ac7d-3656-b6b0-04135d077e29 | -10.1405 | -47.9133 | 2025-09-12 14:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 9101d59b-d16a-302b-9786-f856ba649d81 | -6.8374 | -45.6108 | 2025-09-12 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| a5725e43-33a6-3633-817f-55bd552a6f1f | -11.429 | -43.5307 | 2025-09-12 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 254.2 |
| c7d473b6-b9a8-3e23-a555-cfa85894bbac | -8.9371 | -46.1094 | 2025-09-12 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 172.2 |
| 68411438-63c1-3a2f-914d-88e3f3a8ca01 | -7.5643 | -44.3838 | 2025-09-12 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 98a96195-d327-3a16-a99c-ae9ac8dd2be3 | -9.0939 | -47.0983 | 2025-09-12 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 16c9bb88-3ecc-3049-964f-5b7677075b2d | -9.0373 | -47.1041 | 2025-09-12 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 39ffa828-4193-387e-abad-6d19563e0a79 | -10.6983 | -48.6393 | 2025-09-12 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 5f0c720f-2f11-37ea-863a-a1fdc837b15a | -10.6979 | -48.6612 | 2025-09-12 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 00c7e526-82b1-3d9d-a1f8-9eeccf1fe516 | -12.9289 | -54.7744 | 2025-09-12 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| aadec8e0-a3ac-354b-a7cc-bfa35bdd61c2 | -8.9938 | -46.1034 | 2025-09-12 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 216.9 |
| 1798c294-0b66-33dd-b4da-ca5581b9c6f3 | -8.414 | -47.2766 | 2025-09-12 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 67c542a7-60df-3dfb-94bd-e17015632ce3 | -11.9532 | -51.1023 | 2025-09-12 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| e37e6e93-4b58-364b-a2f8-613e6b1d2d85 | -10.4252 | -50.6078 | 2025-09-12 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 7313551b-dd2f-347d-82bd-be4be928bb95 | -7.5458 | -44.3625 | 2025-09-12 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 1d04e8eb-4f5a-34c1-8bb1-e61aac9c53b4 | -6.2588 | -43.4828 | 2025-09-12 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 79f7a65f-8b53-3ba6-9e5f-7f5b16a2ace8 | -8.4143 | -47.2545 | 2025-09-12 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| fcbef2cb-2e2d-3f59-9378-9d559f4d3a44 | -12.8649 | -62.1268 | 2025-09-12 14:30:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 9f9130fa-edf1-3763-b716-346e593580c6 | -7.4508 | -44.4407 | 2025-09-12 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 2796cb4c-c2b1-339c-8678-d4c8cc0231bc | -14.7397 | -59.6989 | 2025-09-12 14:30:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 5e17314e-1456-3930-9ee5-209cefcd8c56 | -9.0748 | -47.1224 | 2025-09-12 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 390.9 |
| 9429ab20-ec0a-34aa-8cba-552d2bc4efa5 | -6.3092 | -42.2072 | 2025-09-12 14:30:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 116.7 |
| d36e62e0-1bd5-328b-abaf-07c9e1f9592e | -15.1406 | -50.1409 | 2025-09-12 14:30:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 146.3 |
| c05ba419-61c9-3012-8276-127568011961 | -16.5483 | -55.1826 | 2025-09-12 14:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 102.0 |
| cef842fe-ccf9-3155-81ce-7dbae522e1a0 | -7.45 | -51.8256 | 2025-09-12 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| e836fcce-4fc6-32ee-952a-53a76406a966 | -11.6821 | -46.5632 | 2025-09-12 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| ac4ac671-4ea9-3858-ab46-5cb51c10039b | -15.1402 | -50.1628 | 2025-09-12 14:30:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 276.3 |
| 788a54b0-aa9b-3951-93c3-0cfd94710f58 | -9.6473 | -48.0548 | 2025-09-12 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 3bc2c4d3-6e1d-3782-b8f3-9be2cc207f1c | -11.3718 | -43.5157 | 2025-09-12 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 9b946917-30d9-3033-aa6f-0f0ffd4530e1 | -10.8781 | -45.5826 | 2025-09-12 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 0c1bf573-b6e7-3a34-87aa-676b00e0d58d | -5.9466 | -42.7825 | 2025-09-12 14:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 60.6 |
| cc3e6cc3-a58f-3962-ae32-270b11e772f7 | -9.5324 | -54.6277 | 2025-09-12 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 145.0 |
| f7dd2c88-ede3-37eb-9d11-be48381a57b9 | -8.9563 | -46.0849 | 2025-09-12 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| b1d00984-2603-3849-84a9-dc4b0878771c | -6.1732 | -42.6458 | 2025-09-12 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| ef763d34-b1d2-3c4a-8565-057473a6f826 | -8.096 | -45.5641 | 2025-09-12 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 5aa5110b-afbc-30bb-a290-2273b77b9ed5 | -15.5822 | -54.7429 | 2025-09-12 14:30:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 1388efec-495d-3f02-9c87-3c894f623613 | -16.9621 | -45.8176 | 2025-09-12 14:30:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 159.3 |
| d30857d2-ed0b-31c7-9ff1-6862f2aaa180 | -8.8768 | -51.111 | 2025-09-12 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 01cc12c2-2cb9-3496-ab6b-8a7c94e5753b | -11.7192 | -46.6257 | 2025-09-12 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 269.8 |
| b48ee4f1-0454-3987-9f3f-7bf177aba5e3 | -9.0379 | -47.0597 | 2025-09-12 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 5e23057e-44a9-320f-a98f-cd43b0632f50 | -9.1328 | -47.0054 | 2025-09-12 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 1abdbf3c-6faf-3753-9d51-238fc5e439ca | -9.1331 | -46.9831 | 2025-09-12 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 142.7 |
| c46a060b-1a69-3248-a43b-4a4fdcdb8502 | -9.5322 | -54.648 | 2025-09-12 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| a6745ad1-06aa-375a-8306-530a1cfef8cd | -7.542 | -44.6844 | 2025-09-12 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 5bdf199c-c913-3464-ae18-dba83d622ef8 | -10.8972 | -45.58 | 2025-09-12 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| c1a94450-5600-3325-9b9b-ab5069b99f44 | -7.5641 | -44.4068 | 2025-09-12 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 93179d9c-3688-3016-9331-b326ba83d0ef | -6.3041 | -53.4562 | 2025-09-12 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 76d74139-8c5d-3ebc-8a97-f4350c926e60 | -6.3044 | -53.4156 | 2025-09-12 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| ae0eabb5-d2b6-33cc-81dd-6df54e08b443 | -8.4893 | -47.2694 | 2025-09-12 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 7131cb0c-d6cb-33c9-b193-d51528a418a0 | -9.5137 | -54.6292 | 2025-09-12 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 265.7 |
| ad65be23-20d6-3320-b590-b49a597c0758 | -9.0791 | -49.8211 | 2025-09-12 14:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 7a0ab0ea-ec25-336f-bf17-b598fe5b3bc6 | -11.526 | -50.4255 | 2025-09-12 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 189.6 |
| e980c1cc-5ce7-3ec0-8855-3fccffa89881 | -6.684 | -44.1189 | 2025-09-12 14:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 0266c8b7-f54e-3c70-8edc-d70a145c9399 | -9.0382 | -47.0375 | 2025-09-12 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| fbd97371-6367-3cf7-b962-4eb14b2dcacf | -11.809 | -50.5642 | 2025-09-12 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 912ae7da-fc4e-36f2-8097-1d34bc8cf365 | -9.0936 | -47.1205 | 2025-09-12 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 321.4 |
| 7ddbce07-7a27-3a38-be5a-fb9b423cb9ab | -6.6837 | -44.142 | 2025-09-12 14:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| ba27530f-1454-3a6f-9510-f176ce4f2697 | -12.0849 | -47.6065 | 2025-09-12 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 57a08970-0ebf-3d40-a1ef-53c7d87dbed0 | -11.4281 | -43.578 | 2025-09-12 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 2f596d2d-be80-32ed-8af5-06fb3eb4af82 | -8.9368 | -46.132 | 2025-09-12 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 254.7 |
| cbf35689-9158-3614-a1e6-36296a9ea49a | -15.0788 | -52.4331 | 2025-09-12 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| fa482cd0-7ddc-3561-9a6b-bd006d2d03f6 | -6.0704 | -43.568 | 2025-09-12 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 2d4a3a1a-afb9-3e94-a264-4695b9050bc6 | -16.3623 | -51.4969 | 2025-09-12 14:30:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 8ffbffad-0bc0-3870-a5e7-5f7ea2f86bef | -15.0863 | -48.0016 | 2025-09-12 14:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 879554a9-fdcd-322d-9fe0-d5d6b0cf315e | -11.9717 | -51.1427 | 2025-09-12 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 121.2 |
| a103f89c-714f-3b33-99a1-96c0f9330b57 | -15.1058 | -47.9983 | 2025-09-12 14:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 96.9 |
| ab9f1405-9bee-3107-85a2-44545b4f31a9 | -6.1908 | -42.7622 | 2025-09-12 14:30:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 57.8 |
| 5bdd3353-5d21-3519-a1e4-797e977ffcbf | -11.4473 | -43.5751 | 2025-09-12 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 15da9296-ef39-308e-8f97-eff214c81e34 | -10.8968 | -45.6029 | 2025-09-12 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 8b178cac-c345-31dc-b9cd-bfdf92ae24d4 | -9.9571 | -50.3353 | 2025-09-12 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 47a1f77f-e6f3-334b-888c-9c7e2b2f223a | -11.9529 | -51.1236 | 2025-09-12 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 425c439f-7e47-3fce-919d-dbc84201530f | -12.8256 | -47.9709 | 2025-09-12 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 9dbbb932-4e9a-33bd-a963-bd8a36da9ca1 | -11.4477 | -43.5514 | 2025-09-12 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 210.7 |
| be397518-0616-301a-a00e-506d83e361e5 | -11.7208 | -46.5353 | 2025-09-12 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| a9225fed-a3f9-3977-910e-fb0ac4fafb16 | -9.3433 | -45.4082 | 2025-09-12 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 208.1 |
| 8eaff1d4-bdf1-3d8e-946c-0c05509450f1 | -16.5099 | -55.1459 | 2025-09-12 14:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 92.8 |
| 4e75766f-158b-3b5c-b880-81e54e77f425 | -6.1894 | -41.0641 | 2025-09-12 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 106.3 |
| 38e768d0-6323-38e7-a478-6de899b5467c | -10.0947 | -47.1441 | 2025-09-12 14:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 130.9 |
| a2fad9f5-db3c-3aab-86a5-0accfd5fde69 | -9.72 | -46.8749 | 2025-09-12 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 514b2ce9-bd33-33c1-ab55-72f2b466f24c | -11.1949 | -48.4277 | 2025-09-12 14:30:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| bceea6b2-fcde-3a16-b87e-a57fe74e8e28 | -14.4588 | -47.3174 | 2025-09-12 14:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 99.4 |


[Clique aqui para ver as próximas entradas](README138.md)
