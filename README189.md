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

## Dados Diários - Página 189

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b253cb10-e325-3575-91c9-caf28465bb46 | -3.6076 | -59.0769 | 2026-08-31 18:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 131.6 |
| bbc9b303-53d5-3706-87d6-b1d37d23e7f9 | -10.5906 | -57.4936 | 2026-08-31 18:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 43aed5dd-9907-35f7-ac0e-26ba82e3919b | -3.1449 | -61.1808 | 2026-08-31 18:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| a9afdbf0-46dc-3611-8814-4a5a11232add | -7.3302 | -60.589 | 2026-08-31 18:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.1 |
| bc077940-0c61-3fa4-82ef-8b4f391e8d29 | -1.0993 | -48.0561 | 2026-08-31 18:50:00 | GOES-19 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 526fe688-0634-381a-9076-16a24ed826ac | -7.6152 | -44.8605 | 2026-08-31 18:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| f27a1ea7-3857-3f75-b327-f12df529d45a | -4.1516 | -60.6878 | 2026-08-31 18:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 46ecdeb6-a031-3621-883e-238517ef9de0 | -8.3601 | -70.8458 | 2026-08-31 18:50:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 2bbc5299-7ab6-3572-b4c9-3ddca2164513 | -9.1532 | -59.5221 | 2026-08-31 18:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 49dc3240-ebde-3368-9cfb-8686fa584377 | -7.6253 | -55.2787 | 2026-08-31 18:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 128.7 |
| c2c7d61d-e9b9-3781-93d4-3a3011940c32 | 0.1914 | -60.5067 | 2026-08-31 18:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 63.4 |
| b0d692d2-3618-31b1-882a-f279c544b5eb | -11.2103 | -45.1017 | 2026-08-31 18:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 212.0 |
| b0399b76-5554-3da0-819f-b0944ad588d1 | -14.6535 | -53.5642 | 2026-08-31 18:50:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 53.1 |
| c9ce5646-c1fc-3edd-a4ce-dbeb3ef03bef | -9.6939 | -65.1145 | 2026-08-31 18:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 100.9 |
| e5562de4-4f59-353c-8eff-660b05ddc541 | -9.8434 | -64.9777 | 2026-08-31 18:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 8c753397-440e-329e-85e3-2107c7bf1c13 | -3.6216 | -60.547 | 2026-08-31 18:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 136.1 |
| c0a76867-d262-3d18-88b9-7e58c7cccd18 | -11.2478 | -45.1425 | 2026-08-31 18:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 750ae4f2-8184-3e0f-bb46-c2203a28e278 | -8.9428 | -63.2797 | 2026-08-31 18:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| dba27c88-1cf6-3880-b001-605e2dc24e87 | -12.0925 | -44.996 | 2026-08-31 18:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 239.7 |
| 5169d621-4e78-3ffa-abc0-a0d39081316f | -7.6251 | -55.2987 | 2026-08-31 18:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 314.4 |
| b64a55a0-d8a2-3e31-acdb-68411f929bd3 | -8.2605 | -62.758 | 2026-08-31 18:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 75bf65fb-6053-3dfb-8ef6-e68e6526b549 | -9.1273 | -60.5275 | 2026-08-31 18:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 85e44397-81c1-3f33-947b-6192e38c3ef8 | -6.4085 | -45.4198 | 2026-08-31 18:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| cb39fa42-d6bf-3201-8b34-16ee73be838c | -7.6066 | -55.2998 | 2026-08-31 18:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 3f05e6e7-f8be-3f9e-9c9f-c9c25540d8a5 | -15.6336 | -56.3876 | 2026-08-31 18:50:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 1169b748-f50e-30d9-9c74-937001db0651 | -13.471 | -57.0373 | 2026-08-31 18:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 05db891e-3bd6-3373-ac13-33aaac2a74b6 | -8.5969 | -54.7755 | 2026-08-31 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| a32c949f-f0b8-362a-b924-af8168b0a5d9 | -7.6149 | -44.8833 | 2026-08-31 18:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 185.9 |
| 7114f76f-967c-3e9a-bf4b-7dc84f63f9b5 | -9.0058 | -65.4373 | 2026-08-31 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.2 |
| f479e193-3cc1-3894-ab89-dd2c05f47c63 | -11.2482 | -45.1194 | 2026-08-31 18:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| d8fa21e8-3d37-3275-a1cf-e4611cf413fb | -3.4185 | -61.3461 | 2026-08-31 18:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 22e1438f-3cee-3d8c-96fd-216175a9767b | -9.1709 | -59.6374 | 2026-08-31 18:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 806f0525-deb4-3ae6-aec4-69e11ad6076b | -7.3453 | -72.9539 | 2026-08-31 18:50:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| ffeb8a49-05e6-3277-9c1f-eb4e2b45d9ec | -8.8705 | -66.7822 | 2026-08-31 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 318.2 |
| 984566d2-bb25-33dc-8ec5-f29859b9fcf4 | -7.3119 | -60.5706 | 2026-08-31 18:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| e370f6eb-03d6-3f81-bc97-61874b9ae716 | -5.2548 | -55.8907 | 2026-08-31 18:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 951787e9-4236-343c-8fbd-b287867bd273 | -9.6683 | -50.8511 | 2026-08-31 18:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 8f98459e-cdf8-3b3b-bdd5-5fe732ecdd71 | -9.1711 | -59.618 | 2026-08-31 18:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| b6edfa32-470a-31e3-b20b-366444170cfd | -9.1906 | -51.546 | 2026-08-31 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 6c2e0623-785b-3db4-aa5e-4b737852c4e9 | -10.0542 | -48.6888 | 2026-08-31 18:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 9662b7b4-865a-3665-a78a-c6c9aa793541 | -13.4519 | -57.039 | 2026-08-31 18:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| e9b12ee4-bdf6-35cc-a1eb-8c28443e5c17 | -3.9707 | -60.0258 | 2026-08-31 18:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| e37042e3-a652-38d7-a4d6-7dfba7ecef49 | -9.1904 | -51.567 | 2026-08-31 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 1ab8715e-9d17-336a-b5d5-f3e3e2773504 | -9.2089 | -51.5863 | 2026-08-31 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 5d87e28f-a05c-3f8c-b36c-b6e6dd3f0cd9 | -7.2255 | -42.7616 | 2026-08-31 18:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 9491cd52-d031-3371-9a65-ed1f96fc1445 | -10.7271 | -50.6405 | 2026-08-31 18:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 3a98dc37-fd3f-3b9e-bed7-4f65ec91cc6e | -7.77 | -61.2015 | 2026-08-31 18:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| a2f82616-e963-3a0c-af91-0f7649318589 | -8.9873 | -65.4379 | 2026-08-31 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| f7105c9b-457a-34b7-b58d-d7da49b959f1 | -15.6139 | -56.4103 | 2026-08-31 18:50:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| f1f7a1b2-f755-33ee-88ba-c8605b651897 | -8.3785 | -70.8639 | 2026-08-31 18:50:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 5ceb043e-d5b1-3c09-807e-f1d08071f6a9 | -9.6075 | -61.0222 | 2026-08-31 18:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 89fdaeb5-c3e1-3a04-a611-49ac4a31bf04 | -8.8026 | -71.0783 | 2026-08-31 18:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 8905a481-21ba-3dc0-b987-af086795e574 | -10.1084 | -50.299 | 2026-08-31 18:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 5eb16a26-4cb5-3b40-821d-b5821c221e03 | -6.6542 | -59.426 | 2026-08-31 18:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 0df0fc1c-e71d-3c76-a9a3-af615165d4a1 | -3.1266 | -61.2 | 2026-08-31 18:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 3c0c3271-9d7a-3674-b4d8-6ff2579cdeb7 | -7.7941 | -44.0609 | 2026-08-31 18:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 8dc1f65a-1ea8-3159-920c-498b7e69f33c | -13.4899 | -57.0556 | 2026-08-31 18:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 5eb7c77c-30fe-33ec-be6c-d46ab71e988c | -11.2314 | -54.0164 | 2026-08-31 18:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 3c71c5b4-3daa-3be1-8660-3d83e965507b | -6.3032 | -53.5782 | 2026-08-31 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 56f3c2a5-6a8a-3b93-bfb3-0c4f2843458b | -9.1529 | -59.5609 | 2026-08-31 18:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| c8473bdb-ebef-3834-8c60-1d17fab2c7a4 | -11.2317 | -53.9958 | 2026-08-31 18:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 53f3adb1-5315-304a-b17e-5a07077b39db | -6.7514 | -55.6654 | 2026-08-31 18:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| c631eba1-24e8-3c11-af87-7ee46ab2e314 | -14.1459 | -52.7871 | 2026-08-31 18:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| f38d6af3-2c7f-3476-8893-9eea4daf9c2b | -15.6333 | -56.4081 | 2026-08-31 18:50:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| d1d9344a-633c-3107-b48c-8c87cc6ab6b1 | -14.5868 | -54.1153 | 2026-08-31 18:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| f0c76b18-85f3-3d33-816c-dfbbde4fb1ab | -8.8706 | -66.7636 | 2026-08-31 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 223.4 |
| 79ded6b4-a845-3157-a9ad-f21140f1ade2 | -6.1109 | -57.684 | 2026-08-31 18:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 68051430-d580-388b-b02b-5b6902b17137 | -4.1515 | -60.7257 | 2026-08-31 18:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| eeefe20d-142d-3123-ba46-75f9aa9b9559 | -10.7405 | -54.0606 | 2026-08-31 18:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| b4b14b7f-0615-300e-876e-dfabe8a06907 | -3.9708 | -60.0067 | 2026-08-31 18:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| deaf0423-6866-3e86-a2f1-eb1df74b1ddb | -9.6049 | -68.5979 | 2026-08-31 18:50:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 32e3dc8b-4f9d-3d7b-a9a5-63c8da0128b7 | -13.4707 | -57.0574 | 2026-08-31 18:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 37acb496-9a58-3550-966b-b1da6dae94a8 | -9.02 | -57.5377 | 2026-08-31 18:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 69ecc2b5-fc82-3934-9895-4bb7a40c4b01 | -14.1263 | -52.8106 | 2026-08-31 18:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 0b6534c4-ab50-3649-a2fe-ce80e8887d1c | -9.1718 | -59.5211 | 2026-08-31 18:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 4bd351d1-f35d-38e5-85c0-eb68ed69dd51 | -14.2369 | -51.9498 | 2026-08-31 18:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 052127c2-7d85-3e64-b73d-be254f721f40 | -7.4735 | -61.3846 | 2026-08-31 18:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| fe6a8730-60d8-324b-b92c-c73d622d595d | -9.173 | -59.3659 | 2026-08-31 18:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 0caa20b8-790a-3854-b53e-5167194f0132 | -8.6674 | -62.8179 | 2026-08-31 18:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 418e2c26-c1b7-3d15-b10f-6262108c7089 | -9.2098 | -59.4221 | 2026-08-31 18:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 47421618-54bc-3f91-81e3-86cfa9f16a40 | -8.7968 | -62.8695 | 2026-08-31 18:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 43.6 |
| e9b30cb8-8452-3205-88a8-120db1152ed6 | -10.5451 | -46.1933 | 2026-08-31 18:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 199.9 |
| de891a35-f680-308c-8e22-6603dcc1843c | -8.0481 | -70.209 | 2026-08-31 18:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 865206ce-100a-3519-9ea9-57922a5dfea4 | -9.9896 | -53.9404 | 2026-08-31 18:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 3dbf20cd-6f45-3d0e-976f-1054055bd3d3 | -4.1698 | -60.7064 | 2026-08-31 18:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| a6f6db62-491f-36b9-881b-2e8d0750e53b | -6.7887 | -55.6237 | 2026-08-31 18:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 68074cf5-8edb-304e-8330-afd0dcae1fd9 | -10.4793 | -64.5201 | 2026-08-31 18:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 4bb32863-c481-348b-9fce-562c3d09fb79 | -11.1807 | -55.1024 | 2026-08-31 18:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| a0a55c02-417c-3b3f-980f-f810854547cc | -6.6541 | -59.4452 | 2026-08-31 18:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| f1f32122-3c63-3e30-8711-a37e8d733432 | -9.694 | -65.0958 | 2026-08-31 18:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| c7f5f723-db05-3ba3-94a3-0cdfb9206049 | -3.1997 | -61.1799 | 2026-08-31 18:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 255933ba-3338-370e-ba06-6b8305caeb45 | -8.7628 | -46.4642 | 2026-08-31 18:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 9c22d246-612c-3e0b-8a3d-9d81a3b4fec5 | -14.2599 | -52.8782 | 2026-08-31 18:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 101.1 |
| a99b7214-4ae8-3f2c-ba39-2772e6c015c7 | -4.9788 | -55.8417 | 2026-08-31 18:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 6e1e4bf2-ec17-3525-9e1c-1a28494f6adb | -7.2933 | -60.5905 | 2026-08-31 18:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 988f38a8-1ed4-3f58-b0f7-874bc7b6197b | -10.4961 | -59.6195 | 2026-08-31 18:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 7987962c-dbc9-3b52-8609-3418fd892fcf | -15.2275 | -56.3716 | 2026-08-31 18:50:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 6b8ed75c-8c30-3f95-a083-21aecf31a5d2 | -10.572 | -57.4752 | 2026-08-31 18:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| bfa3dfe2-8df0-39bf-a6c6-b770b57c0544 | -9.153 | -59.5415 | 2026-08-31 18:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 61251b14-427d-3ebf-8354-4094c979818d | -9.208 | -65.8044 | 2026-08-31 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |


[Clique aqui para ver as próximas entradas](README190.md)
