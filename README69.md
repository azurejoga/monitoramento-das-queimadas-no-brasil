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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a800da0b-d52b-3912-979f-5259ef28a08d | -9.47707 | -62.38292 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbf14b77-b191-3aa1-811a-4b507ceeef53 | -9.69545 | -61.28598 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84277488-7d63-3516-85d1-ea4cfbdf0b82 | -9.15339 | -62.35252 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba14abe4-373b-3a7d-83fd-9223e8cfbb01 | -8.88479 | -62.48071 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c256f48-6a96-383b-9773-c4228c730855 | -13.63299 | -48.23969 | 2025-08-28 05:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3c347a5-d04d-3950-95bd-30bb83f4df19 | -9.49393 | -62.38566 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e174ac19-efb3-3738-81c5-0cf1d379a855 | -7.56233 | -63.84534 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be057c8f-37c7-3ede-8bba-f2ba55321797 | -8.93034 | -65.93269 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a07e4c9-cbc3-31fd-90dc-6483a1e8eef3 | -11.36035 | -63.264 | 2025-08-28 05:25:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5668840d-cdc6-3c5a-9a96-7d580a799c7c | -8.8847 | -60.74817 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c7cb598-7cd5-3477-8007-cb5ee9d042f7 | -8.34764 | -62.9428 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fceb6387-edb6-381f-b760-1ccf55463eaf | -12.99602 | -56.90668 | 2025-08-28 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c66b67ba-57eb-39e1-9133-d26eb3af7e7a | -8.8825 | -60.76214 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 607b0ed8-7f74-3db8-94b6-25151390d2fd | -9.18966 | -60.80742 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed85b295-5a4c-35c3-a9dc-5a6fe7282710 | -12.85859 | -48.11174 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b947966-a9c2-3f85-984c-c5ad5135207a | -6.2373 | -60.00562 | 2025-08-28 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5d9607b-8f89-3b1c-9e89-7dea736b19d3 | -8.51488 | -69.79543 | 2025-08-28 05:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc29ccc2-f05f-3cc5-8be0-f26c8f9a7b5a | -8.88415 | -60.75166 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75f43581-0f5e-3bb4-beb2-69536d3e4def | -9.14943 | -62.35559 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b1f8d48-0ae3-3bc9-8537-40302ba9073d | -9.59655 | -55.38713 | 2025-08-28 05:25:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5686aac8-46ed-358d-b832-a51852e9d935 | -9.11495 | -65.78109 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 9cde349e-9649-38dd-83ac-ab19abcab6b3 | -8.94474 | -65.94914 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07388e0b-e35b-3a7f-89da-8406df29bd4d | -6.24843 | -60.02163 | 2025-08-28 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6a8c553-ea2f-36d0-a4a9-9ce8a4b8b41c | -9.25617 | -65.89789 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 11183b51-1492-3e64-bfba-5fc1e3163b9c | -7.62364 | -60.84791 | 2025-08-28 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 181ed631-4cbf-3d44-82d6-0c5f8823e913 | -9.10521 | -61.42828 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8c487fff-c69b-3c9c-8edb-1a9177ad3984 | -8.70569 | -70.5487 | 2025-08-28 05:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be33add1-3907-3628-8b18-c755c18ef46d | -7.46163 | -61.40194 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc2d8cb5-086b-31bd-bf02-90bbd041a776 | -8.44572 | -70.14481 | 2025-08-28 05:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97a0df6d-bffb-35a3-a2e3-d9e1d0711704 | -10.47773 | -57.9346 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 29ca43eb-5143-39a9-ab20-42824647d1ec | -9.16439 | -59.55725 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66a5ea64-4d44-3ff1-90c6-9566891bc689 | -12.81837 | -48.12318 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ad87b328-7038-3145-9f1b-d68471fd04f5 | -8.24559 | -61.45185 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d80b094d-244b-36f7-8089-65a39471c8d8 | -9.79965 | -64.27008 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4faf625e-e7f6-3fa4-a880-ac5f6155f3bf | -7.35196 | -59.6551 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e254d1c-e0f1-3566-b1a5-3c912dd25238 | -9.66155 | -48.31659 | 2025-08-28 05:25:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 676b7cab-7ba7-3207-ab36-89f1f5627d2e | -7.3529 | -59.6585 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 631eadc0-af48-300d-86dd-3f1f9c51e313 | -9.20061 | -59.54787 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2265938-6905-320a-9e7c-4eded9a82a83 | -7.47221 | -61.40003 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eab7ceac-d822-30bd-ab27-4d99a33316e0 | -7.3447 | -59.6576 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02ccd875-c117-32ab-b04f-4529dd3ab47d | -9.79163 | -64.2516 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66985d56-00d3-3f8e-9b89-dfbbe25183d5 | -12.86517 | -48.11734 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5b5402b1-03bf-3654-9590-b003c1960037 | -7.35008 | -57.63326 | 2025-08-28 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87103bf0-24e7-319d-9f7e-6144dc62e370 | -9.45347 | -51.96404 | 2025-08-28 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b9463a6-3096-344e-9f1f-0a1583d95c70 | -9.31846 | -57.70401 | 2025-08-28 05:25:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 925ac57b-d2d9-3d5f-adbe-3e5ff7081eb6 | -9.21244 | -60.85766 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c06f540c-1d06-318e-80e1-77f0f71bbc83 | -7.54423 | -63.84233 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0155dfd8-ed56-3a87-9d95-977ccbf17ea1 | -9.63778 | -59.63357 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55b5e79e-84df-3763-9cb5-2a561510455c | -10.4739 | -57.96069 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aff301fb-b9d6-31f1-b0f8-a7c407265b1d | -9.40975 | -60.50038 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfce3320-67d9-3d87-b3d7-ef58091b266e | -7.37024 | -64.36898 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c18c11d0-3353-3249-937c-b6adaec8fc65 | -9.27027 | -59.7751 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c04d5f2-a359-37c8-a2fd-afde810d4490 | -9.52773 | -60.52679 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44d572c3-deb8-3757-8bfb-74ab6d5129d5 | -10.25523 | -64.49313 | 2025-08-28 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07ea966c-0669-38e6-a9e0-e321469fbf34 | -13.37823 | -51.75644 | 2025-08-28 05:25:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79988a88-a65a-31d9-af65-1d78cf1c5b92 | -9.7093 | -61.28462 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df6a25cc-4559-3574-b978-da9c8dd697ea | -12.81055 | -48.1294 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8822ddee-6edc-309c-9099-bb7d77a746a6 | -11.22705 | -55.0481 | 2025-08-28 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7339fd81-1801-30cc-99de-ac534e2c5f13 | -8.09329 | -71.24937 | 2025-08-28 05:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0dfe2f9-dff5-301b-a364-3c87d8c60485 | -8.8207 | -63.11218 | 2025-08-28 05:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7fe15275-cf1a-37a6-abdd-af6b6967f351 | -8.93733 | -65.9443 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 183610e6-b0fd-39dd-acfd-895da9575ac9 | -8.07671 | -61.53314 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b1f2342-6a59-3915-a076-b8b414dd3849 | -9.10436 | -65.74791 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7adf82c9-fdf4-3750-bf9c-ab131de1b266 | -10.48011 | -57.94395 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0f185fbe-a893-33c6-8967-9e3ecdb8b6eb | -8.95676 | -65.95123 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c66c918-3ac7-373b-a76c-1afd0457520e | -10.53894 | -57.97249 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ec0925a-0d80-3d5b-a511-73853c244698 | -6.00675 | -57.85322 | 2025-08-28 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79bb8492-5f2e-3d54-8295-4167f47cc56e | -13.72999 | -51.91267 | 2025-08-28 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d83986ab-6424-347c-ba0b-d96573145a53 | -8.95895 | -65.96249 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 762d42ca-6456-3750-a405-7656bb525bdb | -2.44469 | -47.32505 | 2025-08-28 05:25:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13281749-a36b-31c3-9ed9-47dbeef0f5a8 | -10.08632 | -62.89301 | 2025-08-28 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7beb7137-ce94-3d9e-89a0-af838a02c20d | -9.1728 | -59.45721 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7efcd90b-726f-3f63-8f4d-d4395414377c | -8.95737 | -65.94772 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd623cd3-a3ca-3e85-933d-a51a815e51f2 | -9.41591 | -60.52662 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36348f3e-6671-37c1-847a-a5d8111149fb | -8.96116 | -65.97363 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e254879-4e16-32b8-a770-f5dda367e138 | -8.34419 | -62.94223 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb860bf7-1e7c-3045-82ed-2d41ee940f82 | -9.2593 | -65.90364 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1699a657-cca3-3d7a-8df5-d7c2cd6cb750 | -9.08259 | -65.7158 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a8809b5-d061-3a22-a348-5291290a3091 | -10.31859 | -62.62335 | 2025-08-28 05:25:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 68a21364-d97c-3cbe-a45b-ef86ba5f8d09 | -12.55707 | -60.9202 | 2025-08-28 05:25:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9d5f9107-e204-330a-82af-7067e756de0e | -8.8836 | -60.75515 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b28d3efa-2b09-3efb-85f8-1e39b5d1d29a | -9.8079 | -61.19997 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb80cb6e-2f55-3e19-a15a-50f863ae3840 | -8.4554 | -64.06471 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d764c29-7924-3dc8-bf07-eb3b27d5c139 | -6.00263 | -57.85659 | 2025-08-28 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c16f8613-22bd-39d4-a950-eab82f33a659 | -10.46223 | -57.96353 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4ec33c18-3d7c-3c9b-a714-cab7c0822be0 | -6.62814 | -60.02032 | 2025-08-28 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c92b8b74-c437-3287-a112-4307320d9da1 | -7.45055 | -57.62698 | 2025-08-28 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5a15787-890b-3ce7-b773-ad957644a823 | -9.21737 | -59.75925 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27d51ade-71e4-3e54-b7f9-1b6eced6f248 | -8.90682 | -60.71587 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57763a2d-348d-3ce7-a586-0dfa22193bca | -10.81164 | -60.77231 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 25fe8bfe-808a-35b1-9cd6-570692d669db | -9.18085 | -60.86338 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5efa8963-2709-3df4-8298-3bf67b8a7cf7 | -9.39238 | -62.49907 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a26c7897-f611-3d9e-bd68-27a9f7f0df9c | -10.47644 | -57.94336 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 59081a2a-7e7a-3e67-b8e7-e305df302e7c | -7.46219 | -61.39843 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fa89d13-16c3-3dbc-b2dc-fa2841aac3ca | -10.0835 | -62.8888 | 2025-08-28 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29da157b-1ea0-397b-be75-fded8e1af230 | -7.62697 | -60.84844 | 2025-08-28 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e15423b0-b5fb-33c3-a4bc-088b72c2fae8 | -12.80969 | -48.16474 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4057eecd-6ee8-3053-83fe-69a287d8a064 | -9.78734 | -64.25515 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf159747-c104-38c0-a339-4f8dbe1d31ff | -9.40266 | -60.5678 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf3452a7-564f-33d7-b15c-0866f027312a | -8.90505 | -67.45756 | 2025-08-28 05:25:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README70.md)
