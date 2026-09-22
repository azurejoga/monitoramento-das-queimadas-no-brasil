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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84cd07a8-7f41-337b-b957-a3572ce68c0b | -6.3436 | -55.8243 | 2026-09-22 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 606a7e77-844a-36bd-a5e6-6e2962a6720c | -3.7856 | -60.7335 | 2026-09-22 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 243.9 |
| 67608754-f3f3-3fe1-82c7-002ac93ff630 | -10.6878 | -50.751 | 2026-09-22 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 3bb247e0-de5e-3ed4-95a0-1a7474b83609 | -11.6891 | -50.9619 | 2026-09-22 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 7828b082-5bde-364b-ab60-bc1d343898ab | -3.6033 | -60.5664 | 2026-09-22 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| ff17ca8e-3422-3bbf-abf3-8e50aff12477 | -9.6111 | -43.9243 | 2026-09-22 14:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 107.6 |
| 5e238d4a-8953-3d2d-a3ff-385f448981b4 | -9.257 | -46.1873 | 2026-09-22 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| ed400a02-84c4-3c99-8701-6d2b47b356f4 | -9.2762 | -46.1627 | 2026-09-22 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 306.8 |
| 236b1fe8-1af5-32f8-ba44-2ea9f6d2b069 | -12.0836 | -50.0378 | 2026-09-22 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 6baa6bd1-362a-3053-8d73-69ec1727fab6 | -6.0365 | -57.8235 | 2026-09-22 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 5bbfd141-64fe-3036-87d4-42d9ad656272 | -11.118 | -54.0268 | 2026-09-22 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 7f7bc1c1-64eb-30eb-90e2-8efe9bfb46bd | -11.2404 | -40.2582 | 2026-09-22 14:10:00 | GOES-19 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 95.0 |
| 975fc026-ee87-326e-8074-887216399bc1 | -7.4765 | -45.4872 | 2026-09-22 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 2654cca3-780d-3702-85a9-198e536e701b | -12.3478 | -50.221 | 2026-09-22 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 32215154-f608-3b58-b03c-864322ea1a5c | -12.853 | -50.8885 | 2026-09-22 14:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| fe81fc39-e30d-3207-837c-1e5ff281744c | -12.8 | -44.2073 | 2026-09-22 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 627.0 |
| bdf57eef-da75-3324-ac6d-0506dd69a6c9 | -11.44 | -47.3579 | 2026-09-22 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| d4cf5e39-a90a-3842-8e3e-bdbafcd74c66 | -6.7464 | -59.4223 | 2026-09-22 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| f44b10a9-3d3a-380b-8bc4-f7f7b4022160 | -8.6322 | -62.4974 | 2026-09-22 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 6f6193eb-b2ca-3d74-8db4-47b1575cc5c5 | -6.0172 | -45.2462 | 2026-09-22 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| a70915cd-c44b-39d7-a357-ceaebe08e3f5 | -3.2396 | -53.9417 | 2026-09-22 14:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 150.0 |
| 102bcad1-c66d-3cb2-a51a-2e517e1698a9 | -12.6796 | -50.974 | 2026-09-22 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 80fbf0ed-6c7e-3f67-8d38-774e7f419ec8 | -9.2948 | -46.1831 | 2026-09-22 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 32707dbc-8db5-3e0a-a520-2e0653fb91a5 | -10.6094 | -53.9902 | 2026-09-22 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 522cc71f-faaf-3007-ad03-cc149bc1e967 | -3.6215 | -60.585 | 2026-09-22 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 9f4040df-147b-3a2d-8525-91b53699f916 | -2.8791 | -57.799 | 2026-09-22 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 2586eaa0-b0c7-3f79-9e49-127322289bac | -12.2827 | -50.7226 | 2026-09-22 14:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 04fbc21d-1aa7-3ea7-a8d3-65951c279a93 | -6.3135 | -57.7342 | 2026-09-22 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| dafea745-18cf-3cf1-a6c3-144dc5bb5077 | -6.0926 | -57.6652 | 2026-09-22 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 5f804546-8768-3566-bccb-91c7105d03e0 | -13.8952 | -45.4913 | 2026-09-22 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 201.6 |
| f7cb0e80-e6c6-3ea4-b532-c0cab985c815 | -6.9683 | -47.4899 | 2026-09-22 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 144add32-0521-35a5-9dbd-d88261b80a40 | -7.1553 | -47.4971 | 2026-09-22 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| e690e555-c137-3681-b925-3d923e240661 | -3.3 | -57.8681 | 2026-09-22 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 5225216d-3039-3710-8ce0-956cfbee3f6d | -14.6688 | -45.6565 | 2026-09-22 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 190.0 |
| edf12252-59d9-351c-bfbe-2cb4d72b9d2b | -6.2759 | -47.6506 | 2026-09-22 14:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| a5faafdd-15ab-3dde-860f-7ab167d813e9 | -3.3493 | -59.8479 | 2026-09-22 14:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 23c721b6-6ed3-3428-a06e-94ba1e32405b | -6.0992 | -59.9267 | 2026-09-22 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 1e496385-9deb-3259-8a4f-5f0f218a5d3b | -12.3297 | -50.1586 | 2026-09-22 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 178.2 |
| cecd1977-5dad-305a-bcd9-31d48ca05fbf | -6.2948 | -47.6274 | 2026-09-22 14:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 9b3ad6b0-2307-3ba7-beae-aa98118b46e8 | -6.0549 | -57.8227 | 2026-09-22 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| f02cf754-2d34-372c-835e-6b56e68adc41 | -3.3309 | -59.8673 | 2026-09-22 14:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| a79ffb07-8479-30a3-a8f5-94f56893854a | -7.1203 | -43.7323 | 2026-09-22 14:10:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 0ef31293-fdb4-313a-9be9-bc26dea33e4f | -12.8056 | -54.0462 | 2026-09-22 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| dc46ff09-6ad8-3aaa-98e7-e31d17a01a45 | -6.4302 | -59.9724 | 2026-09-22 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 9b3cb3c0-79bc-3a8a-af4f-e8f2b4da91d3 | -10.5748 | -46.7296 | 2026-09-22 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| faee2b20-8212-3d9b-a192-b19236d87411 | -12.1027 | -50.0355 | 2026-09-22 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| c025e354-a241-3b8e-92a2-eaa1fe65738c | -2.9157 | -57.7983 | 2026-09-22 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 102.7 |
| a7516c05-b305-3c48-8a05-b44a8bb80d70 | -11.4209 | -47.3603 | 2026-09-22 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| bae3e9c4-713a-335b-9e52-0e12380c4355 | -9.152 | -50.0066 | 2026-09-22 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 74a2ac38-f25b-3e79-92bc-752941428f19 | -6.2763 | -47.6069 | 2026-09-22 14:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 0696e8e6-c010-3349-9aac-bca25e0ff7b1 | -6.3842 | -55.265 | 2026-09-22 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| d46fd35c-9f42-392e-824b-ad6dd88035b7 | -8.4611 | -57.6292 | 2026-09-22 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 63f17fbb-226c-3cb8-9ea6-ddf12f17c276 | -12.283 | -50.7011 | 2026-09-22 14:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| f8e1fe07-1b28-3886-8dfd-7226979aafd1 | -12.2726 | -50.1441 | 2026-09-22 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| dac46859-7e03-3e27-b118-2da696a177f7 | -9.5542 | -47.9549 | 2026-09-22 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 2685a15e-966f-36ac-a6c4-5e90f3e5a6d7 | -11.4404 | -47.3355 | 2026-09-22 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 895aa95e-794e-3ebb-9c83-2cdbdbfe50e1 | -3.6215 | -60.566 | 2026-09-22 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 8c118364-0db5-3677-aee2-6428ae3994ed | -5.7873 | -43.7758 | 2026-09-22 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 217.1 |
| e816140e-73d1-3de2-b860-a1fd05f6d6b9 | -9.5833 | -45.8345 | 2026-09-22 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 1455c708-23e6-3f38-9651-90dc0a43ff65 | -10.4539 | -51.3038 | 2026-09-22 14:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 6d5a137b-e674-33f6-8466-8b870f21a86b | -2.9158 | -57.7789 | 2026-09-22 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| f6f7a9b6-57ba-3dad-92d1-d46a2fcdc02e | -12.891 | -50.9052 | 2026-09-22 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 148.1 |
| a69d25c9-1ba3-3049-ad2f-db65d22febe4 | -6.1109 | -57.684 | 2026-09-22 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 112.5 |
| a03689fe-9528-3d61-aa57-b7963385bd68 | -3.2395 | -53.9618 | 2026-09-22 14:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 143.0 |
| b1464dc4-d28a-3e0b-9d2d-c32d2ae3e74e | -3.3867 | -59.5223 | 2026-09-22 14:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 95.0 |
| da530954-cc91-313d-9d7f-c1c0b5f75f86 | -12.4204 | -47.0228 | 2026-09-22 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 118.2 |
| e1734e77-6de8-31fe-89ed-c8c203a87f27 | -12.8246 | -54.0442 | 2026-09-22 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 4d792fb7-03fe-3f5a-8f27-97e0daaa3fc2 | -2.9709 | -57.7197 | 2026-09-22 14:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| e15a15de-07f8-328a-8674-f44a96b33abe | -10.4536 | -51.325 | 2026-09-22 14:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| db92b2e4-171d-30e3-abc2-90f9b88140a1 | -3.6398 | -60.5846 | 2026-09-22 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 24e13dc1-0def-30ec-bc6f-fe0373a46d94 | -6.9414 | -42.907 | 2026-09-22 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 126.9 |
| b3050902-11ea-3cb2-a204-34f16658db47 | -3.2212 | -53.9422 | 2026-09-22 14:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| ca4eaa61-ff1f-37cc-94cf-7d9012fae8e5 | -6.295 | -57.735 | 2026-09-22 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 371a35a1-8858-31fb-8df1-51890d655540 | -13.2791 | -51.7737 | 2026-09-22 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| fdf0c21d-804c-3643-947b-9156528dc049 | -10.0484 | -52.0974 | 2026-09-22 14:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 3e38f546-aa0f-3001-8aaf-ce54d1615bd1 | -10.7466 | -50.5959 | 2026-09-22 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 27c68cf5-3f5b-37cb-95be-299eda8cf9bf | -3.1901 | -57.8898 | 2026-09-22 14:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| d6a006c4-846d-3198-b2a2-077c165a9812 | -3.7364 | -58.8626 | 2026-09-22 14:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 29988ba0-7708-3f29-bb00-26ca5c39fac9 | -3.3863 | -49.521 | 2026-09-22 14:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| aff7b872-b86a-32ad-a691-f51146c066ca | -8.5982 | -54.6341 | 2026-09-22 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| dbff8401-3fa7-3912-8862-19f4137e084d | -9.6108 | -43.9477 | 2026-09-22 14:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 20c597b3-7772-3d93-b68d-ee40cb3e55d2 | -3.2817 | -57.8685 | 2026-09-22 14:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 93a03ae1-d27a-3dc5-8bd8-6ca6d068ba3b | -12.6608 | -50.9549 | 2026-09-22 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 0060d9cd-ebb3-3c3b-80ae-8db08afe7612 | -4.6589 | -42.0726 | 2026-09-22 14:10:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| b46dbba3-570b-3334-9307-c9ae26383557 | -10.2635 | -49.984 | 2026-09-22 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 3da3b189-b587-3d33-b38c-6f5204726700 | -11.0052 | -53.996 | 2026-09-22 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 768e34fd-ac35-370e-a860-1f54d997ca8b | -3.1901 | -57.8704 | 2026-09-22 14:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 801ce7ab-423a-3c6f-a9bf-a26a39f49ce4 | -9.5329 | -45.3861 | 2026-09-22 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| f5a8aba6-7c95-3e26-8c85-19ce0847d852 | -12.4208 | -47.0002 | 2026-09-22 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 270.7 |
| 496ba61b-e224-3aaa-b7b8-75e079961b2d | -6.9871 | -47.4885 | 2026-09-22 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| d08c01ee-d396-3d37-9652-0f655d46998a | -11.2879 | -54.0317 | 2026-09-22 14:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 3b495def-6b34-3214-b007-121469198576 | -6.1838 | -47.5258 | 2026-09-22 14:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 07ccc998-05b1-3ce8-8a87-8c25dd6c195c | -3.4057 | -59.273 | 2026-09-22 14:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 0924894a-6c79-388b-a3b4-6e7c0fa85d55 | -7.9825 | -44.0647 | 2026-09-22 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 99.1 |
| f37e94e8-a7d5-3ac2-ab5f-fd8c02393714 | -9.8665 | -45.8918 | 2026-09-22 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 9930a9d7-9d53-3b06-85e2-cf8691dda271 | -13.2979 | -51.7926 | 2026-09-22 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 1c3f6b60-5d01-3a82-a5d6-467f2568b9fa | -6.1111 | -57.6645 | 2026-09-22 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| b24acc39-a576-34fa-b398-763c33e198ce | -7.146 | -48.4352 | 2026-09-22 14:10:00 | GOES-19 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 210.5 |
| c8d1e816-9a36-37ae-9b84-f6a21f372316 | -3.7673 | -60.7339 | 2026-09-22 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 162.3 |
| 1622bd2c-7e9f-317a-b520-12da4c7144ff | -10.5906 | -53.9918 | 2026-09-22 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |


[Clique aqui para ver as próximas entradas](README135.md)
