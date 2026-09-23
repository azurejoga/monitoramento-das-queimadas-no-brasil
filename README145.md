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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa3cf685-a568-3ab8-b404-f024207f969b | -6.3383 | -59.9374 | 2026-09-23 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| f61749f3-0067-31ee-afc8-1c461f9358b6 | -8.7772 | -49.955 | 2026-09-23 15:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| d471b6c2-a24c-35bf-a73d-857d50d2716a | -7.4495 | -44.5557 | 2026-09-23 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 0c66600c-27ed-354c-831e-cdce7507e635 | -7.5477 | -61.3247 | 2026-09-23 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| ac242dd0-775f-3d06-993a-cb74ec947849 | -8.746 | -44.8586 | 2026-09-23 15:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 5e4bbfed-63f8-322d-9d50-139475289dd3 | -7.5704 | -57.6766 | 2026-09-23 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| da3efb6c-7279-3bd7-adb1-42bf22b90b66 | -9.8875 | -48.445 | 2026-09-23 15:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 051fa7ed-f874-3c74-a101-6b100efdf6e8 | 1.2055 | -50.9974 | 2026-09-23 15:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 3ad7dd52-f0a3-3ad7-9898-8b25607a2e6c | -6.5446 | -44.9099 | 2026-09-23 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| f6317d8e-471d-34e3-8d81-faf3066c996f | -8.9205 | -45.931 | 2026-09-23 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 31f5e29a-f3d8-38fa-acdb-d8e8f54c801f | -6.5763 | -45.4968 | 2026-09-23 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 206ce084-3ebf-30b2-bdde-8c4b7c392677 | -8.4305 | -47.4736 | 2026-09-23 15:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 96c0c5f3-6c63-32bc-9ca9-0ec2bd1d0e64 | -8.0094 | -61.3633 | 2026-09-23 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 01027189-d79f-3c06-a437-ad0fd1075fed | -11.4209 | -47.3603 | 2026-09-23 15:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 6698ce7d-9ca4-3f25-a538-17d261098f36 | -5.6223 | -43.3701 | 2026-09-23 15:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| e80ca8cd-2119-3268-b9d0-9c42f14a5142 | -8.4985 | -57.6075 | 2026-09-23 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 263.1 |
| 40893fed-d025-39b6-afed-aca0be9bd911 | -5.8276 | -47.768 | 2026-09-23 15:00:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 093fd88e-3d57-360e-9da3-47e2fe2e7061 | -6.5056 | -45.0723 | 2026-09-23 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 6707ebe2-faab-33e5-9690-beabfefe112f | -8.3134 | -44.7446 | 2026-09-23 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 88.2 |
| ee5149cf-1a32-3114-b055-519a8ba24844 | -4.2632 | -55.4303 | 2026-09-23 15:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 672cf507-3902-3eff-a50e-39c7df5f1f2e | -6.5948 | -45.5179 | 2026-09-23 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 65d1c70d-9d12-3a36-8741-e9fc3a60b20c | -8.7069 | -49.5336 | 2026-09-23 15:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 1faaddda-5660-367f-820c-bd6d73f1ec96 | -5.9337 | -59.9132 | 2026-09-23 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| c5027ead-7b4b-3200-bec1-5bb95a959dcb | -8.4983 | -57.6271 | 2026-09-23 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 122.8 |
| b0162bb6-52eb-3722-ad14-ef2b1999d4f1 | -6.4671 | -59.9711 | 2026-09-23 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 2a23113f-c6a4-3573-97d0-48f9dc83a1e7 | -5.9985 | -45.2476 | 2026-09-23 15:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| d29e6556-a69c-35de-9e23-adc620ccb623 | -9.8139 | -48.2999 | 2026-09-23 15:00:00 | GOES-19 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 47749600-50fb-396a-b9f6-f00ca1774b37 | -8.7735 | -45.6303 | 2026-09-23 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 256.8 |
| 380ae53e-88e9-31e5-9725-be2393556cd8 | -6.4129 | -44.9661 | 2026-09-23 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 40.4 |
| f2f453bd-a4c7-3ce1-b690-d2f54e96b471 | -9.5731 | -47.9529 | 2026-09-23 15:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| bf7efb20-1d69-3e1d-bfa9-53e07ab639cc | -11.3359 | -43.3793 | 2026-09-23 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 99bec28d-1faa-3ffb-82b3-85b75547830c | -6.6515 | -59.9258 | 2026-09-23 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 4146c533-90ad-390f-a842-1b03a9d3d57b | -5.809 | -47.7692 | 2026-09-23 15:00:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 0258fbc5-78e0-3e7b-93a2-23c8500f1512 | -10.8335 | -48.4706 | 2026-09-23 15:00:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 7583a816-0eff-30cc-90b9-75f88126772f | -6.9225 | -42.9088 | 2026-09-23 15:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.1 |
| cddfcafd-fdd3-30da-84bc-2b0a53794211 | -6.9029 | -46.5456 | 2026-09-23 15:00:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 63e20acb-6e36-3bb0-bd2e-d5bb43c66e17 | -6.6148 | -59.908 | 2026-09-23 15:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 110.8 |
| a06d541b-08a5-3f69-b62e-ea0ccfff740b | -9.406 | -47.7507 | 2026-09-23 15:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 68fe46c9-e54d-33ce-ae80-3e3b1634c9be | -7.8811 | -61.1779 | 2026-09-23 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 33ba93d7-9f8a-3267-9dfa-8b49873e2dd1 | -5.7565 | -45.1293 | 2026-09-23 15:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 4ce43d49-7559-3097-91cc-c52914e87d0f | -2.5687 | -57.5135 | 2026-09-23 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 82a6196d-ccfa-3e34-ae86-e255e4ebb1dc | -6.3382 | -59.9566 | 2026-09-23 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 18c13d7f-1edf-3a11-939a-7fbc46efc375 | -1.1533 | -48.9993 | 2026-09-23 15:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 84c0fedb-80b7-3c8e-83fa-0d1e6e620f42 | -8.0279 | -61.3626 | 2026-09-23 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 07c3e0d2-5524-3dec-ad0a-ecf56ccaeeb1 | -2.5872 | -57.416 | 2026-09-23 15:10:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 3cbf981a-abf3-3111-8059-b63952933948 | -6.2765 | -47.585 | 2026-09-23 15:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| df5b2e3b-8bca-3d07-8a75-8855f2b1d6d9 | -8.8735 | -49.7328 | 2026-09-23 15:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 8e7ab58c-929d-3e06-9e0c-c3ac9b88fc25 | -6.5446 | -44.9099 | 2026-09-23 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 5578db46-e678-30ac-a295-e0a2fd3656db | -6.467 | -59.9902 | 2026-09-23 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 47f6149e-9fa5-3359-8712-412047d87193 | -7.2994 | -59.5343 | 2026-09-23 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| df9d259d-0c52-392c-b6b5-6d9c205e4f30 | -6.9029 | -46.5456 | 2026-09-23 15:10:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 0947c76a-2e8a-35b9-8623-6236909d927e | -6.9414 | -42.907 | 2026-09-23 15:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.6 |
| ef1c0baa-0362-38ed-a75c-6209ade6d3f4 | -6.9223 | -42.9323 | 2026-09-23 15:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |
| ce8b4304-867b-3eed-9c3e-67c7ac65ad9e | -6.5639 | -44.8628 | 2026-09-23 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 13cafc44-950f-3691-91b3-9fbd34231ae9 | -1.9088 | -58.2589 | 2026-09-23 15:10:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 95.4 |
| dd92904a-c268-3bfc-a0c5-5844bc9d91ba | -8.4613 | -57.6096 | 2026-09-23 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| f3380e73-1889-3969-a393-c26fe77b445a | -10.8335 | -48.4706 | 2026-09-23 15:10:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| f3f0bcf8-15cf-3ed2-9c80-3c313fd6d5d2 | -6.5963 | -59.9087 | 2026-09-23 15:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 7877a7d5-7301-3557-9248-9e97cb78b459 | -6.7452 | -45.4604 | 2026-09-23 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 96bc4abb-e58a-3ea4-9bae-9354ddcfb2bd | -8.3134 | -44.7446 | 2026-09-23 15:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 7d27a5af-cb5e-3662-b65c-dcd39968d939 | -6.5636 | -44.8856 | 2026-09-23 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 0ecea047-8450-347a-a13b-b6df45deb665 | -6.5605 | -45.204 | 2026-09-23 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| eb6618b3-b3ad-3229-8587-eaf4671ab058 | -8.4472 | -47.648 | 2026-09-23 15:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 530497d5-2a4d-3299-9436-90d1e9921205 | -1.8218 | -55.7037 | 2026-09-23 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| f7da7ab2-5e76-36c9-85fa-fe1b921525bb | 1.2239 | -50.9972 | 2026-09-23 15:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 75.5 |
| d7a2c095-fa51-3358-9053-77a667772660 | -6.2832 | -59.9202 | 2026-09-23 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| b9728430-7f0b-3d33-a98a-b9de03d9a687 | -9.831 | -48.4292 | 2026-09-23 15:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 15257c1d-9917-3b39-a054-ef32db7c5be8 | -6.4671 | -59.9711 | 2026-09-23 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| c298085e-76f1-3efa-89cb-a2b9339f8e82 | -1.9271 | -58.2587 | 2026-09-23 15:10:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 69ede05e-7833-3e7d-9deb-e2d791b98c22 | -8.7069 | -49.5336 | 2026-09-23 15:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 6dd603a8-5d72-33b9-a2e3-e5d8b2b794a7 | -1.5674 | -54.4555 | 2026-09-23 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 901929d2-c1a7-3080-83fc-28eb3ab4d5b4 | -6.5634 | -44.9084 | 2026-09-23 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| bb86c076-e45e-3390-9223-de2bab73ddf7 | -6.3199 | -59.9381 | 2026-09-23 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 2d7f9e80-dbe3-3582-9340-60eaefc0dd6f | -5.9985 | -45.2476 | 2026-09-23 15:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 962fb263-35f6-3ad5-a022-d87fe250ad3e | -6.6148 | -59.908 | 2026-09-23 15:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 174.6 |
| c1efd075-42df-3cac-b0f8-19d27ee3e051 | -2.7713 | -57.0229 | 2026-09-23 15:10:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| dce39f1f-af4a-3c67-9027-0385f06e60ff | -7.3564 | -44.4726 | 2026-09-23 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 9b2fb596-175c-3727-9e0d-6220e0344d4d | -11.4209 | -47.3603 | 2026-09-23 15:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 184.3 |
| c322dfee-f304-312b-82de-08b029ddadc3 | -5.2402 | -49.2261 | 2026-09-23 15:10:00 | GOES-19 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 883e8ac3-b9b3-34fe-ad37-cc58996db90e | -6.4302 | -59.9724 | 2026-09-23 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 0810f8fe-d279-37fe-86fc-2f557e855048 | -7.4092 | -44.7885 | 2026-09-23 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 76da77e9-c1fb-3c29-a2fc-bcbfa21dab55 | -6.6332 | -59.9073 | 2026-09-23 15:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 10012b41-d7bc-36cf-9bca-76af1fd0d82c | -11.1204 | -48.327 | 2026-09-23 15:10:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 0c6876d8-4d9c-386f-a21d-5dd37b18a995 | -6.5449 | -44.8871 | 2026-09-23 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| d8079095-cf6c-34fe-abe9-e65f1d586951 | -7.8406 | -61.7887 | 2026-09-23 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| a3f76f2b-bf8a-3ffc-97fa-9f099b2bb32f | -8.1212 | -48.2463 | 2026-09-23 15:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 693909fe-cde5-373e-b342-f28cb86f8445 | -6.5243 | -45.0708 | 2026-09-23 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 2e9614aa-fd02-35c2-99c6-7c73f82b0a9c | -6.5444 | -44.9327 | 2026-09-23 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| d6a19428-0466-3633-8c4b-f59f16c95704 | 1.224 | -50.9764 | 2026-09-23 15:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 60.5 |
| b006511d-8486-302e-8462-368ba7bffa7c | -6.4368 | -48.4436 | 2026-09-23 15:10:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 337d0aa8-cbcf-3f3f-8af8-2b0210352276 | -6.4601 | -54.9814 | 2026-09-23 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 5bc2e536-2e95-326b-8ad0-80415bf06add | -2.5687 | -57.494 | 2026-09-23 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 279dca25-3451-3fa8-a418-06d8b65c1424 | -6.5953 | -45.4727 | 2026-09-23 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 01850282-9253-3ca7-a1d5-1f42796685e4 | -1.5858 | -54.4353 | 2026-09-23 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 685f4e82-15a6-3efe-85df-ca277b988cfc | -6.5763 | -45.4968 | 2026-09-23 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 5f0c30ee-40d5-36e2-a596-ce0509d38775 | -2.5687 | -57.5135 | 2026-09-23 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 512d898c-8361-3ea4-bbcc-90e0b6724a58 | -5.9337 | -59.9132 | 2026-09-23 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.5 |
| c0429f34-38f4-3f51-9317-fc6131fed7fc | -8.1215 | -48.2245 | 2026-09-23 15:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 004ab984-a607-3853-9133-c7a7c9de3d26 | -3.7167 | -54.1896 | 2026-09-23 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 153.3 |
| b9de6efc-e606-3916-80be-b07968464da4 | -1.4303 | -48.9316 | 2026-09-23 15:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |


[Clique aqui para ver as próximas entradas](README146.md)
