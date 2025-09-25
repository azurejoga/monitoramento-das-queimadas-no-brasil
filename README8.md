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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 966ac231-6097-327d-ba0e-31e6be78579a | -6.4319 | -43.0707 | 2025-09-25 03:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 216e8935-e4e3-3aaf-a60f-c3c1c71db5ed | -17.9312 | -55.8548 | 2025-09-25 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.5 |
| 56c626bb-d88b-31cc-9347-90f9edaaabf6 | -6.4317 | -43.0942 | 2025-09-25 03:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 54640fce-480c-334e-aaee-a1890f3bc2f0 | -21.9929 | -49.5054 | 2025-09-25 03:40:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.4 |
| c30365f9-33f6-3c89-a227-c36d30077558 | -6.4129 | -43.0958 | 2025-09-25 03:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 45511fd7-3983-34c6-8be2-8942de3eb5cc | -20.9925 | -50.0261 | 2025-09-25 03:40:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 127.8 |
| 6bbe57f6-8724-3909-9d75-063c56960b83 | -16.8538 | -50.5026 | 2025-09-25 03:40:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 8e85f29b-3da4-3160-94da-611cd3e3e0ba | -17.951 | -55.8522 | 2025-09-25 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.4 |
| 275bba38-2275-3b1d-8875-e34da3f95365 | -20.9931 | -50.0032 | 2025-09-25 03:40:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 105.9 |
| c98ea7e1-0069-3d55-9e50-e648741bcc25 | -21.9721 | -49.5102 | 2025-09-25 03:40:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.1 |
| 44a7ad9a-3863-3c3f-8157-9fb335f2609d | -3.30494 | -42.17662 | 2025-09-25 03:40:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 794c3f0c-6002-3515-86f8-dc79299edae3 | -5.61361 | -43.00116 | 2025-09-25 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4582b77d-b6b4-3ac6-8161-f281b954d0e3 | -4.7686 | -42.70369 | 2025-09-25 03:40:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f503d0b7-5105-36c3-8fd1-86209793319e | -3.80463 | -41.56914 | 2025-09-25 03:40:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| c24406d7-c681-3816-842d-26e8a45327ac | -4.60739 | -43.91454 | 2025-09-25 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4489be5f-1a8d-399f-b34e-4b4ab41e270b | -3.39608 | -47.50377 | 2025-09-25 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66709529-127d-3f0c-a73b-db648bcb74c2 | -5.6146 | -42.9955 | 2025-09-25 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 76d1064f-e0c9-3e10-a40a-c7fec40120b8 | -5.09181 | -37.60847 | 2025-09-25 03:40:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 70afdcb4-359d-3629-a219-71651c817559 | -3.78696 | -41.73096 | 2025-09-25 03:40:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 090574b1-059f-3bdc-bb88-1f9213452d9a | -6.70768 | -35.00176 | 2025-09-25 03:40:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4db9fab8-9baf-3b79-8277-57765f6eac01 | -4.79837 | -47.28225 | 2025-09-25 03:40:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7e4c4f1-536a-3486-b575-36e23c787a2c | -5.9315 | -42.92327 | 2025-09-25 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| fa0f8b09-d8f4-3b1e-8690-bc7dd97f1c5b | -5.79124 | -42.8044 | 2025-09-25 03:40:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b8132a11-cbfb-3def-b1d5-0d81afaee387 | -5.53998 | -42.80391 | 2025-09-25 03:40:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f96d4f10-0ec0-32c2-97e7-d60a638cbf22 | -6.14595 | -42.45776 | 2025-09-25 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c3346e38-7ecf-32fd-97d8-7a0addf1e199 | -6.11815 | -44.00034 | 2025-09-25 03:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6d9e32e-02fc-3a78-85e5-b9540741c892 | -2.82839 | -46.73363 | 2025-09-25 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2464d01d-db3a-32eb-a2fd-d9670fc48374 | -3.78614 | -41.7359 | 2025-09-25 03:40:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1d5ab40f-c6d5-36cb-bce9-15c1aa399518 | -5.08461 | -42.99594 | 2025-09-25 03:40:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14555cf9-788e-3797-b8fc-d43c289505b3 | -4.79736 | -43.53266 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 08071ebb-24ed-3840-821b-83650f0c82d8 | -4.74687 | -43.25846 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3544e0b7-d563-3295-b33a-ea097927a112 | -5.78635 | -42.80373 | 2025-09-25 03:40:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cac2d080-7034-3ed4-86df-426a907b48d0 | -4.74547 | -43.61531 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a149e171-ee46-340c-9fd0-d263c4e29962 | -2.91441 | -40.39073 | 2025-09-25 03:40:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 27ead5e3-4e73-3722-bbef-ddafb670a0bc | -5.0892 | -37.60463 | 2025-09-25 03:40:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8105ff95-5808-371f-9abc-306d1a165fa2 | -5.94995 | -42.90433 | 2025-09-25 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 969214be-5981-32f2-992c-936a8d25e6bf | -5.1618 | -42.05712 | 2025-09-25 03:40:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 998dd577-c6b4-3b3f-aafe-f8d3ac50e1fc | -4.80719 | -43.53778 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 63eab495-59e7-3db7-bcb4-a62c0422a956 | -3.80383 | -41.57392 | 2025-09-25 03:40:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 14fdad22-00a0-3ba2-94c2-5a76c03ffbbf | -3.23679 | -46.79868 | 2025-09-25 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e6edcf9d-fb36-3f1a-aa0d-28fe57e39cd9 | -2.9218 | -48.31886 | 2025-09-25 03:40:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| ce1ce46b-0a66-3d45-a2ac-eca5b6a8c35f | -5.88684 | -43.2044 | 2025-09-25 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4d993fa2-536d-31fe-9e0c-836a3055a849 | -4.80147 | -43.53991 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ee862f6f-772e-36b9-b80f-895a111f8cef | -4.66954 | -48.16444 | 2025-09-25 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1f58f531-69fb-3be3-ac79-81376b3b2e56 | -4.78203 | -43.20564 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98ce61e3-8076-3cb6-933f-46b0d27fd9f7 | -3.79163 | -41.73182 | 2025-09-25 03:40:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| df21fc52-7631-3fa5-9b6b-c20a201c621c | -2.82749 | -46.72814 | 2025-09-25 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6dc22429-1b9f-3cca-a6f5-fb19079f6c6b | -5.24489 | -43.08053 | 2025-09-25 03:40:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 008a3d1a-7fa6-3a0c-bebc-4ec875b2d0d6 | -5.5439 | -42.81035 | 2025-09-25 03:40:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7ab4d640-20de-30f5-ac5a-bdeeeac0e9e3 | -4.80201 | -43.53675 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3aeac434-2065-3330-981e-4b3de87866ba | -5.29322 | -35.56929 | 2025-09-25 03:40:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5bdd6ab6-e15d-3fd1-a3c2-9df35c0177f0 | -5.08363 | -43.00158 | 2025-09-25 03:40:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc563cc6-f43b-31fc-9897-ec64c59cbc0c | -6.12339 | -44.0013 | 2025-09-25 03:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0573ef9-25d3-367f-94b7-2b81d0ee6508 | -5.93543 | -42.91612 | 2025-09-25 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| aca8dcb9-c6f3-3a70-8a9e-c6e3ddcfe3da | -5.9374 | -42.9184 | 2025-09-25 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4568668b-6c67-3390-9bad-37c4e54d6ebd | -5.38729 | -42.28974 | 2025-09-25 03:40:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 06211c2d-dd79-3500-a46e-37f56c88ecaa | -4.77135 | -43.2069 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 25c1bd07-9583-361d-bf0d-4692931640b0 | -5.23291 | -43.69527 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7a1521b-455b-355f-9e1a-3c5484e7daad | -4.76372 | -43.25203 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eb19394d-1b9e-3a70-8902-c1e3525a7c6e | -5.23183 | -43.70161 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f16a784f-ce6e-3efb-b8ed-967958f86545 | -5.88732 | -43.20155 | 2025-09-25 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 12488544-b3b7-39bb-8311-3f86903d05c3 | -5.39152 | -42.27212 | 2025-09-25 03:40:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| de19a105-d4c0-330e-b99d-2afd3a11071e | -5.52601 | -43.87144 | 2025-09-25 03:40:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fbc1c71-cde0-32d7-9a26-f3d84d51b894 | -5.95187 | -42.90811 | 2025-09-25 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 8d4a8966-d1ba-38b8-815d-bc83e85955fd | -5.15713 | -42.0563 | 2025-09-25 03:40:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 94552519-9101-3346-95f4-d89033f945fc | -3.7908 | -41.73676 | 2025-09-25 03:40:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 80667b3e-e5a5-34c8-82b3-98d8343dfdbe | -3.7853 | -41.74085 | 2025-09-25 03:40:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 34e42486-c4b7-31fa-a72f-624261c7fe14 | -4.46116 | -41.92347 | 2025-09-25 03:40:00 | NOAA-20 | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a5d3ae82-ea2a-3af7-beb0-5473a1c9375c | -4.76321 | -43.25505 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc699c62-d1c0-3009-8db5-97ad32b957cf | -5.52073 | -43.87066 | 2025-09-25 03:40:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4c0f211-edb9-3248-a7b8-b4bf7c82faff | -2.92306 | -48.31152 | 2025-09-25 03:40:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 35d10793-94ca-3a66-8e4c-9b87c9a6eaa8 | -4.79937 | -47.27659 | 2025-09-25 03:40:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9d720c91-788a-311e-b772-2c145115a49f | -5.93928 | -42.93639 | 2025-09-25 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| e0f3abf5-482d-37ea-963d-82bbabe1aa40 | -2.91008 | -40.39002 | 2025-09-25 03:40:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 11.7 |
| c04a5f45-703b-35de-832d-99bf68b57b2a | -3.99647 | -38.33379 | 2025-09-25 03:40:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2f24ba47-d415-30f8-bbf0-85b1ccdfa581 | -3.30405 | -42.18195 | 2025-09-25 03:40:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c0cf66a8-e06b-3f7c-9098-3b6a30731dc8 | -5.95487 | -42.90495 | 2025-09-25 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 0947f72b-df66-31f1-9af8-e6f392df3bf2 | -5.93453 | -42.92147 | 2025-09-25 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 6922030d-afc3-32e6-8f64-be8bc5c39319 | -4.75299 | -43.25338 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba642056-9bb1-3fc2-8e55-6eecbaebad82 | -4.22603 | -38.0885 | 2025-09-25 03:40:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d4303464-320e-3410-9382-07a6780ed697 | -4.74738 | -43.25547 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e27aaf93-c59b-3ea4-a957-1a7392d70072 | -6.06468 | -44.08779 | 2025-09-25 03:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2b5e2efb-ab84-3b99-8562-336d91f35d9a | -4.78662 | -43.20947 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65eb4b5b-029b-3f78-b412-bf821eac82b4 | -3.99429 | -38.33136 | 2025-09-25 03:40:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 467f5815-6c5b-3410-a2b2-07f49240d06f | -2.91588 | -48.31022 | 2025-09-25 03:40:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a91ddbb1-50bd-386e-8178-f67cee55480b | -6.14121 | -42.45701 | 2025-09-25 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 242a9869-358f-3928-a416-396c3265986d | -6.31941 | -41.88807 | 2025-09-25 03:40:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3a9211f3-8a15-3534-ac53-78c0e6cbb5d8 | -3.1766 | -42.94918 | 2025-09-25 03:40:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1d7435a-ea82-3b41-bc35-9dca03a66db4 | -3.61743 | -40.64131 | 2025-09-25 03:40:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6f070eb7-616c-3342-b497-9b364cf450ab | -5.78437 | -42.55757 | 2025-09-25 03:40:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| dd40c2eb-9fb6-3a30-941a-3667b11a9d11 | -6.11758 | -44.00355 | 2025-09-25 03:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 344635a5-b4c5-388f-aa88-efdbd2150053 | -3.78229 | -41.73016 | 2025-09-25 03:40:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 86949ecf-3d12-38ce-aa08-df3f3d0b6062 | -5.6129 | -42.99989 | 2025-09-25 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 31734eff-9be1-3b6e-82b5-86e083459a98 | -5.42721 | -41.31513 | 2025-09-25 03:40:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a515fa68-65e1-3659-b185-15c6eddb42d6 | -5.92863 | -42.92655 | 2025-09-25 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f696794a-f6b3-333d-b82b-79503be2e058 | -6.32019 | -41.88338 | 2025-09-25 03:40:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b49f0e01-210c-3ffd-b7ea-13d7b4f1463f | -3.78997 | -41.74168 | 2025-09-25 03:40:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 941db33a-6b4c-3045-a265-f5cfc4b2297e | -4.79521 | -43.54517 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aff16b0b-4864-33cd-b37d-508804732556 | -5.08856 | -37.60864 | 2025-09-25 03:40:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3a5897c2-6863-3fed-846a-33faba9b818e | -5.72037 | -42.61583 | 2025-09-25 03:40:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |


[Clique aqui para ver as próximas entradas](README9.md)
