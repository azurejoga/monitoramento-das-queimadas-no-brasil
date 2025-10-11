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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c494a73f-b04a-3463-bb13-82e874d2a711 | -14.92578 | -46.77397 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09e37ebe-50b0-3964-9f70-6fc461df3de5 | -11.78528 | -63.18873 | 2025-10-11 05:04:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9085e195-9859-332b-94f8-f3139dadf006 | -15.70501 | -46.64124 | 2025-10-11 05:04:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abb9ab07-160f-30f5-b47b-9184f88189e1 | -17.25798 | -46.89838 | 2025-10-11 05:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f855663f-fc0f-3d44-8b9f-f7d44c0cee59 | -15.19682 | -56.79629 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e27e4d7-72a3-3807-81c3-4bd53af302bb | -18.05523 | -57.56223 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 56f53486-c40c-3f1c-9221-6aa5c8df231d | -17.26349 | -46.89918 | 2025-10-11 05:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c731ff86-8f2d-3f78-8c29-2925d89447ac | -16.31109 | -47.15329 | 2025-10-11 05:04:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e678254-0326-3c91-b1ad-ce18f19e0c9e | -14.94589 | -46.75342 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37fc031c-20fc-3fb9-86f0-cfe8392b57d3 | -15.98068 | -48.18371 | 2025-10-11 05:04:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43d66d9d-7cf2-3889-a1c9-d558379c75f3 | -17.95892 | -57.61744 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2037707a-7083-3467-88c0-867559697f34 | -18.03306 | -57.55061 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 64bee4b8-3992-35f9-ade8-63b9fdffeabb | -15.16926 | -56.83976 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 786fedfb-ad8d-36d6-b830-0ffddef45e50 | -15.0116 | -56.06687 | 2025-10-11 05:04:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e29c8f5-0e34-3650-b8e8-efb5464e2042 | -15.42128 | -48.0282 | 2025-10-11 05:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a9c5ac6-9dfb-357c-96b8-5d28fcfd5b92 | -18.05189 | -57.56164 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e4b4659c-2f6e-303a-bbdc-683b3acde1c4 | -13.08387 | -54.84148 | 2025-10-11 05:04:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 681b23b9-a36b-3299-a83f-42f59e45f737 | -17.81845 | -57.64497 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 29458ee3-ca5b-33fa-ba53-e4d0ff4f7d18 | -15.32258 | -46.19103 | 2025-10-11 05:04:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b0ba6165-fe8e-30da-b9d1-14e6562adf21 | -17.83671 | -57.65973 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4c2a82b3-be7f-3a60-88aa-91560f04f91c | -14.95593 | -46.76169 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ea53717-992e-3afb-b48f-63c68ca53d04 | -17.84518 | -57.58593 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0f81cf8a-fdba-3a5a-9b1a-1dd268417713 | -15.70545 | -46.63713 | 2025-10-11 05:04:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43a4fa06-f667-3753-bf08-6fa2baa5a5e2 | -17.82944 | -57.6622 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cf616758-9f20-38d0-a460-aca918e87f61 | -15.70045 | -48.398 | 2025-10-11 05:04:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e4a40a91-7393-3f6a-b2aa-40235357185c | -18.04737 | -57.56843 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 89a71e73-eb56-3a62-8898-b07c41502575 | -17.81548 | -57.66337 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d1e4be45-2251-3a60-b7cf-56bd7250eeb8 | -18.07016 | -45.0195 | 2025-10-11 05:04:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6637411-a320-3dbb-8fa6-3b2032243f68 | -17.26266 | -46.8982 | 2025-10-11 05:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| abd04fc7-e075-3a61-b2ef-d14fe5ddefda | -14.94022 | -46.75498 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 969d49e5-3db9-3089-b119-8d92f740cfb5 | -18.03974 | -57.55178 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5bb5f7d1-f484-3d98-9ca8-e3a40b56d35b | -17.89478 | -57.67395 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 996d0408-e83c-32f8-96ba-f27495cf1f31 | -18.04856 | -57.56102 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c25332df-4c04-347e-9de4-208419ac07f5 | -15.31975 | -46.19328 | 2025-10-11 05:04:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8f2dab03-f3f5-3fab-9b90-04d401061451 | -15.06362 | -46.60088 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da2ffec0-ee39-394c-85b1-c7051754381e | -15.18198 | -56.74606 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79ef270c-634b-36f1-9777-7b2aa4e19a14 | -17.82079 | -57.63056 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7f9af7c0-2c71-3219-8749-e4115d68f3a1 | -14.73996 | -46.11571 | 2025-10-11 05:04:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6ff349d-0a6b-3b90-81ab-24c5c0d4bfb9 | -16.30693 | -47.14169 | 2025-10-11 05:04:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 462e07cd-81f5-3a09-8bac-ff6e9b627d4b | -15.16485 | -56.72471 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8e8ea47-2c73-3b62-bf69-14d18e561879 | -15.18738 | -56.79107 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9d6c3e7e-f0bf-324d-9f23-47c14744d62e | -15.27978 | -56.90976 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c09ab1a3-3983-3007-944b-809e9a703d66 | -17.82276 | -57.66092 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 97a65ec5-23e4-3da7-b8f1-dc8093cbd35b | -17.21326 | -47.65807 | 2025-10-11 05:04:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e559c58f-0933-36a3-8687-87c6e341b285 | -14.9414 | -46.7444 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5db26f19-8f74-3eb8-b2d0-dc35ce218ab4 | -15.60384 | -42.67577 | 2025-10-11 05:04:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 59471722-827c-3db9-84ae-db14e233e82f | -17.49225 | -43.33257 | 2025-10-11 05:04:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5125488-fe06-3098-b282-99b370150a66 | -18.05857 | -57.56287 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c57d3c0a-bcc4-3ec6-8dbf-3386b61ae2cb | -15.16427 | -56.83549 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9547c0a7-3cd2-3eaa-8e1b-aa4a36f119ab | -12.0949 | -63.86129 | 2025-10-11 05:04:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 541a4609-75e0-3b17-a318-41487cc1cfac | -15.20308 | -56.86395 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf3a0f78-c201-3f52-99f4-c8dba8a3bcb0 | -17.84301 | -57.57804 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9fe322b3-2c55-3ba7-81cf-e48c9143ece7 | -18.04582 | -57.55664 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9c452399-031e-3a74-990d-0c72d701d9eb | -15.1683 | -56.81027 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d441e11-d454-368a-aa17-a6dd2259bbce | -14.74514 | -46.12037 | 2025-10-11 05:04:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| effda81f-12c5-396e-a2cc-62e38dd22d82 | -17.83003 | -57.6585 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0e771a9b-aebf-3adb-8023-4784d0ad74ad | -14.9894 | -45.56044 | 2025-10-11 05:04:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b584908-eb27-3078-87ce-8358769c19dd | -18.81258 | -54.96861 | 2025-10-11 05:04:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ef44468b-592a-3beb-8eb5-00ad81588d41 | -14.99393 | -45.58011 | 2025-10-11 05:04:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89abdfcc-5bef-3d4f-9755-9803976474e6 | -19.50494 | -57.47042 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.3 |
| d9c03830-c697-3ed2-9c25-3bc6fa2c966d | -15.15817 | -56.83076 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 234abafb-d7a1-3208-b2a1-67f4a637e7cb | -15.7407 | -48.97628 | 2025-10-11 05:04:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 713fc63c-1d70-3fc6-8187-0c1edf974c38 | -21.28039 | -57.67994 | 2025-10-11 05:06:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.1 |
| ee64a002-a250-39de-9772-3889f10028ab | -22.54162 | -52.05244 | 2025-10-11 05:06:00 | NPP-375D | JARDIM OLINDA | PARANÁ | Brasil | 4112603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 883c0599-455f-3231-9de9-c727b3dadcda | -21.28431 | -57.67682 | 2025-10-11 05:06:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.1 |
| d9786ada-edd6-3c37-9604-247860d8c044 | -22.54584 | -52.05312 | 2025-10-11 05:06:00 | NPP-375D | JARDIM OLINDA | PARANÁ | Brasil | 4112603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 0e5fad7e-b736-3ec2-b9a2-89eb1b878224 | -22.54634 | -52.04894 | 2025-10-11 05:06:00 | NPP-375D | JARDIM OLINDA | PARANÁ | Brasil | 4112603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| d6cf1a3a-5fbb-3ade-98a6-9b2c6cec7882 | -23.89366 | -52.35445 | 2025-10-11 05:06:00 | NPP-375D | PEABIRU | PARANÁ | Brasil | 4118808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2e15566b-ee8d-330c-9545-a5412a0ee36c | -5.86693 | -42.83945 | 2025-10-11 05:08:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 126.8 |
| 5434973a-d28e-3a63-9e47-1c0049dfabb9 | -7.21087 | -39.89497 | 2025-10-11 05:08:00 | AQUA_M-M | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 17.6 |
| eb8894de-1044-3f7a-8492-ba51a0bfdf88 | -8.18985 | -43.30635 | 2025-10-11 05:08:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.8 |
| 92278cc2-4a5a-32c1-bb30-bb80a8ad9e4c | -7.8544 | -44.48911 | 2025-10-11 05:08:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 34.2 |
| fecc6bcc-cc2e-3977-b088-564bd59d5d8c | -8.20519 | -43.30883 | 2025-10-11 05:08:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 29.9 |
| 50db13a4-9926-30ca-89d9-038f6f143367 | -5.85153 | -42.83671 | 2025-10-11 05:08:00 | AQUA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 223.6 |
| 0889effa-6178-3c12-8922-58f2f081fbeb | -8.20292 | -43.31346 | 2025-10-11 05:08:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.1 |
| 38f656db-c4c0-35c6-96fb-296d3e93609e | -8.19752 | -43.34385 | 2025-10-11 05:08:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 44b2ff6d-cb93-340f-9a52-2861d11da908 | -5.84624 | -42.86825 | 2025-10-11 05:08:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 28.3 |
| 343abb7c-1449-3175-82dc-36bf37de921f | -8.19997 | -43.33953 | 2025-10-11 05:08:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 37.0 |
| 63f39750-ec67-36ee-ad36-4edef64cd5fa | -7.21539 | -39.90596 | 2025-10-11 05:08:00 | AQUA_M-M | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 87edb11e-36f4-34e0-9831-d869ca940920 | -8.1876 | -43.31089 | 2025-10-11 05:08:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.3 |
| 3e22d7e5-6811-3ecd-97a5-5a8f1e1a098d | -27.72536 | -51.22158 | 2025-10-11 05:08:00 | NPP-375D | ANITA GARIBALDI | SANTA CATARINA | Brasil | 4201000 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1d1dabe4-a8fe-3de4-bb8c-018c730b690f | -28.27548 | -49.34058 | 2025-10-11 05:08:00 | NPP-375D | ORLEANS | SANTA CATARINA | Brasil | 4211702 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 61cbb312-0ceb-320e-bb6e-fea65ba49f5c | -28.27515 | -49.34446 | 2025-10-11 05:08:00 | NPP-375D | ORLEANS | SANTA CATARINA | Brasil | 4211702 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 33ba8524-d0ae-3bfb-befb-22da77eda807 | -13.20042 | -42.34364 | 2025-10-11 05:12:00 | AQUA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 38.8 |
| 961b9688-068a-31aa-b802-dbbf6b06ac64 | -13.21693 | -42.32544 | 2025-10-11 05:12:00 | AQUA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 133.5 |
| 4a571b48-df2a-3705-8444-da06e58b8040 | -13.21329 | -42.34594 | 2025-10-11 05:12:00 | AQUA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 118.7 |
| 9d3eddcc-fc2a-3dfe-8962-3070ca64b22d | -13.20407 | -42.32322 | 2025-10-11 05:12:00 | AQUA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 22.7 |
| eccdc8ec-4aac-32ca-aa61-36d133180f9e | 1.21532 | -50.86716 | 2025-10-11 05:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc9aa624-6f68-3fc8-847f-a07ee5df8cac | 1.19988 | -50.86418 | 2025-10-11 05:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c18d59fd-b92a-3667-9c5e-24e0bd5ca227 | -2.63545 | -59.6018 | 2025-10-11 05:21:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 499a4e99-a7b1-346b-91f2-50c760b4c73e | -3.41119 | -52.66334 | 2025-10-11 05:21:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 979da2a4-c6d4-30b5-b18e-79466cc96275 | 1.20474 | -50.86339 | 2025-10-11 05:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db9f2095-f666-32ad-84f2-f9bb319bf939 | -4.42624 | -47.59946 | 2025-10-11 05:21:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 773a9c1d-8b8a-3e18-ac52-176781b8dab6 | 1.21045 | -50.86796 | 2025-10-11 05:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 471b2e25-037a-3e22-b4e9-f70a7990f300 | 1.18786 | -50.8827 | 2025-10-11 05:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e0708eb-87ba-39eb-b4df-e7611dec245c | -4.42545 | -47.60503 | 2025-10-11 05:21:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e787a66-43ad-3882-8214-36fd50b9e4f6 | -4.42703 | -47.59984 | 2025-10-11 05:21:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 324ff6d7-69e5-3ff4-97e6-172b6ed8fee6 | 1.20244 | -50.88032 | 2025-10-11 05:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc7f5b19-fd85-3a20-ac32-2ed06c0873c0 | 1.2096 | -50.86258 | 2025-10-11 05:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec2e9298-0228-361c-83f3-1ea01f6cb65c | 1.19273 | -50.88195 | 2025-10-11 05:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README42.md)
