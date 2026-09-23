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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90ab280f-ae64-3740-91c8-2468f0160f33 | -12.3867 | -50.1731 | 2026-09-23 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| a3a9dcaa-a3b0-3655-ad8e-a4c4ae11fcb2 | -6.6315 | -43.7533 | 2026-09-23 02:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 227.7 |
| f6c0a42d-72a4-389c-8a54-eb3775719ce1 | -8.8105 | -44.2757 | 2026-09-23 02:50:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 8aba774a-e2f6-3ae5-9662-722870e58009 | -14.7536 | -47.1548 | 2026-09-23 02:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 625.6 |
| 7d1b4b9d-7350-3749-9d04-8e9725ad7f60 | -12.3488 | -50.1563 | 2026-09-23 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 186.1 |
| 0731e4e7-7697-37a8-9b06-ad2b38478ad8 | -12.3676 | -50.1755 | 2026-09-23 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 6f47f018-f94c-3479-9d55-5a2577367c41 | -14.7736 | -47.1287 | 2026-09-23 02:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 9e9141d9-3496-3cec-b8a4-77231cbfbbb0 | -12.7575 | -50.8789 | 2026-09-23 02:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 3d8eaae8-a3a5-388b-978a-b40dd79cbcf4 | -11.6324 | -50.947 | 2026-09-23 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 9eb19707-c8cf-3306-a8bf-685b97f0b2bf | -6.6129 | -43.7317 | 2026-09-23 02:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 296.4 |
| 2f36643b-d819-39b5-a7f9-2c56317a5047 | -6.6127 | -43.7549 | 2026-09-23 02:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 429.9 |
| 485741d3-4791-333f-aeb3-85b699861830 | -6.6145 | -59.9464 | 2026-09-23 02:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 103d21b8-03cd-363a-884d-8c80faea2c4e | -12.4212 | -46.9777 | 2026-09-23 02:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 9faaf947-f607-3474-8e55-d4675add3d9f | -12.3484 | -50.1779 | 2026-09-23 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 50babe45-52f3-3c90-8f0c-d1fe920d8006 | -8.935 | -61.495 | 2026-09-23 02:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 6156b30b-d684-3ac1-b3e0-7bc733e02570 | -8.9351 | -61.4759 | 2026-09-23 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 7b20044b-7c10-3ee6-a469-7fb119bea6cd | -14.7541 | -47.1321 | 2026-09-23 02:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 263.4 |
| 2b4fa18d-55ba-3887-a283-f657c9d98939 | -5.8166 | -49.1504 | 2026-09-23 02:50:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 934792d3-4c72-34ed-8106-29bda3c16f27 | -14.7341 | -47.1581 | 2026-09-23 02:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 38c981a7-f3d1-37d0-9740-ec1bc79831c4 | -11.304 | -51.3646 | 2026-09-23 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 4f4801c8-9098-34da-9b56-63b3d208dc14 | -6.6146 | -59.9272 | 2026-09-23 02:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 189.4 |
| 61dc0646-cb16-326a-8a51-8cc858708911 | -6.5941 | -43.7333 | 2026-09-23 02:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 62b9e24c-dd91-3ffd-8841-17c51701f984 | -4.0925 | -62.0874 | 2026-09-23 02:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 3085375f-eaa3-3731-97ca-fc662d6a28c3 | -6.6317 | -43.73 | 2026-09-23 02:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 4b7bc1ca-0f07-3778-a1c0-9b9b5c6d92a7 | -9.1024 | -61.4491 | 2026-09-23 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 50f071a2-b9d3-30ca-8356-0f0ef80287ad | -6.633 | -59.9457 | 2026-09-23 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.6 |
| a63f3034-920d-38f3-b570-bb524cbd38ac | -12.387 | -50.1515 | 2026-09-23 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| b17dc86f-72bc-3f83-974b-191c53ae0963 | -12.7572 | -50.9004 | 2026-09-23 02:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 71106d8f-1dc8-3c2f-8f72-e0cc3d84cc71 | -14.7279 | -45.6226 | 2026-09-23 02:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| e5c2caa1-b5d1-32c4-aec0-964b04bac2b9 | -5.6246 | -45.2518 | 2026-09-23 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 56f95cfa-b058-3722-9be5-46b7d7891cfa | -14.7531 | -47.1776 | 2026-09-23 02:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 07f4650e-9b88-31eb-b65a-82d41ba640e6 | -8.9165 | -61.4767 | 2026-09-23 03:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 33664ced-4d5d-3c1b-b22b-fe0ddc0c4f79 | -12.3679 | -50.1539 | 2026-09-23 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 215.2 |
| 81b0ee11-ed7f-3ae3-89f3-af6a7b020c67 | -12.0595 | -50.3634 | 2026-09-23 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| b3b58136-98c0-3d41-bb37-1a7a9bb5f3d9 | -6.0925 | -57.6847 | 2026-09-23 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 2149ec34-fe9b-3ffa-893d-9c43e9ef013e | -3.2129 | -46.9383 | 2026-09-23 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 09a0ab47-e6bc-3ba6-8cd8-997ac5afb0ab | -11.304 | -51.3646 | 2026-09-23 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| a7822d7e-82f0-3b06-9b58-ef7cd8187f17 | -7.5151 | -45.3931 | 2026-09-23 03:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 5f27262f-6d11-3bdb-83c2-310c23779648 | -6.6129 | -43.7317 | 2026-09-23 03:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 178.0 |
| b94801eb-f39c-3ee7-b1c3-fdbf49e90dd3 | -12.3484 | -50.1779 | 2026-09-23 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 480e904f-da2a-35a7-a2a4-c40bd933a803 | -8.4985 | -57.6075 | 2026-09-23 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| e3ed6f3a-9c12-36d8-945d-1f9249a31dbb | -6.6815 | -55.0703 | 2026-09-23 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| ca842191-bac9-33b2-8e0c-ee6e54e65441 | -12.3867 | -50.1731 | 2026-09-23 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 8129c972-845c-35d6-953c-9f6c7937bc3c | -3.2313 | -46.9596 | 2026-09-23 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 8fda4fdd-5775-3a06-84d7-bc44c1b159f9 | -12.3676 | -50.1755 | 2026-09-23 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 930748a9-eb86-3a4b-9bcf-9f8d38a40e68 | -6.5939 | -43.7565 | 2026-09-23 03:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| cb056d19-1ad4-3c74-afbc-d0383dee65d2 | -6.633 | -59.9457 | 2026-09-23 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 392d14c9-def4-350f-be71-74b23fc47da7 | -12.1192 | -45.6368 | 2026-09-23 03:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 770b443a-6c47-36e9-b1a9-8449ccfbe888 | -6.5941 | -43.7333 | 2026-09-23 03:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 1b5de296-4627-3f00-b4fa-1ed8e04308e2 | -11.6514 | -50.9449 | 2026-09-23 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| a8cbe35c-ede7-3e77-a158-409337b82715 | -8.935 | -61.495 | 2026-09-23 03:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 72.8 |
| c284205a-db38-3441-9623-0afb2de282ea | -9.1025 | -61.4299 | 2026-09-23 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| db7d50e3-70f2-3d2a-bb54-272c88f3d5a6 | -6.6127 | -43.7549 | 2026-09-23 03:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 186.7 |
| 3ab40336-e687-30c7-b459-39dfb7333ee9 | -3.6946 | -60.5835 | 2026-09-23 03:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| f9a81b99-d76b-3e72-840a-293f6e5356f6 | -3.6763 | -60.5839 | 2026-09-23 03:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| a14f9b26-0d48-3f66-819e-b3bf86a6cd23 | -11.2853 | -51.3454 | 2026-09-23 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| c7078fb9-f172-311d-a793-4f74168c7e35 | -6.6148 | -59.908 | 2026-09-23 03:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 32db0394-ab06-3087-97c2-854cab7b255e | -8.4726 | -48.6927 | 2026-09-23 03:00:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 9d8bd9f2-7de2-30f5-93f9-9f8f977d26e6 | -6.9214 | -46.5663 | 2026-09-23 03:00:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 99a4fa84-0c87-3ad1-a408-a3df871da859 | -6.6315 | -43.7533 | 2026-09-23 03:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 568cf96f-0fdc-37cc-a9c6-89a6f46e0464 | -3.2314 | -46.9376 | 2026-09-23 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 8d90dea3-fb43-31e1-bfc1-757eb006d814 | -11.6321 | -50.9683 | 2026-09-23 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 4a9a37d9-5f3c-388e-8d0a-d8efc869f451 | -12.3488 | -50.1563 | 2026-09-23 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 7207081c-de56-336c-9ac0-fb34f4efd8ae | -12.387 | -50.1515 | 2026-09-23 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 26088380-f903-3995-84fc-25d9f6b1227a | -6.6317 | -43.73 | 2026-09-23 03:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| a223321c-0f69-35d3-8fa4-9e02d0730312 | -9.1024 | -61.4491 | 2026-09-23 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 93156944-0fe5-3b27-81ed-4ce728ac8164 | -6.6331 | -59.9265 | 2026-09-23 03:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 129.1 |
| 5163d5f0-dab1-37c5-a79b-a6fdf8bba954 | -6.9403 | -46.5426 | 2026-09-23 03:00:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 66b6f44f-59b0-3aeb-801e-847b2fd32d86 | -11.6701 | -50.9641 | 2026-09-23 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 51953417-4efd-3540-8844-1df81da82595 | -8.4538 | -48.6944 | 2026-09-23 03:00:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 68.9 |
| f6521ad0-04ac-3ba8-b916-53d6dc474ac3 | -11.3037 | -51.3858 | 2026-09-23 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| e5060313-6ba1-365a-b8af-0ea8814866b7 | -11.2856 | -51.3243 | 2026-09-23 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 56.2 |
| cfd9d5a4-f1a4-3950-a26a-8c891ae00155 | -11.6511 | -50.9662 | 2026-09-23 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 30c85044-38d0-3ede-819d-5bb28b028a48 | -6.6145 | -59.9464 | 2026-09-23 03:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| a55fa509-c853-36d3-b4f9-4ba667ef0f0c | -8.9351 | -61.4759 | 2026-09-23 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 5e72e724-6fa7-36cb-9a65-5e50679c3f9b | -12.4212 | -46.9777 | 2026-09-23 03:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 998ccd5d-0c9b-3099-84c4-4d5871368a7d | -5.6246 | -45.2518 | 2026-09-23 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| c04cb3d6-9488-3e2f-83d9-9bfd1c164bd7 | -6.6146 | -59.9272 | 2026-09-23 03:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 180.5 |
| 27b6f559-fe34-30ea-b4d7-b9706c3c135a | -5.7567 | -45.1067 | 2026-09-23 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 6f7dab40-b3b8-3f33-b131-c489b70f1f5f | -12.1385 | -45.6339 | 2026-09-23 03:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 53.0 |
| c4685d48-c513-3c9b-8fd0-eb4c9b5a16a5 | -6.9401 | -46.5648 | 2026-09-23 03:00:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 164.5 |
| 21d100b4-08c0-3bb0-aaca-464f447a43a9 | -11.3043 | -51.3434 | 2026-09-23 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| e730f505-cc2a-3677-9278-e77caa364843 | -8.9164 | -61.4958 | 2026-09-23 03:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 94.4 |
| d4d3f6b1-2140-3338-9136-e6c716c31046 | -12.0786 | -50.3611 | 2026-09-23 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 21d5fbf8-69cd-3d74-bbc4-77eaf3bd700d | -6.61 | -43.74 | 2026-09-23 03:00:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8879816-1428-3f51-a3e0-54838c7c823b | -6.61 | -43.79 | 2026-09-23 03:00:00 | MSG-03 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b08c9031-85ba-3f70-ae1c-7be1f3cb9235 | -12.35 | -50.14 | 2026-09-23 03:00:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ad930978-980c-30ad-8ad4-74dd4f0572af | -6.58 | -43.74 | 2026-09-23 03:00:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd29f867-edc6-34f9-a85b-9276aab2f3e2 | -6.58 | -43.78 | 2026-09-23 03:00:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa738043-4aa6-32a4-bc2c-53041979e6e3 | -6.58 | -43.69 | 2026-09-23 03:00:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8b83759-ffb7-3aac-ac83-d62f66cf5ea8 | -6.61 | -43.7 | 2026-09-23 03:00:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad26955f-3e9b-3f74-a549-d17ef98be710 | -14.6497 | -45.6367 | 2026-09-23 03:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 33e3ed04-d3a3-35c0-b6e8-2416155a142a | -7.5151 | -45.3931 | 2026-09-23 03:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 345481b3-51e8-3396-bcfc-48cadccc2e19 | -9.1024 | -61.4491 | 2026-09-23 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| a9780684-b5c6-3e29-bc72-9e03805d7749 | -12.387 | -50.1515 | 2026-09-23 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| afc948dc-8269-35b9-b147-6a07fc8f3a02 | -6.1111 | -57.6645 | 2026-09-23 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 0fa5588b-3454-3b32-b736-37439444c9f6 | -6.6145 | -59.9464 | 2026-09-23 03:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| d05e8bcc-585d-3ba1-b817-815fd86160d3 | -11.3043 | -51.3434 | 2026-09-23 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 5cc584b9-02a1-3859-ba43-21946fd39b95 | -8.9164 | -61.4958 | 2026-09-23 03:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 85.3 |
| e30bd181-ee8b-3cc8-9fb3-40373550ebb9 | -12.3679 | -50.1539 | 2026-09-23 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.0 |


[Clique aqui para ver as próximas entradas](README39.md)
