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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c1b8910-e8ca-36bc-9952-859e652fd70d | -3.3309 | -59.8673 | 2026-09-22 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 25738347-eec8-3c11-960c-cc0a0c8cdb25 | 3.8953 | -60.7313 | 2026-09-22 15:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 8ba5b594-e64c-3e67-b65d-72a9ccb81ae2 | -8.1304 | -62.8763 | 2026-09-22 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| dda1f9d9-8764-330b-b1bc-33ad8bd6754a | -7.5548 | -48.6843 | 2026-09-22 15:10:00 | GOES-19 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 92.8 |
| ee5867e4-7442-3811-986d-e0dbdb5ff2de | -3.3183 | -57.8677 | 2026-09-22 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 8686ec2c-93c4-38d5-b9dc-8d42d1541efb | -5.8159 | -57.7346 | 2026-09-22 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| bd17d2da-2d65-345c-b5b2-12cead42562c | -3.331 | -59.8292 | 2026-09-22 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 980e42d9-2da5-3230-b03c-ba45e831311f | -3.3821 | -61.2901 | 2026-09-22 15:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 95b0c5d2-f2e8-3c47-883a-d5d8c7d126e2 | -2.4206 | -58.2712 | 2026-09-22 15:10:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| f1172e6e-0b39-3854-9610-bef7ce834462 | -6.295 | -57.735 | 2026-09-22 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 31b0452e-8bfa-3147-bd0f-98f6e79b559a | -3.1902 | -57.851 | 2026-09-22 15:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| b5c0f5eb-7a26-3ee2-b017-6b6d1fef9ee8 | -2.9709 | -57.7197 | 2026-09-22 15:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 5e883109-4c8e-35bc-823b-6d470c17e906 | -6.5455 | -56.033 | 2026-09-22 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| fe8fc429-5931-363e-8db8-73a44c48a8ed | -3.7364 | -58.8626 | 2026-09-22 15:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| f4bef469-4c7a-334f-9bd8-2cc2fec78d2b | -3.1278 | -60.6889 | 2026-09-22 15:10:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 99003c31-2487-3e3e-a101-1f074b885e48 | -3.7547 | -58.8622 | 2026-09-22 15:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| da9d67d5-faf5-308f-bde7-c6baf63d6c7b | -5.8595 | -53.5196 | 2026-09-22 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 16c099e6-b9dc-3ec5-a510-7b8236476962 | -9.6111 | -43.9243 | 2026-09-22 15:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 596.7 |
| a7c93fef-9e4e-3d45-ba38-1c47d7d6a2ae | -10.8002 | -50.8243 | 2026-09-22 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.8 |
| ade62b07-98e5-3546-a667-3f30a8423ac7 | -11.3972 | -44.2401 | 2026-09-22 15:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| ca507536-cee0-36e4-b12b-6277e13235eb | -3.132 | -59.029 | 2026-09-22 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| d3b6eba2-3079-3793-8949-ae1906b7f56b | -9.3797 | -48.3232 | 2026-09-22 15:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 5ef6d4e7-7563-3017-b8c5-7239ec67086c | -7.1273 | -48.4366 | 2026-09-22 15:10:00 | GOES-19 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 34c79783-b9f6-32e5-9e55-45fd187021c7 | -10.3916 | -50.2916 | 2026-09-22 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 8d323b02-9a75-386f-a205-569b3a17255c | 2.2003 | -50.8773 | 2026-09-22 15:10:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 21ace2e8-8f62-3d0b-b63b-a836973c502e | -6.7637 | -59.6334 | 2026-09-22 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| a08720b7-6dd4-3cda-899a-fb04a9ec3bb6 | -5.6223 | -43.3701 | 2026-09-22 15:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 9c5db411-8d38-3911-a2d9-d2ff94644200 | -3.2183 | -61.0472 | 2026-09-22 15:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 498a5439-faf3-325b-9847-cae3ae8a9ece | -12.6799 | -50.9526 | 2026-09-22 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 78c3e8a7-c8e2-392f-bebc-2d6c86260483 | -3.3321 | -59.4469 | 2026-09-22 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| ab80b442-557e-3b83-b4c7-f5f1f20e3f70 | -5.8489 | -49.7875 | 2026-09-22 15:10:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| d1b3e37d-183d-3f53-aa23-735b45aad8e3 | -3.3138 | -59.4281 | 2026-09-22 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 90c2ce9c-da42-37a1-b765-cbee01bc0640 | -5.7615 | -57.5807 | 2026-09-22 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 50cc9184-1b6a-337d-ab33-55299a257036 | -2.5492 | -58.0179 | 2026-09-22 15:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 2c74f2ac-3bd7-31af-88b7-9476e0c2fa3f | -2.9998 | -54.1889 | 2026-09-22 15:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 15069987-ce8b-31fc-b46d-14c1f8a622d3 | -3.4214 | -60.2086 | 2026-09-22 15:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 811fcc8d-e875-3097-8aba-74192eaf7a3a | -3.6813 | -58.9216 | 2026-09-22 15:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| e453f106-d7ae-3551-8fc9-9c9b0ea2e236 | -11.3784 | -44.2195 | 2026-09-22 15:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 497.1 |
| 5b06044d-04ce-380c-8ba6-5bb7b8b8eb53 | -9.8404 | -46.3911 | 2026-09-22 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 232.7 |
| 824edbf1-5a0a-37f8-943b-aa3b675196ee | -3.4272 | -58.1945 | 2026-09-22 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| c34a9fd2-19ac-3634-8b72-045e3c52b516 | -9.247 | -57.1488 | 2026-09-22 15:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 50687094-25f1-3a1d-8c11-034ed3a97533 | 3.9315 | -60.8633 | 2026-09-22 15:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 73.6 |
| c6267ebc-da5c-31ef-9b08-17496256e381 | -6.5449 | -44.8871 | 2026-09-22 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| bf818199-4287-3f03-a657-945641289842 | -8.1496 | -54.8049 | 2026-09-22 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 064710cf-43e2-33c8-86b8-28d62a6a46a0 | -8.4799 | -57.6085 | 2026-09-22 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| ad49c881-5f75-3d96-86af-1f94d7a15833 | 3.859 | -60.6561 | 2026-09-22 15:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| ad0988d4-2d88-3108-a73a-5f3e0df92cc4 | -9.8118 | -48.453 | 2026-09-22 15:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 7514a900-8462-387b-becb-6d4adff9d23a | -1.5858 | -54.4353 | 2026-09-22 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| ea22da89-07f0-300a-a5bb-c99edb168d57 | -10.3546 | -50.2313 | 2026-09-22 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| a6c84788-8cd5-31e6-b228-e8b13e285bf7 | 4.0579 | -61.4095 | 2026-09-22 15:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 1cbcb6eb-3034-3c90-8b31-982dea3e9b92 | -3.4003 | -61.2898 | 2026-09-22 15:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 82279f06-0286-38fb-b6af-598779abaf79 | -5.8411 | -53.5002 | 2026-09-22 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 5f4ec617-f7e2-33a1-a45c-024e3c3097cb | -3.3493 | -59.8288 | 2026-09-22 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 4607ba4f-b574-343b-804d-cd571af7654d | -2.9723 | -57.1945 | 2026-09-22 15:10:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 4500e181-8490-3e97-8d09-b145c6ca6c92 | -6.4302 | -59.9724 | 2026-09-22 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 110.9 |
| e1afa2a4-a38d-3b6e-af7e-e8b719691518 | -10.7997 | -50.8668 | 2026-09-22 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 131.9 |
| f663ad70-1571-30e2-b035-798cc5ba6840 | -12.9273 | -51.0291 | 2026-09-22 15:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| b4c1077c-062d-3712-ab22-9c4dcd25d6c0 | -6.3196 | -59.9956 | 2026-09-22 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| ee3a602e-db83-3379-8320-9c5eab4acdea | -3.3136 | -59.5046 | 2026-09-22 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 563aea22-b7fe-3bd9-99bb-c763dfc283ab | 3.9503 | -60.7111 | 2026-09-22 15:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 754b094e-399e-3da3-9e42-f6af26f28c08 | -8.3134 | -44.7446 | 2026-09-22 15:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 4d394e55-dbb8-3ae1-85d1-bc4c47be9271 | -10.9068 | -47.3808 | 2026-09-22 15:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 8cc8b382-bb38-37e4-8fe0-2a029a05e2aa | -7.9172 | -61.329 | 2026-09-22 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 2472719a-31e1-3176-a4a1-fbcc07313629 | -2.9999 | -54.1688 | 2026-09-22 15:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| d7fcf6e9-4ebf-32ea-8a76-0f6eb2fd61d5 | -5.4179 | -60.2166 | 2026-09-22 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 5fe527e8-34b8-3605-b982-08ab29fcd8ce | -3.0534 | -61.2767 | 2026-09-22 15:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 5f0ea8ff-2839-3f67-a6dd-700fdad807cd | -3.6814 | -58.9023 | 2026-09-22 15:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 543cbc43-066d-3832-9a54-fbc1649d10a5 | -3.6215 | -60.566 | 2026-09-22 15:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 54e7e379-6207-3bae-afcf-fd46b55b4214 | -3.6447 | -58.9224 | 2026-09-22 15:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 431fd07f-b28c-321c-a9e9-558b7803617c | -3.3358 | -58.1384 | 2026-09-22 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 500824b4-ecf4-397b-99de-ebf07d331c66 | -12.2827 | -50.7226 | 2026-09-22 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| da75c2b8-954e-3b81-9d36-25535a2e12e0 | -11.118 | -54.0268 | 2026-09-22 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 88a9726b-f534-3dfd-a897-866b922324fb | -11.3976 | -44.2167 | 2026-09-22 15:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 196.6 |
| b09ec3cd-6d3b-3291-a8ac-60f87e8c0ce4 | -6.2219 | -45.3665 | 2026-09-22 15:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 521a041e-a850-3b96-9940-38cc0b3ba417 | 4.0595 | -60.8795 | 2026-09-22 15:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 68.5 |
| d2c5c579-2e3c-3f2a-8fd1-d11fc941e973 | -10.6875 | -50.7722 | 2026-09-22 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| c0732a60-1a99-3573-89aa-8de3e2379e86 | -10.7999 | -50.8455 | 2026-09-22 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 117.8 |
| c6964b69-8565-3f49-be68-489e6364ffe9 | -3.3638 | -61.2904 | 2026-09-22 15:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 8d92bd50-2edc-3742-916d-b61aacd3013b | -10.0295 | -52.0991 | 2026-09-22 15:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 67268e1c-0270-3bfe-a0a5-aca1b4ce8c38 | -3.2817 | -57.8685 | 2026-09-22 15:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 676d402c-b39d-3356-9bec-74cc7d6b59e9 | -3.3138 | -59.4472 | 2026-09-22 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 21885db3-e71c-3a12-9470-7442f5bdfc82 | -9.8514 | -48.3178 | 2026-09-22 15:10:00 | GOES-19 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| ee90021e-7f50-343e-b328-5d361aa46063 | -9.2491 | -48.2272 | 2026-09-22 15:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 79a9e09f-03a9-369b-af95-1327c9f6b902 | -6.4301 | -59.9916 | 2026-09-22 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.2 |
| ef5de9ff-dfed-30a6-90eb-19f328e03306 | -10.6878 | -50.751 | 2026-09-22 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 126.1 |
| babf9e8f-e656-3199-a8ee-0ca4e8008ada | -6.6098 | -45.8991 | 2026-09-22 15:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 74c1334d-4b00-3bcb-8852-14f562aa304c | 3.6753 | -60.9443 | 2026-09-22 15:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 63.6 |
| af649d7d-1dc0-3d06-8046-9da436a23e4d | -7.0619 | -47.4826 | 2026-09-22 15:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 84120fed-f785-324e-957c-c00303f408a9 | -10.1179 | -45.5662 | 2026-09-22 15:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 89.9 |
| a7ae384b-744d-362b-a709-84f3ad47424c | -7.5705 | -57.657 | 2026-09-22 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| beb75795-53df-3a02-b593-6bdb50150406 | 3.6753 | -60.9632 | 2026-09-22 15:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 6f83db5e-c592-31f1-a98c-cc951463852a | -3.3134 | -59.5812 | 2026-09-22 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| b3416986-524a-3ae2-a255-80d482a31549 | -11.378 | -44.2429 | 2026-09-22 15:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 177.8 |
| e8f8bfef-addc-34a0-8a7e-d086999d439b | -3.2818 | -57.8491 | 2026-09-22 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 7d5828ed-8f4c-328d-b467-634a1ae27e28 | -9.788 | -46.0819 | 2026-09-22 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| d4b4a78c-c639-303a-9214-1c04e950244c | -3.6032 | -60.5853 | 2026-09-22 15:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 5b2e3241-e199-35bd-9c22-b01352252b37 | -10.8941 | -50.8782 | 2026-09-22 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.8 |
| f8b07c1c-e10e-305a-ab6b-41974910a809 | -5.9152 | -59.933 | 2026-09-22 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| d7b84354-03b6-32dc-9e00-1bddd42a7ca6 | -12.4182 | -45.0385 | 2026-09-22 15:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 281.0 |
| a89b256c-746b-3dcd-8785-a553db9720b9 | -2.9723 | -57.214 | 2026-09-22 15:10:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |


[Clique aqui para ver as próximas entradas](README148.md)
