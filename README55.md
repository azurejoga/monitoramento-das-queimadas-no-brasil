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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ec114d9-0a34-3c5b-9c9b-f35a8c615429 | -13.45913 | -46.28154 | 2026-09-24 04:46:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f82d563-1024-3978-ab12-a19503b7c894 | -10.90945 | -53.94363 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 563f2264-8d04-3815-96da-bb9a8b183b61 | -6.6416 | -59.9314 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f6204c93-1650-3491-bc3b-1ea6dbf18fe5 | -12.15144 | -47.36065 | 2026-09-24 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69f1076d-a96a-3888-bc81-c940a51ab212 | -6.44176 | -59.96558 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 781f9e5c-8e3c-3281-8aec-10acc1b5278a | -10.56089 | -46.70789 | 2026-09-24 04:46:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a74de089-7ee8-3a6a-bb7c-d86943f66426 | -12.13658 | -50.74323 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a19d05d-3829-3a72-82f5-d089fceedb55 | -8.72687 | -47.60775 | 2026-09-24 04:46:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b14cf9c-c505-3291-960c-392bbb473dfe | -11.91807 | -50.73343 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8cfe813c-5087-361d-a90a-3dbac4ddd42d | -11.92489 | -50.73458 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43c70fc1-0bd7-3026-978e-b1194ad0e9a5 | -13.93468 | -47.82378 | 2026-09-24 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 936d2042-cfdb-3c73-b2d8-322a1469410f | -11.92829 | -50.73516 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76937626-463e-35f0-938a-0cd5c539e415 | -10.70152 | -48.72303 | 2026-09-24 04:46:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1baaca38-7566-31ab-838f-a3e4d2ca31e5 | -12.14278 | -50.74809 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2baaca32-21b6-33a8-92c0-ce11a99c38b0 | -10.08005 | -46.02785 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f211cda-2e64-3cc9-9eab-3a3267efeafa | -8.78459 | -45.84148 | 2026-09-24 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d94dc01c-3679-310c-9be3-ae2514a44d0c | -6.67417 | -58.57804 | 2026-09-24 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| abad559a-c6d4-32bb-bf73-438461ba495c | -9.46942 | -40.33851 | 2026-09-24 04:46:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 36.4 |
| 83562cd7-1868-3983-8d38-f3e490a311f2 | -10.27372 | -49.95472 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 811eb6f3-c887-394c-a239-83279ed55ed7 | -9.47553 | -40.32812 | 2026-09-24 04:46:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 0baad78e-1fb8-3e58-a285-58f33f2db3e9 | -10.07552 | -46.01606 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| f9e0a793-464a-3a9d-85b9-8316ab604f8d | -12.15219 | -50.7528 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b30a7a8-e596-369b-a1f7-e596077c2a12 | -9.18015 | -46.5061 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c69fe02d-bf58-3403-b7fa-89c6707d689f | -10.42129 | -49.3707 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89c54a88-5b75-3010-a805-15230ab54528 | -7.39738 | -55.2171 | 2026-09-24 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88b479f7-fd82-3e14-9689-00533c80f41b | -13.17957 | -51.53799 | 2026-09-24 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 51265ce4-ceb3-3d4a-ba61-d38822ad2f60 | -10.4151 | -49.35493 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 152975b6-3c94-36f6-a5b9-51307ef6aec7 | -9.54184 | -45.3647 | 2026-09-24 04:46:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eceeef4a-8ea5-3658-8ad4-a4735a6e9045 | -10.84535 | -43.24697 | 2026-09-24 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9b0b0a9a-010f-3f1c-aac3-992c00836660 | -9.14721 | -49.96547 | 2026-09-24 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2304b478-19f6-3957-a321-92e7f0713a3d | -11.26374 | -45.37965 | 2026-09-24 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b22096c2-e207-38e1-89b7-8a416ef498a3 | -14.37415 | -47.24073 | 2026-09-24 04:46:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8afacf68-5fd2-32f0-8186-c441bd0d2997 | -11.29138 | -51.31789 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bcbd622f-c4c0-3718-ba26-0ebf22252878 | -6.07262 | -57.79884 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d591624-141a-3360-a57b-dcdfcb0f7f70 | -7.43268 | -49.82907 | 2026-09-24 04:46:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 23a10874-f581-3705-94a2-cbbc824cdbfe | -11.64947 | -50.62424 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7f59e43-5901-3f35-a6c7-753811fcdf01 | -9.23899 | -47.37128 | 2026-09-24 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0d1ba4f5-5f6a-3356-9000-a59bc69fe05e | -11.71677 | -50.76466 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20dd8d2e-f02c-3e5d-ab3f-37d7e55c6b0c | -8.82302 | -45.94242 | 2026-09-24 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8509e27f-fb57-306f-a265-037eaf8363d7 | -6.65378 | -55.05603 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e209c674-25a1-3aef-95d9-fb2209bf4473 | -14.62324 | -50.59908 | 2026-09-24 04:46:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f518b8ec-1a14-3c1d-bc0c-4ae6666b21e0 | -12.92541 | -50.91955 | 2026-09-24 04:46:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9df700ba-86bf-3467-a9a0-c296d3489014 | -6.23707 | -60.02579 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 908a7a77-8dcb-328d-b60d-6481c271c6d5 | -10.07615 | -46.01196 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| e4262226-1478-3a94-9cd1-952a8f3a4901 | -10.71761 | -48.72923 | 2026-09-24 04:46:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61d12453-99d4-329b-8e8f-f8073b1a435b | -13.79265 | -54.06215 | 2026-09-24 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 560c3d2f-526d-30c7-a2c9-a3667816b0cc | -5.91704 | -59.92066 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58667f30-b5a0-32f6-b978-a40d52f7a1b4 | -6.01182 | -59.94615 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 21f8e0ee-4bf3-3dea-a38a-c73c494012eb | -11.91868 | -50.72971 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e63850b4-6b2c-3461-903e-84e52fb7d6ce | -11.86587 | -49.96189 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc2f3bad-3518-328d-886d-828849de4c65 | -13.08205 | -47.40852 | 2026-09-24 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f833ec4-fd2e-3dc2-b3dc-257a260812da | -12.3346 | -50.14643 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be4387ef-9a03-336a-8c25-ef4141cc8827 | -11.43051 | -44.19088 | 2026-09-24 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3b71edc7-581c-309f-afef-d2f8095a3dfe | -6.89638 | -55.57976 | 2026-09-24 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 403ec6d5-5819-303a-94a1-8a74e6b74fa3 | -12.12061 | -47.38262 | 2026-09-24 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05b94aed-1c9d-334a-931e-ce6c8a5780bf | -8.12463 | -54.82185 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3345afff-0d21-3a3a-870a-17d65771fcca | -8.89882 | -46.81778 | 2026-09-24 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b140812d-3e9c-33b2-af8b-320942457c55 | -10.24481 | -49.98333 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6307ef47-4f8c-3fb6-8291-ecd1bf3dd5f1 | -10.43325 | -46.2662 | 2026-09-24 04:46:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bd34974-9ba9-38d7-9267-e1aa9712dd32 | -12.14059 | -47.36278 | 2026-09-24 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35091a8d-e2eb-357a-8840-eceec56de048 | -10.44509 | -45.10794 | 2026-09-24 04:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a13cb1c-c7cb-38a3-835f-05850e64773f | -11.92928 | -50.75061 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c62998de-0cab-369d-9614-30f4bc4a238b | -12.12576 | -50.74519 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e407603f-da36-3c06-9785-e94f7f227a32 | -8.72073 | -47.60316 | 2026-09-24 04:46:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98ba4f00-c048-33be-8a93-5b3e6e608595 | -8.93474 | -45.94283 | 2026-09-24 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 259b16d9-cec0-3530-9411-b045fb4e7247 | -9.84671 | -48.50275 | 2026-09-24 04:46:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50c16c53-59b0-3f73-8618-4f59074b850e | -12.14879 | -50.75223 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4c7d57eb-c1f2-37ac-99e3-345742be8b81 | -6.01252 | -59.94637 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 87340af9-3caf-369a-a998-630cd5c91dd1 | -10.41139 | -54.41415 | 2026-09-24 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5821007-527c-33d7-b481-d969539ce2f3 | -6.6268 | -59.93957 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b2162aae-f226-3710-bbca-27a3a1b89535 | -12.42086 | -46.9543 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f4ee80f9-dab9-33e6-bf3a-a86f99cbf3fa | -11.69656 | -44.49243 | 2026-09-24 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b9dcf97-0d91-3d3c-885e-cf374908e854 | -8.38959 | -46.29971 | 2026-09-24 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a8263ec5-26ff-3903-9ad3-c4264ed00fbf | -12.41141 | -46.96167 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 32276100-dabb-3a43-b2dd-4369db4f6cd0 | -7.90331 | -61.17299 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cd148d7a-4978-3de4-8648-80bba5262301 | -11.62464 | -50.60459 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8819b200-ba01-3c9d-87be-67782770320d | -11.23205 | -51.37223 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| caceeeed-6ab0-3342-97a1-371881e3b4b2 | -11.22658 | -51.38343 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f0e55d6-551c-3c6e-b10f-f9b9ae8fed81 | -12.67878 | -46.37804 | 2026-09-24 04:46:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5220af59-8e78-36d7-ac86-b1b9a57ac857 | -11.20189 | -54.12636 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd4dac86-e78a-3815-921c-864ccfb932f5 | -10.27196 | -49.96555 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06345bc2-276c-34f5-b680-1cd25837708b | -7.41975 | -49.86502 | 2026-09-24 04:46:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75e94ebd-dc24-3080-9059-40127535d111 | -11.92148 | -50.734 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 32fee38d-83b1-3fc1-83a6-dfeb8e6124b4 | -9.84061 | -48.49818 | 2026-09-24 04:46:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e21f017-a66c-3fdc-a430-489e8b8eaff8 | -12.13537 | -50.75064 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9c567c9d-0b0f-3d2c-841f-ec50d0875c49 | -12.00464 | -52.46307 | 2026-09-24 04:46:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 1076e19e-3e6c-3059-98c7-1c5f549fe039 | -10.43266 | -46.27013 | 2026-09-24 04:46:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2c38bed-7dc0-3ed6-b89f-a4facae82678 | -11.94324 | -38.29617 | 2026-09-24 04:46:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f4e687c7-78a5-33ee-873b-b2b47ad7805d | -11.12188 | -48.33175 | 2026-09-24 04:46:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a03c34f7-0c7e-3654-8090-989861457f74 | -11.2257 | -51.3671 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 740eb9c2-9f86-3ea9-9766-64484782490a | -12.4197 | -46.96209 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0d03283c-85d7-3086-9e38-d731c4409b6a | -13.46164 | -46.26448 | 2026-09-24 04:46:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f68e32d1-b08f-3899-9f98-b28ca55ad718 | -9.02185 | -49.81104 | 2026-09-24 04:46:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36bbdce7-6dae-3763-974e-6b7cd1ccbf39 | -7.90311 | -61.16784 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8496ea0d-3dd2-361f-b743-15c25999b8c8 | -11.42751 | -47.40026 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 732e582f-8198-3371-8f41-19e85a032fcb | -6.10091 | -57.67469 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8cd33f15-87fb-3022-b8bf-1c20c49083f3 | -6.60775 | -59.93281 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d667b1bd-f70c-38b1-a49a-eaad514bce54 | -8.38614 | -46.29916 | 2026-09-24 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 26b3195f-6bdd-3bb2-8716-adb0bcc3b8c4 | -10.61692 | -53.99527 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33d6f4c8-5bd8-32a7-9c10-8ca7c51c4f99 | -12.12637 | -50.74149 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |


[Clique aqui para ver as próximas entradas](README56.md)
