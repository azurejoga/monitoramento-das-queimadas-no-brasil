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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76467586-3ad0-35ed-b568-2cc1d74092a1 | -17.5779 | -46.5756 | 2025-08-23 00:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 30e512e6-c981-3f3c-ac83-a632819eacb6 | -3.4255 | -49.0303 | 2025-08-23 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| a0154495-9a36-371a-b1d0-07844470e51b | -17.5985 | -46.5481 | 2025-08-23 00:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 113.5 |
| f51c3643-db4c-3136-a838-5bdb00de307b | -3.4254 | -49.0517 | 2025-08-23 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| cd7aeb55-d475-3c40-bc8f-e116ab02cf13 | -20.0506 | -43.169 | 2025-08-23 00:10:00 | GOES-19 | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 54.2 |
| 5cfe49d1-835c-379c-8770-766c39e3e58b | -7.2157 | -45.307 | 2025-08-23 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 985cc8db-c530-385f-a784-e12b66adba1c | -9.4638 | -47.6565 | 2025-08-23 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 702146b7-b79a-354a-ba95-73123735284b | -5.118 | -43.2198 | 2025-08-23 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 746cb61a-c5f2-3dfa-8863-ab42c38f51b7 | -10.6122 | -55.413 | 2025-08-23 00:10:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 9e64ef77-4557-3025-b961-f56bc1212153 | -19.73 | -45.6884 | 2025-08-23 00:10:00 | GOES-19 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 85.7 |
| b034a5d0-e1dc-396c-abfc-1b4d553b1df1 | -29.0074 | -49.4984 | 2025-08-23 00:10:00 | GOES-19 | ARARANGUÁ | SANTA CATARINA | Brasil | 4201406 | 42 | 33 | nan | nan | nan | Mata Atlântica | 135.3 |
| 2a619056-ac1a-3e35-9257-729dc65be3b6 | -9.1712 | -59.5987 | 2025-08-23 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 80aa5787-c86e-3343-9116-f463eed38936 | -6.8733 | -59.8213 | 2025-08-23 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 7d38c761-640d-3a7a-81ea-d5799117b59c | -6.4138 | -41.2132 | 2025-08-23 00:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 175.3 |
| 1a558706-df0d-3ede-8058-4559d5854aeb | -9.2095 | -59.4609 | 2025-08-23 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| aa8d0d98-42e4-3cd3-9668-e750dbfe20eb | -9.1711 | -59.618 | 2025-08-23 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 5bbdc6b1-6c2d-3860-abd1-185ab0321e62 | -6.4327 | -41.2114 | 2025-08-23 00:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 262.0 |
| 8eaef507-1935-3aa9-b18e-b40220b29ddd | -9.2083 | -59.6161 | 2025-08-23 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 8473d8f8-adf7-3b56-81b8-8c63be34fb66 | -11.3303 | -55.2111 | 2025-08-23 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| bb4afed2-3a16-3615-b6d5-77f68cffccdc | -7.7945 | -63.5663 | 2025-08-23 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 410cf722-06c4-30a2-acef-c519d525d41a | -5.48981 | -42.16731 | 2025-08-23 00:11:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| b742dc8b-0bc7-3aa6-8971-92f37a045cbf | -5.66417 | -45.12466 | 2025-08-23 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2e611c39-9b2e-3c22-9c10-fc5969c56b6e | -4.31013 | -48.10876 | 2025-08-23 00:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 014a0804-2a40-3180-a3bf-b10e83f8e1a0 | -3.43783 | -49.05799 | 2025-08-23 00:11:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| bca847e9-addb-3695-991c-1e9a807a62d1 | -5.66551 | -45.13479 | 2025-08-23 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| e7e68471-1f00-3117-a1ee-6e18e0e695bc | -3.81887 | -41.5543 | 2025-08-23 00:11:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| fd775d0e-5293-3957-b2a1-443b3ac402d7 | -6.60799 | -47.99114 | 2025-08-23 00:11:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 034bf07f-5aa6-36d0-ac0a-1f62d0fcc248 | -6.39014 | -45.52561 | 2025-08-23 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8f7a2eda-2078-3ddd-b6c8-7556f2d9718b | -5.15371 | -44.93745 | 2025-08-23 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b29da0ea-344a-38a3-be28-00696c31b335 | -6.23542 | -47.31569 | 2025-08-23 00:11:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| e8f82db0-e74d-3e72-8df1-01019a007aea | -3.58678 | -47.32038 | 2025-08-23 00:11:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0b6255be-b817-302e-9734-d682b6c15911 | -2.25494 | -47.8561 | 2025-08-23 00:11:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 5dd66d80-7304-3f6b-b49f-f209821624dc | -6.2325 | -47.30742 | 2025-08-23 00:11:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| c8b356db-b28b-392b-9539-07a38902f0b8 | -3.44099 | -49.02827 | 2025-08-23 00:11:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 0f0d2c96-e200-3e76-9800-2fdc2da24a15 | -3.81241 | -41.57463 | 2025-08-23 00:11:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| e5450a5b-e748-3710-a22a-a6f9d63b2e67 | -4.59817 | -48.95613 | 2025-08-23 00:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 851e4948-6389-3435-b116-f38ee2b2a4e4 | -3.43554 | -49.04049 | 2025-08-23 00:11:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 226.9 |
| 50f57827-8609-3837-91f8-b8d350ad5942 | -3.04614 | -47.00951 | 2025-08-23 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9df35c35-8d79-3a24-ab08-6ae31753fd85 | -3.55175 | -41.62025 | 2025-08-23 00:11:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 18.8 |
| b6d91c33-737e-3715-adda-feeda7a8569d | -3.04779 | -47.02145 | 2025-08-23 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 599f45af-b73c-3498-af7d-f66ce5873846 | -5.3642 | -45.20042 | 2025-08-23 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 35311cfd-ec3e-3037-aef7-58666ec998c3 | -3.44341 | -49.04567 | 2025-08-23 00:11:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 95d1c716-80df-3754-b298-1f151b1dcdd1 | -4.30815 | -48.0935 | 2025-08-23 00:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 7b666bd6-2851-3421-a4f4-8c9f3f4fbaa1 | -5.36282 | -45.19029 | 2025-08-23 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 14d7212e-7c5c-300d-9dea-989c5af26724 | -4.98111 | -38.60458 | 2025-08-23 00:11:00 | TERRA_M-M | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 26.6 |
| db80f450-5cf7-3839-ba66-0cf03ee0cd3d | -5.48856 | -42.15836 | 2025-08-23 00:11:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 9e43763e-da65-3582-bb44-524cfc62d66e | -4.81561 | -43.54348 | 2025-08-23 00:11:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b212835a-87e8-3820-bfb4-124e56aab779 | -3.51171 | -47.20621 | 2025-08-23 00:11:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 986305c4-b641-3d5d-8d91-b48b5dda48aa | -5.1095 | -43.21341 | 2025-08-23 00:11:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 136.5 |
| e448de02-0201-3bc7-b7d5-9149e73228fe | -3.98178 | -43.24786 | 2025-08-23 00:11:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5d243768-93e3-33ab-a53b-9935c789b032 | -4.14521 | -46.45602 | 2025-08-23 00:11:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9d62b2b9-eace-302a-82b4-083f7dad0fc3 | -6.18423 | -45.43475 | 2025-08-23 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| c74bd0ef-0609-3567-a93a-b82b0edf7ff0 | -5.64136 | -44.19841 | 2025-08-23 00:11:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1af0e499-b5a5-3987-9c77-e4a9259a0c02 | -5.95509 | -44.13616 | 2025-08-23 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 75a69539-90e3-317c-9e92-501c6d1cd071 | -5.14445 | -44.93877 | 2025-08-23 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 33c8f432-9d96-3aa6-ac90-20c0781cabc5 | -4.22661 | -47.21716 | 2025-08-23 00:11:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 22.3 |
| abf09980-63d0-3592-b69d-ba8b24c0f547 | -4.63741 | -41.4117 | 2025-08-23 00:11:00 | TERRA_M-M | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 91981d57-47e0-3ade-a9f9-bdf0d37c5929 | -2.62513 | -46.84954 | 2025-08-23 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b679e57f-2df7-35d8-ba51-68749dcf4a9b | -6.04739 | -44.00434 | 2025-08-23 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| dc924032-3cbf-39df-8dda-1d965b4c3263 | -3.82156 | -41.57331 | 2025-08-23 00:11:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 3333981c-0072-35da-b1b4-d534937b69d2 | -2.25793 | -47.85 | 2025-08-23 00:11:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| fdff2d3b-0d45-3353-b4c8-83ae959d5a80 | -5.11072 | -43.22223 | 2025-08-23 00:11:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 44213f20-608a-34ff-90c4-35b1355d18e2 | -4.22488 | -47.20415 | 2025-08-23 00:11:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 426beb9e-2e28-3cc7-9645-68660ea168f6 | -5.09689 | -44.79675 | 2025-08-23 00:11:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f5cdf756-f786-3168-a32a-df014f63c6fb | -4.79084 | -45.32573 | 2025-08-23 00:11:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2422a41a-4998-35b4-80bb-f98c2341f32a | -3.52218 | -47.20472 | 2025-08-23 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 57827244-cf45-37ab-94e2-2b503cce6ffa | -3.54259 | -41.62155 | 2025-08-23 00:11:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| a730b776-639d-3bd1-914b-e8734018e381 | -4.31004 | -48.09889 | 2025-08-23 00:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 09c53be0-5f1f-3e3e-8dd5-c9f9f5311e16 | -3.55309 | -41.62976 | 2025-08-23 00:11:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 8181c460-098f-3bc7-91f0-9907a149813f | -5.94605 | -44.13742 | 2025-08-23 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| d06030b9-e8cb-3707-8714-66e178f29819 | -5.1061 | -44.79554 | 2025-08-23 00:11:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 47f38fdc-9fb1-322c-8bbf-0c91e9fa7337 | -5.83276 | -52.0811 | 2025-08-23 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 4c04c056-00e3-3a6e-a852-6677555b74d7 | -4.12767 | -48.11488 | 2025-08-23 00:11:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 6b715033-93c8-3944-8b0b-582f9b908e1c | -6.18565 | -45.44545 | 2025-08-23 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3dd900c6-a49b-343c-ad26-ac92f70cd95a | -5.59488 | -44.53562 | 2025-08-23 00:11:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 05703fea-ea4d-3b74-9484-8b778c6c3b17 | -6.23443 | -47.32161 | 2025-08-23 00:11:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 2d81f4e8-af26-3418-8820-a244b7e0c82c | -5.94734 | -44.14681 | 2025-08-23 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1c5a3394-418f-32f5-a577-8e578f919ce8 | -5.67493 | -45.13347 | 2025-08-23 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 07c146bb-efbb-326c-9eff-a7775844a8f5 | -3.82022 | -41.56382 | 2025-08-23 00:11:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 745b094c-627c-3193-8c60-163ee3dd6a8d | -3.43128 | -49.04731 | 2025-08-23 00:11:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 504a3170-b0b0-3252-939e-551c664f12f0 | -5.59616 | -44.54514 | 2025-08-23 00:11:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 926b41b3-0271-3708-8793-44b8a8364d5c | -6.38328 | -45.54865 | 2025-08-23 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 542f4fb7-02da-34dc-981f-44c44f58085b | -11.6613 | -51.5798 | 2025-08-23 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 5fbfdf03-cc4d-3902-b979-b028b87e2077 | -6.433 | -41.1872 | 2025-08-23 00:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 63.6 |
| 4e6cfb2c-c4f2-3be6-bc7a-183db25e500e | -11.6423 | -51.5819 | 2025-08-23 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 7623377d-2d55-32ad-9f3d-3a3139df18a6 | -8.9106 | -62.4289 | 2025-08-23 00:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 4d6886ff-a335-35fd-ad09-c4f855bb4856 | -17.2751 | -46.777 | 2025-08-23 00:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 7681e382-c377-31ed-bd91-7654de698b57 | -17.2956 | -46.7497 | 2025-08-23 00:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 43.5 |
| b4933f80-3355-3d05-8868-fbdcabd0f4a6 | -7.813 | -63.5656 | 2025-08-23 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 135.6 |
| 79377f7e-9c3e-302c-a893-7779f98f7bcd | -5.7614 | -57.6002 | 2025-08-23 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 0e6fab98-9f8a-361e-9407-401f766a765a | -17.3202 | -46.5593 | 2025-08-23 00:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 6607e4bd-e82b-3641-b98e-b7d44bc90e04 | -17.3196 | -46.5827 | 2025-08-23 00:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 0172437b-90a5-3a58-a03d-f74cb0764d82 | -15.2288 | -53.8481 | 2025-08-23 00:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 0e73f146-2f65-31ba-a1ee-9786803f3c54 | -14.3126 | -58.5431 | 2025-08-23 00:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| eb8556d7-1d1f-33cd-9760-73b71bd5a28e | -5.7615 | -57.5807 | 2025-08-23 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 5563cb17-00aa-34f8-a578-2f6a623f41db | -20.097 | -47.7676 | 2025-08-23 00:20:00 | GOES-19 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 102.4 |
| a23f868d-ded4-343c-ae6e-6d727df0f61f | -3.4439 | -49.051 | 2025-08-23 00:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 56991502-3bed-34fd-812b-45e09d7dc9b0 | -5.118 | -43.2198 | 2025-08-23 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 18e2c49a-e10e-3a9c-8e72-be3e8388c96a | -17.5979 | -46.5715 | 2025-08-23 00:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 90890f4c-d4f0-32a9-bc49-175dbfac5988 | -10.6122 | -55.413 | 2025-08-23 00:20:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |


[Clique aqui para ver as próximas entradas](README5.md)
